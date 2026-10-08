Surah: 79. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S79 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s079/surah.r2/text.md =====
# Surah 79

- 79:1 وَٱلنَّٰزِعَٰتِ غَرْقًۭا
- 79:2 وَٱلنَّٰشِطَٰتِ نَشْطًۭا
- 79:3 وَٱلسَّٰبِحَٰتِ سَبْحًۭا
- 79:4 فَٱلسَّٰبِقَٰتِ سَبْقًۭا
- 79:5 فَٱلْمُدَبِّرَٰتِ أَمْرًۭا
- 79:6 يَوْمَ تَرْجُفُ ٱلرَّاجِفَةُ
- 79:7 تَتْبَعُهَا ٱلرَّادِفَةُ
- 79:8 قُلُوبٌۭ يَوْمَئِذٍۢ وَاجِفَةٌ
- 79:9 أَبْصَٰرُهَا خَٰشِعَةٌۭ
- 79:10 يَقُولُونَ أَءِنَّا لَمَرْدُودُونَ فِى ٱلْحَافِرَةِ
- 79:11 أَءِذَا كُنَّا عِظَٰمًۭا نَّخِرَةًۭ
- 79:12 قَالُوا۟ تِلْكَ إِذًۭا كَرَّةٌ خَاسِرَةٌۭ
- 79:13 فَإِنَّمَا هِىَ زَجْرَةٌۭ وَٰحِدَةٌۭ
- 79:14 فَإِذَا هُم بِٱلسَّاهِرَةِ
- 79:15 هَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- 79:16 إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- 79:17 ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- 79:18 فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
- 79:19 وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
- 79:20 فَأَرَىٰهُ ٱلْءَايَةَ ٱلْكُبْرَىٰ
- 79:21 فَكَذَّبَ وَعَصَىٰ
- 79:22 ثُمَّ أَدْبَرَ يَسْعَىٰ
- 79:23 فَحَشَرَ فَنَادَىٰ
- 79:24 فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
- 79:25 فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
- 79:26 إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- 79:27 ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا
- 79:28 رَفَعَ سَمْكَهَا فَسَوَّىٰهَا
- 79:29 وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا
- 79:30 وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ
- 79:31 أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا
- 79:32 وَٱلْجِبَالَ أَرْسَىٰهَا
- 79:33 مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- 79:34 فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- 79:35 يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ
- 79:36 وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- 79:37 فَأَمَّا مَن طَغَىٰ
- 79:38 وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 79:39 فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
- 79:40 وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
- 79:41 فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- 79:42 يَسْـَٔلُونَكَ عَنِ ٱلسَّاعَةِ أَيَّانَ مُرْسَىٰهَا
- 79:43 فِيمَ أَنتَ مِن ذِكْرَىٰهَآ
- 79:44 إِلَىٰ رَبِّكَ مُنتَهَىٰهَآ
- 79:45 إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
- 79:46 كَأَنَّهُمْ يَوْمَ يَرَوْنَهَا لَمْ يَلْبَثُوٓا۟ إِلَّا عَشِيَّةً أَوْ ضُحَىٰهَا


===== _commentary/v16/work/s079/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ز ع (root_001489): 79:1 وَٱلنَّٰزِعَٰتِ

- **B001** yerinden çekip çıkarma — yerinden çekip çıkarmak · çekip almak, söküp çıkarmak · kalpteki düşmanlığı veya sevgiyi gidermek · sözden anlam çıkarmak
  أصل صحيح يدل على قلع شيء (maqayis)؛ نزعت الشيء قلعته (ayn)؛ نزعت الشيء من مكانه قلعته (sihah)؛ نزع الشيء جذبه من مقره (mufradat)؛ انتزعت آية من القرآن ونزع فلان كذا أي سلب (mufradat)؛ تنزع الأرواح وتقلع الناس من مقرهم (mufradat)
- **B002** yayın kirişini çekme — yayın kirişini çekip germek · yayın kirişini çeken atıcılar
  الذي ينزع في القوس يجذب وتره بالسهم (maqayis)؛ نزع في القوس مدها أي جذب وترها (sihah)؛ نزع في القوس إذا مد وترها (tahdhib)؛ كنزع القوس عن كبده (mufradat)
- **B003** vazgeçip geri durma [kalıp] — o işi bırakıp ondan vazgeçmek · gençlik heveslerinden vazgeçmek
  نزع عن الأمر نزوعا تركه (maqayis)؛ نزع عن الأمر نزوعا انتهى عنه (sihah)؛ نزع الرجل عن الصبا إذا كف عنه (tahdhib)؛ النزع عن الشيء الكف عنه (mufradat)
- **B004** özlemle yönelme — bir şeyi isteyip ona yönelmek · ailesini veya yurdunu özlemek · otlağını veya yurdunu özleyen deve · develeri yurtlarına yönelmek · eşleşmek isteyen koyunlar
  نازعت النفس إلى الأمر نزاعا ونزعت إليه إذا اشتهته (maqayis)؛ نزع فلان إلى أهله أي اشتاق (sihah)؛ هو ينزع إليه نزاعا (tahdhib)؛ النزوع الاشتياق الشديد (mufradat)؛ أنزع القوم نزعت إبلهم إلى أوطانها (mufradat)؛ غنم نزع إذا حنت فاشتهت الفحل (tahdhib)
- **B005** köken bağı veya topluluk dışına çıkmışlık — babasına veya soyuna çekmek · soyuna çeken ya da başka bir topluluktan alınmış atlar · kendi topluluğu dışında evlenen kadınlar · kendi halkı dışında yaşayan yabancı
  نزع إلى أبيه في الشبه (maqayis)؛ النزائع من الخيل التي نزعت إلى أعراق (maqayis;sihah;tahdhib)؛ النزائع من النساء اللواتي يزوجن في غير عشائرهن (maqayis;sihah)؛ كل غريب نزيع (maqayis)؛ إنما هو عرق نزعه (tahdhib)
- **B006** karşılıklı çekişme — çekişme, tartışma · karşılıklı çekişme veya tartışma · kadehi birbirine uzatmak · el sıkışmak
  نازعته منازعة ونزاعا إذا جاذبته في الخصومة (sihah)؛ التنازع التخاصم (sihah)؛ المنازعة في الخصومة مجاذبة الحجج (tahdhib)؛ منازعة الكأس معاطاتها (tahdhib)؛ نازعني فلان بنانه أي صافحني (tahdhib)؛ التنازع والمنازعة المجاذبة ويعبر بهما عن المخاصمة والمجادلة (mufradat)
- **B007** şakaklardan gerilemiş saç çizgisi — saçları şakaklardan gerilemiş erkek · alnın iki yanındaki açılmış saç çizgisi bölgeleri
  النزعة الموضع من رأس الأنزع (maqayis)؛ رجل أنزع بين النزع (sihah)؛ الأنزع الذي انحسر الشعر عن جانبي جبهته (tahdhib)؛ رجل أنزع زال عنه شعر رأسه (mufradat)؛ لا يقال امرأة نزعاء ولكن زعراء (maqayis;mufradat)
- **B008** elle su çekilen sığ kuyu [kalıp] — elle su çekilen sığ kuyu · kovayı elle çekerek kuyudan su almak
  بئر نزوع قريبة القعر ينزع منها باليد (maqayis)؛ بئر نزوع ونزيع أي قريبة القعر ينزع منها باليد (sihah)؛ نزع بيده إذا استقى بدلو علق فيها الرشاء (tahdhib)؛ بئر نزوع قريبة القعر ينزع منها باليد (mufradat)
- **B009** görüş ve amaç yönelimi — görüş, düzenleme yolu ve amaç gücü · amacı yakın, erişimi kolay
  فلان قريب المنزعة أي قريب الهمة (maqayis;sihah)؛ منزعة الرجل رأيه (maqayis)؛ المنزعة ما يرجع إليه الرجل من أمره ورأيه وتدبيره (sihah)؛ المنزعة قوة عزم الرأي والهمة (tahdhib)
- **B010** eş adlı somut araç ve nesneler — bal toplayanın kullandığı geniş kaşıksı araç · atılan ok · su çekenin üzerinde durduğu kaya · içe doğru eğri yay
  المنزعة كالملعقة يكون مع مشتار العسل (maqayis)؛ المنزع بالكسر السهم (sihah)؛ المنزعة الصخرة التي يقوم عليها الساقي (tahdhib)؛ المنزعة القوس الفجواء (tahdhib)؛ خشبة عريضة نحو الملعقة تكون مع مشتار العسل (tahdhib)
- **B011** hoş içim bitişi [kalıp] — içim bitişi ve son tadı hoş içecek
  شراب طيب المنزعة أي طيب مقطع الشرب (maqayis;sihah)؛ شراب طيب المنزعة إذا كان طيب الختام وهو ساعة ينزعه عن فيه (tahdhib)؛ شراب طيب المنزعة أي المقطع إذا شرب (mufradat)
- **B012** hızla ileri atılma — atlar serbestçe ve hızla koşmak · bir hedefe hızla atılan
  يقال للخيل إذا جرت طلقا لقد نزعت (sihah)؛ منتزعا إلى كذا أي متسرعا إليه نازعا (sihah)؛ يقال للخيل إذا جرت لقد نزعت سننا (tahdhib)
- **B013** arazilerin sınırdaş olması [kalıp] — bizim araziye sınırdaş arazi
  هذه أرض تنازع أرضنا إذا كانت تتاخمها (tahdhib)
- **B014** çapraz yönlerden esen rüzgârlar [kalıp] — farklı ve çapraz yönlerden esen rüzgârlar
  النزائع من الرياح هي النكب سميت نزائع لاختلاف مهابها (tahdhib)
- **B015** türü belirtilmemiş bir bitki — türü belirtilmemiş bilinen bir bitki
  النزعة نبت معروف (tahdhib)
- **B016** ölümün son anlarını yaşama [kalıp] — can çekişmekte olmak
  فلان في النزع أي في قلع الحياة (sihah)؛ فلان ينزع نزعا إذا كان في السياق عند الموت (tahdhib)

## غ ر ق (root_001080): 79:1 غَرْقًا

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

## ن ش ط (root_001505): 79:2 وَٱلنَّٰشِطَٰتِ, 79:2 نَشْطًا

- **B001** istek ve canlılıkla harekete geçme — istekli ve canlı olmak · istekli, canlı ve çalışmaya hazır · istekli ve etkin · bir işe istekle yönelmek · topluluğun binek hayvanları dinç olmak · dişi deve yürüyüşünü güçlendirip ön ayaklarını ileri atmak · otlak onu semirtip yapısını güçlendirmek · onu yakalayıp yürürken ön ayaklarını hızla geri çekmek
  أصل صحيح يدل على اهتزاز وحركة (maqayis)؛ نشط الإنسان ينشط نشاطا فهو نشيط طيب النفس للعمل (ayn;tahdhib)؛ نشط الرجل ينشط نشاطا فهو نشيط (sihah)؛ أنشط القوم إذا كانت دوابهم نشيطة (maqayis;sihah)؛ أنشطه الكلأ أي سمنه (sihah;tahdhib)
- **B002** bulunduğu yerden çıkıp başka yere geçme — bir bölgeden başka bir bölgeye çıkan hayvan · kaygılar sahibini oradan oraya sürüklemek
  الثور ناشط لأنه ينشط من بلد إلى بلد (maqayis)؛ الناشط اسم للثور الوحشي وهو الخارج من أرض إلى أرض (ayn)؛ النجوم تنشط من برج إلى برج (sihah)؛ الحمار ينشط من بلد إلى بلد والهموم تنشط بصاحبها (tahdhib)؛ ثور ناشط خارج من أرض إلى أرض (mufradat)
- **B003** ana yoldan yana ayrılan yol — ana yoldan sağa veya sola ayrılan yol · ana akıştan yana ayrılan su yolları · yol onları ana güzergâhtan yana çevirdi
  طريق ناشط ينشط في الطريق الأعظم يمنة ويسرة (maqayis)؛ طريق ناشط ينشط من الطريق الأعظم يمنة ويسرة (ayn)؛ وكذلك النواشط من المسايل (ayn;tahdhib)؛ نشط بهم الطريق (tahdhib)
- **B004** dışını soyup kabuğundan çıkarma [kalıp] — bir şeyi soyup dış örtüsünden çıkarmak · balığın derisini soymak
  نشطت الشيء قشرته كأنه لما قشر أخرج من جلده (maqayis)؛ انتشطت السمكة إذا قشرتها (tahdhib)
- **B005** kolay çözülen ilmekle bağlama veya çekerek çözme — çekilince kolay çözülen ilmek düğümü · ipi ilmek düğümüyle bağlamak · düğümleri kolay çözülen ilmekle bağlamak · ilmeği çekerek bağı çözmek · ipi kendine çekip çözülmesini sağlamak · bağından çözülmüş gibi hızla atılmak · tutulan hayvanları serbest bırakıp otlağa salmak · yeniden örmek için halatları sökenler
  الأنشوطة العقدة مثل عقدة السراويل (maqayis)؛ عقدة يسهل انحلالها (ayn;sihah)؛ نشطت الحبل عقدته أنشوطة وأنشطته حللته (sihah;tahdhib)؛ الانتشاط وهو مدك شيئا إليك حتى ينحل (ayn)؛ الملائكة التي تعقد الأمور (mufradat)؛ النشط ناقضو الحبال (tahdhib)؛ نشطت الإبل تنشيطا إذا كانت ممنوعة من الرعي فأرسلتها ترعى (tahdhib)
- **B006** doğrudan çekip yerinden çıkarma [kalıp] — kovası tek çekişte çıkan sığ kuyu · kovası ancak çok kez çekilerek çıkan kuyu · kovayı yardımcı düzenek olmadan kuyudan yukarı çekmek · hayvanın otu dişleriyle çekip koparması
  بئر أنشاط قريبة القعر يخرج دلوها بجذبة (maqayis;mufradat)؛ نشطت الدلو من البئر بغير قامة (maqayis;tahdhib)؛ نزعتها بغير بكرة (sihah)؛ تنشط الأرواح نشطا أي تنزعها نزعا كما ينزع الدلو من البئر (tahdhib)؛ الملائكة التي تنشط أرواح الناس أي تنزع (mufradat)؛ انتشط المال المرعى أي انتزعته بالأسنان كالاختلاس (tahdhib)
- **B007** sefer yolunda veya bölüşümden önce alınan küçük ganimet — sefer yolunda veya bölüşümden önce alınan küçük ganimet
  النشيطة من الإبل أن توجد فتساق من غير أن يعمد لها (maqayis)؛ مال هي إبل يسيرة ينشطها الجيش أو بعضهم فلا تسع القسمة فيجعلونها للرئيس (ayn)؛ ما يغنمه الغزاة في الطريق قبل البلوغ إلى الموضع الذي قصدوه (sihah)؛ ما أصاب الرئيس في الطريق قبل أن يصل إلى بيضة القوم (tahdhib)؛ ما ينشط الرئيس لأخذه قبل القسمة (mufradat)
- **B008** yılanın dişiyle ısırıp sokması [kalıp] — yılan onu dişiyle ısırmak · engerek onu ısırıp sokmak · ölüm onu bir ısırık gibi yakalamak
  نشطته الحية إذا عضته بنابها (sihah)؛ نشطته الأفعى إذا نهشته (tahdhib)؛ نشطته الأفعى إذا عضته (tahdhib)؛ نشطته شعوب نشطا وهي المنية (tahdhib)؛ نشطته الحية نهشته (mufradat)
- **B009** tuzlu suda bekletilen bir balık türü — su ve tuz içinde bekletilen bir balık türü
  النشوط كلمة عراقية وهو سمك يمقر في ماء وملح (ayn)؛ النشوط أيضا ضرب من السمك وليس بالشبوط (sihah)؛ النشوط كلام عراقي وهو سمك يمقر في ماء وملح (tahdhib)
- **B010** uzun binicilikten sonra binekten inmiş kişi [kalıp] — uzun binicilikten sonra bineğinden inmiş adam · uzun binicilikten sonra bineğinden inmiş adam
  رجل منتشط من الانتشاط ومتنشط من التنشيط إذا نزل عن دابته من طول الركوب ولا يقال ذلك للراجل (tahdhib)
- **B011** doğanın kuşu pençesiyle kavraması [kalıp] — doğanın kuşu pençesiyle yakalaması
  نشط الصقر الطائر أي خلبه بمخلبه (ayn)

## س ب ح (root_000666): 79:3 وَٱلسَّٰبِحَٰتِ, 79:3 سَبْحًا

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

## س ب ق (root_000671): 79:4 فَٱلسَّٰبِقَٰتِ, 79:4 سَبْقًا

- **B001** harekette ya da işte öne geçme ve yarışarak ön alma — koşuda, işte ya da bir şeyde başkasının önüne geçmek · öne geçme; koşuda ya da işte önce gelme · bir işte önceden kazanılmış öncelik · yarışma; koşuda ve benzeri bir alanda birbirini geçmeye çalışma · yarışmak ya da bir şeye önce davranmak · atış yarışmasına gitmek · kapıya ilk varmak için birbirinden önce davranmak · yolu aşıp geçerek yönünü kaybetmek · yarışta başa geçen at ya da benzeri varlık · iyi işlerle ödüle önden koşanlar · önceden kesinleşip yürürlüğe girmek
  أصل واحد صحيح يدل على التقديم (maqayis)؛ السبق القدمة في الجري وفي الأمر (ayn;tahdhib)؛ وسبق يسبق سبقا (jamhara)؛ سابقته فسبقته سبقا واستبقنا في العدو أي تسابقنا (sihah)؛ أصل السبق التقدم في السير والاستباق التسابق (mufradat)
- **B002** yarışta ortaya konup kazananın aldığı pay — yarışta ya da atışta ortaya konup kazananın aldığı pay · yarış payını almak ya da yarış payını vermek · ortaya konan yarış payını kazandı
  السبق الخطر الذي يأخذه السابق (maqayis)؛ السبق الخطر يوضع بين أهل السباق (ayn;sihah)؛ السبق الرهن (jamhara)؛ الخطر الذي يوضع في النضال والرهان في الخيل فمن سبق أخذه (tahdhib)
- **B003** avcı kuşun ayaklarına takılan iki bağ — avcı kuşun ayaklarına takılan iki bağ · avcı kuşun ayaklarına bu iki bağı takmak
  السباقان قيد أرجل الطائر الجارح بسير أو خيط (ayn)؛ سباقا البازي قيداه من سير أو غيره (sihah)؛ السباقان في رجل الطائر الجارح قيداه من سير أو خيط وسبقت البازي إذا جعلت السباقان في رجليه (tahdhib)
- **B004** yakalanmaktan kurtulacak kadar öne kaçma — takip edenin elinden kaçıp kurtulmak · kaçıp kurtulmuş olmamak; takip edeni aşamamış olmak
  وما نحن بمسبوقين أي لا يفوتوننا؛ ولا يحسبن الذين كفروا سبقوا؛ وما كانوا سابقين (mufradat)

## د ب ر (root_000458): 79:5 فَٱلْمُدَبِّرَٰتِ, 79:22 أَدْبَرَ

- **B001** arka taraf — bir şeyin arkası ve önünün karşıtı · söyleneni duymazdan gelmek ve önemsememek
  الدبر خلاف القبل (maqayis;jamhara;sihah;tahdhib;mufradat)؛ جعلت قوله دبر أذني (maqayis;jamhara;sihah;tahdhib)
- **B002** sonuna erip geçme — günün sonuna gelmesi veya geçip gitmesi · ibadetlerin son bölümleri ya da hemen sonrası · geçip gitmiş dün · bir sürenin son vakti
  دبر النهار وأدبر إذا جاء آخره (maqayis;sihah;tahdhib;mufradat)؛ أدبار السجود أواخر الصلوات (tahdhib;mufradat)؛ أمس الدابر الذاهب (jamhara;sihah;tahdhib)؛ الدبر الموت (tahdhib)
- **B003** sırtını dönüp uzaklaşma — sırtını dönmek, yüz çevirmek veya kaçmak · yenilgi; bağlama göre savaşta üstünlük
  الإدبار خلاف الإقبال (jamhara;sihah;mufradat)؛ يولون الدبر (tahdhib;mufradat)؛ جعلت كلامه دبر أذني أي أعرضت عنه (maqayis;jamhara;sihah;tahdhib)؛ الدبرة الهزيمة (sihah;tahdhib)
- **B004** son izine kadar yok etme — bir topluluğun son kalanını ve soyunu tümüyle yok etmek · yok oluş ve iz kalmaması
  قطع الله دابرهم أي آخر من بقي منهم (maqayis;sihah;tahdhib;mufradat)؛ الدبار الهلاك وانقطاع الأثر (jamhara;sihah;tahdhib;mufradat)؛ الدابر الأصل والعقب (tahdhib)
- **B005** karşılıklı sırt çevirip bağ kesme — birine sırt çevirip düşmanlık etmek · karşılıklı ilişkiyi kesip düşmanlaşmak
  دابرت فلانا عاديته (maqayis;sihah;mufradat)؛ لا تدابروا (maqayis;sihah;tahdhib;mufradat)؛ تدابر القوم إذا تقاطعوا وتعادوا (jamhara;sihah;tahdhib)
- **B006** sonucunu düşünerek planlama — bir işi sonucunu düşünerek planlamak · bir işin sonunu ve sonuçlarını düşünüp değerlendirmek
  التدبير أن يدبر الإنسان أمره (maqayis)؛ التدبير في الأمر أن تنظر إلى ما يؤول إليه عاقبته (sihah;tahdhib)؛ التدبير التفكر في دبر الأمور (mufradat)
- **B007** ölümden sonra özgür bırakma — köle durumundaki kişiyi sahibinin ölümünden sonra özgür bırakma · sahibi öldükten sonra özgür olacak köle durumundaki kişi
  التدبير عتق الرجل عبده أو أمته عن دبر (maqayis)؛ عبد مدبر إذا قيل له إذا مت فأنت حر (jamhara)؛ التدبير عتق العبد عن دبر (sihah;mufradat)؛ أن يعتق الرجل عبده بعد موته (tahdhib)
- **B008** başkasından söz aktarma — 
  دبرت الحديث عن فلان إذا حدثت به عنه (maqayis)؛ دبرت الحديث إذا حدثت به عن غيرك (sihah;tahdhib)؛ ليس بمعروف وإنما هو يذبره (tahdhib)
- **B009** arka uzuv bölümü — kuşun ayağındaki arka parmak · toynağın bileğe yakın arka bölümü · insanın topuk arkası
  دابرة الطائر الإصبع التي في مؤخر رجله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ دابرة الإنسان عرقوبه (jamhara;sihah;tahdhib)؛ دابرة الحافر ما حاذى مؤخر الرسغ (maqayis;sihah;tahdhib;mufradat)
- **B010** geriye yönelmiş işleme — ipliğin geriye doğru bükülen bölümü · kulağının arka tarafı yarılmış hayvan · kulağın arkasındaki yarık veya kıvrım
  الدبير ما أدبرت به المرأة من غزلها (maqayis;sihah;mufradat)؛ القبيل ما فتلته إلى قدام والدبير ما فتلته إلى خلف (jamhara;tahdhib)؛ الشاة مدابرة تشق أذنها من قبل قفاها (maqayis;jamhara;sihah;tahdhib;mufradat)
- **B011** iki yandan arı soylu [kalıp] — hem anne hem baba yönünden arı ve saygın soylu
  رجل مقابل مدابر كريم النسب من قبل أبويه (maqayis)؛ مقابل ومدابر إذا كان محضا من أبويه (jamhara;sihah;tahdhib;mufradat)
- **B012** karşıt yönlü batı rüzgârı — karşı yöndeki rüzgârın zıddı sayılan batı rüzgârı · rüzgârın bu batı yönlü türe dönüşmesi
  الدبور ريح تقبل من دبر الكعبة (maqayis)؛ الدبور الريح المعروفة (jamhara;mufradat)؛ الدبور الريح التي تقابل الصبا (sihah;tahdhib)؛ دبرت الريح إذا صارت دبورا (jamhara;sihah)
- **B013** öndeki kümeyi izleyen yıldız — belirli yıldız kümesini izleyen yıldız veya küçük yıldız kümesi
  الدبران نجم سمي بذلك لأنه يدبر الثريا (maqayis;tahdhib)؛ الدبران معروف لأنه يدبر الثريا (jamhara)؛ الدبران خمسة كواكب من الثور (sihah)؛ الدابر يقال للتابع (mufradat)
- **B014** arı topluluğu — arı ve eşek arısı topluluğu · bu topluluğun tek bir arısı
  الدبر النحل الواحدة دبرة (jamhara;mufradat)؛ الدبر جماعة النحل ويجمع على دبور (sihah)؛ الدبر النحل وجمعه دبور (tahdhib)؛ الدبر النحل والزنابير ونحوهما مما سلاحها في أدبارها (mufradat)
- **B015** ekim alanındaki tarla parçası — ekim alanındaki tarla bölmeleri · ekim alanındaki tek tarla bölmesi
  الدبار المشارات من الزرع (maqayis)؛ الدبار واحدها دبارة وهي المشارات (jamhara)؛ الدبرة والدبارة المشارة في المزرعة (sihah)؛ الدبار المشارات واحدتها دبرة (tahdhib)؛ الدبرة من المزرعة جمعها دبار (mufradat)
- **B016** çok miktarda mal — çok ve kalıcı mal · çok malı olan kişi
  المال الكثير يقال مال دبر (maqayis;jamhara;sihah;tahdhib)؛ المدبور الكثير المال (tahdhib)؛ الدبر المال الكثير الذي يبقى بعد صاحبه (mufradat)
- **B017** hayvan sırtındaki yara — devenin veya başka bir hayvanın sırtındaki yara · hayvanın sırtında yara oluşmak
  الدبرة في ظهر البعير وغيره (jamhara)؛ أدبرت البعير فدبر (sihah)؛ دبر البعير يدبر دبرا (tahdhib)؛ دبر البعير دبرا فهو أدبر ودبر (mufradat)
- **B018** okun hedefin arkasına düşmesi — okun hedefi geçip arkasına düşmesi · hedefin arkasına çıkan ok
  دابر من السهام الذي يخرج من الهدف (maqayis;sihah)؛ دبر السهم الهدف إذا سقط وراءه (jamhara)؛ دبر السهم الهدف إذا صار من وراء الهدف (tahdhib)؛ دبر السهم الهدف سقط خلفه (mufradat)
- **B019** bahisli çekimde kaybeden ok — bahisli ok çekiminde kazanamayan ok · bahisli oyunda malını yitirmek
  الدابر من القداح الذي لم يخرج وهو خلاف الفائز (maqayis)؛ الدابر من القداح خلاف الفائز وصاحبه مدابر (sihah)؛ المدابر الذي يضرب بالقداح (tahdhib)؛ دبر بالقمار إذا ذهب به (maqayis)
- **B020** Çarşamba gününün eski adı — Çarşamba gününün eski dönemlerdeki adı
  دبار اسم يوم الأربعاء وفي مثل هذا نظر (maqayis)؛ دبار اسم يوم أحسبه يوم الأربعاء (jamhara)؛ دبار اسم يوم الأربعاء من أسمائهم القديمة (sihah)؛ دبار يوم الأربعاء (tahdhib)؛ سمي يوم الأربعاء في الجاهلية دبارا (mufradat)
- **B021** denizde su basıp açılan yükselti — denizde su yükselince örtülen, çekilince açılan ada benzeri yer
  الدبر قطعة تغلظ في البحر كالجزيرة يعلوها الماء وينضب عنها (jamhara)
- **B022** güreşte özel düşürme tutuşu — güreşte rakibi düşürmeye yarayan özel tutuş
  الدابرة ضرب من أخذ الصرع (maqayis)؛ الدابرة ضرب من الشغزبية في الصراع (sihah;tahdhib)

## ء م ر (root_000051): 79:5 أَمْرًا

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

## ي و م (root_001700): 79:6 يَوْمَ, 79:35 يَوْمَ, 79:46 يَوْمَ

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

## ر ج ف (root_000545): 79:6 تَرْجُفُ, 79:6 ٱلرَّاجِفَةُ

- **B001** şiddetle sarsılıp çalkalanmak — şiddetle sarsılıp çalkalanmak · şiddetli sarsıntı ve çalkantı · yüreğin korkudan çarpıp titremesi · çalkantılı deniz · gök gürültüsünün gökte yankılanması · gök gürültüsünün yinelenen uğultusu
  أصل يدل على اضطراب (maqayis)؛ رجف الشيء يرجف رجفا ورجفانا (ayn;tahdhib)؛ رجف القلب إذا اضطرب من فزع (jamhara)؛ البحر رجاف لاضطرابه (maqayis;sihah)؛ الرعد يرجف رجفا ورجيفا (ayn;tahdhib)؛ الرجف الاضطراب الشديد (mufradat)
- **B002** şiddetli yer sarsıntısı — yerin şiddetle sarsılması · yer sarsıntısı; bir topluluğu yakalayan ceza · şiddetle sarsılan yer veya sarsıntı olayı
  رجفت الأرض (maqayis)؛ رجفت الأرض تزلزلت (ayn)؛ رجفت الأرض إذا زلزلت (jamhara)؛ الرجفة الزلزلة (sihah)؛ كل عذاب أنزل فأخذ قوما فهو رجفة وصيحة وصاعقة (ayn)؛ الرجفة في القرآن كل عذاب أخذ قوما فهو رجفة وصيحة وصاعقة (tahdhib)؛ فأخذتهم الرجفة (mufradat)
- **B003** asılsız haberle kargaşa çıkarmak — kötü ya da asılsız haberleri yayarak karışıklık çıkarmak · haber yoluyla huzursuzluk ve karışıklık çıkarma · karışıklık doğuran asılsız haberler · asılsız haber üreterek halkı huzursuz edenler
  أرجف الناس في الشيء إذا خاضوا فيه واضطربوا (maqayis)؛ أرجف الناس بكذا وكذا إذا خاضوا فيه واضطربوا (jamhara)؛ الإرجاف واحد أراجيف الأخبار (sihah)؛ أرجف القوم إذا خاضوا في الأخبار السيئة وذكر الفتن (tahdhib)؛ يولدون الأخبار الكاذبة التي يكون معها اضطراب في الناس (tahdhib)؛ الإرجاف إيقاع الرجفة إما بالفعل وإما بالقول (mufradat)
- **B004** savaşa hazırlanmak [kalıp] — topluluğun savaşa hazırlanması
  رجف القوم تهيأوا للحرب (ayn)؛ رجف القوم إذا تهيئوا للحرب (tahdhib)

## ت ب ع (root_000175): 79:7 تَتْبَعُهَا

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

## ر د ف (root_000556): 79:7 ٱلرَّادِفَةُ

- **B001** ardından gelme ve izleme — onu izledi ve ardından geldi · peş peşe gelme · geride kalan · size yaklaştı · ardından bir sonuç doğuran iş · birbirinin ardından gelenler
  أصل واحد مطرد يدل على اتباع الشيء (maqayis); فالترادف التتابع (maqayis); كل شئ تبع شيئا فهو ردفه (sihah); ردف لكم أي قرب لكم أو دنا لكم (tahdhib); الرادف المتأخر (mufradat); تعاونوا عليه وترادفوا بمعنى (maqayis;sihah)
- **B002** arkaya bindirme veya arkada binme — arkada binen yolcu · onu arkasına bindirdi · adamın arkasına bindim veya onu arkama bindirdim · arka yolcu taşımayan binek · çekirgelerin çiftleşirken üst üste binmesi · birbirinin ardından gelen veya birbirini arkaya bindirenler
  الرديف الذي يرادفك (maqayis); لا يحمل رديفا (maqayis); الذي يركب خلف الراكب (sihah); أردفته أركبته خلفي (tahdhib); أردفته حملته على ردف الفرس (mufradat); مرادفة الجراد ركوب الذكر الأنثى (maqayis;sihah)
- **B003** arka beden bölümü — kalça ve kıç bölgesi · arka yolcunun oturduğu yer · hurma ağacının gövde çevresindeki çıkıntıları
  سميت العجيزة ردفا (maqayis); الردف الكفل والعجز (sihah); الردف الكفل (tahdhib); ردف المرأة عجيزتها (mufradat); الرداف موضع مركب الردف (maqayis); الروادف رواكيب النخلة (sihah)
- **B004** ardından gelip görevini üstlenme — hükümdarın ardından işlerini yürüten görevliler · hükümdarın yanındaki ikinci görev ve makam · yorulanın yerini alan sürücüler veya yardımcılar
  أرداف الملوك في الجاهلية الذين كانوا يخلفون الملوك (maqayis); الردافة الاسم من إرداف الملوك في الجاهلية (sihah); أرداف الملوك الذين يخلفونهم في القيام بأمر المملكة بمنزلة الوزراء (tahdhib); أرداف الملوك الذين يخلفونهم (mufradat); الردافى الحداة لأنهم إذا أعيا أحدهم خلفه الآخر (maqayis;tahdhib)
- **B005** göksel ve zamansal ardışıklık — karşılığı batarken doğan veya Vega'ya yakın gök cismi · yıldızların birbirinin ardından görünmesi · birbirini izleyen gece ile gündüz
  أرداف النجوم تواليها (maqayis;sihah;tahdhib); الرديف النجم الذي ينوء من المشرق إذا انغمس رقيبه في المغرب (maqayis); الرديف كوكب قريب من النسر الواقع (tahdhib); الردفان الليل والنهار (maqayis;sihah;tahdhib)
- **B006** uyakta ana sesten önceki uzun ses [kalıp] — şiir uyağında ana ünsüzden hemen önceki uzun ses harfi
  الردف في الشعر حرف ساكن من حروف المد واللين يقع قبل حرف الروى (sihah)
- **B007** kişiye ulaşıp onu alma — onu arkadan yakalayıp ele geçirdik
  أتينا فلانا فارتدفناه ارتدافا أي أخذناه أخذا (maqayis); الارتداف الاستدبار أتينا فلانا فارتدفناه أي أخذناه من وراثه أخذا (sihah); أتينا فلانا فارتدفناه أي أخذناه أخذا (tahdhib)

## ق ل ب (root_001248): 79:8 قُلُوبٌ

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

## و ج ف (root_001628): 79:8 وَاجِفَةٌ

- **B001** hızlı yol alma; bineği hızlandırıp yürütme — hızlı yol alma · deve ya da atın hızlı yürümesi · deve ve atlara özgü, daha hızlı bir yürüyüş derecesinin altında kalan hızlı yürüyüş biçimi · deveyi ya da atı hızlandırıp yürütmek · bir yer üzerine at ya da binek sürüp bunları işletmek · bineğin hızla yürütüldüğü gidiş biçimi · atı zayıflayıncaya kadar hızla sürmek
  الوجف سرعة السير (ayn;tahdhib)؛ وجف البعير يجف وجفا ووجيفا (jamhara;sihah;tahdhib)؛ ضرب من سير الإبل والخيل (jamhara;sihah)؛ أوجفت البعير إذا حملته على الوجيف (jamhara)؛ أوجفت البعير أسرعته (mufradat)؛ ما أعملتم (sihah)؛ الوجيف دون التقريب من السير (tahdhib)
