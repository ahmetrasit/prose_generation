Surah: 64. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S64 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s064/surah.r2/text.md =====
# Surah 64

- 64:1 يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ لَهُ ٱلْمُلْكُ وَلَهُ ٱلْحَمْدُ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- 64:2 هُوَ ٱلَّذِى خَلَقَكُمْ فَمِنكُمْ كَافِرٌۭ وَمِنكُم مُّؤْمِنٌۭ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
- 64:3 خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ ۖ وَإِلَيْهِ ٱلْمَصِيرُ
- 64:4 يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ ۚ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- 64:5 أَلَمْ يَأْتِكُمْ نَبَؤُا۟ ٱلَّذِينَ كَفَرُوا۟ مِن قَبْلُ فَذَاقُوا۟ وَبَالَ أَمْرِهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- 64:6 ذَٰلِكَ بِأَنَّهُۥ كَانَت تَّأْتِيهِمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَقَالُوٓا۟ أَبَشَرٌۭ يَهْدُونَنَا فَكَفَرُوا۟ وَتَوَلَّوا۟ ۚ وَّٱسْتَغْنَى ٱللَّهُ ۚ وَٱللَّهُ غَنِىٌّ حَمِيدٌۭ
- 64:7 زَعَمَ ٱلَّذِينَ كَفَرُوٓا۟ أَن لَّن يُبْعَثُوا۟ ۚ قُلْ بَلَىٰ وَرَبِّى لَتُبْعَثُنَّ ثُمَّ لَتُنَبَّؤُنَّ بِمَا عَمِلْتُمْ ۚ وَذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- 64:8 فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَٱلنُّورِ ٱلَّذِىٓ أَنزَلْنَا ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌۭ
- 64:9 يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- 64:10 وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ خَٰلِدِينَ فِيهَا ۖ وَبِئْسَ ٱلْمَصِيرُ
- 64:11 مَآ أَصَابَ مِن مُّصِيبَةٍ إِلَّا بِإِذْنِ ٱللَّهِ ۗ وَمَن يُؤْمِنۢ بِٱللَّهِ يَهْدِ قَلْبَهُۥ ۚ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- 64:12 وَأَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ ۚ فَإِن تَوَلَّيْتُمْ فَإِنَّمَا عَلَىٰ رَسُولِنَا ٱلْبَلَٰغُ ٱلْمُبِينُ
- 64:13 ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۚ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ
- 64:14 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ مِنْ أَزْوَٰجِكُمْ وَأَوْلَٰدِكُمْ عَدُوًّۭا لَّكُمْ فَٱحْذَرُوهُمْ ۚ وَإِن تَعْفُوا۟ وَتَصْفَحُوا۟ وَتَغْفِرُوا۟ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ
- 64:15 إِنَّمَآ أَمْوَٰلُكُمْ وَأَوْلَٰدُكُمْ فِتْنَةٌۭ ۚ وَٱللَّهُ عِندَهُۥٓ أَجْرٌ عَظِيمٌۭ
- 64:16 فَٱتَّقُوا۟ ٱللَّهَ مَا ٱسْتَطَعْتُمْ وَٱسْمَعُوا۟ وَأَطِيعُوا۟ وَأَنفِقُوا۟ خَيْرًۭا لِّأَنفُسِكُمْ ۗ وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- 64:17 إِن تُقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًۭا يُضَٰعِفْهُ لَكُمْ وَيَغْفِرْ لَكُمْ ۚ وَٱللَّهُ شَكُورٌ حَلِيمٌ
- 64:18 عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْعَزِيزُ ٱلْحَكِيمُ


===== _commentary/v16/work/s064/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ب ح (root_000666): 64:1 يُسَبِّحُ

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

## ء ل ه (root_000047): 64:1 لِلَّهِ, 64:2 وَٱللَّهُ, 64:4 وَٱللَّهُ, 64:6 ٱللَّهُ, 64:6 وَٱللَّهُ, 64:7 ٱللَّهِ, 64:8 بِٱللَّهِ, 64:8 وَٱللَّهُ, 64:9 بِٱللَّهِ, 64:11 ٱللَّهِ, 64:11 بِٱللَّهِ, 64:11 وَٱللَّهُ, 64:12 ٱللَّهَ, 64:13 ٱللَّهُ, 64:13 إِلَٰهَ, 64:13 ٱللَّهِ, 64:14 ٱللَّهَ, 64:15 وَٱللَّهُ, 64:16 ٱللَّهَ, 64:17 ٱللَّهَ, 64:17 وَٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 64:1 لِلَّهِ, 64:2 وَٱللَّهُ, 64:4 وَٱللَّهُ, 64:6 ٱللَّهُ, 64:6 وَٱللَّهُ, 64:7 ٱللَّهِ, 64:8 بِٱللَّهِ, 64:8 وَٱللَّهُ, 64:9 بِٱللَّهِ, 64:11 ٱللَّهِ, 64:11 بِٱللَّهِ, 64:11 وَٱللَّهُ, 64:12 ٱللَّهَ, 64:13 ٱللَّهُ, 64:13 إِلَٰهَ, 64:13 ٱللَّهِ, 64:14 ٱللَّهَ, 64:15 وَٱللَّهُ, 64:16 ٱللَّهَ, 64:17 ٱللَّهَ, 64:17 وَٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## س م و (root_000745): 64:1 ٱلسَّمَٰوَٰتِ, 64:3 ٱلسَّمَٰوَٰتِ, 64:4 ٱلسَّمَٰوَٰتِ

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

## ECHO و س م (root_001650): for 64:1 ٱلسَّمَٰوَٰتِ, 64:3 ٱلسَّمَٰوَٰتِ, 64:4 ٱلسَّمَٰوَٰتِ: withheld observed target; not identity

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

## ء ر ض (root_000025): 64:1 ٱلْأَرْضِ, 64:3 وَٱلْأَرْضَ, 64:4 وَٱلْأَرْضِ

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

## م ل ك (root_001444): 64:1 ٱلْمُلْكُ

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

## ح م د (root_000355): 64:1 ٱلْحَمْدُ, 64:6 حَمِيدٌ

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

## ك ل ل (root_001315): 64:1 كُلِّ, 64:11 بِكُلِّ

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

## ش ي ء (root_000831): 64:1 شَىْءٍ, 64:11 شَىْءٍ

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

## ش ي ء (root_000832): 64:1 شَىْءٍ, 64:11 شَىْءٍ

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

## ق د ر (root_001205): 64:1 قَدِيرٌ

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

## خ ل ق (root_000434): 64:2 خَلَقَكُمْ, 64:3 خَلَقَ

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

## ك ف ر (root_001307): 64:2 كَافِرٌ, 64:5 كَفَرُوا۟, 64:6 فَكَفَرُوا۟, 64:7 كَفَرُوٓا۟, 64:9 يُكَفِّرْ, 64:10 كَفَرُوا۟

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

## ء م ن (root_000054): 64:2 مُّؤْمِنٌ, 64:8 فَـَٔامِنُوا۟, 64:9 يُؤْمِنۢ, 64:11 يُؤْمِنۢ, 64:13 ٱلْمُؤْمِنُونَ, 64:14 ءَامَنُوٓا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ع م ل (root_001046): 64:2 تَعْمَلُونَ, 64:7 عَمِلْتُمْ, 64:8 تَعْمَلُونَ, 64:9 وَيَعْمَلْ

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

## ب ص ر (root_000121): 64:2 بَصِيرٌ

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

## ح ق ق (root_000347): 64:3 بِٱلْحَقِّ

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

## ص و ر (root_000891): 64:3 وَصَوَّرَكُمْ, 64:3 صُوَرَكُمْ

- **B001** bir yöne eğilme veya yöneltme — 
  صور يصور إذا مال؛ صرت الشيء أصوره وأصرته إذا أملته إليك (maqayis)؛ يصور عنقه إلى الشيء إذا مال نحوه (ayn;tahdhib)؛ الصور بالتحريك الميل؛ أصاره فانصار؛ طعنه فتصور أي مال للسقوط؛ صر إلي وصر وجهك إلي أي أقبل علي (sihah)؛ صرعه فتجور وتصور إذا سقط (tahdhib)
- **B002** toplama ya da kesip ayırma — 
  صرهن أي ضمهن ويقال قطعهن (ayn)؛ صرت الشيء أيضا قطعته وفصلته؛ فصرهن بضم الصاد وكسرها (sihah)
- **B003** ayırt edici görünüş ve biçim — bir şeyin ayırt edici görünüşü veya somut ya da zihinsel biçimi · varlıklara görünüş ve biçim veren · güzel görünümlü erkek · bir şeyi zihnimde canlandırdım · yapılmış görüntüler veya heykeller
  الصورة صورة كل مخلوق وهي هيئة خلقته؛ البارئ المصور؛ رجل صير إذا كان جميل الصورة (maqayis)؛ صورت صورة وتجمع على صور (ayn)؛ صوره الله صورة حسنة فتصور؛ تصورت الشيء؛ التصاوير التماثيل (sihah)؛ المصور من صفات الله تعالى لتصويره صور الخلق؛ حسن الصورة والهيئة (tahdhib)؛ الصورة ما ينتقش به الأعيان ويتميز بها غيرها؛ محسوس؛ معقول (mufradat)
- **B004** üfleme boynuzu — içine üflenilen boynuz biçimli araç
  الصور القرن (sihah)؛ الصور القرن فهو واحد لا يجوز أن يقال واحدته صورة؛ صاحب القرن قد التقم القرن (tahdhib)
- **B005** palmiye kümesi — palmiye kümesi veya genç palmiyelik · palmiye ağacı · ağaçlı arazi · atın palmiye kümesine benzetilen alın yelesi
  الصور جماعة النخل وهو الحائش؛ شعر الناصية من الفرس يسمى صورا؛ التشبيه بصور النخل؛ الصارة أرض ذات شجر (maqayis)؛ الصور النخل الصغار (ayn)؛ الصور بالتسكين النخل المجتمع الصغار؛ كأن عرفا مائلا من صوره؛ أرض ذات شجر (sihah)؛ دخل صور نخل؛ الصور جماع النخل؛ الصورة النخلة (tahdhib)
- **B006** sığır sürüsü — sığır sürüsü, özellikle yabani sığır sürüsü · sığır sürüleri · az sayıdaki sığır sürülerini bildiren çoğul
  الصوار وهو القطيع من البقر والجمع صيران (maqayis)؛ الصوار والصوار القطيع من بقر الوحش والعدد أصورة ويجمع على صيران (ayn)؛ الصيران جمع صوار وهو القطيع من البقر (sihah)؛ الصوار والصوار القطيع من البقر والعدد أصورة والجميع صيران (tahdhib)
- **B007** miskin kokusu, kabı, kesesi veya parçası — miskin kokusu, kabı, keseleri veya parçaları · misk keseleri ya da gömlek düğmelerine yerleştirilen misk parçaları · miskle ilgili aynı adın değişik söylenişi
  الصوار صوار المسك؛ قال قوم هو ريحه وقال قوم هو وعاؤه (maqayis)؛ أصورة المسك نافقاته؛ الصوار ريح المسك؛ أصورة المسك قطع تجعل في أزرار القمص (ayn)؛ الصوار أيضا وعاء المسك (sihah)؛ أصورة المسك نافقاته (tahdhib)
- **B008** baş derisinde kaşıntı — başta, saçı ayıklatma isteği veren kaşıntı benzeri duyum
  أجد في رأسي صورة أي حكة (maqayis)؛ أجد في رأسي صورة وهي شبه الحكة حتى يشتهي أن يفلى رأسه (sihah)؛ الصورة الحكة انتغاش الحطى في الرأس؛ تشفيني من الصورة (tahdhib)
- **B009** çağrılınca karşılık veren serçe [kalıp] — çağrılınca karşılık veren serçe
  عصفور صوار وهو الذي إذا دعي أجاب؛ لا أحسبه عربيا؛ إن صح أن يكون من الباب لأنه يميل إلى داعيه (maqayis)؛ عصفور صوار وهو الذي يجيب الداعي (ayn;tahdhib)؛ عصفور صوار للذي يجيب إذا دعي (sihah)
- **B010** ağzın iki köşesi — ağzın iki köşesi · ağzın iki köşesi için kullanılan halk söyleyişi
  الصواران صماغا الفم؛ العامة تسميهما الصوارين وهما الصامغان أيضا (tahdhib)

## ح س ن (root_000323): 64:3 فَأَحْسَنَ, 64:17 حَسَنًا

- **B001** akla, eğilime veya duyulara göre güzel ve beğenilir olma — güzel ve beğenilir olma; güzellik · güzel olmak · güzel erkek · güzel kadın · güzel kadın · çok güzel kadın · çok güzel · güzel yanlar ve iyi nitelikler · bedenin güzel yeri
  الحسن ضد القبح (maqayis;sihah)؛ حسن الشيء فهو حسن (ayn)؛ الحسن نعت لما حسن (tahdhib)؛ كل مبهج مرغوب فيه (mufradat)؛ مستحسن من جهة العقل ومستحسن من جهة الهوى ومستحسن من جهة الحس (mufradat)؛ رجل حسن وامرأة حسناء وحسانة (maqayis)؛ الحسان الحسن جدا (ayn)؛ المحاسن ضد المساوىء (maqayis;ayn;sihah;tahdhib)
- **B002** bir şeyi güzelleştirme, işi iyi yapma veya başkasına iyilik etme — bir şeyi güzelleştirmek · birine iyilik etmek · işini iyi ve ustalıkla yapmak · iyilik etme veya işi iyi yapma · iyilik eden veya işini iyi yapan kimse · sürekli iyilik eden kimse · güzel bulmak; beğenmek
  أحسنت إليه وبه (sihah)؛ وهو يحسن الشيء أي يعمله (sihah)؛ حسنت الشيء تحسينا زينته (sihah)؛ أحسن يا هذا فإنك محسان (tahdhib)؛ الإحسان ضد الإساءة (tahdhib)؛ أحسنت بفلان أي أحسنت إليه (tahdhib)؛ الإحسان يقال على وجهين الإنعام على الغير وإحسان في فعله (mufradat)؛ الإحسان فوق العدل (mufradat)
- **B003** kişiye ulaşan sevindirici iyilik, karşılık veya iyi sonuç — kişiye ulaşan iyilik, bolluk veya ödül · iyi son veya en güzel karşılık; sonsuz mutluluk yurdu, utkı ya da inancı uğruna ölme · iki iyi sonuçtan biri: utkı ya da inancı uğruna ölme · kötü işleri gideren iyi işler, özellikle beş günlük tapınma
  للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى (ayn)؛ الحسنة خلاف السيئة (sihah)؛ الحسنى خلاف السوأى (sihah)؛ الحسنى هي الجنة وضد الحسنى السوءى (tahdhib)؛ إحدى الحسنيين يعني الظفر أو الشهادة (tahdhib)؛ حسنة أي نعمة (tahdhib)؛ أي غنيمة وخصب (tahdhib)؛ الحسنة يعبر عنها عن كل ما يسر من نعمة (mufradat)؛ خصب وسعة وظفر (mufradat)؛ من ثواب وما أصابك من سيئة أي من عقاب (mufradat)
- **B004** yer, gök cismi ve beden bölümü adları ile kum tepesine oturma kullanımı — bir dağın, kum sırtının, kumluğun veya kum tepesinin adı · ön kolun bileğe yakın yarısı · ay · yüksek dağ · temiz ve yüksek bir kum tepesine oturmak · iki yerin veya iki kum sırtının birlikte anılışı
  الحسن جبل وحبل من حبال الرمل (maqayis)؛ الحسن من الذراع النصف الذي يلي الكوع (maqayis)؛ حسن اسم رملة لنبي سعد (ayn)؛ الحاسن القمر (sihah)؛ الحسن اسم رملة لبنى سعد (sihah)؛ الحسن نقا في ديار بني تميم (tahdhib)؛ أحسن الرجل إذا جلس على الحسن وهو الكثيب النقي العالي (tahdhib)؛ الحسين الجبل العالي (tahdhib)
- **B005** bir işteki en yüksek çabası ve erişebileceği son sınır — bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır · bir işi yaparken gösterebileceği en yüksek çaba ve erişebileceği son sınır
  حُسَيْناؤه أن يفعل كذا وحُسَيْناه مثله أي جهده وغايته (tahdhib)

## ص ي ر (root_000897): 64:3 ٱلْمَصِيرُ, 64:10 ٱلْمَصِيرُ

- **B001** bir durumdan ötekine geçme, bir sonuca varma veya bir şeyi o duruma getirme — olmak, bir duruma dönüşmek · bir yere ya da sonuca varmak · bir şeyi belirli bir duruma getirmek · varış yeri, son veya sonuç · oluş, bir duruma geçiş · işin sonu, varacağı sonuç · bir işin sonuçlanma eşiğinde
  صار يصير صيرا وصيرورة؛ صير كل شيء مصيره؛ صيور الأمر آخره؛ صار الشيء كذا؛ صرت إلى فلان مصيرا؛ صيرته أنا كذا أي جعلته؛ صار إلى كذا انتهى إليه؛ صار عبارة عن التنقل من حال إلى حال
- **B002** bir işin sonuçlanma eşiği veya dağın başı — bir işin sonuçlanma eşiğinde · dağın başı, zirvesi · tepe başındaki dairesel yapı veya taş yığını
  على صير أمر أي إشراف من قضائه؛ صير الأمر شرفه؛ على صير أمر إذا كان على إشراف من قضائه؛ على صير أمر أي على طرف منه؛ صارة الجبل رأسه؛ الصيرة على رأس القارة
- **B003** sığır veya koyun ağılı — sığır veya koyun ağılı · ağıllar
  الصير كالحظائر يتخذ للبقر والواحدة صيرة؛ صيرة البقر موضع يتخذ من أغصان الشجر والحجارة كالحظيرة؛ الصيرة حظيرة الغنم وجمعها صير؛ الصيرة الحظيرة للغنم
- **B004** yarık açma, kesme, yana eğme veya boyun bükme — yarık, özellikle kapı aralığı · kapıdaki bakma yarığı · kesmek veya yana eğmek · insanların boyunlarını büken kimse
  الصير وهو الشق؛ الصير الشق؛ صير باب؛ صاره يصيره لغة في يصوره أي قطعه وكذلك إذا أماله؛ الصير شق الباب؛ الصائر الملوي أعناق الرجال؛ الصير الشق وهو المصدر
- **B005** niteliği açıklanmamış bir yiyecek türü — niteliği açıklanmamış bir yiyecek türü
  الصير وهو شيء يقال له الصحناة؛ الصير شبه الصحناء؛ الصير أيضا الصحناة؛ الصير فذاق منه؛ تفسيره في الحديث أنه الصحناء
- **B006** babasına çekmek [kalıp] — babasına çekmek
  تصير فلان أباه إذا نزع إليه في الشبه؛ تصير فلان أباه إذا نزع إليه في الشبه؛ تصير فلان أباه وتقيضه إذا نزع إليه في الشبه
- **B007** mezar ya da konak yeri; su başına varma veya konak yerine dönme — mezar, ölünün karar yeri · konak yeri, menzil · su başına varmak · konak yerine dönmüş topluluk veya konak yerine dönüş
  صيره قبره؛ هذا صير فلان أي قبره؛ أين مصيركم أي أين منزلكم؛ صار الرجل يصير إذا حضر الماء؛ الصير رجوع المنتجعين إلى محاضرهم
- **B008** topluluk, grup — topluluk, grup
  الصير الجماعة
- **B009** zilin çınlaması — zil sesi, çınlama
  الصيار صوت الصنج؛ رنات الصيار

## ع ل م (root_001040): 64:4 يَعْلَمُ, 64:4 وَيَعْلَمُ, 64:4 عَلِيمٌۢ, 64:11 عَلِيمٌ, 64:18 عَٰلِمُ

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

## س ر ر (root_000697): 64:4 تُسِرُّونَ

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

## ع ل ن (root_001041): 64:4 تُعْلِنُونَ

- **B001** açığa çıkıp yayılma; açığa vurup belli etme — açığa çıkmak; duyulup yayılmak · açığa vurmak; açıkça belli etmek · işin duyulup yaygınlaşması · gizli olmayan açık durum; açıklık · karşılıklı açık konuşma; iki tarafın içindekini birbirine söylemesi · içindekileri karşılıklı olarak açıkça söyleme · sırrını açıkça söyleyen kişi · bir şeyi açığa vurmak
  يدل على إظهار الشيء والإشارة إليه وظهوره، علن الأمر يعلن، وأعلنته أنا، والعلان المعالنة (maqayis)؛ علن الأمر يعلن علونا وعلانية أي شاع وظهر، وأعلنته إعلانا (ayn)؛ العلانية خلاف السر، علن الأمر يعلن علونا، وأعلنته أنا إذا أظهرته، والعلان المعالنة، ورجل علنة يبوح بسره (sihah)؛ علن الأمر يعلن علنا، وعلن يعلن إذا شاع وظهر، أعلن الأمر إذا اشتهر، استعلن أي أظهره، العلان المعالنة إذا أعلن كل واحد لصاحبه ما في نفسه، العلانية ظهور الأمر (tahdhib)؛ العلانية ضد السر، وأكثر ما يقال ذلك في المعاني دون الأعيان، علن كذا، وأعلنته أنا (mufradat)
- **B002** kitap başlığı ve başlık koyma — kitabın başlığı · kitaba başlık koymak
  علوان الكتاب عنوانه، وقد علونت الكتاب إذا عنونته (sihah)

## ص د ر (root_000849): 64:4 ٱلصُّدُورِ

- **B001** göğüs bölgesi — göğüs · göğüsler · göğsün üstte çıkıntılı kesimi · göğsü örten kısa giysi · devenin göğsündeki damga · yükü sabitleyen göğüs bağı · göğsünden rahatsız olan kimse · birinin göğsüne bir şeyle vurmak · göğsü ağrımak · güçlü göğüslü aslan
  الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)
- **B002** ön, üst ya da başlangıç bölümü — ön, üst ya da başlangıç bölümü · mızrağın üst bölümü · işin başlangıcı · toplantının ön kısmı; kitabın veya sözün başlangıcı · okun ortasından ucuna uzanan ön bölümü · ön gövdesi kalın ok · göğsüyle öne çıkıp yarışı geçmek · kitaba giriş bölümü koymak · toplantının başköşesine oturmak
  الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)
- **B003** geldiği yerden ayrılıp dönme — bir yerden ya da durumdan ayrılış · su başından, geldikten sonra ayrılmak · geri döndürmek · su başından dönüşü sağlayan yol
  صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)
- **B004** eylem türetme temeli; çıkış yeri veya zamanı — eylemlerin türediği temel sözcük biçimi · çıkış yeri ya da zamanı
  المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)
- **B005** para ödeme ve güvence yükümlülüğü koyma — birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak · kendisine para ödeme ve güvence yükümlülüğü konmak
  صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)
- **B006** bir şeyin bölümü ya da kümesi — bir şeyin bölümü ya da kümesi
  الصدر الطائفة من الشيء (sihah)

## ء ت ي (root_000009): 64:5 يَأْتِكُمْ, 64:6 تَّأْتِيهِمْ

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

## ن ب ء (root_001464): 64:5 نَبَؤُا۟, 64:7 لَتُنَبَّؤُنَّ

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

## ق ب ل (root_001198): 64:5 قَبْلُ

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

## ذ و ق (root_000526): 64:5 فَذَاقُوا۟

- **B001** ağızla tadını algılamak — yiyeceği ağzıyla tatmak · ağızla tatma · tat; ağızda algılanan nitelik · tatma veya algılanan tat · tatma; tadılan yiyecek miktarı · hiçbir şey tatmadım · yiyecekten hiçbir şey tatmadım · bir şeyi azar azar tatmak
  ذقت المأكول أذوقه ذوقا (maqayis)؛ ذواقه ومذاقه طيب أي طعمه (ayn;tahdhib)؛ ما ذقت ذوقا أي شيئا (sihah)؛ ما ذقت ذواقا وهو ما يذاق من الطعام (tahdhib)
- **B002** bizzat yaşayarak veya sınayarak tanımak — bir kişiyi sınayıp tanımak · birinin elindekini sınayıp tanımak · kötü bir olayı bizzat yaşamak · işinin kötü sonucunu veya cezasını yaşamak · azabı doğrudan yaşamak · açlık ve korku cezasını yaşatmak · denenmiş ve bilinen · birini sınayıp hakkında olumsuz sonuca varmak
  ذقت ما عند فلان اختبرته (maqayis)؛ كل ما نزل بإنسان من مكروه فقد ذاقه (maqayis;ayn;tahdhib)؛ ذقت فلانا وذقت ما عنده (ayn;tahdhib)؛ ذقت ما عند فلان أي خبرته (sihah)؛ أذاقه الله وبال أمره (sihah)؛ أمر مستذاق أي مجرب معلوم (sihah)؛ فذاقت وبال أمرها أي خبرت (tahdhib)؛ الذوق يكون بالفم وبغير الفم (tahdhib)
- **B003** yayı çekip gücünü sınamak — yayı çekip esnekliğini ve gücünü sınamak · tüccarların elleriyle yoklayıp sınadığı
  ذاق القوس إذا نظر ما مقدار إعطائها وكيف قوتها (maqayis)؛ ذقت القوس إذا جذبت وترها لتنظر ما شدتها (sihah)؛ ذق هذا القوس أي انزع فيها لتخبر لينها وشدتها (tahdhib)؛ نظر إلى القوس ورازها (tahdhib)
- **B004** eşinden çabuk bıkıp sürekli yeni eş arayan — evlilikte eşinden çabuk bıkan; sık evlenip boşanan · evlilikte eşlerine bağlanamayıp başkasına yönelen erkekler ve kadınlar · çok evlenip çok boşanan erkek
  لا يحب الذواقين والذواقات (ayn;tahdhib)؛ كلما تزوجا كرها ومدا أعينهما إلى غيرهما (ayn)؛ ألا يطمئن ولا تطمئن كلما تزوج أو تزوجت كرها وطمحا إلى غير الزوج (tahdhib)؛ الذواق الملول (sihah)؛ رجل ذواق مطلاق إذا كان كثير النكاح كثير الطلاق (tahdhib)
- **B005** cinsel birleşmenin hazzını yaşamak — kadına girip onunla cinsel birleşmenin hazzını yaşamak · erkekle cinsel birleşip birlikteliğin hazzını yaşamak
  ذاق الرجل عسيلة المرأة إذا أولج فيها أدافه حتى خبر طيب جماعها وذاقت هي عسيلته كذلك لما خالطها فوجدت حلاوة لذة الخلاط
- **B006** senden sonra belirli bir duruma gelmek — senden sonra seçkin biri oldu · senden sonra cömert oldu · at senden sonra hızlı koşar oldu
  أذاق فلان بعدك سروا أي صار سريا؛ أذاق بعدك كرما؛ أذاق الفرس بعدك عدوا أي صار عداء بعدك

## و ب ل (root_001619): 64:5 وَبَالَ

- **B001** çok güçlü ağır yağmur — şiddetli ve ağır damlalı yağmur · iri damlalı çok güçlü yağmur · gök çok güçlü yağmur yağdırdı
  الوبل والوابل المطر الشديد (maqayis)؛ المطر الشديد الوقع وهو الوابل (jamhara)؛ الوابل المطر الشديد (sihah)؛ المطر الشديد الضخم القطر الغليظ العظيم (tahdhib)؛ الوبل والوابل المطر الثقيل القطار (mufradat)
- **B002** ağır ve zararlı sertlik — bir şeyde ağırlık · ağır, sert ve yıpratıcı · ağırlık, zarar veya kötü sonuç · çok sert taşlı zemin · üstlendiği işi düzeltemeyen hantal kişi · bir işin zararı ve ağırlığı
  وبلة الشيء ثقله؛ شيء وبيل أي وخيم؛ الوبيل الضرب الشديد (maqayis)؛ أمر وبيل أي شديد؛ الوبال الثقل (jamhara)؛ الوبلة الثقل والوخامة؛ أخذا وبيلا أي شديدا؛ ضرب وبيل وعذاب وبيل أي شديد (sihah)؛ أخذا هو الثقيل الغليظ جدا؛ الوبال الفساد؛ شره ومضرته (tahdhib)؛ لمراعاة الثقل قيل للأمر الذي يخاف ضرره وبال؛ أخذا وبيلا (mufradat)
