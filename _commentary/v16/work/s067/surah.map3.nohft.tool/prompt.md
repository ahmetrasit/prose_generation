Surah: 67. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S67 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s067/surah.r2/text.md =====
# Surah 67

- 67:1 تَبَٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- 67:2 ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
- 67:3 ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ ۖ فَٱرْجِعِ ٱلْبَصَرَ هَلْ تَرَىٰ مِن فُطُورٍۢ
- 67:4 ثُمَّ ٱرْجِعِ ٱلْبَصَرَ كَرَّتَيْنِ يَنقَلِبْ إِلَيْكَ ٱلْبَصَرُ خَاسِئًۭا وَهُوَ حَسِيرٌۭ
- 67:5 وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًۭا لِّلشَّيَٰطِينِ ۖ وَأَعْتَدْنَا لَهُمْ عَذَابَ ٱلسَّعِيرِ
- 67:6 وَلِلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ عَذَابُ جَهَنَّمَ ۖ وَبِئْسَ ٱلْمَصِيرُ
- 67:7 إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ
- 67:8 تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ ۖ كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ
- 67:9 قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا وَقُلْنَا مَا نَزَّلَ ٱللَّهُ مِن شَىْءٍ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ كَبِيرٍۢ
- 67:10 وَقَالُوا۟ لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ مَا كُنَّا فِىٓ أَصْحَٰبِ ٱلسَّعِيرِ
- 67:11 فَٱعْتَرَفُوا۟ بِذَنۢبِهِمْ فَسُحْقًۭا لِّأَصْحَٰبِ ٱلسَّعِيرِ
- 67:12 إِنَّ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌۭ
- 67:13 وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- 67:14 أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ
- 67:15 هُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ ذَلُولًۭا فَٱمْشُوا۟ فِى مَنَاكِبِهَا وَكُلُوا۟ مِن رِّزْقِهِۦ ۖ وَإِلَيْهِ ٱلنُّشُورُ
- 67:16 ءَأَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يَخْسِفَ بِكُمُ ٱلْأَرْضَ فَإِذَا هِىَ تَمُورُ
- 67:17 أَمْ أَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا ۖ فَسَتَعْلَمُونَ كَيْفَ نَذِيرِ
- 67:18 وَلَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ فَكَيْفَ كَانَ نَكِيرِ
- 67:19 أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ ۚ مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍۭ بَصِيرٌ
- 67:20 أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- 67:21 أَمَّنْ هَٰذَا ٱلَّذِى يَرْزُقُكُمْ إِنْ أَمْسَكَ رِزْقَهُۥ ۚ بَل لَّجُّوا۟ فِى عُتُوٍّۢ وَنُفُورٍ
- 67:22 أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 67:23 قُلْ هُوَ ٱلَّذِىٓ أَنشَأَكُمْ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۖ قَلِيلًۭا مَّا تَشْكُرُونَ
- 67:24 قُلْ هُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
- 67:25 وَيَقُولُونَ مَتَىٰ هَٰذَا ٱلْوَعْدُ إِن كُنتُمْ صَٰدِقِينَ
- 67:26 قُلْ إِنَّمَا ٱلْعِلْمُ عِندَ ٱللَّهِ وَإِنَّمَآ أَنَا۠ نَذِيرٌۭ مُّبِينٌۭ
- 67:27 فَلَمَّا رَأَوْهُ زُلْفَةًۭ سِيٓـَٔتْ وُجُوهُ ٱلَّذِينَ كَفَرُوا۟ وَقِيلَ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تَدَّعُونَ
- 67:28 قُلْ أَرَءَيْتُمْ إِنْ أَهْلَكَنِىَ ٱللَّهُ وَمَن مَّعِىَ أَوْ رَحِمَنَا فَمَن يُجِيرُ ٱلْكَٰفِرِينَ مِنْ عَذَابٍ أَلِيمٍۢ
- 67:29 قُلْ هُوَ ٱلرَّحْمَٰنُ ءَامَنَّا بِهِۦ وَعَلَيْهِ تَوَكَّلْنَا ۖ فَسَتَعْلَمُونَ مَنْ هُوَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- 67:30 قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ


===== _commentary/v16/work/s067/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ب ر ك (root_000109): 67:1 تَبَٰرَكَ

- **B001** çöküp yerinde durma — deve çöktü ve yerinde kaldı · deveyi çöktürdü · çökmüş develer topluluğu · develerin çöktüğü yer · çökme veya yerleşip kalma
  أبركت الناقة فبركت؛ البرك الإبل البوارك (ayn)؛ برك البعير يبرك بروكا أي استناخ؛ كل شيء ثبت وأقام فقد برك؛ ما أحسن بركة هذه الناقة وهو اسم للبروك (sihah)؛ البرك الإبل البروك؛ أبركت الناقة فبركت بروكا؛ التبراك بفتح التاء البروك (tahdhib)؛ أصل البرك صدر البعير؛ وبرك البعير ألقى بركه (mufradat)؛ أصل واحد وهو ثبات الشيء؛ برك البعير يبرك بروكا؛ مبرك الإبل (maqayis)؛ تبراك فالتاء فيه زائدة وإنما هو تفعال من برك أي ثبت وأقام (maqayis-tabraak)
- **B002** göğüsle bastırma — devenin göğsü ve alt göğüs bölgesi · hayvanın yere değen karın ve göğüs derisi · göğsüyle sürttü veya ezdi · göğsünü yere veya bir şeyin üstüne bıraktı · onu yere serip altında bıraktı
  البرك كلكل البعير وصدره الذي يدوك به الشيء تحته؛ حكه ودكه ببركه (ayn)؛ البرك أيضا الصدر؛ بركة زور؛ ابترك الرجل أي ألقى بركه؛ ابتركته إذا صرعته وجعلته تحت بركك (sihah)؛ البركة ما ولي الأرض من جلد بطن البعير وما يليه من الصدر؛ البرك كلكل البعير وصدره؛ حكه ودكه وداكه ببركه ودلكه (tahdhib)؛ أصل البرك صدر البعير (mufradat)؛ البرك أيضا كلكل البعير وصدره؛ البركة ما ولى الأرض من جلد البطن وما يليه من الصدر من كل دابة (maqayis)
- **B003** su tutan havuzcuk — suyun durduğu havuz veya su tutma çukuru
  البركة أيضا كالحوض والجمع البرك؛ سميت بذلك لإقامة الماء فيها (sihah)؛ البركة شبه حوض يحفر في الأرض؛ الصهاريج التي سويت بالآجر وصرجت بالنورة بركا (tahdhib)؛ سمي محبس الماء بركة (mufradat)؛ البركة شبه حوض يحفر في الأرض؛ البركة المصنعة وجمعها برك (maqayis)
- **B004** kalıcı hayır artışı — hayırda artış ve kalıcı iyilik · hayır ve artış dileme · Tanrının ona hayır ve artış vermesini dilemek · kendinde veya kendisinden çok hayır bulunan · ondan iyi sonuç ve hayır umdu · hayrı bol yiyecek
  البركة النماء والزيادة؛ التبريك الدعاء بالبركة؛ بارك الله لك وفيك وعليك؛ تبركت به أي تيمنت به؛ طعام بريك كأنه مبارك (sihah)؛ معنى البركة الكثرة في كل خير؛ المبارك ما يأتي من قبله الخير الكثير؛ أصل البركة الزيادة والنماء؛ التبريك الدعاء للإنسان وغيره بالبركة؛ بركت عليه تبريكا أي قلت بارك الله عليك؛ البركات السعادة (tahdhib)؛ البركة ثبوت الخير الإلهي في الشيء؛ المبارك ما فيه ذلك الخير؛ يقال لكل ما يشاهد منه زيادة غير محسوسة هو مبارك وفيه بركة (mufradat)؛ البركة من الزيادة والنماء؛ التبريك أن تدعو بالبركة؛ طعام بريك أي ذو بركة (maqayis)
- **B005** Tanrıyı yüceltme — Tanrı yücedir, uludur, kutsaldır ve bütün hayır ona özgüdür
  تبارك الله أي بارك (sihah)؛ تبارك ارتفع؛ تبارك تعالى وتعاظم؛ تبارك الله تمجيد وتعظيم؛ تبارك تقدس (tahdhib)؛ كل موضع ذكر فيه لفظ تبارك فهو تنبيه على اختصاصه تعالى بالخيرات المذكورة (mufradat)؛ تبارك الله تمجيد وتجليل؛ وفسر على تعالى الله (maqayis)
- **B006** işe yapışıp sürdürme — savaşta yer tutup çatışmayı sürdürdüler · savaşta direnme ve çatışma yeri · koşuda var gücüyle çabaladı · onun hakkında kötülemeyi ısrarla sürdürdü · işe devam etti ve onu bırakamadı · bulut aynı yere durmadan yağmur bıraktı
  ابترك أي أسرع في العدو وجد؛ البراكاء الثبات في الحرب والجد؛ براك براك أي ابركوا (sihah)؛ ابترك الرجل في عرض أخيه إذا اجتهد في ذمه؛ الابتراك في العدو الاجتهاد فيه؛ ابترك القوم في الحرب إذا جثوا على الركب ثم اقتتلوا؛ البراكاء مباحة القتال؛ ابترك السحاب إذا ألح بالمطر؛ باركت على التجارة وغيرها أي واظبت عليها (tahdhib)؛ ابتركوا في الحرب أي ثبتوا ولازموا موضع الحرب؛ براكاء الحرب وبروكاؤها للمكان الذي يلزمه الأبطال (mufradat)؛ ابترك الرجل في آخر يتنقصه ويشتمه؛ ابتركوا في الحرب؛ براك براك بمعنى ابركوا؛ برك فلان على الأمر وبارك جميعا إذا واظب عليه؛ ابترك الفرس في عدوه أي اجتهد؛ ابترك السحاب إذا ألح بالمطر (maqayis)
- **B007** çökmüş devenin sabah sütü [kalıp] — çökmüş dişi devenin memesinde birikip sabah sağılan süt · çökeğinde biriken sütünü sağdı
  البركة أن يدر لبن الناقة باركة فيقيمها ويحلبها؛ حلبت بركتها (tahdhib)؛ البركة أن تحلب قبل أن تخرج؛ حلبت الناقة بركتها وحلبت الإبل بركتها إذا حلبت لبنها الذي اجتمع في ضرعها في مبركها؛ لا يسمى بركة إلا ما اجتمع في ضرعها بالليل وحلب بالغدوة (maqayis)
- **B008** beyaz su kuşu — beyaz bir su kuşu
  البركة بالضم طائر من طير الماء أبيض والجمع برك (sihah)؛ البرك واحدتها بركة وهو من طير الماء أبيض (tahdhib)
- **B009** büyük oğlu varken evlenen kadın — büyük oğlu veya büyük çocuğu varken evlenen kadın
  البروك من النساء التي تتزوج ولها ابن بالغ كبير (sihah)؛ البروك من النساء التي تتزوج ولها ولد كبير واسم ذلك الولد الجرنبذ (tahdhib)

## ي د ي (root_001693): 67:1 بِيَدِهِ

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

## ECHO ء ي د (root_000071): for 67:1 بِيَدِهِ: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## م ل ك (root_001444): 67:1 ٱلْمُلْكُ

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

## ك ل ل (root_001315): 67:1 كُلِّ, 67:8 كُلَّمَآ, 67:19 بِكُلِّ (also echo for 67:15 وَكُلُوا۟)

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

## ش ي ء (root_000831): 67:1 شَىْءٍ, 67:9 شَىْءٍ, 67:19 شَىْءٍۭ

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

## ش ي ء (root_000832): 67:1 شَىْءٍ, 67:9 شَىْءٍ, 67:19 شَىْءٍۭ

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

## ق د ر (root_001205): 67:1 قَدِيرٌ

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

## خ ل ق (root_000434): 67:2 خَلَقَ, 67:3 خَلَقَ, 67:3 خَلْقِ, 67:14 خَلَقَ

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

## م و ت (root_001454): 67:2 ٱلْمَوْتَ

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

## ح ي ي (root_000383): 67:2 وَٱلْحَيَوٰةَ

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

## ح ي و (root_005544): documented alternative for 67:2 وَٱلْحَيَوٰةَ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## ب ل و (root_000153): 67:2 لِيَبْلُوَكُمْ

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

## ECHO ب ل ي (root_000154): for 67:2 لِيَبْلُوَكُمْ: withheld observed target; not identity

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

## ح س ن (root_000323): 67:2 أَحْسَنُ

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

## ع م ل (root_001046): 67:2 عَمَلًا

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

## ع ز ز (root_001008): 67:2 ٱلْعَزِيزُ

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

## غ ف ر (root_001096): 67:2 ٱلْغَفُورُ, 67:12 مَّغْفِرَةٌ

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

## س ب ع (root_000669): 67:3 سَبْعَ

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

## س م و (root_000745): 67:3 سَمَٰوَٰتٍ, 67:5 ٱلسَّمَآءَ, 67:16 ٱلسَّمَآءِ, 67:17 ٱلسَّمَآءِ

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

## ECHO و س م (root_001650): for 67:3 سَمَٰوَٰتٍ, 67:5 ٱلسَّمَآءَ, 67:16 ٱلسَّمَآءِ, 67:17 ٱلسَّمَآءِ: withheld observed target; not identity

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

## ط ب ق (root_000927): 67:3 طِبَاقًا

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

## ر ء ي (root_000531): 67:3 تَرَىٰ, 67:3 تَرَىٰ, 67:19 يَرَوْا۟, 67:27 رَأَوْهُ, 67:28 أَرَءَيْتُمْ, 67:30 أَرَءَيْتُمْ

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

## ECHO ر و ي (root_000615): for 67:3 تَرَىٰ, 67:3 تَرَىٰ, 67:19 يَرَوْا۟, 67:27 رَأَوْهُ, 67:28 أَرَءَيْتُمْ, 67:30 أَرَءَيْتُمْ: withheld observed target; not identity

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

## ر ح م (root_000552): 67:3 ٱلرَّحْمَٰنِ, 67:19 ٱلرَّحْمَٰنُ, 67:20 ٱلرَّحْمَٰنِ, 67:28 رَحِمَنَا, 67:29 ٱلرَّحْمَٰنُ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ف و ت (root_001183): 67:3 تَفَٰوُتٍ

- **B001** erişemeden kaçırma — ulaşamama, erişimden çıkma · bir şeyi kaçırmak, ona yetişememek · birine bir şeyi kaçırtmak · kaçırılmış veya erişilemez olmuş şey · bir şeyi kaçırıp ona erişemeyen kimse · mızrağın yetişemeyeceği uzaklık · görüp de ağzıyla ulaşamayacağı yerdeki rızık · kaçış yok, kurtulma olanağı yok
  خلاف إدراك الشيء والوصول إليه؛ فاته الشيء فوتا (maqayis)؛ الفوت: الفوات، فاته الشئ وأفاته إياه غيره (sihah)؛ فلا فوت أي لم يسبقوا ما أريد به (tahdhib)؛ الفوت: بعد الشيء عن الإنسان بحيث يتعذر إدراكه (mufradat)
- **B002** uzaklık ya da nitelik ayrılığı — iki şeyin birbirinden uzaklaşması veya ayrışması · uzaklık, nitelik ayrılığı veya düzen bozukluğu · iki şey arasındaki ayrılık veya kusur · aralarında belirgin bir uzaklık bulunması
  تفاوت الشيئان تباعد ما بينهما أي لم يدرك هذا ذاك (maqayis)؛ تفاوت الشيئان أي تباعد ما بينهما (sihah)؛ من تفاوت من اختلاف واضطراب، والتفاوت التباعد (tahdhib)؛ التفاوت: الاختلاف في الأوصاف (mufradat)
- **B003** söz sahibine danışmadan işe girişme — söz sahibine danışmadan işe girişme · birini atlayarak onunla ilgili işi yürütmek · onun sözü dışında hiçbir iş yapılmamak · malı sahibine sormadan kullanıp harcamak · görüşünü hiçe sayıp tek başına karar vermek · kendi görüşünü tek başına dayatmak · işi tek başına karara bağlamak
  الافتيات افتعال من الفوت وهو السبق إلى الشيء دون الائتمار (maqayis)؛ لا يعمل شئ دون أمره؛ افتات عليه بأمر كذا (sihah)؛ افتات عليه في رأيه أي سبقه؛ تفوت على أبيه في ماله؛ استبد علينا برأيه (tahdhib)؛ يفعل الإنسان الشيء من دون ائتمار من حقه أن يؤتمر فيه (mufradat)
- **B004** iki şey arasındaki açıklık — iki şey veya iki parmak arasındaki açıklık · iki şey veya parmaklar arasındaki açıklıklar
  الفوت الفرجة بين الشيئين كالفرجة بين الإصبعين والجمع أفوات (maqayis)؛ الفوت: الفرجة بين الإصبعين والجمع أفوات (jamhara)؛ الفوت: الفرجة ما بين إصبعين، والجمع أفوات (sihah)
- **B005** hazırlık fırsatı bırakmayan ansızın ölüm [kalıp] — son isteğini bildirmeye fırsat bırakmayan ansızın ölüm
  مات موت الفوات إذا فوجئ كأنه فاته ما أراد من وصية وشبهها (maqayis)؛ مات فلان موت الفوات، أي فوجئ (sihah)؛ موت الفوات موت الفجاءة (tahdhib)

## ر ج ع (root_000544): 67:3 فَٱرْجِعِ, 67:4 ٱرْجِعِ

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

## ب ص ر (root_000121): 67:3 ٱلْبَصَرَ, 67:4 ٱلْبَصَرَ, 67:4 ٱلْبَصَرُ, 67:19 بَصِيرٌ, 67:23 وَٱلْأَبْصَٰرَ

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

## ف ط ر (root_001165): 67:3 فُطُورٍ

- **B001** yarılıp açılma — yarma ve açma · yarıklar, çatlaklar veya yapı bozuklukları · kumaş yarıldı · çatlaklı ya da kesmeyen kılıç · parmağına vurup kanayacak biçimde yardı · az miktarda gelen ince cinsel sıvı; adlandırmanın hangi benzetmeye dayandığı tartışmalıdır · ne yararı ne zararı olan, anlayışı kıt adam
  أصل صحيح يدل على فتح شيء وإبرازه (maqayis)؛ انفطر الثوب وتفطر أي انشق (ayn)؛ الفطر أيضا الشق وتفطر الشيء تشقق (sihah)؛ أصل الفطر الشق (tahdhib)؛ أصل الفطر الشق طولا (mufradat)
- **B002** ilk kez var edip başlatma — Tanrı canlıları yarattı ve yapımlarını ilk kez başlattı · göklerle yeri ilk kez yaratan · kuyunun kazısını ilk kez başlattı
  الفطرة الخلقة (maqayis)؛ فطر الله الخلق أي خلقهم وابتدأ صنعة الأشياء (ayn)؛ فطره أي خلقه؛ الفطر الابتداء والاختراع (sihah)؛ فاطر السماوات والأرض؛ فطرني أي خلقني؛ أنا فطرتها أي أنا ابتدأت حفرها (tahdhib)؛ فطر الله الخلق وهو إيجاده الشيء وإبداعه (mufradat)
- **B003** doğuştan gelen temel yapı — doğuştan gelen yapı; inanç veya ilk bilgiyle yorumlanan temel yönelim · Tanrı'nın insanları üzerinde yarattığı doğuştan yapı veya yönelttiği inanç yolu
  الفطرة الخلقة (maqayis;sihah)؛ الفطرة التي طبعت عليها الخليقة من الدين (ayn)؛ الفطرة الخلقة التي يخلق عليها المولود؛ فطرة ثانية وهي الكلمة التي يصير بها العبد مسلما (tahdhib)؛ ومنه الفطرة (mufradat)
- **B004** orucu sona erdirme — orucu bırakma ve oruçsuz duruma geçme · oruçlu kişi orucunu bozdu · orucunu bozmuş veya oruç tutmayan kişi · orucun açıldığı yiyecek ya da içecek
  الفطر من الصوم؛ أفطر إفطارا وقوم فطر أي مفطرون (maqayis)؛ فطرت وأفطرت الرجل وفطرته من الفطر بمعنى ترك الصوم (ayn)؛ أفطر الصائم والاسم الفطر؛ الفطور ما يفطر عليه (sihah)؛ فطرت الصائم فأفطر؛ الفطور ما يفطر عنه (tahdhib)
- **B005** iki parmakla sağma — koyunu veya deveyi parmak uçlarıyla sağmak · sağım anında çıkan az miktarda süt · az miktarda gelen ince cinsel sıvı; adlandırmanın sağmaya mı kanlı yarılmaya mı dayandığı tartışmalıdır
  فطرت الشاة فطرا إذا حلبتها؛ الفطر يكون الحلب بإصبعين (maqayis)؛ الفطر شيء قليل من اللبن؛ فطرت الناقة أي حلبتها بأطراف الأصابع (ayn)؛ الفطر حلب الناقة بالسبابة والإبهام (sihah)؛ الفطر شيء قليل من اللبن؛ الحلب بأطراف الأصابع (tahdhib)؛ فطرت الشاة حلبتها بإصبعين (mufradat)
- **B006** olgunlaşmadan aceleye getirme — mayalanmamış veya olgunlaşmadan aceleye getirilmiş şey · hamuru ya da kili hazırlayıp bekletmeden hemen işlemek · yeterince düşünülmeden ileri sürülmüş ham görüş · deriyi yeterince işleyip doyurmadın
  فطرت العجين والطين أي عجنته واختبزته من ساعته (ayn)؛ الفطير خلاف الخمير؛ كل شيء أعجلته عن إدراكه فهو فطير (sihah)؛ فطرت العجين والطين وهو أن تعجنه ثم تخبزه من ساعته؛ أفطرت جلدك إذا لم تروه من الدباغ (tahdhib)؛ فطرت العجين إذا عجنته فخبزته من وقته (mufradat)
- **B007** devenin köpek dişinin sürmesi — devenin köpek dişi sürüp çıktı · köpek dişi çıkmış deve
  فطر ناب البعير طلع (ayn;sihah)؛ فطر ناب البعير إذا طلع؛ فطرنا به إذا بزل (tahdhib)
- **B008** bir yer mantarı türü — bir yer mantarı türü · bu türden tek bir yer mantarı
  الفطر ضرب من الكماة وهو المروزي ونحوه الواحدة بالهاء (ayn)؛ الفطر أيضا ضرب من الكمأة أبيض عظام الواحدة فطرة (sihah)؛ الفطر ضرب من الكمأة والواحدة فطرة (tahdhib)

## ك ر ر (root_001292): 67:4 كَرَّتَيْنِ

- **B001** bir şeye geri dönme ve onu yineleme — geri dönüş; yeniden yönelme · kez; geri dönüş · düşmana yeniden saldırmak · bir şeyi tekrar tekrar yapmak veya söylemek · bir işte kararsız kalıp gidip gelmek · birini bir şeyden geri çevirmek veya alıkoymak · geri dönüşe, saldırıya ve kaçışa elverişli at · yineleme
  أصل صحيح يدل على جمع وترديد وكررت وذلك رجوعك إليه بعد المرة الأولى (maqayis); الكر الرجوع عليه ومنه التكرار (ayn); كر يكر كرا إذا رجع بعد فرار وبعد ذهاب (jamhara); الكرة المرة وكررت الشيء تكريرا وتكرارا وتكرر الرجل في أمره أي تردد وكر على العدو (sihah); الكر مصدر كر يكر كرا والرجوع على الشيء ومنه التكرار وكر على العدو (tahdhib); الكر العطف على الشيء بالذات أو بالفعل (mufradat)
- **B002** kalın ve sık bükülmüş ip — kalın veya sık bükülmüş ip · ağaca çıkma ipi veya yelken halatı · kalın, bükülmüş ipler · eyerin iki yan parçasını birleştiren deri bağlar
  الكر حبل سمي بذلك لتجمع قواه (maqayis); الكر الحبل الغليظ وهو أيضا حبل يصعد به على النخل (ayn); الكر حبل شديد الفتل وربما سمي الحبل الذي ترتقى به النخلة كرا (jamhara); الكر حبل يصعد به على النخلة وحبل الشراع وواحد الأكرار (sihah); الكر من الليف ومن قشر العراجين والذي يصعد به على النخل وحبل شراع السفينة وأكرار الرحل (tahdhib); الحبل المفتول كر وجمعه كرور (mufradat)
- **B003** doğal su gözü veya bol sulu küçük göl — su gözü veya bol sulu küçük göl · su gözleri veya vadideki su birikintileri
  الكر الحسى من الماء وجمعه كرار (maqayis); الكر غدير كثير الماء وواد ذو كرار إذا كانت فيه مستنقعات ماء (jamhara); الكرار الأحساء واحدها كر وكر (sihah); الكر الحسي وجمعه كرار ويقال للحسي كر أيضا (tahdhib)
- **B004** Irak'ta kullanılan büyük tahıl ölçüsü — Irak'ta kullanılan tahıl ölçüsü · tahıl ölçüsü birimleri
  الكر مكيال لأهل العراق (ayn); الكر الذي يكال به عربي صحيح (jamhara); الكر واحد أكرار الطعام (sihah); الكر مكيال لأهل العراق والكر ستون قفيزا (tahdhib)
- **B005** zırhı parlatan dışkı-kül karışımı — zırhı parlatmak için kullanılan dışkı, gübre veya kül karışımı
  الكرة سرقين وتراب يجلى به الدروع (ayn); الكرة البعر يحرق وينثر على الدرع لكيلا تصدأ (jamhara); الكرة بالضم البعر العفن تجلى به الدروع (sihah); الكرة البعر (tahdhib); يقولون أن الكرة رماد تجلى به الدروع ويقال هو فتات البعر (maqayis)
- **B006** boğazda yinelenen hırıltılı ses — boğaz hırıltısı veya boğulur gibi çıkan ses · tozdan oluşan ses kısıklığı · gövdede yinelenen ses veya içten kıkırdama · tavuğa tekrarlı biçimde seslenmek
  الكرير كالحشرجة في الحلق سمى بذلك لأنه يرددها وكركرت بالدجاجة صحت بها لأنك تردد الصياح بها (maqayis); الكرير صوت في الحلق كالحشرجة وبحة تعتري من الغبار والكركرة في الضحك فوق القرقرة (ayn); الكرير صوت كصوت المخنوق والحشرجة عند الموت والكركرة في الضحك وكركرت بالدجاجة (sihah); الكرير مثل صوت المختنق وكر يكر كريرا إذا حشرج عند الموت والكركرة صوت يردده الإنسان في جوفه وكركر الضاحك (tahdhib)
- **B007** devenin göğüs nasırı — devenin göğsündeki yuvarlak nasır; beş temel nasırdan biri · develerin göğüs nasırları
  الكركرة رحى زور البعير (maqayis;ayn;mufradat); الكركرة رحى زور البعير وهي إحدى الثفنات الخمس (sihah); الكركرة رحى زور البعير وجمعها كراكر (tahdhib)
- **B008** toplanmış insan grubu veya atlı birlik kümesi — bir araya gelmiş insan topluluğu · atlı birlik kümeleri
  الكركرة الجماعة من الناس (maqayis;sihah); ويعبر بها عن الجماعة المجتمعة (mufradat); الكراكر كراديس من الخيل (ayn;tahdhib)
- **B009** rüzgarın dağınık bulutları sürüp toplaması — rüzgarın dağılmış bulutları sürüp yeniden toplaması
  الكركرة تصريف الرياح السحاب وجمعها إياه بعد تفرق (maqayis); الكركرة تعريف الريح السحاب إذا جمعته بعد تفرق (ayn); الكركرة تصريف الريح السحاب إذا جمعته بعد تفرق (sihah;tahdhib); الكركرة تصريف الريح السحاب وذلك مكرر من كر (mufradat)
- **B010** değirmeni döndürüp öğütmeyi yinelemek — değirmeni döndürüp öğütme hareketini yinelemek · arpa taneleri öğütülmek
  كركر الرحى كركرة إذا أدارها (tahdhib); الكركرة من الإدارة والترديد وكركرة الرحى تردادها (tahdhib); تكركر أي تطحن وسميت كركرة لترديد الرحى على الطحن (tahdhib)

## ق ل ب (root_001248): 67:4 يَنقَلِبْ

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

## خ س ء (root_000408): 67:4 خَاسِئًا

- **B001** aşağılayarak azarlayıp uzaklaştırma — köpeği aşağılayarak azarlayıp kovmak · azarlanıp geri çekilmek veya kovulmak · defol, uzaklaş · benden uzaklaş, öteye çekil · kovulmuş ve aşağılanmış kimse ya da hayvan
  يدل على الإبعاد (maqayis)؛ خسأت الكلب إذا زجرته (ayn)؛ المباعد ومدحورين (ayn)؛ خسأت الكلب خسأ طردته (sihah)؛ زجرته مستهينا به فانزجر (mufradat)
- **B002** bakışın yorulup güçten düşmesi — görüşün yorulması, şaşırması veya aşağılanmışçasına geri çekilmesi · yorgun ve bitkin biçimde geri dönen bakış
  خسأ البصر أي كل وأعيا (ayn)؛ خسأ بصره أي سدر (sihah)؛ خسأ البصر أي انقبض عن مهانة (mufradat)
- **B003** ceviz oyununda tek-çift ayrımı — ceviz oyununda tek mi, çift mi sorusu · ceviz oyunundaki tek sonuç · ceviz oyununda tek olanlar · iki ayak ve bir ayak düzeninde yürümek
  خسا أم زكا؛ فخسا فرد وزكا زوج؛ الزاكي من المخاسي؛ خسازكا
- **B004** karşılıklı taş atma — topluluğun birbirine taş atması · taraflar arasında karşılıklı taş atma
  تخاسأ القوم بالحجارة تراموا بها؛ كانت بينهم مخاسأة

## ح س ر (root_000320): 67:4 حَسِيرٌ

- **B001** örtüyü kaldırıp açığa çıkarma — üzerini açmak, örtüsünü sıyırmak · örtüsü açılmak · rüzgarın bulutları dağıtması · suyun çekilip kıyıyı açığa çıkarması · evi süpürmek · süpürge · sınandığında huyu iyi çıkan kimse
  حسرت عن الذراع أي كشفته (maqayis); الحسر كشطك الشيء عن الشيء (ayn;tahdhib); حسرت الريح السحاب حسرا (ayn;jamhara;tahdhib); حسر البحر عن الساحل إذا نضب (ayn;tahdhib); حسرت البيت إذا كنسته والمحسرة المكنسة (maqayis;jamhara;sihah;mufradat); كريم المحسر أي كريم المخبر (maqayis;sihah;mufradat)
- **B002** koruyucu giysisi veya başlığı olmayan kişi — zırhsız ya da başı açık kişi · giysileri açılmış kadın · savaşta zırhsız piyadeler
  الحاسر الذي لا درع عليه ولا مغفر (maqayis;jamhara;sihah;mufradat); رجل حاسر خلاف الدارع (ayn); الحاسر الذي لا بيضة على رأسه (tahdhib); رجل حاسر لا عمامة على رأسه وامرأة حاسر (tahdhib); يقال للرجالة في الحرب الحسر (tahdhib)
- **B003** gücün veya sürdürecek imkanın tükenmesi — yolculuktan sonra bitkin düşmek · bitkin, gücü kesilmiş · gözün yorulup bakışın kesilmesi · yorulup ya da bıkıp sürdürmeyi bırakmak · elinde hiçbir şey kalmamış
  الحسر والحسور الإعياء (ayn;tahdhib); حسرت الدابة وحسرها بعد السير فهي حسير ومحسورة وهن حسرى (ayn;sihah;tahdhib); حسر البصر إذا كل وهو حسير (maqayis;jamhara;sihah;tahdhib); ناقة حسير انحسر عنها اللحم والقوة (mufradat); لا تملوا (tahdhib); يبقى محسورا لا شيء عنده (tahdhib)
- **B004** kaçırılmış olana duyulan derin pişmanlık ve üzüntü — kaçırılan şey için duyulan derin pişmanlık ve üzüntü · kaçırdığı şeye yanıp derin pişmanlık duymak
  الحسرة التلهف على الشيء الفائت (maqayis); حسر حسرة وحسرا أي ندم على أمر فاته (ayn); حسر الرجل حسرة وحسرا إذا كمد على الشيء الفائت وتلهف عليه (jamhara); الحسرة أشد التلهف على الشيء الفائت (sihah); الحسرة أشد الندم (tahdhib); الحسرة الغم على ما فاته والندم عليه (mufradat)
- **B005** eski tüyün veya kılın dökülmesi ya da gevşek etin sıkılaşması — kuşun eski tüylerini döküp yeni tüylere geçmesi · deve tüyünün ya da eşek kılının dökülmesi · gevşekliği gidip etin yerli yerine oturması
  انحسر الطير خرج من الريش العتي إلى الحديث (ayn); حسرت الطير تحسيرا سقط ريشها (sihah); تحسر وبر البعير أي سقط (sihah); تحسر الوبر عن البعير والشعر عن الحمار إذا سقط (tahdhib); الجارية تتحسر إذا صار لحمها في مواضعه وكذلك البعير (ayn;tahdhib)
- **B006** küçümsenmiş, incitilmiş veya dışlanmış kişi — küçümsenmiş, incitilmiş veya yönetici çevresinden dışlanmış
  المحسر المحقر كأنه حسر أي جعل ذا حسرة (maqayis); رجل محسر أي محقر مؤذى (ayn;sihah); أصحابه محسرون محقرون مقصون عن أبواب السلطان (ayn;tahdhib)
- **B007** çayırlarda yetişen, develerde dışkılamayı artıran ot — çayırlarda yetişen ve develerde dışkılamayı artıran ot
  الحسار ضرب من النبات يسلح الإبل (ayn;tahdhib); الحسار من العشب ينبت في الرياض الواحدة حسارة (tahdhib)

## ز ي ن (root_000660): 67:5 زَيَّنَّا

- **B001** ayıptan uzak güzellik — güzellik; ayıp ve çirkinliğin karşıtı · güzel ve alımlı yüz · güzelliği onu güzel ve alımlı kıldı
  الزين نقيض الشين (maqayis;ayn;tahdhib)؛ زانه الحسن يزينه زينا (ayn;tahdhib)؛ الزينة الحقيقية ما لا يشين الإنسان (mufradat)
- **B002** güzelleştirme ve güzelliğini görünür kılma — bir şeyi güzelleştirmek ve güzelliğini ortaya çıkarmak · onun güzelliğini davranışla ya da sözle görünür kılmak · yer, otlarıyla güzelleşip canlandı · yer güzelleşip canlandı · yer güzelleşip canlandı · onu gönlünde güzel ve sevimli göstermek · yaptığı işi ona güzel göstermek · yeryüzündekileri ona güzel göstermek · dünya hayatını güzel göstermek · yakın göğü kandillerle bezemek
  أصل صحيح يدل على حسن الشيء وتحسينه (maqayis)؛ زينت الشيء تزيينا (maqayis)؛ ازدانت الأرض بعشبها وازينت وتزينت (ayn;tahdhib)؛ زانه وزينه إذا أظهر حسنه إما بالفعل أو بالقول (mufradat)؛ زينا السماء الدنيا بمصابيح وزينة الكواكب (mufradat)
- **B003** bezenmeye yarayan nitelik ve şeylerin bütünü — bezenmek için kullanılan her şeyin ortak adı · kişiyi hiçbir durumda ayıplı kılmayan gerçek güzellik · bilgi ve iyi inanç gibi içsel güzellik · güç ve uzun boy gibi bedensel güzellik · mal ve saygınlık gibi dışsal süs · mal, eşya ve saygınlık türünden dünyalık süs · Tanrı'nın sunduğu süs; başka yorumlarda cömertlik ya da kötülükten sakınma erdemi · yıldızların gözle algılanan süsü
  الزينة جامع لكل ما يتزين به (ayn)؛ الزينة اسم جامع لكل شيء يتزين به (tahdhib)؛ الزينة بالقول المجمل ثلاث: زينة نفسية وزينة بدنية وزينة خارجية (mufradat)؛ فهي الزينة الدنيوية من المال والأثاث والجاه (mufradat)

## د ن و (root_000493): 67:5 ٱلدُّنْيَا

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

## ص ب ح (root_000839): 67:5 بِمَصَٰبِيحَ, 67:30 أَصْبَحَ

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

## ج ع ل (root_000248): 67:5 وَجَعَلْنَٰهَا, 67:15 جَعَلَ, 67:23 وَجَعَلَ

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

## ر ج م (root_000547): 67:5 رُجُومًا

- **B001** taş ya da benzeriyle vurma — taşlama; taşlayarak öldürme · ona taş ya da başka bir nesne attı · atışta kullanılan taşlar veya gök cisimleri · birbirlerine taş attılar · seni ağır sözlerle inciteceğim; başka yoruma göre öldüreceğim
  الرمي بالحجارة؛ الرجام وهي الحجارة؛ رجم فلان إذا ضرب بالحجارة (maqayis)؛ الرجم في القرآن القتل؛ الرجم اسم لما يرجم به الشيء؛ الرجوم التي ترمى بها الشياطين؛ الرجم الرمي بالحجارة (ayn)؛ رجمته بيدي رجما بحجر أو غيره؛ الرجوم النجوم التي يرمى بها (jamhara)؛ الرجم القتل وأصله الرمي بالحجارة؛ تراجموا بالحجارة أي ترموا بها (sihah)؛ الرجم الرمي بالحجارة؛ الرجم القتل؛ رجم الثيبين؛ الرجوم مرامي لهم (tahdhib)؛ الرجام الحجارة؛ الرجم الرمي بالرجام؛ المقتولين أقبح قتلة؛ رجوما للشياطين (mufradat)
- **B002** ağır sözlerle sövme — birine ağır sözler söyleyip sövdü · karşılıklı sövüşme ve çirkin sözler · durmadan sert sözler söyleyen dil · seni ağır sözlerle inciteceğim; başka yoruma göre öldüreceğim
  رجمت فلانا بالكلام إذا شتمته؛ ضربه به كما يرجم الإنسان بالحجارة (maqayis)؛ لأقولن فيك ما تكره (ayn)؛ المراجم قبيح الكلام؛ تراجم القوم بينهم بمراجم قبيحة (jamhara)؛ الرجم السب والشتم؛ لأسبنك وأشتمنك؛ الرجيم بمعنى المشتوم المسبوب؛ لسان مرجم إذا كان قوالا (tahdhib)؛ يستعار الرجم للشتم؛ لأقولن فيك ما تكره؛ المراجمة المسابة الشديدة (mufradat)
- **B003** iyilikten kovulmuş kötü varlık [kalıp] — iyilikten kovulmuş ve kınanmış kötü varlık
  الشيطان رجيم مرجوم ملعون (ayn)؛ الرجم اللعن؛ الشيطان الرجيم بمعنى المرجوم وهو الملعون المبعد؛ الرجيم بمعنى الملعون؛ الرجم الهجران؛ الرجم الطرد (tahdhib)؛ والشيطان الرجيم المطرود عن الخيرات وعن منازل الملإ الأعلى (mufradat)
- **B004** bilmeden kestirimde bulunma — bilinmeyen hakkında dayanaksız konuşmak · kesinliğe dayanmayan söz · gerçek durumu belirlenemez oldu
  الرجم القذف بالغيب وبالظن؛ الحديث المرجم أي قوله بالغيب والظن (ayn)؛ رجم الرجل بالغيب إذا تكلم بما لا يعلم؛ كلام مرجم عن غير يقين (jamhara)؛ الرجم أن يتكلم الرجل بالظن؛ رجما بالغيب؛ الحديث المرجم (sihah)؛ الرجم القول بالظن والحدس؛ رجما بالغيب؛ رجم ظنون؛ الحديث المرجم؛ الرجم الظن (tahdhib)؛ يستعار الرجم للرمي بالظن والتوهم؛ رجما بالغيب؛ الحديث المرجم (mufradat)
- **B005** taş yığını ve onunla belirtilen gömüt — gömüt veya gömüt üstündeki taş yığını · taş yığını, gömüt taşı, taş tepe veya taş işaret · gömüdün üstüne taş yığdı · yaban hayvanı inine girip gömütteymiş gibi oldu
  الرجمة القبر وهي الحجارة التي تجمع على القبر؛ لا تجعلوا عليه الحجارة (maqayis)؛ للحجارة المجتمعة رجمة؛ القبر الرجم؛ كأن الوحشي لما صار في وجاره صار في قبر (maqayis)؛ الرجم القبر؛ الرجمة حجارة مجموعة؛ رجمت القبر جعلت فوقه رجمة (ayn)؛ الرجمة القبر؛ يجمع رجما ورجاما (jamhara)؛ الرجمة واحدة الرجم والرجام؛ جمعت على القبر؛ الرجم القبر؛ الرجمة وجار الضبع (sihah)؛ الرجم القبر؛ الرجمة حجارة مجموعة؛ الرجام الهضاب؛ الرجمات المنار؛ رجمت القبر؛ الرجم والرجام الحجارة المجموعة على القبور (tahdhib)؛ الرجمة أحجار القبر؛ يعبر بها عن القبر؛ رجمت القبر وضعت عليه رجاما (mufradat)
- **B006** kuyu kovası için ağırlık veya çift destek — kuyuya sarkıtılan bağlı ağırlık taşı · kuyu kovasını taşıyan iki ahşap destek
  الرجام حجر يشد في طرف الحبل ثم يدلى في البئر؛ حجر يشد بطرف عرقوة الدلو (maqayis)؛ الرجامان خشبتان تنصبان على رأس البئر (ayn)؛ الرجام حجر يشد بطرف عرقوة الدلو (jamhara)؛ الرجام المرجاس؛ شد بطرف عرقوة الدلو؛ الرجامان خشبتان تنصبان على رأس البئر (sihah)؛ الرجام حجر يشد في طرف الحبل ثم يدلى في البئر؛ الرجام ما يبنى على البئر ثم تعرض عليه الخشبة للدلو (tahdhib)
- **B007** topluluğu uğruna savaşarak savunma [kalıp] — topluluğu uğruna savaşıp onu savundu · savaşta güçlü ve saygınlığını savunan kişi
  رجل مرجم مدافع عن حسبه ونسبه في الحرب (ayn)؛ أرجم الرجل عن قومه وراجم عن قومه إذا ناضل عنهم (jamhara)؛ رجل مرجم أي شديد؛ رجم فلان عن قومه إذا ناضل عنهم (sihah)
- **B008** hayvanın yeri ağır adımlarla dövmesi [kalıp] — yeri tırnakları veya tabanlarıyla ağır biçimde döven at ya da deve
  بعير مرجم يرجم الأرض بأخفافه رجما وهو الثقيل المشي من غير بطء (ayn)؛ فرس مرجم أي يرجم الأرض بحوافره يرميها بها (jamhara)؛ فرس مرجم يرجم في الأرض بحوافره (sihah)
- **B009** sözü başka dilde açıklama — sözünü başka bir dilde açıkladı · diller arasında sözlü açıklama yapan kişi
  ترجم كلامه إذا فسره بلسان آخر؛ الترجمان والجمع التراجم (sihah)؛ يقال ترجمان وترجمان (tahdhib)؛ الترجمان تفعلان من ذلك (mufradat)
- **B010** üst üste yığılıp birikme — üst üste binip yığıldı
  ارتجم الشيء وارتجن إذا ركب بعضه بعضا (tahdhib)

## ش ط ن (root_000796): 67:5 لِّلشَّيَٰطِينِ

- **B001** uzaklaşma ve uzaklaştırma — uzaklaşmak, uzak olmak · uzaklaştırmak · evin uzakta kalması · uzaklara düşüren ayrılık · uzak sefer · yurttan çok uzakta kalış · dibi çok uzakta olan kuyu
  أصل مطرد صحيح يدل على البعد (maqayis)؛ شطن عنه بعد وأشطنه أبعده وبئر شطون بعيدة القعر ونوى شطون بعيدة (sihah)؛ غزوة شطون أي بعيدة وشطنت الدار شطونا إذا بعدت (tahdhib)؛ الشيطان من شطن أي تباعد (mufradat)
- **B002** uzun kuyu ipi ve onunla bağlama — su çekmeye yarayan uzun, sıkı bükülmüş ip · uzun ipler · uzun iple bağlamak · iki yanından iki iple bağlanmış at · iki ip arasında çırpınmak; azgın ve güçlü kişi için de söylenir · kuyudan kovayı iki iple çeken kişi
  الشطن الحبل وهو القياس لأنه بعيد ما بين الطرفين (maqayis)؛ الشطن الحبل الطويل الشديد الفتل يستقى به (ayn;tahdhib)؛ شطنته أشطنه إذا شددته بالشطن (sihah)؛ المشاطن الذي ينزع الدلو من البئر بحبلين (tahdhib)
- **B003** yönünden ayırma ve bağlama göre eğrilik ya da çetinlik — birini niyet ettiği yönden ayırmak · bir yana yatık kalça · kıvrımlı ve eğri kuyu · ağır ve çetin savaş · uzun ve eğri mızrak
  شطنه يشطنه شطنا إذا خالفه عن نية وجهه (sihah)؛ خالفه عن نيته ووجهه وألية شطون إذا كانت مائلة في شق وبئر شطون ملتوية عوجاء وحرب شطون عسرة شديدة ورمح شطون طويل أعوج (tahdhib)
- **B004** azgın ve başkaldıran kötü varlık — iyiden uzaklaşmış, azgın ve başkaldıran kötü varlık · insanlar, görünmez varlıklar veya hayvanlar arasındaki her azgın başkaldıran · azgın ve başkaldıran kötü varlık · kişinin kötücül varlık gibi olup onun yaptığını yapması · kişinin kötücül varlığa dönüşüp onun gibi davranması
  كل عات متمرد من الجن والإنس والدواب شيطان (maqayis;sihah)؛ الشيطان فيعال من شطن أي بعد وشيطن الرجل وتشيطن إذا صار كالشيطان وفعل فعله (tahdhib)؛ الشيطان اسم لكل عارم من الجن والإنس والحيوانات وسمي كل خلق ذميم للإنسان شيطانا (mufradat)
- **B005** çirkin yılan ve bitki adıyla ürkütücü baş benzetmesi — kötü varlık adı verilen çirkin görünüşlü yılan · çirkin bir yılanın ya da bitkinin başları; ürkütücü çirkinlik benzetmesi
  الحية تسمى شيطانا (maqayis)؛ العرب تسمي الحية شيطانا ونبت قبيح يسمى رءوس الشياطين (sihah)؛ بعض الحيات شيطانا وهو حية ذو عرف قبيح المنظر والشيطان نبت قبيح يسمى برؤوس الشياطين (tahdhib)؛ كأنه رؤوس الشياطين قيل هي حية خفيفة الجسم وقيل أراد به عارم الجن فتشبه به لقبح تصورها (mufradat)

## ع ت د (root_000978): 67:5 وَأَعْتَدْنَا

- **B001** el altında bulunma, önceden hazırlama ve gereksinim için saklanan gereç veya kap — yakın ve gereksinim anında kullanılabilecek biçimde el altında olmak · yakın, el altında veya önceden kullanıma uygun duruma getirilmiş · bir iş için önceden hazırlayıp kullanıma uygun duruma getirmek · önceden hazırlanıp kullanıma uygun duruma getirilmiş · bir iş için önceden hazırlanmış gereç, donanım veya stok · önceden hazırlanmış gereçler ve donanımlar · bakım ve koku gereçlerinin gerektiğinde kullanılmak üzere el altında tutulduğu kap veya takım
  أصل واحد يدل على حضور وقرب (maqayis)؛ عتد الشيء وهو يعتد عتادا فهو عتيد حاضر (maqayis;ayn;tahdhib)؛ العتيد الشيء المعد (ayn)؛ العتيد الشئ الحاضر المهيا (sihah)؛ العتاد الشيء الذي تعده لأمر ما وتهيئه له (tahdhib)؛ العتاد ادخار الشيء قبل الحاجة إليه (mufradat)؛ العتيدة التي يكون فيها الطيب والأدهان (maqayis;ayn;tahdhib;jamhara)
- **B002** binmeye hazırlanmış, koşuya hazır veya güçlü ve sağlam yapılı at [kalıp] — binmeye hazırlanmış, koşuya hazır veya güçlü, sağlam ve gelişkin at
  هذا الفرس عتد أي معد متى شاء صاحبه ركبه (maqayis)؛ فرس عتد صلب شديد وليس له فعل يتصرف (jamhara)؛ فرس عتد وعتد المعد للجري وهو الشديد التام الخلق (sihah;tahdhib)؛ فرس عتيد وعتد حاضر العدو (mufradat)
- **B003** erkek oğlak; bazı kaynaklarda işkembesi gelişmiş, otlayıp güçlenerek bir yaşını doldurmuş veya çiftleşme çağına gelmiş — erkek oğlak; bazı kaynaklarda gelişim eşiği işkembe, güç, yaş veya çiftleşme olgunluğuyla belirlenir · erkek oğlaklar
  العتود الجدي الذي قد استكرش (ayn)؛ العتود من أولاد المعز ما رعى وقوي وأتى عليه حول (sihah;tahdhib)؛ العتود الذي بلغ السفاد (maqayis;tahdhib)؛ العتود من أولاد المعز (mufradat)
- **B004** içme kabı, özellikle iri bir tas veya çanak — içme veya sunma kabı; özellikle iri bir tas ya da çanak
  ربما سموا القدح الضخم عتادا (sihah)؛ العتاد القدح وهو العسف والصحن (tahdhib)

## ECHO ع د د (root_000989): for 67:5 وَأَعْتَدْنَا, 67:25 ٱلْوَعْدُ: withheld observed target; not identity

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

## ع ذ ب (root_000994): 67:5 عَذَابَ, 67:6 عَذَابُ, 67:28 عَذَابٍ

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

## س ع ر (root_000708): 67:5 ٱلسَّعِيرِ, 67:10 ٱلسَّعِيرِ, 67:11 ٱلسَّعِيرِ

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

## ك ف ر (root_001307): 67:6 كَفَرُوا۟, 67:20 ٱلْكَٰفِرُونَ, 67:27 كَفَرُوا۟, 67:28 ٱلْكَٰفِرِينَ

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

## ر ب ب (root_000532): 67:6 بِرَبِّهِمْ, 67:12 رَبَّهُم

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

## ECHO ر ب و (root_000537): for 67:6 بِرَبِّهِمْ, 67:12 رَبَّهُم: withheld observed target; not identity

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

## ب ء س (root_000079): 67:6 وَبِئْسَ

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

## ص ي ر (root_000897): 67:6 ٱلْمَصِيرُ

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

## ل ق ي (root_001372): 67:7 أُلْقُوا۟, 67:8 أُلْقِىَ

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

## س م ع (root_000741): 67:7 سَمِعُوا۟, 67:10 نَسْمَعُ, 67:23 ٱلسَّمْعَ

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

## ش ه ق (root_000824): 67:7 شَهِيقًا

- **B001** yükselme ve çok uzun olma — çok yüksek ve son derece uzun · çok yüksek ve uzun dağlar veya nesneler · yükselip uzamak · yükselip uzama veya soluk alma
  أصل واحد يدل على علو (maqayis)؛ جبل شاهق أي عال (maqayis)؛ جبل شاهق ممتنع طولا (ayn;tahdhib)؛ شهق يشهق أي ارتفع (sihah)؛ كل شيء ارتفع وطال فقد شهق (tahdhib)؛ متناهي الطول (mufradat)
- **B002** nefesi içeri çekme ve yüksek soluk alma — nefesi içeri çekmek ve yüksek sesle solumak · nefesi içeri çekme, soluk alma · çok şiddetli ve yüksek inilti · eşeğin anırmasının son sesi · ani, şiddetli soluk veya çığlık · yüksek sesle soluk çekme · soluk çeker gibi kesik kesik gülme · yüksek sesle soluyan erkek deve · yükselip uzama veya soluk alma
  الشهيق ضد الزفير (maqayis;ayn;tahdhib)؛ الشهيق رد النفس والزفير إخراج النفس (maqayis;ayn;sihah;tahdhib)؛ تنفس نفسا عاليا (tahdhib)؛ الشهيق الأنين الشديد المرتفع جدا (tahdhib)؛ شهيق الحمار آخر صوته (sihah;tahdhib)؛ الشهقة كالصيحة (sihah)؛ التشهاق الشهيق (sihah)؛ الشهيق طول الزفير وهو رد النفس (mufradat)
- **B003** şiddetli öfke; hayvanda sesli saldırgan kızışma [kalıp] — şiddetle öfkelenmiş kimse · kızışıp saldıran ve gövdesinden ses çıkaran erkek hayvan
  فلان ذو شاهق إذا اشتد غضبه (maqayis;sihah;tahdhib)؛ فحل ذو شاهق إذا هاج وصال فسمعت له صوتا يخرج من جوفه (tahdhib)
- **B004** gözünü dikerek göz değdirme veya göz değmesinden korkulma — bakanın gözünü dikip göz değdirmesi veya göz değmesinden korkulması
  شهقت عين الناظر عليه إذا أصابته بعين (tahdhib)؛ فتح إنسان عينه عليه فخشيت أن يصيبه بعينه (tahdhib)

## ف و ر (root_001185): 67:7 تَفُورُ

- **B001** kaynayıp coşarak kabarma — kaynama ve şiddetli kaynama · kaynamak veya coşup kabarmak · öfkesi kabarmak · suyu coşup fışkıran kaynak veya kaynayan kabın püskürttüğü şey · kabın hararetle kaynayıp yükselen kısmı
  الفور الغليان؛ فارت القدر تفور فورا؛ فار غضبه إذا جاش (maqayis); الفور فور القدر والنار والدخان والغضب؛ الفوارة العين تجيش وتفور بمائها؛ كل جائش فائر (ayn); فارت القدر تفور فورا وفورانا: جاشت؛ فار فائره إذا جاش غضبه؛ فوراة القدر ما يفور من حرها (sihah); الفور: شدة الغليان؛ يقال ذلك في النار نفسها إذا هاجت، وفي القدر، وفي الغضب؛ فار التنور؛ الفوارة ما تقذف به القدر؛ فوارة الماء سميت تشبيها بغليان القدر (mufradat)
- **B002** daha yatışmadan hemen [kalıp] — hemen, daha yatışmadan · savaş coşkusuyla bulundukları yönden doğrudan gelmek
  فعله من فوره أي في بدء أمره قبل أن يسكن (maqayis); جاء القوم من فورهم أي جاشوا للحرب فأقبلوا من وجههم ذلك (ayn); أتيت فلانا من فوري، أي قبل أن أسكن (sihah); فعلت كذا من فوري، أي: غليان الحال، وقيل: سكون الأمر؛ ويأتوكم من فورهم هذا (mufradat)
- **B003** sıcağın şiddeti [kalıp] — sıcağın en şiddetli hali
  فورة الحر: شدته
- **B004** karanlık bastıktan sonraki vakit [kalıp] — gece karanlığı bastıktan sonraki vakit
  فورة العشاء: بعد العتمة
- **B005** bedende şişip harlanma — sinirleri yayılıp belirginleşmiş hayvan · damarı şişip belirginleşmek · ateşli hastalıktan bedeni harlanmak
  الفائر المنتشر العصب من الدواب وغيرها؛ فار العرق يفور فورا أي انتفخ (ayn); فار فلان من الحمى يفور؛ ولا العرق فارا (mufradat)
- **B006** hurmalı çemen içeceği — kaynatılıp süzülen, hurma katılmış lohusa çemen içeceği
  الفيرة حلبة تطبخ حتى إذا فارت فوراتها ألقيت في معصرة فصفيت ثم يلقى عليها تمر فتتحساها المرأة النفساء
- **B007** özel anatomik delik veya bez çifti [kalıp] — kalça kemiğindeki delik · işkembenin içindeki iki bez
  في الكرش فوارتان في باطنهما غدتان من كل ذي لحم (ayn); فوارة الورك بالفتح والتشديد: ثقبها (sihah)
- **B008** terazi dilinin iki yan parçası — terazi dilini iki yandan kuşatan parçalar
  الفياران: اللذان يكتنفان لسان الميزان
- **B009** tekili ayrı adla karşılanan ceylanlar — tekili aynı sözden olmayan ceylanlar
  الفور بالضم: الظباء، لا واحد لها من لفظها؛ لا أفعل كذا ما لألأت الفور

## ك و د (root_001329): 67:8 تَكَادُ

- **B001** bir şeyi biraz güçlükle aramak — bir şeyi biraz güçlükle aradı
  التماس شيء ببعض العناء؛ كاد يكود كودا ومكادا
- **B002** eyleme ramak kalmak; olumluda yapmamak, olumsuzda güçlükle yapmak — az kalsın yapacaktı, ama yapmadı · güçlükle de olsa yaptı · az kalsın yapacaktı · bir kimse az kalsın yapacaktı
  فأما قولهم في المقاربة كاد فمعناها قارب (maqayis)؛ كاد يفعل كذا يكاد كودا ومكادة أي قارب ولم يفعل (sihah)؛ مجردة فلم يقع ذلك الشيء وقرنت بجحد فقد وقع (maqayis)؛ مجرده ينبئ عن نفي الفعل ومقرونه بالجحد ينبئ عن وقوع الفعل (sihah)
- **B003** vermeyi ya da yapmayı kesin biçimde reddetmek [kalıp] — Hayır, vermeye hiç niyetim yok. · Bunu kesinlikle yapmam. · Bunu ne önemsiyorum ne de yapmaya yanaşıyorum.
  لمن يطلب منك الشيء فلا تريد إعطاءه لا ولا مكادة (maqayis)؛ لا أفعل ذلك ولا كودا (sihah)؛ لا مهمة لي ولا مكادة أي لا أهم ولا أكاد (sihah)
- **B004** istemek, niyet etmek — ondan ne istendiği · onu gizlemek istiyorum
  عرف فلان ما يكاد منه أي ما يراد منه؛ قال بعضهم في قوله أكاد أخفيها أريد أخفيها؛ كادت وكدت وتلك خير إرادة

## ECHO ك ي د (root_001334): for 67:8 تَكَادُ: withheld observed target; not identity

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

## م ي ز (root_001461): 67:8 تَمَيَّزُ

- **B001** ayırıp ayırt etme — şeyleri birbirinden ayırt etme · benzerleri birbirinden ayırt etme · bir şeyi ayırıp gruplama · bir şeyi ayırıp belirgin kılma · başkasından ayrılma · topluluk üyelerinin birbirinden çekilip ayrılması · topluluk üyelerinin birbirinden ayrılması · birbirinden ayrılma
  أصل صحيح يدل على تزيل شيء من شيء وتزييله (maqayis)؛ الميز التمييز بين الأشياء (ayn)؛ مزت الشئ أميزه ميزا: عزلته وفرزته (sihah)؛ الميز والتمييز: الفصل بين المتشابهات (mufradat)؛ امتاز القوم تنحى بعضهم عن بعض (ayn)؛ امتاز القوم، إذا تميز بعضهم من بعض (sihah)
- **B002** öfkeden parçalanacak gibi olma [kalıp] — öfkeden parçalanacak gibi olma
  ويكاد يتميز غيظا أي يتقطع (maqayis)؛ فلان يكاد يتميز من الغيظ، أي يتقطع (sihah)؛ تميز كذا مطاوع ماز. أي: انفصل وانقطع؛ تكاد تميز من الغيظ (mufradat)
- **B003** anlam çıkarma yetisi — anlam çıkarma yetisi · anlam çıkarma yetisi yok
  والتمييز يقال تارة للفصل، وتارة للقوة التي في الدماغ، وبها تستنبط المعاني؛ فلان لا تمييز له (mufradat)
- **B004** boynu uzatma buyruğu — boynunu uzat · başını uzat · boynunu uzat
  وإذا أراد الرجل أن يضرب عنق رجل يقول له ماز عنقك ويقال ماز رأسك أي مد عنقك؛ أو يقول ماز ويسكت من غير أن يذكر الرأس (ayn)

## غ ي ظ (root_001121): 67:8 ٱلْغَيْظِ

- **B001** başkasının doğurduğu, içte yanan ağır öfke — içte duyulan ağır ve yakıcı öfke · onu çok öfkelendirdi; içine ağır öfke saldı · onu çok öfkelendirdi · öfkelendirilmiş, içine ağır öfke dolmuş kimse · öfke uyandıran; çok öfkelendirici · çok öfkelendi; içine ağır öfke doldu · onu çok öfkelendirdi; kullanımı tartışmalı biçim
  كرب يلحق الإنسان من غيره (maqayis)؛ غظته أغيظه غيظا والتغيظ الاغتياظ (ayn)؛ الغيظ غضب كامن للعاجز (sihah)؛ غظت فلانا أغيظه غيظا والتغيظ الاغتياظ وقد اغتاظ عليه وتغيظ (tahdhib)؛ الغيظ أشد غضب وهو الحرارة التي يجدها الإنسان من فوران دم قلبه (mufradat)
- **B002** karşılıklı ya da aralıklı öfkelendirme — birbirini ya da aralıklarla öfkelendirme
  المغايظة فعل في مهلة أو منهما جميعا (ayn;tahdhib)؛ غايظه فاغتاظ وتغيظ بمعنى (sihah)
- **B003** sıcağın taşarcasına şiddetlenmesi — öğle sıcağı iyice bastırdı · ateşin aşırı sıcaklığı
  تغيظت الهاجرة إذا اشتد حميها؛ من شدة الحر
- **B004** öfkeyi dışa vurma — öfkeyi dışa vurma · öfkeyi duyulur bir soluk sesiyle dışa vurma
  التغيظ هو إظهار الغيظ وقد يكون ذلك مع صوت مسموع

## ف و ج (root_001184): 67:8 فَوْجٌ

- **B001** insan topluluğu — insan topluluğu · insan toplulukları · çok sayıda insan topluluğu · çok sayıda insan topluluğu · insan toplulukları · art arda gelen topluluklar · grup grup, art arda
  كلمة تدل على تجمع؛ الفوج الجماعة من الناس والجمع أفواج وجمع الجمع أفاوج وأفاويج (maqayis)؛ الفوج القطيع من الناس والجميع الأفواج (ayn)؛ الفوج من الناس الجماعة والجمع أفواج وجمع أفواج أفاوج وأفاويج (jamhara)؛ الفوج الجماعة من الناس والجمع فؤوج وأفواج وجمع الجمع أفاوج وأفاويج (sihah)؛ جماعات كثيرة والفوج قطيع من الناس وجمعه أفواج والفيوج جماعة والفيج الجماعة من الناس وأفائج وأفاوج يجمع أفواج أي فوجا بعد فوج (tahdhib)؛ الفوج الجماعة المارة المسرعة وجمعه أفواج (mufradat)
- **B002** iki yükselti arasındaki geniş açıklık — iki yükselti arasındaki geniş açıklık · yükseltiler arasındaki geniş açıklıklar · geniş düz arazi
  الفائجة متسع ما بين كل مرتفعين من غلظ أو رمل (sihah)؛ الفوائج متسع ما بين كل مرتفعين من غلظ أو رمل والفائج البساط الواسع من الأرض (tahdhib)

## س ء ل (root_000661): 67:8 سَأَلَهُمْ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 67:8 سَأَلَهُمْ: withheld observed target; not identity

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

## خ ز ن (root_000406): 67:8 خَزَنَتُهَآ

- **B001** saklayarak koruma — bir şeyi saklayarak koruma · bir şeyi güvenli bir yere koyup saklamak · bir şeyi saklamak veya kendine ayırmak · sırrı gizli tutmak · onu şükürle koruyup sürdürebilecek değilsiniz
  خزن الشيء إذا أحرزه في خزانة واختزنته لنفسي (ayn)؛ خزنت المال واختزنته جعلته في الخزانة وخزنت السر واختزنته كتمته (sihah)؛ خزن الشيء إذا أحرزه في خزانة واختزنه لنفسه وخزن المال إذا غيبه (tahdhib)؛ الخزن حفظ الشيء في الخزانة ثم يعبر به عن كل حفظ كحفظ السر ونحوه وما أنتم له بخازنين قيل حافظين له بالشكر (mufradat)؛ أصل يدل على صيانة الشيء وخزنت الدرهم وغيره وخزنت السر (maqayis)
- **B002** saklama yeri ve mecazi kaynak — saklama yeri · depo · saklama yerleri; mecazen kaynaklar · Tanrı'nın gizli bilgisi, yapabilecekleri, sınırsız iyiliği ve kudreti · göklerde ve yerde var edilebilecek her şeyin Tanrı'nın kudretinde bulunması · kalp, insanın sakladıklarının deposudur · Kur'an'ın her bölümü, içindeki anlamı saklayan bir kap gibidir · bir kentin, bir topluluğun bilgi ve dil bakımından başlıca dayanağı olması
  الخزانة الموضع الذي يخزن فيه الشيء وخزانتي قلبي والبصرة خزانة العرب (ayn)؛ المخزن ما يخزن فيه الشيء والخزانة واحدة الخزائن (sihah)؛ الخزانة اسم المكان الذي يخزن فيه الشيء وخزائن الله غيوب علم الله وآيات القرآن خزائن وشبه الآية بالوعاء الذي يجمع فيه المال المخزون فيه (tahdhib)؛ خزائنه ولله خزائن السماوات والأرض إشارة إلى قدرته أو إلى الحالة وخزائن الله مقدوراته وجوده الواسع وقدرته وقوله كن (mufradat)
- **B003** saklananı koruyan görevli ve koruma görevi — saklananı koruyan görevli · koruma görevlileri · koruma görevi · dilim, içimde tuttuklarımın koruyucusudur
  خازني لساني وإذا كان خازنك حفيظا والخزانة عمل الخازن (ayn)؛ خازنك حفيظا يعني اللسان والخزانة عمل الخازن (tahdhib)؛ الخزنة جمع الخازن وقال لهم خزنتها في صفة النار وصفة الجنة (mufradat)
- **B004** etin kokup bozulması [kalıp] — et kokup bozuldu
  خزن اللحم أي تغير (ayn)؛ خزن اللحم أنتن مثل خنز مقلوب منه (sihah)؛ خزن اللحم وخنز كله بمعنى واحد إذا تغير (tahdhib)؛ الخزن في اللحم أصله الادخار فكني به عن نتنه وخزن اللحم إذا أنتن وخنز بتقدم النون (mufradat)؛ خزن اللحم تغيرت رائحته فليس من هذا إنما هذا من المقلوب والأصل خنز (maqayis)؛ خنز اللحم إذا تغيرت رائحته وخزن وقد مضى (maqayis)
- **B005** en kısa yolu seçme [kalıp] — kestirme yolu seçmek · yolun en yakın ve kısa bölümleri
  اختزنت طريقا واختصرته وأخذنا مخازن الطريق ومخاصرها أي أخذنا أقربها (tahdhib)
- **B006** yoksulluktan sonra varlıklı olma — yoksulluktan sonra varlıklı olmak
  أخزن الرجل إذا استغنى بعد فقر (tahdhib)

## ء ت ي (root_000009): 67:8 يَأْتِكُمْ, 67:30 يَأْتِيكُم

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

## ن ذ ر (root_001488): 67:8 نَذِيرٌ, 67:9 نَذِيرٌ, 67:17 نَذِيرِ, 67:26 نَذِيرٌ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ق و ل (root_001272): 67:9 قَالُوا۟, 67:9 وَقُلْنَا, 67:10 وَقَالُوا۟, 67:13 قَوْلَكُمْ, 67:23 قُلْ, 67:24 قُلْ, 67:25 وَيَقُولُونَ, 67:26 قُلْ, 67:27 وَقِيلَ, 67:28 قُلْ, 67:29 قُلْ, 67:30 قُلْ

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

## ق ل ل (root_001251): 67:23 قَلِيلًا (also echo for 67:9 قَالُوا۟, 67:9 وَقُلْنَا, 67:10 وَقَالُوا۟, 67:13 قَوْلَكُمْ, 67:23 قُلْ, 67:24 قُلْ, 67:25 وَيَقُولُونَ, 67:26 قُلْ, 67:27 وَقِيلَ, 67:28 قُلْ, 67:29 قُلْ, 67:30 قُلْ)

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

## ج ي ء (root_000281): 67:9 جَآءَنَا

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

## ج ي ء (root_000282): 67:9 جَآءَنَا

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ك ذ ب (root_001290): 67:9 فَكَذَّبْنَا, 67:18 كَذَّبَ

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

## ن ز ل (root_001492): 67:9 نَزَّلَ

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

## ء ل ه (root_000047): 67:9 ٱللَّهُ, 67:26 ٱللَّهِ, 67:28 ٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 67:9 ٱللَّهُ, 67:26 ٱللَّهِ, 67:28 ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ض ل ل (root_000913): 67:9 ضَلَٰلٍ, 67:29 ضَلَٰلٍ

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

## ك ب ر (root_001281): 67:9 كَبِيرٍ, 67:12 كَبِيرٌ

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

## ك و ن (root_001332): 67:10 كُنَّا, 67:10 كُنَّا, 67:18 كَانَ, 67:25 كُنتُمْ, 67:27 كُنتُم

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

## ع ق ل (root_001036): 67:10 نَعْقِلُ

- **B001** bilgiyi edinip kavrama, ayırt etme ve davranışı denetleme yetisi — kavrama, ayırt etme ve bilgi edinme yetisi · bilmediğini kavramak veya yanlış davranıştan geri durmak · anlayışlı ve ayırt etme gücü olan · çok iyi anlayan ve duyduğunu unutmayan · zihinde kavranan şey veya kavrama gücü · anlayışlı görünmeye çalışmak · öyle olmadığı halde anlayışlı görünmek
  العقل نقيض الجهل (maqayis;ayn)؛ عقل يعقل عقلا إذا عرف ما كان يجهله أو انزجر عما كان يفعله (maqayis)؛ العقل الحجر والنهى (sihah)؛ القوة المتهيئة لقبول العلم والعلم الذي يستفيده الإنسان (mufradat)؛ العقل التثبت في الأمور والقلب (tahdhib)
- **B002** devenin ön ayağını büküp bağlayarak tutma — devenin ön ayağını büküp bağlamak · devenin ön ayağını bağlayan ip · kadının saçını tarayıp toplaması
  عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط (maqayis)؛ عقلت البعير عقلا شددت يده بالعقال أي الرباط (ayn)؛ عقلت البعير أعقله عقلا وهو أن تثني وظيفه مع ذراعه (sihah)؛ أصل العقل مصدر عقلت البعير بالعقال والعقال حبل (tahdhib)؛ كعقل البعير بالعقال (mufradat)؛ عقلت المرأة شعرها (sihah;tahdhib;mufradat)
- **B003** dilin tutulup konuşamaz hâle gelmesi — dili tutulup konuşamaz hâle gelmek · dilini tutup konuşmasını engellemek
  اعتقل لسان فلان إذا احتبس عن الكلام (maqayis)؛ اعتقل لسانه إذا لم يقدر على الكلام (sihah;tahdhib)؛ عقل لسانه كفه (mufradat)
- **B004** öldürme veya yaralama karşılığı ödeme ve bu yükü paylaşma düzeni — öldürme veya yaralama için ödenen karşılık · öldürülen kişinin karşılığını ödemek · birinin yaralama yükünü üstlenip karşılığını ödemek · yanlışlıkla öldürmede ödemeyi üstlenen baba yanından yakınlar · bir topluluğun üstüne düşen öldürme karşılığı payı · yaralama karşılıklarında belirli sınıra kadar denk olmak
  العقل وهي الدية (maqayis;sihah;tahdhib)؛ عقلت القتيل أعطيته ديته (maqayis;ayn;sihah;tahdhib;mufradat)؛ العاقلة القوم تقسم عليهم الدية (maqayis)؛ العاقلة هم العصبة (tahdhib)؛ دية معقلة على قومه (mufradat)
- **B005** yıllık hayvan vergisi ve bunun tahsili — bir yıllık hayvan vergisi veya onunla birlikte verilen pay · iki yıllık hayvan vergisi · vergi görevlisinin zorunlu payı teslim alması
  العقال صدقة عام من الإبل (ayn)؛ الصدقة كلها عقال (maqayis)؛ العقال صدقة عام (sihah;tahdhib;mufradat)؛ على بني فلان عقالان أي صدقة سنتين (sihah)؛ أعطى معها عقلها وأرويتها (maqayis)
- **B006** ishali yiyecek veya ilaçla durdurma — yiyecek veya ilacın ishali durdurması · ishal kesici ilaç
  عقل الطعام بطنه إذا أمسكه (maqayis)؛ العقول من الدواء ما يمسك البطن (maqayis;sihah)؛ عقل بطن المريض بعدما استطلق استمسك (ayn)؛ عقل الدواء بطنه أي أمسكه (sihah;tahdhib;mufradat)
- **B007** korunaklı sığınak ve oraya çekilerek korunma — sığınak ve sağlam korunaklı yer · korunmak için sığınılan yer · geyik veya dağ keçisinin yüksek dağa sığınıp korunması
  المعقل والعقل وهو الحصن (maqayis)؛ العقل الحصن وجمعه العقول وهو المعقل أيضا (ayn)؛ العقل الملجأ والمعقل الملجأ (sihah)؛ المعقل وهو الملجأ (tahdhib;mufradat)؛ عقل الظبي إذا امتنع في الجبل (maqayis;tahdhib)؛ عقل الوعل أي امتنع في الجبل العالي (sihah)
- **B008** bir topluluğun veya türün en seçkin ve değerli örneği — seçkin ve değerli kadın, kişi veya hayvan · her şeyin en değerli ve seçkin olanı · denizin değerli incisi
  فلانة عقيلة قومها فهي كريمتهم وخيارهم (maqayis)؛ العقيلة المرأة المخدرة المحبوسة في بيتها (ayn)؛ عقيلة كل شيء أكرمه (maqayis;ayn;sihah;tahdhib)؛ الدرة عقيلة البحر (maqayis;ayn;sihah;tahdhib)؛ العقيلة من النساء والدر وغيرهما التي تعقل أي تحرس وتمنع (mufradat)
- **B009** diz çarpışmasına yol açan bacak eğriliği veya hayvanlarda bacak hastalığı — dizlerin çarpışması veya bacak eğriliği · bacağı eğri ve dışa açık deve · hayvanın bacaklarını tutan hastalık veya topallık
  العقل في الرجلين اصطكاك الركبتين (maqayis)؛ العقل في الرجل اصطكاك الركبتين وقيل إلتواء في الرجل (ayn)؛ بعير أعقل وناقة عقلاء بين العقل وهو إلتواء في رجل البعير (ayn;sihah;tahdhib)؛ العقال داء يأخذ الدواب في الرجلين (maqayis;ayn)؛ العقال ظلع يأخذ في قوائم الدابة (sihah;tahdhib)
- **B010** bir şeyi bükülmüş bacaklar arasında sıkıştırıp tutma — mızrağı üzengi ile baldır arasına sıkıştırmak · koyunun ayağını sağmak için bacaklar arasında tutmak · güreşte rakibin bacaklarını kilitleme tekniği · rakibin bacağına bacağını dolayarak onu düşürmek
  اعتقل رمحه إذا وضعه بين ركابه وساقه (maqayis;sihah;tahdhib;mufradat)؛ اعتقل شاته إذا وضع رجلها بين فخذه وساقه فحلبها (maqayis;sihah;tahdhib)؛ لفلان عقلة يعتقل بها الناس إذا صارعهم عقل أرجلهم (maqayis;sihah;tahdhib)؛ اعتقل الرحل إذا ثنى رجله فوضعها على المورك (tahdhib)
- **B011** eğrilip kıvrılan bölüm veya iç içe yığılmış kum tepesi — nehir, vadi veya kumun eğri ve kıvrımlı bölümü · işlerin dolaşık ve çözülmesi güç yanları · iç içe geçmiş büyük kum tepesi
  العاقول من النهر والوادي ومن الأمور أيضا ما التبس واعوج (maqayis)؛ العاقول من النهر والوادي والرمل المعوج منه وعواقيل الأمور ما التبس منها (sihah)؛ العقنقل من الرمل وهو ما أرتكم منه (maqayis)؛ كل ما تحوى والتوى فهو عقنقل (maqayis)؛ العقنقل الكثيب العظيم المتداخل الرمل (sihah)
- **B012** gün ortasında gölgenin kısalıp sabit görünmesi — gölgenin gün ortasında kısalıp sabit görünmesi · topluluğun gölgenin kısaldığı öğle vaktine girmesi
  عقل الظل أي قام قائم الظهيرة (sihah)؛ أعقل القوم إذا عقل بهم الظل أي لجأ وقلص عند انتصاف النهار (sihah)؛ عقل الظل إذا قام قائم الظهيرة (tahdhib)
- **B013** kırmızı veya desenli dokuma giysi türü — kırmızı giysi veya desenli dokuma türü
  العقل ثوب تتخذه نساء الأعراب (ayn)؛ العقل ثوب أحمر (sihah)؛ يقال هما ضربان من البرود (ayn;sihah)؛ العقل ضرب من الوشي (tahdhib)
- **B014** büyünün bağlayıcı etkisi ve bunu çözme uygulaması — büyünün bağlayıcı etkisi
  به عقلة من السحر وقد عملت له نشرة (sihah)

## ص ح ب (root_000844): 67:10 أَصْحَٰبِ, 67:11 لِّأَصْحَٰبِ

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

## ع ر ف (root_001002): 67:11 فَٱعْتَرَفُوا۟

- **B001** kalıp sözlerde peş peşe gelme veya üst üste yığılma [kalıp] — birbiri ardından peş peşe gelme · at yelesi gibi art arda gönderilenler · katları üst üste konmuş yemek · çokluktan dolayı üst üste yığmak
  تتابع الشيء متصلا بعضه ببعض (maqayis)؛ جاءت القطا عرفا عرفا (maqayis;mufradat)؛ المرسلات عرفا متتابعة كعرف الفرس (sihah;tahdhib;mufradat)؛ خزير معرف بعضه على بعض (tahdhib)
- **B002** bir şeyin üzerindeki belirgin tepe, sırt veya üst çıkıntı — yele, ibik ya da belirgin yükselti · atın yelesini kırpmak · iki düzlük arasındaki yüksekçe arazi veya kum sırtı · yüksek yerler ya da yüksek bir duvar · denizin dalgalarının yükselmesi veya sıvının köpüklenmesi
  العرف عرف الفرس (maqayis;sihah;tahdhib;mufradat)؛ العرفة أرض منقادة مرتفعة (maqayis)؛ عرفت الفرس أي جززت عرفه (sihah)؛ الأعراف جمع عرف وهو كل عال مرتفع (tahdhib)؛ العرف والعرف الرمل المرتفع (sihah)؛ أعراف الرياح والسحاب أوائلها وأعاليها (tahdhib)
- **B003** bir iz veya belirti üzerinden tanıyıp ayırt etme — iz veya belirti üzerinden tanıma ve ayırt etme · bir şeyi bilip başkalarından ayırt etmek · bilinen ve ayırt edilmiş, bilinmez olmayan · topluluktakilerin birbirini tanıması · bildirme ve bilinir duruma getirme · birinin elindekini araştırıp öğrenmek · anlatının bir bölümünü bildirip bir bölümünü bırakmak · yerlerini önceden betimleyip tanınır kılmak
  عرف فلان فلانا عرفانا ومعرفة (maqayis)؛ عرفت الشيء معرفة وعرفانا (ayn;sihah;tahdhib)؛ المعرفة والعرفان إدراك الشيء بتفكر وتدبر لأثره (mufradat)؛ تعارف القوم أي عرف بعضهم بعضا (sihah;mufradat)؛ التعريف الإعلام (sihah)؛ تعرفت ما عند فلان أي تطلبت حتى عرفت (sihah)
- **B004** koku; ayrıca güzel kokulu duruma getirme — hoş ya da kötü olabilen koku · bir şeyi güzel kokulu duruma getirme · güzel kokuyla işlenmiş veya süslenmiş yemek · onlar için güzel kokulu ve süslü duruma getirmek · güzel kokuyu çok kullanmak ya da kullanmayı bırakmak
  العرف وهي الرائحة الطيبة (maqayis)؛ العرف الريح طيبة كانت أو منتنة (sihah)؛ العرف الرائحة تكون طيبة وغير طيبة (tahdhib)؛ التعريف التطييب (sihah)؛ عرفها لهم أي طيبها وزينها (mufradat)
- **B005** iyi sayılan ve benimsenen davranış veya iyilik — iyilik ve başkasına iyi davranma · düşünce veya bağlayıcı ölçülerce iyi sayılan davranış · bilinen ve beğenilen iş
  العرف المعروف (maqayis;ayn;tahdhib;mufradat)؛ المعروف ضد المنكر والعرف ضد النكر (sihah)؛ كل ما تعرفه النفس من الخير وتبسأ به وتطمئن إليه (tahdhib)؛ اسم لكل فعل يعرف بالعقل أو الشرع حسنه (mufradat)
- **B006** topluluğu tanıyan ve işlerini gözeten görevli — topluluğun işlerini bilen gözetmen veya temsilci · topluluk gözetmenliği görevi veya yetkisi
  العريف القيم بأمر قوم (maqayis;ayn)؛ العريف النقيب وهو دون الرئيس (sihah)؛ عريف القوم سيدهم (tahdhib)؛ العريف بمن يعرف الناس ويعرفهم (mufradat)
- **B007** belirli ibadet yeri, onun günü ve orada bulunup durma — belirli bir ibadet bölgesinin adı · insanların o ibadet yerinde durduğu belirli gün · belirli ibadet yerinde bulunup durma
  عرفات سميت بذلك لأن آدم وحواء تعارفا بها (maqayis)؛ يوم عرفة موقف الناس بعرفات (ayn)؛ عرفات موضع (sihah)؛ عرف الناس إذا شهدوا عرفة وهو المعرف للموقف بعرفات (tahdhib)؛ عرفات اسم لبقعة مخصوصة (mufradat)
- **B008** tanıyanı duyuruyla arama veya sorarak haber öğrenme [kalıp] — kayıp veya bulunan şeyi tanıyanı duyuruyla arama · insanlara bir haber öğrenmek için sormak · bulunan şeyi özelliklerinden tanıyan kişi
  التعريف تعريف الضالة واللقطة أن يقول من يعرف هذا (maqayis)؛ التعريف أن تصيب شيئا فتعرفه إذا ناديت من يعرف هذا (ayn)؛ التعريف إنشاد الضالة (sihah)؛ اعترفت القوم سألتهم (sihah;tahdhib)؛ من يعترفها فمعناه معرفته إياها بصفتها (tahdhib)
- **B009** bir şeyi veya suçu açıkça kabul edip üstlenme — bir şeyi veya suçu açıkça kabul etme · kişinin kendi suçunu kabul etmesi · kimsenin beni yenebileceğini kabul etmem
  اعترف بالشيء إذا أقر (maqayis)؛ الاعتراف الإقرار بالذنب والذل والمهانة والرضى به (ayn)؛ المعرف الاسم من الاعتراف وله علي ألف عرفا أي اعترافا (sihah)؛ عرف الرجل ذنبه إذا أقر به (tahdhib)؛ اعترف فلان إذا ذل وانقاد (tahdhib)
- **B010** yüklenilen duruma dayanıp içten sakinleşme — üzerine yüklenene dayanıp sakinleşen ruh · sıkıntı karşısında sabırlı kişi · sabır ve dayanma
  النفس عروف إذا حملت على أمر فباءت به أي اطمأنت (maqayis)؛ النفس عروف إذا حملت على أمر بسأت به أي اطمأنت (ayn)؛ العارف الصبور والعروف مثله (sihah)؛ رجل عارف أي صبور ونفس عروف صبور (tahdhib)؛ العرف بالكسر الصبر (tahdhib)
- **B011** avuç içinin açık bölümünde çıkan yara veya çıban — avuç içinin açık renkli bölümünde çıkan yara
  العرفة قرحة تخرج في بياض الكف (sihah;tahdhib)؛ عرف الرجال فهو معروف أي خرجت به تلك القرحة (sihah)
- **B012** gizli haber iddiacısı, hekim veya işinin uzmanı — gizli haber bildiğini öne süren kişi, hekim veya işinin uzmanı
  العراف الكاهن والطبيب (sihah)؛ للحازي عراف وللقناقن عراف وللطبيب عراف (tahdhib)؛ العراف كالكاهن إلا أن العراف يختص بمن يخبر بالأحوال المستقبلة (mufradat)
- **B013** yüzü veya araziyi tanıtan belirgin görünür bölümler — yüzler ve yüzün görünen bölümleri · arazinin tanınan ve görünür kısımları
  امرأة حسنة المعارف أي الوجه وما يظهر منها (sihah)؛ المعارف الوجوه والمعرف واحد (tahdhib)؛ معارف الأرض ما عرف منها (tahdhib)؛ أصبت عرفه أي خده (mufradat)
- **B014** kötülüğe hazırlanıp sert ve saldırgan bir tavır alma [kalıp] — kötülüğe hazırlanıp sert bir tavır almak
  اعرورف الرجل أي تهيأ للشر (sihah)؛ اعرورف فلان للشر كقولك اجثأل وتشزن (tahdhib)

## ذ ن ب (root_000521): 67:11 بِذَنۢبِهِمْ

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

## س ح ق (root_000683): 67:11 فَسُحْقًا

- **B001** ezip ufalamak — bir şeyi ezip ufalamak · ezilip ufalanmak
  سحقت الشيء أسحقه سحقا (maqayis;jamhara)؛ السحق دون الدق (ayn)؛ سحقت الشئ فانسحق (sihah)؛ السحق تفتيت الشيء ويستعمل في الدواء إذا فتت (mufradat)
- **B002** uzaklık ve uzaklaştırma — uzaklık; uzaklaştırma · Tanrı onu uzak etsin · çok uzak bir yer · Tanrı onu uzaklaştırdı · adam uzaklaşıp gitti · uzaklaştırma; uzağa düşürme
  السحق وهو البعد (maqayis)؛ السحق البعد (ayn)؛ أسحق الرجل إذا بعد (jamhara)؛ السحق بالضم البعد (sihah)؛ أبعده الله وأسحقه أي جعله سحيقا (mufradat)
- **B003** uzun boylu — uzun palmiye veya uzun boylu hayvan · uzun boylu dişi ve erkek eşek · uzun boylu · uzun palmiye
  السحوق النخلة الطويلة (maqayis)؛ أتان سحوق وحمار سحوق وهي طوال (ayn)؛ نخلة سحوق طويلة (jamhara)؛ السحوق من النخل الطويلة والسمحوق من النخل الطويلة (sihah)
- **B004** yıpranıp eskimek — eskimiş giysi · yıpranma onu eskitip tüketti · giysi eskidi ve yıprandı
  السحق الثوب البالي (maqayis;sihah;mufradat)؛ سحقه البلى فانسحق (maqayis;ayn)؛ أسحق الثوب إذا أخلق (jamhara;sihah;mufradat)
- **B005** sütü çekilip memesi yükselmek — memenin sütü çekilip karna doğru yükseldi · devenin sütü azalıp memesi yükseldi
  أسحق الضرع إذا ذهب لبنه وبلي (maqayis)؛ الاسحاق ارتفاع الضرع ولزوقه بالبطن (ayn)؛ أسحقت الناقة إذا ارتفع لبنها وقل (jamhara)؛ أسحق الضرع أي ذهب لبنه وبلي ولصق بالبطن (sihah)؛ أسحق الضرع أي صار سحقا لذهاب لبنه (mufradat)
- **B006** sıvıyı tüketmek ve tükenmiş göstermek — göz, gözyaşını tüketti · tükenmiş gözyaşı; tükenmiş gözyaşları · tükenmiş kan
  العين تسحق الدمع سحقا (maqayis;ayn)؛ دمع منسحق ودموع مساحيق (ayn)؛ دم منسحق وسحوق مستعار (mufradat)
- **B007** orta hızlı koşu — yürüyüşten hızlı, tam hızlı koşudan yavaş koşu
  السحق في العدو دون الحضر وفوق السحج (ayn)؛ السحق في العدو فوق المشي ودون الحضر (sihah)
- **B008** şiddetle kovmak — onu şiddetle kovdu
  سحقه وسحجه إذا طرده طردا شديدا (ayn)
- **B009** ayak tabanı esneklik kazanmak — devenin ayak tabanı alışıp esneklik kazandı
  أسحق خف البعير أي مرن (sihah)
- **B010** ince zar ve ince parçalar — kafatası kemiği üzerindeki ince zar; bu zara ulaşan baş yarası · ince bulut parçaları · karın iç zarındaki ince yağ parçaları
  السمحاق قشرة رقيقة فوق عظم الرأس (sihah)؛ الشجة إذا بلغت إليها سمحاقا (sihah)؛ سماحيق السماء القطع الرقاق من الغيم (sihah)؛ على ثرب الشاة سماحيق من شحم (sihah)

## خ ش ي (root_000413): 67:12 يَخْشَوْنَ

- **B001** korku duyma — korku; özellikle saygı ve bilgiyle karışan korku · korkmak · korkan erkek · korkan kadın · ondan daha çok korku duydum · bu yer ötekinden daha çok korku verir · onu korkuttu
  الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذاك أي أفزعه (ayn)؛ خشي الرجل يخشى خشية أي خاف فهو خشيان والمرأة خشياء؛ كنت أشد خشية منه؛ هذا المكان أخشى أي أشد خوفا؛ خشاه تخشية أي خوفه (sihah)؛ الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذلك المكان؛ معناها من الآدميين الخوف (tahdhib)؛ الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم (mufradat)؛ يدل على خوف وذعر فالخشية الخوف ورجل خشيان؛ كنت أشد خشية منه؛ هذا المكان أخشى من ذلك أي أشد خوفا (maqayis)
- **B002** bilmek — bildim
  خشيت بأن من تبع الهدى معناه علمت (sihah)؛ فخشينا أي فعلمنا (tahdhib)؛ المجاز قولهم خشيت بمعنى علمت؛ أي علمت (maqayis)
- **B003** istememe ve hoşnutsuzluk [kalıp] — Tanrı'ya yüklenen kullanımda istememe ve hoşnutsuzluk
  فخشينا أن يرهقهما طغيانا وكفرا قال الأخفش معناه كرهنا (sihah)؛ فخشينا عن الله لأن الخشية من الله تعالى معناها الكراهة ومعناها من الآدميين الخوف (tahdhib)
- **B004** kuruyup sertleşmiş veya buruşup niteliğini yitirmiş olma — buruşmuş, düşük nitelikli hurma · hurma ağacı buruşmuş, düşük nitelikli meyve verdi · kuru et
  الخشي وهو اليابس؛ الخشو الحشف من التمر؛ خشت النخلة تخشو إذا أحشفت (sihah)؛ مما شذ عن الباب وقد يمكن الجمع بينهما على بعد الخشو التمر الحشف؛ خشت النخلة تخشو خشوا؛ الخشي من اللحم اليابس (maqayis)

## غ ي ب (root_001117): 67:12 بِٱلْغَيْبِ

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

## ء ج ر (root_000015): 67:12 وَأَجْرٌ (also echo for 67:28 يُجِيرُ)

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## س ر ر (root_000697): 67:13 وَأَسِرُّوا۟

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

## ج ه ر (root_000269): 67:13 ٱجْهَرُوا۟

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

## ع ل م (root_001040): 67:13 عَلِيمٌۢ, 67:14 يَعْلَمُ, 67:17 فَسَتَعْلَمُونَ, 67:26 ٱلْعِلْمُ, 67:29 فَسَتَعْلَمُونَ

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

## ص د ر (root_000849): 67:13 ٱلصُّدُورِ

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

## ل ط ف (root_001356): 67:14 ٱللَّطِيفُ

- **B001** incitmeden iyilik ve özenle davranma — bir işi yumuşaklıkla yapma, iyilik ve ikram · kullarına şefkatli ve yumuşak davranan · çocuğuna iyilik eden ve onu gözeten anne · bu işi yumuşaklık ve idareyle yürüten · birine yumuşak davrandı · Tanrı, sevdiğin şeyi sana incitmeden ulaştırdı · Tanrı'nın yardım edip doğru sonuca eriştirmesi ve koruması · karşılıklı iyilik ve yumuşak davranış · işi yumuşaklıkla ele alma · kullarına yumuşak davranan; ince ayrıntıları bilen
  اللطف الرفق في العمل (maqayis;sihah)؛ لطيف بعباده أي رءوف رفيق (maqayis)؛ البر والتكرمة (ayn;tahdhib)؛ أم لطيفة بولدها تلطف إلطافا (ayn;tahdhib)؛ رفيق بمداراته (ayn)؛ التوفيق والعصمة (sihah)؛ يوصل إليك أربك في رفق (tahdhib)؛ لطف الله لك أي أوصل إليك ما تحب برفق (tahdhib)؛ لرفقه با (mufradat)
- **B002** küçüklük, incelik ve güç algılanırlık — kullarına yumuşak davranan; ince ayrıntıları bilen · küçüldü, inceldi ve hafifleşti · küçük, ince, hafif ve kaba olmayan · anlamı ince ya da örtük söz · ince, sert ve kaba olmayan çubuk · karnı çekik, beli ince kadın · incelik, küçüklük ve hafiflik · duyularla algılanamayacak kadar ince şeyler
  صغر في الشيء (maqayis)؛ لطيف الشيء الذي لا يتجافى من الكلام وغيره والعود ونحوه (ayn)؛ كلام لطيف وعود لطيف (ayn)؛ لطافة خلق غير جسيمة (ayn)؛ لطف الشيء يلطف لطافة أي صغر (sihah)؛ جارية لطيفة الخصر ضامرة البطن (tahdhib)؛ اللطيف من الكلام ما غمض معناه وخفي (tahdhib)؛ ضد الجثل وهو الثقيل (mufradat)؛ الحركة الخفيفة (mufradat)؛ تعاطي الأمور الدقيقة (mufradat)؛ اللطائف عما لا تدركه الحاسة (mufradat)؛ معرفته بدقائق الأمور (mufradat)
- **B003** iyiliği gösteren seçkin armağan — iyilik göstergesi olarak verilen seçkin armağan · ona bir şey vererek iyilik etti · falancadan gelen armağan
  اللطف من طرف التحف ما ألطفت به أخاك ليعرف به برك (ayn;tahdhib)؛ ألطفه بكذا أي بره به (sihah)؛ لطفة من فلان أي هدية (sihah)
- **B004** erkek devenin organını çiftleşme yerine yerleştirme — çiftleşme yerini bulamayan erkek devenin cinsel organını dişinin üreme açıklığına yerleştirmek · erkek devenin cinsel organını kendiliğinden dişinin üreme açıklığına sokması
  الإلطاف للبعير إذا لم يهتد لموضع الضراب فألطف له (maqayis)؛ ألطف الرجل البعير أدخل قضيبه في الحياء (sihah)؛ استلطف العبير أي أدخله فيها بنفسه (sihah)؛ إذا لم يسترشد لطروقته فأدخل الراعي قضيبه في حيائها قد أخلطه إخلاطا وألطفه إلطافا (tahdhib)؛ استلطف إذا فعل ذلك من تلقاء نفسه (tahdhib)
- **B005** bir nesneyi yana bitiştirme — nesneyi yanıma yapıştırdım · onu yanıma yapıştırdım · yana yapıştırılmış ya da giysinin altına yaklaştırılmış
  ألطفت الشيء بجنبي واستلطفته إذا ألصقته (tahdhib)؛ ضد جافيته عني (tahdhib)

## خ ب ر (root_000387): 67:14 ٱلْخَبِيرُ

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

## ء ر ض (root_000025): 67:15 ٱلْأَرْضَ, 67:16 ٱلْأَرْضَ, 67:24 ٱلْأَرْضِ

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

## ذ ل ل (root_000519): 67:15 ذَلُولًا

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

## م ش ي (root_001427): 67:15 فَٱمْشُوا۟, 67:22 يَمْشِى, 67:22 يَمْشِى

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

## ن ك ب (root_001546): 67:15 مَنَاكِبِهَا

- **B001** bir şeyden ya da izlenen yönden sapmak — bir şeyden, yoldan veya yönden sapmak · bir şeyden uzaklaşıp kaçınmak · ondan ayrılıp uzak durmak · onu bizden uzaklaştırmak
  نكب عن الشيء ينكب (maqayis)؛ كل شيء ملت عنه فقد تنكبته (jamhara)؛ نكب عن الطريق ينكب نكوبا أي عدل؛ نكبه تنكيبا أي عدل عنه واعتزله؛ تنكبه أي تجنبه (sihah)؛ نكب الدليل عن صوبه؛ نكب عنا أي نحه عنا؛ تنكب فلان عنا (tahdhib)؛ نكب عن كذا أي مال (mufradat)
- **B002** ana yönlerden sapan ara yön rüzgarı — ana rüzgar yönlerinden sapan ara yön rüzgarı · dört ara yön rüzgarı
  النَّكباء كل ريح عدلت عن مهب الرياح الأربع (maqayis)؛ النكباء ريح تجري بين مجرى ريحين (jamhara)؛ النكباء الريح الناكبة التي تنكب عن مهاب الرياح (sihah)؛ كل ريح من الرياح تحرفت فوقعت بين ريحين فهي نكباء (tahdhib)؛ النكباء ريح ناكبة عن المهب (mufradat)
- **B003** yürüyüşte veya duruşta yana eğiklik — yana eğik duran veya yürüyen · eğik yürüyen ya da duran · yürüyüşte yana eğilme · eğik boy
  الأنكب الذي كأنه يمشي في شق (maqayis)؛ المائل ناكب (jamhara)؛ النكب بالتحريك الميل في المشي؛ مائل الرأس أنكب (sihah)؛ النكب شبه ميل في المشي؛ قامة نكباء مائلة (tahdhib)؛ الأنكب المائل المنكب ومن الإبل الذي يمشي في شق (mufradat)
- **B004** omuz ve ona benzetilen yan bölüm — omuz; omuza benzetilen yan bölüm · dağın yanları · yayı veya sadağı omzuna asmak · yerin yüksek yanı, dağları, yolları veya kenarları
  المنكب مجتمع ما بين العضد والكتف (maqayis)؛ منكبا الإنسان معروفان؛ مناكب الجبل نواحيه (jamhara)؛ تنكب القوس أي ألقاها على منكبه؛ المنكب مجمع عظم العضد والكتف؛ المناكب في جناح الطائر؛ المنكب من الأرض الموضع المرتفع (sihah)؛ ينتكب كنانته ويتنكبها إذا ألقاها في منكبه؛ منكبا كل شيء؛ في جوانبها؛ في جبالها؛ في طرقها (tahdhib)؛ المنكب مجتمع ما بين العضد والكتف؛ منه استعير للأرض (mufradat)
- **B005** topluluğun güvendiği baş görevli [kalıp] — topluluğun güvendiği baş gözetmen veya yönetici yardımcısı · topluluğunun dayanağı ve baş gözetmeni olmak · topluluk içindeki önderlik ve dayanılma konumu
  المنكب عون العريف (maqayis)؛ نكب على قومه إذا كان منكبا لهم يعتمدون عليه وهو رأس العرفاء (sihah)؛ منكب القوم رأس العرفاء؛ له النكابة في قومه (tahdhib)؛ منكب القوم رأس العرفاء؛ ولفلان النكابة في قومه (mufradat)
- **B006** omuz hastalığı veya taşın ayak ucunu sıyırması — devenin omzunu tutan hastalık; omuz ağrısı · taşın tırnağı, toynağı veya yumuşak ayak tabanını sıyırması · taşla sıyrılmış yumuşak ayak tabanı
  النَّكَب داء يأخذ الإبل في مناكبها (maqayis)؛ نكبته الحجارة نكبا أي لثمته وخدشته؛ النكب داء يأخذ الإبل في مناكبها (sihah)؛ النكب أن ينكب الحجر ظفرا أو حافرا أو منسما؛ نكب فلان إذا اشتكى منكبه (tahdhib)؛ النكب داء يأخذ في المنكب (mufradat)
- **B007** kabı ters çevirip kuru içeriğini dökmek [kalıp] — kabın kuru içindekilerini devirip dökmek · sadağı ters çevirip okları boşaltmak
  نكبت الإناء أنكبه نكبا إذا صببت ما فيه ولا يكون للشيء السائل إنما يكون لليابس؛ نكب الرجل كنانته إذا ألقى ما فيها (jamhara)؛ نكب كنانته نكبا كبها (sihah)؛ نكب فلان كنانته إذا كبها ليخرج ما فيها من السهام (tahdhib)
- **B008** başa gelen yıkıcı kötü olay — zamanın getirdiği yıkıcı kötü olay · ağır bir kötü olayın vurduğu kimse
  أصابته نكبة من الدهر أي جائحة؛ المصاب بالنكبة منكوب (jamhara)؛ النكبة واحدة نكبات الدهر؛ أصابته نكبة؛ نكب فلان فهو منكوب (sihah)؛ نكبته حوادث الدهر وأصابته نكبة ونكبات ونكوب كثيرة (tahdhib)؛ نكبته حوادث الدهر أي هبت عليه هبوب النكباء (mufradat)
- **B009** toynak veya ayak tabanındaki dairesel oluşum — toynak veya yumuşak ayak tabanındaki dairesel işaret
  النكيب دائرة الحافر والخف (sihah)
- **B010** yanında yay bulunmayan kimse — yanında yay bulunmayan kimse
  الأنكب الذي لا قوس معه (sihah)

## ء ك ل (root_000043): 67:15 وَكُلُوا۟

- **B001** yeme, yiyecek ve yeme rolleri — yemek yemek · yiyecek · bir öğünlük yeme veya tek lokma · çok yiyen, obur · birlikte yemek yiyen kişi · başkasını doyuran kişi · yenilen şey, yiyecek · yenmek üzere hazırlanmış yiyecek
  الأكل معروف؛ أكلت الطعام أكلا ومأكلا؛ الأكل تناول المطعم؛ الأكلة المرة واللقمة؛ رجل أكول كثير الأكل؛ أكيلك الذي يؤاكلك؛ المؤكل المطعم
- **B002** ağaç ve ekin ürünü — ağacın meyvesi veya verimi
  أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر؛ أكل بستانك دائم وأكله ثمره؛ والأكل لما يؤكل قال تعالى أكلها دائم
- **B003** verilen pay ve geçimlik — dünya payı ve geniş geçimliği olan · yöneticilerin verdiği tahsisatlar · kişiye ayrılmış, hesabı sorulmayan pay
  الأكل حظ الرجل وما يعطاه من الدنيا؛ المأكلة ما جعل للإنسان لا يحاسب عليه؛ فلان ذو أكل إذا كان ذا حظ من الدنيا ورزق واسع؛ الأكل الطعمة؛ يعبر به عن النصيب
- **B004** malı harcama veya ele geçirme [kalıp] — malı harcamak veya tüketerek elden çıkarmak · insanların mallarını alıp onları sömürmek
  يستأكل قوما أي يأكل أموالهم؛ فلان يستأكل الضعفاء أي يأخذ أموالهم؛ يعبر بالأكل عن إنفاق المال؛ أكل المال بالباطل صرفه إلى ما ينافيه الحق
- **B005** ateşin tüketmesi, beslenmesi ve harlanması — ateş odunu yakıp tüketti · ateşi odunla besledi · ateş iyice harlandı · öfkesinden alevlendi · kılıç keskinliğinden parladı
  أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ الرجل إذا اشتد غضبه يأتكل؛ تأكل السيف أي توهج من الحدة؛ وعلى طريق التشبيه قيل أكلت النار الحطب
- **B006** aşınma, bozulma ve kaşıntı — beden veya baş kaşıntısı · dişlerde aşınma veya çürüme · deride işlenince ortaya çıkan ince kusurlu yer · gebe deve, yavrusunun çıkan tüyünden kaşınıp rahatsız oldu · aşınıp bozulmak
  الأكال الحكاك؛ الأكل في الأديم مكان رقيق؛ بأسنانه أكل؛ والأكال أن يتأكل عود أو شيء؛ في جسدي إكلة من الأكال؛ تأكل كذا فسد؛ أصابه إكال في رأسه وفي أسنانه
- **B007** av olmuş veya yenmek için ayrılmış hayvan — yırtıcının yiyip bıraktığı av · kurdun yediği koyun veya başka av · yenmek için ayrılıp beslenen koyun · ürünü yenmek üzere ayrılmış hurma ağaçları
  أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته؛ الأكولة من الشاء التي ترعى للأكل لا للنسل والبيع؛ الأكولة الشاة التي تعزل للأكل وتسمن؛ أكيلة السبع؛ الأكولة من الغنم ما يؤكل
- **B008** arkadan çekiştirip saygınlığı zedeleme [kalıp] — birinin saygınlığını arkadan çekiştirerek zedelemek · insanları sürekli arkalarından çekiştiren
  فلان ذو أكلة في الناس إذا كان يغتابهم؛ ذو أكلة وإكلة إذا كان يغتاب الناس؛ تأكل لحومنا وتغتابنا؛ أكل فلان فلانا اغتابه وكذا أكل لحمه
- **B009** söz taşıyarak arayı bozma [kalıp] — aralarında söz taşıyıp onları birbirine düşürmek · ara bozucu söz taşıyıcı
  آكلت بين القوم أفسدت؛ المؤكل النمام؛ الإيكال بين الناس السعي بينهم بالنمائم؛ آكلت بين القوم أي حرشت وأفسدت
- **B010** biçime bağlı adlandırmalar [kalıp] — bana yapmadığım veya almadığım şeyi yükledin · onu senin erişimine bıraktım
  أكلتني ما لم آكل أي ادعيته علي؛ آكلتني أيضا أي ادعيته علي؛ آكلتك فلانا إذا أمكنته منه؛ أليس قبيحا أن تؤكلني ما لم آكل
- **B011** bir başla doyacak kadar az topluluk [kalıp] — tek bir hayvan başının doyuracağı kadar az topluluk
  ما هم إلا أكلة رأس؛ هم أكلة رأس أي هم قليل يشبعهم رأس واحد؛ عبارة عن ناس من قلتهم يشبعهم رأس
- **B012** biçime bağlı adlandırmalar [kalıp] — ipliği çok, sık dokulu ve güçlü kumaş · akıl ve sağlam görüş sahibi kişi
  ثوب ذو أكل أي كثير الغزل؛ رجل ذو أكل ذو رأي وعقل؛ ثوب ذو أكل إذا كان كثير الغزل صفيقا؛ رجل ذو أكل إذا كان ذا عقل ورأي؛ ثوب ذو أكل كثير الغزل كذلك
- **B013** yemek yenilen kap veya yer — içinde yemek yenilen çanak veya tencere · kendisinden yemek yenilen yer
  المئكل إناء يؤكل فيه؛ المئكلة قصعة تشبع الرجلين والثلاثة؛ المأكلة والمأكلة الموضع الذي منه يؤكل؛ المئكلة ضرب من البرام وضرب من الأقداح وكل ما أكل فيه
- **B014** ete işleyen kesici veya vurucu araç [kalıp] — et kesen bıçak; ayrıca sivri sopa veya kamçı
  للسكين آكلة اللحم؛ آكلة اللحم عصا محددة؛ الأصل في هذا أنها السكين؛ قيل في آكلة اللحم إنها السياط

## ر ز ق (root_000560): 67:15 رِّزْقِهِۦ, 67:21 يَرْزُقُكُمْ, 67:21 رِزْقَهُۥ

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

## ن ش ر (root_001503): 67:15 ٱلنُّشُورُ

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

## ء م ن (root_000054): 67:16 ءَأَمِنتُم, 67:17 أَمِنتُم, 67:29 ءَامَنَّا

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## خ س ف (root_000410): 67:16 يَخْسِفَ

- **B001** yerin çöküp üzerindekini toprağa gömmesi — yerin içeri çöküp toprağa gömülmesi · Tanrı'nın yeri çökertip onu toprağa gömdürmesi · yerin çöküp onu içine alması · üzerine basanı içine alacak kadar yumuşak araziler
  الخسف غموض ظاهر الأرض (maqayis); الخسف سؤوخ الأرض بما عليها (ayn;tahdhib); خسف المكان ذهب في الأرض (sihah); أخاسيف من الأرض وهي اللينة (maqayis;sihah); خسفه الله وخسف هو (mufradat)
- **B002** Ay'ın veya Güneş'in ışığının kaybolması [kalıp] — Ay tutulması · Güneş tutulması veya Güneş'in göğe girmesi
  خسوف القمر (maqayis;sihah;mufradat); خسفت الشمس وكسفت بمعنى واحد (tahdhib); خسوف الشمس يوم القيامة دخولها في السماء (ayn;tahdhib); الخسوف إذا ذهب كله (mufradat)
- **B003** göz bebeğinin içeri göçüp görünmez olması [kalıp] — bebeği delinip içeri göçmüş göz · gözün körleşmesi veya içeri çökmesi
  انخسفت العين عميت (maqayis); عين خاسفة فقئت وغابت حدقتها (ayn;tahdhib); خسوف العين ذهابها في الرأس (sihah); عين خاسفة إذا غابت حدقتها (mufradat)
- **B004** kuyuda derin ve sürekli su kaynağına ulaşma — kayası delinerek bol ve tükenmez suya ulaşılmış kuyu · derin suya açılmış ya da suyu çekilip tükenmiş kuyu · kuyunun su çıkışı · kazıda sürekli yer altı suyuna ulaşma
  بئر خسيف إذا كسر جيلها فانهار ولم ينتزح ماؤها (maqayis); بئر خسيف مخسوفة أي نقب جبلها عن عيلم الماء فلا تنزف أبدا (ayn;tahdhib); خسف الركية مخرج مائها (sihah); الخسف أن يبلغ الحافر إلى ماء عد (tahdhib); بئر مخسوفة إذا غاب ماؤها ونزف (mufradat)
- **B005** eksilme, açlık ya da zayıflık — eksilme ve açlık · aç veya zayıf kimse · geceyi aç ve istediği yiyecekten yoksun geçirmek
  المهزول يسمى خاسفا (maqayis); بات على الخسف إذا بات جائعا (maqayis); الخسف النقصان (sihah;tahdhib); الخاسف المهزول (sihah;tahdhib); الخسف الجوع والخاسف الجائع (tahdhib)
- **B006** aşağılama ve istemediği yüke zorlama — horlanma, aşağı durum ve istemediği yüke zorlanma · onu aşağılayıp ağır sıkıntıya koşmak · hor ve aşağı duruma razı olmak · haksızlık ve baskı
  رضي بالخسف أي الدنية (maqayis;sihah); الخسف تحميلك إنسانا ما يكره (ayn;tahdhib); الخسف الجور بلغة الشحر (ayn); سامه الخسف أي أولاه ذلا وكلفه المشقة والذل (sihah); تحمل فلان خسفا (mufradat); الخسف الذل (tahdhib)
- **B007** bol su taşıma ya da bol süt verme — bol su taşıyan bulut · bol sütlü, sütü kışın çabuk kesilen dişi deve
  السحاب الذي يأتي بالماء الكثير خسيف (maqayis); الخسيف من السحاب ما نشأ من قبل العين وفيه ماء كثير (ayn); الخسيف من السحاب حامل ماء كثير (tahdhib); ناقة خسيفة أي غزيرة (maqayis); ناقة خسيف غزيرة سريعة القطع في الشتاء (ayn;tahdhib)
- **B008** yenilen ceviz — yenilen ceviz
  الخسف الجوز المأكول (maqayis); الخسف الجوز الذي يؤكل (tahdhib); الخسف الجوز بلغة الشحر (tahdhib)
- **B009** hareketli ve çevik oğlan [kalıp] — hareketli, çevik ve canlı oğlan
  يقال للغلام الخفيف النشيط خاسف وخاشف (tahdhib)

## م و ر (root_001456): 67:16 تَمُورُ

- **B001** enine gidip gelme ve dalgalanma — enine gidip gelmek, salınmak · gidip gelerek salınma · göğün dalgalanıp çalkalanması · dalga, dalgalanma · üst kolları yanları boyunca salınmak · saplamanın sağa veya sola yatması
  أصل صحيح يدل على تردد (maqayis)؛ المور الموج (maqayis;ayn;sihah)؛ مار الشيء يمور مورا أي تحرك وجاء وذهب (sihah)؛ يوم تمور السماء مورا (ayn;sihah;mufradat)؛ الطعنة تمور إذا مالت يمينا أو شمالا (ayn)
- **B002** kanın yüzeyde gidip gelerek yayılması; hızlı akış — kanın yüzeye dökülüp akarak yayılması · kanı akıtmak; alternatif rivayette başka bir köke bağlanan kullanım · akan kanlar · hızlı akış
  مار الدم على وجه الأرض انصب وتردد (maqayis;ayn)؛ مار الدم على وجه الأرض وأماره غيره (sihah)؛ مار الدم على وجهه (mufradat)؛ المور الجريان السريع (mufradat)
- **B003** rüzgârın döndürdüğü toz — rüzgârın savurup döndürdüğü toz veya toprak
  المور تراب تمور به الريح (maqayis)؛ المور تراب وجولان تمور به الريح (ayn)؛ المور بالضم الغبار بالريح (sihah)؛ التراب المتردد به الريح (mufradat)
- **B004** salınarak hızlı gidiş [kalıp] — salınarak hızla giden dişi deve · sırtı yürüyüşte salınan at
  الناقة تمور في سيرها وهي موارة سريعة (maqayis)؛ ناقة موراة سريعة في سيرها (ayn)؛ ناقة موارة اليد أي سريعة (sihah)؛ ناقة تمور في سيرها فهي موارة (mufradat)؛ فرس موارة الظهر (maqayis)
- **B005** ilk tüy örtüsünün dökülmesi — eşek veya sıpanın doğum tüylerinin dökülmesi · eşekten dökülen tüy parçası
  انمارت عقيقة الحمار سقطت عنه (maqayis;sihah)؛ انمارت لبدة الفحل وعقيقة الجحش إذا سقطت عنه (ayn)؛ الموارة نسيل الحمار وقد تمور عليه نسيله (sihah)
- **B006** gidilip gelinen yol — insanların gidip geldiği yol
  المور الطريق لأن الناس يمورون فيه أي يترددون (maqayis)؛ المور الطريق (sihah)
- **B007** aşağıya gitmek mi, dönüp yukarı gelmek mi — Aşağı bölgeye mi gitti, yoksa dönüp yüksek bölgeye mi geldi, bilmiyorum.
  لا أدري أغار أم مار أي أتى غورا أم دار فرجع إلى نجد (maqayis;sihah)
- **B008** darbede ilerleyen keskin kılıç — kesme darbesinde ilerleyen keskin kılıç
  المائر السيف القاطع الذي يمور في الضريبة (maqayis)؛ السائر الشعر المروي (maqayis)

## ر س ل (root_000563): 67:17 يُرْسِلَ

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

## ح ص ب (root_000325): 67:17 حَاصِبًا

- **B001** çakıl taşı, çakıllı zemin ve çakılla döşeme — çakıl taşı; küçük ya da büyük çakıllardan oluşan taş malzemesi · çakıllı arazi · ibadet yerini çakıl taşlarıyla döşemek
  الحَصْباء جنس من الحصى (maqayis)؛ الحصب بالحصباء أي صغار الحصى أو كبارها (ayn)؛ الحَصْباء الحصى الصغار (jamhara)؛ الحَصْباء الحصى (sihah)؛ أرض محصبة ذات حصباء (maqayis;sihah)؛ حصبت المسجد إذا فرشته بها (sihah)
- **B002** çakıl atma, karşılıklı taşlama ve atın koşuda çakıl kaldırması [kalıp] — birini çakıl taşıyla taşlamak · bir yere küçük çakıl taşları atmak · karşılıklı çakıl taşı atmak · at koşarken çakıl taşlarını havalandırmak
  حصبت الرجل بالحصباء (maqayis)؛ الحصب رمك بالحصباء (ayn)؛ تحاصبوا (ayn)؛ حصبت الموضع إذا ألقيت فيه الحصى الصغار (jamhara)؛ تحاصب القوم إذا تقاذفوا بالحصى (jamhara)؛ حصبت الرجل أي رميته بالحصباء (sihah)؛ أحصب الفرس أثار الحصباء في عدوه (sihah)
- **B003** toz taşıyıp çakıl kaldıran sert rüzgar; ince dolu ve kar serpintisi — toz taşıyan veya çakıl kaldıran sert rüzgar · saçılan ince dolu ve kar parçacıkları
  ريح حاصب إذا أتت بالغبار (maqayis)؛ الحاصب الريح تحمل التراب (ayn)؛ ما تناثر من دقاق البرد والثلج (ayn)؛ ريح حاصب تقشر الحصى عن وجه الأرض (jamhara)؛ الحاصب الريح الشديدة التي تثير الحصباء (sihah)
- **B004** ateşe atılan yakıt ve ateşi bu yolla besleme — ateşe atılan odun veya başka bir yakıt maddesi · ateşe odun ya da yakıt atmak · azap ateşine atılanlar
  الحصب الحطب للتنور أو في وقود (ayn)؛ كل شيء ألقيته في النار ليتقد فهو حصب لها (jamhara)؛ حَصَب جهنم (jamhara)؛ الحصب ما يحصب به في النار أي يرمى (sihah)؛ كل ما ألقيته في النار فقد حصبتها به (sihah)
- **B005** kızamık; vücutta çıkan döküntü ve kabarcıklar — kızamık; vücutta veya gövdenin yanında çıkan döküntü kabarcıkları · derisinde kızamık döküntüsü çıkmak
  الحصبة بثرة تخرج بالجسد (maqayis)؛ الحصبة معروفة تخرج بالجنب (ayn)؛ الحصبة داء يصيب الناس معروف وهو بثر يخرج على الإنسان (jamhara)؛ الحصبة بثر يخرج بالجسد (sihah)
- **B006** kutsal bölgedeki belirli konak alanı ve vadide kısa geceleme — kutsal şehir çevresindeki taş atma yerlerinin bulunduğu belirli konak alanı · vadide gecenin bir bölümünde uyuyup sonra kutsal şehre çıkma
  المحصب بمنى موضع الجمار (maqayis)؛ المحصب موضع الجمار (ayn)؛ التحصيب النوم بالشعب الذي مخرجه إلى الأبطح ساعة من الليل (ayn)؛ المحصب بمكة الموضع الذي يحصب فيه (jamhara)؛ المحصب موضع الجمار بمنى (sihah)
- **B007** yeryüzünde gitmek ve birinden hızla uzaklaşmak [kalıp] — yeryüzünde yol alıp gitmek · topluluk olarak yanındaki kişiden hızla uzaklaşmak
  حصب القوم عن صاحبهم يحصبون فذلك توليهم عنه مسرعين كالحاصب (maqayis)؛ حصب في الأرض ذهب فيها (sihah)
- **B008** soğuktan koyulaşıp yağı çıkmayan süt — soğuktan koyulaşıp yağı çıkmayan süt
  الحصب من الألبان الذي لا يخرج زبده (maqayis)؛ كأنه من برده يشتد حتى يصير كالحصباء فلا يخرج زبدا (maqayis)

## ق ب ل (root_001198): 67:18 قَبْلِهِمْ

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

## ن ك ر (root_001550): 67:18 نَكِيرِ

- **B001** tanımama ve tanınmış saymama — tanımamak; içten veya sözle kabul etmemek · tanımamak ya da yadsımak · yadırgayarak sormak veya karşı çıkmak · tanınmayan ya da belirsiz olan · yadsıma ve kabul etmeme · birbirini tanımıyormuş gibi davranma
  خلاف المعرفة التي يسكن إليها القلب (maqayis)؛ نكر الشيء وأنكره لم يقبله قلبه ولم يعترف به لسانه (maqayis)؛ النكرة نقيض المعرفة (ayn;tahdhib)؛ النكرة ضد المعرفة (sihah)؛ الإنكار ضد العرفان (mufradat)؛ الإنكار خلاف الاعتراف (maqayis)
- **B002** uyanıklık ve ince kavrayış — uyanıklık ve ince kavrayış · uyanık ve işbilir adam · uyanık ve işbilir adam · uyanık ve aklı başında kimse · işbilir uyanıklık
  النكر الدهاء (maqayis;ayn;tahdhib;mufradat)؛ رجل نكر ورجل منكر داه (ayn;sihah;tahdhib)؛ النكارة الدهاء (sihah)
- **B003** çetin ve yadırgatıcı durum — çetin ve ağır durum · tanınması güç, çetin iş · işin güçleşip ağırlaşması
  النكراء الأمر الصعب الشديد (maqayis)؛ النكر نعت للأمر الشديد (ayn;tahdhib)؛ النكر المنكر (sihah)؛ الأمر الصعب الذي لا يعرف (mufradat)؛ نكر الأمر نكارة (maqayis;sihah;mufradat)
- **B004** tanınmazlaştırma veya kötüleşme — iyi bir durumdan kötü bir duruma dönüşme · değiştirip tanınmaz hale getirmek · bir şeyi tanınmaz hale getirme
  التنكر التنقل من حال تسر إلى أخرى تكره (maqayis)؛ نكره فتنكر أي غيره فتغير إلى مجهول (sihah)؛ التنكر التغير عن حال تسرك إلى حال تكرهها (tahdhib)؛ تنكير الشيء جعله بحيث لا يعرف (mufradat)
- **B005** kanlı ya da irinli bedensel akıntı — bedenden çıkan kanlı ya da irinli akıntı · kan ve cerahat boşaltmak
  لما يخرج من الحولاء من دم وما أشبهه نكرة (maqayis)؛ النكرة اسم لما خرج من الحولاء وهو الخراج من قيح ودم كالصديد وكذلك من الزجير (tahdhib)؛ أسهل فلان نكرة ودما (tahdhib)
- **B006** çirkin bulunan eylem ve onu engelleme — aklın çirkin bulduğu, geri çevrilmesi gereken eylem · kötü eylemi değiştirme veya yapanı caydırma · kötü eylemi değiştirme ve caydırma · birini yaptığı kötülükten caydıracak biçimde davranmak · seslerin en çirkini
  المنكر واحد المناكر (sihah)؛ النكير والإنكار تغيير المنكر (sihah)؛ المنكر كل فعل تحكم العقول الصحيحة بقبحه (mufradat)؛ نكرت على فلان وأنكرت إذا فعلت به فعلا يردعه (mufradat)؛ النكير اسم للإنكار الذي معناه التغيير (tahdhib)؛ أنكر الأصوات أقبح الأصوات (tahdhib)
- **B007** karşılıklı düşmanlık ve çatışma — karşılıklı düşmanlık ve çatışma · onunla savaşmak ya da ona düşmanlık etmek · birbirine düşman olup çatışmak
  ناكره أي قاتله (sihah)؛ المناكرة المحاربة (tahdhib)؛ بينهما مناكَرة أي معاداة وقتال (tahdhib)؛ استعيرت المناكرة للمحاربة (mufradat)

## ط ي ر (root_000962): 67:19 ٱلطَّيْرِ

- **B001** kanatlı canlı ve uçuş — kuşlar; kuş türünden kanatlı canlı · kuş; havada uçan kanatlı canlı · kuşlar · uçmak; uçmuşçasına hızlanmak · uçma, uçuş · uçurmak, uçmaya yöneltmek · hızlı at · kuş desenli dokuma veya giysi · kuşu bol arazi
  الطير جمع طائر (maqayis;sihah;mufradat); الطائر كل ذي جناح يسبح في الهواء (mufradat); الطيران مصدر طار يطير (ayn;sihah); لكل من خف قد طار وكل سرعة (maqayis); فرس مطار للسريع وحديد الفؤاد (mufradat;ayn); المطير من البرود والثياب ما صور فيه صور الطيور (ayn); أرض مطارة كثيرة الطير (sihah)
- **B002** dağılıp yayılma — dağılmak, ayrılıp gitmek · ışığı ufka yayılmış tan · her yana yayılmış kötülük · havaya yayılmış toz · uzayıp dağılan saç · uzayıp yayılmış hörgüç ucu
  تطاير الشيء تفرق (maqayis;sihah); التطاير التفرق والذهاب (ayn); فجر مستطير إذا انتشر ضوؤه في الأفق (ayn); فجر مستطير أي فاش وغبار مستطار (mufradat); خذ ما طار من شعر رأسك أي ما انتشر (mufradat;sihah)
- **B003** belirtiyi uğur ya da uğursuzluk sayma — bir şeyi uğurlu ya da uğursuz saymak · uğursuzluk çıkarma; kötü sayılan belirti · kişiye yüklenen işi veya uğursuz payı · kuş hareketinden uğur ya da uğursuzluk çıkarma · uğursuzluk çıkarmayı reddeden söz · seni uğursuz saydık; ayrıca kaçırdık ya da kurtardık diye de açıklanır
  تطير من الشيء فاشتقاقه من الطير (maqayis); الطيرة مصدر قولك اطيرت أي تطيرت (ayn); الطائر من الزجر في التشؤم والتسعد (ayn); طائر الإنسان عمله الذي قلده (ayn;sihah); ألا إنما طائرهم عند الله أي شؤمهم (mufradat); كل إنسان ألزمناه طائره في عنقه أي عمله (mufradat)
- **B004** ağzı geniş kuyu [kalıp] — ağzı geniş kuyu · geniş ağızlı kuyu çukuru
  بئر مطارة إذا كانت واسعة الفم (maqayis); بئر مطارة واسعة الفم (sihah); جفر مطار (maqayis;sihah)
- **B005** öfkeli taşkınlık ve ölçüsüz atılganlık — öfke ve öfkeli taşkınlık · hafif ve düşünmeden davranan · taşkınlığının ve düşüncesizliğinin yanları · coşmuş, saldırgan köpek · yürekli, atılgan ve hızlı at
  الطيرة الغضب وسمي كذا لأنه يستطار له الإنسان (maqayis); في فلان طيرة وطيرورة أي خفة وطيش (sihah); ازجر أحناء طيرك أي جوانب خفتك وطيشك (sihah); كلب مستطير كما يقال للفحل هائج (ayn); فرس مستطار أي حديد الفؤاد ماض طيار (ayn); فرس مطار للسريع ولحديد الفؤاد (mufradat)
- **B006** kuşun durgunluğuyla anlatılan heybet veya bolluk [kalıp] — heybetten çıt çıkarmadan durmak · bolluk ve iyilik içinde olmak
  كأن على رؤوسهم الطير إذا سكنوا من هيبة (sihah); في الخصب وكثرة الخير قولهم في شيء لا يطير غرابه (sihah)

## ف و ق (root_001188): 67:19 فَوْقَهُمْ

- **B001** üstte bulunma — üstünde; yukarıda
  الفوق نقيض التحت (ayn;sihah;tahdhib)؛ الأول الفوق وهو العلو (maqayis)؛ فوق يستعمل في المكان والزمان والجسم (mufradat)؛ باعتبار العلو وباعتبار الصعود والحدور (mufradat)؛ يفوق السطح أي يعلوه (ayn)؛ يفوق سطحا أي يعلوه (tahdhib)
- **B002** değer ve mertebe üstünlüğü — derece ve erdem bakımından üstün · saygınlık ve değer bakımından arkadaşlarını aşmak · güzelliğiyle öne çıkan genç kadın · niteliği veya değeri çok yüksek · kısa bir sağım aralığı kadar bekleyerek veya paylaştırmada birini üstün tutarak
  فلان يفوق قومه أي يعلوهم (ayn;tahdhib)؛ جارية فائقة الجمال أي فاقت في الجمال (ayn;tahdhib)؛ فاق الرجل أصحابه يفوقهم أي علاهم بالشرف (sihah)؛ أمر فائق أي مرتفع عال (maqayis)؛ باعتبار الفضيلة الدنيوية أو الأخروية (mufradat)؛ الفوق أعلى الفضائل (tahdhib)
- **B003** baskın ve egemen olma — üzerinde egemen ve baskın
  السادس باعتبار القهر والغلبة؛ وهو القاهر فوق عباده؛ وإنا فوقهم قاهرون
- **B004** bir ölçü sınırını aşma — bir sayıdan, nicelikten veya ölçüden daha ileride
  يقال في العدد نحو فإن كن نساء فوق اثنتين (mufradat)؛ في الكبر والصغر مثلا ما بعوضة فما فوقها (mufradat)؛ فما فوقها قال أبو عبيدة فما دونها أي أعظم منها (sihah)؛ من قال أراد ما دونها فإنما قصد هذا المعنى وتصور بعض أهل اللغة أنه يعني أن فوق يستعمل بمعنى دون وهذا توهم منه (mufradat)
- **B005** bilincin veya gücün geri gelmesi — ayılmak veya yeniden güç kazanmak · hiçbir geri dönüşü, arası, dinlenmesi veya beklemesi olmamak · kuraklıktan sonra yeniden verimli olmak
  فواق ناقة بمعنى الإفاقة كإفاقة المغشي عليه أفاق يفيق إفاقة وفواقا (ayn;tahdhib)؛ كل مغشي عليه أو سكران إذا انجلى عنه ذلك قيل أفاق واستفاق (ayn)؛ استفاق من مرضه ومن سكره وأفاق بمعنى (sihah)؛ الإفاقة رجوع الفهم إلى الإنسان بعد السكر أو الجنون والقوة بعد المرض (mufradat)؛ ما لها من فواق أي ما لها من رجوع ولا مثنوية ولا ارتداد (maqayis)؛ أي ما لها من نظرة وراحة وإفاقة (sihah;tahdhib)؛ أفاق الزمان إذا أخصب بعد جدب (tahdhib)
- **B006** sağım arası süt dönüşü — devenin memesinde sütün yeniden birikmesi veya iki sağım arasındaki süre · iki sağım arasında memede biriken süt · devenin memesi yeniden sütle dolmak ve sağım vakti gelmek · kısa bir sağım aralığı kadar bekleyerek veya paylaştırmada birini üstün tutarak
  فواق الناقة رجوع اللبن في ضرعها بعد حلبها (ayn;tahdhib;maqayis)؛ ما بين الحلبتين من الوقت (sihah;mufradat)؛ كلما اجتمع من الفواق درة فاسمها الفيقة (ayn;tahdhib)؛ الفيقة ما اجتمع من الدرة في الضرع والأصل الواو (maqayis:2694)؛ أفاقت الناقة واستفاقها أهلها إذا نفسوا حلبها حتى تجتمع درتها (ayn;tahdhib)
- **B007** aralıklı küçük paylarla alma — yavruya sütü aralıklı küçük paylarla içirmek · yavrunun sütü ara ara içmesi · bir şeyi tek seferde değil, parça parça ve ara vererek almak veya okumak · azar azar alınan yiyecek veya içecek · içmeye hiç ara vermemek
  فوقت الفصيل أي سقيته اللبن فواقا فواقا وتفوق الفصيل إذا شرب اللبن كذلك (sihah)؛ أتفوقه تفوق اللقوح أي أقرأ منه شيئا بعد شيء (sihah;tahdhib;maqayis)؛ المفوق الذي يؤخذ قليلا قليلا من مأكول أو مشروب (tahdhib)؛ فوق فصيلك أي اسقه ساعة بعد ساعة وظل يتفوق المخض (mufradat)؛ لا يستفيق من الشراب أي لا يجعل لشربه وقتا (tahdhib)؛ خرجنا بعد أفاويق من الليل أي بعدما تمضي عامة الليل (tahdhib)
- **B008** bulut suyunun aralıklı yağış payları — bulutta biriken su veya ara ara yağan yağmur payları
  الأفاويق ما اجتمع من الماء في السحاب (ayn;maqayis)؛ الأفاويق أيضا ما اجتمع في السحاب من ماء فهو يمطر ساعة بعد ساعة (sihah)؛ أفاويق السحابة مطرها مرة بعد مرة (tahdhib)
- **B009** okun kiriş kertiği — okun kirişe oturan arka kertiği · okların kiriş kertikleri · ok kertiği adının sesçe çevrilmiş çoğul biçimi · kiriş kertiği eğri veya kırık ok · oka kiriş kertiği açmak veya kertiği düzeltmek · eksik bir payla veya sonuç alamadan dönmek
  الفوق مشق السهم حيث يقع الوتر (ayn;tahdhib)؛ الفوق موضع الوتر من السهم والجمع أفواق وفوق (sihah)؛ فوق السهم وسمى لأن الوتر يجعل فيه كأنه قد رد فيه والجمع أفواق (maqayis)؛ من فوق يشتق فوق السهم وسهم أفوق انكسر فوقه (mufradat)؛ سهم أفيق وأفوق إذا كان في الفوق ميل أو انكسار (ayn)؛ الأفوق السهم المكسور الفوق (sihah;tahdhib)؛ رجع فلان بأفوق ناصل أي بسهم منكسر لا نصل فيه (sihah;tahdhib)؛ الفقي ملين فجمع فوق وهو مقلوب وليس من هذا الباب (maqayis:2641)
- **B010** göğüsten yükselen kesik soluk — baskın hıçkırık veya göğüsten yükselen kesik soluk · son nefesini vermek üzere olmak
  الفواق ترجيع الشهقة الغالبة (ayn;tahdhib)؛ يفوق فواقا وفؤوقا (ayn;tahdhib)؛ وفاق الرجل فواقا إذا شخصت الريح من صدره (sihah)؛ فلان يفوق بنفسه فؤوقا إذا كانت نفسه على الخروج (sihah)؛ الفواق الذي يأخذ الإنسان عند النزع وكذلك الريح التي تشخص من صدره (sihah)؛ الفوق نفس الموت (tahdhib)؛ مما شذ عن هذين الأصلين قولهم هو يفوق بنفسه وهذا من باب الإبدال وإنما أصله يسوق (maqayis)
- **B011** yoksulluk ve gereksinim içinde olma — yoksulluk ve gereksinim · yoksullaşmak ve gereksinim içine düşmek
  الفاقة الحاجة ولا فعل لها (ayn;tahdhib)؛ الفاقة الفقر والحاجة وافتاق الرجل أي افتقر (sihah)؛ يقال من الفاقة إنه لمفتاق ذو فاقة (tahdhib)
- **B012** özel adlandırma kümesi — yemek dolu büyük kap; ayrıca pişmiş yağ, yağ veren bir ağaç veya çöl ve arazi için aktarılan ad
  الفاق الجفنة المملوءة طعاما (ayn;tahdhib)؛ الفاق الزيت المطبوخ (tahdhib)؛ الفاق البان (tahdhib)؛ الفاق الصحراء وقال مرة هي أرض (tahdhib)
- **B013** özel adlandırma kümesi — baş ile boynun birleşme yeri · erkeklik organının üst bölümü · her dişinde ok gezi gibi iki kertik bulunan çark
  الفائق موصل العنق في الرأس (sihah)؛ فوق الذكر أعلاه (tahdhib)؛ محالة فوقاء إذا كان لكل سن منها فوقان مثل فوقي السهم (tahdhib)

## ص ف ف (root_000871): 67:19 صَٰٓفَّٰتٍ

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

## ق ب ض (root_001197): 67:19 وَيَقْبِضْنَ

- **B001** bütün elle kavrayıp alma — bir şeyi bütün elle kavrayıp almak · bütün elle kavrayarak alma · bir avuçta alınan miktar
  قبضت الشيء من المال وغيره قبضا (maqayis)؛ القبض بجمع الكف على الشيء (ayn;tahdhib)؛ قبضت الشيء وقبضت عليه بيدي (jamhara)؛ قبضت الشئ قبضا أخذته (sihah)؛ القبض تناول الشيء بجميع الكف (mufradat)
- **B002** elle tutulan bölüm — bir aracın elle tutulan sapı ya da bölümü · sırığın veya sap takılmış bir aracın el yeri
  مقبض السيف ومقبضه حيث تقبض عليه (maqayis)؛ مقبض القوس حيث يقبض عليه بجمع اليد (ayn)؛ مقبض السيف قائمه (jamhara)؛ المقبض من القوس والسيف حيث يقبض عليه بجمع الكف (sihah)؛ مقبض السكين ومقبضته موضع اليد من القناة (tahdhib)
- **B003** malı denetime alıp iyeliğe katma; ettirgende alıcıya verme — senin iyeliğinde veya denetiminde · toplanıp elde edilmiş mal · malı ya da eşyayı kabul edip kendi alanına almak · malı onu alacak kişiye vermek
  القبض ما جمع من الغنائم وحصل (maqayis)؛ القبض ما جمع من الغنائم فألقي في قبضه (ayn;tahdhib)؛ صار في قبضك إذا صار في ملكك (jamhara;sihah)؛ تقبيض المال إعطاؤه لمن يأخذه (sihah)؛ قبض قبولك المتاع وإن لم تحوله وتحويلك المتاع إلى حيزك (tahdhib)
- **B004** bedeni toparlayarak hızla ilerleme veya sürme — hızla ilerleme ya da hızlı sürme · adımlarını çabuk aktararak hızlı giden · ayaklarını çabuk aktararak koşan at · hayvanı veya sürüyü hızlı süren sürücü · sert ve hızlı süren kişi ya da sürüyü çabuk yürüten eşek · toplulukça hızla yola koyulmak
  القبض الذي هو الإسراع إذا أسرع جمع نفسه وأطرافه (maqayis)؛ يسرعن في الطيران (maqayis)؛ القبيض السريع نقل القوائم (ayn;tahdhib)؛ القبض السوق السريع (ayn;sihah)؛ القابض السائق السريع السوق (jamhara;tahdhib)
- **B005** sürüyü dağıtmadan götürüp yerinde otlamaya salan çoban [kalıp] — sürüsünü dar alanda toplu otlatan çoban · sürüyü toplu götürüp uygun yerde otlamaya salan ölçülü çoban
  راع قبضة إذا كان لا يتفسح في مرعى غنمه (maqayis;jamhara;sihah)؛ قبضة رفضة أي يقبضها حتى إذا بلغ المكان يومه رفضها (maqayis)؛ الراعي الحسن التدبير الرفيق برعيته إنه لقبضة رفضة (tahdhib)
- **B006** içe toplanıp büzülme; kişide geri çekilme veya duraksama — bir şeyden tiksinip geri çekilmek · bir iş üzerinde durup ilerlememek · büzülme, kasılma ya da içe çekilme · kötülüğün kişiyi sıkıp içini daraltması
  انقبض عن الأمر وتقبض إذا اشمأز (maqayis)؛ إنه ليقبضني ما قبضك؛ الخير يبسطه والشر يقبضه؛ التقبض التشنج (ayn;tahdhib)؛ تقبض الرجل على الأمر إذا توقف عليه وتقبض عنه إذا اشمأز (jamhara)؛ الانقباض خلاف الانبساط؛ تقبضت الجلدة في النار إذا انزوت (sihah)؛ قبضها عن الشيء جمعها (mufradat)
- **B007** canın alınmasıyla yaşamın sona ermesi [kalıp] — kişinin ölmesi, yaşamının sona ermesi · ölüm anında canları alan görevli
  قبض الإنسان إذا مات (jamhara)؛ قبض فلان أي مات فهو مقبوض (sihah)؛ الملك قابض الأرواح (tahdhib)

## م س ك (root_001424): 67:19 يُمْسِكُهُنَّ, 67:21 أَمْسَكَ

- **B001** tutup alıkoymak veya sıkıca bağlanmak — bir şeyi tutmak, korumak veya alıkoymak · bir şeye sıkıca tutunmak ve onu dayanak edinmek · konuşmaktan kaçınıp susmak · bir şeyi ondan esirgemek veya ona vermemek · kendini tutmak veya sağlam durmak · onunla kokulan veya onu elinde tut · bir sözü birinin aleyhine kanıt olarak kullanmak · kitaba inanıp hükümlerine uymak
  حبس الشيء أو تحبسه (maqayis)؛ مسكت بالشيء وتمسكت به واستمسكت به (ayn)؛ أمسكت الشيء وتمسكت به واستمسكت به كله بمعنى اعتصمت به (sihah)؛ التمسك استمساكك بالشيء (tahdhib)؛ إمساك الشيء التعلق به وحفظه (mufradat)
- **B002** elindekini vermeyen cimrilik — elindekini vermeyen cimri · cimri adam · cimrilik ve eli sıkılık · cimri veya tuttuğunu bırakmayan adam
  البخيل ممسك والإمساك البخل والمسيك البخيل (maqayis)؛ في فلان إمساك ومساك ومسكة كله من البخل (ayn)؛ المسيك البخيل وفيه إمساك ومساك ومساكة أي بخل (sihah)؛ كل ذلك من البخل والتمسك بما لديه ضنا به (tahdhib)؛ كني عن البخل بالإمساك (mufradat)
- **B003** yaşamı sürdüren az miktar veya kalan pay [kalıp] — canı sürdürecek kadar yiyecek veya içecek · iyilik, güç veya akıldan kalan küçük pay
  المسكة ما يمسك الرمق من طعام أو شراب (ayn)؛ فيه مسكة من خير أي بقية (sihah)؛ المسكة من الطعام والشراب ما يمسك الرمق (tahdhib)؛ ما بفلان مسكة أي ما به قوة ولا عقل (tahdhib)؛ المسكة من الطعام والشراب ما يمسك الرمق (mufradat)
- **B004** suyu emmeden veya sızdırmadan tutan yer ya da kap [kalıp] — suyu emmeden tutan yer veya toprak · kuyunun örülmesi gerekmeyen sert kesimi · suyu sızdırmadan tutan su kabı · suyu emmeyen sert toprak
  المسكة من البئر المكان الصلب الذي لا يحتاج إلى طي (maqayis)؛ المساك من الأرض ما يمسك الماء (ayn)؛ سقاء مسيك كثير الأخذ (ayn)؛ المساك المكان الذي يمسك الماء (sihah)؛ قد بلغوا مسكة صلبة (tahdhib)؛ أرض مسيكة لا تنشف الماء (tahdhib)؛ التناهي التي تمسك ماء السماء مساك ومساكة (tahdhib)؛ المسيك من الأساقي الذي يحبس الماء فلا ينضح (tahdhib)
- **B005** gövdeyi veya kap içeriğini saran deri ve post — gövdeyi veya içindekini saran deri ve post · tilki postları
  المسك الإهاب لأنه يمسك فيه الشيء إذا جعل سقاء (maqayis)؛ المسك الإهاب (ayn)؛ المسك بالفتح الجلد (sihah)؛ المسك الجلد (tahdhib)؛ من مسك فرس ذبح (tahdhib)؛ الجلد الممسك للبدن (mufradat)
- **B006** boynuz veya fildişinden bilezik — boynuz veya fildişinden yapılmış bilezik
  المسك السوار من الذبل (maqayis)؛ المسك الذبل الواحدة مسكة (ayn)؛ أسورة من ذبل أو عاج (sihah)؛ مثل الأسورة من قرون أو عاج (tahdhib)؛ الذبل المشدود على المعصم (mufradat)
- **B007** kokulanmada kullanılan belirli yoğun koku maddesi — kokulanmada kullanılan yoğun koku maddesi · bu koku maddesiyle boyanmış kumaş · onunla kokulan veya onu elinde tut
  مما شذ عنه المسك من الطيب (maqayis)؛ المسك معروف ليس بعربي محض (ayn)؛ المسك من الطيب فارسي معرب (sihah)؛ المسك معروف إلا أنه ليس بعربي محض (tahdhib)؛ تمسكي أي تطيبي من المسك (tahdhib)
- **B008** ateşi oyukta yakıtla veya toprağa gömerek korumak [kalıp] — ateşi yakıtla örterek veya toprağa gömerek korumak
  مسكت بالنار تمسيكا وثقبت بها تثقيبا إذا فحصت لها في الأرض ثم جعلت عليها بعرا أو خشبا أو دفنتها في التراب
- **B009** insanları bağlayan sıkı akrabalık ilişkisi [kalıp] — insanları birbirine bağlayan sıkı akrabalık
  بيننا ماسكة رحم كقولك ماسة رحم وواشجة رحم
- **B010** yenidoğanın baş ve el uçlarındaki özel deri — yenidoğanın başında ve el uçlarında bulunan özel deri
  الماسكة الجلدة التي تكون على رأس الولد وعلى أطراف يديه
- **B011** at bacaklarının beyazlık dağılımını karşıt biçimde niteleme — sağ ve sol bacakları beyazlık dağılımına göre karşıt nitelenen at
  هو ممسك الأيامن مطلق الأياسر؛ كل قائمة بها بياض فهي ممسكة؛ جانب أمسك لا بياض
- **B012** düşmanına diken gibi takılan cesur kişi — düşmanına diken gibi takılan cesur kişi
  فلان حسكة مسكة أي شجاع كأنه حسك في حلق عدوه
- **B013** alışveriş için önceden verilen para — alışveriş için önceden verilen para
  المسكان العربان ويجمع مساكين يقال أعطه المسكان

## ج ن د (root_000264): 67:20 جُندٌ

- **B001** birlik olup destek veren topluluk — ordu; birbirini destekleyen yardımcılar topluluğu · onun yardımcıları ve destekçileri · aynı türden varlıkların oluşturduğu topluluk · ordular; topluluklar · ordular; topluluklar · canlar, uyumlarına göre birleşen ya da ayrışan kümelerdir · toplanıp düzenlenmiş topluluk · toplanmış ve düzenlenmiş
  يدل على التجمع والنصرة وأعوانه ونصاره (maqayis)؛ كل صنف من الخلق يقال لهم جند (ayn;tahdhib)؛ الجند الأعوان والأنصار (sihah)؛ الجند معروف جند وأجناد وجنود وجند مجند أي مجموع (jamhara)؛ يقال للعسكر الجند ولكل مجتمع جند (mufradat)
- **B002** beyaz taşlı sert arazi veya balçığı andıran taşlar — beyaz taşlar içeren sert arazi · balçığa benzeyen taşlar
  الجند الأرض الغليظة فيها حجارة بيض (maqayis)؛ الجند حجارة شبه الطين (ayn;tahdhib)؛ الجند الأرض الغليظة (jamhara)؛ الجند أي الأرض الغليظة التي فيها حجارة (mufradat)
- **B003** belirli yer ve idari bölge adları — Yemen'deki Jand şehri veya yeri · Şam'ın beş idari çevresi · Şam'daki Ajnadin yeri ve onunla anılan gün
  الأجناد أجناد الشام وهي خمسة (maqayis)؛ جند موضع باليمن (ayn)؛ الجند موضع باليمن وأجنادين موضع بالشام (jamhara)؛ جند بالتحريك بلد باليمن (sihah)؛ أجناد الشام خمس كور ويوم أجنادين (tahdhib)
- **B004** topluluk ve kişi adları ile aidiyet sıfatı — Yemen'den Janada topluluğu · Janad kişi adı · Janada kişi adı · Junayd kişi adı · Jand'a, o topluluğa veya yere mensup kimse
  جنادة حي من اليمن (ayn;tahdhib)؛ سمت العرب جنادا وجنادة وجنيدا (jamhara)؛ فلان الجندي (tahdhib)

## ن ص ر (root_001510): 67:20 يَنصُرُكُم

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

## د و ن (root_000502): 67:20 دُونِ

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

## غ ر ر (root_001078): 67:20 غُرُورٍ

- **B001** katlama ve kırılma izi — kumaşta veya deride kat ve kırık izi · kumaşı ilk kat izinden katla
  الغر وهو الكسر في الثوب (maqayis)؛ الغر الكسر في الثوب وفي الجلد (ayn)؛ غر الثوب وهو أثر تكسر الطي (jamhara)؛ الغرور مكاسر الجلد وطويت الثوب على غره (sihah)؛ مكاسر الجلد وخنثه أي على كسره (tahdhib)؛ غر الثوب أثر كسره (mufradat)
- **B002** örnek kalıp ve aynı örüntü — örnek kalıp; aynı biçimde ilerleyen düzen · aynı yol veya örüntü üzerinde
  الغرار المثال الذي يطبع عليه السهام وولدت على غرار واحد (maqayis)؛ الغرار المثال الذي تطبع عليه نصال السهام (ayn)؛ الغرار الطريقة وعلى غرار واحد (sihah)؛ الغرار الطريقة والمثال الذي يضرب النصال (tahdhib)
- **B003** alındaki ak leke ve görünür aklık — atın alnındaki ak leke; görünür aklık · ak; alnında belirgin aklık bulunan
  الغرة البياض وكل أبيض أغر (maqayis)؛ الغرة في الجبهة بياض والأغر الأبيض (ayn)؛ غرة الفرس وكل شيء بدا لك من ضوء (jamhara)؛ الغرة بياض في جبهة الفرس والأغر الأبيض (sihah)؛ الغرة من البياض في وجه الفرس (tahdhib)؛ غرة الفرس (mufradat)
- **B004** seçkinlik, önderlik ve güzel yaradılış — topluluğun önderi veya en seçkini · bağlama göre bir şeyin başlangıcı ya da en seçkin yanı · iyi ve yumuşak yaradılış
  غرة كل شيء أكرمه والغرير الخلق الحسن (maqayis)؛ فلان غرة من غرر قومه وغرة المتاع (ayn)؛ غرة القوم سيدهم (jamhara)؛ فلان غرة قومه أي سيدهم وغرة كل شيء أوله وأكرمه (sihah)؛ غرة المال أفضله وغرة القوم سيدهم (tahdhib)؛ فلان أغر إذا كان مشهورا كريما (mufradat)
- **B005** başlangıç ve ayın ilk geceleri — bağlama göre bir şeyin başlangıcı ya da en seçkin yanı · ayın ilk üç gecesi · ayın ince yayınının ilk görüldüğü gece
  لثلاث ليال من أول الشهر غرة (maqayis)؛ غرة كل شيء أوله وغرة الهلال والغرر ثلاثة أيام (ayn)؛ ثلاث ليال لأول الشهر يسمين الغرر (jamhara)؛ غرة كل شيء أوله والغرر ثلاث ليال (sihah)؛ ثلاث غرر واحدتها غرة وبياض الهلال (tahdhib)؛ الغرر لثلاث ليال من أول الشهر (mufradat)
- **B006** dölüt için köleyle ödenen kan bedeli [kalıp] — dölüt için erkek ya da kadın köleyle ödenen kan bedeli
  في الجنين غرة عبد أو أمة (maqayis)؛ في الجنين غرة يعني عبدا أو أمة (jamhara)؛ قضى في الجنين بغرة كأنه عبر عن الجسم كله بالغرة (sihah)؛ جعل في الجنين غرة عبدا أو أمة (tahdhib)
- **B007** deneyimsiz ve kötülüğü sezmeyen saflık — az deneyimli, saf ve uyanıksız · deneyimsiz veya kolayca aldanan · deneyim azlığı ve dalgın saflık
  الغرارة كالغفلة ومن نقصان الفطنة (maqayis)؛ الغر الذي لم يجرب الأمور والمؤمن غر كريم (ayn)؛ رجل غر إذا لم يجرب الأمور (jamhara)؛ رجل غر وغرير أي غير مجرب والغرة الغفلة (sihah)؛ الغر الذي لا يفطن للشر (tahdhib)؛ الغرة غفلة في اليقظة (mufradat)
- **B008** yanıltıcı görünüşle aldatma — birini yalan görünüş veya sözle aldatmak · kişiyi aldatan şey veya ayartıcı
  الغرور من غر يغر فيغتر به المغرور والغرور الشيطان (ayn)؛ غر الرجل الرجل إذا أوطأه عشوة أو خبره بكذب (jamhara)؛ غره يغره غرورا خدعه والغرور الشيطان (sihah)؛ لا تغرنكم الدنيا والغرور الشيطان والباطل (tahdhib)؛ الغرور كل ما يغر الإنسان من مال وجاه وشهوة وشيطان (mufradat)
- **B009** sonucu belirsiz tehlike — sonucu belirsiz tehlike · sonucu ve konusu belirsiz, güvencesiz satış · kendini tehlikeye atmak
  بيع الغرر وهو الخطر الذي لا يدري أيكون أم لا (maqayis)؛ الغرر كالخطر وغرر بماله أي حمله على الخطر (ayn)؛ الغرر الخطر وبيع الغرر (sihah)؛ بيع الغرر على غير عهدة ولا ثقة والبيوع المجهولة (tahdhib)؛ الغرر الخطر (mufradat)
- **B010** azalma, azlık ve eksik bırakma — azalma, azlık veya tamamlanmama · ibadeti ve selam karşılığını eksik bırakmamak · az ve kısa uyku · dişi devenin sütü azalmak
  غارت الناقة إذا نقص لبنها ولا غرار في صلاة والغرار النوم القليل (maqayis)؛ غرار نقصان لبن الناقة ولا غرار في الصلاة والغرار النوم القليل (ayn)؛ الغرار النوم القليل ونقصان لبن الناقة ولا غرار في صلاة (sihah)؛ الغرار النقصان وقل لبنها وغرار النوم قلته وما أقمت إلا غرارا وغارت السوق إذا كسدت (tahdhib)؛ الغرار لبن قليل وغارت الناقة قل لبنها (mufradat)
- **B011** ağza besin itme veya su kabını doldurma — kuş yavrusunun ağzına veya kursağına besin vermek · su kabını suya sokup elle doldurmak
  غر الطائر فرخه إذا زقه (maqayis)؛ الطائر يغر فرخه إذا زقه (ayn)؛ غر الطير فرخه إذا زقه (jamhara)؛ غر الطائر فرخه أي زقه (sihah)؛ الطائر يغر فرخه وغر في سقائك وغررت الأساقي إذا ملأتها (tahdhib)
- **B012** kılıcın veya bıçağın keskin ağzı [kalıp] — kılıcın keskin ağzı veya kesen kenarı
  غرار السيف وهو حده وكل شيء له حد فحده غرار (maqayis)؛ الغرار حد الشفرة والسيف (ayn)؛ الغراران شفرتا السيف وكل شيء له حد فحده غراره (sihah)؛ الغرار حد السيف وحد السكين الغرار (tahdhib)؛ غرار السيف أي حده (mufradat)
- **B013** yük taşımaya yarayan büyük çuval — yük taşımaya yarayan çuval veya büyük torba
  الغرارة وعاء (ayn)؛ الغرارة واحدة الغرائر التي للتبن وأظنه معربا (sihah)؛ الغرارة الجوالق وجمعها غرائر (tahdhib)
- **B014** biçime bağlı adlandırmalar — boğazda çalkalanma veya boğazdan yinelenen ses · ağız ve boğazda çalkalanan ilaç
  الغرغرة التغرغر في الحلق (ayn)؛ الغرغرة تردد الروح في الحلق والراعي يغرغر بصوته ويتغرغر بالدواء (sihah)؛ تغرغرت عينه بالدمع والغرغرة حكاية صوت وغرغر بالدواء (tahdhib)

## ل ج ج (root_001344): 67:21 لَّجُّوا۟

- **B001** inatla sürdürme ve geri adım atmama — bir işi inatla sürdürmek · inatla sürdürme ve diretme · çekişmeyi inatla sürdürme · çok inatçı ve direşken · yemininden dönmeyip telafi yoluna gitmemek
  اللجاج يقال لج يلج (maqayis)؛ لج يلج لجاجا (ayn)؛ لج يلج لجاجا إذا محك في الأمر (jamhara-108)؛ الملاجة التمادي في الخصومة (sihah)؛ إذا استلج أحدكم بيمينه (tahdhib)؛ اللجاج التمادي والعناد في تعاطي الفعل المزجور عنه (mufradat)
- **B002** denizin engin, derin ve dalgalı kesimi — denizin engin ve derin kesimi · engin ve derin deniz · denizin dalgaları çalkalanmak · geminin açık ve derin suya girmesi
  لج البحر وهو قاموسه وكذلك لجته (maqayis)؛ لجة البحر حيث لا ترى أرض ولا جبل؛ بحر لجي واسع اللجة (ayn)؛ لجة البحر والجمع لج ولجج (jamhara-108)؛ لجة البحر وهو معظم مائه؛ التج البحر إذا اضطربت أمواجه (jamhara-2260)؛ لجة الماء معظمه؛ لججت السفينة خاضت اللجة (sihah)؛ لجة البحر حيث لا يدرك قعره؛ لج البحر الماء الكثير الذي لا يرى طرفاه (tahdhib)؛ لجة البحر تردد أمواجه (mufradat)
- **B003** deniz gibi parıldayan heybetli kılıç — deniz gibi parıldayan heybetli kılıç
  السيف يسمى لجا (maqayis)؛ اللجة اسم من أسامي السيف وإنما هو اللج (ayn)؛ يعني السيف شبه بريقه بلجة البحر (jamhara-108)؛ اللج أيضا السيف (sihah)؛ عنى باللج السيف؛ شبهه بلجة البحر في هوله (tahdhib)؛ السيف المتموج ماؤه (mufradat)
- **B004** sözü ya da lokmayı ağızda yineleyip ilerletememe — konuşurken ya da yutarken takılıp yineleme · lokmayı ağızda çevirip yutmamak · dili ağır, sözünü açık söyleyemeyen · karışık ve anlaşılmaz söz
  لجلج الرجل المضغة في فيه إذا رددها ولم يسغها؛ اللجلاج الذي يلجلج في كلامه لا يعرب (maqayis)؛ اللجلجة كلام الرجل بلسان غير بين؛ كلام ملجلج مختلط (ayn)؛ اللجلجة والتلجلج التردد في الكلام؛ يلجلج المضغة (sihah)؛ اللجلجة أن يتكلم الرجل بلسان غير بين؛ لجلج الرجل اللقمة (tahdhib)؛ اللجلجة التردد في الكلام وفي ابتلاع الطعام (mufradat)
- **B005** topluluk seslerinin yükselip birbirine karışması [kalıp] — insanların sesleri ve uğultusu · sesler yükselip birbirine karışmak
  اللجة الجلبة (maqayis)؛ الأصوات اختلطت وارتفعت (ayn)؛ لجة القوم أي أصواتهم (jamhara-108)؛ لجة أصوات القوم إذا اجتمعوا (jamhara-2260)؛ لجة الناس أصواتهم وضجتهم؛ التجت الأصوات اختلطت (sihah)؛ التجت الأصوات إذا ارتفعت فاختلطت؛ اللجة الصوت (tahdhib)؛ لجة الصوت تردده (mufradat)
- **B006** açlıktan yüreğin durmaksızın çarpması [kalıp] — açlıktan yüreğin çarpıp sakinleşmemesi
  في فؤاد فلان لجاجة وهو أن يخفق لا يسكن من الجوع (maqayis)
- **B007** karanlığın ya da koyu rengin yoğunlaşması [kalıp] — karanlığın karışıp koyulaşması · gecenin kapkaranlık olması · kapkara göz · koyu ve yoğun yeşil toprak
  التجاج الظلام اختلاطه؛ عين ملتجة شديدة السواد (maqayis)؛ التج الظلام اختلط (ayn)؛ لج الليل شدة ظلمته وسواده؛ عين ملتجة شديدة السواد؛ الملتجة الأرض الشديدة الخضرة (tahdhib)؛ لجة الليل تردد ظلامه (mufradat)
- **B008** bir şeye el atıp kendine geçirme [kalıp] — bir şeye atılıp onu almak · başkasının malını kendinin olduğunu öne sürmek · birinin evini elinden almak
  فلان يلج بالشيء أي يبادر به فيؤخذ؛ تلجلج داره أي أخذها منه (ayn)؛ استلج فلان متاع فلان وتلججه إذا ادعاه (tahdhib)
- **B009** çok kalabalık topluluk — çok kalabalık topluluk
  اللجة الجماعة الكثيرة كلجة البحر وهي اللج (tahdhib)
- **B010** vadinin yanı ya da denizin eni [kalıp] — vadinin yanı · denizin eni
  لج الوادي جانبه؛ لج البحر عرضه (tahdhib)

## ع ت و (root_000981): 67:21 عُتُوٍّ

- **B001** kibirle itaati reddedip sınırı aşma — kibirli itaatsizlik ve sınır tanımazlık · kibirlenip itaate yanaşmamak ve sınırı aşmak · itaate yanaşmayan kibirli zorba · itaate yanaşmayan kibirli zorbalar · itaat etmemek ve karşı gelmek · ahlaksız ve azgın erkekler
  أصل صحيح يدل على استكبار (maqayis)؛ عتا عتوا وعتيا إذا استكبر (ayn)؛ تعتى فلان وتعتت فلانة إذا لم تطع (maqayis;ayn)؛ مجاوزة الحد إذا استكبر (tahdhib)؛ العتو النبو عن الطاعة (mufradat)
- **B002** son sınırına varma; yaşlılıkta geri döndürülemez gerileme — yaşlanıp ömrün gerileme dönemine girmek; son sınırına ulaşmak · düzeltilmesi mümkün olmayan ileri yaşlılık durumu
  عتا الشيخ يعتو عتيا وعتيا كبر وولى (sihah)؛ كل شيء قد انتهى فقد عتا (tahdhib)؛ من الكبر عتيا أي حالة لا سبيل إلى إصلاحها ومداواتها (mufradat)

## ن ف ر (root_001532): 67:21 وَنُفُورٍ

- **B001** ürküntüyle uzaklaşma veya uzaklaştırma — ürküp, tedirgin olup veya yüz çevirip uzaklaşmak · uzaklaşma; yüz çevirme · ürkütüp ya da soğutup uzaklaştırmak · ürküp kaçan ya da ürküten · eşinin eziyeti yüzünden ondan ürküp ayrılıktan korkan kadın
  أصل صحيح يدل على تجاف وتباعد (maqayis)؛ نفرت الدابة نفارا ونفورا (maqayis;sihah;tahdhib)؛ نفور أي تباعد عن الحق (tahdhib;mufradat)؛ مستنفرة بمعنى نافرة أو مذعورة (sihah;tahdhib;mufradat)
- **B002** çağrı üzerine savaşa veya yardıma çıkma — savaşa, yardıma veya önemli bir işe kalkıp gitmek · insanları savaşa ya da ortak göreve çıkmaya çağırmak
  ينفرون للنصرة (maqayis)؛ إذا حزبهم أمر اجتمعوا ونفروا إلى عدوهم (ayn)؛ نفر القوم في الأمور نفورا (sihah)؛ استنفر الإمام الناس لجهاد العدو فنفروا (tahdhib)؛ نفر إلى الحرب وينفر نفرا (mufradat)
- **B003** üç-on kişilik erkek topluluğu veya yakın destek çevresi — üçten ona kadar erkekten oluşan grup; kişinin yakınları ve destekçileri · birlikte harekete geçen topluluk; kişinin yakın çevresi · kişinin ailesi ve yakın erkek çevresi
  النفير النفر وكذا النفر والنفرة (maqayis)؛ النفر من الثلاثة إلى العشرة (ayn;sihah;tahdhib)؛ نفرك أي رهطك (ayn)؛ نفرة الرجل ونفره أي رهطه وأسرته (sihah;tahdhib)؛ عدة رجال يمكنهم النفر (mufradat)
- **B004** Mina adlı hac konaklama alanından ikinci veya üçüncü gün ayrılma [kalıp] — Mina adlı hac konaklama alanından çıkış günü; ilk veya ikinci ayrılış günü · hac yolcusunun Mina adlı konaklama alanından ayrılması
  يوم النفر يوم ينفر الناس عن منى (maqayis)؛ النفر نفر الحجاج في الثاني والثالث (ayn)؛ نفر الحاج من منى نفرا (sihah)؛ يوم النفر الأول ثم يوم النفر الثاني (tahdhib)؛ ومنه يوم النفر (mufradat)
- **B005** hastalık yüzünden şişip kabarma [kalıp] — derinin, ağzın veya yaranın şişip kabarması
  نفر جلده ورم (maqayis;sihah;mufradat)؛ نفر الجرح إذا ورم نفورا (tahdhib)؛ نفر فمه أي ورم (maqayis;sihah;tahdhib)؛ من نفار الشيء عن الشيء وتجافيه عنه (maqayis;sihah;tahdhib;mufradat)
- **B006** çekişme veya üstünlük iddiasını hakeme götürme — iki kişinin çekişme veya övünme yarışını karar için hakeme götürmesi · biriyle çekişme veya övünme yarışına girip hakeme başvurmak · onu üstün saymak veya onun üstünlüğüne hükmetmek
  المنافرة المحاكمة إلى القاضي بين اثنين (maqayis)؛ المحاكمة إلى من يقضي في خصومة أو مفاخرة (ayn)؛ المنافرة المحاكمة في الحسب (sihah)؛ أن يفتخر الرجلان ثم يحكما بينهما رجلا (tahdhib)؛ المنافرة المحاكمة في المفاخرة (mufradat)
- **B007** çocuğa kötülüğü uzaklaştıracak caydırıcı ad takma [kalıp] — çocuğa zararlı güçleri uzaklaştıracağı düşünülen caydırıcı bir ad takmak
  نفرت عن الصبي أي لقبته لقبا تنفيرا للجن عنه وللعين (maqayis)؛ نفر عنه أي لقبه لقبا تنفير للجن والعين عنه (sihah)؛ نفر فلان إذا سمي باسم يزعمون أن الشيطان ينفر عنه (mufradat)
- **B008** herkesten önce; ilk olarak — herkesten önce; ilk olarak
  لقيته قبل صيح ونفر أي قبل كل صائح ونافر (maqayis)؛ قبل كل صيح ونفر أي أولا (sihah)

## ك ب ب (root_001278): 67:22 مُكِبًّا

- **B001** yüzü üzerine çevirip düşürme — bir şeyi yüzü üzerine çevirmek veya düşürmek · develerin hastalık ya da güçsüzlükten yere serilmesi
  كببت الشيء لوجهه أكبه كبا (maqayis)؛ كببته لوجهه فانكب أي قلبته (ayn)؛ كببت الشيء أكبه كبا إذا قلبته (jamhara)؛ كبه الله لوجهه أي صرعه (sihah)؛ كببت فلانا لوجهه فانكب وكببت القصعة قلبتها على وجهها (tahdhib)؛ الكب إسقاط الشيء على وجهه (mufradat)
- **B002** üzerine eğilip bırakmadan uğraşma — bir işe kapanıp onu sürdürmek · bir kimseden isteğini ısrarla sürdürmek · işin üzerine eğilip onu bırakmamak · yüzünü aşağı eğmiş, işe kapanmış
  وأكب فلان على الأمر يفعله (maqayis)؛ وأكب القوم على الشيء يعلمونه وأكب فلان على فلان يطالبه (ayn)؛ وأكب الرجل على الشيء إذا عكف عليه وأكببت على الشيء إذا تجانأت عليه (jamhara)؛ وأكب فلان على الامر يفعله وانكب بمعنى (sihah)؛ وأكب الرجل على عمل يعمله وأكب فلان على فلان يطالبه (tahdhib)؛ الإكباب جعل وجهه مكبوبا على العمل (mufradat)
- **B003** çukura atıp art arda yuvarlama — bir şeyi çukura atıp art arda yuvarlamak
  والكبكبة أن يتدهور الشيء إذا ألقى في هوة حتى يستقر (maqayis)؛ والكبكبة الدهورة دهوروا وجمعوا ثم رمي بهم في هوة من النار (ayn)؛ وكبكبه أي كبه (sihah)؛ دهوروا وحقيقة ذلك في اللغة تكرير الانكباب (tahdhib)؛ والكبكبة تدهور الشيء في هوة (mufradat)
- **B004** toplanıp sıkışmış kütle veya topluluk — iplik yumağı · ipliği yumak yapmak · kum ya da nemli toprak kümesi · toprak ve benzeri maddelerden oluşmuş yığın · izdiham veya topluluk · at topluluğu · iri develer
  تجمع من الرمل كباب والكبة من الغزل والكبة الزحام والكبكبة الجماعة من الخيل (maqayis)؛ والكبكبة جماعة من الخيل وكببت الغزل جعلته كبة (ayn)؛ ونعم كباب أي كثير مجتمع والكب الشيء المجتمع من تراب وغيره وبه سميت كبة الغزل (jamhara)؛ والكبة من الغزل عربية معروفة (jamhara2)؛ الكبة الجروهق من الغزل والكبة أيضا الزحام والكباب ما تكبب من الرمل (sihah)؛ الكبة والكبكبة جماعة من الخيل والكبة الجماعة والكبة من الغزل والكباب ما تكبب من الرمل (tahdhib)
- **B005** birden bastıran sert atılım veya şiddet — savaşta veya koşuda atılım, hücum · kışın sert bastırması
  والكبة الحملة في الحروب (jamhara)؛ والكبة بالفتح الدفعة في القتال والجري وكذلك كبة الشتاء شدته ودفعته (sihah)؛ والكبة الدفعة في القتال وشدته وكذلك كبة الشتاء دفعته وشدته (tahdhib)
- **B006** yalıtık adlandırmalar — 
  كوكب الماء وهو معظمه والكوكب يسمى كوكبا من هذا القياس ولنور الروضة كوكب فذاك على التشبيه من باب الضياء ولبريق الكتيبة كوكب (maqayis)؛ والكواكب النجوم البادية ولا يقال لها كواكب إلا إذا بدت وكوكب العسكر ما يلمع فيها من الحديد (mufradat)

## و ج ه (root_001630): 67:22 وَجْهِهِۦٓ, 67:27 وُجُوهُ

- **B001** yüz ve bir şeyin öne bakan yanı — yüz; bir şeyin öne bakan veya görünen yanı · kötü bir yüz ifadesiyle bakmak
  الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)
- **B002** yön ve hedef; o yöne sevk etme veya yolu belli etme — yön, taraf · yönelinen yön veya hedef · bir şeyi belirli bir yöne çevirmek veya göndermek · tek bir yöne çevrilmiş · bir şeye doğru yönelmek · rüzgarın çakılı bir yöne sürüklemesi · yolu yürüyerek izini belirginleştirmek · perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak
  الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)
- **B003** karşı karşıya gelme ve doğrudan yüzüne söyleme — birinin karşısına çıkmak, onunla yüz yüze gelmek · karşılaşma, yüzleşme · karşında, tam karşı tarafta
  واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)
- **B004** yüzün varlığın kendisini temsil etmesi — 
  ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)
- **B005** amaç edinip yönelme; ibadette içtenlikle bağlanma — 
  وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)
- **B006** toplumsal itibar, yüksek mevki ve önde gelen kişi — topluluğun önderi · yerleşimin ileri gelenleri · itibarlı, yüksek mevkili · toplumsal itibar ve mevki · itibarlı ve yüksek mevkili olmak · onu itibarlı ve yüksek mevkili kılmak
  وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)
- **B007** günün başı, ilk saatleri [kalıp] — günün başı, ilk saatleri
  وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)
- **B008** sözün veya işin doğru yönü ve ona uygun düzenleme — sözün amaçlanan yönü · doğru görüş · aklına bir görüş gelmek · bir şeyi doğru yolundan saptırmak · işi gerektiği gibi düzenleyip her şeyi yerine koymak · hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi
  وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)
- **B009** yaşlanıp ömrünün son dönemine girmek — yaşlanıp ömrünün son dönemine girmek
  توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)
- **B010** doğumda ellerin veya ön ayakların önce çıkması — elleri veya ön ayakları önce çıkan yavru · yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak
  للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)
- **B011** kurucu uzun ünlü ile ana uyak harfi arasındaki harf — kurucu uzun ünlü ile ana uyak harfi arasındaki harf
  التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)
- **B012** hıyar veya kavunun altını kazıp yana yatırma — hıyar veya kavunun altını kazıp yana yatırma
  التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)
- **B013** yüzüne vurma ve yüzüne vurulmuş olma — birinin yüzüne vurmak · yüzüne vurulmuş
  وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)
- **B014** yanına gelen kişiyi geri çevirmek — yanına gelen kişiyi geri çevirmek
  أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)
- **B015** iki yüzlü nesne; içiyle dışı uyuşmayan kişi [kalıp] — iki yüzü bulunan kumaş · içiyle dışı uyuşmayan iki yüzlü kimse
  كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)

## ه د ي (root_001583): 67:22 أَهْدَىٰٓ

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

## ECHO ه د د (root_001580): for 67:22 أَهْدَىٰٓ: withheld observed target; not identity

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

## س و ي (root_000766): 67:22 سَوِيًّا

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

## ص ر ط (root_000858): 67:22 صِرَٰطٍ

- **B001** yol, özellikle düz yol — yol, özellikle düz yol · yol veya düz yol · yol
  الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)
- **B002** geçişte gözden kaybolmak; özellikle yiyeceği yutmak — yiyeceği boğazdan geçirip gözden kaybolacak biçimde yutmak · kolayca yutulan pelte kıvamlı tatlı · geniş boğazlı
  أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب؛ السرطراط على فعلال الفالوذ لأنه يسترط (maqayis 1774)؛ السرطم: الواسع الحلق، والميم فيه زائدة، وإنما هو من سرط، إذا بلع (maqayis السرطم)
- **B003** vuruşta kesip ilerleyen kılıç — vuruşta kesip ilerleyen kılıç
  والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)

## ق و م (root_001273): 67:22 مُّسْتَقِيمٍ

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

## ن ش ء (root_001502): 67:23 أَنشَأَكُمْ

- **B001** yükselmek veya yükseltmek — yükselmek, yukarı çıkmak · bulutun havada oluşup yükselmesi · Tanrı'nın bulutu yükseltmesi · yelkenleri kaldırılmış gemiler · yelkenlerini kaldıran gemiler · yükseltilmiş kum tepeleri
  أصل صحيح يدل على ارتفاع في شيء وسمو، ونشأ السحاب ارتفع، وأنشأه الله رفعه (maqayis)؛ أنشأ الله السحاب فنشأ أي ارتفع (ayn)؛ نشأت السحابة ارتفعت، والجوار المنشآت السفن التي رفع قلعها (sihah)؛ نشأ ارتفع، ونشأت السحابة ارتفعت، والمنشآت السفن المرفوعات الشرع (tahdhib)
- **B002** büyüyüp gençliğe erişmek — gençler, genç kuşak · çocukluk sınırını aşmaya yaklaşan gençler · çocukluğu geride bırakmış genç · büyüyüp gençliğe erişen kız · bir topluluk içinde büyüyüp yetişmek · süs içinde yetiştirilmek
  النشء والنشأ أحداث الناس، ونشأ فلان في بني فلان، والناشئ الشاب الذي نشأ وارتفع وعلا (maqayis)؛ النشأ أحداث الناس الصغار، والناشئ الشاب (ayn)؛ الناشئ الحدث الذي قد جاوز حد الصغر، ونشأت في بني فلان إذا شببت فيهم (sihah)؛ الناشئ الشاب حين نشأ أي بلغ قامة الرجل، وغلام ناشئ وجارية ناشئة (tahdhib)؛ أومن ينشأ في الحلية أي يربى (mufradat)
- **B003** gece içinde başlayan kalkış ya da zaman dilimi — Tanrı'ya yönelmek için geceleyin kalkıp ayakta durma · gecenin başı veya ilk saatleri · gecenin bütün saatleri veya gece içinde ortaya çıkanlar · uykudan sonraki gece bölümü
  ناشئة الليل يراد بها القيام والانتصاب للصلاة (maqayis;mufradat)؛ الناشئة أول الليل (ayn)؛ ناشئة الليل أول ساعاته أو ما ينشأ في الليل من الطاعات (sihah)؛ ناشئة الليل ساعاته كلها أو أوله أو ما كان بعد النوم أو متى قمت (tahdhib)
- **B004** bir işe ya da söze başlamak [kalıp] — bir işi yapmaya başlamak · bir konuşmaya başlamak · anlatılar kurup ortaya koymak · şiir söylemeye veya söylev vermeye başlamak ve bunu iyi yapmak
  أنشأ فلان حديثا وأنشأ ينشد ويقول (maqayis)؛ أنشأت حديثا ابتدأت (ayn)؛ أنشأ يفعل كذا أي ابتدأ، وفلان ينشئ الأحاديث أي يضعها (sihah)؛ أنشأ إذا أنشد شعرا أو خطب خطبة، وأنشأ فلان حديثا أي ابتدأ حديثا ورفعه (tahdhib)
- **B005** rüzgârı burnuna çekerek koklamak [kalıp] — rüzgârı burnuna çekerek koklamak
  استنشأت الريح تشممتها كأنك ترفعها إلى أنفك (maqayis)؛ الذئب يستنشئ الريح بالهمز، وإنما هو من نشيت الريح غير مهموز أي شممتها (sihah)
- **B006** var edip geliştirmek — Tanrı'nın bir şeyi yaratıp var etmesi · var oluş, meydana getirilme ve yetiştirilme · yaratma ve meydana getirme · bir şeyi var etme ve geliştirip yetiştirme · öteki yaşamı yaratıp var etme
  أنشأه الله خلقه، والاسم النشأة والنشاءة (sihah)؛ النشء والنشأة إحداث الشيء وتربيته، والإنشاء إيجاد الشيء وتربيته (mufradat)
- **B007** havuzun ilk ya da destekleyici taş bölümü — havuzun destek, başlangıç veya taban taşı
  نشيئة الحوض أعضاده إذا كان الحوض على وجه الأرض رفعت له نصائب الحجارة (ayn)؛ النشيئة أول ما يعمل من الحوض، وحجر يجعل أسفل الحوض (sihah)؛ النشيئة الحجر الذي يجعل أسفل الحوض، والنصائب ما نصب حوله (tahdhib)
- **B008** bir yere yönelip gelmek — yönelmek ya da bir yerden gelmek · nereden geldin · ihtiyacım için kalkıp ona doğru yürüdüm · işi için sabahleyin yola koyulmak · yaklaşıp uzaklaşan gemiler
  من أين أنشأت أي من أين جئت، وأنشأ فلان أقبل، وتنشأت إلى حاجتي نهضت إليها ومشيت، وتنشأ فلان غاديا إذا ذهب لحاجته، والمنشآت فهن اللائي يقبلن ويدبرن (tahdhib)
- **B009** dişi devenin gebe kalması [kalıp] — dişi devenin gebe kalması
  أنشأت الناقة فهي مبشئ إذا لقحت (tahdhib)

## ف ء د (root_001122): 67:23 وَٱلْأَفْـِٔدَةَ

- **B001** yüksek ateş ısısı; ateşte pişirme, ateş yakma ve bunların ürün, araç ve yerleri — eti ateşte kızartmak veya pişirmek · ateşte kızartılmış ya da pişirilmiş · kızartma veya közde pişirme aracı; şiş ya da fırını karıştırma çubuğu · kızartma ya da ateş yakma yeri · ekmeği sıcak kül ve köz içinde pişirmek · ekmek için kül ve ateş içinde pişirme yuvası açmak · ekmeğin yerleştirildiği sıcak kül ve ateş yuvası · fırını karıştırma veya kızartma araçları · kızartma şişi · onu ateşte kızarttı · kızartma şişi veya ateşte pişirme aracı · ateş · topluluk ateş yaktı
  أصل صحيح يدل على حمى وشدة حرارة (maqayis)؛ فأدت اللحم شويته ولحم فئيد أي مشوي (maqayis;sihah;mufradat)؛ فأدت الخبزة مللتها أو خبزتها في الملة (maqayis;sihah;tahdhib)؛ افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها (tahdhib)؛ المفأد السفود أو ما يخبز ويشوى به والمفتأد موضع الوقود (maqayis;sihah;tahdhib)
- **B002** iç ısısı gözetilen yürek — yürek; iç ısısı veya yanışı gözetilerek adlandırılan organ · yürekler
  الفؤاد القلب والجمع الأفئدة (sihah)؛ الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد (mufradat)؛ الفؤاد سمي بذلك لحرارته أو لتفؤده (maqayis;tahdhib)
- **B003** yüreği vurup yaralama veya yürekte hastalık oluşması — yüreğe vurup yaralama eylemi · yüreğine vurmak veya yüreğinde hastalık oluşturmak · yüreğinden vurulmuş veya yüreği hastalanmış kimse · adamın yüreği hastalandı
  الفأد مصدر فأدته إذا أصبت فؤاده (maqayis)؛ فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده (sihah)؛ فأدت الصيد إذا أصبت فؤاده وفئد الرجل أصابه داء في فؤاده (tahdhib)
- **B004** yüreksiz ve korkak kişi — yüreği zayıf, yüreksiz ve korkak kimse · yüreksiz veya yüreği zayıf kimse
  رجل مفؤود وفئيد لا فؤاد له (sihah)؛ المفؤود الضعيف الفؤاد الجبان مثل المنخوب (tahdhib)

## ش ك ر (root_000810): 67:23 تَشْكُرُونَ

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

## ذ ر ء (root_000510): 67:24 ذَرَأَكُمْ

- **B001** varlıkları yaratıp bireylerini ortaya çıkarma ve çoğaltma — yaratmak ve bireylerini varlığa çıkarmak · ateş için yaratılmış olanlar · varlıkları yaratan · onun aracılığıyla sizi çoğaltmak ve çiftler halinde sürdürmek
  ذرأ الله الخلق يذرؤهم (maqayis;sihah;tahdhib); خلقهم (sihah;tahdhib); يذرؤكم به أي يكثركم (tahdhib); الذرء إظهار الله تعالى ما أبداه وأوجد أشخاصهم (mufradat)
- **B002** çocuklar ve onların soyundan gelenler — 
  منه الذرية وهي نسل الثقلين (sihah); الذرء عدد الذرية وأنمى الله ذرءك أي ذريتك (tahdhib); الذرية أصلها الصغار من الأولاد (mufradat)
- **B003** toprağa tohum ekme ve ilk ekin — toprağa tohum ekmek · ekimden sonraki ilk ekin
  ذرأنا الأرض أي بذرناها (maqayis); ذرأت الأرض أي بذرتها وزرع ذرئ (sihah); الزرع أول ما تزرعه تسميه الذريء وقد ذرأنا أرضا (tahdhib)
- **B004** kırlaşmadan veya başka bir kaynaktan doğan beyazlık — kırlaşmadan ya da benzeri bir durumdan doğan beyazlık · başın ön kısmındaki kır saç · kır saçlı ya da başında veya kulağında beyaz işaret bulunan · kır saçlı kadın ya da başında beyaz işaret bulunan dişi hayvan · çok beyaz tuz · saçı ağarıp kırlaşmak
  الذرأة البياض من شيب وغيره (maqayis); الذُّرْأ الشيب في مقدم الرأس وملح ذرآني (sihah); ذُرِئ رأس فلان إذا ابيض وجدي أذرأ وملح ذرآني (tahdhib); الذرأة بياض الشيب والملح (mufradat)
- **B005** birini öfkelendirme, bir şeye dadandırma ya da birine karşı kışkırtma [kalıp] — birini bir şeye öfkelendirmek ya da ona dadandırmak · birini arkadaşına karşı kışkırtıp onun üzerine salmak
  أذرأت فلانا بكذا أولعته به (maqayis); أذرأني فلان أي أغضبني وأذرأت الرجل بصاحبه إذا حرشته عليه وأولعته به (tahdhib)
- **B006** iki kişi arasındaki ayırıcı engel — iki kişi arasındaki engel
  ما بيني وبينه ذرء أي حائل (maqayis)
- **B007** sözün küçük ve tamamlanmamış bir parçası [kalıp] — sözün küçük ve tamamlanmamış bir parçası
  بلغني عن فلان ذرء من قول إذا بلغك طرف منه ولم يتكامل؛ الشيء اليسير من القول (tahdhib)

## ح ش ر (root_000324): 67:24 تُحْشَرُونَ

- **B001** topluluğu sevk ederek toplama — topluluğu sevk ederek toplama · toplayıp bir hedefe sevk etmek · toplanma yeri · insanları toplayıp önden götüren · bütün yaratılmışların toplanıp yeniden diriltildiği gün · kadınlar savaşa çıkarılmaz
  السوق والبعث والانبعاث، والحشر الجمع مع سوق، والمحشر، والحاشر يحشر الناس على قدميه (maqayis)؛ الحشر حشر يوم القيامة، والمحشر المجمع الذي يحشر إليه القوم (ayn;tahdhib)؛ حشرتهم إذا جمعتهم، والمحشر مجتمعهم (jamhara)؛ جمعتهم ومنه يوم الحشر، والمحشر موضع الحشر، والحاشر اسم من أسماء النبي (sihah)؛ إخراج الجماعة عن مقرهم وإزعاجهم عنه إلى الحرب ونحوها، ولا يقال الحشر إلا في الجماعة (mufradat)
- **B002** çetin yılın insanları kentlere sürüp malı tüketmesi [kalıp] — çetin yıl onları kentlere sürdü · çetin yıl malı tüketti
  حشرت مال بني فلان السنة كأنها جمعته ذهبت به وأتت عليه (maqayis)؛ حشرتهم السنة تضمهم من النواحي إلى الأمصار (ayn;tahdhib)؛ حشرتهم السنة إذا أصابهم الضر حتى يهبطوا الأمصار (jamhara)؛ حشرت السنة مال فلان أي أهلكته (sihah)؛ حشرت السنة مال بني فلان أي أزالته عنهم (mufradat)
- **B003** hayvanların ölmesi — yaban hayvanlarının ölmesi
  قيل هو الموت (ayn)؛ حشرها موتها (sihah;tahdhib)
- **B004** küçük kara hayvanları — küçük kara hayvanı · küçük kara hayvanları · karada yaşayan küçük hayvanlar
  حشرات الأرض دوابها الصغار كاليرابيع والضباب وما أشبهها (maqayis)؛ الحشرة ما كان من صغار دواب الأرض مثل اليرابيع والقنافذ والضباب ونحوها (ayn;tahdhib)؛ حشرات الأرض دوابها الصغار واحدتها حشرة (jamhara)؛ الحشرة واحدة الحشرات وهي صغار دواب الأرض (sihah)
- **B005** sıkı yapılılık ya da iri karınlılık — sıkı yapılı veya iri karınlı · sıkı yapılı veya yanları kabarık · cinsel organı ve karnı iri olmak
  الحشور من الرجال العظيم الخلق أو البطن (maqayis)؛ الحشور كل ملزز الخلق شديدة (ayn)؛ دابة حشورة إذا كان ملزز الخلق شديده، والعظيم البطن من الرجال حشور (jamhara)؛ الحشور المنتفخ الجنبين، فرس حشور والأنثى حشورة (sihah)؛ حشر فلان في ذكره وفي بطنه إذا كانا ضخمين، والحشور من الدواب كل ملزز الخلق شديده ومن الرجال العظيم البطن (tahdhib)
- **B006** ince, sivri ya da hafif olma — ince, küçük ve sivri kulak · ince ve sivri kulak · ince ok tüyleri · ince sivriltilmiş mızrak ucu · hafif ok · mızrak ucunu inceltip sivriltmek · hafif ve çevik adam · kulakları yayvan ve sivri adam
  أذن حشرة مجتمعة الخلق، والحشر من القذذ ما لطف، وسنان حشر أي دقيق، وقد حشرته، والرجل الخفيف حشر (maqayis)؛ الحشر من الآذان ومن قذذ السهام ما لطف، وحشرت السنان أي رققته وألطفته (ayn;tahdhib)؛ سهم حشر خفيف، وأذن حشرة مؤللة أي دقيقة (jamhara)؛ أذن حشر أي لطيفة، والحشر من القذذ ما لطف، وسنان حشر دقيق، وقد حشرته، سهم حشر (sihah)؛ رجل حشر الأذنين أي في أذنيه انتشار وحدة (mufradat)
- **B007** taneye bitişik iç kabuk — taneye bitişik iç kabuk · taneye bitişik iç kabuklar
  الحبة عليها قشرتان، فالتي تلي الحبة الحشرة والجميع الحشر، والتي فوق الحشرة القصرة (tahdhib)
- **B008** hasat sonrası tarlada kalan bitki örtüsü — hasat sonrası tarlada kalan ve otlatılan bitki örtüsü
  المحشرة في لغة أهل اليمن ما بقي في الأرض وما فيها من نبات بعدما يحصد الزرع، فربما ظهر من تحته نبات أخضر، أرسلوا دوابهم في المحشرة (tahdhib)

## و ع د (root_001662): 67:25 ٱلْوَعْدُ

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

## ECHO ع و م (root_001063): for 67:25 ٱلْوَعْدُ: withheld observed target; not identity

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

## ص د ق (root_000852): 67:25 صَٰدِقِينَ

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

## ع ن د (root_001052): 67:26 عِندَ

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

## ب ي ن (root_000170): 67:26 مُّبِينٌ, 67:29 مُّبِينٍ

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

## ز ل ف (root_000639): 67:27 زُلْفَةً

- **B001** yaklaşıp ilerleme; yaklaştırarak toplama — yaklaşıp ilerlemek · öne doğru ilerlemek · yaklaştırmak; birbirine yaklaştırarak toplamak · öne doğru ilerleme · insanların yaklaşıp toplandığı yer
  يدل على اندفاع وتقدم في قرب إلى شيء؛ ازدلف الرجل: تقدم (maqayis)؛ أزلفته قربته؛ وازدلف اقترب (ayn)؛ وأزلفه أي قربه؛ والزلف التقدم؛ تزلفوا وازدلفوا أي تقدموا (sihah)؛ أزلفنا أي قربنا؛ جمعهم تقريب بعضهم من بعض؛ يزدلفن أي يقتربن؛ وأزلفت الجنة أي قربت (tahdhib)
- **B002** yakın tutulma ve saygın konum — yakınlık, gözde tutulma ve saygın konum · yakın tutulma, değer görme ve saygın yer · dereceler ve konumlar
  لفلان عند فلان زلفى أي قربى؛ والزلف والزلفة: الدرجة والمنزلة (maqayis)؛ الزلفى وهي القربة (ayn)؛ الزلفة والزلفى: القربة والمنزلة (sihah)؛ أصل الزلفى في كلام العرب: القربى؛ الزلف والزلفة: الدرجة والمنزلة (tahdhib)؛ الزلفة: المنزلة والحظوة؛ والزلفى: الحظوة (mufradat)
- **B003** gecenin birbirini izleyen ilk dilimleri [kalıp] — gecenin birbirine yakın bölümleri · gecenin başından bir bölüm · gecenin başına yakın vakitler · aşama aşama, azar azar
  الزلف من الليل طوائف منه لأن كل طائفة منها تقرب من الأخرى (maqayis)؛ زلفة من الليل طائفة من أوله (ayn)؛ الزلفة: الطائفة من أول الليل؛ زلفا فزلفا منزلة بعد منزلة ودرجة بعد درجة (sihah)؛ زلفا من الليل الصلاة القريبة من أول الليل؛ الزلف: أول ساعات الليل؛ زلفا فزلفا أي قليلا قليلا (tahdhib)؛ منازل الليل: زلف؛ طي الليالي زلفا فزلفا (mufradat)
- **B004** geniş kap veya su haznesi — dolu su haznesi veya geniş yemek tabağı · su hazneleri ve geniş leğenler
  الزلف: الأجاجين الخضر؛ الماء لا يثبت فيها عند امتلائها بل يندفع (maqayis)؛ الزلف المصانع واحدتها زلفة؛ والزلفة الصحفة وجمعها زلف (ayn)؛ الزلفة بالتحريك: المصنعة الممتلئة؛ وهي المصانع (sihah)؛ الزلف: المصانع واحدتها زلفة؛ الزلفة: الصحفة وجمعها زلف؛ الأجاجين الخضر؛ البركة تطفح مثل الزلف (tahdhib)
- **B005** kır ile tarım yerleşimleri arasındaki köyler — kır ile yerleşik tarım bölgesi arasındaki köy veya kasaba · kır ile yerleşik tarım bölgesi arasındaki köyler ve kasabalar
  المزالف هي بلاد بين البر والريف؛ سميت بذلك لقربها من الريف (maqayis)؛ المزلفة قرية تكون بين البر وبلاد الريف والجميع مزالف (ayn)؛ المزالف: البراغيل وهي البلاد التي بين الريف والبر الواحدة مزلفة (sihah)؛ المزالف واحدها مزلفة وهي القرى التي بين البر والريف مثل القادسية والأنبار (tahdhib)
- **B006** anlattıklarına ekleme yapmak [kalıp] — anlattıklarına ekleme yapmak
  يقال: فلان يزلف في حديثه ويزرف أي يزيد (tahdhib)
- **B007** kadının yüzü — kadının yüzü
  الزلف وجه المرأة (tahdhib)

## س و ء (root_000755): 67:27 سِيٓـَٔتْ

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

## د ع و (root_000478): 67:27 تَدَّعُونَ

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

## ECHO د ع ع (root_000477): for 67:27 تَدَّعُونَ: withheld observed target; not identity

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

## ه ل ك (root_001596): 67:28 أَهْلَكَنِىَ

- **B001** yok olma veya yok etme — yok olmak, bozulmak veya ölmek · yok oluş, kayıp, bozulma veya ölüm · sahibinin elinden çıkıp başka birinde kalmak · yiyecek bozulmak · yok etmek veya mahvetmek · yok etmek · yok olmuş şey veya yok oluş · yatağın üzerine düşmek
  يدل على كسر وسقوط (maqayis)؛ الهلك الهلاك (ayn;tahdhib)؛ هلك الشيء يهلك هلاكا وهلوكا (sihah)؛ الهلاك على أوجه افتقاد الشيء واستحالة وفساد والموت وبطلان الشيء وعدمه (mufradat)؛ يقال للعذاب والخوف والفقر الهلاك (mufradat)
- **B002** kendini ölümcül tehlikeye atma ve buna götüren tehlike — sonu yok oluşa varan tehlike · kendini ölümcül tehlikeye atma · korkudan kendini tehlikeli yere atmak
  الاهتلاك رمي الإنسان نفسه في تهلكة (ayn;tahdhib)؛ التهلكة كل شيء يصير عاقبته إلى الهلاك (ayn;tahdhib)؛ اهتلكت القطاة خوف البازي رمت بنفسها على المهالك (maqayis;sihah)؛ التهلكة ما يؤدي إلى الهلاك (mufradat)
- **B003** salınarak ve kırıtılarak yürüme — yürürken salınmak ve kırıtmak · kırıtarak yürüyen; eski kullanımda ahlaksız diye nitelenen kadın
  امرأة هلوك إذا تهالكت في غنجها متكسرة (maqayis)؛ الهلوك المرأة الفاجرة (ayn;tahdhib)؛ الهلوك من النساء الفاجرة المتساقطة على الرجال (sihah)؛ تهالكت المرأة في مشيتها (tahdhib)؛ كني بالهلوك عن الفاجرة لتمايلها (mufradat)
- **B004** geçinmek için sürekli yardım arayan yoksullar — kendisine bakacak birini sürekli arayan yoksul · iyilik ve yardım arayan yoksullar
  المهتلك الذي يهتلك أبدا إلى من يكفله وناس مهتلكون وهلاك (maqayis)؛ الهلاك الصعاليك الذين ينتابون الناس طلبا لمعروفهم من سوء الحال (ayn;tahdhib)؛ الأرامل والهلاك يعني به الفقراء (sihah)
- **B005** kurak arazi, çetin kıtlık yılı veya yağmursuz dağılan bulut — uzun süredir yağış almamış çorak arazi · üzerinde hiçbir şey yetişmeyen kurak arazi · çetin kıtlık yılı
  الأرض الهلكين الجدبة (maqayis)؛ أرض هلكون إذا لم يكن فيها شيء (tahdhib)؛ تركتها آرمة هلكين إذا لم يصبها الغيث منذ دهر طويل (tahdhib)؛ الهلك السنة الشديدة (tahdhib)؛ هالكة من السحاب المصوب ثم يقلع فلا يكون له مطر (tahdhib)
- **B006** ölümcül ıssız arazi veya dağlar arasındaki uçurum — geçeni ölüme götüren ıssız arazi · geçenleri öldüren tehlikeli ıssız arazi · dağlar arasındaki uçurum veya uçurum kenarı
  الهلك المهوى بين الجبلين (maqayis;tahdhib)؛ الهلكة مشرفة المهواة (ayn;tahdhib)؛ المهلكة والمهلكة المفازة (sihah)؛ مفازة هالكة من سلكها أي هالكة السالكين (ayn;tahdhib)
- **B007** belirli bir toplulukla anılan demirci — belirli bir toplulukla anılan demirci; genelleşmiş olarak demirci
  الهالكي الحداد (ayn)؛ الهالكي فالحداد نسب إلى الهالك بن عمرو (maqayis)؛ الهالكي الحداد نسب إلى الهالك ابن عمرو بن أسد (sihah)؛ أراد بالهالكي الحداد (tahdhib)؛ الهالكي كان حدادا من قبيلة هالك فسمي كل حداد هالكيا (mufradat)
- **B008** her durumda — her durumda; nasıl anlaşılırsa anlaşılsın
  افعل ذاك إما هلكت هلك أي على كل حال (sihah)؛ إما هلكت هلك أي على ما خيلت أي على كل حال (tahdhib)؛ إن شبه عليكم بكل معنى وعلى كل حال (tahdhib)
- **B009** kendini bir uğurda tüketmek veya yolda tükenmek [kalıp] — bir iş uğruna kendini tüketmek · geçen yolcuyu tüketen yol
  استهلك الرجل في كذا وكذا إذا جهد نفسه واهتلك مثله (tahdhib)؛ أي يجهد قلبه في إثرها (tahdhib)؛ طريق مستهلك الورد أي يجهد من سلكه (tahdhib)
- **B010** çölde yönünü şaşırıp dolanmak [kalıp] — ıssız arazide yönünü şaşırıp dönmek
  كنت أتهلك في مفاوز أي كنت أدور فيها شبه المتحير (tahdhib)؛ بين السماء وبين الأرض تهتلك (tahdhib)
- **B011** boş ve asılsız bir işe saplanmak — boş ve asılsız bir işe saplanma
  وقع في وادي تهلك بضم التاء والهاء واللام مشددة وهو غير مصروف مثل تخيب ومعناهما الباطل (sihah)
- **B012** doymaz bir istekle saldırırcasına yönelme — doymaz bir istekle yönelmek · doymak bilmeyen, aşırı istekli kadın ve erkekler · doymak bilmeyen istek taşıyan benlik
  الهلكى الشرهون من الرجال والنساء (tahdhib)؛ الهالكة النفس الشرهة (tahdhib)؛ هلك يهلك هلاكا إذا شره (tahdhib)؛ يقال للمزاحم على الموائد المتهالك (tahdhib)
- **B013** ailesi içinde yok olan ya da ailesini yok eden kimse [kalıp] — ailesi içinde yok olan veya ailesini yok eden kimse
  هالك أهل الذي يهلك في أهله وكذلك الذي يهلك أهله (ayn)؛ هو الذي يهلك في أهله ويكون هالك أهل الذي يهلك أهله (tahdhib)

## ج و ر (root_000275): 67:28 يُجِيرُ

- **B001** doğru yoldan, amaçtan, haktan ve adaletten sapma — amaçtan, adaletten veya haktan sapma · yoldan sapmak · hüküm verirken ona haksızlık etmek · sapmış; haktan ayrılmış · doğru doğrultudan sapan yol · zulmeden topluluk
  أصل واحد وهو الميل عن الطريق وجار جورا (maqayis)؛ الجور نقيض العدل والجور ترك القصد في السير (ayn)؛ الجور ضد القصد وجار عن الطريق إذا مال عنه وجور الحاكم إذا مال عن الحق (jamhara)؛ الجور الميل عن القصد وجار عن الطريق وجار عليه في الحكم وجوره تجويرا نسبه إلى الجور (sihah)؛ جار عن الطريق ثم جعل ذلك أصلا في العدول عن كل حق ومنها جائر أي عادل عن المحجة (mufradat)
- **B002** komşuluk ve mekânsal yakınlık — komşu · komşuluk ve yan yana bulunma · komşular · birbirine komşu olmak · bir erkeğin eşi
  الجار مجاورك في المسكن والجوار مصدر من المجاورة والجوار الاسم والجميع الأجوار والجيران جماعة (ayn)؛ الجار الذي يجاورك وجاورته مجاورة وجوارا وتجاور القوم واجتوروا وامرأة الرجل جارته (sihah)؛ الجار من يقرب مسكنه منك ومن يقرب من غيره جاره وجاوره وتجاور وفي الأرض قطع متجاورات (mufradat)
- **B003** koruma isteme ve güvence altına alma — güvence altına alınmış kişi · koruma istemek ve korumaya almak · Tanrı onu cezadan kurtardı
  الذي استجارك في الذمة تجيره وتمنعه (ayn)؛ الجار الذي أجرته من أن يظلمه ظالم واستجاره من فلان فأجاره منه وأجاره الله من العذاب أنقذه (sihah)؛ استجرته فأجارني وإني جار لكم وهو يجير ولا يجار عليه (mufradat)
- **B004** ibadet amacıyla camide kalma — ibadet amacıyla camide kalma
  المجاورة الاعتكاف في المسجد
- **B005** bağ veya bahçe işçisi — bağda veya bahçede çalışan tarım işçisi
  الجوار الأكار الذي يعمل لك في كرم أو بستان
- **B006** vurarak yere sermek [kalıp] — onu saplayarak veya vurarak yere sermek
  طعنه فجوره أي صرعه (maqayis)؛ ضربه فجوره أي صرعه مثل كوره فتجور (sihah)
- **B007** bir yer adı — bir yer adı
  جور اسم بلد يذكر ويؤنث
- **B008** bol veya gürültülü sağanak [kalıp] — bol yağmurlu veya gök gürültüsü güçlü yağış
  الغيث الجور وهو الغزير فشاذ عن الأصل ويمكن أن يكون من الجيم والهمزة والراء ومن الجؤار وهو الصوت (maqayis)؛ غيث جور أي شديد صوت الرعد (sihah)
- **B009** güçlü ve sert [kalıp] — güçlü, sert ve sağlam adam · güç ve sağlamlık alanına bağlanan, anlamı doğrulanması gereken niteleme
  رجل جور شديد صلب (jamhara)؛ بازل جور (sihah)
- **B010** öfke veya üzüntünün iç yakıcılığı — öfke veya üzüntünün göğüste duyulan yakıcı sıcaklığı
  الجائر ما يجده الإنسان في صدره من حرارة غيظ أو حزن فهو من باب الواو وقد مضى ذكره

## ECHO ج ي ر (root_000285): for 67:28 يُجِيرُ: withheld observed target; not identity

- **B001** ant gücünde doğrulama sözü — gerçekten; ant gücünde pekiştirme sözü
  جير بمعنى حقا (maqayis)؛ جير يمين للعرب (ayn)؛ جير لأفعلن كلمة يؤكدون بها كتأكيدهم بالقسم (jamhara)؛ جير لا آتيك يمين للعرب ومعناها حقا (sihah)
- **B002** belirli bir yapı harcı — belirli bir yapı harcı
  الجيار وهو الصاروج فكلمة معربة (maqayis)؛ الجيار الصاروج (ayn;sihah)
- **B003** yalıtık adlandırmalar — sade yağ yerken boğazı tutan gıcık · öfke ya da açlıktan göğüste duyulan yakıcı sıcaklık · öfke ya da üzüntüden göğüste duyulan yakıcı sıcaklık
  الجيار حلق الحلق يأخذ عند أكل السمن (ayn)؛ الجيار حرارة في الصدر من غيظ أو جوع وكذلك الجائر (sihah)؛ الجائر ما يجده الإنسان في صدره من حرارة غيظ أو حزن وهو من باب الواو (maqayis)

## ء ل م (root_000046): 67:28 أَلِيمٍ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## و ك ل (root_001681): 67:29 تَوَكَّلْنَا

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

## م و ه (root_001458): 67:30 مَآؤُكُمْ, 67:30 بِمَآءٍ

- **B001** su ve su adının biçim ailesi — bilinen ve içilen su · su adının küçültme biçimi · su adının çoğul biçimleri · suya ilişkin, suyla ilgili · su adının tekil veya dişil biçimi · suyun rengi
  الموه أصل بناء الماء (maqayis)؛ الموهة لون الماء وتصغير الماء مويه والجميع المياه (ayn)؛ الماء معروف وأصله الهاء مكان الهمزة (jamhara)؛ الماء الذي يشرب وأصله موه ويجمع على أمواه ومياه وتصغيره مويه (sihah)؛ أصل الماء ماه وجمع الماء مياه وأمواه (tahdhib)؛ أصل ماء موه بدلالة أمواه ومياه ومويه (mufradat)
- **B002** suyun belirmesi, çoğalması, içeri girmesi veya bir şeyi doldurması [kalıp] — kuyunun suyu belirdi veya çoğaldı · gemiye su girdi · toprakta sızıntı suyu belirdi · gök bol su akıttı · hurma veya üzüm meyvesi suyla dolup olgunlaşmaya hazırlandı · suyu bol kuyu
  ماهت السفينة تموه وتماه دخل فيها الماء وأماهت الأرض ظهر فيها نز (maqayis;ayn)؛ ماهت الركي إذا كثر ماؤها (jamhara)؛ ماهت الركية إذا ظهر ماؤها وكثر وكذلك السفينة إذا دخل فيها الماء وأماهت الأرض ظهر فيها النز (sihah)؛ موهت السماء أسالت ماء كثيرا وماهت البئر وأماهت في كثرة مائها وتموه ثمر النخل والعنب إذا امتلأ ماء (tahdhib)؛ ماهت الركية تميه وتماه وبئر ميهة وماهة (mufradat)
- **B003** su verme, içine su koyma ve sulanmış hale getirme — nesneye su verdi veya içine su koydu · adama su verdi · adama veya bıçağa su verdi · hokkaya su döktü · bana su ver · sulanmış ağaç
  موهت الشيء كأنك سقيته الماء وأمهت السكين وأمهيته سقيته (maqayis)؛ مهت الرجل ومهته إذا سقيته الماء وأمهت الرجل والسكين وأمهت الدواة صببت فيها الماء (sihah)؛ موه فلان حوضه إذا جعل فيه الماء وأمهني أي اسقني وشجر موهي إذا كان مسقويا (tahdhib)
- **B004** üreme sıvısını dişinin döl yatağına bırakma — erkek, üreme sıvısını dişinin döl yatağına bıraktı
  أماه الفحل ألقى ماءه في رحم الأنثى (maqayis;sihah)
- **B005** başka metali altın veya gümüşle kaplama ve gerçeği görünüşle gizleme — nesneyi, alttaki başka metali örtecek biçimde gümüş veya altınla kapladı · kılıcı veya başka bir nesneyi altınla kaplama · gerçeği başka göstererek aldatma · yanlışı doğru gibi gösteren aldatıcı · yanlışı doğru görünümüne soktu
  موهت الشيء طليته بفضة أو ذهب (maqayis)؛ موهت الشيء طليته بفضة أو ذهب وتحت ذلك نحاس أو حديد ومنه التمويه وهو التلبيس (sihah)؛ الميه طلاء السيف وغيره بماء الذهب ومنه قيل للمخادع مموه وقد موه علي الباطل إذا لبسه (tahdhib)
- **B006** belirli kalıplarda yüz güzelliği, söz tatlılığı, üzüm olgunluğu veya hayvan varlığının semirmesi [kalıp] — üzüm olgunlaşıp güzel renk aldı · yüzündeki gençlik canlılığı ve güzellik · üzerinde canlı bir güzellik var · güzel ve tatlı söz · ailesinin süsü ve güzelliği · hayvan varlığı bahar otuyla semirdi
  ما أحسن موهة وجهه أي ترقرق ماء الشباب فيه (maqayis)؛ الموهة لون الماء يقال ما أحسن موهة وجهه (ayn)؛ عليه موهة من حسن وتموه المال للسمن وتموه العنب إذا جرى فيه الينع وحسن لونه وكلام عليه موهة أي حسن وحلاوة (tahdhib)
- **B007** kaya kristali veya ayna — kaya kristali · suyla ilişkilendirilen ayna
  الماوية حجر البلور وكذلك الماوية المرآة (maqayis)؛ الماوية المرآة كأنها منسوبة إلى الماء (sihah)
- **B008** gönlünde suyu çok denilen, bazı aktarımlarda anlayışı kıt adam [kalıp] — anlayışı kıt ve ağır adam · gönlünde suyun çok olduğu söylenen adam
  رجل ماه القلب أي كثير ماء القلب ويكون صاحب ذلك بليدا (maqayis)؛ رجل ماه أي كثير ماء القلب أي بليد (sihah)؛ رجل ماهي القلب كثر ماء قلبه (mufradat)

## غ و ر (root_001112): 67:30 غَوْرًا

- **B001** derine alçalma veya içe çekilme — bir şeyin dibi ve derinliği · derinliği uzak; içyüzü zor kavranan · yerin derinlerine çekilmiş su · su toprağın içine çekildi · gözü çukuruna çekildi · semirdi ve içine yağ doldu · yaranın derinliği · yara şişti
  خفوض في الشيء وانحطاط وتطامن (maqayis)؛ قعر الشيء غوره (maqayis;sihah)؛ الغور المنهبط من الأرض (mufradat)؛ ماء غور أي غائر (sihah;mufradat)؛ غارت عينه غورا وغؤورا (sihah;mufradat)؛ غور القرحة (maqayis)؛ استغار أي سمن ودخل فيه الشحم (sihah)
- **B002** alçak bölge ve oraya yönelme — alçak, çukur arazi · güneydeki belirli alçak bölge · alçak bölgeye gitti veya indi · bir kullanımda alçak bölgeye gitti · alçak bölgeye gitme
  الغور تهامة وما يلي اليمن (maqayis;sihah)؛ الغور المطمئن من الأرض (sihah)؛ يقال غار الرجل إذا أتى الغور وأغار (maqayis)؛ يقال غار الرجل وأغار (mufradat)؛ التغوير إتيان الغور (sihah)
- **B003** dağ mağarası veya alçak sığınak — dağ mağarası · mağara veya alçak sığınak · mağara
  الغار كالكهف في الجبل (sihah)؛ المغار مثل الغار وكذلك المغارة (sihah)؛ الغار في الجبل (mufradat)؛ المغار من المكان كالغور (mufradat)
- **B004** güneşin ufukta batıp kaybolması — güneş battı ve gözden kayboldu · güneşin batışı ve kayboluşu
  غارت الشمس غيارا غابت (maqayis)؛ غارت الشمس تغور غيارا أي غربت (sihah)؛ غارت الشمس غيارا (mufradat)
- **B005** öğle dinlenmesi için konaklama — öğle dinlenmesi için konakladı · öğle uykusu veya bu amaçla konaklama · öğle dinlenmesi için konaklayın · öğle dinlenmesi vakti
  غور الرجل إذا نزل للقائلة (maqayis)؛ التغوير القيلولة (sihah)؛ غوروا أي انزلوا للقائلة (sihah)؛ يقال للقائلة الغائرة (sihah)
- **B006** baskın yapma veya hızla ileri atılma — düşmana baskın yapma · baskın · baskın yapan atlılar · düşmana baskın yaptı · onlara baskın yaptı veya onlarla çarpıştı · tilkinin hızla koşması · hızla koştu ve ileri atıldı · baskına atılan atlar · çok baskın yapan savaşçı
  إقدام على أخذ مال قهرا أو حربا (maqayis)؛ أغار بنو فلان على بني فلان إغارة وغارة (maqayis)؛ إغارة الثعلب عدوه (maqayis)؛ الغارة الاسم من الإغارة على العدو (sihah)؛ أغار على العدو إغارة ومغارا (sihah)؛ أغار أي شد العدو وأسرع (sihah)؛ أغار على العدو إغارة وغارة (mufradat)؛ فالمغيرات صبحا عبارة عن الخيل (mufradat)
- **B007** karın ile cinsel organı birlikte anlatan örtmece — karın ile cinsel organı birlikte anlatan örtmeceli ikili
  الغاران البطن والفرج (sihah)؛ كني عن الفرج والبطن بالغارين (mufradat)
- **B008** iyilikle yarar sağlama veya yağmur yardımı dileme — ona iyilik ederek yarar sağladı · bize yağmurla yardım et diye yakarış
  غاره بخير يغوره ويغيره أي نفعه (sihah)؛ اللهم غرنا منك بغيث أي أغثنا به (sihah)
- **B009** ipi sıkıca bükme veya sıkı bükülmüş ip [kalıp] — sıkı bükülmüş ip · ipi büktüm
  حبل شديد الغارة أي شديد الفتل (sihah)؛ أغرت الحبل أي فتلته فهو مغار (sihah)

## ع ي ن (root_001069): 67:30 مَّعِينٍۭ

- **B001** gören göz — göz, görme organı
  العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)
- **B002** gözle görüp kesin biçimde tanıma — gözle görerek, yüz yüze · yüz yüze görerek · bilerek, görüp emin olarak · gördükten sonra ayrıca iz aramam
  رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)
- **B003** koruyup gözetme — korumam altında, özenle gözeterek · gözümün önünde, korumam altında · gözetimimiz ve korumamız altında
  أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)
- **B004** kötü bakışla zarar verme — gözüyle zarar verdi · gözü değen kimse · göz değmiş kimse · gözü sık değen kimse
  عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)
- **B005** haber toplayan gizli gözcü — gizli gözcü veya öncü · gizli gözcü · bizim için çevreyi yoklayıp haber getirdi
  العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)
- **B006** akan su kaynağı — akan su kaynağı · göz önünde akan su · su aktı veya kaynağı ortaya çıktı
  العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)
- **B007** su sızdıran ince delik — su kabındaki ince veya delik sızıntı yeri · incelip su tutamaz olmuş su kabı · dikiş delikleri kapansın diye kaba su döktü
  عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)
- **B008** güneş yuvarlağı — güneşin gövdesi veya yuvarlağı
  عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)
- **B009** göze benzer çukur, yer veya eğim — dizin önündeki çukur · kuyunun kaynak yeri veya çukuru · terazideki küçük eğim veya dengesizlik · yayda merminin yerleştiği bölüm
  عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)
- **B010** belirli yönden gelen bulut veya dinmeyen yağmur — kıblenin sağından gelen bulut · günlerce dinmeyen yağmur
  العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)
- **B011** hemen elde bulunan para — elde hazır bulunan para · altın para, eldeki para
  العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)
- **B012** ertelenmiş ödemeli alımla para edinme — önceden verilen para veya para sağlamak için yapılan satış · malı ödemesi ertelenmiş olarak satın aldı
  العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)
- **B013** şeyin bizzat kendisi ve belirlenmiş olanı — şeyin bizzat kendisi · tam kendisi, yerine başkası değil · bir şeyi topluluk içinden belirleyip ayırma
  عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)
- **B014** bir şeyin en iyi ve seçkin bölümü — bir şeyin en iyi ve seçkin bölümü
  عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)
- **B015** önde gelen kişiler veya anne baba bir kardeşler — topluluğun önde gelen seçkin kişileri · anne baba bir kardeşler veya aynı kadının çocukları
  أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)
- **B016** geniş ve güzel gözlü olma — geniş ve güzel gözlü · gözlerinin güzelliğiyle adlandırılan yaban sığırı · geniş ve güzel gözlü kadınlar · göz benzeri küçük kare desenli kumaş
  توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)
- **B017** kimse veya orada bulunan insanlar — orada hiç kimse yok · ev halkı veya orada bulunanlar · bir topluluk içinde
  ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)



===== _commentary/v16/work/s067/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s067/reader_a_pilot.md)

# s067 Semantic Channel Discovery

## Parent Channels

### 1. P1: Dominion as a Gripping, Measuring Hand
- Semantic invariant: Rule is materialized as the capacity to possess, hold, measure, and make the whole answer to one directing hand.
- Surface relation: direct; 67:1 `بِيَدِهِ ٱلْمُلْكُ`, `كُلِّ شَىْءٍ`, and `قَدِيرٌ`, extended by 67:2 `ٱلْعَزِيزُ` and 67:6,12 `رَبِّهِمْ/رَبَّهُم`.
- Surprising reach: The royal declaration opens into a load-bearing machine: authority is not only rank but grip, cohesion, handles, skilled manipulation, and control of the water on which settlement depends.

#### Subchannel A. Possession, Force, and Comprehensive Command
- Reading type: mixed
- Scene or process: A sovereign hand encloses the field of objects, possesses it, and has enough force to determine each thing's measure.
- Active motifs: property under disposal (`quranic:root_001444:B002/m01`); kingship and political sovereignty (`quranic:root_001444:B003/m01`); hand as force (`quranic:root_001693:B002/m01`); hand as possession (`quranic:root_001693:B004/m01`); hand as enforceable authority (`quranic:root_001693:B005/m01`); hand yielded in submission (`quranic:root_001693:B006/m01`); bounded measure (`quranic:root_001205:B001/m01`); effective capacity (`quranic:root_001205:B003/m01`); total enclosure of parts (`quranic:root_001315:B003/m01`); the knowable object (`quranic:root_000831:B001/m01`); lordship as ownership (`quranic:root_000532:B001/m01`); invincible strength (`quranic:root_001008:B001/m01`); overpowering a rival (`quranic:root_001008:B002/m01`).
- Ayah anchors: 67:1 `مُلْكُ` (م ل ك), `يَدِ` (ي د ي), `قَدِيرٌ` (ق د ر), `كُلِّ` (ك ل ل), `شَىْءٍ` (ش ي ء); 67:2 `عَزِيزُ` (ع ز ز); 67:6 `رَبِّ` (ر ب ب); 67:8 `كُلَّمَآ` (ك ل ل); 67:9 `شَىْءٍ` (ش ي ء); 67:12 `رَبَّ` (ر ب ب).
- Synthesis: The hand, kingdom, totality, thing, and capacity form one command scene. What is possessed is not inert inventory: the hand supplies force, the kingdom supplies legitimate disposal, measure gives each object a limit, and lordship makes the whole field answerable to a single owner. The yielded hand reverses the relation from sovereign grip to creaturely submission.

#### Subchannel B. Load-Bearing Rule and Skilled Direction
- Reading type: latent/lexical
- Scene or process: A structure or expedition remains viable because a mainstay, handle, skilled operator, and forward leader keep its parts coherent and its route supplied.
- Active motifs: material cohesion (`quranic:root_001444:B001/m01`); the affair's mainstay (`quranic:root_001444:B005/m01`); middle course of road or valley (`quranic:root_001444:B006/m01`); water that lets travelers master their situation (`quranic:root_001444:B007/m01`); leading animal at the head of a herd (`quranic:root_001444:B008/m01`); implement handle (`quranic:root_001693:B013/m01`); manual skill (`quranic:root_001693:B015/m01`); protecting hand (`quranic:root_001693:B016/m01`); deliberative planning (`quranic:root_001205:B005/m01`); prior measuring and cutting (`quranic:root_000434:B001/m01`); shaft next to a spearhead (`quranic:root_001046:B009/m01`); working limbs (`quranic:root_001046:B010/m01`); chief whose word takes effect (`quranic:root_001272:B004/m01`); captain of sailors (`quranic:root_000532:B017/m01`).
- Ayah anchors: 67:1 `مُلْكُ` (م ل ك), `يَدِ` (ي د ي), `قَدِيرٌ` (ق د ر); 67:2 `خَلَقَ` (خ ل ق), `عَمَلًا` (ع م ل); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق); 67:6 `رَبِّ` (ر ب ب); 67:9 `قَالُ/قُلْ` (ق و ل); 67:10 `قَالُ` (ق و ل); 67:12 `رَبَّ` (ر ب ب); 67:13 `قَوْلَ` (ق و ل); 67:14 `خَلَقَ` (خ ل ق).
- Synthesis: Sovereignty becomes the engineering of continuance. Cohesion holds the structure, a mainstay bears it, a handle and skilled hand transmit intention, a shaft carries force, a leader sets direction, and water preserves operational independence. The captain and effective chief make the same invariant social: command is the part that keeps a many-part system from coming apart.

### 2. P1: Creation as a Workshop and a Stress Test
- Semantic invariant: Making assigns form and fit, while testing exposes whether the made thing, deed, or body retains integrity under use.
- Surface relation: direct; 67:2 `خَلَقَ`, `لِيَبْلُوَكُمْ`, `أَحْسَنُ عَمَلًا`; 67:3 `خَلْقِ`, `تَفَٰوُتٍ`, `فُطُورٍ`; 67:14 `خَلَقَ`.
- Surprising reach: The life test is reframed as workshop inspection: patterning, cutting, smoothing, joining, wearing, fracture, repair, and relapse all pressure the claim of a well-made form.

#### Subchannel A. Pattern, Cut, Join, and Finish
- Reading type: mixed
- Scene or process: A maker measures material, brings a form into existence, fits parts together, cuts at the joint, and checks the finished surface.
- Active motifs: prior measuring and cutting (`quranic:root_000434:B001/m01`); origination (`quranic:root_000434:B002/m01`); finished bodily form (`quranic:root_000434:B003/m01`); smooth worked surface (`quranic:root_000434:B008/m01`); making a thing (`quranic:root_000248:B001/m01`); changing it into a specified state (`quranic:root_000248:B002/m01`); cloth used to lower a hot pot (`quranic:root_000248:B007/m01`); opening by a split (`quranic:root_001165:B001/m01`); initiating a created thing (`quranic:root_001165:B002/m01`); calculated arrangement (`quranic:root_001205:B005/m02`); fit to an assigned proportion (`quranic:root_001205:B006/m01`); correspondence between parts (`quranic:root_000927:B003/m01`); cutting exactly through a joint (`quranic:root_000927:B006/m01`); excellent execution (`quranic:root_000323:B002/m01`); putting an instrument or mind to work (`quranic:root_001046:B002/m01`); sawing wood into parts (`quranic:root_001503:B005/m01`).
- Ayah anchors: 67:1 `قَدِيرٌ` (ق د ر); 67:2 `خَلَقَ` (خ ل ق), `أَحْسَنُ` (ح س ن), `عَمَلًا` (ع م ل); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق), `فُطُورٍ` (ف ط ر), `طِبَاقًا` (ط ب ق); 67:5 `جَعَلْ` (ج ع ل); 67:14 `خَلَقَ` (خ ل ق); 67:15 `جَعَلَ` (ج ع ل), `نُّشُورُ` (ن ش ر).
- Synthesis: These motifs occupy one fabrication sequence rather than a generic creation field. Material is measured before action, opened or cut, joined by correspondence, transformed into a designated state, and finished to a smooth or well-proportioned form. The pot cloth and saw make the scene concrete: making requires both force and protection from the process that applies it.

#### Subchannel B. Wear Reveals Quality, and Repair Reveals Residual Weakness
- Reading type: mixed
- Scene or process: Use abrades a made object or body; examination reveals its condition; good performance, excuse, fracture repair, or relapse supplies the verdict.
- Active motifs: wearing out under travel or use (`quranic:root_000153:B001/m01`); testing that discloses quality (`quranic:root_000153:B002/m01`); distinguished performance in benefaction or struggle (`quranic:root_000153:B003/m01`); an excuse exposed to remove blame (`quranic:root_000153:B004/m01`); worn fabric (`quranic:root_000154:B001/m01`); trial that manifests condition (`quranic:root_000154:B002/m01`); demonstrably good performance (`quranic:root_000154:B003/m01`); displayed excuse (`quranic:root_000154:B004/m01`); oath offered as a test (`quranic:root_000154:B005/m01`); refusal to care about the result (`quranic:root_000154:B009/m01`); fabric worn smooth and bare (`quranic:root_000434:B009/m01`); abrasion into decay (`quranic:root_000683:B004/m01`); a fracture healed crooked (`quranic:root_000015:B002/m01`); a wound or illness relapsing after improvement (`quranic:root_001096:B004/m01`); intentional action as the test object (`quranic:root_001046:B001/m01`); desirable quality (`quranic:root_000323:B001/m01`); checking whether struck prey has truly died (`quranic:root_001454:B014/m01`).
- Ayah anchors: 67:2 `يَبْلُوَ` (ب ل و), `خَلَقَ` (خ ل ق), `غَفُورُ` (غ ف ر), `عَمَلًا` (ع م ل), `أَحْسَنُ` (ح س ن), `مَوْتَ` (م و ت); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق); 67:11 `سُحْقًا` (س ح ق); 67:12 `أَجْرٌ` (ء ج ر), `مَّغْفِرَةٌ` (غ ف ر); 67:14 `خَلَقَ` (خ ل ق); surface anchors unavailable for `ب ل ي` (missing root coverage).
- Synthesis: The test is a condition-revealing operation. Wear exposes hidden weakness; conduct displays quality; an excuse or oath is laid out for examination; and repair can leave a crooked set or conceal a future relapse. Indifference is not a neutral state here but refusal of inspection. The death-check closes the sequence by showing that even an apparently final condition must be verified.

### 3. P1: Life, Death, and Reanimation as Changes of Force
- Semantic invariant: Life is the presence, recovery, or propagation of effective force; death is its removal, arrest, or conversion into inert matter.
- Surface relation: direct; 67:2 `ٱلْمَوْتَ وَٱلْحَيَوٰةَ`; 67:15 `ٱلنُّشُورُ`, with 67:3 sky and 67:15 earth providing the environmental frame.
- Surprising reach: Mortality expands into weather, pasture, sleep, seizure, worn cloth, dead ground, and revived vegetation, making resurrection a family of observable state changes rather than an isolated endpoint.

#### Subchannel A. Force Withdrawn, Arrested, or Restored
- Reading type: mixed
- Scene or process: Vital force disappears, is deliberately weakened, falls into temporary arrest, or is restored after a deathlike state.
- Active motifs: loss of life and force (`quranic:root_001454:B001/m01`); deliberate weakening or killing (`quranic:root_001454:B002/m01`); mortality spreading through people or livestock (`quranic:root_001454:B004/m01`); a single manner of dying (`quranic:root_001454:B008/m01`); seizure, fainting, or madness followed by recovery (`quranic:root_001454:B009/m01`); spending oneself without regard for death (`quranic:root_001454:B010/m01`); wind, sleep, or cloth becoming still and dead (`quranic:root_001454:B012/m01`); submitting to truth (`quranic:root_001454:B013/m01`); ensouled life (`quranic:root_000383:B003/m01`); sparing a life (`quranic:root_000383:B006/m01`); life as rescue and benefit (`quranic:root_000383:B013/m01`); sudden death that preempts action (`quranic:root_001183:B005/m01`); destructive arrival (`quranic:root_000009:B011/m01`); final outcome (`quranic:root_000897:B001/m01`); reviving the dead (`quranic:root_001503:B002/m01`).
- Ayah anchors: 67:2 `مَوْتَ` (م و ت), `حَيَوٰةَ` (ح ي ي); 67:3 `تَفَٰوُتٍ` (ف و ت); 67:6 `مَصِيرُ` (ص ي ر); 67:8 `يَأْتِ` (ء ت ي); 67:15 `نُّشُورُ` (ن ش ر).
- Synthesis: Death is represented by several mechanically distinct failures: force can be removed, intentionally damped, suddenly interrupted, spent in reckless commitment, or suspended in sleep and seizure. Life answers through sparing, rescue, and reanimation. The lexical submission-to-truth motif supplies a striking role reversal: yielding can look like death to self-direction while becoming alignment with the life-giving order.

#### Subchannel B. Rain Turns Dead Ground into Yield
- Reading type: latent/lexical
- Scene or process: Water descends or returns, settles in land and plant, and converts inert ground into pasture, fruit, milk, and renewed growth.
- Active motifs: rain enlivening soil and vegetation (`quranic:root_000383:B002/m01`); dry herbage greening after rain (`quranic:root_001503:B004/m01`); fertile soft earth (`quranic:root_000025:B002/m01`); rain named as provision (`quranic:root_000560:B003/m01`); flood arriving from a rained-on district (`quranic:root_000009:B005/m01`); crop, fruit, and abundant water as yield (`quranic:root_000009:B007/m01`); tree and crop produce (`quranic:root_000043:B002/m01`); fixed increase and blessing (`quranic:root_000109:B004/m01`); milk gathered from a kneeling she-camel (`quranic:root_000109:B007/m01`); sweet tree exudate (`quranic:root_001096:B007/m01`); rain-bearing layered cloud (`quranic:root_000532:B008/m01`); persistent green plant (`quranic:root_000532:B012/m01`); abundant gathered water (`quranic:root_000532:B013/m01`); sky as cloud and rain (`quranic:root_000745:B004/m01`); returning rainwater (`quranic:root_000544:B006/m01`); truffle emerging from soil (`quranic:root_001165:B008/m01`); soft plant and froth (`quranic:root_000387:B005/m01`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:2 `حَيَوٰةَ` (ح ي ي), `غَفُورُ` (غ ف ر); 67:3 `سَمَٰوَٰتٍ` (س م و), `ٱرْجِعِ` (ر ج ع), `فُطُورٍ` (ف ط ر); 67:4 `ٱرْجِعِ` (ر ج ع); 67:5 `سَّمَآءَ` (س م و); 67:6 `رَبِّ` (ر ب ب); 67:8 `يَأْتِ` (ء ت ي); 67:12 `مَّغْفِرَةٌ` (غ ف ر), `رَبَّ` (ر ب ب); 67:14 `خَبِيرُ` (خ ب ر); 67:15 `نُّشُورُ` (ن ش ر), `أَرْضَ` (ء ر ض), `رِّزْقِ` (ر ز ق), `كُلُ` (ء ك ل).
- Synthesis: The scene is a complete ecological conversion: cloud carries water, rain returns, a foreign flood delivers it, soil receives it, dry growth greens, and plants yield food, exudate, and milk. Blessing is therefore not an abstract surplus but increase fixed in a living supply chain. The resurrection anchor at 67:15 is materially rehearsed by dead pasture taking water and standing green again.

### 4. P1: The Sky as a Fitted, Covered Fabric
- Semantic invariant: Ordered creation is a superposed enclosure whose integrity depends on fit, continuous covering, closed surfaces, and the absence of gaps.
- Surface relation: direct; 67:3 `سَبْعَ سَمَٰوَٰتٍ طِبَاقًا`, `تَفَٰوُتٍ`, `فُطُورٍ`; 67:5 `ٱلسَّمَآءَ ٱلدُّنْيَا`.
- Surprising reach: Cosmology takes the vocabulary of tailoring, sheathing, canopies, fruit husks, sealed stone, hollow shafts, and exact joint work.

#### Subchannel A. Superposed Layers Make One Enclosure
- Reading type: mixed
- Scene or process: Like fitted coverings, multiple layers are placed one over another until they form a continuous overhead whole.
- Active motifs: covering one thing with its counterpart (`quranic:root_000927:B001/m01`); layers stacked above layers (`quranic:root_000927:B002/m01`); parts brought into correspondence (`quranic:root_000927:B003/m02`); movement through successive states or layers (`quranic:root_000927:B004/m01`); a class composed by likeness (`quranic:root_000927:B005/m01`); a temporal layer (`quranic:root_000927:B010/m01`); sky as everything high enough to shade (`quranic:root_000745:B004/m02`); encircling crown or cloud (`quranic:root_001315:B005/m01`); protective canopy (`quranic:root_001315:B006/m01`); general covering and preservation (`quranic:root_001096:B001/m02`); nap or hair covering a surface (`quranic:root_001096:B003/m01`); material covering (`quranic:root_001307:B001/m01`); darkness or expanse as an engulfing cover (`quranic:root_001307:B002/m01`); fruit sheath (`quranic:root_001307:B010/m01`); clouds riding in layers (`quranic:root_000532:B008/m02`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر); 67:3 `طِبَاقًا` (ط ب ق), `سَمَٰوَٰتٍ` (س م و); 67:5 `سَّمَآءَ` (س م و); 67:6 `كَفَرُ` (ك ف ر), `رَبِّ` (ر ب ب); 67:8 `كُلَّمَآ` (ك ل ل); 67:12 `مَّغْفِرَةٌ` (غ ف ر), `رَبَّ` (ر ب ب).
- Synthesis: The heavens become an enclosure assembled by correspondence. Layer is not mere multiplicity: each covering must sit against another, the whole must shade, and its perimeter must remain continuous like a crown, canopy, nap, or fruit sheath. The sequence from layer to whole explains why discrepancy is sought as a failure of fit.

#### Subchannel B. Seams, Voids, and Forced Openings
- Reading type: mixed
- Scene or process: Inspection targets the places where a supposedly continuous surface could split, gape, detach, or conceal a hollow.
- Active motifs: opening and fissure (`quranic:root_001165:B001/m02`); disparity between two things (`quranic:root_001183:B002/m01`); a physical gap such as that between fingers (`quranic:root_001183:B004/m01`); closure that prevents extension (`quranic:root_000927:B008/m01`); an all-enclosing calamity (`quranic:root_000927:B009/m01`); smooth sealed stone or surface (`quranic:root_000434:B008/m02`); solid blockage (`quranic:root_000434:B012/m01`); stripping away a cover (`quranic:root_000320:B001/m01`); thick edge and seam joining two panels (`quranic:root_000121:B006/m01`); hollow interior of a shaft (`quranic:root_000697:B008/m01`); visible cleft in an upper lip (`quranic:root_001040:B004/m01`); opening of a crack as the diagnostic contrast (`quranic:root_000434:B003/m02`).
- Ayah anchors: 67:2 `خَلَقَ` (خ ل ق); 67:3 `فُطُورٍ` (ف ط ر), `تَفَٰوُتٍ` (ف و ت), `طِبَاقًا` (ط ب ق), `خَلَقَ/خَلْقِ` (خ ل ق), `بَصَرَ` (ب ص ر); 67:4 `حَسِيرٌ` (ح س ر), `بَصَرَ/بَصَرُ` (ب ص ر); 67:13 `أَسِرُّ` (س ر ر), `عَلِيمٌۢ` (ع ل م); 67:14 `خَلَقَ` (خ ل ق), `يَعْلَمُ` (ع ل م).
- Synthesis: These motifs define a diagnostic edge scene. A seam can join panels, a gap can disclose failed correspondence, a smooth face can hide a hollow, and a forced opening can expose what covering concealed. The command to look for rupture is thus pressured by craft knowledge: integrity is established at seams and voids, not by the uninterrupted face alone.

### 5. P1: Repeated Inspection Exhausts the Instrument, Not the Object
- Semantic invariant: Perception is sent out, recalled, and sent again; the observed order remains, while the returning organ loses force and status.
- Surface relation: direct; 67:3-4 `فَٱرْجِعِ ٱلْبَصَرَ`, `كَرَّتَيْنِ`, `يَنقَلِبْ`, `خَاسِئًا`, `حَسِيرٌ`.
- Surprising reach: Looking behaves like repeated travel, echo, grinding, re-inking, drawing a weapon, and checking diagnostic traces.

#### Subchannel A. Return, Repetition, and Reinspection
- Reading type: mixed
- Scene or process: An observing action goes out and comes back repeatedly, varying its route or operation while preserving the same object of inspection.
- Active motifs: return or restoration (`quranic:root_000544:B001/m01`); answer returning to a speaker (`quranic:root_000544:B005/m01`); echoing voice (`quranic:root_000544:B007/m01`); repeated steps of an animal (`quranic:root_000544:B008/m01`); retraced tattoo or writing (`quranic:root_000544:B009/m01`); hand returning to quiver or sword (`quranic:root_000544:B010/m01`); birds returning after migration (`quranic:root_000544:B012/m01`); body or mount restored after wasting (`quranic:root_000544:B014/m01`); reused or returned material (`quranic:root_000544:B015/m01`); a repeated return or charge (`quranic:root_001292:B001/m01`); sound reiterated in the throat (`quranic:root_001292:B006/m01`); wind regathering dispersed cloud (`quranic:root_001292:B009/m01`); mill repeatedly turning over grain (`quranic:root_001292:B010/m01`); sensory sight (`quranic:root_000531:B001/m01`); reflective judgment (`quranic:root_000531:B002/m01`); making another see (`quranic:root_000531:B012/m01`); turning a thing from face to face (`quranic:root_001248:B004/m01`).
- Ayah anchors: 67:3 `ٱرْجِعِ` (ر ج ع), `تَرَىٰ/تَرَىٰ` (ر ء ي); 67:4 `ٱرْجِعِ` (ر ج ع), `كَرَّتَيْنِ` (ك ر ر), `يَنقَلِبْ` (ق ل ب).
- Synthesis: Return is not one undifferentiated motion. It can be recall, echo, retracing, a hand reaching again for an implement, migratory return, restoration after wasting, or a mill's recurrent pass. Together they model inspection as an iterative operation: the observer changes passes and angles, but no altered object appears.

#### Subchannel B. A Humbled and Depleted Sensorium
- Reading type: mixed
- Scene or process: The eye is driven back, contracts, loses sharpness, and becomes the failed component in an otherwise intact inspection system.
- Active motifs: exhaustion and loss of visual force (`quranic:root_000320:B003/m01`); regret over what escaped (`quranic:root_000320:B004/m01`); one kept away from a ruler's doors (`quranic:root_000320:B006/m01`); humiliating expulsion (`quranic:root_000408:B001/m01`); sight contracting in fatigue and abasement (`quranic:root_000408:B002/m01`); dullness of blade, tongue, hearing, or sight (`quranic:root_001315:B001/m01`); blood trace used as evidence (`quranic:root_000121:B004/m01`); shield or armor as a "sight" (`quranic:root_000121:B005/m01`); pale or shining soft stone (`quranic:root_000121:B007/m01`); eye overcome by sunlight (`quranic:root_000269:B004/m01`); distant sight in a horse (`quranic:root_000831:B007/m01`); the duplicate far-sighted image (`quranic:root_000832:B003/m01`); eye opened under threat of its harmful gaze (`quranic:root_000824:B004/m01`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل), `شَىْءٍ` (ش ي ء); 67:3 `بَصَرَ` (ب ص ر); 67:4 `حَسِيرٌ` (ح س ر), `خَاسِئًا` (خ س ء), `بَصَرَ/بَصَرُ` (ب ص ر); 67:7 `شَهِيقًا` (ش ه ق); 67:8 `كُلَّمَآ` (ك ل ل); 67:9 `شَىْءٍ` (ش ي ء); 67:13 `ٱجْهَرُ` (ج ه ر).
- Synthesis: The scene distinguishes evidence from capacity. Blood trace, armor, bright stone, glare-blinded eye, and far-sighted horse supply different material conditions of seeing, but the repeated gaze ends in dullness, contraction, and exclusion. The object is not defeated by scrutiny; the scrutinizing instrument is driven from the court of what it hoped to indict.

### 6. P1: Celestial Ornament Converts into an Armory
- Semantic invariant: What marks beauty and visibility can be reassigned as a defensive instrument that strikes, expels, and guards a boundary.
- Surface relation: direct; 67:5 `زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًا لِّلشَّيَٰطِينِ`.
- Surprising reach: The same scene joins cosmetics, dawn, lunar stations, banners, stones, well tackle, hoof strikes, armor, battle readiness, and verbal missiles.

#### Subchannel A. Light, Appearance, and Elevated Display
- Reading type: mixed
- Scene or process: A high surface is made visible and attractive by luminous marks whose placement gives the whole a distinguished appearance.
- Active motifs: beauty without blemish (`quranic:root_000660:B001/m01`); active beautification (`quranic:root_000660:B002/m01`); ornament worn or displayed (`quranic:root_000660:B003/m01`); lamp or luminary (`quranic:root_000839:B005/m01`); bright complexion (`quranic:root_000839:B006/m01`); height and elevation (`quranic:root_000745:B001/m01`); high figure visible from afar (`quranic:root_000745:B002/m01`); overhead sky (`quranic:root_000745:B004/m03`); near or lower world (`quranic:root_000493:B002/m01`); attraction toward a thing (`quranic:root_000831:B005/m01`); cloud flashing like a smile (`quranic:root_001315:B011/m01`); lunar station of small stars (`quranic:root_001096:B006/m01`); Antares as the scorpion's heart (`quranic:root_001248:B010/m01`); hidden crescent at month's end (`quranic:root_000697:B004/m01`); dawn and first light (`quranic:root_000839:B001/m01`).
- Ayah anchors: 67:1 `شَىْءٍ` (ش ي ء), `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر); 67:3 `سَمَٰوَٰتٍ` (س م و); 67:4 `يَنقَلِبْ` (ق ل ب); 67:5 `زَيَّ` (ز ي ن), `مَصَٰبِيحَ` (ص ب ح), `سَّمَآءَ` (س م و), `دُّنْيَا` (د ن و); 67:8 `كُلَّمَآ` (ك ل ل); 67:9 `شَىْءٍ` (ش ي ء); 67:12 `مَّغْفِرَةٌ` (غ ف ر); 67:13 `أَسِرُّ` (س ر ر).
- Synthesis: Ornament here is spatially disciplined. Elevation makes the marks visible, nearness defines the lowest celestial field, and lamp, dawn, crescent, lunar station, and named star supply several temporal scales of light. The flashing-cloud image bridges ornament and weather without turning the scene into a generic catalogue of brightness.

#### Subchannel B. Stones, Expulsion, and Boundary Defense
- Reading type: mixed
- Scene or process: A prepared defense converts stones and forceful impacts into projectiles that drive a transgressor away from a guarded region.
- Active motifs: hurtful speech as stone throwing (`quranic:root_000547:B002/m01`); cursing as expulsion (`quranic:root_000547:B003/m01`); conjecture cast into the unseen (`quranic:root_000547:B004/m01`); heap of stones and grave marker (`quranic:root_000547:B005/m01`); stone and wooden tackle at a well (`quranic:root_000547:B006/m01`); active defense of one's people (`quranic:root_000547:B007/m01`); hoof striking the ground (`quranic:root_000547:B008/m01`); things piled one upon another (`quranic:root_000547:B010/m01`); remoteness and severance (`quranic:root_000796:B001/m01`); long strong tether (`quranic:root_000796:B002/m01`); deviating and opposing force (`quranic:root_000796:B003/m01`); rebellious adversary (`quranic:root_000796:B004/m01`); hideous serpent image (`quranic:root_000796:B005/m01`); equipment held ready (`quranic:root_000978:B001/m01`); prepared warhorse (`quranic:root_000978:B002/m01`); armor or shield (`quranic:root_000121:B005/m02`); severe battle strength (`quranic:root_000079:B001/m01`); persistence in combat (`quranic:root_000109:B006/m01`); descent to single combat (`quranic:root_001492:B007/m01`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:3 `بَصَرَ` (ب ص ر); 67:4 `بَصَرَ/بَصَرُ` (ب ص ر); 67:5 `رُجُومًا` (ر ج م), `شَّيَٰطِينِ` (ش ط ن), `أَعْتَدْ` (ع ت د); 67:6 `بِئْسَ` (ب ء س); 67:9 `نَزَّلَ` (ن ز ل).
- Synthesis: The armory is built from a precise action chain: equipment is ready, an adversary crosses or resists a boundary, a projectile is cast, impact drives the target away, and defenders preserve their people. Verbal abuse and conjecture are not stray additions; both are lexical stone-throws, one against a person and one against the unseen. The well tackle adds a useful mechanical bridge: a stone can be suspended and directed rather than merely lying inert.

### 7. P1: Hell Behaves as a Furnace-Organism
- Semantic invariant: Fire is both a combustion system that consumes fuel and a living-seeming body that boils, breathes, rages, and strains toward rupture.
- Surface relation: direct; 67:5-7 `عَذَابَ ٱلسَّعِيرِ`, `شَهِيقًا`, `تَفُورُ`; 67:8 `تَمَيَّزُ مِنَ ٱلْغَيْظِ`; 67:10-11 `أَصْحَٰبِ ٱلسَّعِيرِ`.
- Surprising reach: The infernal scene includes ovens, cooking pots, fuel feeding, fevered veins, balance tongues, high inhalation, and a neck extended for a blow.

#### Subchannel A. Fuel, Ignition, Boiling, and Heat Transfer
- Reading type: mixed
- Scene or process: Prepared fuel is fed into a confined heat source; ignition grows into boiling, swelling pressure, and consuming flame.
- Active motifs: ignited and blazing fire (`quranic:root_000708:B001/m01`); war or evil heated like flame (`quranic:root_000708:B002/m01`); burning hunger, madness, or torment (`quranic:root_000708:B004/m01`); mange beginning in hot body folds (`quranic:root_000708:B005/m01`); pit oven (`quranic:root_000708:B009/m01`); acute first onset (`quranic:root_000708:B010/m01`); tall or severe fire-kindler (`quranic:root_000708:B011/m01`); pot, oven, water, or smoke boiling up (`quranic:root_001185:B001/m01`); first eruptive surge (`quranic:root_001185:B002/m01`); sudden intensity of heat (`quranic:root_001185:B003/m01`); fevered vein swelling (`quranic:root_001185:B005/m01`); bodily vents (`quranic:root_001185:B007/m01`); flanks of a balance tongue (`quranic:root_001185:B008/m01`); fire consuming its feed (`quranic:root_000043:B005/m01`); painful punishment (`quranic:root_000994:B005/m01`); ready apparatus (`quranic:root_000978:B001/m02`); cooking pot and its contents (`quranic:root_001205:B007/m01`); heat-shielding pot cloth (`quranic:root_000248:B007/m02`).
- Ayah anchors: 67:1 `قَدِيرٌ` (ق د ر); 67:5 `سَّعِيرِ` (س ع ر), `عَذَابَ` (ع ذ ب), `أَعْتَدْ` (ع ت د), `جَعَلْ` (ج ع ل); 67:6 `عَذَابُ` (ع ذ ب); 67:7 `تَفُورُ` (ف و ر); 67:10 `سَّعِيرِ` (س ع ر); 67:11 `سَّعِيرِ` (س ع ر); 67:15 `كُلُ` (ء ك ل), `جَعَلَ` (ج ع ل).
- Synthesis: This is a furnace sequence with distinct roles: apparatus, fuel, ignition, enclosure, heat transfer, and pressure. The pit oven and pot localize the fire; feeding and consumption sustain it; the first surge and swollen vein give pressure a bodily analogue. The balance tongue sharpens the image of a system whose internal heat is also an enacted judgment.

#### Subchannel B. Breath, Rage, and Self-Rupture
- Reading type: mixed
- Scene or process: The heated body draws a high breath, voices its agitation, and strains so violently that its own structure begins to separate.
- Active motifs: towering height (`quranic:root_000824:B001/m01`); high indrawn breath, groan, or cry (`quranic:root_000824:B002/m01`); stallion's angry internal roar (`quranic:root_000824:B003/m01`); dangerous opened gaze (`quranic:root_000824:B004/m02`); anger compressed in the chest (`quranic:root_001121:B001/m01`); reciprocal provocation (`quranic:root_001121:B002/m01`); heat raging like anger (`quranic:root_001121:B003/m01`); anger made audible (`quranic:root_001121:B004/m01`); separating mixed things (`quranic:root_001461:B001/m01`); tearing apart from rage (`quranic:root_001461:B002/m01`); stretched neck exposed for striking (`quranic:root_001461:B004/m01`); restless racing in every direction (`quranic:root_000708:B007/m01`); chest as bodily container (`quranic:root_000849:B001/m01`); exhausted force (`quranic:root_000320:B003/m02`); general sensory dulling (`quranic:root_001315:B001/m02`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:4 `حَسِيرٌ` (ح س ر); 67:5 `سَّعِيرِ` (س ع ر); 67:7 `شَهِيقًا` (ش ه ق); 67:8 `غَيْظِ` (غ ي ظ), `تَمَيَّزُ` (م ي ز), `كُلَّمَآ` (ك ل ل); 67:10 `سَّعِيرِ` (س ع ر); 67:11 `سَّعِيرِ` (س ع ر); 67:13 `صُّدُورِ` (ص د ر).
- Synthesis: Breath and anger make the fire act like a torso under impossible internal pressure. The chest contains rage, the roar externalizes it, and separation turns emotion into structural failure. The extended neck and harmful gaze make the furnace predatory, while exhaustion hints that its violence is a ceaseless operation rather than a momentary flare.

### 8. P1: Cast Arrivals Become Accounted-for Batches
- Semantic invariant: Entry into the punishment scene is forced, grouped, stored under custody, and converted into an interrogable record.
- Surface relation: direct; 67:7-8 `أُلْقُوا۟ فِيهَا`, `أُلْقِىَ فِيهَا فَوْجٌ`, `خَزَنَتُهَا`, `سَأَلَهُمْ`, `أَلَمْ يَأْتِكُمْ نَذِيرٌ`.
- Surprising reach: The scene resembles a gate, storehouse, receiving station, and legal intake desk, with discarded objects, outsiders, dues, shortcuts, and obligations all entering the same custody logic.

#### Subchannel A. Forced Casting and Batch Intake
- Reading type: mixed
- Scene or process: Participants meet the threshold, are thrown across it in groups, and become deposited objects within a receiving enclosure.
- Active motifs: encounter between opposed parties (`quranic:root_001372:B004/m01`); throwing or depositing (`quranic:root_001372:B005/m01`); discarded object with no owner (`quranic:root_001372:B006/m01`); what one meets of evil (`quranic:root_001372:B007/m01`); body laid on its back (`quranic:root_001372:B009/m01`); endpoints forced to meet (`quranic:root_001372:B010/m01`); words received and learned (`quranic:root_001372:B011/m01`); incoming human group (`quranic:root_001184:B001/m01`); broad pass between elevations (`quranic:root_001184:B002/m01`); provision prepared for a new arrival (`quranic:root_001492:B005/m01`); calamity descending on a people (`quranic:root_001492:B006/m01`); encompassing totality (`quranic:root_001315:B003/m02`); companions attached to one destination (`quranic:root_000844:B001/m01`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:7 `أُلْقُ` (ل ق ي); 67:8 `أُلْقِىَ` (ل ق ي), `فَوْجٌ` (ف و ج), `كُلَّمَآ` (ك ل ل); 67:9 `نَزَّلَ` (ن ز ل); 67:10 `أَصْحَٰبِ` (ص ح ب); 67:11 `أَصْحَٰبِ` (ص ح ب).
- Synthesis: Casting is not merely downward motion. It makes persons resemble ownerless deposited objects, batches them as an arriving group, and passes them through a broad threshold into a prepared but hostile reception. Receiving words supplies the moral counter-operation: the same root that depicts bodies thrown away also depicts instruction taken in, the choice that could have prevented this intake.

#### Subchannel B. Keepers, Questions, and Outstanding Obligations
- Reading type: mixed
- Scene or process: Custodians preserve a closed store, question each arriving batch, and establish whether warning and obligation had already reached it.
- Active motifs: securing and hiding stored property (`quranic:root_000406:B001/m01`); keeper charged with custody (`quranic:root_000406:B003/m01`); stored meat turning foul (`quranic:root_000406:B004/m01`); shortest controlled route (`quranic:root_000406:B005/m01`); wealth after poverty (`quranic:root_000406:B006/m01`); request or interrogation (`quranic:root_000661:B001/m01`); requested object (`quranic:root_000661:B002/m01`); satisfying a claim (`quranic:root_000661:B003/m01`); mutual questioning (`quranic:root_000661:B004/m01`); arrival (`quranic:root_000009:B001/m02`); outsider entering another people (`quranic:root_000009:B006/m01`); tax or due rendered (`quranic:root_000009:B008/m01`); inhabited route and terminal approach (`quranic:root_000009:B010/m01`); warning that awakens caution (`quranic:root_001488:B001/m01`); self-imposed obligation (`quranic:root_001488:B002/m01`); assessed compensation for a wound (`quranic:root_001488:B003/m01`).
- Ayah anchors: 67:8 `خَزَنَتُ` (خ ز ن), `سَأَلَ` (س ء ل), `يَأْتِ` (ء ت ي), `نَذِيرٌ` (ن ذ ر); 67:9 `نَذِيرٌ` (ن ذ ر).
- Synthesis: Custody, inquiry, and liability form one institutional scene. The keepers control access and route, the question establishes prior notice, and the warning behaves like an obligation already delivered. Tax and wound-compensation sharpen the accountancy: an arrival can carry an outstanding due. Foul stored meat supplies the scene's grim material pressure, since confinement preserves neither innocence nor condition.

### 9. P1: Warning Moves from Delivery to a Tribunal of Reception
- Semantic invariant: A message arrives, is made audible and intelligible, is denied or fabricated against, and finally returns as confession and sentence.
- Surface relation: direct; 67:8-11 `نَذِيرٌ`, `جَآءَنَا`, `فَكَذَّبْنَا`, `مَا نَزَّلَ ٱللَّهُ`, `نَسْمَعُ أَوْ نَعْقِلُ`, `فَٱعْتَرَفُوا۟ بِذَنۢبِهِمْ`.
- Surprising reach: Communication is modeled as transport, compulsion, inscription, tethering, blood-liability, and the final expulsion of a condemned company.

#### Subchannel A. Arrival, Carriage, and Placement of the Message
- Reading type: mixed
- Scene or process: Warning comes from outside, carries content into the audience's space, and places that content where it can be received.
- Active motifs: coming and reaching (`quranic:root_000009:B001/m03`); bringing or giving (`quranic:root_000009:B002/m01`); finding the proper approach (`quranic:root_000009:B003/m01`); penetrating arrival (`quranic:root_000009:B013/m01`); coming with intent (`quranic:root_000281:B001/m01`); prevailing through repeated approach (`quranic:root_000281:B002/m01`); bringing an object into presence (`quranic:root_000281:B004/m01`); compelling it toward a destination (`quranic:root_000281:B005/m01`); duplicated arrival and prevalence (`quranic:root_000282:B001/m01`); danger-report that induces caution (`quranic:root_001488:B001/m02`); descent and settlement (`quranic:root_001492:B001/m01`); causing content to descend (`quranic:root_001492:B002/m01`); placing it in its proper station (`quranic:root_001492:B004/m01`); one discrete descent (`quranic:root_001492:B010/m01`); making another hear (`quranic:root_000741:B004/m01`); articulated utterance (`quranic:root_001272:B001/m01`).
- Ayah anchors: 67:7 `سَمِعُ` (س م ع); 67:8 `يَأْتِ` (ء ت ي), `نَذِيرٌ` (ن ذ ر); 67:9 `جَآءَ` (ج ي ء), `نَذِيرٌ` (ن ذ ر), `نَزَّلَ` (ن ز ل), `قَالُ/قُلْ` (ق و ل); 67:10 `نَسْمَعُ` (س م ع), `قَالُ` (ق و ل); 67:13 `قَوْلَ` (ق و ل).
- Synthesis: Warning is a transport operation with stages: approach, arrival, carriage, descent, placement, and audibility. Compulsion is a latent edge rather than an imported conclusion; it shows how delivery can bring content up to a hearer without forcing assent. The discrete descent motif keeps a single reception event distinct from the broader process of transmission.

#### Subchannel B. Denial Manufactures a Counter-Account
- Reading type: mixed
- Scene or process: Recipients reject the delivered account, attribute falsehood, and manufacture an alternative statement about revelation and error.
- Active motifs: false statement or act (`quranic:root_001290:B001/m01`); charging another with falsehood (`quranic:root_001290:B002/m01`); failed resolve in a charge (`quranic:root_001290:B004/m01`); acting without delay (`quranic:root_001290:B005/m01`); expected milk failing to persist (`quranic:root_001290:B006/m01`); fleeing animal stopping to look back (`quranic:root_001290:B007/m01`); self that gives a false account (`quranic:root_001290:B008/m01`); decorated cloth misrepresenting its condition (`quranic:root_001290:B009/m01`); attributing words never spoken (`quranic:root_001272:B005/m01`); rumor circulating among people (`quranic:root_001272:B007/m01`); speech operating as conjecture (`quranic:root_001272:B011/m01`); unvoiced internal proposition (`quranic:root_001272:B012/m01`); doctrine or adopted position (`quranic:root_001272:B013/m01`); object signifying without speech (`quranic:root_001272:B014/m01`); fabricated discourse (`quranic:root_000434:B007/m01`); coercing a thing into an affair (`quranic:root_000831:B003/m01`); deviation from guidance (`quranic:root_000913:B001/m01`); disappearance and loss (`quranic:root_000913:B002/m01`); losing the sought object (`quranic:root_000913:B003/m01`); loss from memory (`quranic:root_000913:B004/m01`); covering or denying truth (`quranic:root_001307:B003/m01`); affirmative reply after negation (`quranic:root_000154:B010/m01`).
- Ayah anchors: 67:1 `شَىْءٍ` (ش ي ء); 67:2 `خَلَقَ` (خ ل ق); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق); 67:6 `كَفَرُ` (ك ف ر); 67:9 `كَذَّبْ` (ك ذ ب), `قَالُ/قُلْ` (ق و ل), `شَىْءٍ` (ش ي ء), `ضَلَٰلٍ` (ض ل ل); 67:10 `قَالُ` (ق و ل); 67:13 `قَوْلَ` (ق و ل); 67:14 `خَلَقَ` (خ ل ق); surface anchors unavailable for `ب ل ي` (missing root coverage).
- Synthesis: Denial is shown as active counter-production. It can accuse, fabricate, circulate, harden into doctrine, or make appearance misreport condition. Failed milk and the fleeing animal that pauses to look back give false expectation and interrupted commitment concrete forms. Error then appears as both wrong direction and loss of the very object or memory needed to correct it.

#### Subchannel C. Hearing and Reasoning Bind Impulse
- Reading type: mixed
- Scene or process: Sound reaches an ear, becomes understood instruction, and should be held by an inward restraint that prevents reckless action.
- Active motifs: auditory reception (`quranic:root_000741:B001/m01`); ear and auditory opening (`quranic:root_000741:B002/m01`); comprehension followed by compliance (`quranic:root_000741:B003/m01`); public reputation carried by hearing (`quranic:root_000741:B005/m01`); abusive speech entering the ear (`quranic:root_000741:B006/m01`); bucket handle balancing a load (`quranic:root_000741:B008/m01`); restraining shackle (`quranic:root_000741:B009/m01`); report heard but not reaching its target (`quranic:root_000741:B011/m01`); conjecture from uncertain hearing and sight (`quranic:root_000741:B013/m01`); empty land beyond hearing and sight (`quranic:root_000741:B014/m01`); paired plow beams (`quranic:root_000741:B015/m01`); brain as "mother of hearing" (`quranic:root_000741:B016/m01`); intellect that restrains ignorance (`quranic:root_001036:B001/m01`); camel bound by a tether (`quranic:root_001036:B002/m01`); restrained tongue (`quranic:root_001036:B003/m01`); fortified refuge (`quranic:root_001036:B007/m01`); protected valuable (`quranic:root_001036:B008/m01`); entangling crooked course (`quranic:root_001036:B011/m01`); spell as a binding knot (`quranic:root_001036:B014/m01`).
- Ayah anchors: 67:7 `سَمِعُ` (س م ع); 67:10 `نَسْمَعُ` (س م ع), `نَعْقِلُ` (ع ق ل).
- Synthesis: Hearing becomes accountable only when it reaches the brain, is understood, and exerts restraint. Handles, paired plow beams, tethers, and fortifications all materialize the rational function of holding a course. The abusive report and uncertain hearer mark failure modes: sound may arrive yet become scandal, conjecture, or noise rather than guidance.

#### Subchannel D. Confession Converts Hidden Guilt into Sentence
- Reading type: mixed
- Scene or process: The offender recognizes and states the offense; liability becomes visible, and the condemned company is assigned distance and destination.
- Active motifs: recognition by sign (`quranic:root_001002:B003/m01`); known good against which conduct is judged (`quranic:root_001002:B005/m01`); explicit confession and submission (`quranic:root_001002:B009/m01`); inward patience under calamity (`quranic:root_001002:B010/m01`); sin with a harmful consequence (`quranic:root_000521:B001/m01`); trailing end or consequence (`quranic:root_000521:B002/m01`); subordinate followers (`quranic:root_000521:B003/m01`); allotted share of punishment (`quranic:root_000521:B006/m01`); full bucket as allotted measure (`quranic:root_000521:B007/m01`); pulverization (`quranic:root_000683:B001/m01`); banishment to distance (`quranic:root_000683:B002/m01`); violent expulsion (`quranic:root_000683:B008/m01`); companionship and attached status (`quranic:root_000844:B001/m02`); preservation through company (`quranic:root_000844:B002/m01`); final destination (`quranic:root_000897:B001/m02`); miserable condition (`quranic:root_000079:B002/m01`); grief at the hated outcome (`quranic:root_000079:B003/m01`); condemning formula (`quranic:root_000079:B004/m01`).
- Ayah anchors: 67:6 `مَصِيرُ` (ص ي ر), `بِئْسَ` (ب ء س); 67:10 `أَصْحَٰبِ` (ص ح ب); 67:11 `ٱعْتَرَفُ` (ع ر ف), `ذَنۢبِ` (ذ ن ب), `سُحْقًا` (س ح ق), `أَصْحَٰبِ` (ص ح ب).
- Synthesis: Confession moves guilt from inward condition to acknowledged record. The tail image makes the offense inseparable from its consequence; the bucket and allotted share make sentence measurable; pulverization and expulsion enact the verdict. "Companions" then becomes a severe social relation: the group is constituted by the destination it shares.

### 10. P1: Concealment Is Permeable to Knowledge
- Semantic invariant: Speech and intention can move between hidden and exposed states, but no covering blocks the knowledge of the one who formed the interior.
- Surface relation: direct; 67:12 `بِٱلْغَيْبِ`; 67:13 `أَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِ`, `بِذَاتِ ٱلصُّدُورِ`; 67:14 `يَعْلَمُ مَنْ خَلَقَ`, `ٱللَّطِيفُ ٱلْخَبِيرُ`.
- Surprising reach: Secrecy includes a hidden crescent, navel, hollow fire-drill, palm lines, intimate chamber, buried roots, covered surfaces, and a wound protected from its consequence.

#### Subchannel A. Speech Crosses the Hidden-Open Boundary
- Reading type: mixed
- Scene or process: A proposition exists inwardly, is shared in secret, or is projected outward through voice and visible declaration.
- Active motifs: concealed communication (`quranic:root_000697:B001/m01`); hidden crescent (`quranic:root_000697:B004/m02`); innermost and choicest part (`quranic:root_000697:B005/m01`); navel and severed cord (`quranic:root_000697:B006/m01`); hollow fire-drill or tube (`quranic:root_000697:B008/m02`); palm and forehead lines (`quranic:root_000697:B009/m01`); concealed joy and ease (`quranic:root_000697:B010/m01`); resting couch or seat (`quranic:root_000697:B011/m01`); expert who penetrates secrets (`quranic:root_000697:B014/m01`); audible public declaration (`quranic:root_000269:B001/m01`); visible appearance after a veil is removed (`quranic:root_000269:B002/m01`); impressive visible form (`quranic:root_000269:B003/m01`); water exposed by cleaning a well (`quranic:root_000269:B008/m01`); voiced consonant blocking then releasing breath (`quranic:root_000269:B011/m01`); articulated saying (`quranic:root_001272:B001/m02`); tongue as speech instrument (`quranic:root_001272:B002/m01`); inward unuttered speech (`quranic:root_001272:B012/m02`); chest as container (`quranic:root_000849:B001/m02`); source from which action issues (`quranic:root_000849:B004/m01`).
- Ayah anchors: 67:9 `قَالُ/قُلْ` (ق و ل); 67:10 `قَالُ` (ق و ل); 67:13 `أَسِرُّ` (س ر ر), `ٱجْهَرُ` (ج ه ر), `قَوْلَ` (ق و ل), `صُّدُورِ` (ص د ر).
- Synthesis: Hidden and public speech are two states of one process. The hollow drill, navel, palm lines, chest, and cleaned well each place an interior behind a surface; voice then gives the interior a channel outward. The voiced-consonant image is especially exact: pressure is held at an articulatory boundary until sound is released.

#### Subchannel B. Fine-Grained Knowledge Reaches the Interior
- Reading type: mixed
- Scene or process: An expert knower reads signs, tests hidden structure, and reaches details too fine or inward for ordinary sensation.
- Active motifs: knowledge as disclosure (`quranic:root_001040:B001/m01`); sign or landmark that guides (`quranic:root_001040:B002/m01`); hidden reservoir of abundant water (`quranic:root_001040:B005/m01`); expert knowledge of inward condition (`quranic:root_000387:B001/m01`); low soft land holding water (`quranic:root_000387:B002/m01`); cultivator who knows and repairs land (`quranic:root_000387:B003/m01`); capacious vessel or abundant she-camel (`quranic:root_000387:B004/m01`); tactful beneficence (`quranic:root_001356:B001/m01`); fineness, smallness, and sensory elusiveness (`quranic:root_001356:B002/m01`); subtle gift (`quranic:root_001356:B003/m01`); close adhesion to a flank (`quranic:root_001356:B005/m01`); inward insight (`quranic:root_000121:B002/m01`); knowing through feared consequence (`quranic:root_000413:B002/m01`); penetrating secrets (`quranic:root_000697:B014/m02`).
- Ayah anchors: 67:3 `بَصَرَ` (ب ص ر); 67:4 `بَصَرَ/بَصَرُ` (ب ص ر); 67:12 `يَخْشَ` (خ ش ي); 67:13 `عَلِيمٌۢ` (ع ل م), `أَسِرُّ` (س ر ر); 67:14 `يَعْلَمُ` (ع ل م), `خَبِيرُ` (خ ب ر), `لَّطِيفُ` (ل ط ف).
- Synthesis: Knowledge here is not generic awareness. It resembles a landmark that reveals route, a field expert who reads low wet ground, a vessel whose capacity is known from within, and a fine movement beneath sensory resolution. Creation grounds the access: the maker knows the adhered parts and hidden capacities because those details belong to the made structure.

#### Subchannel C. Covering Protects Without Erasing the Record
- Reading type: mixed
- Scene or process: A vulnerable surface or guilty person is covered and protected from exposure or consequence, while the covered condition remains known.
- Active motifs: protective covering (`quranic:root_001096:B001/m03`); forgiveness covering an offense and its effect (`quranic:root_001096:B002/m01`); garment nap covering a surface (`quranic:root_001096:B003/m02`); concealment from sight (`quranic:root_001117:B001/m01`); pit in which an object disappears (`quranic:root_001117:B002/m01`); grove that hides its entrant (`quranic:root_001117:B003/m01`); hidden tree roots (`quranic:root_001117:B008/m01`); burial (`quranic:root_001117:B009/m01`); armor left bare of its cover (`quranic:root_000320:B002/m01`); fitted defensive armor (`quranic:root_000121:B005/m03`); canopy against pests (`quranic:root_001315:B006/m02`); wrapping material around an object (`quranic:root_001307:B001/m02`); expiation that covers an offense (`quranic:root_001307:B009/m01`); awe toward what is unseen (`quranic:root_000413:B001/m01`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر); 67:3 `بَصَرَ` (ب ص ر); 67:4 `حَسِيرٌ` (ح س ر), `بَصَرَ/بَصَرُ` (ب ص ر); 67:6 `كَفَرُ` (ك ف ر); 67:8 `كُلَّمَآ` (ك ل ل); 67:12 `مَّغْفِرَةٌ` (غ ف ر), `غَيْبِ` (غ ي ب), `يَخْشَ` (خ ش ي).
- Synthesis: Covering has several functions: visual concealment, bodily defense, burial, and protection from an offense's consequence. Forgiveness belongs to this mechanism without becoming ignorance; the record is covered in its harmful effect, not rendered inaccessible to knowledge. The bare soldier supplies the contrast that makes protection visible.

### 11. P1: The Earth Is a Tamed Route with Bodily Topography
- Semantic invariant: Habitable ground is made traversable by lowering resistance, while walking reads its sides, shoulders, inclines, and hazards as a body-like route.
- Surface relation: direct; 67:15 `جَعَلَ لَكُمُ ٱلْأَرْضَ ذَلُولًا فَٱمْشُوا۟ فِى مَنَاكِبِهَا`.
- Surprising reach: The earth becomes carpet, animal underside, shoulder, hoof-circle, crosswind, bodily tremor, termite-eaten timber, and a path whose ease is learned through gait.

#### Subchannel A. A Tractable Road Receives the Walker
- Reading type: mixed
- Scene or process: Ground is lowered from resistance into a compliant route, and a traveler advances by reading its sides and maintaining an intentional gait.
- Active motifs: earth as the low counterpart of sky (`quranic:root_000025:B001/m01`); staying close to the ground (`quranic:root_000025:B006/m01`); confronting or presenting oneself on the ground (`quranic:root_000025:B007/m01`); humility under force (`quranic:root_000519:B001/m01`); gentle compliance without humiliation (`quranic:root_000519:B002/m01`); road or mount made easy after difficulty (`quranic:root_000519:B003/m01`); proper course along which an affair runs (`quranic:root_000519:B004/m01`); swift compliant movement (`quranic:root_000519:B007/m01`); intentional locomotion (`quranic:root_001427:B001/m01`); growth and livestock that "walk" as wealth (`quranic:root_001427:B003/m01`); turning aside from a route (`quranic:root_001546:B001/m01`); gait or body leaning to one side (`quranic:root_001546:B003/m01`); shoulder and side of land or mountain (`quranic:root_001546:B004/m01`); community's dependable shoulder (`quranic:root_001546:B005/m01`).
- Ayah anchors: 67:15 `أَرْضَ` (ء ر ض), `ذَلُولًا` (ذ ل ل), `ٱمْشُ` (م ش ي), `مَنَاكِبِ` (ن ك ب).
- Synthesis: Traversability is a relation between resisting ground and a directed body. The earth is low, the route is softened, the walker chooses a course, and shoulders mark lateral structure. The dependable human shoulder extends the same operation socially: a path or group works when weight can be borne without collapse or coercive humiliation.

#### Subchannel B. Ground Carries Obstacles, Lesions, and Shock
- Reading type: latent/lexical
- Scene or process: A traveler encounters a terrain-body whose surface can shake, sicken, be eaten from within, injure a hoof, or suffer a sudden blow of circumstance.
- Active motifs: thick woolen ground-cover (`quranic:root_000025:B005/m01`); bodily tremor called "earth" (`quranic:root_000025:B008/m01`); cold or catarrh (`quranic:root_000025:B009/m01`); termite consuming timber (`quranic:root_000025:B010/m01`); suppurating ulcer (`quranic:root_000025:B011/m01`); involuntary bodily agitation (`quranic:root_000025:B012/m01`); low dangling part (`quranic:root_000519:B005/m01`); peg whose head is battered (`quranic:root_000519:B006/m01`); crosswind off the main directions (`quranic:root_001546:B002/m01`); shoulder or hoof injury (`quranic:root_001546:B006/m01`); contents dumped from a vessel (`quranic:root_001546:B007/m01`); sudden worldly calamity (`quranic:root_001546:B008/m01`); circular mark in hoof or pad (`quranic:root_001546:B009/m01`).
- Ayah anchors: 67:15 `أَرْضَ` (ء ر ض), `ذَلُولًا` (ذ ل ل), `مَنَاكِبِ` (ن ك ب).
- Synthesis: The tractable earth is not flattened into featureless ease. Carpet, shoulder, peg, hoof, lesion, and crosswind make a textured route whose defects can be external or hidden within its material. The termite and ulcer are especially close analogues: both destroy a supporting surface from inside before failure becomes obvious.

#### Subchannel C. Eating Converts the Route into Provision and Return
- Reading type: mixed
- Scene or process: Walking reaches edible yield; food becomes an allotted share; consumption sustains the traveler until the final return.
- Active motifs: eating food (`quranic:root_000043:B001/m01`); fruit and crop yield (`quranic:root_000043:B002/m02`); edible allotted share (`quranic:root_000043:B003/m01`); consuming property (`quranic:root_000043:B004/m01`); prey prepared for eating (`quranic:root_000043:B007/m01`); small company measured by one head of food (`quranic:root_000043:B011/m01`); strength and completeness of material (`quranic:root_000043:B012/m01`); eating vessel and place (`quranic:root_000043:B013/m01`); apportioned gift (`quranic:root_000560:B001/m01`); sustaining food (`quranic:root_000560:B002/m01`); fortune as one's lot (`quranic:root_000560:B006/m01`); opening and spreading (`quranic:root_001503:B001/m01`); revival after death (`quranic:root_001503:B002/m02`); livestock spreading to pasture (`quranic:root_001503:B006/m01`); public written decree (`quranic:root_001503:B009/m01`); generosity (`quranic:root_001503:B010/m01`); movement toward final outcome (`quranic:root_000897:B001/m03`); settled destination (`quranic:root_000897:B007/m01`).
- Ayah anchors: 67:6 `مَصِيرُ` (ص ي ر); 67:15 `كُلُ` (ء ك ل), `رِّزْقِ` (ر ز ق), `نُّشُورُ` (ن ش ر).
- Synthesis: Provision is a route process rather than a static possession: land yields, a share is assigned, a company eats, strength is maintained, livestock fan out, and the traveler proceeds toward a settled end. Consumption of another's property supplies the ethical failure within the same mechanism. The open decree and generosity show provision as both material distribution and publicly ordered gift.

### 12. P1: Waterworks Feed a Dairy and Crop Economy
- Semantic invariant: Water is collected, routed, held, and converted into biological yield; the same infrastructure joins basin, well, field, udder, and morning ration.
- Surface relation: indirect; 67:1 `تَبَٰرَكَ`; 67:2 `ٱلْحَيَوٰةَ`; 67:3,5 `سَمَٰوَٰتٍ/ٱلسَّمَآءَ`; 67:8 `يَأْتِ`; 67:15 `أَرْضَ`, `كُلُوا`, `رِّزْقِهِ`.
- Surprising reach: The network links heavenly provision to channels, cisterns, stagnant fortress pools, rock-cut catchments, bucket tackle, udder return, breakfast drink, and milk scarcity.

#### Subchannel A. Channel, Catchment, Well, and Returning Flow
- Reading type: latent/lexical
- Scene or process: Water arrives, is steered through a channel, gathers in a catchment, and is recovered from a well or recurring pool.
- Active motifs: directed water channel (`quranic:root_000009:B004/m01`); imported flood (`quranic:root_000009:B005/m02`); fixed cistern or pool (`quranic:root_000109:B003/m01`); stagnant water around a fortification (`quranic:root_000281:B003/m01`); duplicate fortress catchment (`quranic:root_000282:B002/m01`); rock hollow or new well holding rain (`quranic:root_000434:B011/m01`); returning rain and pool water (`quranic:root_000544:B006/m02`); abundant gathered water (`quranic:root_000532:B013/m02`); sea or water-rich well (`quranic:root_001040:B005/m02`); uncovered well (`quranic:root_001248:B007/m01`); water-filled hollow (`quranic:root_001292:B003/m01`); well stone and suspension timbers (`quranic:root_000547:B006/m02`); bucket handle that balances drawing (`quranic:root_000741:B008/m02`); low soft ground where water gathers (`quranic:root_000387:B002/m02`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:2 `خَلَقَ` (خ ل ق); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق), `ٱرْجِعِ` (ر ج ع); 67:4 `ٱرْجِعِ` (ر ج ع), `يَنقَلِبْ` (ق ل ب), `كَرَّتَيْنِ` (ك ر ر); 67:5 `رُجُومًا` (ر ج م); 67:6 `رَبِّ` (ر ب ب); 67:7 `سَمِعُ` (س م ع); 67:8 `يَأْتِ` (ء ت ي); 67:9 `جَآءَ` (ج ي ء); 67:10 `نَسْمَعُ` (س م ع); 67:12 `رَبَّ` (ر ب ب); 67:13 `عَلِيمٌۢ` (ع ل م); 67:14 `خَلَقَ` (خ ل ق), `يَعْلَمُ` (ع ل م), `خَبِيرُ` (خ ب ر).
- Synthesis: The motifs assemble an actual water system. An external flood enters a directed channel, settles in a basin or rock hollow, and is accessed by well tackle and balanced bucket. Recurrence matters: return is the operation that renews supply. The fortress pool adds pressure by showing that collected water can preserve a settlement yet become foul when flow stops.

#### Subchannel B. Water Becomes Fruit, Milk, and Morning Ration
- Reading type: latent/lexical
- Scene or process: Stored moisture enters plants and animals, returns as fruit or milk, and is taken as an early ration.
- Active motifs: biological yield and abundant water (`quranic:root_000009:B007/m02`); milk of a kneeling she-camel (`quranic:root_000109:B007/m02`); crop and tree produce (`quranic:root_000043:B002/m03`); thick syrup used to preserve or improve (`quranic:root_000532:B006/m01`); recently delivered milk ewe (`quranic:root_000532:B009/m01`); herd of cattle or camels (`quranic:root_000532:B014/m01`); udder with little milk (`quranic:root_001008:B006/m01`); milk drawn by fingertips (`quranic:root_001165:B005/m01`); morning drink or feed (`quranic:root_000839:B003/m01`); capacious skin or abundant she-camel (`quranic:root_000387:B004/m02`); ibex calf and dam (`quranic:root_001096:B005/m01`); living pasture from rain (`quranic:root_000383:B002/m02`); edible sustenance (`quranic:root_000560:B002/m02`); livestock increase (`quranic:root_001427:B003/m02`); favorable lot (`quranic:root_000560:B006/m02`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:2 `عَزِيزُ` (ع ز ز), `غَفُورُ` (غ ف ر), `حَيَوٰةَ` (ح ي ي); 67:3 `فُطُورٍ` (ف ط ر); 67:5 `مَصَٰبِيحَ` (ص ب ح); 67:6 `رَبِّ` (ر ب ب); 67:8 `يَأْتِ` (ء ت ي); 67:12 `رَبَّ` (ر ب ب), `مَّغْفِرَةٌ` (غ ف ر); 67:14 `خَبِيرُ` (خ ب ر); 67:15 `كُلُ` (ء ك ل), `رِّزْقِ` (ر ز ق), `ٱمْشُ` (م ش ي).
- Synthesis: Moisture passes through a conversion chain: rain makes pasture, pasture sustains herd and dam, the udder gathers milk, and morning consumption realizes the provision. Scarcity at the udder is a precise pressure point because it shows that possession of an animal does not guarantee flow. Syrup and skin-vessel motifs add the post-yield operations of preserving and carrying what has been given.

### 13. P1: The Tamed Earth Is Rehearsed in Camel and Herd Mechanics
- Semantic invariant: Tractability is learned through animal bodies: kneeling, tethering, stepping, carrying, breeding, grazing, and exposure to predation.
- Surface relation: indirect; 67:1 `تَبَٰرَكَ`; 67:2 `ٱلْحَيَوٰةَ`; 67:3 `طِبَاقًا`; 67:15 `ذَلُولًا`, `ٱمْشُوا`, `مَنَاكِبِهَا`, `كُلُوا`.
- Surprising reach: The manageable earth is pressured by a complete pastoral scene involving chest callus, alternating forelegs, shoulder lesions, working limbs, harness seams, estrus, pregnancy, offspring, and the predator's ration.

#### Subchannel A. Kneeling, Harness, and Coordinated Gait
- Reading type: latent/lexical
- Scene or process: A working camel is made manageable, lowered to the ground, fitted with tackle, and moved by coordinated limbs over a legible surface.
- Active motifs: camel kneeling and remaining fixed (`quranic:root_000109:B001/m01`); chest pressed to ground (`quranic:root_000109:B002/m01`); forelegs returning in gait (`quranic:root_000009:B009/m01`); animal steps changing cadence (`quranic:root_000544:B008/m02`); returned mount restored after travel (`quranic:root_000544:B014/m02`); breast callus of the camel (`quranic:root_001292:B007/m01`); hind foot placed in forefoot track (`quranic:root_000927:B007/m01`); working camel formed for labor (`quranic:root_001046:B008/m01`); load-bearing limbs (`quranic:root_001046:B010/m02`); hide left with hair attached (`quranic:root_000844:B006/m01`); mount and road made tractable (`quranic:root_000519:B003/m02`); shoulder and terrain flank (`quranic:root_001546:B004/m02`); shoulder or hoof lesion (`quranic:root_001546:B006/m02`); circular mark in hoof or pad (`quranic:root_001546:B009/m02`); physical hand or forelimb (`quranic:root_001693:B001/m01`); underbody nearest the earth (`quranic:root_000025:B001/m02`); shedding old hair (`quranic:root_000320:B005/m01`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك), `يَدِ` (ي د ي); 67:2 `عَمَلًا` (ع م ل); 67:3 `ٱرْجِعِ` (ر ج ع), `طِبَاقًا` (ط ب ق); 67:4 `ٱرْجِعِ` (ر ج ع), `كَرَّتَيْنِ` (ك ر ر), `حَسِيرٌ` (ح س ر); 67:8 `يَأْتِ` (ء ت ي); 67:10 `أَصْحَٰبِ` (ص ح ب); 67:11 `أَصْحَٰبِ` (ص ح ب); 67:15 `ذَلُولًا` (ذ ل ل), `مَنَاكِبِ` (ن ك ب), `أَرْضَ` (ء ر ض).
- Synthesis: Tractability appears as trained biomechanics. The animal lowers its chest, receives a hair-on hide and harness, places feet in a controlled sequence, and transfers load through hand, shoulder, and hoof. Lesion and callus mark the cost of repeated contact. This concrete scene materializes 67:15's relation between a compliant earth and the body that can travel it.

#### Subchannel B. Breeding, Herd Continuity, and Predation
- Reading type: latent/lexical
- Scene or process: A herd reproduces, recognizes pregnancy and maturation, loses offspring, and remains vulnerable to beasts that turn livestock into prey.
- Active motifs: she-camel seeking the male (`quranic:root_000009:B012/m01`); female animal in estrus (`quranic:root_000248:B009/m01`); ostrich chick (`quranic:root_000248:B010/m01`); snake as a living creature (`quranic:root_000383:B004/m01`); predatory beast (`quranic:root_000669:B002/m01`); extreme taking like a beast (`quranic:root_000669:B005/m01`); prey reserved or fattened for eating (`quranic:root_000043:B007/m02`); hideous animal called a devil (`quranic:root_000796:B005/m02`); newly delivered milk animal (`quranic:root_000532:B009/m02`); collected herd (`quranic:root_000532:B014/m02`); suspected pregnancy that does not hold (`quranic:root_000544:B013/m01`); visible pregnancy and swelling udder (`quranic:root_000531:B010/m01`); fast conception (`quranic:root_001372:B003/m01`); erupting tooth as maturity sign (`quranic:root_001165:B007/m01`); parent losing offspring (`quranic:root_001454:B005/m01`); ibex offspring and dam (`quranic:root_001096:B005/m02`); remarriage of a woman with an adult son (`quranic:root_000109:B009/m01`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:2 `حَيَوٰةَ` (ح ي ي), `مَوْتَ` (م و ت), `غَفُورُ` (غ ف ر); 67:3 `سَبْعَ` (س ب ع), `ٱرْجِعِ` (ر ج ع), `تَرَىٰ/تَرَىٰ` (ر ء ي), `فُطُورٍ` (ف ط ر); 67:4 `ٱرْجِعِ` (ر ج ع); 67:5 `جَعَلْ` (ج ع ل), `شَّيَٰطِينِ` (ش ط ن); 67:6 `رَبِّ` (ر ب ب); 67:7 `أُلْقُ` (ل ق ي); 67:8 `يَأْتِ` (ء ت ي), `أُلْقِىَ` (ل ق ي); 67:12 `رَبَّ` (ر ب ب), `مَّغْفِرَةٌ` (غ ف ر); 67:15 `جَعَلَ` (ج ع ل), `كُلُ` (ء ك ل).
- Synthesis: The scene follows herd continuity through desire, conception, pregnancy signs, birth, maturation, and loss. Predation is the counter-process that converts nurtured stock into another creature's food. Remarriage after a son matures extends continuity into household structure without merging the domestic role with the animal breeding operation.

### 14. P1: Surfaces Are Sewn, Wrapped, and Worked by Implements
- Semantic invariant: Integrity is made at a material boundary by joining panels, preserving skins, wrapping surfaces, and applying purpose-built tools.
- Surface relation: indirect; 67:3-4 inspection for `فُطُورٍ`; 67:5 transformation into `مَصَٰبِيحَ` and `رُجُومًا`; 67:13 hidden and exposed speech.
- Surprising reach: Cosmic fit and moral covering are reframed through hide, nap, worn cloth, tattoo lines, rope, quiver, bucket, armor, cooking pot, bracelet, plow beam, and spear shaft.

#### Subchannel A. Hide, Cloth, Seam, and Surface Wear
- Reading type: latent/lexical
- Scene or process: A skin or fabric is cut, joined, marked, wrapped, worn, and sometimes reworked after its surface has deteriorated.
- Active motifs: thick edge and sewn panels (`quranic:root_000121:B006/m02`); surface nap or hair (`quranic:root_001096:B003/m03`); hide retaining hair (`quranic:root_000844:B006/m02`); worn cloth stripped of nap (`quranic:root_000434:B009/m02`); textile worn by use (`quranic:root_000153:B001/m02`); duplicate worn-cloth image (`quranic:root_000154:B001/m02`); fabric abraded into decay (`quranic:root_000683:B004/m02`); thin membrane over bone or fat (`quranic:root_000683:B010/m01`); sewn protective canopy (`quranic:root_001315:B006/m03`); thick woolen carpet (`quranic:root_000025:B005/m02`); retraced tattoo or inscription (`quranic:root_000544:B009/m02`); old material reworked after undoing (`quranic:root_000544:B015/m02`); palm and forehead lines (`quranic:root_000697:B009/m02`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر), `خَلَقَ` (خ ل ق), `يَبْلُوَ` (ب ل و); 67:3 `بَصَرَ` (ب ص ر), `خَلَقَ/خَلْقِ` (خ ل ق), `ٱرْجِعِ` (ر ج ع); 67:4 `بَصَرَ/بَصَرُ` (ب ص ر), `ٱرْجِعِ` (ر ج ع); 67:8 `كُلَّمَآ` (ك ل ل); 67:10 `أَصْحَٰبِ` (ص ح ب); 67:11 `أَصْحَٰبِ` (ص ح ب), `سُحْقًا` (س ح ق); 67:12 `مَّغْفِرَةٌ` (غ ف ر); 67:13 `أَسِرُّ` (س ر ر); 67:14 `خَلَقَ` (خ ل ق); 67:15 `أَرْضَ` (ء ر ض); surface anchors unavailable for `ب ل ي` (missing root coverage).
- Synthesis: Surface integrity emerges from several precise operations: leave hair on hide, preserve nap, fold while damp, sew edges, retrace marks, and rework old material. Wear is not conflated with rupture; abrasion, loss of nap, and seam failure are different states. The textile scene gives the sky's searched-for fissure and forgiveness's covering a shared but materially disciplined substrate.

#### Subchannel B. Containers, Handles, Tethers, and Heat Tools
- Reading type: latent/lexical
- Scene or process: A workshop or camp uses vessels to hold material, handles and ropes to direct load, and tools to manage fire, drawing, grinding, and striking.
- Active motifs: unguarded roof surface (`quranic:root_000015:B003/m01`); bowl or eating vessel (`quranic:root_000043:B013/m02`); heat-protecting pot cloth (`quranic:root_000248:B007/m03`); hide container for gaming arrows (`quranic:root_000532:B010/m01`); well stone and suspension timbers (`quranic:root_000547:B006/m03`); bucket handle (`quranic:root_000741:B008/m03`); paired plow beams (`quranic:root_000741:B015/m02`); camel tether and hobble (`quranic:root_001036:B002/m02`); cooking pot and butcher-cook (`quranic:root_001205:B007/m02`); hand reaching into quiver (`quranic:root_000544:B010/m02`); thick twisted rope (`quranic:root_001292:B002/m01`); long well rope (`quranic:root_000796:B002/m02`); spear shaft (`quranic:root_001046:B009/m02`); shield or armor (`quranic:root_000121:B005/m04`); large drinking vessel (`quranic:root_000978:B004/m01`); bracelet (`quranic:root_001248:B008/m01`); instrument handle (`quranic:root_001693:B013/m02`); mill's rotating grind (`quranic:root_001292:B010/m02`).
- Ayah anchors: 67:1 `قَدِيرٌ` (ق د ر), `يَدِ` (ي د ي); 67:2 `عَمَلًا` (ع م ل); 67:3 `ٱرْجِعِ` (ر ج ع), `بَصَرَ` (ب ص ر); 67:4 `ٱرْجِعِ` (ر ج ع), `كَرَّتَيْنِ` (ك ر ر), `بَصَرَ/بَصَرُ` (ب ص ر), `يَنقَلِبْ` (ق ل ب); 67:5 `جَعَلْ` (ج ع ل), `رُجُومًا` (ر ج م), `شَّيَٰطِينِ` (ش ط ن), `أَعْتَدْ` (ع ت د); 67:6 `رَبِّ` (ر ب ب); 67:7 `سَمِعُ` (س م ع); 67:10 `نَسْمَعُ` (س م ع), `نَعْقِلُ` (ع ق ل); 67:12 `أَجْرٌ` (ء ج ر), `رَبَّ` (ر ب ب); 67:15 `كُلُ` (ء ك ل), `جَعَلَ` (ج ع ل).
- Synthesis: Each object has a bounded mechanical role. Vessels hold, ropes suspend, handles transmit grip, quivers stage projectiles, plow beams align animal force, a pot cloth interrupts heat transfer, and the mill applies repeated rotation. This is a coherent implement system, not a list of artifacts, because every motif converts bodily force into controlled material action.

### 15. P1: Rule Extends into Office, Labor, Contract, and Household
- Semantic invariant: Authority persists through delegated offices, compensated work, binding agreements, and households that reproduce social responsibility.
- Surface relation: indirect; 67:1 `ٱلْمُلْكُ`; 67:2 `عَمَلًا`; 67:6,12 `رَبِّهِمْ/رَبَّهُم`; 67:8 `خَزَنَتُهَا`; 67:12 `أَجْرٌ`; 67:15 `رِّزْقِهِ`.
- Surprising reach: Kingdom becomes tax office, custody, sharecropping, wage, dowry, marriage contract, fosterage, inheritance, and the covenant that secures a neighbor or dependent.

#### Subchannel A. Office, Custody, and Delegated Administration
- Reading type: latent/lexical
- Scene or process: A sovereign order assigns custodians and officers to preserve goods, supervise land, know a community, and make commands effective.
- Active motifs: sovereign administration (`quranic:root_001444:B003/m02`); lord as owner (`quranic:root_000532:B001/m02`); nurturing and completion under care (`quranic:root_000532:B002/m01`); learned religious administrator (`quranic:root_000532:B003/m01`); captain of sailors (`quranic:root_000532:B017/m02`); chief with effective word (`quranic:root_001272:B004/m02`); appointed keeper (`quranic:root_000406:B003/m02`); public office and tax work (`quranic:root_001046:B003/m01`); local officer who knows his people (`quranic:root_001002:B006/m01`); authoritative hand (`quranic:root_001693:B005/m02`); capacity to execute (`quranic:root_001205:B003/m02`); inherited high station (`quranic:root_001281:B005/m01`); confiscation or official financial liability (`quranic:root_000849:B005/m01`); tax or tribute rendered (`quranic:root_000009:B008/m02`); reward placed on a task (`quranic:root_000248:B005/m01`).
- Ayah anchors: 67:1 `مُلْكُ` (م ل ك), `يَدِ` (ي د ي), `قَدِيرٌ` (ق د ر); 67:2 `عَمَلًا` (ع م ل); 67:5 `جَعَلْ` (ج ع ل); 67:6 `رَبِّ` (ر ب ب); 67:8 `خَزَنَتُ` (خ ز ن), `يَأْتِ` (ء ت ي); 67:9 `قَالُ/قُلْ` (ق و ل), `كَبِيرٍ` (ك ب ر); 67:10 `قَالُ` (ق و ل); 67:11 `ٱعْتَرَفُ` (ع ر ف); 67:12 `رَبَّ` (ر ب ب), `كَبِيرٌ` (ك ب ر); 67:13 `قَوْلَ` (ق و ل), `صُّدُورِ` (ص د ر); 67:15 `جَعَلَ` (ج ع ل).
- Synthesis: Administration transmits rule through differentiated roles: owner, captain, keeper, land-knower, tax officer, and community head. Custody and knowledge are operational requirements, while tribute, confiscation, and task reward expose the economic force of office. The scene keeps divine dominion distinct from human administration while using the latter to materialize delegation.

#### Subchannel B. Work Is Assigned, Performed, and Compensated
- Reading type: mixed
- Scene or process: A task is defined, a worker or crew undertakes it, and wage or provision returns in exchange for accountable performance.
- Active motifs: recompense, wage, or hire (`quranic:root_000015:B001/m01`); intentional work (`quranic:root_001046:B001/m02`); employing an instrument or person (`quranic:root_001046:B002/m02`); appointment to office (`quranic:root_001046:B003/m02`); worker's pay (`quranic:root_001046:B004/m01`); reciprocal transaction (`quranic:root_001046:B005/m01`); manual work crew (`quranic:root_001046:B006/m01`); effort and hardship (`quranic:root_001046:B007/m01`); animal formed for labor (`quranic:root_001046:B008/m02`); worked road (`quranic:root_001046:B011/m01`); travelers on foot (`quranic:root_001046:B012/m01`); bounty attached to a task (`quranic:root_000248:B005/m02`); possession and transfer (`quranic:root_001444:B002/m02`); military ration (`quranic:root_000560:B004/m01`); negotiation over an affair (`quranic:root_001272:B009/m01`); covenant or protection agreement (`quranic:root_000532:B011/m01`).
- Ayah anchors: 67:1 `مُلْكُ` (م ل ك); 67:2 `عَمَلًا` (ع م ل); 67:5 `جَعَلْ` (ج ع ل); 67:6 `رَبِّ` (ر ب ب); 67:9 `قَالُ/قُلْ` (ق و ل); 67:10 `قَالُ` (ق و ل); 67:12 `أَجْرٌ` (ء ج ر), `رَبَّ` (ر ب ب); 67:13 `قَوْلَ` (ق و ل); 67:15 `جَعَلَ` (ج ع ل), `رِّزْقِ` (ر ز ق).
- Synthesis: The process separates assignment, execution, and return. Work may be manual, administrative, animal-powered, or travel itself, but it remains accountable action that consumes effort and justifies pay. The covenant and negotiation motifs show how labor enters a social agreement rather than remaining isolated exertion.

#### Subchannel C. Marriage, Fosterage, and Inheritance Carry Obligation Forward
- Reading type: latent/lexical
- Scene or process: Marriage forms a household, children are reared into companions and heirs, and kinship binds care, property, and covenant across generations.
- Active motifs: mother with adult son remarrying (`quranic:root_000109:B009/m02`); large kin group (`quranic:root_000532:B004/m01`); foster-child and caregiver (`quranic:root_000532:B005/m01`); kinship covenant (`quranic:root_000532:B011/m02`); clan or lineage (`quranic:root_000383:B010/m01`); concealed sexual organ or womb (`quranic:root_000383:B011/m01`); face or person in household life (`quranic:root_000383:B012/m01`); kinship bond (`quranic:root_000552:B002/m01`); womb as place of growth (`quranic:root_000552:B003/m01`); postpartum womb distress (`quranic:root_000552:B004/m01`); wage also serving as dowry (`quranic:root_000015:B001/m02`); marriage contract (`quranic:root_001444:B004/m01`); marital return after divorce (`quranic:root_000544:B004/m01`); collateral kin and inheritance (`quranic:root_001315:B004/m01`); son grown into his father's companion (`quranic:root_000844:B005/m01`); navel and severed birth cord (`quranic:root_000697:B006/m02`); greeting that invokes continued life (`quranic:root_000383:B007/m01`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك), `مُلْكُ` (م ل ك), `كُلِّ` (ك ل ل); 67:2 `حَيَوٰةَ` (ح ي ي); 67:3 `رَّحْمَٰنِ` (ر ح م), `ٱرْجِعِ` (ر ج ع); 67:4 `ٱرْجِعِ` (ر ج ع); 67:6 `رَبِّ` (ر ب ب); 67:8 `كُلَّمَآ` (ك ل ل); 67:10 `أَصْحَٰبِ` (ص ح ب); 67:11 `أَصْحَٰبِ` (ص ح ب); 67:12 `رَبَّ` (ر ب ب), `أَجْرٌ` (ء ج ر); 67:13 `أَسِرُّ` (س ر ر).
- Synthesis: Household continuity is built from contract, womb, birth, fosterage, maturation, companionship, and inheritance. The dowry anchors marriage economically, while collateral kin and covenant show obligations that outlive the immediate pair. Postpartum pain keeps the scene embodied: continuity is carried through a vulnerable organ, not an abstract lineage diagram.

### 16. P1: Distance, Expulsion, and Shelter Reassign Social Place
- Semantic invariant: A person can be placed outside by remoteness, deviation, or sentence, or placed under protection by covering, covenant, and guarded proximity.
- Surface relation: direct; 67:4 `خَاسِئًا`; 67:5 `لِّلشَّيَٰطِينِ`; 67:9 `ضَلَٰلٍ كَبِيرٍ`; 67:11 `سُحْقًا`; 67:12 `بِٱلْغَيْبِ`, `مَّغْفِرَةٌ`.
- Surprising reach: Exile includes foreigner status, a distant well, failed arrival, a ruler's closed door, and the expelled dog; shelter includes armor, canopy, grove, carpet, storehouse, covenant, and preserved companionship.

#### Subchannel A. Remoteness Becomes a Sentence of Exclusion
- Reading type: mixed
- Scene or process: Deviation or hostility produces increasing distance until the person is expelled from a protected center.
- Active motifs: geographic severance and exile (`quranic:root_000796:B001/m02`); opposing course (`quranic:root_000796:B003/m02`); rebellious outsider (`quranic:root_000796:B004/m02`); banishment (`quranic:root_000683:B002/m02`); violent chasing away (`quranic:root_000683:B008/m02`); humiliating expulsion (`quranic:root_000408:B001/m02`); exclusion from the ruler's court (`quranic:root_000320:B006/m02`); stranger called a son of the earth (`quranic:root_000025:B004/m01`); outsider entering another people (`quranic:root_000009:B006/m02`); nearness and approach (`quranic:root_000493:B001/m01`); lower and nearer status (`quranic:root_000493:B002/m02`); baseness and low rank (`quranic:root_000493:B003/m01`); body bent downward (`quranic:root_000493:B005/m01`); goal or limit reached (`quranic:root_000076:B001/m01`); delayed or detained movement (`quranic:root_000076:B013/m01`); object escaping acquisition (`quranic:root_001183:B001/m01`); loss of route (`quranic:root_000913:B001/m02`); expulsion by curse (`quranic:root_000547:B003/m02`).
- Ayah anchors: 67:3 `تَفَٰوُتٍ` (ف و ت); 67:4 `خَاسِئًا` (خ س ء), `حَسِيرٌ` (ح س ر); 67:5 `شَّيَٰطِينِ` (ش ط ن), `دُّنْيَا` (د ن و), `رُجُومًا` (ر ج م); 67:8 `يَأْتِ` (ء ت ي); 67:9 `ضَلَٰلٍ` (ض ل ل); 67:11 `سُحْقًا` (س ح ق); 67:15 `أَرْضَ` (ء ر ض); surface anchors unavailable for `ء ل ي` (missing root coverage).
- Synthesis: The process begins with misalignment and ends with social-spatial removal. Nearness and low rank establish a center-periphery scale; the stranger, remote traveler, and excluded courtier occupy intermediate positions; curse, chasing, and the command to a dog enact final expulsion. Error is thus not only an incorrect proposition but a trajectory out of protected relation.

#### Subchannel B. Cover, Covenant, and Company Make a Refuge
- Reading type: latent/lexical
- Scene or process: A vulnerable person or object is brought under a physical cover and a social guarantee that preserve it from attack or loss.
- Active motifs: fortified refuge (`quranic:root_001036:B007/m02`); roof lacking a guard wall (`quranic:root_000015:B003/m02`); protective canopy (`quranic:root_001315:B006/m04`); general covering (`quranic:root_001096:B001/m04`); armor (`quranic:root_000121:B005/m05`); covenant of protection (`quranic:root_000532:B011/m03`); preservation by companionship (`quranic:root_000844:B002/m02`); material wrapper (`quranic:root_001307:B001/m03`); secure storage (`quranic:root_000406:B001/m02`); thick carpet underfoot (`quranic:root_000025:B005/m03`); grove that conceals (`quranic:root_001117:B003/m02`); restraining oneself from harm (`quranic:root_000994:B003/m01`); absence of harm and assurance (`quranic:root_000079:B005/m01`); protective hand (`quranic:root_001693:B016/m02`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل), `يَدِ` (ي د ي); 67:2 `غَفُورُ` (غ ف ر); 67:3 `بَصَرَ` (ب ص ر); 67:4 `بَصَرَ/بَصَرُ` (ب ص ر); 67:5 `عَذَابَ` (ع ذ ب); 67:6 `رَبِّ` (ر ب ب), `كَفَرُ` (ك ف ر), `عَذَابُ` (ع ذ ب), `بِئْسَ` (ب ء س); 67:8 `كُلَّمَآ` (ك ل ل), `خَزَنَتُ` (خ ز ن); 67:10 `نَعْقِلُ` (ع ق ل), `أَصْحَٰبِ` (ص ح ب); 67:11 `أَصْحَٰبِ` (ص ح ب); 67:12 `أَجْرٌ` (ء ج ر), `مَّغْفِرَةٌ` (غ ف ر), `رَبَّ` (ر ب ب), `غَيْبِ` (غ ي ب); 67:15 `أَرْضَ` (ء ر ض).
- Synthesis: Refuge requires both enclosure and recognized status. Roof, canopy, armor, grove, store, and carpet protect by material placement; covenant, companionship, harmlessness, and the protecting hand keep an aggressor from violating that placement. The unguarded roof clarifies why mere elevation or possession is not yet security.

#### Subchannel C. Rank Rises or Falls with Strength and Submission
- Reading type: mixed
- Scene or process: Persons and acts are placed on a vertical scale of force, honor, difficulty, abasement, and willing compliance.
- Active motifs: honor and invulnerability (`quranic:root_001008:B001/m02`); prevailing over an opponent (`quranic:root_001008:B002/m02`); rare and hard to obtain (`quranic:root_001008:B003/m01`); reinforcement (`quranic:root_001008:B004/m01`); grave difficulty (`quranic:root_001008:B005/m01`); magnitude (`quranic:root_001281:B001/m01`); chief burden of an affair (`quranic:root_001281:B002/m01`); magnification in the chest (`quranic:root_001281:B003/m01`); high inherited station (`quranic:root_001281:B005/m02`); pride and self-exaltation (`quranic:root_001281:B006/m01`); burden too heavy to accept (`quranic:root_001281:B010/m01`); rivalrous overpowering (`quranic:root_001281:B011/m01`); elevated fame (`quranic:root_000745:B001/m02`); rivalry in elevation (`quranic:root_000745:B007/m01`); abasement under force (`quranic:root_000519:B001/m02`); gentle willingness (`quranic:root_000519:B002/m02`); miserable deprivation (`quranic:root_000079:B002/m02`).
- Ayah anchors: 67:2 `عَزِيزُ` (ع ز ز); 67:3 `سَمَٰوَٰتٍ` (س م و); 67:5 `سَّمَآءَ` (س م و); 67:6 `بِئْسَ` (ب ء س); 67:9 `كَبِيرٍ` (ك ب ر); 67:12 `كَبِيرٌ` (ك ب ر); 67:15 `ذَلُولًا` (ذ ل ل).
- Synthesis: Rank is not one moral value. Strength may secure honor, reinforcement may lift weakness, and willing tractability may be praiseworthy, while self-magnification and coerced abasement corrupt the same vertical scale. The chest image localizes pride as an inward act of making something loom large before it becomes outward status.

### 17. P1: Bodily Interiors Fail by Pressure, Lesion, and Decay
- Semantic invariant: Hidden bodily systems disclose disorder through pressure, altered sensation, visible marks, suppuration, wasting, or involuntary movement.
- Surface relation: indirect; 67:3-4 the eye is tested and exhausted; 67:7 `شَهِيقًا`; 67:8 `ٱلْغَيْظِ`; 67:13 `ذَاتِ ٱلصُّدُورِ`; 67:14 `ٱلْخَبِيرُ`.
- Surprising reach: The moral and infernal discourse is materially pressured by lung, heart, chest, cleft lip, vein, palsied face, ulcer, pus, rotten flesh, seizure, and relapsing wound.

#### Subchannel A. Chest, Heart, Eye, and Breath Under Pressure
- Reading type: latent/lexical
- Scene or process: Pressure accumulates in an interior organ, changes breath and vision, and appears at a bodily boundary.
- Active motifs: camel chest pressing downward (`quranic:root_000109:B002/m02`); chest and breast (`quranic:root_000849:B001/m03`); front or upper part (`quranic:root_000849:B002/m01`); source from which acts issue (`quranic:root_000849:B004/m02`); heart as organ and understanding (`quranic:root_001248:B001/m01`); heart disease (`quranic:root_001248:B011/m01`); turned lip (`quranic:root_001248:B012/m01`); strike to the heart (`quranic:root_001248:B016/m01`); lung and pulmonary complaint (`quranic:root_000531:B009/m01`); glare-blinded eye (`quranic:root_000269:B004/m02`); high inhalation or groan (`quranic:root_000824:B002/m02`); exhausted vision (`quranic:root_000320:B003/m03`); brain as seat behind hearing (`quranic:root_000741:B016/m02`); chest-contained rage (`quranic:root_001121:B001/m02`); fevered swelling of vein (`quranic:root_001185:B005/m02`); upper-lip cleft (`quranic:root_001040:B004/m02`).
- Ayah anchors: 67:1 `تَبَٰرَكَ` (ب ر ك); 67:3 `تَرَىٰ/تَرَىٰ` (ر ء ي); 67:4 `يَنقَلِبْ` (ق ل ب), `حَسِيرٌ` (ح س ر); 67:7 `شَهِيقًا` (ش ه ق), `سَمِعُ` (س م ع), `تَفُورُ` (ف و ر); 67:8 `غَيْظِ` (غ ي ظ); 67:10 `نَسْمَعُ` (س م ع); 67:13 `صُّدُورِ` (ص د ر), `ٱجْهَرُ` (ج ه ر), `عَلِيمٌۢ` (ع ل م); 67:14 `يَعْلَمُ` (ع ل م).
- Synthesis: The body is a pressured container. Rage occupies the chest, breath forces a path outward, fever swells a vein, and visual or auditory systems fail at their organs. Cleft and turned lip make internal disorder visible at the surface; the struck heart and pressed chest turn moral pressure into vulnerable anatomy.

#### Subchannel B. Wounds, Corrosion, and Relapse Expose Hidden Damage
- Reading type: latent/lexical
- Scene or process: Damage begins beneath or within a surface, produces decay or discharge, and may return after apparent healing.
- Active motifs: bodily tremor (`quranic:root_000025:B008/m02`); cold or catarrh (`quranic:root_000025:B009/m02`); ulcer filling with pus (`quranic:root_000025:B011/m02`); involuntary agitation or possession (`quranic:root_000025:B012/m02`); crookedly healed fracture (`quranic:root_000015:B002/m02`); bodily corrosion and itching (`quranic:root_000043:B006/m01`); pus collected in a wound (`quranic:root_000281:B006/m01`); duplicate wound discharge (`quranic:root_000282:B003/m01`); palm ulcer (`quranic:root_001002:B011/m01`); rotting flesh (`quranic:root_000406:B004/m02`); relapse after improvement (`quranic:root_001096:B004/m02`); cardiac disease (`quranic:root_001248:B011/m02`); shedding hair or feathers (`quranic:root_000320:B005/m02`); seizure or fainting (`quranic:root_001454:B009/m02`); facial palsy (`quranic:root_001372:B001/m01`); sensory dullness (`quranic:root_001315:B001/m03`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر), `مَوْتَ` (م و ت); 67:4 `يَنقَلِبْ` (ق ل ب), `حَسِيرٌ` (ح س ر); 67:7 `أُلْقُ` (ل ق ي); 67:8 `خَزَنَتُ` (خ ز ن), `أُلْقِىَ` (ل ق ي), `كُلَّمَآ` (ك ل ل); 67:9 `جَآءَ` (ج ي ء); 67:11 `ٱعْتَرَفُ` (ع ر ف); 67:12 `أَجْرٌ` (ء ج ر), `مَّغْفِرَةٌ` (غ ف ر); 67:15 `أَرْضَ` (ء ر ض), `كُلُ` (ء ك ل).
- Synthesis: The lesion scene distinguishes break, corrosion, infection, discharge, palsy, seizure, and relapse. Several failures remain hidden until matter gathers or movement changes. The pattern usefully pressures the interior-knowledge claim: expert knowledge is needed because a repaired surface, stored flesh, or quiet wound can conceal continuing damage.

### 18. P1: Light Is Timed, Displayed, and Socially Heard
- Semantic invariant: Appearance becomes meaningful through temporal placement, visible marking, and the reputation or interpretation that observers carry away.
- Surface relation: indirect; 67:5 `زَيَّنَّا`, `مَصَٰبِيحَ`; 67:7 `سَمِعُوا`; 67:13 `أَسِرُّوا/ٱجْهَرُوا`; 67:15 the movement into an ordered day of work and food.
- Surprising reach: The lamps open onto dawn, morning raid, breakfast cup, late-rising camel, lunar hiding, named stars, facial beauty, banner, perfume, rumor, and the false display of decorated cloth.

#### Subchannel A. Dawn, Morning Operations, and Celestial Calendar
- Reading type: latent/lexical
- Scene or process: Light marks the start of a day, schedules arrival, raid, feeding, and work, and belongs to larger lunar and stellar cycles.
- Active motifs: dawn and first morning (`quranic:root_000839:B001/m02`); arriving in the morning (`quranic:root_000839:B002/m01`); morning drink and food (`quranic:root_000839:B003/m02`); morning alarm or raid (`quranic:root_000839:B004/m01`); lamp (`quranic:root_000839:B005/m02`); sleeping after dawn (`quranic:root_000839:B007/m01`); she-camel remaining kneeling into morning (`quranic:root_000839:B008/m01`); appointment on a specified morning (`quranic:root_000839:B009/m01`); entering a new state by morning (`quranic:root_000839:B010/m01`); crescent hidden at month's end (`quranic:root_000697:B004/m03`); lunar station (`quranic:root_001096:B006/m02`); Antares (`quranic:root_001248:B010/m02`); encircling lunar crown (`quranic:root_001315:B005/m02`); a layer of night or day (`quranic:root_000927:B010/m02`); recurring rain cycle (`quranic:root_000544:B006/m03`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:2 `غَفُورُ` (غ ف ر); 67:3 `طِبَاقًا` (ط ب ق), `ٱرْجِعِ` (ر ج ع); 67:4 `يَنقَلِبْ` (ق ل ب), `ٱرْجِعِ` (ر ج ع); 67:5 `مَصَٰبِيحَ` (ص ب ح); 67:8 `كُلَّمَآ` (ك ل ل); 67:12 `مَّغْفِرَةٌ` (غ ف ر); 67:13 `أَسِرُّ` (س ر ر).
- Synthesis: Morning is an operational threshold: people arrive, alarms sound, food and drink are taken, animals rise, and appointments begin. Lunar hiding, stellar station, and cyclic rain place that threshold within longer recurring measures. The lamp belongs to this timed system rather than floating as an isolated object of beauty.

#### Subchannel B. Mark, Face, Scent, and Reputation
- Reading type: latent/lexical
- Scene or process: A person or object is made attractive or recognizable, then its appearance is carried into public interpretation and report.
- Active motifs: beautification (`quranic:root_000660:B002/m02`); visible ornament (`quranic:root_000660:B003/m02`); impressive outward form (`quranic:root_000269:B003/m02`); mirror and visible aspect (`quranic:root_000531:B006/m01`); display for human eyes (`quranic:root_000531:B005/m01`); raised banner (`quranic:root_000531:B011/m01`); outward mark made visible (`quranic:root_000531:B012/m02`); name as designation (`quranic:root_000745:B005/m01`); good reputation carried widely (`quranic:root_000745:B008/m01`); public fame or scandal (`quranic:root_000741:B005/m02`); circulating report (`quranic:root_001272:B007/m02`); fragrance and perfuming (`quranic:root_001002:B004/m01`); bright complexion (`quranic:root_000839:B006/m02`); smile or lightning-flash (`quranic:root_001315:B011/m02`); decorated cloth misreporting its condition (`quranic:root_001290:B009/m02`); low status beneath display (`quranic:root_000493:B003/m02`).
- Ayah anchors: 67:1 `كُلِّ` (ك ل ل); 67:3 `تَرَىٰ/تَرَىٰ` (ر ء ي), `سَمَٰوَٰتٍ` (س م و); 67:5 `زَيَّ` (ز ي ن), `سَّمَآءَ` (س م و), `مَصَٰبِيحَ` (ص ب ح), `دُّنْيَا` (د ن و); 67:7 `سَمِعُ` (س م ع); 67:8 `كُلَّمَآ` (ك ل ل); 67:9 `قَالُ/قُلْ` (ق و ل), `كَذَّبْ` (ك ذ ب); 67:10 `نَسْمَعُ` (س م ع), `قَالُ` (ق و ل); 67:11 `ٱعْتَرَفُ` (ع ر ف); 67:13 `ٱجْهَرُ` (ج ه ر), `قَوْلَ` (ق و ل).
- Synthesis: Recognition is manufactured through face, mirror, mark, banner, name, scent, and ornament, then stabilized or distorted by public report. The decorated cloth is the scene's pressure point: visible enhancement can become a false account of condition. Reputation therefore belongs to the same perceptual economy as adornment but is not identical to beauty.

### 19. P2: Security Is Inverted by Ground and Sky
- Semantic invariant: A seemingly stable enclosure can reverse its protective role: the floor engulfs, the ground oscillates, and the overhead sends abrasive matter downward.
- Surface relation: direct; 67:16-17 `ءَأَمِنتُم`, `يَخْسِفَ بِكُمُ ٱلْأَرْضَ`, `تَمُورُ`, `يُرْسِلَ عَلَيْكُمْ حَاصِبًا`.
- Surprising reach: Security is tested through soft ground, a sunken eye, hunger, humiliating burden, water-rich cloud, dust eddy, rapid mount, hail, fire fuel, and the milk that will not yield butter.

#### Subchannel A. The Trusted Floor Swallows and Oscillates
- Reading type: mixed
- Scene or process: Confidence rests on a floor assumed to hold; that floor softens, takes bodies inward, and moves laterally beneath them.
- Active motifs: settled safety and trust (`quranic:root_000054:B001/m01`); assent that gives inward assurance (`quranic:root_000054:B002/m01`); earth swallowing an object (`quranic:root_000410:B001/m01`); eye sinking into the head (`quranic:root_000410:B003/m01`); bodily depletion through hunger (`quranic:root_000410:B005/m01`); humiliating burden imposed on a person (`quranic:root_000410:B006/m01`); cloud holding abundant water (`quranic:root_000410:B007/m01`); quick, active youth (`quranic:root_000410:B009/m01`); earth as low support (`quranic:root_000025:B001/m03`); clinging heavily to ground (`quranic:root_000025:B006/m02`); bodily tremor named as earth (`quranic:root_000025:B008/m03`); involuntary bodily agitation (`quranic:root_000025:B012/m03`); oscillation and wave motion (`quranic:root_001456:B001/m01`); blood running in a wavering flow (`quranic:root_001456:B002/m01`); dust rotated by wind (`quranic:root_001456:B003/m01`); circling back after descending toward lowland (`quranic:root_001456:B007/m01`); sky as overhead cover (`quranic:root_000745:B004/m04`).
- Ayah anchors: 67:16 `أَمِن` (ء م ن), `يَخْسِفَ` (خ س ف), `أَرْضَ` (ء ر ض), `تَمُورُ` (م و ر), `سَّمَآءِ` (س م و); 67:17 `أَمِن` (ء م ن), `سَّمَآءِ` (س م و); 67:24 `أَرْضِ` (ء ر ض); 67:29 `ءَامَ` (ء م ن).
- Synthesis: Security is located in a relation between body, floor, and overhead. Swallowing removes the floor, while oscillation prevents footing even before engulfment. The sunken eye and hunger make loss of support bodily; the water-rich cloud shows that what is overhead can carry either life or threat. Trust is therefore interrogated as confidence in a support whose behavior one does not control.

#### Subchannel B. A Dispatched Storm Abrades the Surface
- Reading type: mixed
- Scene or process: An overhead sender releases a moving mass of grit or ice that strikes, scatters, and may become either weapon or fuel.
- Active motifs: pebble field and gravel (`quranic:root_000325:B001/m01`); throwing with pebbles (`quranic:root_000325:B002/m01`); violent wind carrying grit or hail (`quranic:root_000325:B003/m01`); material cast into fire as fuel (`quranic:root_000325:B004/m01`); blistering eruption (`quranic:root_000325:B005/m01`); gravelled ritual ground (`quranic:root_000325:B006/m01`); rapid departure across land (`quranic:root_000325:B007/m01`); chilled milk whose butter cannot separate (`quranic:root_000325:B008/m01`); dispatch and release (`quranic:root_000563:B001/m01`); successive groups sent out (`quranic:root_000563:B005/m01`); warning report (`quranic:root_001488:B001/m03`); overhead sky (`quranic:root_000745:B004/m05`); wind-driven dust (`quranic:root_001456:B003/m02`); light matter dispersed as if flying (`quranic:root_000962:B002/m01`).
- Ayah anchors: 67:16 `سَّمَآءِ` (س م و), `تَمُورُ` (م و ر); 67:17 `حَاصِبًا` (ح ص ب), `يُرْسِلَ` (ر س ل), `نَذِيرِ` (ن ذ ر), `سَّمَآءِ` (س م و); 67:19 `طَّيْرِ` (ط ي ر); 67:26 `نَذِيرٌ` (ن ذ ر).
- Synthesis: The storm has a complete dispatch mechanism: matter is released from overhead, wind entrains it, successive particles travel, and the surface receives impact. Pebble, hail, blister, and abrasive field distinguish projectile, weather, bodily effect, and resulting terrain. Chilled unchurnable milk gives the same granulation a domestic pressure point: particulate hardness can also appear as failed separation in a provision system.

### 20. P2: Flight Is a Cycle of Extension, Contraction, and Holding
- Semantic invariant: Stable flight emerges from alternating wing configurations, coordinated alignment, rapid contraction, and a sustaining hold that does not abolish motion.
- Surface relation: direct; 67:19 `ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍ وَيَقْبِضْنَ`, `مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ`, `بِكُلِّ شَىْءٍ بَصِيرٌ`.
- Surprising reach: The bird scene opens into battle ranks, smooth ground, meat laid in rows, a saddle pad, fast gait, a sword grip, a shepherd's gather-release cycle, bodily contraction, and the deathly taking of the soul.

#### Subchannel A. Wings Alternate between Row and Contraction
- Reading type: mixed
- Scene or process: Flying bodies align in an extended plane, contract their moving parts, and repeat that controlled alternation in air.
- Active motifs: light aerial flight (`quranic:root_000962:B001/m01`); dispersal after swift motion (`quranic:root_000962:B002/m02`); wide-open mouth or cavity (`quranic:root_000962:B004/m01`); volatile speed and agitation (`quranic:root_000962:B005/m01`); bird stillness as a sign (`quranic:root_000962:B006/m01`); bodies aligned on one line (`quranic:root_000871:B001/m01`); milk animal aligning limbs (`quranic:root_000871:B002/m01`); meat laid in rows (`quranic:root_000871:B003/m01`); building ledge or saddle pad (`quranic:root_000871:B004/m01`); smooth level ground (`quranic:root_000871:B005/m01`); gathering along water (`quranic:root_000871:B007/m01`); hand closing around an object (`quranic:root_001197:B001/m01`); grip of weapon or tool (`quranic:root_001197:B002/m01`); rapid gait from compact motion (`quranic:root_001197:B004/m01`); shepherd gathering then releasing a flock (`quranic:root_001197:B005/m01`); contraction after extension (`quranic:root_001197:B006/m01`); taking of the soul (`quranic:root_001197:B007/m01`).
- Ayah anchors: 67:19 `طَّيْرِ` (ط ي ر), `صَٰٓفَّٰتٍ` (ص ف ف), `يَقْبِضْ` (ق ب ض).
- Synthesis: The mechanics distinguish extension from support. Alignment supplies a broad lifting configuration; contraction changes that configuration without ending flight; compact movement produces speed; and the shepherd's gather-release image gives the alternation a controlled rhythm. The soul-taking sense marks contraction's terminal limit but is not allowed to define every wingbeat.

#### Subchannel B. Sustaining Hold Preserves Moving Parts
- Reading type: mixed
- Scene or process: An encompassing holder keeps a moving body from falling while preserving its components, relations, and sensory field.
- Active motifs: holding, guarding, and preventing loss (`quranic:root_001424:B001/m01`); remnant that preserves life or reason (`quranic:root_001424:B003/m01`); ground or well stratum that holds water (`quranic:root_001424:B004/m01`); enclosing skin (`quranic:root_001424:B005/m01`); fire banked in earth (`quranic:root_001424:B008/m01`); kinship bond that holds people together (`quranic:root_001424:B009/m01`); membrane holding a newborn (`quranic:root_001424:B010/m01`); legs kept in a marked configuration (`quranic:root_001424:B011/m01`); fighter fixed in an enemy's throat (`quranic:root_001424:B012/m01`); compassion and beneficence (`quranic:root_000552:B001/m01`); sensory sight (`quranic:root_000121:B001/m02`); inward discernment (`quranic:root_000121:B002/m02`); knowable object (`quranic:root_000831:B001/m02`); will directed toward an object (`quranic:root_000831:B002/m01`); totality of components (`quranic:root_001315:B003/m03`); watchful care (`quranic:root_001069:B003/m01`); sufficient guardian (`quranic:root_001681:B006/m01`).
- Ayah anchors: 67:19 `يُمْسِكُ` (م س ك), `رَّحْمَٰنُ` (ر ح م), `بَصِيرٌ` (ب ص ر), `شَىْءٍۭ` (ش ي ء), `كُلِّ` (ك ل ل); 67:20 `رَّحْمَٰنِ` (ر ح م); 67:21 `أَمْسَكَ` (م س ك); 67:23 `أَبْصَٰرَ` (ب ص ر); 67:28 `رَحِمَ` (ر ح م); 67:29 `رَّحْمَٰنُ` (ر ح م), `تَوَكَّلْ` (و ك ل); 67:30 `مَّعِينٍۭ` (ع ي ن).
- Synthesis: Holding is distributed across water-bearing ground, skin, membrane, kinship, banked fire, and bodily configuration, but its invariant is preservation without inert immobilization. The birds continue moving because the sustaining relation keeps parts and medium in order. Sight and guardianship make the hold attentive rather than merely mechanical.

### 21. P2: A False Garrison Substitutes Display for Protection
- Semantic invariant: A human force claims the role of defender, but its apparent strength can be only a bright surface, risky promise, or dependent relation without real capacity to preserve.
- Surface relation: direct; 67:20 `جُندٌ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ`, `فِى غُرُورٍ`.
- Surprising reach: The substitute army includes stony ground, military payroll, rain rescue, remote drainage, heraldic whiteness, market risk, a feed-filled crop, refuge by covenant, and mutual dependence that lets the task fail.

#### Subchannel A. Troop, Reinforcement, and Mobilized Support
- Reading type: mixed
- Scene or process: A gathered force is organized, supplied, and sent to reinforce a threatened party.
- Active motifs: mutually supporting army or party (`quranic:root_000264:B001/m01`); hard stony ground (`quranic:root_000264:B002/m01`); military districts (`quranic:root_000264:B003/m01`); named troop affiliation (`quranic:root_000264:B004/m01`); help that makes one prevail (`quranic:root_001510:B001/m01`); oppressed party taking redress (`quranic:root_001510:B002/m01`); entering a land (`quranic:root_001510:B003/m01`); rain as rescuing reinforcement (`quranic:root_001510:B004/m01`); gift as support (`quranic:root_001510:B005/m01`); confessional affiliation (`quranic:root_001510:B006/m01`); remote drainage reaching a reservoir (`quranic:root_001510:B007/m01`); near but short of the goal (`quranic:root_000502:B001/m01`); inferior rank (`quranic:root_000502:B002/m01`); substitute other than the principal (`quranic:root_000502:B003/m01`); mobilization for war or aid (`quranic:root_001532:B002/m01`); supporting band (`quranic:root_001532:B003/m01`); contest before a judge (`quranic:root_001532:B006/m01`).
- Ayah anchors: 67:20 `جُندٌ` (ج ن د), `يَنصُرُ` (ن ص ر), `دُونِ` (د و ن); 67:21 `نُفُورٍ` (ن ف ر).
- Synthesis: The garrison is a system of bodies, terrain, affiliation, supply, mobilization, and reinforcement. Rain and remote drainage reveal the functional invariant of help: aid must actually reach the threatened site. The "other than" and "short of" senses expose substitution as insufficiency, not merely difference.

#### Subchannel B. Bright Front, Hidden Risk, and Diminishing Return
- Reading type: mixed
- Scene or process: A promising surface attracts confidence while concealing inexperience, uncertain outcome, short measure, and a cutting edge.
- Active motifs: visible crease left by folding (`quranic:root_001078:B001/m01`); repeated template or track (`quranic:root_001078:B002/m01`); white blaze on a forehead (`quranic:root_001078:B003/m01`); finest or leading member (`quranic:root_001078:B004/m01`); first beginning (`quranic:root_001078:B005/m01`); inexperienced and unsuspecting person (`quranic:root_001078:B007/m01`); deceptive glitter (`quranic:root_001078:B008/m01`); exposure to unknown outcome (`quranic:root_001078:B009/m01`); deficient milk, sleep, or market (`quranic:root_001078:B010/m01`); feeding a chick or filling a skin (`quranic:root_001078:B011/m01`); blade edge (`quranic:root_001078:B012/m01`); carried sack (`quranic:root_001078:B013/m01`); concealment of truth (`quranic:root_001307:B003/m02`); refusal to acknowledge provision (`quranic:root_001307:B004/m01`).
- Ayah anchors: 67:20 `غُرُورٍ` (غ ر ر), `كَٰفِرُونَ` (ك ف ر); 67:27 `كَفَرُ` (ك ف ر); 67:28 `كَٰفِرِينَ` (ك ف ر).
- Synthesis: Deception works by converting a visible mark of excellence into confidence about what cannot yet be known. The same surface can hide a deficient return, dangerous edge, or empty market. Feeding and filling show how confidence is maintained: the deceptive system keeps supplying appearances until the concealed risk matures.

#### Subchannel C. Refuge Requires a Valid Protector
- Reading type: mixed
- Scene or process: A vulnerable party seeks proximity, covenant, and rescue from a protector with actual power to intervene.
- Active motifs: deviation from justice (`quranic:root_000275:B001/m01`); neighboring proximity (`quranic:root_000275:B002/m01`); asylum under a guarantee (`quranic:root_000275:B003/m01`); cultivator in a protected garden (`quranic:root_000275:B005/m01`); strike that knocks down (`quranic:root_000275:B006/m01`); inward heat of grief or anger (`quranic:root_000275:B010/m01`); sanctuary status of protected person or captive (`quranic:root_001583:B007/m01`); sufficient keeper (`quranic:root_001681:B006/m02`); redress from oppression (`quranic:root_001510:B002/m02`); genuine safety (`quranic:root_000054:B001/m02`); merciful beneficence (`quranic:root_000552:B001/m02`); mutual reliance that lets an affair be lost (`quranic:root_001681:B004/m01`).
- Ayah anchors: 67:16 `أَمِن` (ء م ن); 67:17 `أَمِن` (ء م ن); 67:19 `رَّحْمَٰنُ` (ر ح م); 67:20 `يَنصُرُ` (ن ص ر), `رَّحْمَٰنِ` (ر ح م); 67:22 `أَهْدَىٰٓ` (ه د ي); 67:28 `يُجِيرُ` (ج و ر), `رَحِمَ` (ر ح م); 67:29 `تَوَكَّلْ` (و ك ل), `ءَامَ` (ء م ن), `رَّحْمَٰنُ` (ر ح م).
- Synthesis: Refuge is a three-party relation: threatened person, aggressor, and recognized protector. Neighboring and garden cultivation show protected proximity; asylum and captive status formalize it; knockdown and redress reveal the violence to be prevented. Mutual reliance without an effective keeper is the failed version of the same structure.

### 22. P2: Provision Depends on Release, Retention, and Conversion
- Semantic invariant: Provision moves only when a giver releases an allotted resource and a receiving system holds it long enough to convert it into food, growth, or strength.
- Surface relation: direct; 67:21 `يَرْزُقُكُمْ`, `إِنْ أَمْسَكَ رِزْقَهُ`; 67:23 `قَلِيلًا مَّا تَشْكُرُونَ`; 67:30 `مَآؤُكُمْ`, `بِمَآءٍ مَّعِينٍ`.
- Surprising reach: Withholding opens into military payroll, wet leather, healing, capture, speech articulation, milk, rain, new shoots, and the small remnant that keeps a body alive.

#### Subchannel A. Allotment Is Held, Spent, or Withheld
- Reading type: mixed
- Scene or process: A resource is apportioned, possessed, retained, and either released for use or stopped at the holder.
- Active motifs: allotted gift and benefit (`quranic:root_000560:B001/m02`); food entering the body (`quranic:root_000560:B002/m03`); rainfall as provision (`quranic:root_000560:B003/m02`); military pay (`quranic:root_000560:B004/m02`); favorable allotment (`quranic:root_000560:B006/m03`); white linen or named grape (`quranic:root_000560:B007/m01`); general retention and prevention (`quranic:root_001424:B001/m02`); miserly retention of wealth (`quranic:root_001424:B002/m01`); remnant preserving life or reason (`quranic:root_001424:B003/m02`); water-holding stratum (`quranic:root_001424:B004/m02`); containing skin (`quranic:root_001424:B005/m02`); banked fire (`quranic:root_001424:B008/m02`); kinship bond (`quranic:root_001424:B009/m02`); possession achieved by taking hold (`quranic:root_000152:B004/m01`); material due presented for taking (`quranic:root_001573:B001/m01`).
- Ayah anchors: 67:19 `يُمْسِكُ` (م س ك); 67:21 `يَرْزُقُ/رِزْقَ` (ر ز ق), `أَمْسَكَ` (م س ك); surface anchors unavailable for `ب ل ل`, `ه ا ء` (missing root coverage).
- Synthesis: Provision is not identified with unrestricted flow. It must be allotted, held against waste, and released against need. Miserliness is a failed holding operation, while skin, soil, and banked fire show constructive retention. The presentation motif supplies the final transfer from holder to recipient.

#### Subchannel B. Moisture Converts into Health, Milk, and New Growth
- Reading type: latent/lexical
- Scene or process: Moisture enters body, soil, or vessel and becomes healing, kinship benefit, milk, tender growth, and grateful increase.
- Active motifs: wetness and dew (`quranic:root_000152:B001/m01`); moisture as benefaction and kin support (`quranic:root_000152:B002/m01`); recovery after wasting (`quranic:root_000152:B003/m01`); folding while moisture remains (`quranic:root_000152:B007/m02`); water-like moan or bird sound (`quranic:root_000152:B010/m01`); little feed producing visible increase (`quranic:root_000810:B002/m01`); udder filling with milk (`quranic:root_000810:B003/m01`); tender shoot emerging (`quranic:root_000810:B004/m01`); rain, wind, heat, or cold intensifying (`quranic:root_000810:B005/m01`); recurring milk flow (`quranic:root_000563:B006/m01`); rain rescuing land (`quranic:root_001510:B004/m03`); distant channel feeding a basin (`quranic:root_001510:B007/m02`); chilled milk refusing butter (`quranic:root_000325:B008/m02`); sowing seed (`quranic:root_000510:B003/m01`); water-bearing cloud (`quranic:root_000410:B007/m02`).
- Ayah anchors: 67:16 `يَخْسِفَ` (خ س ف); 67:17 `يُرْسِلَ` (ر س ل), `حَاصِبًا` (ح ص ب); 67:20 `يَنصُرُ` (ن ص ر); 67:23 `تَشْكُرُ` (ش ك ر); 67:24 `ذَرَأَ` (ذ ر ء); surface anchors unavailable for `ب ل ل` (missing root coverage).
- Synthesis: Moisture is followed through conversion rather than treated as a topic. It heals a wasted body, supports kin, fills an udder, germinates a shoot, and rescues land through rain or channel. Failed butter separation and over-intensified weather identify two places where moisture can cease to be usable provision.

### 23. P2: Obstinacy Behaves like a Churning Medium
- Semantic invariant: Persistent refusal is motion without progress: speech, appetite, heart, crowd, or traveler churns within a medium while recoiling from the offered direction.
- Surface relation: direct; 67:21 `لَّجُّوا۟ فِى عُتُوٍّ وَنُفُورٍ`; 67:26 `ٱلْعِلْمُ عِندَ ٱللَّهِ`; 67:29 `ضَلَٰلٍ مُّبِينٍ`.
- Surprising reach: Moral obstinacy takes the forms of rough sea, repeated mouth movement, mixed voices, hunger-palpitations, black night, swollen skin, boastful litigation, and a tongue that can articulate yet refuses correction.

#### Subchannel A. Churning without Exit
- Reading type: mixed
- Scene or process: A participant remains inside an agitated medium, repeating movement or speech without crossing to a new state.
- Active motifs: persistence in dispute or oath (`quranic:root_001344:B001/m01`); deep agitated sea (`quranic:root_001344:B002/m01`); sword named for the sea's flash (`quranic:root_001344:B003/m01`); speech or food repeatedly turned in the mouth (`quranic:root_001344:B004/m01`); crowd noise and mixed voices (`quranic:root_001344:B005/m01`); hungry heart palpitating (`quranic:root_001344:B006/m01`); intermingled darkness (`quranic:root_001344:B007/m01`); rushing to claim property (`quranic:root_001344:B008/m01`); crowd like a sea (`quranic:root_001344:B009/m01`); side of valley or breadth of sea (`quranic:root_001344:B010/m01`); arrogance that exceeds obedience (`quranic:root_000981:B001/m01`); senescent state beyond repair (`quranic:root_000981:B002/m01`); oscillating ground (`quranic:root_001456:B001/m02`).
- Ayah anchors: 67:16 `تَمُورُ` (م و ر); 67:21 `لَّجُّ` (ل ج ج), `عُتُوٍّ` (ع ت و).
- Synthesis: The core operation is recurrent motion trapped inside its own medium. The sea, mouth, crowd, heart, and dark all agitate, but none reaches a stable destination. Arrogance names the social-moral form of that churning; senescence beyond repair gives its persistence a terminal pressure.

#### Subchannel B. Recoil, Swelling, and Refusal of Alignment
- Reading type: mixed
- Scene or process: A body or group recoils from a call, swells away from its proper place, and converts refusal into rivalry or estrangement.
- Active motifs: recoiling and distancing from a thing (`quranic:root_001532:B001/m01`); mobilizing at a call (`quranic:root_001532:B002/m02`); band that rises to support (`quranic:root_001532:B003/m02`); skin or wound swelling away from its bed (`quranic:root_001532:B005/m01`); rivalrous adjudication (`quranic:root_001532:B006/m02`); protective naming intended to repel harm (`quranic:root_001532:B007/m01`); acting before any caller can rise (`quranic:root_001532:B008/m01`); fierce disputant and obstruction (`quranic:root_000152:B005/m01`); articulate tongue (`quranic:root_000152:B006/m01`); adversative break in discourse (`quranic:root_000152:B008/m01`); mental and vocal confusion (`quranic:root_000152:B009/m01`); inward heart-heat (`quranic:root_001122:B002/m01`); tremor from fear or anger (`quranic:root_001251:B005/m01`); willful deviation despite knowledge (`quranic:root_001052:B001/m01`).
- Ayah anchors: 67:21 `نُفُورٍ` (ن ف ر); 67:23 `أَفْـِٔدَةَ` (ف ء د), `قَلِيلًا` (ق ل ل); 67:26 `عِندَ` (ع ن د); surface anchors unavailable for `ب ل ل` (missing root coverage).
- Synthesis: Refusal is expressed as spatial detachment: skin lifts from tissue, a group recoils from a summons, and a disputant blocks approach. Articulation and the discourse break show that inability to speak is not the cause; the tongue can form words while the will turns the exchange aside. Mobilization and support provide the role reversal of what the same energy could have done.

### 24. P2: Two Gaits Materialize Two Moral Orientations
- Semantic invariant: Direction becomes bodily truth through posture, balance, contact with the ground, and relation to a marked path.
- Surface relation: direct; 67:22 `يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِ` versus `يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ`.
- Surprising reach: The contrast recruits overturned vessels, bodies tumbling into a pit, compressed cavalry, swallowed food, a cutting sword, saddle pads, moon balance, market value, route leadership, bridal procession, and the weak person walking between supports.

#### Subchannel A. Face-Down Motion Loses Forward Perception
- Reading type: mixed
- Scene or process: A body is overturned onto its front, clings to what lies immediately beneath it, and moves without an open field of view.
- Active motifs: intentional walking (`quranic:root_001427:B001/m02`); gossip carried by a walker (`quranic:root_001427:B004/m01`); an influence spreading internally (`quranic:root_001427:B005/m01`); object or person overturned onto its face (`quranic:root_001278:B001/m01`); stooping and clinging to a task (`quranic:root_001278:B002/m01`); bodies rolled and cast into a pit (`quranic:root_001278:B003/m01`); compact tangled mass (`quranic:root_001278:B004/m01`); rushing shock or charge (`quranic:root_001278:B005/m01`); face and frontal surface (`quranic:root_001630:B001/m01`); direction and intended course (`quranic:root_001630:B002/m01`); face-to-face encounter (`quranic:root_001630:B003/m01`); correctness of an affair's "face" (`quranic:root_001630:B008/m01`); blow to the face (`quranic:root_001630:B013/m01`); being turned back (`quranic:root_001630:B014/m01`); two-faced discrepancy (`quranic:root_001630:B015/m01`); deviation from guidance (`quranic:root_000913:B001/m03`); hidden or lost object (`quranic:root_000913:B002/m02`); stray animal (`quranic:root_000913:B005/m01`).
- Ayah anchors: 67:22 `يَمْشِى/يَمْشِى` (م ش ي), `مُكِبًّا` (ك ب ب), `وَجْهِ` (و ج ه); 67:27 `وُجُوهُ` (و ج ه); 67:29 `ضَلَٰلٍ` (ض ل ل).
- Synthesis: Face-down motion is a mechanical loss of orientation. Overturning redirects the front toward the ground, compression restricts movement, and clinging converts purposeful advance into fixation. Gossip and two-facedness extend the posture socially: speech moves while the speaker's true direction remains concealed.

#### Subchannel B. Uprightness Aligns Body, Measure, and Road
- Reading type: mixed
- Scene or process: A body stands in balanced proportion and advances on a route whose surface, measure, and direction agree.
- Active motifs: equality between two measures (`quranic:root_000766:B001/m01`); bodily straightness after crookedness (`quranic:root_000766:B002/m01`); stable mounting (`quranic:root_000766:B003/m01`); turning deliberately toward a direction (`quranic:root_000766:B004/m01`); completed bodily maturity (`quranic:root_000766:B005/m01`); fair middle and level place (`quranic:root_000766:B006/m01`); broad smooth ground (`quranic:root_000766:B009/m01`); saddle cloth that balances a rider (`quranic:root_000766:B010/m01`); full moon at balance (`quranic:root_000766:B012/m01`); amount equal to one's head in wealth (`quranic:root_000766:B013/m01`); straight road (`quranic:root_000858:B001/m01`); passage by swallowing (`quranic:root_000858:B002/m01`); cutting sword passing cleanly (`quranic:root_000858:B003/m01`); standing body (`quranic:root_001273:B002/m01`); straightness and rectitude (`quranic:root_001273:B008/m01`); bodily stature (`quranic:root_001273:B011/m01`); equal weight (`quranic:root_001273:B015/m01`); arrested movement as the contrast (`quranic:root_001273:B016/m01`); blind eye remaining physically intact (`quranic:root_001273:B021/m01`).
- Ayah anchors: 67:22 `سَوِيًّا` (س و ي), `صِرَٰطٍ` (ص ر ط), `مُّسْتَقِيمٍ` (ق و م).
- Synthesis: Upright travel coordinates proportion, support, and destination. Balanced saddle, level ground, equal weight, mature stature, and rectitude all keep force centered over the route. The swallowed passage and cutting sword supply functional analogies of unobstructed transit. The intact but blind eye warns that correct outward form alone is insufficient if perception is absent.

#### Subchannel C. Guidance Places a Leader before the Route
- Reading type: mixed
- Scene or process: A guide identifies direction, goes first, and enables others, including the weak or burdened, to move with composure.
- Active motifs: gentle indication toward road and truth (`quranic:root_001583:B001/m01`); direction and manner of proceeding (`quranic:root_001583:B002/m01`); leader at the head of a moving group (`quranic:root_001583:B003/m01`); gift sent toward a beloved (`quranic:root_001583:B004/m01`); offering conducted to sanctuary (`quranic:root_001583:B005/m01`); bride conducted to spouse (`quranic:root_001583:B006/m01`); weak person walking between supports (`quranic:root_001583:B008/m01`); slow, weak follower (`quranic:root_001583:B009/m01`); calm and composed gait (`quranic:root_001583:B010/m01`); poetic address sent to a person (`quranic:root_001583:B011/m01`); rising with resolve (`quranic:root_001273:B003/m01`); stewardship and maintenance (`quranic:root_001273:B004/m01`); standing in another's place (`quranic:root_001273:B007/m01`); life-supporting mainstay (`quranic:root_001273:B009/m01`); structural upright piece (`quranic:root_001273:B012/m01`); resurrection standing (`quranic:root_001273:B013/m01`); resistance and contest (`quranic:root_001273:B014/m01`); thriving market (`quranic:root_001273:B018/m01`); bodily pain that prevents standing (`quranic:root_001273:B019/m01`); leg disease that forces standing (`quranic:root_001273:B020/m01`).
- Ayah anchors: 67:22 `أَهْدَىٰٓ` (ه د ي), `مُّسْتَقِيمٍ` (ق و م).
- Synthesis: Guidance is not only a sign; it is a relational locomotion system. A leader takes the front, a gift or bride is conducted toward a recognized recipient, supports enable a weak walker, and composure preserves direction. Stewardship and mainstay motifs show how guidance continues after the first indication by maintaining the conditions of movement.

### 25. P2: The Sensorium Is an Entrusted Instrument Panel
- Semantic invariant: Hearing, sight, and heart are created interfaces that must receive, distinguish, and convert signals into acknowledgment.
- Surface relation: direct; 67:19 `يَرَوْا`, `بَصِيرٌ`; 67:23 `أَنشَأَكُمْ`, `ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ`, `قَلِيلًا مَّا تَشْكُرُونَ`.
- Surprising reach: The endowed organs extend into ear canal, bucket handle, plow yoke, brain, shield, blood trace, bright stone, furnace-heart, struck heart, weak courage, tender shoot, milk-filled udder, and a large jar.

#### Subchannel A. Created Interfaces Receive and Process Signals
- Reading type: mixed
- Scene or process: A created body is fitted with auditory, visual, and inward-processing organs that convert external signal into understood condition.
- Active motifs: elevation and emergence (`quranic:root_001502:B001/m01`); youth growing under nurture (`quranic:root_001502:B002/m01`); initiating speech or action (`quranic:root_001502:B004/m01`); created existence joined to upbringing (`quranic:root_001502:B006/m01`); first structural stones of a basin (`quranic:root_001502:B007/m01`); rising and moving toward a need (`quranic:root_001502:B008/m01`); conception beginning (`quranic:root_001502:B009/m01`); making and assigning function (`quranic:root_000248:B001/m02`); transforming into a specified state (`quranic:root_000248:B002/m03`); auditory reception (`quranic:root_000741:B001/m02`); ear and auditory canal (`quranic:root_000741:B002/m02`); understood obedience (`quranic:root_000741:B003/m02`); bucket handle that balances drawing (`quranic:root_000741:B008/m02`); brain behind hearing (`quranic:root_000741:B016/m03`); sensory vision (`quranic:root_000121:B001/m03`); inward insight (`quranic:root_000121:B002/m03`); joined sensory edge (`quranic:root_000121:B006/m03`); heart as inward heat and awareness (`quranic:root_001122:B002/m02`).
- Ayah anchors: 67:19 `بَصِيرٌ` (ب ص ر); 67:23 `أَنشَأَ` (ن ش ء), `جَعَلَ` (ج ع ل), `سَّمْعَ` (س م ع), `أَبْصَٰرَ` (ب ص ر), `أَفْـِٔدَةَ` (ف ء د).
- Synthesis: The organs form a signal path: ear admits sound, brain and heart process it, and sight tests external configuration. Handles and basin foundations are functional analogies, not decoration: an interface balances incoming load and a foundation determines what the later structure can hold. Creation includes both origination and the assignment of these roles.

#### Subchannel B. The Heart Can Heat, Fail, or Be Struck
- Reading type: latent/lexical
- Scene or process: The inward organ carries heat and courage, suffers direct injury or disease, and may become too weak to perform judgment.
- Active motifs: furnace heat that roasts and bakes (`quranic:root_001122:B001/m01`); heart understood through internal burning (`quranic:root_001122:B002/m03`); strike or disease reaching the heart (`quranic:root_001122:B003/m01`); weak or absent courage (`quranic:root_001122:B004/m01`); dull, water-heavy heart (`quranic:root_001458:B008/m01`); hungry heart palpitating (`quranic:root_001344:B006/m02`); small remnant of reason preserving its owner (`quranic:root_001424:B003/m03`).
- Ayah anchors: 67:19 `يُمْسِكُ` (م س ك); 67:21 `لَّجُّ` (ل ج ج), `أَمْسَكَ` (م س ك); 67:23 `أَفْـِٔدَةَ` (ف ء د); 67:30 `مَآؤُ/مَآءٍ` (م و ه).
- Synthesis: The heart is a heated central processor whose failures are materially distinct: overheating, hunger-palpitations, direct strike, disease, cognitive dullness, and depleted courage. The small remaining measure of reason shows how little capacity may still keep the whole person from collapse.

#### Subchannel C. Scarcity and Gratitude Measure Response
- Reading type: mixed
- Scene or process: A small input produces an observable response; gratitude recognizes the source, while scarcity, trembling, or failure to increase exposes poor reception.
- Active motifs: small quantity and rarity (`quranic:root_001251:B001/m01`); summit or head (`quranic:root_001251:B002/m01`); large storage jar (`quranic:root_001251:B003/m01`); carrying and rising under a load (`quranic:root_001251:B004/m01`); tremor of fear or anger (`quranic:root_001251:B005/m02`); recognition and praise of benefaction (`quranic:root_000810:B001/m01`); small feed visibly increasing an animal (`quranic:root_000810:B002/m02`); milk-filled udder (`quranic:root_000810:B003/m02`); tender shoot and new growth (`quranic:root_000810:B004/m02`); intensified weather response (`quranic:root_000810:B005/m02`); sexual euphemism (`quranic:root_000810:B006/m01`); named tribal affiliations (`quranic:root_000810:B007/m01`); the small amount used almost as negation (`quranic:root_001251:B001/m02`).
- Ayah anchors: 67:23 `قَلِيلًا` (ق ل ل), `تَشْكُرُ` (ش ك ر).
- Synthesis: Gratitude is modeled by visible response to a small gift, like an animal thriving on little feed or a shoot emerging after slight rain. Jar, carrying, and rising distinguish capacity from acknowledgment: one may hold or bear much and still respond little. Trembling supplies the bodily sign of an input that overwhelms instead of nourishing.

### 26. P2: Scattering Is Answered by Muster
- Semantic invariant: Created individuals are sown and dispersed across earth, then regrouped, driven, or assembled toward a common destination.
- Surface relation: direct; 67:24 `ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ`; supported by 67:19 aligned birds and 67:20 the gathered troop.
- Surprising reach: Human distribution is reframed through seed, first growth, white flecks, social provocation, a barrier between people, insects, harvest stubble, a fine arrow, and a famine that drives populations into cities.

#### Subchannel A. Seed, Proliferation, and Dispersal across Ground
- Reading type: mixed
- Scene or process: Distinct lives are generated, multiplied like seed, placed through a terrain, and sometimes separated by barriers or conflict.
- Active motifs: bringing created individuals into being and multiplying them (`quranic:root_000510:B001/m01`); sowing seed and first shoot (`quranic:root_000510:B003/m02`); white flecking like salt or gray hair (`quranic:root_000510:B004/m01`); provoking one person against another (`quranic:root_000510:B005/m01`); barrier between two parties (`quranic:root_000510:B006/m01`); small unfinished fragment of speech (`quranic:root_000510:B007/m01`); fertile earth that receives seed (`quranic:root_000025:B002/m02`); grain-covering cultivator (`quranic:root_001307:B008/m01`); sheath around fruit (`quranic:root_001307:B010/m02`); tender new shoot (`quranic:root_000810:B004/m03`); light matter spreading like flight (`quranic:root_000962:B002/m03`); successive dispatched groups (`quranic:root_000563:B005/m02`); recoil and separation (`quranic:root_001532:B001/m02`).
- Ayah anchors: 67:16 `أَرْضَ` (ء ر ض); 67:17 `يُرْسِلَ` (ر س ل); 67:19 `طَّيْرِ` (ط ي ر); 67:20 `كَٰفِرُونَ` (ك ف ر); 67:21 `نُفُورٍ` (ن ف ر); 67:23 `تَشْكُرُ` (ش ك ر); 67:24 `ذَرَأَ` (ذ ر ء), `أَرْضِ` (ء ر ض); 67:27 `كَفَرُ` (ك ف ر); 67:28 `كَٰفِرِينَ` (ك ف ر).
- Synthesis: Scattering begins as productive multiplication but can become estrangement. Seed is covered, a first shoot emerges, and distinct individuals spread through receptive earth; barriers and provocation then show how separateness can harden into conflict. The unfinished speech fragment gives dispersion a discourse analogue: a part is released before the whole relation is formed.

#### Subchannel B. Driven Groups Converge on One Destination
- Reading type: mixed
- Scene or process: Dispersed participants are collected, driven from separate locations, and compacted into an ordered or pressured assembly.
- Active motifs: gathering while driving toward a goal (`quranic:root_000324:B001/m01`); famine driving people together and stripping property (`quranic:root_000324:B002/m01`); multiplying small ground creatures (`quranic:root_000324:B004/m01`); tightly packed body or swollen flank (`quranic:root_000324:B005/m01`); fine sharp point or swift arrow (`quranic:root_000324:B006/m01`); inner husk of a grain (`quranic:root_000324:B007/m01`); crop residue after harvest (`quranic:root_000324:B008/m01`); supporting army (`quranic:root_000264:B001/m02`); aligned row (`quranic:root_000871:B001/m02`); assembly along water (`quranic:root_000871:B007/m02`); supporting band (`quranic:root_001532:B003/m03`); people constituted as a group (`quranic:root_001273:B001/m01`); gathering place and time (`quranic:root_001273:B006/m01`); standing at resurrection (`quranic:root_001273:B013/m02`); all parts enclosed (`quranic:root_001315:B003/m04`).
- Ayah anchors: 67:19 `صَٰٓفَّٰتٍ` (ص ف ف), `كُلِّ` (ك ل ل); 67:20 `جُندٌ` (ج ن د); 67:21 `نُفُورٍ` (ن ف ر); 67:22 `مُّسْتَقِيمٍ` (ق و م); 67:24 `تُحْشَرُ` (ح ش ر).
- Synthesis: Muster is not bare plurality. It includes a driver, destination, changing density, and internal order. Famine, army, water gathering, packed body, and resurrection assembly supply different causes for convergence. Grain husk and harvest residue pressure the human scene by showing what remains around or after the collected yield.

### 27. P2: The Promise Is a Scheduled Claim before Located Knowledge
- Semantic invariant: A future claim acquires force through truthful commitment and a specified appointment, while its timing remains located with the one who knows.
- Surface relation: direct; 67:25-26 `مَتَىٰ هَٰذَا ٱلْوَعْدُ`, `إِن كُنتُمْ صَٰدِقِينَ`, `إِنَّمَا ٱلْعِلْمُ عِندَ ٱللَّهِ`, `نَذِيرٌ مُّبِينٌ`.
- Surprising reach: Promise becomes mutual contract, threatening stallion, weather sign, dowry, friendship, alms, hard spear, present location, lateral deviation, water-rich well, and the visible cleft that marks an upper lip.

#### Subchannel A. Commitment, Appointment, and Verification
- Reading type: mixed
- Scene or process: A speaker opens expectation, fixes or withholds an appointment, and becomes accountable for whether word and event correspond.
- Active motifs: promise that opens expectation (`quranic:root_001662:B001/m01`); threat directed toward harm (`quranic:root_001662:B002/m01`); appointed time or place (`quranic:root_001662:B003/m01`); mutual promising (`quranic:root_001662:B004/m01`); stallion's warning bellow before attack (`quranic:root_001662:B005/m01`); sign that forecasts coming conditions (`quranic:root_001662:B006/m01`); truthful correspondence of report and reality (`quranic:root_000852:B001/m01`); hard, straight implement (`quranic:root_000852:B002/m01`); complete and dependable condition (`quranic:root_000852:B003/m01`); making a promise or vision come true (`quranic:root_000852:B004/m01`); sincere friendship (`quranic:root_000852:B005/m01`); truthful redistribution of wealth (`quranic:root_000852:B006/m01`); marriage payment (`quranic:root_000852:B007/m01`); occurrence in time (`quranic:root_001332:B001/m01`); place and status (`quranic:root_001332:B002/m01`); bad resulting condition (`quranic:root_001332:B006/m01`).
- Ayah anchors: 67:18 `كَانَ` (ك و ن); 67:25 `وَعْدُ` (و ع د), `صَٰدِقِينَ` (ص د ق), `كُن` (ك و ن); 67:27 `كُن` (ك و ن).
- Synthesis: Promise is a temporal contract. Expectation is opened, an appointment can be specified, and fulfillment tests the correspondence of speech and event. The forecasting sign and stallion's bellow show that a future occurrence may be announced before its exact moment is possessed by the hearer. Friendship, alms, and dowry distinguish social commitments carried by the same truth relation.

#### Subchannel B. Knowledge Has a Place, Mark, and Responsible Holder
- Reading type: mixed
- Scene or process: Information is situated with a knower, disclosed by signs and clear speech, and guarded from willful distortion.
- Active motifs: knowledge that discloses (`quranic:root_001040:B001/m02`); sign, banner, or landmark (`quranic:root_001040:B002/m02`); upper-lip cleft as visible mark (`quranic:root_001040:B004/m03`); abundant water gathered in sea or well (`quranic:root_001040:B005/m03`); named hunting bird (`quranic:root_001040:B006/m01`); male hyena (`quranic:root_001040:B007/m01`); willful opposition to known truth (`quranic:root_001052:B001/m02`); lateral departure from group or route (`quranic:root_001052:B002/m01`); flow that runs off to one side (`quranic:root_001052:B003/m01`); nearness and presence at a place (`quranic:root_001052:B004/m01`); no available alternative (`quranic:root_001052:B005/m01`); command to take what is present (`quranic:root_001052:B006/m01`); warning that carries danger knowledge (`quranic:root_001488:B001/m04`); obligatory vow (`quranic:root_001488:B002/m02`); assessed wound liability (`quranic:root_001488:B003/m02`).
- Ayah anchors: 67:17 `تَعْلَمُ` (ع ل م), `نَذِيرِ` (ن ذ ر); 67:26 `عِلْمُ` (ع ل م), `عِندَ` (ع ن د), `نَذِيرٌ` (ن ذ ر); 67:29 `تَعْلَمُ` (ع ل م).
- Synthesis: Knowledge is located rather than diffused. A holder possesses it, a mark or landmark makes part of it public, and warning transmits the portion needed for action. Side-running flow and lateral departure model the failure of willfully leaving what one knows. The water-rich well gives hidden abundance a concrete location even when the surface reveals little.

#### Subchannel C. Clarity Separates, Connects, and Interprets
- Reading type: mixed
- Scene or process: Clear communication distinguishes one thing from another while preserving the relation needed to convey meaning.
- Active motifs: separation after contact (`quranic:root_000170:B001/m01`); interval between parties (`quranic:root_000170:B002/m01`); connection holding parties together (`quranic:root_000170:B003/m01`); visible disclosure and proof (`quranic:root_000170:B004/m01`); linguistic or gestural explanation (`quranic:root_000170:B005/m01`); deep or wide distance (`quranic:root_000170:B006/m01`); tract of land within sight (`quranic:root_000170:B007/m01`); limb or string separating from its body (`quranic:root_000170:B008/m01`); position on one side of a milking animal (`quranic:root_000170:B009/m01`); time interval during an event (`quranic:root_000170:B010/m01`); intermediate quality (`quranic:root_000170:B011/m01`); irrevocable separation (`quranic:root_000170:B012/m01`); utterance as explicit statement (`quranic:root_001272:B001/m03`); logical definition (`quranic:root_001272:B016/m01`).
- Ayah anchors: 67:23 `قُلْ` (ق و ل); 67:24 `قُلْ` (ق و ل); 67:25 `يَقُولُ` (ق و ل); 67:26 `مُّبِينٌ` (ب ي ن), `قُلْ` (ق و ل); 67:27 `قِيلَ` (ق و ل); 67:28 `قُلْ` (ق و ل); 67:29 `مُّبِينٍ` (ب ي ن), `قُلْ` (ق و ل); 67:30 `قُلْ` (ق و ل).
- Synthesis: Clarity does two jobs that must not be collapsed. It separates objects or claims enough to distinguish them, yet also establishes the connecting relation by which meaning crosses an interval. Milking position, detached limb, time interval, and land within sight materialize distinct kinds of "between." Definition and explanation convert those separations into communicable knowledge.

### 28. P2: The Distant Claim Enters the Visual Field and Alters the Face
- Semantic invariant: A denied or demanded event moves from remote speech into perceptible nearness, where recognition registers bodily on the claimant's face.
- Surface relation: direct; 67:25 `مَتَىٰ هَٰذَا ٱلْوَعْدُ`; 67:27 `رَأَوْهُ زُلْفَةً`, `سِيٓـَٔتْ وُجُوهُ`, `هَٰذَا ٱلَّذِى كُنتُم بِهِ تَدَّعُونَ`.
- Surprising reach: Nearness is rendered as filled bowls, villages between desert and cultivated land, added detail in a story, mirrors, banners, pregnancy signs, visible lung, ritual direction, birth presentation, poetic meter, plant trenches, and the collapse of a building one part after another.

#### Subchannel A. Approach Changes a Claim into an Encounter
- Reading type: mixed
- Scene or process: What had been spoken of at a distance advances, enters mutual visibility, and occupies a near, socially consequential position.
- Active motifs: movement into nearness (`quranic:root_000639:B001/m01`); favored proximity and rank (`quranic:root_000639:B002/m01`); near portions of night (`quranic:root_000639:B003/m01`); full bowls or overflowing basins (`quranic:root_000639:B004/m01`); settlements between desert and cultivated land (`quranic:root_000639:B005/m01`); adding to a report (`quranic:root_000639:B006/m01`); woman's face (`quranic:root_000639:B007/m01`); sensory seeing (`quranic:root_000531:B001/m02`); reflective judgment (`quranic:root_000531:B002/m02`); dream image (`quranic:root_000531:B003/m01`); mutual visibility (`quranic:root_000531:B004/m01`); mirror and aspect (`quranic:root_000531:B006/m02`); visible pregnancy (`quranic:root_000531:B010/m02`); raised banner (`quranic:root_000531:B011/m02`); making another see (`quranic:root_000531:B012/m03`); interrogative alert "tell me" (`quranic:root_000531:B013/m01`); facing or meeting (`quranic:root_001198:B001/m01`); temporal and spatial precedence (`quranic:root_001198:B002/m01`); source or side from which something comes (`quranic:root_001198:B003/m01`).
- Ayah anchors: 67:18 `قَبْلِ` (ق ب ل); 67:19 `يَرَ` (ر ء ي); 67:27 `زُلْفَةً` (ز ل ف), `رَأَ` (ر ء ي); 67:28 `رَءَيْ` (ر ء ي); 67:30 `رَءَيْ` (ر ء ي).
- Synthesis: Approach is resolved into distance, visible entry, and encounter. Night portions, intermediate settlements, and full basins mark progressive nearness; mutual visibility and the alert formula establish recognition. Added narration supplies the discourse version of bringing an event closer by filling in what was previously remote.

#### Subchannel B. The Face Registers Injury, Status, and Reversal
- Reading type: mixed
- Scene or process: Recognition strikes the frontal surface, changing its appearance and exposing social and inward condition.
- Active motifs: ugly or bad condition (`quranic:root_000755:B001/m01`); distressing event (`quranic:root_000755:B002/m01`); visible disease or blemish (`quranic:root_000755:B003/m01`); concealed shame (`quranic:root_000755:B004/m01`); reproach for a bad act (`quranic:root_000755:B005/m01`); condemning formula (`quranic:root_000755:B006/m01`); frontal surface (`quranic:root_001630:B001/m02`); direction (`quranic:root_001630:B002/m02`); face-to-face encounter (`quranic:root_001630:B003/m02`); social prominence (`quranic:root_001630:B006/m01`); first face of the day (`quranic:root_001630:B007/m01`); correct aspect of an affair (`quranic:root_001630:B008/m02`); aging face and life-direction (`quranic:root_001630:B009/m01`); newborn presenting hands first (`quranic:root_001630:B010/m01`); poetic boundary near rhyme (`quranic:root_001630:B011/m01`); plant laid into a trench (`quranic:root_001630:B012/m01`); blow to the face (`quranic:root_001630:B013/m02`); outward double face (`quranic:root_001630:B015/m02`).
- Ayah anchors: 67:22 `وَجْهِ` (و ج ه); 67:27 `سِيٓـَٔتْ` (س و ء), `وُجُوهُ` (و ج ه).
- Synthesis: The face is at once body surface, direction, social rank, and visible report of inward change. Blemish, shame, reproach, blow, and double face distinguish several ways appearance can be morally or physically altered. Birth presentation and plant trench preserve the spatial invariant of a front entering a receiving opening, but remain subordinate to the recognition scene.

#### Subchannel C. Calling for an Event Can Become Its Own Collapse
- Reading type: mixed
- Scene or process: A claimant calls, attributes, or challenges until the demanded event arrives and the claim's supporting structure falls.
- Active motifs: calling by voice (`quranic:root_000478:B001/m01`); claiming right or lineage (`quranic:root_000478:B002/m01`); milk left to draw later milk (`quranic:root_000478:B003/m01`); calling down harm (`quranic:root_000478:B004/m01`); parts collapsing one after another (`quranic:root_000478:B005/m01`); turns of time that summon a person (`quranic:root_000478:B006/m01`); riddling challenge (`quranic:root_000478:B007/m01`); house with no caller or inhabitant (`quranic:root_000478:B008/m01`); false assertion (`quranic:root_001290:B001/m02`); attribution of falsehood (`quranic:root_001290:B002/m02`); articulated claim (`quranic:root_001272:B001/m04`); circulating claim (`quranic:root_001272:B007/m03`); present state (`quranic:root_001332:B001/m02`).
- Ayah anchors: 67:18 `كَذَّبَ` (ك ذ ب), `كَانَ` (ك و ن); 67:23 `قُلْ` (ق و ل); 67:24 `قُلْ` (ق و ل); 67:25 `يَقُولُ` (ق و ل), `كُن` (ك و ن); 67:26 `قُلْ` (ق و ل); 67:27 `تَدَّعُ` (د ع و), `قِيلَ` (ق و ل), `كُن` (ك و ن); 67:28 `قُلْ` (ق و ل); 67:29 `قُلْ` (ق و ل); 67:30 `قُلْ` (ق و ل).
- Synthesis: Calling is not limited to request. It can assert ownership, invoke harm, pose a riddle, or draw a later flow. The collapse motif completes the scene: once the demanded event enters actuality, parts of the claimant's counter-structure fail in sequence. An empty house gives the terminal condition in which no answering voice remains.

### 29. P2: Mercy and Ruin Compete for the Same Vulnerable Body
- Semantic invariant: A threatened life can be destroyed, painfully constrained, or preserved through mercy and recognized protection.
- Surface relation: direct; 67:28 `إِنْ أَهْلَكَنِىَ ٱللَّهُ وَمَن مَّعِىَ أَوْ رَحِمَنَا فَمَن يُجِيرُ ٱلْكَٰفِرِينَ مِنْ عَذَابٍ أَلِيمٍ`.
- Surprising reach: Ruin includes drought-land, deadly pass, circular wandering, exhausted effort, appetite stampede, exposed body, dangling thong, postpartum discharge, and sweet water; mercy reaches womb, kinship, neighbor-covenant, and the painful organ after birth.

#### Subchannel A. Ruin Removes Life, Route, and Remaining Resource
- Reading type: mixed
- Scene or process: Destruction exhausts a body or route, removes usable resource, and leaves no viable way through a dangerous landscape.
- Active motifs: death, corruption, and annihilation (`quranic:root_001596:B001/m01`); casting oneself into destruction (`quranic:root_001596:B002/m01`); body breaking into a swaying gait (`quranic:root_001596:B003/m01`); destitute person seeking support (`quranic:root_001596:B004/m01`); drought land without rain (`quranic:root_001596:B005/m01`); lethal pass or chasm (`quranic:root_001596:B006/m01`); exhausting all effort (`quranic:root_001596:B009/m01`); circling lost in a desert (`quranic:root_001596:B010/m01`); falling into falsehood (`quranic:root_001596:B011/m01`); appetite-driven stampede (`quranic:root_001596:B012/m01`); sweet usable water or food (`quranic:root_000994:B001/m01`); body refusing food and drink (`quranic:root_000994:B002/m01`); restraint and deprivation (`quranic:root_000994:B003/m02`); body exposed under sky (`quranic:root_000994:B004/m01`); painful punishment (`quranic:root_000994:B005/m02`); dangling whip-tip or thong (`quranic:root_000994:B006/m01`); noble character (`quranic:root_000994:B008/m01`); postpartum discharge and womb (`quranic:root_000994:B009/m01`); felt pain (`quranic:root_000046:B001/m01`); inflicted or painful condition (`quranic:root_000046:B002/m01`).
- Ayah anchors: 67:28 `أَهْلَكَ` (ه ل ك), `عَذَابٍ` (ع ذ ب), `أَلِيمٍ` (ء ل م).
- Synthesis: Ruin is a system failure: life, route, water, appetite, and effort all cease to support continuance. Drought and lethal pass externalize the body's loss of usable intake; circular wandering wastes the last effort. The exposed body and whip-tip make punishment spatial and tactile rather than merely terminal.

#### Subchannel B. Mercy Houses, Connects, and Relieves
- Reading type: mixed
- Scene or process: Mercy places a vulnerable life within a relation of care, kinship, and protection that interrupts destructive force.
- Active motifs: compassion and beneficence (`quranic:root_000552:B001/m03`); kinship bond (`quranic:root_000552:B002/m02`); womb as protected place of growth (`quranic:root_000552:B003/m02`); postpartum womb distress requiring care (`quranic:root_000552:B004/m02`); neighboring proximity (`quranic:root_000275:B002/m02`); asylum under a protector's covenant (`quranic:root_000275:B003/m02`); genuine safety (`quranic:root_000054:B001/m03`); rescuing support (`quranic:root_001510:B001/m02`); defender's redress (`quranic:root_001510:B002/m03`); protected sanctuary status (`quranic:root_001583:B007/m02`); guardian sufficient for the entrusted matter (`quranic:root_001681:B006/m03`); withholding painful force (`quranic:root_000994:B003/m03`).
- Ayah anchors: 67:16 `أَمِن` (ء م ن); 67:17 `أَمِن` (ء م ن); 67:19 `رَّحْمَٰنُ` (ر ح م); 67:20 `رَّحْمَٰنِ` (ر ح م), `يَنصُرُ` (ن ص ر); 67:22 `أَهْدَىٰٓ` (ه د ي); 67:28 `رَحِمَ` (ر ح م), `يُجِيرُ` (ج و ر), `عَذَابٍ` (ع ذ ب); 67:29 `رَّحْمَٰنُ` (ر ح م), `ءَامَ` (ء م ن), `تَوَكَّلْ` (و ك ل).
- Synthesis: Mercy is a containing relation whose bodily paradigm is the womb and whose social paradigm is protected neighborhood. It houses, connects, and restrains harm while care continues after birth in the distressed organ. Rescue and sufficient guardianship show that tenderness is operational protection, not merely feeling.

### 30. P2: Trust Is Delegation without Abdication
- Semantic invariant: Reliance transfers an affair to a competent keeper while preserving truthful orientation; failed reliance transfers responsibility among dependents until the affair is lost.
- Surface relation: direct; 67:29 `ءَامَنَّا بِهِۦ وَعَلَيْهِ تَوَكَّلْنَا`, followed by `فَسَتَعْلَمُونَ مَنْ هُوَ فِى ضَلَٰلٍ مُّبِينٍ`.
- Surprising reach: Trust reaches legal agency, bodily weakness, a lagging mount, camel stewardship, mutual neglect, safe assent, held fire, social bond, and the straight path maintained by an appointed custodian.

#### Subchannel A. Competent Delegation Preserves the Affair
- Reading type: mixed
- Scene or process: A person knowingly entrusts an affair to a capable guardian and relies on that guardian's continuing care.
- Active motifs: transferring an affair to an agent (`quranic:root_001681:B001/m01`); active reliance (`quranic:root_001681:B002/m01`); sufficient keeper and guarantor (`quranic:root_001681:B006/m04`); settled safety and trustworthiness (`quranic:root_000054:B001/m04`); assent that settles the heart (`quranic:root_000054:B002/m02`); prayer for acceptance (`quranic:root_000054:B003/m01`); stewardship over an affair (`quranic:root_001273:B004/m02`); acting in another's place (`quranic:root_001273:B007/m02`); mainstay that keeps life upright (`quranic:root_001273:B009/m02`); retaining and protecting (`quranic:root_001424:B001/m03`); watchful eye (`quranic:root_001069:B003/m02`); clear knowledge (`quranic:root_001040:B001/m03`); disclosed proof (`quranic:root_000170:B004/m02`).
- Ayah anchors: 67:16 `أَمِن` (ء م ن); 67:17 `أَمِن` (ء م ن), `تَعْلَمُ` (ع ل م); 67:19 `يُمْسِكُ` (م س ك); 67:21 `أَمْسَكَ` (م س ك); 67:22 `مُّسْتَقِيمٍ` (ق و م); 67:26 `عِلْمُ` (ع ل م), `مُّبِينٌ` (ب ي ن); 67:29 `تَوَكَّلْ` (و ك ل), `ءَامَ` (ء م ن), `تَعْلَمُ` (ع ل م), `مُّبِينٍ` (ب ي ن); 67:30 `مَّعِينٍۭ` (ع ي ن).
- Synthesis: Trust joins informed assent to competent agency. The guardian watches, holds, and keeps the affair upright; the entruster does not deny the affair's real direction or evidence. Mainstay and proxy show why delegation can preserve action rather than suspend it.

#### Subchannel B. Mutual Dependence Can Dissolve Responsibility
- Reading type: latent/lexical
- Scene or process: Weak agents pass the affair among one another, a mount lags behind its rider, and no participant supplies the missing capacity.
- Active motifs: dependent person who abandons his own affair (`quranic:root_001681:B003/m01`); mutual reliance that loses the task (`quranic:root_001681:B004/m02`); lagging animal that leans on its rider (`quranic:root_001681:B005/m01`); bodily weakness relying on support (`quranic:root_001583:B009/m02`); weak walker leaning between two people (`quranic:root_001583:B008/m02`); remnant of strength barely preserving life (`quranic:root_001424:B003/m04`); substitute force below the needed rank (`quranic:root_000502:B003/m02`); recoil from the required action (`quranic:root_001532:B001/m03`); explicit error of direction (`quranic:root_000913:B001/m04`); separation that breaks connection (`quranic:root_000170:B001/m02`).
- Ayah anchors: 67:19 `يُمْسِكُ` (م س ك); 67:20 `دُونِ` (د و ن); 67:21 `أَمْسَكَ` (م س ك), `نُفُورٍ` (ن ف ر); 67:22 `أَهْدَىٰٓ` (ه د ي); 67:26 `مُّبِينٌ` (ب ي ن); 67:29 `تَوَكَّلْ` (و ك ل), `ضَلَٰلٍ` (ض ل ل), `مُّبِينٍ` (ب ي ن).
- Synthesis: Failed delegation is not trust directed at the wrong strong party; it is responsibility circulating among weak parties until action disappears. The lagging mount and supported walker separate legitimate assistance from abandonment: aid may enable movement, but mutual abdication leaves no one carrying the load.

### 31. P2: Water Can Withdraw into Depth or Reappear as a Visible Source
- Semantic invariant: Water's availability depends on vertical position, permeable apertures, directed flow, and the power to bring hidden substance back into reach.
- Surface relation: direct; 67:30 `إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًا فَمَن يَأْتِيكُم بِمَآءٍ مَّعِينٍ`.
- Surprising reach: The terminal question unfolds into valley lowland, mountain cave, sunset, noonday descent, raid, bodily cavities, eye, spy, skin puncture, cloud-eye, cash, credit, aristocratic "eyes," gold wash, mirror, and deceptive surface luster.

#### Subchannel A. Descent Removes Water from Reach
- Reading type: mixed
- Scene or process: Water drops below the accessible surface, enters a low place or hidden cavity, and leaves users unable to draw it.
- Active motifs: descent into depth (`quranic:root_001112:B001/m01`); lowland and travel down to it (`quranic:root_001112:B002/m01`); cave or mountain refuge (`quranic:root_001112:B003/m01`); sun disappearing below the horizon (`quranic:root_001112:B004/m01`); descent for the noon halt (`quranic:root_001112:B005/m01`); rapid raid or downward rush (`quranic:root_001112:B006/m01`); bodily cavities of belly and genitals (`quranic:root_001112:B007/m01`); ground swallowing (`quranic:root_000410:B001/m02`); oscillating flow across ground (`quranic:root_001456:B002/m02`); water-holding stratum (`quranic:root_001424:B004/m03`); low earth beneath sky (`quranic:root_000025:B001/m04`); becoming a changed condition by morning (`quranic:root_000839:B010/m02`).
- Ayah anchors: 67:16 `يَخْسِفَ` (خ س ف), `تَمُورُ` (م و ر), `أَرْضَ` (ء ر ض); 67:19 `يُمْسِكُ` (م س ك); 67:21 `أَمْسَكَ` (م س ك); 67:24 `أَرْضِ` (ء ر ض); 67:30 `غَوْرًا` (غ و ر), `أَصْبَحَ` (ص ب ح).
- Synthesis: Withdrawal is a vertical and accessibility change, not annihilation. Water can remain in a lowland, cave, stratum, or bodily cavity while becoming unavailable at the working surface. Sunset and noon descent supply timed analogies; the raid supplies a fast version of the same directional motion. Morning makes the changed state newly discoverable.

#### Subchannel B. Spring, Aperture, and Watchful Eye
- Reading type: mixed
- Scene or process: A hidden reservoir becomes usable through an opening that releases flow and remains visible enough to be found or watched.
- Active motifs: seeing eye (`quranic:root_001069:B001/m01`); direct witnessing (`quranic:root_001069:B002/m01`); guarding eye (`quranic:root_001069:B003/m03`); harmful gaze (`quranic:root_001069:B004/m01`); scout or spy (`quranic:root_001069:B005/m01`); flowing spring (`quranic:root_001069:B006/m01`); puncture in a skin or watersack (`quranic:root_001069:B007/m01`); sun's disk (`quranic:root_001069:B008/m01`); eye-like socket or notch in an implement (`quranic:root_001069:B009/m01`); cloud aperture and sustained rain (`quranic:root_001069:B010/m01`); water as known substance (`quranic:root_001458:B001/m01`); water appearing and increasing in well or earth (`quranic:root_001458:B002/m01`); delivering water by pouring and irrigation (`quranic:root_001458:B003/m01`); directed water channel (`quranic:root_000009:B004/m02`); external flood delivering water (`quranic:root_000009:B005/m03`); arrival and bringing (`quranic:root_000009:B001/m04`); bringing a thing with another (`quranic:root_000009:B002/m02`).
- Ayah anchors: 67:30 `مَّعِينٍۭ` (ع ي ن), `مَآؤُ/مَآءٍ` (م و ه), `يَأْتِي` (ء ت ي).
- Synthesis: Eye and spring share a precise aperture relation: an opening makes an interior medium visible or lets it flow outward. Skin puncture and tool notch distinguish leak from controlled release; the watchful eye and scout distinguish finding from guarding. The final question therefore concerns both hidden supply and the agent capable of reopening its route.

#### Subchannel C. Water Is Substance, Appearance, and Liquid Value
- Reading type: latent/lexical
- Scene or process: Water or water-like luster enters bodies, surfaces, and exchange systems, where real substance can be distinguished from cosmetic appearance.
- Active motifs: reproductive fluid entering a womb (`quranic:root_001458:B004/m01`); metal washed with gold or silver and made deceptive (`quranic:root_001458:B005/m01`); facial and verbal luster like water (`quranic:root_001458:B006/m01`); crystal or mirror clarity (`quranic:root_001458:B007/m01`); dull water-heavy heart (`quranic:root_001458:B008/m02`); cash present to hand (`quranic:root_001069:B011/m01`); credit transaction producing cash (`quranic:root_001069:B012/m01`); the exact thing itself (`quranic:root_001069:B013/m01`); choice specimen (`quranic:root_001069:B014/m01`); notables or full siblings (`quranic:root_001069:B015/m01`); wide beautiful eye (`quranic:root_001069:B016/m01`); people visibly present (`quranic:root_001069:B017/m01`); yield and abundance brought forth (`quranic:root_000009:B007/m03`); tax rendered (`quranic:root_000009:B008/m03`); destructive arrival (`quranic:root_000009:B011/m02`); penetrating agent (`quranic:root_000009:B013/m02`).
- Ayah anchors: 67:30 `مَآؤُ/مَآءٍ` (م و ه), `مَّعِينٍۭ` (ع ي ن), `يَأْتِي` (ء ت ي).
- Synthesis: The scene separates liquid reality from its analogues. Water can be reproductive substance, life-bearing yield, surface luster, mirror clarity, metallic wash, or a metaphor for ready cash. Gold wash is the crucial pressure: a water-like sheen may imitate value without supplying the substance required for life. "The thing itself" marks the demand for actual water rather than its appearance.

### 32. P2: "Above" Organizes Hierarchy, Recovery, and Recurrent Supply
- Semantic invariant: Vertical superiority can denote location, rank, or control, while the same root tracks cyclical return of consciousness, milk, rain, breath, and measured intake.
- Surface relation: direct; 67:19 `ٱلطَّيْرِ فَوْقَهُمْ`; indirectly related to 67:16-17 `فِى ٱلسَّمَآءِ` and 67:21 withheld provision.
- Surprising reach: A simple spatial preposition opens into political dominance, beauty and honor, numeric excess, recovery from fainting, the interval between milkings, cloud bursts, arrow nock, terminal breath, poverty, and the joint where neck meets head.

#### Subchannel A. Height Becomes Rank, Control, and Measured Excess
- Reading type: mixed
- Scene or process: An entity occupies a higher position that can become superior status, governing force, or an amount beyond a threshold.
- Active motifs: spatial position above (`quranic:root_001188:B001/m01`); superior beauty, honor, or degree (`quranic:root_001188:B002/m01`); domination from above (`quranic:root_001188:B003/m01`); amount beyond a stated measure (`quranic:root_001188:B004/m01`); arrow nock receiving the string (`quranic:root_001188:B009/m01`); upper bodily and mechanical joints (`quranic:root_001188:B013/m01`); overhead sky (`quranic:root_000745:B004/m06`); troop beneath a possible defender (`quranic:root_000264:B001/m03`); upright rank (`quranic:root_001273:B008/m02`).
- Ayah anchors: 67:16 `سَّمَآءِ` (س م و); 67:17 `سَّمَآءِ` (س م و); 67:19 `فَوْقَ` (ف و ق); 67:20 `جُندٌ` (ج ن د); 67:22 `مُّسْتَقِيمٍ` (ق و م).
- Synthesis: Height is made relational. Birds are above observers; a ruler or force may be above dependents; a measured amount can exceed its limit; and an arrow nock locates the upper interface that transmits force. The channel therefore distinguishes simple elevation from hierarchy while preserving their common vertical geometry.

#### Subchannel B. Recovery and Supply Return in Intervals
- Reading type: latent/lexical
- Scene or process: A depleted system recovers by pauses and repeated small returns of awareness, milk, rain, or intake.
- Active motifs: recovery of consciousness or strength (`quranic:root_001188:B005/m01`); milk returning between two milkings (`quranic:root_001188:B006/m01`); taking drink or food in intervals (`quranic:root_001188:B007/m01`); repeated cloud releases (`quranic:root_001188:B008/m01`); hiccup, gasp, or departing breath (`quranic:root_001188:B010/m01`); poverty and need (`quranic:root_001188:B011/m01`); provision allotted as food (`quranic:root_000560:B002/m04`); recurring milk (`quranic:root_000563:B006/m02`); water-bearing cloud (`quranic:root_000410:B007/m03`); remnant preserving life (`quranic:root_001424:B003/m05`).
- Ayah anchors: 67:16 `يَخْسِفَ` (خ س ف); 67:17 `يُرْسِلَ` (ر س ل); 67:19 `فَوْقَ` (ف و ق), `يُمْسِكُ` (م س ك); 67:21 `يَرْزُقُ/رِزْقَ` (ر ز ق), `أَمْسَكَ` (م س ك).
- Synthesis: Supply is rhythmic. Milk reaccumulates, cloud releases water in bursts, and a drinker takes measured intervals; consciousness and strength similarly return after interruption. Poverty names the condition in which those returns no longer meet need. The final gasp marks the cycle's terminal failure.

### 33. P2: Prior Reception Turns into Estrangement and Rejection
- Semantic invariant: A message or event approaches a receiving side, is either accepted and borne, or is made strange, altered, and opposed.
- Surface relation: direct; 67:17 `يُرْسِلَ`; 67:18 `كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ`, `نَكِيرِ`; 67:26 `نَذِيرٌ مُّبِينٌ`.
- Surprising reach: Reception is modeled by midwife, bucket receiver, guarantee, joined skull plates, headwind, first crescent, magical bead, easy gait, deliberate pace, courtship after widowhood, and the discharge that makes an inward lesion visible.

#### Subchannel A. Facing, Receiving, and Bearing What Comes
- Reading type: mixed
- Scene or process: A receiving side turns toward an arrival, accepts or refuses it, and may assume responsibility for carrying it forward.
- Active motifs: face-to-face reception (`quranic:root_001198:B001/m02`); precedence in time and place (`quranic:root_001198:B002/m02`); source-side of an event (`quranic:root_001198:B003/m02`); accepting with approval (`quranic:root_001198:B004/m01`); ritual direction faced (`quranic:root_001198:B005/m01`); kiss and direct contact (`quranic:root_001198:B006/m01`); midwife or bucket receiver (`quranic:root_001198:B007/m01`); guarantee and written undertaking (`quranic:root_001198:B008/m01`); facing social group or tribe (`quranic:root_001198:B009/m01`); matched joined parts (`quranic:root_001198:B010/m01`); bodily mark turned toward a side (`quranic:root_001198:B011/m01`); wind facing the opposite wind (`quranic:root_001198:B012/m01`); capacity to confront (`quranic:root_001198:B013/m01`); watering at animals' mouths (`quranic:root_001198:B014/m01`); fresh beginning without preparation (`quranic:root_001198:B015/m01`); bead intended to turn a person's face (`quranic:root_001198:B016/m01`).
- Ayah anchors: 67:18 `قَبْلِ` (ق ب ل).
- Synthesis: Reception has orientation, contact, acceptance, and liability. Midwife, bucket receiver, guarantor, and watering at the mouth each show a receiver prepared to take what arrives. Headwind and magical bead supply opposed or manipulated orientation. "Before" thus becomes more than chronology: it is a prior receiving side whose response established a precedent.

#### Subchannel B. The Known Is Made Strange and Opposed
- Reading type: mixed
- Scene or process: Recognition is refused, an object or act is altered until unfamiliar, and opposition escalates toward censure or combat.
- Active motifs: nonrecognition and denial (`quranic:root_001550:B001/m01`); shrewdness toward an unfamiliar matter (`quranic:root_001550:B002/m01`); severe strange event (`quranic:root_001550:B003/m01`); alteration into an unknown or hated state (`quranic:root_001550:B004/m01`); discharge revealing an internal lesion (`quranic:root_001550:B005/m01`); reprehensible act that must be stopped (`quranic:root_001550:B006/m01`); hostile confrontation (`quranic:root_001550:B007/m01`); attribution of falsehood (`quranic:root_001290:B002/m03`); covering known truth (`quranic:root_001307:B003/m03`); visible proof as the rejected contrast (`quranic:root_000170:B004/m03`).
- Ayah anchors: 67:18 `نَكِيرِ` (ن ك ر), `كَذَّبَ` (ك ذ ب); 67:20 `كَٰفِرُونَ` (ك ف ر); 67:26 `مُّبِينٌ` (ب ي ن); 67:27 `كَفَرُ` (ك ف ر); 67:28 `كَٰفِرِينَ` (ك ف ر); 67:29 `مُّبِينٍ` (ب ي ن).
- Synthesis: Rejection actively makes the known strange. It denies recognition, alters the object or account, labels it hateful, and may proceed to hostile confrontation. Bodily discharge supplies a diagnostic reversal: what was hidden becomes unmistakably manifest even while the subject would prefer not to know it.

#### Subchannel C. The Messenger Carries Content with Deliberate Pace
- Reading type: mixed
- Scene or process: A carrier is released with speech, moves in a controlled manner, and establishes a relation between sender and recipient.
- Active motifs: messenger and carried message (`quranic:root_000563:B002/m01`); smooth easy gait (`quranic:root_000563:B003/m01`); deliberation and measured pace (`quranic:root_000563:B004/m01`); ease and familiarity with another (`quranic:root_000563:B007/m01`); correspondence and paired performance (`quranic:root_000563:B008/m01`); widow approached by suitors (`quranic:root_000563:B009/m01`); generous ease in giving (`quranic:root_000563:B010/m01`); specifically named carried objects (`quranic:root_000563:B011/m01`); dispatch and release (`quranic:root_000563:B001/m02`); warning-bearing agent (`quranic:root_001488:B001/m05`).
- Ayah anchors: 67:17 `يُرْسِلَ` (ر س ل), `نَذِيرِ` (ن ذ ر); 67:26 `نَذِيرٌ` (ن ذ ر).
- Synthesis: Message transport is defined by sender, carrier, content, pace, and recipient. Ease and deliberation keep release from becoming uncontrolled scattering. Correspondence makes communication reciprocal, while courtship and giving show the same carrier relation operating in socially delicate approaches.

### 34. P2: Deixis and Accompaniment Fix the Parties to the Challenge
- Semantic invariant: Repeated commands, demonstratives, questions, and accompaniment terms identify who speaks, what is being indicated, and with whom responsibility is shared.
- Surface relation: direct; 67:20-21 `هَٰذَا ٱلَّذِى`; 67:23-30 repeated `قُلْ`; 67:25 `هَٰذَا ٱلْوَعْدُ`; 67:27 `هَٰذَا ٱلَّذِى`; 67:28 `وَمَن مَّعِىَ`.
- Surprising reach: The discourse frame includes possession by attribution, relative and demonstrative reference, interrogative compounds, answer particles, repetitive writing, being "with whoever wins," battlefield din, heat-travel, hurried work, companionship, algae attached to water, and the submissive dependent.

#### Subchannel A. Demonstration, Question, and Effective Saying
- Reading type: mixed
- Scene or process: A speaker arrests attention, points to a referent, asks or answers about it, and uses repeated utterance to define the challenged proposition.
- Active motifs: possessor identified by relation (`quranic:root_000527:B001/m01`); relative expression "the one who" (`quranic:root_000527:B002/m01`); demonstrative pointing (`quranic:root_000527:B003/m01`); interrogative or relative compound (`quranic:root_000527:B004/m01`); attention-opening particle (`quranic:root_001573:B002/m01`); vocal answer or response (`quranic:root_001573:B003/m01`); interrogative substitution (`quranic:root_001573:B004/m01`); letter-name and articulation (`quranic:root_001573:B006/m01`); loquacious speaker (`quranic:root_001272:B003/m01`); speech drawn inward to oneself (`quranic:root_001272:B006/m01`); wooden bat used in a game (`quranic:root_001272:B008/m01`); imposing one's judgment (`quranic:root_001272:B010/m01`); serious concern expressed by saying (`quranic:root_001272:B015/m01`); interrogative alert (`quranic:root_000531:B013/m02`); clear explanatory speech (`quranic:root_000170:B005/m02`).
- Ayah anchors: 67:19 `يَرَ` (ر ء ي); 67:23 `قُلْ` (ق و ل); 67:24 `قُلْ` (ق و ل); 67:25 `يَقُولُ` (ق و ل); 67:26 `قُلْ` (ق و ل), `مُّبِينٌ` (ب ي ن); 67:27 `قِيلَ` (ق و ل), `رَأَ` (ر ء ي); 67:28 `قُلْ` (ق و ل), `رَءَيْ` (ر ء ي); 67:29 `قُلْ` (ق و ل), `مُّبِينٍ` (ب ي ن); 67:30 `قُلْ` (ق و ل), `رَءَيْ` (ر ء ي); surface anchors unavailable for `ذ و و`, `ه ا ء` (missing root coverage).
- Synthesis: The repeated challenge is organized by attention, reference, and predication. Demonstratives fix the object, relative forms define it by relation, questions demand a response, and `قُلْ` repeatedly reassigns the speaking turn. Loquacity and self-directed speech mark failure modes in which verbal volume or inward rehearsal replaces an answer.

#### Subchannel B. "With Me" Distinguishes Fellowship from Opportunism
- Reading type: mixed
- Scene or process: Accompaniment places persons in one ordeal, but shared position can mean loyal company, mere adjacency, or opportunistic alignment with whoever prevails.
- Active motifs: din of fire and battle (`quranic:root_001434:B001/m01`); severe heat and travel through it (`quranic:root_001434:B002/m01`); hurried work (`quranic:root_001434:B004/m01`); joining whichever side wins (`quranic:root_001434:B005/m01`); repeated writing or saying of "with" (`quranic:root_001434:B006/m01`); guaranteeing another (`quranic:root_001332:B003/m01`); submissive dependence (`quranic:root_001332:B004/m01`); old man defined by his past claim (`quranic:root_001332:B005/m01`); neighboring proximity (`quranic:root_000275:B002/m03`); asylum under protection (`quranic:root_000275:B003/m03`); sanctuary status (`quranic:root_001583:B007/m03`); mutual reliance that can lose an affair (`quranic:root_001681:B004/m03`).
- Ayah anchors: 67:18 `كَانَ` (ك و ن); 67:22 `أَهْدَىٰٓ` (ه د ي); 67:25 `كُن` (ك و ن); 67:27 `كُن` (ك و ن); 67:28 `يُجِيرُ` (ج و ر); 67:29 `تَوَكَّلْ` (و ك ل); surface anchors unavailable for `م ع ع` (missing root coverage).
- Synthesis: Accompaniment is tested under heat and conflict. Protected proximity and guarantee can make company durable; opportunism merely follows the winner; mutual abdication lets the shared affair fail. Repetition of "with" exposes how the language of solidarity can be present even when commitment is absent.

## Standalone Subchannels

### S1. A Mount Is Left to Die at Its Owner's Grave
- Reading type: latent/lexical
- Scene or process: A camel or other mount is tethered beside its owner's grave, denied feed and water, and left there until it dies.
- Active motifs: mount bound at its owner's grave (`quranic:root_000153:B005/m01`); grave animal denied food and water until death (`quranic:root_000154:B006/m01`).
- Ayah anchors: 67:2 `يَبْلُوَ` (ب ل و); surface anchors unavailable for `ب ل ي` (missing root coverage).
- Synthesis: The two variant-root branches preserve one complete mortuary rite: owner, grave, tethered animal, deliberate deprivation, and a second death. It usefully pressures 67:2 by showing humans manufacturing death as a display beside the dead, whereas the surah locates death, life, and trial under divine creation; the rite can consume another life but cannot produce the promised return.

### S2. A Postpartum Fenugreek Drink Is Boiled and Finished
- Reading type: latent/lexical
- Scene or process: Fenugreek is cooked until it boils, strained, mixed with dates, and given as a drink to a woman after childbirth.
- Active motifs: fenugreek cooked to the boil (`quranic:root_001185:B006/m01`); boiled liquid strained and mixed with dates (`quranic:root_001185:B006/m02`); finished drink taken by a postpartum woman (`quranic:root_001185:B006/m03`).
- Ayah anchors: 67:7 `تَفُورُ` (ف و ر).
- Synthesis: Ingredient, heat, filtering, sweetening, and patient form a closed domestic treatment sequence. This controlled boil materializes the threshold in 67:7: the same activation that can mark a prepared drink reaching readiness makes hell's `تَفُورُ` an uncontrolled vessel-state whose contents and force no attendant can regulate.

### S3. A Singer Is Heard with Drum and Cymbal
- Reading type: latent/lexical
- Scene or process: A singer or singing woman gives a pleasurable vocal performance while a single-headed drum and ringing cymbal articulate the sound around her.
- Active motifs: pleasurable singing and its performer (`quranic:root_000741:B007/m01`); ringing cymbal (`quranic:root_000897:B009/m01`); single-headed drum (`quranic:root_001281:B012/m01`).
- Ayah anchors: 67:6 `ٱلْمَصِيرُ` (ص ي ر); 67:7 `سَمِعُوا۟` (س م ع); 67:9 `كَبِيرٍۢ` (ك ب ر); 67:10 `نَسْمَعُ` (س م ع); 67:12 `كَبِيرٌۭ` (ك ب ر); 67:23 `ٱلسَّمْعَ` (س م ع).
- Synthesis: Performer, voice, drumhead, cymbal, and listeners make a compact auditory scene rather than a generic music field. It sharpens the surah's distinction between hearing and heedful listening: the condemned hear hell in 67:7 yet regret in 67:10 that they did not listen, while this ensemble shows listening as selective attention to an intelligible arrangement of sounds.

### S4. Lost Property Is Announced and Identified by Its Marks
- Reading type: latent/lexical
- Scene or process: An announcer calls out a found or lost object, asks the community for information, and accepts a claimant who can identify it by description.
- Active motifs: public announcement of lost or found property (`quranic:root_001002:B008/m01`); asking who recognizes the object (`quranic:root_001002:B008/m02`); claimant identifying it by its description (`quranic:root_001002:B008/m03`).
- Ayah anchors: 67:11 `ٱعْتَرَفُوا۟` (ع ر ف).
- Synthesis: Object, announcer, witnesses, descriptive marks, and claimant complete an evidentiary recognition procedure. The scene materializes the force of 67:11: after warning has supplied the identifying description, confession is recognition of a liability that now matches its announced marks, not merely an unprompted admission.

### S5. Pilgrims Stand at the Appointed Station of Arafat
- Reading type: latent/lexical
- Scene or process: Pilgrims reach the named place on its appointed day and perform the defining act of standing or witnessing there.
- Active motifs: Arafat as designated place and day (`quranic:root_001002:B007/m01`); standing or witnessing at Arafat (`quranic:root_001002:B007/m02`); ritual `ta'rif` at the station (`quranic:root_001002:B007/m03`).
- Ayah anchors: 67:11 `ٱعْتَرَفُوا۟` (ع ر ف).
- Synthesis: Appointed time, bounded place, assembled pilgrims, and standing make this a complete rite of recognition. It gives spatial and bodily pressure to `ٱعْتَرَفُوا۟` in 67:11: recognition can mean taking one's exposed place at an appointed station, whereas the companions of the blaze reach recognition only after their destination has closed around them.

### S6. A Handler Guides a Camel in Mating
- Reading type: latent/lexical
- Scene or process: A male camel fails to locate the mating position, so a handler guides its member into place, or the animal succeeds in making that exact placement itself.
- Active motifs: camel unable to find the mating position (`quranic:root_001356:B004/m01`); handler guiding the insertion (`quranic:root_001356:B004/m02`); animal making the precise placement itself (`quranic:root_001356:B004/m03`).
- Ayah anchors: 67:14 `ٱللَّطِيفُ` (ل ط ف).
- Synthesis: Animal, hidden anatomical target, failed attempt, fine manual intervention, and successful placement form a precise husbandry scene. Its activation materializes `ٱللَّطِيفُ` in 67:14 as exact access and minimally scaled direction within a created body, usefully pressing "subtle" knowledge toward concrete precision rather than vague gentleness.

### S7. A Visible Trace Distinguishes Menstruation from Purity
- Reading type: latent/lexical
- Scene or process: A woman examines a yellow or white trace, sometimes on a cloth, and uses what she sees to distinguish menstruation from ritual purity.
- Active motifs: yellow or white bodily trace or test cloth (`quranic:root_000531:B007/m01`); visual distinction between menstruation and purity (`quranic:root_000531:B007/m02`).
- Ayah anchors: 67:3 `تَرَىٰ/تَرَىٰ` (ر ء ي); 67:19 `يَرَوْا۟` (ر ء ي); 67:27 `رَأَوْهُ` (ر ء ي); 67:28 `أَرَءَيْتُمْ` (ر ء ي); 67:30 `أَرَءَيْتُمْ` (ر ء ي).
- Synthesis: Observer, small bodily sign, cloth, threshold states, and practical verdict make a complete diagnostic scene. It reframes the surah's repeated seeing as discrimination from exact evidence: the decisive visual act is not spectacle but reading a slight trace well enough to determine which state now obtains.

### S8. A Purgative Is Followed by a Binding Remedy
- Reading type: latent/lexical
- Scene or process: A person drinks a purgative that loosens the bowels, then takes a food or medicine that checks the discharge and restores bodily restraint.
- Active motifs: drinking a purgative (`quranic:root_001427:B002/m01`); bowel release caused by the drug (`quranic:root_001427:B002/m02`); binding food or medicine (`quranic:root_001036:B006/m01`); bowel restraint after looseness (`quranic:root_001036:B006/m02`).
- Ayah anchors: 67:10 `نَعْقِلُ` (ع ق ل); 67:15 `ٱمْشُوا۟` (م ش ي); 67:22 `يَمْشِى/يَمْشِى` (م ش ي).
- Synthesis: Dose, internal release, counter-remedy, and restored containment make a complete treatment cycle. The scene concretely pressures the surah's paired activations: `م ش ي` can mark uncontrolled bodily passage as well as gait, while `ع ق ل` can restore holding as well as reason; guidance therefore appears as regulated movement rather than motion or restraint alone.

### S9. A Bulk Food Sale Is Priced, Measured, and Settled
- Reading type: latent/lexical
- Scene or process: A merchant sets the food price, values the lot, measures a large quantity by the `kurr` and its subordinate measures, and receives immediate hand-to-hand payment.
- Active motifs: market food price and price-setting (`quranic:root_000708:B003/m01`); bulk measure calculated by `kurr`, `qafiz`, or `wasq` (`quranic:root_001292:B004/m01`); valuation of commodity or property (`quranic:root_001273:B010/m01`); immediate hand-to-hand settlement (`quranic:root_001693:B007/m01`).
- Ayah anchors: 67:1 `بِيَدِهِ` (ي د ي); 67:4 `كَرَّتَيْنِ` (ك ر ر); 67:5 `ٱلسَّعِيرِ` (س ع ر); 67:10 `ٱلسَّعِيرِ` (س ع ر); 67:11 `ٱلسَّعِيرِ` (س ع ر); 67:22 `مُّسْتَقِيمٍۢ` (ق و م).
- Synthesis: Seller, food lot, quoted price, standard measure, valuation, and cash transfer form one bounded transaction. It materializes the human handling of provision in 67:21: people can price, measure, and settle what reaches the market, but the question of who supplies when provision is withheld exposes the transaction's dependence on a prior giver beyond the paying hand.

### S10. Incense and Perfume Fill a Space with Traceable Scent
- Reading type: latent/lexical
- Scene or process: Aloeswood is burned, `khaluq` and camphor are applied as perfume, and the resulting fragrance spreads from the treated body or material into the surrounding air.
- Active motifs: aloeswood burned as incense (`quranic:root_000076:B014/m01`); application or coating with `khaluq` perfume (`quranic:root_000434:B010/m01`); camphor used as perfume (`quranic:root_001307:B011/m01`); pleasant scent spreading outward (`quranic:root_001503:B003/m01`).
- Ayah anchors: 67:2 `خَلَقَ` (خ ل ق); 67:3 `خَلَقَ/خَلْقِ` (خ ل ق); 67:6 `كَفَرُوا۟` (ك ف ر); 67:14 `خَلَقَ` (خ ل ق); 67:15 `ٱلنُّشُورُ` (ن ش ر); 67:20 `ٱلْكَٰفِرُونَ` (ك ف ر); 67:27 `كَفَرُوا۟` (ك ف ر); 67:28 `ٱلْكَٰفِرِينَ` (ك ف ر); surface anchors unavailable for `ء ل ي` (missing root coverage).
- Synthesis: Fuel, smoke, applied substances, body or surface, and diffusing scent make a complete perfuming operation. The scene gives `ٱلنُّشُورُ` a compact material analogue: a prepared source releases an invisible but unmistakable trace through a wider field, usefully reframing emergence and disclosure as effects that propagate beyond their point of origin.

### S11. Walnuts Decide an Odd-or-Even Call
- Reading type: latent/lexical
- Scene or process: Players use walnuts in a counting game and call `khasa or zaka` according to whether the count is odd or even.
- Active motifs: walnuts used in a counting game (`quranic:root_000408:B003/m01`); `khasa or zaka` as the odd-or-even verdict (`quranic:root_000408:B003/m02`).
- Ayah anchors: 67:4 `خَاسِئًۭا` (خ س ء).
- Synthesis: Players, countable objects, a numerical result, binary call, and verdict make a complete game. The activation usefully reframes the returned gaze in 67:4: `خَاسِئًا` carries the surprise of a decisive game-call, so repeated inspection ends not in an open search but in a result already settled against the challenger.

### S12. An Act or Food Breaks a Fast
- Reading type: latent/lexical
- Scene or process: A fasting person crosses into `iftar` by performing an act or taking the food that ends abstention.
- Active motifs: leaving the state of fasting and entering `iftar` (`quranic:root_001165:B004/m01`); act or food by which the fast is broken (`quranic:root_001165:B004/m02`).
- Ayah anchors: 67:3 `فُطُورٍۢ` (ف ط ر).
- Synthesis: Fasting person, maintained restraint, threshold act, food, and changed state complete a ritual transition. This activation pressures the search for `فُطُورٍ` in 67:3: a breach is not merely an empty crack but the point at which a bounded regime is broken and a previously withheld intake begins; the inspected sky yields no such violated threshold.

### S13. An Interpreter Carries Speech into Another Tongue
- Reading type: latent/lexical
- Scene or process: A speaker's words reach an interpreter, who explains them in another language to a recipient who otherwise could not understand them.
- Active motifs: speech rendered in another tongue (`quranic:root_000547:B009/m01`); interpreter as agent of clarification (`quranic:root_000547:B009/m02`).
- Ayah anchors: 67:5 `رُجُومًۭا` (ر ج م).
- Synthesis: Speaker, utterance, language boundary, interpreter, second rendering, and recipient form a complete transfer scene. It usefully pressures the surah's adjacency of projectiles and warning speech: the root activated by `رُجُومًا` can also carry meaning across a boundary, sharpening the difference between a message that reaches understanding and an assertion merely cast toward the unseen.

### S14. A Caller Summons Hearers to Prayer
- Reading type: latent/lexical
- Scene or process: A caller gives the imperative `hayya 'ala al-salah`, and hearers are summoned to approach and join the prayer.
- Active motifs: imperative `hayya 'ala` as a summons to come (`quranic:root_000383:B009/m01`); movement toward prayer in response to the call (`quranic:root_000383:B009/m02`).
- Ayah anchors: 67:2 `ٱلْحَيَوٰةَ` (ح ي ي).
- Synthesis: Caller, audible formula, hearers, directed approach, and communal act make a complete summons. The scene materializes the life-root in 67:2 as responsive motion: life is not only a condition opposed to death but an ability to hear a call and move toward an accountable act within the test.

### S15. A Familiar Spirit Appears with Divination or Medicine
- Reading type: latent/lexical
- Scene or process: A jinn familiar presents itself to a person and shows or supplies divinatory knowledge or medical guidance.
- Active motifs: jinn familiar appearing to a person (`quranic:root_000531:B008/m01`); familiar spirit offering divination or medicine (`quranic:root_000531:B008/m02`).
- Ayah anchors: 67:3 `تَرَىٰ/تَرَىٰ` (ر ء ي); 67:19 `يَرَوْا۟` (ر ء ي); 67:27 `رَأَوْهُ` (ر ء ي); 67:28 `أَرَءَيْتُمْ` (ر ء ي); 67:30 `أَرَءَيْتُمْ` (ر ء ي).
- Synthesis: Human seeker, appearing spirit, hidden information, and proposed remedy form a complete rival-knowledge scene. It usefully pressures the surah's repeated demands to see and its restriction of knowledge: an apparition may claim access to divination or cure, but 67:13-14 and 67:26 locate exhaustive hidden knowledge with the creator rather than with an episodic intermediary.

### S16. A `Nushra` Incantation Releases an Afflicted Person
- Reading type: latent/lexical
- Scene or process: A practitioner applies a `nushra` incantation or treatment to a person regarded as mad or bewitched so that the affliction is removed from them.
- Active motifs: incantation or treatment for madness or bewitchment (`quranic:root_001503:B008/m01`); affliction unfolded and removed from the patient (`quranic:root_001503:B008/m02`).
- Ayah anchors: 67:15 `ٱلنُّشُورُ` (ن ش ر).
- Synthesis: Practitioner, afflicted patient, applied formula, constraining condition, and release make a complete healing rite. Its activation supports `ٱلنُّشُورُ` by materializing emergence as an unbinding from a state that held the person closed, while the surah enlarges that release from an individual treatment to the return of all creatures.

### S17. A Hunting Party Sets Out with Its Implements
- Reading type: latent/lexical
- Scene or process: A group goes out to hunt, its hunters carry their implements, and they seek wild game.
- Active motifs: group setting out to hunt (`quranic:root_000745:B006/m01`); hunters seeking wild animals (`quranic:root_000745:B006/m02`); implement carried by a hunter (`quranic:root_000745:B006/m03`).
- Ayah anchors: 67:3 `سَمَٰوَٰتٍۢ` (س م و); 67:5 `ٱلسَّمَآءَ` (س م و); 67:16 `ٱلسَّمَآءِ` (س م و); 67:17 `ٱلسَّمَآءِ` (س م و).
- Synthesis: Departing party, open hunting ground, game, pursuit, and tool make a closed subsistence expedition. The scene grounds the sky-root in a human attempt to obtain provision from mobile creatures; beside the birds of 67:19 and the provision question of 67:21, it exposes the hunter's dependence on a domain whose flight and yield remain held beyond the implement in his hand.

### S18. P1 to P2: Commanded Walking Becomes a Verdict on Gait
- Reading type: surface-primary
- Scene or process: P1 (67:15) to P2 (67:22); role progression and contrast: movement first appears as an authorized use of a tractable earth, then becomes the bodily test that distinguishes prone wandering from upright travel on a path.
- Active motifs: intentional locomotion (`quranic:root_001427:B001/m01`); intentional walking (`quranic:root_001427:B001/m02`).
- Ayah anchors: 67:15 `ٱمْشُوا۟` (م ش ي); 67:22 `يَمْشِى/يَمْشِى` (م ش ي).
- Synthesis: The shared scene signature is one walker moving over a supporting surface toward an end; the bridge changes the role of gait. P1 grants movement and livelihood, while P2 asks whether the moving body is correctly oriented. Walking therefore progresses from permission to diagnosis: access to the earth does not by itself establish guidance.

### S19. P1 to P2: Heard Sound Becomes an Accountable Faculty
- Reading type: surface-primary
- Scene or process: P1 (67:7,10) to P2 (67:23); causal role progression: subjects first hear the blaze and regret failed listening, then hearing is named among the created instruments entrusted to them.
- Active motifs: auditory reception (`quranic:root_000741:B001/m01`); comprehension followed by compliance (`quranic:root_000741:B003/m01`); ear and auditory canal (`quranic:root_000741:B002/m02`).
- Ayah anchors: 67:7 `سَمِعُوا۟` (س م ع); 67:10 `نَسْمَعُ` (س م ع); 67:23 `ٱلسَّمْعَ` (س م ع).
- Synthesis: The bridge is a role progression from event, to failed response, to disclosed endowment. P1 separates exposure to sound from listening that changes conduct; P2 supplies the causal ground by identifying hearing as a made capacity. The regret is thus attached to misuse of an entrusted instrument, not to absence of access.

### S20. P1 to P2: The Examiner Becomes the Confronted Witness
- Reading type: surface-primary
- Scene or process: P1 (67:3-4) to P2 (67:27); reversal: the observer who repeatedly searches creation for a defect later occupies the position of one made to see the denied event at close range.
- Active motifs: sensory sight (`quranic:root_000531:B001/m01`); reflective judgment (`quranic:root_000531:B002/m01`); making another see (`quranic:root_000531:B012/m01`).
- Ayah anchors: 67:3 `تَرَىٰ/تَرَىٰ` (ر ء ي); 67:27 `رَأَوْهُ` (ر ء ي).
- Synthesis: Both pericopes stage an observer, an object, visual access, and a verdict, but agency reverses. In P1 the human gaze chooses its target and returns unable to establish a flaw; in P2 the denied object enters the visual field and alters the observers' faces. The canonical bridge is this transfer from examining creation to being confronted by what one's prior judgment excluded.

### S21. P1 to P2: A Retrospective Warning Becomes the Present Messenger's Office
- Reading type: surface-primary
- Scene or process: P1 (67:8-9) to P2 (67:17,26); role progression and causal sequence: keepers ask condemned arrivals whether a warner came, then the surah places a clear warner before its current hearers while the danger is still prospective.
- Active motifs: warning that awakens caution (`quranic:root_001488:B001/m01`); danger-report that induces caution (`quranic:root_001488:B001/m02`); warning-bearing agent (`quranic:root_001488:B001/m05`).
- Ayah anchors: 67:8 `نَذِيرٌۭ` (ن ذ ر); 67:9 `نَذِيرٌۭ` (ن ذ ر); 67:17 `نَذِيرِ` (ن ذ ر); 67:26 `نَذِيرٌۭ` (ن ذ ر).
- Synthesis: The bridge turns a completed liability inquiry into a live opportunity for caution. P1 shows warning after its rejection, as evidence in a terminal interview; P2 identifies the messenger now carrying that same role. The repeated scene is not merely "warning" as a topic: sender, agent, danger knowledge, recipient, response window, and consequence advance from report of failure to present address.

### S22. P1 to P2: Divine Knowledge Is Present Before Human Knowledge Arrives
- Reading type: surface-primary
- Scene or process: P1 (67:13-14) to P2 (67:17,26,29); contrast and role progression: the creator already knows concealed speech and created interiors, while human opponents are repeatedly told that they will come to know and that the event's knowledge remains with God.
- Active motifs: knowledge as disclosure (`quranic:root_001040:B001/m01`).
- Ayah anchors: 67:13 `عَلِيمٌۢ` (ع ل م); 67:14 `يَعْلَمُ` (ع ل م); 67:17 `فَسَتَعْلَمُونَ` (ع ل م); 67:26 `ٱلْعِلْمُ` (ع ل م); 67:29 `فَسَتَعْلَمُونَ` (ع ل م).
- Synthesis: The invariant is access to a state before or after disclosure; the roles are unequal. P1 locates knowledge prior to speech becoming public because creation itself is accessible to its maker. P2 delays human knowledge until warning or consequence discloses the matter and withholds the timing from the messenger. The bridge therefore contrasts continuous possession of knowledge with knowledge acquired only when the scene opens.

### S23. P1 to P2: Fear of the Unseen Reverses False Security
- Reading type: surface-primary
- Scene or process: P1 (67:12) to P2 (67:16-17,29); contrast and reversal: reverent fear without sight receives forgiveness, complacent security is destabilized by threats from ground and sky, and faith with reliance supplies the settled alternative.
- Active motifs: awe toward what is unseen (`quranic:root_000413:B001/m01`); settled safety and trust (`quranic:root_000054:B001/m01`); active reliance (`quranic:root_001681:B002/m01`).
- Ayah anchors: 67:12 `يَخْشَوْنَ` (خ ش ي); 67:16 `أَمِنتُم` (ء م ن); 67:17 `أَمِنتُم` (ء م ن); 67:29 `ءَامَنَّا` (ء م ن), `تَوَكَّلْنَا` (و ك ل).
- Synthesis: The bridge is a reversal of apparent emotional positions. P1's fear is not insecurity but correct orientation to an unseen Lord; P2's self-declared security is unstable because it assumes control of supporting media. Faith and reliance in 67:29 resolve the contrast by locating safety in the trusted relation rather than in confidence that earth and sky must remain harmless.

### S24. P1 to P2: Granted Provision Becomes a Withholding Counterfactual
- Reading type: surface-primary
- Scene or process: P1 (67:15) to P2 (67:21); causal sequence and reversal: people are authorized to eat an allotted provision, then asked who could continue supplying it if its source retained it.
- Active motifs: apportioned gift (`quranic:root_000560:B001/m01`); sustaining food (`quranic:root_000560:B002/m01`); general retention and prevention (`quranic:root_001424:B001/m02`).
- Ayah anchors: 67:15 `رِّزْقِهِۦ` (ر ز ق); 67:21 `يَرْزُقُكُمْ/رِزْقَهُۥ` (ر ز ق), `أَمْسَكَ` (م س ك).
- Synthesis: The repeated scene has giver, allotment, bodily intake, continued flow, and possible interruption. P1 presents provision at the point of permitted use; P2 runs the supply chain backward by removing release at its source. The bridge makes consumption evidence of dependence: possession of today's food does not confer control over tomorrow's issuance.

### S25. P1 to P2: The Upper Field Alternates Release and Holding
- Reading type: mixed
- Scene or process: P1 (67:5) to P2 (67:17,19); contrast through a repeated aerial scene: a luminary becomes a projectile, the sky can dispatch a grit-bearing force, and flying creatures remain aloft through an opposing operation of restraint.
- Active motifs: lamp or luminary (`quranic:root_000839:B005/m01`); violent wind carrying grit or hail (`quranic:root_000325:B003/m01`); dispatch and release (`quranic:root_000563:B001/m01`); light aerial flight (`quranic:root_000962:B001/m01`); holding, guarding, and preventing loss (`quranic:root_001424:B001/m01`).
- Ayah anchors: 67:5 `مَصَٰبِيحَ` (ص ب ح), `رُجُومًۭا` (ر ج م); 67:17 `يُرْسِلَ` (ر س ل), `حَاصِبًۭا` (ح ص ب); 67:19 `ٱلطَّيْرِ` (ط ي ر), `يُمْسِكُهُنَّ` (م س ك).
- Synthesis: The shared scene signature is an upper field, a moving body, a directed force, and a governed outcome. P1 emphasizes conversion into released impact; P2 places destructive dispatch beside sustained flight. The bridge is the operational contrast between letting force descend and holding vulnerable motion aloft, not a generic sky theme.

### S26. Whole Surah: Created Life Proceeds through Scattering to Gathering
- Reading type: surface-primary
- Scene or process: P1 (67:2,15) to P2 (67:24,28); causal sequence with terminal contrast: death and life are created as a test, resurrection is announced, created persons are spread through the earth and gathered, and ruin or mercy defines the final branch.
- Active motifs: loss of life and force (`quranic:root_001454:B001/m01`); ensouled life (`quranic:root_000383:B003/m01`); reviving the dead (`quranic:root_001503:B002/m01`); bringing created individuals into being and multiplying them (`quranic:root_000510:B001/m01`); gathering while driving toward a goal (`quranic:root_000324:B001/m01`); death, corruption, and annihilation (`quranic:root_001596:B001/m01`); compassion and beneficence (`quranic:root_000552:B001/m03`).
- Ayah anchors: 67:2 `ٱلْمَوْتَ` (م و ت), `ٱلْحَيَوٰةَ` (ح ي ي); 67:15 `ٱلنُّشُورُ` (ن ش ر); 67:24 `ذَرَأَكُمْ` (ذ ر ء), `تُحْشَرُونَ` (ح ش ر); 67:28 `أَهْلَكَنِىَ` (ه ل ك), `رَحِمَنَا` (ر ح م).
- Synthesis: The bridge is a causal life-course rather than a thematic list. P1 establishes the governing conditions and names return; P2 supplies the middle operation of dispersal and the convergent operation of muster, then places destruction and mercy as opposed outcomes. Each local scene retains its own placement; the whole-surah channel consists in their irreversible order from created animation to accountable regathering.