- **B002** sarsıntılı hareket; yüreğin çarpıp ürpermesi — sarsılıp düzensiz hareket etmek · sarsıntılı; yürek için çarpan ya da korkuyla ürperen · yürek çarpıntısı
  وجف الشيء أي اضطرب (sihah)؛ قلب واجف (sihah)؛ واجفة شديدة الاضطراب (tahdhib)؛ واجفة خائفة (tahdhib)؛ قلوب يومئذ واجفة أي مضطربة (mufradat)؛ وجيب القلب من الإبدال والأصل الوجيف (maqayis)
- **B003** sevginin gönlü alıp götürmesi [kalıp] — sevginin gönlünü alıp götürmesi
  استوجف الحب فؤاده إذا ذهب به (tahdhib)

## ب ص ر (root_000121): 79:9 أَبْصَٰرُهَا

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

## خ ش ع (root_000412): 79:9 خَٰشِعَةٌ

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

## ق و ل (root_001272): 79:10 يَقُولُونَ, 79:12 قَالُوا۟, 79:18 فَقُلْ, 79:24 فَقَالَ

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

## ECHO ق ل ل (root_001251): for 79:10 يَقُولُونَ, 79:12 قَالُوا۟, 79:18 فَقُلْ, 79:24 فَقَالَ: withheld observed target; not identity

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

## ر د د (root_000555): 79:10 لَمَرْدُودُونَ

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

## ECHO م ر د (root_001413): for 79:10 لَمَرْدُودُونَ: withheld observed target; not identity

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

## ح ف ر (root_000341): 79:10 ٱلْحَافِرَةِ

- **B001** aşağı doğru kazma ve kazının doğrudan sonuçları — toprağı ya da bir şeyi aşağı doğru kazmak · çukur; kazılmış yer · çukur; kazılmış yer · hendek ya da kuyu gibi kazılmış yer · kazıdan çıkarılan toprak · kuyu ya da mezar gibi kazılmış yer · toprak kazmaya yarayan demir araç · toprak kazmaya yarayan demir araç · kazma aracı · bir çöl kemirgeninin yuvasında aşağı doğru kazıp geçitleri karmaşıklaştırması · nehir yatağının kazılma zamanı gelmek
  حفر الشيء وهو قلعه سفلا (maqayis)؛ حفرت الأرض حفرا (maqayis;jamhara;sihah)؛ الحفرة في الأرض والحفر اسم المكان الذي حفر (ayn;tahdhib)؛ الحفر التراب المستخرج من الحفرة (maqayis;sihah;mufradat)؛ كل حديدة حفرت بها الأرض فهي محفرة ومحفار (jamhara)؛ حافر اليربوع محافرة وذلك أن يحفر في لغز من ألغازه فيذهب سفلا (tahdhib)
- **B002** hayvan toynağı — atın ya da başka bir hayvanın toynağı
  حافر الفرس من ذلك كأنه يحفر به الأرض (maqayis)؛ الحافر الدابة (ayn)؛ حافر الفرس وغيره معروف وإنما سمي حافرا لأنه يؤثر في الأرض (jamhara)؛ الحافر واحد حوافر الدابة (sihah)؛ سمي حافر الفرس تشبيها لحفره في عدوه (mufradat)
- **B003** ilk duruma geri dönüş — ilk durum ya da ilk var ediliş hali · geldiği yoldan geri dönmek · yaşlı kişinin güçsüzlük ve bunama haline dönmesi
  الحافرة أي الأمر الأول (maqayis)؛ الحافرة العودة في الشيء حتى يرد آخره على أوله (ayn;tahdhib)؛ مردودون في الحافرة أي في الخلق الأول بعدما نموت (ayn;mufradat)؛ رجع فلان على حافرته إذا رجع على الطريق الذي أخذ فيه (maqayis;jamhara;sihah;tahdhib)؛ رجع الشيخ على حافرته إذا هرم وخرف (maqayis;jamhara;mufradat)
- **B004** işin başında gecikmeden yerine getirme — satış bedelini ayrılmadan peşin almak · bedeli daha ilk sözde peşin almak · karşılaşır karşılaşmaz dövüşmek
  النقد عند الحافر أي لا يزول حافر الفرس حتى تنقدني ثمنه (maqayis)؛ النقد عند الحافر لا تبرح حتى تنقد (ayn;tahdhib)؛ النقد عند حافره أي لا يزول حافره حتى آخذ ثمنه (jamhara)؛ النقد عند الحافرة أي عند أول كلمة (sihah;tahdhib)؛ أقل ما يقع حافر الفرس على الحافرة فقد وجب النقد (tahdhib)؛ لما يباع نقدا (mufradat)
- **B005** dişte aşınma, kök bozulması veya birikinti — dişlerin aşınması, köklerinin bozulması ya da diş taşıyla kaplanması · diş kökleri bozulmak
  الحفر في الفم وهو تآكل الأسنان (maqayis)؛ الحفر ما يلزق بالأسنان من ظاهر وباطن (ayn;tahdhib)؛ في أسنان الرجل حفر وهو نقد واصفرار (jamhara)؛ في أسنانه حفر إذا فسدت أصولها (sihah)؛ الحفر تأكل الأسنان (mufradat)؛ هو أن يحفر القلح أصول الأسنان بين اللثة وأصل السن (tahdhib)
- **B006** tayın diş değiştirme evresine girmesi — tayın süt dişleri düşüp yenileri çıkmaya başlamak
  أحفر المهر للإثناء والإرباع إذا سقط بعض أسنانه لنبات ما بعده (maqayis)؛ أحفر المهر للإثناء والإرباع والقروح إذا ذهبت رواضعه وطلع غيرها (sihah)؛ إحفاره أن يتحرك الثنيتان السفليان والعلييان من رواضعه (tahdhib)؛ أحفر المهر للإثناء والإرباع (mufradat)
- **B007** deve dışında gebeliğin gebe canlıyı zayıflatması — gebelik, gebe canlıyı zayıflatıp güçten düşürmek · zayıflatıp cılızlaştırmak
  ما من حامل إلا والحمل يحفرها إلا الناقة فإنها تسمن عليه (maqayis;sihah)؛ حفره حفرا هزله (sihah)
- **B008** develerin otladığı bir ilkbahar bitkisi — develerin otladığı bir ilkbahar bitkisi · ilkbaharda yetişen belirli bir bitki · develerini bu ilkbahar bitkisinde otlatmak
  الحفراة نبت من نبات الربيع (ayn;tahdhib)؛ الحفرى ضرب من النبات (jamhara)؛ الحفرى نبت (sihah)؛ أحفر الرجل إذا رعى إبله الحفرى (tahdhib)
- **B009** tahıl savurmaya yarayan parmaklı tahta araç — tahılı samandan ayırmaya yarayan parmaklı tahta araç · parmaklı tahta araçla tahılı savurmak
  الحفراة خشبة ذات أصابع تذرى بها الكدوس المدوسة وينقى بها البر (ayn)؛ الحفراة الخشبة ذات الأصابع التي يذرى بها (sihah)؛ الحفراة وهي الرقش الذي تذرى به الحنطة (tahdhib)
- **B010** belirli yer ve kuyu adları — bilinen bir yer adı · bilinen bir yer adı · bilinen yerlerin ya da kuyuların toplu adı
  حفير وحفيرة اسما موضعين (ayn;tahdhib)؛ الحفر والحفير موضعان بين مكة والبصرة (jamhara)؛ الأحفار مواضع معروفة (jamhara)؛ الأحفار المعروفة في بلاد العرب ثلاثة (tahdhib)
- **B011** birinin durumunu araştırıp öğrenmek — birinin durumunu araştırıp öğrenmek
  حفرت ثرى فلان إذا فتشت عن أمره ووقفت عليه (tahdhib)
- **B012** cinsel ilişkide bulunmak — cinsel ilişkide bulunmak
  حفر إذا جامع (tahdhib)
- **B013** bozulmak — bozulmak
  حفر إذا فسد (tahdhib)

## ك و ن (root_001332): 79:11 كُنَّا

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

## ع ظ م (root_001029): 79:11 عِظَٰمًا

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

## ن خ ر (root_001482): 79:11 نَّخِرَةً

- **B001** burundan ses çıkarma — burnundan ses çıkarmak · burundan çıkan hırıltılı ses · burnundan ses çıkaran
  النخير صوت يخرج من المنخرين (maqayis)؛ نخر الحمار بأنفه نخيرا (ayn)؛ نخر الإنسان والحمار وغيرهما نخيرا (jamhara)؛ النخير صوت بالأنف (sihah)؛ النخير صوت من الأنف (mufradat)
- **B002** burun deliği ve burun — iki burun deliği · burun deliği; kimi kullanımlarda bütün burun · burun deliğinin değişik söylenişi · burun; hayvanlarda burnun ön bölümü
  فقيل لخرقي الأنف النخرتان؛ النخرة الأنف نفسه (maqayis)؛ نخرتا الأنف خرقاه؛ والمنخر لجميع الأنف (ayn)؛ المنخر الأنف؛ يسمى المنخر أيضا النخرة والجمع نخر (jamhara)؛ المنخر ثقب الأنف؛ المنخور لغة في المنخر (sihah)؛ حرفا الأنف نخرتاه ومنخراه (mufradat)
- **B003** çürüyüp ufalanma — çürüyüp ufalanmak · çürümüş ve içi boşalmış · çürümüş, ufalanmış · rüzgarın içinden geçtiği oyuk çürük kemik
  الشجرة النخرة والعظم النخر؛ النخر البالي؛ الناخر الذي تدخل فيه الريح وتخرج منه (maqayis)؛ نخر العظم إذا بلي؛ عظاما نخرة وناخرة؛ عود نخر (jamhara)؛ نخر الشيء أي بلي وتفتت؛ الناخر من العظام الذي تدخل الريح فيه (sihah)؛ نخرت الشجرة أي بليت (mufradat)
- **B004** rüzgarın esmesi, sert esişi [kalıp] — rüzgarın esmesi veya sert esişi
  لهبوب الريح نخرة (maqayis)؛ نخرة الريح شدة هبوبها (sihah)؛ نخرة الريح أي هبوبها (mufradat)
- **B005** süt salması burun uyarısına bağlı dişi deve — burnuna dokunulmadan veya burun deliğine parmak sokulmadan sütünü salmayan dişi deve
  النخور الناقة لا تدر حتى تدخل الإصبع في منخرها (maqayis)؛ النخور من النوق التي لا تدر حتى يضرب أنفها؛ حتى تدخل إصبعك في أنفها (sihah)؛ النخور الناقة التي لا تدر أو يدخل الأصبع في منخرها (mufradat)
- **B006** idrar kanalı geniş olan — idrar kanalı geniş olan
  النخوري الواسع الإحليل (maqayis;sihah)؛ شيء يدخله الريح بنخرة (maqayis)
- **B007** orada hiç kimse yok [kalıp] — orada hiç kimse yok
  ما بها ناخر أي أحد يراد بها مصوت (maqayis)؛ ما بها ناخر أي ما بها أحد (sihah)؛ ما بالدار ناخر (mufradat)

## ك ر ر (root_001292): 79:12 كَرَّةٌ

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

## خ س ر (root_000409): 79:12 خَاسِرَةٌ

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

## ز ج ر (root_000624): 79:13 زَجْرَةٌ

- **B001** sertçe engelleme; hayvanı sesle yürütme — sertçe engelleme ve azarlama · azarlayıp engelledi veya sesle uzaklaştırdı · engelledi ya da caydırdı · geri durdu veya vazgeçti · deveyi seslenerek sürdü · tek bir sert sesleniş · bulutları sesle süren melekler · kötü işlerden uzaklaştıran uyarı · gür ve uğultulu ses
  زجرته فانزجر أي نهيته (ayn)؛ زجرت الرجل أو السبع وهو انتهارك إياه (jamhara)؛ الزجر المنع والنهي؛ زجر البعير أي ساقه (sihah)؛ زجرت البعير حتى ثار ومضى؛ للبعير كالحث بلفظ؛ الزجر للإبل والدواب والسباع (tahdhib)؛ الزجر طرد بصوت؛ يستعمل في الطرد تارة وفي الصوت أخرى (mufradat)؛ كلمة تدل على الانتهار؛ زجرت البعير حتى مضى؛ زجرت فلانا عن الشيء فانزجر (maqayis)؛ الزمجرة الصوت والميم فيه زائدة وأصله من الزجر (maqayis)
- **B002** hayvan hareketini iyiye veya kötüye yorma — kuş ve benzeri hayvanların geçişini iyiye veya kötüye yorma · hayvanların görünüş ve geçişinden gelecek için anlam çıkarma · hayvan hareketlerini yorumlayıp geleceği kestiren kişi
  زجر الطير أن يقول الإنسان إذا رأى طائرا أو ظبيا أو نحوه (ayn)؛ زجر الطائر وهو التفاؤل به (jamhara)؛ الزجر العيافة وهو ضرب من التكهن (sihah)؛ الزجر للطير وغيرها التيمن بسنوحها أو التشاؤم ببروحها (tahdhib)
- **B003** iri bir balık türü — iri bir balık türü; kimi anlatımlarda küçük pullu · bu balık türünü bildiren çoğul ad
  الزجر ضرب من السمك عظام صغار الحرشف ويجمع الزجور (ayn)؛ الزجر ضرب من الحيتان عظام (jamhara)؛ الزجر ضرب من السمك عظام والجميع الزجور (tahdhib)
- **B004** görünüşten tanıyıp kokudan yadırgayan; sütünü esirgeyen deve — görünüşten tanıyıp kokudan yadırgayan deve · yavruya burnuyla yakınlık gösterip sütünü vermeyen dişi deve
  الزجور من الإبل التي تعرف بعينها وتنكر بأنفها (maqayis)؛ الزجور من الإبل التي تعرف بعينها وتنكر بأنفها (sihah)؛ الناقة العلوق زجور؛ التي ترأم بأنفها وتمنع درها (tahdhib)
- **B005** sırtı çökmüş veya yaralı; sağrısı ağır deve — omurları çökmüş ya da sırtı yaralı deve · sağrısı ağır olduğu için zor kalkan dişi deve
  الأزجر من الإبل الذي في فقار ظهره انخزال أو من دبر؛ ناقة زجراء وهي التي في وركيها ثقل فلا تكاد تقوم (ayn)

## و ح د (root_001631): 79:13 وَٰحِدَةٌ

- **B001** tek başına ve ayrı olma — tek başına ve ayrı olma · tek başına · tek başına olan · kimsesiz ve tek başına olan · ötekilerden ayrı olarak · yalnız, kimsesiz · tek başına kaldı · öteki tepelerden ayrı duran tepecik · bu konuda yalnız değilim · kendi görüşünde tek kaldı
  أصل واحد يدل على الانفراد (maqayis)؛ الوحد المنفرد (ayn)؛ رجل واحد منفرد (jamhara)؛ الوحدة الانفراد ورجل وحد ووحيد أي منفرد (sihah)؛ الوحدة الانفراد والوحد المفرد (mufradat)
- **B002** bir sayısı, birer birerlik ve tek parça — birer birer, tek tek · bir sayısı · bir; ikisinden biri · on birinci · birlerden oluşan topluluk; tekler · teker teker · bir bütünün tek parçası
  الواحد أول عدد من الحساب (ayn)؛ الواحد أول العدد والأحد مثل الواحد وأحاد أحاد واحد واحد (jamhara)؛ الواحد أول العدد وأحاد ووحاد وموحد والميحاد (sihah)؛ لمبدإ العدد كقولك واحد اثنان (mufradat)
- **B003** övgüde ya da yergide eşi benzeri olmama — kabilesinde eşi olmayan · eşi benzeri olmayan · yergide benzeri olmayan · kötülükte eşi olmayan · çağının eşsizi · çağdaşları arasında eşsiz · benzeri olmayan, eşsiz · eşi benzeri olmayan
  واحد قبيلته إذا لم يكن فيهم مثله ونسيج وحده (maqayis)؛ لا يقارعه في الفضل أحد (ayn)؛ فلان واحد دهره أي لا نظير له وأوحد أهل زمانه (sihah)؛ واحد لعدم نظيره ونسيج وحده وعيير وحده وجحيش وحده (mufradat)
- **B004** Tanrı'nın tek, ortaksız ve bölünmez oluşu ve buna inanma — Tanrı'nın tek ve ortaksız olduğuna inanma · parçalanması ve çoğalması düşünülemeyen tek Tanrı · mutlak anlamda yalnız Tanrı için kullanılan tek nitelemesi · Tanrı'nın tek ve ortaksız oluşu
  التوحيد الإيمان بالله وحده لا شريك له والله الواحد الأحد ذو التوحد والوحدانية (ayn)؛ إذا وصف الله تعالى بالواحد فمعناه هو الذي لا يصح عليه التجزي ولا التكثر (mufradat)
- **B005** ortak bir yönden bir ve aynı sayılma — aynı anlamda veya aynı değerde · tür veya bağlantı bakımından bir olan
  الجلوس والقعود واحد وأصحابك وأصحابي واحد (ayn)؛ واحدا في الجنس أو في النوع وواحدا بالاتصال (mufradat)
- **B006** tek yavru doğurma veya çağının eşsizi kılma [kalıp] — tek yavru doğurdu · onu çağının eşsizi yaptı
  أوحدت الشاة فهي موحد أي وضعت واحدا؛ أوحده الله جعله واحد زمانه (sihah)

## س ه ر (root_000752): 79:14 بِٱلسَّاهِرَةِ

- **B001** uykusuz kalma — uykusuz kalmak, uykusu kaçmak · uykusuz bırakmak · uykusuz kalan kimse · uykusuz kalmış kimse · çok uykusuz kalan, az uyuyan adam · uykusuzluk
  الأرق وهو ذهاب النوم (maqayis)؛ السهر الأرق (sihah)؛ السهر امتناع النوم بالليل (tahdhib)
- **B002** yeryüzünün açık yüzü — yeryüzünün yüzü; geniş düz yer; kıyamet yeri
  للأرض الساهرة سميت بذلك لأن عملها في النبت دائما ليلا ونهارا (maqayis)؛ الساهرة وهي وجه الأرض (sihah)؛ الساهرة وجه الأرض العريضة البسيطة (tahdhib)؛ الساهرة قيل وجه الأرض وقيل أرض القيامة (mufradat)
- **B003** ayın çevresi — ayın örtüsü veya çevresi · ay · yer yüzünün gölgesi · ay tutulunca kendi çevresine girdi · ay sonunun kalan dokuz gecesi
  الساهور غلاف القمر ويقال هو القمر (maqayis)؛ الساهور غلاف القمر (sihah)؛ الساهور ظل الساهرة (sihah)؛ الساهور من أسماء القمر (tahdhib)؛ دخل في ساهوره (tahdhib)؛ ليالي الساهور التسع البواقي من آخر الشهر (tahdhib)
- **B004** burun içindeki iki damar — burun içindeki iki damar · erkeklik organı ve burnu
  الأسهران عرقان في الأنف من باطن (maqayis)؛ الاسهران عرقان في المنخرين (sihah)؛ الأسهران عرقان في الأنف من باطن (tahdhib)؛ أسهراه ذكره وأنفه (tahdhib)؛ الأسهران عرقان في الأنف (mufradat)
- **B005** su gözünün kaynağı [kalıp] — su gözünün aslı ve kaynağı · akan su gözü
  ساهور العين أصلها ومنبع مائها (tahdhib)؛ عين الماء ساهرة إذا كانت جارية (tahdhib)
- **B006** bol sütlü deve [kalıp] — memesinde uzun süre süt tutan ve çok süt veren deve
  يقال للناقة إنها لساهرة العرق وهو طول حفلها وكثرة لبنها (tahdhib)

## ء ت ي (root_000009): 79:15 أَتَىٰكَ

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

## ح د ث (root_000299): 79:15 حَدِيثُ

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

## ن د و (root_001486): 79:16 نَادَىٰهُ, 79:23 فَنَادَىٰ

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

## ECHO ن د ي (root_001487): for 79:16 نَادَىٰهُ, 79:23 فَنَادَىٰ: withheld observed target; not identity

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

## ECHO ن و د (root_001563): for 79:16 نَادَىٰهُ, 79:23 فَنَادَىٰ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## ر ب ب (root_000532): 79:16 رَبُّهُۥ, 79:19 رَبِّكَ, 79:24 رَبُّكُمُ, 79:40 رَبِّهِۦ, 79:44 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 79:16 رَبُّهُۥ, 79:19 رَبِّكَ, 79:24 رَبُّكُمُ, 79:40 رَبِّهِۦ, 79:44 رَبِّكَ: withheld observed target; not identity

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

## و د ي (root_001637): 79:16 بِٱلْوَادِ

- **B001** idrar sonrası ince akıntı ve erkek hayvanda organın dışarı çıkıp dikleşerek sıvı damlatması — idrar sonrası gelen ince akıntı · idrar sonrası gelen ince akıntı · akmak veya ince akıntı çıkarmak · atın çiftleşmek ya da işemek için cinsel organını dışarı çıkarması · eşeğin cinsel organının dikleşmesi ve sıvı damlatması
  ودى الفرس ليضرب أو يبول إذا أدلى (maqayis); الودى ماء يخرج من الإنسان كالمذي (maqayis); ودى الدابة والرجل يدي وديا وهو الماء الرقيق الذي يخرج مع البول (jamhara); الودي بالتسكين ما يخرج بعد البول (sihah); ودى الفرس إذا أخرج جردانه (tahdhib); ودى أي سال ومنه الودي لخروجه وسيلانه (tahdhib); ودى الحمار فهو واد إذا أنعظ (tahdhib); ودى بمعنى قطر منه الماء عند الإنعاظ (tahdhib)
- **B002** öldürülen kişi için mali karşılık ve bu karşılığı ödeme ya da alma — öldürülen kişi için hak sahibine ödenmesi gereken mali karşılık · öldürülen kişinin mali karşılığını hak sahibine ödemek · öldürülen kişi için ödenen mali karşılığı almak
  وديت الرجل أديه دية (maqayis); ووديت القتيل أديه دية إذا أعطيت ديته (jamhara); الدية واحدة الديات وديت القتيل أديه دية إذا أعطيت ديته (sihah); واتديت أي أخذت ديته (sihah); ودى فلانا إذا أدى ديته إلى وليه (tahdhib)
- **B003** küçük hurma fidanı ve bu fidanların topluluğu — küçük hurma fidanları · bir küçük hurma fidanı · küçük hurma fidanları
  الودى صغار الفسلان (maqayis); والودي الفسيل والواحد ودية (jamhara); الودى على فعيل صغار الفسيل الواحدة ودية (sihah); هو الودي لصغار النخل واحدتها ودية (tahdhib); تجمع الودية ودايا (tahdhib)
- **B004** ölmek veya yok olmak; zaman ya da ölüm tarafından yok edilmek — ölmek veya yok olmak · zamanın ya da ölümün birini yok etmesi · ölme veya yok olma · ölmüş veya yok olmuş · yok oluş için az kullanılan ad
  وأودى الشيء يودي إيداء إذا تلف وأودى به الدهر (jamhara); أودى فلان أي هلك فهو مود (sihah); أودى الرجل إذا هلك (tahdhib); أودى به المنون أي أهلكه (tahdhib); اسم الهلاك من ذلك الودى وقلما يستعمل والمصدر الحقيقي الإيداء (tahdhib)
- **B005** yükseltiler arasında sel sularına yol veren vadi — yükseltiler arasında sel sularına yol veren vadi · vadi sözünün son sesi düşmüş biçimi · vadiler
  والوادي معروف وأحسبه راجعا إلى هذا لسيلان الماء فيه (jamhara); والوادي معروف والجمع الأودية (sihah); ومنه الوادي (tahdhib); والوادي كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل أو منفذا (tahdhib)
- **B006** yavrunun emmesini önlemek için devenin meme uçlarına bağlanan tahta parçaları — yavrunun emmesini önlemek için devenin meme uçlarına bağlanan tahta parçaları · emme önleyici takımın tek bir tahta parçası · devenin meme uçlarını iki tahta parçayla bağlamak
  التوادي الخشبات التى تشد على خلف الناقة إذا صرت الواحدة تودية (sihah); والتوادي الخشبات التي تصر بها أطباء الناقة لئلا يرضعها الفصيل وقد وديت الناقة بتوديتين (tahdhib)

## ق د س (root_001206): 79:16 ٱلْمُقَدَّسِ

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

## ط و ي (root_000960): 79:16 طُوًى

- **B001** katlayıp iç içe geçirmek ve kıvrımlı katlar oluşturmak — bir şeyi katlayıp bölümlerini üst üste getirmek · bir katlama veya katlama biçimi · kıvrılıp dolanmak · ipliğin üzerine sarıldığı araç · kıvrımlar, katlar ve yağ tabakaları
  طويت الصحيفة أطويها طيا؛ طويتها طية واحدة؛ ضرب من الطي (ayn)؛ انطوى يقال للحية وما يشبهها؛ المطوى شيء تطوى عليه المرأة غزلها؛ أطواء الناقة طرائق شحم؛ مطاوي الحية والأمعاء والشحم والبطن والثوب أطواؤها وغضونها (ayn)؛ وكذلك الثوب إذا ثنى بعضه على بعض (jamhara)؛ طويت الشئ طيا فانطوى؛ وتطوت الحية أي تحوت؛ أطواء الناقة طرائق شحمها (sihah)؛ طويت الشيء طيا وذلك كطي الدرج (mufradat)؛ أصل صحيح يدل على إدراج شيء حتى يدرج بعضه في بعض؛ طويت الثوب والكتاب طيا؛ أطواء الناقة وهي طرائق شحم جنبيها (maqayis)
- **B002** mesafeyi aşarak kapatmak veya uzaklığı yakın etmek — araziyi, çölü veya ülkeleri aşmak · uzaklığı yakın etmek
  طوى الله لك البعد أي قربه؛ فلان يطوي البلاد أي يقطعها بلدا عن بلد (ayn)؛ طوى الأرض يطويها طيا إذا قطعها (jamhara)؛ ومنه طويت الفلاة (mufradat)
- **B003** ömrü geçirip sona erdirmek [kalıp] — ömrünü geçirip sona erdirmek
  طوى الله عمر الميت (maqayis)؛ ويعبر بالطي عن مضي العمر؛ طوى الله عمره؛ والسماوات مطويات بيمينه يصح أن يكون من الأول وأن يكون من الثاني والمعنى مهلكات (mufradat)
- **B004** kuyuyu taşla örmek ve taşla örülmüş kuyu — taşla örülmüş kuyu · kuyuyu taşla örmek
  الطوي البئر المطوية؛ والطي فيها طي الحجارة (ayn)؛ وطوى الركي بالحجارة؛ ولا يسمى الركي طويا حتى تطوى بالحجارة (jamhara)؛ والطوي البئر المطوية (sihah)؛ والطوي البئر المطوية (maqayis)
- **B005** içte taşınan niyet ve yönelinen hedef — niyet, amaçlanan yer veya iç düşünce
  الطية تكون منزلا وتكون منتوى؛ مضى فلان لطيته أي لنيته التي انتواها؛ حوشي الطيات أي بعيد الهمة (ayn)؛ والطية النية؛ الطية تكون منزلا وتكون منتأى؛ مضى لطيته أي لنيته التي انتواها؛ بعدت عنا طيته؛ طية بعيدة أي شاسعة؛ والطوية الضمير (sihah)
- **B006** çekip gitmek veya dostluğu kesip yüz çevirmek [kalıp] — çekip gitmek ya da dostluğu kesip yüz çevirmek
  طوى فلان كشحه أي ذهب لوجهه (ayn)؛ فلان طوى كشحه إذا أعرض بوده (sihah)؛ لمن مضى على وجهه طوى كشحه؛ إذا مضى وغاب عنه فكأنه أدرج (maqayis)
- **B007** sırrı veya öğüdü açıklamayıp saklamak [kalıp] — sırrı ya da öğüdü saklamak
  وطوى عني نصيحته أي كتمها (ayn)؛ وطوى السر دوني إذا كتمه (jamhara)
- **B008** açlık, aç kalma ve karın çöküklüğü — açlık ve açlıktan karın çökmesi · günü aç geçirmek veya bilerek aç kalmak · açlıktan ya da yaradılıştan karnı çökük
  طوى فلان نهاره جائعا يطوي طوى فهو طاو؛ والطيان الطاوي البطن؛ أبيت على الطوى (ayn)؛ رجل طاوي البطن شديد الطوى؛ رجل طيان إذا كان طاوي البطن من خلقة (jamhara)؛ والطوى الجوع؛ طوي بالكسر يطوى طوى فهو طاو وطيان؛ طوى بالفتح يطوي طيا إذا تعمد ذلك؛ طوي البطن أي ضامر البطن (sihah)؛ والطيان الطاوي البطن؛ إذا جاع وضمر صار كالشيء الذي لو ابتغي طيه لأمكن؛ فإن تعمد للجوع قال طوى يطوي طيا؛ أدرج الأوقات فلم يأكل فيها (maqayis)
- **B009** dağ, vadi, yer veya arazi adı — dağ, vadi, yer veya arazi adı · Mekke'de bir yer adı · kutsal vadi ya da kutsal arazi için kullanılan yer adı
  وطوى جبل بالشام ويقال بل طوى واد في أصل الطور (ayn)؛ طوى اسم موضع بالشأم؛ فمن صرفه جعله اسم واد ومكان؛ وذو طوى بالضم موضع بمكة (sihah)؛ إنك بالواد المقدس طوى قيل هو اسم الوادي؛ وقيل هو اسم أرض (mufradat)
- **B010** iki kez kutsama veya iki kez seslenme yorumu — iki kez kutsama ya da seslenme biçiminde yorumlanan tekrar
  طوى مرتين أي قدس؛ ثنيت فيه البركة والتقديس مرتين (sihah)؛ وقيل هو مصدر طويت؛ ومعناه نوديته مرتين (mufradat)
- **B011** düz yüzey, hurma kurutma alanı veya kumluktaki büyük kaya — düz yüzey, hurma kurutma alanı veya kumlukta büyük kaya
  والطاية السطح ومر بد التمر (sihah)؛ غيروا هذا البناء أدنى تغيير فزال المعنى إلى غيره؛ الطاية كلمة صحيحة تدل على استواء في مكان؛ الطاية السطح؛ مربد التمر؛ صخرة عظيمة في أرض ذات رمل (maqayis)

## ذ ه ب (root_000522): 79:17 ٱذْهَبْ

- **B001** altın ve altından bir parça — altın, işlenmemiş altın · altından bir parça
  الذَّهَب معروف (maqayis;jamhara;sihah)؛ الذَّهَب التبر (ayn;tahdhib)؛ القطعة منه ذهبة (maqayis;ayn;sihah;tahdhib)
- **B002** altınla kaplama ve altın kaplı nesne — altınla kaplanmış veya bezenmiş nesne · altınla bezenmiş kayışlar, deriler veya kumaşlar · altınla kaplama · altınla kaplama
  المذاهب سيور تموه بالذهب (maqayis;sihah)؛ كل شيء مموه بذهب فهو مذهب (maqayis;sihah)؛ الشيء المطلي بماء الذهب (ayn;tahdhib)؛ التمويه بالذهب (sihah)
- **B003** altın görünce şaşakalma, gözü kamaşma veya ürkme — altını görünce şaşakalmak, gözü kamaşmak veya ürkmek
  ذهب الرجل إذا رأى معدن الذهب فدهش (maqayis)؛ إذا رأى ذهبا في المعدن فبرق بصره (sihah;tahdhib)؛ فأفزعه (jamhara)
- **B004** kızılına sarılık çalan doru at rengi — kızılına sarılık çalan doru at · kızılına sarılık çalan dişil renk biçimi
  كميت مذهب إذا علته حمرة إلى اصفرار (maqayis)؛ كميت مذهب للذي تعلو حمرته صفرة (sihah;tahdhib)
- **B005** bir biçimde iyi yağmur, öbüründe hafif yağmur — yağmur, özellikle iyi ve yararlı yağmur · hafif, az veya güçsüz yağmurlar
  الذهبة فمطر جود (maqayis)؛ الذهبة المطرة الجودة (ayn;tahdhib)؛ الذهاب مطر خفيف قليل (jamhara)؛ الذهاب الأمطار الضعيفة (tahdhib)؛ الذهبة المطرة (sihah)
- **B006** gitme, geçme ve uzaklaşma — gitmek, geçmek · gitme ve geçme · gitmesini sağlamak veya ortadan kaldırmak · gitme
  ذهاب الشيء مضيه (maqayis)؛ الذهاب والذهوب مصدر ذهبت (ayn)؛ ذهب يذهب ذهابا وذهوبا (jamhara;sihah;tahdhib)؛ الذهاب المرور (sihah)
- **B007** gidilen yol, yer veya zaman; izlenen yöntem ve tutum — yol, gidilen yer veya vakit; gereksinim giderme yeri · çıkış yolları daraldı · iyi veya kötü tutum ve yöntem
  ضاقت عليه مذاهبه أي طرقه (jamhara)؛ مذهب الرجل ممشاه لقضاء الحاجة (jamhara)؛ حسن المذهب وقبيح المذهب أي الطريقة (jamhara)؛ المذهب اسما للموضع ووقتا من الزمان (ayn)؛ موضع الغائط الخلاء والمذهب (tahdhib)؛ ذهب مذهبا حسنا (maqayis;sihah)
- **B008** Yemen'de kullanılan bir ölçü — Yemen halkınca kullanılan bilinen bir ölçü
  الذهب مكيال لأهل اليمن (ayn;jamhara;sihah;tahdhib)؛ الجمع أذهاب ثم أذاهب (ayn;sihah;tahdhib)
- **B009** su kullanımı veya abdestte yinelemeli kuruntu ve abdestte veya başka durumlarda ayartan şeytanın adı — su kullanımı ve abdest sırasında yinelemeli kuşku veya kuruntu · abdestte veya başka durumlarda insanları ayarttığı söylenen şeytanın adı
  المذهب اسم شيطان من ولد إبليس (ayn;tahdhib)؛ به مذهب يعنون به الوسوسة في الماء (sihah)؛ للموسوس به المذهب (tahdhib)؛ هذا الداء الذي يسمى المذهب فما أحسبه عربيا صحيحا (jamhara)

## ط غ ي (root_000937): 79:17 طَغَىٰ, 79:37 طَغَىٰ

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

## ECHO ط غ و (root_000936): for 79:17 طَغَىٰ, 79:37 طَغَىٰ: withheld observed target; not identity

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

## ز ك و (root_000637): 79:18 تَزَكَّىٰ

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

## ه د ي (root_001583): 79:19 وَأَهْدِيَكَ

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

## ECHO ه د د (root_001580): for 79:19 وَأَهْدِيَكَ: withheld observed target; not identity

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

## خ ش ي (root_000413): 79:19 فَتَخْشَىٰ, 79:26 يَخْشَىٰٓ, 79:45 يَخْشَىٰهَا

- **B001** korku duyma — korku; özellikle saygı ve bilgiyle karışan korku · korkmak · korkan erkek · korkan kadın · ondan daha çok korku duydum · bu yer ötekinden daha çok korku verir · onu korkuttu
  الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذاك أي أفزعه (ayn)؛ خشي الرجل يخشى خشية أي خاف فهو خشيان والمرأة خشياء؛ كنت أشد خشية منه؛ هذا المكان أخشى أي أشد خوفا؛ خشاه تخشية أي خوفه (sihah)؛ الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذلك المكان؛ معناها من الآدميين الخوف (tahdhib)؛ الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم (mufradat)؛ يدل على خوف وذعر فالخشية الخوف ورجل خشيان؛ كنت أشد خشية منه؛ هذا المكان أخشى من ذلك أي أشد خوفا (maqayis)