- **B003** bedene yaramayan uygunsuzluk — sağlığa dokunma ve elverişsizlik · dokunan, sindirilmeyen veya zararı beklenen · bir yeri bedene ve yemeğe uygun bulmamak
  استوبلت البلد إذا لم يوافقك؛ الوبيل الكلأ (maqayis)؛ كلأ وبيل أي لا يمرئ الراعية (jamhara)؛ وبل المرتع فهو وبيل أي وخيم؛ استوبلت البلد أي استوخمته ولم يوافقك في بدنك (sihah)؛ استوبلت الأرض استوخمتها؛ ماء وبيل ووبيء ووخيم؛ الوبيل من المرعى الوخيم؛ كلأ وبيلا (tahdhib)؛ طعام وبيل وكلأ وبيل يخاف وباله (mufradat)
- **B004** kalın sopa veya odun demeti — iri sopa · kalın sopa veya odun demeti · iri sopa · çamaşır dövme tahtası · odun demeti · odun demeti · odun demeti
  الوبيل خشبة القصار؛ الوبيل الحزمة من الحطب (maqayis)؛ الوبيلة العصا الغليظة أو الحزمة من الحطب (jamhara)؛ الوبيل العصا الضخمة؛ الموبل الحزمة من الحطب وكذلك الوبيل (sihah)؛ الوبيل والموبل العصا الضخمة؛ الموبل الحزمة من الحطب؛ الوبيل خشبة القصار (tahdhib)
- **B005** yeri tartışmalı eklem parçası — yeri tartışmalı eklem parçası
  الوابلة عظم مفصل الركبة (maqayis)؛ الوابلة رأس المنكب (jamhara)؛ الوابلة طرف الكتف وهو رأس العضد (sihah)؛ الوابلة طرف الكتف ولحمة الكتف وطرف عظم العضد الذي يلي المنكب ورأس العضد في حق الكتف (tahdhib)
- **B006** dişi koyunda çiftleşme isteği — dişi koyunda erkeğe duyulan güçlü çiftleşme isteği · koyun sürüsünün çiftleşme isteğine girmesi
  بالشاة وبلة شديدة أي شهوة للفحل؛ وقد استوبلت الغنم (sihah)

## ء م ر (root_000051): 64:5 أَمْرِهِمْ

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

## ع ذ ب (root_000994): 64:5 عَذَابٌ

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

## ء ل م (root_000046): 64:5 أَلِيمٌ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ك و ن (root_001332): 64:6 كَانَت

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

## ر س ل (root_000563): 64:6 رُسُلُهُم, 64:8 وَرَسُولِهِۦ, 64:12 ٱلرَّسُولَ, 64:12 رَسُولِنَا

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

## ب ي ن (root_000170): 64:6 بِٱلْبَيِّنَٰتِ, 64:12 ٱلْمُبِينُ

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

## ق و ل (root_001272): 64:6 فَقَالُوٓا۟, 64:7 قُلْ

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

## ECHO ق ل ل (root_001251): for 64:6 فَقَالُوٓا۟, 64:7 قُلْ: withheld observed target; not identity

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

## ب ش ر (root_000120): 64:6 أَبَشَرٌ

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

## ه د ي (root_001583): 64:6 يَهْدُونَنَا, 64:11 يَهْدِ

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

## ECHO ه د د (root_001580): for 64:6 يَهْدُونَنَا, 64:11 يَهْدِ: withheld observed target; not identity

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

## و ل ي (root_001684): 64:6 وَتَوَلَّوا۟, 64:12 تَوَلَّيْتُمْ

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

## غ ن ي (root_001110): 64:6 وَّٱسْتَغْنَى, 64:6 غَنِىٌّ

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

## ز ع م (root_000633): 64:7 زَعَمَ

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

## ب ع ث (root_000129): 64:7 يُبْعَثُوا۟, 64:7 لَتُبْعَثُنَّ

- **B001** durgun olanı harekete geçirme — harekete geçirmek; uyandırmak · devenin bağını çözüp onu ayağa kaldırmak · uyuyanı uyandırmak · kargaşanın kabarmaları ve alevlenmeleri · neredeyse hiç uyumayan adam · neredeyse hiç çökmeyen dişi deve
  الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)
- **B002** gönderme veya yöneltme — göndermek; yöneltmek · görevle göndermek; yola çıkarmak · birini bir iş için göndermek · birini bir işi yapmaya isteklendirip yöneltmek · asker birliğini düşmana karşı göndermek · göreve gönderilmiş topluluk veya birlik · gönderilmiş ordular
  البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)
- **B004** yola koyulup ilerleme — harekete geçip ilerlemek; hızlanmak · yola koyulma ve ilerleme · şiir benden akıp geldi
  انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)

## ر ب ب (root_000532): 64:7 وَرَبِّى

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

## ECHO ر ب و (root_000537): for 64:7 وَرَبِّى: withheld observed target; not identity

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

## ي س ر (root_001694): 64:7 يَسِيرٌ

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

## ن و ر (root_001564): 64:8 وَٱلنُّورِ, 64:10 ٱلنَّارِ

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

## ن ز ل (root_001492): 64:8 أَنزَلْنَا

- **B001** aşağı inme veya bir yere konaklama — yüksekten inmek veya bir yerde konaklamak · yağmurun gökten yağması · bir yerde yükünü bırakıp konaklamak · ağır ağır inme
  هبوط شيء ووقوعه؛ نزل عن دابته نزولا؛ نزل المطر من السماء نزولا (maqayis)؛ نزل فلان عن الدابة أو من علو إلى سفل (ayn)؛ المنزل النزول وهو الحلول؛ التنزل النزول في مهلة (sihah)؛ النزول في الأصل هو انحطاط من علو؛ نزل في مكان كذا حط رحله (mufradat)
- **B002** Tanrısal iyilik, ceza veya bildiriyi insanlara ulaştırma — başkasını indirmek veya bir şeyi yerine ulaştırmak · Tanrı'nın iyilikleri ve cezaları insanlara vermesi · bölüm bölüm ve yinelenerek bildirme · Tanrısal esirgemenin onlara erişmesi
  تنزلت الرحمة عليهم (tahdhib)؛ إنزال الله تعالى نعمه ونقمه على الخلق وإعطاؤهم إياها؛ إما بإنزال الشيء نفسه كإنزال القرآن وإما بإنزال أسبابه؛ التنزيل يختص بما أنزل مفرقا ومرة بعد أخرى (mufradat)
- **B003** konaklama yeri veya bulunulan derece — konaklama yeri, ev veya su başı · derece veya konum · birinin derecesini düşürmek · topluluğu konaklama yerlerine yerleştirmek
  مكان نزل ينزل فيه كثيرا؛ وجدت القوم على نزلاتهم أي منازلهم (maqayis)؛ المنزل المنهل والدار؛ المنزلة المرتبة؛ استنزل فلان أي حط عن مرتبته (sihah)؛ نزلت القوم أي أنزلتهم المنازل؛ نزل فلان غيره أي قدر لها المنازل (tahdhib)؛ أنزلني منزلا مباركا؛ نزل في مكان كذا حط رحله (mufradat)
- **B004** bir şeyi uygun yerine veya sırasına koyma — bir şeyi düzenleyip uygun yerine veya sırasına koyma
  التنزيل ترتيب الشيء ووضعه منزله (maqayis)؛ التنزيل أيضا الترتيب (sihah)؛ التنزيل يختص بالموضع الذي يشير إليه إنزاله مفرقا ومرة بعد أخرى (mufradat)
- **B005** konuk için hazırlanan yiyecek ve ağırlama payı — konuğa hazırlanan yiyecek veya yol azığı · ürün geliri, fazlalık veya bağış · konuk · birini konuk etmek · topluluğun geçim payları · bol ve bereketli yemek · bol veren ve eli açık olan · bir araya gelmiş pay
  النزل ما يهيأ للنزيل؛ طعام ذو نزل؛ النزيل الضيف (maqayis)؛ النزل ما يهيأ للقوم والضيف؛ النزل ريع ما يزرع (ayn)؛ النزل ما يهيأ للنزيل؛ النزل أيضا الريع؛ النزيل الضيف (sihah)؛ حسن النزل أي الضيافة؛ أنزال القوم أرزاقهم؛ أقمت لهم غذاءهم وما يصلح معه أن ينزلوا عليه؛ النزل الريع والفضل (tahdhib)؛ النزل ما يعد للنازل من الزاد؛ أنزلت فلانا أضفته؛ ذو نزل له ريع؛ حظ نزل مجتمع تشبيها بالطعام النزل (mufradat)
- **B006** başa gelen ağır sıkıntı — insanların başına gelen ağır sıkıntı veya felaket
  النازلة الشديدة من شدائد الدهر تنزل (maqayis)؛ النازلة الشديدة من شدائد الدهر تنزل بالقوم وجمعها النوازل (ayn)؛ النازلة الشديدة من شدائد الدهر تنزل بالناس (sihah;tahdhib)؛ يعبر بالنازلة عن الشدة وجمعها نوازل (mufradat)
- **B007** savaşmak için karşı karşıya inme — savaşta karşı karşıya gelme · savaşmak üzere inin
  النزال في الحرب أن يتنازل الفريقان؛ نزال كلمة توضع موضع انزل (maqayis)؛ النزال المنازلة في الحرب أن ينزلا معا فيقتتلا؛ نزال أي انزلوا للحرب (ayn)؛ نزال بمعنى انزل؛ النزال في الحرب أن يتنازل الفريقان (sihah)؛ النزال في الحرب المنازلة (mufradat)
- **B008** hac yolculuğunda Mina'ya varma — hac yapmak veya Mina'ya gelmek · topluluğun Mina'ya gelmesi
  يعبرون عن الحج بالنزول؛ نزل إذا حج؛ نزلنا أتينا منى (maqayis)؛ نزل القوم إذا أتوا منى (sihah;tahdhib)؛ نزل فلان إذا أتى منى (mufradat)
- **B009** erkeğin dışarı çıkan üreme sıvısı — erkeğin dışarı çıkan üreme sıvısı · cinsel birleşme sırasında boşalmak · kadının erkeğin boşalmasını istemesi
  النزالة ماء الرجل (maqayis)؛ النزالة بالضم ماء الرجل وقد أنزل (sihah)؛ أنزل الرجل ماءه إذا جامع والمرأة تستنزل ذلك (tahdhib)؛ النزالة والنزل يكنى بهما عن ماء الرجل إذا خرج عنه (mufradat)
- **B010** bir kez inme — bir kez inme · bir kez daha · soğuk algınlığına benzer geçici rahatsızlık
  النزلة المرة الواحدة؛ ولقد رآه نزلة أخرى أي مرة أخرى (ayn)؛ النزلة كالزكام؛ ولقد رآه نزلة أخرى قالوا مرة أخرى (sihah)؛ النزلة المرة الواحدة من النزول (tahdhib)
- **B011** akış, konaklanma veya biçim özelliğiyle nitelenen yer [kalıp] — az yağmurda bile hızla su akıtan sert arazi · sık konaklanan, geniş uzak, otlaklı veya suyu çabuk akan yer · dar vadi
  مكان نزل ينزل فيه كثيرا (maqayis)؛ أرض نزلة ومكان نزل إذا كانت تسيل من أدنى مطر لصلابتها (sihah)؛ طعام نزل وأرض نزلة ومكان نزل سريع السيل؛ مكان نزل ينزل فيه كثيرا؛ مكان نزل واسع بعيد؛ مكان نزل إذا كان محلالا مربا؛ النزل من الأودية الضيق منها (tahdhib)

## خ ب ر (root_000387): 64:8 خَبِيرٌ

- **B001** bilgi edinme, bildirme ve deneyerek iç yüzü tanıma — bir olay veya durum hakkında edinilen ve aktarılan bilgi · bilgi vermek; bildirmek · bir konuyu sorup bilgi edinmek · sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma · sınayıp deneyerek bilgi sahibi olmuş kişi · bilgili; bir işin iç yüzüne hakim · dış görünüşün karşısındaki iç yüz ve gerçek nitelik
  الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)
- **B002** gevşek, alçak ve su tutan arazi veya su birikintisi — gevşek, yumuşak veya alçak olup su toplayan arazi · sıcak, ağaçlı ve suyu bol yer · akış yatağında oluşan geçilebilir su birikintisi
  الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)
- **B003** üründen pay karşılığı ortakçılık ve bunu yapan çiftçi — toprağı işleyen çiftçi · ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık
  الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)
- **B004** büyük su tulumu ve bolluğuyla ona benzetilen dişi deve — büyük ve geniş su tulumu · bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve
  الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)
- **B005** yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü — kesilip yenebilen yumuşak bitki · yün veya ince hayvan kılı · devenin ağzında oluşan veya ağzından çıkan köpük
  الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)
- **B006** ortak alınıp kesilen koyun veya bölüşülen et-balık payı — ortaklaşa alınıp kesilen ve eti bölüşülen koyun · et veya balıktan alınan pay
  الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)

## ي و م (root_001700): 64:9 يَوْمَ, 64:9 لِيَوْمِ, 64:9 يَوْمُ

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

## ج م ع (root_000259): 64:9 يَجْمَعُكُمْ, 64:9 ٱلْجَمْعِ

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

## غ ب ن (root_001072): 64:9 ٱلتَّغَابُنِ

- **B001** işlemde gizlice hakkını eksiltme — alışverişte gizli haksız eksiltme · satışta karşı tarafı aldatarak hakkını eksiltmek · alışverişte haksız kayba uğratılmış · alışverişteki gizli haksız eksiltme · bu iş senin zararına ve hakkını eksiltir
  غبن الرجل في بيعه إذا اهتضم فيه (maqayis)؛ الغبن في البيع وغبنته فهو مغبون في تجارته (ayn)؛ إذا نقصه (jamhara)؛ في البيع أي خدعته (sihah)؛ أن تبخس صاحبك في معاملة بينك وبينه بضرب من الإخفاء (mufradat)
- **B002** görüş ve kavrayış zayıflığı — görüş zayıflığı · görüşünde zayıf veya yetersiz olmak · görüşü zayıf, aklı veya dini eksik · görüş zayıflığı
  غبن في رأيه إذا ضعف رأيه (maqayis)؛ الغبن في الرأي (ayn)؛ وغبن دينه وعقله فهو غبين في العقل والدين (jamhara)؛ وغبن رأيه إذا نقصه فهو غبين أي ضعيف الرأي (sihah)؛ وإن كان في رأي يقال غبن (mufradat)
- **B003** karşılıklı zarara uğratma ve kaybın açığa çıkışı — birbirini karşılıklı zarara uğratma · insanların yaptıklarındaki kazanç ve kaybın ortaya çıktığı son yargı günü
  ويوم التغابن في الآخرة بالأعمال (ayn)؛ التغابن أن يغبن القوم بعضهم بعضا ومنه قيل يوم التغابن ليوم القيامة (sihah)؛ يوم التغابن يوم القيامة لظهور الغبن في المبايعة (mufradat)
- **B004** bedenin gizli kıvrım yeri — bedenin gizli ve kıvrımlı bölgeleri · bedenin gizli bir kıvrım yeri · bedeninin gizli bölgeleri temiz ve hoş kokulu
  والمغابن الأرفاغ سميت بذلك للينها وضعفها (maqayis)؛ والمغابن الأرفاغ والآباط الواحد مغبن (ayn)؛ والمغابن الأرفاغ (sihah)؛ كل منثن من الأعضاء كأصول الفخذين والمرافق مغابن لاستتاره (mufradat)
- **B005** gizli kıvrıma alma veya giysi ya da yiyeceği katlama — bir şeyi gizli bir kıvrıma almak · giysiyi veya yiyeceği kıvırıp katlamak
  واغتبنت الشيء أخذته في المغبن (ayn)؛ وغبنت الثوب والطعام مثل خبنت (sihah)
- **B006** dikkatsizlikle kaçırıp kayıp sayma — bir şeyi dikkatsizlikle gözden kaçırıp bunu kayıp saymak
  وغبنت كذا غبنا إذا غفلت عنه فعددت ذلك غبنا (mufradat)

## ص ل ح (root_000876): 64:9 صَٰلِحًا

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

## س و ء (root_000755): 64:9 سَيِّـَٔاتِهِۦ

- **B001** çirkinlik ve kötülük — çirkinlik, kötülük ve nitelikçe bozukluk · çirkin adam · çirkin kadın · kötü ve çirkin iş · kötü davranış veya günah · kötü davranış veya en kötü sonuç · ceza ateşi veya görünüşü kötü son · kötü veya ayıplanan adam · kötü iş · kötü söz · çirkin durum veya huy · utanç verici iş veya durum · kusurları ve hastalıkları
  من باب القبح (maqayis)؛ السوء نعت لكل شيء رديء وساء الشيء قبح (ayn)؛ السوءى نقيض الحسنى والسيئة أصلها سيوئة (sihah)؛ كل كلمة أو فعلة قبيحة فهي سوء (tahdhib)؛ عبر عن كل ما يقبح بالسوأى والسيئة الفعلة القبيحة (mufradat)
- **B002** birini üzme veya ona kötülük etme — insanı üzen kötülük veya istenmeyen sonuç · onu üzdü veya ona istemediği bir şey yaşattı · birine kötülük etti veya onu üzdü · ona kötü davrandı · üzüldü ve sıkıntı duydu · üzme veya kötülük etme · yenilgi, yıkım veya acı getiren kötü son · başlarına onları üzen bir şey geldi
  سؤت وجه فلان وأنا أسوءه مساءة وأسأت إليه في الصنع (ayn)؛ ساءه يسوءه سوءا ومساءة نقيض سره (sihah)؛ ساء يسوء فعل لازم ومجاوز واستاء فلان من السوء (tahdhib)؛ السوء كل ما يغم الإنسان وساءني كذا وأسأت إلى فلان (mufradat)
- **B003** bedensel kusur veya hastalık — bedensel kusur, bozukluk veya hastalık · beyaz lekeli deri hastalığı veya başka bir bedensel kusur olmadan
  السوء اسم جامع للآفات والداء ويكنى بالسوء عن البرص (ayn)؛ من غير برص (sihah)؛ السوء الاسم الجامع للآفات والداء والسوء كناية عن اسم البرص (tahdhib)؛ من غير آفة بها وفسر بالبرص (mufradat)
- **B004** örtülmesi gereken cinsel bölge — kadın veya erkeğin örtülmesi gereken cinsel bölgesi · örtülmesi gereken özel bölgeler
  السوأة فرج الرجل والمرأة (ayn)؛ السوأة العورة والفاحشة (sihah)؛ السوء فرج الرجل والمرأة والسوءة كل عمل وأمر شائن (tahdhib)؛ كني عن الفرج بالسوأة (mufradat)
- **B005** yaptığını ayıplayıp kötüleme — ayıplama ve kötü yaptığını söyleme · yaptığı işi yüzüne karşı ayıplayıp kötüledi
  سوأت عليه ما صنع تسوئة وتسويئا إذا عبته عليه وقلت له أسأت (sihah)؛ ما صنع تسوئة وتسويئا إذا عبت ما صنع (tahdhib)
- **B006** ne kötü! — ne kötü; pek kötü · yaptıkları ne kötü · ne kötü bir örnek
  فساء هاهنا تجري مجرى بئس (mufradat)

## د خ ل (root_000464): 64:9 وَيُدْخِلْهُ

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

## ج ن ن (root_000266): 64:9 جَنَّٰتٍ

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

## ج ر ي (root_000240): 64:9 تَجْرِى

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

## ت ح ت (root_000177): 64:9 تَحْتِهَا

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ن ه ر (root_001559): 64:9 ٱلْأَنْهَٰرُ

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

## خ ل د (root_000429): 64:9 خَٰلِدِينَ, 64:10 خَٰلِدِينَ

- **B001** kalıcı olma ve durumunu koruma — kalmak; varlığını sürdürmek · kalıcılık; bulunduğu durumda kalma · kalıcılık; kalıcı yaşam yurdu · sonsuz yaşam bahçesi · ölümden sonraki kalıcı yaşam yurdu · kalıcı kılmak; kalacağına hükmetmek · yaşlandığı halde saçına ak düşmeyen · ön kesici dişleri, yan kesici dişleri çıkana kadar düşmeyen hayvan · yıkıntılar yok olduktan sonra kalan ocak taşları ve kayalar
  أصل واحد يدل على الثبات والملازمة (maqayis)؛ الخلود البقاء فيها (ayn)؛ دوام البقاء (jamhara;sihah)؛ دار الخلود والخلد الآخرة والجنة (jamhara)؛ بقاؤه على الحالة التي هو عليها (mufradat)؛ مخلد إذا أبطأ عنه الشيب (maqayis;jamhara;sihah;mufradat)؛ خوالد للأثافي والحجارة لطول مكثها (ayn;sihah;mufradat)
- **B002** yönelip bağlanma, yapışma ya da ayrılmadan kalma [kalıp] — yere yapışmak veya ona bağlanmak · ona yönelmek ve ondan hoşnut olmak · o yerde kalmak · arkadaşının yanından ayrılmamak
  أخلد إلى الأرض إذا لصق بها (maqayis;jamhara)؛ أخلد إلى كذا أي ركن إليه ورضي به (ayn)؛ أخلدت إلى فلان أي ركنت إليه (sihah)؛ أخلد بالمكان أقام به وأخلد بصاحبه لزمه (sihah)؛ ركن إليها ظانا أنه يخلد فيها (mufradat)
- **B003** küpe; küpe veya bilezikle süslenmiş olma — küpe; bir tür kulak süsü
  ولدان مخلدون مقرطون (ayn;mufradat)؛ من الخلد والخلد جمع خلدة وهي القرط (maqayis)؛ مقرطون مشنفون (maqayis)؛ مسورون لغة يمانية (jamhara)
- **B004** akıl ve akla gelen düşünce — akıl; zihinde yer eden düşünce · aklıma geldi
  الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت (maqayis)؛ ما يقع ذلك في خلدي (ayn)؛ وقع ذلك في خلدي أي في قلبي (jamhara)؛ وقع ذلك في خلدي أي في ورعي وقلبي (sihah)
- **B005** gözsüz faremsi küçük hayvan — gözleri olmayan, fareye veya sıçana benzeyen küçük hayvan
  الخلد ضرب من الجرذان عمي لم يخلق لها عيون (ayn)؛ الخلد دويبة تشبه الفأرة (jamhara)؛ ضرب من الجرذان أعمى (sihah)

## ء ب د (root_000004): 64:9 أَبَدًا

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

## ف و ز (root_001186): 64:9 ٱلْفَوْزُ

- **B001** iyiliğe erişip kötülükten kurtulma — iyiliğe erişip kötülükten kurtulma · kurtulup iyiliğe erişmek · kurtulup iyiliğe erişen kimse · bir şeyi ele geçirip onunla uzaklaşmak · Tanrı'nın ona bir şeyi alıp götürtmesi · kumarda kura payının sahibine çıkması
  الفوز الظفر بالخير والنجاة من الشر (ayn;sihah;tahdhib;mufradat)؛ فاز بالأمر إذا ذهب به وخلص (maqayis;sihah)؛ إذا خرج قدح قوم في القمار قيل قد فاز (ayn;tahdhib)
- **B002** ölüp dünyadan ayrılma — ölmek, yaşamını yitirmek
  فوز الرجل إذا مات (maqayis;sihah;tahdhib)؛ فوز الرجل إذا هلك (mufradat)؛ صار في مفازة بين الدنيا والآخرة (ayn;tahdhib)
- **B003** kurtuluş; susuz ve tehlikeli ıssız çöl — susuz çöle girip orada yol almak · cezadan kurtuluş · susuz, ölüm tehlikesi taşıyan ıssız çöl · kurtuluş veya kurtuluş yeri
  المفازة المنجاة (maqayis;ayn;sihah;tahdhib)؛ المفازة الفلاة التي لا ماء فيها (tahdhib)؛ سميت مفازة تفاؤلا بالسلامة والفوز (maqayis;sihah;mufradat)؛ سميت من فوز إذا هلك (maqayis;sihah;mufradat)؛ فوز الرجل تفويزا ركب المفازة ومضى فيها (ayn;tahdhib)
- **B004** askerî konak yerinde kurulan yapı veya direkli gölgelik — askerî konak yerinde kurulan yapı veya direkli gölgelik
  الفازة من أبنية الحزق وغيرها تبنى في العساكر (ayn;tahdhib)؛ الفازة مظلة تمد بعمود (sihah)

## ع ظ م (root_001029): 64:9 ٱلْعَظِيمُ, 64:15 عَظِيمٌ

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

## ك ذ ب (root_001290): 64:10 وَكَذَّبُوا۟

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

## ء ي ي (root_000074): 64:10 بِـَٔايَٰتِنَآ

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

## ص ح ب (root_000844): 64:10 أَصْحَٰبُ

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

## ب ء س (root_000079): 64:10 وَبِئْسَ

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

## ص و ب (root_000889): 64:11 أَصَابَ, 64:11 مُّصِيبَةٍ

- **B001** yukarıdan inip yerleşen yağış — yağmur veya yağmurun yukarıdan inmesi · yağmur taşıyan bulut veya yağmur · yağmurun bir yere inmesi
  الصوب المطر؛ الصيب سحاب ذو صوب؛ صاب الغيث بمكان كذا (ayn)؛ الصوب نزول المطر؛ الصيب السحاب دون الصوب؛ صاب أي نزل (sihah)؛ الصيب في اللغة المطر؛ كل نازل من علو إلى استفال فقد صاب يصوب؛ الصوب المطر؛ الصيب سحاب ذو صوب (tahdhib)؛ جعل الصوب لنزول المطر؛ الصيب السحاب المختص بالصوب؛ قيل هو السحاب وقيل هو المطر (mufradat)؛ أصل صحيح يدل على نزول شيء واستقراره قراره؛ الصوب وهو نزول المطر؛ الصيب السحاب ذو الصوب (maqayis)
- **B002** yanlışa karşı doğru olan — yanlışın karşıtı olan doğru ve uygun şey · ona doğru yaptın demek · bir davranışı doğru saymak · doğru sonuca yönelmek veya onu bulmak · işin tam yerine oturması
  الصواب نقيض الخطأ (ayn)؛ خطئي وصوبي أي صوابي؛ الصواب نقيض الخطأ؛ صوبه أي قال له أصبت؛ استصوب فعله واستصاب فعله (sihah)؛ الصواب نقيض الخطأ؛ أصاب فلان الصواب فأخطأ الجواب (tahdhib)؛ الصواب يقال على وجهين؛ في نفسه محمودا ومرضيا؛ باعتبار القاصد إذا أدرك المقصود؛ الصواب التام (mufradat)؛ الصواب في القول والفعل؛ خلاف الخطأ؛ قد صابت بقر (maqayis)
- **B003** hedefe yönelip varma — okun hedefe yönelmesi veya hedefe varması · hedefe yönelen ok · arananı bulmak veya hedeflenene ulaşmak · yönünü koru · yönünden sapmayan
  صاب السهم نحو الرمية يصوب صيبوبة إذا قصد؛ سهم صائب أي قاصد؛ أقم صوبك أي قصدك؛ مستقيم الصوب إذا لم يزغ عن قصده (ayn)؛ صاب السهم يصوب صيبوبة أي قصد ولم يجر؛ صاب السهم القرطاس؛ أصابه أي وجده (sihah)؛ صاب إذا أصاب؛ صاب السهم نحو الرمية يصوب صيبوبة إذا قصد؛ صاب السهم الرمية يصوبها وأصابها إذا قصدها؛ حيث أراد أنه يصيب (tahdhib)؛ أصاب كذا أي وجد ما طلب؛ أصاب السهم إذا وصل إلى المرمى بالصواب (mufradat)
