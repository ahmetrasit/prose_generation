Surah: 55. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S55 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s055/surah.r2/text.md =====
# Surah 55

- 55:1 ٱلرَّحْمَٰنُ
- 55:2 عَلَّمَ ٱلْقُرْءَانَ
- 55:3 خَلَقَ ٱلْإِنسَٰنَ
- 55:4 عَلَّمَهُ ٱلْبَيَانَ
- 55:5 ٱلشَّمْسُ وَٱلْقَمَرُ بِحُسْبَانٍۢ
- 55:6 وَٱلنَّجْمُ وَٱلشَّجَرُ يَسْجُدَانِ
- 55:7 وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
- 55:8 أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ
- 55:9 وَأَقِيمُوا۟ ٱلْوَزْنَ بِٱلْقِسْطِ وَلَا تُخْسِرُوا۟ ٱلْمِيزَانَ
- 55:10 وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ
- 55:11 فِيهَا فَٰكِهَةٌۭ وَٱلنَّخْلُ ذَاتُ ٱلْأَكْمَامِ
- 55:12 وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ
- 55:13 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:14 خَلَقَ ٱلْإِنسَٰنَ مِن صَلْصَٰلٍۢ كَٱلْفَخَّارِ
- 55:15 وَخَلَقَ ٱلْجَآنَّ مِن مَّارِجٍۢ مِّن نَّارٍۢ
- 55:16 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:17 رَبُّ ٱلْمَشْرِقَيْنِ وَرَبُّ ٱلْمَغْرِبَيْنِ
- 55:18 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:19 مَرَجَ ٱلْبَحْرَيْنِ يَلْتَقِيَانِ
- 55:20 بَيْنَهُمَا بَرْزَخٌۭ لَّا يَبْغِيَانِ
- 55:21 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:22 يَخْرُجُ مِنْهُمَا ٱللُّؤْلُؤُ وَٱلْمَرْجَانُ
- 55:23 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:24 وَلَهُ ٱلْجَوَارِ ٱلْمُنشَـَٔاتُ فِى ٱلْبَحْرِ كَٱلْأَعْلَٰمِ
- 55:25 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:26 كُلُّ مَنْ عَلَيْهَا فَانٍۢ
- 55:27 وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو ٱلْجَلَٰلِ وَٱلْإِكْرَامِ
- 55:28 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:29 يَسْـَٔلُهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ كُلَّ يَوْمٍ هُوَ فِى شَأْنٍۢ
- 55:30 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:31 سَنَفْرُغُ لَكُمْ أَيُّهَ ٱلثَّقَلَانِ
- 55:32 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:33 يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ إِنِ ٱسْتَطَعْتُمْ أَن تَنفُذُوا۟ مِنْ أَقْطَارِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ فَٱنفُذُوا۟ ۚ لَا تَنفُذُونَ إِلَّا بِسُلْطَٰنٍۢ
- 55:34 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:35 يُرْسَلُ عَلَيْكُمَا شُوَاظٌۭ مِّن نَّارٍۢ وَنُحَاسٌۭ فَلَا تَنتَصِرَانِ
- 55:36 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:37 فَإِذَا ٱنشَقَّتِ ٱلسَّمَآءُ فَكَانَتْ وَرْدَةًۭ كَٱلدِّهَانِ
- 55:38 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:39 فَيَوْمَئِذٍۢ لَّا يُسْـَٔلُ عَن ذَنۢبِهِۦٓ إِنسٌۭ وَلَا جَآنٌّۭ
- 55:40 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:41 يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ
- 55:42 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:43 هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى يُكَذِّبُ بِهَا ٱلْمُجْرِمُونَ
- 55:44 يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- 55:45 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:46 وَلِمَنْ خَافَ مَقَامَ رَبِّهِۦ جَنَّتَانِ
- 55:47 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:48 ذَوَاتَآ أَفْنَانٍۢ
- 55:49 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:50 فِيهِمَا عَيْنَانِ تَجْرِيَانِ
- 55:51 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:52 فِيهِمَا مِن كُلِّ فَٰكِهَةٍۢ زَوْجَانِ
- 55:53 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:54 مُتَّكِـِٔينَ عَلَىٰ فُرُشٍۭ بَطَآئِنُهَا مِنْ إِسْتَبْرَقٍۢ ۚ وَجَنَى ٱلْجَنَّتَيْنِ دَانٍۢ
- 55:55 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:56 فِيهِنَّ قَٰصِرَٰتُ ٱلطَّرْفِ لَمْ يَطْمِثْهُنَّ إِنسٌۭ قَبْلَهُمْ وَلَا جَآنٌّۭ
- 55:57 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:58 كَأَنَّهُنَّ ٱلْيَاقُوتُ وَٱلْمَرْجَانُ
- 55:59 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:60 هَلْ جَزَآءُ ٱلْإِحْسَٰنِ إِلَّا ٱلْإِحْسَٰنُ
- 55:61 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:62 وَمِن دُونِهِمَا جَنَّتَانِ
- 55:63 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:64 مُدْهَآمَّتَانِ
- 55:65 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:66 فِيهِمَا عَيْنَانِ نَضَّاخَتَانِ
- 55:67 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:68 فِيهِمَا فَٰكِهَةٌۭ وَنَخْلٌۭ وَرُمَّانٌۭ
- 55:69 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:70 فِيهِنَّ خَيْرَٰتٌ حِسَانٌۭ
- 55:71 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:72 حُورٌۭ مَّقْصُورَٰتٌۭ فِى ٱلْخِيَامِ
- 55:73 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:74 لَمْ يَطْمِثْهُنَّ إِنسٌۭ قَبْلَهُمْ وَلَا جَآنٌّۭ
- 55:75 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:76 مُتَّكِـِٔينَ عَلَىٰ رَفْرَفٍ خُضْرٍۢ وَعَبْقَرِىٍّ حِسَانٍۢ
- 55:77 فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
- 55:78 تَبَٰرَكَ ٱسْمُ رَبِّكَ ذِى ٱلْجَلَٰلِ وَٱلْإِكْرَامِ


===== _commentary/v16/work/s055/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ح م (root_000552): 55:1 ٱلرَّحْمَٰنُ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ع ل م (root_001040): 55:2 عَلَّمَ, 55:4 عَلَّمَهُ, 55:24 كَٱلْأَعْلَٰمِ

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

## ق ر ء (root_001210): 55:2 ٱلْقُرْءَانَ

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

## ق ر ء (root_001211): 55:2 ٱلْقُرْءَانَ

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

## خ ل ق (root_000434): 55:3 خَلَقَ, 55:14 خَلَقَ, 55:15 وَخَلَقَ

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

## ء ن س (root_000059): 55:3 ٱلْإِنسَٰنَ, 55:14 ٱلْإِنسَٰنَ, 55:33 وَٱلْإِنسِ, 55:39 إِنسٌ, 55:56 إِنسٌ, 55:74 إِنسٌ

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

## ب ي ن (root_000170): 55:4 ٱلْبَيَانَ, 55:20 بَيْنَهُمَا, 55:44 بَيْنَهَا, 55:44 وَبَيْنَ

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

## ش م س (root_000818): 55:5 ٱلشَّمْسُ

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

## ق م ر (root_001255): 55:5 وَٱلْقَمَرُ

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

## ح س ب (root_000318): 55:5 بِحُسْبَانٍ

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

## ن ج م (root_001475): 55:6 وَٱلنَّجْمُ

- **B001** yıldız veya gökte görünen ışıklı cisim — yıldız; bazı bağlamlarda belirli bir yıldız kümesi · Ay'ın konaklarından biri · yıldızların bütünü
  النجم الثريا (maqayis;tahdhib)؛ كل كوكب يسمى نجما (ayn)؛ النجم واحد النجوم (jamhara)؛ النجم الكوكب (sihah)؛ النجوم تجمع الكواكب كلها (tahdhib)؛ أصل النجم الكوكب الطالع (mufradat)
- **B002** yükselip ortaya çıkmak; başlangıcı bulunmak — yükselip ortaya çıkmak, görünür olmak · bu işin bir başlangıcı ya da dayanağı yok · yükselip beliren, görünür olan · ortaya çıkan topluluk veya olay
  أصل صحيح يدل على طلوع وظهور (maqayis)؛ نجم النجم طلع (maqayis)؛ كل طالع ناجم (jamhara)؛ نجم الشيء ظهر وطلع (sihah)؛ نجم السن والقرن والنبت ونجم الخارجي (sihah)؛ يقال لكل ما طلع قد نجم (tahdhib)؛ ليس لهذا الأمر نجم أي أصل (tahdhib)
- **B003** gövdesiz, yerde yayılarak büyüyen bitki — gövdesiz, yerde yayılarak büyüyen bitki · ilkbaharda köklerden beliren sürgünler · yere yayılan küçük bitki
  النجم من النبات ما لم يكن له ساق (maqayis;sihah)؛ النجم من النبات ما لم يقم على ساق (ayn)؛ ما نجم من البقل على غير ساق (jamhara)؛ النجوم ما نجم من العروق أيام الربيع (ayn;tahdhib)؛ النجمة نبتة صغيرة (tahdhib)؛ النجمة تنبت ممتدة على وجه الأرض (tahdhib)
- **B004** belirli zamanda gelen taksit veya aşamalı bölüm — kutsal kitabın bölüm bölüm indirilen parçaları · taksit veya belirlenmiş ödeme zamanı · borcu belirli vadelere ve taksitlere bölmek
  النجوم وظائف الأشياء وكل وظيفة نجم (ayn;tahdhib)؛ نجوم القرآن أنزل جملة ثم أنزل نجوما (ayn)؛ الوقت الذي يحل فيه الدين (jamhara)؛ نجمت الدين تنجيما (jamhara)؛ نجمت المال إذا أديته نجوما (sihah)؛ نزول القرآن نجما بعد نجم (tahdhib)؛ الديون المنجمة (tahdhib)
- **B005** yıldızları gözlemek; bir işi düşünüp tasarlamak — bir işi nasıl yürüteceğini düşünüp tartmak · yıldızları gözleyen kişi · yıldızları gözlemek; uykusuzca onları izlemek
  نظر النجوم (ayn)؛ المنجم الذي ينظر في النجوم (ayn)؛ تنجم الرجل إذا نظر في النجوم (jamhara)؛ تنجم إذا رعى النجوم من سهر (jamhara)؛ نظر في النجوم أي تفكر ليدبر حجة (tahdhib)؛ يقال للإنسان إذا تفكر في أمر لينظر كيف يدبره نظر في النجوم (tahdhib)
- **B006** özel adlandırma kümesi — terazinin dilini taşıyan enine demir parça · atın art ayağındaki iki çıkıntılı kemik · açık seçik yol · kişinin iki topuğu · günün doğup belirdiği yer veya an
  المنجم في الميزان الحديدة المعترضة التي فيها اللسان (maqayis;sihah)؛ منجما الفرس العظمان الناتئان دوين العرقوب (jamhara)؛ المنجم الطريق الواضح (tahdhib)؛ منجما الرجل كعباها (tahdhib)؛ المنجم منجم النهار حين ينجم (tahdhib)
- **B007** göğün açılması veya yağmurun ya da soğuğun kesilmesi [kalıp] — gökyüzünün açılması ve yıldızların görünmesi · yağmurun ya da soğuğun kesilmesi
  أنجمت السماء بدت نجومها (ayn)؛ أنجمت السماء أقشعت (sihah)؛ أنجم البرد وأنجم المطر أقلع (sihah)؛ أنجم المطر إذا أقلع (tahdhib)
- **B008** kötülük ve sapkınlığın kaynağı olan kimse [kalıp] — kötülük ve sapkınlığın çıktığı kaynak kişi
  فلان منجم الباطل والضلالة أي معدنه (sihah)

## ش ج ر (root_000777): 55:6 وَٱلشَّجَرُ

- **B001** gövdeli bitki; ağaçlık yer ve ağaç otlatma kullanımları — ağaç, gövdeli bitki · tek bir ağaç · ağaç topluluğu, ağaçlık · ağacı bol vadi · ağacı bol arazi · çok ağaç yetişen yer, ağaçlık · daha ağaçlık, ağacı daha bol · ot kalmayınca hayvanların ağaçları otlaması
  الشجر معروف الواحدة شجرة؛ الشجر كل نبت له ساق (maqayis;mufradat)؛ واد شجير كثير الشجر (maqayis;jamhara;sihah;mufradat)؛ المشجرة أرض تنبت الشجر الكثير (ayn;sihah;tahdhib)؛ شاجر المال إذا صار إلى الشجر يرعاه (sihah;tahdhib)
- **B002** sözlerin birbirine karıştığı çekişme — aralarında anlaşmazlık çıkmak · çekişip sözleri birbirine karışmak
  شجر بين القوم الأمر إذا اختلفوا وتشاجروا فيه (maqayis)؛ قد شجر بينهم أمر وخصومة أي اختلط واختلف (ayn)؛ التشاجر في الخصومة إذا دخل كلام بعضهم في بعض (jamhara)؛ شجر بين القوم إذا اختلف الأمر بينهم (sihah)؛ وقع من الاختلاف من الخصومات حتى اشتجروا وتشاجروا (tahdhib)؛ الشجار المشاجرة والتشاجر المنازعة (mufradat)
- **B003** mızraklarla çarpışma, mızrakların iç içe geçmesi ve mızrak saplama [kalıp] — mızraklarla çarpışmak, mızrakları birbirine geçmek · ona mızrak saplamak · birbirinin arasına giren mızraklar
  تشاجر القوم بالرماح تطاعنوا بها (maqayis;jamhara;sihah)؛ الرماح شواجر يختلف بعضا في بعض (ayn)؛ التقى فئتان فتشاجروا برماحهم أي تشابكوا (tahdhib)؛ شجره بالرمح أي طعنه بالرمح (sihah;tahdhib;mufradat)
- **B004** birleştirilmiş taşıyıcı, dayanak, askı ya da engel ağaçları — birleştirilmiş taşıyıcı ya da dayanak ağaçları · giysi askılığı · kadınların bindiği ahşap taşıt ya da tahtırevan çubukları
  الشجار خشب الهودج (maqayis;ayn;tahdhib;mufradat)؛ الشجار عصي تجمع كالمحفة (jamhara)؛ المشجر المشجب (sihah)؛ الخشبة التي توضع خلف الباب والشجار خشب البئر (sihah;tahdhib)؛ عود يجعل في فم الجدي لئلا يرضع أمه (tahdhib)
- **B005** ağız-çene birleşimi ve buna bağlı çeneyi dayama ya da ağzı çubukla açma — iki çene arası, çene ya da ağız açıklığı · çenenin iki ucu · elini çenesinin altına koyup dayanmak · ağzına çubuk sokup açmak · oğlan çocuğunun çenesindeki küçük benek
  الشجر مفرج الفم (maqayis;ayn;tahdhib)؛ الشجر الذقن بعينه (maqayis;jamhara)؛ الشجران طرفا اللحيين (jamhara)؛ الشجر بالفتح ما بين اللحيين (sihah;tahdhib)؛ اشتجر الرجل إذا وضع يده تحت شجره على حنكه (sihah;tahdhib)؛ شجروا فاها أي أدخلوا فيه عودا ففتحوه (tahdhib)
- **B006** sarkanı kaldırıp uzaklaştırma; başka yöne çevirme; uzaklaşıp kurtulma — sarkan şeyi kaldırıp geriye almak · onu başka yöne çevirmek, uzaklaştırmak · aralanmak, uzaklaşıp kurtulmak
  شجرت الشيء إذا تدلى فرفعته (maqayis;ayn;tahdhib)؛ ما شجرك عنه أي ما صرفك (sihah;mufradat)؛ شجرت فلانا إذا صرفته (tahdhib)؛ شجر الشيء إذا نحاه (tahdhib)؛ الاشتجار والانشجار النجاء (tahdhib)
- **B007** kendi topluluğundan ya da takımından olmayan yabancı unsur — yabancı kişi ya da deve; bazı aktarımlarda arkadaş veya karışmış kişi · ödünç ya da ait olmadığı okların arasına katılmış ok
  الشجير الغريب الذي لا قدح له (ayn)؛ الشجير الغريب من الناس والإبل (sihah;tahdhib)؛ القدح الشجير هو المستعار (tahdhib)؛ كل قدح كان من غير النبع فهو شجير (jamhara)؛ ألقوه في القداح التي ليست من شجرها (sihah)
- **B008** ağaç biçimli resim ya da desen — ağaç biçiminde resmedilmiş ya da desenlenmiş · ağaç desenli ipekli kumaş
  المشجر ضرب من التصاوير على صفة الشجر (ayn)؛ ديباج مشجر نقشه على هيئة الشجر (sihah)؛ المشجر من التصاوير ما يصور على صيغة الشجر (tahdhib)
- **B009** kutlu bir soydan gelmek [kalıp] — kutlu bir soydan gelmek
  فلان من شجرة مباركة أي من أصل مبارك (tahdhib)

## س ج د (root_000675): 55:6 يَسْجُدَانِ

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

## س م و (root_000745): 55:7 وَٱلسَّمَآءَ, 55:29 ٱلسَّمَٰوَٰتِ, 55:33 ٱلسَّمَٰوَٰتِ, 55:37 ٱلسَّمَآءُ, 55:78 ٱسْمُ

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

## و س م (root_001650): documented alternative for 55:78 ٱسْمُ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı (also echo for 55:7 وَٱلسَّمَآءَ, 55:29 ٱلسَّمَٰوَٰتِ, 55:33 ٱلسَّمَٰوَٰتِ, 55:37 ٱلسَّمَآءُ, 55:41 بِسِيمَٰهُمْ)

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

## ر ف ع (root_000582): 55:7 رَفَعَهَا

- **B001** bir şeyi yukarı kaldırmak — bir şeyi bulunduğu yerden yukarı kaldırmak · kendiliğinden yükselmek · yapıyı yükseltip uzatmak · üst üste serilmiş döşekler · onu göğe çıkarmak veya onurlandırmak · bir şeyi eliyle kaldırmak
  رفعت الشيء رفعا وهو خلاف الخفض (maqayis;ayn); الرفع ضد الخفض (tahdhib); الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها (mufradat); في البناء إذا طولته (mufradat)
- **B002** saygınlığı yüksek olmak veya yükseltmek — değerli ve onurlu döşekler · anılışını yüceltmek · konumunu ve saygınlığını yükseltmek · saygın ve yüksek konumlu · yüksek saygınlık ve onur · bir topluluğu alçaltıp diğerini yükselten · onu göğe çıkarmak veya onurlandırmak · değerli ve onurlandırılmış sayfalar · evleri onurlandırıp yüceltmek
  رفع الرجل يرفع رفاعة فهو رفيع إذا شرف (ayn;tahdhib); رجل رفيع أي شريف (sihah); الرفعة نقيض الذلة (tahdhib); في الذكر إذا نوهته (mufradat); في المنزلة إذا شرفتها (mufradat)
- **B003** bineğin orta-üst hızda ilerlemesi veya ilerletilmesi — devenin yürüyüşünü hızlandırmak · ağır yürüyüşle tam koşu arasında hızlı gidiş · hızı yer yer artan koşu
  مرفوع الناقة في سيرها خلاف الموضوع (maqayis); المرفوع من حضر الفرس والبرذون دون الحضر وفوق الموضوع (ayn;tahdhib); رفع البعير في السير أي بالغ (sihah); مرفوع السير شديدة (mufradat)
- **B004** yaklaştırmak veya yetkili önüne sunmak — kullanacaklara yaklaştırılmış döşekler · yaklaştırma · yönetici veya yargıç önüne sunmak · yargılanması için yetkili önüne çıkarmak · dilekçesini veya şikayetini sunmak · onu iki perdenin bulunduğu yere kadar ilerletmek · bir topluluğu savaşta öne sürmek
  الرفع تقريب الشيء (maqayis;sihah); رفعته للسلطان (maqayis); رفعته إلى السلطان (sihah); رفعت فلانا إلى الحاكم أي قدمته إليه (tahdhib); رفعت قصتي قدمتها (tahdhib)
- **B005** haberi açığa çıkarıp yaymak — açığa çıkarıp yayma · birinin yönetici hakkındaki haberini yaymak · iletileni duyurup yayan topluluk
  الرفع إذاعة الشيء وإظهاره (maqayis); كل رافعة رفعت علينا من البلاغ (maqayis;sihah;tahdhib); رفع فلان على العامل إذا أذاع خبره (maqayis;tahdhib); أذاع خبر ما احتجبه (mufradat)
- **B006** hasat ürününü harman yerine taşımak — hasat edilen ürünü harman yerine taşımak · ürünün harman yerine taşındığı dönem veya bu iş
  رفع الزرع أن يحمل بعد الحصاد إلى البيدر (maqayis;sihah); جاء زمن الرفاع إذا رفع الزرع (tahdhib); الرفاع أن يحصد الزرع ويرفع (tahdhib)
- **B007** dişi devenin sütünü memesinde tutması [kalıp] — sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve
  ناقة رافع إذا رفعت اللبأ في ضرعها (maqayis;sihah); التي رفعت لبنها فلم تدر رافع (tahdhib)
- **B008** kalçayı büyük gösteren dolgu — kadının kalçasını büyük göstermek için kullandığı dolgu
  الرفاعة ما تتعظم به المرأة الرسحاء (sihah); الرفاعة شيء تعظم به المرأة عجيزتها (tahdhib); الرفاعة ما ترفع به المرأة عجيزتها (mufradat)
- **B009** bağı yukarı çekmeye yarayan ip — bağlı kişinin bağını yukarı çekmekte kullandığı ip · bağlı kişinin elinde tutup bağını kaldırdığı ip
  رفاعة المقيد خيط يرفع به قيده إليه (sihah); الرفاع حبل القيد يأخذه المقيد بيده يرفعه إليه (tahdhib)
- **B010** sesin yüksekliği [kalıp] — sesin yüksekliği
  في صوته رفاعة ورفاعة (sihah;tahdhib); إذا كان رفيع الصوت (tahdhib)
- **B011** toplulukça ülke içinde ilerlemek — topluluğun ülke içinde yola koyulup ilerlemesi · yolculukta ilerleyenler
  رفع القوم فهم رافعون إذا أصعدوا في البلاد (tahdhib); الروافع إذا رفعوا في سيرهم (tahdhib)
- **B012** dil bilgisinde ötreye karşılık gelen çekim durumu — dil bilgisinde ötreye karşılık gelen çekim durumu
  الرفع في الإعراب كالضم في البناء (sihah); وهو من أوضاع النحويين (sihah)

## و ض ع (root_001657): 55:7 وَوَضَعَ, 55:10 وَضَعَهَا

- **B001** bir şeyi indirip yerine koyma; konduğu yer — bir şeyi yerine koymak veya elden bırakmak · yer, konum · yerine konmuş şey · ev yapmak veya kurmak · yazılı kayıtları ortaya çıkarmak
  أصل واحد يدل على الخفض للشيء وحطه (maqayis)؛ الوضع مصدر قولك وضع يضع (ayn)؛ الموضع المكان ومصدر وضعت الشيء من يدي (sihah)؛ وضعت الشيء أضعه وضعا وهو ضد رفعته (tahdhib)؛ الوضع أعم من الحط ومنه الموضع (mufradat)
- **B002** doğumla yükü bırakma ve özel gebe kalma zamanı — kadının çocuğunu doğurması · adet öncesi temizlik sonunda gebe kalma
  وضعت المرأة ولدها (maqayis)؛ وضعت المرأة وضعا بالفتح أي ولدت (sihah)؛ وضعت المرأة فهي تضع وضعا وتضعا فهي واضع (tahdhib)؛ وضعت المرأة الحمل وضعا (mufradat)؛ ما حملته أمه وضعا أي ما حملته على حيض (tahdhib)
- **B003** hayvanın hızlı ya da özel yürüyüşle ilerlemesi — bineğin hızlı gitmesi veya koşması · sürücünün bineği hızlandırması · bu yürüyüşü güzel olan
  الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع (maqayis)؛ الدابة تضع السير وضعا وهو سير دون (ayn)؛ وضع البعير وغيره أي أسرع في سيره (sihah)؛ وضع البعير إذا عدا وأوضعته أنا (tahdhib)؛ وضعت الدابة تضع في سيرها وضعا أسرعت (mufradat)
- **B004** ticarette zarar ve sermaye indirimi — ticarette zarar etmek · sermayeden düşülen indirim veya eksilti
  وضع في تجارته يوضع خسر (maqayis)؛ الوضيعة ما تضعه من رأس مالك (ayn)؛ وضع الرجل في تجارته خسر (sihah)؛ الوضيعة الحطيطة وقد استوضع (tahdhib)؛ الوضيعة الحطيطة من رأس المال (mufradat)
- **B005** düşük konum ve kendini alçaltma — düşük konumlu kişi · aşağı konum, düşüklük · kendini alçaltarak boyun eğme
  الوضيع الرجل الدني (maqayis)؛ الوضاعة الضعة (ayn)؛ الوضيع الدنئ من الناس وفي حسبه ضعة (sihah)؛ رجل وضيع ضد الشريف والتواضع التذلل (tahdhib)؛ رجل وضيع بين الضعة في مقابلة رفيع (mufradat)
- **B006** yerleştirilmiş topluluk, kayıtlı asker ya da yük — başka bir yere taşınıp yerleştirilen topluluklar · bölgeye kaydedilen askerler veya topluluğun yükleri
  الوضائع قوم ينقلون من أرض إلى أرض (maqayis)؛ الوضيعة نحو وضائع كسرى (ayn)؛ الوضيعة واحدة الوضائع وهي أثقال القوم (sihah)؛ الوضيعة قوم من الجند يجعل أسماؤهم في كورة (tahdhib)
- **B007** devenin tuzcul otu otlaması ve orada konaklaması — tuzcul otu otlayan veya yanında konaklayan dişi deve · tuzcul bitkiyi otlayan develer · tuzcul yemlik bitki veya develerin kaldığı otlak
  الواضعات الإبل تأكل الخلة (maqayis)؛ ناقة واضعة للتي ترعاها وأصحاب الوضيعة أصحاب حمض (sihah)؛ إبل واضعة أي مقيمة في الحمض (tahdhib)؛ الحمض يقال له الوضيعة والجمع وضائع (tahdhib)
- **B008** kumaşa pamuk serip dikme — kumaşa pamuk koyma veya sonra giysiyi dikme
  الخياط يوضع القطن على الثوب توضيعا (ayn)؛ التوضيع خياطة الجبة بعد وضع القطن (sihah)؛ الخياط يوضع القطن توضيعا على الثوب (tahdhib)
- **B009** baş örtüsünü çıkarıp baş örtüsüz kalma [kalıp] — baş örtüsünü çıkardığı için baş örtüsüz kadın
  وضعت المرأة خمارها وامرأة واضع أي لا خمار عليها (sihah)؛ امرأة واضع بغير هاء إذا وضعت خمارها (tahdhib)
- **B010** saklaması için birine bırakma [kalıp] — bir şeyi saklaması için birinin yanına bırakmak
  وضعت عند فلان وضيعا أي استودعته وديعة (sihah)؛ يقال للوديعة وضيع وقد وضعت عند فلان وضيعا إذا استودعته وديعة (tahdhib)
- **B011** karşılıklı anlaşma ve görüşme — bir işte karşılıklı anlaşmak ve onu görüşmek · karşılıklı para koymalı sözleşme veya satışı bırakma
  المواضعة أن تواضع أخاك أمرا فتناظره فيه (ayn)؛ المواضعة المراهنة والمواضعة متاركة البيع وواضعته في الأمر (sihah)؛ المواضعة أن تواضع صاحبك أمرا تناظره فيه (tahdhib)
- **B012** sağlamlık eksikliği ve kusurlu yumuşama — işi veya yapısı sağlam olmayan, kadınsı sayılan kişi · kadın konuşmasına benzetilen yumuşama · alt bacağını yayarak yürüyen kusurlu at
  الرجل الموضع الذي ليس بمستحكم الأمر (maqayis)؛ في كلامه توضيع إذا كان فيه تأنيث كلام النساء (ayn)؛ رجل موضع أي مطرح ليس بمستحكم الخلق (sihah)؛ يقال في فلان توضيع أي تخنيث وفلان موضع إذا كان مخنثا (tahdhib)؛ فرس موضع إذا كان يفترش وظيفه وهو عيب (tahdhib)
- **B013** binmek için devenin boynunu alçaltma — binmek için devenin boynunu veya başını alçaltması
  الاتضاع أن تخفض رأس البعير لتضع قدمك على عنقه فتركب (sihah)؛ اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه (tahdhib)

## و ز ن (root_001645): 55:7 ٱلْمِيزَانَ, 55:8 ٱلْمِيزَانِ, 55:9 ٱلْوَزْنَ, 55:9 ٱلْمِيزَانَ

- **B001** tartarak veya yaklaşık ölçüp biçerek niceliği belirleme — bir şeyi tartmak veya ölçüsünü belirlemek · hurma ürününün miktarını yaklaşık kestirmek · bir şeyin ağırlık ölçüsü · bir dirhem ağırlığında gelmek · bir kimse için veya ona karşı bir şeyi tartmak · kendisi için tartılanı teslim almak
  وزنت الشيء وزنا؛ الزنة قدر وزن الشيء (maqayis)؛ الوزن ثقل شيء بشيء مثله؛ وزن الشيء إذا قدره؛ وزن ثمر النخل إذا خرصه (ayn;tahdhib)؛ وزنت الشئ وزنا وزنة؛ هذا يزن درهما (sihah)؛ الوزن معرفة قدر الشيء؛ ما يقدر بالقسط والقبان (mufradat)
- **B002** tartı aracı ve adil değerlendirme ölçütü — terazi · teraziler ve tartı ağırlıkları · hesapta adil ve denk değerlendirme
  بناء يدل على تعديل واستقامة (maqayis)؛ الميزان ما وزنت به (ayn)؛ الميزان معروف (sihah)؛ الموازين واحدها ميزان وهو المثاقيل؛ الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل (tahdhib)؛ مراعاة المعدلة؛ الوزن يومئذ الحق فإشارة إلى العدل في محاسبة الناس (mufradat)
- **B003** iki şeyi denk veya karşılıklı konumda tutma — iki şeyi karşılaştırıp birbirine denklemek · bu, ötekiyle aynı ölçüde veya onun hizasındadır · dağın yanı veya hizası · bu, ötekiyle zihinde denk tutulur
  هذا يوازن ذلك أي هو محاذيه (maqayis)؛ وازنت بين الشيئين؛ هذا يوازن هذا إذا كان على زنته أو كان محاذيه؛ هو وزن الجبل أي ناحية منه؛ هو زنة الجبل أي حذاءه (sihah)؛ هذا في وزن هذا؛ قام في النفس مساويا لغيره (tahdhib)
- **B004** günün tam ortasına gelmesi [kalıp] — gün ortalandı
  قام ميزان النهار إذا انتصف النهار (maqayis;mufradat)؛ قام ميزان النهار أي انتصف (sihah)
- **B005** sağlam yargı ve kararlı yöneliş [kalıp] — sağlam ve ağırbaşlı düşünceli · yargısı güçlü ve aklı sağlam · kendini o işe hazırlayıp kararlılıkla yönelmek
  وزين الرأى معتدله؛ راجح الوزن إذا نسبوه إلى رجاحة الرأي وشدة العقل (maqayis)؛ رجل وزين الرأي وقد وزن وزانة إذا كان متثبتا (ayn;tahdhib)؛ فلان وزين الرأي أي رزينه (sihah)؛ أوزن فلان نفسه على الأمر إذا وطن نفسه عليه (tahdhib)
- **B006** kısa boylu, kimi kullanımda aklı başında kadın — kısa boylu kız · kısa boylu, aklı başında kadın · kısa boylu kadın
  جارية موزونة فيها قصر (ayn;tahdhib)؛ امرأة موزونة قصيرة عاقلة؛ الوزنة المرأة القصيرة (tahdhib)
- **B007** toplumsal değer; eksiksiz ağırlıktaki para [kalıp] — bizim yanımızda hiçbir değeri ve saygınlığı yok · onlara hiçbir değer ve saygınlık tanımayız · tam ağırlıktaki dirhem
  درهم وازن أي تام (sihah)؛ ما لفلان عندنا وزن أي قدر لخسته؛ فلا نقيم لهم يوم القيامة وزنا (tahdhib)؛ فلا نقيم لهم يوم القيامة وزنا (mufradat)
- **B008** ölçülü ve dengeli yaratılmış şey [kalıp] — ölçülü ve dengeli yaratılmış şey
  بناء يدل على تعديل واستقامة (maqayis)؛ وأنبتنا فيها من كل شيء موزون؛ قيل هو المعادن كالفضة والذهب؛ كل ما أوجده الله وأنه خلقه باعتدال (mufradat)

## ط غ ي (root_000937): 55:8 تَطْغَوْا۟

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

## ECHO ط غ و (root_000936): for 55:8 تَطْغَوْا۟: withheld observed target; not identity

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

## ق و م (root_001273): 55:9 وَأَقِيمُوا۟, 55:46 مَقَامَ

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

## ق س ط (root_001224): 55:9 بِٱلْقِسْطِ

- **B001** hakkı gözetme ve adil davranma — hükümde ve paylaşımda adalet · adil davranmak ve hakkaniyetle paylaştırmak · adil ve hakkaniyetli kişi
  القسط العدل؛ أقسط يقسط؛ الإقساط العدل في القسمة والحكم؛ أقسطت بينهم وأقسطت إليهم؛ أقسط الرجل فهو مقسط؛ الإقساط أن يعطي قسط غيره
- **B002** haktan sapma ve haksızlık — haksızlık ve haktan sapma · haksızlık etmek ve haktan sapmak · haktan ayrılma ve sapma · haksızlık eden ve haktan sapan kişi
  القسط بفتح القاف الجور؛ القسوط العدول عن الحق؛ القسوط الميل عن الحق؛ القسوط الجور والعدول عن الحق؛ قسط الرجل إذا جار
- **B003** pay ve eşitçe paylaştırma — pay ve hisse · şeyi aralarında eşitçe bölüşmek
  القسط النصيب؛ تقسطنا الشيء بيننا؛ القسط الحصة والنصيب؛ تقسطوا بينهم الشيء أي اقتسموه بالتسوية؛ أخذ كل واحد منهم قسطه أي حصته؛ تقسطوا الشيء بينهم أي اقتسموه على السواء والعدل؛ تقسطنا بيننا أي اقتسمنا
- **B004** doğru tartan terazi — doğru ve güvenilir terazi
  القسطاس الميزان؛ القسطاس والقسطاس أقوم الموازين؛ هو أقوم الموازين وبعضهم يقول هو الشاهين؛ القسطاس الميزان ويعبر به عن العدالة
- **B005** bacak eğriliği veya dikliği; uzuvlarda kuruyup sertleşme — bacaklarda eğrilik · bacakları eğri dişi · bacak sinirleri doğuştan sert deve · kemikleri zayıflıktan kuruyup sertleşmek
  القسط اعوجاج في الرجلين؛ رجل قسطاء في ساقها اعوجاج؛ القسط خلاف الفحج؛ القسط بالتحريك انتصاب في رجلي الدابة؛ الأقسط من الإبل الذي في عصب قوائمه يبس؛ وقد يكون القسط يبسا في العنق؛ قسطت عظامه قسوطا إذا يبست من الهزال؛ في رجله قسط وهو أن تكون الرجل ملساء الأسفل
- **B006** tütsü ve ilaçta kullanılan Hint kökenli kokulu odun — tütsü ve ilaçta kullanılan Hint kökenli kokulu odun
  القسط شيء يتبخر به عربي؛ القسط عود هندي يجعل في البخور والدواء؛ القسط بالضم من عقاقير البحر؛ القسط عود يجاء به من الهند يجعل في البخور والدواء؛ يقال لهذا البخور قسط وكسط وكشط
- **B007** su ve başka maddeler için miktar veya ölçü birimi — belirli miktar veya ölçü birimi
  كل مقدار فهو قسط في الماء وغيره؛ القسط أيضا مكيال وهو نصف صاع؛ الفرق ستة أقساط؛ القسط أربعمائة واحد وثمانون درهما؛ القسط نصف الصاع
- **B008** gökkuşağı — gökkuşağı · gökkuşağı · gökkuşağı
  القسطانة قوس قزح؛ يقال لقوس الله القسطاني؛ القسطان قوس قزح
- **B009** birbirinden ayrı topluluk kümeleri — birbirinden ayrı topluluklar
  إذ هن أقساط كرجل الدبى؛ أراد أنها جماعات في تفرقة
- **B010** ev halkına yapılan harcamayı kısmak [kalıp] — ev halkına yapılan harcamayı kısmak
  قسط على عياله النفقة تقسيطا أي قترها
- **B011** toz — toz
  القسطان والكسطان الغبار

## خ س ر (root_000409): 55:9 تُخْسِرُوا۟

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

## ء ر ض (root_000025): 55:10 وَٱلْأَرْضَ, 55:29 وَٱلْأَرْضِ, 55:33 وَٱلْأَرْضِ

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

## ء ن م (root_000061): 55:10 لِلْأَنَامِ

- **B001** yeryuzundeki butun yaratilmislardan olusan topluluk — yeryuzu uzerindeki butun yaratilmislardan olusan topluluk · insanlar ve cinler · siir dilinde yeryuzundeki butun yaratilmislari anlatan bicim
  الأَنام ما على ظهر الأرض من جميع الخلق؛ يجوز في الشعر الأَنيم؛ الأَنام هم الجن والإنس

## ف ك ه (root_001174): 55:11 فَٰكِهَةٌ, 55:52 فَٰكِهَةٍ, 55:68 فَٰكِهَةٌ

- **B001** neşeli hoşnutluk içinde olup elindekinin tadını çıkarma — neşeli, güler yüzlü ve şakacı · rahatlık içinde, elindekinden hoşnut · kendisine verilenlerden hoşnut ve memnun · neşeli ve şakacı olma hali · ondan tat alıp yararlandım · yiyeceği veya meyveyi tat alarak yemek · neşeli ve şakacı kimse · neşeli ve şakacı kadın
  الرجل الفكه الطيب النفس (maqayis)؛ فاكهين أي ناعمين معجبين بما هم فيه والفكه الطيب النفس (ayn)؛ فكه إذا كان طيب النفس مزاحا وفاكهين أي ناعمين وتفكهت بالشيء تمتعت به (sihah)؛ الفكه الطيب النفس الضحوك والفاكه أيضا الناعم والفكه المعجب (tahdhib)
- **B002** yenmesi hoş meyve — meyve; yenmesi hoş bulunan ürünler · topluluğa meyve yedirmek veya sunmak · meyve satıcısı · yiyeceği veya meyveyi tat alarak yemek
  الفاكهة لأنها تستطاب وتستطرف (maqayis)؛ كل الثمار فاكهة وفكهت القوم بالفاكهة تفكيها (ayn)؛ الفاكهة معروفة وأجناسها الفواكه والفاكهاني الذي يبيعها (sihah)؛ كل الثمار فاكهة ولم يخرجهما من الفاكهة (tahdhib)؛ الفاكهة قيل هي الثمار كلها وقيل ما عدا العنب والرمان (mufradat)
- **B003** tatlı sözlerle şakalaşma — neşeli ve şakacı olma hali · şaka ve yakın kimselerin sıcak söyleşisi · tatlı sözlerle karşılıklı şakalaşma · toplulukla tatlı sözlerle şakalaşmak · şakacı kimse
  المفاكهة وهي المزاحة وما يستحلى من كلام (maqayis)؛ فاكهتهم مفاكهة بملح الكلام والمزاح والفكاهة المزاح والفاكه المازح (ayn)؛ الفكاهة المزاح والمفاكهة الممازحة (sihah)؛ فاكهت مازحت والفاكه ههنا المازح (tahdhib)؛ الفكاهة حديث ذوي الأنس (mufradat)
- **B004** doğumdan önce sütün gelmesi veya koyulaşması — devenin doğumdan önce sütünün gelmesi veya koyulaşması · doğumu yaklaşmış ve sütü belirginleşmiş deve · doğumdan önce sütü akmaya başlayan deve
  أفكهت الناقة والشاة إذا درتا عند أكل الربيع وكان في اللبن أدنى خثورة وهو أطيب اللبن (maqayis)؛ أفكهت الناقة إذا رأيت في لبنها خثورة قبل أن تضع فهي مفكه (ayn)؛ أفكهت الناقة إذا درت عند أكل الربيع قبل أن تضع فهي مفكهة (sihah)؛ المفكه من النوق التي يهراق لبنها عند النتاج قبل أن تضع وقد أفكهت وناقة مفكهة ومفكه (tahdhib)
- **B005** özel adlandırma kümesi — 
  فليس من هذا وهو من باب الإبدال والأصل تفكنون وهو من التندم (maqayis)؛ تفكهنا من كذا أي تعجبنا ويقال تفكهون تندمون (ayn)؛ تفكه تعجب ويقال تندم (sihah)؛ تتعجبون مما نزل بكم ويقال معنى فظلتم تندمون وكذلك تفكنون (tahdhib)؛ تفكهون قيل تتعاطون الفكاهة وقيل تتناولون الفاكهة (mufradat)
- **B006** şımarık ve küstah taşkınlık — şımarık, küstah ve ölçüsüz
  وما كان لأهل النار فكهين أي أشرين بطرين (ayn)؛ والفكه أيضا الأشر البطر وقرئ فكهين أي أشرين (sihah)؛ الفكه الأشر وما كان من وصف أهل النار فكهين يعني أشرين بطرين (tahdhib)
- **B007** birini arkasından kötüleyip çekiştirme [kalıp] — insanların saygınlığına dil uzatıp onları çekiştirmek · birini arkasından kötüleyip çekiştirmek
  يتفكه بالطعام أو بالفاكهة أو بأعراض الناس؛ تركت القوم يتفكهون بفلان أي يغتابونه ويتناولون منه؛ الفكه الذي ينال من أعراض الناس (tahdhib)

## ن خ ل (root_001483): 55:11 وَٱلنَّخْلُ, 55:68 وَنَخْلٌ

- **B001** hurma ağacı ve hurma ağaçları — hurma ağacı; topluluk adı olarak hurma ağaçları · bir hurma ağacı · hurma ağaçları
  النخل سمي به لأنه أشرف كل شجر ذي ساق والواحدة نخلة (maqayis)؛ النخلة شجرة التمر والجماعة نخل ونخيل (ayn)؛ والنخل معروف يذكر ويؤنث (jamhara)؛ النخل والنخيل بمعنى والواحدة نخلة (sihah)؛ النخل معروف وقد يستعمل في الواحد والجمع وجمعه نخيل (mufradat)
- **B002** elekten geçirerek ayırma — unu elemek ve elekten geçirerek ayırmak · kepek; eleme sırasında undan ayrılan kaba artık · undan ayrılan eleme artığı · elek · eleme ve elekten geçirerek ayırma
  النخل نخلك الدقيق بالمنخل وما سقط منه فهو نخالة (maqayis)؛ فالنخل التصفية (ayn)؛ نخلت الدقيق وغيره وما سقط منه فهو نخالة ونخال (jamhara)؛ نخل الدقيق غربلته والنخالة ما يخرج منه والمنخل ما ينخل به (sihah)؛ النخل نخل الدقيق بالمنخل (mufradat)
- **B003** inceleyip en iyisini seçme — bir şeyi inceleyip en iyisini seçmek · bir şeyi seçip ayırmak · gönlümün seçtiği kişi · seçilmiş şey · bir şeyin en iyisini araştırıp seçmek
  كلمة تدل على انتقاء الشيء واختياره وانتخلته استقصيت حتى أخذت أفضله (maqayis)؛ الانتخال الاختيار لنفسك أفضله وهو التنخل أيضا (ayn)؛ انتخلت الشيء إذا اخترته وتنخلته أيضا وفلان نخيلة نفسي أي تنخلته واخترته (jamhara)؛ انتخلت الشيء استقصيت أفضله وتنخلته تخيرته (sihah)؛ انتخلت الشيء انتقيته فأخذت خياره (mufradat)
- **B004** karın ya da yağmurun tane tane düşmesi — karın ve yağmurun tane tane düşmesi · gece kar yağdı ya da bol olmayan yağmur aldı
  النخل تنخيل الثلج والودق؛ وانتخلت ليلتنا الثلج أو مطرا غير جود (ayn)
- **B005** bir tanıklıkta hurma biçimli takı türü — hurma ağacı biçimli bir takı türü
  والنخل ضرب من الحلي على صورة النخل (maqayis)؛ فالنخل قالوا ضرب من الحلي والكروم القلائد (sihah)
- **B006** yer, topluluk ve şair adları — çölde bir yer adı · belirli bir ülkede bulunan bir yer adı · belirli bir bölgede, iki kent arasında bulunan bir yer adı · bir yer adı · belirli bir kentin yakınındaki bir yer adı · iki ayrı yer adı · bir topluluk kolunun adı · bir şairin adı · bir şairin lakabı
  نخيلة موضع بالبادية وذات نخل موضع بالعراق وبطن نخلة بالحجاز (ayn)؛ النخيلة موضع وبطن نخل موضع ونخلة موضع قريب من مكة ونخلة اليمانية والشامية موضعان وبنو نخلان بطن (jamhara)؛ بطن نخلة موضع بين مكة والطائف والمنخل اسم شاعر والمتنخل لقب شاعر (sihah)

## ك م م (root_001319): 55:11 ٱلْأَكْمَامِ

- **B001** kolu veya başı örten giysi parçası — gömleğin eli ve kolu örten kol kısmı · takke benzeri yuvarlak başlık · başlık taktı veya başını örttü · başını başlığa benzer bir örtüyle kapatan kadın
  الكمة وهي القلنسوة (maqayis)؛ والكم كم القميص (maqayis;ayn;tahdhib)؛ والكمة من القلانس (ayn;tahdhib)؛ الكمة: القلنسوة المدورة لأنها تغطي الرأس (sihah)؛ الكم: ما يغطي اليد من القميص، والكمة: ما يغطي الرأس كالقلنسوة (mufradat)
- **B002** bitki kılıfı ve bitkiyi kılıfa alma — tomurcuk, çiçek veya meyve kılıfı · tomurcuk ve meyve kılıfları · tomurcuk veya çiçek kılıfı · ağaç kılıfını çıkardı veya meyvesi ağırlaştı · ağaç tomurcuk ve meyve kılıflarını çıkardı · körpe sürgünü güçleninceye kadar özenle örttü · meyvesi taze kalsın ve kuşlarla sıcaktan korunsun diye örtülmüş salkım
  والكم وعاء الطلع والجمع الأكمام، والأكاميم أغطية النور، ويقال كم الفسيل إذا أشفق عليه فستر حتى يقوى (maqayis)؛ والكم الطلع، لكل شجرة كم وهو برعومته، وقد كمت النخلة كما وكموما (ayn)؛ والكم والكمة بالكسر والكمامة: وعاء الطلع وغطاء النور، وكمت النخلة فهي مكمومة، وكم الفسيل إذا أشفق عليه فستر حتى يقوى، وأكمت النخلة وكممت أي أخرجت كمامها (sihah)؛ وكل شجرة تخرج ما هو مكمم فهي ذات أكمام، وأكمام النخلة ما غطى جمارها، والمكموم من العذوق ما غطي (tahdhib)؛ والكم: ما يغطي الثمرة، وجمعه أكمام (mufradat)
- **B003** hayvanın ağız ve burun örtüsü — hayvanın ağzına veya burnuna geçirilen ağızlık · ağzına ağızlık geçirilmiş deve · eşeğin burnuna geçirilen torba biçimli ağızlık
  والكمام شيء يجعل في فم البعير أو البرذون لئلا يعض (ayn)؛ والكمام بالكسر والكمامة أيضا: ما يكم به فم البعير لئلا يعض، بعير مكموم (sihah)؛ الكمامة التي يجعلها على منخرها لئلا يؤذيها الذباب، والمغمة والمكمة شيء يوضع على أنف الحمار كالكيس (tahdhib)
- **B004** örtmek, sıkıca kapatmak veya bastırıp gizlemek — nesnenin üstünü örttü veya çamurla sıvadı · tanenin ya da kabın ağzını sıkıca bağladı · tulumun ağzını kapatıp çamurla sıvadı · tanıklığı bastırıp gizledi · toprağı kabarttı, ardından diş izlerini bir tahtayla silip düzeltti
  أصل واحد يدل على غشاء وغطاء (maqayis)؛ وكممت الشيء طينته (ayn)؛ وكممت الشيء: غطيته، وكممت الحب إذا شددت رأسه (sihah)؛ الكمة: كل ظرف غطيت به شيئا، وكممت رأس الدن أي سددته وطينته، وقيل كمت أي غطيت، والكم: قمع الشيء وستره، ومنه كميت الشهادة إذا قمعتها وسترتها (tahdhib)
- **B005** sıkı yapılı olma veya bir araya toplanma — sıkı ve toplu yapılı kimse · bir araya toplandılar
  ومن الباب الكمكام المجتمع الخلق (maqayis)؛ بل لو شهدت الناس إذ تكموا أي اجتمعوا (ayn)
- **B006** bunaltıcı bir örtü altında bilincini yitirmek — bunaltıcı bir örtüyle kaplanıp bayıldılar
  وتكموا أي أغمي عليهم وغطوا (sihah)؛ تكموا أي ألبسوا غمة كموا بها، والغمة ما غطاك من شيء (tahdhib)

## ح ب ب (root_000286): 55:12 وَٱلْحَبُّ

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

## ع ص ف (root_001020): 55:12 ٱلْعَصْفِ

- **B001** tahıl kabuğu, ufalanmış ekin yaprağı ve ham biçilmiş bitki artığı — tahıl kabuğu, kuruyup ufalanmış ekin yaprağı veya olgunlaşmadan biçilmiş yeşil ekin · başak yaprağı ya da birikmiş saman · başaktan dökülen saman ve benzeri kırıntı · ekinin uçlarını ya da yapraklarını olgunlaşmadan biçmek · ekin artığı veya ekini bol yer · ekinden başak yaprağını ya da samanı almak
  العصف ما على الحب من قشور التبن (maqayis)؛ ما على ساق الزرع من الورق الذي يبس فتفتت (ayn;maqayis;tahdhib)؛ العصف بقل الزرع (sihah;tahdhib)؛ العصف والعصيفة الذي يعصف من الزرع وحطام النبت المتكسر (mufradat)
- **B002** önündekileri sürükleyip savuran ve kimi nesneleri kırıp ufaltan sert rüzgar — rüzgar şiddetlenip önüne gelenleri sürükledi · şiddetli rüzgar · nesneleri kırıp bitki kırıntısına çeviren sert rüzgar · şiddetli rüzgar · toz ve yaprak kaldıran rüzgarlar · sert rüzgarlı gün
  الريح العاصف الشديدة (maqayis)؛ الريح تعصف بما مرت عليه من جولان التراب (ayn)؛ عصفت الريح أي اشتدت فهي ريح عاصف وعصوف (sihah)؛ ريح عاصف ومعصفة إذا اشتدت والمعصفات الرياح التي تثير التراب والورق (tahdhib)؛ عاصفة ومعصفة تكسر الشيء فتجعله كعصف (mufradat)
- **B003** harekette hafiflik ve hız — harekette hafiflik ve hız · binicisini hızla götüren dişi deve · hızlı deve kuşu · at hızla geçti · dişi deve hızlandı · develerin su isteğiyle kuyu çevresinde dönüp toprağı ezerek toz kaldırması
  أصل واحد صحيح يدل على خفة وسرعة (maqayis)؛ ناقة عصوف تعصف براكبها أي تمضي به كسرعة الريح والعصف السرعة في كل شيء (ayn)؛ أعصف الفرس إذا مر مرا سريعا ونعامة عصوف وناقة عصوف أي سريعة (sihah)؛ العصف السرعة والعصوف السريعة من الإبل وأعصفت الناقة إذا أسرعت (tahdhib)
- **B004** alıp götürerek, yok ederek veya kırıp ufalayarak ortadan kaldırma — savaş topluluğu silip süpürdü ve yok etti · adam yok oldu · rüzgar onları alıp götürdü ya da yok etti · yok etme
  الحرب تعصف بالقوم تذهب بهم (maqayis)؛ الحرب تعصف بالقوم أي تذهب بهم وتهلكهم وأعصف الرجل أي هلك (sihah)؛ الإعصاف الإهلاك وتعصف بالدارع والحاسر أي تهلكهما وتعصف بهما أي تذهب بهما (tahdhib)؛ عاصفة ومعصفة تكسر الشيء فتجعله كعصف وعصفت بهم الريح تشبيها بذلك (mufradat)
- **B005** geçim kazanmak için çabalayıp çare arama — kazanma ve geçimlik · kazandı ve geçimini aradı · kazanç sağlamada becerikli ve çareli · kazanç uğruna didinme ve yorulma
  عصف واعتصف إذا كسب وهو ذو عصف أي حيلة (maqayis)؛ العصف الكسب وكذلك الاعتصاف (sihah)؛ يعتصف إذا طلب الرزق والعصف الرزق ويعصف ويعتصف أي يكسب ويطلب ويحتال والعصوف الكد (tahdhib)

## ر و ح (root_000609): 55:12 وَٱلرَّيْحَانُ

- **B001** bedene canlılık veren iç varlık — bedene yaşam veren ve ölümde ayrılan iç varlık
  الروح النفس التي يحيا بها البدن؛ خرجت روحه أي نفسه (ayn)؛ روح الإنسان مختلف فيه فقال قوم هي نفسه التي يقوم بها جسمه وقال آخرون الروح خلاف النفس (jamhara)؛ الروح يذكر ويؤنث والجمع الأرواح (sihah)؛ فالروح روح الإنسان وإنما هو مشتق من الريح (maqayis)
- **B002** kutsal bildiri veya göksel varlık adı — vahyi taşıyan göksel elçi veya kutsal bildiri için kullanılan ad · göksel varlıklara ilişkin veya canlılık taşıyan
  الروحاني من الخلق نحو الملائكة؛ الروح جبرئيل وهو روح القدس؛ الروح ملك يقوم وحده (ayn)؛ الروح الأمين جبريل؛ الروحانيون من الملائكة (jamhara)؛ يسمى القرآن روحا وكذلك جبريل وعيسى؛ روحانيون (sihah)؛ والروح جبرئيل عليه السلام (maqayis)
- **B003** hareket eden hava ve esinti — rüzgar · yel esintisi · yeli hoş gün · sert yelli gün · yelpaze · rüzgar geçiren açık yer
  الريح معروفة وأصل هذه الياء واو (jamhara)؛ الريح واحدة الرياح والأرياح؛ الروح نسيم الريح؛ يوم روح وريوح أي طيب؛ راح اليوم إذا اشتدت ريحه؛ المروحة ما يتروح بها والموضع الذي تخترق فيه الرياح (sihah)؛ أصل ذلك كله الريح؛ الروح نسيم الريح؛ ريح الغدير أصابته الريح؛ أراح القوم دخلوا في الريح؛ يوم ريح طيب ويوم راح ذو ريح شديدة؛ المروحة الموضع تخترق فيه الريح (maqayis)؛ فالريح معروفة (maqayis-ريح)
- **B004** koku ve kokudaki değişim — şeyin kokusu · burunla algılanan koku · et koktu · suyun kokusu değişti · kokulandırılmış yağ
  إرواح اللحم تغير ريحه (ayn)؛ مكان ريح أي طيب الروح (jamhara)؛ وجدت ريح الشيء ورائحته؛ الدهن المروح المطيب؛ أراح اللحم أي أنتن؛ أراح الشيء أي وجد ريحه؛ أروح الماء وغيره أي تغيرت ريحه؛ تروح الماء إذا أخذ ريح غيره؛ أروحت من فلان طيبا (sihah)؛ أروح الماء وغيره تغيرت رائحته؛ الدهن المروح المطيب؛ لم يرح رائحة الجنة؛ أروحني الصيد إذا وجد ريحك؛ أروحت من فلان طيبا (maqayis)
- **B005** geç gün vakti ve akşam dönüşü — öğle sonrası vakit ve bu vakitte gidiş · geç gün vaktinde yola çıktı · sürüyü akşam barınağa döndürdü · sürünün geceleme yeri
  الرواح من لدن زوال الشمس إلى الليل؛ السير والعمل بالعشي؛ تروح القوم في معنى راحوا؛ المراح الموضع؛ الإراحة رد الإبل بالعشي (ayn)؛ راح الرجل من رواح العشي؛ أراح ماشيته؛ الرواح الراحة أيضا (jamhara)؛ الرواح نقيض الصباح من زوال الشمس إلى الليل؛ سرحت الماشية بالغداة وراحت بالعشي؛ المراح حيث تأوي إليه الإبل والغنم؛ المراح الموضع الذي يروح منه القوم أو يروحون إليه (sihah)؛ الرواح العشي؛ راحوا في ذلك الوقت من لدن زوال الشمس إلى الليل؛ أرحنا إبلنا رددناها ذلك الوقت؛ المراح حيث تأوي الماشية بالليل (maqayis)
- **B006** hakkını kendisine geri vermek [kalıp] — onun hakkını kendisine geri verdim
  أرحت على الرجل حقه إذا رددته عليه (sihah)؛ أرحت على الرجل حقه إذا رددته إليه (maqayis)
- **B007** dinlenip güç toplama — dinlenme ve yorgunluğu giderme · soluklandı ve yorgunluktan toparlandı · kolaylık ve sıkıntısızlık · gereksinim giderme yeri · ona yaslanıp dinginleşti · gece ibadetinin her dört bölümlük dizisinden sonraki dinlenme
  ما لفلان في كذا من رواح أي من راحة (ayn)؛ الرواح الراحة أيضا؛ أرحت فلانا من كذا إراحة (jamhara)؛ الروح والراحة من الاستراحة؛ أراحه الله فاستراح؛ أراح الرجل رجعت إليه نفسه بعد الإعياء؛ أراح تنفس؛ افعل ذاك في سراح ورواح أي سهولة؛ استراح الرجل من الراحة؛ المستراح المخرج؛ استروح إليه أي استنام (sihah)؛ أراح الإنسان إذا تنفس؛ أراح الرجل إذا رجعت إليه نفسه بعد الإعياء؛ أفعل ذلك في سراح ورواح أي في سهولة؛ سميت الترويحة لاستراحة القوم (maqayis)
- **B008** iki seçenek arasında nöbetleşme — iki iş veya durum arasında nöbetleşme · ağırlığını sırayla iki bacağına verdi
  المراوحة عملان في عمل يعمل ذاك مرة وهذا مرة (ayn)؛ المراوحة في العملين أن يعمل هذا مرة وهذا مرة؛ راوح بين رجليه إذا قام على إحداهما مرة وعلى الأخرى مرة (sihah)؛ المراوحة في العملين أن يعمل هذا مرة وهذا مرة (maqayis)
- **B009** duyusal açıklık ve yayvan genişlik — ayakların ön bölümlerindeki açıklık · ayak uçları birbirinden açık duran · sığ ve geniş çanak
  رجل أروح في صدر قدمه انبساط؛ بعير أروح وقدم أروح وروحاء؛ قصعة روحاء قريبة القعر (ayn)؛ رجل أروح وامرأة روحاء وهو دون الفحج (jamhara)؛ الروح بالتحريك السعة؛ الروح أيضا سعة في الرجلين؛ قصعة روحاء أي قريبة القعر (sihah)؛ أصل كبير يدل على سعة وفسحة؛ الأروح الذي في صدور قدميه انبساط؛ قصعة روحاء قريبة القعر؛ لكل شيء واسع أريح (maqayis)
- **B010** iyiliğe hevesle yönelme — iyilik için gönüllü coşku ve geniş gönüllülük · iyilik yapmaya hevesle yöneldi
  راح فلان للمعروف يراح راحة إذا أخذته له خفة وأريحية؛ راحت يده بكذا؛ الراح الارتياح؛ الارتياح النشاط؛ الأريحي الواسع الخلق؛ أخذته الأريحية إذا ارتاح للندى (sihah)؛ يقال فلان يراح للمعروف إذا أخذته له أريحية؛ أريحي؛ الأريحي مأخوذ من راح يراح (maqayis)
- **B011** güç, üstünlük ve egemenlik — güç, üstünlük ve egemenlik
  قد تكون الريح بمعنى الغلبة والقوة؛ وتذهب ريحكم (sihah)؛ الريح الغلبة والقوة في قوله تعالى فتفشلوا وتذهب ريحكم (maqayis-ريح)
- **B012** kokulu bitki veya ekin yaprağı — kokulu bitki veya ekinin yaprağı
  الريحان نبت معروف؛ والحب ذو العصف والريحان فالعصف ساق الزرع والريحان ورقه (sihah)؛ الريحان معروف (maqayis-ريح)
- **B013** ferahlık ve geçim payı — ferahlık veya esirgeme ile geçim payı · yaratıcıdan gelen veya istenen geçim payı
  روح وريحان؛ الروح الراحة والريحان الرزق (jamhara)؛ روح وريحان أي رحمة ورزق؛ الريحان الرزق؛ خرجت أبتغي ريحان الله؛ سبحان الله وريحانه يريدون استرزاقا (sihah)؛ الريحان الرزق؛ الولد من ريحان الله (maqayis-ريح)
- **B014** avuç içi — avuç içi · avuç içleri
  راحة الإنسان معروفة والجمع راح (jamhara)؛ الراح جمع راحة وهي الكف (sihah)؛ الراح جماعة راحة الكف (maqayis)
- **B015** üzümden yapılan sarhoş edici içki — üzümden yapılan sarhoş edici içki
  الرياح بالفتح الراح وهي الخمر؛ الراح الخمر (sihah)؛ الراح الخمر (maqayis)
- **B016** öldü [kalıp] — adam öldü
  أراح الرجل أي مات (sihah)؛ يقال للميت إذا قضى قد أراح (maqayis)
- **B017** ağacın yapraklanması veya bitkinin uzaması [kalıp] — ağaç yaz sonrasında yeniden yapraklandı · bitki boy attı
  راح الشجر يراح مثل تروح أي تفطر بورق؛ تروح الشجر إذا تفطر بورق بعد إدبار الصيف؛ تروح النبت أي طال (sihah)؛ تروح الشجر وراح يراح معناهما أن يتفطر بالورق (maqayis)
- **B018** erkek atın damızlık olgunluğa erişmesi [kalıp] — erkek at damızlık olgunluğa erişti
  راح الفرس يراح راحة إذا تحصن أي صار فحلا (sihah)؛ وراح الفرس يراح راحة إذا تحصن (maqayis)
- **B019** dağılan veya yuvasına dönen kuşlar — 
  الروح في هذا البيت المتفرقة (ayn)؛ طير روح أي متفرقة؛ وقيل هي الرائحة إلى مواضعها (sihah)؛ قال قوم هي المتفرقة وقال آخرون هي الرائحة إلى أوكارها (maqayis)

## ء ل و (root_000048): 55:13 ءَالَآءِ, 55:16 ءَالَآءِ, 55:18 ءَالَآءِ, 55:21 ءَالَآءِ, 55:23 ءَالَآءِ, 55:25 ءَالَآءِ, 55:28 ءَالَآءِ, 55:30 ءَالَآءِ, 55:32 ءَالَآءِ, 55:34 ءَالَآءِ, 55:36 ءَالَآءِ, 55:38 ءَالَآءِ, 55:40 ءَالَآءِ, 55:42 ءَالَآءِ, 55:45 ءَالَآءِ, 55:47 ءَالَآءِ, 55:49 ءَالَآءِ, 55:51 ءَالَآءِ, 55:53 ءَالَآءِ, 55:55 ءَالَآءِ, 55:57 ءَالَآءِ, 55:59 ءَالَآءِ, 55:61 ءَالَآءِ, 55:63 ءَالَآءِ, 55:65 ءَالَآءِ, 55:67 ءَالَآءِ, 55:69 ءَالَآءِ, 55:71 ءَالَآءِ, 55:73 ءَالَآءِ, 55:75 ءَالَآءِ, 55:77 ءَالَآءِ

- **B001** eksik kalmak — bir şeyde eksik kalmak veya ağırdan almak · sana öğüt vermede kusur etmez · öğüt veya çaba konusunda kusur etmeyen kişi · kusur etmeden, geri durmadan · eksik kalmak ve yavaş davranmak · işte eksik kalmak
  ألا الرجل يألو، أي قصر؛ وفلان لا يألوك نصحا؛ ألى يؤلى تألية، إذا قصر وأبطأ؛ ائتلى في الأمر، إذا قصر
- **B002** gücü yetmek — ona gücü yetmek · bunu yapamadım · ne bildin ne de yapabildin, kınama veya dua kalıbı
  آلاه يألوه ألوا: استطاعه؛ ما ألوت هذا، أي ما استطعته؛ لا دريت ولا ائتليت، هو افتعلت من قولك: ما ألوت هذا، أي ما استطعته
- **B003** ant içmek — ant içmek ve bağlayıcı söz kurmak · ant içmek · ant içmek · ant · ant · ant
  آلى يؤلى إبلاء: حلف؛ وتألى وائتلى مثله فيه؛ والالية: اليمين؛ وكذلك الألوة والألوة والإلوة
- **B004** iyilikler — iyilikler veya bağışlar · tek bir iyilik veya bağış
  والآلاء: النعم، واحدها ألا بالفتح
- **B005** ağaç türü — güzel görünüşlü, acı tatlı bir ağaç türü · bu ağaç türünden tek bir ağaç · bir ağaç türü · bu ağaç türünden tek bir ağaç
  والألاء مثل العلاء: ضرب من الشجر، الواحدة ألاءة (jamhara)؛ والألالاء مثل العلالاع: ضرب من الشجر (jamhara)؛ والالاء بالفتح: شجر حسن المنظر مر الطعم (sihah)

## ECHO ت ل و (root_000186): for 55:13 ءَالَآءِ, 55:16 ءَالَآءِ, 55:18 ءَالَآءِ, 55:21 ءَالَآءِ, 55:23 ءَالَآءِ, 55:25 ءَالَآءِ, 55:28 ءَالَآءِ, 55:30 ءَالَآءِ, 55:32 ءَالَآءِ, 55:34 ءَالَآءِ, 55:36 ءَالَآءِ, 55:38 ءَالَآءِ, 55:40 ءَالَآءِ, 55:42 ءَالَآءِ, 55:45 ءَالَآءِ, 55:47 ءَالَآءِ, 55:49 ءَالَآءِ, 55:51 ءَالَآءِ, 55:53 ءَالَآءِ, 55:55 ءَالَآءِ, 55:57 ءَالَآءِ, 55:59 ءَالَآءِ, 55:61 ءَالَآءِ, 55:63 ءَالَآءِ, 55:65 ءَالَآءِ, 55:67 ءَالَآءِ, 55:69 ءَالَآءِ, 55:71 ءَالَآءِ, 55:73 ءَالَآءِ, 55:75 ءَالَآءِ, 55:77 ءَالَآءِ: withheld observed target; not identity

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

## ر ب ب (root_000532): 55:13 رَبِّكُمَا, 55:16 رَبِّكُمَا, 55:17 رَبُّ, 55:17 وَرَبُّ, 55:18 رَبِّكُمَا, 55:21 رَبِّكُمَا, 55:23 رَبِّكُمَا, 55:25 رَبِّكُمَا, 55:27 رَبِّكَ, 55:28 رَبِّكُمَا, 55:30 رَبِّكُمَا, 55:32 رَبِّكُمَا, 55:34 رَبِّكُمَا, 55:36 رَبِّكُمَا, 55:38 رَبِّكُمَا, 55:40 رَبِّكُمَا, 55:42 رَبِّكُمَا, 55:45 رَبِّكُمَا, 55:46 رَبِّهِۦ, 55:47 رَبِّكُمَا, 55:49 رَبِّكُمَا, 55:51 رَبِّكُمَا, 55:53 رَبِّكُمَا, 55:55 رَبِّكُمَا, 55:57 رَبِّكُمَا, 55:59 رَبِّكُمَا, 55:61 رَبِّكُمَا, 55:63 رَبِّكُمَا, 55:65 رَبِّكُمَا, 55:67 رَبِّكُمَا, 55:69 رَبِّكُمَا, 55:71 رَبِّكُمَا, 55:73 رَبِّكُمَا, 55:75 رَبِّكُمَا, 55:77 رَبِّكُمَا, 55:78 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 55:13 رَبِّكُمَا, 55:16 رَبِّكُمَا, 55:17 رَبُّ, 55:17 وَرَبُّ, 55:18 رَبِّكُمَا, 55:21 رَبِّكُمَا, 55:23 رَبِّكُمَا, 55:25 رَبِّكُمَا, 55:27 رَبِّكَ, 55:28 رَبِّكُمَا, 55:30 رَبِّكُمَا, 55:32 رَبِّكُمَا, 55:34 رَبِّكُمَا, 55:36 رَبِّكُمَا, 55:38 رَبِّكُمَا, 55:40 رَبِّكُمَا, 55:42 رَبِّكُمَا, 55:45 رَبِّكُمَا, 55:46 رَبِّهِۦ, 55:47 رَبِّكُمَا, 55:49 رَبِّكُمَا, 55:51 رَبِّكُمَا, 55:53 رَبِّكُمَا, 55:55 رَبِّكُمَا, 55:57 رَبِّكُمَا, 55:59 رَبِّكُمَا, 55:61 رَبِّكُمَا, 55:63 رَبِّكُمَا, 55:65 رَبِّكُمَا, 55:67 رَبِّكُمَا, 55:69 رَبِّكُمَا, 55:71 رَبِّكُمَا, 55:73 رَبِّكُمَا, 55:75 رَبِّكُمَا, 55:77 رَبِّكُمَا, 55:78 رَبِّكَ: withheld observed target; not identity

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

## ك ذ ب (root_001290): 55:13 تُكَذِّبَانِ, 55:16 تُكَذِّبَانِ, 55:18 تُكَذِّبَانِ, 55:21 تُكَذِّبَانِ, 55:23 تُكَذِّبَانِ, 55:25 تُكَذِّبَانِ, 55:28 تُكَذِّبَانِ, 55:30 تُكَذِّبَانِ, 55:32 تُكَذِّبَانِ, 55:34 تُكَذِّبَانِ, 55:36 تُكَذِّبَانِ, 55:38 تُكَذِّبَانِ, 55:40 تُكَذِّبَانِ, 55:42 تُكَذِّبَانِ, 55:43 يُكَذِّبُ, 55:45 تُكَذِّبَانِ, 55:47 تُكَذِّبَانِ, 55:49 تُكَذِّبَانِ, 55:51 تُكَذِّبَانِ, 55:53 تُكَذِّبَانِ, 55:55 تُكَذِّبَانِ, 55:57 تُكَذِّبَانِ, 55:59 تُكَذِّبَانِ, 55:61 تُكَذِّبَانِ, 55:63 تُكَذِّبَانِ, 55:65 تُكَذِّبَانِ, 55:67 تُكَذِّبَانِ, 55:69 تُكَذِّبَانِ, 55:71 تُكَذِّبَانِ, 55:73 تُكَذِّبَانِ, 55:75 تُكَذِّبَانِ, 55:77 تُكَذِّبَانِ

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

## ص ل ص ل (root_000878): 55:14 صَلْصَٰلٍ

- **B001** sert nesneden uzayan ya da yankılanan çınlama — uzayan ya da yankılanan sert bir ses çıkarmak · gemin yinelenen veya yankılanan çınlama sesi · takının yinelenerek çınlaması
  صل اللجام صليلا وإن توهمت ترجيعا قلت صلصل وكل ذي صلابة يصلصل (ayn)؛ صلصلة اللجام صوته إذا ضوعف وتصلصل الحلي أي صوت وصل المسمار يصل صليلا (sihah)؛ أصل الصلصال تردد الصوت من الشيء اليابس ومنه قيل صل المسمار (mufradat)
- **B002** kuruyunca ses veren ve pişince çömleğe dönüşen kil — kuruyunca ses veren ve pişirilince çömleğe dönüşen kil
  الطين صلصال لتصلصله إذا حرك فإذا طبخ فهو فخار (ayn)؛ الصلصال الطين الحر خلط بالرمل فصار يتصلصل إذا جف فإذا طبخ بالنار فهو الفخار (sihah)؛ وسمي الطين الجاف صلصالا (mufradat)
- **B003** gölet ya da su kabının dibinde kalan az su — gölette ya da su tulumunda kalan, hareket edince ses çıkaran az su · su kabının veya göletin dibinde kalan az su
  الصلصلة بقية الماء في الغدير (ayn)؛ الصلصل أيضا بقية الماء في الإداوة وفي أسفل الغدير (sihah)؛ الصلصلة بقية ماء سميت بذلك لحكاية صوت تحركه في المزادة (mufradat)
- **B004** kumru ya da kumruya benzeyen kuş — kumru ya da kumruya benzeyen kuş
  الصلصل طائر تسميه العجم الفاختة ويقال بل يشبهها (ayn)؛ الصلصل بالضم الفاختة (sihah)
- **B005** atın perçemi veya ön bölümü — atın perçemi veya ön tarafındaki bölüm
  الصلصل ناهية الفرس (ayn)؛ الصلصل أيضا ناصية الفرس (sihah)
- **B006** aktarılan bir görüşe göre kokuşup değişmiş kil — aktarılan bir görüşe göre kokuşup değişmiş kil
  وقيل الصلصال المنتن من الطين من قولهم صل اللحم وقرئ أئذا صللنا أي أنتنا وتغيرنا (mufradat)

## ف خ ر (root_001135): 55:14 كَٱلْفَخَّارِ

- **B001** geçmiş başarıları sayıp böbürlenme — övünme; geçmiş üstünlükleri sayıp böbürlenme · övündü, böbürlendi · övündü, başarılarını sayıp döktü · topluluk birbirine karşı övündü · onunla övünme yarışına girdi · karşısındakine övünerek meydan okuyan kişi · çok övünen, böbürlenmeye düşkün kişi · övünme konusu edilen ya da övünme yarışında yenilen kişi; anlamı kesin değil · övüngen, böbürlenen · çok övünen, böbürlenmeye düşkün · kendini büyük görme ve böbürlenme · kendini büyük gören, böbürlenen · övünç kaynağı sayılan başarı · karşılıklı övünme
  الفخر هو عد القديم (maqayis); الفخر المباهاة في الأشياء الخارجة عن الإنسان (mufradat); الفخر الافتخار وعد القديم (sihah); تفاخر القوم وفاخروا وافتخروا (jamhara); التفخر التعظم والتكبر (maqayis;sihah); المفخرة المأثرة (jamhara;sihah); الفخير الكثير الفخر (maqayis;ayn;sihah)
- **B002** övünmede üstün sayma veya üstün gelme [kalıp] — adamı arkadaşından övünme bakımından üstün tuttu · onunla övünme yarışına girip onu yendi · onu ötekinden övünme bakımından üstün saydı
  فخرت الرجل على صاحبه أفخره فخرا أي فضلته عليه (maqayis); فاخرته ففخرته (ayn); فخرت الرجل على صاحبه فأنا أفخره فخرا (jamhara); أفخرته على فلان إذا فضلته عليه في الفخر (sihah); حكمت له بفضل عليه (mufradat)
- **B003** iyi, değerli ve seçkin — iyi, değerli ve seçkin · değerli, iyi nitelikli kumaş · değerli bir kumaş satın aldı · evlilikte seçkin nitelikte olanı aradı; ayrıntısı kesin değil · seçkin nitelikli bir çocuk doğurdu
  الفاخر الشيء الجيد (maqayis); الفاخر الجيد (ayn); استفخرت الثوب اشتريته فاخرا وكذلك في التزويج (ayn); أفخرت المرأة ولدت فاخرا (ayn); يعبر عن كل نفيس بالفاخر ويقال ثوب فاخر (mufradat)
- **B004** iri gövdeli hurma ağacı veya iri çekirdeksiz ham hurma [kalıp] — iri gövdeli, kalın yapraklı hurma ağacı · iri büyüyen, çekirdeksiz ham hurma
  نخلة فخور عظيمة الجذع غليظة السعف (maqayis;jamhara;sihah); الفاخر من البسر الذي يعظم ولا نوى فيه (maqayis); الفاخر من البسر الذي يعظم ولا نوى له (jamhara;sihah)
- **B005** iri memeli dişi hayvan veya üreme organı iri at [kalıp] — memesi iri dişi deve; süt verimi konusunda görüş ayrılığı vardır · memesi iri, sütü az koyun · iri fakat sütü az meme · üreme organı iri at
  ناقة فخور عظيمة الضرع القليلة الدر (maqayis); ناقة فخور أي غزيرة (ayn); شاة فخور إذا عظم ضرعها وقل لبنها (jamhara); فرس فخور إذا عظم جردانه (maqayis;jamhara;sihah); ناقة فخور هي العظيمة الضرع الضيقة الأحاليل (sihah); ناقة فخور عظيمة الضرع كثيرة الدر (mufradat)
- **B006** pişmiş toprak kap ve çanak çömlek — pişmiş toprak kaplar; çanak çömlek
  الفخار من الجرار معروف (maqayis); الفخار الخزف المتخذ من الطين (jamhara); الفخار الخزف (sihah); الفخار الجرار (mufradat); حمأة الغدير إذا جف فسمعت له صلصلة كالخزف (jamhara)
- **B007** geniş yapraklı, kırmızı çiçekli, hoş kokulu fesleğen türü — geniş yapraklı, kırmızı çiçekli ve hoş kokulu bir fesleğen türü
  الفاخور ضرب من الريحان (ayn); عرض ورقه وخرجت جماميحه رؤوسه في وسطه كأطراف أذناب الثعالب نورها أحمر طيب الريح يسميه أهل البصرة ريحان الشيوخ (ayn); الفاخور ضرب من الرياحين (sihah)

## ج ن ن (root_000266): 55:15 ٱلْجَآنَّ, 55:33 ٱلْجِنِّ, 55:39 جَآنٌّ, 55:46 جَنَّتَانِ, 55:54 ٱلْجَنَّتَيْنِ, 55:56 جَآنٌّ, 55:62 جَنَّتَانِ, 55:74 جَآنٌّ

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

## م ر ج (root_001411): 55:15 مَّارِجٍ, 55:19 مَرَجَ, 55:22 وَٱلْمَرْجَانُ, 55:58 وَٱلْمَرْجَانُ

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

## ن و ر (root_001564): 55:15 نَّارٍ, 55:35 نَّارٍ

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

## ش ر ق (root_000790): 55:17 ٱلْمَشْرِقَيْنِ

- **B001** doğmak, ışımak; doğu ve doğuya yönelmek — doğmak, doğu ufkundan yükselmek · ışımak, aydınlatmak · yüzü sevinç ve güzellikle ışıldamak · güneşin doğuşu · doğan, yükselen · doğu, güneşin doğduğu yön; bazı kullanımlarda güneş · güneşin doğduğu yer veya mevsimlere göre doğuş yerleri · doğuya ait, doğu tarafındaki · doğuya yönelme · güneşin doğduğu vakte girmek · güneş yükseldikten sonraki vakit; başka bir açıklamada ölüm anında tükürüğüne boğulma
  شرقت الشمس إذا طلعت (maqayis;sihah;mufradat)؛ وأشرقت إذا أضاءت (maqayis;sihah;mufradat)؛ الشرق خلاف الغرب (ayn)؛ المشرق والمغرب (mufradat)؛ مكانا شرقيا (mufradat)؛ التشريق الأخذ في ناحية المشرق (sihah)
- **B002** eti güneşte kurutmak [kalıp] — eti güneşe serip kurutma · kurban etlerinin güneşte kurutulduğu günler · eti güneş alan yere koymak
  لحوم الأضاحي تشرق فيها للشمس (maqayis;sihah)؛ تشريقهم اللحم في الشمس بمنى (ayn)؛ تشريق اللحم تقديده (sihah)؛ شرقت اللحم ألقيته في المشرقة (mufradat)
- **B003** rengin güçlenip doygunlaşması — kanı andıracak kadar kızarmak · utançtan yüzü kan kırmızısına dönmek · kırmızı boya · çok koyu kırmızı · kırmızı, yağsız et · safrana iyice doyurulmuş · suyu belli olan gür yeşil arazi
  اللحم الأحمر يسمى شرقا (maqayis)؛ شرق شرقا إذا حمرته بدم أو بحسن لون أحمر (ayn;tahdhib)؛ الشرقي الأحمر من الصبغ (ayn)؛ أحمر شارق شديد الحمرة (mufradat)؛ الشريق المشبع بالزعفران (tahdhib)؛ الشرقة الأرض الشديدة الخضرة الريا (tahdhib)
- **B004** koyunun kulağını yarıp ikiye ayırmak — koyunun kulağını yarmak · bir veya iki kulağı ikiye yarılmış koyun
  الشاة الشرقاء المشقوقة الأذن (maqayis)؛ شاة شرقاء مشقوقة الأذنين نصفين (ayn)؛ شرقت الشاة أشرقها أي شققت أذنها (sihah)
- **B005** suya, tükürüğe veya yiyeceğe boğulmak — tükürüğüne boğulmak · suya boğulmak, su içerken tıkanmak · boğaza takılma, boğulma · güneş yükseldikten sonraki vakit; başka bir açıklamada ölüm anında tükürüğüne boğulma
  شرق بالماء إذا غص به شرقا (maqayis)؛ شرق فلان بريقه والشرق كالغص بالطعام (ayn)؛ الشرق الشجا والغصة وشرق بريقه (sihah)؛ شرق فلان بريقه وكذلك غص بريقه (tahdhib)
- **B006** güneş alan oturma yeri ve bayram namazı alanı — güneş alan oturma yeri · güneş alan yerde oturmak · bayram namazı kılınan alan
  المشرقة متشرق القوم في الشمس (ayn)؛ المشرقة موضع القعود في الشمس (sihah)؛ تشرقت أي جلست فيه (sihah)؛ المشرقة المكان الذي يظهر للشرق (mufradat)؛ المشرق مصلى العيد (mufradat)

## غ ر ب (root_001077): 55:17 ٱلْمَغْرِبَيْنِ

- **B001** keskin uç ve uç noktaya varan yoğunluk — bir şeyin keskin ucu, sertliği veya vardığı son sınır · bir şeyin, özellikle balta ya da bıçağın keskin ağzı · sertliğini köreltmek veya atılımını durdurmak · gülmeyi aşırıya vardırmak, kahkahaya boğulmak
  الغرب حد الشيء؛ كففت من غربه؛ استغرب الرجل إذا بالغ في الضحك (maqayis)؛ الغرب التمادي وهو اللجاجة؛ كف من غربك أي من حدتك؛ استغرب الرجل إذا لج في الضحك (ayn)؛ غرب كل شيء حده وكذلك غراب كل شيء؛ الغراب حد السكين والفأس (jamhara)؛ غراب الفأس حدها؛ غرب كل شيء حده؛ في لسانه غرب؛ غرب الفرس حدته وأول جريه (sihah)؛ غرب السيف؛ فلان غرب اللسان (mufradat)
- **B002** büyük kuyu kovası ve onunla su alma — büyük ve tam kuyu kovası veya su taşıma kabı · büyük kovayı almak veya ondan daha çok kullanmak · su tulumunu doldurmak
  الغرب الدلو العظيمة؛ الغرب بفتح الراء الراوية (maqayis)؛ الغرب أعظم من الدلو وهو دلو تام؛ الغرب الراوية؛ أغرب الساقي أي أكثر الغرب (ayn)؛ الغرب دلو عظيمة (jamhara)؛ الغرب الدلو العظيمة؛ أغربت السقاء ملأته (sihah)؛ سمي الدلو غربا لتصور بعدها في البئر؛ أغرب الساقي تناول الغرب (mufradat)
- **B003** kuyuda dökülen su ve su taşkınlığı — kuyuda kovalardan dökülüp kokusu değişen su · havuzun kenarlarından taşmasını sağlamak · çok su, bol su
  الغرب ما انصب من الماء عند البئر فتغيرت رائحته (maqayis)؛ الزغرب وهو الماء الكثير؛ زيدت فيه الزاء والأصل راجع إلى الغرب (maqayis)؛ الغرب ما يقطر من الدلاء عند البئر من الماء فيتغير سريعا ريحه؛ إذا أفاض جوانب الحوض قيل أغرب الحوض (ayn)؛ الغرب الماء الذي يقطر من الدلاء بين البئر والحوض وتتغير ريحه سريعا (sihah)
- **B004** gözyaşı yolları, akışı ve göz pınarı rahatsızlığı [kalıp] — gözyaşı yolları veya gözden taşan yaş · gözyaşının aktığı yol ve taşan yaş · gözün ön ve arka uçları · gözde şişlik, apse veya sürekli sulayan damar
  الغربان من العين مقدمها ومؤخرها؛ الغروب مجاري العين؛ الغرب الورم في المأق؛ الغرب عرق يسقي ولا ينقطع (maqayis)؛ كل فيضة من الدمع غرب؛ فاضت غروب العين؛ الغربان مؤخر العين ومقدمها؛ الغرب خراج يخرج في العين (ayn)؛ غرب الدمع مسيله؛ الغرب بثرة تكون في العين (jamhara)؛ الغروب مجاري الدمع؛ لعينه غرب إذا كانت تسيل ولا تنقطع دموعها؛ الغرب عرق في مجرى الدمع (sihah)
- **B005** dişlerin suyu, parlaklığı ve keskin uçları [kalıp] — dişlerin suyu, parlaklığı veya keskin uçları
  غروب الأسنان ماؤها (maqayis)؛ غروب الأسنان الماء الذي يجري عليها؛ غروب الأسنان أطرافها (ayn)؛ الغروب حدة الأسنان وماؤها واحدها غرب (sihah)
- **B006** güneşin batması, batı yönü ve batış yeri — güneş batmak, yeryüzünden uzaklaşıp gözden kaybolmak · batı yönü veya güneşin battığı yer · yaz ve kış güneşinin iki batış noktası · güneşin batma vakti · güneşin çeşitli doğuş ve batış yerleri
  غروب الشمس كأنه بعدها عن وجه الأرض (maqayis)؛ الغرب المغرب؛ الغروب غيبوبة الشمس؛ مغيربان الشمس؛ رب المشرقين ورب المغربين؛ المشارق والمغارب (ayn)؛ الغرب خلاف الشرق؛ غربت الشمس غروبا؛ المشرق والمغرب معروفان؛ المشرقان والمغربان (jamhara)؛ المغرب الذي يأخذ في ناحية المغرب؛ الغرب والمغرب بمعنى واحد؛ غربت الشمس غروبا (sihah)؛ الغرب غيبوبة الشمس؛ مغرب الشمس ومغيربانها؛ رب المشرق والمغرب؛ لا شرقية ولا غربية (mufradat)
- **B007** yurttan uzaklaşma ve uzaklaştırma — yurttan uzakta bulunma ve uzak yerde yaşama · yurdundan ayrılıp uzakta yaşamak veya akraba dışından evlenmek · benden uzaklaş, uzağa git · hedefin veya gidilecek yerin uzaklığı · uzak bir yerden gelen haber · avın peşinde çok ileri gitmek · uzaklaşmak, kenara çekilmek · onu uzaklaştırmak veya kenara çekmek · ülkeden sürme ve uzaklaştırma · uzak hedef veya uzun mesafe
  الغربة البعد عن الوطن؛ شأو مغرب أي بعيد؛ مغربة خبر؛ إذا أمعنت الكلاب في طلب الصيد قيل غربت وفيه نظر (maqayis)؛ الغربة الاغتراب من الوطن؛ غرب فلان عنا أي تنحى؛ أغربته وغربته أي نحيته؛ غربة النوى؛ أغرب القوم انتووا؛ غربت الكلاب أمعنت (ayn)؛ غرب الرجل تغريبا إذا بعد؛ اغرب عني أي ابعد؛ مغربة خبر؛ المصدر الغربة (jamhara)؛ الغربة الاغتراب؛ الغرباء الأباعد؛ التغريب النفي عن البلد؛ اغرب عني أي تباعد؛ نوى غربة (sihah)؛ لكل متباعد غريب؛ الغراب سمي لكونه مبعدا في الذهاب (mufradat)
- **B008** nadir, benzersiz veya anlaşılması güç — nadir, benzersiz veya anlaşılması güç · alışılmadık veya nadir bir şey getirmek
  الغريب الغامض من الكلام؛ غربت الكلمة؛ صاحبه مغرب (ayn)؛ الغريب من هذا والمصدر الغربة (jamhara)؛ أغرب الرجل جاء بشيء غريب (sihah)؛ لكل شيء فيما بين جنسه عديم النظير غريب؛ العلماء غرباء لقلتهم (mufradat)
- **B009** üst sırt, yüksek tepe ve serbest bırakma — üst sırt, hörgüç ile boyun arası veya dalga tepesi · serbestsin, dilediğin yere git
  الغارب أعلى الظهر والسنام؛ ألقى حبله على غاربه إذا خلاه (maqayis)؛ الغارب أعلى الموج وأعلى الظهر؛ حبلك على غاربك (ayn)؛ غارب البعير ما انحدر من سنامه إلى عنقه؛ غارب كل شيء أعلاه (jamhara)؛ الغارب ما بين السنام والعنق؛ حبلك على غاربك؛ غوارب الماء أعالي موجه (sihah)؛ غارب السنام لبعده عن المنال (mufradat)
- **B010** karga ve karga gibi kapkara — karga · karga gibi çok koyu siyah
  الغراب معروف؛ الغربيب الأسود مشتق من لون الغراب (maqayis)؛ جمع الغراب غربان والعدد أغربة؛ الغربيب الأسود (ayn)؛ الغراب الطائر المعروف والجمع غربان وأغرب وغرب وأغربة؛ الغربيب الأسود (jamhara)؛ الغراب واحد الغربان؛ جمع القلة أغربة؛ أسود غربيب؛ غرابيب سود (sihah)؛ الغراب سمي لكونه مبعدا في الذهاب؛ غرابيب سود؛ الغربيب المشبه للغراب في السواد (mufradat)
- **B011** sağrı çukurları ve çok sıkı bağ — sağrıdaki iki çukur veya kalça kemiklerinin iki kenarı · çok sıkı bir bağlama ve düğüm türü · işi iyice daralıp güçleşmek
  الغرابان نقرتان عند صلوى العجز من الفرس؛ رجل الغراب نوع من الصر (maqayis)؛ الغرابان نقرتان في العجز؛ رجل الغراب وهو أشد صرارا؛ صر عليه رجل الغراب (ayn)؛ غرابا الفرس والبعير حرفا الوركين (jamhara)؛ غرابا الفرس والبعير حد الوركين؛ رجل الغراب ضرب من الصرار شديد (sihah)؛ الغرابان نقرتان عند صلوي العجز تشبيها بالغراب في الهيئة (mufradat)
- **B012** beyaz kirpikli, yaygın ak alınlıklı veya sonradan beliren — beyaz, özellikle kirpikleri beyaz olan · atın ak alınlığı gözlerine kadar yayılıp kirpiklerini beyazlatmak · başta sonradan çıkan yeni saç teli
  المغرب الأبيض الأشفار من كل شيء (maqayis)؛ المغرب الأبيض الأشفار من كل صنف؛ الشعرة الغريبة لأنها حدث في الرأس (ayn)؛ يسمى البرد غرابا لبياضه؛ الفرس المغرب تتسع غرته حتى تجاوز عينيه وتبيض أشفاره؛ الرجل المغرب الذي يبياض شعر رأسه ولحيته من خلقة (jamhara)؛ المغرب الأبيض؛ المغرب الأبيض الأشفار من كل شيء؛ أغرب الفرس إذا فشت غرته حتى تأخذ العينين فتبيض الأشفار (sihah)؛ المغرب الأبيض الأشفار كأنما أغربت عينه في ذلك البياض (mufradat)
- **B013** kaynağı bilinmeyen ok ve hedefsiz bakış [kalıp] — atıcısı veya geldiği yön bilinmeyen ok · belirli bir hedefe yönelmeyen bakış
  أتاه سهم غرب إذا لم يدر من رماه به (maqayis)؛ سهم غرب لا يعرف راميه (ayn)؛ أتاه سهم غرب إذا جاءه من حيث لا يدري به (jamhara)؛ أصابه سهم غرب إذا كان لا يدرى من رماه (sihah)؛ سهم غرب لا يدرى من رماه؛ نظر غرب ليس بقاصد (mufradat)
- **B014** uzak uçan söylence kuşu veya büyük felaket — uzak uçan söylence kuşu veya büyük felaket
  العنقاء المغرب ويقال المغربة وإغرابها في طيرانها (ayn)؛ عنقاء مغرب طائر وليس بثبت غير أنهم يسمون الداهية عنقاء مغرب (jamhara)؛ عنقاء مغرب وصف بذلك لأنه كان طيرا تناول جارية فأغرب بها (mufradat)
- **B015** belirli bir ağaç, kırmızı reçinesi veya boyası — özel adla anılan bir ağaç türü · batış güneşini alan ağaç, kırmızı reçine veya boya
  الغرب شجر؛ الغربي صبغ أحمر (maqayis)؛ الغربي شجر تصيبه الشمس بحرها عند الأفول؛ الغربي صمغ أحمر؛ الغرب شجرة (ayn)؛ الغرب شجرة (jamhara)؛ الغرب ضرب من الشجر (sihah)؛ الغرب شجر لا يثمر لتباعده من الثمرات (mufradat)
- **B016** hurma mayalaması veya şarap — olgunlaşmamış hurmadan yapılan mayalı içecek · şarap
  الغربي الفضيخ من البسر ينبذ (maqayis)؛ الغربي الفضيخ من النبيذ (ayn)؛ الغرب أيضا الخمر (sihah)
- **B017** şiddetli ağrı veya koyunda tüy döken hastalık — ağrısı çok şiddetlenmek · koyunun burun ve göz çevresi tüylerini döken hastalık
  أغرب الرجل إذا اشتد وجعه؛ الغرب في الشاة داء يتمعط منه خرطومها ويسقط منه شعر عينيها (sihah)
- **B018** gümüş, altın veya bunlardan yapılmış değerli kap — gümüş, altın veya bunlardan yapılmış değerli kap
  الغرب إناء من ذهب أو فضة (maqayis)؛ الغرب جام من فضة؛ الغرب أقداح من غرب (ayn)؛ الغرب إناء من فضة (jamhara)؛ الغرب بالتحريك الفضة (sihah)؛ الغرب الذهب لكونه غريبا فيما بين الجواهر الأرضية (mufradat)

## ب ح ر (root_000086): 55:19 ٱلْبَحْرَيْنِ, 55:24 ٱلْبَحْرِ

- **B001** genis büyük su kütlesi — genis ve cok su, büyük su kütlesi veya büyük irimak · kucuk deniz gibi anilan su birikimi ya da büyük gol
  سمي به لاستبحاره وهو انبساطه وسعته (ayn;tahdhib)؛ كل مكان واسع جامع للماء الكثير (mufradat)؛ كل نهر عظيم بحر (sihah;tahdhib)؛ إذا كان البحر صغيرا قيل له بحيرة (ayn;tahdhib)
- **B002** genisleyip derinlesmek — bilgisinde veya herhangi bir alanda genislemis kisi · bir seyi deniz genisligi gibi genisletmek · bilgi, mal veya otlakta genislemek ve derinlesmek · kosusu genis, cok kosan iyi at
  استبحر في العلم (ayn;tahdhib;mufradat)؛ تبحر في العلم وغيره أي تعمق فيه وتوسع (sihah)؛ تبحر الراعي في رعي كثير (ayn;tahdhib)؛ تبحر في المال إذا كثر ماله (tahdhib)؛ فرس بحر باعتبار سعة جريه (sihah;tahdhib;mufradat)؛ استبحر الشاعر إذا اتسع له القول (tahdhib)
- **B003** kulagi genis yarikla kesmek — kulagi genis bir yarikla kesip delmek · kulagi yarilip belli bir adet icin saliverilen deve veya koyun
  الناقة تبحر بحرا وشق أذنها (ayn)؛ بحرت أذن الناقة بحرا شققتها وخرقتها (sihah)؛ بحروا أذنها أي شقوها (tahdhib)؛ بحرت البعير شققت أذنه شقا واسعا ومنه سميت البحيرة (mufradat)
- **B004** suyun tuzlu olmasi — tuzlu su · suyun tuzlu hale gelmesi · tuzlu su
  ماء بحر أي ملح وأبحر الماء ملح (sihah)؛ الماء البحر هو الملح وقد أبحر الماء إذا صار ملحا (tahdhib)؛ ماء بحراني أي ملح وقد أبحر الماء (mufradat)
- **B005** acikta karsilasmak [kalıp] — onu acikta, arada engel olmadan karsiladim
  لقيته صحرة بحرة أي بارزا ليس بينك وبينه شيء (sihah)؛ وهو من قولهم لقيته صحرة بحرة (tahdhib)؛ لقيته صحرة بحرة أي ظاهرا حيث لا بناء يستره (mufradat)
- **B006** yer ve su cukuru adi — belde, toprak veya köy · cayir, alcak yer, su biriktiren cukur veya vadi bitkiligi · arazide su birikintilerinin cogalmasi
  البحرة البلدة هذه بحرتنا أي بلدتنا وأرضنا (sihah;tahdhib)؛ لكل قرية هذه بحرتنا (tahdhib)؛ الروضة بحرة وقد أبحرت الأرض إذا كثر مناقع الماء فيها (tahdhib)؛ البحرة الأوقة يستنقع فيها الماء (tahdhib)؛ البحرة المنخفض من الأرض (tahdhib)؛ البحرة منبت الثمام من الأودية (tahdhib)
- **B007** derinlikten gelen koyu kirmizilik — rahmin dibi veya derinligi · saf ve siddetli kirmizi kan · cok siddetli kirmizi
  البحر عمق الرحم ومنه الدم الخالص الحمرة باحر وبحراني (sihah)؛ أبحر الرجل إذا اشتدت حمرة أنفه (tahdhib)؛ أحمر باحري وبحراني (tahdhib)؛ الدم البحراني منسوب إلى قعر الرحم وعمقها (tahdhib)؛ دم باحري إذا كان شديد الحمرة (tahdhib)
- **B008** saskinliktan donakalmak — konusulunca sersem gibi kalan aptal kimse · korkudan saskinliga düsmek veya denizi görünce ürküp donakalmak
  الباحر الأحمق الذي إذا كلم بحر وبقي كالمبهوت (ayn)؛ الباحر الأحمق (sihah;tahdhib)؛ بحر الرجل إذا تحير من الفزع (sihah)؛ بحر الرجل إذا رأى البحر ففرق حتى دهش (tahdhib)؛ الباحر الفضولي والباحر الكذاب (tahdhib)
- **B009** denize binmek ve denize nispetli olmak — denize veya suya binip yolculuk etmek · Bahreyn'e nispet edilen · denize nispet edilen veya deniz yolculuguna cikan topluluk
  أبحر فلان إذا ركب البحر (sihah)؛ أبحر الرجل إذا ركب البحر والماء (tahdhib)؛ رجل بحراني منسوب إلى البحرين (ayn;tahdhib)؛ النسبة إلى البحرين بحراني (sihah;tahdhib)؛ كل ما نسب إلى البحر فهو بحري (tahdhib)؛ البحرية لأنها ركبت البحر (tahdhib)
- **B010** kastsiz rastlamak — bir insana onu görme niyeti olmadan rastlamak
  أبحر إذا صادف إنسانا على غير اعتماد وقصد لرؤيته (tahdhib)
- **B011** verem gibi zayiflatici hastalik — kisinin vereme tutulmasi · verem doguran hastalik veya bedeni etten düsüren zayiflama
  أبحر الرجل إذا أخذه السل (tahdhib)؛ البحير والبحر الذي به السل (tahdhib)؛ البحر داء في الإبل وقد بحرت (sihah)؛ وأما البحر فهو داء يورث السل (tahdhib)؛ البحير المسلول الجسم الذاهب اللحم (tahdhib)
- **B012** sonradan turemis tibbi kriz terimi — akut hastalikta hastaya birden gelen degisim · tibbi kriz günü · Temmuz sicaginin siddetli günü
  التغير الذي يحدث للعليل دفعة في الأمراض الحادة بحران (sihah)؛ هذا يوم بحران بالإضافة (sihah)؛ يوم باحورى منسوب إلى باحور وباحوراء وهو شدة الحر في تموز؛ وجميع ذلك مولد (sihah)
- **B013** büyük karinli — büyük karinli kimse
  يقال للعظيم البطن بحري (tahdhib)
- **B014** sudan kanmayacak kadar susamak — siddetle susayip sudan kanmamak
  بحر إذا اشتد عطشه فلم يرو من الماء (sihah)؛ الداء الذي يصيب البعير فلا يروى من الماء هو النجر والبجر وكذلك البقر، وأما البحر فهو داء يورث السل (tahdhib)

## ل ق ي (root_001372): 55:19 يَلْتَقِيَانِ

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

## ب غ ي (root_000138): 55:20 يَبْغِيَانِ

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

## خ ر ج (root_000400): 55:22 يَخْرُجُ

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

## ل ء ل ء (root_001337): 55:22 ٱللُّؤْلُؤُ

- **B001** inci — inci · inci tanesi · inciler · inci sahibi ya da inci işleyeni · inci işleme mesleği · inci sahibi
  اللؤلؤ معروف وصاحبه لئال واللئالة حرفة اللئال (ayn)؛ اللؤلؤة: الدرة، والجمع اللؤلؤ واللآلئ (sihah)؛ لؤلؤ جمعه: لآلئ (mufradat)
- **B002** parıldamak — parıldamak · parıltı ve ışıldama · ateş tutuşup alevlendi
  تلألؤ النجم والنار بريقهما (ayn)؛ تلألأ النجم تلألؤا إذا لمع (jamhara)؛ تلألأ البرق: لمع (sihah)؛ تلألأ الشيء: لمع لمعان اللؤلؤ (mufradat)
- **B003** kuyruğunu oynatmak, kimi durumda parıldatmak — kuyruğunu hareket ettirip parlatmak · ceylanlar kuyruklarını oynattı · yaban sığırları kuyruk salladığı sürece
  لألأ بذنبه إذا حرك ذنبه فلمع لأنه أبيض الذنب (ayn)؛ لألأت الظباء بأذنابها إذا حركتها (jamhara)؛ ما لألأت الفور أي بصبصت بأذنابها (sihah)؛ ما لألأت الظباء بأذنابها (mufradat)
- **B004** göz parıldatma ve avuç çevirme — kadın gözünü parıldattı · avuçlarını göğüslerine doğru çevirip döndürüyorlar
  لألأت المرأة بعينها ورأرأت أي برقتها؛ وتلألئ تقلب كفيها (ayn)

## ج ر ي (root_000240): 55:24 ٱلْجَوَارِ, 55:50 تَجْرِيَانِ

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

## ن ش ء (root_001502): 55:24 ٱلْمُنشَـَٔاتُ

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

## ك ل ل (root_001315): 55:26 كُلُّ, 55:29 كُلَّ, 55:52 كُلِّ

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

## ف ن ي (root_001181): 55:26 فَانٍ

- **B001** sona erme veya ortadan kaldırma — tükenip gitmek, sona ermek · ortadan kaldırmak, yok etmek · savaşta birbirini yok etmek · yaşlanıp ölümün eşiğine gelmek
  فنى الشيء فناء وأفناه غيره (sihah)؛ تفانوا أي أفنى بعضهم بعضا في الحرب (sihah)؛ الفناء نقيض البقاء والفعل فنى يفنى فناء فهو فان (tahdhib)؛ فني الرجل يفنى إذا هرم وأشرف على الموت (tahdhib)؛ ليت ربي قد أهلكها ودماها (tahdhib)؛ فنى يفنى فناء والله تعالى أفناه وذلك إذا انقطع (maqayis)؛ قطعه أي ذهب به (maqayis)
- **B002** evin önü ve yanlarındaki açık alan [kalıp] — evin önünde veya yanlarında uzanan açık alan
  فناء الدار ما امتد من جوانبها والجمع أفنية (sihah)؛ الفناء سعة أمام الدار وجمعه الأفنية (tahdhib)؛ الفناء ما امتد مع الدار من جوانبها والجمع أفنية (maqayis)
- **B003** bağları bilinmeyen karışık insan topluluğu [kalıp] — bağları bilinmeyen karışık insanlar
  هو من أفناء الناس إذا لم يعلم ممن هو (sihah)؛ بها أفناء من الناس وأعناء أي أخلاط (tahdhib)؛ هؤلاء من أفناء الناس ولا يقال في الواحد رجل من أفناء الناس (tahdhib)؛ قوم من هاهنا وهاهنا نزاع (tahdhib)؛ هو من أفناء العرب إذا لم يدر ممن هو (maqayis)
- **B004** itüzümü ve benzeri ot ya da çalı adı — itüzümü veya kırmızı taneli bir çalı · sarı ya da kırmızı renkli bir ot; itüzümü
  الفَنا مقصور عنب الثعلب (sihah;tahdhib;maqayis)؛ شجر له حب أحمر تتخذ منه القلائد (sihah)؛ الأفاني نبت ما دام رطبا فإذا يبس فهو الحماط (sihah)؛ ويقال أيضا هو عنب الثعلب (sihah)؛ أنبت لها الفنا وهو عنب الثعلب حتى تغزر وتسمن (tahdhib)؛ الأفاني نبت أصفر وأحمر (tahdhib)؛ الأفاني نبت من ذكور البقل وإذا يبس تناثر ورقه (tahdhib)؛ والأفاني نبت الواحدة أفانية (maqayis)
- **B005** inek — inek
  الفناة أيضا البقرة والجمع فنوات (sihah)؛ الفناة البقرة وجمعها فنوات (tahdhib;maqayis)
- **B006** yumuşakça idare edip yatıştırma; mala bakıp düzeltme — yumuşak davranarak idare etmek · yatıştırmak, sakinleştirmek · malın başında durup bakımını yapmak ve düzeltmek
  فانيته أي داريته (sihah)؛ فانيته أي سكنته (sihah;tahdhib)؛ المفاناة المداراة (tahdhib;maqayis)؛ ما يعانون مالهم ولا يفانونه أي ما يقومون عليه ولا يصلحونه (tahdhib)
- **B007** dalları her yöne yayılan ağaç — dalları her yöne yayılan çok dallı ağaç
  شجرة فنواء أي ذات أفنان (sihah;tahdhib)؛ شجرة فنواء إذا ذهبت أفنانها في كل شيء (maqayis)؛ القياس فناء لأنه من الفنن (maqayis)؛ وهو على غير قياس لأن قياسه فناء (sihah)

## ب ق ي (root_000142): 55:27 وَيَبْقَىٰ

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

## و ج ه (root_001630): 55:27 وَجْهُ

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

## ج ل ل (root_000255): 55:27 ٱلْجَلَٰلِ, 55:78 ٱلْجَلَٰلِ

- **B001** değerce yücelik ve yüceltme — gözümde büyüdü, değeri yükseldi · onu yüce saydım, ona büyük değer verdim · Tanrı'nın yüceliği · yücelik ve iyilik sahibi · ulu, değeri çok yüksek · büyük ve önemli iş
  جل في عيني أي عظم وأجللته أي أعظمته (ayn;tahdhib)؛ جل الشيء عظم وجلال الله عظمته وذو الجلال والإكرام والجلل الأمر العظيم (maqayis)؛ جلال الله عظمته والجلال بالضم العظيم والجليل العظيم (sihah)؛ الجلالة عظم القدر والجلال التناهي في ذلك والجليل العظيم القدر (mufradat)
- **B002** büyük bölüm ve iri olan — şeyin büyük bölümü · yaşlı ya da iri develer ve benzerleri · büyük deve ya da büyük armağan · küçüğü büyüğü hiçbir şeyi yok
  جل الشيء معظمه والجلة الإبل المسان والجليلة خلاف الدقيقة وما له دقيقة ولا جليلة (maqayis)؛ كل شيء يدق فجلاله خلاف دقاقه وجل كل شيء عظمه والجلة العظام من الإبل (ayn)؛ جل الشيء معظمه والجلة من الإبل المسان ومشيخة جلة وما له جليلة ولا دقيقة (sihah;tahdhib)؛ قيل للبعير جليل وللشاة دقيق وما له جليل ولا دقيق (mufradat)
- **B003** küçük ve önemsiz sayılma — hafif, küçük ve önemsiz · gözümde küçüldü ve önemsizleşti
  جل في عيني أي احتقر وتهاون وهذه من المضاد (ayn)؛ الجلل أيضا الهين وهو من الأضداد (sihah)؛ الجلل في كلام العرب من الأضداد ويقال للكبير جلل والصغير جلل (tahdhib)؛ عبر به عن الشيء الحقير وعلى ذلك قوله كل مصيبة بعده جلل (mufradat)
- **B004** senin uğruna ve sana verdiğim değerden [kalıp] — senin uğruna ya da sana verdiğim büyük değerden · senin uğruna
  فعلت ذاك من جلالك معناه من عظمك في صدري (maqayis;tahdhib)؛ فعلته من جلالك أي من أجلك وفعلت ذاك من جلك أي من أجلك (sihah)؛ الجلل بمعنى الأجل (ayn)
- **B005** örtü ve bütünü kaplama — hayvan örtüsü · her şeyin örtüsü · gemi yelkeni · her yanını kapladı · yeryüzünü yağmurla kaplayan bulut
  الأصل الثاني شيء يشمل شيئا مثل جل الفرس والمجلل الغيث الذي يجلل الأرض والجلول شرع السفن (maqayis)؛ جل الدابة معروف وجلال كل شيء غطاؤه (ayn)؛ الجل بالضم واحد جلال الدواب وجمع الجلال أجلة وجلل الشيء تجليلا أي عم والمجلل السحاب الذي يجلل الأرض بالمطر (sihah)؛ جلال كل شيء غطاؤه والجلول شراع السفينة (tahdhib)؛ المجلة ما يغطى به الصحف وسحاب مجلل يجلل الأرض بالماء والنبات (mufradat)
- **B006** yazılı yaprak veya kitap — yazılı yaprak veya kitap
  المجلة صحيفة يكتب فيها شيء من الحكمة (jamhara)؛ المجلة الصحيفة فيها الحكمة وكل كتاب عند العرب مجلة (sihah;tahdhib)؛ المجلة الصحيفة وهي شاذة عن الباب إلا أن تلحق بالأول لعظم خطر العلم وجلالته (maqayis)؛ المجلة ما يغطى به الصحف ثم سميت الصحف مجلة (mufradat)؛ المجلة الصحيفة هو من جل (maqayis-xref)
- **B007** hayvan dışkısı, toplama ve pislik yiyen hayvan — hayvan dışkısı · hayvan dışkısı toplamak · dışkı veya pislik yiyen hayvan
  مما شذ عن الباب الجلة البعر (maqayis)؛ إبل جلالة أي تأكل العذرة والجلة البعر وهو يجتله أي يلتقطه (ayn)؛ الجلة البعر وهم يجتلون الجلة أي يلقطون البعر والجلالة البقرة التي تتبع النجاسات (sihah)؛ الجلالة التي تأكل الجلة والجلة البعر وجل يجل جلا إذا التقط البعر واجتله مثله (tahdhib)؛ جللت كذا تناولت وتجللت البقر تناولت جلاله (mufradat)
- **B008** hasat sapı veya zayıf dolgu otu — hasattan sonra kalan ekin sapları · dolgu için kullanılan zayıf bir ot türü
  الجل سوق الزرع إذا حصد عنه السنبل والجليل الكلأ وهو الثمام (ayn)؛ الجل بالكسر قصب الزرع إذا حصد والجليل الثمام نبت ضعيف (sihah)؛ الجل سوق الزرع إذا حصد عنه السنبل والجليل الثمام (tahdhib)؛ منه الجل قصب الزرع ومحتمل أن يكون من الباب الأول لغلظه ومنه الجليل وهو الثمام (maqayis)
- **B009** palmiye yaprağından hurma sepeti — palmiye yaprağından hurma sepeti
  الجلة وعاء التمر من خوص (ayn)؛ الجلة وعاء التمر (sihah)؛ الجلة تتخذ من الخوص وعاء للتمر يكنز فيها وجمعها جلال (tahdhib)
- **B010** çınlama, çalkalama ve zemine batma — çıngırak · çıngırak sesi, gök gürültüsü veya çıngırağı sallama · gök gürültülü bulut · toprağa gömülüp içine girmek · açık ve duru anıran eşek
  الأصل الثالث من الصوت يقال سحاب مجلجل إذا صوت والجلجل مشتق منه وجلجلت الشيء في يدي إذا خلطته ثم ضربته (maqayis)؛ التجلجل السؤوخ في الأرض والتحرك والجوالان وحركة الريح والجلجلة تحريك الجلجل وصوت الرعد (ayn)؛ الجلجل واحد الجلاجل وصوته الجلجلة وصوت الرعد أيضا والمجلجل السحاب الذي فيه صوت الرعد وجلجلت الشيء إذا حركته وتجلجل في الأرض أي ساخ فيها ودخل وتجلجلت قواعد البيت أي تضعضعت (sihah)
- **B011** bitkisel tane ve kalbin en iç özü — kişniş meyvesi ya da kabuğundaki susam · kalbin en iç noktası ve özü
  الجلجلان ثمر الكزبرة (ayn)؛ جلجلان السمسم لأنه يتجلجل في سنفه إذا يبس وأصبت جلجلان قلبه أي حبة قلبه (maqayis)؛ الجلجلان ثمرة الكزبرة وهو السمسم في قشره قبل أن يحصد والجلجلان حبة القلب (sihah)
- **B012** yurttan çıkıp ayrılma — 
  جل القوم من البلد يجلون بالضم جلولا أي جلوا وخرجوا إلى آخر فهم جالة (sihah)؛ جل الرجل عن وطنه يجل جلولا وجلا يجلو جلاء وأجلى يجلي إجلاء إذا أخل بوطنه والجالية والجالة (tahdhib)

## ك ر م (root_001294): 55:27 وَٱلْإِكْرَامِ, 55:78 وَٱلْإِكْرَامِ

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

## س ء ل (root_000661): 55:29 يَسْـَٔلُهُۥ, 55:39 يُسْـَٔلُ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 55:29 يَسْـَٔلُهُۥ, 55:39 يُسْـَٔلُ: withheld observed target; not identity

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

## ي و م (root_001700): 55:29 يَوْمٍ

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

## ش ء ن (root_000773): 55:29 شَأْنٍ

- **B001** iş, durum veya önemli olay — iş, durum veya önemli olay
  الشأن الخطب (ayn)؛ الشأن الأمر والحال (sihah)؛ الشأن الحال والأمر الذي يتفق ويصلح ولا يقال إلا فيما يعظم من الأحوال والأمور (mufradat)
- **B002** bir amaca yönelme ve onu isteme [kalıp] — onun yöneldiği hedefe yöneldim · bu benim istediğim ve aradığım şey değil
  أصل واحد يدل على ابتغاء وطلب (maqayis)؛ شأنت شأنه أي قصدت قصده (maqayis;sihah)؛ ما هذا من شأني أي ما هذا من مطلبي والذي أبتغيه (maqayis)
- **B003** iyi bildiğin işi yap [kalıp] — iyi bildiğin işi yap
  اشأن شأنك أي اعمل ما تحسنه (sihah)
- **B004** onların işini mutlaka bozacağım [kalıp] — onların işini mutlaka bozacağım
  لأشأنن شأنهم أي لأفسدن أمرهم (sihah)
- **B005** kafatası birleşimleri, gözyaşı yolları ve gözlere inen iki damar — kafatası kemiklerinin birleşim yeri · kafatası birleşim çizgileri ve gözyaşı yolları · baştan kaşlara ve gözlere inen iki damar
  الشؤون فما بين قبائل الرأس الواحد شأن وإنما سميت بذلك لأنها مجاري الدمع (maqayis)؛ الشؤون نمانم في الجمجمة بين القبائل أي خطوط بين القبائل الأربع (ayn)؛ الشأن واحد الشؤون وهي مواصل قبائل الرأس وملتقاها ومنها تجيء الدموع (sihah)؛ الشأنان عرقان ينحدران من الرأس إلى الحاجبين ثم إلى العينين (sihah)؛ شأن الرأس جمعه شئون وهو الوصلة بين متقابلاته (mufradat)
- **B006** onu umursamama [kalıp] — onu hiç umursamadım
  ما شأنت شأنه أي لم أكترث له (sihah)

## ف ر غ (root_001147): 55:31 سَنَفْرُغُ

- **B001** meşguliyetten çıkma veya içi boş kalma — işi bitip boş kalmak · meşguliyetsizlik, boş zaman · boş, sabırdan veya akıldan yoksun · korku kalplerinden gitti · boşaltılmış, içi boş
  الفراغ خلاف الشغل (maqayis;mufradat)؛ فرغت من الشغل (sihah)؛ فؤاد أم موسى فارغا أي خاليا من الصبر (ayn)؛ كأنما فرغ من لبها (mufradat)؛ حتى إذا فرغ عن قلوبهم أي ذهب بالخوف (ayn)
- **B002** dökerek boşaltma veya akıp dökülme — döküp boşaltmak · bize bol bol sabır vermek · su akıp döküldü · dökerek boşaltmak · kapları boşaltma · suyu kendi üzerine dökmek · kovanın su çıkış ağzı · kovanın suyun döküldüğü yanı · kovanın ön ve arka su çıkışlarından ad alan iki ay konağı · dökümle yapılmış, kenarları dolu halka
  الفرغ مفرغ الدلو الذي ينصب منه الماء (maqayis)؛ أفرغت الماء صببته وافترغت إذا صببت الماء على نفسك (maqayis)؛ الفراغ ناحيته التي يصب الماء منها (ayn)؛ فرغ الماء انصب وأفرغت الدلاء أرقتها وفرغته تفريغا (sihah)؛ تفريغ الظروف إخلاؤها (sihah)؛ أفرغت الدلو صببت ما فيه ومنه استعير أفرغ علينا صبرا (mufradat)؛ الفرغان فرغ الدلو المقدم وفرغ الدلو المؤخر (sihah)؛ حلقة مفرغة لأنه شيء يصب صبا (maqayis)
- **B003** geniş adımlı, geniş izli veya enli olma [kalıp] — geniş adımlı yürüyen veya koşan at · geniş yara açıp kan akıtan darbe · geniş yara açan saplama · enli yol
  فرس فريغ أي واسع المشي (maqayis;sihah)؛ ضربة فريغ واسعة وطعنة أيضا وطريق فريغ واسع (maqayis)؛ الطعنة الفرغاء ذات الفرغ وهو السعة (sihah)؛ فرس فريغ واسع العدو وضربة فريغة واسعة ينصب منها الدم (mufradat)
- **B004** kanı yerde kalmak [kalıp] — kanı yerde kaldı, öcü aranmadı
  ذهب دمه فرغا أي باطلا لم يطلب به (maqayis)؛ ذهب دمه فرغا وفرغا أي هدرا لم يطلب به (sihah)؛ ذهب دمه فرغا أي مصبوبا ومعناه باطلا لم يطلب به (mufradat)
- **B005** erkeğin döl sıvısı — erkeğin döl sıvısı
  الفراغة ماء الرجل وهو النطفة (sihah)
- **B006** birine veya işe yönelip kendini ona verme [kalıp] — size yöneleceğiz · bir işe bilerek yönelmek · kendini belirli bir işe vermek
  سنفرغ أي نعمد (maqayis)؛ فرغت إلى أمر كذا أي عمدت له (maqayis)؛ تفرغت لكذا (sihah)

## ث ق ل (root_000202): 55:31 ٱلثَّقَلَانِ

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

## ع ش ر (root_001016): 55:33 يَٰمَعْشَرَ

- **B001** on ve yirmi sayı adları — eril adlarla kullanılan on sayısı · dişil adlarla kullanılan on sayısı · yirmi sayısı · on bir sayısı
  العشرة والعشر في المؤنث (maqayis); العشر عدد المؤنث والعشرة عدد المذكر (ayn;tahdhib); عشرة رجال وعشر نسوة (sihah); العشرة والعشر والعشرون معروفة (mufradat)
- **B002** dokuzu ona tamamlama — dokuz kişiyi ona tamamlayan onuncu kişi · bir topluluğun onuncu kişisi olmak · dokuz kişiyi veya şeyi bir ekleyerek ona tamamlamak
  عشرت القوم إذا صرت عاشرهم (maqayis;ayn;tahdhib); كانوا تسعة فتموا بي عشرة (maqayis;ayn); أعشر القوم صاروا عشرة (sihah); عشرتهم صيرت مالهم عشرة (mufradat)
- **B003** onda bir — onda bir · onda bir · bir şeyin onda biri
  العشر جزء من الأجزاء العشرة وهو العشير والمعشار (maqayis); العشر جزء من عشرة أجزاء وهو العشير والمعشار (ayn); معشار الشيء عشره (sihah;mufradat); العشير والعشر واحد (tahdhib)
- **B004** maldan onda bir alma — mallarının onda birini almak · mallardan onda bir alan görevli
  عشرت القوم إذا أخذت عشر أموالهم (maqayis); عشرتهم تعشيرا أخذت العشر من أموالهم (ayn); إذا أخذت منهم عشر أموالهم ومنه العاشر والعشار (sihah); عشرت أموالهم إذا أخذت منهم العشر (tahdhib); عشرهم أخذ عشر مالهم (mufradat)
- **B005** onar onar gelme — onar onar · onar onar
  جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة (maqayis;ayn;tahdhib); عشار بالضم معدول من عشرة (sihah); جاءوا عشارى عشرة عشرة (mufradat)
- **B006** develerin onuncu gün sulanması — develerin onuncu gün suya gelmesi veya iki sulama arası · her on günde bir suya gelen develer
  العشر ورد الإبل يوم العاشر (maqayis;ayn;tahdhib); العشر بالكسر ما بين الوردين (sihah); العشر في الإظماء وإبل عواشر (mufradat)
- **B007** gebeliği on aya ulaşmış deve — gebeliği on aya ulaşmış deve · gebeliği on aya ulaşmış veya doğumu yaklaşmış develer
  ناقة عشراء وهي التي أقربت سميت عشراء لتمام عشرة أشهر لحملها (maqayis); الناقة التي أتت عليها عشرة أشهر (sihah); إذا بلغت الناقة في حملها عشرة أشهر فهي عشراء (tahdhib); ناقة عشراء مرت من حملها عشرة أشهر وجمعها عشار (mufradat); الظباء الحديثات العهد بالنتاج (tahdhib)
- **B008** eşeğin on kez yinelenen anırması — çok ve art arda anıran eşek · eşeğin on kez anırması
  المعشر الحمار الشديد النهيق (maqayis;ayn;tahdhib); تعشير الحمار نهيقه عشرة أصوات (sihah); التعشير نهاق الحمير لكونه عشرة أصوات (mufradat)
- **B009** parçalara, paylara veya dağınık kümelere ayrılma — kırık parçalar veya bölüşülmüş paylar · parça parça kırılmış çömlek · herhangi bir şeyden ayrılmış parça · her yana dağılmış topluluklar
  العشر القطعة تنكسر من القدح أو البرمة (maqayis); برمة أعشار إذا انكسرت قطعا قطعا (sihah;tahdhib); أعشار الجزور الأنصباء (sihah); قدح أعشار منكسر (mufradat); العشارة القطعة من كل شيء (tahdhib); ذهب القوم عشاريات متفرقين في كل وجه (tahdhib)
- **B010** on arşın uzunluğunda olan şey — on arşın uzunluğunda olan şey
  العشاري ما بلغ طوله عشر أذرع (maqayis); العشارى ما يقع طوله عشرة أذرع (sihah); العشاري ما طوله عشرة أذرع (mufradat)
- **B011** Muharrem ayının onuncu günü — Muharrem ayının onuncu günü · Muharrem ayının onuncu günü
  عاشوراء اليوم العاشر من المحرم (maqayis); يوم عاشوراء وعشوراء أيضا (sihah); يوم عاشوراء هو اليوم العاشر من المحرم (tahdhib)
- **B012** yakın ilişki ve birlikte yaşama — birlikte yaşama ve yakın ilişki · yakın ilişki içinde birlikte yaşama · yakın ilişki kurulan kimse veya eş
  المخالطة والمداخلة فالعشرة والمعاشرة وعشيرك الذي يعاشرك (maqayis); المعاشرة المخالطة وكذلك التعاشر (sihah); العشير الزوج سمي عشيرا لأنه يعاشرها وتعاشره (tahdhib); عاشرته صرت له كعشرة في المصاهرة والعشير المعاشر (mufradat)
- **B013** akraba topluluğu veya ortak amaçlı topluluk — kişinin ailesi, yakın akrabaları veya kabilesi · ortak bir işte birleşen topluluk
  عشيرة الرجل لمعاشرة بعضهم بعضا (maqayis); المعشر كل جماعة أمرهم واحد (maqayis;tahdhib); العشيرة القبيلة (sihah); العشيرة أهل الرجل الذين يتكثر بهم (mufradat)
- **B014** tatlı özsulu iri bir ağaç — tatlı özsuyu olan iri ağaç veya bitki
  العشر نبت (maqayis); العشر شجر له صمغ (sihah); العشر من كبار الشجر وله صمغ حلو (tahdhib)
- **B015** her on ayeti gösteren işaretleme — kutsal metin nüshasında her on ayete işaret koyma · kutsal metin nüshasında her on ayeti gösteren işaretler
  تعشير المصاحف جعل العواشر فيها (sihah); العاشرة حلقة التعشير من عواشر المصحف (tahdhib); العشور في المصاحف علامة العشر الآيات (mufradat)
- **B016** dokuzlu gecelerden sonraki üç gece — ayın dokuzlu gecelerinden sonraki üç gece
  يقال أيضا لثلاث ليال من ليالى الشهر عشر وهي بعد التسع (sihah); كان أبو عبيدة يبطل التسع والعشر إلا أشياء منه معروفة (sihah)
- **B017** kuşun öndeki uçuş telekleri — kuşun öndeki uçuş telekleri
  الأعشار قوادم ريش الطائر (sihah)

## ط و ع (root_000956): 55:33 ٱسْتَطَعْتُمْ

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

## ECHO س ط ع (root_000706): for 55:33 ٱسْتَطَعْتُمْ: withheld observed target; not identity

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

## ن ف ذ (root_001531): 55:33 تَنفُذُوا۟, 55:33 فَٱنفُذُوا۟, 55:33 تَنفُذُونَ

- **B001** delip karşı yana geçme — delip karşı tarafa geçti · delip karşı tarafa geçirdi · içinden geçip kurtulma · öte yana geçmiş saplama yarası · göklerin ve yerin sınırlarını aşıp çıkmak
  نفذ السهم الرمية نفاذا (maqayis)؛ نفذ السهم من الرمية (sihah;tahdhib)؛ نفذت الطعنة أي جاوزت الجانب الآخر (tahdhib)؛ المثقب في الخشب إذا خرق إلى الجهة الأخرى (mufradat)
- **B002** uygulayıp yürürlüğe koyma — işi sürdürüp uyguladı · işinde kararlılıkla ilerleyen · geçerli ve uyulan buyruk · yazı ilgili kişiye ulaştı ve içeriği uygulandı · buyruğu yürürlüğe koyma · uygulama ve yürürlüğe koyma · orduyu sefere gönderdi · yoluna devam et ve git
  هو نافذ ماض في أمره (maqayis)؛ رجل نافذ في أمره أي ماض وأمره نافذ أي مطاع (sihah)؛ وأما النفذ فإنه يستعمل في موضع إنفاذ الأمر (tahdhib)؛ نفذت الأمر تنفيذا والجيش في غزوه (mufradat)
- **B003** geçilebilir ve ulaştıran açıklık — tıkanmamış, çıkışı olan yol · bir yere ulaşır · geçit ve çıkış · iç dünyaya sevinç ya da üzüntü ulaştıran kanallar
  الطريق النافذ الذي يسلك وليس بمسدود (tahdhib)؛ فيه منفذ للقوم أي مجاز (tahdhib)؛ النوافذ كل سم يوصل إلى النفس (tahdhib)؛ المنفذ الممر النافذ (mufradat)
- **B004** kapsamın tümüne erişip aşma [kalıp] — bakış onların hepsine ulaşır · topluluğun ortasından geçip gitti · topluluğu geçip geride bıraktı · bakışı bana ulaşıp beni aştı
  ينفذهم بصر الرحمن حتى يأتي عليهم كلهم؛ أنفذت القوم إذا خرقتهم ومشيت في وسطهم؛ نفذتهم إذا جزتهم حتى تخلفهم؛ نفذني بصره إذا بلغني وجاوزني
- **B005** çıkış yoluna ya da hedefe ulaşma [kalıp] — söylediğine bir çıkış yolu getirdi · çekişen taraflar yargıca ulaştı
  أتى ينفذ ما قال أي بالمخرج منه (sihah)؛ ائتني بنفذ ما قلت أي بالمخرج منه (tahdhib)؛ قد تنافذوا إليه أي خلصوا إليه (tahdhib)
- **B006** atın iki yanındaki beden işareti [kalıp] — atın iki yanında birden bulunan beden işareti
  من دوائر الفرس دائرة نافذة وذلك إذا كانت الهقعة في الشقين جميعا وإذا كانت في شق واحد فهي هقعة

## ق ط ر (root_001238): 55:33 أَقْطَارِ

- **B001** yan, yön ve dış bölüm — yan, yön; yanlar ve yönler · atın veya dağın yüksek, dışa taşan bölümleri
  القطر الناحية والأقطار النواحي (ayn)؛ القطر الناحية والجانب والجمع الأقطار (sihah)؛ أقطارها نواحيها واحدها قطر (tahdhib)؛ القطر الجانب وجمعه أقطار (mufradat)؛ فالقطر الناحية والأقطار الجوانب (maqayis)؛ القتر فالجانب وليس من هذا لأنه من الإبدال وهو القطر (maqayis-ibdal)؛ أقطار الفرس ما أشرف منه وأقطار الجبل أعاليه (ayn;tahdhib)
- **B002** yana devirip düşürmek — birini yana devirip düşürmek · yanı üzerine düşmek
  قطرت فلانا تقطيرا صرعته صرعة شديدة (ayn)؛ طعنه فقطره تقطيرا أي ألقاه على أحد قطريه (sihah)؛ طعنه فقطره إذا ألقاه على أحد قطريه وصرعه (tahdhib)؛ قطرته ألقيته على قطره وتقطر وقع على قطره (mufradat)؛ طعنه فقطره أي ألقاه على أحد قطريه (maqayis)
- **B003** damlama, damla damla akma — yağmur veya damla damla düşen su; damla · damla damla akmak veya düşmek · bir şeyi damla damla akıtmak · idrarı sürekli damlayan deve · tahıl ve benzeri üründen damlayıp sızan sıvı · zehri çokça damlayan yılan · küçük damla; önemsiz ve değersiz şey
  القطر والقطران مصدر قطر الماء (ayn)؛ القطر المطر والقطر جمع قطرة وقد قطر الماء وغيره (sihah)؛ قطر الماء قطرا وقطرانا (tahdhib)؛ قطر المطر أي سقط وسمي لذلك قطرا (mufradat)؛ القطر قطر الماء وغيره وهذا باب ينقاس لأن معناه التتابع (maqayis)؛ البعير القاطر الذي لا يزال بوله يقطر (sihah;tahdhib;maqayis)؛ القطارة ما قطر من الحب ونحوه (sihah)؛ القطاري الحية مأخوذ من القطار وهو سمه الذي يقطر (tahdhib)؛ القطيرة تصغير القطرة وهو الشيء التافه الخسيس (tahdhib)
- **B004** aynı düzende art arda sıralanma — birbirini aynı düzende izleyen deve dizisi · gruplar halinde art arda gelmek · tutukluların ayaklarını tek sıra halinde bağlayan delikli kütük · develeri satış için dizi dizi getirmek
  القطار قطار الإبل بعضها إلى بعض على نسق واحد (ayn;tahdhib)؛ قطار الإبل (sihah;maqayis)؛ تقاطر القوم جاؤوا أرسالا مأخوذ من قطار الإبل (sihah;mufradat;maqayis)؛ المقطرة اشتقت منه لأن من حبس فيها صار على قطار واحد (ayn;tahdhib)؛ قطروا الإبل فجلبوها للبيع قطارا قطارا (sihah;maqayis)
- **B005** ağaçtan elde edilen koyu katran — ağaçtan sızdırılıp pişirilen koyu katran · deveyi katranla kaplamak
  القطران ما يتحلب من شجر الأبهل يطبخ فيتحلب منه (ayn;tahdhib)؛ الهناء هو القطران وتقول قطرت البعير طليته بالقطران (sihah)؛ القطران ما يتقطر من الهناء (mufradat)؛ القطران ممكن أن يسمى بذلك لأنه مما يقطر (maqayis)
- **B006** erimiş bakır — bakır, özellikle erimiş bakır
  القطر النحاس الذائب (ayn)؛ القطر بالكسر النحاس ومنه عين القطر (sihah)؛ القطر النحاس والآني الذي قد انتهى حره (tahdhib)؛ قطرا أي نحاسا مذابا (mufradat)؛ مما ليس من هذا القياس القطر النحاس (maqayis)
- **B007** tütsü odunu ve tütsü kabı — yakılarak koku veren tütsü odunu · tütsü kabı, tütsülük
  القطر عود يتبخر به (ayn;tahdhib)؛ القطر والقطر العود الذي يتبخر به والمقطرة المجمرة (sihah)؛ القطر العود (maqayis)
- **B008** karada gitmek; birinden geri kalmak [kalıp] — karada ilerleyip gitmek · birinden geri kalmak
  قطر في الأرض قطورا ذهب (sihah)؛ قطر الرجل في الأرض قطورا إذا ذهب فيها (tahdhib)؛ تقطر عني أي تخلف عني (tahdhib)؛ قطر في الأرض أي ذهب (maqayis)
- **B009** hücuma hazırlanıp konum almak [kalıp] — savaşa veya hücuma hazırlanıp konum almak
  التقطر لغة في التقتر وهو التهيؤ للقتال (sihah)؛ تقطر فلان للقتال تقطرا وتقتر وتشذر إذا تهيأ له وتحرف لذلك (tahdhib)؛ تشذر فلان وتقتر وتقطر وتشزن إذا تهيأ للحملة (tahdhib)
- **B010** eğilip kurumaya yüz tutmak — bitki eğilip bükülerek kurumaya yüz tutmak
  اقطار النبت اقطيرارا تهيأ لليبس (sihah)؛ قد أقطار أقطيرارا وهو أن ينثني ويعوج ثم يهيج يعني النبات (tahdhib)؛ اقطار النبات إذا قارب اليبس (maqayis)
- **B011** örnek hesaba göre toplu ve ölçüsüz satış — malı örnek hesaba göre veya bütünü ölçmeden topluca satmak
  القطر أن يزن جلة من تمر أو عدلا من المتاع والحب ويأخذ ما بقي على حساب ذلك ولا يزن (tahdhib)؛ القطر هو البيع نفسه (tahdhib)؛ المقاطرة أن يقول بعني ما لك في هذا البيت من التمر جرافا بلا كيل ولا وزن (tahdhib)
- **B012** gidiş dönüş için kiralamak [kalıp] — hem gidiş hem dönüş için kiralamak
  أكريته مقاطرة إذا أكراه ذاهبا وجائيا (tahdhib)
- **B013** yer nispetiyle anılan — belirli bir yere nispet edilen kumaş, binek veya deve kuşu
  القطر أيضا ضرب من البرود يقال لها القطرية (sihah)؛ البرود القطرية حمر لها أعلام فيها بعض الخشونة (tahdhib)؛ مدينة يقال لها قطر وأحسبهم نسبوا هذه الثياب إليها (tahdhib)؛ أراد بالقطريات نجائب نسبها إلى قطر (tahdhib)؛ جعل النعام قطرية نسب النعائم إلى قطر (tahdhib)
- **B014** koyu renkli belirli bir bitki — koyu renkli belirli bir bitkinin adı
  قطور اسم نبات سوادية (ayn)؛ قطوراء ممدود اسم نبت وهي سوادية (tahdhib)

## س ل ط (root_000732): 55:33 بِسُلْطَٰنٍ

- **B001** boyun eğdirme gücü — 
  أصل واحد وهو القوة والقهر؛ السلاطة من التسلط وهو القهر (maqayis)؛ أصله من التسليط (ayn)؛ السلاطة: القهر، وقد سلطه الله فتسلط عليهم (sihah)؛ سمي سلطانا لتسليطه، إلا أنا سلطناه عليهم (tahdhib)؛ السلاطة: التمكن من القهر، يقال سلطته فتسلط (mufradat)
- **B002** üstün gelen güçlü kanıt — 
  والسلطان الحجة (maqayis)؛ السلطان في معنى الحجة، أي حجتيه (ayn)؛ السلطان أيضا: الحجة والبرهان (sihah)؛ كل سلطان في القرآن فهو حجة، والسلطان: الحجة (tahdhib)؛ سمي الحجة سلطانا، فأتونا بسلطان مبين (mufradat)
- **B003** yönetme yetkisi ya da yetkili yönetici — 
  السلطان قدرة الملك، وقدرة من جعل ذلك له (ayn)؛ السلطان: الوالي (sihah)؛ قيل للأمراء: سلاطين؛ السلطان: قدرة الملك وقدرة من جعل ذلك له (tahdhib)؛ قد يقال لذي السلاطة وهو الأكثر (mufradat)
- **B004** keskin, akıcı ve güçlü konuşma — akıcı ve sivri dilli erkek · gürültücü, sivri ya da uzun dilli kadın · dil keskinliği ve söz söyleme gücü · uzun dilli oldu ve gürültülü biçimde çıkıştı · söz söyleme gücü ve dil keskinliği; çoğunlukla yergi bildirir · sivri ya da uzun dilli kadın
  السليط من الرجال الفصيح اللسان الذرب، والسليطة المرأة الصخابة (maqayis)؛ سلطت إذا طال لسانها واشتد صخبها (ayn)؛ رجل سليط فصيح حديد اللسان، وامرأة سليطة صخابة (sihah)؛ امرأة سليطة اللسان: حديدة اللسان أو طويلة اللسان (tahdhib)؛ سلاطة اللسان: القوة على المقال، وذلك في الذم أكثر (mufradat)
- **B005** aydınlatmada kullanılan bitkisel yağ — aydınlatmada kullanılan bitkisel yağ; kimi aktarımlarda özellikle susam yağı
  ومما شذ عن الباب السليط الزيت بلغة أهل اليمن، وبلغة غيرهم دهن السمسم (maqayis)؛ السليط الزيت (ayn)؛ السليط: الزيت عند عامة العرب، وعند أهل اليمن دهن السمسم (sihah)؛ السليط ما يضاء به، ومن هذا قيل للزيت السليط (tahdhib)؛ السليط: الزيت بلغة أهل اليمن (mufradat)
- **B006** uzun, keskin ya da sert parça — uzun ok · uzun oklar ya da keskin uçlar · anahtar dişleri · tek bir anahtar dişi · keskin ya da güçlü ve uzun toynak uçları · bilenmiş keskin uçlar · uzun bacaklar · sert ve dayanıklı toynak ya da taban
  السلطة: السهم الطويل؛ المساليط: أسنان المفاتيح؛ سنابك سلطات، أي حداد (sihah)؛ السلاطة بمعنى الحدة؛ نصالا محددة؛ السلط: القوائم الطوال؛ سلط الحافر (tahdhib)؛ سنابك سلطات: لها تسلط بقوتها وطولها (mufradat)
- **B007** iç yakan yoğun susuzluk — iç yakan yoğun susuzluk
  والسلاط الغليل (ayn)

## ر س ل (root_000563): 55:35 يُرْسَلُ

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

## ش و ظ (root_000828): 55:35 شُوَاظٌ

- **B001** dumansız alev — dumansız ateş alevi
  الشُّواظ شواظ اللهب من النار لا دخان معه (maqayis)؛ الشُّواظ اللهب الذي لا دخان فيه (ayn;mufradat)؛ الشُّواظ والشُّواظ اللهب الذي لا دخان له (sihah)؛ الشُّواظ اللهب الذي لا دخان معه (tahdhib)
- **B002** ateş dumanı veya ateşten ya da güneşten gelen ısı — ateş dumanı, ateş ısısı veya güneş ısısı
  يقال لدخان النار شُواظ ولحرها شُواظ وحر الشمس شُواظ؛ أصابني شُواظ من الشمس (tahdhib)

## ن ح س (root_001480): 55:35 وَنُحَاسٌ

- **B001** uğursuzluk ve ters talih — uğursuzluk, ters talih · uğursuz hâle gelmek · uğursuz, bahtsız · uğursuz gün · uğursuz günler · uğursuz yıl · uğursuz sayılan yıldızlar ve benzerleri · uğursuzluklar, kötü alametler
  النحس خلاف السعد (maqayis;ayn;jamhara); النحس ضد السعد (sihah;tahdhib;mufradat); يوم نحس وأيام نحسات (maqayis;ayn;sihah;tahdhib;mufradat); المناحس المشائم (jamhara)
- **B002** soğuk rüzgâr ve rüzgârda soğuma — çok soğuk günler · soğuk rüzgâr; rüzgârda soğuma
  العرب تسمي الريح الباردة إذا دبرت نحسا (tahdhib); لنحس أي وضعت في ريح فبردت (tahdhib); قيل شديدات البرد (mufradat)
- **B003** kuraklıkta göğü kaplayan veya kalkan toz — kuraklıkta göğü kaplayan veya kalkan toz · toz kalktı
  النحس الغبار في أقطار السماء إذا عكف الجدب عليها (jamhara); النحس الغبار، يقال هاج النحس أي الغبار (tahdhib)
- **B004** kızılımsı bakır veya pirinç türü metal — bakır, pirinç türü metal veya bu metalden kap
  النحاس من هذه الجواهر (maqayis); النحاس ضرب من الصفر شديد الحمرة (ayn); النحاس القطر عربي معروف (jamhara); النحاس معروف (sihah); النحاس الصفر والآنية (tahdhib); تشبيه في اللون بالنحاس (mufradat)
- **B005** alevsiz duman — 
  النحاس الدخان لا لهب فيه (maqayis); النحاس الدخان الذي لا لهب فيه (ayn;jamhara); النحاس أيضا دخان لا لهب فيه (sihah); النحاس الدخان (tahdhib)
- **B006** dumansız alev — 
  فالنحاس اللهيب بلا دخان (mufradat); تشبيه في اللون بالنحاس (mufradat); أصل النحس أن يحمر الأفق فيصير كالنحاس (mufradat)
- **B007** köken, tabiat ve yaradılış — köken, tabiat ve yaradılış · soylu yaradılışlı · soylu bir kökten
  مبلغ أصل الشيء نحاس (maqayis); النحاس مبلغ طبع وأصله (ayn); فلان من نحاس صدق أي من أصل كريم (jamhara); النحاس الطبيعة والأصل وكريم النحاس (sihah); النحاس والنحاس جميعا الطبيعة، ونحاس الرجل ونحاسه سجيته وطبيعته (tahdhib)
- **B008** haberi soruşturup izini sürmek — haberleri soruşturup izlemek · haberin izini sürüp araştırmak
  تنحست الأخبار وعن الأخبار إذا تخبرت عنها وتتبعتها بالاستخبار سرا وعلانية (sihah); استنحست الخبر إذا تندسته وتحسسته (tahdhib)
- **B009** acıkmak; belirli kullanımda hayvan eti yemeyi bırakmak — Hristiyanlar hayvan eti yemeyi bıraktı · acıkmak, aç kalmak
  تنحس النصارى عربي صحيح لتركهم أكل الحيوان ولا أدري ما أصله (jamhara); تنحس فلان إذا تجوع (jamhara)

## ن ص ر (root_001510): 55:35 تَنتَصِرَانِ

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

## ش ق ق (root_000807): 55:37 ٱنشَقَّتِ

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

## ECHO ش ق و (root_000808): for 55:37 ٱنشَقَّتِ: withheld observed target; not identity

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ن ش ق (root_001506): for 55:37 ٱنشَقَّتِ: withheld observed target; not identity

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

## ك و ن (root_001332): 55:37 فَكَانَتْ

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

## و ر د (root_001640): 55:37 وَرْدَةً

- **B001** bir yere yönelip varma ve birini oraya ulaştırma — gelmek veya bir şeye varmak · suya yönelip varmak · getirmek veya hedefe ulaştırmak · getirtmek veya getirilmesini istemek · suya giden veya topluluktan önce gidip su sağlayan kişi · varılan şey veya ulaşılmak istenen su · suya giden yol veya suya varılan yer · suya giden yollar, pınarlar veya varılan yerler · ateşe varmak; bağlama göre ona ulaşmak veya içine girmek
  أصلان أحدهما الموافاة إلى الشيء (maqayis)؛ ورد فلان ورودا حضر وأورده غيره أي أحضره (sihah)؛ الورد ورد القوم الماء والمورد الطريق إلى الماء (tahdhib)؛ الورود أصله قصد الماء ثم يستعمل في غيره (mufradat)
- **B002** alışılmış okuma payı veya belirlenmiş sulama vakti — alışılmış okuma bölümü veya payı · sulama günü ve iki susuzluk dönemi arasındaki belirlenmiş zaman
  الورد: الجزء، يقال قرأت وردي (sihah)؛ الورد وقت يوم الورد بين الظمأين... سمي النصيب من قراءة القرآن وردا من هذا (tahdhib)
- **B003** belirli zamanda gelen ateşli hastalık nöbeti — belirli zamanda gelen ateşli hastalık nöbeti · ateşli hastalık nöbetine tutulmuş kişi
  الورد: ورد الحمى إذا أخذت صاحبها لوقت (maqayis)؛ الورد: يوم الحمى إذا أخذ صاحبها لوقت (sihah)؛ الورد يوم الحمى وقد وردته الحمى فهو مورود (tahdhib)؛ يعبر عن المحموم بالمورود وعن إتيان الحمى بالورد (mufradat)
- **B004** boynun iki yanındaki damarlar; geniş anlamda nabız atan damar — boyun damarı; geniş kullanımda nabız atan damar · boyun damarı · boynun iki yanındaki iki damar
  والوريدان عرقان مكتنفا صفقى العنق... ويسميان من الورود أيضا كأنهما توافيا في ذلك المكان (maqayis)؛ حبل الوريد: عرق... وهما وريدان مكتنفا صفقي العنق (sihah)؛ الوريدان في العنق... عرقان بين الأوداج وبين اللبتين، وكل عرق ينبض فهو من الأوردة (tahdhib)
- **B005** gül ve gül tonundaki kızıllık — gül · bir gül veya gül rengi görünüm · koyu doru ile al arası renkte at · gül renginde aslan · gül rengine boyanmış · ağaç çiçek açtı · kadın yanağına kızıl boya sürdü · gün batımında ufku kızarmış akşam
  الأصل الآخر الورد... لونه لون الورد (maqayis)؛ الورد بالفتح: الذي يشم، وبلونه قيل للأسد ورد وللفرس ورد، وقميص مورد صبغ على لون الورد (sihah)؛ الورد اسم نور، والورد من ألوان الدواب لون يضرب إلى الصفرة الحسنة، وردت المرأة خدها، وعشية وردة إذا احمر أفقها (tahdhib)
- **B006** uzayıp aşağıdaki bir yere erişecek kadar uzun veya sarkık [kalıp] — uzun burunlu · sırta veya kalçaya kadar uzanan saç · dalları aşağı sarkan ağaç
  فلان وارد الأرنبة إذا كان فيها طول (sihah)؛ كل طويل وارد، وشعر وارد... وشجرة واردة الأغصان إذا تدلت أغصانها (tahdhib)؛ وشعر وارد: قد ورد العجز أو المتن (mufradat)
- **B007** bölük bölük içeri girme veya karşıdakinin önüne ilerleme — az az içeri girmek veya birinin önüne ilerlemek · atlar şehre az az ve bölük bölük girdi · rakibinin önüne engellenmeden ilerleyen kişi
  توردت الخيل البلدة أي دخلتها قليلا قليلا قطعة قطعة (sihah)؛ ما لك توردني أي تقدم علي، والمتورد هو المتقدم على قرنه (tahdhib)

## د ه ن (root_000497): 55:37 كَٱلدِّهَانِ

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

## ذ ن ب (root_000521): 55:39 ذَنۢبِهِۦٓ

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

## ع ر ف (root_001002): 55:41 يُعْرَفُ

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

## ج ر م (root_000239): 55:41 ٱلْمُجْرِمُونَ, 55:43 ٱلْمُجْرِمُونَ

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

## س و م (root_000764): 55:41 بِسِيمَٰهُمْ

- **B001** alım satımda fiyat isteme ve pazarlık — alım satımda fiyat isteme ve teklif etme · fiyat pazarlığı · bir mal için fiyat isteme veya fiyat bildirme · istenen fiyat veya fiyat düzeyi
  أصل يدل على طلب الشيء (maqayis); السوم سومك في البياعة ومنه المساومة والاستيام (ayn); السوم في المبايعة؛ ساومته سواما واستام علي وتساومنا (sihah); السوم عرض السلعة على البيع؛ سمت فلانا سلعتي سوما؛ غالي السيمة (tahdhib); السوم أصله الذهاب في ابتغاء الشيء؛ السوم في البيع (mufradat)
- **B002** eziyet veya kötülük yükleme — size ağır işkence çektirmek · onu aşağılanmaya uğratmak · işkence etmek veya ağır bir güçlüğe zorlamak · gereksiz bir şeyi teklif etmek
  سمته خسفا أي أوليته إياه وأوردته عليه (sihah); يسومونكم سوء العذاب؛ يولونكم سوء العذاب؛ تجشم إنسانا مشقة أو سوءا أو ظلما؛ سام إذا عذب (tahdhib); يسومونكم سوء العذاب؛ سيم فلان الخسف فهو يسام الخسف (mufradat)
- **B003** serbestçe otlama ve otlatmaya salma — hayvanların merada dilediğince otlaması · serbest bırakılarak otlayan hayvan · serbestçe otlayan sürü · develeri otlamaya salmak · orada hayvan otlatırsınız · hizmetçimi kendi isteğine bırakmak · birine malım üzerinde karar yetkisi vermek · otlamaya salınmış atlar · atları serbest bırakmış olanlar
  سامت الراعية تسوم وأسمتها أنا؛ سومت غلامي خليته وما يريد؛ الخيل المسومة المرسلة (maqayis); الخيل المسومة المرعية؛ السوام والسائم المال الراعي؛ سامت الماشية؛ أسمتها أنا (sihah); سامت الراعية إذا رعت حيث شاءت؛ السوام كل ما رعى؛ أسمت الإبل إذا خليتها ترعى؛ الخيل المسومة المرسلة (tahdhib); سامت الإبل فهي سائمة؛ سمت الإبل في المرعى وأسمتها وسومتها (mufradat)
- **B004** tanıtıcı işaret ve işaretleme — bir şeyin üzerine konan işaret · bir şeyi tanıtan işaret · tanıtıcı işaret için kullanılan iki uzatılmış biçim · işaret konmuş veya işaret taşıyan · mühür benzeri izler taşıyan taşlar · bir işaretle belirlenmiş olanlar · atına tanıtıcı işaret koymak · koyunların yünündeki işaretler
  السومة وهي العلامة؛ السيما؛ السيماء (maqayis); السومة العلامة؛ المسومة المعلمة؛ مسومة عليها أمثال الخواتيم؛ السيما والسيماء والسيمياء (sihah); السيم العلامات؛ مسومين معلمين؛ سوم فلان فرسه إذا أعلم عليه؛ السيما هي العلامة (tahdhib); السيماء والسيمياء العلامة؛ سومته أي أعلمته؛ مسومين معلمين (mufradat)
- **B005** ilerleyip geçme — sürekli ilerleyiş veya hızlı geçiş · rüzgarın geçişi ve sürekli esişi · geçip gitmek · devenin ilerleyip gitmesi veya hızlanması
  السوم من سير الإبل وهبوب الريح إذا كانت مستمرة في سكون (ayn); سام أي مر؛ سوم الرياح مرها (sihah); السوم سرعة المر؛ سرعة المر مع قصد الصواب؛ سام يسوم إذا مر؛ سامت الناقة إذا مضت (tahdhib)

## ء خ ذ (root_000018): 55:41 فَيُؤْخَذُ

- **B001** ele geçirip edinme — nesneyi ele geçirip almak · al · söylediğimi dinle, kuşkuyu ve çekişmeyi bırak · yuları tut · alma eylemini yoğunluk bildiren kalıpla anlatan biçim
  الأصل حوز الشيء وجبيه وجمعه (maqayis)؛ الأخذ التناول (ayn)؛ أخذت الشئ آخذه أخذا تناولته (sihah)؛ خلاف العطاء وهو التناول (tahdhib)
- **B002** suçundan sorumlu tutma [kalıp] — onu suçundan ötürü hesaba çekip cezalandırdı
  آخذه بذنبه مؤاخذة (sihah)
- **B003** yakalayıp tutsak etme — tutsak edilmiş kişi · falanca yakalanıp tutsak edildi · onları tutsak edin
  الأخيذ الأسير والمرأة أخيذة (sihah)؛ ومن هنا قيل للأسير أخيذ وقد أخذ فلان إذا أسر وخذوهم معناه ائسروهم (tahdhib)
- **B004** büyüsel yolla etkileyip engelleme — gözü ve benzeri durumları etkilediğine inanılan sözlü uygulama veya büyüsel nesne · eşi başka kadınlarla birleşmekten büyüsel yollarla alıkoyma · kadınlarla birleşmekten büyüsel yolla alıkonmuş
  الأخذة رقية تأخذ العين ونحوها والمؤخذ الرجل كأنه حبس (maqayis)؛ الأخذة رقية تأخذ العين ورجل مؤخذ عن النساء (ayn)؛ الأخذة رقية كالسحر أو خرزة تؤخذ بها النساء الرجال من التأخيذ (sihah)؛ التأخيذ حيل من السحر تمنع الزوج من جماع غيرها (tahdhib)
- **B005** sahiplenilip işletilen arazi — kişinin kendisi için sahiplenip denetimine aldığı arazi
  الإخاذة الضيعة يتخذها الإنسان لنفسه (ayn)؛ الاخاذة والاخاذ أرض يجوزها الرجل لنفسه أو السلطان (sihah)؛ الإخاذة الأرض يأخذها الرجل فيحوزها لنفسه ويتخذها ويحييها (tahdhib)
- **B006** su tutan çukur veya havuz — suyu günlerce tutan birikme yeri, havuz veya çukur
  الإخاذ مجمع الماء شبيه بالغدير (maqayis)؛ الإخاذة والإخذ ما حفرت لنفسك كهيئة الحوض تمسك الماء أياما (ayn)؛ الاخاذة شئ كالغدير والجمع إخاذ (sihah)؛ الإخذ صنع الماء يجتمع فيه (tahdhib)
- **B007** bedende bir durumun baş gösterip etkisini göstermesi — süt emen yavru fazla sütten rahatsızlandı · deve veya koyunda deliliğe benzer bir hal başladı · gözü yangılandı · hastalık veya göz ağrısı yüzünden başını eğip çökmüş kişi · yağ tutmaya başlamış deve
  الأدواء تسمى بهذا لأخذها الإنسان واستأخذ الرمد فيه (maqayis)؛ الأخذ من الإبل حين يأخذ فيه السمن وأخذ البعير كهيئة الجنون ومريض مستأخذ (ayn)؛ أخذ الفصيل اتخم من اللبن ورجل أخذ أي رمد والمستأخذ لمطأطئ رأسه من رمد أو وجع (sihah)؛ بعينه أخذ وهو الرمد وأخذ البعير كهيئة الجنون والفصيل اتخم من اللبن (tahdhib)
- **B008** ay konaklarının yıldızları [kalıp] — ayın her gece birinde bulunduğu ay konaklarının yıldızları
  نجوم الأخذ منازل القمر لأن القمر يأخذ كل ليلة في منزل (maqayis)؛ نجوم الأخذ منازل القمر لأن القمر يأخذ كل ليلة في منزل منها (sihah)؛ نجوم الأخذ هي نجوم منازل القمر لأخذ القمر في منازلها (tahdhib)
- **B009** bir topluluğun yolunu ve özelliklerini benimseme [kalıp] — bizim yolumuzu, tutumumuzu ve özelliklerimizi benimseyip izledi
  لو كنت منا لأخذت بإخذنا أي بخلائقنا وشكلنا (sihah)؛ لأخذت بإخذنا أي بشكلنا وهدينا ومن أخذ إخذهم أي من سار سيرهم (tahdhib)
- **B010** kendisi için edinip kazanma — bir şeyi kendisi için edinmek veya kazanmak · mal edindim veya kazandım · bunun karşılığında ücret alırdım
  الإتخاذ من تخذ يتخذ تخذا وتخذت مالا أي كسبته (ayn)؛ الاتخاذ افتعال من الأخذ وتخذ يتخذ (sihah)؛ اتخذ فلان مال الله دولا وتخذت مالا أي كسبته ولو شئت لتخذت عليه أجرا (tahdhib)
- **B011** güreşte kavrayıp kilitleme [kalıp] — topluluk karşılıklı kavrayarak dövüştü veya güreşti · güreşçinin rakibini kilitlediği kavrama tutuşu
  ائتخذوا في القتال أي أخذ بعضهم بعضا (sihah)؛ ائتخذ القوم إذا تصارعوا فأخذ كل واحد على مصارعه أخذة يعتقله بها (tahdhib)
- **B012** kancalı aracın tutamağı [kalıp] — kancalı aracın sapı ve tutamağı
  إخاذة الحجنة مقبضها وهي ثقافها (tahdhib)

## ن ص ي (root_001512): 55:41 بِٱلنَّوَٰصِى

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

## ق د م (root_001207): 55:41 وَٱلْأَقْدَامِ

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

## ط و ف (root_000957): 55:44 يَطُوفُونَ

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

## ح م م (root_000001): 55:44 حَمِيمٍ

- **B001** kömürleşme ve kara is — kömür, yanık kül · bir kömür parçası · kara duman veya kapkara şey · yüzünü isle kararttı · yavrunun tüyleri çıktı · tıraştan sonra başı karardı · siyah, kara renkli · kapkara şey veya kara renkli bitki · siyahlık, kara renk
  الحمم الفحم؛ اليحموم الدخان؛ حممته إذا سخمت وجهه بالسخام (maqayis)؛ الحمم أيضا الفحم البارد؛ جارية حمة أي سوداء؛ اليحموم الدخان (ayn)؛ الحمحم الشديد السواد؛ الأحم الأسود؛ الحمم الرماد والفحم؛ اليحموم أيضا الدخان (sihah)؛ الحمم الفحم البارد؛ اليحموم الشديد السواد؛ حممت وجه الرجل إذا سودته بالحمم؛ حمم رأسه بعد الحلق إذا اسود (tahdhib)
- **B002** sıcak su ve onun kullanımı — sıcak veya kaynar su · sıcak su kaynağı · suyu ısıttı · sıcak suyla yıkandı; sonradan genel olarak yıkandı · ısıtılmış su
  الحميم الماء الحار والاستحمام الاغتسال به (maqayis)؛ الحميم الماء الحار؛ الحمة عين فيها ماء حار (ayn)؛ الحميم الماء الحار؛ الحمة العين الحارة؛ حممت الماء أي سخنته (sihah)؛ الحميم الماء الحار؛ الحمة عين ماء فيها ماء حار؛ الحميمة الماء يسخن (tahdhib)؛ الحميم الماء الشديد الحرارة (mufradat)
- **B003** eritilmiş yağ veya yağ artığı — eritilmiş kuyruk yağı veya yağ artığı · eritilmiş yağdan bir parça · kuyruk yağını eritti
  الحم وهي الألية تذاب فالذي يبقى منها بعد الذوب حم واحدته حمة (maqayis)؛ الحم ما اصطهرت إهالته من الألية والشحم الواحدة حمة (ayn)؛ الحم ما يبقى من الألية بعد الذوب؛ حممت الألية أي أذبتها (sihah)؛ الحم ما اصطهرت إهالته من الألية والشحم؛ ما أذيب من الألية فهو حم (tahdhib)
- **B004** sıcağın ter ve yaz üzerindeki etkisi — ter · at terledi · sıcak yaz yağmuru · yakıcı yaz sıcağı
  الحميم وهو العرق (maqayis)؛ الحميم العرق؛ استحم الفرس إذا عرق (ayn)؛ الحميم العرق؛ استحم أي عرق؛ الحميم المطر الذي يأتي في شدة الحر؛ الحميم القيظ (sihah)؛ الحميم العرق؛ استحم الفرس إذا عرق؛ الحميم المطر الذي يكون في الصيف حين تسخن الأرض (tahdhib)
- **B005** ateşli hastalık ve ona bağlı nitelemeler — deve veya hayvan ateşi · adam ateşli hastalığa tutuldu · arazi ateşli hastalığın yaygın olduğu yer oldu · yiyeni ateşli hastalığa düşüren yiyecek
  الحمام وهو حمى الإبل؛ أحمت الأرض إذا صارت ذات حمى (maqayis)؛ أحمت الأرض؛ حم الرجل فهو محموم؛ الحمام حمى الإبل والدواب (ayn)؛ حم الرجل من الحمى؛ أحمت الأرض صارت ذات حمى؛ الحمام بالضم حمى الإبل؛ أرض محمة ذات حمى (sihah)؛ حم البعير حماما؛ حم الرجل حمى شديدة؛ المحمة أرض ذات حمى؛ طعام محمة (tahdhib)
- **B006** vakti yaklaşmak ve gelmek [kalıp] — ihtiyaç yaklaştı, vakti geldi · iş yaklaştı, zamanı geldi
  أحمت الحاجة حضرت وأحم الأمر دنا (maqayis)؛ أحمت حاجة الغد أي حانت ولزمت (ayn)؛ أحم خروجنا أي دنا؛ أجم الأمر وأحم أي حان وقته (sihah)؛ أحمت الحاجة وأجمت إذا دنت؛ أحم قدومهم دنا (tahdhib)
- **B007** atın alçak yem isteme sesi — atın kişnemeden alçak sesi · at alçak ses çıkardı
  الحمحمة حمحمة الفرس عند العلف (maqayis)؛ الحمحمة صوت الفرس دون الصوت العالي (ayn)؛ حمحم الفرس وتحمحم وهو صوته إذا طلب العلف (sihah)؛ الحمحمة صوت للبرذون دون الصوت العالي وللفرس دون الصهيل (tahdhib)
- **B008** hedefe yönelmek ve peşine düşmek — onun hedeflediği şeye yöneldim · onu istedim, peşine düştüm · bineğin yola çıkışını hızlandırdım
  حممت حمة أي قصدت قصده (maqayis)؛ حم هذا لذاك أي قضي وقدر وقصد (ayn)؛ حممت حمك أي قصدت قصدك؛ حممت ارتحال البعير أي عجلته؛ حاممته أي طالبته (sihah)؛ حممت حمه أي قصدت قصده؛ حاممته محامة طالبته (tahdhib)
- **B009** boşanma sonrası maddi destek vermek — boşadığı kadına maddi destek verdi · boşanma desteği olarak verilen giysiler
  حممها إذا متعها بثوب أو نحوه (maqayis)؛ يطلق المرأة فيحممها أي يمتعها تحميما (ayn)؛ حمم امرأته أي متعها بشيء بعد الطلاق (sihah)؛ حممها إياها أي متعها بها بعد الطلاق؛ ثياب التحمة ما يلبس المطلق امرأته إذا متعها (tahdhib)
- **B010** belirlenmiş yazgı ve ölüm payı — iş karara bağlandı ve belirlendi · belirlenmiş ölüm payı · belirlenmiş ayrılık payı · ölümler, ölüm payları
  حم الأمر قضي؛ الحمام قضاء الموت؛ حم هذا لذاك أي قضي وقدر؛ الحمم المنايا (ayn)؛ حم أيضا بمعنى قدر؛ الحمام بالكسر قدر الموت؛ حمة الفراق ما قدر وقضي (sihah)؛ حم الأمر إذا قدر؛ نزل به حمامه أي قدره وموته؛ عجلت بنا حمة الفراق وحمة الموت (tahdhib)
- **B011** sevilen yakın ve özel aile çevresi — sevilen ve seven yakın kişi · kişinin yakın ailesi ve akrabaları
  الحامة خاصة الرجل من أهله وولده وذوي قرابته؛ الحميم الذي يودك وتوده (ayn)؛ حميمك قريبك الذي تهتم لأمره؛ الحامة الخاصة أقرباؤه (sihah)؛ الحميم القريب الذي توده ويودك؛ الحامة خاصة الرجل من أهله وولده وذي قرابته؛ الحميم القرابة (tahdhib)
- **B012** güvercin türünden kuş — güvercinler ve güvercin türleri · bir güvercin; kimi kullanımlarda erkek veya dişi
  الحمام طائر؛ حمامة ذكر وحمامة أنثى والجميع حمام (ayn)؛ الحمام عند العرب ذوات الأطواق؛ الواحدة حمامة؛ اليمام الحمام الوحشي (sihah)؛ الحمامة طائر؛ الحمام كل ما كان ذا طوق؛ كل ما عب وهدر فهو حمام (tahdhib)
- **B013** su ısıtma kabı veya yıkanma yapısı — küçük su ısıtma kabı · yıkanma yapısı
  المحم القمقم الصغير يسخن فيه الماء؛ الحمام مشددا واحد الحمامات المبنية (sihah)؛ جاء بمحم أي بقمقم يسخن فيه الماء؛ طاب حميمك وحمتك للذي يخرج من الحمام (tahdhib)
- **B014** malın seçkin ve değerli bölümü — seçkin develer veya değerli mallar · seçkin develer · malın en değerli parçası
  الحميمة واحدة الحمائم وهي كرائم المال؛ إبل حامة إذا كانت خيارا (sihah)؛ الحميمة وجمعها حمائم كرائم الإبل؛ الحمامة خيار المال (tahdhib)
- **B015** canlıya göre değişen arka beden bölgesi — insanın arka alt bölgesi, kaba et · devenin hörgüç çıkıntısı veya atın sağrısı
  الحماء الدبر لأنه محمم بالشعر (ayn)؛ الحماء سافلة الإنسان (sihah)؛ الحمامة سعدانة البعير؛ الحمامة من الفرس القص (tahdhib)
- **B016** biçime bağlı yalıtık adlandırmalar — ayna; saray avlusu; kuyu makarası; güzel kadın; kapı halkası
  الحمامة المرآة؛ الحمامة ساحة القصر النقية؛ الحمامة بكرة الدلو؛ الحمامة المرأة الجميلة؛ الحمامة حلقة الباب (tahdhib)
- **B017** bir işte kararlı ve sabit kalmak — bu işte kararlı ve sabitim
  أنا محام على هذا الأمر أي ثابت عليه (tahdhib)

## ء ن ي (root_000063): 55:44 ءَانٍ

- **B001** ağırdan alma ve geciktirme — ağırbaşlılık ve acele etmeme · bir işte acele etmemek, bekleyip yumuşak davranmak · işlerde duraklayıp acele etmeme · bir şeyi geciktirmek, bekletmek ve yavaşlatmak · birini aceleye sürmemek, onun için beklemek · acele etmeyen, ağırbaşlı kişi · ağırbaşlı kadın veya kalkarken gevşek davranan kadın
  الأناة الحلم والفعل منه تأنى وتأيا (maqayis)؛ التأني (maqayis)؛ آنيت يعني أخرت المجيء وأبطأت (maqayis)؛ الإيناء بمعنى الإبطاء وآنيت الشيء أي أخرته (ayn)؛ آناه يؤنيه إيناء أي أخره وحبسه وأبطأه (sihah)؛ الأناة التؤدة وتأنيت تأخرت (mufradat)
- **B002** gecenin zaman bölümleri — gecenin zaman bölümleri · gecenin tek bir zaman bölümü · ara sıra, zaman zaman
  الإني والأنى ساعة من ساعات الليل والجمع آناء (maqayis;ayn)؛ وآناء الليل واحدها إني وهي الساعة من الليل (jamhara)؛ آناء الليل ساعاته (sihah;tahdhib;mufradat)
- **B003** zamanı gelip olgunluğa erişme — bir şeyin zamanı, olgunluğu veya erişme noktası · zamanı gelmek, olgunlaşmak ve erişmek · senin için zamanı gelmedi mi · yemeğin pişip olgunlaşmasını beklemek · ısısı doruğa varmış çok sıcak su · ısısı yükselmiş sıcak kaynak · olgunlaşmış ve erişmiş
  الإني إدراك الشيء (maqayis)؛ انتظرنا إنى الطعام أي إدراكه (maqayis;ayn)؛ ما أنى لك ولم يأن لك أي لم يحن (maqayis;ayn)؛ حميم آن قد انتهى حره وعين آنية (maqayis;ayn)؛ أنى الشيء يأنى إنى أي حان وأنى أيضا أدرك (sihah)؛ بلغ إناه من شدة الحر (mufradat)
- **B004** içine şey konan kap — içine bir şey konan kap · kaplar ve daha geniş çoğul biçimi
  الإناء ممدود من الآنية والأواني جمع جمع (maqayis)؛ الإناء معروف وجمعه آنية والأواني (sihah)؛ الإناء ما يوضع فيه الشيء وجمعه آنية (mufradat)
- **B005** nereden ve nasıl diye sorma sözü — nereden, hangi yönden, nasıl veya ne zaman · bu sana nereden ya da nasıl geldi · hangi yönden gelirsen, sana gelirim · nereye ya da nasıl yönelirse
  أنى معناها كيف ومن أين (ayn)؛ أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف (sihah)؛ أنى أداة لها معنيان متى ومن أين ويحتمل كيف (tahdhib)؛ أنى للبحث عن الحال والمكان (mufradat)

## ECHO ء و ن (root_000068): for 55:44 ءَانٍ: withheld observed target; not identity

- **B001** yumuşak ve rahat davranma — yumuşak davrandı · rahatlık, dinginlik ve yumuşak davranma · yolculukta kendini yorma, rahat git · yumuşak ve rahat davrandın · rahat ve dingin adam · rahat ve dingin geceler
  كلمة واحدة تدل على الرفق (maqayis); آن يؤون أونا إذا رفق (maqayis); الأون: الدعة والسكينة والرفق (sihah); أن على نفسك أي ارفق في السير واتدع (maqayis;sihah); رجل آئن (maqayis); رجل آين أي رافه وادع (sihah); ليال أوائن روافه وآينات وادعات (sihah)
- **B002** yük yanı — yük kabının bir yanı; dengeli yük parçası · iki yanlı çıkın veya çift yanlı yük · eşeğin yiyip içince karnı ve iki yanı yük gibi doldu
  الأون: أحد جانبي الخرج (sihah); الأون: العدل (sihah); أون الحمار إذا أكل وشرب وامتلأ بطنه وامتدت خاصرتاه فصار مثل الأون (sihah)
- **B003** belirli zaman — belirli zaman · ayrı zamanlar, ara ara gelen vakitler · o işi ara sıra yapar ve ara sıra bırakır
  الأوان: الحين، والجمع آونة (sihah); فلان يصنع ذلك الأمر آونة إذا كان يصنعه مرارا ويدعه مرارا (sihah)
- **B004** büyük kemerli yapı bölümü — büyük kemerli yapı bölümü · büyük kemerli yapı bölümü; belirli saray örneğiyle de anılır · büyük kemerli yapı bölümü · büyük kemerli yapı bölümleri · büyük kemerli yapı bölümleri
  الأوان والإيوان: الصفة العظيمة كالأزج (sihah); إيوان كسرى (sihah); جمع الإوان أون وجمع الإيوان إيوانات وأواوين (sihah)

## خ و ف (root_000447): 55:46 خَافَ

- **B001** bir belirtiye dayanarak kötü bir şey bekleme korkusu — korku · korkmak · korku hali · korku halleri · korku ve sakınma · korkan kimse · çok korkan adam · korkan topluluk · korkan topluluk · kork! · onun başına bir şey gelmesinden korkmak
  الخوف ضد الأمن خاف يخاف خوفا (jamhara خفو)؛ والخيفة مثل الخوف والجمع خيف (jamhara خيف)؛ خاف الرجل يخاف خوفا وخيفة ومخافة فهو خائف؛ والخيفة الخوف والجمع خيف وأصله الواو (sihah)؛ الخوف توقع مكروه عن أمارة مظنونة أو معلومة ويضاد الخوف الأمن (mufradat)؛ أصل واحد يدل على الذعر والفزع؛ خفت الشيء خوفا وخيفة (maqayis 992)؛ الخيف فجمع خيفة وليس من هذا الباب وقد ذكر في باب الواو بعد الخاء (maqayis 1001)؛ الخيفة الخوف (ayn)
- **B002** korku doğurma ya da korkulur kılma — korkutma veya korkuyla sakındırma · başkasını korkutma · korkutucu · korkulan veya tehlikeli · insanların korktuğu tehlikeli yol · Tanrı'nın korku uyandırarak sakındırması
  ومنه التخويف والإخافة؛ طريق مخوف يخافه الناس ومخيف يخيف الناس؛ خوفت الرجل جعلت فيه الخوف؛ خوفت الرجل أي صيرته بحال يخافه الناس (ayn)؛ الإخافة التخويف؛ وجع مخيف أي يخيف من رآه؛ طريق مخوف لأنه لا يخيف وإنما يخيف فيه قاطع الطريق (sihah)؛ التخويف من الله تعالى هو الحث على التحرز؛ ذلك يخوف الله به عباده؛ الشيطان يخوف أولياءه (mufradat)
- **B003** korkuda yarışıp ötekinden daha çok korkma — korkuda yarışıp ötekinden daha çok korkmak
  خاوفه فخافه يخوفه غلبه بالخوف أي كان أشد خوفا منه (sihah)؛ خاوفني فلان فخفته أي كنت أشد خوفا منه (maqayis)
- **B004** bir şeyden alarak eksiltme — bir şeyi eksiltip ondan bir bölüm almak
  والتخوف التنقص (ayn)؛ وتخوفه أي تنقصه (sihah)؛ تخوفناهم أي تنقصناهم تنقصا اقتضاه الخوف منه (mufradat)؛ تخوفت الشيء أي تنقصته فهو الصحيح الفصيح إلا أنه من الإبدال والأصل النون من التنقص (maqayis)
- **B005** korkunun kişide dışa vurması — korkunun kişide dışa vurması
  والتخوف ظهور الخوف من الإنسان (mufradat)
- **B006** arıcı ya da su taşıyıcısının deri torbası veya üstlüğü — arıcı veya su taşıyıcısının deri torbası, kabı ya da üstlüğü · aynı eşyanın küçük biçimi
  الخافة تصغيرها خويفة واشتقاقها من الخوف وهي جبة يلبسها العسال والسقاء والخافة العيبة (ayn)؛ الخافة خريطة من أدم يشتار فيها العسل (sihah)

## ف ن ن (root_001180): 55:48 أَفْنَانٍ

- **B001** güçlük çıkarma, sertçe sürme ve geciktirme — eziyet, zorlama ve sertçe sürme · adamı eziyete sokup zorlama · sürüp uzaklaştırma · develeri sürüp uzaklaştırma · develeri sürüp uzaklaştırır · oyalama ve geciktirme
  الفن وهو التعنية والإطراد الشديد، فننته فنا (maqayis)؛ الفن الطرد، فننت الإبل (sihah)؛ الفن العناء، فننت الرجل، الفن الطرد، الفن المطل (tahdhib)
- **B002** tür, çeşit, yol veya anlatım biçimi — tür ya da çeşit · türler ve çeşitler · türler, yollar ve anlatım biçimleri · konuşmasında ve söylevinde türlü anlatım yolları kullanmak · çok yönlü ve türlü becerileri olan · sözü bir türden ötekine geçirerek çeşitlendirmek · çeşitlendirme ve türden türe geçme · konuşması türlü yollar ve beklenmedik açılımlar taşıyan kişi · renkler ya da türler · iki ayrı renge sahip olanlar
  الأفانين أجناس الشيء وطرقه (maqayis)؛ فن من الفنون أي ضرب من الضروب (jamhara)؛ الفن واحد الفنون وهي الأنواع، والأفانين الأساليب وهي أجناس الكلام وطرقه (sihah)؛ الفنون الضروب، يفنن الكلام أي يشتق في فن بعد فن، أفنان بمعنى الألوان (tahdhib)؛ يقال ذلك للنوع من الشيء وجمعه فنون، وقيل ذواتا ألوان مختلفة (mufradat)
- **B003** ağaç dalı; dala benzetilen saç tutamı — dal; özellikle düz ya da taze yapraklı dal · dallar · dalları olan iki şey · çok dallı ağaç · dalları olan ağaç · ağaç dalları · dala benzetilen saç tutamları · uzun ve güzel saç · kıvrımlı dal
  الفنن وهو الغصن وجمعه أفنان، شجرة فنواء (maqayis)؛ الفنن جمعه أفنان ثم أفانين وهي الأغصان (sihah)؛ الفنن الغصن المستقيم، أفنان بمعنى الأغصان، أفانين جمع أفنان وهو الخصلة من الشعر شبه بالغصن، الفينان الشعر الطويل الحسن (tahdhib)؛ الفنن الغصن الغض الورق وجمعه أفنان (mufradat)
- **B004** uyumsuz karıştırma ve kararsızca çeşitlendirme — uyumsuz biçimde karıştırma · yabancı çizgileri veya göze batan kusuru bulunan kumaş · görüşünü değiştirip birinde durmamak · düzensiz koşu veya dağınık konuşma
  التفنين التخليط، ثوب فيه تفنين إذا كانت فيه طرائق ليست من جنسه (sihah)؛ التفنين فعل الثوب إذا بلي فتفزر بعضه، فنن فلان رأيه إذا لونه ولم يثبت، التفنين البقعة السخيفة السمجة في الثوب، الأفنون الجري المختلط والكلام المثبج (tahdhib)
- **B005** durum — durum
  الفن الحال (tahdhib)
- **B006** bir zaman dilimi — zamandan bir bölüm · zamandan bir bölüm
  فنة من الدهر وفينة من الدهر وضربة من الدهر أي طرفا من الدهر (tahdhib)
- **B007** şaşırtıcı ve olağandışı iş — şaşırtıcı, olağandışı iş · şaşırtıcı işler yapan adam
  لاجعلن لابنة عثم فنا أي أمرا عجبا، رجل مفن يأتي بالعجائب (sihah)

## ع ي ن (root_001069): 55:50 عَيْنَانِ, 55:66 عَيْنَانِ

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

## ز و ج (root_000652): 55:52 زَوْجَانِ

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

## و ك ء (root_001678): 55:54 مُتَّكِـِٔينَ, 55:76 مُتَّكِـِٔينَ

- **B001** kap agzini sikica baglayan bag — tulum ya da kap agzini sikica baglayan ip veya kayis · tulumu ya da kabi agiz bagiyla sikica baglamak
  الوكاء الذي يشد به (maqayis)؛ الوكاء كل سير أو خيط يشد به السقاء أو الوعاء (tahdhib)؛ الوكاء رباط الشيء (mufradat)
- **B002** vermekten kacinma veya agzini tutup susma — cimrilik edip vermekten kacinmak · elinden hicbir sey cikarmayan cimri · agzini tutup konusmamak · agzini kapa ve sus · iki yer arasinda konusmamak
  سألته فأوكى على أي بخل (maqayis)؛ فلان لوكاء ما يبض بشيء (maqayis)؛ يوكي فاه فلا يتكلم (tahdhib)؛ أوك حلقك أي شد فمك واسكت (tahdhib)
- **B003** arayi siddetli yuruyusle butunuyle katetme — iki yer arasini siddetli yuruyusle butunuyle katetmek · yuruyusunu sertlestirip kendini zorlayan kisi
  يوكى بين الصفا والمروة أي يملأ ما بينهما سعيا (maqayis)؛ الإيكاء في كلام العرب يكون بمعنى السعي الشديد (tahdhib)؛ الموكي الذي يتشدد في مشيه (tahdhib)؛ يملأ ما بينهما سعيا كما يوكى السقاء بعد الملء (mufradat)
- **B004** yaslanma, dayanak saglama ve yaslandirma — bir seye yaslanip ondan destek almak · bir seye dayanip yaslanmak · cok yaslanan kimse · yaslanilan sey · yaslanilan yer ya da dayanak · oturulan yer · birine yaslanacagi dayanak hazirlamak · birini destek uzerine koyup yaslandirmak · birini yaslanan kisi durusuna sokmak
  توكأت على كذا أي اتكأت (maqayis)؛ التوكؤ التحامل على العصا (ayn;tahdhib)؛ اتكأ على الشيء فهو متكئ والموضع متكأ (sihah)؛ أوكأت فلانا إيكاء إذا نصبت له متكأ (ayn;sihah;tahdhib)؛ توكأ على العصا اعتمد بها وتشدد بها (mufradat)
- **B005** cinsel birlesmeye siddetle ihtiyac duyma [kalıp] — cinsel birlesmeye siddetle ihtiyac duyan
  فلان موكي الغلمة ومزك الغلمة ومشط الغلمة إذا كانت به حاجة شديدة إلى الخلاط (tahdhib)
- **B006** dogum sancisinda devenin kivranmasi [kalıp] — devenin dogum sancisinda kivranip carpinmasi
  توكأت الناقة وهو تصلقها عند مخاضها (ayn;tahdhib)
- **B007** dolup dolgunlasma veya bosaltimin tutulmasi — develerin yaglanip dolgunlasmasi · insanin karninin tutulup diski cikaramamasi · tulumun ya da benzeri bir kabin dolmasi · kalin derili tulum agzi icin kullanilan, anlami belirsiz niteleme
  استوكت الإبل استيكاء إذا امتلأت سمنا (tahdhib)؛ استوكى بطن الإنسان وهو أن لا يخرج منه نجوه (tahdhib)؛ للسقاء ونحوه إذا امتلأ قد استوكى (tahdhib)

## ف ر ش (root_001143): 55:54 فُرُشٍۭ

- **B001** yayıp düzleyerek hazırlama — sermek, yayıp düzlemek · işini ona bütünüyle açıp anlatmak · üzerinde yerleşmeye elverişli kılınmış yer · evin zeminini döşemek · geniş
  أصل صحيح يدل على تمهيد الشيء وبسطه؛ فرشت الفراش أفرشه (maqayis)؛ فرشت الفراش بسطته؛ فرشته أمري بسطته كله له (ayn)؛ فرشت الشيء بسطته؛ الفرش الفضاء الواسع؛ أكمة مفترشة الظهر إذا كانت دكاء (sihah)؛ فرشت زيدا بساطا؛ فرش فلان داره إذا بلطها؛ فرشته أمري أي بسطته كله (tahdhib)؛ الفرش بسط الثياب؛ جعل لكم الأرض فراشا أي ذللها (mufradat)؛ الفرشاط الواسع مما زيدت فيه الطاء والأصل فرش (maqayis_variant)
- **B002** serili yatak ve döşek — serili ev eşyası, döşek · oturmak için serilen örtü · ev veya kuş yuvası
  الفرش المفروش أيضا (maqayis)؛ المفرش شيء يكون مثل شاذكونه؛ المفرشة على الرحل (ayn)؛ الفراش واحد الفرش؛ الفرش المفروش من متاع البيت (sihah)؛ الفراش ما ينامان عليه؛ الفراش البيت؛ الفراش عش الطائر؛ المفرشة تكون على الرحل (tahdhib)؛ يقال للمفروش فرش وفراش؛ وفرش مرفوعة؛ فرش بطائنها من إستبرق (mufradat)
- **B003** evlilik bağı ve yatağı — eş veya evlilik birliğinin sahibi · çocuk evlilik birliğinin sahibine bağlanır · soylu kadınlarla evlenmiş · bir erkeğin birlikte olduğu cariye
  الولد للفراش؛ أراد به الزوج؛ الفراش في الحقيقة المرأة؛ كريم المفارش إذا تزوج كريم النساء (maqayis)؛ جارية فريش افترشها الرجل (ayn)؛ الفراش يكنى به عن المرأة؛ كريم المفارش إذا تزوج كرائم النساء؛ افترشه أي وطئه (sihah)؛ الفراش الزوج؛ الفراش المرأة؛ الولد للفراش معناه لمالك الفراش؛ جارية فريش قد افترشها الرجل؛ افترش كريمة بني فلان إذا تزوجها (tahdhib)؛ كني بالفراش عن كل واحد من الزوجين؛ الولد للفراش؛ كريم المفارش أي النساء (mufradat)
- **B004** küçük veya yük taşımayan evcil hayvan — küçük, yük taşımayan veya kesimlik evcil hayvanlar
  الفرش من الأنعام الذي لا يصلح إلا للذبح والأكل (maqayis)؛ الفرش من النعم التي لا تصلح إلا للذبح وهي ما دون الحمولة؛ ومن الأنعام حمولة وفرشا (ayn)؛ الفرش صغار الإبل؛ حمولة وفرشا؛ يحتمل أن يكون مصدرا من فرشها الله أي بثها بثا (sihah)؛ الفرش الصغار؛ أجمع أهل اللغة على أن الفرش صغار الإبل وأن الغنم والبقر من الفرش (tahdhib)؛ الفرش ما يفرش من الأنعام أي يركب؛ حمولة وفرشا (mufradat)
- **B005** ışık çevresinde çırpınan küçük güve — ışığa veya ateşe uçan küçük güve · pervane gibi hafif adam
  الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف (maqayis)؛ الفراش التي تطير طالبة للضوء؛ يقال للخفيف من الرجال فراشة (ayn)؛ الفراشة التي تطير وتهافت في السراج؛ أطيش من فراشة (sihah)؛ الفراش ما تراه كصغار البق يتهافت في النار؛ الفراش الذي يطير؛ الخفيف من الرجال فراشة (tahdhib)؛ الفراش طير معروف؛ كالفراش المبثوث (mufradat)
- **B006** yere yakın kanat çırpma — yere yakın kanatlarını açıp çırpmak
  تفرش الطائر إذا قرب من الأرض ورفرف بجناحه؛ فجاءت الحمرة تفرش (maqayis)؛ تفرش الطائر رفرف بجناحيه وبسطهما (sihah)؛ فرش الطائر تفريشا إذا جعل يرفرف على الشيء وهي الشرشرة والرفرفة (tahdhib)
- **B007** bedeni veya uzuvları yere yayma — toprağı veya örtüyü altına serip üzerine yatmak · kollarını yere serip üzerlerine dayanmak · yere devirip altına almak veya üzerine basmak · yolda ilerlemek · bacakları birbirinden ayırmak
  افترش السبع ذراعيه (maqayis)؛ افترش فلان ترابا أو ثوبا تحته؛ افترش الذئب ذراعيه ربض عليهما (ayn)؛ افترش الشيء أي انبسط؛ افترش ذراعيه بسطهما على الأرض؛ افترشه أي وطئه (sihah)؛ افتراش السبع أن يبسط ذراعيه؛ لقي فلان فلانا فافترشه إذا صرعه؛ افترش القوم الطريق إذا سلكوه (tahdhib)؛ الفرشحة أن يفرج الإنسان بين رجليه ويباعد إحداهما من الأخرى وهي من فرش وفسح (maqayis_variant)
- **B008** yayılmış ekin ve ince küçük dallar — yere yayılan veya en az üç yapraklı ekin · ağaç ve yakacağın ince küçük parçaları
  الفرش دق الحطب (maqayis)؛ الفرش من الشجر والحطب الدق الصغار (ayn)؛ الفرش الزرع إذا فرش؛ المفرش الزرع إذا انبسط (sihah)؛ الفرش الزرع الذي بثلاث ورقات أو أكثر؛ الفرش من الشجر والحطب الدق والصغار (tahdhib)
- **B009** ince su kalıntısı, kurumuş iz veya kabarcık — su çekilince kuruyup kabuklanan çamur · kapta veya yerde kalan az su · içecek veya ter yüzeyindeki küçük kabarcıklar
  الفراشة الماء على وجه الأرض قبيل نضوبه؛ الفراشة من الأرض الذي نضب عنه الماء فيبس وتقشر (maqayis)؛ فراش القاع والطين ما يبس بعد نضوب الماء؛ ما بقي في الحوض إلا فراشة من ماء (ayn)؛ الفراش ما يبس بعد الماء من الطين على وجه الأرض؛ فراش النبيذ الحبب وكذلك حبب العرق (sihah)؛ فراش القاع والطين ما يبس بعد نضوب الماء؛ الفراش أقل من الضحضاح؛ فراش المسيح كالجمان المحبب (tahdhib)؛ الفراشة الماء القليل في الإناء (mufradat)
- **B010** ince kemik veya metal levha — kafatasının ince kemik tabakaları veya dil altındaki et · ince kemik veya demir levha · kilit ve gemdeki ince metal parçalar · omuz başlarındaki çıkıntılar ve kaş kemiği
  فراش الرأس طرائق دقاق تلي القحف؛ الفراشة فراشة القفل (maqayis)؛ فراش اللسان لحمه تحته؛ فراش الرأس طرائق من القحف (ayn)؛ الفراشة كل عظم رقيق؛ فراش الرأس عظام رقاق تلي القحف؛ فراشة القفل ما ينشب فيه (sihah)؛ فراش اللسان اللحمة التي تحتها؛ فراش الرأس طرائق رقاق من القحف؛ كل رقيق من عظم أو حديد فهو فراشة؛ الفراش عظم الحاجب؛ فراشا الكتفين؛ فراشا اللجام الحديدتان (tahdhib)؛ به شبه فراشة القفل (mufradat)
- **B011** ince kemik tabakasına ulaşan yara — ince kafatası kemiğine ulaşan veya kemiği çatlatan yara · kemiğin içine giren delici yara
  شجة مفترشة ومفرشة تبلغ فراش القحف؛ طعنة فارشة مفرشة أي داخلة في العظم (ayn)؛ المفرشة الشجة التي تصدع العظم ولا تهشم (sihah)؛ المنقلة التي يخرج منها فراش العظام؛ ضربة فأطار فراش رأسه؛ طعنة فارشة مفرشة (tahdhib)
- **B012** dili serbest bırakma ve sözle kötüleme [kalıp] — dilini tutmadan istediği gibi konuşmak · arkadaşının ardından kötü konuşmak · dostlarına karşı açık ve cömert
  أفرش الرجل صاحبه إذا اغتابه وأساء القول؛ كأنه توطأه بكلام غير حسن؛ افترش الرجل لسانه إذا تكلم كيف شاء (maqayis)؛ افترش فلان لسانه يتكلم به ما شاء (ayn)؛ افترش لسانه إذا تكلم كيف شاء أي بسطه (sihah)؛ افترش فلان لسانه يتكلم كيف ما يشاء؛ فلان كريم متفرش لأصحابه إذا كان يفرش نفسه لهم (tahdhib)؛ أفرش الرجل صاحبه أي اغتابه وأساء القول فيه (mufradat)
- **B013** el çekme veya üzerinden kalkma [kalıp] — ondan el çekmedi, onu bırakmadı · ölüm üzerlerinden kalktı
  ما أفرش عنه أي ما أقلع (sihah)؛ أفرش عنهم الموت أي ارتفع؛ ضربه فما أفرش عنه حتى قتله أي أقلع عنه (tahdhib)؛ ما أفرش عنه أي ما أقلع عنه؛ تبعد عن قياس الباب وأظنها من باب الإبدال كأنه أفرج (maqayis)
- **B014** doğumdan yedi gün sonraki kısrak — doğumunun üzerinden yedi gün geçmiş tek tırnaklı dişi · kısrak bekledi
  مما شذ عن هذا الأصل الفريش من الخيل التي أتى لوضعها سبعة أيام (maqayis)؛ الفريش من الخيل التي أتى عليها من يوم وضعت سبعة أيام وبلغت أن يضربها الفحل (ayn)؛ كل ذات حافر فهي فريش بعد نتاجها بسبعة أيام (sihah)؛ أفرشت الفرس إذا استأنت؛ الفريش من الخيل التي أتى عليها بعد ولادتها سبعة أيام؛ الفريش من الحافر بمنزلة النفساء (tahdhib)
- **B015** deve bacağında ölçülü açıklık veya hörgüçsüzlük — deve bacağındaki az ve olumlu açıklık · bacağı dışa eğri dişi deve · hörgücü olmayan erkek deve
  جمل مفرش لا سنام له (maqayis)؛ الفرش في رجل البعير اتساع قليل وهو محمود؛ إذا كثر فهو العقل؛ أن لا يكون فيها انتصاب ولا إقعاد (sihah)؛ ناقة مفروشة الرجل إذا كان فيها انئطار وانحناء؛ الفرش مدح والعقل ذم؛ الفرش اتساع في رجل البعير (tahdhib)
- **B016** yalan söyleme — yalan; yalan söylemek
  الفرش الكذب؛ كم تفرش أي كم تكذب (tahdhib)

## ب ط ن (root_000128): 55:54 بَطَآئِنُهَا

- **B001** karın, iç ya da alt yüz — karın; bir şeyin iç veya alt yüzü · yerin içi · vadinin iç kesimi · avuç içi · ayakkabının ayağa değen iç yüzü · teleğin sap altında kalan yüzü · birinin karnına vurmak · doğurmak · yumurtlamak ya da dışkılamak · dişi deveyi on kez yavrulatmak · atın ön bacaklarının içindeki iki damar · kılıcı böğrünün altına yerleştirmek · çene altındaki sakalı kırpmak
  البطن خلاف الظهر (maqayis;sihah;mufradat)؛ بطن الإنسان معروف (tahdhib)؛ البطن في كل شيء خلاف الظهر كبطن الأرض وظهرها (ayn)؛ بطن الراحة وظهر الكف وباطن الخف (ayn;tahdhib)؛ ألقت المرأة ذا بطنها (ayn;tahdhib)
- **B002** gizli iç yüz ve onu kavrama — işin görünmeyen iç yüzü · işin iç yüzünü bilmek · işe derinlemesine girip iç yüzünü öğrenmek · gizli veya içeride kalan yan · gizli ya da kişiye özgü iyilik
  باطن الأمر دخلته خلاف ظاهره (maqayis)؛ بطنت هذا الأمر إذا عرفت باطنه (maqayis;sihah)؛ تبطنت في هذا الأمر أي دخلت فيه حتى عرفت باطنه (ayn)؛ كل غامض بطن وكل ظاهر ظهر (mufradat)؛ الباطن علم السرائر والخفيات (tahdhib)
- **B003** astar ve astarlama — giysi astarı · giysiyi astarlamak · astarlı örtü
  البطانة والظهارة يعني باطن الثوب وظاهره (ayn)؛ بطانة الثوب خلاف ظهارته (sihah)؛ بطن فلان ثوبه تبطينا وهي البطانة والظهارة (tahdhib)؛ بطنت ثوبي بآخر جعلته تحته (mufradat)
- **B004** sırlara alınmış yakın çevre — kişinin sırlarına alınmış yakın çevresi · birinin özel çevresine girmek · birini özel çevresine almak
  بطانته دخلاؤه الذين يبطنون أمره (maqayis)؛ بطانة الرجل وليجته من القوم (ayn)؛ بطنت بفلان صرت من خواصه (sihah)؛ البطانة الدخلاء الذين ينبسط إليهم ويستبطنون (tahdhib)؛ تستعار البطانة لمن تختصه بالاطلاع على باطن أمرك (mufradat)
- **B005** karın görünüşü, doluluğu, yeme düşkünlüğü ya da rahatsızlığı — karnı iri adam · karın rahatsızlığı olan kişi · çok yiyen, karnı sürekli şiş kişi · karnı çökük kişi · tıka basa doyma ve karın doluluğu · yemekten başka şey düşünmeyen kişi
  البطين الرجل العظيم البطن والمبطون العليل البطن والمبطان الكثير الأكل والمبطن الخميص البطن (maqayis)؛ البطنة امتلاء البطن من الطعام (ayn)؛ بطن بالكسر عظم بطنه من الشبع (sihah)؛ المبطان ضخم البطن من كثرة الأكل (tahdhib)؛ البطنة كثرة الأكل (mufradat)
- **B006** yük hayvanının karın altı kayışı — devenin karnı altından geçirilen yük kayışı · devenin karın altı kayışını sıkmak · iş iyice çetinleşti
  البطان بطان الرحل وهو حزامه وذلك أنه يلي البطن (maqayis)؛ البطان للبعير كالحزام للدابة (ayn)؛ البطان للقتب الحزام الذي يجعل تحت بطن البعير (sihah)؛ البطان الحزام الذي يلي البطن (tahdhib)؛ البطان حزام يشد على البطن (mufradat)
- **B007** kabile içindeki soy bölümü [kalıp] — Araplarda kabileden küçük soy topluluğu
  البطن من العرب دون القبيلة (maqayis;sihah)؛ البطن من العرب اعتبارا بأنهم كشخص واحد (mufradat)
- **B008** Koç'un karın bölgesindeki ay konağı [kalıp] — Koç'un karın bölgesindeki yıldız veya ay konağı
  البطين نجم يقال إنه بطن الحمل (maqayis)؛ البطين من منازل القمر وهو بطن الحمل (sihah)؛ البطين نجم من منازل القمر بين الشرطين والثريا (tahdhib)؛ البطين نجم هو بطن الحمل (mufradat)
- **B009** vadiye girmek; arazi veya otlukta dolaşmak — otluğun içinde dolaşmak · vadinin iç kesimine girmek
  تبطنت الكلأ إذا جولت فيه (maqayis)؛ تبطنت الأرض والكلأ أي جولت فيه (ayn)؛ بطنت الوادي دخلته (sihah)؛ تبطنت الوادي أي دخلت بطنه وجولت فيه (tahdhib)؛ بطن الوادي (mufradat)
- **B010** cariyesiyle karın karına temas; erkek damızlığın dişi sürünün tümüyle çiftleşip onları gebe bırakması — cariyesiyle karın karına cinsel temasta bulunmak · erkek damızlığın sürüdeki bütün dişileri döllemesi
  تبطنت الجارية (sihah)؛ تبطن الرجل جاريته إذا باشرها ولمسها (tahdhib)؛ تبطنها إذا باشر بطنه بطنها (tahdhib)؛ استبطن الفحل الشول إذا ضربها كلها فلقحت (tahdhib)

## ج ن ي (root_000267): 55:54 وَجَنَى

- **B001** Ürünü yetiştiği yerden toplama, toplanan ürün, başkası için toplama ve ürün verir duruma gelme — meyveyi veya başka bir ürünü ağacından ya da yetiştiği yerden toplamak · ağaçtan veya başka bir yerden toplanan, çoğunlukla taze ürün · zamanında toplanmış veya toplandığında tazeliğini koruyan meyve · toplanıp getirilen seçme ürün · toplanabilir ürünü alma · biri için veya birinin hesabına ürün toplamak · ağacın meyvesinin olgunlaşması veya ağacın ürün verir hale gelmesi · toprağın ot, mantar ve benzeri toplanabilir ürünlerce bollaşması · kazanan veya elde eden kişi
  أخذ الثمرة من شجرها (maqayis)؛ جنيت الثمرة أجنيها واجتنيتها (maqayis;sihah)؛ الجنى الرطب والعسل وكل ثمرة تجتنى (ayn;tahdhib)؛ ما يجتنى من الشجر وغيره (sihah)؛ كل ثمر يجتنى فهو جنى (tahdhib;mufradat)؛ جنيت فلانا جنى أي جنيته له؛ الجاني الكاسب (tahdhib)؛ أجنى الشجر وأجنت الأرض (sihah;mufradat)
- **B002** Kendine, topluluğuna ya da başkasına karşı suç işleyip sonucundan bizzat sorumlu olma — kendisine veya topluluğuna yük getiren ya da birine yönelen suç işlemek · suçu işleyen ve bu yüzden cezalandırılan kişi · Sana karşı suç işleyen, senin suçlundur. · Yıkımına yol açanlar, onu düşüncesizce kuranlardır.
  جنيت الجناية أجنيها (maqayis)؛ جنى فلان جناية أي جر جريرة على نفسه أو على قومه (ayn;tahdhib)؛ جنى عليه جناية (sihah)؛ استعير من ذلك جنى فلان جناية (mufradat)؛ يعاقب بجنايته ولا يؤخذ غيره بذنبه (tahdhib)
- **B003** Suçsuz birine işlemediği bir suçu yükleme [kalıp] — birine işlemediği bir suçu yüklemek · birine asılsız bir suç yüklemek
  تجنى فلان علي ذنبا إذا تقوله علي وأنا بريء (ayn)؛ التجني مثل التجرم وهو أن يدعي عليك ذنبا لم تفعله (sihah)؛ تجنى فلان على فلان ذنبا لم يجنه إذا تقوله عليه وهو بريء (tahdhib)
- **B004** Her toplayan kendine ayırırken topladığının en iyisini arkadaşına verme sözü — Topladığımın seçmesini dostuma veririm; herkes topladığını kendi ağzına götürse de.
  هذا جناي وخياره فيه إذ كل جان يده إلى فيه؛ يضرب هذا مثلا للرجل يؤثر صاحبه بخيار ما عنده؛ يجتنوا له الكمأة (tahdhib)

## د ن و (root_000493): 55:54 دَانٍ

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

## ق ص ر (root_001231): 55:56 قَٰصِرَٰتُ, 55:72 مَّقْصُورَٰتٌ

- **B001** kısa olma veya kısaltma; kısa çocuk doğurma ya da yaşla diş uçlarının kısalması — kısalık · kısa olmak · kısaltmak · kısa boylu çocuklar doğurmak · yaşlanıp dişlerinin uçları kısalmak
  القصر خلاف الطول (maqayis;mufradat)؛ قصر الشيء خلاف طال (sihah)؛ القصر نقيض الطول (tahdhib)؛ قصرته أي صيرته قصيرا (maqayis;sihah;tahdhib;mufradat)؛ أقصرت المرأة ولدت أولادا قصارا (maqayis;sihah;tahdhib;mufradat)؛ أقصرت الشاة أسنت حتى تقصر أطراف أسنانها (maqayis;sihah;tahdhib;mufradat)
- **B002** hedefe erişememe, görevde gevşeklik veya hakkı eksik verme — ulaşamamak, erişememek · işte gevşek davranmak, savsaklamak · birine hakkından az vermek · tembellik
  ألا يبلغ الشيء مداه ونهايته (maqayis)؛ قصرت عنه قصورا عجزت (maqayis)؛ قصرت عن الشيء عجزت عنه ولم أبلغه (sihah;tahdhib)؛ قصر السهم عن الهدف أي لم يبلغه (sihah;mufradat)؛ قصرت في الأمر تقصيرا إذا توانيت (maqayis;sihah;mufradat)؛ قصر فلان في الحاجة إذا ونى فيها وضعف (tahdhib)؛ قصرت بفلان أي أعطيته مخسوسا (ayn)؛ مقصر أي أمر دون أو يسير (sihah;tahdhib)
- **B003** ibadeti yolculukta kısaltma veya saçı bütünüyle almadan kesme [kalıp] — yolculukta ibadetin bazı birimlerini bırakmak · saçın bir bölümünü kesip tamamını almamak
  قصر الصلاة وهو ألا يتم لأجل السفر (maqayis)؛ قصرت الصلاة قصرا وقصرتها (ayn)؛ قصرت من الصلاة (sihah;tahdhib;mufradat)؛ قصر من شعره تقصيرا إذا حذف منه شيئا (tahdhib;mufradat)؛ التقصير من الشعر مثل القصر (sihah)
- **B004** hapsetmek veya belirli bir kişi ya da şeye özgü tutmak; gücü varken vazgeçmek — hapsetme, engelleme · çadırlarda alıkonmuş kadınlar · bakışlarını eşlerinden başkasına çevirmeyen kadınlar · kendini yalnızca bir şeye yöneltip sınırlamak · dişi devenin sütünü belirli bir ata ayırmak · gücü varken vazgeçmek · değerinden dolayı başıboş bırakılmayan at · evinde korunaklı tutulan, dışarı çıkmayan kadın
  القصر الحبس يقال قصرته إذا حبسته (maqayis;sihah)؛ حور مقصورات في الخيام أي محبوسات (maqayis;tahdhib;mufradat)؛ قاصرات الطرف لا تمده إلى غير بعلها (maqayis;ayn;sihah;tahdhib;mufradat)؛ قصرت نفسي على كذا (ayn;tahdhib)؛ قصرت اللقحة على فرسي حبست درها عليه (sihah;tahdhib;mufradat)؛ أقصر عنه إذا كف ونزع مع القدرة (maqayis;sihah;tahdhib;mufradat)؛ فرس قصير مقربة لا تترك ترود (maqayis;sihah;tahdhib)؛ امرأة قصيرة وقصورة أي مقصورة في البيت (maqayis;sihah;tahdhib)
- **B005** saray veya çevrilerek ayrılmış özel bölüm — saray, görkemli büyük yapı · çevrilmiş özel bölüm; ibadet yöneticisinin durduğu ayrılmış yer
  القصر واحد القصور (sihah)؛ القصر المجدل أي الفدن الضخم (ayn;tahdhib)؛ قصر مشيد ويجعل لك قصورا (mufradat)؛ المقاصير جمع مقصورة وكل ناحية من الدار الكبيرة إذا أحيط عليها فهي مقصورة (maqayis;ayn;tahdhib)؛ مقصورة الجامع (sihah)
- **B006** varılan son sınır veya bu sınırla yetinme — son sınır, varılabilecek en ileri nokta · yapabileceğinin en ilerisi · bununla yetinmek
  القصر الغاية وهو القصار والقصارى (ayn)؛ قصرك أي أجلك وموتك وغايتك (ayn;tahdhib)؛ قصرك وقصاراك أي غايتك وآخر أمرك وما اقتصرت عليه (sihah;tahdhib)؛ اقتصر على كذا أي قنع به (ayn;mufradat)؛ قصاراك أن تفعل كذا (maqayis)
- **B007** akşamın yaklaşması ve karanlığın karıştığı vakte girme — karanlık karışıp yayılmak · akşam yaklaşmak · akşamın bu vaktine girmek
  قصر الظلام وهو اختلاطه (maqayis;sihah)؛ أقبلت مقاصر الظلام (maqayis;sihah;tahdhib)؛ قصر العشي إذا أمسيت (sihah;tahdhib)؛ أقصرنا أي دخلنا في ذلك الوقت (maqayis;sihah;tahdhib)؛ أتيته قصرا أي عشيا (sihah;tahdhib)
- **B008** boynun veya ağacın kalın dip kısmı; boyun dibindeki hastalık — boynun veya ağacın kalın dip kısmı · boyun dibinden hastalanmak
  القصر جمع قصرة وهي أصل العنق وأصل الشجرة ومستغلظها (maqayis)؛ القصرة أصل العنق والجمع قصر (sihah)؛ قصر النخل الواحدة قصرة (tahdhib)؛ القصر أصول الشجر الواحدة قصرة (tahdhib;mufradat)؛ القصر داء يأخذ في القصرة (maqayis;sihah;tahdhib)
- **B009** böğürle karın arasındaki alt kaburga — böğürle karın arasındaki alt kaburga
  القصيرى أسفل الأضلاع وهي الواهنة (maqayis)؛ القصيرى الضلع التي تلي الشاكلة بين الجنب والبطن (ayn;sihah;tahdhib)
- **B010** başkalarını dışlayan özel tahsis veya doğrudan yakınlık — yalnız onlara özgü; doğrudan yakın · öz amca oğlu, yakın amca oğlu · babasıyla tanınan ve soyunu daha uzağa götürmeyen
  قصرة أي يقصر به عليهم خاصة لا يعطى غيرهم (ayn)؛ هو ابن عمه قصرة ومقصورة أي دنيا (sihah;tahdhib)؛ أبلغ هذا الكلام بني فلان قصرة ومقصورة أي دون الناس (tahdhib)؛ فلان جاري مقاصري أي قصره بحذاء قصري (tahdhib)؛ قصير النسب إذا كان أبوه معروفا (tahdhib)
- **B011** kumaşı döverek işleme; ayrıca giysi veya ipi kısaltma — kumaşı dövüp işlemek · kumaş işleme ustası ve mesleği
  قصرت الثوب والحبل تقصيرا (maqayis)؛ قصرت الثوب أقصره قصرا دققته ومنه سمي القصار (sihah)؛ القصار يقصر الثوب قصرا وحرفته القصارة (tahdhib)
- **B012** başakta kalan tane, tane kabuğu veya saman dibi — dövmeden sonra başakta kalan tane · başaktaki tanenin dış kabuğu
  القصارة ما بقي في السنبل من الحب بعدما يداس (sihah;tahdhib)؛ القصرة قشر الحبة إذا كانت في السنبلة وهي القصارة (tahdhib)؛ القصر والقصل أصول التبن (tahdhib)
- **B013** boynu yakından saran kısa kolye — boynu yakından saran kısa kolye
  التقصار قلادة شبيهة بالمخنقة (maqayis;sihah;tahdhib)؛ التقصار والتقصارة قلادة قصيرة (sihah;mufradat)؛ قصارها أطواقها (tahdhib)
- **B014** soğuk su veya otlağı yakında olan su — soğuk su veya otlağı yakında olan su
  ماء قاصر أي بارد (sihah)؛ ماء قاصر ومقصر إذا كان مرعاه قريبا (tahdhib)
- **B015** hurma saklanan kamış veya hasır örgüsü kap — hurma saklanan kamış veya hasır örgüsü kap
  القوصرة وعاء من قصب للتمر (tahdhib)؛ القوصرة هذا الذي يكنز فيه التمر من البواري (sihah)؛ القوصرة معروفة (mufradat)

## ط ر ف (root_000931): 55:56 ٱلطَّرْفِ

- **B001** kenar, uç veya yan — kenar, uç, yan veya yön · uçlar, kenarlar veya yönler · iki tarafından hangisinin üstün olduğu bilinmez · ekinin uçlarından alınan bölüm · burnunda ve kuyruğunda birer iğne bulunan yılan
  طرف الشيء والثوب والحائط (maqayis)؛ الطرف الناحية من النواحي والطائفة من الشئ (sihah)؛ أطراف الأرض نواحيها وأطراف النهار ساعاته وأطراف الأصابع (tahdhib)؛ طرف الشيء جانبه ويستعمل في الأجسام والأوقات (mufradat)؛ كريم الطرفين أي الأب والأم وقيل الذكر واللسان (mufradat)
- **B002** göz kırpma ve bakış — göz kırpma veya göz kapaklarını kapatma · göz, görme veya bakış · bakışlarını indirenler · aslanın gözleri sayılan iki yıldız · gözler
  الطرف تحريك الجفون في النظر (maqayis;ayn;tahdhib)؛ الطرف العين (sihah)؛ الطرف اسم جامع للبصر (ayn;tahdhib)؛ طرف بصره إذا أطبق أحد جفنيه على الآخر (sihah)؛ طرف العين جفنه والطرف تحريك الجفن وعبر به عن النظر (mufradat)
- **B003** gözü etkileyip yaşartma — erkeklere gözü kayan veya bir erkeğe bağlı kalmayan kadın · gözüne bir şey değdi ve gözü yaşardı · bir şeyin değmesiyle yaşaran göz · keder onu ağlatıp gözünü etkiledi · çokluğu veya şaşırtıcılığıyla gözü hayrete düşüren şey
  عين مطروفة يصيبها طرف شيء ثوب أو غيره فتغرورق دمعا وطرفها الحزن (maqayis)؛ الطرف إصابتك عينا بثوب أو غيره وطرفها الحزن بالبكاء (ayn)؛ طرفت عينه إذا أصبتها بشئ فدمعت والطرفة نقطة حمراء من الدم (sihah)؛ الدنيا قد طرفت أعينكم ومطروفة العينين (tahdhib)؛ طرف فلان أصيب طرفه (mufradat)؛ جاء فلان بطارفة عين أي بشيء تتحير له العين من كثرته (maqayis)؛ جاء فلان بطارفة عين إذا جاء بمال كثير (sihah)
- **B004** soylu ve köklü — anne ve baba tarafından soylu · yakın akrabalar veya seçkinler · iki tarafından hangisinin üstün olduğu bilinmez · soylu at, soylu kişi veya köklü soy
  هو كريم الطرفين يراد به نسب الأب والأم (maqayis;sihah;tahdhib;mufradat)؛ أطرافه أبواه وإخوته وأعمامه وكل قريب له محرم (sihah;tahdhib)؛ الأطراف بمعنى الأشراف (sihah;tahdhib)؛ الطرف الفرس الكريم (maqayis;sihah;tahdhib)؛ فلان طريف النسب (tahdhib)
- **B005** yeni veya yeni edinilmiş — yeni şey veya yeni edinilmiş mal · yenisini edinmek veya yeni satın almak · yeni edinilip beğenilen şey
  الشيء المستحدث طريف وهو خلاف التليد واطرفت الشيء إذا استحدثته (maqayis)؛ اطرفت الشئ أي اشتريته حديثا والطارف والطريف من المال المستحدث وهو خلاف التالد والتليد (sihah)؛ هل وراك طريفة خبر تطرفنا والطرفة كل شيء استحدثته فأعجبك (tahdhib)؛ وقد أطرفت مالا والطريف ما يتناوله (mufradat)
- **B006** bir yerde durmayıp yenisine yönelme — otlak kenarlarında veya çayırlar arasında dolaşan deve · eşine, arkadaşına veya sözüne bağlı kalmayan kişi · erkeklere gözü kayan veya bir erkeğe bağlı kalmayan kadın
  ناقة طرفة ترعى أطراف المرعى ولا تختلط بالنوق (maqayis)؛ الرجل الطرف الذي لا يثبت على امرأة ولا صاحب والمرأة المطروفة لا تثبت على رجل (maqayis)؛ ناقة طرفة لا تثبت على مرعى واحد ورجل طرف لا يثبت على امرأة ولا على صاحب (sihah)؛ ناقة طرفة إذا كانت تطرف الرياض روضة بعد روضة ورجل طرف وامرأة طرفة إذا كانا لا يثبتان على عهد (tahdhib)؛ ناقة طرفة ومستطرفة ترعى أطراف المرعى (mufradat)
- **B007** çadır kenarı ve uçları işaretli giysi — çadırın dışarı bakmak için kaldırılan yanları · uçlarında iki işaret veya bordür bulunan giysi · deriden yapılmış çadır
  الطوارف من الخباء ما رفعت من جوانبه لتنظر (maqayis;sihah;tahdhib)؛ المطرف من الثياب ما جعل في طرفيه علمان (sihah;tahdhib)؛ الطراف بيت من أدم (maqayis;sihah;tahdhib)؛ الطراف بيت أدم يؤخذ طرفه ومطرف الخز ما يجعل له طرف (mufradat)
- **B008** uçları farklı renkte — uçları gövdesinden farklı renkte hayvan · kız parmak uçlarını boya ile renklendirdi
  المطرف من الخيل هو الأبيض الرأس والذنب وسائر جسده يخالف ذلك (sihah)؛ نعجة مطرفة وهي التي اسودت أطراف أذنيها وسائرها أبيض (tahdhib)؛ طرفت الجارية بنانها إذا خصبت أطراف أصابعها بالحناء (tahdhib)
- **B009** çevirip geri püskürtme — onu bir şeyden çevirip geri döndürdü · ordunun uç kesiminde savaşıp karşıdakileri geri sürdü · birini arkadaşlarının gerisinden geri çevirme
  طرفه عنه أي صرفه ورده (sihah)؛ طرف فلان إذا قاتل حول العسكر لأنه يحمل على طرف منهم فيردهم إلى الجمهور (sihah)؛ طرفت فلانا إذا صرفته عن شيء (tahdhib)؛ التطريف أن يرد الرجل الرجل عن أخريات أصحابه (tahdhib)
- **B010** belirli ağaç ve olgun ot adları — belirli ağaç topluluğu ve onun tek ağacı · olgunlaşıp beyazlaşmış belirli ot · bu otun bol bulunduğu arazi
  الطرفاء شجر والواحدة طرفة (sihah)؛ الطريفة النصى إذا ابيض وأرض مطروفة كثيرة الطريفة (sihah)؛ الطرف اسم يجمع الطرفاء والواحدة طرفة (tahdhib)؛ الطريفة من النصي والصليان إذا أعتما وتما وقد أطرفت الأرض (tahdhib)

## ط م ث (root_000949): 55:56 يَطْمِثْهُنَّ, 55:74 يَطْمِثْهُنَّ

- **B001** dokunma; olumsuz kuruluşlarda daha önce dokunulmamış olma — dokunma ve değme · onlara daha önce hiç kimse dokunmadı · otlağa daha önce hiç kimse dokunmadı ya da ondan yararlanmadı · çayıra daha önce hiç kimse dokunmadı ya da ondan yararlanmadı · dişi deveye daha önce hiçbir erkek deve dokunmadı
  أصل صحيح يدل على مس الشيء؛ الطمث المس وذلك في كل شيء يمس (maqayis;sihah)؛ لم يطمثهن أي لم يمسسهن (ayn;jamhara;tahdhib)؛ ما طمث المرتع أو الروضة أحد وما طمث الناقة حبل أو جمل (maqayis;sihah;mufradat)
- **B002** cinsel birleşmeyle dokunma ve kızlık zarını bozma — kadına cinsel birleşmeyle dokundu veya kızlık zarını bozdu · genç kadının kızlık zarını bozdu · benden önce cinsel birleşme yaşamamışlardı
  طمث الرجل المرأة مسها بجماع (maqayis)؛ الطمث الافتضاض وطمثت الجارية افترعتها (ayn)؛ طمثها إذا افتضها (sihah;mufradat)؛ الافتضاض وهو النكاح بالتدمية وأدميت بالافتضاض وعذارى غير مفترعات (tahdhib)
- **B003** kadının dönemsel kanaması, bu kan ve kanama gören kadın — dönemsel kanama gören kadın · dönemsel kanama gören kadın için kullanılan başka bir biçim · dönemsel kanama ve bu sırada çıkan kan · kadın dönemsel kanama gördü, özellikle ilk kez
  الطامث وهي الحائض (maqayis)؛ الطامت لغة في الحائض (ayn)؛ الطمث الحيض (jamhara)؛ طمثت المرأة حاضت فهي طامث (sihah;tahdhib)؛ الطمث دم الحيض والطامث الحائض (mufradat)؛ الطمث هو الدم (tahdhib)
- **B004** deveyi bağlama; olumsuz kuruluşta ona hiç ip değmemiş olma [kalıp] — deveyi bağladı ve hareketini kısıtladı · ona hiçbir zaman ip ya da bağ değmedi
  طمثت البعير طمثا إذا عقلته (maqayis;ayn;tahdhib)؛ بعير ما طمثه حبل قط أي ما مسه (jamhara)؛ ما طمث هذه الناقة حبل قط أي ما مسها عقال (sihah)

## ق ب ل (root_001198): 55:56 قَبْلَهُمْ, 55:74 قَبْلَهُمْ

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

## ج ز ي (root_000244): 55:60 جَزَآءُ

- **B001** iyiliğe ya da kötülüğe denk karşılık verme — birine yaptığını iyilikle ya da kötülükle karşılama · birine yaptığının karşılığını verme · yapılana verilen iyi ya da kötü karşılık · çok geçmeden öç alma karşılığı · iyi işlerin ve yerine getirilmesi gereken yükümlülüklerin karşılıkları
  جزى يجزي جزاء أي كافأ بالإحسان وبالإساءة (ayn)؛ جزيته بما صنع جزاء وجازيته (sihah)؛ الجزاء يكون ثوابا ويكون عقابا؛ جزيت فلانا بما صنع جزاء؛ جزاء العطاس؛ الجوازي معناها الجزاء (tahdhib)؛ الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر؛ جزيته بكذا وجازيته (mufradat)؛ مكافأته إياه؛ جزيت فلانا أجزيه جزاء وجازيته مجازاة (maqayis)
- **B002** yerini tutup yükümlülüğü karşılama — yeterlilik ve bir işi başkası adına yerine getirme · bu işi benim yerime görüp tamamlama · bir koyunun senin adına yükümlülüğü karşılaması · yeterli olan ve başkasının yerini tutan kimse · birinin alacağını ya da borcunu ödeme
  فلان ذو غناء وجزاء (ayn)؛ جزى عني هذا الأمر أي قضى؛ جزت عنك شاة؛ رجل جازيك أي حسبك (sihah)؛ الجزاء أيضا القضاء؛ لا تقضي فيه نفس عن نفس شيئا؛ جزيت فلانا حقه؛ جزيته قرضه؛ صدقتك جزت عنك؛ هذا رجل حسبك وناهيك وكافيك وجازيك (tahdhib)؛ الجزاء الغناء والكفاية؛ لا يجزي والد عن ولده؛ جازيك فلان أي كافيك (mufradat)؛ قيام الشيء مقام غيره؛ ينوب مناب كل أحد؛ جزى عني هذا الأمر يجزي كما تقول قضى يقضي (maqayis)
- **B003** alacağı talep etme — borcumu ondan isteme · alacağını isteyen veya borcun ödenmesini talep eden kimse
  تجازيت ديني تقاضيته (ayn)؛ تجازيت ديني على فلان إذا تقاضيته؛ المتجازي المتقاضي (sihah)؛ أمرت فلانا يتجازى ديني أي يتقاضاه؛ أهل المدينة يسمون المتقاضي المتجازي (tahdhib)؛ تجازيت ديني على فلان أي تقاضيته؛ أهل المدينة يسمون المتقاضي المتجازي (maqayis)
- **B004** koruma statüsüne bağlı tarihsel vergi — koruma statüsündeki topluluklardan alınan tarihsel vergi · koruma statüsüne bağlı tarihsel vergiler
  الجزية ما يؤخذ من أهل الذمة والجمع الجزى (sihah)؛ الجزية جزية الناس التي تؤخذ من أهل الذمة؛ الجزية الخراج المجعول على الذمي سميت جزية لأنها قضاء منه لما عليه (tahdhib)؛ الجزية ما يؤخذ من أهل الذمة وتسميتها بذلك للاجتزاء بها عن حقن دمهم (mufradat)
- **B005** karşılık vermede üstün gelme [kalıp] — karşılık verme yarışında ötekine üstün gelme
  جازيته فجزيته أي غلبته (sihah)

## ECHO ج ز ز (root_000242): for 55:60 جَزَآءُ: withheld observed target; not identity

- **B001** saç, yün veya bitkiyi kırkıp kesme — saçı, yünü veya bitkiyi kırkıp kesmek · kırkma aleti · yünü kırkılan koyunlar
  جززت الصوف جزا (maqayis); الجز جز الشعر والصوف وغيره (ayn); جززت البر والنخل والصوف أجزه جزا والمجز ما يجز به (sihah); الجز جز الشعر والصوف والحشيش ونحوه وقد جززت الكبش والنعجة (tahdhib)
- **B002** kesim ya da hasat vaktinin gelmesi — kırkım, hasat veya ürün toplama zamanı · ağaç ürününün, ekinin veya koyunun kesim ya da kırkım vaktinin gelmesi · topluluğun koyunlarını kırkma ya da ekinini biçme vaktinin gelmesi · ekinin biçilecek duruma gelmesi
  هذا زمن الجزاز والجزاز (maqayis); الجزاز كالحصاد يقع على الحين والأوان وأجز النخل مثل أحصد البر (ayn); هذا زمن الجزاز والجزاز أي زمن الحصاد وصرام النخل وأجز النخل والبر والغنم واستجز البر (sihah); الجزاز كالحصاد واقع على الحين والأوان وأجز النخل حان له أن يجز وأجز القوم إذا حان أن تجز غنمهم (tahdhib)
- **B003** yeni kırkılmış yün veya kesimden kalan parça — henüz kullanılmamış kırkılmış yün · bir koyundan bir yılda kırkılan yün · deri veya başka bir şey kesilince düşen ya da fazla kalan parça · bir tutam yün
  الجزيزة خصلة من صوف والجمع جزائز والجزازة ما سقط من الأديم (maqayis); الجزز الصوف الذي لم يستعمل بعد ما جز وصوف كل شاة جزة والجزاز ما فضل من الأديم (ayn); الجزة صوف شاة والجزازة ما سقط من الأديم والجزيزة خصلة من الصوف (sihah); الجزز الصوف الذي لم يستعمل بعدما جز وهذه جزة هذه الشاة والجزاز ما فضل من الأديم (tahdhib)
- **B004** asılan boyalı yün süsü veya süs boncuğu — deve üzerindeki yolcu bölmesine bağlanan veya asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesine asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesinden sarkan boyalı yün parçası · insanı süslemek için kullanılan bir boncuk türü
  الجزائر عهون تشد على الهوادج (ayn); الجزجزة وهي عهنة تعلق من الهودج (sihah); الجزاجز خصل العهن والصوف المصبوغة تعلق على هوادج الظعائن وهي الثكن والجزائز وقيل الجزيز ضرب من الخرز (tahdhib)
- **B005** hurmanın kuruması veya hurmadaki kuruluk — hurmanın kuruması · hurmanın kuruması · hurmadaki kuruluk veya kuruma durumu
  جز التمر يجز بالكسر جزوزا أي يبس وأجز مثله وتمر فيه جزوز (sihah); قد جز التمر إذا يبس يجز جزوزا وتمر فيه جزوز (tahdhib)
- **B006** rivayette bir çıkış yeri olarak anılan yer adı — rivayette bir çıkış yeri olarak anılan yer adı
  جزة اسم أرض يقال إن الدجال يخرج منها (ayn); جزة اسم أرض منها يخرج الدجال فيما روي (tahdhib)

## ح س ن (root_000323): 55:60 ٱلْإِحْسَٰنِ, 55:60 ٱلْإِحْسَٰنُ, 55:70 حِسَانٌ, 55:76 حِسَانٍ

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

## د و ن (root_000502): 55:62 دُونِهِمَا

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

## د ه م (root_000496): 55:64 مُدْهَآمَّتَانِ

- **B001** koyu siyahlık ve siyaha çalan doygun renk — gecenin karanlık bir bölümü · siyahlık; gece karanlığı · siyah ya da çok koyu postlu · saf kızıl koyun · kararmak · ekin bol sulanmaktan koyulaşmak · bol su nedeniyle siyaha çalan koyu yeşil iki bahçe
  الدهمة السواد (maqayis;sihah); الأدهم الأسود (ayn;tahdhib); ادهام الزرع إذا علاه السواد ريا (maqayis;ayn;tahdhib); مدهامتان أي سوداوان من شدة الخضرة والري (maqayis;sihah;tahdhib); الدهمة سواد الليل وقد يعبر بها عن الخضرة الكاملة اللون (mufradat); مر دهم من الليل أي طائفة (maqayis)
- **B002** kalabalık insan topluluğu — kalabalık; çok sayıda insan · kalabalık topluluklar · hep birlikte, bir kerede geldiler · insan topluluğu · halkın kalabalığı · kalabalık ordu
  الدهم العدد الكثير (maqayis;sihah); الدهم الجماعة الكثيرة ودهمونا أي جاؤونا بمرة جماعة (ayn;tahdhib); دهماء الناس جماعتهم (ayn;sihah;tahdhib); وأنتم الدهم أي العدد الكثير وجيش دهم أي كثير (tahdhib)
- **B003** kaplayarak üzerine gelmek — atlılar üzerlerine akın etti · olay onları yayılıp sardı · büyük bir felaketle
  دهمتهم الخيل إذا غشيتهم (maqayis;sihah;tahdhib); دهمهم أمر أي غشيهم فاشيا (ayn;tahdhib); دهمهم الأمر يدهمهم (sihah;tahdhib); من أراد أهل المدينة بدهم أي بغائلة وأمر عظيم (tahdhib)
- **B004** karanlık ve ağır felaket — karanlık ve ağır felaket · büyük felaket; kötülük simgesi · felaketin kalıplaşmış adı · kapkara olan; büyük felaket
  الدهيماء تصغير الدهماء وهي الداهية سميت لإظلامها (maqayis;sihah); الدهيم الداهية (ayn); الدهيم وأم الدهيم من أسماء الدواهي (sihah); الدهماء السوداء المظلمة ويقال أراد بذلك الداهية (tahdhib); ضربت العرب الدهيم مثلا في الشر والداهية (tahdhib)
- **B005** özel adlandırma kümesi — isle kararmış tencere · kişinin yüz görünümü · bir ot türü · tahta pranga · eski ya da yeni basılmış yer; aktarım çelişkili · yakın zamanda bir topluluğun konakladığı yer · hapsedilmiş ve kötülenmiş kişi
  الدهماء القدر (maqayis;ayn;sihah;tahdhib); الدهماء سحنة الرجل (ayn;sihah;tahdhib); الدهماء بقلة (ayn;tahdhib); يقال للقيد الأدهم (sihah;tahdhib); الوطأة الدهماء القديمة (sihah); الوطأة الدهماء الجديدة (tahdhib); ربع أدهم حديث العهد (tahdhib); المتدهم هو المحبوس (tahdhib)

## ن ض خ (root_001514): 55:66 نَضَّاخَتَانِ

- **B001** kalıcı bir leke veya iz bırakma — kalıcı leke veya bulaşık izi · giysisine güzel koku sürüp izini bırakmak · öldürülen kişinin kalmış kan lekesi
  النضخ كاللطخ من الشيء يبقى له أثر (maqayis)؛ النضخ كاللطخ مما يبقى له أثر (ayn;tahdhib)؛ نضخ ثوبه بالطيب (maqayis;tahdhib)؛ النضخ الأثر يبقى في الثوب وغيره (sihah)؛ ما كان من الدم والزعفران والطين وما أشبهه (tahdhib)
- **B002** suyun coşup fışkırması; bol yağmur veya bir sağanak — suyun kaynaktan coşup fışkırması · bol yağan yağmur · suyu bol ve fışkıran kaynak · bir sağanak veya yağış geçişi
  النضخ من فور الماء من العين والجيشان (ayn)؛ النضخ في فور الماء من العين والجيشان (tahdhib)؛ عين نضاخة كثيرة الماء (maqayis;sihah)؛ فوارتان (sihah;tahdhib)؛ غيث نضاخ غزير (maqayis;sihah)؛ النضخة المطرة (sihah)؛ وقعت نضخة بالأرض أي مطرة (tahdhib)
- **B003** küçük parçalar halinde serpme veya sıçratma — serpme veya sıçratma; miktarı kullanıma göre değişen eylem · idrar ya da toz serpintisine uğramak · serpmek veya sıçratmak · karşılıklı serpme veya atışma · suyun damlacıklar halinde sıçraması · onlara okları dağıtarak atmak
  والنضخ دون النضح (jamhara)؛ ينضخ بالبول والغبار (jamhara)؛ النضخ الرش مثل النضح وهما سواء (sihah)؛ النضاخ المناضخة (sihah)؛ انتضخ الماء ترشش (sihah)؛ نضخناهم بالنبل إذا فرقوها فيهم (sihah)

## ر م ن (root_000602): 55:68 وَرُمَّانٌ

- **B001** nar — nar · bir nar · narlık · küçük nar
  الرُّمّان (maqayis)؛ الرُّمّان معروف من الفواكه الواحدة رُمّانة (ayn)؛ الرُّمّان معروف، الواحدة رُمّانة (sihah)؛ الرُّمّان معروف من الفواكه (tahdhib)؛ يقال لمنبت الرُّمّان مَرْمَنة (tahdhib)؛ الرُّمّانة تصغر رُمَيْمِينة (tahdhib)
- **B002** coğrafi yer adı — bir topluluğun yurdundaki iki tepenin adı · bir dağın veya başka bir coğrafi yerin adı
  الرُّمّانتان هضبتان في بلاد عبس (maqayis)؛ ورَمّان بفتح الراء جبل لطيئ (sihah)؛ ورَمّان بفتح الراء موضع (tahdhib)

## خ ي ر (root_000452): 55:70 خَيْرَٰتٌ

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

## ح و ر (root_000369): 55:72 حُورٌ

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

## خ ي م (root_000455): 55:72 ٱلْخِيَامِ

- **B001** çadır ve bir yerde yerleşip kalma — çadır · çadır direkleri · çadırlar · bir yerde konaklayıp kalmak · çadır biçimine sokmak · bir yerde çadır kurmak
  أصل يدل على الإقامة والثبات؛ فالخيمة معروفة؛ والخيم عيدان تبنى عليها الخيمة؛ خيم بالمكان أقام به؛ الخيم جمع خيمة؛ خيام وخيم؛ الخيمة بيت تبنيه العرب من عيدان الشجر؛ خيمه أي جعله كالخيمة؛ تخيم بمكان ضرب خيمته به
- **B002** yerleşik huy ve yaratılış — huy, yaratılış ve doğal eğilim · iyi huylu adam
  الخِيم السجية بكسر الخاء؛ وخيم الرجل غريزته؛ رجل حسن الخيم؛ الخيم بالكسر السجية والطبيعة
- **B003** bir şeyden sapmak veya korkup geri durmak — korkaklığından kımıldamayan kimse · bir şeyden sapmak veya korkup geri durmak · sapma veya korkakça geri durma eylemi
  للجبان خائم لأنه من جبنه لا حراك به؛ خام يخيم؛ خام عن الشيء يخيم خيما إذا حاد عنه؛ خام عنه يخيم خيمومة أي جبن
- **B004** bacağını kaldırmak — bacağımı kaldırdım · bacağı kaldırmak
  أخيمها أراد رفعها فكأنه شبهها بالخيم وهي عيدان الخيمة؛ خمت رجلي خيما إذا رفعتها؛ رأوني أخيمها
- **B005** dağ ve yer adı — bilinen bir dağın adı · bir yerin adı
  خيم جبل معروف؛ وخيم أيضا جبل؛ وذو خيم موضع؛ خيم اسم جبل

## ر ف ر ف (root_000581): 55:76 رَفْرَفٍ

- **B001** kanat çırpma — kuşun havada kanat çırpması · kuşun konacağı yerin çevresinde kanat çırpması · kanat çırpışıyla anılan bir kuş; kimi kullanımlarda deve kuşu
  الرفرفة هي تحريك الطائر جناحيه (maqayis;tahdhib)؛ رفرف الطائر إذا حرك جناحيه حول الشيء يريد أن يقع عليه (sihah)؛ الرفراف الظليم يرفرف بجناحيه ثم يعدو (maqayis;tahdhib)؛ الرفراف طائر وخاطف ظله وربما سموا الظليم بذلك (sihah)
- **B002** çadırın kenar veya tavan parçası, zırhın sarkan eteği ya da yapıdaki çıkıntılı bölüm — çadırın sarkan alt kenarı veya eteği · zırhın yanlarından ya da alt ucundan sarkan etek · çadırın üst örtüsü veya tavanı
  الرفرف كسر الخباء ونحوه (maqayis;tahdhib)؛ كسر الخباء وجوانب الدرع وما تدلى منها (sihah)؛ خرقة تخاط في أسفل الفسطاط وطرف الفسطاط (tahdhib)؛ طرف الفسطاط والخباء الواقع على الأرض دون الأطناب والأوتاد (mufradat)؛ رفرف الدرع ما فضل من ذيلها والرفرف الروشن ورفيف الفسطاط سقفه (tahdhib)
- **B003** yeşil bahçeler ya da yeşil yaygı ve dinlenme döşemeleri — kutsal metindeki kullanımda yeşil bahçeler, yaygılar, kumaşlar, oturma yerleri ya da yastıklar · yeşil bahçeler ya da serilmiş yeşil yaygılar · yaygılar ve döşemeler
  في الرفرف يقال هي الرياض ويقال هي البسط ويقال الرفرف ثياب خضر (maqayis)؛ الرفرف ثياب خضر تتخذ منها المحابس (sihah)؛ رفرف خضر: رياض الجنة والمجالس والفرش والبسط وفضول الفرش والوسائد (tahdhib)؛ الرفرف ضرب من الثياب مشبه بالرياض وذكر أنها المخاد (mufradat)
- **B004** yayılan veya sarkan dallar ya da tazelikle titreşip parlayan yeşillik — ağacın taze veya nemli görünüşü ya da dallarının yayılıp titreşmesi · taze, yeşil ve hafifçe titreşen ağaç · koruluğun aşağı sarkan dalları · yayılmış yapraklar veya gevşekçe uzanan dallı ağaç
  الرفيف رفيف الشجرة إذا تندت (maqayis)؛ شجر رفيف إذا تندت (sihah)؛ النبات الذي يهتز خضرة وتلألؤا وشجر يرف ورفرف الأيكة ما تهدل من غصونها وشجر مسترسل (tahdhib)؛ رفيف الشجر انتشار أغصانه والرفرف المنتشر من الأوراق (mufradat)

## خ ض ر (root_000418): 55:76 خُضْرٍ

- **B001** yeşil ve karaya çalan koyu yeşil renk — yeşil renk · yeşermek · siyah, karanlık ya da çok koyu renkli · rengi veya enginliği bakımından gökyüzü · demir karaltısının örttüğü askerî birlik · bozluğa koyu renk karışmış at · kara ya da esmer tenli; bağlama göre soyu arı veya bolluk içinde
  الخضرة من الألوان معروفة (maqayis;jamhara;sihah); الخضرة أحد الألوان بين البياض والسواد وهو إلى السواد أقرب (mufradat); العرب تسمّي الأسود أخضر والخضرة عند العرب سواد (maqayis;jamhara;sihah;tahdhib;mufradat); اخضرار مصدر من قولك اخضر واخضر الشيء اخضرارا (ayn;sihah); الخضرة في ألوان الإبل والخيل غبرة تخالطها دهمة (jamhara;sihah;tahdhib)
- **B002** yeşil ve taze bitki örtüsü — yeşil ekin veya her türlü yeşil bitki · ilk çıkan taze ot · sebzelik otlar ve yeşil bitkiler · kesilmiş taze ve körpe ağaç parçası · bitkiyle yeşermiş toprak
  النبات الناعم الريان يرى لشدة خضرته أسود والخضار البقل الأول (maqayis); الخضر في القرآن الزرع الأخضر وفي الكلام كل نبات من الخضر والخضر والمخضور للرخص من الشجر (ayn); الخضار نبت وواد خضار كثير الشجر (jamhara); الخضار البقل الأول وللزرع الخضاري (sihah); الخضر الزرع الأخضر وضرب من الجنبة والبقول يقال لها الخضارة والخضراء والخضر والمخضور للرخص من الشجر (tahdhib); الأرض مخضرة وثيابا خضرا (mufradat)
- **B003** taze, rahat ve bolluk içindeki yaşayış — rahat, yumuşak ve bolluk içindeki yaşayış · çekici, canlı ve hoş dünya yaşayışı · taze, güzel ve gönül rahatlığıyla alınabilir · bir işte işleri verimli biçimde yolunda gitmek · bollukları, çoğunlukları veya dünya varlıkları yok olsun
  خذ الشيء خضرا مضرا أي غضا حسنا (ayn); عيش خضر إذا كان غضا رافها والدنيا حلوة خضرة مضرة (jamhara); الدنيا حلوة خضرة وأباد الله خضراءهم أي سوادهم ومعظمهم أو غضراءهم خيرهم وغضارتهم (sihah); عيش خضر ناعم والخضيرة النعمة ومن خضر له في شيء فليلزمه وخضرا مضرا أي هنيئا مريئا ويأكل خضرتها يعني غضها وناعمها وهنيئها وأباد الله خضراءهم أي نعيمهم وخصبهم (tahdhib)
- **B004** tamamına ermeden kesmek, tüketmek veya sona ermek — genç yaşta ölmek · otu büyümesi tamamlanmadan biçmek · meyveyi olgunlaşmadan yemek · bir kız çocuğuyla ergenlikten önce cinsel ilişkiye girmek · hurmanın yeşil dalını kancayla kesmek
  اختضر فلان إذا مات شابا وتختضرون أي تموتون شبابا (ayn); اختضرت الكلأ إذا جززته وهو أخضر ومنه قيل للرجل إذا مات شابا غضا قد اختضر (sihah); اختضر فلان إذا مات شابا والنبات الغض يرعى ويختضر ويجز قبل تناهي طوله واختضرت الفاكهة إذا أكلتها قبل إناء إدراكها وخضر الرجل خضر النخل بمخلبه واختضره إذا قطعه واختضر الجارية إذا اقترعها قبل بلوغها (tahdhib)
- **B005** olgunlaşmadan önce ürün satışı — meyve veya yeşil ürünü olgunlaşmadan önce satma
  المخاضرة بيع الثمار قبل بدو صلاحها (maqayis); المخاضرة بيع الثمار قبل بدو صلاحها وهي خضر بعد (ayn); المخاضرة بيع الثمار قبل أن يبدو صلاحها وهي خضر ويدخل فيه بيع الرطاب والبقول (sihah); بيع المخاضرة المنهي عنه بيع الثمار وهي خضر لم يبد صلاحها (tahdhib); المخاضرة المبايعة على الخضر والثمار قبل بلوغها (mufradat)
- **B006** güzel görünüş, kötü yetişme çevresi — kötü çevrede yetişmiş güzel kadın
  خضراء الدمن المرأة الحسناء في منبت سوء كأنها شجرة ناضرة في دمنة بعر (maqayis); المرأة الحسناء في منبت السوء يشبهها بالشجرة الناضرة في دمنة البعر (ayn); خضراء الدمن المرأة الحسناء في منبت السوء (sihah;mufradat); جعلها خضراء الدمن تشبيها بالبقلة الناضرة تنبت في دمنة البعر فمنظرها حسن ومنبتها فاسد (tahdhib)
- **B007** öldürülmenin karşılıksız kalması — kanı yerde kalmak, ölümü karşılıksız bırakılmak
  ذهب دمه خضرا إذا طل وذهب دمه طريا كالنبات الأخضر وبطل وذبل (maqayis); ذهب دمه خضرا مضرا إذا ذهب هدرا باطلا ولم يطلب (ayn); ذهب دمه خضرا أي هدرا (sihah); ذهب دمه خضرا مضرا وذهب بطرا إذا ذهب هدرا باطلا (tahdhib)
- **B008** çok su katılmış süt — çok su katılıp yeşilimsi veya boz olmuş süt
  الخضار اللبن الذي أكثر ماؤه (maqayis); الخضار اللبن الذي قد أكثر ماؤه نحو السجاج والسمار (jamhara); الخضار بالفتح اللبن الذي أكثر ماؤه (sihah); الخضار من اللبن الذي مذق بماء كثير حتى اخضر وصار أورق (tahdhib)
- **B009** kişi ve topluluk özel adları — bir peygamberin yol arkadaşı sayılan anlatı kişisi · koyu tenle ilişkilendirilen bir topluluk veya kabile · insanlara verilen iki kişi adı
  الخضر قوم سموا بذلك لسواد ألوانهم (maqayis); الخضر نبي معمر وهو صاحب موسى (ayn); الخضر اسم نبي معروف والخضر قبيلة من العرب وقد سمت العرب أخضر وخضيرا (jamhara); خضر صاحب موسى (sihah); الخضر نبي من بني إسرائيل وصاحب موسى والخضر قبيلة والخضر عبد صالح وقيل سمي الخضر لحسنه وإشراق وجهه (tahdhib)
- **B010** yeşilimsi kuş ve evcil güvercin adları — damağında kızıllık bulunan yeşilimsi bir kuş · baskın boz-yeşil tonlarıyla adlandırılan evcil güvercinler
  الخضاري طائر يسمى الأخيل وهو أخضر في حنكه حمرة (ayn;tahdhib); الخضار طائر معروف وتسمى الحمام الدواجن في البيوت الخضر وإن اختلفت ألوانها لأن أكثر ألوانها الخضرة والورقة (jamhara); الخضاري طائر يسمى الأخيل (sihah); الحمام الدواجن الخضر وإن اختلفت ألوانها لغلبة الورقة عليها (tahdhib)
- **B011** yeşil meyve ve dallarıyla tanımlanan hurma adları — ham meyvesi yeşilken dökülen hurma ağacı · yeşil meyvesi iyi olan hurma ağacı · hurmanın yeşil yaprak ve dalları
  الخضيرة النخلة التي ينتثر بسرها وهو أخضر (sihah;mufradat); الخضرية نخلة طيبة التمر خضراؤه والخضيرة النخلة التي ينتثر بسرها وهو أخضر ولسعف النخل وجريده الأخضر الخضر (tahdhib)
- **B012** sudan ve eskilikten yeşermiş kap [kalıp] — eskilikten, içinde kalan su yüzünden yeşermiş su tulumları; bir yoruma göre mideler · uzun süre su çekmekten yeşermiş kova
  خضر المزاد التي بقيت فيها بقايا ماء فاخضرت من القدم ويقال بل خضر المزاد الكروش (maqayis); الدلو التي استقي بها حتى اخضرت خضراء (tahdhib)

## ع ب ق ر (root_000976): 55:76 وَعَبْقَرِىٍّ

- **B001** doğaüstü varlıklarla ilişkilendirilen ve olağanüstülüğün kaynağı sayılan efsanevi çöl yeri — doğaüstü varlıkların yaşadığı varsayılan efsanevi çöl yeri · o efsanevi yere ait sayılan doğaüstü varlıklar
  عبقر موضع بالبادية كثير الجن (ayn;tahdhib); موضع تزعم العرب أنه من أرض الجن (sihah); موضع للجن ينسب إليه كل نادر (mufradat)
- **B002** renkli desenli değerli dokuma yaygı — desenli ve değerli dokuma yaygı türü · tek bir desenli değerli yaygı veya bu nitelikteki dokumayı belirten biçim
  العبقري ضرب من البسط (ayn); هذه البسط التي فيها الأصباغ والنقوش (sihah); الطنافس الثخان والديباج والزرابي وعتاق الزرابي (tahdhib); العبقري البساط المنقش (tahdhib); ضرب من الفرش (mufradat)
- **B003** enderliği, ustalığı, yapım niteliği veya gücüyle olağanüstü üstün — enderliği, ustalığı, yapım niteliği veya gücüyle olağanüstü üstün · topluluğunun önderi, büyüğü ve en güçlü kişisi
  كل شئ تعجبوا من حذقه أو جودة صنعته وقوته فقالوا عبقري (sihah); هذا عبقري قوم سيد قوم وكبيرهم وشديدهم وقويهم (tahdhib); السيد من الرجال وهو الفاخر من الحيوان والجوهر (tahdhib); كل نادر من إنسان وحيوان وثوب (mufradat)
- **B004** biçime bağlı adlandırmalar — dolgun ve güzel kadın · kadın kişiadı olarak kullanım
  العبقرة المرأة التارة الجميلة (ayn;tahdhib); عبقر اسم من أسماء النساء (tahdhib)
- **B005** uzakta su gibi görünen hava görüntüsünün titreşerek parıldaması — uzakta su gibi görünen hava görüntüsünün titreşen parıltısı · uzakta su gibi görünen hava görüntüsü titreşerek parladı
  العبقرة تلألؤ السراب (ayn); عبقر السراب تلالا (sihah)
- **B006** aşırı soğukluk bildiren kalıplaşmış karşılaştırma — buz gibi, son derece soğuk; aşırı soğukluk bildiren kalıplaşmış karşılaştırma · bu kalıplaşmış söz çevresinde soğukluk
  أبرد من عبقر (sihah;tahdhib); العبقر والحبقر والعضرس البرد (tahdhib); والعبقر البرد (tahdhib); أبرد من عب قر والعب اسم للبرد (sihah;tahdhib)
- **B007** içinde hiçbir doğruluk bulunmayan katışıksız yalan [kalıp] — içine hiçbir doğruluk karışmamış düpedüz yalan
  العبقري الكذب البحت; كذب عبقري وسماق خالص لا يشوبه صدق

## ب ر ك (root_000109): 55:78 تَبَٰرَكَ

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



===== _commentary/v16/work/s055/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s055/reader_a_pilot.md)

# s055 Semantic Channel Discovery

## Parent Channels

### 1. P1 Calibrated Disclosure
- Semantic invariant: Knowledge becomes communicable and actionable by being gathered, marked, counted, and held to a just measure.
- Surface relation: direct; 55:1-9 moves from mercy, teaching, recitation, and expression to celestial reckoning and the command to maintain the balance.
- Surprising reach: The lexical field treats language, celestial motion, creation, and fair exchange as different instruments of calibration: each makes an otherwise hidden order legible.

#### Subchannel A. Teaching, Gathering, and Disclosure
- Reading type: mixed
- Scene or process: A merciful source imparts knowledge; recitation gathers speech, expression discloses meaning, and sensory recognition receives it.
- Active motifs: merciful care `quranic:root_000552:B001/m01`; imparted knowledge `quranic:root_001040:B001/m01`; reading and recitation `quranic:root_001210:B002/m01`; gathered utterance and study `quranic:root_001211:B001/m01`; appearing and becoming clear `quranic:root_000170:B004/m01`; disclosure by speech or sign `quranic:root_000170:B005/m01`; perception by sight, hearing, or sensation `quranic:root_000059:B002/m01`.
- Ayah anchors: 55:1 `رَّحْمَٰنُ` (ر ح م); 55:2 `عَلَّمَ` (ع ل م), `قُرْءَانَ` (ق ر ء); 55:3 `إِنسَٰنَ` (ء ن س); 55:4 `عَلَّمَ` (ع ل م), `بَيَانَ` (ب ي ن).
- Synthesis: Instruction is not only the transfer of propositions. Recitation first gathers articulated material; teaching makes it known; and *bayān* opens the gathered material into an evident meaning that can be seen, heard, or inwardly detected. Mercy supplies the social and affective frame for this movement from held knowledge to intelligible expression.

#### Subchannel B. Celestial Signs and Reckoning
- Reading type: mixed
- Scene or process: Luminous bodies rise and appear as marks whose ordered motions can be counted.
- Active motifs: sun and daylight `quranic:root_000818:B001/m01`; moon and moonlight `quranic:root_001255:B001/m01`; counting and computation `quranic:root_000318:B001/m01`; rising star `quranic:root_001475:B001/m01`; emergence into visibility `quranic:root_001475:B002/m01`; prominent guiding mark `quranic:root_001475:B006/m01`; distinguishing sign `quranic:root_001040:B002/m01`.
- Ayah anchors: 55:2, 55:4 `عَلَّمَ` (ع ل م); 55:5 `شَّمْسُ` (ش م س), `قَمَرُ` (ق م ر), `حُسْبَانٍ` (ح س ب); 55:6 `نَّجْمُ` (ن ج م).
- Synthesis: The sun and moon are not merely bright objects but readable motions, while the star is simultaneously a rising body and a conspicuous marker. Reckoning converts their appearance into an ordered schedule, extending the teaching-and-disclosure scene from utterance into the visible sky.

#### Subchannel C. Just Measure and Non-Diminution
- Reading type: mixed
- Scene or process: A scale is raised and established; parties compare quantities, allot shares, and prevent commercial diminution.
- Active motifs: physical weighing and estimation `quranic:root_001645:B001/m01`; scale of justice `quranic:root_001645:B002/m01`; comparison and equivalence `quranic:root_001645:B003/m01`; proportioned creation `quranic:root_001645:B008/m01`; justice and giving the due `quranic:root_001224:B001/m01`; allotted share `quranic:root_001224:B003/m01`; straight balance `quranic:root_001224:B004/m01`; measured quantity `quranic:root_001224:B007/m01`; short measure `quranic:root_000409:B003/m01`; commercial loss `quranic:root_000409:B002/m01`; straightness and rectitude `quranic:root_001273:B008/m01`; sustaining framework `quranic:root_001273:B009/m01`; equal weight `quranic:root_001273:B015/m01`; prior measuring and shaping `quranic:root_000434:B001/m01`.
- Ayah anchors: 55:3 `خَلَقَ` (خ ل ق); 55:7 `مِيزَانَ` (و ز ن); 55:8 `مِيزَانِ` (و ز ن); 55:9 `أَقِيمُ` (ق و م), `وَزْنَ` and `مِيزَانَ` (و ز ن), `قِسْطِ` (ق س ط), `تُخْسِرُ` (خ س ر).
- Synthesis: The balance assembles a complete transactional mechanism: an upright instrument, commensurable quantities, allotted rights, and the prohibited outcome of diminution. The creation sense of prior measuring presses the legal scene outward: just exchange imitates a world whose forms have already been proportioned.

### 2. P1 Vertical Ordering and Responsive Bodies
- Semantic invariant: Raised, placed, upright, and bowed forms disclose an ordered vertical relation rather than inert spatial arrangement.
- Surface relation: direct; 55:6-10 places prostrating vegetation beneath a raised sky and a laid-out earth.
- Surprising reach: The stemless plant and the trunked tree become contrasting body-types that perform the same submission, while uprightness can signify both physical stance and moral rectitude.

#### Subchannel A. Raised Canopy and Placed Ground
- Reading type: mixed
- Scene or process: An overhead canopy is elevated while the lower ground is set down as a stable field of habitation.
- Active motifs: elevation `quranic:root_000745:B001/m01`; sheltering sky or roof `quranic:root_000745:B004/m01`; physical raising `quranic:root_000582:B001/m01`; elevation in rank `quranic:root_000582:B002/m01`; placing in a lower or assigned position `quranic:root_001657:B001/m01`; lowering in rank `quranic:root_001657:B005/m01`; ground opposite the sky `quranic:root_000025:B001/m01`.
- Ayah anchors: 55:7 `سَّمَآءَ` (س م و), `رَفَعَ` (ر ف ع), `وَضَعَ` (و ض ع); 55:10 `أَرْضَ` (ء ر ض), `وَضَعَ` (و ض ع).
- Synthesis: Raising and placing establish opposed but coordinated surfaces: a sheltering upper expanse and a habitable lower field. Their lexical extensions into rank make the construction simultaneously architectural and hierarchical.

#### Subchannel B. Upright Growth Bending in Submission
- Reading type: mixed
- Scene or process: Different vegetal bodies rise from the ground yet bend or lower themselves under a common order.
- Active motifs: stemless plant `quranic:root_001475:B003/m01`; rising or protruding form `quranic:root_001475:B002/m01`; trunked tree `quranic:root_000777:B001/m01`; prostration and submission `quranic:root_000675:B001/m01`; bending the head or body `quranic:root_000675:B004/m01`; upright bodily stance `quranic:root_001273:B002/m01`; straightness and rectitude `quranic:root_001273:B008/m01`.
- Ayah anchors: 55:6 `نَّجْمُ` (ن ج م), `شَّجَرُ` (ش ج ر), `يَسْجُدَ` (س ج د); 55:9 `أَقِيمُ` (ق و م).
- Synthesis: The low, stemless plant and the visibly upright tree differ in structure but converge in a single action of lowering. The scene reframes prostration as the responsive motion of growth itself: elevation is completed, not contradicted, by submission.

### 3. P1 Contained Generation
- Semantic invariant: Living yield develops inside a holding form and becomes available through maturation, opening, or release.
- Surface relation: indirect; 55:10-15 presents fertile ground, enclosed palm fruit, grain with husk, human creation, and the creation of the hidden being.
- Surprising reach: Plant envelopes, wombs, and gathered embryonic matter form parallel containers; threshing and wind expose the productive release that follows enclosure.

#### Subchannel A. Fertile Ground and Edible Yield
- Reading type: mixed
- Scene or process: Productive ground supports trees, fruit, grain, and aromatic vegetation for the earth's inhabitants.
- Active motifs: fertile, well-grown earth `quranic:root_000025:B002/m01`; creatures dwelling on earth `quranic:root_000061:B001/m01`; fruit `quranic:root_001174:B002/m01`; palm tree `quranic:root_001483:B001/m01`; seed and cereal grain `quranic:root_000286:B001/m01`; aromatic or leafy plant `quranic:root_000609:B012/m01`; trunked tree `quranic:root_000777:B001/m01`; dense and lengthening vegetation `quranic:root_000266:B011/m01`.
- Ayah anchors: 55:6 `شَّجَرُ` (ش ج ر); 55:10 `أَرْضَ` (ء ر ض), `أَنَامِ` (ء ن م); 55:11 `فَٰكِهَةٌ` (ف ك ه), `نَّخْلُ` (ن خ ل); 55:12 `حَبُّ` (ح ب ب), `رَّيْحَانُ` (ر و ح); 55:15 `جَآنَّ` (ج ن ن).
- Synthesis: The earth is characterized by its capacity to establish and multiply growth. Tree, fruit, grain, and fragrant leaf occupy distinct roles in one food ecology, while the lexical density of vegetation makes the garden-like world a covering habitat rather than a bare inventory of produce.

#### Subchannel B. Husk, Envelope, and Productive Release
- Reading type: latent/lexical
- Scene or process: Plant yield is enclosed, protected, sifted, fragmented, and dispersed before becoming usable.
- Active motifs: fruit envelope and bud sheath `quranic:root_001319:B002/m01`; covering, sealing, and suppression `quranic:root_001319:B004/m01`; sieving and purification `quranic:root_001483:B002/m01`; selecting the best `quranic:root_001483:B003/m01`; grain husk and dry leaf `quranic:root_001020:B001/m01`; wind that scatters and breaks material `quranic:root_001020:B002/m01`; moving air `quranic:root_000609:B003/m01`; released scent `quranic:root_000609:B004/m01`; renewed leafing and elongation `quranic:root_000609:B017/m01`.
- Ayah anchors: 55:11 `نَّخْلُ` (ن خ ل), `أَكْمَامِ` (ك م م); 55:12 `عَصْفِ` (ع ص ف), `رَّيْحَانُ` (ر و ح).
- Synthesis: The palm sheath protects developing fruit, while grain reaches use through the opposite operations of breaking, winnowing, and selection. Wind is both the dispersing tool and the carrier by which the plant's scent becomes perceptible, so enclosure culminates in controlled release rather than mere concealment.

#### Subchannel C. Womb, Gathered Embryo, and Birth
- Reading type: latent/lexical
- Scene or process: A protected interior gathers generative matter, carries a hidden being, and releases a formed creature.
- Active motifs: female womb `quranic:root_000552:B003/m01`; womb gathering blood or fetus `quranic:root_001210:B004/m01`; gathered embryonic matter `quranic:root_001211:B003/m01`; fetus hidden in the belly `quranic:root_000266:B007/m01`; laying down a burden in birth `quranic:root_001657:B002/m01`; prior measuring `quranic:root_000434:B001/m01`; bringing a creature into being `quranic:root_000434:B002/m01`; completed bodily form `quranic:root_000434:B003/m01`; manifest human kind `quranic:root_000059:B001/m01`.
- Ayah anchors: 55:1 `رَّحْمَٰنُ` (ر ح م); 55:2 `قُرْءَانَ` (ق ر ء); 55:3 and 55:14 `إِنسَٰنَ` (ء ن س), `خَلَقَ` (خ ل ق); 55:7 and 55:10 `وَضَعَ` (و ض ع); 55:15 `خَلَقَ` (خ ل ق), `جَآنَّ` (ج ن ن).
- Synthesis: The lexical imagery supplies a full gestational mechanism: a womb as containing place, matter gathered within it, concealment during development, measured formation, and the laying down of the burden at birth. It materializes creation as staged care inside an enclosure.

### 4. P1 Elemental Formation
- Semantic invariant: Distinct created forms emerge through material transformation, with sound, heat, light, and motion revealing the process.
- Surface relation: direct; 55:14-15 juxtaposes human formation from resonant clay with the hidden being's formation from a moving flame.
- Surprising reach: The material pair is acoustically and kinetically differentiated: clay announces dryness by ringing, while flame is identified by restless, luminous motion.

#### Subchannel A. Resonant Clay Becoming Pottery
- Reading type: mixed
- Scene or process: Measured clay dries into a hard, sounding body and becomes a ceramic vessel or object.
- Active motifs: ringing of hard material `quranic:root_000878:B001/m01`; dry sounding clay `quranic:root_000878:B002/m01`; ceramic and earthenware `quranic:root_001135:B006/m01`; measuring before making `quranic:root_000434:B001/m01`; bringing form into being `quranic:root_000434:B002/m01`; smooth, even surface `quranic:root_000434:B008/m01`.
- Ayah anchors: 55:14 `خَلَقَ` (خ ل ق), `صَلْصَٰلٍ` (ص ل ص ل), `فَخَّارِ` (ف خ ر).
- Synthesis: Dryness is made sensible through resonance: the material rings because it has hardened. Measuring, smoothing, drying, and firing therefore form a compact craft process beneath the surface creation statement.

#### Subchannel B. Moving Flame Forming the Hidden Being
- Reading type: mixed
- Scene or process: A bright, mixed, restless flame supplies the material of an otherwise hidden creature.
- Active motifs: rising smokeless flame `quranic:root_001411:B003/m01`; mixing and restless disorder `quranic:root_001411:B004/m01`; fire in active motion `quranic:root_001564:B002/m01`; emitted light `quranic:root_001564:B001/m01`; hidden beings `quranic:root_000266:B005/m01`; bringing a creature into being `quranic:root_000434:B002/m01`.
- Ayah anchors: 55:15 `خَلَقَ` (خ ل ق), `جَآنَّ` (ج ن ن), `مَّارِجٍ` (م ر ج), `نَّارٍ` (ن و ر).
- Synthesis: The flame is not a static substance: it shines, rises, mixes, and refuses stable boundaries. That mobility gives a material analogue for the hidden creature formed from it, contrasting with the hardened and audible clay body.

### 5. P2 Paired Limits and Controlled Passage
- Semantic invariant: Paired fields meet or move within assigned limits, and productive passage occurs without dissolving those limits.
- Surface relation: direct; 55:17-25 moves from paired horizons to paired seas, a separating barrier, emergent pearls, and raised vessels underway.
- Surprising reach: The same geometry governs horizon, water interface, extraction, and navigation; a boundary can prevent destructive trespass while still permitting emergence and transit.

#### Subchannel A. Paired Horizons as Endpoints
- Reading type: mixed
- Scene or process: Light rises from one directional limit and withdraws at another, establishing opposed but coordinated horizons.
- Active motifs: sunrise and eastern direction `quranic:root_000790:B001/m01`; sunset and western direction `quranic:root_001077:B006/m01`; distance and removal from home `quranic:root_001077:B007/m01`; sheltering sky `quranic:root_000745:B004/m01`; ground opposite the sky `quranic:root_000025:B001/m01`; ownership and command `quranic:root_000532:B001/m01`; gradual ordering and care `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:17 `رَبُّ` (ر ب ب), `مَشْرِقَيْنِ` (ش ر ق), `مَغْرِبَيْنِ` (غ ر ب); 55:29 `سَّمَٰوَٰتِ` (س م و), `أَرْضِ` (ء ر ض).
- Synthesis: East and west are not isolated places but terminal relations within one managed field. Rising, setting, distance, and return make the horizon pair a temporal-spatial instrument whose limits remain under a single owner.

#### Subchannel B. Meeting Waters Held Apart
- Reading type: mixed
- Scene or process: Broad bodies of water are released toward encounter, meet at an interface, and remain restrained by a divider.
- Active motifs: broad abundant water `quranic:root_000086:B001/m01`; saline water `quranic:root_000086:B004/m01`; water-gathering depression `quranic:root_000086:B006/m01`; mixing and disturbance `quranic:root_001411:B004/m01`; instability within a place `quranic:root_001411:B005/m01`; interlaced or twisted branches `quranic:root_001411:B006/m01`; encounter of opposed participants `quranic:root_001372:B004/m01`; joining two ends `quranic:root_001372:B010/m01`; physical or conceptual divider `quranic:root_000106:B001/m01`; interval between endpoints `quranic:root_000106:B004/m01`; interspace between two things `quranic:root_000170:B002/m01`; wide separating distance `quranic:root_000170:B006/m01`; intermediate state `quranic:root_000170:B011/m01`; transgressive excess `quranic:root_000138:B003/m01`.
- Ayah anchors: 55:19 `مَرَجَ` (م ر ج), `بَحْرَيْنِ` (ب ح ر), `يَلْتَقِيَ` (ل ق ي); 55:20 `بَيْنَ` (ب ي ن), `يَبْغِيَ` (ب غ ي). No surface ayah anchor is available for `quranic:root_000106:B001` or `quranic:root_000106:B004`.
- Synthesis: Encounter does not entail fusion. The two waters approach and touch within an interspace whose function is to stop transgressive overflow. Lexical images of twisting, instability, and intermediate states sharpen the pressure on the divider: it maintains difference at the exact site of contact.

#### Subchannel C. Hidden Depth Yielding Brilliance
- Reading type: mixed
- Scene or process: A concealed object is brought out from depth and becomes visible through its own gleam.
- Active motifs: passage from an interior to the outside `quranic:root_000400:B001/m01`; extraction from concealment `quranic:root_000400:B002/m01`; pearl or worked gem `quranic:root_001337:B001/m01`; visible luster `quranic:root_001337:B002/m01`; flashing eye and hand display `quranic:root_001337:B004/m01`; deep red interior or depth `quranic:root_000086:B007/m01`.
- Ayah anchors: 55:19 `بَحْرَيْنِ` (ب ح ر); 55:22 `يَخْرُجُ` (خ ر ج), `لُّؤْلُؤُ` (ل ء ل ء).
- Synthesis: Extraction changes the epistemic state of the object: what was held in depth passes outward and announces itself by luster. The pearl therefore functions both as recovered material and as evidence made visible.

#### Subchannel D. Raised Vessels Underway
- Reading type: mixed
- Scene or process: Constructed vessels rise above broad water, follow a navigable course, and use prominent forms as orientation.
- Active motifs: running vessel or current `quranic:root_000240:B001/m02`; rising or raised structure `quranic:root_001502:B001/m01`; created construction `quranic:root_001502:B006/m01`; first structural member `quranic:root_001502:B007/m01`; approach and getting underway `quranic:root_001502:B008/m01`; broad sea `quranic:root_000086:B001/m01`; spacious course `quranic:root_000086:B002/m01`; seafaring `quranic:root_000086:B009/m01`; mountain or landmark `quranic:root_001040:B002/m02`; gathered deep water `quranic:root_001040:B005/m01`; chief navigator `quranic:root_000532:B017/m01`.
- Ayah anchors: 55:24 `جَوَارِ` (ج ر ي), `مُنشَـَٔاتُ` (ن ش ء), `بَحْرِ` (ب ح ر), `أَعْلَٰمِ` (ع ل م); 55:23 and 55:25 `رَبِّ` (ر ب ب).
- Synthesis: The maritime scene has craft, medium, motion, and orientation: a built body is raised, enters a broad course, and is read against mountain-like marks. The lexical chief of sailors adds a social role to the same governed passage.

### 6. P2 Enduring Authority and Continuous Provision
- Semantic invariant: Contingent beings pass and repeatedly need, while a distinguished authority remains and continually answers changing affairs.
- Surface relation: direct; 55:26-30 contrasts universal passing with the remaining face of majesty and honor, then depicts all in sky and earth as petitioners.
- Surprising reach: Remaining is not inert duration; lexical pardon, reserve, encompassing cover, and daily administration turn persistence into active preservation.

#### Subchannel A. Passing Totality and the Remaining Face
- Reading type: mixed
- Scene or process: An encompassing totality comes to an end while a visible, ranked, and honored presence remains.
- Active motifs: cessation after duration `quranic:root_001181:B001/m01`; open precinct around a house `quranic:root_001181:B002/m01`; heterogeneous people without fixed lineage `quranic:root_001181:B003/m01`; preservation by management `quranic:root_001181:B006/m01`; continued existence `quranic:root_000142:B001/m01`; surviving remainder `quranic:root_000142:B002/m01`; sparing and pardon `quranic:root_000142:B003/m01`; held reserve `quranic:root_000142:B004/m01`; totality embracing all parts `quranic:root_001315:B003/m01`; enclosing crown or cloud `quranic:root_001315:B005/m01`; visible face or front `quranic:root_001630:B001/m01`; rank and distinction `quranic:root_001630:B006/m01`; sound governance `quranic:root_001630:B008/m01`; majesty `quranic:root_000255:B001/m01`; encompassing cover `quranic:root_000255:B005/m01`; honor and generosity `quranic:root_001294:B001/m01`; the precious one `quranic:root_001294:B010/m01`.
- Ayah anchors: 55:26 `كُلُّ` (ك ل ل), `فَانٍ` (ف ن ي); 55:27 `يَبْقَىٰ` (ب ق ي), `وَجْهُ` (و ج ه), `رَبِّ` (ر ب ب), `جَلَٰلِ` (ج ل ل), `إِكْرَامِ` (ك ر م).
- Synthesis: The contrast is between exposed contingency and a presence that remains capable of sparing, reserving, covering, and governing. The face is both visible front and social rank; majesty and honor identify persistence as distinguished agency rather than bare survival.

#### Subchannel B. Petition and Daily Administration
- Reading type: mixed
- Scene or process: Dependents present needs to an owner who attends to, repairs, and carries out a changing succession of affairs.
- Active motifs: asking and requesting `quranic:root_000661:B001/m01`; desired need `quranic:root_000661:B002/m01`; satisfying a request `quranic:root_000661:B003/m01`; reciprocal questioning `quranic:root_000661:B004/m01`; affair or weighty circumstance `quranic:root_000773:B001/m01`; aim and sought object `quranic:root_000773:B002/m01`; competent execution `quranic:root_000773:B003/m01`; disruption of an affair `quranic:root_000773:B004/m01`; bounded day `quranic:root_001700:B001/m01`; duration `quranic:root_001700:B002/m01`; critical event `quranic:root_001700:B003/m01`; sovereign ownership `quranic:root_000532:B001/m01`; gradual repair and nurture `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:29 `يَسْـَٔلُ` (س ء ل), `سَّمَٰوَٰتِ` (س م و), `أَرْضِ` (ء ر ض), `كُلَّ` (ك ل ل), `يَوْمٍ` (ي و م), `شَأْنٍ` (ش ء ن); 55:27-30 `رَبِّ` (ر ب ب).
- Synthesis: Asking supplies participants and needs; *shaʾn* supplies the mutable work; and the day supplies recurring time. Lordship joins ownership to incremental repair, so the scene is one of continuous administration in which changing requests are met without exhausting the remaining source.

### 7. P3 The Closed Field of Escape
- Semantic invariant: Attention fixes on weighty communities whose attempted passage through the cosmic field is tested, blocked, and met by force.
- Surface relation: direct; 55:31-38 addresses the two weighty communities, challenges them to penetrate the regions of sky and earth, sends flame and smoke or copper against them, and ruptures the sky.
- Surprising reach: Emptying, pouring, penetration, missile motion, metallurgy, and splitting turn eschatological address into a tightly material enforcement mechanism.

#### Subchannel A. Deliberate Attention to Weighty Communities
- Reading type: mixed
- Scene or process: Competing activity is cleared away so focused action can turn toward two socially gathered, weight-bearing communities.
- Active motifs: clearing after occupation `quranic:root_001147:B001/m01`; pouring out a container `quranic:root_001147:B002/m01`; deliberate orientation toward a matter `quranic:root_001147:B006/m01`; physical or semantic weight `quranic:root_000202:B001/m01`; precious weight and rank `quranic:root_000202:B005/m01`; burden and slowness `quranic:root_000202:B006/m01`; impaired reception `quranic:root_000202:B009/m01`; community sharing one concern `quranic:root_001016:B013/m01`; manifest human community `quranic:root_000059:B001/m01`; hidden community `quranic:root_000266:B005/m01`.
- Ayah anchors: 55:31 `نَفْرُغُ` (ف ر غ), `ثَّقَلَانِ` (ث ق ل); 55:33 `مَعْشَرَ` (ع ش ر), `جِنِّ` (ج ن ن), `إِنسِ` (ء ن س).
- Synthesis: *Farāgh* supplies more than leisure: it is an emptied field and an act of concentrated intention. The addressees are "weighty" both as burdens and as precious entities of consequence, while *maʿshar* organizes them as communities rather than isolated individuals.

#### Subchannel B. Attempted Penetration and Required Warrant
- Reading type: mixed
- Scene or process: Communities test their ability to pierce a boundary and reach the far side, but passage requires a power or warrant they do not possess.
- Active motifs: practical capacity `quranic:root_000956:B003/m01`; effort to acquire capacity `quranic:root_000956:B004/m01`; piercing through to the other side `quranic:root_001531:B001/m01`; open passage `quranic:root_001531:B003/m01`; sight or movement traversing a whole group `quranic:root_001531:B004/m01`; sides and outer regions `quranic:root_001238:B001/m01`; being cast onto a side `quranic:root_001238:B002/m01`; going out across the land `quranic:root_001238:B008/m01`; sheltering upper expanse `quranic:root_000745:B004/m01`; lower ground `quranic:root_000025:B001/m01`; coercive power `quranic:root_000732:B001/m01`; compelling proof `quranic:root_000732:B002/m01`; delegated authority `quranic:root_000732:B003/m01`.
- Ayah anchors: 55:33 `ٱسْتَطَعْ` (ط و ع), `تَنفُذُ`/`ٱنفُذُ` (ن ف ذ), `أَقْطَارِ` (ق ط ر), `سَّمَٰوَٰتِ` (س م و), `أَرْضِ` (ء ر ض), `سُلْطَٰنٍ` (س ل ط).
- Synthesis: The verbs of penetration imagine a real traversable thickness: a point of entry, an open route, and a far side. Yet ability alone is insufficient. *Sulṭān* binds force to authorization and proof, making legitimate passage depend on a warrant that can overcome the boundary.

#### Subchannel C. Fiery Interception and Failed Aid
- Reading type: mixed
- Scene or process: A dispatched barrage of smokeless flame, heat, smoke, and copper intercepts movement while attempted self-defense fails.
- Active motifs: dispatch and release `quranic:root_000563:B001/m01`; successive groups sent out `quranic:root_000563:B005/m01`; smokeless flame `quranic:root_000828:B001/m01`; heat and smoke `quranic:root_000828:B002/m01`; active fire `quranic:root_001564:B002/m01`; red copper `quranic:root_001480:B004/m01`; smoke without flame `quranic:root_001480:B005/m01`; molten copper `quranic:root_001238:B006/m01`; aid against an enemy `quranic:root_001510:B001/m01`; self-defense and retaliation `quranic:root_001510:B002/m01`; rescue like rain `quranic:root_001510:B004/m01`; channels bringing water from afar `quranic:root_001510:B007/m01`.
- Ayah anchors: 55:35 `يُرْسَلُ` (ر س ل), `شُوَاظٌ` (ش و ظ), `نَّارٍ` (ن و ر), `نُحَاسٌ` (ن ح س), `تَنتَصِرَ` (ن ص ر); 55:33 `أَقْطَارِ` (ق ط ر).
- Synthesis: The attack is differentiated into luminous flame, bare heat, choking smoke, and molten metal. The aid-root adds a pointed reversal: its latent water and rescue channels are unavailable precisely when the barrage closes the route.

#### Subchannel D. The Boundary Itself Splits and Changes State
- Reading type: mixed
- Scene or process: The overhead boundary opens, reddens like a flower, and takes on the slick or coating quality of oil.
- Active motifs: splitting and opening `quranic:root_000807:B001/m01`; two opposed halves `quranic:root_000807:B002/m01`; communal schism `quranic:root_000807:B004/m01`; detached sheet or fragment `quranic:root_000807:B006/m01`; sky as overhead cover `quranic:root_000745:B004/m01`; rose and red color `quranic:root_001640:B005/m01`; oil or coating `quranic:root_000497:B001/m01`; oil-holding basin `quranic:root_000497:B005/m01`; smooth path `quranic:root_000497:B009/m01`; occurrence and changed state `quranic:root_001332:B001/m01`.
- Ayah anchors: 55:37 `ٱنشَقَّتِ` (ش ق ق), `سَّمَآءُ` (س م و), `كَانَتْ` (ك و ن), `وَرْدَةً` (و ر د), `دِّهَانِ` (د ه ن).
- Synthesis: The containing sky ceases to behave as a continuous roof. It separates into sides or sheets and changes visual and tactile state, becoming red, coated, and slick. The cosmic boundary is thus not merely crossed; it is materially reconstituted.

### 8. P3 Embodied Adjudication
- Semantic invariant: Hidden culpability becomes legible on bodies and is converted into seizure, restraint, and consequence.
- Surface relation: direct; 55:39-43 withholds questioning, identifies criminals by marks, seizes forelocks and feet, and names the denied destination.
- Surprising reach: Recognition by sign replaces testimony, while crime's lexical senses of cutting, harvesting, and earning portray guilt as material accumulated and then separated from its bearer.

#### Subchannel A. Guilt Recognized Without Interrogation
- Reading type: mixed
- Scene or process: Questions are suspended because guilt is already distinguishable through visible marks and embodied identity.
- Active motifs: interrogation and demand `quranic:root_000661:B001/m01`; offense and sin `quranic:root_000521:B001/m01`; recognition by distinguishing trace `quranic:root_001002:B003/m01`; confession and acknowledgment `quranic:root_001002:B009/m01`; visible facial or bodily feature `quranic:root_001002:B013/m01`; identifying mark `quranic:root_000764:B004/m01`; criminal offense `quranic:root_000239:B004/m01`; bodily mass `quranic:root_000239:B007/m01`; manifest humanity `quranic:root_000059:B001/m01`; hidden beings `quranic:root_000266:B005/m01`.
- Ayah anchors: 55:39 `يُسْـَٔلُ` (س ء ل), `ذَنۢبِ` (ذ ن ب), `إِنسٌ` (ء ن س), `جَآنٌّ` (ج ن ن); 55:41 `يُعْرَفُ` (ع ر ف), `مُجْرِمُونَ` (ج ر م), `سِيمَٰ` (س و م).
- Synthesis: The body functions as a complete evidentiary surface. A recognized sign links identity to offense so directly that verbal inquiry and confession become unnecessary; what was morally hidden is already externalized.

#### Subchannel B. Seizure by the Body's Leading and Supporting Parts
- Reading type: mixed
- Scene or process: Identified offenders are grasped at the forelock and feet, converting recognition into immobilizing custody.
- Active motifs: taking possession `quranic:root_000018:B001/m01`; accountability for an offense `quranic:root_000018:B002/m01`; capture and imprisonment `quranic:root_000018:B003/m01`; grappling hold `quranic:root_000018:B011/m01`; graspable handle `quranic:root_000018:B012/m01`; forelock and control by it `quranic:root_001512:B001/m01`; selected leaders or foremost group `quranic:root_001512:B003/m01`; foot that bears weight `quranic:root_001207:B001/m01`; advance to the front `quranic:root_001207:B004/m01`; front rank or leading edge `quranic:root_001207:B007/m01`; raised visible crest `quranic:root_001002:B002/m01`.
- Ayah anchors: 55:41 `يُؤْخَذُ` (ء خ ذ), `يُعْرَفُ` (ع ر ف), `نَّوَٰصِى` (ن ص ي), `أَقْدَامِ` (ق د م).
- Synthesis: The forelock is both an anatomical handle and a figure of command; the foot is both support and forward motion. Seizing both poles captures initiative and mobility at once, translating legal apprehension into a bodily mechanism.

#### Subchannel C. Crime as Cutting, Earning, and Allotted Residue
- Reading type: latent/lexical
- Scene or process: Wrongdoing is acquired, cut away like a harvest, leaves residue, and yields an assigned share of consequence.
- Active motifs: cutting and harvesting `quranic:root_000239:B001/m01`; fallen harvest residue `quranic:root_000239:B002/m01`; earning or causing an acquisition `quranic:root_000239:B003/m01`; criminal act `quranic:root_000239:B004/m01`; completed and elapsed term `quranic:root_000239:B006/m01`; offense with bad outcome `quranic:root_000521:B001/m01`; trailing end `quranic:root_000521:B002/m01`; ripening from the end `quranic:root_000521:B005/m01`; allotted share `quranic:root_000521:B006/m01`; full bucket `quranic:root_000521:B007/m01`; ladle or scoop `quranic:root_000521:B008/m01`; being held answerable `quranic:root_000018:B002/m01`.
- Ayah anchors: 55:39 `ذَنۢبِ` (ذ ن ب); 55:41 and 55:43 `مُجْرِمُونَ` (ج ر م); 55:41 `يُؤْخَذُ` (ء خ ذ).
- Synthesis: Crime is rendered as a productive but destructive process: an act is earned, reaches completion, is cut off, and leaves a gatherable remainder. The bucket, share, and scoop imagery gives consequence a measured materiality, as though the offender receives the yield of what was accumulated.

### 9. P3 The Thermal Circuit
- Semantic invariant: Punishment is organized as repeated movement through an enclosure whose heat advances matter toward blackening, melting, and full readiness.
- Surface relation: direct; 55:44 depicts continual circling between the destination and fully heated water.
- Surprising reach: Bathhouse, heating vessel, due time, and melting fat turn the scene into an apparatus with containers, stages, and a repeated route.

#### Subchannel A. Enclosing Circulation
- Reading type: mixed
- Scene or process: Participants repeatedly move around and between bounded stations without reaching an exit.
- Active motifs: circling around a center `quranic:root_000957:B001/m01`; engulfing flood or event `quranic:root_000957:B002/m01`; night watch circling a protected place `quranic:root_000957:B005/m01`; lashed raft for crossing `quranic:root_000957:B006/m01`; fortified surrounding wall `quranic:root_000957:B010/m01`; interspace between stations `quranic:root_000170:B002/m01`; widening separation `quranic:root_000170:B006/m01`.
- Ayah anchors: 55:44 `يَطُوفُ` (ط و ف), `بَيْنَ`/`بَيْنَ` (ب ي ن).
- Synthesis: Circular movement promises transit but returns the mover to the enclosing field. Even the raft sense, normally a means of crossing, is absorbed into a route with no liberating far side.

#### Subchannel B. Heat, Blackening, and Full Readiness
- Reading type: mixed
- Scene or process: Water is heated to its terminal state while surrounding matter blackens, sweats, softens, and melts.
- Active motifs: soot, coal, and black smoke `quranic:root_000001:B001/m01`; hot water or thermal spring `quranic:root_000001:B002/m01`; melted fat `quranic:root_000001:B003/m01`; sweat under heat `quranic:root_000001:B004/m01`; fevered body or ground `quranic:root_000001:B005/m01`; arrival of the appointed matter `quranic:root_000001:B006/m01`; decreed death `quranic:root_000001:B010/m01`; bathhouse and heating vessel `quranic:root_000001:B013/m01`; delay and waiting `quranic:root_000063:B001/m01`; ripeness and terminal heating `quranic:root_000063:B003/m01`; containing vessel `quranic:root_000063:B004/m01`.
- Ayah anchors: 55:44 `حَمِيمٍ` (ح م م), `ءَانٍ` (ء ن ي).
- Synthesis: *Ḥamīm ān* is materially overdetermined as water whose heat has reached its due endpoint. The surrounding senses supply a heating vessel, a bath-like enclosure, sweat, black residue, melting matter, and decreed arrival, making the destination a completed thermal process.

### 10. P4 Garden Infrastructure and Ordered Abundance
- Semantic invariant: Reward is spatially prepared through a protected threshold, branching cover, flowing sources, and paired produce.
- Surface relation: direct; 55:46-53 introduces two gardens for one who fears the standing before the Lord, then supplies branches, running springs, and paired fruit.
- Surprising reach: Fear is not only emotion but visible contraction and loss; the garden answers it with an opposite architecture of secure station, branching extension, and repeatable flow.

#### Subchannel A. Fearful Standing and Sheltered Entry
- Reading type: mixed
- Scene or process: A person anticipates a charged standing, while the promised destination takes the form of a protected, planted enclosure.
- Active motifs: fearful anticipation `quranic:root_000447:B001/m01`; loss by gradual taking `quranic:root_000447:B004/m01`; fear becoming outwardly visible `quranic:root_000447:B005/m01`; station or place of standing `quranic:root_001273:B006/m01`; resurrection and standing for judgment `quranic:root_001273:B013/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and repair `quranic:root_000532:B002/m01`; tree-covered garden `quranic:root_000266:B003/m01`; protective shield `quranic:root_000266:B008/m01`; sheltered place `quranic:root_000266:B017/m01`; extended bough `quranic:root_001180:B003/m01`.
- Ayah anchors: 55:46 `خَافَ` (خ و ف), `مَقَامَ` (ق و م), `رَبِّ` (ر ب ب), `جَنَّتَانِ` (ج ن ن); 55:48 `أَفْنَانٍ` (ف ن ن).
- Synthesis: The feared *maqām* is a fixed point of accountability; the garden answers it with another kind of fixed place, one made safe by cover, enclosure, and living extension. The movement is from exposed anticipation to prepared shelter.

#### Subchannel B. Branching Canopy and Flowing Sources
- Reading type: mixed
- Scene or process: Dense vegetation spreads overhead while springs emerge and maintain continuous movement through the enclosure.
- Active motifs: covered orchard `quranic:root_000266:B003/m01`; thick and lengthening growth `quranic:root_000266:B011/m01`; branching bough `quranic:root_001180:B003/m01`; multiple kinds and paths `quranic:root_001180:B002/m01`; spring or visible source `quranic:root_001069:B006/m01`; flowing water `quranic:root_000240:B001/m01`.
- Ayah anchors: 55:46 `جَنَّتَانِ` (ج ن ن); 55:48 `أَفْنَانٍ` (ف ن ن); 55:50 `عَيْنَانِ` (ع ي ن), `تَجْرِيَ` (ج ر ي).
- Synthesis: Branching multiplies sheltered routes above, and water multiplies sustaining routes below. Together they form infrastructure rather than decoration: cover, source, and continuous distribution.

#### Subchannel C. Paired Produce and Encompassing Plenty
- Reading type: mixed
- Scene or process: Fruit is sorted into paired kinds within an abundance that includes every desired class.
- Active motifs: totality gathering all parts `quranic:root_001315:B003/m01`; encircling crown or flowering enclosure `quranic:root_001315:B005/m01`; pleasant enjoyment `quranic:root_001174:B001/m01`; edible fruit `quranic:root_001174:B002/m01`; one of a joined pair `quranic:root_000652:B001/m01`; class or variety `quranic:root_000652:B004/m01`; analogous companions `quranic:root_000652:B005/m01`.
- Ayah anchors: 55:52 `كُلِّ` (ك ل ل), `فَٰكِهَةٍ` (ف ك ه), `زَوْجَانِ` (ز و ج).
- Synthesis: Pairing is a classificatory operation as well as a numerical one: each fruit belongs to a kind and appears with its counterpart. The enclosing sense of *kull* turns this paired inventory into organized completeness.

### 11. P4 Layered Repose and Guarded Intimacy
- Semantic invariant: Comfort and intimacy are made possible by layered interiors, bodily support, controlled sight, and a maintained boundary against prior contact.
- Surface relation: direct; 55:54-59 places reclining figures on lined beds near fruit and describes restrained gaze and untouched companions.
- Surprising reach: Textile lining, confidants, shields, tied openings, and graspable boundaries make privacy a constructed mechanism rather than an abstract condition.

#### Subchannel A. Supported Body inside a Layered Interior
- Reading type: mixed
- Scene or process: A reclining body is supported by spread furnishings whose hidden lining creates an interior within the garden enclosure.
- Active motifs: reclining on a support `quranic:root_001678:B004/m01`; spreading and preparing a surface `quranic:root_001143:B001/m01`; bed and household furnishing `quranic:root_001143:B002/m01`; thin plates and layers `quranic:root_001143:B010/m01`; interior or underside `quranic:root_000128:B001/m01`; hidden interior `quranic:root_000128:B002/m01`; garment lining `quranic:root_000128:B003/m01`; intimate inner circle `quranic:root_000128:B004/m01`; concealment `quranic:root_000266:B001/m01`; protective cover `quranic:root_000266:B008/m01`; tying a vessel closed `quranic:root_001678:B001/m01`.
- Ayah anchors: 55:54 `مُتَّكِـِٔينَ` (و ك ء), `فُرُشٍۭ` (ف ر ش), `بَطَآئِنُ` (ب ط ن), `جَنَّتَيْنِ` (ج ن ن).
- Synthesis: The furnishing is a nested structure: spread surface, internal lining, and supported body. Lexical extensions from lining to confidant and from covering to shield make the physical interior simultaneously a social zone of protected nearness.

#### Subchannel B. Restrained Gaze and First Contact
- Reading type: mixed
- Scene or process: Sight is held within a limit and bodily contact is defined by the absence of any prior touch.
- Active motifs: confinement to one object `quranic:root_001231:B004/m01`; reaching a terminal limit `quranic:root_001231:B006/m01`; exclusive nearness `quranic:root_001231:B010/m01`; eye and gaze `quranic:root_000931:B002/m01`; turning the gaze away `quranic:root_000931:B009/m01`; first touch or its absence `quranic:root_000949:B001/m01`; sexual first contact `quranic:root_000949:B002/m01`; first menstrual blood `quranic:root_000949:B003/m01`; temporal precedence `quranic:root_001198:B002/m01`; kiss or mouth-contact `quranic:root_001198:B006/m01`; receiver at birth `quranic:root_001198:B007/m01`; human community `quranic:root_000059:B001/m01`; hidden beings `quranic:root_000266:B005/m01`; seeing eye `quranic:root_001069:B001/m01`; wide beautiful eye `quranic:root_001069:B016/m01`.
- Ayah anchors: 55:50 `عَيْنَانِ` (ع ي ن); 55:56 `قَٰصِرَٰتُ` (ق ص ر), `طَّرْفِ` (ط ر ف), `يَطْمِثْ` (ط م ث), `إِنسٌ` (ء ن س), `قَبْلَ` (ق ب ل), `جَآنٌّ` (ج ن ن).
- Synthesis: Restraint operates across sight, time, and touch. The gaze is not merely modest but spatially bounded; *before* establishes a closed temporal boundary; and the contact-root supplies sexual, menstrual, tethering, and birth-reception thresholds, concentrating the scene on guarded first access.

### 12. P4 Recompense as Return and Yield
- Semantic invariant: An action produces a corresponding return in the same way that a cultivated source yields fruit for gathering.
- Surface relation: direct; 55:54 brings harvest within reach and 55:60 asks whether excellence has any recompense but excellence.
- Surprising reach: Harvest vocabulary carries an embedded legal reversal: *jany* can name both gathering fruit and incurring an offense, so beneficial and harmful deeds each generate their own yield.

#### Subchannel A. Near Harvest and Acquired Yield
- Reading type: mixed
- Scene or process: Ripe produce remains close enough to be selected and gathered directly from its source.
- Active motifs: gathering produce from its source `quranic:root_000267:B001/m01`; incurring an offense `quranic:root_000267:B002/m01`; false accusation `quranic:root_000267:B003/m01`; giving a companion the best gathered portion `quranic:root_000267:B004/m01`; edible fruit `quranic:root_001174:B002/m01`; physical nearness `quranic:root_000493:B001/m01`.
- Ayah anchors: 55:52 `فَٰكِهَةٍ` (ف ك ه); 55:54 `جَنَى` (ج ن ي), `دَانٍ` (د ن و).
- Synthesis: Nearness removes the interval between source, choice, and possession. Yet the same gathering-root can describe drawing culpability onto oneself or another, making harvest a neutral mechanism whose moral quality depends on what action has been cultivated.

#### Subchannel B. Excellence Answered in Kind
- Reading type: mixed
- Scene or process: A good act returns as a matching good, functioning as payment, substitution, or completed counter-performance.
- Active motifs: recompense for an act `quranic:root_000244:B001/m01`; one thing standing in for another `quranic:root_000244:B002/m01`; collection and settlement of debt `quranic:root_000244:B003/m01`; prevailing in reciprocation `quranic:root_000244:B005/m01`; desirable goodness `quranic:root_000323:B001/m01`; beneficent and well-made action `quranic:root_000323:B002/m01`; utmost effort `quranic:root_000323:B005/m01`.
- Ayah anchors: 55:60 `جَزَآءُ` (ج ز ي), `إِحْسَٰنِ`/`إِحْسَٰنُ` (ح س ن).
- Synthesis: Recompense is exact enough to settle an obligation yet generous enough to exceed bare justice. The repeated *iḥsān* makes deed and return mirror one another, while the debt and substitution senses specify the mechanism by which one answers for the other.

### 13. P5 Saturated Lower Gardens
- Semantic invariant: A nearer or lower garden tier is intensified through dark vegetal density, forceful water, and diverse fruit.
- Surface relation: direct; 55:62-69 presents another pair of gardens, dark green from saturation, with gushing springs, fruit, palms, and pomegranates.
- Surprising reach: Darkness can mark danger or an overwhelming crowd, but here it is converted into the visual index of water-rich growth; retained pools and forceful spray explain how that density is sustained.

#### Subchannel A. Nearer Tier and Dark Vegetal Density
- Reading type: mixed
- Scene or process: A lower or nearer enclosure becomes so saturated with growth that its green reads as blackness.
- Active motifs: nearness below a farther limit `quranic:root_000502:B001/m01`; other or lower-ranked thing `quranic:root_000502:B003/m01`; covered garden `quranic:root_000266:B003/m01`; dense lengthening vegetation `quranic:root_000266:B011/m01`; blackness and black-green saturation `quranic:root_000496:B001/m01`; gathered multitude `quranic:root_000496:B002/m01`; overwhelming arrival `quranic:root_000496:B003/m01`; green tending toward dark `quranic:root_000418:B001/m01`; fresh green vegetation `quranic:root_000418:B002/m01`; lush ease and prosperity `quranic:root_000418:B003/m01`.
- Ayah anchors: 55:62 `دُونِ` (د و ن), `جَنَّتَانِ` (ج ن ن); 55:64 `مُدْهَآمَّتَانِ` (د ه م); 55:76 `خُضْرٍ` (خ ض ر).
- Synthesis: The tier is spatially "below" or nearer, but its vegetation is not diminished. Saturation compresses green into near-black, while crowd and overrunning senses make the density feel active, as if growth has occupied the whole enclosure.

#### Subchannel B. Gushing Sources and Retained Water
- Reading type: mixed
- Scene or process: Springs force water outward, scatter droplets, leave traces, and feed stable retaining basins.
- Active motifs: spring or visible source `quranic:root_001069:B006/m01`; opening in a waterskin `quranic:root_001069:B007/m01`; persistent stain or splash `quranic:root_001514:B001/m01`; abundant surging water `quranic:root_001514:B002/m01`; dispersed spray `quranic:root_001514:B003/m01`; water retained in a basin `quranic:root_000109:B003/m01`; fixed and increasing good `quranic:root_000109:B004/m01`.
- Ayah anchors: 55:66 `عَيْنَانِ` (ع ي ن), `نَضَّاخَتَانِ` (ن ض خ); 55:78 `تَبَٰرَكَ` (ب ر ك).
- Synthesis: The source is imagined as an opening under pressure: water surges, sprays, and marks what it touches. The stable basin and fixed blessing complete the mechanism by converting forceful emission into retained, renewable supply.

#### Subchannel C. Fruit, Palm, and Pomegranate
- Reading type: mixed
- Scene or process: A covered orchard offers pleasant produce, selected palm yield, and distinct pomegranate fruit.
- Active motifs: pleasant enjoyment `quranic:root_001174:B001/m01`; edible fruit `quranic:root_001174:B002/m01`; palm tree `quranic:root_001483:B001/m01`; choosing the best `quranic:root_001483:B003/m01`; pomegranate `quranic:root_000602:B001/m01`; green palm and frond `quranic:root_000418:B011/m01`; cutting produce before ripeness `quranic:root_000418:B004/m01`; covered orchard `quranic:root_000266:B003/m01`.
- Ayah anchors: 55:62 `جَنَّتَانِ` (ج ن ن); 55:68 `فَٰكِهَةٌ` (ف ك ه), `نَخْلٌ` (ن خ ل), `رُمَّانٌ` (ر م ن); 55:76 `خُضْرٍ` (خ ض ر).
- Synthesis: The list differentiates generic enjoyment, orchard fruit, the structured palm, and the singular pomegranate. Selection and ripeness senses keep the scene procedural: produce must mature and be chosen, not merely be present.

### 14. P5 Selected Companionship in Fixed Shelter
- Semantic invariant: Chosen goodness and visible beauty are protected by a stable enclosure and a maintained threshold against prior contact.
- Surface relation: direct; 55:70-75 places good and beautiful companions in tents and states that neither humans nor hidden beings touched them before.
- Surprising reach: Choice, character, eye-contrast, fixed habit, dialogue, confinement, and first-touch vocabulary make companionship both ethical and spatially guarded.

#### Subchannel A. Chosen Goodness and Visible Beauty
- Reading type: mixed
- Scene or process: Excellent companions are selected for beneficial character and made perceptible through beauty, especially the eye's contrast.
- Active motifs: beneficial good `quranic:root_000452:B001/m01`; excellence and selection `quranic:root_000452:B002/m01`; choosing and seeking the better `quranic:root_000452:B003/m01`; generosity and gift `quranic:root_000452:B005/m01`; desirable beauty `quranic:root_000323:B001/m01`; beneficent action `quranic:root_000323:B002/m01`; white-dark contrast of the eye `quranic:root_000369:B001/m01`; whitening and brightness `quranic:root_000369:B002/m01`; seeing eye `quranic:root_001069:B001/m01`; wide beautiful eye `quranic:root_001069:B016/m01`.
- Ayah anchors: 55:66 `عَيْنَانِ` (ع ي ن); 55:70 `خَيْرَٰتٌ` (خ ي ر), `حِسَانٌ` (ح س ن); 55:72 `حُورٌ` (ح و ر).
- Synthesis: Beauty is not detached appearance: *khayr* supplies benefit, choice, and generosity, while *ḥusn* joins desirability to beneficent action. The eye's intense white-dark contrast makes that selected excellence visibly legible.

#### Subchannel B. Tent, Confinement, and Untouched Threshold
- Reading type: mixed
- Scene or process: Companions remain in a fixed shelter whose spatial and temporal boundaries preserve first contact.
- Active motifs: confinement and restriction `quranic:root_001231:B004/m01`; enclosed building `quranic:root_001231:B005/m01`; exclusive nearness `quranic:root_001231:B010/m01`; tent and settled residence `quranic:root_000455:B001/m01`; stable disposition `quranic:root_000455:B002/m01`; first touch or its absence `quranic:root_000949:B001/m01`; sexual first contact `quranic:root_000949:B002/m01`; temporal precedence `quranic:root_001198:B002/m01`; acceptance with satisfaction `quranic:root_001198:B004/m01`; kiss or mouth-contact `quranic:root_001198:B006/m01`; receiver at birth `quranic:root_001198:B007/m01`; manifest human community `quranic:root_000059:B001/m01`; hidden beings `quranic:root_000266:B005/m01`.
- Ayah anchors: 55:72 `مَّقْصُورَٰتٌ` (ق ص ر), `خِيَامِ` (خ ي م); 55:74 `يَطْمِثْ` (ط م ث), `إِنسٌ` (ء ن س), `قَبْلَ` (ق ب ل), `جَآنٌّ` (ج ن ن).
- Synthesis: The tent is a residence and the confinement is purposeful, producing a bounded zone of exclusive nearness. The first-contact complex extends from touch and sexuality to acceptance and birth reception, concentrating several threshold events at the protected opening of the shelter.

### 15. P5 Living Textiles and Repose
- Semantic invariant: Furnishings imitate living cover through flutter, hanging edges, saturated green, pattern, and shimmer.
- Surface relation: direct; 55:76 depicts reclining on green *rafraf* and fine patterned *ʿabqarī*.
- Surprising reach: Textile surfaces become canopy, wing, leaf, and uncanny crafted landscape, so repose occurs on an artifact that remains visually in motion.

#### Subchannel A. Green Fluttering Canopy
- Reading type: mixed
- Scene or process: A reclining body rests on or beneath a green surface whose edges flutter like wings and whose folds resemble living foliage.
- Active motifs: reclining support `quranic:root_001678:B004/m01`; wing-beat around an object `quranic:root_000581:B001/m01`; hanging or sheltering edge `quranic:root_000581:B002/m01`; spreading shimmering greenery `quranic:root_000581:B004/m01`; dark saturated green `quranic:root_000418:B001/m01`; fresh vegetation `quranic:root_000418:B002/m01`; lush ease `quranic:root_000418:B003/m01`.
- Ayah anchors: 55:76 `مُتَّكِـِٔينَ` (و ك ء), `رَفْرَفٍ` (ر ف ر ف), `خُضْرٍ` (خ ض ر).
- Synthesis: The furnishing is simultaneously support and canopy. Wing motion, hanging tent-edge, and trembling foliage give its green surface a controlled animation that envelops the reclining body without destabilizing it.

#### Subchannel B. Patterned and Uncanny Craft
- Reading type: latent/lexical
- Scene or process: Fine carpets are dyed and patterned so skillfully that their surface evokes an extraordinary place and seems to shimmer.
- Active motifs: uncanny or wondrous place `quranic:root_000976:B001/m01`; patterned precious carpets `quranic:root_000976:B002/m01`; exceptional craft and rarity `quranic:root_000976:B003/m01`; shimmering mirage `quranic:root_000976:B005/m01`; desirable beauty `quranic:root_000323:B001/m01`; beneficent workmanship `quranic:root_000323:B002/m01`; sheltering textile edge `quranic:root_000581:B002/m01`.
- Ayah anchors: 55:76 `عَبْقَرِىٍّ` (ع ب ق ر), `حِسَانٍ` (ح س ن), `رَفْرَفٍ` (ر ف ر ف).
- Synthesis: The carpet's value lies in more than material fineness. Pattern and dye create an apparently inhabited surface whose shimmer evokes a distant extraordinary place; craftsmanship converts floor covering into a visual environment.

### 16. P5 Stable Blessing and the Exalted Name
- Semantic invariant: Beneficence is fixed, renewed, and publicly marked by the name of an exalted owner characterized by majesty and generosity.
- Surface relation: direct; 55:78 closes with the blessed name of the Lord of majesty and honor.
- Surprising reach: Blessing joins stability to growth, water retention, persistence in work, rain, and yield; the name operates as both identifying sign and circulating reputation.

#### Subchannel A. Fixed Good that Continues to Yield
- Reading type: latent/lexical
- Scene or process: Good settles into a place, persists through repeated work, retains resources, and continues to produce growth and provision.
- Active motifs: settling firmly in a place `quranic:root_000109:B001/m01`; retained basin water `quranic:root_000109:B003/m01`; fixed and increasing good `quranic:root_000109:B004/m01`; persistent effort `quranic:root_000109:B006/m01`; milk yielded while settled `quranic:root_000109:B007/m01`; nurture and completion `quranic:root_000532:B002/m01`; lasting residence `quranic:root_000532:B007/m01`; layered rain cloud `quranic:root_000532:B008/m01`; abundant water `quranic:root_000532:B013/m01`; fertile rain and soil `quranic:root_001294:B002/m01`; grapevine and fruit `quranic:root_001294:B004/m01`.
- Ayah anchors: 55:78 `تَبَٰرَكَ` (ب ر ك), `رَبِّ` (ر ب ب), `إِكْرَامِ` (ك ر م).
- Synthesis: Blessing is a state that stays and a process that keeps yielding. Stable residence, stored water, persistent labor, rain, milk, and fruit assemble a resource cycle in which constancy is proven by renewed provision.

#### Subchannel B. Name, Renown, Majesty, and Honor
- Reading type: mixed
- Scene or process: A name identifies and elevates its bearer, circulates as good renown, and gathers the social predicates of majesty, covering presence, honor, and preciousness.
- Active motifs: name and designation `quranic:root_000745:B005/m01`; elevated rank `quranic:root_000745:B001/m01`; circulating good renown `quranic:root_000745:B008/m01`; sovereign owner `quranic:root_000532:B001/m01`; majesty and greatness `quranic:root_000255:B001/m01`; encompassing cover `quranic:root_000255:B005/m01`; inscribed book or scroll `quranic:root_000255:B006/m01`; honor and generosity `quranic:root_001294:B001/m01`; necklace and ordered ornament `quranic:root_001294:B003/m01`; precious person or thing `quranic:root_001294:B010/m01`.
- Ayah anchors: 55:78 `ٱسْمُ` (س م و), `رَبِّ` (ر ب ب), `جَلَٰلِ` (ج ل ل), `إِكْرَامِ` (ك ر م).
- Synthesis: The name is an identifying mark that also raises and circulates reputation. Majesty gives it scale, encompassing cover gives it presence, and honor gives it the social action of generosity; inscription and ornament materialize how such a name is preserved and displayed.

## Standalone Subchannels

### S1. P1 The Refrain as Gift, Pledge, Capacity, and Denial
- Reading type: mixed
- Scene or process: Repeated address presents benefits as gifts under a pledge-like relation and tests whether the addressees will acknowledge, fail, delay, or deny.
- Active motifs: shortfall and delay `quranic:root_000048:B001/m01`; capacity `quranic:root_000048:B002/m01`; oath and binding pledge `quranic:root_000048:B003/m01`; benefits and favors `quranic:root_000048:B004/m01`; beautiful but bitter tree `quranic:root_000048:B005/m01`; benefits `quranic:root_000076:B006/m01`; oath `quranic:root_000076:B007/m01`; slackening `quranic:root_000076:B008/m01`; exertion `quranic:root_000076:B010/m01`; capacity `quranic:root_000076:B011/m01`; gift `quranic:root_000076:B012/m01`; direct denial `quranic:root_001290:B002/m01`; failure to persist `quranic:root_001290:B005/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and completion `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:13 and 55:16 `ءَالَآءِ` (ء ل و), `رَبِّ` (ر ب ب), `تُكَذِّبَ` (ك ذ ب). No surface ayah anchor is available for the cited `quranic:root_000076:*` motifs.
- Synthesis: Within P1, the refrain turns creation, instruction, balance, food, and elemental formation into presented benefits that demand an answer. The oath and capacity senses sharpen that answer into a relation of commitment: denial can appear as false attribution, insufficient effort, or failure to sustain acknowledgment.

### S2. P2 The Refrain as Gift, Pledge, Capacity, and Denial
- Reading type: mixed
- Scene or process: Repetition interrupts each bounded-water, maritime, mortality, and provision scene with a renewed demand for acknowledgment.
- Active motifs: shortfall and delay `quranic:root_000048:B001/m01`; capacity `quranic:root_000048:B002/m01`; oath and binding pledge `quranic:root_000048:B003/m01`; benefits and favors `quranic:root_000048:B004/m01`; beautiful but bitter tree `quranic:root_000048:B005/m01`; benefits `quranic:root_000076:B006/m01`; oath `quranic:root_000076:B007/m01`; slackening `quranic:root_000076:B008/m01`; exertion `quranic:root_000076:B010/m01`; capacity `quranic:root_000076:B011/m01`; gift `quranic:root_000076:B012/m01`; direct denial `quranic:root_001290:B002/m01`; failure to persist `quranic:root_001290:B005/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and completion `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:18, 55:21, 55:23, 55:25, 55:28, and 55:30 `ءَالَآءِ` (ء ل و), `رَبِّ` (ر ب ب), `تُكَذِّبَ` (ك ذ ب). No surface ayah anchor is available for the cited `quranic:root_000076:*` motifs.
- Synthesis: In P2, each recurrence measures acknowledgment against paired limits, extracted goods, safe passage, passing life, and continuous petition. The failure-to-persist sense is especially resonant beside the contrast between what vanishes and what remains.

### S3. P3 The Refrain as Gift, Pledge, Capacity, and Denial
- Reading type: mixed
- Scene or process: Repetition frames challenge, failed escape, material collapse, bodily recognition, and punishment as disclosures whose denial is repeatedly tested.
- Active motifs: shortfall and delay `quranic:root_000048:B001/m01`; capacity `quranic:root_000048:B002/m01`; oath and binding pledge `quranic:root_000048:B003/m01`; benefits and favors `quranic:root_000048:B004/m01`; beautiful but bitter tree `quranic:root_000048:B005/m01`; benefits `quranic:root_000076:B006/m01`; oath `quranic:root_000076:B007/m01`; slackening `quranic:root_000076:B008/m01`; exertion `quranic:root_000076:B010/m01`; capacity `quranic:root_000076:B011/m01`; gift `quranic:root_000076:B012/m01`; direct denial `quranic:root_001290:B002/m01`; failed persistence `quranic:root_001290:B005/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and completion `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:32, 55:34, 55:36, 55:38, 55:40, 55:42, and 55:45 `ءَالَآءِ` (ء ل و), `رَبِّ` (ر ب ب), `تُكَذِّبَ` (ك ذ ب); 55:43 `يُكَذِّبُ` (ك ذ ب). No surface ayah anchor is available for the cited `quranic:root_000076:*` motifs.
- Synthesis: In P3, denial is pressured by increasingly material evidence: blocked passage, flame, a split sky, bodily marks, seizure, and heated water. Capacity and exertion also reverse the failed escape challenge, where effort cannot produce the warrant needed for passage.

### S4. P4 The Refrain as Gift, Pledge, Capacity, and Denial
- Reading type: mixed
- Scene or process: Repeated address punctuates each layer of garden shelter, water, produce, intimacy, and recompense with a local acknowledgment test.
- Active motifs: shortfall and delay `quranic:root_000048:B001/m01`; capacity `quranic:root_000048:B002/m01`; oath and binding pledge `quranic:root_000048:B003/m01`; benefits and favors `quranic:root_000048:B004/m01`; beautiful but bitter tree `quranic:root_000048:B005/m01`; benefits `quranic:root_000076:B006/m01`; oath `quranic:root_000076:B007/m01`; slackening `quranic:root_000076:B008/m01`; exertion `quranic:root_000076:B010/m01`; capacity `quranic:root_000076:B011/m01`; gift `quranic:root_000076:B012/m01`; direct denial `quranic:root_001290:B002/m01`; failure to persist `quranic:root_001290:B005/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and completion `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, and 55:61 `ءَالَآءِ` (ء ل و), `رَبِّ` (ر ب ب), `تُكَذِّبَ` (ك ذ ب). No surface ayah anchor is available for the cited `quranic:root_000076:*` motifs.
- Synthesis: In P4, the refrain repeatedly converts sensuous garden detail into a relational claim. The gift and pledge senses prevent the scenes from remaining private luxury: each element is presented as a benefit whose source and terms are to be acknowledged.

### S5. P5 The Refrain as Gift, Pledge, Capacity, and Denial
- Reading type: mixed
- Scene or process: Repetition accompanies the lower gardens, gushing water, selected companions, and living textiles before the closing blessing of the name.
- Active motifs: shortfall and delay `quranic:root_000048:B001/m01`; capacity `quranic:root_000048:B002/m01`; oath and binding pledge `quranic:root_000048:B003/m01`; benefits and favors `quranic:root_000048:B004/m01`; beautiful but bitter tree `quranic:root_000048:B005/m01`; benefits `quranic:root_000076:B006/m01`; oath `quranic:root_000076:B007/m01`; slackening `quranic:root_000076:B008/m01`; exertion `quranic:root_000076:B010/m01`; capacity `quranic:root_000076:B011/m01`; gift `quranic:root_000076:B012/m01`; direct denial `quranic:root_001290:B002/m01`; failure to persist `quranic:root_001290:B005/m01`; sovereign ownership `quranic:root_000532:B001/m01`; nurture and completion `quranic:root_000532:B002/m01`.
- Ayah anchors: 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77 `ءَالَآءِ` (ء ل و), `رَبِّ` (ر ب ب), `تُكَذِّبَ` (ك ذ ب). No surface ayah anchor is available for the cited `quranic:root_000076:*` motifs.
- Synthesis: In P5, the acknowledgment test follows intensification rather than novelty alone: darker growth, stronger springs, fixed shelter, and richer textiles. The final movement toward the blessed name resolves the refrain's relational question by identifying the enduring source of the benefits.

### S6. Timed, Oriented Worship
- Reading type: mixed
- Scene or process: A devout reader receives a recurring portion of recitation, enters an oriented prayer place at the appointed light, and enacts the words through bodily prostration.
- Active motifs: communal prayer place `quranic:root_000675:B002/m01`; bodily points of prostration `quranic:root_000675:B003/m01`; visible trace of prostration `quranic:root_000675:B003/m02`; sunrise prayer place `quranic:root_000790:B006/m01`; direction of prayer `quranic:root_001198:B005/m01`; devout reader `quranic:root_001210:B006/m01`; recurring portion of recitation `quranic:root_001640:B002/m01`; receiving and learning recited words `quranic:root_001372:B011/m01`.
- Ayah anchors: 55:2 `قُرْءَانَ` (ق ر ء); 55:6 `يَسْجُدَ` (س ج د); 55:17 `مَشْرِقَيْنِ` (ش ر ق); 55:19 `يَلْتَقِيَ` (ل ق ي); 55:37 `وَرْدَةً` (و ر د); 55:56 and 55:74 `قَبْلَ` (ق ب ل).
- Synthesis: This regimen supports the surah's movement from a taught Qur'an to cosmic prostration by showing revelation received as a repeated portion and then embodied at specific points of the body. Sunrise and prayer-direction senses also turn the paired east-west horizon into practical orientation, so measured cosmic order becomes a pattern for recurrent worship.

### S7. Incense Preparation and Fumigation
- Reading type: mixed
- Scene or process: Aromatic woods and costus are selected for a censer, compounded with perfume, applied to a person or object, and released as a perceptible scent.
- Active motifs: aloeswood for incense `quranic:root_000076:B014/m01`; costus used in incense `quranic:root_001224:B006/m01`; aromatic incense wood `quranic:root_001238:B007/m01`; censer holding incense `quranic:root_001238:B007/m02`; compounded perfume `quranic:root_000434:B010/m01`; coating oneself or another with perfume `quranic:root_000434:B010/m02`; fragrance `quranic:root_001002:B004/m01`; perfuming and adornment `quranic:root_001002:B004/m02`; released scent `quranic:root_000609:B004/m01`.
- Ayah anchors: 55:3, 55:14, and 55:15 `خَلَقَ` (خ ل ق); 55:9 `قِسْطِ` (ق س ط); 55:12 `رَّيْحَانُ` (ر و ح); 55:33 `أَقْطَارِ` (ق ط ر); 55:41 `يُعْرَفُ` (ع ر ف). No surface ayah anchor is available for `quranic:root_000076:B014`.
- Synthesis: The scene materializes fragrant provision as a made effect: substances, vessel, application, and perception cooperate to produce aroma. It supports the surah's sensory presentation of benefit by showing how fragrance is produced, and it reframes the fire complex by contrasting destructive, unmastered heat with heat bounded in a tool to yield fragrance and honor.

### S8. Arrow-Lot Gambling as Counterfeit Measure
- Reading type: latent/lexical
- Scene or process: Marked gaming arrows are kept together in a leather receptacle, used in a wager, and made to assign divided portions through chance and deceptive victory.
- Active motifs: mark on a gaming arrow `quranic:root_001040:B002/m03`; leather receptacle for gaming arrows `quranic:root_000532:B010/m01`; assembled set of gaming arrows `quranic:root_000532:B010/m02`; gambling wager `quranic:root_001255:B007/m01`; victory by deception `quranic:root_001255:B007/m02`; cut and divided portions `quranic:root_001016:B009/m01`.
- Ayah anchors: 55:2 and 55:4 `عَلَّمَ`, and 55:24 `أَعْلَٰمِ` (ع ل م); 55:5 `قَمَرُ` (ق م ر); 55:13, 55:16-18, 55:21, 55:23, 55:25, 55:27-28, 55:30, 55:32, 55:34, 55:36, 55:38, 55:40, 55:42, 55:45-47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, 55:61, 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77-78 `رَبِّ`/`رَبُّ` (ر ب ب); 55:33 `مَعْشَرَ` (ع ش ر).
- Synthesis: This game usefully pressures the surah's balance, calculation, and recompense by presenting a counterfeit allocation system. Its pieces are marked and its shares are divided, but chance and deception determine the result; the contrast clarifies that the surah's measured order and answering yield are neither arbitrary nor manipulable.

### S9. Drawing and Retaining Well Water
- Reading type: latent/lexical
- Scene or process: An upright well apparatus carries a large bucket, water pours from repeated lifts, and the supply is transferred into vessels that fill, retain moisture, and show the trace of long use.
- Active motifs: upright pulley apparatus at a well `quranic:root_001273:B012/m01`; large drawing bucket `quranic:root_001077:B002/m01`; water pouring from buckets at the well `quranic:root_001077:B003/m01`; filling a waterskin to repletion `quranic:root_000286:B006/m01`; filled and retaining waterskin `quranic:root_001678:B007/m01`; vessel greened by retained water and repeated drawing `quranic:root_000418:B012/m01`.
- Ayah anchors: 55:9 `أَقِيمُ` and 55:46 `مَقَامَ` (ق و م); 55:12 `حَبُّ` (ح ب ب); 55:17 `مَغْرِبَيْنِ` (غ ر ب); 55:54 and 55:76 `مُتَّكِـِٔينَ` (و ك ء); 55:76 `خُضْرٍ` (خ ض ر).
- Synthesis: The apparatus materializes provision as transfer and retention: water must be raised, poured, caught, and kept, and repeated service alters the vessel itself. This supports the surah's universal petition and garden springs by giving continuous supply a concrete delivery mechanism rather than treating abundance as a static backdrop.

### S10. Timed Pasture and Camel Watering
- Reading type: latent/lexical
- Scene or process: A herd is released into open pasture, remains on forage near water, returns as darkness gathers, and drinks according to a recurring watering interval while a handler draws at the animals' mouths.
- Active motifs: open grazing meadow `quranic:root_001411:B001/m01`; release of animals to graze `quranic:root_000764:B003/m01`; pasture and residence around water `quranic:root_001657:B007/m01`; gathering dusk `quranic:root_001231:B007/m01`; evening return of livestock `quranic:root_000609:B005/m01`; camel watering on the tenth day `quranic:root_001016:B006/m01`; recurring watering interval `quranic:root_001640:B002/m02`; drawing water at camels' mouths `quranic:root_001198:B014/m01`.
- Ayah anchors: 55:7 and 55:10 `وَضَعَ` (و ض ع); 55:12 `رَّيْحَانُ` (ر و ح); 55:15 `مَّارِجٍ`, 55:19 `مَرَجَ`, and 55:22 and 55:58 `مَرْجَانُ` (م ر ج); 55:33 `مَعْشَرَ` (ع ش ر); 55:37 `وَرْدَةً` (و ر د); 55:41 `سِيمَٰ` (س و م); 55:56 and 55:72 `قَٰصِرَٰتُ`/`مَّقْصُورَٰتٌ` (ق ص ر); 55:56 and 55:74 `قَبْلَ` (ق ب ل).
- Synthesis: The cycle supports the primary picture of ongoing divine administration by making provision recurrent and scheduled: release, forage, return, and watering each have their time. It also materializes the repeated asking of creatures as bodily dependence at the water source, where an allotted interval becomes actual drink.

### S11. Moonlit Hunt Through Concealing Night
- Reading type: latent/lexical
- Scene or process: Hunters set out during the watches of a darkening night and use lunar light to locate prey whose sight and concealment are compromised.
- Active motifs: watches and portions of night `quranic:root_000063:B002/m01`; night covering a place in darkness `quranic:root_000266:B002/m01`; hunters setting out after game `quranic:root_000745:B006/m01`; hunting by moonlight `quranic:root_001255:B003/m01`.
- Ayah anchors: 55:5 `قَمَرُ` (ق م ر); 55:7 `سَّمَآءَ`, 55:29 and 55:33 `سَّمَٰوَٰتِ`, 55:37 `سَّمَآءُ`, and 55:78 `ٱسْمُ` (س م و); 55:15 `جَآنَّ`, 55:33 `جِنِّ`, 55:39, 55:56, and 55:74 `جَآنٌّ`, 55:46 and 55:62 `جَنَّتَانِ`, and 55:54 `جَنَّتَيْنِ` (ج ن ن); 55:44 `ءَانٍ` (ء ن ي).
- Synthesis: The hunt reframes the calculated moon as operational light: its measure governs when concealment protects and when it fails. That pressure sharpens the surah's escape, recognition, and seizure sequence, because pursuit unfolds inside a cosmos whose darkness, illumination, and outer bounds are already ordered.

### S12. Fulling, Dyeing, and Quilting a Furnishing
- Reading type: mixed
- Scene or process: Cloth is saturated with color, beaten and fulled, patterned, padded with cotton, sewn, and finished with an interior lining.
- Active motifs: saturated dye color `quranic:root_000790:B003/m01`; beating and fulling cloth `quranic:root_001231:B011/m01`; multicolored patterned cloth whose appearance misleads `quranic:root_001290:B009/m01`; laying cotton onto cloth `quranic:root_001657:B008/m01`; sewing a padded garment `quranic:root_001657:B008/m02`; garment lining `quranic:root_000128:B003/m01`.
- Ayah anchors: 55:7 and 55:10 `وَضَعَ` (و ض ع); 55:13, 55:16, 55:18, 55:21, 55:23, 55:25, 55:28, 55:30, 55:32, 55:34, 55:36, 55:38, 55:40, 55:42-43, 55:45, 55:47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, 55:61, 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77 `تُكَذِّبَ`/`يُكَذِّبُ` (ك ذ ب); 55:17 `مَشْرِقَيْنِ` (ش ر ق); 55:54 `بَطَآئِنُ` (ب ط ن); 55:56 and 55:72 `قَٰصِرَٰتُ`/`مَّقْصُورَٰتٌ` (ق ص ر).
- Synthesis: The workshop materializes the surah's rose-red and richly lined surfaces as transformations of material, and it gives the garden furnishings a sequence of skilled operations. The cloth that "lies" through its pattern also usefully pressures the refrain: visual splendor can misrepresent, whereas the surah presents crafted beauty as a truthful benefit whose source is acknowledged.

### S13. Death, Shrouding, and Interment
- Reading type: mixed
- Scene or process: Death is spoken of as release into rest, after which the body is covered, shrouded, placed in a grave, and given a protective grave canopy.
- Active motifs: death expressed as release or rest `quranic:root_000609:B016/m01`; covering the dead `quranic:root_000266:B009/m01`; burial shroud `quranic:root_000266:B009/m02`; grave and interment `quranic:root_000266:B009/m03`; canopy or cupola over a grave `quranic:root_001315:B006/m01`.
- Ayah anchors: 55:12 `رَّيْحَانُ` (ر و ح); 55:15 `جَآنَّ`, 55:33 `جِنِّ`, 55:39, 55:56, and 55:74 `جَآنٌّ`, 55:46 and 55:62 `جَنَّتَانِ`, and 55:54 `جَنَّتَيْنِ` (ج ن ن); 55:26 `كُلُّ`, 55:29 `كُلَّ`, and 55:52 `كُلِّ` (ك ل ل).
- Synthesis: This sequence materializes "everyone upon it is passing" as the full social handling of a body, not an abstract statement of impermanence. Covering and burial move the dead from visibility into concealment, sharpening the contrast with the divine Face that remains and with the gardens whose covering signifies living shelter rather than a grave.

### S14. P1-P3-P4 Measured Administration and Enforceable Settlement
- Reading type: latent/lexical
- Scene or process: Public conduct is inspected against a considered standard, a case is elevated to officials who know the parties, litigants gain access to authority, and the authority's order is carried out through custodial administration, including discharge of a public financial obligation.
- Active motifs: practical public accounting `quranic:root_000318:B006/m01`; municipal inspector who checks wrongdoing `quranic:root_000318:B006/m02`; settled and weighty deliberation `quranic:root_001645:B005/m01`; presenting a person or case to a ruler `quranic:root_000582:B004/m01`; local official acquainted with the community `quranic:root_001002:B006/m01`; litigants reaching the judge `quranic:root_001531:B005/m01`; execution of an order or document `quranic:root_001531:B002/m01`; sustained custodial administration `quranic:root_001273:B004/m01`; financial levy discharging an obligation `quranic:root_000244:B004/m01`.
- Ayah anchors: 55:5 `حُسْبَانٍ` (ح س ب); 55:7 `رَفَعَ` (ر ف ع); 55:7 `مِيزَانَ`, 55:8 `مِيزَانِ`, and 55:9 `وَزْنَ`/`مِيزَانَ` (و ز ن); 55:9 `أَقِيمُ` and 55:46 `مَقَامَ` (ق و م); 55:33 `تَنفُذُ`/`ٱنفُذُ` (ن ف ذ); 55:41 `يُعْرَفُ` (ع ر ف); 55:60 `جَزَآءُ` (ج ز ي).
- Synthesis: Bridge: P1 to P3 to P4, a causal sequence and role progression from measured oversight, through recognized jurisdiction, to enforceable settlement. The shared invariant is that order becomes effective when a standard passes through accountable roles into an executed outcome; this social mechanism materializes the surah's primary movement from balance, through recognition without interrogation, to recompense.

### S15. Recovering Lost Property by Description and Report
- Reading type: latent/lexical
- Scene or process: A found object is publicly announced and described while inquiries are made, reports are circulated, and successive leads are tracked until a claimant can recognize it.
- Active motifs: seeking news by inquiry `quranic:root_000318:B010/m01`; publicizing and transmitting a report `quranic:root_000582:B005/m01`; announcing found property `quranic:root_001002:B008/m01`; identification by description `quranic:root_001002:B008/m02`; tracking news through repeated inquiry `quranic:root_001480:B008/m01`.
- Ayah anchors: 55:5 `حُسْبَانٍ` (ح س ب); 55:7 `رَفَعَ` (ر ف ع); 55:35 `نُحَاسٌ` (ن ح س); 55:41 `يُعْرَفُ` (ع ر ف).
- Synthesis: Ordinary recovery requires a chain of announcement, description, inquiry, circulation, and recognition. That complete procedure usefully pressures P3's judgment scene by contrast: sinners are recognized immediately by their marks and need not be questioned, so bodily evidence replaces the social apparatus normally needed to establish identity.

### S16. Milking at the Threshold of Birth
- Reading type: latent/lexical
- Scene or process: An animal near parturition produces rich milk; a milker approaches from the designated side, and the udder may retain the milk, release it in repeated yield, or cease to supply what was expected.
- Active motifs: approaching parturition `quranic:root_000493:B004/m01`; rich milk before birth `quranic:root_001174:B004/m01`; milker positioned on a designated side `quranic:root_000170:B009/m01`; milk retained in the udder `quranic:root_000582:B007/m01`; repeated flow and yield of milk `quranic:root_000563:B006/m01`; low milk and weakness `quranic:root_000497:B006/m01`; expected milk that fails to continue `quranic:root_001290:B006/m01`.
- Ayah anchors: 55:4 `بَيَانَ`, 55:20 `بَيْنَ`, and 55:44 `بَيْنَ` (ب ي ن); 55:7 `رَفَعَ` (ر ف ع); 55:11, 55:52, and 55:68 `فَٰكِهَةٌ`/`فَٰكِهَةٍ` (ف ك ه); 55:13, 55:16, 55:18, 55:21, 55:23, 55:25, 55:28, 55:30, 55:32, 55:34, 55:36, 55:38, 55:40, 55:42-43, 55:45, 55:47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, 55:61, 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77 `تُكَذِّبَ`/`يُكَذِّبُ` (ك ذ ب); 55:35 `يُرْسَلُ` (ر س ل); 55:37 `دِّهَانِ` (د ه ن); 55:54 `دَانٍ` (د ن و).
- Synthesis: The scene materializes creation and provision as an embodied yield that has timing, an animal source, a human operator, and variable release. Retention, scarcity, and milk that "lies" by failing to continue sharpen the repeated acknowledgment test: dependable provision is an actively sustained benefit, not an automatic property of the source.

### S17. Treating an Infected Wound
- Reading type: latent/lexical
- Scene or process: A patient presents persistent local pain and a wound that swells, spreads, and suppurates; a practitioner identifies the condition and treats it with costus and a thick medicinal coating.
- Active motifs: persistent pain in a body part `quranic:root_001273:B019/m01`; wound swelling and spreading into corruption `quranic:root_000138:B004/m01`; suppurating ulcer `quranic:root_000025:B011/m01`; practitioner or physician `quranic:root_001002:B012/m01`; costus used as medicine `quranic:root_001224:B006/m02`; thick medicinal coating `quranic:root_000532:B006/m01`.
- Ayah anchors: 55:9 `قِسْطِ` (ق س ط); 55:9 `أَقِيمُ` and 55:46 `مَقَامَ` (ق و م); 55:10 `أَرْضَ`, 55:29 and 55:33 `أَرْضِ` (ء ر ض); 55:13, 55:16-18, 55:21, 55:23, 55:25, 55:27-28, 55:30, 55:32, 55:34, 55:36, 55:38, 55:40, 55:42, 55:45-47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, 55:61, 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77-78 `رَبِّ`/`رَبُّ` (ر ب ب); 55:20 `يَبْغِيَ` (ب غ ي); 55:41 `يُعْرَفُ` (ع ر ف).
- Synthesis: This treatment scene reframes P3's recognized bodies and punitive liquids as an anti-treatment. Ordinary care identifies a spreading lesion and applies medicine to arrest corruption; judgment instead exposes the body's condition and subjects it to a circuit that aggravates rather than repairs.

### S18. Bargaining a Commodity Sale Across Cash and Credit
- Reading type: latent/lexical
- Scene or process: A merchant, represented by an oil seller, presents stock; parties negotiate and appraise its price, payment is arranged as cash or deferred credit, and remaining goods may be sold in bulk without measurement, exposing capital to loss.
- Active motifs: oil merchant `quranic:root_000497:B010/m01`; bargaining and stated price `quranic:root_000764:B001/m01`; immediate cash payment `quranic:root_001069:B011/m01`; purchase on credit or deferred payment `quranic:root_001069:B012/m01`; appraisal and pricing of goods `quranic:root_001273:B010/m01`; bulk sale without measure `quranic:root_001238:B011/m01`; reduction of capital through trade loss `quranic:root_001657:B004/m01`.
- Ayah anchors: 55:7 and 55:10 `وَضَعَ` (و ض ع); 55:9 `أَقِيمُ` and 55:46 `مَقَامَ` (ق و م); 55:33 `أَقْطَارِ` (ق ط ر); 55:37 `دِّهَانِ` (د ه ن); 55:41 `سِيمَٰ` (س و م); 55:50 and 55:66 `عَيْنَانِ` (ع ي ن).
- Synthesis: The transaction materializes the balance command as a vulnerable commercial practice: value must be appraised, price negotiated, payment timed, and stock measured. A bulk shortcut and capital loss show what happens when exact measure is displaced, while cash and credit clarify the temporal dimension of an obligation awaiting settlement.

### S19. Gift Exchange Under Rivalry and Expected Return
- Reading type: latent/lexical
- Scene or process: Donors bestow goods in a social exchange where openhanded giving, rivalry in generosity, a gift designed to obtain reward or praise, and the receiver's pleased acceptance coexist.
- Active motifs: openhanded giving `quranic:root_000563:B010/m01`; bestowal of good `quranic:root_001510:B005/m01`; rivalry in generosity `quranic:root_001294:B006/m01`; gift offered to obtain reward or praise `quranic:root_001294:B008/m01`; response of pleased acceptance `quranic:root_001294:B009/m01`.
- Ayah anchors: 55:27 and 55:78 `إِكْرَامِ` (ك ر م); 55:35 `يُرْسَلُ` (ر س ل); 55:35 `تَنتَصِرَ` (ن ص ر).
- Synthesis: The social frame distinguishes generosity from strategic exchange. It usefully pressures the refrain and P4's recompense: an answer to real beneficence differs from a prestige payment engineered by a competitive giver, even when both outwardly take the form of gift and response.

### S20. Tanning and Red-Finishing a Hide
- Reading type: latent/lexical
- Scene or process: Tannin-bearing plant material and red resin are prepared for a hide, which is tanned, colored, coated, and repaired as its surface begins to fissure.
- Active motifs: tannin-bearing plant `quranic:root_000076:B005/m01`; red resin and dye from a tree `quranic:root_001077:B015/m01`; tanned and reddened hide `quranic:root_000369:B004/m01`; fissuring of the hide `quranic:root_000369:B004/m02`; thick treatment used to repair leather `quranic:root_000532:B006/m02`.
- Ayah anchors: 55:13, 55:16-18, 55:21, 55:23, 55:25, 55:27-28, 55:30, 55:32, 55:34, 55:36, 55:38, 55:40, 55:42, 55:45-47, 55:49, 55:51, 55:53, 55:55, 55:57, 55:59, 55:61, 55:63, 55:65, 55:67, 55:69, 55:71, 55:73, 55:75, and 55:77-78 `رَبِّ`/`رَبُّ` (ر ب ب); 55:17 `مَغْرِبَيْنِ` (غ ر ب); 55:72 `حُورٌ` (ح و ر); no surface ayah anchor is available for `quranic:root_000076:B005`.
- Synthesis: The craft materializes P3's rose-red sky as a transformation of surface: plant-derived color, coating, and cracking become one unstable material state. In contrast with the stable lined and patterned furnishings of the gardens, the fissured red hide supplies a tactile model for a sky whose apparent fabric is coming apart.