- **B002** bilmek — bildim
  خشيت بأن من تبع الهدى معناه علمت (sihah)؛ فخشينا أي فعلمنا (tahdhib)؛ المجاز قولهم خشيت بمعنى علمت؛ أي علمت (maqayis)
- **B003** istememe ve hoşnutsuzluk [kalıp] — Tanrı'ya yüklenen kullanımda istememe ve hoşnutsuzluk
  فخشينا أن يرهقهما طغيانا وكفرا قال الأخفش معناه كرهنا (sihah)؛ فخشينا عن الله لأن الخشية من الله تعالى معناها الكراهة ومعناها من الآدميين الخوف (tahdhib)
- **B004** kuruyup sertleşmiş veya buruşup niteliğini yitirmiş olma — buruşmuş, düşük nitelikli hurma · hurma ağacı buruşmuş, düşük nitelikli meyve verdi · kuru et
  الخشي وهو اليابس؛ الخشو الحشف من التمر؛ خشت النخلة تخشو إذا أحشفت (sihah)؛ مما شذ عن الباب وقد يمكن الجمع بينهما على بعد الخشو التمر الحشف؛ خشت النخلة تخشو خشوا؛ الخشي من اللحم اليابس (maqayis)

## ر ء ي (root_000531): 79:20 فَأَرَىٰهُ, 79:36 يَرَىٰ, 79:46 يَرَوْنَهَا

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

## ECHO ر و ي (root_000615): for 79:20 فَأَرَىٰهُ, 79:36 يَرَىٰ, 79:46 يَرَوْنَهَا: withheld observed target; not identity

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

## ء ي ي (root_000074): 79:20 ٱلْءَايَةَ

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

## ك ب ر (root_001281): 79:20 ٱلْكُبْرَىٰ, 79:34 ٱلْكُبْرَىٰ

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

## ك ذ ب (root_001290): 79:21 فَكَذَّبَ

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

## ع ص ي (root_001022): 79:21 وَعَصَىٰ

- **B001** buyruğa uymayıp söz dinlemekten çıkma — buyruğa karşı gelmek; söz dinlememek · söz dinlememe; buyruğa karşı gelme · buyruğa aykırı davranış · söz dinlemeyen, buyruğa karşı gelen kimse · boyun eğmeyen, söz dinlemeyen kimse · ona karşı gelmek; sözünü dinlememek · söz dinlemez duruma gelmek; boyun eğmemek · topluluğun birliğini bozup onu bölmek · anlaşmazlık çıkıp birliğin dağılması
  العصيان خلاف الطاعة، وقد عصاه يعصيه عصيا ومعصية (sihah)؛ عصى فلان أميره يعصيه عصيا وعصيانا إذا لم يطعه، وعصى العبد ربه إذا خالف أمره (tahdhib)؛ عصى عصيانا إذا خرج عن الطاعة (mufradat)

## س ع ي (root_000709): 79:22 يَسْعَىٰ, 79:35 سَعَىٰ

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

## س و ع (root_000760): 79:42 ٱلسَّاعَةِ (also echo for 79:22 يَسْعَىٰ, 79:35 سَعَىٰ)

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

## ح ش ر (root_000324): 79:23 فَحَشَرَ

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

## ع ل و (root_001042): 79:24 ٱلْأَعْلَىٰ

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

## ء خ ذ (root_000018): 79:25 فَأَخَذَهُ

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

## ء ل ه (root_000047): 79:25 ٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 79:25 ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ن ك ل (root_001554): 79:25 نَكَالَ

- **B001** bağ, bağlama ya da hedefinden uzaklaştırma yoluyla engelleme — köstek, bağ, gem demiri veya engelleyici araç · köstekler ve bağlar · birini amacından veya bir nesneyi yerinden uzaklaştırmak · yöneldiği şeyden geri itilemez · onu bağladı
  أصل صحيح يدل على منع وامتناع، وأصل ذلك النكل القيد، وجمعه أنكال، والنكل حديدة اللجام (maqayis)؛ النكل والنكل ضرب من اللجم والقيود وكل شيء ينكل به غيره فهو نكل (ayn)؛ النكل بالكسر القيد، والنكل أيضا حديدة اللجام، النكل لجام البريد (sihah)؛ الأنكال قيود من نار، والنكل القيد، والنكل اللجام، لجام البريد، أنكلت الرجل عن حاجته، وأنكلت الحجر عن مكانه، لا تنكل أي لا تدفع (tahdhib)؛ نكلته قيدته، والنكل قيد الدابة وحديدة اللجام لكونهما مانعين، والجمع الأنكال (mufradat)
- **B002** korku veya güçsüzlükle geri durma, yeminden kaçınma — korku, güçsüzlük veya yetersizlik yüzünden geri durmak · korkak ve güçsüz kimse · yeminden kaçınma
  نكل عنه نكولا ينكل؛ وهو ناكل عن الأمور ضعيف عنها (maqayis)؛ نكل الرجل عن صاحبه إذا جبن عنه؛ ونكل عن اليمين حاد عنه والنكول عن اليمين الامتناع منها (ayn)؛ نكل عن العدو وعن اليمين أي جبن، والناكل الجبان الضعيف (sihah)؛ نكل الرجل عن الأمر ينكل نكولا إذا جبن عنه (tahdhib)؛ نكل عن الشيء ضعف وعجز (mufradat)
- **B003** cezalandırılanı tekrardan, başkalarını benzerinden caydıran ibretlik ceza — kişiyi durduran veya yıldıran şey · ibret olsun diye cezalandırmak · başkalarına ibret olan caydırıcı ceza · kişiyi cezalandırıp caydırmaya yarayan araç
  رماه بما ينكله؛ نكلت به تنكيلا، ونكلت به نكالا، فعل به ما يمنعه من المعاودة ويمنع غيره من إتيان مثل صنيعه؛ المنكل الشيء الذي ينكل بالإنسان (maqayis)؛ النكال اسم لما جعلته نكالا لغيره إذا بلغه أو رآه خاف أن يعمل عمله (ayn)؛ نكل به تنكيلا إذا جعله نكالا وعبرة لغيره، والمنكل الذي ينكل بالإنسان (sihah)؛ النكال اسم لما جعلته نكالا لغيره إذا رآه خاف أن يعمل عمله؛ نكلت بفلان إذا عاقبته في جرم أجرمه عقوبة تنكل غيره عن ارتكاب مثله؛ جعلنا هذه الفعلة عبرة ينكل أن يفعل مثلها فاعل (tahdhib)؛ نكلت به إذا فعلت به ما ينكل به غيره، واسم ذلك الفعل نكال (mufradat)
- **B004** güçlü, deneyimli kişi veya güçlü ve deneyimli at üzerindeki usta binici — güçlü ve deneyimli at üzerindeki güçlü, deneyimli binici · güçlü, deneyimli ve rakibini alt edebilen adam · kötülükte güçlü ve atılgan olmak
  إن الله تعالى يحب النكل على النكل؛ الرجل القوي المجرب على الفرس القوي المجرب؛ وليس هو من الأصل الذي ذكرناه (maqayis)؛ إن الله يحب النكل على النكل يعني الرجل القوي المجرب على الفرس القوى المجرب (sihah)؛ النكل على النكل: الرجل القوي المجرب المبدىء المعيد على الفرس المجرب المبدىء المعيد؛ رجل نكل ونكل ومعناه قريب من التفسير الذي في الحديث؛ فلان نكل شر أي قوي عليه (tahdhib)؛ إن الله يحب النكل على النكل أي الرجل القوي على الفرس القوي (mufradat)

## ء خ ر (root_000019): 79:25 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ء و ل (root_000067): 79:25 وَٱلْأُولَىٰٓ

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

## ECHO و ل ي (root_001684): for 79:25 وَٱلْأُولَىٰٓ: withheld observed target; not identity

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

## ع ب ر (root_000974): 79:26 لَعِبْرَةً

- **B001** bir yandan öbür yana geçme ve buna bağlı geçiş öğeleri — ırmağı geçmek · ırmak kıyısı ya da öte yan · geçiş yeri ya da geçiş aracı · ırmak geçiş teknesi · yoldan geçen kişi ya da yolcu · ölmek; yaşam yolunu geçmiş sayılmak · kullanımda geçerli dil biçimi
  أصل صحيح واحد يدل على النفوذ والمضي في الشيء (maqayis)؛ عبرت النهر عبورا (maqayis;ayn;sihah;tahdhib)؛ العبر شاطئ النهر وهما عبران (jamhara)؛ المعبر شط نهر هيء للعبور (maqayis;ayn;tahdhib)؛ المعبرة سفينة يعبر عليها النهر (ayn;tahdhib)؛ رجل عابر سبيل أي مار (maqayis;ayn;sihah)؛ عابر سبيل (mufradat)؛ عبر القوم أي ماتوا (sihah;tahdhib)
- **B002** düşün görünür içeriğinden örtük anlamını çıkarma — düşü yorumlamak · düş yorumu · düşünü yorumlatmak için birine anlatmak
  عبر الرؤيا يعبرها عبرا وعبارة ويعبرها تعبيرا إذا فسرها (maqayis)؛ عبر يعبر الرؤيا تعبيرا (ayn)؛ عبرت الرؤيا أعبرها وعبرتها تعبيرا والاسم العبارة (jamhara)؛ عبرت الرؤيا أعبرها عبارة فسرتها (sihah)؛ إن كنتم للرؤيا تعبرون (tahdhib;mufradat)؛ العابر الذي ينظر في الكتاب فيعبره أي يعتبر بعضه ببعض حتى يقع فهمه عليه (tahdhib)؛ التعبير مختص بتعبير الرؤيا وهو العابر من ظاهرها إلى باطنها (mufradat)
- **B003** düşünceyi sözle aktarma ve metni içten kavrama — sözü iyi aktarış · birinin söyleyemediğini onun adına dile getirmek · kitabı içinden okuyup düşünmek
  عبرت عن فلان تعبيرا إذا عي بحجته فتكلمت بها عنه (maqayis;ayn;tahdhib)؛ رجل حسن العبارة إذا كان حسن الأداء لما يسمع (jamhara)؛ عبرت الكتاب أعبره عبرا إذا تدبرته في نفسك ولم ترفع به صوتك (sihah;tahdhib)؛ اللسان يعبر عما في الضمير (sihah)؛ العبارة مختصة بالكلام العابر الهواء من لسان المتكلم إلى سمع السامع (mufradat)
- **B004** gözlenen durumdan karşılaştırmayla sonuç ve ders çıkarma — ders çıkarılacak olay ya da belirti · gözleyip karşılaştırarak ders çıkarmak
  العبرة الاعتبار لما مضى (ayn)؛ العبرة ما اعتبرت به من الآيات (jamhara)؛ فاعتبروا يا أولي الأبصار أي تدبروا وانظروا (tahdhib)؛ العبرة الاعتبار بما مضى (tahdhib;maqayis)؛ الاعتبار والعبرة بالحالة التي يتوصل بها من معرفة المشاهد إلى ما ليس بمشاهد (mufradat)؛ اعتبرت الشيء فكأنك نظرت إلى الشيء فجعلت ما يعنيك عبرا لذاك (maqayis)
- **B005** üzüntüyle gözyaşının birikip akması — gözyaşının akışı ya da gözyaşı · ağlamalı bir üzüntü yaşamak · gözleri yaşarmak · gözü yaşartan şey
  عبرة الدمع جريه والدمع أيضا نفسه عبرة (maqayis;ayn;tahdhib)؛ عبر فلان يعبر عبرا من الحزن وهو عبران والمرأة عبرى وعبرة (maqayis;ayn)؛ استعبر إذا جرت عبرته (maqayis;ayn;sihah)؛ العبرة تردد البكاء في الصدر وربما قيل لتردد الدمع في العين عبرة (jamhara)؛ العبرة بالفتح تحلب الدمع (sihah)؛ رأى فلان عبر عينيه أي ما يسخن عينيه (sihah;tahdhib)؛ عبر العين للدمع والعبرة كالدمعة (mufradat)
- **B006** uzun yolculukları sürdürecek güç ve dayanıklılık — uzun yolculuklara dayanıklı dişi deve · yolculuğa dayanıklı deve ya da develer · hızlı dişi deve
  ناقة عبر أسفار لا يزال يسافر عليها (maqayis;ayn)؛ ناقة عبر سفر إذا كانت قوية عليه (jamhara)؛ جمل عبر أسفار وجمال عبر أسفار وناقة عبر أسفار الذي لا يزال يسافر عليها (sihah)؛ فلان عبر أسفار إذا كان قويا على السفر (tahdhib)؛ العبار الإبل القوية على السير (tahdhib)؛ ناقة عبر أسفار (mufradat)؛ العبسرة الناقة السريعة والسين في ذلك زائدة وإنما هو من ناقة عبر أسفار (maqayis-routing)
- **B007** ırmak kıyısında yetişen iri ağaç ya da iri dikenli çalı — ırmak kıyısında yetişen iri ağaç; kimi kullanımda iri dikenli çalı
  العبري ضرب من السدر ويقال العبري الطويل من السدر الذي له سوق والضال ما صغر منه (ayn)؛ العبري السدر الذي ينبت على شاطئ الأنهار والضال ما نبت في السفوح وغيرها (jamhara)؛ العبري ما نبت من السدر على شطوط الأنهار وعظم (sihah)؛ العبري من السدر ما كان على شطوط الأنهار (tahdhib)؛ يقال للسدر وما عظم من العوسج العبري (tahdhib)؛ العبري ما ينبت على عبر النهر (mufradat)؛ ضرب من السدر عبري وإنما يكون كذلك إذا نبت على شطوط الأنهار (maqayis)
- **B008** Samanyolu'nu geçtiği söylenen belirli yıldız — Samanyolu'nu geçtiği söylenen yıldız
  الشعرى العبور نجم خلف الجوزاء (ayn)؛ الشعرى العبور سميت بذلك لأنها عبرت المجرة (jamhara)؛ الشعرى العبور إحدى الشعريين وهي التي خلف الجوزاء سميت بذلك لأنها عبرت المجرة (sihah)؛ الشعرى العبور سميت عبورا لأنها عبرت المجرة (tahdhib)؛ الشعرى العبور سميت بذلك لكونها عابرة (mufradat)
- **B009** paraları tek tek ya da ayrımdan sonra tartma; paraları çıkarma — paraları birer birer tartmak · paraları ayırdıktan sonra topluca tartmak · paraları dışarı çıkarmak
  عبرت الدنانير تعبيرا وزنتها دينارا دينارا (ayn;maqayis)؛ تعبير الدراهم وزنها جملة بعد التفاريق (sihah)؛ عبرت الدنانير تعبيرا إذا وزنتها دينارا دينارا (tahdhib)؛ لقد أسرعت استعبارك الدراهم أي استخراجك إياها (tahdhib)
- **B010** kesme ya da azaltma yapılmadan tam bırakılma — koyunların yününü bir yıl kırkmadan bırakmak · sünnet edilmemiş oğlan · cinsel organına kesim uygulanmamış kız · damızlık olması için yünü kırkılmamış koç · kılı yıllarca kırkılmamış teke · tüyleri tam bırakılmış ok
  كبش معبر إذا لم يجز صوفه ليستفحل (jamhara)؛ غلام معبر لم يختن (jamhara;sihah;tahdhib)؛ أعبرت الغنم إذا تركتها عاما لا تجزها (sihah;tahdhib)؛ جارية معبرة لم تخفض (sihah)؛ سهم معبر موفر الريش (sihah)؛ المعبر من الجمال الكثير الوبر والمعبر من الغلمان الذي لم يختن وما أدري ما وجه القياس في هذا (maqayis)؛ المعبر التيس الذي ترك عليه شعره سنوات فلم يجز (tahdhib)؛ العبر من الناس القلف واحدهم عبور (tahdhib)
- **B011** safran ya da safranlı kokulu madde karışımı — koku maddesi; safran ya da safranlı koku karışımı
  العبير ضرب من الطيب (ayn)؛ العبير ضرب من الطيب واختلف فيه أهل اللغة فقال قوم هو الزعفران بعينه وقال آخرون بل هو أنواع من الطيب تخلط (jamhara)؛ العبير أخلاط تجمع بالزعفران وقال أبو عبيدة العبير عند العرب الزعفران وحده (sihah)؛ العبير عند أهل الجاهلية الزعفران (tahdhib)؛ العبير ضرب من الطيب (tahdhib)؛ من هذا الشاذ العبير قال قوم هو الزعفران وقال قوم هي أخلاط طيب (maqayis)
- **B012** sayıca ya da miktarca çok olma — herhangi bir şeyin çoğu · çok kişinin bulunduğu oturum
  مجلس عبر كثير الأهل (jamhara)؛ العبر بالضم الكثير من كل شيء (sihah)؛ العبر أيضا الكثير في كل شيء (tahdhib)
- **B013** kaynağa göre yaşı ya da iriliği belirlenen dişi koyun — kaynağa göre belirli yaşta ya da irilikte dişi koyun
  العبور في بعض اللغات الجذعة من الغنم أو أصغر منها (jamhara)؛ العبور من الغنم فوق العظيم من إناث الغنم يقال لي نعجتان وثلاث عبائر (tahdhib)

## ش د د (root_000782): 79:27 أَشَدُّ

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

## خ ل ق (root_000434): 79:27 خَلْقًا

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

## س م و (root_000745): 79:27 ٱلسَّمَآءُ

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

## ECHO و س م (root_001650): for 79:27 ٱلسَّمَآءُ: withheld observed target; not identity

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

## ب ن ي (root_000156): 79:27 بَنَىٰهَا

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

## ر ف ع (root_000582): 79:28 رَفَعَ

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

## س م ك (root_000742): 79:28 سَمْكَهَا

- **B001** yükselme veya yükseltme — yükselmek, yukarı çıkmak · yükseltmek, yukarı kaldırmak · yükselmek, basamak çıkmak · yüksek, yükselmiş · yükseltilmiş · yükseltilmiş gökler · boy, düşey yükseklik
  أصل واحد يدل على العلو (maqayis)؛ يقال سمك إذا ارتفع (maqayis)؛ سمك الله السماء سمكا رفعها (sihah)؛ السماء مسموكة أي مرفوعة (ayn;tahdhib)؛ سنام سامك أي عال (maqayis;ayn;sihah;mufradat)؛ اسمك أي اصعد في الدرجة (maqayis;sihah)؛ السمك القامة من كل شيء بعيد طويل السمك (tahdhib)
- **B002** üst örtü ve taşıyıcı desteği — tavan, çatı · evi, duvarı veya tavanı yükseltip destekleyen araç · çadır evini ayakta tutan sırık · çadır direği veya yapıyı yükseltmeye yarayan araç
  المسماك ما سمكت به البيت (maqayis)؛ السماك ما سمكت به حائطا أو سقفا والسمك يجيء في موضع السقف (ayn)؛ سمك البيت سقفه والمساك عود يكون في الخباء يسمك به البيت (sihah)؛ السقف يسمى سمكا والمسماك عمود من أعمدة الخباء (tahdhib)؛ السماك ما سمكت به البيت (mufradat)
- **B003** belirli yıldız adları ile Balık burcu — Balık burcu · bir yıldız adı · iki yıldızdan oluşan çift · Ay konağı sayılan yıldız · Ay konağı sayılmayan öteki yıldız
  السماك نجم (maqayis;mufradat)؛ السمكة برج في السماء يقال له الحوت (ayn;tahdhib)؛ السماكان كوكبان نيران السماك الأعزل والسماك الرامح (sihah)؛ السماكان نجمان أحدهما الأعزل والآخر الرامح (tahdhib)
- **B004** balık — balık · bir balık · balıklar · balıklar
  ومما شذ عن الباب وباين الأصل السمك (maqayis)؛ السمك في الماء الواحدة سمكة (ayn;tahdhib)؛ السمك من خلق الماء الواحدة سمكة وجمع السمك سماك وسموك (sihah)؛ السمك معروف (mufradat)

## س و ي (root_000766): 79:28 فَسَوَّىٰهَا

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

## غ ط ش (root_001094): 79:29 وَأَغْطَشَ

- **B001** karanlık; gecenin kararması, karartılması veya koyu karanlığı — karanlık ve ona benzer durum · gece karardı · geceyi karanlık kıldı · gece kendiliğinden karardı · çok karanlık gece
  غطش الليل وليل غاطش مطلخم (ayn)؛ أغطش الله سبحانه الليل أي أظلمه وأغطش الليل أيضا بنفسه (sihah)؛ أغطش ليلها أي جعله مظلما (mufradat)؛ أصل واحد صحيح يدل على ظلمة وما أشبهها (maqayis)؛ غطش الليل أظلم والله تعالى أغطشه (maqayis)
- **B002** gözde bulanık ve zayıf görme — gözde bulanık ve zayıf görme · görüşü bulanık kişi · görüşü bulanıklaştı · görüşü bulanık kadın · görmesi zayıf kişi
  رجل أغطش في عينه شبه العمش (ayn)؛ الغطش في العين شبه العمش والرجل أغطش وقد غطش والمرأة غطشاء (sihah)؛ الأغطش وهو الذي في عينه شبه عمش (mufradat)؛ الأغطش وهو الذي في عينه شبه العمش والمرأة غطشاء (maqayis)؛ الغطمش الكليل البصر وهذا مما زيدت فيه الميم والأصل الغطش وهو الظلمة (maqayis)
- **B003** yolu bulunamayan ıssız arazi [kalıp] — yolu bulunamayan ıssız arazi
  فلاة غطشى لا يهتدى لها (sihah)؛ فلاة غطشى لا يهتدى فيها (mufradat)؛ فلاة غطشى لا يهتدى لها (maqayis)
- **B004** bilerek görmezden gelme — bilerek görmezden gelme · bilerek görmezden gelen kişi · adaleti görmezden gelir · adaleti hiçe sayan zalim
  المتغاطش المتعامى عن الشئ (sihah)؛ التغاطش التعامي عن الشيء (mufradat)؛ المتغاطش المتعامي عن الشيء ويقال هو يتغاطش (maqayis)؛ الغطمش الظلوم الجائر والجائر يتغاطش عن العدل أي يتعامى (maqayis)

## ل ي ل (root_001392): 79:29 لَيْلَهَا

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## خ ر ج (root_000400): 79:29 وَأَخْرَجَ, 79:31 أَخْرَجَ

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

## ض ح و (root_000904): 79:29 ضُحَىٰهَا, 79:46 ضُحَىٰهَا

- **B001** güneş yükseldikten sonraki kuşluk vakti — günün yükseldiği erken vakit · kuşluk vakti · günün uzayıp öğleye yaklaştığı kuşluk vakti · güneş doğduktan sonraki ilk kuşluk vakti · kuşluk vaktine girmek veya o vakte kadar kalmak · kuşluk namazını vakit iyice yükselene kadar geciktirmek
  الضحاء امتداد النهار (maqayis); الضحو ارتفاع النهار والضحى فويق ذلك والضحاء ممدود إذا امتد النهار (ayn); الضحو لغة في الضحى (jamhara); ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء (sihah); الضحى انبساط الشمس وامتداد النهار وسمي الوقت به (mufradat)
- **B002** güneşe veya bakışa açık olup görünürleşme — güneşe çıkmak veya güneşin ısısına maruz kalmak · güneşe çık · yol görünür hale geldi · yerleşimin dışta ve açıkta kalan yanı · dışta kalan açık bölgeler veya kenarlar · bunu açıkça ve herkesin gözü önünde yaptı · açıkta ve görünür yer · güneşin neredeyse hiç eksik olmadığı yer · atın bacakları arasındaki bölüm görünür olur · terledim
  ضحى الرجل يضحى إذا تعرض للشمس (maqayis); اضح أي ابرز للشمس (maqayis;ayn); ضحا الطريق إذا بدا وظهر (maqayis;sihah); ضاحية كل بلدة ناحيتها البارزة (maqayis;ayn;sihah;mufradat); فعل ذلك ضاحية أي ظاهرا بينا (maqayis;ayn;sihah); ضحيت عرقت وضحيت للشمس إذا برزت لها (sihah)
- **B003** erken gündüz öğünü ve o vakitte otlatma — kuşluk öğünü · kuşluk öğününü yemek · develer günün başında otlamaya koyuldu · koyunlarını kuşluk vaktinde otlatmak
  للطعام الذي يؤكل في ذلك الوقت ضحاء (maqayis); هم يتضحون أي يتغدون والغداء الضحاء (maqayis); نتضحى أي نتغدى (ayn); تضحت الإبل أخذت في الرعي من أول النهار (ayn); الضحاء أيضا الغداء وهم يتضحون أي يتغدون (sihah); ضحى فلان غنمه أي رعاها بالضحا (sihah); تضحى أكل ضحى والضحاء والغداء لطعامهما (mufradat)
- **B004** bayram gününde dinsel amaçla kesilen hayvan — bayram gününde dinsel amaçla kesilen koyun veya başka hayvan · bayram gününde dinsel amaçla kesilen hayvan · aynı hayvan için kullanılan başka bir ad · dinsel hayvan kesiminin yapıldığı bayram günü veya o gün kesilen hayvanlar · bayram gününde dinsel amaçla bir koyun kesmek
  الضحية معروفة وهي الأضحية (maqayis); أربع لغات أضحية وإضحية وضحية وأضحاة (maqayis;sihah); الضحية الأضحية والجميع الضحايا والأضاحي وهي الشاة يضحي بها يوم الأضحى (ayn); ضحى بشاة من الأضحية وهي شاة تذبح يوم الأضحى (sihah); الأضحية جمعها أضاحي وقيل ضحية وضحايا وأضحاة وأضحى (mufradat)
- **B005** kuşluk aydınlığını andıran parlak açıklık — güneş · bulutsuz ve aydınlık gece · bulutsuz, berrak ve aydınlık gece · bulutsuz ve aydınlık gün · açık kır-boz renkli at · açık kır-boz renkli kısrak
  تسمى الشمس الضحاء (ayn); ليلة إضحيانة وضحياء أي مضيئة لا غيم فيها (maqayis); ليلة ضحياء مضيئة لا غيم فيها وليلة إضحيانة (sihah); يوم إضحيان مضيء لا غيم فيه (ayn); الأضحى من الخيل الأشهب والأنثى ضحياء (sihah); ليلة إضحيانة وضحياء مضيئة إضاءة الضحى (mufradat)
- **B006** yumuşak davranıp acele etmemek — bir işi yumuşak davranarak ve ağırdan alarak yürütmek · acele etme, yavaş ol
  ضحيت عن الأمر إذا رفقت (maqayis;sihah); ضح رويدا أي لا تعجل (sihah)

## ء ر ض (root_000025): 79:30 وَٱلْأَرْضَ

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

## ب ع د (root_000131): 79:30 بَعْدَ

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

## د ح و (root_000462): 79:30 دَحَىٰهَآ

- **B001** bir şeyi yayıp düzlemek — bir şeyi yayıp düzlemek ve genişletmek · yeryüzünü yayıp düzleyerek genişletmek
  دحوت الشيء دحوا بسطته (sihah)؛ الدحو البسط (tahdhib)؛ داحي المدحيات يعني باسط الأرضين السبع وموسعها (tahdhib)؛ دحا الله الأرض أوسعها (tahdhib)؛ أصل واحد يدل على بسط وتمهيد (maqayis)؛ دحا الله الأرض يدحوها دحوا إذا بسطها (maqayis)؛ الطحو وهو كالدحو وهو البسط (maqayis)
- **B002** yüzey boyunca itip yerinden uzaklaştırmak — yağmurun çakılları sürükleyip zemin yüzünden uzaklaştırması · bir şeyi itmek, fırlatmak veya yerinden uzaklaştırmak · taşı elle itip fırlatmak · atın ön ayaklarını yere yakın biçimde öne atarak veya sürüyerek ilerlemesi · çocukların yerde kaydırdığı tahta oyun aracı veya bu araçla oynanan oyun · yerdeki bir çukura doğru kaydırılan yassı oyun taşları · taşı eliyle itip fırlatan oyuncu
  دحا به على وجه الأرض (jamhara)؛ ينفي الحصى عن جديد الأرض (jamhara)؛ دحا المطر الحصى عن وجه الأرض (sihah;maqayis;mufradat)؛ للاعب بالجوز أبعد المدى وادحه أي ارمه (sihah)؛ للفرس مر يدحو دحوا إذا رمى بيديه رميا لا يرفع سنبكه عن الأرض كثيرا (sihah;maqayis)؛ المدحاة خشبة يدحى بها الصبي فتمر على وجه الأرض (tahdhib)؛ دحاه يدحوه إذا دفعه ورمى به (tahdhib)؛ يدحو الحجر بيده أي يرمي به ويدفعه (tahdhib)؛ المداحي أحجار أمثال القرصة يدحون بتلك الأحجار إلى تلك الحفيرة (tahdhib)؛ أزالها عن مقرها (mufradat)؛ جرفها (mufradat)؛ مر الفرس يدحو دحوا إذا جر يده على وجه الأرض (mufradat)
- **B003** deve kuşunun eşerek hazırladığı yumurtlama yeri — deve kuşunun ayağıyla eşip yumurtladığı veya yavru çıkardığı yer · deve kuşunun yumurtlama yeri · gökte yıldız kümeleri arasındaki belirli konak
  أدحي النعام الموضع الذي يبيض فيه والجمع الأداحي (jamhara)؛ مدحى النعامة موضع بيضها وأدحيها موضعها الذي تفرخ فيه (sihah)؛ لأنها تدحوه برجلها ثم تبيض فيه وليس للنعام عش (sihah)؛ الأدحي مبيض النعام (tahdhib)؛ المنزل الذي يقال له البلدة في السماء يقال له الأدحي (tahdhib)؛ أدحى النعام الموضع الذي يفرخ فيه (maqayis)؛ لأنه يدحوه برجله ثم يبيض فيه وليس للنعامة عش (maqayis)؛ منه أدحي النعام وهو أفعول من دحوت (mufradat)
- **B004** geniş yerde uzanmak veya dinlenme yerini eşmek — geniş ve açık bir yerde uzanmak · develerin kolay dinlenme yerlerini eşip çukur izler bırakması
  نام فلان فتدحى أي اضطجع في سعة الأرض (tahdhib)؛ تدحت الإبل إذا تفحصت في مباركها السهلة حتى تدع فيها قراميص أمثال الحفار (tahdhib)
- **B005** topluluk veya ordu önderi — ordu veya topluluğun başındaki önder
  سمت العرب دحية ودحيا (jamhara)؛ دحية بالكسر هو دحية بن خليفة الكلبي (sihah)؛ الدحية رئيس الجند وبه سمي دحية الكلبي (tahdhib)؛ الدحية رئيس القوم وسيدهم بكسر الدال (tahdhib)؛ دحية اسم رجل (mufradat)

## م و ه (root_001458): 79:31 مَآءَهَا

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

## ر ع ي (root_000574): 79:31 وَمَرْعَىٰهَا

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

## ج ب ل (root_000217): 79:32 وَٱلْجِبَالَ

- **B001** dağ — dağ · dağlar
  تجمع الشيء في ارتفاع؛ الجبل معروف (maqayis)؛ اسم لكل وتد من أوتاد الأرض إذا عظم وطال (ayn;tahdhib)؛ الجبل واحد الجبال (sihah)؛ الجبل جمعه أجبال وجبال (mufradat)
- **B002** çok büyük topluluk ya da çok miktarda mal — çok büyük insan topluluğu · büyük insan topluluğu veya geçmiş bir halk · çok miktarda mal · nüfusu çok kalabalık topluluk
  الجبل الجماعة العظيمة الكثيرة (maqayis)؛ الخلق الجبلة وكل أمة مضت فهي جبلة (ayn)؛ الجبل من الناس الجماعة (jamhara;sihah)؛ الجبل الناس الكثير (tahdhib)؛ الجماعة العظيمة جبل (mufradat)؛ مال جبل أي كثير (jamhara;sihah;tahdhib)
- **B003** bedensel irilik ve kalınlık; kalın ve kuru olma — iri ve kalın yapılı kimse · iri ve kalın yapılı · iri ve kalın yapılı kadın · hörgüç veya yaradılıştaki bedensel irilik · yüz derisi ya da baş derisi ve kemikleri kalın · kalın ve kuru şey
  الناقة العظيمة السنام جبلة؛ امرأة جبلة عظيمة الخلق (maqayis)؛ رجل جبل الوجه غليظ بشرة الوجه؛ رجل جبل الرأس غليظ جلد الرأس والعظام (ayn;tahdhib)؛ ذو جبلة إذا كان غليظ الجسم (jamhara;mufradat)؛ شيء جبل غليظ جاف؛ الجبلة السنام؛ امرأة مجبال غليظة الخلق (sihah)
- **B004** doğuştan yapı ve ona göre biçimlenme — doğuştan yapı, yaradılış ve huy · onu yarattı ve belli bir yapıyla donattı · insanı bir işe doğuştan yatkın kıldı · yaratılmış veya belli bir huyda biçimlenmiş kimseler · dağın yaratılıştan gelen yapısının kuruluşu
  الجبلة الخليقة (maqayis)؛ جبلة كل مخلوق توسه الذي طبع عليه؛ جبل الإنسان على هذا الأمر أي طبع عليه (ayn)؛ الجبلة الفطرة؛ خليقته التي خلق عليها (jamhara)؛ جبله الله أي خلقه؛ الجبلة الخلقة (sihah)؛ الجبل الخلق جبلهم الله فهم مجبولون؛ جبل الإنسان على هذا الأمر أي طبع عليه (tahdhib)؛ جبله الله على كذا؛ الطبع الذي يأبى على الناقل نقله (mufradat)
- **B005** kazarken kazılamayan sert zemine ulaşma [kalıp] — yerin sertliği · kazıda kazılamayan sert yere ulaşmak
  حفر القوم فأجبلوا إذا بلغوا مكانا صلبا (maqayis)؛ جبلة الأرض صلابها (ayn)؛ أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه (jamhara)؛ أجبل القوم إذا حفروا فبلغوا المكان الصلب (sihah)
- **B006** dağlara varma veya girme — topluluk dağa veya dağlara vardı · dağların içine girdiler
  أجبل القوم أي صاروا في الجبال وتجبلوا أي دخلوها (ayn;tahdhib)؛ أجبل القوم أي صاروا إلى الجبل (sihah)
- **B007** dokuması, ipliği ve bükümü iyi kumaş [kalıp] — dokuması, ipliği ve bükümü iyi kumaş
  الثوب الجيد النسج والغزل والفتل جيد الجبلة (ayn;tahdhib)؛ ثوب جيد الجبلة (mufradat)
- **B008** kurumuş ağaç — kurumuş ağaç veya ağaçlar
  الجبل الشجر اليابس (ayn;tahdhib)
- **B009** sözün tıkanması veya engelleme — ozanın söz söylemekte zorlanması · engelleme veya alıkonma alanındaki şey
  أجبل الشاعر إذا صعب عليه القول (jamhara)؛ المجبل في المنع (tahdhib)