- **B004** başına gelen kötü olay — kişinin başına gelen kötü olay veya sıkıntı · başına kötü olay gelmek · kötü olaydan etkilenmiş ya da aklı bozulmuş kişi · akılda hafif bozulma
  أصابته مصيبة أي أخذته فهو مصاب؛ في عقله صابة أي فيه طرف من الجنون (sihah)؛ مصيبة كانت في الأصل مصوبة؛ مصائب؛ في عقل فلان صابة؛ يقال للمجنون مصاب (tahdhib)؛ المصيبة أصلها في الرمية ثم اختصت بالنائبة؛ أصاب جاء في الخير والشر؛ الإصابة في الخير اعتبارا بالصوب وفي الشر اعتبارا بإصابة السهم (mufradat)
- **B005** aşağı eğme — aşağı doğru eğimli oluş · kabı veya tahta ucunu aşağı indirmek · başı aşağı eğme · atı koşuya salmak
  التصوب حدب في حدور؛ صوبت الإناء ورأس الخشبة إذا خفضته؛ كره تصويب الرأس في الصلاة (ayn)؛ التصوب مثله؛ صوبت الفرس إذا أرسلته في الجري؛ صوب رأسه أي خفضه (sihah)؛ التصوب حدب في حدور؛ صوبت الإناء ورأس الخشبة تصويبا إذا خفضته؛ كره تصويب الرأس في الصلاة (tahdhib)؛ التصويب حدب في حدور لا يكون إلا كذا (maqayis)
- **B006** saf seçkin öz — her şeyin seçkin kısmı · topluluğun saf soyu ve iç özü
  الصياب الخيار من كل شيء؛ الصياب والصيابة أصل كل قوم؛ من صميم النوب (ayn)؛ قوم صياب أي خيار؛ صيابة قومه وصوابة قومه أي في صميم قومه؛ الصيابة الخيار من كل شيء (sihah)؛ من صيابة قومه أي من مصاصهم وأخلصهم نسبا؛ من صوابة قومه مثله (tahdhib)؛ الصيابة فالخيار من كل شيء؛ كأنه من الصوب وهو خالص ماء السحاب (maqayis)
- **B007** acı bitki özsuyu — acı ağaç veya bitki özsuyu
  الصاب عصارة شجرة مرة؛ يقال هو عصارة الصبر (ayn)؛ الصاب عصارة شجر مر (sihah)؛ الصاب والسلع ضربان من الشجر مران؛ الصاب عصارة شجر مر (tahdhib)
- **B008** dökülüp oluşan yığın — toprak yığını, hurma yeri veya dökülmüş şey
  أهل الفلج يسمون الجرين الصوبة وهو موضع التمر؛ الدنانير صوبة أي مهيلة (sihah)؛ الصوبة الكثبة من تراب أو غيره (tahdhib)
- **B009** yana sapma — yana eğilmek veya sapmak · kötülükten uzaklaşıp ayrılmak
  صاف عن الشر إذا عدل؛ من باب الإبدال؛ يقال صاب إذا مال؛ وقد ذكر في بابه (maqayis)

## ECHO ن ص ب (root_001507): for 64:11 أَصَابَ, 64:11 مُّصِيبَةٍ: withheld observed target; not identity

- **B001** dikme, dik durma ve yükselme — bir şeyi dikmek veya dik konuma kaldırmak · boynuzları dik olan · boynuzu dik veya göğsü yüksek dişi hayvan · havaya yükselmiş toz · perdeyi kaldırmak · kuş avlamak için tuzak kurmak · kazanın üzerine konduğu demir destek · dikili direk veya sütun
  أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)
- **B002** tapınma veya adak kesme taşı — tapınılan veya üzerinde adak kesilen dikili taş · tapınılan ya da adak kesilen dikili taşlar
  النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)
- **B003** sınır işareti veya kuyu-havuz taşı — dikili işaret veya havuz kenarı taşı · kuyu ya da havuz ağzının çevresine dizilen taşlar · taşlardan kurulmuş havuz · topluluk veya sınır için dikilmiş işaret
  النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)
- **B004** yorgunluk ve yıpratıcı sıkıntı — yorgunluk, bitkinlik, zahmet ve sıkıntı · hastalığın verdiği bitkinlik · beni yordu ve huzursuz etti · yorucu veya yorgunluk içindeki
  النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)
- **B005** belirlenmiş pay — pay veya bir şeyden ayrılan belirli bölüm · pay
  النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)
- **B006** temel veya sabit başvuru noktası — bir şeyin temeli ve dönülen başvuru noktası · bıçağın sapı veya arka bölümü · mal için mali yükümlülük doğuran alt miktar · köken, soy ve aileden gelen saygınlık · güneşin battığı ve döndüğü yer
  نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)
- **B007** dil bilgisinde yükleme konumu [kalıp] — çekimde üst konumun karşıtı olan yükleme konumu · yükleme konumuna getirilmiş sözcük
  في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)
- **B008** birine savaş veya düşmanlıkla karşı çıkma — birine savaş veya düşmanlıkla karşı çıkmak · ona düşman olmak veya düşmanlık yöneltmek
  ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)
- **B009** özel bir şarkı veya ezgi türü — yolcuların söylediği özel ezgi türü · hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi · yolcu ezgisini söyledi
  النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)
- **B010** yolculuğu yumuşak sürdürme veya artırma — gün boyunca yumuşak biçimde ilerlediler · yol alışlarını yükseltip artırdılar
  نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)

## ء ذ ن (root_000022): 64:11 بِإِذْنِ

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

## ق ل ب (root_001248): 64:11 قَلْبَهُۥ

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

## ط و ع (root_000956): 64:12 وَأَطِيعُوا۟, 64:12 وَأَطِيعُوا۟, 64:16 ٱسْتَطَعْتُمْ, 64:16 وَأَطِيعُوا۟

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

## ECHO س ط ع (root_000706): for 64:12 وَأَطِيعُوا۟, 64:12 وَأَطِيعُوا۟, 64:16 ٱسْتَطَعْتُمْ, 64:16 وَأَطِيعُوا۟: withheld observed target; not identity

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

## ب ل غ (root_000151): 64:12 ٱلْبَلَٰغُ

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

## و ك ل (root_001681): 64:13 فَلْيَتَوَكَّلِ

- **B001** bir işi başkasına devredip onu kendi adına yetkilendirme — onu birine bırakıp işini ona devretmek · belirli bir iş için onu yetkili kılmak · bir başkasını kendi adına yetkilendirme · temsil görevi; başkasının işini yürütme · kendisine iş devredilen yetkili temsilci · iş onun kararına bırakılmıştır · beni onlarla baş başa bırak
  وكلته إليك أكله كلة أي فوضته (ayn)؛ سمي الوكيل لأنه يوكل إليه الأمر (maqayis)؛ وكلته بأمر كذا توكيلا والاسم الوكالة (sihah)؛ وكيل الرجل الذي يقوم بأمره (tahdhib)؛ التوكيل أن تعتمد على غيرك وتجعله نائبا عنك (mufradat)
- **B002** kendi yetersizliğini kabul edip başkasına dayanarak güvenme — Tanrı'ya güvenmek ve onun koruyup yeteceğine inanmak · birine dayanıp güvenmek · Tanrı'ya dayanıp onu yeterli görmek · birine dayanıp güvenmek
  التوكل منه وهو إظهار العجز في الأمر والاعتماد على غيرك (maqayis)؛ وكلت بالله وتوكلت على الله (ayn)؛ التوكل إظهار العجز والاعتماد على غيرك (sihah)؛ قد اتكل فلان عليك (tahdhib)؛ توكلت عليه بمعنى اعتمدته (mufradat)
- **B003** güçsüzlüğü yüzünden işini başkasına bırakıp aksatan kişi — güçsüz, etkisiz ve işini başkasına bırakan kişi · işini insanlara bırakıp başkasına dayanan kişi · işinde sürekli başkasına dayanan kişi · başkasına dayanıp işini aksatan veya çevik olmayan kişi · işini başkasına güvenerek savsaklamak
  الوَكَلَة والوَكَل الرجل الضعيف (maqayis)؛ رجل وكل ووكلة وهو المواكل يتكل على غيره فيضيع أمره (ayn)؛ رجل وكل ووكلة وتكلة أي عاجز يكل أمره إلى غيره (sihah)؛ رجل وكل إذا كان ضعيفا ليس بنافذ (tahdhib)؛ رجل وكلة تكلة إذا اعتمد غيره في أمره (mufradat)
- **B004** tarafların işte karşılıklı olarak birbirine dayanması — birine dayanmak, onun da sana dayanması · topluluktaki herkesin işi birbirine bırakması
  واكلت الرجل إذا اتكلت عليه واتكل عليك (maqayis)؛ واكلت فلانا مواكلة إذا اتكلت عليه واتكل هو عليك (sihah)؛ تواكل القوم إذا اتكل كل على الآخر (mufradat)
- **B005** hayvanın geride kalarak veya eşine dayanarak kötü yürümesi — hayvanın geride kalması ya da ancak öteki hayvanlarla yürümesi · hayvanın kötü yürümesi · koşuda eşine dayanıp dürtülmeye ihtiyaç duyan at · koşuda eşine dayanarak giden at · kalkışında ve yürüyüşünde yavaşlamak
  الوكال في الدابة أن يتأخر أبدا خلف الدواب (maqayis)؛ الوكال في الدابة أن تحب التأخر خلف الدواب (ayn)؛ فرس واكل يتكل على صاحبه في العدو (sihah)؛ واكلت الدابة وكالا إذا أساءت السير (tahdhib)؛ الوكال في الدابة أن لا يمشي إلا بمشي غيره (mufradat)
- **B006** kendisine bırakılan işi üstlenip koruyan yeterli görevli — birinin işini üstlenip yürütmek · işi üstlenen, koruyan, yeterli olan ve güvence veren görevli · deve sahibi
  سمي الوكيل لأنه يوكل إليه الأمر (maqayis)؛ الوكيل كافينا والكافي والحافظ والكفيل والذي توكل بالقيام بجميع ما خلق (tahdhib)؛ الوكيل فعيل بمعنى المفعول واكتف به أن يتولى أمرك وحافظ لهم والكفيل (mufradat)

## ز و ج (root_000652): 64:14 أَزْوَٰجِكُمْ

- **B001** eş; çift veya çiftin her bir üyesi — eş; çift veya çiftin her bir üyesi · birbirine bağlı iki öğe; bir çift · eşler; çiftler
  أصل يدل على مقارنة شيء لشيء (maqayis)؛ زوجان من الحمام أي ذكر وأنثى (ayn)؛ كل اثنين زوج والزوج ضد الفرد (jamhara)؛ الزوج خلاف الفرد وكل واحد منهما يسمى زوجا (sihah)؛ كل شيء اقترن أحدهما بالآخر فهما زوجان (tahdhib)؛ لكل قرينين زوج ولكل ما يقترن بآخر مماثلا له أو مضادا زوج (mufradat)
- **B002** eş; evlilikteki kadın veya erkek — evlilikteki kadın veya erkek eş · kadın eş · evlilikteki eşler
  الزوج زوج المرأة والمرأة زوج بعلها (maqayis)؛ زوج المرأة والمرأة زوج الرجل (jamhara)؛ زوج المرأة بعلها وزوج الرجل امرأته (sihah)؛ الرجل زوج المرأة والمرأة زوج الرجل وزوجته (tahdhib)؛ وزوجك الجنة وزوجة لغة رديئة (mufradat)
- **B003** eş kılmak, eş edinmek veya eşleştirmek — birine bir kadın eş sağlamak · bir kadınla evlenmek · bir kadınla evlenmek; belirli bir ağızda kullanılan kuruluş · eşleşme ve çift oluşturma · eşleştirme ve birbirine eş kılma · eşleşme ve çift oluşturma · kuşların birbiriyle eşleşmesi · eşleşmiş; bir eşi bulunan · onları eşleriyle bir araya getirmek · onları erkekler ve dişiler olarak eşleştirmek veya sınıflandırmak · kadının erkeği kendine eş edinmesi
  زوجته امرأة وتزوجت امرأة (sihah;tahdhib)؛ زوجناهم بحور عين أي قرناهم بهن (sihah;mufradat)؛ معنى يزوجهم يقرنهم وكل شيء اقترن أحدهما بالآخر فهما زوجان (tahdhib)
- **B004** tür, sınıf veya renk çeşidi — türler ve sınıflar · renk, tür veya sınıf · bir kumaş rengi · güzel bir bitki türü · çeşitli ve benzer bitki türleri · onları erkekler ve dişiler olarak eşleştirmek veya sınıflandırmak
  من كل زوج بهيج أراد به اللون (maqayis)؛ زوج من الثياب أي لون ومنها من كل زوج بهيج أي لون (ayn)؛ من كل ضرب من النبات حسن والزوج اللون وأزواج أي أنواع والزوج الصنف (tahdhib)؛ أزواجا من نبات شتى أي أنواعا متشابهة وثمانية أزواج أي أصناف (mufradat)
- **B005** benzerler ve aynı tutumu izleyen yoldaşlar — benzerler, denkler ve aynı tutumu izleyen yoldaşlar
  أزواجهم أي قرناءهم (sihah)؛ أزواجهم معناه نظراءهم ضرباءهم وعندي من هذا أزواج أي أمثال (tahdhib)؛ أزواجهم أي أقرانهم المقتدين بهم في أفعالهم وأشباها وأقرانا (mufradat)
- **B006** kapalı yolcu oturağına serilen desenli örtü — deve üzerindeki kapalı yolcu oturağına serilen desenli örtü
  النمط الذي يطرح على الهودج زوج لأنه زوج لما يلقى عليه (maqayis)؛ الزوج النمط يطرح على الهودج (jamhara;sihah;tahdhib)

## و ل د (root_001683): 64:14 وَأَوْلَٰدِكُمْ, 64:15 وَأَوْلَٰدُكُمْ

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

## ع د و (root_000993): 64:14 عَدُوًّا

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

## ECHO ع د د (root_000989): for 64:14 عَدُوًّا: withheld observed target; not identity

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

## ECHO ع و د (root_001058): for 64:14 عَدُوًّا: withheld observed target; not identity

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

## ح ذ ر (root_000301): 64:14 فَٱحْذَرُوهُمْ

- **B001** uyanıkça sakınma — bir şeyden sakınıp korkmak · sakınma ve uyanıklık · uyanık ve sakıngan · çok sakıngan ve uyanık · çok ürkek ve sakıngan · korkanlar · ürküntü
  الحذر من التحرز والتيقظ (maqayis)؛ الحذر مصدر حذرت أحذر حذرا (ayn;tahdhib)؛ الحذر والحذر التحرز ورجل حذر (sihah)؛ الحذر احتراز من مخيف (mufradat)؛ حذرون خائفون والمحذورة الفزع ورجل حذريان (maqayis;sihah;tahdhib)
- **B002** uyarıp sakındırma — korkutup sakındırma · onu sakındırdı ve uyardı · sakın! · seni ona karşı uyarıyorum
  حذار بمعنى احذر (maqayis;sihah;mufradat)؛ حذار يا فلان أي احذر (ayn;tahdhib)؛ التحذير التخويف (sihah)؛ أنا حذيرك منه أي أحذركه (ayn;tahdhib)؛ حذرته (mufradat)
- **B003** tehlikeye karşı hazırlıklı ve donanımlı olma — hazırlıklı olanlar · hazırlıklı ve silahlı kimse · korunma araçlarınızı yanınıza alın
  حاذرون متأهبون (maqayis;sihah)؛ حاذرون أي مستعدون (ayn;tahdhib)؛ مؤذون ذوو أداة من السلاح والحاذر الشاك في السلاح (tahdhib)؛ خذوا حذركم أي ما فيه الحذر من السلاح وغيره (mufradat)
- **B004** sert ve kaba yapılı arazi parçası — sert ve kaba yapılı yer parçası
  الحذرية المكان الغليظ (maqayis)؛ الحذرية قطعة من الأرض غليظة (sihah)؛ الحذرية من الأرض الخشنة والأرض الغليظة وأعلى الجبل إذا كان صلبا غليظا مستويا (tahdhib)
- **B005** göze kaçan yabancı maddeden doğan ağırlık [kalıp] — göze kaçan yabancı maddeden doğan ağırlık
  في العين الحذر وهو ثقل فيها من قذى يصيبها (tahdhib)
- **B006** horozun kabarttığı tüy demeti [kalıp] — horozun kabarttığı tüy demeti
  نفش الديك حذريته أي عفريته (sihah)

## ع ف و (root_001032): 64:14 تَعْفُوا۟

- **B001** hak edilmiş cezadan vazgeçip suçu silme — cezadan vazgeçip suçu silme · suçu yüzünden cezalandırmamak · Tanrı'nın kulunu cezalandırmayıp suçunu silmesi
  عفو الله تعالى عن خلقه وذلك تركه إياهم فلا يعاقبهم (maqayis)؛ العفو تركك إنسانا استوجب عقوبة (ayn)؛ عفوت عن ذنبه إذا تركته ولم تعاقبه (sihah)؛ محو الله ذنوب عبده عنه (tahdhib)؛ عفوت عنه قصدت إزالة ذنبه (mufradat)
- **B002** kötülüğü uzaklaştırıp esenlik sağlama — kötülüklerden korunma ve esenlik · Tanrı'nın kişiyi kötülükten koruyup esen kılması · Tanrı'nın kişiyi başkalarının zararından, başkalarını da onun zararından koruması
  العافية دفاع الله تعالى عن العبد (maqayis;ayn)؛ عافاه الله من سقم أو بلية (tahdhib)؛ عافاه الله وأعفاه بمعنى والاسم العافية (sihah)؛ أسألك العفو والعافية أي ترك العقوبة والسلامة (mufradat)
- **B003** zahmetsiz seçkin artığı verme veya alacaktan vazgeçme — kolay elde edilen artan ve seçkin mal · giderden artan veya zahmetsizce gelen mal · istenmeden ve yük oluşturmadan mal vermek · kendisine borçlu olunan hakkı karşılıksız bırakmak · yüklenen bir işten bağışık tutulmayı isteme
  العفو أحل المال وأطيبه (ayn;tahdhib)؛ عفو المال ما يفضل عن النفقة (sihah)؛ العفو الفضل الذي يجيء بغير كلفة (tahdhib)؛ ما يسهل قصده وتناوله (mufradat)؛ أعطيته المال عفوا أي عن غير مسألة (maqayis;tahdhib)؛ عفوت له عما لي عليه إذا تركته له (tahdhib)
- **B004** birine yönelip iyilik veya geçimlik arama — iyilik ve fazlalık isteyenler · birinden iyilik ve fazlalık istemek · yiyecek arayan insanlar, hayvanlar ve kuşlar
  العفاة طلاب المعروف وهم المعتفون (maqayis;ayn)؛ اعتفيت فلانا طلبت معروفه (maqayis;ayn)؛ العافية كل طالب رزق (sihah;tahdhib;mufradat)؛ العفو القصد لتناول الشيء (mufradat)
- **B005** kullanım izi taşımayan yer veya su [kalıp] — ayak basılmamış ve sahiplenilmemiş toprak · uğranıp bulandırılmamış veya çekişmeden alınabilen su · daha önce kimsenin dokunmadığı yemek
  العفو المكان الذي لم يوطأ (maqayis)؛ أرض عفو ليس فيها أثر (maqayis)؛ العفو الأرض الغفل التي لم توطأ (sihah)؛ عفو البلاد ما لا أثر لأحد فيها بملك (tahdhib)؛ عفا الماء أي لم يطأه شيء يكدره (maqayis)
- **B006** aşınıp silinerek iz bırakmama — toprak, harap oluş ve izlerin kaybolması · rüzgârın yapının izlerini silmesi · izi silinsin diye edilen kötü dilek
  العفاء التراب والدروس (ayn;tahdhib)؛ العفاء الدروس والهلاك (sihah)؛ عفت الريح المنزل درسته (sihah)؛ عفت الرياح الآثار إذا درستها ومحتها (tahdhib)؛ عفت الدار كأنها قصدت البلى (mufradat)
- **B007** büyüyüp çoğalma veya bir ölçüde başkasını aşma — saçın bırakıldıkça uzayıp çoğalması · sakalı kesmeyip gürleşmeye bırakma · gür ve sık tüy ya da telek · bitkinin veya ağacın büyüyüp çoğalması ve yeri örtmesi · bilgi veya vermede birini aşmak · devenin sırtını binmeden dinlendirip etlenmesini ve yarasının iyileşmesini sağlamak
  عفا الشعر وغيره إذا كثر (sihah;tahdhib)؛ حتى عفوا أي نموا وكثروا (maqayis;sihah;tahdhib)؛ العفاء ما كثر من الريش والوبر (ayn;sihah;tahdhib;mufradat)؛ عفا النبت والشجر قصد تناول الزيادة (mufradat)؛ عفا فلان على فلان في العلم إذا زاد عليه (tahdhib)
- **B008** biçime bağlı adlandırmalar — genç eşek yavrusu, sıpa · dişi eşek yavrusu veya genç eşek yavruları topluluğu · devenin sırtını binmeden dinlendirip etlenmesini ve yarasının iyileşmesini sağlamak
  العفو ولد الحمار والأنثى عفوة والجمع عفاء (maqayis;ayn)؛ العفو والعفا الجحش والأنثى عفوة (sihah)؛ الأعفاء أولاد الحمير (tahdhib)
- **B009** seçkin yiyecek payı veya tencereye geri konan et suyu — yemekten veya et suyundan ayrılıp değer verilen kişiye sunulan pay · yemeğin veya içeceğin en seçkin bölümü · ödünç tencere geri verilirken içinde bırakılan veya geri konan et suyu
  العفاوة شيء يرفع من الطعام (maqayis)؛ عفوة الطعام والشراب خياره (sihah;tahdhib)؛ العافي ما يرده مستعير القدر من المرق (sihah;tahdhib;mufradat)؛ عافي القدر الذي يرده المستعير للقدر (maqayis)

## ص ف ح (root_000867): 64:14 وَتَصْفَحُوا۟

- **B001** enine yüz, geniş yassı parça ve enli kılma — en, yan veya yan yüz · insanın ya da hayvanın böğrünün enli yanı · yüzün yanı · kılıcın yassı yüzü · kılıcın enli yüzü · dağın yamacı veya yanı · dağın yamacı veya yanı · enli yassı parça, geniş taş veya geniş kılıç · geniş yassı parçalar veya levhalar · geniş ve yassı taşlar · yüz derisi · geniş veya hafifçe uzamış baş · geniş göğüs · bir şeyi enli duruma getirme · hörgüçleri enine geniş develer
  الصفح الجنب من كل شيء وصفحتا السيف وجهاه وكل حجر عريض أو خشبة أو لوح أو حديدة أو سيف له طول وعرض فهو صفيحة (ayn)؛ صفحة الإنسان والدابة عرض جنبه والصفيحة النصل العريض من السيوف والقطعة من الصخر العريضة ورأس مصفح (jamhara)؛ صفحة كل شيء جانبه وصفح الجبل مضطجعه وصفائح الباب ألواحه وتصفيح الشيء جعله عريضا (sihah)؛ صفح الشيء عرضه وجانبه كصفحة الوجه وصفحة السيف وصفحة الحجر (mufradat)؛ صفح الشيء عرضه والصفيحة كل سيف عريض وكل حجر عريض صفيحة (maqayis)؛ سفح الجبل من باب الإبدال والأصل فيه صفح (maqayis)
- **B002** başa kakmadan bağışlayıp yüz çevirme — başa kakmadan bağışlama · kusurunu bağışlayıp ondan yüz çevirmek · ondan yüz çevirip onu bırakmak · bir şeyi bırakıp ondan yüz çevirmek · başa kakmadan güzelce bağışlama
  صفحت عنه أي عفوت عنه (ayn)؛ صفحت عن الرجل إذا عفوت عن جرمه وأضربت عن هذا الأمر صفحا إذا تركته (jamhara)؛ صفحت عن فلان إذا أعرضت عن ذنبه وقد ضربت عنه صفحا إذا أعرضت عنه وتركته (sihah)؛ الصفح ترك التثريب وهو أبلغ من العفو (mufradat)؛ صفح عنه وذلك إعراضه عن ذنبه (maqayis)
- **B003** sayfa sayfa veya kişi kişi gözden geçirme — yazılı yaprakları çevirmek · topluluğu kişi kişi gözden geçirmek · sayfalarına veya aralarına bakarak incelemek
  صفحت ورق المصحف صفحا وصفحت القوم عرضتهم واحدا واحدا وتصفحتهم نظرت في خلالهم (ayn)؛ تصفحت الشيء إذا نظرت في صفحاته (sihah)؛ تصفحت الكتاب (mufradat)
- **B004** el sıkışma — el sıkışma · iki kişinin avuçlarını birbirine değdirerek el sıkışması
  المصافحة معروفة (ayn)؛ تصافح الرجلان بكفيهما إذا ألصق كل واحد منهما كفه بكف صاحبه (jamhara)؛ المصافحة الأخذ باليد والتصافح مثله (sihah)؛ المصافحة الإفضاء بصفحة اليد (mufradat)؛ المصافحة باليد كأنه ألصق يده بصفحة يد ذاك (maqayis)
- **B005** çekişmede kendini karşısındakine açık etmek [kalıp] — çekişmede kendini karşısındakine açık etmek
  أبدى فلان لي صفحته إذا أمكنك من نفسه في خصومة أو حرد
- **B006** bir yöne eğilmiş veya çevrilmiş olma — bir yöne eğilmiş veya çevrilmiş · gerçekten yüz çevirmiş iç yöneliş · gerçeğe yönelmiş veya ona bağlı iç yöneliş
  المصفح الممال وقلب المنافق مصفح أي ممال عن الحق (jamhara)؛ المصفح أيضا الممال وقلب المؤمن مصفح على الحق (sihah)
- **B007** kılıcın yassı yüzüyle vurma [kalıp] — kılıcın yassı yüzüyle vurmak · kılıcın keskin ağzıyla değil yassı yüzüyle vurmak
  ضربته بالسيف مصفحا ومصفوحا إذا ضربته بعرضه ولم تضربه بحده (jamhara)؛ ضربه بصفح السيف أي بعرضه وصفحته وأصفحته إذا ضربته بالسيف مصفحا أي بعرضه (sihah)
- **B008** el çırpma — el çırpma
  التصفيح التصفيق باليدين (jamhara)؛ التصفيح مثل التصفيق (sihah)
- **B009** istekte bulunanı geri çevirip vermemek [kalıp] — istekte bulunanı geri çevirip istediğini vermemek
  صفحت فلانا وأصفحته إذا سألك فرددته (sihah)؛ صفحت الرجل وأصفحته إذا سألك فمنعته وهو من أنك أريته صفحتك معرضا عنه (maqayis)
- **B010** develeri suluk boyunca geçirmek [kalıp] — develeri suluk boyunca geçirmek
  صفحت الإبل على الحوض إذا أمررتها (sihah)؛ صفحت الإبل على الحوض إذا أمررتها عليه وكأنك أريت الحوض صفحاتها وهي جنوبها (maqayis)
- **B011** talih oyunundaki altıncı ok — talih oyunundaki altıncı ok; başka bir adla da anılır
  المصفح أيضا السادس من سهام الميسر ويقال له المسبل أيضا
- **B012** bir erkeğe herhangi bir içecek verme [kalıp] — bir erkeğe herhangi bir içecek vermek
  مما شذ عن الباب قولهم صفحت الرجل صفحا إذا سقيته أي شراب كان

## غ ف ر (root_001096): 64:14 وَتَغْفِرُوا۟, 64:14 غَفُورٌ, 64:17 وَيَغْفِرْ

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

## ر ح م (root_000552): 64:14 رَّحِيمٌ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## م و ل (root_001457): 64:15 أَمْوَٰلُكُمْ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ف ت ن (root_001128): 64:15 فِتْنَةٌ

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