- **B010** birini bir işi yapmaya zorlamak [kalıp] — birini belirli bir işi yapmaya zorlamak
  اجتبلت فلانا على أمر وجبلته أي أجبرته (tahdhib)
- **B011** geniş ve uzun kum sırtına rastlamak — geniş ve uzun bir kum sırtına rastlamak
  أجبل إذا صادف جبلا من الرمل وهو العريض الطويل؛ أحبل إذا صادف حبلا من الرمل وهو الدقيق الطويل (tahdhib)
- **B012** topluluğun önderi veya bilgini; ileri gelenler — topluluğun önderi ve bilgini · bir topluluğun önderleri ve ileri gelenleri
  الجبل سيد القوم وعالمهم؛ هؤلاء جبال بني فلان؛ أي سادتهم (tahdhib)

## ر س و (root_000564): 79:32 أَرْسَىٰهَا, 79:42 مُرْسَىٰهَا

- **B001** sağlamca yerinde kalmak; sabitlemek — yerinde sabit kaldı · sabitledi, sağlamca yerleştirdi · sabit ve sağlam yerleşmiş · yerinden ayrılmayan, sabit · sağlamca yerleşmiş sabit dağlar · duruşta veya savaşta ayakları sağlam bastı · yerinden ayrılmayan sabit kazan · bulut bir yerde kaldı ve orada devam etti · bir işin sabitlenip yerleşeceği zaman
  رسا الشيء يرسو إذا ثبت (maqayis;ayn;sihah;mufradat)؛ أرسى الجبال أي أثبتها (maqayis;mufradat)؛ رواسي من الجبال الثوابت الرواسخ (sihah)؛ رست قدماه في الموقف والحرب (ayn;sihah)؛ قدر راسية لا تبرح مكانها (ayn)؛ ألقت السحابة مراسيها ثبتت في موضع أو دامت (maqayis;ayn;sihah;mufradat)
- **B002** geminin demirleyip hareketsiz kalması — gemi demirleyip ilerlemez oldu · demirleme; demirleme yeri, zamanı veya demirlenen şey · gemiyi yerinde tutan çapa
  رست السفينة انتهت إلى قرار الماء فبقيت لا تسير (ayn)؛ رست السفينة ترسوا رسوا أي وقفت على اللنجر (sihah)؛ المرساة أنجر يشد بالحبال فيرسل في البحر فيمسك بالسفينة ويرسيها فلا تسير (ayn)؛ المرساة التي ترسى بها السفينة (sihah)؛ مرساها من أجريت وأرسيت، فالمرسى يقال للمصدر والمكان والزمان والمفعول (mufradat)
- **B003** anlatıyı nakletmek, kısmen söylemek veya zihinde pekiştirmek [kalıp] — ondan bir anlatı nakledip aktardı · işin veya anlatının bir bölümünü ona söyledi · anlatıyı kendi zihninde iyice pekiştirdi
  رسوت عنه حديثا أرسوه إذا حدثت به عنه (maqayis)؛ رسوت لفلان من هذا الأمر أو الحديث أي ذكرت له طرفا منه (ayn;sihah)؛ رسوت الحديث أحكمته فيما بينك وبين نفسك (ayn)
- **B004** insanların arasını düzeltip barışı yerleştirmek [kalıp] — insanların arasını düzeltip barışı yerleştirdi
  رسوت بين القوم رسوا إذا أصلحت (maqayis;sihah)؛ رسوت بين القوم أي أثبت بينهم إيقاع الصلح (mufradat)
- **B005** erkek devenin dağılan dişileri çağırıp geri toplaması [kalıp] — erkek deve dağılan dişi grubunu çağırıp geri topladı
  الفحل إذا تفرقت عنه شوله فصاح بها استقرت فيقال رسا بها (maqayis)؛ الفحل من الإبل إذا تفرق عنه شوله فهدر بها وراغت إليه وسكنت قيل رسا بها (ayn)؛ قد رسا الفحل بالشول وذلك إذا قعا عليها (sihah)

## م ت ع (root_001395): 79:33 مَتَٰعًا

- **B001** yararlanma, haz alma ve yarar sağlayan şey — bir şeyden yararlanıp haz almak · yararlanılan ve haz alınan şey · yarar sağlayan ve kullanılan şey
  أصل صحيح يدل على منفعة وامتداد مدة في خير؛ المتعة والمتاع المنفعة (maqayis)؛ المتعة ما تمتعت به (jamhara)؛ المتاع أيضا المنفعة وما تمتعت به، وتمتعت بكذا واستمتعت به بمعنى (sihah)؛ كل شيء ينتفع به ويتبلغ به ويتزود (tahdhib)؛ كل ما ينتفع به على وجه ما فهو متاع ومتعة (mufradat)
- **B002** uzama, yükselme ve kimi bağlamlarda doruğa ulaşma — günün uzayıp yükselmesi ve öğle öncesinde doruğa yaklaşması · kuşluk vaktinin en yüksek düzeyine ulaşması · serabın günün başında uzayıp yükselmesi · bitkinin ilk büyümesinde boy atması · uzama ve yükselme
  متع النهار طال؛ متع النبات؛ متع السراب طال في أول النهار (maqayis)؛ متع النهار متوعا وذلك قبل الزوال، ومتع الضحى إذا بلغ غايته (ayn)؛ متع النهار إذا ارتفع، ومتع السراب إذا ارتفع في أول النهار (jamhara)؛ متع النهار أي ارتفع وطال (sihah)؛ متع النهار متوعا إذا ارتفع حتى بلغ غاية ارتفاعه قبل أن يزول (tahdhib)؛ المتوع الامتداد والارتفاع (mufradat)
- **B003** işe yarayan eşya, mal ve azık — gereksinimlerde kullanılan eşya veya mal · evde gereksinimler için kullanılan eşyalar · az miktardaki azıklar
  المتاع من أمتعة البيت ما يستمتع به الإنسان في حوائجه (maqayis)؛ المتاع السلعة (sihah)؛ كل شيء ينتفع به ويتبلغ به ويتزود، الزاد القليل (tahdhib)؛ لما فتحوا متاعهم أي طعامهم، وقيل وعاءهم (mufradat)
- **B004** boşanan kadına verilen yararlanma desteği [kalıp] — boşanan kadına yararlanması için verilen mal veya destek · boşanma nedeniyle verilen yararlanma desteği
  متعت المطلقة بالشيء لأنها تنتفع به (maqayis)؛ متعة الطلاق لأنه انتفاع (sihah)؛ متعة ومتاعا، بما ينفعها به من ثوب أو خادم أو دراهم أو طعام (tahdhib)؛ المتاع والمتعة ما يعطى المطلقة لتنتفع به مدة عدتها (mufradat)
- **B005** evlilik ilişkisinden yararlanma ve süreli evlilik anlaşması — evlilik bağının kurulması veya eşlerin birleşmesi · belirli para ve süreye bağlı evlilik · belirli bir süre şartına bağlanan evlilik
  نكاح المتعة التي كرهت أحسبها من هذا (maqayis)؛ نكاح المتعة الذي ذكر أحسبه من هذا (jamhara)؛ منه متعة النكاح لأنه انتفاع (sihah)؛ فما استمتعتم به منهن على عقد التزويج؛ المتعة الشرطية (tahdhib)؛ متعة النكاح هي أن الرجل كان يشارط المرأة بمال معلوم إلى أجل معلوم (mufradat)
- **B006** iki kutsal ziyareti birleştirip arada serbest kalma — iki kutsal ziyareti birleştirip arada yasaklardan çıkma · küçük kutsal ziyareti yapıp büyük ziyarete kadar serbest kalma
  متعة الحج لأنه انتفاع (sihah)؛ سمي متمتعا بالعمرة إلى الحج لأنه حل له كل شيء كان حرم عليه في إحرامه (tahdhib)؛ متعة الحج ضم العمرة إليه (mufradat)
- **B007** yaşatıp yararlanacağı süre verme — Tanrı'nın birini yaşatıp yararlanmasını sağlaması · belirli bir sona kadar sağlık içinde yaşatmak
  متع الله به فلانا تمتيعا وأمتعه به إمتاعا أي أبقاه ليستمتع به (maqayis)؛ أمتعه الله بكذا ومتعه بمعنى (sihah)؛ يمتعكم متاعا حسنا إلى أجل مسمى أي يبقيكم بقاء في عافية، ومتع الله فلانا وأمتعه إذا أبقاه وأنسأه (tahdhib)؛ متعناهم إلى حين، نمتعهم قليلا، فأمتعه قليلا (mufradat)
- **B008** alanında üstün, güçlü veya fazla — alanında üstün, güçlü veya fazla · uzun, iyi bükülmüş ve sağlam ip · koyu kızıl veya çok nitelikli mayalı içki · niteliğiyle haz veren ve kızıl olabilen içki · güçlü deve · ağır basan ve fazlalık gösteren tartı
  حبل ماتع جيد، ماتع راجح زائد، وشراب ماتع أحمر (maqayis)؛ الماتع الطويل من كل شيء، حبل ماتع جيد الفتل، نبيذ ماتع شديد الحمرة، وكل شيء جيد فهو ماتع (sihah)؛ الماتع من كل شيء البالغ في الجودة الغاية في بابه، نبيذ ماتع إذا كان أحمر (tahdhib)؛ شراب ماتع قيل أحمر وإنما هو الذي يمتع بجودته، وجمل ماتع قوي، ماتع أي راجح زائد (mufradat)
- **B009** bir şeyi alıp gitme veya birine gerek duymama — bir şeyi alıp onunla gitmek · birine gerek duymamak
  وقد متع به يمتع متعا، لئن اشتريت هذا الغلام لتمتعن منه بغلام صالح أي لتذهبن به، أمتعت عن فلان أي استغنيت عنه (sihah)؛ متعت بالشيء ذهبت به، لتمتعن منه بغلام صالح أي لتذهبن، أمتعت عن فلان أي استغنيت عنه (tahdhib)

## ن ع م (root_001525): 79:33 وَلِأَنْعَٰمِكُمْ

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

## ج ي ء (root_000281): 79:34 جَآءَتِ

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

## ج ي ء (root_000282): 79:34 جَآءَتِ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ط م م (root_000952): 79:34 ٱلطَّآمَّةُ

- **B001** doldurup üstünü düzlemek — bir şeyi toprakla doldurup üstünü düzlemek · kuyuyu toprakla doldurup kapatmak ve düzlemek · kabını doldurmak · doldurulup üstü düzlenmiş
  تغطية الشيء للشيء حتى يسويه به الأرض (maqayis)؛ طم البئر بالتراب ملأها وسواها (maqayis)؛ طم الشيء بالتراب (ayn)؛ طم إناءه أي ملأه (ayn)؛ فطم الركية أي دفنها وسواها (sihah)؛ طم البئر بالتراب وهو الكبس (tahdhib)؛ دفنها حتى يسويها (tahdhib)
- **B002** çoğalıp aşarak bastırmak — çoğalıp yükselerek ötekileri bastırmak · denizin yatağını aşması veya öteki suları bastırması · her şeyi bastıran çok büyük olay · her büyük olayın üstünde daha büyüğü vardır
  طم الأمر إذا علا وغلب (maqayis)؛ الطامة التي تطم على ما سواها أي تزيد وتغلب (ayn)؛ كل شئ كثر حتى علا وغلب فقد طم (sihah)؛ الشيء الذي يكثر حتى يعلو قد طم (tahdhib)؛ الطامة تطم على كل شيء (tahdhib)؛ طم على كذا وسميت القيامة طامة لذلك (mufradat)
- **B003** deniz; ikili kalıpta bütünlük ve çokluk — deniz · denizle toprak veya yaşla kuru gibi karşıt uçların bütünü · çok mal getirmek veya büyük bir işle gelmek
  للبحر الطم (maqayis)؛ الطم البحر والرم الثرى (maqayis)؛ جاءوا بالطمس والرم أي بأمر عظيم (ayn)؛ طم البحر غلب سائر البحور (ayn)؛ والطم البحر (ayn)؛ جاء بالطم والرم أي بالمال الكثير (sihah)؛ الطم الرطب والرم اليابس (tahdhib)؛ الطم هو البحر والرم الثرى (tahdhib)؛ الطم البحر المطموم يقال له الطم والرم (mufradat)
- **B004** saçı kesmek ya da bağlayıp toplamak — saçını kesmek veya saçından bir miktar almak · saçını büküp bağlayarak toplamak · saçının kesim zamanı gelmek · bükülüp bağlanarak toplanmış saç
  طم شعره إذا أخذ منه (maqayis)؛ طم شعره أي جزه (sihah)؛ طم شعره طموما إذا عقصه فهو شعر مطموم (sihah)؛ أطم شعره أي حان له أن يطم أي يجز (sihah)؛ يطم رأسه طما (tahdhib)
- **B005** hafifçe ilerlemek veya yükselip konmak — hafifçe ilerlemek veya kolay bir koşuyla gitmek · kolay koşu; hızlı giden at · atın veya kuşun yükselmesi; kuşun dala konması
  طم الفرس إذا علا وطم الطائر إذا علا الشجرة (maqayis)؛ الرجل يطم في سيره طميما أي يمضي ويخف (ayn)؛ مر يطم طميما أي يعدو عدوا سهلا (sihah)؛ للطائر إذا وقع على غصن قد طمم تطميما (sihah)؛ طم البعير يطم طميما إذا مر يعدو عدوا سهلا (tahdhib)؛ الرجل يطم في سيره طميما وهو مضاؤه وخفته (tahdhib)؛ الطميم الفرس المسرع (tahdhib)
- **B006** yabancı söyleyiş yüzünden açık konuşamama — yabancı söyleyiş etkisiyle açık konuşamayan kimse · yabancı söyleyiş etkisiyle sözlerini açık çıkaramayan · açık söyleyişi engelleyen yabancı dil etkisi
  الطمطم الرجل الذي لا يفصح (maqayis)؛ الطمطم والطمطمي والطمطماني هو الأعجم الذي لا يفصح (ayn)؛ رجل طمطم أي في لسانه عجمة لا يفصح (sihah)؛ الطمطمي والطمطماني هو الأعجم الذي لا يفصح وفي لسانه طمطانية (tahdhib)
- **B007** topluluğun ortası ve toplu kesimi [kalıp] — topluluğun ortası ve bir araya geldiği kesim
  طمة القوم جماعتهم ووسطهم (tahdhib)؛ لقيته في طمة القوم أي في مجتمعهم (tahdhib)

## ذ ك ر (root_000516): 79:35 يَتَذَكَّرُ, 79:43 ذِكْرَىٰهَآ

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

## ء ن س (root_000059): 79:35 ٱلْإِنسَٰنُ

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

## ب ر ز (root_000105): 79:36 وَبُرِّزَتِ

- **B001** görünür hâle gelme veya getirme — gizlilikten çıkıp görünmek · görünür kılmak, ortaya çıkarmak · bir şeyi gösterip belirginleştirmek · görünür; kitap için yayımlanmış · yayımlanmış veya görünür durumdaki kitap
  أصل واحد وهو ظهور الشيء وبدوه؛ برز الشيء فهو بارز؛ أبرزت الشيء أبرزه إبرازا؛ المبروز الظاهر؛ وقال قوم المبروز المنشور (maqayis)؛ برز فلان أي ظهر بعد الخفاء؛ أبرزت الكتاب والشيء أي أظهرته؛ كتاب مبروز مبرز أي منشور (ayn)؛ برزت الشيء تبريزا أي أظهرته وبينته؛ كتاب مبروز أي منشور (sihah)؛ برز أي هو منكشف الشأن ظاهره؛ برز مخفف فمعناه ظهر بعد الخفاء (tahdhib)؛ أن يظهر بذاته؛ أن ينكشف عنه ما كان مستورا منه (mufradat)
- **B002** geniş ve açık arazi — geniş, açık ve örtüsüz arazi · açık araziye çıkmak veya orada bulunmak
  البراز المتسع من الأرض لأنه باد ليس بغائط ولا دحل ولا هوة (maqayis)؛ البراز المكان الفضاء من الأرض البعيد الواسع؛ تبرز فلان خرج إلى البراز (ayn)؛ برز الرجل يبرز بروزا خرج؛ البراز بالفتح الفضاء الواسع؛ الموضع الذي ليس به خمر من شجر ولا غيره؛ تبرز الرجل أي خرج إلى البراز للحاجة (sihah)؛ البراز المكان الفضاء من الأرض البعيد الواسع؛ خرج الإنسان إلى ذلك الموضع قيل قد برز (tahdhib)؛ البراز الفضاء؛ برز حصل في براز (mufradat)
- **B003** saflardan çıkıp teke tek dövüşme — savaşta teke tek çarpışma · rakibinin karşısına savaşmak için çıkmak · karşılıklı olarak saftan çıkıp teke tek dövüşmek
  انفراد الشيء من أمثاله نحو تبارز الفارسين؛ كل واحد منهما ينفرد عن جماعته إلى صاحبه (maqayis)؛ البراز المبارزة من القرنين في الحرب؛ تبارزا؛ بارز القرن مبارزة وبرازا (ayn)؛ البراز المبارزة في الحرب (sihah)؛ المبارزة الحرب؛ البراز أخذ من هذا؛ تبارز القرنان (tahdhib)؛ المبارزة للقتال وهي الظهور من الصف (mufradat)
- **B004** yarışta veya erdemde öne geçme — arkadaşlarını geride bırakmak veya onlardan üstün olmak
  برز الرجل والفرس إذا سبقا وهو من الباب (maqayis)؛ إذا تسابقت الخيل قيل لسابقها قد برز عليها (ayn)؛ برز الرجل أيضا فاق على أصحابه؛ وكذلك الفرس إذا سبق (sihah)؛ إذا تسابقت الخيل قيل لسابقها قد برز عليها (tahdhib)؛ أن يظهر بفضله وهو أن يسبق في فعل محمود (mufradat)
- **B005** insanlar önünde saygın, güvenilir ve iffetli kimse — açık tavırlı, temiz karakterli ve iffetli · insanlar önünde saygın, görüşüne güvenilen ve iffetli kadın
  امرأة برزة أي جليلة تبرز وتجلس بفناء بيتها؛ رجل برز وامرأة برزة يوصفان بالجهارة والعقل؛ رجل برز طاهر عفيف (maqayis)؛ رجل برز أي طاهر الخلق عفيف؛ امرأة برزة موثوق برأيها وفضلها وعفافها (ayn)؛ امرأة برزة أي جليلة تبرز وتجلس للناس؛ رجل برز وامرأة برزة يوصفان بالجهارة والعقل؛ رجل برز أي عفيف (sihah)؛ البرزة من النساء الجليلة التي تظهر للناس ويجلس إليها القوم؛ رجل برز طاهر الخلق عفيف؛ امرأة برزة موثوق برأيها وعفافها (tahdhib)؛ امرأة برزة عفيفة لأن رفعتها بالعفة (mufradat)
- **B006** büyük abdestini yapma örtmecesi — büyük abdestini yapmak · dışkı · ayakyolu, ihtiyaç giderme yeri
  تبرز في التغوط كناية عنه؛ أي خرج إلى براز من الأرض (ayn)؛ البراز كناية عن ثفل الغذاء وهو الغائط؛ المبرز المتوضأ؛ تبرز الرجل أي خرج إلى البراز للحاجة (sihah)؛ قيل في التغوط تبرز فلان كناية أي خرج إلى براز من الأرض (tahdhib)؛ يقال تبرز فلان كناية عن التغوط (mufradat)
- **B007** seyahate çıkmaya kesin karar verme — seyahate çıkmaya kesin karar vermek
  أبرز الرجل إذا عزم على السفر (tahdhib)
- **B008** iki şeyi ayıran engel — iki şeyin arasındaki ayırıcı engel
  البرزخ الحائل بين الشيئين؛ كأن بينهما برازا أي متسعا من الأرض؛ الخاء زائدة (maqayis)
- **B009** belirli bir aslan adı — aslan; köken açıklamasında rakibinin karşısına çıkan aslan
  الهزبر الأسد؛ زيدت فيه الهاء؛ من برز أي إنه مبارز (maqayis)

## ج ح م (root_000225): 79:36 ٱلْجَحِيمُ, 79:39 ٱلْجَحِيمَ

- **B001** şiddetle harlanan büyük ateş ve yakıcı sıcaklık — şiddetle harlanan büyük ateş · çok sıcak yer ya da harlanmış ateş · ateşin harlanıp korunun çoğalması · ateşin güçlü biçimde harlanması · sıkışıp daralmak ya da hırs ve cimrilikten içi yanmak
  عظمها به الحرارة وشدتها والجاحم المكان الشديد الحر وبه سميت الجحيم (maqayis)؛ الجحيم النار الشديدة التأجج والالتهاب (ayn)؛ الجحيم اسم من أسماء النار وكل نار عظيمة في مهواة فهي جحيم (sihah)؛ كل نار توقد على نار جحيم والجمر بعضه على بعض جحيم ورأيت جحمة النار أي توقدها (tahdhib)؛ الجحمة شدة تأجج النار ومنه الجحيم (mufradat)
- **B002** savaşta öldürmenin ve ölüm tehlikesinin doruğa çıkması — savaştaki yoğun öldürme · ölümün iyice şiddetlenmesi · sıkışıp daralmak ya da hırs ve cimrilikten içi yanmak
  الموت جاحم (maqayis;sihah)؛ جاحم الحرب شدة القتل في معركتها (ayn;tahdhib)؛ الحرب لا يبقى لجاحمها التخيل والمراح (tahdhib)
- **B003** göz; dik ve keskin bakış; iri kızıl göz; göz şişliği hastalığı — göz · aslanın iki parlak gözü · gözlerini dikerek açmak · keskin keskin bakmak · iri ve koyu kızıl gözlü · gözleri şişiren bir göz hastalığı
  الجحمة العين بلغة اليمن وجحمتا الأسد عيناه وجحم الرجل إذا فتح عينيه كالشاخص والعين جاحمة والجحام داء يصيب الإنسان في عينيه والأجحم الشديد حمرة العين مع سعتها (maqayis)؛ الجحمة العين بلغة حمير وجحمتا الأسد عيناه بكل لغة والأجحم الشديد حمرة العين مع سعتها (ayn)؛ جحم الرجل فتح عينيه كالشاخص وجحمني بعينيه تجحيما أحد إلي النظر والجحام داء يصيب الانسان فترم عيناه (sihah)؛ الجحمة هي العين بلغة حمير وجحمتا الأسد عيناه بكل لغة والأجحم الشديد حمرة العين مع سعتها والجحام داء معروف (tahdhib)؛ جحمتا الأسد عيناه لتوقدهما (mufradat)
- **B004** yüzün yoğun öfkeden ateş gibi alevlenmesi — yüzü yoğun öfkeden alev alev olmak
  جحم وجهه من شدة الغضب استعارة من جحمة النار وذلك من ثوران حرارة القلب (mufradat)
- **B005** utanma duygusu az olan kişi — utanma duygusu az olan kişi
  الجحم القليلو الحياء (tahdhib)

## ء ث ر (root_000011): 79:38 وَءَاثَرَ

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

## ECHO ث و ر (root_000210): for 79:38 وَءَاثَرَ: withheld observed target; not identity

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

## ح ي ي (root_000383): 79:38 ٱلْحَيَوٰةَ

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

## ح ي و (root_005544): documented alternative for 79:38 ٱلْحَيَوٰةَ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

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

## د ن و (root_000493): 79:38 ٱلدُّنْيَا

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

## ء و ي (root_000070): 79:39 ٱلْمَأْوَىٰ, 79:41 ٱلْمَأْوَىٰ

- **B001** sığınıp barınma ve barındırma — bir eve ya da yere yönelip katılmak · başkasını bir yere alıp barındırmak · sığınılan veya barınılan yer · develerin barındığı yer · toplanma ve birbirine katılma · yaranın iyileşmeye yaklaşması · atları sesle geri çağırmak · aynı anlamda bir yere yönelip katılmak
  أوى الرجل إلى منزله وآوى غيره والمأوى مكان كل شيء يأوي إليه ليلا أو نهارا والتأوي التجمع (maqayis)؛ أوى الإنسان إلى منزله وآويته إيواء وتأوت الطير إذا انضم بعضها إلى بعض (ayn)؛ المأوى كل مكان يأوى إليه شيء ليلا أو نهارا وتأوت الطير تأويا تجمعت (sihah)؛ أوى إلى منزله وآويته أنا إيواء وتأوى الجرح إذا تقارب للبرء وأويت بالخيل إذا دعوتها آووه لتريع إلى صوتك (tahdhib)؛ أوى إلى كذا انضم إليه وآواه غيره (mufradat)؛ ضويت إليه وأويت بمعنى (maqayis)
- **B002** acıyarak içi yumuşama — birine acımak ve onun için içi yumuşamak · birinden acıma ve yumuşaklık istemek · acıma ve iç yumuşaması bildiren eylem adı · acıma ve iç yumuşaması bildiren değişimli eylem adı · acıma ve iç yumuşaması bildiren eylem adı · acıma ve iç yumuşaması bildiren eylem adı
  أويت لفلان إذا رحمته ورثيت له (ayn)؛ أويت لفلان أي أرثي له وأرق (sihah)؛ أويت له إذا رثيت له ونرق له ونشفق عليه واستأويته أي استرحمته (tahdhib)؛ أويت له رحمته وتحقيقه رجعت إليه بقلبي (mufradat)؛ الأصل الآخر أويت لفلان وهو أن يرق له ويرحمه واستأويت فلانا أي سألته أن يأوي لي (maqayis)

## خ و ف (root_000447): 79:40 خَافَ

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

## ق و م (root_001273): 79:40 مَقَامَ

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

## ن ه ي (root_001560): 79:40 وَنَهَى, 79:44 مُنتَهَىٰهَآ

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

## ن ف س (root_001533): 79:40 ٱلنَّفْسَ

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

## ه و ي (root_001609): 79:40 ٱلْهَوَىٰ

- **B001** hava ve boşluk; kalpte boşluk ve yüreksizlik — hava; boşluk veya aralık · kalpleri bomboş, kavrayışsız ve kararsızdır · yüreksiz, korkak ya da akılsız kimse
  الهَواء ممدود هو الجو (ayn)؛ قلبه هَواء (ayn)؛ هَواء الجو ممدود (jamhara)؛ الهَواء ما بين السماء والأرض وكل خال هواء (sihah)؛ الهَواء والخواء واحد (tahdhib)؛ الهَواء كل فرجة بين شيئين (tahdhib)؛ هوى صدره أي خلا (tahdhib)؛ الهوهاءة الضعيف الفؤاد الجبان (tahdhib)؛ الهَواء ما بين الأرض والسماء (mufradat)؛ أصل صحيح يدل على خلو وسقوط (maqayis)؛ أصله الهَواء بين الأرض والسماء سمي لخلوه (maqayis)
- **B002** yukarıdan düşme; yönlü gidiş, derin çukur, düşürme, ölüm ve yas bağlantıları — yukarıdan aşağı düştü veya indi · dipsiz uçurum; ateş azabının adı · derin çukur veya düşme yeri · topluluk derin çukura birbiri ardınca düştü
  هوى الطائر يهوي هويا (ayn)؛ هاوية من أسماء جهنم والهاوية كل مهواة لا يدرك قعرها (ayn)؛ هوى فلان أي مات (ayn)؛ هوى الشيء يهوي إذا خر من علو إلى سفل (jamhara)؛ هوى بالفتح يهوي هويا أي سقط إلى أسفل (sihah)؛ الهاوية اسم من أسماء النار والهاوية المهواة (sihah)؛ هوت أمه فهي هاوية أي ثاكلة (sihah)؛ هويت أهوي هويا إذا سقطت من علو إلى أسفل (tahdhib)؛ المؤتفكة أهوى أي أسقطها (tahdhib)؛ الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة (tahdhib)؛ الهوي سقوط من علو إلى سفل (mufradat)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ هوى الشيء يهوي سقط (maqayis)؛ تهاوى القوم في المهواة سقط بعضهم في إثر بعض (maqayis)
- **B003** eli ya da nesneyi hedefe yöneltmek; yukarıdan atmak — almak için elini ona uzattı · nesneyle işaret etti veya kılıçla vurdu · onu yukarıdan aşağı attı
  أهوى إليه فأخذه أي أهوى إليه يده (ayn)؛ أهوى إليه بيده ليأخذه (sihah)؛ أهويت بالشيء إذا أومأت به (sihah)؛ أهويت له بالسيف (sihah)؛ أهويت له بالسيف وغيره (tahdhib)؛ أهويته إذا ألقيته من فوق (tahdhib)؛ هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء (tahdhib)؛ أهوى إليه بيده ليأخذه كأنه رمى إليه بيده إذا أرسلها (maqayis)
- **B004** benliğin sevgi ve isteğe yönelmesi — benliğin sevgiye veya isteğe yönelmesi · sevdi, gönlü ona yöneldi · ötekinden daha çok sevilen · çeşitli kişisel eğilimlerin izleyicileri
  الهَوَى مقصور الحب (ayn)؛ هوى النفس مقصور (jamhara)؛ الهَوَى مقصور هوى النفس والجمع الأهواء (sihah)؛ هوى بالكسر يهوى هوى أي أحب (sihah)؛ هذا الشيء أهوى إلى من كذا أي أحب إلي (sihah)؛ أفئدة من الناس تهوى إليهم يقول تريدهم (tahdhib)؛ وتهوي إليهم تهواهم (tahdhib)؛ الهَوَى مقصور هوى الضمير (tahdhib)؛ أهل الأهواء واحدها هوى (tahdhib)؛ الهَوَى ميل النفس إلى الشهوة (mufradat)؛ الهوى هوى النفس فمن المعنيين جميعا (maqayis)؛ هويت أهوى هوى (maqayis)
- **B005** ayartıp şaşkınlığa ve isteklerinin peşine sürüklemek [kalıp] — ayartıcı güçler onu yoldan çıkarıp şaşkınlığa sürükledi
  استهوته الشياطين فهو حيران هائم (ayn)؛ استهواه الشيطان أي استهامه (sihah)؛ استهوته الشياطين فهو حيران هائم (tahdhib)؛ كالذي زينت له الشياطين هواه حيران (tahdhib)؛ استهوته الشياطين هوت به وأذهبته (tahdhib)؛ استهوته الشياطين أي حملته على اتباع الهوى (mufradat)
- **B006** uzun bir zaman veya gecenin bir bölümü — uzun bir zaman · gecenin bir bölümü veya dilimi
  الهوي الملي الحين الطويل من الزمان (ayn)؛ مر هوي من الليل أي قطعة منه وكذلك تهواء من الليل (jamhara)؛ مضى هوى من الليل أي هزيع منه (sihah)؛ الهوي الملي الحين الطويل من الزمان (tahdhib)
- **B007** yaranın açılması veya gövdenin boşalıp oyuklaşması [kalıp] — saplama yarası açılıp genişledi · böğür bölgesi zayıflıktan oyuklaşıp açıldı
  هوت الطعنة تهوى فتحت فاها (sihah)؛ هوى بين الكلى والكراكر (sihah)؛ هوت الطعنة إذا فتحت فاها (tahdhib)؛ خلا وانفتح من الضمر (tahdhib)؛ هوى صدره يهوي هواء إذا خلا (tahdhib)؛ هوت الطعنة فتحت فاها تهوى وهو من الهواء الخالي (maqayis)
- **B008** hızlı yönlü ilerleme, atılımlı koşu ve sert yol alma — hızlı veya güçlü ilerleme · yırtıcı kuş hızla daldı veya deve güçlü biçimde koştu · sert ve hızlı yol alma · çeşitli yol alış biçimleri
  الهوي في السير إذا مضى (sihah)؛ المهاواة شدة السير (sihah)؛ الهوي في السير إذا مضى (tahdhib)؛ الهوي السريع إلى أسفل والهوي السريع إلى فوق (tahdhib)؛ هوت العقاب إذا انقضت (tahdhib)؛ هوت الناقة تهوي إذا عدت عدوا أرفع العدو (tahdhib)؛ الهواهي ضروب من السير (tahdhib)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ الهوي ذهاب في انحدار والهوى في الارتفاع (maqayis)؛ شدة السير لما في ذلك من الترامي بالأبدان عند السير (maqayis)
- **B009** karşılıklı inatlaşma ve çekişme — karşılıklı inatlaşma ve çekişme
  المهاواة الملاجة (sihah)؛ المهاواة فذكر أبو عمرو أنها الملاجة (maqayis)؛ أما الملاجة فلأن كل واحد منهما يحب هوى صاحبه (maqayis)
- **B010** asılsız ve boş sözler — asılsız ve boş sözler
  الهواهي الباطل واللغو من القول (sihah)؛ الهواهي الأباطيل (tahdhib)

## ج ن ن (root_000266): 79:41 ٱلْجَنَّةَ

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

## س ء ل (root_000661): 79:42 يَسْـَٔلُونَكَ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 79:42 يَسْـَٔلُونَكَ: withheld observed target; not identity

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

## ن ذ ر (root_001488): 79:45 مُنذِرُ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ل ب ث (root_001339): 79:46 يَلْبَثُوٓا۟

- **B001** bir yerde kalıp orada bulunmayı sürdürmek — bir yerde kalmak ve orada bulunmayı sürdürmek · bir yerde kalma ve ikamet etme · kalıp durma, ikamet etme · kalma ve ikamet etme · bir yerde kalan veya ikamet eden · birinin kalmasını sağlamak veya onu bulunduğu yerde tutmak · birini kalmaya yöneltmek veya onun kalmasını sağlamak
  حرف يدل على تمكث؛ لبث بالمكان أقام (maqayis)؛ لبث بالمكان يلبث (jamhara)؛ اللبث واللباث المكث (sihah)؛ اللبث المكث (tahdhib)؛ لبث بالمكان أقام به ملازما له (mufradat)
- **B002** bir işte duraksayıp ağırdan almak — bir mesele üzerinde durup beklemek ve ağırdan almak · yavaş davranan veya oyalanan · bir ihtiyaç karşısında ağırdan alan · duraksamak, ağırdan almak ve oyalanmak · duraksayan, ağır davranan veya oyalanan
  لي لبثة على هذا الأمر أي توقف (jamhara)؛ ذا لبث (sihah)؛ اللبث البطيء؛ تلبث تلبثا فهو متلبث (tahdhib)

## ع ش و (root_001017): 79:46 عَشِيَّةً

- **B001** karanlık ve görüş açıklığının azalması — gecenin ilk karanlığı ve koyuluğu · gece karanlığı · gecenin başlangıç karanlığı; bilgisizliğin karanlığı
  يدل على ظلام وقلة وضوح في الشيء؛ العشاء وهو أول ظلام الليل (maqayis)؛ عشواء الليل ظلمته (maqayis)؛ مضى من الليل عشوة وهو ما بين أوله إلى ربعه (sihah)؛ أخذت عليهم بالعشوة أي بالسواد من الليل (sihah)؛ العشوة ظلمة الكفر وكلما ركب الإنسان أمرا بجهل لا يبصر وجهه فهو عشوة (tahdhib)