## ع ن د (root_001052): 64:15 عِندَهُۥٓ

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

## ء ج ر (root_000015): 64:15 أَجْرٌ

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## و ق ي (root_001677): 64:16 فَٱتَّقُوا۟, 64:16 يُوقَ

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

## س م ع (root_000741): 64:16 وَٱسْمَعُوا۟

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

## ن ف ق (root_001537): 64:16 وَأَنفِقُوا۟

- **B001** tükenip sona erme; özel kullanımlarda alıcı bulma, çabuk kesilme veya yüzeyden ayrılma — hayvan öldü · tükendi, sona erdi · fiyat veya satış canlandı, mal alıcı buldu · topluluğun pazarı canlandı, malları alıcı buldu · eşi bulunmayan kadına evlenme isteğiyle başvuranlar çoğaldı · koşusu çabuk kesilen at · kesintiye uğrayan gidiş · yaranın kabuğu soyuldu · develerin semirmeden dolayı tüyleri döküldü · insanlara söven kişi karşılığında sövgü görür ve onurunu diline düşürür
  نفقت الدابة نفوقا أي ماتت (maqayis;ayn;sihah;tahdhib;mufradat); نفق الشيء فني ونفد (maqayis;sihah;tahdhib;mufradat); نفق السعر أو البيع نفاقا وكثر مشتروه (maqayis;ayn;sihah;tahdhib;mufradat); فرس نفق الجري وسير نفق سريع الانقطاع (maqayis;sihah;tahdhib); نفق الجرح إذا انقشر وانتثرت الأوبار عن سمن (tahdhib)
- **B002** bir şeyi gider olarak elden çıkarma; özel kullanımda elindekini tüketip yoksullaşma — geçim için yapılan gider; harcanan şey · harcadı, elden çıkardı · adam malı tükenince yoksullaştı · çok harcayan kişi
  النَّفَقَة لأنها تمضي لوجهها (maqayis); النَّفَقَة ما أنفقت واستنفقت على العيال ونفسك (ayn;tahdhib); أنفقت الدرهم من النَّفَقَة ورجل منقاق كثير النَّفَقَة (sihah); الإنفاق قد يكون في المال وفي غيره واجبا وتطوعا (mufradat); أنفق الرجل افتقر وذهب ما عنده أو ماله (maqayis;sihah;tahdhib;mufradat)
- **B003** başka bir yere açılan yer altı geçidi ve kemirgen yuvasındaki gizli çıkış — çıkışı bulunan yer altı geçidi · kemirgen yuvasındaki inceltilmiş gizli çıkış · kemirgen yuvasındaki gizli çıkış · gizli çıkıştan dışarı çıktı · kemirgeni sıkıştırıp gizli çıkışından kaçırdık · kemirgen gizli çıkışına girdi
  النفق سرب في الأرض له مخلص إلى مكان (maqayis;ayn;sihah;tahdhib); النفق الطريق النافذ والسرب في الأرض النافذ فيه (mufradat); النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج (maqayis;ayn;sihah;tahdhib); بعضهم يسمي النافقاء النَّفَقَة (ayn;sihah;tahdhib)
- **B004** içindeki inanç veya tutumun tersini göstererek bağlı görünme — içindekinin tersini gösterme ve inançta ikiyüzlülük · içindekinden başkasını göstererek ikiyüzlü davrandı · içinde sakladığının tersini gösteren kimse
  النفاق لأن صاحبه يكتم خلاف ما يظهر (maqayis); النفاق الخلاف والكفر والفعل نافق نفاقا (ayn); ومنه اشتقاق المنافق في الدين (sihah); سمي المنافق منافقا للنفق وهو السرب في الأرض (tahdhib); النفاق الدخول في الشرع من باب والخروج عنه من باب (mufradat)

## خ ي ر (root_000452): 64:16 خَيْرًا

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

## ن ف س (root_001533): 64:16 لِّأَنفُسِكُمْ, 64:16 نَفْسِهِۦ

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

## ش ح ح (root_000778): 64:16 شُحَّ

- **B001** elde tutma hırsıyla cimrilik — elde tutma hırsıyla cimrilik · elde tutma hırsıyla cimrilik etmek · elde tutmaya aşırı düşkün ve cimri · elde tutmaya aşırı düşkün cimri kimseler · elde tutmaya aşırı düşkün cimri kimseler · elde tutmaya aşırı düşkün cimri kişi · pinti ve eli sıkı kişi · pinti ve eli sıkı kişi · pinti ve eli sıkı kişi
  الأصل فيه المنع ثم يكون منعا مع حرص (maqayis)؛ الشح البخل مع حرص (maqayis;sihah;mufradat)؛ الشح البخل وهو الحرص (ayn;tahdhib)؛ الشح والشح لغتان (jamhara)؛ رجل شحيح وقوم شحاح وأشحة (ayn;sihah;mufradat)؛ الشحشح البخيل الممسك (tahdhib)
- **B002** bir şeyi ya da kişiyi başkasına bırakmamakta direnme [kalıp] — iki kişinin bir şeyi birbirine kaptırmamak için yarışması · birini başkasına vermeye kıyamayıp esirgemek
  تشاح الرجلان على الأمر إذا أراد كل واحد منهما الفوز به ومنعه من صاحبه (maqayis)؛ يتشاحان على الأمر لا يريد كل واحد منهما أن يفوته (ayn;sihah;tahdhib)؛ فلان يشاح على فلان أي يضن به (sihah)
- **B003** ateş vermeyen çakmak taşı [kalıp] — ateş vermeyen çakmak taşı
  الزند الشحاح الذي لا يوري (maqayis;sihah)؛ زند شحاح أي لا يوري (ayn)؛ زند شحاح إذا كان لا يورى (tahdhib)
- **B004** ancak bol yağmurda su akıtan arazi [kalıp] — ancak çok yağmurda su akıtan arazi · ancak güçlü ve bol yağmurda su akıtan arazi
  أرض شحاح لا تسيل إلا من مطر كثير (sihah)؛ أرض شحاح لا تسيل إلا من مطر جود وأرض شحشح كذلك (tahdhib)
- **B005** bomboş, geniş ve çıplak kır [kalıp] — içinde hiçbir şey olmayan geniş ve çıplak kır
  فلاة شحشح لا شيء فيها (tahdhib)؛ الشحشح الفلاة الواسعة (tahdhib)؛ فلاة شحشح جرد (tahdhib)
- **B006** kararlılıkla sürdüren ve ilerleyen — bir işi kararlılıkla sürdüren ve onda ilerleyen · konuşmasını ustalıkla ve duraksamadan sürdüren konuşmacı · yolculukta kararlılıkla ilerleyen sürücü
  الشحشح المواظب على الشيء (maqayis;ayn;tahdhib)؛ الشحشح الماضي فيه (ayn;sihah)؛ الخطيب الماهر في خطبته الماضي فيها شحشح (ayn;tahdhib)؛ كل ماض في كلام أو سير فهو شحشح (tahdhib)؛ خطيب شحشح ماض في خطبته (mufradat)
- **B007** kıskançça koruyan ya da cesurca savunan kişi — kıskançça koruyan veya cesurca savunan kişi
  للغيور شحشح لأنه إذا غار منع وكذلك الشجاع وهو المانع ما وراء ظهره (maqayis)؛ الشحشح الرجل الغيور (ayn)؛ الشحشح الغيور والشجاع أيضا (sihah)؛ يقال للغيور شحشح (tahdhib)
- **B008** hayvana göre nitelenen ses çıkarma — devenin arı olmayan bir homurtu çıkarması · çok ses çıkaran kuzgun · örümcek kuşunun ötmesi
  شحشح البعير في الهدر وهو الذي ليس بالخالص من الهدر (ayn)؛ شحشح البعير في هديره وذلك إذا لم يكن خالصا (sihah;tahdhib)؛ من قولهم شحشح البعير في هديره (mufradat)؛ غراب شحشح كثير الصوت وشحشح الصرد إذا صات (tahdhib)
- **B009** hızlı ve hafif hareket — hızlı uçuş · hızlı bağırtlak kuşu · hafif ve çevik eşek
  الشحشحة الطيران السريع (sihah)؛ قطاة شحشح أي سريعة (sihah)؛ حمار شحشح خفيف (tahdhib)
- **B010** kötü huylu adam [kalıp] — kötü huylu adam
  رجل شحشح سيء الخلق (tahdhib)

## ف ل ح (root_001175): 64:16 ٱلْمُفْلِحُونَ

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

## ق ر ض (root_001217): 64:17 تُقْرِضُوا۟, 64:17 قَرْضًا

- **B001** dişle ya da küçük bir araçla kesmek — dişle ya da küçük bir kesme aracıyla kesme · bir şeyi kesip ondan parça ayırmak · küçük kesme aracı, makas · kesilerek düşen kırıntı veya artık · başka bir harfle düzeltilmiş, güvenilmez bir böcek uzvu ifadesi
  القرض القطع بالناب والمقراض الجلم الصغير (ayn)؛ قرضت الشئ قرضا قطعته (sihah)؛ أصل القرض في اللغة القطع ومنه أخذ المقراض (tahdhib)؛ القرض ضرب من القطع (mufradat)؛ أصل صحيح يدل على القطع يقال قرضت الشيء بالمقراض (maqayis)
- **B002** geçip bir yanda bırakmak — bir yeri geçip bir yanda bırakmak · güneşin onları geçip sol yanında bırakması
  قرضته يمنة ويسرة إذا عدلت عن شيء في سيرك أي تركته عن اليمين وعن الشمال (ayn)؛ تقرضهم ذات الشمال أي تخلفهم شمالا وتجاوزهم وتقطعهم وتتركهم عن شمالها (sihah)؛ تقرضهم ذات الشمال أي تجاوزهم وتتركهم عن شمالها؛ تعدل عنهم (tahdhib)؛ سمي قطع المكان وتجاوزه قرضا؛ تجوزهم وتدعهم إلى أحد الجانبين (mufradat)
- **B003** dengi ya da karşılığı beklenerek vermek — dengi geri verilecek mal veya karşılığı beklenen davranış · birine dengi geri verilmek üzere mal vermek · birinden borç istemek ya da borç almak · Tanrı katında karşılık bekleyerek bağış yapmak veya iyi iş işlemek · iyi ya da kötü, karşılığı beklenen davranış
  أقرضته قرضا وكل أمر يتجافاه الناس فيما بينهم فهو من القروض (ayn)؛ القرض ما تعطيه من المال لتقضاه؛ ما سلفت من إحسان ومن إساءة (sihah)؛ القرض اسم لكل ما يلتمس عليه الجزاء من صدقة أو عمل صالح؛ القرض في اللغة البلاء الحسن والبلاء السيء (tahdhib)؛ ما يدفع إلى الإنسان من المال بشرط رد بدله قرضا (mufradat)؛ القرض ما تعطيه الإنسان من مالك لتقضاه وكأنه شيء قد قطعته من مالك (maqayis)
- **B004** sermaye verip ticari kazancı paylaşmak — sermayeyi işletip kazancı paylaşmaya dayalı ticaret ortaklığı · birine işletmesi ve kazancı paylaşması için sermaye vermek
  المقارضة المضاربة؛ دفعت إليه مالا يتجر فيه ويكون الربح بينكما (sihah)؛ القراض في كلام أهل الحجاز المضاربة (tahdhib)؛ القراض في التجارة من هذا وكأن صاحب المال قد قطع من ماله طائفة وأعطاها مقارضة ليتجر فيها (maqayis)
- **B005** iyiliğe, kötülüğe ya da söze benzeriyle karşılık vermek — birine yaptığına veya söylediğine benzeriyle karşılık vermek · karşılıklı iyilik, kötülük ya da övgüde bulunmak · birini övmek ya da yermek
  قرضته قرضا وقارضته أي جازيته؛ فلان يقرض صاحبه إذا مدحه أو ذمه؛ يتقارضان الخير والشر (sihah)؛ هما يتقارضان الثناء والخير والشر أي يتجازيان؛ التقارض في الخير والشر (tahdhib)؛ يتقارضان الثناء إذا أثنى كل واحد منهما على صاحبه (maqayis)
- **B006** birinin onurunu çekiştirip karalamak [kalıp] — bir kişiyi veya onurunu çekiştirerek ve asılsız sözle karalamak
  اقترض مسلما أي نال منه وعابه وقطعه بالغيبة والبهتان؛ إذا اقترض رجل عرضك بكلام يسوءك ويحزنك
- **B007** şiir söylemek veya düzenlemek — şiir söylemek veya düzenlemek · şiir · boğucu sıkıntının şiire mi yoksa gevişe mi engel olduğunu tartışmalı bırakan söz
  القرض نطق الشعر والقريض الاسم كالقصيد (ayn)؛ القرض أيضا قول الشعر خاصة؛ الشعر قريض (sihah)؛ القرض أيضا قرض الشعر ولهذا سمي الشعر القريض (tahdhib)؛ القريض للشعر مستعار استعارة النسج والحوك (mufradat)؛ الظاهر أنه أريد به الشعر وهو أصح (maqayis)
- **B008** devenin gevişini çiğneyip geri göndermesi — boğucu sıkıntının gevişe mi yoksa şiire mi engel olduğunu tartışmalı bırakan söz · devenin gevişini çiğneyip işkembesine geri göndermesi · devenin geri getirip çiğnediği geviş parçası
  البعير يقرض جرته وهو مضغها والجرة المقروضة وهي القريض (ayn)؛ القريض أيضا ما يرده البعير من جرته وكذلك المقروض (sihah)؛ البعير يقرض جرته وهو مضغها وردها إلى الكرش والجرة المقروضة هي القريض (tahdhib)؛ يقولون القريض الجرة في قولهم حال الجريض دون القريض (maqayis)
- **B009** ölmek veya hiç kimse kalmadan tükenmek — ölmek, dünyadan ayrılmak · topluluğun hiç kimse kalmadan tükenmesi · ölümün eşiğine gelmek veya dünyayla bağını koparmak
  قرض فلان أي مات؛ انقرض القوم درجوا ولم يبق منهم أحد (sihah)؛ قرض إذا مات؛ يقال للرجل إذا مات قرض رباطه؛ جاء فلان وقد قرض رباطه إذا جاء مجهودا قد أشرف الموت (tahdhib)
- **B010** güvercin öldüren uzun sırtlı küçük hayvan adı — dört ayaklı, uzun sırtlı, güvercin öldüren küçük hayvan · bazı aktarımlarda erkek böceğe verilen ad
  ابن مقرض ذو القوائم الأربع طويل الظهر قتال للحمام (ayn)؛ ابن مقرض دويبة يقال لها بالفارسية دله وهو قتال الحمام (sihah)؛ ابن مقرض هو ذو القوائم الأربع الطويل الظهر القتال للحمام؛ من أسماء الخنفساء ويقال لذكرها المقرض (tahdhib)

## ض ع ف (root_000909): 64:17 يُضَٰعِفْهُ

- **B001** güçsüzlük — zayıflık, güçsüzlük · zayıflamak, güçten düşmek · zayıf veya güçsüz kimse · zayıflar, zayıf kimseler · zayıf kadınlar · zayıflatmak, güçsüz kılmak · zayıf bulmak veya saymak ve ezmek · zayıflıkla niteleme · yürüyüş onu zayıflattı · hafif yağmur almış arazi · aklı zayıf adam · gözü görmeyen kimse
  الضعف خلاف القوة (maqayis;ayn;sihah;mufradat)؛ الضعف في العقل والرأي والضعف في الجسد (ayn;tahdhib;mufradat)؛ الضعف قد يكون في النفس وفي البدن وفي الحال (mufradat)؛ أضعفته أي صيرته ضعيفا واستضعفته وجدته ضعيفا (ayn;sihah;tahdhib;mufradat)؛ أرض مضعفة أصابها مطر ضعيف (tahdhib)
- **B002** bir şeyi iki veya daha çok katına çıkarma — bir şeyi iki veya daha çok katına çıkarmak · bir katı veya ona eklenen eş miktar · iki katı · katları veya çoğaltılmış miktarları · iki kez veya iki katlık miktar · katlanmış veya bir eşi eklenmiş şey · bir topluluğa karşı sayıca iki kat olmak · topluluğa iki kat verilmek · halkaları ikişer örülmüş zırh · katlı veya katlanmış kumaşlar
  أضعفت الشيء وضعفته وضاعفته وهو أن يزاد على أصل الشيء فيجعل مثلين أو أكثر (maqayis;ayn;sihah;tahdhib;mufradat)؛ ضعف الشيء مثله وضعفاه مثلاه وأضعافه أمثاله (sihah;tahdhib;mufradat)؛ الضعف في الأصل زيادة غير محصورة (tahdhib)؛ المضاعفة الدرع نسجت حلقتين حلقتين والثياب المضعفة (maqayis;sihah;tahdhib)
- **B003** satır araları, kenar ve bedenin iç bölümleri — kitabın satır araları veya kenarı · bedenin kemikleri veya organları · bedenin iç boşluğu veya iç kısmı
  وقع في أضعاف كتابه أي في أثناء السطور أو الحاشية (sihah)؛ أضعاف الجسد عظامه وأعضاؤه والأضعاف الجوف (tahdhib)
- **B004** bineği zayıf adam [kalıp] — bineği zayıf adam
  أضعف الرجل ضعفت دابته (sihah)؛ الضعيف في بدنه والمضعف الذي دابته ضعيفة (tahdhib)
- **B005** mülkleri çok ve dağınık adam [kalıp] — mülkleri çok ve dağınık adam
  يقال للرجل إذا انتشرت ضيعته وكثرت أضعف الرجل فهو مضعف (tahdhib)

## ش ك ر (root_000810): 64:17 شَكُورٌ

- **B001** İyiliği tanıyıp söz ve davranışla karşılık verme — iyiliği tanıma, iyilik yapanı övme ve iyiliği görünür kılma · yaptığı iyilikten ötürü onu övdüm ve iyiliğini kabul ettim · ona karşı duyduğum gönül borcunu göstermeye çabaladım · iyiliği kabul edip karşılık verme; iyiliği yadsımanın karşıtı · iyiliği içten kavrayıp kabul etme · iyilik yapanı sözle övme · iyiliğin değerine uygun davranışla karşılık verme · Tanrı için, kullarının az iyiliğini değerli sayıp onları ödüllendiren · Tanrı'ya bağlı davranarak gördüğü iyiliğe karşılık vermeye çok çabalayan kul
  الشكر الثناء على الإنسان بمعروف يوليكه (maqayis)؛ الشكر عرفان الإحسان ونشره وحمد موليه (ayn;tahdhib)؛ الشكر الثناء على المحسن بما أولاك من المعروف (sihah)؛ الشكر تصور النعمة وإظهارها (mufradat)؛ شكر القلب وشكر اللسان وشكر سائر الجوارح (mufradat)
- **B002** azla yetinip belirgin biçimde gelişme — az yemle yetinip semiren hayvan · çok az yağışla bile geliştiği görülen bitki için söylenen örnek söz
  حقيقة الشكر الرضا باليسير (maqayis)؛ فرس شكور إذا كفاه لسمنه العلف القليل (maqayis)؛ الشكور من الدواب ما يسمن بالعلف اليسير ويكفيه (ayn)؛ الشكور من الدواب ما يكفيه العلف القليل (sihah;tahdhib)؛ دابة شكور مظهرة بسمنها إسداء صاحبها إليها (mufradat)؛ أشكر من بروقة (maqayis;mufradat)
- **B003** dolup bollaşma — otlayınca sütü bollaşan veya memesi sütle dolan sağmal hayvan · sağmalın sütü otlaktan sonra bollaştı veya memesi sütle doldu · topluluğun hayvanları otlayıp süt vermeye başladı · bol sütlü deve veya koyun sürüsü · sütle dolu meme · hayvanın sütünü artıran ot · yazın bol süt veren veya sütü yıl boyunca süren dişi deve · yağlı et parçası
  الأصل الثاني الامتلاء والغزر في الشيء (maqayis)؛ حلوبة شكرة إذا أصابت حظا من مرعى فغزرت (maqayis)؛ الشكرة من الحلوبات التي تصيب حظا من بقل أو مرعى فتغزر عليه بعد قلة اللبن (ayn;tahdhib)؛ اشتكر الضرع املا لبنا (sihah)؛ ناقة شكرة ممتلئة الضرع من اللبن (mufradat)؛ الفدرة من اللحم إذا كانت سمينة شكرى (tahdhib)
- **B004** körpe sürgün ve ona benzetilen yeni oluşum — ağacın gövdesinden veya dibinden çıkan körpe sürgün · örgülerin arasından yeni çıkan saç · yavru kuşun ince tüyü · taze sürgünlere benzetilen küçük çocuklar veya genç kuşak · ağaç körpe sürgün çıkardı veya dalları çoğaldı · ağaçta körpe bir sürgün çıktı · yeni çıkan saçların veya bitki sürgünlerinin bütünü · belirli bir bitki türü
  الأصل الثالث الشكير من النبات (maqayis)؛ الشكير من النبات ما ينبت من ساق الشجر قضبان غضة (ayn)؛ شكرت الشجرة خرج منها الشكير (sihah)؛ الشكير من الشعر والنبات ما ينبت (tahdhib)؛ الشكير من الفرخ الزغب (tahdhib)؛ وشكير كثير أي ذرية صغار (tahdhib)؛ الشيكَران ضرب من النبت (sihah)؛ الشكير نبت في أصل الشجرة غض (mufradat)
- **B005** şiddetlenip etkisini artırma — yağmurun yere düşüşü şiddetlendi · rüzgarın esişi şiddetlendi · sıcak veya soğuk şiddetlendi
  اشتكرت السماء اشتد وقعها (sihah)؛ اشتكرت السماء وحفلت واغبرت كل ذلك من حين يجد وقع مطرها ويشتد (tahdhib)؛ اشتكرت الريح إذا اشتد هبوبها (tahdhib)؛ اشتكر الحر والبرد كذلك (tahdhib)
- **B006** kadın cinsel organı veya birleşme için örtmece — kadın cinsel organı veya cinsel birleşme için örtmece · kadının cinsel organı · kadınların cinsel organları
  الأصل الرابع الشكر وهو النكاح (maqayis)؛ شكر المرأة فرجها (maqayis;sihah;tahdhib)؛ الشكر الفرج (ayn)؛ الشكر يكنى به عن فرج المرأة وعن النكاح (mufradat)؛ الشكار فروج النساء واحدها شكر (tahdhib)
- **B007** iki ayrı boy adı kullanımı — kanıtta belirtilen bir boyun adı · kanıtta belirtilen başka bir boyun adı
  يشكر قبيلة من ربيعة (ayn;tahdhib)؛ شاكر قبيلة من اليمن من همدان (ayn;tahdhib)

## ح ل م (root_000352): 64:17 حَلِيمٌ

- **B001** ağırdan alma ve kendini tutma — ağırbaşlılık ve kendini tutma · ağırbaşlı ve dayanıklı kimse · topluluğun ağırbaşlı kişileri veya sağduyusu · kendini ağırbaşlı davranmaya zorlamak veya öyle görünmek · birini ağırbaşlı kılmak veya öyle davranmaya yöneltmek · ağırbaşlı çocuklar doğurmak · başkasına ağırbaşlılığı öğreten veya öğütleyen kimse
  الحلم خلاف الطيش (maqayis)؛ الحلم الأناة، وأحلام القوم حلماؤهم، والحليم في صفة الله تعالى معناه الصبور (ayn;tahdhib)؛ الحلم بالكسر الأناة، وتحلم تكلف الحلم، وتحالم أرى من نفسه ذلك وليس به (sihah)؛ الحلم ضبط النفس والطبع عن هيجان الغضب، وليس الحلم في الحقيقة هو العقل (mufradat)
- **B002** uykuda görülen düş veya yaşanan boşalma — uykuda görülen düş · uykuda bir şey görmek · düş görmek veya uykuda boşalmak · görmediği bir düşü gördüğünü ileri sürmek · onu düşünde görmek · bir kadının hayalini düşünde görmek
  رؤية الشيء في المنام، حلم في نومه حلما وحلما (maqayis)؛ الحلم الرؤيا، حلم يحلم إذا رأى في المنام، من تحلم ما لم يحلم، والحلم الاحتلام (ayn;tahdhib)؛ الحلم بالضم ما يراه النائم، حلم واحتلم (sihah)؛ حلم في نومه، وتحلم واحتلم، حلمت به في نومي (mufradat)
- **B003** ergenlik çağına erişme — ergenlik çağı · ergenlik çağına erişmiş kimse · ergen sayılan kimse
  كل حالم دينارا، أراد بالحالم كل من بلغ الحلم، حلم أو لم يحلم (tahdhib)؛ وإذا بلغ الأطفال منكم الحلم أي زمان البلوغ، وسمي الحلم لكون صاحبه جديرا بالحلم (mufradat)
- **B004** parazit yüzünden derinin delinip bozulması — deri veya ham post parazit yüzünden delinip bozulmak · daha yüzülmeden parazitten bozulmuş deri · derisi parazitlerden bozulmuş deve · derisi parazitlerden bozulmuş dişi oğlak
  حلم الأديم إذا تثقب وفسد (maqayis)؛ أديم حلم قد أفسده الحلم قبل أن يسلخ (ayn;tahdhib)؛ الحلم بالتحريك أن يفسد الإهاب في الغمل ويقع فيه دود فيتثقب، حلم الأديم (sihah)؛ حلم الجلد وقعت فيه الحلمة (mufradat)
- **B005** kene ve biçimce ona benzetilen meme ucu — küçük keneler veya keneler topluluğu · iri kene veya çıkıntılı küçük canlı · meme ucu
  الحلم صغار القردان، والحلمة دويبة، وحلمتا الثدي (maqayis)؛ الحلمة والجميع الحلم ما عظم من القراد، والحلمة رأس الثدي (ayn)؛ الحلمة رأس الثدي، والحلمة القراد العظيم (sihah)؛ الحلمة الهنية الشاخصة من ثدي المرأة وثندوة الرجل وهي القراد (tahdhib)؛ الحلمة القراد الكبير، حلمة الثدي تشبيها بالحلمة من القراد في الهيئة (mufradat)
- **B006** bedenin yağlanıp dolgunlaşması — semirip gövdesi dolgunlaşmak · semiz deve · semiz dişi · bedenler veya gövdeler
  تحلم إذا سمن، امتلأ كأنه قراد ممتلئ، بعير حليم أي سمين (maqayis)؛ الأحلام الأجسام (ayn;tahdhib)؛ تحلم الصبي والضب أي سمن واكتنز، وبعير حليم أي سمين (sihah)؛ تحلم الصبي إذا أقبل شحمه، قردانها لم تحلم أي لم تسمن، وشارة حليمة سمينة (tahdhib)
- **B007** kimliği tartışmalı bir mera bitkisi — kimliği kaynaklara göre değişen bir mera otu veya çalısı
  الحلمة شجرة السعدان من أفضل المراعي (ayn)؛ الحلمة أيضا ضرب من النبت، هي الحلمة والينمة (sihah)؛ ليست الحلمة من شجر السعدان في شيء، الحلمة لا شوك لها وهي من الجنبة، ويقال للحلمة الحماطة (tahdhib)
- **B008** keneyi ayıklama ve yatıştırmak için yumuşak davranma [kalıp] — devenin üzerindeki keneleri ayıklamak · yatışması için birine yumuşak davranmak
  حلمت الإبل أخذت عنها الحلم (ayn)؛ حلمت البعير أخذت عنه الحلم (tahdhib)؛ حلمت البعير نزعت عنه الحلمة، ثم يقال حلمت فلانا إذا داريته ليسكن (mufradat)
- **B009** kişi, su, yer ve tarihsel olay adları — bir ırmak, kaynak veya kişi adı · ünlü bir eski savaş gününün adı · bir yer adı
  يوم حليمة وقعة، ومحلم نهر باليمامة (ayn)؛ حليمات موضع، ومحلم نهر يأخذ من عين هجر، ومحلم أيضا اسم رجل (sihah)؛ محلم عين فوارة بالبحرين، وأرى محلما اسم رجل نسبت العين إليه، ويوم حليمة أحد أيام العرب المشهورة (tahdhib)