- **B002** gece kılavuz ateşe yönelme — gece ateşe, ışığından yol bularak yönelmek · gecenin başında yerini bildiği ailesine yönelmek · gece ateş ışığıyla yolunu bulmak · gece görünen alev ya da ateş · gece ateş ışığına gelen varlık
  عشوت إلى ناره ولا يكون ذلك إلا أن تخبط إليه الظلام (maqayis)؛ العاشية كل شيء يعشو بالليل إلى ضوء نار (maqayis)؛ عشوته قصدته ليلا (sihah)؛ عشوت إلى النار إذا استدللت عليها ببصر ضعيف (sihah)؛ عشا يعشو إذا أتى نارا للضيافة (tahdhib)؛ العشو إتيانك نارا ترجو عندها هدى أو خيرا (tahdhib)؛ استعشى فلان نارا إذا اهتدى بها (tahdhib)؛ العشوة أيضا الشعلة من النار (tahdhib)؛ عشوت النار قصدتها ليلا (mufradat)؛ النار التي تبدو بالليل عشوة (mufradat)
- **B003** görmezden gelip yüz çevirme — bilmezden gelme · bir işi bilmez ve görmez gibi davranmak · bir şeyden yüz çevirmek veya onu görmezden gelmek · birinin hakkını görmezden gelip ona haksızlık etmek
  التعاشي التجاهل في الأمر (maqayis)؛ عشوت عنه (sihah)؛ ومن يعش عن ذكر الرحمن (sihah)؛ تعاشى الرجل في أمري إذا تجاهل (tahdhib)؛ عشي الرجل عن حق أصحابه إذا ظلمهم (tahdhib)؛ عشي علي فلان ظلمني (tahdhib)؛ عشوت عنها أي أعرضت عنها (tahdhib)؛ عشي عن كذا نحو عمي عنه (mufradat)؛ ومن يعش عن ذكر الرحمن (mufradat)
- **B004** öğle sonrasından gecenin başına uzanan akşam vakti — öğle sonrasından gecenin başına uzanan akşam vakti · bir günün akşamı · gün batımından gecenin koyulaşmasına kadarki vakit; bu vakitteki gece namazı · gün batımı ve gecenin koyulaşma vakitleri · gün batımı namazından sonraki gece namazı · akşamcık; akşam sözünün küçültme biçimi
  العشي آخر النهار (maqayis)؛ فإذا قلت عشية فهو ليوم واحد (maqayis)؛ كل ما كان بعد الزوال فهو عشي (maqayis)؛ العشي والعشية من صلاة المغرب إلى العتمة (sihah)؛ العشاء بالكسر والمد مثل العشي (sihah)؛ العشاءان المغرب والعتمة (sihah)؛ صلاة العشاء هي التي بعد صلاة المغرب (tahdhib)؛ إذا زالت الشمس دعي ذلك الوقت العشي (tahdhib)؛ العشاء من صلاة المغرب إلى العتمة (mufradat)
- **B005** akşam yemeği ve akşam otlatması — günün sonunda veya gecenin başında yenen akşam yemeği · akşam yemeği yemek · birine akşam yemeği yedirmek · gece otlayan develer · develeri gece veya öğleden sonra otlatmak · Akşam otlayan sürü, otlamayanı da harekete geçirir.
  العشاء هو الطعام الذي يؤكل من آخر النهار وأول الليل (maqayis)؛ عشيت الإبل إذا تعشت فهي عاشية (sihah)؛ العواشي هي التي ترعى ليلا (sihah)؛ عشوت أي تعشيت (sihah)؛ عشوته فتعشى أي أطعمته عشاء (sihah)؛ عشيت الإبل إذا رعيتها بعد غروب الشمس إلى ثلث الليل (tahdhib)؛ عشيتها أيضا إذا رعيتها بعد الزوال إلى غروب الشمس (tahdhib)؛ عشيت الرجل إذا أطعمته العشاء (tahdhib)؛ العواشي الإبل التي ترعى ليلا (mufradat)؛ العشاء طعام العشاء (mufradat)
- **B006** körlüğe varmayan, özellikle gece belirginleşen görme zayıflığı — özellikle geceleri görülen görme zayıflığı · görmesi zayıf veya geceleri göremeyen kişi · görmesi zayıf kişiler · görmesi zayıfmış gibi davranmak · görmesi zayıf veya geceleri göremeyen kadın
  العشا مقصور مصدر الأعشى والمرأة عشواء (maqayis)؛ الذي لا يبصر بالليل وهو بالنهار بصير (maqayis)؛ العشا مصدر الأعشى وهو الذي لا يبصر بالليل ويبصر بالنهار (sihah)؛ العشو جمع الأعشى (tahdhib)؛ العشا يكون سوء البصر من غير عمى (tahdhib)؛ يكون الذي لا يبصر بالليل ويبصر بالنهار (tahdhib)؛ عشا يعشو إذا ضعف بصره (tahdhib)؛ العشا ظلمة تعترض في العين (mufradat)؛ رجل أعشى وامرأة عشواء (mufradat)
- **B007** önünü görmeden sonuç düşünmeksizin ilerleme — önünü göremeyip karşısına çıkanlara çarpan dişi deve · körlemesine ve sonucunu düşünmeden davranmak · bir işi ne yaptığını bilmeden yürütmek · birini doğru yönü belli olmayan bir işe sürüklemek
  العشواء من النوق التي كأنها لا تبصر ما أمامها فتخبط كل شيء بيديها (maqayis)؛ في عشواء من أمرهم (maqayis)؛ العشواء الناقة التي لا تبصر أمامها فهي تخبط بيديها كل شيء (sihah)؛ ركب فلان العشواء إذا خبط أمره على غير بصيرة (sihah)؛ العشوة أن تركب أمرا على غير بيات (sihah)؛ يخبط خبط عشواء يضرب مثلا للسادر الذي يركب رأسه ولا يهتم لعاقبته (tahdhib)؛ أوطأته عشوة حمله على أن يركب أمرا غير مستبين الرشد (tahdhib)؛ يخبط خبط عشواء (mufradat)
- **B008** bir şeye yumuşak ve özenli davranma — bir şeye yumuşak ve özenli davranmak
  عشيت عنه أيضا رفقت به (tahdhib)



===== _commentary/v16/work/s079/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s079/reader_a_pilot.md)

# s079 Semantic Channel Discovery

## Parent Channels

### 1. P1 - Tensioned Release and Projected Motion
- Semantic invariant: Stored tension is converted into a directed release whose success is judged at an endpoint.
- Surface relation: indirect; 79:1 `نَّٰزِعَٰتِ`/`غَرْقًا`, 79:4 `سَّٰبِقَٰتِ`, and 79:5 `مُدَبِّرَٰتِ` supply drawing, extremity, precedence, and aftermath.
- Surprising reach: The opening motion can be materialized as a complete archery mechanism and as the preparation of the cords and joined material that hold tension.

#### Subchannel A. Full Draw, Flight, and the Missed Mark
- Reading type: mixed
- Scene or process: An archer pulls the bowstring to its limit, releases into a contest of precedence, and learns the shot's result at or beyond the target.
- Active motifs: bowstring draw (`quranic:root_001489:B002/m01`); full extension of the bow (`quranic:root_001080:B004/m01`); forward precedence (`quranic:root_000671:B001/m01`); wager on the contest (`quranic:root_000671:B002/m01`); arrow passing behind the target (`quranic:root_000458:B018/m01`); fitting a spear-shaft with a point (`quranic:root_000051:B011/m01`)
- Ayah anchors: 79:1 `نَّٰزِعَٰتِ` (ن ز ع), `غَرْقًا` (غ ر ق); 79:4 `سَّٰبِقَٰتِ`/`سَبْقًا` (س ب ق); 79:5 `مُدَبِّرَٰتِ` (د ب ر), `أَمْرًا` (ء م ر)
- Synthesis: The draw and the extreme extension are distinct operations, not synonyms: one loads the string and the other marks maximum reach. Precedence supplies the competitive flight, while the target-passing arrow and wager make the motion answerable to a concrete result.

#### Subchannel B. Cord, Knot, and Joined Hide
- Reading type: latent/lexical
- Scene or process: Fibres are twisted, a slipknot is tightened or released, hides are joined edge to edge, and a rearward twist controls the assembly.
- Active motifs: slipknot tied and released (`quranic:root_001505:B005/m01`); thick rope of twisted strands (`quranic:root_001292:B002/m01`); backward twist (`quranic:root_000458:B010/m01`); stitching two hides or panels (`quranic:root_000121:B006/m01`); supporting prop that prevents collapse (`quranic:root_000555:B009/m01`)
- Ayah anchors: 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط); 79:12 `كَرَّةٌ` (ك ر ر); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:9 `أَبْصَٰرُ` (ب ص ر); 79:10 `مَرْدُودُونَ` (ر د د)
- Synthesis: Twisting provides tensile strength, the knot controls release, stitching makes a continuous skin, and the prop carries load. Together they form the material precondition for controlled tension rather than a loose inventory of textile terms.

### 2. P1 - Ordered Speed, Overtaking, and Relay
- Semantic invariant: Rapid agents occupy ordered positions by advancing, following, catching, or replacing one another.
- Surface relation: direct; 79:2-4 moves from activation through swimming or running to precedence, and 79:7 explicitly makes one event follow another.
- Surprising reach: The sequence resolves simultaneously as a mounted race and as a political or operational relay in which a rear agent takes the preceding agent's place.

#### Subchannel A. Mounted Race and Pursuit
- Reading type: mixed
- Scene or process: Energized animals break into motion, extend their forelegs, accelerate under a rider, and either win precedence or evade capture.
- Active motifs: energetic readiness for work (`quranic:root_001505:B001/m01`); animal moving out from one ground to another (`quranic:root_001505:B002/m01`); horses running at full release (`quranic:root_001489:B012/m01`); horse extending its forelegs in a swimming gait (`quranic:root_000666:B004/m02`); racing ahead (`quranic:root_000671:B001/m02`); escaping the pursuer (`quranic:root_000671:B004/m01`); rapid camel or horse gait (`quranic:root_001628:B001/m01`); hoof striking the ground (`quranic:root_000341:B002/m01`)
- Ayah anchors: 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط); 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:3 `سَّٰبِحَٰتِ`/`سَبْحًا` (س ب ح); 79:4 `سَّٰبِقَٰتِ`/`سَبْقًا` (س ب ق); 79:8 `وَاجِفَةٌ` (و ج ف); 79:10 `حَافِرَةِ` (ح ف ر)
- Synthesis: Read as one kinetic scene, readiness becomes departure, departure becomes an extended gait, and the gait becomes competitive precedence. The hoof and rider-driven speed give the opening's abstract succession a forceful ground-level mechanics.

#### Subchannel B. Follower, Rear Rider, and Successor
- Reading type: mixed
- Scene or process: A rear agent tracks, catches, rides behind, or assumes the office of the one ahead.
- Active motifs: following a person, command, or trace (`quranic:root_000175:B001/m01`); catching the one who preceded (`quranic:root_000175:B002/m01`); uninterrupted succession (`quranic:root_000175:B004/m01`); an event coming after another (`quranic:root_000556:B001/m01`); rider seated behind a rider (`quranic:root_000556:B002/m01`); deputy who succeeds a king (`quranic:root_000556:B004/m01`)
- Ayah anchors: 79:7 `تَتْبَعُ` (ت ب ع), `رَّادِفَةُ` (ر د ف)
- Synthesis: Following is split into tracking, catching, continuous sequence, physical rear position, and institutional replacement. These operations sharpen the second convulsion as an ordered successor rather than merely another similar event.

### 3. P1 - Atmospheric and Celestial Procession
- Semantic invariant: Directional forces and visible lights move in recurring, ordered courses.
- Surface relation: indirect; the opening's swimmers, preceders, managers, follower, day, lowered sight, and wakeful surface provide motion and temporal order across 79:3-9 and 79:14.
- Surprising reach: The same ordered motion produces both a weather system driven by opposed winds and an astronomical calendar of following and setting bodies.

#### Subchannel A. Crosswinds Gathering Cloud
- Reading type: latent/lexical
- Scene or process: Winds arrive from differing bearings, a western wind drives from behind, gusts rise, and circulating air gathers dispersed cloud.
- Active motifs: winds from divergent bearings (`quranic:root_001489:B014/m01`); west wind coming from behind (`quranic:root_000458:B012/m01`); hard gust of wind (`quranic:root_001482:B004/m01`); wind turning and collecting cloud (`quranic:root_001292:B009/m01`)
- Ayah anchors: 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:11 `نَّخِرَةً` (ن خ ر); 79:12 `كَرَّةٌ` (ك ر ر)
- Synthesis: Direction, rearward pressure, gusting, and rotational collection constitute a weather mechanism. The latent scene makes management in 79:5 materially legible as forces that turn scattered matter into an organized mass.

#### Subchannel B. Stars, Alternating Lights, and Setting
- Reading type: latent/lexical
- Scene or process: Stars run their courses, one constellation follows another, night and day relay each other, and a visible body lowers toward disappearance.
- Active motifs: stars swimming in their sphere (`quranic:root_000666:B004/m03`); al-Dabaran following the Pleiades (`quranic:root_000458:B013/m01`); stars and night/day following in succession (`quranic:root_000556:B005/m01`); Antares as the heart of Scorpio (`quranic:root_001248:B010/m01`); a star sinking toward setting (`quranic:root_000412:B003/m01`); bounded daylight (`quranic:root_001700:B001/m01`)
- Ayah anchors: 79:3 `سَّٰبِحَٰتِ`/`سَبْحًا` (س ب ح); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:7 `رَّادِفَةُ` (ر د ف); 79:8 `قُلُوبٌ` (ق ل ب); 79:9 `خَٰشِعَةٌ` (خ ش ع); 79:6 `يَوْمَ` (ي و م)
- Synthesis: Orbital running, named stellar position, serial following, and setting form a complete sky-clock. The lowered celestial body also mirrors the lowered human gaze without collapsing astronomical motion into bodily fear.

### 4. P1 - Water Depth, Retrieval, and Containment
- Semantic invariant: Fluid moves between depth, surface, source, container, and drinkable portion.
- Surface relation: indirect; 79:1-3 supplies depth, extraction, and swimming, while 79:10-14 contributes pit, return, repetition, and the wakeful or flowing `سَّاهِرَةِ`.
- Surprising reach: Resurrection language is pressured by a hydrological mechanics in which submerged matter is drawn up, collected, and made available.

#### Subchannel A. Immersion, Saturation, and Flowing Source
- Reading type: latent/lexical
- Scene or process: Water engulfs a swimmer, saturates land, gathers in a pool, passes over a low island, and emerges as a running spring.
- Active motifs: submersion in water (`quranic:root_001080:B001/m01`); eye or land filled with water (`quranic:root_001080:B003/m01`); swimming through water (`quranic:root_000666:B004/m01`); collected pool or water-hole (`quranic:root_001292:B003/m01`); thick sea patch alternately covered and exposed (`quranic:root_000458:B021/m01`); flowing spring (`quranic:root_000752:B005/m01`); water mass gathering back (`quranic:root_000555:B007/m01`)
- Ayah anchors: 79:1 `غَرْقًا` (غ ر ق); 79:3 `سَّٰبِحَٰتِ`/`سَبْحًا` (س ب ح); 79:12 `كَرَّةٌ` (ك ر ر); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:14 `سَّاهِرَةِ` (س ه ر); 79:10 `مَرْدُودُونَ` (ر د د)
- Synthesis: The scene has changing vertical states: immersion, saturation, collection, temporary covering, and renewed exposure. It gives the sudden appearance on the `سَّاهِرَةِ` a latent analogue in land or matter reappearing when water withdraws.

#### Subchannel B. Excavated Well and Rapid Draw
- Reading type: latent/lexical
- Scene or process: A shaft is opened, water is reached in a well, and a bucket is pulled quickly without a pulley.
- Active motifs: excavating ground downward (`quranic:root_000341:B001/m01`); unlined well or water-pit (`quranic:root_001248:B007/m01`); hand-drawn water from a shallow well (`quranic:root_001489:B008/m01`); rapid bucket extraction (`quranic:root_001505:B006/m01`)
- Ayah anchors: 79:10 `حَافِرَةِ` (ح ف ر); 79:8 `قُلُوبٌ` (ق ل ب); 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط)
- Synthesis: Excavation supplies the setting, the well the containing object, hand-drawing the general operation, and the fast bucket-pull its intensified execution. This is a tight extraction mechanism rather than a generic water motif.

#### Subchannel C. Full Udder, Draught, and Finish
- Reading type: latent/lexical
- Scene or process: Milk accumulates, remains available, is portioned into a draught, and leaves a final taste as the vessel leaves the mouth.
- Active motifs: udder becoming full (`quranic:root_000555:B007/m02`); prolonged abundance of milk (`quranic:root_000752:B006/m01`); a small draught of milk or drink (`quranic:root_001080:B006/m01`); pleasant finish of a drink (`quranic:root_001489:B011/m01`); abundance and increase (`quranic:root_000051:B004/m01`)
- Ayah anchors: 79:10 `مَرْدُودُونَ` (ر د د); 79:14 `سَّاهِرَةِ` (س ه ر); 79:1 `غَرْقًا` (غ ر ق), `نَّٰزِعَٰتِ` (ن ز ع); 79:5 `أَمْرًا` (ء م ر)
- Synthesis: Accumulation, sustained supply, portion, and aftertaste form a complete consumption sequence. Its restrained scale usefully contrasts with the pericope's overwhelming motion.

### 5. P1 - Pasture, Offspring, and Animal Condition
- Semantic invariant: Herd life depends on growth, following offspring, feeding, lactation, and the bodily effects of work.
- Surface relation: indirect; the opening agents' motion and the later hoof, bones, lowered form, and wakeful source anchor animal movement and condition within 79:1-14.
- Surprising reach: The same roots that stage cosmic terror also produce a detailed husbandry scene of thriving young, depleted bodies, and controlled milk.

#### Subchannel A. Young Animals Following into Pasture
- Reading type: latent/lexical
- Scene or process: Lamb and calf remain with the herd, follow the mother, and grow strong on spring vegetation.
- Active motifs: young lamb (`quranic:root_000051:B009/m01`); calf following its mother (`quranic:root_000175:B007/m01`); animals strengthened by pasture (`quranic:root_001505:B001/m02`); spring plant grazed by camels (`quranic:root_000341:B008/m01`); plant called al-nazah (`quranic:root_001489:B015/m01`); increase and blessing (`quranic:root_000051:B004/m02`)
- Ayah anchors: 79:5 `أَمْرًا` (ء م ر); 79:7 `تَتْبَعُ` (ت ب ع); 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط); 79:10 `حَافِرَةِ` (ح ف ر); 79:1 `نَّٰزِعَٰتِ` (ن ز ع)
- Synthesis: Offspring, maternal following, edible vegetation, and resulting vigor form one husbandry cycle. The latent growth scene provides a life-bearing counterpressure to the pericope's extraction and decay.

#### Subchannel B. Udder Control and Worn Animal Bodies
- Reading type: latent/lexical
- Scene or process: A herder manages an unwilling milking animal while reading signs of pregnancy, depleted fat, sore back, and fatigue after riding.
- Active motifs: camel withholding milk (`quranic:root_000624:B004/m01`); spinal or hip defect in a camel (`quranic:root_000624:B005/m01`); hump losing fat and height (`quranic:root_000412:B004/m01`); pregnancy causing emaciation (`quranic:root_000341:B007/m01`); saddle sore on the back (`quranic:root_000458:B017/m01`); dismounting after a long ride (`quranic:root_001505:B010/m01`)
- Ayah anchors: 79:13 `زَجْرَةٌ` (ز ج ر); 79:9 `خَٰشِعَةٌ` (خ ش ع); 79:10 `حَافِرَةِ` (ح ف ر); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط)
- Synthesis: Refusal, bodily inspection, and the consequences of load and pregnancy make this an animal-care scene. The lowered hump is a particularly concrete analogue for humbled height.

### 6. P1 - Agrarian Production, Exchange, and Loss
- Semantic invariant: Material value is created, measured, negotiated, and sometimes lost.
- Surface relation: indirect; management in 79:5, return in 79:10, declared loss in 79:12, and repeated action in 79:12 provide the operational frame.
- Surprising reach: The proclaimed “losing return” expands into a full economy running from field parcels and milling to market rescission and gaming loss.

#### Subchannel A. Field Parcel, Winnowing, and Milling
- Reading type: latent/lexical
- Scene or process: Crop grows in marked plots, is lifted and winnowed with a toothed wooden tool, then passes repeatedly through a mill.
- Active motifs: field plots or furrows (`quranic:root_000458:B015/m01`); toothed winnowing fork (`quranic:root_000341:B009/m01`); repeated turning of a mill (`quranic:root_001292:B010/m01`); increase and abundant produce (`quranic:root_000051:B004/m03`)
- Ayah anchors: 79:5 `مُدَبِّرَٰتِ`/`أَمْرًا` (د ب ر, ء م ر); 79:10 `حَافِرَةِ` (ح ف ر); 79:12 `كَرَّةٌ` (ك ر ر)
- Synthesis: Parceling organizes cultivation, the fork separates grain from chaff, and rotational grinding finishes processing. Repetition in `كَرَّةٌ` thereby acquires a productive as well as eschatological mechanics.

#### Subchannel B. Bargain, Measure, Rejection, and Rescission
- Reading type: latent/lexical
- Scene or process: Traders negotiate, measure a large quantity, detect deficient or false value, and reverse the sale.
- Active motifs: negotiated bargain (`quranic:root_001272:B009/m01`); large-volume measure (`quranic:root_001292:B004/m01`); short measure or balance (`quranic:root_000409:B003/m01`); trading loss (`quranic:root_000409:B002/m01`); rejection of counterfeit or error (`quranic:root_000555:B003/m01`); rescission and return of goods (`quranic:root_000555:B004/m01`); cash settlement at the hoof (`quranic:root_000341:B004/m01`)
- Ayah anchors: 79:10 `يَقُولُ` (ق و ل), `مَرْدُودُونَ` (ر د د), `حَافِرَةِ` (ح ف ر); 79:12 `كَرَّةٌ` (ك ر ر), `خَاسِرَةٌ` (خ س ر)
- Synthesis: Negotiation initiates exchange, measure tests quantity, criticism rejects false value, and rescission restores the goods. The skeptics' own language of return and loss is thus pressured by the exact mechanics of a failed transaction.

#### Subchannel C. Stake, Losing Lot, and Diminished Share
- Reading type: latent/lexical
- Scene or process: A stake is placed on a contest, a lot fails, and the participant's holding is reduced.
- Active motifs: race wager (`quranic:root_000671:B002/m02`); losing gaming-arrow (`quranic:root_000458:B019/m01`); general diminution (`quranic:root_000409:B001/m01`); failed or ignoble loss (`quranic:root_000409:B005/m01`)
- Ayah anchors: 79:4 `سَّٰبِقَٰتِ`/`سَبْقًا` (س ب ق); 79:5 `مُدَبِّرَٰتِ` (د ب ر); 79:12 `خَاسِرَةٌ` (خ س ر)
- Synthesis: The race creates the stake, the losing lot determines outcome, and diminution names the material result. This scene makes “loss” adjudicated rather than merely emotional.

### 7. P1 - Counsel, Command, and Succession
- Semantic invariant: Authority is exercised through command, deliberation, public speech, following, and replacement.
- Surface relation: indirect; 79:5 names management of an affair, while 79:7 and 79:10-12 stage succession and public speech.
- Surprising reach: Cosmic administration is reframed through recognizable institutions: ruler, council, spokesman, follower, and deputy.

#### Subchannel A. Ruler Deliberating an Affair
- Reading type: mixed
- Scene or process: A holder of authority considers consequences, consults, issues a binding word, and has it carried out.
- Active motifs: authority and office (`quranic:root_000051:B003/m01`); consultation and accepting a considered view (`quranic:root_000051:B007/m01`); planning by looking to the outcome (`quranic:root_000458:B006/m01`); chief whose word has force (`quranic:root_001272:B004/m01`); exercising judgment over another (`quranic:root_001272:B010/m01`)
- Ayah anchors: 79:5 `أَمْرًا`/`مُدَبِّرَٰتِ` (ء م ر, د ب ر); 79:10 `يَقُولُ`, 79:12 `قَالُ` (ق و ل)
- Synthesis: Office identifies the agent, consultation the cognitive process, foresight the temporal horizon, and authoritative speech the operative output. The scene distinguishes administration from raw motion.

#### Subchannel B. Followers, Dynastic Order, and Deputy Rule
- Reading type: latent/lexical
- Scene or process: A polity is ordered by followers and successive rulers, with a deputy standing behind the king and a weak dependent accepting every command.
- Active motifs: follower who obeys (`quranic:root_000175:B001/m02`); kings succeeding one another (`quranic:root_000175:B009/m01`); deputy behind a king (`quranic:root_000556:B004/m02`); weak-minded dependent who seeks every command (`quranic:root_000051:B008/m01`); hereditary honor and standing (`quranic:root_001029:B010/m01`)
- Ayah anchors: 79:7 `تَتْبَعُ`/`رَّادِفَةُ` (ت ب ع, ر د ف); 79:5 `أَمْرًا` (ء م ر); 79:11 `عِظَٰمًا` (ع ظ م)
- Synthesis: Following becomes a social role, rear position becomes deputyship, and recurrence becomes succession in office. The weak dependent supplies the contrast between ordered obedience and unreasoning submission.

### 8. P1 - Dread Registered in Body, Posture, and Voice
- Semantic invariant: An overwhelming event becomes legible through involuntary bodily signals.
- Surface relation: direct; 79:6-9 names convulsion, fluttering hearts, and lowered eyes, while 79:11 adds disintegrating bone.
- Surprising reach: Fear is rendered not only as emotion but as cardiopulmonary motion, lowered anatomy, tissue decay, and broken speech.

#### Subchannel A. Convulsion, Palpitation, and Lowered Gaze
- Reading type: surface-primary
- Scene or process: External shaking is echoed by a heart that flutters and eyes that cannot hold an elevated gaze.
- Active motifs: severe physical disturbance (`quranic:root_000545:B001/m01`); palpitation of a fearful heart (`quranic:root_001628:B002/m01`); heart as organ and seat of understanding (`quranic:root_001248:B001/m01`); heart struck by affliction (`quranic:root_001248:B016/m01`); ocular seeing (`quranic:root_000121:B001/m01`); bowed head and lowered eyes (`quranic:root_000412:B001/m01`)
- Ayah anchors: 79:6 `تَرْجُفُ`/`رَّاجِفَةُ` (ر ج ف); 79:8 `قُلُوبٌ`/`وَاجِفَةٌ` (ق ل ب, و ج ف); 79:9 `أَبْصَٰرُ`/`خَٰشِعَةٌ` (ب ص ر, خ ش ع)
- Synthesis: The macro-convulsion and micro-palpitating heart share an oscillatory shape, while lowered vision supplies the resulting posture. The body becomes a seismograph for the event.

#### Subchannel B. Reduced Height, Rotten Bone, and Corroded Matter
- Reading type: mixed
- Scene or process: Formerly high or hard forms lose bulk, collapse, corrode, and break into porous remains.
- Active motifs: low, inert ground or failing wall (`quranic:root_000412:B002/m01`); hump stripped of fat and prominence (`quranic:root_000412:B004/m02`); hard bone (`quranic:root_001029:B005/m01`); rotten bone or wood crumbling around air (`quranic:root_001482:B003/m01`); eroded teeth (`quranic:root_000341:B005/m01`); corruption (`quranic:root_000341:B013/m01`); diminution (`quranic:root_000409:B001/m02`)
- Ayah anchors: 79:9 `خَٰشِعَةٌ` (خ ش ع); 79:11 `عِظَٰمًا`/`نَّخِرَةً` (ع ظ م, ن خ ر); 79:10 `حَافِرَةِ` (ح ف ر); 79:12 `خَاسِرَةٌ` (خ س ر)
- Synthesis: Lowering, loss of fat, hard skeletal matter, and porous decay form a sequence of material abasement. The scene makes the argument about rotten bones tactile without reducing it to a surface paraphrase.

#### Subchannel C. Nostril, Throat, Shout, and Impeded Tongue
- Reading type: latent/lexical
- Scene or process: Disturbed breathing and rough throat sounds culminate in a forceful shout, while human speech falters.
- Active motifs: snorting from the nostrils (`quranic:root_001482:B001/m01`); nostril as bodily aperture (`quranic:root_001482:B002/m01`); repeated choking or rattling throat-sound (`quranic:root_001292:B006/m01`); repelling shout (`quranic:root_000624:B001/m01`); tongue as speech instrument (`quranic:root_001272:B002/m01`); impediment of tongue or sight (`quranic:root_000555:B008/m01`)
- Ayah anchors: 79:11 `نَّخِرَةً` (ن خ ر); 79:12 `كَرَّةٌ`, `قَالُ` (ك ر ر, ق و ل); 79:13 `زَجْرَةٌ` (ز ج ر); 79:10 `مَرْدُودُونَ` (ر د د)
- Synthesis: Air passes through nose and throat as snort or rattle, then becomes a commanding shout; the impeded tongue marks the opposite state. This acoustic physiology sharpens the contrast between creaturely noise and decisive summons.

### 9. P1 - Extraction, Return, and the Singular Summons
- Semantic invariant: What is removed, dead, or dispersed is restored by a decisive reversal.
- Surface relation: direct; 79:1-2 supplies extraction, 79:10-12 debates return from rotten bone, and 79:13-14 answers with one cry and immediate presence.
- Surprising reach: The resurrection sequence is articulated as extraction from a seat, reversal to an origin, and a command whose singularity defeats repetitive human chatter.

#### Subchannel A. Soul Removal and Death-Throe
- Reading type: mixed
- Scene or process: A living principle is pulled from its seat, the body reaches its death-throe, and hard structure becomes decayed remains.
- Active motifs: pulling a thing from its settled place, including a soul (`quranic:root_001489:B001/m01`); death-throe (`quranic:root_001489:B016/m01`); soul drawn like a rapidly lifted bucket (`quranic:root_001505:B006/m02`); hard bone (`quranic:root_001029:B005/m02`); rotten, wind-hollowed bone (`quranic:root_001482:B003/m02`); temporal occurrence of a state (`quranic:root_001332:B001/m01`)
- Ayah anchors: 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط); 79:11 `عِظَٰمًا`/`نَّخِرَةً`/`كُ` (ع ظ م, ن خ ر, ك و ن)
- Synthesis: Removal, terminal bodily state, structural residue, and decay make one death process. The bucket simile supplies a concrete extraction mechanism while remaining distinct from the hydrological scene in which it is literal.

#### Subchannel B. Return to Origin and Reversal of State
- Reading type: surface-primary
- Scene or process: A prior condition is restored, repeated, and turned from one face or destination to another.
- Active motifs: return to a former place or state (`quranic:root_000555:B001/m01`); repetition and oscillating hesitation (`quranic:root_000555:B010/m01`); return to the first condition (`quranic:root_000341:B003/m01`); renewed return after departure (`quranic:root_001292:B001/m01`); turning a thing from face to face (`quranic:root_001248:B004/m01`); final destination or return-point (`quranic:root_001248:B005/m01`)
- Ayah anchors: 79:10 `مَرْدُودُونَ`/`حَافِرَةِ` (ر د د, ح ف ر); 79:12 `كَرَّةٌ` (ك ر ر); 79:8 `قُلُوبٌ` (ق ل ب)
- Synthesis: Return is disaggregated into restoration, repetition, inversion, and destination. The skeptics' `كَرَّةٌ` is therefore not a vague recurrence but a change of state with an origin and endpoint.

#### Subchannel C. Many Sayings, One Effective Cry
- Reading type: mixed
- Scene or process: People circulate claims, doubts, and inward beliefs; one unrepeatable command cuts through them and produces the outcome.
- Active motifs: articulated statement (`quranic:root_001272:B001/m01`); person characterized by abundant speech (`quranic:root_001272:B003/m01`); false attribution of words (`quranic:root_001272:B005/m01`); publicly circulating talk (`quranic:root_001272:B007/m01`); unspoken statement in the self (`quranic:root_001272:B012/m01`); belief or doctrine (`quranic:root_001272:B013/m01`); rumor that induces disturbance (`quranic:root_000545:B003/m01`); forceful restraining cry (`quranic:root_000624:B001/m02`); numerical oneness (`quranic:root_001631:B002/m01`); indivisible divine unity (`quranic:root_001631:B004/m01`)
- Ayah anchors: 79:10 `يَقُولُ`, 79:12 `قَالُ` (ق و ل); 79:6 `تَرْجُفُ` (ر ج ف); 79:13 `زَجْرَةٌ`/`وَٰحِدَةٌ` (ز ج ر, و ح د)
- Synthesis: Human discourse multiplies into public, false, internal, and doctrinal sayings; the answering cry is singular in count and undivided in agency. The resonance turns 79:13 into a discourse reversal as well as an acoustic event.

### 10. P1 - Conflict, Repulsion, and Social Contention
- Semantic invariant: Opposed agents attempt to strike, repel, outlast, or compel one another.
- Surface relation: indirect; the violent motion of 79:1-7 and the repelling cry of 79:13 provide the pericope's conflict-bearing anchors.
- Surprising reach: The sequence supports both a battlefield assembly of weapons and a civic dispute conducted through claims and negotiated speech.

#### Subchannel A. Armed Charge, Repulse, and Retreat
- Reading type: latent/lexical
- Scene or process: Combatants arm themselves, prepare for battle, charge, repel an attack, counterattack, and break the enemy's rear.
- Active motifs: shield or worn armor (`quranic:root_000121:B005/m01`); pointed spear-shaft (`quranic:root_000051:B011/m02`); preparing for war (`quranic:root_000545:B004/m01`); turning the back in retreat (`quranic:root_000458:B003/m01`); cutting off the enemy's rear and trace (`quranic:root_000458:B004/m01`); countercharge after retreat (`quranic:root_001292:B001/m02`); repelling and preventing (`quranic:root_000555:B002/m01`); shouted command or rebuke (`quranic:root_000624:B001/m03`)
- Ayah anchors: 79:9 `أَبْصَٰرُ` (ب ص ر); 79:5 `أَمْرًا`/`مُدَبِّرَٰتِ` (ء م ر, د ب ر); 79:6 `تَرْجُفُ` (ر ج ف); 79:12 `كَرَّةٌ` (ك ر ر); 79:10 `مَرْدُودُونَ` (ر د د); 79:13 `زَجْرَةٌ` (ز ج ر)
- Synthesis: Equipment, readiness, charge, repulse, retreat, and renewed attack form a coherent battle cycle. Its reversals give the pericope's successive motions a martial pressure without making combat the surface-primary reading.

#### Subchannel B. Claim, Counterclaim, and Estrangement
- Reading type: latent/lexical
- Scene or process: Parties pull against one another, assert claims, negotiate, and finally turn their backs in estrangement.
- Active motifs: mutual pulling, dispute, and argument (`quranic:root_001489:B006/m01`); claimant pursuing a right (`quranic:root_000175:B005/m01`); liability that follows an act (`quranic:root_000175:B006/m01`); negotiation over an affair (`quranic:root_001272:B009/m02`); imposing judgment on another (`quranic:root_001272:B010/m02`); mutual estrangement by turning backs (`quranic:root_000458:B005/m01`)
- Ayah anchors: 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:7 `تَتْبَعُ` (ت ب ع); 79:10 `يَقُولُ`, 79:12 `قَالُ` (ق و ل); 79:5 `مُدَبِّرَٰتِ` (د ب ر)
- Synthesis: The shared invariant is adversarial relation, but the operation is juridical and rhetorical rather than military. Claim, attached liability, bargaining, imposed judgment, and rupture define a complete social conflict.

### 11. P2 - Sacred Terrain as a Managed Watercourse
- Semantic invariant: A bounded sacred place is made habitable by directing, collecting, and distributing water.
- Surface relation: indirect; 79:16 names the sacred valley of Tuwa, and 79:18-19 turns the encounter toward purification and guidance.
- Surprising reach: The valley becomes an engineered hydrological and pastoral setting rather than a merely named backdrop.

#### Subchannel A. Valley Channel, Stone-Lined Well, and Basin
- Reading type: mixed
- Scene or process: Floodwater arrives from elsewhere, enters a valley channel, is directed through a course, retained in a stone-lined well, and measured at a basin outlet.
- Active motifs: channel directing water (`quranic:root_000009:B004/m01`); flood arriving from another district (`quranic:root_000009:B005/m01`); valley as a flood-course (`quranic:root_001637:B005/m01`); stone-lined well (`quranic:root_000960:B004/m01`); Tuwa as named valley or place (`quranic:root_000960:B009/m01`); basin stone at the water outlet (`quranic:root_001206:B010/m01`); abundant gathered water (`quranic:root_000532:B013/m01`)
- Ayah anchors: 79:15 `أَتَىٰ` (ء ت ي); 79:16 `وَادِ` (و د ي), `طُوًى` (ط و ي), `مُقَدَّسِ` (ق د س), `رَبُّ` (ر ب ب)
- Synthesis: Arrival supplies inflow, the valley supplies conveyance, masonry supplies retention, and the basin stone supplies controlled release. Sacred geography is thereby rendered as a functioning water system.

#### Subchannel B. Rain, Dew, Pasture, and Herd Return
- Reading type: latent/lexical
- Scene or process: Rain and dew wet the ground, sustain vegetation, and organize a herd's repeated movement between water and nearby pasture.
- Active motifs: rain and dew (`quranic:root_001486:B003/m01`); livestock moving from watering-place to pasture and back (`quranic:root_001486:B006/m01`); wetness and rain (`quranic:root_001487:B005/m01`); forage growing from dew (`quranic:root_001487:B006/m01`); the same water-pasture circuit (`quranic:root_001487:B004/m01`); rain-cloud stacked in layers (`quranic:root_000532:B008/m01`); persistent green plant (`quranic:root_000532:B012/m01`); herd of wild cattle or camels (`quranic:root_000532:B014/m01`); rain shower (`quranic:root_000522:B005/m01`)
- Ayah anchors: 79:16 and 79:23 `نَادَىٰ` (ن د و), 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب), 79:17 `ٱذْهَبْ` (ذ ه ب); unavailable for ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Moisture, plant response, herd, and return path form one pastoral circuit. The unavailable ن د ي anchors remain lexical support only; the surface-attested ن د و and ر ب ب roots keep the scene local to P2.

#### Subchannel C. Purified Place, Vessel, and Person
- Reading type: mixed
- Scene or process: A purified enclosure contains a washing vessel, and physical cleansing extends into the repair of the person.
- Active motifs: purity and consecration (`quranic:root_001206:B001/m01`); purified sacred place (`quranic:root_001206:B002/m01`); vessel used for purification (`quranic:root_001206:B005/m01`); moral purification and rectitude (`quranic:root_000637:B002/m01`); polishing a heart clean of rust (`quranic:root_000299:B007/m01`); repair and gradual cultivation (`quranic:root_000532:B002/m01`)
- Ayah anchors: 79:16 `مُقَدَّسِ`/`رَبُّ` (ق د س, ر ب ب); 79:18 `تَزَكَّىٰ` (ز ك و); 79:15 `حَدِيثُ` (ح د ث)
- Synthesis: Consecrated setting, cleansing tool, purified state, polished interior, and sustained repair form a single cleansing scene. It converts Moses's invitation into a process with place, instrument, action, and outcome.

### 12. P2 - Guidance as Cultivation and Interior Formation
- Semantic invariant: Right direction is produced by patient correction, growth, knowledge, and a reformed inward disposition.
- Surface relation: direct; 79:18-19 explicitly joins purification, guidance to the Lord, and reverent fear.
- Surprising reach: Guidance behaves like husbandry and craft: it grows, polishes, straightens, and trains rather than merely supplying information.

#### Subchannel A. Growth into Purity
- Reading type: surface-primary
- Scene or process: A person is cultivated from increase toward purity, then stabilized by reverent knowledge.
- Active motifs: growth and increase (`quranic:root_000637:B001/m01`); purification and moral soundness (`quranic:root_000637:B002/m02`); gradual repair and upbringing (`quranic:root_000532:B002/m02`); learned, disciplined knowledge (`quranic:root_000532:B003/m01`); fear joined to reverence (`quranic:root_000413:B001/m01`); knowledge expressed through khashya (`quranic:root_000413:B002/m01`)
- Ayah anchors: 79:18 `تَزَكَّىٰ` (ز ك و); 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:19/26 `تَخْشَىٰ`/`يَخْشَىٰٓ` (خ ش ي)
- Synthesis: Increase names development, purification its ethical direction, upbringing its duration, knowledge its cognitive maturity, and reverence its embodied outcome.

#### Subchannel B. Gentle Leading on a Straight Course
- Reading type: mixed
- Scene or process: A guide goes in front, indicates a route gently, and establishes a settled manner of walking it.
- Active motifs: gentle direction to road and truth (`quranic:root_001583:B001/m01`); course, orientation, and habitual manner (`quranic:root_001583:B002/m01`); guide or leading edge moving first (`quranic:root_001583:B003/m01`); route and method (`quranic:root_000522:B007/m01`); well-travelled road and junction (`quranic:root_000009:B010/m01`); reaching a limit or destination (`quranic:root_000076:B001/m01`)
- Ayah anchors: 79:19 `أَهْدِيَ` (ه د ي); 79:17 `ٱذْهَبْ` (ذ ه ب); 79:15 `أَتَىٰ` (ء ت ي); unavailable for ء ل ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Guide, route, orientation, practice, and destination complete a path scene. The missing ء ل ي surface anchor is not supplied; its endpoint motif remains a lexical extension within P2.

#### Subchannel C. Folded Intention Opened to Deliberation
- Reading type: latent/lexical
- Scene or process: A concealed intention is held inwardly, examined as an opinion, and brought into a declared position.
- Active motifs: inward intention and destination (`quranic:root_000960:B005/m01`); concealed secret or withheld counsel (`quranic:root_000960:B007/m01`); unspoken statement in the self (`quranic:root_001272:B012/m01`); belief or doctrine (`quranic:root_001272:B013/m01`); inward opinion and deliberation (`quranic:root_000531:B002/m01`); composed bearing and quiet manner (`quranic:root_001583:B010/m01`)
- Ayah anchors: 79:16 `طُوًى` (ط و ي); 79:18/24 `قُلْ`/`قَالَ` (ق و ل); 79:20 `أَرَىٰ` (ر ء ي); 79:19 `أَهْدِيَ` (ه د ي)
- Synthesis: The fold is a container for intention, private speech its content, deliberation the inspection process, and a settled manner the resulting disposition. This is an interior reform scene distinct from outward route-finding.

### 13. P2 - Truth Made Audible, Visible, and Memorable
- Semantic invariant: Meaning becomes public by call, sign, narration, and interpretive passage.
- Surface relation: direct; 79:15 introduces a narrated event, 79:16 and 79:23 stage calls, 79:20 displays the great sign, and 79:26 names the lesson.
- Surprising reach: Revelation is assembled as a multimodal communication system whose audible, visible, and mnemonic operations answer fabricated counter-speech.

#### Subchannel A. Elevated Call and Manifest Sign
- Reading type: surface-primary
- Scene or process: A voice carries across distance, makes its source manifest, and directs attention to a visibly marked sign.
- Active motifs: raised, far-carrying call (`quranic:root_001486:B002/m01`); a path or thing appearing as though it calls (`quranic:root_001486:B008/m01`); raised voice and summons (`quranic:root_001487:B001/m01`); manifestation that informs like a call (`quranic:root_001487:B011/m01`); visible sign or mark (`quranic:root_000074:B003/m01`); showing a thing to another (`quranic:root_000531:B012/m01`); great scale (`quranic:root_001281:B001/m01`); awe-struck magnification (`quranic:root_001281:B003/m01`)
- Ayah anchors: 79:16/23 `نَادَىٰ` (ن د و); 79:20 `ءَايَةَ`/`أَرَىٰ`/`كُبْرَىٰ` (ء ي ي, ر ء ي, ك ب ر); unavailable for ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Voice supplies address, manifestation makes the address locatable, the mark supplies visible content, and magnitude supplies impact. The unavailable alternate ن د ي root is kept explicitly unanchored.

#### Subchannel B. Event Becomes Story, Then Lesson
- Reading type: mixed
- Scene or process: A new occurrence is narrated, preserved as public memory, interpreted beyond its surface, and applied as an admonitory analogy.
- Active motifs: event coming into being (`quranic:root_000299:B001/m01`); narrated report (`quranic:root_000299:B003/m01`); person becoming a story among people (`quranic:root_000299:B004/m01`); calamity of time (`quranic:root_000299:B005/m01`); moving meaning through language (`quranic:root_000974:B003/m01`); crossing from a dream's surface to meaning (`quranic:root_000974:B002/m01`); taking one case as an admonitory analogue for another (`quranic:root_000974:B004/m01`); knowledge through reverent perception (`quranic:root_000413:B002/m02`)
- Ayah anchors: 79:15 `حَدِيثُ` (ح د ث); 79:26 `عِبْرَةً`/`يَخْشَىٰٓ` (ع ب ر, خ ش ي)
- Synthesis: Occurrence, narration, public memory, interpretation, and transfer to another case form a causal chain. `عِبْرَةً` is thereby an act of semantic crossing, not merely a label for “lesson.”

#### Subchannel C. Fabricated Speech and Performative Display
- Reading type: mixed
- Scene or process: A ruler rejects the sign, attributes falsehood, turns speech into doctrine, and performs greatness before an audience.
- Active motifs: false statement (`quranic:root_001290:B001/m01`); attributing falsehood to another (`quranic:root_001290:B002/m01`); self-deceiving soul (`quranic:root_001290:B008/m01`); garment whose appearance falsifies its condition (`quranic:root_001290:B009/m01`); false attribution of words (`quranic:root_001272:B005/m01`); publicly circulating talk (`quranic:root_001272:B007/m01`); exercising judgment over another (`quranic:root_001272:B010/m01`); doctrine or position (`quranic:root_001272:B013/m02`); acting to be seen by people (`quranic:root_000531:B005/m01`); self-magnifying arrogance (`quranic:root_001281:B006/m01`)
- Ayah anchors: 79:21 `كَذَّبَ` (ك ذ ب); 79:18/24 `قُلْ`/`قَالَ` (ق و ل); 79:20 `أَرَىٰ` (ر ء ي); 79:20 `كُبْرَىٰ` (ك ب ر)
- Synthesis: Rejection becomes an alternative publicity apparatus: false attribution, repeated public talk, doctrine, visual performance, and self-magnification. It stands as a coherent counter-scene to manifested sign and truthful narration.

### 14. P2 - Rival Regimes of Rule
- Semantic invariant: Rule is defined either by sustaining care and accountable guidance or by self-exalting coercion.
- Surface relation: direct; 79:16-19 repeatedly names the Lord as caller and guide, while 79:17 and 79:24 identify Pharaoh's transgression and supreme claim.
- Surprising reach: The contrast extends from theology into administration, husbandry, captaining, and the organization of a public assembly.

#### Subchannel A. Lordship as Ownership, Repair, and Learned Care
- Reading type: mixed
- Scene or process: A true lord owns, repairs, raises, teaches, keeps covenant, and leads dependents toward completion.
- Active motifs: lordship, ownership, and mastery (`quranic:root_000532:B001/m01`); gradual repair and upbringing (`quranic:root_000532:B002/m03`); learned divine formation (`quranic:root_000532:B003/m02`); covenant and protection (`quranic:root_000532:B011/m01`); captain responsible for sailors (`quranic:root_000532:B017/m01`); policy that repairs an affair (`quranic:root_000067:B004/m01`); gentle guidance (`quranic:root_001583:B001/m02`)
- Ayah anchors: 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:25 `أُولَىٰٓ` (ء و ل); 79:19 `أَهْدِيَ` (ه د ي)
- Synthesis: Ownership establishes jurisdiction, upbringing and knowledge define its method, covenant its relation, captaining its practical analogy, and guidance its direction. Authority is thus measured by care rather than assertion.

#### Subchannel B. Transgression, Idolized Power, and Self-Exaltation
- Reading type: mixed
- Scene or process: A ruler exceeds the limit, becomes a coercive head of misdirection, elevates himself, and seeks worship.
- Active motifs: exceeding the limit in disobedience (`quranic:root_000937:B001/m01`); flood-like force that rises and sweeps away (`quranic:root_000937:B002/m01`); head of misdirection or false object of worship (`quranic:root_000937:B003/m01`); tyrant who coerces people (`quranic:root_000936:B004/m01`); taghut as head of error (`quranic:root_000936:B003/m01`); arrogant elevation over people (`quranic:root_001042:B003/m01`); coercive domination (`quranic:root_001042:B004/m01`); worship and object of worship (`quranic:root_000047:B001/m01`)
- Ayah anchors: 79:17 `طَغَىٰ` (ط غ ي); 79:24 `أَعْلَىٰ` (ع ل و); 79:25 `ٱللَّهُ` (ء ل ه); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Boundary violation becomes rising material force, then coercive office, then a claim to worship. The duplicate ط غ و branch family remains unanchored, while surface-attested ط غ ي carries the local scene.

#### Subchannel C. Mustered Crowd and Sovereign Proclamation
- Reading type: surface-primary
- Scene or process: People are driven into an assembly, a loud call convenes them, and a ruler issues a public claim from its center.
- Active motifs: driving and gathering a crowd (`quranic:root_000324:B001/m01`); densely packed multitude (`quranic:root_000324:B005/m01`); large congregated groups (`quranic:root_000532:B004/m01`); council or public meeting (`quranic:root_001486:B001/m01`); raised proclamation (`quranic:root_001486:B002/m02`); person characterized by abundant speech (`quranic:root_001272:B003/m01`); ruler whose speech has force (`quranic:root_001272:B004/m02`)
- Ayah anchors: 79:23 `حَشَرَ`/`نَادَىٰ` (ح ش ر, ن د و); 79:24 `رَبُّ`/`قَالَ` (ر ب ب, ق و ل)
- Synthesis: Muster creates the audience, council supplies the social setting, raised voice reaches it, and authoritative speech converts assembly into political spectacle.

### 15. P2 - Directed Movement, Muster, and Seizure
- Semantic invariant: Intention is translated into bodily movement that ends either in guidance or in forcible capture.
- Surface relation: direct; 79:17 sends Moses, 79:22 makes Pharaoh turn and strive, 79:23 gathers the people, and 79:25 culminates in seizure.
- Surprising reach: The passage's verbs create a full movement grammar from route selection to retreat, chase, wrestling hold, shackle, and exemplary restraint.

#### Subchannel A. Arrival, Route, and Purposeful Advance
- Reading type: mixed
- Scene or process: An agent arrives, approaches an affair from its proper side, takes a route, follows a guide, and advances toward a defined end.
- Active motifs: arrival and reaching (`quranic:root_000009:B001/m01`); approaching an affair by its proper avenue (`quranic:root_000009:B003/m01`); traversed road and junction (`quranic:root_000009:B010/m02`); going and passing (`quranic:root_000522:B006/m01`); route or method (`quranic:root_000522:B007/m02`); purposeful movement to a sought object (`quranic:root_000709:B001/m01`); leading guide (`quranic:root_001583:B003/m02`); endpoint (`quranic:root_000076:B001/m02`)
- Ayah anchors: 79:15 `أَتَىٰ` (ء ت ي); 79:17 `ٱذْهَبْ` (ذ ه ب); 79:22 `يَسْعَىٰ` (س ع ي); 79:19 `أَهْدِيَ` (ه د ي); unavailable for ء ل ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Arrival, avenue, route, leading agent, purposeful motion, and endpoint form a directed journey. The unanchored endpoint branch is retained only as lexical completion.

#### Subchannel B. Turning Away, Striving, and Muster
- Reading type: surface-primary
- Scene or process: A resisting agent turns his back, moves urgently, uses political action, and gathers others around the refusal.
- Active motifs: turning one's back and rejecting (`quranic:root_000458:B003/m02`); purposeful urgent movement (`quranic:root_000709:B001/m02`); practical activity and energetic conduct (`quranic:root_000709:B002/m02`); informing against someone to authority (`quranic:root_000709:B004/m01`); gathering and driving people (`quranic:root_000324:B001/m02`); public call (`quranic:root_001486:B002/m03`)
- Ayah anchors: 79:22 `أَدْبَرَ`/`يَسْعَىٰ` (د ب ر, س ع ي); 79:23 `حَشَرَ`/`نَادَىٰ` (ح ش ر, ن د و)
- Synthesis: Turning is the directional reversal, striving the energy, political activity the means, and muster the social outcome. The scene reads Pharaoh's response as organized counter-mobilization.

#### Subchannel C. Capture, Wrestling Hold, and Deterrent Restraint
- Reading type: mixed
- Scene or process: The offender is taken, held like a wrestler, bound from movement, and made an example that checks repetition.
- Active motifs: taking possession (`quranic:root_000018:B001/m01`); accountability for an offense (`quranic:root_000018:B002/m01`); capture of a prisoner (`quranic:root_000018:B003/m01`); bodily condition taking hold (`quranic:root_000018:B007/m01`); wrestler's locking hold (`quranic:root_000018:B011/m01`); wrestling takedown (`quranic:root_000458:B022/m01`); shackle or bit preventing motion (`quranic:root_001554:B001/m01`); recoiling in fear (`quranic:root_001554:B002/m01`); exemplary punishment (`quranic:root_001554:B003/m01`)
- Ayah anchors: 79:25 `أَخَذَ`/`نَكَالَ` (ء خ ذ, ن ك ل); 79:22 `أَدْبَرَ` (د ب ر)
- Synthesis: Seizure is decomposed into legal accountability, physical capture, immobilizing hold, restraint, and deterrent effect. The wrestling image materially intensifies `أَخَذَ` without replacing its divine agency.

### 16. P2 - Event, Outcome, and Exemplary Transfer
- Semantic invariant: An occurrence is understood by tracing its temporal sequence into an outcome and transferring that outcome to another case.
- Surface relation: direct; 79:15 opens a past event, 79:25 joins first and last, and 79:26 draws an exemplary inference.
- Surprising reach: Temporal ordering and interpretation become one causal method: event, aftermath, return-point, and analogy.

#### Subchannel A. Occurrence, Aftermath, First, and Last
- Reading type: mixed
- Scene or process: An event arrives, develops into a calamity, and is located by its beginning, aftermath, and final return.
- Active motifs: event coming into existence (`quranic:root_000299:B001/m02`); temporal calamity (`quranic:root_000299:B005/m02`); arrival of expected event or ruin (`quranic:root_000009:B011/m01`); beginning and precedence (`quranic:root_000067:B001/m01`); return to final outcome (`quranic:root_000067:B002/m01`); what comes after the first (`quranic:root_000019:B001/m01`); delay into a later time (`quranic:root_000019:B002/m01`); looking to an affair's consequence (`quranic:root_000458:B006/m02`)
- Ayah anchors: 79:15 `حَدِيثُ`/`أَتَىٰ` (ح د ث, ء ت ي); 79:25 `أُولَىٰٓ`/`ءَاخِرَةِ` (ء و ل, ء خ ر); 79:22 `أَدْبَرَ` (د ب ر)
- Synthesis: Beginning and latter phase do not merely bracket time; they locate a process whose consequence can be anticipated. The event is read through its terminal shape.

#### Subchannel B. Crossing from Case to Admonition
- Reading type: surface-primary
- Scene or process: A hearer passes from narrated facts to their meaning, then measures the present self against the past case.
- Active motifs: passage from side to side (`quranic:root_000974:B001/m01`); interpretation from surface to meaning (`quranic:root_000974:B002/m02`); linguistic conveyance of inward meaning (`quranic:root_000974:B003/m02`); analogical admonition (`quranic:root_000974:B004/m02`); punishment that makes others refrain (`quranic:root_001554:B003/m02`); reverent fear (`quranic:root_000413:B001/m02`)
- Ayah anchors: 79:26 `عِبْرَةً`/`يَخْشَىٰٓ` (ع ب ر, خ ش ي); 79:25 `نَكَالَ` (ن ك ل)
- Synthesis: Physical crossing supplies the shape of interpretation: the mind passes through wording into consequence, then carries that consequence across to its own conduct.

### 17. P2 - Gift, Tribute, Offering, and Covenant
- Semantic invariant: Value moves between parties under relations of generosity, authority, worship, marriage, or obligation.
- Surface relation: indirect; 79:18-19 offers guidance toward the Lord, while 79:24-25 contests ownership and authority.
- Surprising reach: The encounter supports several distinct transfer scenes, from tribute and reparation to sacred offering and household covenant.

#### Subchannel A. Gift, Tribute, and Reparation
- Reading type: latent/lexical
- Scene or process: A giver presents value, a ruler receives levy, generosity grants an unsolicited gift, and injury triggers compensation.
- Active motifs: giving and presentation (`quranic:root_000009:B002/m01`); tribute or levy paid (`quranic:root_000009:B008/m01`); gift or benefit (`quranic:root_000076:B012/m01`); generosity and open-handedness (`quranic:root_001486:B004/m01`); generous giving (`quranic:root_001487:B008/m01`); payment of blood-money (`quranic:root_001637:B002/m01`); affectionate gift (`quranic:root_001583:B004/m01`)
- Ayah anchors: 79:15 `أَتَىٰ` (ء ت ي); 79:16/23 `نَادَىٰ` (ن د و); 79:16 `وَادِ` (و د ي); 79:19 `أَهْدِيَ` (ه د ي); unavailable for ء ل ي and ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Presentation is the shared invariant, but tribute, free generosity, reparation, and affectionate gift retain distinct social roles. Missing-root motifs remain explicitly without ayah anchors.

#### Subchannel B. Sacred Offering to a True Object of Worship
- Reading type: latent/lexical
- Scene or process: Herd wealth is selected and led as an offering into a consecrated precinct under divine ownership.
- Active motifs: sacrificial animal or property led to the sanctuary (`quranic:root_001583:B005/m01`); worship and object of worship (`quranic:root_000047:B001/m02`); consecrated place (`quranic:root_001206:B002/m02`); true ownership and lordship (`quranic:root_000532:B001/m02`); presented gift (`quranic:root_000009:B002/m02`)
- Ayah anchors: 79:19 `أَهْدِيَ` (ه د ي); 79:25 `ٱللَّهُ` (ء ل ه); 79:16 `مُقَدَّسِ`/`رَبُّ` (ق د س, ر ب ب); 79:15 `أَتَىٰ` (ء ت ي)
- Synthesis: Offering, animal, sanctuary, recipient, and transfer form one ritual scene. It counters Pharaoh's claimed lordship with property deliberately returned to its rightful owner.

#### Subchannel C. Fostered Household, Bride, and Binding Pact
- Reading type: latent/lexical
- Scene or process: A dependent is raised within a household, a bride is conducted into it, and the relation is secured by oath and covenant.
- Active motifs: foster child and caretaker (`quranic:root_000532:B005/m01`); covenant and protection (`quranic:root_000532:B011/m02`); need, blessing, and firmly tied bond (`quranic:root_000532:B016/m01`); family to whom a person returns (`quranic:root_000067:B003/m01`); bride conducted to her husband (`quranic:root_001583:B006/m01`); protected person or captive under pledged safety (`quranic:root_001583:B007/m01`); oath (`quranic:root_000076:B007/m01`)
- Ayah anchors: 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:25 `أُولَىٰٓ` (ء و ل); 79:19 `أَهْدِيَ` (ه د ي); unavailable for ء ل ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Care, incorporation, bridal transfer, pledged safety, and covenant form a household institution. Its reciprocal obligations contrast with unilateral tyranny.

### 18. P2 - Navigation, Command, and Landmark
- Semantic invariant: Travel succeeds through a vessel, responsible leader, visible marker, and known destination.
- Surface relation: indirect; 79:16's valley, 79:17's command to go, 79:19's guidance, and 79:20's displayed sign anchor route-finding.
- Surprising reach: Moses's mission can be materialized as navigation in which lordship appears as captaining rather than domination.

#### Subchannel A. Great Vessel, Captain, and Destination
- Reading type: latent/lexical
- Scene or process: A large vessel crosses abundant water under a captain who follows a known route toward an endpoint.
- Active motifs: great ship (`quranic:root_001206:B009/m01`); captain of sailors (`quranic:root_000532:B017/m02`); abundant water (`quranic:root_000532:B013/m02`); leading edge or guide (`quranic:root_001583:B003/m03`); travelled road (`quranic:root_000009:B010/m03`); route and method (`quranic:root_000522:B007/m03`); endpoint (`quranic:root_000076:B001/m03`)
- Ayah anchors: 79:16 `مُقَدَّسِ`/`رَبُّ` (ق د س, ر ب ب); 79:19 `أَهْدِيَ` (ه د ي); 79:15 `أَتَىٰ` (ء ت ي); 79:17 `ٱذْهَبْ` (ذ ه ب); unavailable for ء ل ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Vessel, water, captain, route, leading marker, and destination complete a navigation scene. The captain motif specifies responsible coordination under the root of lordship.

#### Subchannel B. Banner, Appearing Path, and Recognition
- Reading type: latent/lexical
- Scene or process: A raised marker and a conspicuous path let travellers recognize orientation at distance.
- Active motifs: raised visible banner (`quranic:root_000531:B011/m01`); visible sign (`quranic:root_000074:B003/m02`); road that appears as though calling the traveller (`quranic:root_001486:B008/m02`); appearing path that informs (`quranic:root_001487:B011/m02`); gentle route indication (`quranic:root_001583:B001/m03`); direct visual recognition (`quranic:root_000531:B001/m01`)
- Ayah anchors: 79:20 `أَرَىٰ`/`ءَايَةَ` (ر ء ي, ء ي ي); 79:16/23 `نَادَىٰ` (ن د و); 79:19 `أَهْدِيَ` (ه د ي); unavailable for ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Banner and sign are objects, appearance is their mode of disclosure, seeing is the traveller's operation, and guidance is the resulting orientation.

### 19. P2 - Herd Wealth, Reproduction, and Care
- Semantic invariant: Animal wealth is sustained through breeding, pasture, watering, and protective ownership.
- Surface relation: indirect; the valley and repeated lordship anchors at 79:16-24 carry the husbandry senses.
- Surprising reach: Rival rule is tested against a pastoral model in which a lord's legitimacy lies in sustaining vulnerable life.

#### Subchannel A. Ewe, Herd, and Young Animal
- Reading type: latent/lexical
- Scene or process: A recently delivered ewe remains near shelter, the herd gathers, and a young wild bovine is incorporated into the stock.
- Active motifs: ewe near parturition or newly delivered (`quranic:root_000532:B009/m01`); herd of cattle or camels (`quranic:root_000532:B014/m02`); young wild bovine (`quranic:root_000936:B009/m01`); sacrificial livestock (`quranic:root_001583:B005/m02`); female camel desiring the male (`quranic:root_000009:B012/m01`)
- Ayah anchors: 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:19 `أَهْدِيَ` (ه د ي); 79:15 `أَتَىٰ` (ء ت ي); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Breeding state, offspring, herd, and protected livestock form the participants of a husbandry scene. The missing ط غ و anchor is not replaced by the attested ط غ ي occurrence.

#### Subchannel B. Water-Pasture Rotation and Growth
- Reading type: latent/lexical
- Scene or process: Animals leave water briefly for nearby pasture, return, and gain condition through sustained growth.
- Active motifs: movement between water and pasture (`quranic:root_001486:B006/m02`); water-pasture interval (`quranic:root_001487:B004/m02`); abundant water (`quranic:root_000532:B013/m03`); persistent forage (`quranic:root_000532:B012/m02`); biological increase (`quranic:root_000637:B001/m02`)
- Ayah anchors: 79:16/23 `نَادَىٰ` (ن د و); 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:18 `تَزَكَّىٰ` (ز ك و); unavailable for ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Water, forage, timed movement, return, and growth form an operational care cycle. It supplies the material underside of cultivation in 79:18.

### 20. P3 - Creation as Measured Engineering
- Semantic invariant: A stable whole is produced by measuring, assembling, raising, equalizing, and anchoring parts.
- Surface relation: direct; 79:27-32 explicitly moves through creation, building, raising, proportioning, spreading, and fixing.
- Surprising reach: Cosmic creation behaves like disciplined architecture rather than undifferentiated power.

#### Subchannel A. Measurement, Plan, and Composite Form
- Reading type: surface-primary
- Scene or process: A maker measures the intended form, joins parts, and brings a balanced structure into existence.
- Active motifs: measuring before cutting or acting (`quranic:root_000434:B001/m01`); creating and producing (`quranic:root_000434:B002/m01`); complete and proportioned form (`quranic:root_000434:B003/m01`); building by joining parts (`quranic:root_000156:B001/m01`); composite constitution (`quranic:root_000156:B002/m01`); strength and solidity (`quranic:root_000782:B002/m01`)
- Ayah anchors: 79:27 `خَلْقًا`/`بَنَىٰ`/`أَشَدُّ` (خ ل ق, ب ن ي, ش د د)
- Synthesis: Measurement precedes assembly, assembly produces a composite, and proportion and solidity name the achieved state. Creation is presented as an ordered production sequence.

#### Subchannel B. Raised Roof and Equalized Span
- Reading type: mixed
- Scene or process: A roof is lifted, held overhead, and brought into level proportion across its span.
- Active motifs: raising a structure (`quranic:root_000582:B001/m01`); height and ascent (`quranic:root_000742:B001/m01`); roof and element that holds it (`quranic:root_000742:B002/m01`); sky as what rises and shades (`quranic:root_000745:B004/m01`); equality between dimensions (`quranic:root_000766:B001/m01`); straightening and completion (`quranic:root_000766:B002/m01`); stable elevation over a support (`quranic:root_000766:B003/m01`)
- Ayah anchors: 79:28 `رَفَعَ`/`سَمْكَ`/`سَوَّىٰ` (ر ف ع, س م ك, س و ي); 79:27 `سَّمَآءُ` (س م و)
- Synthesis: Lift is the action, roof the object, overhead sky the spatial relation, and leveling the finishing operation. The sequence gives exact roles to the roots in 79:27-28.

#### Subchannel C. Load-Bearing Ribs, Hard Ground, and Anchors
- Reading type: mixed
- Scene or process: Ribs or uprights carry a structure while hard ground and fixed anchors prevent displacement.
- Active motifs: ribs and uprights on which a thing settles (`quranic:root_000156:B009/m01`); solid elevated mass (`quranic:root_000217:B001/m01`); hard ground that stops excavation (`quranic:root_000217:B005/m01`); fastening into stability (`quranic:root_000564:B001/m01`); broad level bearing surface (`quranic:root_000766:B009/m01`); lifting into position (`quranic:root_000582:B001/m02`)
- Ayah anchors: 79:27 `بَنَىٰ` (ب ن ي); 79:32 `جِبَالَ`/`أَرْسَىٰ` (ج ب ل, ر س و); 79:28 `سَوَّىٰ`/`رَفَعَ` (س و ي, ر ف ع)
- Synthesis: Uprights carry load, hard ground resists penetration, broad surface distributes force, and anchoring fixes the whole. Mountains become structural participants, not decorative scenery.

### 21. P3 - Fabric, Cover, and Load-Bearing Body
- Semantic invariant: Flexible material becomes structural through joining, weaving, tightening, padding, and load distribution.
- Surface relation: indirect; 79:27-28 supplies building and raised structure, while 79:30-33 supplies spread surface, mountains, and usable provision.
- Surprising reach: Cosmic architecture is mirrored by tent-making, saddlery, rope-work, and the body's own ribs and thick tissue.

#### Subchannel A. Leather Canopy, Ground Cloth, and Saddle Pad
- Reading type: latent/lexical
- Scene or process: A leather covering is raised over a spread ground-cloth, held by structure, and furnished with a pad for load-bearing use.
- Active motifs: leather dome, curtain, or cover (`quranic:root_000156:B004/m01`); thick woollen ground-rug (`quranic:root_000025:B005/m01`); roof and supporting member (`quranic:root_000742:B002/m02`); saddlecloth or pad over a camel's back (`quranic:root_000766:B010/m01`); padding used to enlarge or support (`quranic:root_000582:B008/m01`); well-made weaving (`quranic:root_000217:B007/m01`)
- Ayah anchors: 79:27 `بَنَىٰ` (ب ن ي); 79:30 `أَرْضَ` (ء ر ض); 79:28 `سَمْكَ`/`سَوَّىٰ`/`رَفَعَ` (س م ك, س و ي, ر ف ع); 79:32 `جِبَالَ` (ج ب ل)
- Synthesis: Covering, floor, support, weave, and padding constitute a tent-and-saddlery scene. It reveals a mobile, inhabited analogue to the raised and spread cosmos.

#### Subchannel B. Tight Weave, Knot, and Worn Cloth
- Reading type: latent/lexical
- Scene or process: Fibres are woven and bound under tension; repeated use then strips the fabric of nap and integrity.
- Active motifs: tight and excellent weaving (`quranic:root_000217:B007/m02`); binding and strengthening a knot (`quranic:root_000782:B001/m01`); lifting cord for a restraint (`quranic:root_000582:B009/m01`); joining parts into a built whole (`quranic:root_000156:B001/m02`); cloth worn smooth and threadbare (`quranic:root_000434:B009/m01`)
- Ayah anchors: 79:32 `جِبَالَ` (ج ب ل); 79:27 `أَشَدُّ`/`بَنَىٰ`/`خَلْقًا` (ش د د, ب ن ي, خ ل ق); 79:28 `رَفَعَ` (ر ف ع)
- Synthesis: Weaving organizes fibres, the knot fixes tension, the cord manages load, and wear records duration. This is a material lifecycle distinct from the rigid architecture above.

#### Subchannel C. Ribs, Thick Body, and Mature Strength
- Reading type: latent/lexical
- Scene or process: Food builds flesh over a ribbed frame until the body reaches full form, thickness, height, and mature strength.
- Active motifs: food building and enlarging flesh (`quranic:root_000156:B010/m01`); thick bodily constitution (`quranic:root_000217:B003/m01`); ribs as supports (`quranic:root_000156:B009/m02`); complete bodily form (`quranic:root_000434:B003/m02`); tall raised stature (`quranic:root_000742:B001/m02`); maturity of strength and judgment (`quranic:root_000782:B004/m01`)
- Ayah anchors: 79:27 `بَنَىٰ`/`خَلْقًا`/`أَشَدُّ` (ب ن ي, خ ل ق, ش د د); 79:28 `سَمْكَ` (س م ك); 79:32 `جِبَالَ` (ج ب ل)
- Synthesis: The body is treated as an engineered structure whose ribs bear, food adds material, form is proportioned, and maturity completes load-bearing capacity.