- **B010** özel adlandırma kümesi — oğlak veya küçükbaş yavrusu · koyulaşıp taze peynire benzeyen süt
  الحلام الجدي (ayn;tahdhib)؛ الحلام والحلان بالميم والنون صغار الغنم (sihah)؛ الحالوم شيء شبيه بالأقط وما أراه عربيا صحيحا (maqayis)؛ الحالوم لبن يغلظ فيصير شبيها بالجبن الرطب (sihah)؛ الأصل حلان وهو فعلان من التحليل فقلبت النون ميما (tahdhib)

## غ ي ب (root_001117): 64:18 ٱلْغَيْبِ

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

## ش ه د (root_000822): 64:18 وَٱلشَّهَٰدَةِ

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

## ع ز ز (root_001008): 64:18 ٱلْعَزِيزُ

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

## ح ك م (root_000348): 64:18 ٱلْحَكِيمُ

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



===== _commentary/v16/work/s064/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s064/reader_a_pilot.md)

# s064 Semantic Channel Discovery

## Parent Channels

### 1. Covering, Exposure, and Release from Exposure
- Semantic invariant: A layer, screen, enclosure, or act of turning-away changes what can reach, reveal, stain, or punish the covered object.
- Surface relation: direct; concealment and disclosure are opposed at 64:4 (`تُسِرُّونَ` / `تُعْلِنُونَ`), moral covering appears at 64:9 (`يُكَفِّرْ`) and 64:14,17 (`تَغْفِرُوا`, `يَغْفِرْ`), and protective action is commanded at 64:14,16 (`فَٱحْذَرُوهُمْ`, `يُوقَ`).
- Surprising reach: The moral sequence of pardon and expiation is materialized as armor, a shield, a tent-like screen, night cover, erased tracks, and a concealed exit; disbelief and hypocrisy become rival uses of the same covering operation.

#### Subchannel A. Layered Defense Against an Incoming Harm
- Reading type: mixed
- Scene or process: A threatened subject becomes alert, equips a barrier, and places a shielding layer between itself and injury.
- Active motifs: armor worn as protection (`quranic:root_000121:B005/m01`); protective shield (`quranic:root_000266:B008/m01`); cautious preparedness and equipment (`quranic:root_000301:B003/m01`); armor or weapon called *zaʿāma* (`quranic:root_000633:B005/m01`); covering that preserves (`quranic:root_001096:B001/m01`); a thin protective screen or tent (`quranic:root_001315:B006/m01`); barrier against damage (`quranic:root_001677:B001/m01`); putting the self into protection (`quranic:root_001677:B002/m01`); warding off harm and clothing in safety (`quranic:root_001032:B002/m01`).
- Ayah anchors: 64:2 `بَصِيرٌ`; 64:7 `زَعَمَ`; 64:9 `جَنَّاتٍ`; 64:11 `كُلِّ`; 64:14 `فَٱحْذَرُوهُمْ`, `تَعْفُوا`, `تَغْفِرُوا`; 64:16 `ٱتَّقُوا`, `يُوقَ`; 64:17 `يَغْفِرْ`.
- Synthesis: Alertness supplies the posture, armor and shield supply hard protection, and screen, cover, and safety supply softer concentric layers. The scene makes caution toward an intimate threat and protection from the self's avarice structurally continuous with being covered against physical impact.

#### Subchannel B. Night, Recess, and the Hidden Way Out
- Reading type: mixed
- Scene or process: An object disappears from ordinary sight by entering darkness, a low recess, a thicket, a secret interior, or a tunnel with a concealed outlet.
- Active motifs: general concealment (`quranic:root_000266:B001/m01`); night covering what it overtakes (`quranic:root_000266:B002/m01`); unseen absence (`quranic:root_001117:B001/m01`); a low hollow in which something vanishes (`quranic:root_001117:B002/m01`); a concealing thicket (`quranic:root_001117:B003/m01`); a secret held inwardly (`quranic:root_000697:B001/m01`); the moon hidden at month's end (`quranic:root_000697:B004/m01`); engulfing darkness or expanse (`quranic:root_001307:B002/m01`); a through-tunnel with an exit (`quranic:root_001537:B003/m01`).
- Ayah anchors: 64:4 `تُسِرُّونَ`; 64:9 `جَنَّاتٍ`; 64:16 `أَنفِقُوا`; 64:18 `ٱلْغَيْبِ`; 64:2,5,6,7,9,10 `كَافِرٌ` / `كَفَرُوا` / `يُكَفِّرْ`.
- Synthesis: Darkness is not merely absence but a navigable architecture: cover above, hollow below, dense growth around, and a passage through. That architecture pressures the opposition between the unseen and the witnessed by asking whether hiddenness shelters, withholds evidence, or enables an unobserved escape.

#### Subchannel C. Pardon as Covering, Erasing, and Turning the Page
- Reading type: surface-primary
- Scene or process: Liability is first exposed, then passed over, screened from consequence, or erased until its trace no longer governs the relation.
- Active motifs: graceful turning-away from an offense (`quranic:root_000867:B002/m01`); waiving punishment and effacing the offense (`quranic:root_001032:B001/m01`); wind or time erasing a track (`quranic:root_001032:B006/m01`); covering a sin and protecting its bearer from its effect (`quranic:root_001096:B002/m01`); expiation that makes a wrong as though unperformed (`quranic:root_001307:B009/m01`); passing beyond and diverting from a thing (`quranic:root_000993:B004/m01`); withholding injury and weaning from it (`quranic:root_000994:B003/m01`); restraint that prevents corruption (`quranic:root_000348:B001/m01`).
- Ayah anchors: 64:9 `يُكَفِّرْ`; 64:14 `تَعْفُوا`, `تَصْفَحُوا`, `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`; 64:18 `ٱلْحَكِيمُ`; 64:5 `عَذَابٌ`; 64:14 `عَدُوًّا`.
- Synthesis: Forgiveness is a sequence of operations rather than a generic kindness: punishment is withheld, the face turns away from accusation, a protective cover blocks the after-effect, and the old track is removed. The sequence also explains how 64:14 can hold caution and mercy together without treating them as opposites.

#### Subchannel D. Counterfeit Cover and Hidden Corruption
- Reading type: mixed
- Scene or process: A surface display conceals an incompatible interior, allowing falsehood or disloyalty to pass as the visible state.
- Active motifs: covering or denying the truth (`quranic:root_001307:B003/m01`); covering a received benefit through ingratitude (`quranic:root_001307:B004/m01`); corruption lodged inside (`quranic:root_000464:B004/m01`); an outsider infiltrating a group or affair (`quranic:root_000464:B005/m01`); showing an entrance while hiding an exit (`quranic:root_001537:B004/m01`); fabricating speech (`quranic:root_000434:B007/m01`); falsehood opposed to truth (`quranic:root_001290:B001/m01`); public manifestation after concealment (`quranic:root_001041:B001/m01`).
- Ayah anchors: 64:2,5,6,7,9,10 `كَافِرٌ` / `كَفَرُوا` / `يُكَفِّرْ`; 64:3 `خَلَقَ`; 64:4 `تُعْلِنُونَ`; 64:9 `يُدْخِلْ`; 64:10 `كَذَّبُوا`; 64:16 `أَنفِقُوا`.
- Synthesis: The concealed outlet of a burrow supplies a precise mechanism for divided allegiance: the visible opening admits membership while the hidden opening preserves withdrawal. Fabricated speech and internal defect extend the same mechanism from spatial concealment to epistemic and social concealment.

### 2. Evidence-Bearing Speech from Sender to Hearer
- Semantic invariant: A meaningful claim must leave a source, travel through a carrier or sign, reach a hearer, and become either acknowledged testimony or exposed fabrication.
- Surface relation: direct; reports and messengers appear at 64:5-8, clear signs and conveyance at 64:6,12, hearing at 64:16, testimony at 64:18, and the contested claim about resurrection at 64:7,10.
- Surprising reach: The communication chain is embodied as dispatch, road markers, an ear that becomes obedience, and an oath that functions like a tested guarantee; false prophecy and attributed speech are broken links in the same chain.

#### Subchannel A. Dispatch, Carrier, and Delivered Report
- Reading type: surface-primary
- Scene or process: A sender launches a bearer carrying information; the message crosses distance and is delivered at its intended audience.
- Active motifs: dispatching a commissioned bearer (`quranic:root_000129:B002/m01`); sending and releasing (`quranic:root_000563:B001/m01`); messenger and carried message (`quranic:root_000563:B002/m01`); bringing the message to its destination (`quranic:root_000151:B002/m01`); consequential report brought to the hearer (`quranic:root_001464:B002/m01`); knowledge of a report's interior (`quranic:root_000387:B001/m01`); sending something down and making it arrive (`quranic:root_001492:B002/m01`); an agent, envoy, or guarantor (`quranic:root_000240:B003/m01`).
- Ayah anchors: 64:5 `نَبَؤُا`; 64:6 `رُسُلُهُم`; 64:7 `لَتُنَبَّؤُنَّ`, `تُبْعَثُ`; 64:8 `رَسُولِهِ`, `أَنزَلْنَا`, `خَبِيرٌ`; 64:9 `تَجْرِي`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`, `ٱلْبَلَاغُ`.
- Synthesis: Sending, carrying, and arriving form distinct roles in one relay. The light of 64:8 is therefore not only content that descends; it enters a delivery system whose human carrier has a bounded duty, while the source remains expert in what the recipients do.

#### Subchannel B. Clear Sign Becoming Witnessed Proof
- Reading type: mixed
- Scene or process: A visible marker directs attention, an explanation discloses its meaning, and informed testimony fixes what the marker proves.
- Active motifs: a manifest sign (`quranic:root_000074:B003/m01`); clear evidence emerging into view (`quranic:root_000170:B004/m01`); disclosure by speech, writing, or gesture (`quranic:root_000170:B005/m01`); a distinguishing mark or road flag (`quranic:root_001040:B002/m01`); testimony stated from knowledge (`quranic:root_000822:B002/m01`); an indicator that bears witness to a condition (`quranic:root_000822:B008/m01`); a beacon or visible landmark (`quranic:root_001564:B005/m01`); establishing and displaying the truth (`quranic:root_000347:B005/m01`); gentle direction toward road or truth (`quranic:root_001583:B001/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:4,11,18 `يَعْلَمُ` / `عَلِيمٌ` / `عَالِمُ`; 64:6 `بِٱلْبَيِّنَاتِ`; 64:8 `ٱلنُّورِ`; 64:10 `بِـَٔايَاتِنَا`; 64:18 `ٱلشَّهَادَةِ`; 64:6,11 `يَهْدُونَنَا`, `يَهْدِ`.
- Synthesis: Marker, interpretation, and witness are successive stages, not synonyms. The latent road-sign and beacon imagery makes revelation inspectable: a sign must be visible, legible, and situated so that it can actually orient a traveler.