### 22. P3 - Shaped Earth, Basin, and Stabilized Terrain
- Semantic invariant: Terrain is made usable by spreading, smoothing, excavating, retaining water, and fixing unstable masses.
- Surface relation: direct; 79:30-32 spreads earth, brings out water, and fixes mountains.
- Surprising reach: The land becomes a worked landscape containing exposed plains, animal hollows, reservoirs, and resistant rock.

#### Subchannel A. Spread and Smoothed Expanse
- Reading type: mixed
- Scene or process: Ground is swept outward, exposed, smoothed, and made into a broad usable surface.
- Active motifs: lower ground opposite the sky (`quranic:root_000025:B001/m01`); soft productive earth (`quranic:root_000025:B002/m01`); pushing or sweeping material over the surface (`quranic:root_000462:B002/m01`); lying or hollowing out in a broad easy place (`quranic:root_000462:B004/m01`); smooth rock or level surface (`quranic:root_000434:B008/m01`); wide smooth tract (`quranic:root_000766:B009/m02`); open exposed space (`quranic:root_000105:B002/m01`)
- Ayah anchors: 79:30 `أَرْضَ`/`دَحَىٰ` (ء ر ض, د ح و); 79:27 `خَلْقًا` (خ ل ق); 79:28 `سَوَّىٰ` (س و ي); 79:36 `بُرِّزَتِ` (ب ر ز)
- Synthesis: Ground, sweeping action, smoothness, breadth, and exposure define a landscape-making process. The scene distinguishes horizontal preparation from vertical building.

#### Subchannel B. Rock Basin, Collected Water, and Fish
- Reading type: latent/lexical
- Scene or process: A depression in hard rock catches rain, water accumulates, and an aquatic habitat forms.
- Active motifs: rock hollow or new well retaining rain (`quranic:root_000434:B011/m01`); water collected in a depression (`quranic:root_000281:B003/m01`); alternate branch for a water hollow (`quranic:root_000282:B002/m01`); water as substance (`quranic:root_001458:B001/m01`); water appearing and increasing in a well (`quranic:root_001458:B002/m01`); fish as water-creature (`quranic:root_000742:B004/m01`); hard stratum stopping excavation (`quranic:root_000217:B005/m02`)
- Ayah anchors: 79:27 `خَلْقًا` (خ ل ق); 79:34 `جَآءَتِ` (ج ي ء); 79:31 `مَآءَ` (م و ه); 79:28 `سَمْكَ` (س م ك); 79:32 `جِبَالَ` (ج ب ل)
- Synthesis: Depression, retaining rock, inflow, accumulation, and aquatic life create a complete reservoir ecology. The duplicate ج ي ء branch IDs remain distinct evidence containers.

#### Subchannel C. Resistant Mountain and Fixed Mass
- Reading type: mixed
- Scene or process: A hard elevated mass arrests digging, resists displacement, and stabilizes the surrounding surface.
- Active motifs: mountain as high solid mass (`quranic:root_000217:B001/m02`); rock that halts the digger (`quranic:root_000217:B005/m03`); long ridge of sand (`quranic:root_000217:B011/m01`); fixing and rooting (`quranic:root_000564:B001/m02`); separating masses by distance (`quranic:root_000131:B003/m01`); sweeping loose material aside (`quranic:root_000462:B002/m02`)
- Ayah anchors: 79:32 `جِبَالَ`/`أَرْسَىٰ` (ج ب ل, ر س و); 79:30 `بَعْدَ`/`دَحَىٰ` (ب ع د, د ح و)
- Synthesis: Loose material is displaced, hard mass remains, and anchoring converts resistance into stability. The scene gives mountains a geotechnical function.

### 23. P3 - Watered Ecology and Provision
- Semantic invariant: Water generates pasture and animal life that becomes durable provision.
- Surface relation: direct; 79:31 brings out water and pasture, and 79:33 names benefit for people and livestock.
- Surprising reach: Provision unfolds as ecological process, animal habitat, usable goods, and bodily or social well-being.

#### Subchannel A. Water, Pasture, and Protective Care
- Reading type: surface-primary
- Scene or process: Water appears, irrigates vegetation, pasture feeds animals, and a caretaker preserves the resource.
- Active motifs: abundant emerging water (`quranic:root_001458:B002/m02`); supplying water by pouring or irrigation (`quranic:root_001458:B003/m01`); pasture and grazing-place (`quranic:root_000574:B001/m01`); pastoral protection and stewardship (`quranic:root_000574:B002/m01`); monitoring an affair's outcome (`quranic:root_000574:B003/m01`); preserving a charge or covenant (`quranic:root_000574:B006/m01`); soft productive ground (`quranic:root_000025:B002/m02`)
- Ayah anchors: 79:31 `مَآءَ`/`مَرْعَىٰ` (م و ه, ر ع ي); 79:30 `أَرْضَ` (ء ر ض)
- Synthesis: Water is the material, irrigation the operation, pasture the produced setting, herd care the social relation, and preservation the outcome.

#### Subchannel B. Ostrich Nest and Morning Grazing
- Reading type: latent/lexical
- Scene or process: An ostrich scrapes a shallow nest into open ground while birds or grazing animals feed in the morning.
- Active motifs: ostrich's scraped nesting hollow (`quranic:root_000462:B003/m01`); ostrich as bird (`quranic:root_001525:B006/m01`); objects compared to an ostrich's form or speed (`quranic:root_001525:B007/m01`); ostrich movement as dispersion or flight (`quranic:root_001525:B008/m01`); morning grazing and meal (`quranic:root_000904:B003/m01`); fertile open earth (`quranic:root_000025:B002/m03`); pasture (`quranic:root_000574:B001/m02`)
- Ayah anchors: 79:30 `دَحَىٰ`/`أَرْضَ` (د ح و, ء ر ض); 79:33 `أَنْعَٰمِ` (ن ع م); 79:29 `ضُحَىٰ` (ض ح و); 79:31 `مَرْعَىٰ` (ر ع ي)
- Synthesis: Nesting action, hollow, bird, open ground, and morning feeding make a compact animal habitat. The ostrich image concretizes `دَحَىٰ` without being treated as its surface translation.

#### Subchannel C. Goods, Enjoyment, and Sustained Benefit
- Reading type: mixed
- Scene or process: Ecological output becomes goods, food, useful equipment, and an extended period of enjoyment.
- Active motifs: benefit and enjoyment (`quranic:root_001395:B001/m01`); goods and provisions used for needs (`quranic:root_001395:B003/m01`); extended life for enjoyment (`quranic:root_001395:B007/m01`); high quality or strength (`quranic:root_001395:B008/m01`); blessing and well-being (`quranic:root_001525:B001/m01`); softness and ease of life (`quranic:root_001525:B002/m01`); livestock wealth (`quranic:root_001525:B005/m01`); agreeable place of settlement (`quranic:root_001525:B011/m01`)
- Ayah anchors: 79:33 `مَتَٰعًا`/`أَنْعَٰمِ` (م ت ع, ن ع م)
- Synthesis: Utility, stored goods, duration, quality, livestock, and settled ease constitute provision as a social economy, not simply as consumption.

### 24. P3 - Darkness, Daybreak, and the Rising Day
- Semantic invariant: Light and darkness are ordered by covering, emergence, extension, and decline.
- Surface relation: direct; 79:29 darkens night and brings out morning light.
- Surprising reach: The daily cycle is constructed through vertical and respiratory imagery: night covers, morning emerges, and daylight rises and opens.

#### Subchannel A. Night Cover and Visual Obscurity
- Reading type: surface-primary
- Scene or process: Night covers the field of vision until route and object become difficult to discern.
- Active motifs: making night intensely dark (`quranic:root_001094:B001/m01`); ocular haze and weak sight (`quranic:root_001094:B002/m01`); pathless dark waste (`quranic:root_001094:B003/m01`); night and its darkness (`quranic:root_001392:B001/m01`); travelling or acting at night (`quranic:root_001392:B002/m01`)
- Ayah anchors: 79:29 `أَغْطَشَ`/`لَيْلَ` (غ ط ش, ل ي ل)
- Synthesis: Darkness is the setting, visual haze the bodily state, pathlessness the navigational outcome, and night travel the pressured action.

#### Subchannel B. Morning Exposure and Clear Brightness
- Reading type: mixed
- Scene or process: Morning extends, exposes surfaces to the sun, and brings a clear visible field out from concealment.
- Active motifs: rising morning interval (`quranic:root_000904:B001/m01`); exposure to sunlight and public visibility (`quranic:root_000904:B002/m01`); clear morning brightness (`quranic:root_000904:B005/m01`); bringing something out from concealment (`quranic:root_000400:B002/m01`); cloud emergence followed by clear sky (`quranic:root_000400:B005/m01`)
- Ayah anchors: 79:29 `ضُحَىٰ`/`أَخْرَجَ` (ض ح و, خ ر ج)
- Synthesis: Extension supplies duration, sunlight supplies illumination, extraction supplies emergence, and clearing supplies visibility. Daybreak is an enacted disclosure.

#### Subchannel C. Daylight Rising to Its Full Height
- Reading type: latent/lexical
- Scene or process: Daylight climbs from morning toward its strongest height and then reaches a bounded span.
- Active motifs: daylight extending and rising (`quranic:root_000904:B001/m02`); extension that reaches its limit (`quranic:root_001395:B002/m01`); high point of day (`quranic:root_000782:B005/m01`); young or high-risen day (`quranic:root_001281:B013/m01`); bounded daylight (`quranic:root_001700:B001/m01`)
- Ayah anchors: 79:29 `ضُحَىٰ` (ض ح و); 79:33 `مَتَٰعًا` (م ت ع); 79:27 `أَشَدُّ` (ش د د); 79:34 `كُبْرَىٰ` (ك ب ر); 79:35 `يَوْمَ` (ي و م)
- Synthesis: Morning begins the ascent, extension carries it upward, height marks the maximum, and “day” bounds the interval. The vertical analogy links temporal progress to the raised architecture of 79:27-28.

### 25. P3 - Catastrophe, Recollection, and Exposure
- Semantic invariant: A final event arrives, overwhelms competing concerns, restores memory, and exposes the outcome to sight.
- Surface relation: direct; 79:34-36 names the great overwhelming event, remembered striving, and displayed fire.
- Surprising reach: Judgment is staged as arrival, flood-like overmastery, retrieval from memory, and forced public visibility.

#### Subchannel A. Arrival that Overwhelms and Levels
- Reading type: surface-primary
- Scene or process: An event arrives with such abundance and force that it covers, dominates, and levels what preceded it.
- Active motifs: arrival and occurrence (`quranic:root_000281:B001/m01`); bringing or forcing something into presence (`quranic:root_000281:B004/m01`); coercive arrival or compulsion (`quranic:root_000281:B005/m01`); mass that rises above and overwhelms (`quranic:root_000952:B002/m01`); sea-like abundance (`quranic:root_000952:B003/m01`); filling a pit until level (`quranic:root_000952:B001/m01`); magnitude and difficulty (`quranic:root_001281:B010/m01`); overcoming a rival (`quranic:root_001281:B011/m01`)
- Ayah anchors: 79:34 `جَآءَتِ`/`طَّآمَّةُ`/`كُبْرَىٰ` (ج ي ء, ط م م, ك ب ر)
- Synthesis: Arrival supplies onset, rising mass supplies force, filling supplies spatial effect, and overcoming supplies relational outcome. The catastrophe is an operation that eliminates rival scales.

#### Subchannel B. Deeds Brought Back into Memory
- Reading type: surface-primary
- Scene or process: A person actively retrieves prior work, recognizes it as his own, and confronts its accumulated character.
- Active motifs: human being as visible person (`quranic:root_000059:B001/m01`); perceiving or sensing a thing (`quranic:root_000059:B002/m01`); retrieval after forgetting (`quranic:root_000516:B003/m01`); speaking or making mention (`quranic:root_000516:B004/m01`); reminder that makes absent content present (`quranic:root_000516:B009/m01`); work and earned action (`quranic:root_000709:B002/m01`); pursuit of honor through action (`quranic:root_000709:B006/m01`); contest in striving (`quranic:root_000709:B008/m01`)
- Ayah anchors: 79:35 `إِنسَٰنُ`/`يَتَذَكَّرُ`/`سَعَىٰ` (ء ن س, ذ ك ر, س ع ي)
- Synthesis: Human subject, sensing, retrieval, naming, work, and competitive effort produce a scene of autobiographical reckoning rather than passive recollection.

#### Subchannel C. Fire Brought into the Open
- Reading type: mixed
- Scene or process: A previously hidden fire is placed in open view, where its heat, glaring eye, and warlike intensity confront the observer.
- Active motifs: uncovering and making visible (`quranic:root_000105:B001/m01`); open exposed field (`quranic:root_000105:B002/m02`); blazing fire and intense heat (`quranic:root_000225:B001/m01`); war at its hottest (`quranic:root_000225:B002/m01`); glaring or inflamed eye (`quranic:root_000225:B003/m01`); face flaring with anger (`quranic:root_000225:B004/m01`); direct sight and insight (`quranic:root_000531:B001/m02`); making another see (`quranic:root_000531:B012/m02`)
- Ayah anchors: 79:36 `بُرِّزَتِ`/`جَحِيمُ`/`يَرَىٰ` (ب ر ز, ج ح م, ر ء ي)
- Synthesis: Exposure is the operation, open field the setting, fire the object, heat and glaring eye its active properties, and seeing the compelled relation. The fire appears almost as a confronting combatant.

### 26. P3 - Inner Formation, Surface Finish, and Deceptive Appearance
- Semantic invariant: A thing's real constitution may agree with, shine through, or be falsified by its visible surface.
- Surface relation: indirect; 79:27 asks about creation, 79:28 proportion, 79:29 visibility, and 79:35-36 recognition and sight.
- Surprising reach: The creation argument reaches into temperament, mirror-like finish, gilding, cosmetics, and deliberate visual deception.

#### Subchannel A. Created Nature and Disposition
- Reading type: latent/lexical
- Scene or process: A formed body bears an inward disposition that may fit or depart from its outward type.
- Active motifs: innate stamped constitution (`quranic:root_000217:B004/m01`); inward nature and temperament (`quranic:root_000434:B004/m01`); complete outward form (`quranic:root_000434:B003/m03`); aptitude or fitness for an act (`quranic:root_000434:B005/m01`); composite bodily constitution (`quranic:root_000156:B002/m02`); creation departing from its expected kind (`quranic:root_000400:B008/m01`); human sociability and personhood (`quranic:root_000059:B003/m01`)
- Ayah anchors: 79:32 `جِبَالَ` (ج ب ل); 79:27 `خَلْقًا`/`بَنَىٰ` (خ ل ق, ب ن ي); 79:29/31 `أَخْرَجَ` (خ ر ج); 79:35 `إِنسَٰنُ` (ء ن س)
- Synthesis: Form, inward nature, aptitude, and deviation from type distinguish ontology from appearance. Human recognition at 79:35 is thereby tied to what kind of self prior acts have formed.

#### Subchannel B. Mirror, Gilding, and Cosmetic Surface
- Reading type: latent/lexical
- Scene or process: A reflective surface beautifies, a thin metallic coating imitates substance, and perfume or cosmetic color completes presentation.
- Active motifs: mirror, visible aspect, and attractive appearance (`quranic:root_000531:B006/m01`); gilding a base metal to disguise it (`quranic:root_001458:B005/m01`); watery lustre in face, speech, or fruit (`quranic:root_001458:B006/m01`); crystal or mirror-like clarity (`quranic:root_001458:B007/m01`); coating with aromatic cosmetic (`quranic:root_000434:B010/m01`); two contrasting colors on one object (`quranic:root_000400:B007/m01`); performing for the gaze of others (`quranic:root_000531:B005/m02`)
- Ayah anchors: 79:36 `يَرَىٰ` (ر ء ي); 79:31 `مَآءَ` (م و ه); 79:27 `خَلْقًا` (خ ل ق); 79:29/31 `أَخْرَجَ` (خ ر ج)
- Synthesis: Reflection and lustre can reveal, while gilding and variegated coating can counterfeit substance. This scene pressures visible “greatness” by asking whether finish corresponds to material.

#### Subchannel C. Emergence into Public View
- Reading type: mixed
- Scene or process: An entity exits concealment, enters open space, and becomes conspicuous enough to be judged.
- Active motifs: emergence from an enclosure or condition (`quranic:root_000400:B001/m01`); extraction from hiddenness (`quranic:root_000400:B002/m02`); disclosure after concealment (`quranic:root_000105:B001/m02`); public prominence through excellence (`quranic:root_000105:B004/m01`); dignified public visibility (`quranic:root_000105:B005/m01`); exposure to sunlight and publicity (`quranic:root_000904:B002/m02`); causing another to see (`quranic:root_000531:B012/m03`)
- Ayah anchors: 79:29/31 `أَخْرَجَ` (خ ر ج); 79:36 `بُرِّزَتِ`/`يَرَىٰ` (ب ر ز, ر ء ي); 79:29 `ضُحَىٰ` (ض ح و)
- Synthesis: Exit, extraction, open placement, conspicuous standing, and observation form a disclosure process. Publicity is an outcome of movement, not a static visual attribute.

### 27. P3 - Confrontation and Overmastery
- Semantic invariant: Opposed agents become visible to each other and test strength until one dominates.
- Surface relation: indirect; 79:27 asks which creation is stronger, 79:34 names an overwhelming event, and 79:36 places the outcome visibly before an observer.
- Surprising reach: Comparative strength becomes a duel scene with open challenge, charge, resistance, and decisive overmastery.

#### Subchannel A. Duel in the Open
- Reading type: latent/lexical
- Scene or process: A fighter leaves the group, faces an opponent in open view, and charges into a direct contest.
- Active motifs: single combat and duel (`quranic:root_000105:B003/m01`); lion as a fighter that comes forward (`quranic:root_000105:B009/m01`); war's intense conflict (`quranic:root_000225:B002/m02`); charge against an enemy (`quranic:root_000782:B003/m01`); partners separating into opposed shares (`quranic:root_000400:B012/m01`); two sides seeing one another (`quranic:root_000531:B004/m01`); overcoming in striving (`quranic:root_000709:B008/m02`)
- Ayah anchors: 79:36 `بُرِّزَتِ`/`جَحِيمُ`/`يَرَىٰ` (ب ر ز, ج ح م, ر ء ي); 79:27 `أَشَدُّ` (ش د د); 79:29/31 `أَخْرَجَ` (خ ر ج); 79:35 `سَعَىٰ` (س ع ي)
- Synthesis: Separation creates opponents, open emergence creates mutual visibility, charge initiates combat, and striving decides it. This is a complete confrontation scene rather than a loose cluster of violence terms.

#### Subchannel B. Rising Mass that Defeats Rival Scale
- Reading type: mixed
- Scene or process: A force grows beyond comparison, rises over its rival, and wins by sheer dominance.
- Active motifs: overwhelming abundance (`quranic:root_000952:B002/m02`); sea-like mass (`quranic:root_000952:B003/m02`); contest and victory through repeated arrival (`quranic:root_000281:B002/m01`); alternate branch for prevailing by arrival (`quranic:root_000282:B001/m01`); overcoming a rival (`quranic:root_001281:B011/m02`); competitive striving (`quranic:root_000709:B008/m03`)
- Ayah anchors: 79:34 `طَّآمَّةُ`/`جَآءَتِ`/`كُبْرَىٰ` (ط م م, ج ي ء, ك ب ر); 79:35 `سَعَىٰ` (س ع ي)
- Synthesis: Magnitude, repeated arrival, and competitive overcoming share a precise dominance invariant. The catastrophe defeats by exceeding every competing measure.

### 28. P4 - Moral Regulation as Overflow, Fall, and Standing
- Semantic invariant: Conduct is a problem of directional control: exceeding a boundary, yielding to downward pull, or holding an upright limit.
- Surface relation: direct; 79:37-40 contrasts transgression and preference with fear, standing before the Lord, and restraining the self from desire.
- Surprising reach: Ethics is materialized through flood dynamics, gravitational fall, posture, and internal braking.

#### Subchannel A. Transgression as Rising Flood and Coercive Height
- Reading type: mixed
- Scene or process: A force exceeds its channel, rises, sweeps away resistance, and converts height into domination.
- Active motifs: exceeding a moral limit (`quranic:root_000937:B001/m02`); flood or sea rising with sweeping force (`quranic:root_000937:B002/m02`); head of misdirection (`quranic:root_000937:B003/m02`); high smooth rock or elevated place (`quranic:root_000937:B005/m01`); water exceeding its measure (`quranic:root_000936:B002/m02`); coercive tyrant (`quranic:root_000936:B004/m02`); proud strength of self (`quranic:root_001533:B014/m01`); lowness and baseness as the opposite pole (`quranic:root_000493:B003/m01`)
- Ayah anchors: 79:37 `طَغَىٰ` (ط غ ي); 79:40 `نَّفْسَ` (ن ف س); 79:38 `دُّنْيَا` (د ن و); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Boundary violation becomes hydraulic excess, hydraulic excess becomes elevated force, and force becomes political domination. The proud self is the internal reservoir of the same upward pressure.

#### Subchannel B. Desire as Inclination, Empty Air, and Plunge
- Reading type: mixed
- Scene or process: The self inclines toward a desired object, loses stable interior support, accelerates, and falls into a depth that becomes its destination.
- Active motifs: desire and inclination of the self (`quranic:root_001609:B004/m01`); empty air and a heart without stability (`quranic:root_001609:B001/m01`); falling into an abyss (`quranic:root_001609:B002/m01`); rapid downward motion (`quranic:root_001609:B008/m01`); false and empty talk (`quranic:root_001609:B010/m01`); preference for a selected object (`quranic:root_000011:B005/m01`); precious object competed over (`quranic:root_001533:B010/m01`); near and lower world (`quranic:root_000493:B002/m01`)
- Ayah anchors: 79:40 `هَوَىٰ`/`نَّفْسَ` (ه و ي, ن ف س); 79:38 `ءَاثَرَ`/`دُّنْيَا` (ء ث ر, د ن و)
- Synthesis: Inclination supplies direction, interior emptiness removes resistance, speed intensifies motion, and abyss supplies outcome. Desire is rendered as a mechanics of destabilization.

#### Subchannel C. Fear, Upright Station, and Internal Prohibition
- Reading type: surface-primary
- Scene or process: Reverent fear makes a person stand, resolve upon restraint, and let reason stop the self before it crosses a boundary.
- Active motifs: expected danger and fear (`quranic:root_000447:B001/m01`); visible fear in the person (`quranic:root_000447:B005/m01`); bodily standing (`quranic:root_001273:B002/m01`); resolve to undertake an affair (`quranic:root_001273:B003/m01`); upright rectitude (`quranic:root_001273:B008/m01`); resurrection-standing before the Lord (`quranic:root_001273:B013/m01`); prohibition and self-restraint (`quranic:root_001560:B001/m01`); reason that prevents ugliness (`quranic:root_001560:B003/m01`); reverent fear (`quranic:root_000413:B001/m03`)
- Ayah anchors: 79:40 `خَافَ`/`مَقَامَ`/`نَهَى` (خ و ف, ق و م, ن ه ي); 79:45 `يَخْشَىٰ` (خ ش ي)
- Synthesis: Fear is the activating state, standing the posture, resolve the decision, reason the internal regulator, and prohibition the completed operation. This is controlled verticality against overflow and fall.

### 29. P4 - Final Lodgings as Hostile and Protective Enclosures
- Semantic invariant: A life-course ends by entering an environment that either consumes or shelters its inhabitant.
- Surface relation: direct; 79:39 and 79:41 name fire and garden as the two `مَأْوَىٰ` outcomes.
- Surprising reach: The destinations develop into complete habitats: one exposes through heat and combat, the other covers through vegetation, shield, water, and care.

#### Subchannel A. Inferno as Heat, Battle, and Hostile Gaze
- Reading type: mixed
- Scene or process: A blazing enclosure attacks through heat, warlike intensity, glaring sight, and inflamed anger.
- Active motifs: intense blazing fire (`quranic:root_000225:B001/m02`); deadly heat of war (`quranic:root_000225:B002/m03`); glaring inflamed eye (`quranic:root_000225:B003/m02`); face flaming with anger (`quranic:root_000225:B004/m02`); shameless exposure (`quranic:root_000225:B005/m01`); lodging that gathers its occupant (`quranic:root_000070:B001/m01`); plunge into a depth (`quranic:root_001609:B002/m02`)
- Ayah anchors: 79:39 `جَحِيمَ`/`مَأْوَىٰ` (ج ح م, ء و ي); 79:40 `هَوَىٰ` (ه و ي)
- Synthesis: Heat is the material condition, battle the active relation, glaring eye the perceptual force, anger the facial manifestation, and lodging the enclosing outcome.

#### Subchannel B. Garden as Covered, Watered Habitat
- Reading type: mixed
- Scene or process: Dense vegetation covers an inhabitant, water sustains growth, and the enclosure becomes a settled refuge.
- Active motifs: covering and concealment (`quranic:root_000266:B001/m01`); garden hidden by trees (`quranic:root_000266:B003/m01`); dense, flourishing vegetation (`quranic:root_000266:B011/m01`); sheltered place (`quranic:root_000266:B017/m01`); abundant water (`quranic:root_000532:B013/m04`); persistent green plant (`quranic:root_000532:B012/m03`); lodging and gathering refuge (`quranic:root_000070:B001/m02`); compassionate reception (`quranic:root_000070:B002/m01`)
- Ayah anchors: 79:41 `جَنَّةَ`/`مَأْوَىٰ` (ج ن ن, ء و ي); 79:40/44 `رَبِّ` (ر ب ب)
- Synthesis: Cover, tree-density, water, plant life, lodging, and compassion form an inhabitable garden ecology. Concealment here is protective, not epistemic failure.

#### Subchannel C. Shielded Refuge and Preserved Life
- Reading type: latent/lexical
- Scene or process: A vulnerable person enters a defended place, receives protection, and is preserved under covenant.
- Active motifs: protective shield (`quranic:root_000266:B008/m01`); hidden refuge (`quranic:root_000266:B017/m02`); compassionate sheltering (`quranic:root_000070:B002/m02`); covenant of protection (`quranic:root_000532:B011/m03`); preservation of life (`quranic:root_000383:B006/m01`); life as benefit and rescue (`quranic:root_000383:B013/m01`); stationary place of residence (`quranic:root_001273:B006/m01`)
- Ayah anchors: 79:41 `جَنَّةَ`/`مَأْوَىٰ` (ج ن ن, ء و ي); 79:40/44 `رَبِّ` (ر ب ب); 79:38 `حَيَوٰةَ` (ح ي ي); 79:40 `مَقَامَ` (ق و م)
- Synthesis: Refuge, shield, compassionate host, covenant, preserved life, and residence define a social protection scene nested within the garden outcome.

### 30. P4 - Anchorage, Terminal Basin, and Compressed Stay
- Semantic invariant: Motion and duration terminate in a fixed point beyond which no further course remains.
- Surface relation: direct; 79:42 asks for the Hour's mooring, 79:44 assigns its endpoint to the Lord, and 79:46 compresses worldly stay.
- Surprising reach: Eschatological timing is materialized through ship anchorage, floodwater settling in a terminal pool, and a traveller's brief lodging.

#### Subchannel A. Mooring under a Captain
- Reading type: mixed
- Scene or process: A vessel ceases movement at its mooring under a captain whose authority governs arrival.
- Active motifs: stability and rooting (`quranic:root_000564:B001/m03`); ship stopping at its anchorage (`quranic:root_000564:B002/m01`); captain of sailors (`quranic:root_000532:B017/m03`); enduring residence (`quranic:root_000532:B007/m01`); lodging that gathers (`quranic:root_000070:B001/m03`)
- Ayah anchors: 79:42 `مُرْسَىٰ` (ر س و); 79:40/44 `رَبِّ` (ر ب ب); 79:39/41 `مَأْوَىٰ` (ء و ي)
- Synthesis: Vessel, stopping action, mooring, captain, and lodging form a complete arrival scene. The Hour's `مُرْسَىٰ` is thus a fixed arrival under command, not merely a date.

#### Subchannel B. Overflow Settling in Its Terminal Pool
- Reading type: latent/lexical
- Scene or process: Floodwater exceeds its course, reaches the valley's end, settles into a pool, and becomes fixed.
- Active motifs: water rising beyond measure (`quranic:root_000937:B002/m03`); alternate overflowing-water branch (`quranic:root_000936:B002/m03`); terminal pool where floodwater settles (`quranic:root_001560:B004/m01`); fixing and settling (`quranic:root_000564:B001/m04`); abundant water (`quranic:root_000532:B013/m05`); water that sustains the self (`quranic:root_001533:B008/m01`)
- Ayah anchors: 79:37 `طَغَىٰ` (ط غ ي); 79:40/44 `نَهَى`/`مُنتَهَىٰ` (ن ه ي); 79:42 `مُرْسَىٰ` (ر س و); 79:40/44 `رَبِّ` (ر ب ب); 79:40 `نَّفْسَ` (ن ف س); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Overflow, channel-end, pooling, and fixed settlement create a hydrological terminus. It is distinct from the moral flood scene because its active operation is containment rather than domination.

#### Subchannel C. Brief Lodging between Evening and Morning
- Reading type: surface-primary
- Scene or process: A stay that seemed long collapses, when seen from its endpoint, into a single evening or morning interval.
- Active motifs: staying in a place (`quranic:root_001339:B001/m01`); delay and slowness (`quranic:root_001339:B002/m01`); bounded daylight (`quranic:root_001700:B001/m02`); duration of time (`quranic:root_001700:B002/m01`); evening interval (`quranic:root_001017:B004/m01`); rising morning (`quranic:root_000904:B001/m03`); near or lower world (`quranic:root_000493:B002/m02`)
- Ayah anchors: 79:46 `يَلْبَثُ`/`يَوْمَ`/`عَشِيَّةً`/`ضُحَىٰ` (ل ب ث, ي و م, ع ش و, ض ح و); 79:38 `دُّنْيَا` (د ن و)
- Synthesis: Residence and delay define experienced duration; evening, morning, and bounded day provide its measure; final sight collapses that measure into a brief lodging.

### 31. P4 - Choice, Value, and the Trace that Remains
- Semantic invariant: Preference assigns value now, while enduring trace reveals what the choice actually produced.
- Surface relation: direct; 79:38 names preference for near life, 79:40 names the self and desire, and 79:43 names remembrance.
- Surprising reach: Moral choice becomes a market of scarce attention, prized objects, exclusive possession, and durable evidence.

#### Subchannel A. Preference and Exclusive Possession
- Reading type: mixed
- Scene or process: A person places one option first, favors it, and seeks to reserve it for himself.
- Active motifs: choosing an action first (`quranic:root_000011:B001/m01`); preferring one object or person (`quranic:root_000011:B005/m02`); exclusive appropriation (`quranic:root_000011:B006/m01`); near and lower option (`quranic:root_000493:B002/m03`); base or diminished rank (`quranic:root_000493:B003/m02`); life as practical benefit (`quranic:root_000383:B013/m02`)
- Ayah anchors: 79:38 `ءَاثَرَ`/`دُّنْيَا`/`حَيَوٰةَ` (ء ث ر, د ن و, ح ي ي)
- Synthesis: Ordering, preference, appropriation, proximity, and utility form a valuation decision. The “near life” is attractive because it is immediately available and usable, not because it is intrinsically higher.

#### Subchannel B. Precious Self and Competitive Desire
- Reading type: latent/lexical
- Scene or process: A valuable object draws competing selves, produces possessive desire, and shapes inward intention.
- Active motifs: precious thing competed over (`quranic:root_001533:B010/m02`); self as exact identity and substance (`quranic:root_001533:B012/m01`); inward intention and thought (`quranic:root_001533:B013/m01`); pride and force of self (`quranic:root_001533:B014/m02`); desire and attachment (`quranic:root_001609:B004/m02`); requested object or wish (`quranic:root_000661:B002/m01`)
- Ayah anchors: 79:40 `نَّفْسَ`/`هَوَىٰ` (ن ف س, ه و ي); 79:42 `يَسْـَٔلُ` (س ء ل)
- Synthesis: Preciousness creates competition, competition recruits desire, and desire settles into inward intention and pride. The self is both valuer and contested object.

#### Subchannel C. Trace, Record, and Public Memory
- Reading type: mixed
- Scene or process: An act leaves a mark, the mark is tracked, preserved as report, and later restored to memory.
- Active motifs: enduring trace of what occurred (`quranic:root_000011:B003/m01`); following a prior trace (`quranic:root_000011:B004/m01`); narrated tradition (`quranic:root_000011:B002/m01`); marked hoof used for tracking (`quranic:root_000011:B008/m01`); practiced knowledge of a trace (`quranic:root_000011:B011/m01`); recollection after absence (`quranic:root_000516:B003/m02`); public mention and reputation (`quranic:root_000516:B007/m01`); legal record of a right (`quranic:root_000516:B008/m01`)
- Ayah anchors: 79:38 `ءَاثَرَ` (ء ث ر); 79:43 `ذِكْرَىٰ` (ذ ك ر)
- Synthesis: Mark, tracker, report, expertise, recollection, reputation, and document form an evidentiary chain. What was preferred becomes knowable by the trace it leaves.

### 32. P4 - Question, Knowledge Boundary, and Warning
- Semantic invariant: Inquiry seeks hidden timing, but authorized communication is limited to reminder and warning.
- Surface relation: direct; 79:42-45 moves from questioning about the Hour to the Lord's endpoint and the messenger's warning.
- Surprising reach: The exchange distinguishes request, reciprocal questioning, remembered knowledge, report, and alarm as separate communicative acts.

#### Subchannel A. Request, Desired Answer, and Reciprocal Questioning
- Reading type: surface-primary
- Scene or process: Questioners seek a desired piece of knowledge and circulate the question among themselves.
- Active motifs: asking and seeking (`quranic:root_000661:B001/m01`); desired object of a question (`quranic:root_000661:B002/m02`); satisfying a request (`quranic:root_000661:B003/m01`); reciprocal questioning (`quranic:root_000661:B004/m01`); reminder that restores the topic (`quranic:root_000516:B009/m02`); interrogative prompting for information (`quranic:root_000531:B013/m01`)
- Ayah anchors: 79:42 `يَسْـَٔلُ` (س ء ل); 79:43 `ذِكْرَىٰ` (ذ ك ر); 79:46 `يَرَ` (ر ء ي)
- Synthesis: Request, desired content, attempted satisfaction, mutual circulation, prompting, and reminder form the inquiry scene. The sought object is not conflated with the act of asking.

#### Subchannel B. Remembered Knowledge and Its Limit
- Reading type: mixed
- Scene or process: Knowledge is retrieved and articulated only up to the endpoint assigned to its proper authority.
- Active motifs: inward recollection (`quranic:root_000516:B003/m03`); articulation and mention (`quranic:root_000516:B004/m02`); reminder as an instrument (`quranic:root_000516:B009/m03`); divine or cultivated knowledge (`quranic:root_000532:B003/m03`); endpoint and limit (`quranic:root_001560:B002/m01`); sufficient point that stops further seeking (`quranic:root_001560:B005/m01`); abandoned pursuit of a request (`quranic:root_001560:B007/m01`)
- Ayah anchors: 79:43 `ذِكْرَىٰ` (ذ ك ر); 79:44 `رَبِّ`/`مُنتَهَىٰ` (ر ب ب, ن ه ي)
- Synthesis: Recollection and articulation explain what can be communicated; endpoint, sufficiency, and cessation define where inquiry stops. The boundary is jurisdictional, not a failure of reminder.