#### Subchannel C. Claim, Counterclaim, and Fabricated Attribution
- Reading type: mixed
- Scene or process: A speaker advances a claim; another party tests its relation to reality, attribution, and competent testimony.
- Active motifs: assertion made without certainty (`quranic:root_000633:B001/m01`); articulated speech (`quranic:root_001272:B001/m01`); attributing words that were never said (`quranic:root_001272:B005/m01`); fabricated discourse (`quranic:root_000434:B007/m01`); falsehood against truth (`quranic:root_001290:B001/m01`); declaring another speaker false (`quranic:root_001290:B002/m01`); false claim to prophetic authority (`quranic:root_001464:B004/m01`); a dispute in which each side claims the right (`quranic:root_000347:B004/m01`); testimony grounded in knowledge (`quranic:root_000822:B002/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`, `خَلَقَ`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:6-7 `قَالُوا`, `قُلْ`, `زَعَمَ`; 64:10 `كَذَّبُوا`; 64:18 `ٱلشَّهَادَةِ`.
- Synthesis: The denial of resurrection is placed inside a forensic speech scene: uncertain assertion faces a counterstatement, attribution is checked, and testimony must be knowledge-bearing. False prophecy is the limiting case in which a carrier fabricates both message and mandate.

#### Subchannel D. Oath as a Tested Guarantee
- Reading type: mixed
- Scene or process: A divine name is invoked, an oath is offered to settle doubt, and the pledge exposes the speaker to verification.
- Active motifs: the divine name in oath and invocation (`quranic:root_000047:B002/m01`); oath-opening affirmation (`quranic:root_000074:B010/m01`); swearing and binding oneself (`quranic:root_000076:B007/m01`); presenting an oath to reassure or test (`quranic:root_000154:B005/m01`); lordship and mastery invoked in the pledge (`quranic:root_000532:B001/m01`); truth fixed against falsehood (`quranic:root_000347:B001/m01`); spoken declaration (`quranic:root_001272:B001/m01`).
- Ayah anchors: 64:1-2,4,6-9,11-17 recurrent `ٱللَّه`; 64:3 `بِٱلْحَقِّ`; 64:6-7 `قَالُوا`, `قُلْ`; 64:7 `وَرَبِّي`; 64:10 `ـَٔايَٰتِ` (in `بِـَٔايَٰتِنَا`). Surface anchors are unavailable for roots `ء ل ي` and `ب ل ي`.
- Synthesis: “By my Lord” is not decorative emphasis: oath, truth claim, and accountability form a guarantee structure. The lexical testing of an oath sharpens the verse's sequence from disputed resurrection to later disclosure of deeds.

#### Subchannel E. Hearing That Becomes Compliance
- Reading type: mixed
- Scene or process: Sound reaches the ear, is attended to and understood, then crosses the decisive threshold into enacted obedience.
- Active motifs: the ear and its receptive opening (`quranic:root_000022:B001/m01`); listening that accepts what is heard (`quranic:root_000022:B002/m01`); auditory reception (`quranic:root_000741:B001/m01`); understanding the utterance (`quranic:root_000741:B003/m01`); compliance after understanding (`quranic:root_000741:B003/m02`); making another hear (`quranic:root_000741:B004/m01`); attentive listening (`quranic:root_000831:B006/m01`); yielding and obedience (`quranic:root_000956:B001/m01`); submission after former resistance (`quranic:root_000844:B003/m01`).
- Ayah anchors: 64:11 `بِإِذْنِ`; 64:1,11 `شَيْءٍ`; 64:10 `أَصْحَابُ`; 64:12,16 `أَطِيعُوا`; 64:16 `ٱسْمَعُوا`.
- Synthesis: The scene distinguishes acoustics from response. An ear can receive sound without granting it authority; the active path is hearing, attending, understanding, accepting, and finally obeying, which gives 64:16 a compact physiology of responsible reception.

### 3. Guided Movement, Deviation, and Arrival
- Semantic invariant: Motion becomes meaningful through an oriented path, a leading agent, a responsive body, and an endpoint; failure appears as balking, veering, or turning away.
- Surface relation: direct; guidance occurs at 64:6,11, descent at 64:8, turning-away at 64:6,12, calamity striking at 64:11, and final destination at 64:3,10.
- Surprising reach: Guidance is materialized by road signs, the lead animal, reins, matched hoof-falls, arrow flight, and a watercourse; moral deviation becomes a measurable change in trajectory.

#### Subchannel A. A Marked Road with a Leader at Its Head
- Reading type: mixed
- Scene or process: A route is made legible by a beaten track and landmarks while a guide or lead animal occupies the front position.
- Active motifs: clear road across easy ground (`quranic:root_001464:B007/m01`); well-traveled road (`quranic:root_001046:B011/m01`); public road and junction (`quranic:root_000009:B010/m01`); distinguishing landmark (`quranic:root_001040:B002/m01`); beacon for finding the way (`quranic:root_001564:B005/m01`); gentle guidance to road or truth (`quranic:root_001583:B001/m01`); guide or foremost member (`quranic:root_001583:B003/m01`); animal leader followed by the rest (`quranic:root_001444:B008/m01`); the front and first part (`quranic:root_000849:B002/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`; 64:4 `عَلِيمٌ`, `ٱلصُّدُورِ`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:6,11 `يَهْدُونَنَا`, `يَهْدِ`; 64:8 `ٱلنُّورِ`; 64:2,7-9 `تَعْمَلُونَ` / `عَمِلْتُمْ` / `يَعْمَلْ`.
- Synthesis: Direction is distributed across infrastructure and agency: the road permits passage, the marker prevents loss, and the leader supplies a moving reference point. This converts “guidance” from an abstract transfer of information into sustained orientation.

#### Subchannel B. Tractable Gait Under Reins
- Reading type: latent/lexical
- Scene or process: A mount is equipped and led; sound gait responds lightly, while fatigue, hoof pain, or dependence on the rider interrupts forward motion.
- Active motifs: smooth, easy gait (`quranic:root_000563:B003/m01`); tractable obedience (`quranic:root_000956:B001/m01`); light responsive movement (`quranic:root_001694:B005/m01`); a mount lagging and relying on its rider (`quranic:root_001681:B005/m01`); guarding a sore hoof (`quranic:root_001677:B003/m01`); matching hind hoof to fore hoof (`quranic:root_000347:B014/m01`); forelegs returning in motion (`quranic:root_000009:B009/m01`); fatigue and loss of edge (`quranic:root_001315:B001/m01`); extending the reins to increase the run (`quranic:root_000151:B007/m01`); bridle or bit that restrains the horse (`quranic:root_000348:B006/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:7 `يَسِيرٌ`; 64:8,12 `رَسُولِهِ`, `ٱلرَّسُولَ`; 64:11 `كُلِّ`; 64:12 `ٱلْبَلَاغُ`; 64:12,16 `أَطِيعُوا`; 64:13 `يَتَوَكَّلِ`; 64:16 `ٱتَّقُوا`, `يُوقَ`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Obedience is neither inert passivity nor mere speed. The animal scene distinguishes responsive ease from forced motion and helpless dependence, giving bodily precision to the surah's pairing of obedience with “as much as you are able.”

#### Subchannel C. Aim, Impact, and the Veering Shot
- Reading type: mixed
- Scene or process: A line of force is aimed, either reaches and penetrates its target or deviates to a side without making the intended mark.
- Active motifs: aiming and hitting the target (`quranic:root_000889:B003/m01`); a calamity that takes its person (`quranic:root_000889:B004/m01`); an arrow that deflects without scratching (`quranic:root_001464:B005/m01`); a straight penetrating thrust (`quranic:root_000347:B009/m01`); a thrust aligned with the face (`quranic:root_001694:B009/m01`); bypass and lateral diversion (`quranic:root_000993:B004/m01`); veering away from the common direction (`quranic:root_001052:B002/m01`); inclining an object toward a side (`quranic:root_000891:B001/m01`); passing a place on one side (`quranic:root_001217:B002/m01`); being turned away from the true course (`quranic:root_001128:B003/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`, `صَوَّرَكُمْ`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:11 `أَصَابَ`, `مُصِيبَةٍ`; 64:14 `عَدُوًّا`; 64:15 `عِندَهُ`, `فِتْنَةٌ`; 64:17 `قَرْضًا`; 64:7 `يَسِيرٌ`.
- Synthesis: The same root scene holds providential impact and ethical deviation: what “hits” is not random merely because its path is unseen, while a deflected shot images a will that misses the disclosed line. This makes 64:11's *muṣība* an exact arrival rather than a generic misfortune.

#### Subchannel D. Arrival, Descent, Departure, and Final Return
- Reading type: surface-primary
- Scene or process: Something comes into range, descends or enters, leaves a source, and is finally returned to an endpoint.
- Active motifs: coming and arriving (`quranic:root_000009:B001/m01`); movement from one land into another (`quranic:root_001464:B001/m01`); descending and settling (`quranic:root_001492:B001/m01`); entering an interior (`quranic:root_000464:B001/m01`); departure from a watering place (`quranic:root_000849:B003/m01`); return and destination (`quranic:root_001248:B005/m01`); becoming and reaching an outcome (`quranic:root_000897:B001/m01`); reaching the limit (`quranic:root_000151:B001/m01`); endpoint and termination (`quranic:root_000076:B001/m01`).
- Ayah anchors: 64:3,10 `ٱلْمَصِيرُ`; 64:4 `ٱلصُّدُورِ`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:8 `أَنزَلْنَا`; 64:9 `يُدْخِلْهُ`; 64:11 `قَلْبَهُ`; 64:12 `ٱلْبَلَاغُ`. Surface anchor is unavailable for root `ء ل ي`.
- Synthesis: The surah repeatedly gives events a vector: reports come, light descends, people enter, and all movement resolves in a *maṣīr*. Departure from a water source adds a useful pressure: return is not static location but the completion of a circuit through need, provision, and accountability.

### 4. Dominion, Delegated Agency, and Liability
- Semantic invariant: Control can be possessed, commanded, delegated, guaranteed, or judged, but each transfer assigns a corresponding burden of answerability.
- Surface relation: direct; dominion and power open the surah at 64:1, command and obedience appear at 64:5,12,16, trust at 64:13, and final judgment of deeds at 64:7-10.
- Surprising reach: Kingship is reframed through custody, brokerage, surety, resale, and animal leadership: authority is not only rank but the capacity to carry an entrusted matter without passing it on until it is lost.

#### Subchannel A. Sovereign Possession and Effective Rule
- Reading type: surface-primary
- Scene or process: A sovereign possesses the field, has power to act in it, and appoints or sustains subordinate offices.
- Active motifs: worship owed to the divine (`quranic:root_000047:B001/m01`); lordship, ownership, and mastery (`quranic:root_000532:B001/m01`); possession and power of disposal (`quranic:root_001444:B002/m01`); kingship and political dominion (`quranic:root_001444:B003/m01`); office and governorship (`quranic:root_000051:B003/m01`); taking charge of an affair (`quranic:root_001684:B003/m01`); effective capacity and dominion (`quranic:root_001205:B003/m01`); might and inviolability (`quranic:root_001008:B001/m01`).
- Ayah anchors: recurrent 64:1-2,4,6-9,11-17 `ٱللَّه`; 64:1 `ٱلْمُلْكُ`, `قَدِيرٌ`; 64:5 `أَمْرِهِم`; 64:6,12 `تَوَلَّوْا`, `تَوَلَّيْتُمْ`; 64:7 `رَبِّي`; 64:18 `ٱلْعَزِيزُ`.
- Synthesis: Possession, sovereignty, and capability occupy different roles: one establishes title, one orders the field, and one makes the order effective. Their convergence clarifies why divine independence in 64:6 does not mean disengagement from governance.

#### Subchannel B. Command Accepted or Turned Away
- Reading type: surface-primary
- Scene or process: An authoritative direction is issued; the recipient can align with it, be coerced away from it, turn toward it, or turn its back.
- Active motifs: binding command (`quranic:root_000051:B002/m01`); obedience and yielding (`quranic:root_000956:B001/m01`); reciprocal compliance (`quranic:root_000956:B002/m01`); authoritative speaker whose word carries (`quranic:root_001272:B004/m01`); restraint for correction (`quranic:root_000348:B001/m01`); coercing an obedient person into disobedience (`quranic:root_001307:B007/m01`); turning the face toward and accepting (`quranic:root_001684:B006/m01`); turning the back and refusing (`quranic:root_001684:B007/m01`).
- Ayah anchors: 64:5 `أَمْرِهِم`; 64:6-7 `قَالُوا`, `قُلْ`, `تَوَلَّوْا`; 64:12 `أَطِيعُوا`, `تَوَلَّيْتُمْ`; 64:16 `أَطِيعُوا`; 64:18 `ٱلْحَكِيمُ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`.
- Synthesis: Command creates an oriented relation rather than a bare utterance. The role reversal in “forcing the obedient into disobedience” is especially useful for 64:14: an intimate party can exert agency against the believer's proper alignment without becoming the final bearer of responsibility.

#### Subchannel C. Delegation, Custody, and the Risk of Mutual Shirking
- Reading type: mixed
- Scene or process: An affair is handed to an agent or guarantor, who must preserve and discharge it rather than relay dependence until nobody acts.
- Active motifs: entrusting an affair to another (`quranic:root_001681:B001/m01`); reliance and trust (`quranic:root_001681:B002/m01`); custodian sufficient to guard the matter (`quranic:root_001681:B006/m01`); undertaking surety (`quranic:root_000633:B003/m01`); written or personal guarantee (`quranic:root_001198:B008/m01`); taking responsibility for another (`quranic:root_001332:B003/m01`); envoy-agent or guarantor (`quranic:root_000240:B003/m01`); disavowing an attachment or liability (`quranic:root_001307:B005/m01`); mutual reliance that lets the affair fail (`quranic:root_001681:B004/m01`).
- Ayah anchors: 64:6 `كَانَت`; 64:7 `زَعَمَ`; 64:9 `تَجْرِي`; 64:13 `فَلْيَتَوَكَّلِ`; 64:5 `قَبْلُ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`.
- Synthesis: Trust is distinguished from incapacity: proper delegation names a competent keeper and preserves answerability, while mutual off-loading destroys the task. This gives the command to rely on God a technical contrast with the household and wealth relations in which human agents can fail their charge.

#### Subchannel D. Right, Adjudication, and Redress
- Reading type: mixed
- Scene or process: A right becomes due, competing parties assert it, an adjudicator distinguishes entitlement, and an injured party seeks enforcement.
- Active motifs: binding entitlement (`quranic:root_000347:B002/m01`); a specific right possessed against another (`quranic:root_000347:B003/m01`); adversarial claims to right (`quranic:root_000347:B004/m01`); judging between people (`quranic:root_000348:B002/m01`); delegating a dispute to an arbitrator (`quranic:root_000348:B005/m01`); priority and superior entitlement (`quranic:root_001684:B008/m01`); petitioning authority for redress (`quranic:root_000993:B005/m01`); confiscation or enforced financial exaction (`quranic:root_000849:B005/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:4 `ٱلصُّدُورِ`; 64:6 `تَوَلَّوْا`; 64:12 `تَوَلَّيْتُمْ`; 64:14 `عَدُوًّا`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Right is not collapsed into power: entitlement, claim, judgment, and enforcement remain distinct. The resulting legal frame intensifies *taghābun*: final exposure is the point at which apparent advantage and actual entitlement can no longer be confused.

### 5. Measured Making, Fitted Form, and Bounded Capacity
- Semantic invariant: A viable thing is estimated before making, formed into a proportionate whole, brought to maturity, and judged against the capacity its measure permits.
- Surface relation: direct; creation, true proportion, and human form appear at 64:2-3, divine capacity at 64:1, human capacity at 64:16, the good loan at 64:17, and consummate wisdom at 64:18.
- Surprising reach: Creation is materialized as cutting hide to measure, fitting joints, tightening a weave, matching hoofprints, and setting a limit; “ability” becomes the room a well-fitted form actually has for action.

#### Subchannel A. Estimate, Create, and Give Form
- Reading type: surface-primary
- Scene or process: A maker estimates dimensions, brings the object into being, and gives it an outward and inward form that can be evaluated as sound or distorted.
- Active motifs: estimating before cutting or acting (`quranic:root_000434:B001/m01`); origination and creation (`quranic:root_000434:B002/m01`); completed bodily formation (`quranic:root_000434:B003/m01`); planning by measure and calculation (`quranic:root_001205:B005/m01`); formed image or configuration (`quranic:root_000891:B003/m01`); beauty opposed to ugliness (`quranic:root_000323:B001/m01`); excellent action and workmanship (`quranic:root_000323:B002/m01`); distortion of face or form (`quranic:root_000832:B002/m01`); open, well-composed appearance (`quranic:root_000120:B006/m01`).
- Ayah anchors: 64:1 `قَدِيرٌ`; 64:2-3 `خَلَقَ`; 64:3 `صَوَّرَكُمْ`, `صُوَرَكُمْ`, `أَحْسَنَ`; 64:6 `بَشَرٌ`; 64:17 `حَسَنًا`; 64:1,11 `شَيْءٍ`.
- Synthesis: Estimation precedes origination, and origination precedes visible form. The contrast with disfigurement shows that “best forms” is not ornamental description: proportion is evidence that measured intention has successfully entered matter.

#### Subchannel B. Joint, Edge, and Fitted Whole
- Reading type: latent/lexical
- Scene or process: Separate pieces are aligned at edges and joints, stitched or interlocked, then tested for cohesion and completeness.
- Active motifs: joining two hide edges by stitching (`quranic:root_000121:B006/m01`); joint, socket, or vessel fitting its place (`quranic:root_000347:B011/m01`); tightly woven and verified construction (`quranic:root_000347:B010/m01`); an intact whole lacking no bodily part (`quranic:root_000259:B009/m01`); totality that includes all parts (`quranic:root_001315:B003/m01`); corresponding pieces joined face-to-face (`quranic:root_001198:B010/m01`); interpenetrating components and connective tissue (`quranic:root_000464:B008/m01`); correspondence to an exact measure (`quranic:root_001205:B006/m01`); cohesion that lets a wall or body stand (`quranic:root_001444:B001/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`, `كُلِّ`, `قَدِيرٌ`; 64:2 `بَصِيرٌ`; 64:3 `بِٱلْحَقِّ`; 64:5 `قَبْلُ`; 64:9 `يَجْمَعُ`, `جَمْعِ`, `يُدْخِلْ`; 64:11 `كُلِّ`.
- Synthesis: The channel gives “truth” a constructive texture: a statement or form is sound when its parts meet, hold, and occupy their proper places. Gathering and totality then become the completion of fitted relations rather than sheer accumulation.

#### Subchannel C. Maturity at the Attained Limit
- Reading type: latent/lexical
- Scene or process: A person, animal, craft, or utterance passes through development until it reaches the state in which its intended function is fully available.
- Active motifs: reaching an endpoint (`quranic:root_000151:B001/m01`); consummate quality without shortfall (`quranic:root_000151:B005/m01`); reaching puberty (`quranic:root_000352:B003/m01`); a camel mature enough for carrying or riding (`quranic:root_000347:B008/m01`); an animal reaching full strength and condition (`quranic:root_000347:B013/m01`); perfected and securely finished work (`quranic:root_000348:B004/m01`); reaching or taking the final goal (`quranic:root_001684:B012/m01`); exertion carried to its utmost (`quranic:root_000323:B005/m01`); a praiseworthy final limit (`quranic:root_000355:B004/m01`).
- Ayah anchors: 64:1,6 `ٱلْحَمْدُ`, `حَمِيدٌ`; 64:3 `بِٱلْحَقِّ`, `أَحْسَنَ`; 64:12 `ٱلْبَلَاغُ`, `تَوَلَّيْتُمْ`; 64:17 `حَلِيمٌ`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Maturity is a functional threshold: speech reaches its audience, a mount becomes load-bearing, and a made thing becomes secure. The scene usefully reframes final return as the point where development can no longer be mistaken for incompletion.

#### Subchannel D. Capacity Within a Given Measure
- Reading type: mixed
- Scene or process: A task is compared with available power; ease, weakness, restriction, and the ability to meet an opposing force determine what can actually be done.
- Active motifs: fixed amount and bounded measure (`quranic:root_001205:B001/m01`); effective capability (`quranic:root_001205:B003/m01`); ability to perform (`quranic:root_000956:B003/m01`); energetic capacity (`quranic:root_000076:B011/m01`); power to face and withstand (`quranic:root_001198:B013/m01`); opening into ease (`quranic:root_001694:B001/m01`); a small or slight amount (`quranic:root_001694:B002/m01`); constricting provision to a narrow measure (`quranic:root_001205:B004/m01`); weakness opposed to strength (`quranic:root_000909:B001/m01`); the incapable dependent who hands over his affair (`quranic:root_001681:B003/m01`).
- Ayah anchors: 64:1 `قَدِيرٌ`; 64:5 `قَبْلُ`; 64:7 `يَسِيرٌ`; 64:12,16 `أَطِيعُوا`, `ٱسْتَطَعْتُم`; 64:13 `فَلْيَتَوَكَّلِ`; 64:17 `يُضَاعِفْ`. Surface anchor is unavailable for root `ء ل ي`.
- Synthesis: Capacity is relational: the same measure can be ample for one agent and restrictive for another. This differentiates divine ease in 64:7 from human obligation “as much as you are able” in 64:16, without reducing either to a vague scale of strength.

### 6. Value Leaving the Hand and Returning Under Account
- Semantic invariant: Work, money, goods, or benefit leaves an agent, enters a relation of exchange, and returns as wage, repayment, multiplication, praise, loss, or exposed deficit.
- Surface relation: direct; deeds are disclosed at 64:7-9, wealth and reward at 64:15, spending at 64:16, and the good loan, multiplication, forgiveness, and acknowledgment at 64:17.
- Surprising reach: The moral economy is made concrete through wages, investment capital, resale, underpayment, a closed fist, a rejected petitioner, and market puffery; *taghābun* becomes an accounting event rather than a loose image of regret.

#### Subchannel A. Work, Office, and Earned Return
- Reading type: mixed
- Scene or process: A worker performs an intentional task, possibly under an appointed office, and receives a wage, provision, or continuing return.
- Active motifs: intentional work (`quranic:root_001046:B001/m01`); wage and recompense (`quranic:root_000015:B001/m01`); worker's pay or ration (`quranic:root_001046:B004/m01`); appointed public work (`quranic:root_001046:B003/m01`); manual laborers (`quranic:root_001046:B006/m01`); continuing provision or disbursement (`quranic:root_000240:B006/m01`); subsistence sufficient for the journey (`quranic:root_000151:B003/m01`); provision prepared for an arriving guest (`quranic:root_001492:B005/m01`).
- Ayah anchors: 64:2,8 `تَعْمَلُونَ`; 64:7 `عَمِلْتُمْ`; 64:9 `يَعْمَلْ`, `تَجْرِي`; 64:12 `ٱلْبَلَاغُ`; 64:15 `أَجْرٌ`; 64:8 `أَنزَلْنَا`.
- Synthesis: The scene separates deed, office, wage, and ongoing provision. This makes “what you did” at 64:7 an account of intentional performance, while the great reward at 64:15 is the return assigned by the one who owns the work's final valuation.

#### Subchannel B. Loan, Capital, and Multiplied Repayment
- Reading type: surface-primary
- Scene or process: A portion is cut from present possession and advanced; it enters productive use and returns with its equivalent or a multiplied surplus.
- Active motifs: cutting off a portion (`quranic:root_001217:B001/m01`); monetary advance to be repaid (`quranic:root_001217:B003/m01`); a deed advanced for later return (`quranic:root_001217:B003/m02`); capital entrusted for shared trade (`quranic:root_001217:B004/m01`); increase by an equal amount or more (`quranic:root_000909:B002/m01`); reciprocal recompense (`quranic:root_001217:B005/m01`); excellent benefaction (`quranic:root_000323:B002/m02`); goodness qualifying the advance (`quranic:root_000323:B001/m01`); acknowledgment of the benefaction (`quranic:root_000810:B001/m01`); covering the lender's offense as part of the return (`quranic:root_001096:B002/m01`).
- Ayah anchors: 64:3,17 `أَحْسَنَ`, `حَسَنًا`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`, `تُقْرِضُوا`, `قَرْضًا`, `يُضَاعِفْهُ`, `شَكُورٌ`.
- Synthesis: The loan is not treated as a metaphor detached from finance. Cutting a present share, entrusting capital, and receiving a multiplied return supply the exact process by which expenditure becomes future value, while forgiveness enters the repayment package as protection from negative account.

#### Subchannel C. Outflow, Open Hand, and Self-Hoarding
- Reading type: mixed
- Scene or process: Wealth can flow outward as voluntary surplus or be arrested by a self that closes its grasp, contests every share, and turns away the asker.
- Active motifs: expenditure as wealth leaving possession (`quranic:root_001537:B002/m01`); accumulated wealth (`quranic:root_001457:B001/m01`); withholding joined to acquisitive greed (`quranic:root_000778:B001/m01`); two parties contesting so neither loses the object (`quranic:root_000778:B002/m01`); rejecting a petitioner by turning away (`quranic:root_000867:B009/m01`); easy surplus left beyond strict claim (`quranic:root_001032:B003/m01`); generosity and gift (`quranic:root_000452:B005/m01`); voluntary contribution (`quranic:root_000956:B005/m01`); the closed fist (`quranic:root_000259:B005/m01`); handshake by open palm (`quranic:root_000867:B004/m01`); demanding praise for one's expenditure (`quranic:root_000355:B005/m01`).
- Ayah anchors: 64:1,6 `ٱلْحَمْدُ`, `حَمِيدٌ`; 64:9 `يَجْمَعُ`; 64:14 `تَعْفُوا`, `تَصْفَحُوا`; 64:15 `أَمْوَالُكُمْ`; 64:16 `أَطِيعُوا`, `أَنفِقُوا`, `شُحَّ`, `خَيْرًا`.
- Synthesis: Closed fist and open palm provide a bodily mechanism for the conflict between *infaq* and *shuḥḥ*. The open hand is not indiscriminate loss: it releases surplus into a reciprocal relation, while self-hoarding tries to keep value outside every claim but its own.

#### Subchannel D. Concealed Defect, Underpayment, and Final Deficit
- Reading type: mixed
- Scene or process: A transaction appears advantageous because a defect, short measure, or manipulative representation is hidden; later accounting reveals who was actually diminished.
- Active motifs: underpayment and concealed loss in exchange (`quranic:root_001072:B001/m01`); deficient judgment (`quranic:root_001072:B002/m01`); a missed opportunity recognized as loss (`quranic:root_001072:B006/m01`); commercial dealing (`quranic:root_001046:B005/m01`); resale at the disclosed original price (`quranic:root_001684:B014/m01`); deceptive sales promotion (`quranic:root_001175:B007/m01`); hidden defect or fraud (`quranic:root_000464:B004/m01`); a patterned cloth whose appearance misrepresents it (`quranic:root_001290:B009/m01`); blame assigned to a bad act (`quranic:root_000755:B005/m01`).
- Ayah anchors: 64:2,8 `تَعْمَلُونَ`; 64:7 `عَمِلْتُمْ`; 64:9 `يَعْمَلْ`, `يَوْمُ ٱلتَّغَابُنِ`, `يُدْخِلْ`, `سَيِّـَٔاتِ`; 64:6 `تَوَلَّوْا`; 64:12 `تَوَلَّيْتُمْ`; 64:10 `كَذَّبُوا`; 64:16 `ٱلْمُفْلِحُونَ`.
- Synthesis: *Taghābun* is resolved as a transaction whose apparent winner relied on hidden information. Honest resale, deceptive display, deficient judgment, and retrospective loss form a precise contrast between transparent valuation and advantage that survives only until the books are opened.

### 7. Cultivation Through Water into Visible Yield
- Semantic invariant: A concealed input enters soil, plant, or animal body, is sustained by water and care, and emerges as growth, fruit, milk, or multiplied stock.
- Surface relation: direct; earth and sky frame 64:1,3-4, gardens and rivers appear at 64:9, wealth and children are tested yield at 64:15, and multiplication follows the good loan at 64:17.
- Surprising reach: Covering seed, opening a watercourse, retaining runoff, exposing shoots, and filling an udder provide one material grammar for faith, expenditure, trial, gratitude, and multiplication.

#### Subchannel A. Preparing Ground and Covering Seed
- Reading type: latent/lexical
- Scene or process: Soft, water-holding land is opened by the plow, seed is covered, and runoff is retained so cultivation can begin.
- Active motifs: fertile soft soil (`quranic:root_000025:B002/m01`); low soft land holding water (`quranic:root_000387:B002/m01`); sharecropping and cultivation (`quranic:root_000387:B003/m01`); splitting soil open (`quranic:root_001175:B001/m01`); the plowman who cuts the earth (`quranic:root_001175:B003/m01`); farmer covering seed with soil (`quranic:root_001307:B008/m01`); fruit sheath covering its growth (`quranic:root_001307:B010/m01`); land that retains its floodwater (`quranic:root_000778:B004/m01`).
- Ayah anchors: 64:1,3,4 `ٱلْأَرْض`; 64:8 `خَبِيرٌ`; 64:16 `شُحَّ`, `ٱلْمُفْلِحُونَ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`.
- Synthesis: The same covering action that can hide truth can also plant a seed. The distinction lies in function and outcome: one cover blocks evidence, while the farmer's cover entrusts a viable input to conditions that will expose its quality through growth.

#### Subchannel B. Shoot, Orchard, Palm, and Blossom
- Reading type: mixed
- Scene or process: Latent growth breaks cover, develops into clustered vegetation, forms an orchard, and becomes flower, fruit, or sweet exudate.
- Active motifs: emergence of yield (`quranic:root_000009:B007/m01`); growth and blessing (`quranic:root_000051:B004/m01`); tree-covered orchard (`quranic:root_000266:B003/m01`); dense and forceful plant growth (`quranic:root_000266:B011/m01`); tender new shoot (`quranic:root_000810:B004/m01`); young palms (`quranic:root_000831:B008/m01`); cluster of palms (`quranic:root_000891:B005/m01`); palm-heart or pith (`quranic:root_001248:B003/m01`); blossom and flowering (`quranic:root_001564:B004/m01`); pasture and fruit becoming ready (`quranic:root_000956:B007/m01`); abundance after being left to grow (`quranic:root_001032:B007/m01`); sweet exudate gathered from trees (`quranic:root_001096:B007/m01`).
- Ayah anchors: 64:1,11 `شَىْءٍ`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5 `أَمْرِهِم`; 64:9 `جَنَّاتٍ`; 64:11 `قَلْبَهُ`; 64:12 `أَطِيعُوا`; 64:16 `ٱسْتَطَعْتُم`, `أَطِيعُوا`; 64:14 `تَعْفُوا`, `تَغْفِرُوا`; 64:17 `شَكُورٌ`; 64:3 `صَوَّرَكُمْ`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`.
- Synthesis: The process moves from a hidden center to visible branching and blossom. It gives “multiplication” an organic timescale and lets the garden promise of 64:9 begin earlier, in the small shoot whose emergence makes prior care legible.

#### Subchannel C. Rain, Runoff, Channel, and River
- Reading type: mixed
- Scene or process: Water descends, gathers force, is retained or directed through a cut channel, and continues as a flowing river.
- Active motifs: channeling water toward a basin (`quranic:root_000009:B004/m01`); flood arriving from another land (`quranic:root_000009:B005/m01`); flowing water (`quranic:root_000240:B001/m01`); layered rain-cloud (`quranic:root_000532:B008/m01`); rain descending from above (`quranic:root_000889:B001/m01`); descent and settling (`quranic:root_001492:B001/m01`); river cutting the ground (`quranic:root_001559:B001/m01`); opening and widening a course until it flows (`quranic:root_001559:B003/m01`); forceful rain and flood (`quranic:root_001008:B008/m01`); heavy downpour (`quranic:root_001619:B001/m01`); rain following the first seasonal rain (`quranic:root_001684:B010/m01`); ground retaining runoff (`quranic:root_000778:B004/m01`).
- Ayah anchors: 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5 `وَبَالَ`; 64:6 `تَوَلَّوْا`; 64:7 `رَبِّي`; 64:8 `أَنزَلْنَا`; 64:9 `تَجْرِي`, `ٱلْأَنْهَارُ`; 64:16 `شُحَّ`; 64:18 `ٱلْعَزِيزُ`; 64:11 `أَصَابَ`.
- Synthesis: Descent alone does not produce fertility. The water must arrive, meet receptive ground, be held, and receive a course. That sequence reframes calamity and revelation as different descending inputs whose outcome depends partly on the receiving terrain.

#### Subchannel D. Water Securing Life and Settlement
- Reading type: latent/lexical
- Scene or process: A traveler or herd finds stored, sweet water; the source sustains life, permits settlement, and organizes approach and departure.
- Active motifs: abundant water (`quranic:root_000532:B013/m01`); sea or water-rich well (`quranic:root_001040:B005/m01`); water by which travelers secure their affairs (`quranic:root_001444:B007/m01`); water that keeps the self alive (`quranic:root_001533:B008/m01`); sweet drinkable water (`quranic:root_000994:B001/m01`); an open well (`quranic:root_001248:B007/m01`); a rock hollow retaining rain (`quranic:root_000434:B011/m01`); returning thirsty camels to drink (`quranic:root_000464:B007/m01`); watering at the animals' mouths (`quranic:root_001198:B014/m01`); departure after watering (`quranic:root_000849:B003/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`; 64:3 `خَلَقَ`; 64:4 `يَعْلَمُ`, `عَلِيمٌ`; 64:11 `عَلِيمٌ`; 64:18 `عَالِمُ`; 64:5 `عَذَابٌ`, `قَبْلُ`; 64:7 `رَبِّي`; 64:9 `يُدْخِلْ`; 64:11 `قَلْبَهُ`; 64:16 `أَنفُسِكُمْ`; 64:4 `ٱلصُّدُورِ`.
- Synthesis: Water is simultaneously substance, infrastructure, and social organizer. It makes travel survivable, fixes where a camp can stand, and imposes an ordered movement into and away from the source, echoing the surah's larger movement from need to provision to return.

#### Subchannel E. Milk, Fertility, and Yield That Can Fail
- Reading type: latent/lexical
- Scene or process: Feed, pregnancy, and bodily condition become milk and offspring; abundance is visible in a full udder, while constriction or failed continuity exposes a false expectation of yield.
- Active motifs: continuous milk flow (`quranic:root_000563:B006/m01`); little feed producing visible fatness (`quranic:root_000810:B002/m01`); full udder and abundant milk (`quranic:root_000810:B003/m01`); increase of milk and offspring (`quranic:root_001694:B006/m01`); constricted passage and low yield (`quranic:root_001008:B006/m01`); milk expected to continue but failing (`quranic:root_001290:B006/m01`); bodily fullness (`quranic:root_000352:B006/m01`); animal reaching full condition (`quranic:root_000347:B013/m01`); recently delivered ewe (`quranic:root_000532:B009/m01`); multiplication beyond the original amount (`quranic:root_000909:B002/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:6,8,12 `رُسُلُهُم`, `رَسُولِهِ`, `ٱلرَّسُولَ`; 64:7 `رَبِّي`, `يَسِيرٌ`; 64:10 `كَذَّبُوا`; 64:17 `شَكُورٌ`, `حَلِيمٌ`, `يُضَاعِفْ`; 64:18 `ٱلْعَزِيزُ`.
- Synthesis: Gratitude is given a bodily indicator: a small input becomes visible fullness and continuing yield. Conversely, milk that “lies” by disappearing turns failed expectation into an image for apparent prosperity that cannot survive final accounting.

### 8. Trial That Reveals Quality Through Impact
- Semantic invariant: A person or material meets a force that tests, strikes, burns, tastes, or disorders it, and the resulting condition reveals what the subject can bear or what it truly is.
- Surface relation: direct; former peoples taste consequence at 64:5, wealth and children are a trial at 64:15, calamity strikes at 64:11, and painful punishment and fire frame 64:5,10.
- Surprising reach: Trial is not one loose hardship category: it separates metal in fire, tests a bow, hits like a projectile, enters the mouth as taste, and can relapse inside a wound or mind.

#### Subchannel A. Assay by Fire and Experience
- Reading type: mixed
- Scene or process: Metal or person enters an ordeal whose heat or pressure separates sound quality from defect and makes the result evidential.
- Active motifs: assaying metal and testing a person (`quranic:root_001128:B001/m01`); burning and blackening by fire (`quranic:root_001128:B002/m01`); an ordeal that reveals condition (`quranic:root_000154:B002/m01`); experiential tasting of what befalls (`quranic:root_000526:B002/m01`); expertise gained through testing interiors (`quranic:root_000387:B001/m02`); evidence stated from knowledge (`quranic:root_000822:B002/m01`); truth fixed against falsehood (`quranic:root_000347:B001/m01`); selecting the sound or better specimen (`quranic:root_000452:B002/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:5 `ذَاقُوا`; 64:8 `خَبِيرٌ`; 64:15 `فِتْنَةٌ`; 64:16 `خَيْرًا`; 64:18 `ٱلشَّهَادَةِ`. Surface anchor is unavailable for root `ب ل ي`.
- Synthesis: The ordeal produces knowledge by transformation: heat does not merely hurt the metal but displays its composition. Wealth and children as *fitna* therefore become testing media whose pressure discloses allegiance, generosity, and restraint.

#### Subchannel B. Calamity as a Descending Impact
- Reading type: surface-primary
- Scene or process: A severe event gathers force, descends along a line, reaches its subject, and leaves an outcome whose weight cannot be dismissed.
- Active motifs: calamity striking its person (`quranic:root_000889:B004/m01`); aimed impact (`quranic:root_000889:B003/m01`); a severe event descending on a group (`quranic:root_001492:B006/m01`); overwhelming disaster (`quranic:root_001029:B004/m01`); heavy harmful consequence (`quranic:root_001619:B002/m01`); hard impact on the self (`quranic:root_001008:B005/m01`); destruction or illness arriving (`quranic:root_000009:B011/m01`); the day's decisive event (`quranic:root_001700:B003/m01`).
- Ayah anchors: 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5 `وَبَالَ`; 64:8 `أَنزَلْنَا`; 64:9 `يَوْمُ`; 64:11 `أَصَابَ`, `مُصِيبَةٍ`; 64:15 `عَظِيمٌ`; 64:18 `ٱلْعَزِيزُ`.
- Synthesis: Impact, descent, and weight make 64:11's calamity a completed trajectory. The scene also preserves the distinction between permission and randomness: an event can arrive through an ordered path even when its route is not visible to the struck subject.

#### Subchannel C. Tasting the Bitter Consequence
- Reading type: surface-primary
- Scene or process: Consequence crosses from external threat into bodily experience as taste, pain, deprivation, or an intake the body cannot accept.
- Active motifs: tasting food or drink (`quranic:root_000526:B001/m01`); experiencing punishment by taste (`quranic:root_000526:B002/m02`); painful punishment (`quranic:root_000994:B005/m01`); felt pain (`quranic:root_000046:B001/m01`); inflicting or describing pain (`quranic:root_000046:B002/m01`); overpowering severity (`quranic:root_000079:B001/m01`); poverty and constricted living (`quranic:root_000079:B002/m01`); unwholesome food, water, or land (`quranic:root_001619:B003/m01`); a body refusing food and drink (`quranic:root_000994:B002/m01`).
- Ayah anchors: 64:5 `ذَاقُوا`, `وَبَالَ`, `عَذَابٌ أَلِيمٌ`; 64:10 `بِئْسَ`.
- Synthesis: “Taste” is the threshold at which reported consequence becomes undeniable experience. Bitter intake, pain, and failure to assimilate give bodily depth to the prior peoples' encounter with the burden of their affair.

#### Subchannel D. Hidden Disorder, Relapse, and Mental Destabilization
- Reading type: latent/lexical
- Scene or process: A defect lodges within body or judgment, spreads or returns after apparent recovery, and disrupts the subject's capacity to perceive and choose.
- Active motifs: internal corruption (`quranic:root_000464:B004/m01`); mind covered by madness (`quranic:root_000266:B006/m01`); deficient judgment (`quranic:root_001072:B002/m01`); loss of mind and property through trial (`quranic:root_001128:B007/m01`); involuntary bodily disturbance (`quranic:root_000025:B012/m01`); disease or leprous affliction (`quranic:root_000755:B003/m01`); relapse of wound or illness (`quranic:root_001096:B004/m01`); disease of the heart (`quranic:root_001248:B011/m01`); affliction reaching the mind (`quranic:root_000889:B004/m02`); transmission of disease (`quranic:root_000993:B006/m01`).
- Ayah anchors: 64:1,3,4 `ٱلْأَرْض`; 64:9 `جَنَّاتٍ`, `يُدْخِلْ`, `يَوْمُ ٱلتَّغَابُنِ`, `سَيِّـَٔاتِ`; 64:11 `مُصِيبَةٍ`, `قَلْبَهُ`; 64:14 `عَدُوًّا`, `تَغْفِرُوا`, `غَفُورٌ`; 64:15 `فِتْنَةٌ`; 64:17 `يَغْفِرْ`.
- Synthesis: The scene distinguishes a visible blow from a disorder that works inwardly or returns later. That pressure matters for the surah's household and wealth trials: danger may operate by altering judgment before it appears as an external loss.

### 9. Gathering a Whole, Sorting It, and Assigning Shares
- Semantic invariant: Dispersed members are brought into one bounded set so they can be counted, paired, classified, enclosed, or allotted unequal outcomes.
- Surface relation: direct; 64:9 names both the day of gathering and the day of mutual loss and gain, while 64:14-15 distinguishes spouses, children, allies, and enemies within the intimate group.
- Surprising reach: The final assembly is materialized as a crowd, herd, livestock pen, paired species, and a gambling draw whose arrows distribute portions; gathering is the precondition for exact separation, not the cancellation of difference.

#### Subchannel A. From Dispersed Members to an Accountable Whole
- Reading type: surface-primary
- Scene or process: Scattered persons are called into one place, counted as a complete body, and made present without remainder.
- Active motifs: gathering dispersed members (`quranic:root_000259:B001/m01`); assembled crowd or mixed host (`quranic:root_000259:B002/m01`); day, place, or call that convenes people (`quranic:root_000259:B004/m01`); intact totality without missing parts (`quranic:root_000259:B009/m01`); mass of people (`quranic:root_000266:B013/m01`); numerous assembled groups (`quranic:root_000532:B004/m01`); the whole crowd without anyone staying behind (`quranic:root_001096:B008/m01`); groups facing one another (`quranic:root_001198:B009/m01`); gathered companies (`quranic:root_001315:B009/m01`); totality enclosing all members (`quranic:root_001315:B003/m01`).
- Ayah anchors: 64:1 `كُلِّ`; 64:5 `قَبْلُ`; 64:7 `رَبِّي`; 64:9 `يَجْمَعُكُمْ`, `يَوْمِ ٱلْجَمْعِ`, `جَنَّاتٍ`; 64:11 `كُلِّ`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`.
- Synthesis: The scene insists on both assembly and completeness. “Day of gathering” is thus not only mass presence; it is the closure of the set, after which no hidden member or omitted action can remain outside the account.

#### Subchannel B. Herd, Pursuit, and Enclosure
- Reading type: latent/lexical
- Scene or process: Animals are found in groups, pursued in sequence, and driven or returned into a bounded shelter.
- Active motifs: herd of wild cattle or camels (`quranic:root_000532:B014/m01`); cattle herd (`quranic:root_000891:B006/m01`); livestock enclosure (`quranic:root_000897:B003/m01`); successive flocks (`quranic:root_000563:B005/m01`); sheltered hiding place (`quranic:root_000266:B017/m01`); thicket in which an entrant disappears (`quranic:root_001117:B003/m01`); setting out to hunt (`quranic:root_000745:B006/m01`); successive taking of prey (`quranic:root_000993:B008/m01`); quarry running and stopping to look back (`quranic:root_001290:B007/m01`).
- Ayah anchors: 64:1,3,4 `ٱلسَّمَاوَات`; 64:3 `صَوَّرَكُمْ`; 64:6 `رُسُلُهُم`; 64:8 `رَسُولِهِ`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`; 64:7 `رَبِّي`; 64:9 `جَنَّاتٍ`; 64:10 `كَذَّبُوا`, `ٱلْمَصِيرُ`; 64:14 `عَدُوًّا`; 64:18 `ٱلْغَيْبِ`.
- Synthesis: Pursuit and enclosure add dynamics to gathering: members do not simply appear together but may flee, look back, follow in batches, and enter shelter. That scene pressures the surah's alternation between summons, turning-away, and final compulsory assembly.

#### Subchannel C. Pairing and Classification Within the Gathered Set
- Reading type: mixed
- Scene or process: Members are matched with counterparts, sorted by kind or conduct, and recognized as companions, peers, or opposed pairs.
- Active motifs: one of a paired couple (`quranic:root_000652:B001/m01`); joining one thing as the counterpart of another (`quranic:root_000652:B003/m01`); class, kind, or species (`quranic:root_000652:B004/m01`); peers joined by likeness or action (`quranic:root_000652:B005/m01`); social categories or tribes (`quranic:root_001198:B009/m02`); age-peer (`quranic:root_001683:B006/m01`); companion defined by close association (`quranic:root_000844:B001/m01`); connection joining opposed sides (`quranic:root_000170:B003/m01`).
- Ayah anchors: 64:5 `قَبْلُ`; 64:6,12 `بَيِّنَات`, `مُبِين`; 64:10 `أَصْحَابُ`; 64:14 `أَزْوَاجِكُمْ`; 64:14-15 `أَوْلَادِكُمْ`.
- Synthesis: Pairing is not limited to marriage: likeness, opposition, age, conduct, and affiliation can all determine a counterpart. This gives the gathered multitude an internal structure through which companions of the garden and companions of the fire become classified relations.

#### Subchannel D. Lots, Portions, and the Disclosure of Gain or Loss
- Reading type: latent/lexical
- Scene or process: A collected stake is divided by marked arrows; each participant receives a portion, and the draw exposes winner, deficit, or exclusion.
- Active motifs: gambling by arrows and division of a slaughtered animal (`quranic:root_001694:B007/m01`); container holding the lot-arrows (`quranic:root_000532:B010/m01`); a named arrow in the lot (`quranic:root_000867:B011/m01`); the fifth gambling arrow (`quranic:root_001533:B016/m01`); winning and carrying away the allotted good (`quranic:root_001186:B001/m02`); loss through an unequal transaction (`quranic:root_001072:B001/m01`); a closed-hand portion (`quranic:root_000259:B005/m01`); fixed portion and measure (`quranic:root_001205:B001/m01`).
- Ayah anchors: 64:1 `قَدِيرٌ`; 64:7 `رَبِّي`, `يَسِيرٌ`; 64:9 `يَجْمَعُكُمْ`, `يَوْمُ ٱلتَّغَابُنِ`, `ٱلْفَوْزُ`; 64:14 `تَصْفَحُوا`; 64:16 `أَنفُسِكُمْ`.
- Synthesis: The lot scene gives mutual gain and loss a visible apparatus: one collective body, finite shares, and an outcome no participant controls after the draw. The surah reverses that uncertainty by tying the final allotment to disclosed belief and work rather than chance.

### 10. Household Bonds Under Hostile Pressure
- Semantic invariant: The closest bodily and genealogical bonds create care, dependency, property, and loyalty, yet those same bonds can reverse into obstruction or hostility and require deliberate repair.
- Surface relation: direct; spouses and children may be enemies at 64:14, wealth and children are trial at 64:15, and caution is followed by pardon, overlooking, forgiveness, and mercy at 64:14.
- Surprising reach: Marriage is rendered as pairing, skin contact, contract, and a bride's transfer; parenthood as womb, afterbirth, navel, and nursing; kinship as inheritance and clientage. The threat arises inside the bond's actual machinery, not from a generic “family domain.”

#### Subchannel A. Pair, Contract, and Intimate Union
- Reading type: mixed
- Scene or process: Two parties become spouses through pairing and contract, enter bodily intimacy, and can later face separation, widowhood, or renewed courtship.
- Active motifs: marital spouse (`quranic:root_000652:B002/m01`); making one party the mate of another (`quranic:root_000652:B003/m02`); marital consummation (`quranic:root_000464:B002/m01`); skin-to-skin contact (`quranic:root_000120:B003/m01`); sexual union (`quranic:root_000259:B006/m01`); euphemism for intercourse (`quranic:root_000810:B006/m01`); emission of semen (`quranic:root_001492:B009/m01`); marriage contract (`quranic:root_001444:B004/m01`); bride conveyed to her husband (`quranic:root_001583:B006/m01`); widow or divorcee receiving suitors (`quranic:root_000563:B009/m01`); divorce cutting off return (`quranic:root_000170:B012/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`; 64:6 `بَشَرٌ`, `رُسُلُهُم`, `بَيِّنَات`, `يَهْدُونَنَا`; 64:8 `رَسُولِهِ`, `أَنزَلْنَا`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`, `مُبِين`; 64:9 `يَجْمَعُ`, `يُدْخِلْ`; 64:11 `يَهْدِ`; 64:14 `أَزْوَاجِكُمْ`; 64:17 `شَكُورٌ`.
- Synthesis: Pairing, contract, bodily entry, and social transfer are distinct steps in one union. Because the bond is structured and consequential, its reversal into hostility at 64:14 is sharper than ordinary disagreement: an institution built for nearness can redirect allegiance.

#### Subchannel B. Womb, Birth, and the Dependent Child
- Reading type: mixed
- Scene or process: A child develops under cover, emerges through birth with bodily traces, and enters a period of dependence under parents or a caregiver.
- Active motifs: child descended from a parent (`quranic:root_001683:B001/m01`); father and mother as parents (`quranic:root_001683:B002/m01`); childbirth and delivery (`quranic:root_001683:B003/m01`); newborn or dependent child (`quranic:root_001683:B004/m01`); womb as the child's vessel (`quranic:root_000552:B003/m01`); fetus hidden in the womb (`quranic:root_000266:B007/m01`); childbirth and postpartum blood (`quranic:root_001533:B005/m01`); receiver of the emerging infant (`quranic:root_001198:B007/m01`); navel and severed cord-remnant (`quranic:root_000697:B006/m01`); afterbirth as evidence of delivery (`quranic:root_000822:B006/m01`); womb and discharge following birth (`quranic:root_000994:B009/m01`); stepchild and responsible carer (`quranic:root_000532:B005/m01`).
- Ayah anchors: 64:4 `تُسِرُّونَ`; 64:5 `عَذَابٌ`; 64:7 `رَبِّي`; 64:9 `جَنَّاتٍ`; 64:14 `رَحِيمٌ`, `أَوْلَادِكُمْ`; 64:15 `أَوْلَادُكُمْ`; 64:16 `أَنفُسِكُمْ`; 64:18 `ٱلشَّهَادَةِ`; 64:5 `قَبْلُ`.
- Synthesis: Hidden fetus, birth, afterbirth, cord, and care make “children” a temporal relation of radical dependency. That dependence explains both the bond's power over action and the need to distinguish care for the child from surrender to the child's contrary demand.

#### Subchannel C. Kinship, Inheritance, and Acquired Allegiance
- Reading type: latent/lexical
- Scene or process: Belonging is transmitted by blood, marriage, inheritance, neighborhood, or manumission, producing overlapping claims of support and succession.
- Active motifs: close kinship and its duties (`quranic:root_000552:B002/m01`); collateral inheritance outside parent and child (`quranic:root_001315:B004/m01`); clientage, kinship, and manumission bond (`quranic:root_001684:B005/m01`); tribe and lineage group (`quranic:root_001198:B009/m02`); age-peer relation (`quranic:root_001683:B006/m01`); grown son becoming his father's companion (`quranic:root_000844:B005/m01`); stepchild and blended-household relation (`quranic:root_000532:B005/m01`); connective bond holding parties together (`quranic:root_000170:B003/m01`).
- Ayah anchors: 64:5 `قَبْلُ`; 64:6 `بَيِّنَات`, `تَوَلَّوْا`; 64:12 `مُبِين`, `تَوَلَّيْتُمْ`; 64:7 `رَبِّي`; 64:10 `أَصْحَابُ`; 64:11 `كُلِّ`; 64:14 `رَحِيمٌ`, `أَوْلَادِكُمْ`; 64:15 `أَوْلَادُكُمْ`.
- Synthesis: Allegiance is not exhausted by descent. Collateral inheritance, clientage, neighborhood, and blended parenting show several routes by which another person acquires standing. This complicates the simple opposition of family and enemy: the same social network can carry care, property, and conflict.

#### Subchannel D. Intimate Enemy, Caution, and Relational Repair
- Reading type: surface-primary
- Scene or process: A spouse or child becomes an opposing force; the believer remains alert without dissolving the bond, then uses pardon, overlooking, forgiveness, and reconciliation to repair it.
- Active motifs: enemy opposed to ally (`quranic:root_000993:B003/m01`); loving and supporting ally (`quranic:root_001684:B004/m01`); marital spouse (`quranic:root_000652:B002/m01`); child (`quranic:root_001683:B001/m01`); vigilant caution (`quranic:root_000301:B001/m01`); waiving punishment (`quranic:root_001032:B001/m01`); graceful overlooking (`quranic:root_000867:B002/m01`); covering the offense (`quranic:root_001096:B002/m01`); mercy and tenderness (`quranic:root_000552:B001/m01`); reconciliation that removes aversion (`quranic:root_000876:B002/m01`); feud or hostility arising among people (`quranic:root_001564:B007/m01`); social conflict and killing (`quranic:root_001128:B006/m01`).
- Ayah anchors: 64:6 `تَوَلَّوْا`; 64:12 `تَوَلَّيْتُمْ`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`; 64:9 `صَالِحًا`; 64:14 `أَزْوَاجِكُمْ`, `أَوْلَادِكُمْ`, `عَدُوًّا`, `فَٱحْذَرُوهُمْ`, `تَعْفُوا`, `تَصْفَحُوا`, `تَغْفِرُوا`, `رَحِيمٌ`; 64:15 `فِتْنَةٌ`.
- Synthesis: The repair sequence does not deny enmity; it regulates the response to it. Caution protects direction, pardon suspends retaliation, overlooking withdraws accusatory attention, forgiveness covers the residue, and mercy preserves the possibility of restored alliance.

### 11. The Inner Center That Can Be Guided, Turned, or Constricted
- Semantic invariant: The heart and self form an interior center where knowledge, intention, security, greed, and direction become embodied states capable of reversal.
- Surface relation: direct; God knows what is in the breasts at 64:4, guides the believer's heart at 64:11, calls believers to trust at 64:13, and locates avarice within the self at 64:16.
- Surprising reach: The heart is at once organ, hidden chamber, mainstay, jewel-center, and turning mechanism; trust steadies it, while greed narrows its internal economy and trial can strike it as disease.

#### Subchannel A. Heart Inside the Ribbed Chest
- Reading type: mixed
- Scene or process: A vital and cognitive center is housed within chest and ribs, concealed yet structurally central to the body's action.
- Active motifs: heart as organ (`quranic:root_001248:B001/m01`); heart as understanding and inward discernment (`quranic:root_001248:B001/m02`); hidden heart within the breast (`quranic:root_000266:B010/m01`); bodily chest (`quranic:root_000849:B001/m01`); ribs or chest bones (`quranic:root_000266:B016/m01`); chest or breast (`quranic:root_001315:B007/m01`); heart as the body's mainstay (`quranic:root_001444:B005/m01`); insight of the heart (`quranic:root_000121:B002/m01`); thought settled in the heart (`quranic:root_000429:B004/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`; 64:2 `بَصِيرٌ`; 64:4 `ٱلصُّدُورِ`; 64:9 `جَنَّاتٍ`; 64:10 `خَالِدِينَ`; 64:11 `قَلْبَهُ`, `كُلِّ`.
- Synthesis: The chest scene joins anatomy and cognition without collapsing them. The heart is hidden because it is physically enclosed and epistemically interior, yet it is also the mainstay from which action and interpretation are organized.

#### Subchannel B. A Heart Reoriented Toward the Right Course
- Reading type: surface-primary
- Scene or process: The inner center is turned from one face to another, brought onto a sound course, and stabilized by accepted truth.
- Active motifs: turning a thing from face to face (`quranic:root_001248:B004/m01`); inward return and destination (`quranic:root_001248:B005/m01`); guidance toward truth (`quranic:root_001583:B001/m01`); rightness opposed to error (`quranic:root_000889:B002/m01`); inclination away from the true course (`quranic:root_001128:B003/m01`); turning toward and accepting (`quranic:root_001684:B006/m01`); turning away and refusing (`quranic:root_001684:B007/m01`); belief settled as trusted assent (`quranic:root_000054:B002/m01`).
- Ayah anchors: 64:2 `مُؤْمِنٌ`; 64:8 `فَـَٔامِنُوا`; 64:9,11 `يُؤْمِن`; 64:13 `ٱلْمُؤْمِنُونَ`; 64:14 `ءَامَنُوا`; 64:6 `يَهْدُونَنَا`, `تَوَلَّوْا`; 64:11 `يَهْدِ`, `قَلْبَهُ`, `مُصِيبَةٍ`; 64:12 `تَوَلَّيْتُمْ`; 64:15 `فِتْنَةٌ`.
- Synthesis: Guidance acts on orientation rather than merely adding information. A heart may know a proposition yet face away from it; faith turns and settles the center so that calamity is interpreted from the right direction.

#### Subchannel C. Breath, Blood, Life, and Inner Intention
- Reading type: mixed
- Scene or process: Breath and blood sustain the living self, while intention, character, and relief describe the interior's non-visible motions.
- Active motifs: breath leaving the interior (`quranic:root_001533:B001/m01`); lifeblood (`quranic:root_001533:B004/m01`); life-sustaining water (`quranic:root_001533:B008/m01`); living soul or life (`quranic:root_001533:B011/m01`); self as the thing's own essence (`quranic:root_001533:B012/m01`); inward intention and reflection (`quranic:root_001533:B013/m01`); force and moral character of the self (`quranic:root_001533:B014/m01`); relief that opens constriction (`quranic:root_001533:B002/m01`); inward joy and ease (`quranic:root_000697:B010/m01`).
- Ayah anchors: 64:4 `تُسِرُّونَ`; 64:16 `أَنفُسِكُمْ`, `نَفْسِهِ`.
- Synthesis: The self is neither a generic person nor a disembodied soul. Breath, blood, water, intention, and character form nested life processes, allowing expenditure “for yourselves” to mean preservation and reformation of the inner agent rather than simple material loss.

#### Subchannel D. Security and Reliance Against the Self's Grasp
- Reading type: mixed
- Scene or process: Trust and familiarity settle the self, while greed and competition constrict it around a valued object and make every transfer feel like danger.
- Active motifs: calm security and entrusted reliability (`quranic:root_000054:B001/m01`); familiarity and relaxed openness (`quranic:root_000563:B007/m01`); reliance on another (`quranic:root_001681:B002/m01`); greedy withholding (`quranic:root_000778:B001/m01`); rivalry to prevent losing a share (`quranic:root_000778:B002/m01`); a precious thing over which selves compete (`quranic:root_001533:B010/m01`); self-sufficiency and freedom from need (`quranic:root_001110:B001/m01`); safety expressed as absence of harm (`quranic:root_000079:B005/m01`); putting the self in protection (`quranic:root_001677:B002/m01`).
- Ayah anchors: 64:2 `مُؤْمِنٌ`; 64:8 `فَـَٔامِنُوا`; 64:9,11 `يُؤْمِن`; 64:13 `ٱلْمُؤْمِنُونَ`; 64:14 `ءَامَنُوا`; 64:6 `ٱسْتَغْنَى`, `غَنِيٌّ`, `رُسُلُهُم`; 64:8 `رَسُولِهِ`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`; 64:10 `بِئْسَ`; 64:13 `فَلْيَتَوَكَّلِ`; 64:16 `شُحَّ`, `نَفْسِهِ`, `ٱتَّقُوا`.
- Synthesis: Greed is a failed security strategy: it narrows the self around possession, whereas trust permits outward action without panic. Divine self-sufficiency supplies the contrast, since God's giving and acknowledgment do not arise from need.

### 12. Praise, Gratitude, and Increase Made Visible
- Semantic invariant: A received good is recognized, spoken of, and embodied in conduct; genuine acknowledgment lets benefit circulate and increase, while ingratitude covers its source.
- Surface relation: direct; praise belongs to God at 64:1, God is rich and praiseworthy at 64:6, and God is appreciative and forbearing in the multiplied-loan sequence at 64:17.
- Surprising reach: Gratitude appears not only as speech but as an animal thriving on little feed, an udder filling, shoots emerging, and rain intensifying; acknowledgment is the visibility of productive response.

#### Subchannel A. Praise Opposed to Public Blame
- Reading type: mixed
- Scene or process: A quality or act is publicly evaluated, producing praise, reputation, blame, or a circulating judgment.
- Active motifs: praise opposed to blame (`quranic:root_000355:B001/m01`); bearer of many praised qualities (`quranic:root_000355:B003/m01`); praiseworthy endpoint (`quranic:root_000355:B004/m01`); formula of blame (`quranic:root_000079:B004/m01`); “bad” functioning as formal condemnation (`quranic:root_000755:B006/m01`); reciprocal praise or blame (`quranic:root_001217:B005/m02`); good reputation spreading (`quranic:root_000745:B008/m01`); report or reputation circulating among people (`quranic:root_000741:B005/m01`).
- Ayah anchors: 64:1,6 `ٱلْحَمْدُ`, `حَمِيدٌ`; 64:9 `سَيِّـَٔاتِ`; 64:10 `بِئْسَ`; 64:16 `ٱسْمَعُوا`; 64:17 `قَرْضًا`; 64:1,3,4 `ٱلسَّمَاوَات`.
- Synthesis: Praise is treated as a reasoned public verdict, not flattery. The polarity with formal blame links the opening *ḥamd* to the closing evaluations of success and bad destination, while circulating reputation previews the full disclosure of deeds.

#### Subchannel B. Gratitude as Productive Response
- Reading type: mixed
- Scene or process: A small provision is received and converted into visible bodily or vegetal increase, making the recipient's response observable.
- Active motifs: acknowledging and displaying a benefit (`quranic:root_000810:B001/m01`); an animal thriving on little feed (`quranic:root_000810:B002/m01`); full udder and abundant milk (`quranic:root_000810:B003/m01`); tender shoot emerging (`quranic:root_000810:B004/m01`); rain or wind intensifying (`quranic:root_000810:B005/m01`); ingratitude that covers the benefit (`quranic:root_001307:B004/m01`); claiming credit and demanding praise for giving (`quranic:root_000355:B005/m01`); giving freely and with ease (`quranic:root_000563:B010/m01`).
- Ayah anchors: 64:1,6 `ٱلْحَمْدُ`, `حَمِيدٌ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`; 64:6 `رُسُلُهُم`; 64:8 `رَسُولِهِ`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`; 64:17 `شَكُورٌ`.
- Synthesis: The grateful recipient does not merely say thanks; it turns input into flourishing. That makes divine *shukr* in 64:17 a promise that the offered good will not disappear unnoticed but will be made productively visible in its return.

#### Subchannel C. Benefaction and Reciprocal Acknowledgment
- Reading type: mixed
- Scene or process: A gift or surplus moves toward another, creates benefit, and returns as acknowledgment, recompense, or successful attainment.
- Active motifs: generosity and gift (`quranic:root_000452:B005/m01`); doing good beyond strict justice (`quranic:root_000323:B002/m03`); freely available surplus (`quranic:root_001032:B003/m01`); giving with an open disposition (`quranic:root_000563:B010/m01`); reciprocal recompense (`quranic:root_001217:B005/m01`); reciprocal praise (`quranic:root_001217:B005/m02`); gift sent to one held in affection (`quranic:root_001583:B004/m01`); wage or beneficial return (`quranic:root_000015:B001/m01`); attaining good and escaping harm (`quranic:root_001186:B001/m01`).
- Ayah anchors: 64:3,17 `أَحْسَنَ`, `حَسَنًا`; 64:6 `رُسُلُهُم`, `يَهْدُونَنَا`; 64:8 `رَسُولِهِ`; 64:11 `يَهْدِ`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`; 64:9 `ٱلْفَوْزُ`; 64:14 `تَعْفُوا`; 64:15 `أَجْرٌ`; 64:16 `خَيْرًا`; 64:17 `قَرْضًا`.
- Synthesis: Gift, loan, and wage remain distinct transactions but share a return-bearing relation. The affectionate gift is especially useful: value can move because of love rather than shortage, aligning divine acknowledgment with abundance rather than dependence.

### 13. Illumination That Guides and Fire That Transforms
- Semantic invariant: Radiant force makes a state visible and actionable, but the same luminous field can guide, expose, mature, burn, or punish according to what receives it.
- Surface relation: direct; the sent-down light appears at 64:8, the fire at 64:10, clear signs at 64:6, and trial at 64:15.
- Surprising reach: Light becomes a road beacon, daylight's opening, blossom, and the first sign before completion; fire becomes both destructive destination and assayer that reveals composition.

#### Subchannel A. Light as Beacon and Legible Direction
- Reading type: mixed
- Scene or process: Illumination reveals a marker, makes its distinction visible, and permits the observer to orient toward a route or truth.
- Active motifs: light and illumination (`quranic:root_001564:B001/m01`); visible beacon or minaret (`quranic:root_001564:B005/m01`); manifest sign (`quranic:root_000074:B003/m01`); distinguishing landmark (`quranic:root_001040:B002/m01`); clear evidence (`quranic:root_000170:B004/m01`); gentle guidance (`quranic:root_001583:B001/m01`); indicator witnessing a condition (`quranic:root_000822:B008/m01`); elevated visible figure (`quranic:root_000745:B002/m01`).
- Ayah anchors: 64:1,3,4 `ٱلسَّمَاوَات`; 64:4 `يَعْلَمُ`, `عَلِيمٌ`; 64:11 `عَلِيمٌ`; 64:18 `عَالِمُ`, `ٱلشَّهَادَةِ`; 64:6 `بَيِّنَات`, `يَهْدُونَنَا`; 64:8 `ٱلنُّورِ`; 64:10 `بِـَٔايَاتِنَا`; 64:11 `يَهْدِ`.
- Synthesis: Light is useful because it reveals differences and directions, not merely because it is bright. Beacon, sign, and guide form a complete orientation scene in which revelation both appears and enables movement.

#### Subchannel B. Fire as Assay, Mark, and Punishment
- Reading type: mixed
- Scene or process: Fire applies heat that illuminates, marks, separates material quality, or consumes the subject that cannot pass through it.
- Active motifs: burning fire and branding flame (`quranic:root_001564:B002/m01`); testing and blackening by fire (`quranic:root_001128:B002/m01`); assaying metal or person (`quranic:root_001128:B001/m01`); painful punishment (`quranic:root_000994:B005/m01`); heavy harmful consequence (`quranic:root_001619:B002/m01`); fire or hardship descending as disaster (`quranic:root_001492:B006/m01`); hard impact on the self (`quranic:root_001008:B005/m01`).
- Ayah anchors: 64:5 `وَبَالَ`, `عَذَابٌ`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`; 64:15 `فِتْنَةٌ`; 64:18 `ٱلْعَزِيزُ`; 64:8 `أَنزَلْنَا`.
- Synthesis: Assay and punishment share heat but not outcome. Assay reveals and separates quality; punitive fire fixes the consequence of a quality already disclosed. The relation makes trial a prior, diagnostic encounter with what final fire makes irreversible.

#### Subchannel C. Dawn, Blossom, and the Opening of Visibility
- Reading type: latent/lexical
- Scene or process: Darkness recedes as dawn opens, light spreads like a widening current, and plant life announces maturity through blossom.
- Active motifs: dawn breathing open (`quranic:root_001533:B009/m01`); daylight opening in brightness (`quranic:root_001559:B002/m01`); opening and widening until flow occurs (`quranic:root_001559:B003/m01`); blossom emerging on a tree (`quranic:root_001564:B004/m01`); smile or lightning appearing from cloud (`quranic:root_001315:B011/m01`); first signs of dawn, rain, or ripening (`quranic:root_000120:B007/m01`); continuous flowing movement (`quranic:root_000240:B001/m01`); night covering the scene (`quranic:root_000266:B002/m01`); crescent hidden at month's end (`quranic:root_000697:B004/m01`).
- Ayah anchors: 64:6 `بَشَرٌ`; 64:9 `تَجْرِي`, `جَنَّاتٍ`, `ٱلْأَنْهَارُ`; 64:11 `كُلِّ`; 64:16 `أَنفُسِكُمْ`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`; 64:4 `تُسِرُّونَ`.
- Synthesis: Visibility arrives progressively: first sign, widening light, blossom, then full flow. This sequence gives revelation and resurrection a shared morphology of emergence without reducing either to a simple sunrise metaphor.

### 14. Appointed Time, Cessation, and the Enduring Abode
- Semantic invariant: A bounded event arrives, interrupts an earlier state, and carries its subjects toward cessation, reactivation, or a durable final residence.
- Surface relation: direct; 64:7 asserts resurrection and disclosure, 64:9 names the gathering day and eternal garden, and 64:10 names eternal fire and the bad destination.
- Surprising reach: The afterlife sequence is materialized through waking a sleeping or kneeling body, extinction of a lineage, burial under cover, a deserted dwelling, and permanent residence; even “winning” has a death-sense that pressures easy equations of worldly success with survival.

#### Subchannel A. Day as Bounded Time and Decisive Event
- Reading type: mixed
- Scene or process: A duration is marked, approaches from “before,” convenes its participants, and becomes the event by which an earlier condition is decisively changed.
- Active motifs: daylight as a bounded interval (`quranic:root_001700:B001/m01`); day as an unspecified duration (`quranic:root_001700:B002/m01`); “day” as decisive occurrence (`quranic:root_001700:B003/m01`); appointed gathering day (`quranic:root_000259:B004/m01`); attendance and presence at an assembly (`quranic:root_000822:B001/m01`); marker or appointed time (`quranic:root_000051:B005/m01`); temporal precedence and the coming period (`quranic:root_001198:B002/m01`); event occurring in time (`quranic:root_001332:B001/m01`).
- Ayah anchors: 64:5 `أَمْرِهِم`, `قَبْلُ`; 64:6 `كَانَت`; 64:9 `يَوْمَ`, `يَوْمِ`, `يَوْمُ`, `يَجْمَعُكُمْ`, `ٱلْجَمْعِ`; 64:18 `ٱلشَّهَادَةِ`.
- Synthesis: The day is both calendar unit and event-container. By gathering participants into an appointed interval, it converts duration into adjudicative presence: a time becomes “the Day” because of what is made to occur and appear within it.

#### Subchannel B. Staying, Clinging, and Durable Residence
- Reading type: mixed
- Scene or process: A subject ceases moving away, adheres to a place or state, and remains through an indefinitely extended duration.
- Active motifs: unending duration (`quranic:root_000004:B001/m01`); remaining in a place without departure (`quranic:root_000004:B006/m01`); stable survival not quickly touched by decay (`quranic:root_000429:B001/m01`); clinging and taking up residence (`quranic:root_000429:B002/m01`); remaining and abiding (`quranic:root_000532:B007/m01`); long residence in a dwelling (`quranic:root_001110:B004/m01`); place of settled return (`quranic:root_000897:B007/m01`); dwelling and rank (`quranic:root_001492:B003/m01`).
- Ayah anchors: 64:3,10 `ٱلْمَصِيرُ`; 64:6 `غَنِيٌّ`; 64:7 `رَبِّي`; 64:8 `أَنزَلْنَا`; 64:9 `أَبَدًا`, `خَالِدِينَ`; 64:10 `خَالِدِينَ`.
- Synthesis: Permanence is built from duration plus adhesion plus residence. This layered account distinguishes merely lasting a long time from being fixed in an abode whose state no longer admits departure.

#### Subchannel C. Death, Extinction, and Burial Under Cover
- Reading type: latent/lexical
- Scene or process: Life or a group is cut off, overpowered, or exhausted; the dead is then concealed in a grave that becomes a final earthly lodging.
- Active motifs: destruction or severe illness arriving (`quranic:root_000009:B011/m01`); “winning” used for death or passing away (`quranic:root_001186:B002/m01`); extinction of a person or people (`quranic:root_001217:B009/m01`); exhaustion, disappearance, or death (`quranic:root_001537:B001/m01`); illness or death gaining mastery (`quranic:root_001008:B009/m01`); burial in a grave (`quranic:root_001117:B009/m01`); covering the dead (`quranic:root_000266:B009/m01`); grave as settled lodging (`quranic:root_000897:B007/m02`); deadly waterless waste (`quranic:root_001186:B003/m01`).
- Ayah anchors: 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:9 `ٱلْفَوْزُ`, `جَنَّاتٍ`; 64:10 `ٱلْمَصِيرُ`; 64:16 `أَنفِقُوا`; 64:17 `قَرْضًا`; 64:18 `ٱلْعَزِيزُ`, `ٱلْغَيْبِ`.
- Synthesis: The death-sense of “winning” is a productive reversal: departure can be named success even when worldly continuity ends. Extinction and burial therefore pressure the surah's final victory to specify what survives, where it resides, and by whose valuation it wins.

#### Subchannel D. Rousing, Dispatching, and Resurrection
- Reading type: surface-primary
- Scene or process: A still or sleeping body is stirred, rises into movement, and is sent forward to face the report of its earlier actions.
- Active motifs: rousing a sleeper or kneeling animal (`quranic:root_000129:B001/m01`); dispatching one who has been raised (`quranic:root_000129:B002/m01`); springing forward into motion (`quranic:root_000129:B004/m01`); consequential report delivered (`quranic:root_001464:B002/m01`); turning from one state to another (`quranic:root_001248:B004/m02`); becoming and reaching an outcome (`quranic:root_000897:B001/m01`); reaching and taking the goal (`quranic:root_001684:B012/m01`); coming out from one land among another people (`quranic:root_001464:B001/m01`).
- Ayah anchors: 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:6 `تَوَلَّوْا`; 64:12 `تَوَلَّيْتُمْ`; 64:7 `يُبْعَثُوا`, `لَتُبْعَثُنَّ`; 64:10 `ٱلْمَصِيرُ`; 64:11 `قَلْبَهُ`.
- Synthesis: Resurrection is decomposed into activation, rise, dispatch, and encounter with news. The animal image keeps the event bodily: the subject is not merely remembered but brought out of stillness into directed accountability.

#### Subchannel E. Garden and Fire as Final Companion-Abodes
- Reading type: surface-primary
- Scene or process: Subjects enter one of two destinations, become its companions, and remain in a state whose value is named as victory or blame.
- Active motifs: entering an interior (`quranic:root_000464:B001/m01`); tree-covered garden (`quranic:root_000266:B003/m01`); river in a cut flowing course (`quranic:root_001559:B001/m01`); enduring permanence (`quranic:root_000429:B001/m01`); companions attached to a thing (`quranic:root_000844:B001/m01`); burning fire (`quranic:root_001564:B002/m01`); settled destination (`quranic:root_000897:B007/m01`); salvation and attainment of good (`quranic:root_001186:B001/m01`); formal blame (`quranic:root_000079:B004/m01`).
- Ayah anchors: 64:9 `يُدْخِلْهُ`, `جَنَّاتٍ`, `ٱلْأَنْهَارُ`, `خَالِدِينَ`, `ٱلْفَوْزُ`; 64:10 `أَصْحَابُ ٱلنَّارِ`, `خَالِدِينَ`, `بِئْسَ ٱلْمَصِيرُ`.
- Synthesis: Destination, companionship, and permanence are distinct: one names where, one names belonging, and one names duration. Their conjunction makes the two outcomes full social habitats rather than isolated rewards and penalties.

### 15. Place, Belonging, and the Terrain Between Homes
- Semantic invariant: Bodies and groups acquire meaning from where they can remain, who admits them, and what route or terrain separates habitation from estrangement.
- Surface relation: indirect; earth and sky recur at 64:1,3-4, reports and messengers arrive at 64:5-8, guidance occurs at 64:6,11, and proximity within spouse and child relations is tested at 64:14-15.
- Surprising reach: Belonging is rendered as settlement, erased ruins, an outsider entering another people, a waterless waste beyond hearing and sight, and hard or soft terrain that changes movement.

#### Subchannel A. Settled Dwelling and Erased Ruin
- Reading type: latent/lexical
- Scene or process: A place is inhabited and furnished for rest, then abandoned until its people and tracks disappear.
- Active motifs: deserted and emptied dwelling (`quranic:root_000004:B003/m01`); tracks and structures erased (`quranic:root_001032:B006/m01`); fixed residence without departure (`quranic:root_000004:B006/m01`); long dwelling in a place (`quranic:root_001110:B004/m01`); house or settled station (`quranic:root_001492:B003/m01`); couch or place of repose (`quranic:root_000697:B011/m01`); isolated settlement (`quranic:root_001307:B012/m02`); grave (`quranic:root_001307:B012/m03`); place and social station (`quranic:root_001332:B002/m01`); presence at a place (`quranic:root_000822:B001/m01`).
- Ayah anchors: 64:6 `غَنِيٌّ`, `كَانَت`; 64:8 `أَنزَلْنَا`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`, `أَبَدًا`; 64:14 `تَعْفُوا`; 64:18 `ٱلشَّهَادَةِ`; 64:4 `تُسِرُّونَ`.
- Synthesis: Habitation is read through its reversibility: the same place can be home, station, ruin, or grave. Erasure of tracks makes abandonment visible by absence, giving prior destroyed peoples a spatial afterimage without reducing their story to a surface summary.

#### Subchannel B. Stranger Entering Another People
- Reading type: latent/lexical
- Scene or process: A person crosses from one land into a group not originally his own, becomes an entrant or companion, and negotiates nearness and recognition.
- Active motifs: stranger among a people not his own (`quranic:root_000009:B006/m01`); “son of the earth” as outsider (`quranic:root_000025:B004/m01`); entrant mixed into another group (`quranic:root_000464:B005/m01`); movement from one country to another (`quranic:root_001464:B001/m01`); companion through sustained association (`quranic:root_000844:B001/m01`); proximity without interval (`quranic:root_001684:B001/m01`); familiarity and ease with another (`quranic:root_000563:B007/m01`); relation that joins separate sides (`quranic:root_000170:B003/m01`).
- Ayah anchors: 64:1,3,4 `ٱلْأَرْض`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:6 `رُسُلُهُم`, `بَيِّنَات`, `تَوَلَّوْا`; 64:8 `رَسُولِهِ`; 64:12 `ٱلرَّسُولَ`, `رَسُولِنَا`, `مُبِين`, `تَوَلَّيْتُمْ`; 64:9 `يُدْخِلْ`; 64:10 `أَصْحَابُ`.
- Synthesis: Arrival does not guarantee belonging. The outsider scene adds social reception to physical motion: entry, sustained companionship, and recognized proximity are separate transitions, each vulnerable to rejection or hidden divided allegiance.

#### Subchannel C. Crossing the Remote Waterless Waste
- Reading type: latent/lexical
- Scene or process: A traveler traverses a broad uninhabited distance beyond ordinary hearing and sight, relying on water, road, and guide to reach safety.
- Active motifs: empty wide wilderness (`quranic:root_000778:B005/m01`); desert poised between escape and death (`quranic:root_001186:B003/m01`); broad gap and remoteness (`quranic:root_000170:B006/m01`); spatial breadth and long interval (`quranic:root_001533:B015/m01`); remote land cut off from people (`quranic:root_001307:B012/m01`); land where nobody hears or sees (`quranic:root_000741:B014/m01`); water by which travelers secure their affairs (`quranic:root_001444:B007/m01`); clear road across easy land (`quranic:root_001464:B007/m01`); public road and junction (`quranic:root_000009:B010/m01`); guidance to the path (`quranic:root_001583:B001/m01`).
- Ayah anchors: 64:1 `ٱلْمُلْكُ`; 64:5-6 `يَأْتِكُمْ`, `تَأْتِيهِم`; 64:5,7 `نَبَؤُا`, `لَتُنَبَّؤُنَّ`; 64:6,12 `بَيِّنَات`, `مُبِين`; 64:6 `يَهْدُونَنَا`; 64:11 `يَهْدِ`; 64:9 `ٱلْفَوْزُ`; 64:16 `ٱسْمَعُوا`, `أَنفُسِكُمْ`, `شُحَّ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`.
- Synthesis: The desert makes guidance existentially concrete: wrong direction consumes distance, water, and life. It also reframes victory as successful passage through a place whose name can signify both salvation and destruction.

#### Subchannel D. Vertical Terrain from Sky Canopy to Cut Ground
- Reading type: mixed
- Scene or process: Sky, ground, hollow, slope, hard ridge, and soft basin form a vertical terrain that governs descent, retention, and passage.
- Active motifs: ground below the sky (`quranic:root_000025:B001/m01`); sky or canopy overhead (`quranic:root_000745:B004/m01`); lower direction (`quranic:root_000177:B001/m01`); depression in which things disappear (`quranic:root_001117:B002/m01`); hard cohesive ground (`quranic:root_001008:B007/m01`); uneven solid terrain (`quranic:root_000993:B010/m01`); rough elevated ground to be avoided (`quranic:root_000301:B004/m01`); soft low water-holding ground (`quranic:root_000387:B002/m01`); descending a slope (`quranic:root_000889:B005/m01`); river cutting open the land (`quranic:root_001559:B001/m01`).
- Ayah anchors: 64:1,3,4 `ٱلسَّمَاوَات`, `ٱلْأَرْض`; 64:8 `خَبِيرٌ`; 64:9 `تَحْتِهَا ٱلْأَنْهَارُ`; 64:11 `مُصِيبَةٍ`; 64:14 `فَٱحْذَرُوهُمْ`, `عَدُوًّا`; 64:18 `ٱلْعَزِيزُ`, `ٱلْغَيْبِ`.
- Synthesis: The cosmological pair “heavens and earth” is given internal topography. Canopy, slope, ridge, hollow, and basin explain how descending force is either shed, resisted, hidden, or gathered, linking creation's scale to the local mechanics of calamity and provision.

## Standalone Subchannels

### S1. Worshipper Oriented by Name, Direction, and Count
- Reading type: latent/lexical
- Scene or process: A worshipper invokes the divine name, faces a prayer direction, performs praise, and counts the repeated act on beads amid a fragrant ritual setting.
- Active motifs: worship directed to the divine (`quranic:root_000047:B001/m01`); prayer, praise, and devotional remembrance (`quranic:root_000666:B001/m01`); direction faced in prayer (`quranic:root_001198:B005/m01`); beads used to count praise (`quranic:root_000666:B006/m01`); fragrant aloeswood burned as incense (`quranic:root_000076:B014/m01`); divine name in invocation (`quranic:root_000047:B002/m01`); saying “amen” as a request for response (`quranic:root_000054:B003/m01`).
- Ayah anchors: recurrent 64:1-2,4,6-9,11-17 `ٱللَّه`; 64:1 `يُسَبِّحُ`; 64:2 `مُؤْمِنٌ`; 64:8 `فَـَٔامِنُوا`; 64:9,11 `يُؤْمِن`; 64:13 `ٱلْمُؤْمِنُونَ`; 64:14 `ءَامَنُوا`; 64:5 `قَبْلُ`. Surface anchor is unavailable for root `ء ل ي`.
- Synthesis: The scene turns worship into an oriented, repeated, embodied action. Direction prevents diffuse motion, the name fixes address, and counted praise makes recurrence tangible; the incense sense remains a material lexical extension rather than a claim about the surface rite.

### S2. Watering a Working Camel at the Trough
- Reading type: latent/lexical
- Scene or process: A mature working camel approaches sweet stored water, drinks in measured breaths, may be reinserted among the herd, and departs the source.
- Active motifs: mature load-bearing camel (`quranic:root_000347:B008/m01`); returning thirsty camels to the trough (`quranic:root_000464:B007/m01`); watering at the animals' mouths (`quranic:root_001198:B014/m01`); passing camels along the basin (`quranic:root_000867:B010/m01`); leaving the watering place (`quranic:root_000849:B003/m01`); breaths or pauses in drinking (`quranic:root_001533:B006/m01`); abundant water (`quranic:root_000532:B013/m01`); sweet potable water (`quranic:root_000994:B001/m01`); large waterskin and abundant contents (`quranic:root_000387:B004/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:4 `ٱلصُّدُورِ`; 64:5 `قَبْلُ`, `عَذَابٌ`; 64:7 `رَبِّي`; 64:8 `خَبِيرٌ`; 64:9 `يُدْخِلْ`; 64:14 `تَصْفَحُوا`; 64:16 `أَنفُسِكُمْ`.
- Synthesis: The trough scene is a complete provisioning sequence with approach, controlled access, bodily intake, and departure. It gives obedience, capacity, and sustenance one shared practical setting without turning animal husbandry into a broad catalog.

### S3. Saddle, Underpad, Cover, and Reins
- Reading type: latent/lexical
- Scene or process: A wooden saddle frame is cushioned, covered, draped, secured to the animal, and joined to bridle and reins for controlled travel.
- Active motifs: wooden saddle frame (`quranic:root_001029:B009/m01`); leather saddle-cover (`quranic:root_001128:B008/m01`); underpad beneath the saddle (`quranic:root_001684:B011/m01`); drape laid over a litter (`quranic:root_000652:B006/m01`); strong leather covering or garment (`quranic:root_000666:B007/m01`); stitched hide edges (`quranic:root_000121:B006/m01`); bridle and bit (`quranic:root_000348:B006/m01`); reins extended to increase the run (`quranic:root_000151:B007/m01`).
- Ayah anchors: 64:1 `يُسَبِّحُ`; 64:2 `بَصِيرٌ`; 64:6 `تَوَلَّوْا`; 64:9,15 `عَظِيمٌ`; 64:12 `ٱلْبَلَاغُ`, `تَوَلَّيْتُمْ`; 64:14 `أَزْوَاجِكُمْ`; 64:15 `فِتْنَةٌ`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Each component has a distinct mechanical role: frame bears weight, underpad protects the back, cover distributes contact, and bridle and reins translate guidance into motion. The assembled equipment gives concrete depth to burden, protection, and responsive capacity.

### S4. Cutting, Stitching, and Tanning a Hide
- Reading type: latent/lexical
- Scene or process: Skin is removed, measured, cut, inspected for damage, cleaned, stitched, tanned, and preserved with or without its hair.
- Active motifs: removing the outer skin (`quranic:root_000120:B004/m01`); measuring hide before cutting (`quranic:root_000434:B001/m01`); stitching hide to hide (`quranic:root_000121:B006/m01`); perforated or damaged leather (`quranic:root_000352:B004/m01`); removing ticks and treating the animal (`quranic:root_000352:B008/m01`); hide preserved with hair or wool (`quranic:root_000844:B006/m01`); a small measured dose of tanning agent (`quranic:root_001533:B007/m01`); thick paste used to condition hide (`quranic:root_000532:B006/m01`); cut-off scraps or offcuts (`quranic:root_001217:B001/m02`); nap or hair covering a surface (`quranic:root_001096:B003/m01`).
- Ayah anchors: 64:2 `بَصِيرٌ`; 64:2-3 `خَلَقَ`; 64:6 `بَشَرٌ`; 64:7 `رَبِّي`; 64:10 `أَصْحَابُ`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`, `حَلِيمٌ`, `قَرْضًا`; 64:16 `أَنفُسِكُمْ`.
- Synthesis: The hide is transformed through controlled subtraction and protective treatment. Cutting removes excess, tanning arrests decay, stitching restores continuity, and retained hair becomes an added cover, forming a precise material analogue for correction without destruction.

### S5. Arming a Shaft and Following the Projectile
- Reading type: latent/lexical
- Scene or process: A shaft receives its point, the combatant equips protection, aims, releases force, and observes penetration or deflection.
- Active motifs: fitting a spear-shaft with a point (`quranic:root_000051:B011/m01`); working forepart of a spear (`quranic:root_001046:B009/m01`); hanging lash or whip-tip (`quranic:root_000994:B006/m01`); armor (`quranic:root_000121:B005/m01`); shield or weapon (`quranic:root_000633:B005/m01`); protective shield (`quranic:root_000266:B008/m01`); aiming and striking a target (`quranic:root_000889:B003/m01`); arrow deflecting without a scratch (`quranic:root_001464:B005/m01`); straight penetrating thrust (`quranic:root_000347:B009/m01`); face-aligned thrust (`quranic:root_001694:B009/m01`).
- Ayah anchors: 64:2 `بَصِيرٌ`, `تَعْمَلُونَ`; 64:3 `بِٱلْحَقِّ`; 64:5 `أَمْرِهِم`, `عَذَابٌ`; 64:7 `زَعَمَ`, `نَبَؤُا`, `يَسِيرٌ`, `عَمِلْتُمْ`; 64:8 `تَعْمَلُونَ`; 64:9 `جَنَّاتٍ`, `يَعْمَلْ`; 64:11 `مُصِيبَةٍ`.
- Synthesis: Weapon assembly and trajectory make caution operational: protection, direction, and impact are coordinated rather than interchangeable. The deflected arrow also supplies a compact contrast between force expended and intended mark actually made.

### S6. Pursuit at the Burrow's Hidden Exit
- Reading type: latent/lexical
- Scene or process: A hunter pursues wary quarry, observes its stop-and-look behavior, and uses the geometry of a multi-exit burrow to draw it out.
- Active motifs: setting out to hunt (`quranic:root_000745:B006/m01`); taking successive prey (`quranic:root_000993:B008/m01`); quarry running and stopping to look back (`quranic:root_001290:B007/m01`); luring an animal from its burrow (`quranic:root_000452:B006/m01`); through-tunnel with a hidden outlet (`quranic:root_001537:B003/m01`); skittish aversion and flight (`quranic:root_001564:B006/m01`); wild animal's aversion to people (`quranic:root_000004:B002/m01`); wolf-hyena offspring with acute hearing (`quranic:root_000741:B010/m01`); male hyena (`quranic:root_001040:B007/m01`); wolf (`quranic:root_001248:B013/m01`).
- Ayah anchors: 64:1,3,4 `ٱلسَّمَاوَات`; 64:4 `يَعْلَمُ`, `عَلِيمٌ`; 64:11 `عَلِيمٌ`; 64:18 `عَالِمُ`; 64:10 `كَذَّبُوا`; 64:11 `قَلْبَهُ`; 64:14 `عَدُوًّا`; 64:16 `أَنفِقُوا`, `خَيْرًا`, `ٱسْمَعُوا`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`; 64:9 `أَبَدًا`.
- Synthesis: The quarry's pause and the burrow's second exit create a scene of pursuit complicated by concealment and backward attention. It is a useful lexical pressure on turning-away: flight can remain strategically aware rather than simply directionless.

### S7. Pot, Tasting, and Provision for a Guest
- Reading type: latent/lexical
- Scene or process: Food is prepared in a handled pot, tasted and selected, placed in a woven container, and served as provision to an arriving guest.
- Active motifs: cooking pot and cooked broth (`quranic:root_001205:B007/m01`); selected or remaining food in the pot (`quranic:root_001032:B009/m01`); food and provision prepared for a guest (`quranic:root_001492:B005/m01`); woven palm-leaf basket for dates (`quranic:root_000464:B010/m01`); pot-handle shaped like an ear (`quranic:root_000022:B001/m02`); sweet palatable food or drink (`quranic:root_000994:B001/m02`); tasting food (`quranic:root_000526:B001/m01`); thick reduction or paste used in food (`quranic:root_000532:B006/m02`).
- Ayah anchors: 64:1 `قَدِيرٌ`; 64:5 `ذَاقُوا`, `عَذَابٌ`; 64:7 `رَبِّي`; 64:8 `أَنزَلْنَا`; 64:9 `يُدْخِلْ`; 64:11 `بِإِذْنِ`; 64:14 `تَعْفُوا`.
- Synthesis: Cooking converts raw provision into something judged by taste and made ready for reception. The guest scene reverses the punitive tasting of 64:5: intake can be an act of welcome when preparation, selection, and arrival are aligned.

### S8. Crescent, Lunar Mansion, Star, and Day Marker
- Reading type: latent/lexical
- Scene or process: The observer tracks disappearance and reappearance of the moon, its named stations, a prominent star, and daylight as a calendar of visible signs.
- Active motifs: crescent hidden at month's end (`quranic:root_000697:B004/m01`); lunar mansion of three small stars (`quranic:root_001096:B006/m01`); Antares or “heart of the scorpion” (`quranic:root_001248:B010/m01`); lunar mansion or encircling crown (`quranic:root_001315:B005/m01`); named stellar markers (`quranic:root_001559:B007/m01`); sky as overhead field (`quranic:root_000745:B004/m01`); daylight interval (`quranic:root_001700:B001/m01`); sunlight as a visible sign (`quranic:root_000074:B003/m02`); landmark that distinguishes and guides (`quranic:root_001040:B002/m01`).
- Ayah anchors: 64:1,3,4 `ٱلسَّمَاوَات`; 64:4 `تُسِرُّونَ`, `يَعْلَمُ`, `عَلِيمٌ`; 64:11 `عَلِيمٌ`, `قَلْبَهُ`, `كُلِّ`; 64:18 `عَالِمُ`; 64:9 `يَوْمَ`, `يَوْمِ`, `يَوْمُ`, `أَنْهَٰرُ`; 64:10 `بِـَٔايَاتِنَا`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`; 64:1 `كُلِّ`.
- Synthesis: Hidden crescent, named station, and returning day form a timekeeping system built from alternating visibility. The scene supports the surah's appointed Day by showing how absence can remain part of a reliable cycle rather than evidence of non-return.

### S9. Composing, Sending, and Performing Verse
- Reading type: latent/lexical
- Scene or process: A poet composes measured speech, sends praise or satire to an addressee, performs it with voice or instrument, and watches it circulate.
- Active motifs: composing verse (`quranic:root_001217:B007/m01`); sending praise or satire as poetry (`quranic:root_001583:B011/m01`); articulated poem (`quranic:root_001272:B001/m02`); circulating public saying (`quranic:root_001272:B007/m01`); stray or unusual line of poetry (`quranic:root_000004:B008/m01`); pleasurable song (`quranic:root_000741:B007/m01`); singing voice (`quranic:root_001110:B003/m01`); ringing cymbal (`quranic:root_000897:B009/m01`); tongue bearing witness to its speaker (`quranic:root_000822:B005/m01`); reciprocal praise or blame (`quranic:root_001217:B005/m02`).
- Ayah anchors: 64:3,10 `مَصِيرُ`; 64:6-7 `قَالُوا`, `قُلْ`; 64:6 `يَهْدُونَنَا`; 64:11 `يَهْدِ`; 64:6 `غَنِيٌّ`; 64:9 `أَبَدًا`; 64:16 `ٱسْمَعُوا`; 64:17 `قَرْضًا`; 64:18 `ٱلشَّهَادَةِ`.
- Synthesis: The scene distinguishes composition, address, performance, and circulation. It usefully pressures praise and testimony by showing how crafted language can carry either acknowledgment or attack and acquire a life beyond its speaker.

### S10. Setting a Fracture and Watching the Wound
- Reading type: latent/lexical
- Scene or process: A damaged bone is aligned and immobilized, pain is managed, and healing is monitored for crooked union or relapse.
- Active motifs: setting a broken bone that may heal crooked (`quranic:root_000015:B002/m01`); bone joint and socket (`quranic:root_000347:B011/m01`); hard bone (`quranic:root_001029:B005/m01`); ribs of the chest (`quranic:root_000266:B016/m01`); restraint used for correction (`quranic:root_000348:B001/m01`); repair opposed to corruption (`quranic:root_000876:B001/m01`); relapse of wound or illness (`quranic:root_001096:B004/m01`); felt pain (`quranic:root_000046:B001/m01`).
- Ayah anchors: 64:3 `بِٱلْحَقِّ`; 64:5 `أَلِيمٌ`; 64:9 `جَنَّاتٍ`, `عَظِيمٌ`, `صَالِحًا`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`; 64:15 `عَظِيمٌ`, `أَجْرٌ`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Repair requires both force and patience: the break must be restrained in a right relation long enough to unite, and apparent improvement must be watched for reversal. The scene gives reform a structural, bodily meaning rather than treating it as a generic moral label.

### S11. Fetter, Burden, and the Difference Between Restraint and Obedience
- Reading type: latent/lexical
- Scene or process: Hands, neck, or animal movement are physically constrained, creating compliance by force that must be distinguished from willing alignment.
- Active motifs: shackle joining hands to neck (`quranic:root_000259:B008/m01`); fetter binding a person (`quranic:root_000741:B009/m01`); bridle and bit restraining a mount (`quranic:root_000348:B006/m01`); dependent burden carried by another (`quranic:root_001315:B002/m01`); obstructing force that diverts a person from his affair (`quranic:root_000993:B007/m01`); straps and corresponding joined pieces (`quranic:root_001198:B010/m01`); willing obedience and tractability (`quranic:root_000956:B001/m01`); rousing a tethered or kneeling camel (`quranic:root_000129:B001/m01`).
- Ayah anchors: 64:7 `يُبْعَثُوا`, `لَتُبْعَثُنَّ`; 64:5 `قَبْلُ`; 64:9 `يَجْمَعُ`; 64:11 `كُلِّ`; 64:12,16 `أَطِيعُوا`; 64:14 `عَدُوًّا`; 64:16 `ٱسْمَعُوا`; 64:18 `ٱلْحَكِيمُ`.
- Synthesis: Physical restraint can produce motion or stillness without producing assent. The contrast preserves a crucial distinction in the obedience sequence: a body made compliant by fetter or bit is not the same as a hearer who understands and willingly follows.

### S12. Page, Heading, Mark, and Explanatory Text
- Reading type: latent/lexical
- Scene or process: A document receives a heading and distinguishing marks, is read page by page, and uses definition and explanation to disclose meaning.
- Active motifs: turning and examining pages (`quranic:root_000867:B003/m01`); book heading or title (`quranic:root_001041:B002/m01`); explanation by speech, writing, or sign (`quranic:root_000170:B005/m01`); mark or patterned line distinguishing an object (`quranic:root_001040:B002/m02`); definition setting a thing's conceptual boundary (`quranic:root_001272:B016/m01`); explicative particle introducing a gloss (`quranic:root_000074:B009/m01`); interrogative or relative compound (`quranic:root_000527:B004/m01`); eloquence that reaches the intended meaning (`quranic:root_000151:B004/m01`).
- Ayah anchors: 64:4 `تُعْلِنُونَ`, `يَعْلَمُ`, `عَلِيمٌ`; 64:11 `عَلِيمٌ`; 64:18 `عَالِمُ`; 64:6,12 `بَيِّنَات`, `مُبِين`; 64:6-7 `قَالُوا`, `قُلْ`; 64:10 `بِـَٔايَاتِنَا`; 64:12 `ٱلْبَلَاغُ`; 64:14 `تَصْفَحُوا`. Surface anchor is unavailable for root `ذ و و`.
- Synthesis: The document scene separates material navigation from semantic disclosure: heading locates, marks distinguish, pages order attention, and definition limits meaning. It extends the surah's light and clear conveyance into the concrete mechanics of a readable message.

### S13. Preparing and Marking the Body Surface
- Reading type: latent/lexical
- Scene or process: Hair or outer skin is removed or retained, the surface is perfumed or treated, and smoke-derived pigment is applied as kohl or tattoo.
- Active motifs: soot used for kohl or tattoo (`quranic:root_001564:B008/m01`); depilatory lime paste (`quranic:root_001564:B009/m01`); perfumed coating (`quranic:root_000434:B010/m01`); camphor fragrance (`quranic:root_001307:B011/m01`); hair or nap covering a surface (`quranic:root_001096:B003/m01`); stripping the outer skin (`quranic:root_000120:B004/m01`); fair outward appearance (`quranic:root_000120:B006/m01`); scalp itch and need for delousing (`quranic:root_000891:B008/m01`).
- Ayah anchors: 64:2-3 `خَلَقَ`; 64:3 `صَوَّرَكُمْ`; 64:6 `بَشَرٌ`; 64:2 `كَافِرٌ`; 64:5-7,10 `كَفَرُوا`; 64:9 `يُكَفِّرْ`; 64:8,10 `ٱلنُّور`, `ٱلنَّار`; 64:14 `تَغْفِرُوا`, `غَفُورٌ`; 64:17 `يَغْفِرْ`.
- Synthesis: The scene distinguishes natural cover, deliberate removal, treatment, fragrance, and visible marking. It pressures the contrast between outward form and inward condition: a surface can truthfully display care, or it can be altered without changing what lies beneath.