#### Subchannel C. Warning that Produces Vigilant Fear
- Reading type: surface-primary
- Scene or process: A messenger announces danger so that the hearer develops visible, reverent caution.
- Active motifs: warning that awakens vigilance (`quranic:root_001488:B001/m01`); obligation voluntarily assumed (`quranic:root_001488:B002/m01`); expected danger (`quranic:root_000447:B001/m02`); making another afraid for protection (`quranic:root_000447:B002/m01`); fear becoming visible (`quranic:root_000447:B005/m02`); reverent fear (`quranic:root_000413:B001/m04`); knowledge through reverence (`quranic:root_000413:B002/m03`)
- Ayah anchors: 79:45 `مُنذِرُ`/`يَخْشَىٰ` (ن ذ ر, خ ش ي); 79:40 `خَافَ` (خ و ف)
- Synthesis: Announcement supplies information, fear supplies alert, visible reaction supplies evidence of reception, and reverence converts alarm into durable restraint.

### 33. P4 - Seeing, Dimming, and the Hidden Interior
- Semantic invariant: Judgment moves between what is exposed to sight, what is obscured, and what is hidden within the self.
- Surface relation: direct; 79:40 names the inward self, 79:41 a covered garden, and 79:46 final seeing across evening and morning.
- Surprising reach: Perception is distributed across eyes, face, dim light, hidden heart, and mental restraint.

#### Subchannel A. Final Seeing and Exposed Countenance
- Reading type: mixed
- Scene or process: An object enters view, faces become legible, and sight recognizes what was previously deferred.
- Active motifs: sensory seeing and insight (`quranic:root_000531:B001/m03`); mutual visibility (`quranic:root_000531:B004/m02`); visible aspect or mirror image (`quranic:root_000531:B006/m02`); making another see (`quranic:root_000531:B012/m04`); human face (`quranic:root_000383:B012/m01`); face inflamed by anger (`quranic:root_000225:B004/m03`); exposure to daylight (`quranic:root_000904:B002/m03`)
- Ayah anchors: 79:46 `يَرَ`/`ضُحَىٰ` (ر ء ي, ض ح و); 79:38 `حَيَوٰةَ` (ح ي ي); 79:39 `جَحِيمَ` (ج ح م)
- Synthesis: Seeing is the operation, exposed face the readable surface, daylight the condition, and mutual visibility the relation. Judgment becomes a face-to-face disclosure.

#### Subchannel B. Evening Dimness and Blind Advance
- Reading type: mixed
- Scene or process: In weak evening light, impaired sight produces uncertain movement and deliberate avoidance of what should be seen.
- Active motifs: first darkness of evening (`quranic:root_001017:B001/m01`); weak night vision (`quranic:root_001017:B006/m01`); blind, erratic advance (`quranic:root_001017:B007/m01`); deliberate turning away or feigned blindness (`quranic:root_001017:B003/m01`); false empty speech (`quranic:root_001609:B010/m02`); visible fear (`quranic:root_000447:B005/m03`)
- Ayah anchors: 79:46 `عَشِيَّةً` (ع ش و); 79:40 `هَوَىٰ`/`خَافَ` (ه و ي, خ و ف)
- Synthesis: Low light, impaired eye, erratic motion, and chosen avoidance form one failed-perception scene. It contrasts with final seeing without treating evening itself as morally defective.

#### Subchannel C. Concealed Heart, Self, and Preventive Reason
- Reading type: latent/lexical
- Scene or process: The inward self holds intention and fear behind a covering until reason checks its impulse.
- Active motifs: concealment from sense (`quranic:root_000266:B001/m02`); heart hidden in the chest (`quranic:root_000266:B010/m01`); mind covered by derangement (`quranic:root_000266:B006/m01`); living self or soul (`quranic:root_001533:B011/m01`); exact inward identity (`quranic:root_001533:B012/m02`); intention and thought (`quranic:root_001533:B013/m02`); reason that prohibits wrong (`quranic:root_001560:B003/m02`)
- Ayah anchors: 79:41 `جَنَّةَ` (ج ن ن); 79:40 `نَّفْسَ`/`نَهَى` (ن ف س, ن ه ي)
- Synthesis: Covering supplies the interior boundary, heart and self the participant, intention the content, derangement the failure mode, and reason the regulating tool.

### 34. P4 - False Cult and True Lordship
- Semantic invariant: Ultimate orientation is determined by what is treated as sovereign and worthy of worship.
- Surface relation: indirect; 79:37 names transgression, 79:40 and 79:44 name the Lord, and 79:42 supplies a root whose lexical branch names the idol Suwa.
- Surprising reach: The question about the Hour is pressured by an alternate cultic scene in which a named idol and taghut compete with true lordship.

#### Subchannel A. Taghut and the Idol Suwa
- Reading type: latent/lexical
- Scene or process: A transgressive head of misdirection becomes an object of obedience or worship, represented concretely by the idol Suwa.
- Active motifs: taghut as head of error and false worship (`quranic:root_000937:B003/m03`); tyrannical head of coercion (`quranic:root_000936:B004/m03`); taghut as false object of worship (`quranic:root_000936:B003/m02`); idol named Suwa (`quranic:root_000760:B003/m01`); hidden spirits (`quranic:root_000266:B005/m01`)
- Ayah anchors: 79:37 `طَغَىٰ` (ط غ ي); 79:42 `سَّاعَةِ` (س و ع); 79:41 `جَنَّةَ` (ج ن ن); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Transgression supplies the social relation, taghut the governing role, Suwa the concrete cult object, and hidden spirits the unseen constituency. The scene remains lexical but directly pressures misplaced eschatological concern.

#### Subchannel B. Lord as Owner, Cultivator, and Final Authority
- Reading type: mixed
- Scene or process: The true Lord owns, cultivates, teaches, protects by covenant, and alone fixes the endpoint.
- Active motifs: divine ownership and lordship (`quranic:root_000532:B001/m03`); cultivation and repair (`quranic:root_000532:B002/m04`); learned divine knowledge (`quranic:root_000532:B003/m04`); covenant and protection (`quranic:root_000532:B011/m04`); responsible captaincy (`quranic:root_000532:B017/m04`); stewardship and preservation (`quranic:root_001273:B004/m01`); final endpoint (`quranic:root_001560:B002/m02`)
- Ayah anchors: 79:40/44 `رَبِّ` (ر ب ب); 79:40 `مَقَامَ` (ق و م); 79:44 `مُنتَهَىٰ` (ن ه ي)
- Synthesis: Ownership establishes authority, cultivation and knowledge its beneficent activity, covenant its relation, captaincy its coordination, and endpoint its exclusive jurisdiction.

### 35. P4 - Hidden Gestation and Compressed Life-Span
- Semantic invariant: Life is bounded by hidden formation, emergence, maturation, and a retrospectively brief duration.
- Surface relation: indirect; 79:38 names life, 79:40 the self, 79:41 concealment, and 79:46 the compressed day-span.
- Surprising reach: Eschatological time is reframed by reproductive time: concealed life approaches birth, emerges, and later appears as no more than an evening or morning.

#### Subchannel A. Concealed Embryo, Birth, and New Life
- Reading type: latent/lexical
- Scene or process: Life is hidden in a womb, approaches delivery, emerges with birth-fluid, and is preserved as a vulnerable new being.
- Active motifs: fetus hidden in the womb (`quranic:root_000266:B007/m01`); birth and postpartum blood (`quranic:root_001533:B005/m01`); approaching parturition (`quranic:root_000493:B004/m01`); ewe newly delivered (`quranic:root_000532:B009/m02`); living creature or soul (`quranic:root_000383:B003/m01`); preserving life rather than killing (`quranic:root_000383:B006/m02`); reproductive fluid before emission (`quranic:root_000760:B005/m01`)
- Ayah anchors: 79:41 `جَنَّةَ` (ج ن ن); 79:40 `نَّفْسَ` (ن ف س); 79:38 `دُّنْيَا`/`حَيَوٰةَ` (د ن و, ح ي ي); 79:40/44 `رَبِّ` (ر ب ب); 79:42 `سَّاعَةِ` (س و ع)
- Synthesis: Concealment is the setting, embryo the participant, approach the temporal state, birth the operation, and preservation the outcome. The reproductive branch of س و ع remains distinct from its surface use for the Hour.

#### Subchannel B. Evening, Morning, and a Life Reduced to One Interval
- Reading type: surface-primary
- Scene or process: A lived duration is remeasured at final sight as one late-day or early-day interval.
- Active motifs: evening and late day (`quranic:root_001017:B004/m02`); evening meal and grazing (`quranic:root_001017:B005/m01`); morning interval (`quranic:root_000904:B001/m04`); morning meal and grazing (`quranic:root_000904:B003/m02`); daylight as one bounded day (`quranic:root_001700:B001/m03`); duration as any span (`quranic:root_001700:B002/m02`); a segment of night or long while (`quranic:root_001609:B006/m01`); staying and delay (`quranic:root_001339:B001/m02`)
- Ayah anchors: 79:46 `عَشِيَّةً`/`ضُحَىٰ`/`يَوْمَ`/`يَلْبَثُ` (ع ش و, ض ح و, ي و م, ل ب ث); 79:40 `هَوَىٰ` (ه و ي)
- Synthesis: Evening and morning are not interchangeable labels: each carries its own light, food, and activity. Final sight compresses the whole stay into either edge of a single day.

## Standalone Subchannels

### S1. P1 - Falcon Capture and Bird Augury
- Reading type: latent/lexical
- Scene or process: A trained raptor is fitted, released, and reads as both hunter and omen-bearing bird.
- Active motifs: falcon seizing prey in its talons (`quranic:root_001505:B011/m01`); jesses fastened to a bird's legs (`quranic:root_000671:B003/m01`); bird movement read for augury (`quranic:root_000624:B002/m01`); bird or star as a physical follower (`quranic:root_000175:B008/m01`)
- Ayah anchors: 79:2 `نَّٰشِطَٰتِ` (ن ش ط); 79:4 `سَّٰبِقَٰتِ` (س ب ق); 79:13 `زَجْرَةٌ` (ز ج ر); 79:7 `تَتْبَعُ` (ت ب ع)
- Synthesis: Equipment, release, predatory capture, and divinatory reading make a compact falconry scene whose directed flight echoes the opening sequence.

### S2. P1 - Snake and Sudden Bite
- Reading type: latent/lexical
- Scene or process: A pale snake approaches and strikes with its fang.
- Active motifs: snake or viper bite (`quranic:root_001505:B008/m01`); white snake named by resemblance to a bracelet (`quranic:root_001248:B009/m01`)
- Ayah anchors: 79:2 `نَّٰشِطَٰتِ` (ن ش ط); 79:8 `قُلُوبٌ` (ق ل ب)
- Synthesis: The snake supplies the agent and the bite the operation. Its sudden, penetrating seizure is a formed predation scene despite its small evidence footprint.

### S3. P1 - Wakefulness after the Event
- Reading type: mixed
- Scene or process: Sleep is removed by a severe event, leaving the subject awake through an extended interval.
- Active motifs: sleeplessness and night wakefulness (`quranic:root_000752:B001/m01`); severe occurrence attached to a day (`quranic:root_001700:B003/m01`); duration of time (`quranic:root_001700:B002/m01`); event occurring in time (`quranic:root_001332:B001/m02`)
- Ayah anchors: 79:14 `سَّاهِرَةِ` (س ه ر); 79:6 `يَوْمَ` (ي و م); 79:11 `كُ` (ك و ن)
- Synthesis: Event, temporal duration, lost sleep, and wakeful state form a direct experiential scene for the sudden arrival on the `سَّاهِرَةِ`.

### S4. P2 - Gold, Silver, and Reflective Display
- Reading type: latent/lexical
- Scene or process: Gold is seen, worked into a surface coating, paired with silver beads, and inspected in a mirror.
- Active motifs: gold as metal (`quranic:root_000522:B001/m01`); gilding and plating (`quranic:root_000522:B002/m01`); dazzlement at the sight of gold (`quranic:root_000522:B003/m01`); red-yellow metallic color (`quranic:root_000522:B004/m01`); gold used as a measure (`quranic:root_000522:B008/m01`); strung silver beads (`quranic:root_001206:B006/m01`); mirror and visible appearance (`quranic:root_000531:B006/m03`)
- Ayah anchors: 79:17 `ٱذْهَبْ` (ذ ه ب); 79:16 `مُقَدَّسِ` (ق د س); 79:20 `أَرَىٰ` (ر ء ي)
- Synthesis: Material, craft operation, color, ornament, valuation, dazzled observer, and mirror produce a coherent luxury-display scene.

### S5. P2 - Stranger Incorporated at a Household Boundary
- Reading type: latent/lexical
- Scene or process: A stranger enters a group, crosses a property boundary, and is either incorporated through household care or excluded by lineage.
- Active motifs: stranger entering a people not his own (`quranic:root_000009:B006/m01`); fostered dependent and caretaker (`quranic:root_000532:B005/m02`); family to whom one returns (`quranic:root_000067:B003/m02`); bride incorporated into a household (`quranic:root_001583:B006/m02`); lineage inclining to a noble origin (`quranic:root_001487:B010/m01`); herd as owned property (`quranic:root_000532:B014/m03`)
- Ayah anchors: 79:15 `أَتَىٰ` (ء ت ي); 79:16/24 `رَبُّ` and 79:19 `رَبِّ` (ر ب ب); 79:25 `أُولَىٰٓ` (ء و ل); 79:19 `أَهْدِيَ` (ه د ي); unavailable for ن د ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Entry, boundary, dependency, marriage, property, and lineage create a social incorporation scene. The unavailable lineage root is not assigned a surface token.

### S6. P2 - Charge, Hesitation, and Failed Flight
- Reading type: latent/lexical
- Scene or process: A combatant begins a charge, falters, looks back, and is seized.
- Active motifs: charge that proves true or false (`quranic:root_001290:B004/m01`); wild animal running then stopping to look behind (`quranic:root_001290:B007/m01`); turning the back in retreat (`quranic:root_000458:B003/m03`); sharp light arrow or spear-point (`quranic:root_000324:B006/m01`); wrestling seizure (`quranic:root_000018:B011/m02`); recoiling from conflict in fear (`quranic:root_001554:B002/m02`)
- Ayah anchors: 79:21 `كَذَّبَ` (ك ذ ب); 79:22 `أَدْبَرَ` (د ب ر); 79:23 `حَشَرَ` (ح ش ر); 79:25 `أَخَذَ`/`نَكَالَ` (ء خ ذ, ن ك ل)
- Synthesis: Charge, faltering, backward glance, retreat, and capture form a complete failed-combat sequence that concretizes Pharaoh's reversal.

### S7. P3 - Governance as Repair and Provision
- Reading type: latent/lexical
- Scene or process: A leader measures needs, repairs the common structure, and converts foresight into public benefit.
- Active motifs: leader of a people or army (`quranic:root_000462:B005/m01`); chiefs likened to mountains (`quranic:root_000217:B012/m01`); measuring before action (`quranic:root_000434:B001/m02`); inward deliberation and foresight (`quranic:root_000531:B002/m02`); useful benefit (`quranic:root_001395:B001/m02`); blessing and welfare (`quranic:root_001525:B001/m02`)
- Ayah anchors: 79:30 `دَحَىٰ` (د ح و); 79:32 `جِبَالَ` (ج ب ل); 79:27 `خَلْقًا` (خ ل ق); 79:36 `يَرَىٰ` (ر ء ي); 79:33 `مَتَٰعًا`/`أَنْعَٰمِ` (م ت ع, ن ع م)
- Synthesis: Leader, senior advisers, measurement, foresight, and welfare define governance as constructive care, providing a social analogue to cosmic engineering.

### S8. P3 - Filled Shaft and Stone Closure
- Reading type: latent/lexical
- Scene or process: A shaft in rock is excavated, packed with material, and brought level until the opening is closed.
- Active motifs: hard rock resisting excavation (`quranic:root_000217:B005/m04`); rock hollow retaining water (`quranic:root_000434:B011/m02`); solid imperforate stone (`quranic:root_000434:B012/m01`); filling and leveling a pit (`quranic:root_000952:B001/m02`); broad smooth surface (`quranic:root_000766:B009/m03`)
- Ayah anchors: 79:32 `جِبَالَ` (ج ب ل); 79:27 `خَلْقًا` (خ ل ق); 79:34 `طَّآمَّةُ` (ط م م); 79:28 `سَوَّىٰ` (س و ي)
- Synthesis: Rock, cavity, fill, closure, and final level surface form one earthwork operation distinct from the open reservoir scene.

### S9. P4 - Snake, Life, and Hidden Spirit
- Reading type: latent/lexical
- Scene or process: A snake is named through “life,” concealed under the jinn-root, and perceived as an uncanny hidden presence.
- Active motifs: snake derived from the life-root (`quranic:root_000383:B004/m01`); jann as snake (`quranic:root_000266:B012/m01`); spirit or jinn appearing to a seer (`quranic:root_000531:B008/m01`); living soul (`quranic:root_001533:B011/m02`)
- Ayah anchors: 79:38 `حَيَوٰةَ` (ح ي ي); 79:41 `جَنَّةَ` (ج ن ن); 79:46 `يَرَ` (ر ء ي); 79:40 `نَّفْسَ` (ن ف س)
- Synthesis: Snake, concealed kind, uncanny perception, and living soul create a compact lexical scene around life that is hidden yet mobile.

### S10. P4 - Vow, Injury, Valuation, and Claim
- Reading type: latent/lexical
- Scene or process: A person assumes an obligation, injury creates a compensable claim, value is assessed, and a legal record preserves the right.
- Active motifs: self-imposed vow (`quranic:root_001488:B002/m02`); injury carrying obligatory compensation (`quranic:root_001488:B003/m01`); requested claim (`quranic:root_000661:B002/m03`); satisfaction of a petition (`quranic:root_000661:B003/m02`); pricing and valuation (`quranic:root_001273:B010/m01`); legal record of a right (`quranic:root_000516:B008/m02`); covenant (`quranic:root_000532:B011/m05`); abandonment of a pursued claim (`quranic:root_001560:B007/m02`)
- Ayah anchors: 79:45 `مُنذِرُ` (ن ذ ر); 79:42 `يَسْـَٔلُ` (س ء ل); 79:40 `مَقَامَ` (ق و م); 79:43 `ذِكْرَىٰ` (ذ ك ر); 79:40/44 `رَبِّ` (ر ب ب); 79:40/44 `نَهَى`/`مُنتَهَىٰ` (ن ه ي)
- Synthesis: Vow creates obligation, injury creates a claim, petition activates it, valuation quantifies it, record and covenant preserve it, and abandonment terminates it.

### S11. P4 - Unattended Herd and Moral Drift
- Reading type: latent/lexical
- Scene or process: Livestock are released without control, drift through pasture, and are contrasted with a recently delivered animal kept under care.
- Active motifs: camels neglected to wander at will (`quranic:root_000760:B002/m01`); young wild bovine (`quranic:root_000936:B009/m02`); gathered herd (`quranic:root_000532:B014/m04`); ewe kept near shelter after birth (`quranic:root_000532:B009/m03`); approaching delivery (`quranic:root_000493:B004/m02`)
- Ayah anchors: 79:42 `سَّاعَةِ` (س و ع); 79:40/44 `رَبِّ` (ر ب ب); 79:38 `دُّنْيَا` (د ن و); unavailable for ط غ و (`surface_context.root_coverage.missing_roots`)
- Synthesis: Release without direction, wandering young, herd, maternal vulnerability, and sheltering care form a husbandry contrast that materially reframes unrestrained desire.

### S12. Honey Harvest from Swarm to Thickened Store
- Reading type: latent/lexical
- Scene or process: A honey collector approaches a swarm, extracts honey with a dedicated implement, receives it in a leather pouch, and the collected liquid thickens.
- Active motifs: swarm of bees or wasps (`quranic:root_000458:B014/m01`); honey collector's extraction tool (`quranic:root_001489:B010/m01`); leather pouch carried for gathered honey (`quranic:root_000447:B006/m01`); honey thickening after collection (`quranic:root_000067:B005/m01`)
- Ayah anchors: 79:1 `نَّٰزِعَٰتِ` (ن ز ع); 79:5 `مُدَبِّرَٰتِ` and 79:22 `أَدْبَرَ` (د ب ر); 79:25 `أُولَىٰٓ` (ء و ل); 79:40 `خَافَ` (خ و ف)
- Synthesis: Swarm, extractor, implement, receptacle, and thickened product form a complete harvesting mechanism. It materializes the opening's extraction and the surah's creation-to-provision arc as hazardous, skilled retrieval in which dispersed motion yields a concentrated good.

### S13. Summoned Prayer, Standing, and Counting Beads
- Reading type: latent/lexical
- Scene or process: A call summons worshippers, they stand in prayer and glorification, and repeated praises are counted on beads.
- Active motifs: summons to come to prayer (`quranic:root_000383:B009/m01`); standing in prayer or remembrance (`quranic:root_001273:B002/m02`); tasbih as prayer and worship (`quranic:root_000666:B001/m01`); beads used to count tasbih (`quranic:root_000666:B006/m01`)
- Ayah anchors: 79:3 `سَّٰبِحَٰتِ`/`سَبْحًا` (س ب ح); 79:38 `حَيَوٰةَ` (ح ي ي); 79:40 `مَقَامَ` (ق و م)
- Synthesis: Summons, bodily response, devotional action, and counting instrument make one enacted rite. It reframes the opening's swimming motion as disciplined worship and pressures Pharaoh's public call with a rival summons answered by standing before the Lord.

### S14. Bier, Shroud, and Grave
- Reading type: latent/lexical
- Scene or process: The dead body is carried on a bier, enclosed in a shroud, and concealed in a grave.
- Active motifs: bier or carrier for the dead (`quranic:root_000067:B008/m01`); shroud enclosing the dead (`quranic:root_000266:B009/m01`); grave concealing the dead (`quranic:root_000266:B009/m02`)
- Ayah anchors: 79:25 `أُولَىٰٓ` (ء و ل); 79:41 `جَنَّةَ` (ج ن ن)
- Synthesis: Carrier, wrapping, burial place, and concealment form the successive operations of interment. This materializes the human closure placed after death, which the surah's single cry and return decisively reverse by bringing the concealed dead back into presence.

### S15. Measured Hide Tanning and Leather Garment
- Reading type: latent/lexical
- Scene or process: A hide is measured before cutting, treated with a small dose of tanning material derived from foliage, and finished as a leather garment.
- Active motifs: hide measured before cutting (`quranic:root_000434:B001/m03`); alaa foliage used for tanning (`quranic:root_000076:B005/m01`); one or two doses of tanning agent (`quranic:root_001533:B007/m01`); child's leather shirt or strong leather cloak (`quranic:root_000666:B007/m01`)
- Ayah anchors: 79:3 `سَّٰبِحَٰتِ`/`سَبْحًا` (س ب ح); 79:27 `خَلْقًا` (خ ل ق); 79:40 `نَّفْسَ` (ن ف س); unavailable for ء ل ي (`surface_context.root_coverage.missing_roots`)
- Synthesis: Measurement governs the cut, foliage supplies the tanning material, dosage controls treatment, and the garment is the finished outcome. The craft materializes creation, proportion, and purification as measured transformation from exposed hide into protective covering.

### S16. Scaling and Salting Fish
- Reading type: latent/lexical
- Scene or process: A scaled fish is prepared by removing its outer covering and preserving it with salt.
- Active motifs: zajr or zajur fish (`quranic:root_000624:B003/m01`); peeling or scaling a fish (`quranic:root_001505:B004/m01`); fish cured in salt (`quranic:root_001505:B009/m01`)
- Ayah anchors: 79:2 `نَّٰشِطَٰتِ`/`نَشْطًا` (ن ش ط); 79:13 `زَجْرَةٌ` (ز ج ر)
- Synthesis: Fish, removable surface, preparation, and salt-preserved outcome form a compact food craft. It materializes the opening's swimmers and the surah's water-based provision in human use: aquatic motion becomes durable sustenance.

### S17. Concealed-Hand Even-or-Odd Game
- Reading type: latent/lexical
- Scene or process: One player grips small objects in a closed hand, another calls whether their number is even or odd, and the hand opens to disclose the result.
- Active motifs: objects gripped in the palm for play (`quranic:root_000637:B005/m01`); even or paired versus odd call (`quranic:root_000637:B005/m02`); hand game requiring its contents to be brought out (`quranic:root_000400:B010/m01`)
- Ayah anchors: 79:18 `تَزَكَّىٰ` (ز ك و); 79:29/31 `أَخْرَجَ` (خ ر ج)
- Synthesis: Concealment, numerical choice, competing guess, and forced reveal form one complete game. It usefully pressures the questioning about the Hour: guessing at hidden contents cannot determine disclosure, which arrives only when what is concealed is brought out.

### S18. Curdled Milk, Clarified Fat, and Thick Condiment
- Reading type: latent/lexical
- Scene or process: Milk thickens, its concentrated fat or clarified extract is recovered, and a dense residue or syrup is used to improve food.
- Active motifs: milk thickening or curdling (`quranic:root_000067:B005/m02`); clarified extract of ghee or milk (`quranic:root_000011:B009/m01`); thick syrup or ghee-and-oil residue used to improve food (`quranic:root_000532:B006/m01`)
- Ayah anchors: 79:16/24 `رَبُّ` and 79:19/40/44 `رَبِّ` (ر ب ب); 79:25 `أُولَىٰٓ` (ء و ل); 79:38 `ءَاثَرَ` (ء ث ر)
- Synthesis: Coagulation, concentration, recovery, and reuse turn a perishable liquid into dense nourishment. This materializes the surah's water-pasture-livestock provision as a full productive chain whose benefit is processed and retained rather than left as raw abundance.

### S19. Protruding Abscess and Suppuration
- Reading type: latent/lexical
- Scene or process: A boil emerges from the body, pus gathers inside it, and the affected tissue festers.
- Active motifs: protruding boil or ulcer (`quranic:root_000400:B004/m01`); pus gathering in an abscess (`quranic:root_000281:B006/m01`); sore festering and corrupting with pus (`quranic:root_000025:B011/m01`)
- Ayah anchors: 79:29/31 `أَخْرَجَ` (خ ر ج); 79:30 `أَرْضَ` (ء ر ض); 79:34 `جَآءَتِ` (ج ي ء)
- Synthesis: Lesion, accumulated matter, internal corruption, and outward protrusion form one pathology. It reframes hidden moral corruption and final exposure through a bodily analogue: what festers inwardly eventually forces itself into view, sharpening the surah's display of remembered striving and exposed fire.

### S20. P1-P3-P4 - Possibility Answered, Timing Withheld
- Reading type: mixed
- Scene or process: P1 challenges whether return to a former state can occur, P3 answers through a comparison of creative power, and P4 asks for a temporal endpoint that is not disclosed.
- Active motifs: return to a former place or state (`quranic:root_000555:B001/m01`); creating and producing (`quranic:root_000434:B002/m01`); strength and solidity (`quranic:root_000782:B002/m01`); asking and seeking (`quranic:root_000661:B001/m01`); endpoint and limit (`quranic:root_001560:B002/m01`)
- Ayah anchors: P1 79:10 `مَرْدُودُونَ` (ر د د); P3 79:27 `خَلْقًا`/`أَشَدُّ` (خ ل ق, ش د د); P4 79:42 `يَسْـَٔلُ` (س ء ل), 79:44 `مُنتَهَىٰ` (ن ه ي)
- Synthesis: Bridge (discourse role progression and contrast): P1's possibility challenge is answered in P3 by the greater-creation comparison, whereas P4's timing demand terminates at the Lord's endpoint rather than receiving a date. The sequence distinguishes power to enact the return from human access to its schedule.

### S21. P2-P3-P4 - The Offered Sign Becomes Unavoidable Sight
- Reading type: mixed
- Scene or process: P2 presents a great sign for recognition, P3 repeats greatness as the catastrophe arrives and becomes visible, and P4 compresses worldly duration under retrospective sight.
- Active motifs: showing a thing to another (`quranic:root_000531:B012/m01`); great scale (`quranic:root_001281:B001/m01`); arrival and occurrence (`quranic:root_000281:B001/m01`); direct sight and insight (`quranic:root_000531:B001/m02`)
- Ayah anchors: P2 79:20 `أَرَىٰ`/`كُبْرَىٰ` (ر ء ي, ك ب ر); P3 79:34 `جَآءَتِ`/`كُبْرَىٰ` (ج ي ء, ك ب ر), 79:36 `يَرَىٰ` (ر ء ي); P4 79:46 `يَرَ` (ر ء ي)
- Synthesis: Bridge (repeated scene signature, causal escalation, and role reversal): P2's `كُبْرَىٰ` is a sign shown to a viewer who can refuse it; P3's `كُبْرَىٰ` is the event that arrives, after which P3-P4 seeing is no longer optional. Offered evidence becomes compelled recognition.

### S22. P2-P3-P4 - Striving Becomes Remembered Evidence and Lodging
- Reading type: mixed
- Scene or process: P2 embodies purposeful striving in a historical actor, P3 turns striving into recalled personal evidence, and P4 gives the resulting person a final lodging.
- Active motifs: purposeful movement to a sought object (`quranic:root_000709:B001/m01`); work and earned action (`quranic:root_000709:B002/m01`); retrieval after forgetting (`quranic:root_000516:B003/m01`); lodging that gathers its occupant (`quranic:root_000070:B001/m01`)
- Ayah anchors: P2 79:22 `يَسْعَىٰ` (س ع ي); P3 79:35 `يَتَذَكَّرُ`/`سَعَىٰ` (ذ ك ر, س ع ي); P4 79:39/41 `مَأْوَىٰ` (ء و ي)
- Synthesis: Bridge (causal sequence and role progression): P2 supplies a concrete act of striving, P3 converts every person's striving into remembered evidence, and P4 converts that evidence-bearing history into an assigned abode. Action passes from present pursuit to recollection and finally to settled consequence.

### S23. P2-P4 - Pharaoh's Role Generalized and His Claim Reversed
- Reading type: mixed
- Scene or process: P2 names a ruler who crosses the limit and claims supreme lordship; P4 repeats the transgressor as a general role and places standing and finality with the true Lord.
- Active motifs: exceeding the limit in disobedience (`quranic:root_000937:B001/m01`); exceeding a moral limit (`quranic:root_000937:B001/m02`); lordship, ownership, and mastery (`quranic:root_000532:B001/m01`); divine ownership and lordship (`quranic:root_000532:B001/m03`)
- Ayah anchors: P2 79:16/19/24 `رَبُّ`/`رَبِّ` (ر ب ب), 79:17 `طَغَىٰ` (ط غ ي); P4 79:37 `طَغَىٰ` (ط غ ي), 79:40/44 `رَبِّ` (ر ب ب)
- Synthesis: Bridge (typological role progression and authority reversal): P2's named transgressor becomes P4's general moral type through the repeated `طَغَىٰ`. At the same time, Pharaoh's claim to highest lordship is reversed by the Lord before whose station one fears and with whom the Hour's endpoint rests.

### S24. P1-P2-P4 - Fear Moves from Seizure to Disciplined Foresight
- Reading type: mixed
- Scene or process: P1 registers fear as involuntary cardiac disturbance, P2 makes reverent fear receptive to guidance and admonition, and P4 turns expected danger into restraint before the Lord.
- Active motifs: palpitation of a fearful heart (`quranic:root_001628:B002/m01`); fear joined to reverence (`quranic:root_000413:B001/m01`); knowledge expressed through khashya (`quranic:root_000413:B002/m01`); expected danger and fear (`quranic:root_000447:B001/m01`); prohibition and self-restraint (`quranic:root_001560:B001/m01`)
- Ayah anchors: P1 79:8 `وَاجِفَةٌ` (و ج ف); P2 79:19/26 `تَخْشَىٰ`/`يَخْشَىٰٓ` (خ ش ي); P4 79:40 `خَافَ`/`نَهَى` (خ و ف, ن ه ي), 79:45 `يَخْشَىٰ` (خ ش ي)
- Synthesis: Bridge (role progression and contrast): P1's fear merely records the event after seizure; P2's fear can receive knowledge before refusal hardens; P4's fear anticipates judgment and restrains desire before action. Reactive terror is contrasted with reverence that changes conduct.

### S25. P3-P4 - Fixed Mountains, Hidden Temporal Anchorage
- Reading type: mixed
- Scene or process: P3 anchors mountains in space, while P4 asks for the Hour's anchorage in time but withholds that temporal mooring from human access.
- Active motifs: fixing and rooting (`quranic:root_000564:B001/m02`); ship stopping at its anchorage (`quranic:root_000564:B002/m01`)
- Ayah anchors: P3 79:32 `أَرْسَىٰ` (ر س و); P4 79:42 `مُرْسَىٰ` (ر س و)
- Synthesis: Bridge (same-root functional analogy and contrast): `أَرْسَىٰ` fixes a spatial mass, while `مُرْسَىٰ` transfers anchorage to a temporal event. Creation supplies stable ground, but the questioner cannot moor the Hour to a disclosed point on the human calendar.

### S26. P1-P3-P4 - Event-Time Expands and World-Time Contracts
- Reading type: mixed
- Scene or process: P1 concentrates resurrection into one vocal impulse, P3 establishes morning as a created interval, and P4 contracts an entire worldly stay into an evening or morning.
- Active motifs: repelling shout (`quranic:root_000624:B001/m01`); numerical oneness (`quranic:root_001631:B002/m01`); rising morning interval (`quranic:root_000904:B001/m01`); staying in a place (`quranic:root_001339:B001/m01`); evening interval (`quranic:root_001017:B004/m01`)
- Ayah anchors: P1 79:13 `زَجْرَةٌ`/`وَٰحِدَةٌ` (ز ج ر, و ح د); P3 79:29 `ضُحَىٰ` (ض ح و); P4 79:46 `يَلْبَثُ`/`عَشِيَّةً`/`ضُحَىٰ` (ل ب ث, ع ش و, ض ح و)
- Synthesis: Bridge (repeated temporal signature and scale reversal): one moment in P1 unfolds the decisive event, while the long stay reviewed in P4 collapses to one daily interval. P3's created morning supplies the stable cosmic measure against which remembered worldly duration contracts.

### S27. P3-P4 - Provision Is Given; Preference Is Judged
- Reading type: mixed
- Scene or process: P3 presents earthly benefit as provision for humans and livestock, while P4 locates culpability in preferring the near life as the governing end.
- Active motifs: benefit and enjoyment (`quranic:root_001395:B001/m01`); goods and provisions used for needs (`quranic:root_001395:B003/m01`); preference for a selected object (`quranic:root_000011:B005/m01`); near and lower world (`quranic:root_000493:B002/m01`)
- Ayah anchors: P3 79:33 `مَتَٰعًا` (م ت ع); P4 79:38 `ءَاثَرَ`/`دُّنْيَا` (ء ث ر, د ن و)
- Synthesis: Bridge (contrast and causal qualification): P3 positively assigns created goods the role of provision; P4 condemns the act of ranking that provision as the ultimate preference. The reversal distinguishes receiving and using worldly benefit from making the near world one's governing end.


