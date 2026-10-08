Surah: 65. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S65 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s065/surah.r2/text.md =====
# Surah 65

- 65:1 يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَطَلِّقُوهُنَّ لِعِدَّتِهِنَّ وَأَحْصُوا۟ ٱلْعِدَّةَ ۖ وَٱتَّقُوا۟ ٱللَّهَ رَبَّكُمْ ۖ لَا تُخْرِجُوهُنَّ مِنۢ بُيُوتِهِنَّ وَلَا يَخْرُجْنَ إِلَّآ أَن يَأْتِينَ بِفَٰحِشَةٍۢ مُّبَيِّنَةٍۢ ۚ وَتِلْكَ حُدُودُ ٱللَّهِ ۚ وَمَن يَتَعَدَّ حُدُودَ ٱللَّهِ فَقَدْ ظَلَمَ نَفْسَهُۥ ۚ لَا تَدْرِى لَعَلَّ ٱللَّهَ يُحْدِثُ بَعْدَ ذَٰلِكَ أَمْرًۭا
- 65:2 فَإِذَا بَلَغْنَ أَجَلَهُنَّ فَأَمْسِكُوهُنَّ بِمَعْرُوفٍ أَوْ فَارِقُوهُنَّ بِمَعْرُوفٍۢ وَأَشْهِدُوا۟ ذَوَىْ عَدْلٍۢ مِّنكُمْ وَأَقِيمُوا۟ ٱلشَّهَٰدَةَ لِلَّهِ ۚ ذَٰلِكُمْ يُوعَظُ بِهِۦ مَن كَانَ يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مَخْرَجًۭا
- 65:3 وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ ۚ وَمَن يَتَوَكَّلْ عَلَى ٱللَّهِ فَهُوَ حَسْبُهُۥٓ ۚ إِنَّ ٱللَّهَ بَٰلِغُ أَمْرِهِۦ ۚ قَدْ جَعَلَ ٱللَّهُ لِكُلِّ شَىْءٍۢ قَدْرًۭا
- 65:4 وَٱلَّٰٓـِٔى يَئِسْنَ مِنَ ٱلْمَحِيضِ مِن نِّسَآئِكُمْ إِنِ ٱرْتَبْتُمْ فَعِدَّتُهُنَّ ثَلَٰثَةُ أَشْهُرٍۢ وَٱلَّٰٓـِٔى لَمْ يَحِضْنَ ۚ وَأُو۟لَٰتُ ٱلْأَحْمَالِ أَجَلُهُنَّ أَن يَضَعْنَ حَمْلَهُنَّ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا
- 65:5 ذَٰلِكَ أَمْرُ ٱللَّهِ أَنزَلَهُۥٓ إِلَيْكُمْ ۚ وَمَن يَتَّقِ ٱللَّهَ يُكَفِّرْ عَنْهُ سَيِّـَٔاتِهِۦ وَيُعْظِمْ لَهُۥٓ أَجْرًا
- 65:6 أَسْكِنُوهُنَّ مِنْ حَيْثُ سَكَنتُم مِّن وُجْدِكُمْ وَلَا تُضَآرُّوهُنَّ لِتُضَيِّقُوا۟ عَلَيْهِنَّ ۚ وَإِن كُنَّ أُو۟لَٰتِ حَمْلٍۢ فَأَنفِقُوا۟ عَلَيْهِنَّ حَتَّىٰ يَضَعْنَ حَمْلَهُنَّ ۚ فَإِنْ أَرْضَعْنَ لَكُمْ فَـَٔاتُوهُنَّ أُجُورَهُنَّ ۖ وَأْتَمِرُوا۟ بَيْنَكُم بِمَعْرُوفٍۢ ۖ وَإِن تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُۥٓ أُخْرَىٰ
- 65:7 لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ ۖ وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ ۚ لَا يُكَلِّفُ ٱللَّهُ نَفْسًا إِلَّا مَآ ءَاتَىٰهَا ۚ سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا
- 65:8 وَكَأَيِّن مِّن قَرْيَةٍ عَتَتْ عَنْ أَمْرِ رَبِّهَا وَرُسُلِهِۦ فَحَاسَبْنَٰهَا حِسَابًۭا شَدِيدًۭا وَعَذَّبْنَٰهَا عَذَابًۭا نُّكْرًۭا
- 65:9 فَذَاقَتْ وَبَالَ أَمْرِهَا وَكَانَ عَٰقِبَةُ أَمْرِهَا خُسْرًا
- 65:10 أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا ۖ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟ ۚ قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا
- 65:11 رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
- 65:12 ٱللَّهُ ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ وَمِنَ ٱلْأَرْضِ مِثْلَهُنَّ يَتَنَزَّلُ ٱلْأَمْرُ بَيْنَهُنَّ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ وَأَنَّ ٱللَّهَ قَدْ أَحَاطَ بِكُلِّ شَىْءٍ عِلْمًۢا


===== _commentary/v16/work/s065/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ب ء (root_001464): 65:1 ٱلنَّبِىُّ

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

## ط ل ق (root_000946): 65:1 طَلَّقْتُمُ, 65:1 فَطَلِّقُوهُنَّ

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

## ن س و (root_001500): 65:1 ٱلنِّسَآءَ, 65:4 نِّسَآئِكُمْ

- **B001** kadın topluluğunu bildiren ayrı biçimli çoğullar — kadınlar topluluğu; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu; aynı biçimden tekili bulunmayan çoğul · kadınlar; tekil kadın adından ayrı biçimli çoğul · kadınlar topluluğu adının küçültme biçimi · kadınlar topluluğu adının çoğul küçültme biçimi
  النُّسوة والنِّسوان والنِّسون كله جملة النساء (ayn)؛ النَّسوة والنُّسوة والنساء والنِّسوان جمع امرأة من غير لفظها وتصغير نسوة نسية ونسيات (sihah)؛ النساء والنسوان والنسوة جمع المرأة من غير لفظها (mufradat)

## ع د د (root_000989): 65:1 لِعِدَّتِهِنَّ, 65:1 ٱلْعِدَّةَ, 65:4 فَعِدَّتُهُنَّ, 65:10 أَعَدَّ (also echo for 65:1 يَتَعَدَّ)

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

## ح ص ي (root_000332): 65:1 وَأَحْصُوا۟

- **B001** çakıl taşı, çakıllar ve çakıllı arazi — küçük taşlar, çakıl · tek bir çakıl taşı · çakıl taşları · çakıllı arazi
  الحصى صغار الحجارة والواحدة حصاة وثلاث حصيات (ayn;tahdhib)؛ الحصاة واحدة الحصى وتجمع على حصيات (sihah)؛ أرض محصاة ذات حصى (sihah)
- **B002** sayıp sayısını eksiksiz belirleme — çakıl kadar çok sayı · onlardan sayıca daha çok · şeyi saydı · sayarak miktarı belirleme ve sayısını eksiksiz bilme · her şeyin sayısını eksiksiz belirleyip bilgisiyle kuşattı · onu koruyamayacak, ona güç yetiremeyecek ya da onu elde edemeyeceksiniz · onları bilgiyle, inanarak ve kesin bir kanaatle kavradı
  والحصى العدد الكثير شبه بحصى الحجارة لكثرتها (ayn)؛ الحصى كثرة العدد شبه بحصى الحجارة في الكثرة (tahdhib)؛ أحصيت الشيء عددته (sihah)؛ الإحصاء إحاطة العلم باستقصاء العدد (ayn)؛ أحاط علمه باستيفاء عدد كل شيء (tahdhib)؛ الإحصاء التحصيل بالعدد (mufradat)
- **B003** sağlam akıl, ağırbaşlılık ve ketum sağduyu — kişinin ağırbaşlılığı · kişinin kendini denetlemesini sağlayan akıl · akıllı ve sağduyulu; tedbirli ve ketum · tedbirli, ketum ve sırrını koruyan · aklı güçlü · aklı güçlü · aklı güçlü
  حصاة الرجل رزانته (ayn)؛ حصاة العقل لأن المرء يحصي بها على نفسه (ayn)؛ فلان ذو حصاة أي ذو عقل ولب (sihah)؛ فلان ذو حصاة وأصاة إذا كان حازما كتوما على نفسه يحفظ سره (tahdhib)؛ فلان حصي وحصيف ومستحص إذا كان شديد العقل (tahdhib)
- **B004** dilin sivri ve keskin oluşu [kalıp] — dilin sivriliği ve sözdeki keskinliği
  حصاة اللسان ذرابته (ayn;tahdhib)؛ وهل يكب الناس على مناخرهم في جهنم إلا حصا ألسنتهم ويقال حصائد (ayn)؛ والرواية الصحيحة إلا حصائد ألسنتهم (tahdhib)
- **B005** misk kesesindeki katı koku maddesi parçası [kalıp] — misk kesesinde bulunan katı misk parçası
  لكل قطعة من المسك حصاة (ayn;tahdhib)؛ حصاة المسك قطعة صلبة توجد في فأرة المسك (sihah)
- **B006** idrarın koyulaşıp taşlaşmasına bağlı mesane taşı hastalığı — idrarın koyulaşıp sertleşmesiyle oluşan mesane taşı hastalığı · mesane taşı hastalığına tutuldu · mesane taşı hastalığına tutulmuş kişi
  الحصاة داء يقع في المثانة يخثر البول فيشتد حتى يصير كالحصاة (ayn)؛ الحصاة داء في المثانة وهو أن يخثر البول فيشتد حتى يصير كالحصاة يقال حصي الرجل فهو محصي (tahdhib)

## و ق ي (root_001677): 65:1 وَٱتَّقُوا۟, 65:2 يَتَّقِ, 65:4 يَتَّقِ, 65:5 يَتَّقِ, 65:10 فَٱتَّقُوا۟

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

## ء ل ه (root_000047): 65:1 ٱللَّهَ, 65:1 ٱللَّهِ, 65:1 ٱللَّهِ, 65:1 ٱللَّهَ, 65:2 لِلَّهِ, 65:2 بِٱللَّهِ, 65:2 ٱللَّهَ, 65:3 ٱللَّهِ, 65:3 ٱللَّهَ, 65:3 ٱللَّهُ, 65:4 ٱللَّهَ, 65:5 ٱللَّهِ, 65:5 ٱللَّهَ, 65:7 ٱللَّهُ, 65:7 ٱللَّهُ, 65:7 ٱللَّهُ, 65:10 ٱللَّهُ, 65:10 ٱللَّهَ, 65:10 ٱللَّهُ, 65:11 ٱللَّهِ, 65:11 بِٱللَّهِ, 65:11 ٱللَّهُ, 65:12 ٱللَّهُ, 65:12 ٱللَّهَ, 65:12 ٱللَّهَ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 65:1 ٱللَّهَ, 65:1 ٱللَّهِ, 65:1 ٱللَّهِ, 65:1 ٱللَّهَ, 65:2 لِلَّهِ, 65:2 بِٱللَّهِ, 65:2 ٱللَّهَ, 65:3 ٱللَّهِ, 65:3 ٱللَّهَ, 65:3 ٱللَّهُ, 65:4 ٱللَّهَ, 65:5 ٱللَّهِ, 65:5 ٱللَّهَ, 65:7 ٱللَّهُ, 65:7 ٱللَّهُ, 65:7 ٱللَّهُ, 65:10 ٱللَّهُ, 65:10 ٱللَّهَ, 65:10 ٱللَّهُ, 65:11 ٱللَّهِ, 65:11 بِٱللَّهِ, 65:11 ٱللَّهُ, 65:12 ٱللَّهُ, 65:12 ٱللَّهَ, 65:12 ٱللَّهَ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ر ب ب (root_000532): 65:1 رَبَّكُمْ, 65:8 رَبِّهَا

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

## ECHO ر ب و (root_000537): for 65:1 رَبَّكُمْ, 65:8 رَبِّهَا: withheld observed target; not identity

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

## خ ر ج (root_000400): 65:1 تُخْرِجُوهُنَّ, 65:1 يَخْرُجْنَ, 65:2 مَخْرَجًا, 65:11 لِّيُخْرِجَ

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

## ب ي ت (root_000166): 65:1 بُيُوتِهِنَّ

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

## ء ت ي (root_000009): 65:1 يَأْتِينَ, 65:6 فَـَٔاتُوهُنَّ, 65:7 ءَاتَىٰهُ, 65:7 ءَاتَىٰهَا

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

## ف ح ش (root_001134): 65:1 بِفَٰحِشَةٍ

- **B001** ağır ve yüz kızartıcı çirkinlik — ağır ve ürkütücü çirkinlik · çok çirkin ve yüz kızartıcı şey · doğru olana uymayan ağır çirkin iş
  تدل على قبح في شيء وشناعة (maqayis)؛ الفحش معروف والفحشاء اسم للفاحشة (ayn;tahdhib)؛ الفحش معروف (jamhara)؛ الفحشاء الفاحشة (sihah)؛ ما عظم قبحه من الأفعال والأقوال (mufradat)
- **B002** hoş karşılanmayan ölçü aşımı — sınırını aştığı için hoş karşılanmayan · iş sınırını aştı ve ağırlaştı · giderek daha aşırı ve çirkin duruma gelmek
  كل شيء جاوز قدره فهو فاحش ولا يكون ذلك إلا فيما يتكره (maqayis)؛ كل شئ جاوز حده فهو فاحش (sihah)؛ كل شيء جاوز حده وقدره فهو فاحش (tahdhib)
- **B003** ağır çirkin söz söyleme veya davranışta bulunma — ağır çirkin söz söylemek veya davranışta bulunmak · utanmazca konuşur veya davranır duruma gelmek · sık sık ağır çirkin söz söyleyen veya davranan · birine ağır çirkin sözler söylemek · konuşmasında bilerek sövgüye ve çirkinliğe başvurmak · insanlara sövmeyi ve kırıcı konuşmayı bilerek sürdüren kişi
  أفحش الرجل قال الفحش وفحش وهو فحاش (maqayis)؛ أفحش في القول والعمل (ayn)؛ جاء الرجل بالفحش والفحشاء إذا أفحش (jamhara)؛ أفحش عليه في المنطق أي قال الفحش وتفحش في كلامه (sihah)؛ قال قولا فاحشا وذو الفحش والخنا من قول وفعل والمتفحش الذي يتكلف سب الناس (tahdhib)؛ ما عظم قبحه من الأفعال والأقوال والمتفحش الذي يأتي بالفحش (mufradat)
- **B004** yasaklanmış ağır davranış — evlilik dışı cinsel ilişki · boşanmış kadının kendisini boşayan kocasının izni olmadan evden çıkması · kadının kocasının yakınlarına kırıcı ve saldırgan konuşması · cinsel yoldan çıkma · evlilik dışı cinsel ilişki veya cinsel yoldan çıkma · yasaklanmış ağır davranışı yapan kişi
  فاحشة مبينة يعني خروجها من بيتها بغير إذن زوجها المطلقها (ayn)؛ ربما جعلوا الفحشاء الفجور (jamhara)؛ يسمى الزنى فاحشة (sihah)؛ الفاحشة المبينة أن تزني أو خروجها من بيتها أو بذاءتها وسلاطة لسانها والفاحشة المنهي عنها وجمعها الفواحش (tahdhib)؛ كناية عن الزنا واللاتي يأتين الفاحشة (mufradat)
- **B005** aşırı cimrilik — cimri veya vermekte aşırı katı kişi · cimrilik
  الفاحش البخيل وهذا على الاتساع والبخل أقبح خصال المرء (maqayis)؛ الذي جاوز الحد في البخل (sihah)؛ الفحشاء هاهنا البخل والعرب تسمي البخيل فاحشا (tahdhib)؛ العظيم القبح في البخل (mufradat)

## ب ي ن (root_000170): 65:1 مُّبَيِّنَةٍ, 65:6 بَيْنَكُم, 65:11 مُبَيِّنَٰتٍ, 65:12 بَيْنَهُنَّ

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

## ح د د (root_000002): 65:1 حُدُودُ, 65:1 حُدُودَ

- **B001** ayıran ve kapsamı belirleyen sınır — iki şeyi ayıran sınır · bir şeyin son noktası · ayırt edici tanım · Tanrı'nın aşılmaması gereken hükümleri · arazisi ya da evi bitişik komşu
  الحد الحاجز بين الشيئين (maqayis;sihah;mufradat)؛ منتهى كل شيء حده (sihah;tahdhib)؛ حدود الأرضين وحدود الحرم (tahdhib)؛ حدود الله هي الأشياء التي بين تحريمها وتحليلها (tahdhib)؛ الوصف المحيط بمعناه المميز له عن غيره (mufradat)
- **B002** engelleme ve geri çevirme — engelleme; geri çevirme · girişi engelleyen kapıcı · çıkışı engelleyen gardiyan · paydan ya da geçimden yoksun · dokunulmaz ve yapılması yasak iş · Tanrı korusun; kesinlikle olmaz · bu işten kaçışım yok · yeniden suç işlemeyi caydıran din hukuku cezası · birini kötülükten alıkoymak
  الأصل الأول المنع (maqayis)؛ للبواب حداد لمنعه الناس (maqayis;sihah;tahdhib;mufradat)؛ السجان حداد لأنه يمنع من الخروج (sihah;tahdhib)؛ محدود ممنوع من البخت أو الرزق (maqayis;sihah;mufradat)؛ حد العاصي لأنه يمنعه عن المعاودة (maqayis;sihah;tahdhib;mufradat)؛ دون ذلك حدد أي منع (sihah;tahdhib)؛ حددا بمعنى معاذ الله أو حراما (maqayis;sihah;tahdhib)
- **B003** karşı çıkma ve direnme — karşı çıkma, başkaldırma ve direnme · karşı çıkıp gerekeni esirgeme · ona karşı geldim · onlara sataşıp çekişmek
  المحادة المخالفة فكأنه الممانعة (maqayis)؛ المحادة المخالفة ومنع ما يجب عليك وكذلك التحاد (sihah)؛ حاددته أي عاصيته (tahdhib)؛ يقال تحدد بهم أي تحرش بهم (tahdhib)؛ يحادون الله ورسوله أي يمانعون (mufradat)
- **B004** sert ve dayanıklı demir — sert ve dayanıklı demir madeni · demir parçası · demirci
  سمي الحديد حديدا لامتناعه وصلابته وشدته (maqayis)؛ الحديد معروف والحديدة أخص منه والجمع الحدائد (sihah)؛ الحديد معروف وصانعه الحداد ويقال ضربه بحديدة (tahdhib)؛ الحديد معروف وأنزلنا الحديد فيه بأس شديد (mufradat)
- **B005** keskin ağız ve nüfuz eden etki — kılıcın keskin ağzı · bıçağın keskin ağzı · keskin ve etkili diller · keskin görüş ve kavrayış
  الأصل الآخر طرف الشيء (maqayis)؛ حد السيف وهو حرفه وحد السكين (maqayis)؛ حد كل شيء شباته (sihah;tahdhib)؛ حد السنان وحد السيف ما دق من شفرته (tahdhib)؛ سيوف حداد وألسنة حداد (sihah;mufradat)؛ بصرك اليوم حديد وحديد النظر وحديد الفهم (tahdhib;mufradat)؛ حددت السكين رققت حده (mufradat)
- **B006** sertlik, atılgan güç ve öfkeli taşkınlık — içkinin sertliği · adamın gücü ve atılganlığı · öfkeli acelecilik ve taşkınlık · öfkesi kabarmak
  حد الشراب صلابته (maqayis;sihah;tahdhib)؛ حد الرجل بأسه (maqayis;sihah;tahdhib)؛ الحدة التي تعتري الإنسان من النزق (maqayis;sihah)؛ الحدة الغضبة (tahdhib)؛ حد يحد إذا أخذته عجلة وطيش (tahdhib)
- **B007** eş için süsten kaçınarak yas tutma — kocası için süsten kaçınarak yas tutmak · kocası için süsten kaçınarak yas tutmak · siyah yas giysileri
  حدت المرأة على بعلها وأحدت إذا منعت نفسها الزينة والخضاب (maqayis)؛ أحدت المرأة امتنعت من الزينة والخضاب بعد وفاة زوجها (sihah)؛ حدت أربعة أشهر وعشرا (tahdhib)؛ إحداد المرأة على زوجها تركها الزينة مأخوذ من المنع (tahdhib)؛ الحداد أيضا ثياب المأتم السود (sihah)
- **B008** demir araç kullanma, tıraş etme ve bileme — demir araç kullanma · kasık kıllarını tıraş etme · bıçak ağzını bileyip keskinleştirme · bıçak ağzını bileyip keskinleştirme
  الاستحداد استعمال الحديد (maqayis)؛ تحديد الشفرة وإحدادها واستحدادها بمعنى (sihah)؛ الاستحداد أيضا حلق شعر العانة (sihah)؛ الاستحداد حلق العانة (tahdhib)؛ استحد الرجل إذا أحد شفرة بحديدة وغيرها (tahdhib)

## ع د و (root_000993): 65:1 يَتَعَدَّ

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

## ECHO ع و د (root_001058): for 65:1 يَتَعَدَّ: withheld observed target; not identity

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

## ظ ل م (root_000967): 65:1 ظَلَمَ, 65:11 ٱلظُّلُمَٰتِ

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

## ن ف س (root_001533): 65:1 نَفْسَهُۥ, 65:7 نَفْسًا

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

## د ر ي (root_000473): 65:1 تَدْرِى

- **B001** bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme — bir şeyi bilmek veya ondan haberdar olmak · birine bildirmek, onun bilmesini sağlamak · bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi · bilmiyorum
  دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)
- **B002** saldırı amacıyla bir yer ya da kişiyi seçmek [kalıp] — bir yeri baskın veya saldırı için seçmek
  أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)
- **B003** avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak — avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan · avı gizlenip aldatarak atış menziline getirmek · hileyle kandırmak
  الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)
- **B004** sivri uç ve bundan ad alan saç düzeltme aracı — sivri boynuz; saçı düzeltmeye yarayan sivri araç · saçı ayırıp düzeltmeye yarayan şiş biçimli araç · saçını tarayıp düzeltmek
  الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)
- **B005** saplama ve atış alıştırma hedefi — üzerinde saplama alıştırması yapılan hedef
  الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)
- **B006** insanlarla yumuşak ve incelikli geçinmek [kalıp] — insanlara karşı yumuşak ve uzlaştırıcı davranmak
  مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)

## ECHO د ر ر (root_000469): for 65:1 تَدْرِى: withheld observed target; not identity

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

## ح د ث (root_000299): 65:1 يُحْدِثُ

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

## ب ع د (root_000131): 65:1 بَعْدَ, 65:7 بَعْدَ

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

## ء م ر (root_000051): 65:1 أَمْرًا, 65:3 أَمْرِهِۦ, 65:4 أَمْرِهِۦ, 65:5 أَمْرُ, 65:6 وَأْتَمِرُوا۟, 65:8 أَمْرِ, 65:9 أَمْرِهَا, 65:9 أَمْرِهَا, 65:12 ٱلْأَمْرُ

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

## ب ل غ (root_000151): 65:2 بَلَغْنَ, 65:3 بَٰلِغُ

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

## ء ج ل (root_000016): 65:2 أَجَلَهُنَّ, 65:4 أَجَلُهُنَّ

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

## م س ك (root_001424): 65:2 فَأَمْسِكُوهُنَّ

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

## ع ر ف (root_001002): 65:2 بِمَعْرُوفٍ, 65:2 بِمَعْرُوفٍ, 65:6 بِمَعْرُوفٍ

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

## ف ر ق (root_001148): 65:2 فَارِقُوهُنَّ

- **B001** ayırt edip birbirinden ayırma — iki şeyi birbirinden ayırıp ayırt etmek · kişilerin birbirinden ayrılması ve uzaklaşması · konunun açıklığa kavuşması · metni sağlamlaştırıp hükümlerini açıklamak ve bölümlendirmek
  أصيل صحيح يدل على تمييز وتزييل بين شيئين (maqayis)؛ الفرق تفريق بين شيئين حتى يفترقا ويتفرقا (ayn)؛ فرقت بين الشيئين أفرق فرقا وفرقانا (sihah)؛ فرقت أفرق بين الكلام وفرقت بين الأجسام (tahdhib)؛ فرقت بين الشيئين فصلت بينهما سواء كان ذلك بفصل يدركه البصر أو بفصل تدركه البصيرة (mufradat)؛ الفراق والمفارقة تكون بالأبدان أكثر (mufradat)؛ فرق لي هذا الأمر إذا تبين ووضح (tahdhib)
- **B002** parçalara ayırıp dağıtma — parçalara ayırma ve dağıtma · ayrı zamanlarda bölümler halinde ulaştırmak · sürüyü dağıtan kokarca
  أخذت حقي منه بالتفاريق (sihah)؛ قرآنا فرقناه من شدد قال أنزلناه مفرقا في أيام (sihah)؛ نزل متفرقا (tahdhib)؛ والتفريق أصله للتكثير ويقال ذلك في تشتيت الشمل والكلمة (mufradat)؛ يفرقون به بين المرء وزوجه (mufradat)؛ إن الذين فرقوا دينهم وقرئ فارقوا (mufradat)؛ ومفرق النعم هو الظربان لأنه إذا فسا بينها وهي مجتمعة تفرقت (sihah)
- **B003** doğruyu yanlıştan ayıran ölçüt veya araç — doğruyu yanlıştan ayıran kitap, kanıt, aydınlık veya destek · doğru ile yanlışın ayrıldığı belirleyici gün · doğruyu yanlıştan hakça ayıran kişi
  الفرقان كتاب الله تعالى فرق به بين الحق والباطل (maqayis)؛ الفرقان كل كتاب أنزل به فرق الله بين الحق والباطل (ayn)؛ يجعل لكم فرقانا أي حجة ظاهرة وظفرا (ayn)؛ كل ما فرق به بين الحق والباطل فهو فرقان (sihah)؛ سمى الله الكتاب المنزل على محمد فرقانا وسمى الكتاب المنزل على موسى فرقانا (tahdhib)؛ يوم الفرقان هو يوم بدر (tahdhib;mufradat)؛ الفرقان أبلغ من الفرق لأنه يستعمل في الفرق بين الحق والباطل (mufradat)؛ نورا وتوفيقا على قلوبكم يفرق به بين الحق والباطل (mufradat)
- **B004** yarılma ve ayrılan parça — yarılmış şeyden ayrılan parça veya su kütlesi · sabahın sökmesi ve aydınlığın yarılarak belirmesi
  الفرق الفلق من الشيء إذا انفلق (maqayis)؛ فانفلق فكان كل فرق كالطود العظيم (maqayis;sihah;mufradat)؛ كل فرق كالطود العظيم يريد من الماء (ayn)؛ انفرق الصبح أي انفلق والفرق هو الفلق (ayn)؛ فانفرق البحر فصار كالجبال العظام (tahdhib)؛ الفرق الموجة والفرق الجبل والفرق الهضبة (tahdhib)؛ الفرق يقارب الفلق لكن الفلق يقال اعتبارا بالانشقاق والفرق يقال اعتبارا بالانفصال (mufradat)
- **B005** ana bütünden ayrılmış topluluk — ayrı insan topluluğu veya grup · koyun sürüsü veya sürüden ayrılan küçük koyun grubu
  الفرق القطيع من الغنم (maqayis)؛ الفريقة وهو القطيع من الغنم كأنها قطعة فارقت معظم الغنم (maqayis)؛ الفرق طائفة من الناس ومن كل شيء والفريق من الناس أكثر من الفرق (ayn)؛ الفرق بالكسر القطيع من الغنم العظيم (sihah)؛ الفرقة طائفة من الناس والفريق أكثر منهم (sihah)؛ الفريقة فريقة الغنم أن تنفرق منها قطعة أو شاة أو شاتان أو ثلاث شياه (tahdhib;sihah)؛ الفريق الجماعة المتفرقة عن آخرين (mufradat)
- **B006** ayrım çizgisi veya çatallanma noktası — saç ayrımı ve saçın ayrıldığı yer · yol ayrımı veya yolun çatallanma noktası
  من ذلك الفرق فرق الشعر (maqayis)؛ الفرق موضع المفرق من الرأس في الشعر (ayn)؛ المفرق والمفرق وسط الرأس وهو الذي يفرق فيه الشعر وكذلك مفرق الطريق ومفرقه (sihah)؛ فرق له الطريق أي اتجه له طريقان (sihah)؛ الفرق مصدر فرقت الشعر (tahdhib)؛ لا يفرق شعره إلا أن ينفرق هو (tahdhib)
- **B007** beden yapısında doğuştan ayrıklık veya eşitsizlik — beden yapısı doğuştan ayrık, aralıklı veya eşitsiz olan
  الأفرق الديك الذي عرفه مفروق والفرق في الخيل أن يكون أحد وركيه أرفع من الآخر (maqayis)؛ الأفرق كالأفلج والأفرق يكون خلقة (ayn)؛ شاة فرقاء بعيدة ما بين الطبيين والأفرق من ذكورها بعيد ما بين الخصيتين (ayn)؛ تباعد ما بين الثنيتين وما بين المنسمين (sihah)؛ ديك أفرق بين الفرق للذي عرفه مفروق (sihah)؛ الأفرق من الخيل الذي نقصت إحدى فخذيه عن الأخرى (tahdhib)؛ الأفرق من الديك ما عرفه مفروق ومن الخيل ما أحد وركيه أرفع من الآخر (mufradat)
- **B008** doğum sancısıyla sürüden ayrılıp başıboş giden dişi deve — doğum sancısıyla sürüden ayrılıp başıboş giden dişi deve · yavrusu ölerek kendisinden ayrılmış dişi deve · öteki bulutlardan ayrı duran tek bulut
  الفارق الخلفة تذهب في الأرض نادة من وجع المخاض (maqayis)؛ سميت بذلك لأنها فارقت سائر النوق (maqayis)؛ تشبه السحابة تنفرد عن السحاب بهذه الناقة (maqayis)؛ الناقة إذا مخضت تفرق فروقا وهو نفارها وذهابها نادة من الوجع (ayn)؛ فرقت الناقة إذا أخذها المخاض فندت في الأرض (sihah)؛ ناقة مفرق أي فارتها ولدها بموت (sihah)؛ السحابة المنفردة لا تخلف (tahdhib)؛ أفرقنا إبلنا العام إذا حلوها في المرعى (tahdhib)؛ الناقة التي تذهب في الأرض نادة من وجع المخاض فارق وبها شبه السحابة المنفردة (mufradat)
- **B009** yüreği dağıtan korku ve yoğun ürküntü — korku, yoğun ürküntü veya çok korkak olma
  رجل فروقة وامرأة فروقة وقد فرق فرقا فهو فرق من الخوف (ayn)؛ الفرق بالتحريك الخوف وقد فرق بالكسر (sihah)؛ الفرق أيضا الخوف وقد فرق يفرق فرقا (tahdhib)؛ رجل فروقة وفروقة وفاروقة وهو الفزع الشديد الفرق (tahdhib)؛ الفرق تفرق القلب من الخوف (mufradat)
- **B010** hastalıktan kurtulup kendine gelme — hastalıktan kurtulup iyileşmek ve kendine gelmek
  إفراق المحموم من حماه وإنما يكون كذا لأنها فارقته (maqayis)؛ المطعون إذا برأ قيل أفرق إفراقا (ayn)؛ أفرق المريض من مرضه والمحموم من حماه أي أقبل (sihah)؛ ما علامة برء المحموم فقال العرق (sihah)؛ المطعون إذا برأ قيل أفرق يفرق إفراقا (tahdhib)؛ كل عليل أفاق من علته فقد أفرق (tahdhib)
- **B011** kap olarak kullanılan tarihsel hacim ölçüsü — kapasitesi aktarıma göre değişen tarihsel ölçü kabı veya hacim birimi
  مما شذ عن هذا الباب الفرق مكيال من المكاييل (maqayis)؛ الفرق مكيال ضخم لأهل العراق (ayn)؛ الفرق مكيال معروف بالمدينة وهو ستة عشر رطلا (sihah)؛ إناء يقال له الفرق (tahdhib)؛ إناء يأخذ ستة عشر مدا وذلك ثلاثة آصع (tahdhib)
- **B012** hurma ve çemenle pişirilen iyileştirici yiyecek — hurma ve çemenle pişirilen besleyici veya iyileştirici karışım
  الفريقة تمر يطبخ بحلبة يتداوى به (maqayis)؛ الفريقة تمر يطبخ بأشياء يتداوى بها (ayn)؛ الفريقة تمر يطبخ بحلبة للنفساء (sihah)؛ الفريقة التمر والحلبة تجعل للنفساء (tahdhib)؛ لون الفريقة صفيت للمدنف (tahdhib;sihah)؛ الفريقة تمر يطبخ بحلبة (mufradat)
- **B013** böbrek çevresi yağı — böbreğin veya böbreklerin çevresindeki yağ
  الفروقة شحم الكليتين (maqayis;tahdhib;mufradat)؛ الفروقة شحم الكلية (ayn)؛ شحم الفروقة والكلى (maqayis;ayn;tahdhib)
- **B014** seyrek ve kesintili bitki örtülü arazi [kalıp] — bitki örtüsü seyrek ve kesintili arazi
  هذه أرض فرقة وفي نبتها فرق إذا كان متفرقا ولم يكن منصلا (sihah)؛ أرض فرقة في نبتها فرق إذا لم تكن واصية متصلة النبات (tahdhib)
- **B015** ayırt edilen türler ve yönler — bir şeyin ayırt edilen türü veya anlatının ayrı yönü
  الماشطة تمشط كذا فرقا أي ضربا (ayn;tahdhib)؛ وقفت فلانا على مفارق الحديث أي على وجوهه (tahdhib)
- **B016** hareketle kenara çekilip dağılma — hareketle kenara çekilip birbirinden ayrılarak dağılmak
  افرنقعوا إذا تنحوا (maqayis)؛ كلمة منحوتة من فرق وفقع لأنهم يتفرقون فيكون لهم عند ذلك فقعة وحركة (maqayis)

## ش ه د (root_000822): 65:2 وَأَشْهِدُوا۟, 65:2 ٱلشَّهَٰدَةَ

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

## ع د ل (root_000991): 65:2 عَدْلٍ

- **B001** hükümde hak gözetme ve güvenilir doğruluk — hükümde hak gözetme ve haksızlığın karşıtı · hakka göre hükmeden kimse · sözüne, hükmüne ve tanıklığına güvenilen kimse · söz ve hükümde doğruluk ve güvenilirlik hali · hak gözeten hüküm ve yönetim düzeni · tanıkların güvenilirliğini onaylama
  العدل نقيض الجور (maqayis;sihah;tahdhib); العدل الحكم بالحق (ayn;tahdhib); رجل عدل مرضي قوله وحكمه (ayn;tahdhib); العدل التقسيط على سواء (mufradat)
- **B002** eşlik ve denklik — eş, denk veya benzer olan şey · birini ötekine denk tutmak · gözümüzde hiçbir şey senin yerini tutmaz
  كل ذلك من المعادلة وهي المساواة (maqayis); عدل الشيء نظيره (ayn); العدل المثل (sihah;tahdhib); لفظ يقتضي معنى المساواة (mufradat)
- **B003** denk kurtulma karşılığı — kurtulma karşılığı veya eşdeğer değer · ondan hiçbir kurtulma karşılığı kabul edilmez · bunun yerine aynı değerde oruç
  العدل قيمة الشيء وفداؤه (maqayis); العدل الفداء (ayn;sihah); العدل الفدية (tahdhib); ما يعادل من الصيام الطعام (mufradat)
- **B004** karşılıklı dengeli yük — hayvanın iki yanındaki denk yüklerden biri · hayvanın iki yanındaki dengeli iki yük · taşıtta veya ağırlıkta denk olan eş · heybeyi hayvanın bir yanına yükleyip öteki yana denklemek
  العدلان حملا الدابة سميا بذلك لتساويهما (maqayis); العدلان الحملان على الدابة من جانبين (ayn); واحد الأعدل عدل (sihah;tahdhib); العديل الذي يعادلك في المحمل (maqayis;ayn;tahdhib); عدلت الجوالق على البعير (tahdhib)
- **B005** düzeltip dengeleme — bir şeyi düzeltip dengeli hale getirmek · düzelip dengelenmek · düzgün, dengeli veya ılımlı · organları uyumlu, güzel yapılı dişi deve
  عدلت الشيء أقمته حتى اعتدل (maqayis;ayn;sihah;tahdhib); يوم معتدل إذا تساوى حره وبرده (maqayis); المعتدلة من النوق الحسنة المتفقة الأعضاء (maqayis;tahdhib); أيام معتدلات طيبات (mufradat)
- **B006** yönünden çevirme ve sapma — yoldan ya da doğrudan sapmak · bir şeyi yönünden çevirip eğmek · kıvrılmak, eğrilmek veya yön değiştirmek · erkek devenin çiftleşmeyi bırakıp sürüden uzaklaşması
  الأصل الآخر في الاعوجاج عدل وانعدل (maqayis); العدل أن تعدل الشيء عن وجهه فتميله (ayn;tahdhib); عدل عن الطريق جار (sihah); عدل عن الحق إذا جار عدولا (mufradat)
- **B007** Tanrı'ya başka bir varlığı eş tutma — Tanrı'ya başka bir varlığı eş tutmak · Tanrı'ya başka bir varlığı eş tutup ona tapan kimse
  المشرك يعدل بربه كأنه يسوي به غيره (maqayis); العادل المشرك الذي يعدل بربه (ayn;sihah); العدل في الإشراك (tahdhib); يجعلون له عديلا (mufradat)
- **B008** iki seçenek arasında kararsız kalıp üstün olanı tartma — iki seçenek arasında tartıp hangisinin üstün olduğuna bakmak · iki seçenek arasında kararsızlık ve kuşku
  يعادل أمره عدالا يميل بين أمرين (sihah); المعادلة الشك في الأمرين (tahdhib); أنا في عدال من هذا الأمر أي في شك منه (tahdhib); عادل بين الأمرين إذا نظر أيهما أرجح (mufradat)

## ق و م (root_001273): 65:2 وَأَقِيمُوا۟

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

## و ع ظ (root_001663): 65:2 يُوعَظُ

- **B001** sakındırıcı öğüt ve öğütten ders alma — iyiyi ve sonuçları hatırlatıp sakındırarak öğüt vermek · iyiyi ve sonuçları hatırlatan, gerektiğinde korkutup sakındıran öğüt verme · uyarıcı ve sakındırıcı öğüt · iyiyi ve sonuçları hatırlatan, gerektiğinde korkutan öğüt · öğüdü kabul edip ders almak · Sen kendin öğüt al, bana öğüt verme.
  الوعظ التخويف والعظة الاسم منه (maqayis)؛ التذكير بالخير وما يرق له قلبه (maqayis;ayn;tahdhib;mufradat)؛ النصح والتذكير بالعواقب (sihah)؛ زجر مقترن بتخويف (mufradat)؛ اتعظ قبل الموعظة (ayn;sihah;tahdhib)

## ك و ن (root_001332): 65:2 كَانَ, 65:6 كُنَّ, 65:9 وَكَانَ

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

## ء م ن (root_000054): 65:2 يُؤْمِنُ, 65:10 ءَامَنُوا۟, 65:11 ءَامَنُوا۟, 65:11 يُؤْمِنۢ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ي و م (root_001700): 65:2 وَٱلْيَوْمِ

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

## ء خ ر (root_000019): 65:2 ٱلْءَاخِرِ, 65:6 أُخْرَىٰ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ج ع ل (root_000248): 65:2 يَجْعَل, 65:3 جَعَلَ, 65:4 يَجْعَل, 65:7 سَيَجْعَلُ

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

## ر ز ق (root_000560): 65:3 وَيَرْزُقْهُ, 65:7 رِزْقُهُۥ, 65:11 رِزْقًا

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

## ح ي ث (root_000375): 65:3 حَيْثُ, 65:6 حَيْثُ

- **B001** ardından gelen yan tümceyle belirlenen yer — ardından gelen yan tümceyle belirlenen yer · her nerede; nerede olursa · belirtilen yerden · aynı yer anlamındaki lehçe varyantı
  كلمة موضوعة لكل مكان وهي مبهمة (maqayis)؛ كلمة معروفة يستدل بها على المكان مبنية على الضم (jamhara)؛ كلمة تدل على المكان لأنه ظرف في الأمكنة بمنزلة حين في الأزمنة (sihah)؛ حيث ظرف من المكان أي الموضع الذي كنت فيه وإلى أي موضع شئت (tahdhib)؛ عبارة عن مكان مبهم يشرح بالجملة التي بعده (mufradat)

## ح س ب (root_000318): 65:3 يَحْتَسِبُ, 65:3 حَسْبُهُۥٓ, 65:8 فَحَاسَبْنَٰهَا, 65:8 حِسَابًا

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

## و ك ل (root_001681): 65:3 يَتَوَكَّلْ

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

## ك ل ل (root_001315): 65:3 لِكُلِّ, 65:12 كُلِّ, 65:12 بِكُلِّ

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

## ش ي ء (root_000831): 65:3 شَىْءٍ, 65:12 شَىْءٍ, 65:12 شَىْءٍ

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

## ش ي ء (root_000832): 65:3 شَىْءٍ, 65:12 شَىْءٍ, 65:12 شَىْءٍ

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

## ق د ر (root_001205): 65:3 قَدْرًا, 65:7 قُدِرَ, 65:12 قَدِيرٌ

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

## ي ء س (root_001690): 65:4 يَئِسْنَ

- **B001** umudu kesme veya birine umudunu kestirme — umudu kesme, umutsuzluk · umudunu kesmek, umutsuzluğa düşmek · umudunu kesmek, umutsuzluğa düşmek · büsbütün umudunu kesmek · birine bir şeyden umudunu kestirmek · umudu kesme, umutsuzluk · çok umutsuz, umudunu çabuk kesen · umudunu kesmek
  اليأس قطع الرجاء (maqayis)؛ اليأس ضد الرجاء (jamhara)؛ اليأس القنوط (sihah)؛ اليأس انتفاء الطمع (mufradat)؛ آيسه فلان من كذا فاستيأس منه بمعنى أيس (sihah)؛ أيس يأيس وآيسته أي أيأسته وهو اليأس والإياس (tahdhib)
- **B002** bilme diye açıklanan tartışmalı kullanım — 
  ألم تيأس أي ألم تعلم (maqayis)؛ يئس أيضا بمعنى علم في لغة النخع (sihah)؛ أفلم ييأس أفلم يعلم (tahdhib)؛ ييأس بمعنى يعلم لغة للنخع (tahdhib)؛ ولم يرد أن اليأس موضوع في كلامهم للعلم (mufradat)

## ح ي ض (root_000379): 65:4 ٱلْمَحِيضِ, 65:4 يَحِضْنَ

- **B001** belirli zamanda görülen rahim kanaması — belirli zamanda görülen rahim kanaması · kadının adet görmesi · tek bir adet kanaması · adet kanaması · adet kanaması; bunun zamanı veya yeri · adet gören kadın; benzetme yoluyla lohusa kadın · kadının adet günlerinde namazı bırakması
  الحيض معروف (ayn;jamhara); حاضت المرأة تحيض حيضا ومحيضا (ayn;sihah); الدم الخارج من الرحم على وصف مخصوص في وقت مخصوص (mufradat); المحيض الحيض ووقت الحيض وموضعه (mufradat); سميت النفساء حائضا تشبيها لدمها بذلك الماء (maqayis)
- **B002** olağan adet günlerinden sonra kesilmeyen kanama — kadının olağan günlerinden sonra kanamasının sürmesi · olağan günlerinden sonra kanaması kesilmeyen kadın
  المستحاضة التي غلب عليها الدم فلا يرقأ (ayn); استحيضت المرأة أي استمر بها الدم بعد أيامها فهي مستحاضة (sihah)
- **B003** kadının adet sırasında üzerine yerleştirdiği bez parçası — adet sırasında kullanılan bez parçası · adet sırasında kullanılan bez parçası
  الحيضة أيضا الخرقة التي تستثفر بها المرأة؛ وكذلك المحيضة والجمع المحايض
- **B004** bir ağacın kanı andıran kırmızı sıvı çıkarması [kalıp] — ağacın kanı andıran kırmızı bir sıvı çıkarması
  حاضت السمرة إذا خرج منها ماء أحمر (maqayis); حاضت السمرة حيضا وهي شجرة يسيل منها شيء كالدم (sihah)

## ر ي ب (root_000616): 65:4 ٱرْتَبْتُمْ

- **B001** kuşku ve güvensizlik — kuşku ve zihinsel kararsızlık · suçlayıcı kuşku ve güven eksikliği · bende kuşku ve korku uyandırdı · bende kuşku uyandırdı · kuşkulu duruma geldi veya kuşku uyandırır oldu · ondan veya o şeyden kuşkulandı · onda kuşku uyandıran bir belirti gördü · kuşku duyan veya kuşku uyandıran
  الريب الشك (maqayis;ayn;jamhara;sihah)؛ الريب التهمة (jamhara)؛ ما رابك من أمر تخوفت عاقبته (ayn)؛ رابني هذا الأمر إذا أدخل عليك شكا وخوفا (maqayis;ayn)؛ الريبة اسم من الريب تدل على دغل وقلة يقين (mufradat)؛ أراب الرجل صار ذا ريبة (maqayis;ayn;sihah)؛ ارتبت به أي ظننت به (ayn)
- **B002** zamanın değişimleri ve olayları [kalıp] — zamanın değişimleri, olayları ve terslikleri · ölümün ne zaman geleceğine ilişkin korkulan olaylar
  ريب الدهر صروفه (maqayis;jamhara;mufradat)؛ الريب صرف الدهر وعرضه وحدثه (ayn)؛ ريب المنون حوادث الدهر (sihah)؛ ريب المنون من جهة وقته لا من جهة كونه (mufradat)
- **B003** karşılanması gereken gereksinim — elden kaçırma kaygısıyla aranan gereksinim
  الريب الحاجة (sihah)؛ فيقال إن الريب الحاجة (maqayis)؛ طالب الحاجة شاك على ما به من خوف الفوت (maqayis)

## ث ل ث (root_000203): 65:4 ثَلَٰثَةُ

- **B001** uc sayisi — uc sayisi · ucer ucer
  اثنان وثلاثة (maqayis)؛ الثلاثة في عدد المذكر والثلاث في عدد المؤنث (sihah)؛ الثلاثة من العدد (tahdhib)؛ الثلاثة والثلاثون والثلاث والثلاثمائة وثلاثة آلاف (mufradat)
- **B002** ucte birlik pay — ucte bir · ucte bir anlamli bicim · ucte ikiler ve ucte birlik paylar · bir seyi uc parcaya bolmek · toplulugun malinin ucte birini almak · meyvenin ucte ikisi olgunlasmak
  الثلث سهم من ثلاثة (sihah)؛ ثلثت القوم إذا أخذت ثلث أموالهم (sihah;tahdhib;mufradat)؛ الثلث والثلثان والجمع أثلاث (mufradat)؛ ثلثت الشيء جزأته أثلاثا (mufradat)؛ ثلث البسر إذا بلغ الرطب ثلثيه (mufradat)
- **B003** ucuncu olma — grup uc kisi olmak veya uce tamamlanmak · ucun ucuncusu veya ucten biri · ikiyi kendisiyle uce tamamlayan · atin yarista ucuncu gelmesi
  أثلثهم إذا كنت ثالثهم أو كملتهم ثلاثة بنفسك (sihah)؛ أثلث القوم صاروا ثلاثة (sihah;mufradat)؛ ثالث ثلاثة مضاف (sihah;tahdhib)؛ ثلث الفرس جاء ثالثا في السباق (mufradat)
- **B004** uc parcali yapida olan — uc burumlu ip · uc deriden yapilmis su tulumu · uc malzemeden dokunmus kumas · uc koseli veya uc katli sey · uc arsin uzunlugunda giysi · uc unsurlu bag takimi
  المثلوثة المزادة تكون من ثلاثة جلود (maqayis;sihah;tahdhib)؛ حبل مثلوث إذا كان على ثلاث قوى (maqayis;sihah;mufradat)؛ كساء مثلوث منسوج من صوف ووبر وشعر (tahdhib)؛ شيء مثلث ذو أركان ثلاثة (sihah)؛ المثلث ما كان من الأشياء على ثلاثة أثناء (tahdhib)؛ ثوب ثلاثي طوله ثلاثة أذرع (mufradat)
- **B005** uc meme veya uc kapla ilgili deve — uc kap sut veren ya da uc memeden sagilan deve · uc memeli deve · devenin uc memesini baglamak
  الثلوث من الإبل التي تملأ ثلاثة آنية إذا حلبت (maqayis)؛ الثلوث من النوق التي تجمع بين ثلاث آنية تملؤها إذا حلبت (sihah)؛ ناقة ثلوث إذا أصاب أحد أخلافها شيء فيبس (tahdhib)؛ ناقة ثلوث تحلب من ثلاثة أخلاف (mufradat)
- **B006** Sali — Sali
  الثلاثاء من الأيام (maqayis;sihah)؛ الثلاثاء اسم مؤنث ممدود (tahdhib)؛ الثلاثاء والأربعاء من الأيام (mufradat)
- **B007** ocak icin ucuncu kaya — tencere icin iki tasa eklenen kaya cikintisi · bir toplulugu buyuk bir isle karsilamak
  ثالثة الأثافي الحيد النادر من الجبل يجمع إليه صخرتان (maqayis;sihah)؛ رميناهم بثالثة الأثافي إذا رمي القوم بأمر عظيم (tahdhib)
- **B008** ucte bire kaynatilmis icecek — ucte biri kalincaya kadar kaynatilmis icecek
  المثلث من الشراب الذي طبخ حتى ذهب ثلثاه
- **B009** yoneticiye kardesini sikayet eden kisi — kardesini yoneticiye zarar verecek sekilde sikayet eden kisi
  ما المثلث؛ هو الرجل يمحل بأخيه إلى إمامه فيبدأ بنفسه ثم بأخيه ثم بإمامه
- **B010** hurma sulama ifadesindeki ozel kullanim — hurma sulamada yalniz bu ifadeye ozgu kullanim
  الثلث بالكسر من قولهم هو يسقي نخلة الثلث؛ لا يستعمل الثلث إلا في هذا الموضع؛ وليس في الورد ثلث

## ش ه ر (root_000823): 65:4 أَشْهُرٍ

- **B001** ayın ilk görünümüne göre belirlenen otuz günlük süre — ay; ayın ilk görünümüyle belirlenen yaklaşık otuz günlük süre · aylar; birden çok ayın sayısı veya süresi · aylar topluluğu · ay ay yapılan işlem veya aylık anlaşma · bir yerde bir ay kalmak · üzerinden bir ay geçmek veya yeni aya girmek · güz dönemi ile kış arasındaki ay
  الشهر الهلال ثم سمي كل ثلاثين يوما باسم الهلال (maqayis); الشهر والأشهر عدد والشهور جماعة (ayn;tahdhib); الشهر واحد الشهور (sihah); مدة مشهورة بإهلال الهلال (mufradat); المشاهرة المعاملة شهرا بشهر (ayn;tahdhib); أشهرنا بالمكان إذا أقمنا به شهرا (maqayis;sihah;mufradat); دخلنا في الشهر (sihah)
- **B002** insanlar arasında belirginleşip yaygın biçimde bilinme — herkesçe bilinme, tanınmışlık; kötü bağlamda dillere düşme · adı duyulmak, insanlar arasında tanınır hâle gelmek · tanınmış, herkesçe bilinen
  الشهرة وضوح الأمر (maqayis;sihah); ظهور الشيء في شنعة حتى يشهره الناس (ayn;tahdhib); شهر فلان واشتهر يقال في الخير والشر (mufradat); الشهرة الفضيحة (tahdhib); مشهور ومشهر (ayn;tahdhib)
- **B003** kılıcı kınından çekip görünür hâle getirme [kalıp] — kılıcını kınından çekip görünür hâle getirmek · silahı üzerlerine çekip kaldırmak
  شهر سيفه إذا انتضاه (maqayis); شهر سيفه إذا انتضاه فرفعه على الناس (ayn;tahdhib); شهر سفيه أي سله (sihah); شهر علينا السلاح (ayn;tahdhib)

## ء و ل (root_000067): 65:4 وَأُو۟لَٰتُ, 65:6 أُو۟لَٰتِ, 65:10 يَٰٓأُو۟لِى

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

## ECHO و ل ي (root_001684): for 65:4 وَأُو۟لَٰتُ, 65:6 أُو۟لَٰتِ, 65:10 يَٰٓأُو۟لِى: withheld observed target; not identity

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

## ح م ل (root_000357): 65:4 ٱلْأَحْمَالِ, 65:4 حَمْلَهُنَّ, 65:6 حَمْلٍ, 65:6 حَمْلَهُنَّ

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

## و ض ع (root_001657): 65:4 يَضَعْنَ, 65:6 يَضَعْنَ

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

## ي س ر (root_001694): 65:4 يُسْرًا, 65:7 يُسْرًا

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

## ن ز ل (root_001492): 65:5 أَنزَلَهُۥٓ, 65:10 أَنزَلَ, 65:12 يَتَنَزَّلُ

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

## ك ف ر (root_001307): 65:5 يُكَفِّرْ

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

## س و ء (root_000755): 65:5 سَيِّـَٔاتِهِۦ

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

## ع ظ م (root_001029): 65:5 وَيُعْظِمْ

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

## ء ج ر (root_000015): 65:5 أَجْرًا, 65:6 أُجُورَهُنَّ

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## س ك ن (root_000726): 65:6 أَسْكِنُوهُنَّ, 65:6 سَكَنتُم

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

## و ج د (root_001626): 65:6 وُجْدِكُمْ

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

## ECHO ج د د (root_000227): for 65:6 وُجْدِكُمْ: withheld observed target; not identity

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

## ض ر ر (root_000907): 65:6 تُضَآرُّوهُنَّ

- **B001** zarar, eksilme ve kötü duruma düşme — zarar, kötü durum · zarar vermek, eksiltmek · zarar, eksilme · yararın karşıtı olan zarar · sıkıntı, süreğen düşkünlük veya kötü yıl · görme yetisini yitirmiş, hasta veya bedeni zarar görmüş adam · hasta veya görme yetisini yitirmiş kadın · görme yetisini yitirmiş topluluk · zarar verme ve zararla karşılık verme yoktur
  الضر ضد النفع (maqayis;tahdhib)؛ الضرر النقصان يدخل في الشيء (ayn;tahdhib)؛ الضر المرض والهزال (jamhara;maqayis)؛ الضر سوء الحال (sihah;mufradat)؛ رجل ضرير ذاهب البصر (ayn;sihah;tahdhib;mufradat)
- **B002** zarar verme ve karşılıklı zararlaşma — zarar verme, karşılıklı zararlaşma · zarar verme ve zararla karşılık verme yoktur · karşı çıkmak veya karşılıklı zarar vermek · kimse zarar vermesin veya zarara uğratılmasın
  الضرير المضارة وأكثر ما يستعمل في الغيرة (maqayis;ayn;sihah;tahdhib)؛ لا ضرر ولا ضرار (tahdhib)؛ ضاررته ضرارا ومضارة إذا خالفته (tahdhib)؛ ولا تضاروهن ولا يضار كاتب ولا شهيد (mufradat)
- **B003** zorunluluk ve mecbur kalma — zorunluluk, mecbur bırakan ihtiyaç · zorunluluk anlamındaki şiir dili biçimi · bir şeye mecbur kalmak · bir şeye mecbur bırakılmış kişi · mecbur bırakan bir ihtiyacı olan adam
  الضرورة اسم لمصدر الاضطرار (ayn;tahdhib)؛ الضرورة والضارورة واحد وهو الاضطرار إلى الشيء (jamhara)؛ اضطر فلان إلى كذا من الضرورة (maqayis;sihah)؛ الاضطرار حمل الإنسان على ما يضره (mufradat)
- **B004** kuma ilişkisi ve eşin üzerine evlenme — kuma, kocasının başka eşi bulunan kadın · aynı erkeğin iki eşi · aynı kocayı paylaşan eşler · eşin üzerine evlenme durumu · eşinin üzerine başka biriyle evlenmek · birden çok eşi olan erkek veya kuması olan kadın
  الضرة امرأة زوجها (sihah)؛ الضرتان امرأتان لرجل واحد (ayn;tahdhib)؛ الضر تزوج المرأة على ضرة (maqayis;jamhara;sihah;tahdhib)؛ رجل مضر ذو ضرائر (maqayis;ayn;sihah;tahdhib;mufradat)
- **B005** sıkıştırıcı yakınlık, darlık ve vadi kıyısı — beni sıkıştıracak kadar yaklaştı · yol topluluğa dar geldi ve onları sıkıştırdı · dar yer · vadinin iki yanı veya kıyısı · yere yakın, alçak bulut
  أضرني إضرارا أي دنا مني دنوا شديدا (ayn;sihah;tahdhib)؛ أضر الطريق بالقوم ضاق بهم ودنا منهم (ayn)؛ مكان ذو ضرار أي ضيق (sihah;tahdhib)؛ ضريرا الوادي جانباه (jamhara;sihah;tahdhib)؛ ضرير الوادي شاطئه الذي ضره الماء (mufradat)
- **B006** belirli kalıplarda toplu et, yağ veya mal kütlesi [kalıp] — memenin eti veya süt bulunan kökü · başparmağın altındaki et yastığı · kalçanın iki yanındaki yağlı bölümler · toplu veya çok miktarda mal ya da deve · çok veya toplu malı olan adam
  ضرة الضرع لحمته (maqayis;ayn;sihah;tahdhib)؛ ضرة الإبهام لحمة تحتها (maqayis;ayn;jamhara;sihah;tahdhib)؛ الضرتان الأليتان شحمتان (ayn;tahdhib)؛ الضرة المال الكثير (sihah;tahdhib)؛ المضر الذي له ضرة من مال (maqayis;ayn;sihah;tahdhib)
- **B007** iç güç, sabır ve dayanıklılık — iç güç ve kalan dayanma gücü · bir şeye sabırla dayanma gücü olan · güçlü, dayanıklı ve geç yorulan dişi deve · at gemin ağızlık parçasını sıkıca kavradı · biraz hızlanarak koştu · görüşünde kurnaz, güçlü ve çareci adam
  الضرير قوة النفس (maqayis)؛ ذو ضرير على الشيء إذا كان ذا صبر عليه ومقاساة (maqayis;sihah;tahdhib)؛ الضرير من الدواب الصبور على كل شيء (sihah)؛ ضريرها شدتها (tahdhib)؛ أضر الفرس على فأس اللجام إذا أزم عليه (maqayis;sihah;tahdhib)؛ رجل ضر أضرار إذا كان داهية في رأيه (tahdhib)
- **B008** belirli olumsuz kalıplarda daha fazlasını sağlamamak [kalıp] — bu adamın yeterliliğini aşacak başka bir adam bulamazsın · onun üstüne bir yük daha eklemez · onun üstüne bir kadın köle daha eklemez · kertenkeleye dayanma sabrını daha fazla artırmaz
  لا يضرك عليه رجل أي لا يزيدك (sihah;tahdhib)؛ ما يضرك عليها جارية أي ما يزيدك (tahdhib)؛ ما يضيرك على الضب صبرا أي ما يزيدك (tahdhib)

## ض ي ق (root_000925): 65:6 لِتُضَيِّقُوا۟

- **B001** dar olma veya daraltma — daralmak veya yeterli genişliği bulunmamak · darlık ve genişlik yokluğu · dar ve yeterince geniş olmayan · yeri daraltmak veya birine daha az alan bırakmak · huy veya mekan bakımından birbirine geniş davranamamak · dar geçit veya dar yer · en dar olanı belirten dişil biçim · karşılıklı sıkıştırma veya birbirine alan bırakmama
  خلاف السعة (maqayis;mufradat); ضاق الأمر يضيق ضيقا فهو ضيق (ayn;tahdhib); ضاق الشيء يضيق ضيقا (sihah); مكان ضيق وضيق (tahdhib); ضيقت عليك الموضع (sihah)
- **B002** iç daralması ve dayanamama [kalıp] — ona dayanamamak veya onu kaldıracak gücü kalmamak · iç daralması, tasa ve üzüntü
  ضقت به ذرعا أي ضاق ذرعي به (sihah); في صدر فلان ضيق وضيق (tahdhib); الضيقة يستعمل في الغم (mufradat); كل ذلك عبارة عن الحزن (mufradat); ما ضاق عنه صدرك (tahdhib)
- **B003** geçim darlığı, eli sıkılık ve gider kısma — yoksulluk ve kötü geçim durumu · malını yitirmek veya geçimi daralmak · eli sıkı davranmak · bakmakla yükümlü olduğu kişilerin giderini kısmak
  الضيقة الفقر (maqayis); أضاق الرجل ذهب ماله (maqayis;sihah); ضاق إذا بخل (maqayis); الضيق جمع الضيقة وهي الفقر وسوء الحال (sihah); أضاق الرجل فهو مضيق إذا ضاق عليه معاشه (tahdhib); الضيقة يستعمل في الفقر والبخل (mufradat); تضييق النفقة (mufradat)
- **B004** belirli bir ay konağının adı — komşu göksel işaretler arasında bulunan belirli bir ay konağının adı
  الضيقة منزل في منازل القمر (maqayis); الضيق والضيقة منزل للقمر بلزق الثريا مما يلي الدبران (ayn); الضيقة بين النجم والدبران (sihah;tahdhib); جعله اسما علما لذلك الموضع (tahdhib)
- **B005** kuşku — kuşku
  الضيق بفتح الياء الشك (tahdhib); الضيق محركة الياء الشك (tahdhib)

## ن ف ق (root_001537): 65:6 فَأَنفِقُوا۟, 65:7 لِيُنفِقْ, 65:7 فَلْيُنفِقْ

- **B001** tükenip sona erme; özel kullanımlarda alıcı bulma, çabuk kesilme veya yüzeyden ayrılma — hayvan öldü · tükendi, sona erdi · fiyat veya satış canlandı, mal alıcı buldu · topluluğun pazarı canlandı, malları alıcı buldu · eşi bulunmayan kadına evlenme isteğiyle başvuranlar çoğaldı · koşusu çabuk kesilen at · kesintiye uğrayan gidiş · yaranın kabuğu soyuldu · develerin semirmeden dolayı tüyleri döküldü · insanlara söven kişi karşılığında sövgü görür ve onurunu diline düşürür
  نفقت الدابة نفوقا أي ماتت (maqayis;ayn;sihah;tahdhib;mufradat); نفق الشيء فني ونفد (maqayis;sihah;tahdhib;mufradat); نفق السعر أو البيع نفاقا وكثر مشتروه (maqayis;ayn;sihah;tahdhib;mufradat); فرس نفق الجري وسير نفق سريع الانقطاع (maqayis;sihah;tahdhib); نفق الجرح إذا انقشر وانتثرت الأوبار عن سمن (tahdhib)
- **B002** bir şeyi gider olarak elden çıkarma; özel kullanımda elindekini tüketip yoksullaşma — geçim için yapılan gider; harcanan şey · harcadı, elden çıkardı · adam malı tükenince yoksullaştı · çok harcayan kişi
  النَّفَقَة لأنها تمضي لوجهها (maqayis); النَّفَقَة ما أنفقت واستنفقت على العيال ونفسك (ayn;tahdhib); أنفقت الدرهم من النَّفَقَة ورجل منقاق كثير النَّفَقَة (sihah); الإنفاق قد يكون في المال وفي غيره واجبا وتطوعا (mufradat); أنفق الرجل افتقر وذهب ما عنده أو ماله (maqayis;sihah;tahdhib;mufradat)
- **B003** başka bir yere açılan yer altı geçidi ve kemirgen yuvasındaki gizli çıkış — çıkışı bulunan yer altı geçidi · kemirgen yuvasındaki inceltilmiş gizli çıkış · kemirgen yuvasındaki gizli çıkış · gizli çıkıştan dışarı çıktı · kemirgeni sıkıştırıp gizli çıkışından kaçırdık · kemirgen gizli çıkışına girdi
  النفق سرب في الأرض له مخلص إلى مكان (maqayis;ayn;sihah;tahdhib); النفق الطريق النافذ والسرب في الأرض النافذ فيه (mufradat); النافقاء موضع يرققه اليربوع فإذا أتي من قبل القاصعاء ضربها برأسه فانتفق أي خرج (maqayis;ayn;sihah;tahdhib); بعضهم يسمي النافقاء النَّفَقَة (ayn;sihah;tahdhib)
- **B004** içindeki inanç veya tutumun tersini göstererek bağlı görünme — içindekinin tersini gösterme ve inançta ikiyüzlülük · içindekinden başkasını göstererek ikiyüzlü davrandı · içinde sakladığının tersini gösteren kimse
  النفاق لأن صاحبه يكتم خلاف ما يظهر (maqayis); النفاق الخلاف والكفر والفعل نافق نفاقا (ayn); ومنه اشتقاق المنافق في الدين (sihah); سمي المنافق منافقا للنفق وهو السرب في الأرض (tahdhib); النفاق الدخول في الشرع من باب والخروج عنه من باب (mufradat)

## ر ض ع (root_000568): 65:6 أَرْضَعْنَ, 65:6 فَسَتُرْضِعُ

- **B001** memeden süt emme ve emzirme — memeden ya da hayvan memesinden süt emip içmek · çocuğu emzirmek · yanında emzirdiği bebeği bulunan kadın · çocuğunu o anda emziren kadın · süt emme çağındaki bebek · süt emme çağındaki bebekler · yavrusunu emziren koyun · çocuğu emzirecek bir kadın istemek · çocuğunu emzirmesi için sütanneye vermek · süt emme ve emzirme eylemi · süt emme ve emzirme eylemi
  شرب اللبن من الضرع أو الثدي (maqayis)؛ رضع الصبي رضاعا ورضاعة أي مص الثدي وشرب (ayn)؛ رضع الصبي أمه يرضعها رضاعا (sihah)؛ المرضعة التي ترضع والمرضع التي معها الصبي الرضيع (tahdhib)؛ رضع المولود يرضع ورضع يرضع رضاعا ورضاعة (mufradat)
- **B002** süt emmeyle kurulan akrabalık — süt kardeşi · aynı kadından süt emmiş kişi · evlenme engeli doğuran çocukluk emmesi · çocuğu doyurup besleyen süt emme
  هو أخوه من الرضاعة؛ وهو رضيعي (maqayis)؛ هذا أخي من الرضاعة وهذا رضيعي (sihah)؛ الرضاع الذي يحرم رضاع الصبي لأنه يشبعه ويغذوه (tahdhib)؛ أخو فلان من الرضاعة؛ يحرم من الرضاع ما يحرم من النسب (mufradat)
- **B003** aşağılık ve aşırı cimri kişi — hayvanından gizlice süt emen birine benzetilen cimri ve aşağılık kişi · malını saklamak için hayvanından gizlice süt emen aşırı cimri · gizli süt emme benzetmesiyle aşağılanan cimri kişi · konuktan sütü saklamak için koyunundan ağzıyla emen aşağılık kişi
  لئيم راضع وكأنه من لؤمه يرضع إبله لئلا يسمع صوت حلبه (maqayis)؛ رضع الرجل فهو رضيع راضع لئيم (ayn)؛ لئيم راضع أصله رجل كان يرضع إبله وغنمه ولا يحلبها (sihah)؛ الراضع والرضع الخسيس من الأعراب (tahdhib)؛ عنه استعير لئيم راضع (mufradat)
- **B004** bebeğin süt içerken kullandığı ve emme çağında çıkan dişler — bebeğin süt içerken dayandığı iki ön kesici diş · bebeğin emme döneminde çıkan dişleri
  الراضعتان الثنيتان اللتان يشرب عليهما (maqayis)؛ الراضعتان من السن اللتان شرب عليهما اللبن والرواضع الأسنان التي تطلع في فم المولود في وقت رضاعه (ayn)؛ الراضعتان ثنيتا الصبي اللتان يشرب عليهما اللبن (sihah)؛ الراضعتان من السن اللتان شرب عليهما اللبن (tahdhib)؛ سمي الثنيتان من الأسنان الراضعتين لاستعانة الصبي بهما في الرضع (mufradat)
- **B005** küçük hurma ağaçları — küçük hurma ağaçları · küçük bir hurma ağacı
  الرضع: صغار النخل، واحده رضعة (tahdhib)

## ع س ر (root_001012): 65:6 تَعَاسَرْتُمْ, 65:7 عُسْرٍ

- **B001** güçlük ve çetinlik — güçlük, çetinlik; kolaylığın karşıtı · zorlaşmak, çetin hale gelmek · zor, çetin · zor ve çetin gün · kolaylaşmayan zor işler · zor olan veya kolay olanın karşıtı
  أصل صحيح واحد يدل على صعوبة وشدة (maqayis); العسر نقيض اليسر (maqayis;ayn;sihah;tahdhib;mufradat); أمر عسير ويوم عسير (maqayis;ayn;sihah;tahdhib;mufradat); العسرى الأمور التي تعسر ولا تتيسر (tahdhib)
- **B002** para darlığı — para darlığı, maddi sıkıntı · maddi darlık, parasızlık · maddi sıkıntı içinde olan kimse · varlıktan maddi darlığa düşmek
  الإقلال أيضا عسرة (maqayis); العسر قلة ذات اليد (ayn); العسرة قلة ذات اليد وكذلك الإعسار (tahdhib); العسرة تعسر وجود المال (mufradat); أعسر الرجل إذا صار من ميسرة إلى عسرة (maqayis)
- **B003** darlıktaki borçluyu sıkıştırmak — darlıktaki borçludan borcu katılıkla istemek · darlık zamanında benden bir şey istemek · alacak istemede ve işte katı davrananlar
  عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته (maqayis); عسرت الغريم أعسره إذا طلبت منه الدين على عسرته (sihah); عسرت الغريم أعسره عسرا إذا أخذته على عسرة ولم ترفق به (tahdhib); عسرني الرجل طالبني بشيء حين العسرة (mufradat)
- **B004** karşı çıkıp işi güçleştirmek — karşı çıkma ve dolambaçlılık · iş ona dolambaçlı ve güç gelmek · ona karşı çıkmak veya işi ona güçleştirmek · iş dolambaçlı ve güç hale gelmek · birbirlerine işi güçleştirmek · birinden elde edilmesi güç olan şeyi istemek
  العسر الخلاف والالتواء (maqayis;ayn); عسرت عليه تعسيرا إذا خالفته (maqayis); عسر عليه الأمر أي التاث (sihah); عسرت على فلان الأمر تعسيرا (tahdhib); استعسرت فلانا إذا طلبت معسوره (tahdhib); تعاسر القوم طلبوا تعسير الأمر (mufradat)
- **B005** sol taraf ve sola özgü olma — sol taraf · solak, sol eliyle çalışan · iki elini de kullanabilen · soluma gelmek · sol yanında fazla tüy veya beyazlık bulunan kartal · sol kanadında beyazlık bulunan güvercin
  العسرى خلاف اليسرى (maqayis;sihah); الذي يعمل بشماله أعسر (maqayis); رجل أعسر بين العسر وامرأة عسراء (sihah;tahdhib); عقاب عسراء ريشها من الجانب الأيسر أكثر من الأيمن (sihah); حمام أعسر وعقاب عسراء بجناحه من يساره بياض (sihah;tahdhib)
- **B006** güç doğum yapmak — kadının doğumu güçleşmek · doğumu güç olsun ve kız doğursun diye beddua etmek
  أعسرت المرأة إذا عسر عليها ولادها (maqayis;sihah;tahdhib); أعسرت وآنثت (maqayis;tahdhib); أيسرت وأذكرت (maqayis;tahdhib)
- **B007** o yıl gebe kalmayan deve — o yıl çiftleştiği halde gebe kalmayan deve
  العسير الناقة التي اعتاطت واعتاصت فلم تحمل عامها (maqayis); العسير الناقة إذا اعتاطت عامها فلم تحمل (sihah); تفسير الليث للعسير أنها الناقة التي اعتاطت غير صحيح (tahdhib)
- **B008** hazır olmadan zorlayıp kullanmak veya almak — eğitilmeden binilen deve · eğitilmeden önce binilen deve · zorla almak · oğlu istemediği halde malından almak · sözü hazırlamadan doğaçlama söylemek
  الناقة التي تركب قبل أن تراض عوسرانية (maqayis); العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض (sihah); اعتسره مثل اقتسره (sihah); العسير الناقة التي ركبت قبل تذليلها (tahdhib); يعتسر الرجل من مال ولده معناه يأخذ من ماله وهو كاره (tahdhib); اعتسرت الكلام إذا اقتضبته قبل أن تزوره وتهيئه (tahdhib)
- **B009** koşarken kuyruğunu kaldırmak — koşarken kuyruğunu kaldırıp büken deve · koşarken kuyruğunu kaldıran deve · koşarken kuyruklarını kaldıran veya büken develer ya da kurtlar
  العاسر من النوق إذا عدت رفعت ذنبها (maqayis); عسرت الناقة بذنبها إذا شالت به (sihah); العاسرة من النوق فهي التي إذا عدت رفعت ذنبها (tahdhib); عواسر الذئاب التي تعسل في عدوها وتكسر أذنابها (tahdhib); ناقة عوسرانية إذا كان من دأبها تكسير ذنبها ورفعه إذا عدت (tahdhib)
- **B010** uğursuz gün [kalıp] — uğursuz gün
  يوم أعسر أي مشئوم (tahdhib)
- **B011** dağınık veya art arda ilerleme — dağınık halde veya birbiri ardınca
  ذهبت الإبل عساريات وعشاريات إذا انتشرت وتفرقت (tahdhib); جاءوا عساريات وعسارى أي بعضهم في إثر بعض (tahdhib)
- **B012** cin topluluğu veya yer adı — bir cin topluluğunun adı · cin topluluğu, cinlerin yaşadığı arazi veya yer adı
  العسرة قبيلة من قبائل الجن (tahdhib); عسر قبيلة من الجن (tahdhib); عسر أرض يسكنها الجن (tahdhib); عسر موضع (tahdhib)
- **B013** çubuk atıp dikili çubuğu çıkarma oyunu — dikili çubuğa başka çubuk atıp onu yerinden çıkarma oyunu
  العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع (tahdhib)

## و س ع (root_001647): 65:7 سَعَةٍ, 65:7 سَعَتِهِۦ

- **B001** genişlik, genişleme ve genişletme — geniş duruma gelmek · bir şeyi genişletmek · genişlemek · genişlemek veya daha çok alan istemek · genişletme · oturma yerinde birbirine yer açmak · uzamsal genişlik · geniş, dar olmayan
  خلاف الضيق والعسر؛ وسع الشيء واتسع (maqayis)؛ وسعت الشيء فاتسع واستوسع؛ توسعوا في المجلس (sihah)؛ وسعت البيت وغيره فاتسع واستوسع؛ جعلنا بينها وبين الأرض سعة (tahdhib)؛ السعة تقال في الأمكنة؛ وسع الشيء اتسع (mufradat)
- **B002** güç yetirme ve alma kapasitesi — güç yetirme kapasitesi · gücü ve maddi varlığı ölçüsünde · bir işe gücü yetmek · bir kabın belirli miktarı içine alması · evinde kalıp onunla yetinmek
  الوسع الجدة والطاقة (maqayis;sihah)؛ الوسع جدة الرجل وقدرة ذات يده؛ طاقتك؛ لا يسعك (ayn)؛ ما أطيقه؛ هل تسع هذا أي هل تطيقه؛ هذا الوعاء يسع عشرين كيلا (tahdhib)؛ الوسع من القدرة؛ لا يكلف الله نفسا إلا وسعها (mufradat)
- **B003** para ve geçim bolluğu — varlık ve para gücü · para ve geçim bolluğu · varlıklı duruma gelmek · varlıklı ve ödeme gücü olan · varlıklı, geçimi bol · Tanrı sana bolluk verdi · gücü ve maddi varlığı ölçüsünde · zengin ve bolluk sahibi
  الوسع الغنى؛ والله الواسع أي الغني؛ الجدة؛ ذو سعة من سعته؛ أوسع الرجل كان ذا سعة (maqayis)؛ جدة الرجل وقدرة ذات يده؛ صار ذا سعة في المال؛ ذو سعة في عيشه (ayn)؛ الجدة والطاقة؛ سعة وغنى؛ أوسع الله عليك أي أغناك (sihah)؛ موسع وهو المليء؛ كثر ماله؛ سعة من عيشه (tahdhib)؛ في الحال؛ الموسع قدره؛ الغنى؛ صار ذا سعة (mufradat)
- **B004** her şeyi kuşatan bilgi, esirgeme, güç ve bağış — bilgisi, esirgemesi, gücü ve bağışı her şeyi kuşatan · Tanrı'nın esirgemesi her şeyi kuşattı · bilgisiyle her şeyi kuşatmak
  رحمة الله وسعت كل شيء (ayn)؛ الواسع من صفات الله؛ وسع رزقه جميع خلقه؛ وسعت رحمته كل شيء؛ المحيط بكل شيء؛ الكثير العطايا (tahdhib)؛ وسع ربنا كل شيء علما؛ والله واسع عليم؛ سعة قدرته وعلمه ورحمته وإفضاله (mufradat)
- **B005** kolaylık tanıyıp güçlüğü azaltma [kalıp] — geniş kolaylık tanıyan ve her şeyi bilen · mal yetmese de güler yüzle insanları hoşnut etmek
  خلاف الضيق والعسر (maqayis)؛ توسعة على الناس في شيء رخص لهم (tahdhib)؛ يكلف عبده دوين ما ينوء به قدرته؛ يريد الله بكم اليسر ولا يريد بكم العسر (mufradat)
- **B006** geniş ve uzun adımlı hızlı gidiş — geniş adımlı, uzun erişimli ve hızlı · geniş adımlı ve hızlı koşan at · atın adım ve bacak erişimi genişliği · geniş ve uzun adımlı gidiş
  الفرس الذريع الخطو وساع (maqayis)؛ وسع الفرس سعة ووساعة فهو وساع؛ سير وسيع ووساع (ayn)؛ فرس وساع أي واسع الخطو؛ وسع وساعة (sihah)؛ فرس وساع إذا كان جوادا ذا سعة في خطوه وذرعه؛ وسع وساعة (tahdhib)؛ فرس وساع الخطو شديد العدو (mufradat)

## ECHO س و ع (root_000760): for 65:7 سَعَةٍ, 65:7 سَعَتِهِۦ: withheld observed target; not identity

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

## ك ل ف (root_001314): 65:7 يُكَلِّفُ

- **B001** yüzde veya ciltte beliren renk bozukluğu — yüzde veya ciltte beliren renk bozukluğu · yüzü lekelenip teni değişmek · yüzü veya cildi kaplayan renk lekesi · renginde hafif karalık veya bulanıklık bulunan · kırmızısına siyahlık karışmış dişi deve
  الكلف شيء يعلو الوجه فيغير بشرته (maqayis)؛ كلف وجهه يكلف كلفا، وبه كلفة، لون يعلو الجلد فيغير بشرته (ayn;tahdhib)؛ الكلف شيء يعلو الوجه كالسمسم، لون بين السواد والحمرة (sihah)؛ البهق الكلف (tahdhib)؛ الكلف في الوجه (mufradat)
- **B002** bir şeye tutkuyla bağlanma — tutkulu bağlılık · bir şeye veya birine tutkuyla bağlanmak · birini bir şeye tutkuyla bağlamak · bir şeye tutkuyla bağlanmış kimse · kadınlara çok düşkün erkek
  أصل صحيح يدل على إيلاع بالشيء وتعلق به (maqayis)؛ الكلف الإيلاع بالشيء، كلف بهذا الأمر وبهذه الجارية (ayn)؛ كلفت بهذا الأمر أي أولعت به (sihah)؛ كلفت بها أشد الكلف إذا أحبها، رجل مكلاف محب للنساء (tahdhib)؛ الكلف الإيلاع بالشيء (mufradat)
- **B003** güçlükle yük üstlenme veya yükümlü kılma — üstlenilen yük veya zahmet · güç gelen bir işle yükümlü kılmak · bir işi zahmetle üstlenmek · gücünü zorlayarak taşıma · güç gelen bir yükümlülük getirme · başkaları için üstlenilen yükler · bir işi güçlükle yapmaya çalışma
  الكلفة ما يتكلف من نائبة أو حق (maqayis;ayn;tahdhib)؛ كلفه تكليفا أي أمره بما يشق عليه، وتكلفت الشيء تجشمته (sihah)؛ حملت الشيء تكلفة إذا لم تطقه إلا تكلفا (sihah)؛ صارت الكلفة اسما للمشقة، لا يكلف الله نفسا إلا وسعها (mufradat)
- **B004** yapay veya yersiz davranma — kendini ilgilendirmeyen işe karışan veya yapmacık davranan kimse · kendini ilgilendirmeyen işlere atılan kimse · gösterişçi yapmacıklık
  المتكلف العريض لما لا يعنيه (maqayis;sihah)؛ المكلف الوقاع فيما لا يعنيه (ayn;tahdhib)؛ التكلف مذموم وهو ما يتحراه الإنسان مراءاة، وما أنا من المتكلفين (mufradat)

## ق ر ي (root_001222): 65:8 قَرْيَةٍ

- **B001** insanların toplandığı yerleşim ve halkı — insanların toplandığı yerleşim ya da o yerin halkı · köyler ya da yerleşimler · ayet bağlamında sözü edilen iki şehir · yerleşimde oturan ile açık arazide yaşayan
  القرية سميت قرية لاجتماع الناس فيها (maqayis)؛ القرية معروفة والجمع القرى؛ القريتين مكة والطائف؛ جاءني كل قار وباد (sihah)؛ القرية اسم للموضع الذي يجتمع فيه الناس وللناس جميعا (mufradat)
- **B002** havuzda, ağızda, yarada veya kursakta toplama ve birikme — havuzda ya da başka bir yerde birikmiş su · suyu havuzda toplamak · bir şeyi ağzında toplamak · devenin yemi yanağında biriktirmesi · irinin yarada birikmesi · suyun biriktiği yer ya da aktığı yatak · yiyecek biriktiren kursak
  قريت الماء في المقراة جمعته؛ وذلك الماء المجموع قرى (maqayis)؛ القري جبي الماء في الحوض؛ المقرى مجتمع ماء كثير؛ المدة تقري في الجرح أي تجتمع (ayn)؛ قريت الماء في الحوض أي جمعت؛ البعير يقري العلف في شدقه أي يجمعه (sihah)؛ قريت الماء في الحوض؛ قرى الشيء في فمه جمعه؛ قريان الماء مجتمعه (mufradat)؛ الجرية الحوصلة كأن أصلها قرية لأنها تقري الشيء أي تجمعه (maqayis-jry)
- **B003** konuğu yiyecekle ağırlama — konuğu yiyecekle ağırlama · konuğu doyurup iyi ağırlamak · konuğa sunulan yiyecek · konukların çevresinde toplandığı büyük yemek çanağı · konuklara yemek sunulan büyük çanaklar · konuğun ağırlandığı yemek kabı
  المقراة الجفنة سميت لاجتماع الضيف عليها أو لما جمع فيها من طعام (maqayis)؛ القرى الإحسان إلى الضيف؛ قراه يقريه قرى؛ المقاري جفان يقرى فيها الأضياف (ayn)؛ المقرى إناء يقرى فيه الضيف؛ قريت الضيف قرى وقراء أحسنت إليه؛ ما قري به الضيف (sihah)؛ قريت الضيف قرى (mufradat)
- **B004** su ya da yiyecek toplayan kap veya oyuk — su ya da yiyecek toplayan havuz, oluk veya büyük çanak · suyun toplandığı yer ya da onu tutan kap · ahşap kap, yalak, uzun havuz ya da oyulmuş toplama yeri · hayvanın su içtiği yalak
  المقراة الجفنة؛ القرو كالمعصرة؛ القرو حوض معروف ممدود (maqayis)؛ المقراة شبه حوض ضخم؛ المقاري جفان؛ المقرى مجتمع ماء كثير (ayn)؛ القرو قدح من خشب؛ القرو ميلغ الكلب؛ القرو أسفل النخلة ينقر؛ القرو حوض طويل؛ المقراة المسيل؛ المقرى إناء؛ الجفنة مقراة (sihah)
- **B005** bir güzergâhı yer yer izleyerek ilerleme — ülkeleri ya da toprakları birer birer izleyip dolaşmak · ülkeleri yer yer izleyerek baştan başa dolaşmak · su kaynaklarını takip etmek · yolun izlenen yönü ya da yanı
  القرو القصد؛ قروت وقريت إذا سلكت؛ يتبعها قرية قرية (maqayis)؛ قروت البلاد وقريتها واقتريتها واستقريتها إذا تتبعتها؛ تقريت المياه أي تتبعتها (sihah)؛ تنح عن سنن الطريق وقريه وقرقه بمعنى واحد (tahdhib)
- **B006** tek yol ya da tek örtü halinde olma [kalıp] — aynı yol ya da durum üzerinde · yağmurun tek örtü gibi kapladığı toprak
  القرو كل شيء على طريقة واحدة؛ رأيت القوم على قرو واحد (maqayis)؛ تركت الأرض قروا واحدا إذا طبقها المطر؛ رأيت القوم على قرو واحد أي على طريقة واحدة (sihah)
- **B007** sırt ve güçlü sırtlı dişi deve — kemiklerin birleştiği sırt · uzun hörgüçlü ya da güçlü sırtlı dişi deve
  القرى الظهر وسمى قرى لما اجتمع فيه من العظام؛ ناقة قرواء شديدة الظهر (maqayis)؛ القرا الظهر؛ ناقة قرواء طويلة السنام ويقال الشديدة الظهر (sihah)
- **B008** ev direğinin başını taşıyan yuvalı ahşap düzenek — ev direğinin başı için yuvası bulunan ahşap düzenek
  القرية على فعيلة خشبات فيها فرض يجعل فيها رأس عمود البيت (sihah)؛ القرية بلا همز أن تؤخذ عصيتان طولهما ذراع ثم يعرض على أطرافهما عويد؛ يكون فيه رأس العمود (tahdhib)
- **B009** toplama ve belirli döneme girme çevresindeki kullanımlar — içindeki hükümleri ve anlatıları bir araya getiren kutsal kitap · temizlik ya da aybaşı dönemi için belirli vakit · kadının temizlikten aybaşına ya da tersine geçmesi · dişi devenin hiç gebe kalmamış olması
  إذا همز هذا الباب كان هو والأول سواء؛ ما قرأت هذه الناقة سلى؛ ومنه القرآن كأنه سمى بذلك لجمعه ما فيه؛ أقرأت المرأة؛ القرء وقت يكون للطهر مرة وللحيض مرة؛ هبت الرياح لقارئها لوقتها
- **B010** izleyip bilgi toplayan tanık — izleyip bilgi toplayarak tanıklık eden kişi · insanları ve yaptıklarını izleyen tanıklar
  القارئة وهو الشاهد؛ الناس قوارى الله تعالى في الأرض هم الشهود؛ يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها (maqayis)؛ الناس قواري الله في الأرض أي شهداء الله؛ يقرون الناس أي يتبعونهم فينظرون إلى أعمالهم (sihah)
- **B011** sürü malı ya da bakmakla yükümlü olunan ev halkı — deve ve koyunlardan oluşan mal varlığı · bakmakla yükümlü olunan ev halkı
  القرة المال من الإبل والغنم؛ والقرة العيال؛ القرة التي هي المال
- **B012** mızrak ucunun sivri tepesi ve keskin kenar — mızrak ucunun en üstteki sivri ve keskin bölümü · bir şeyin keskin ucu ya da kenarı
  مما شذ عن هذا الباب القارية طرف السنان؛ وحد كل شيء قاريته (maqayis)؛ القارية من السنان أعلاه وحده وكذلك حد السيف ونحوه (sihah)

## ع ت و (root_000981): 65:8 عَتَتْ

- **B001** kibirle itaati reddedip sınırı aşma — kibirli itaatsizlik ve sınır tanımazlık · kibirlenip itaate yanaşmamak ve sınırı aşmak · itaate yanaşmayan kibirli zorba · itaate yanaşmayan kibirli zorbalar · itaat etmemek ve karşı gelmek · ahlaksız ve azgın erkekler
  أصل صحيح يدل على استكبار (maqayis)؛ عتا عتوا وعتيا إذا استكبر (ayn)؛ تعتى فلان وتعتت فلانة إذا لم تطع (maqayis;ayn)؛ مجاوزة الحد إذا استكبر (tahdhib)؛ العتو النبو عن الطاعة (mufradat)
- **B002** son sınırına varma; yaşlılıkta geri döndürülemez gerileme — yaşlanıp ömrün gerileme dönemine girmek; son sınırına ulaşmak · düzeltilmesi mümkün olmayan ileri yaşlılık durumu
  عتا الشيخ يعتو عتيا وعتيا كبر وولى (sihah)؛ كل شيء قد انتهى فقد عتا (tahdhib)؛ من الكبر عتيا أي حالة لا سبيل إلى إصلاحها ومداواتها (mufradat)

## ر س ل (root_000563): 65:8 وَرُسُلِهِۦ, 65:11 رَّسُولًا

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

## ش د د (root_000782): 65:8 شَدِيدًا, 65:10 شَدِيدًا

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

## ع ذ ب (root_000994): 65:8 وَعَذَّبْنَٰهَا, 65:8 عَذَابًا, 65:10 عَذَابًا

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

## ن ك ر (root_001550): 65:8 نُّكْرًا

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

## ذ و ق (root_000526): 65:9 فَذَاقَتْ

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

## و ب ل (root_001619): 65:9 وَبَالَ

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

## ع ق ب (root_001033): 65:9 عَٰقِبَةُ

- **B001** bağlama ve kiriş yapımında kullanılan sert beyaz tendon — kiriş yapılan sert beyaz tendon · ayak bileklerinin arkasındaki gergin tendon · oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak
  العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)
- **B002** topuk ve hemen arkasında kalan iz — topuk, ayağın arka bölümü · topuklar · ardınca çok kişi yürüyen, çok izlenen · birinin hemen ardından, onun izinden
  العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)
- **B003** dönüp geri çekilmek [kalıp] — dönüp geri çekilmek · geri dönmedi, arkasına bakmadı veya beklemedi
  ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)
- **B004** ardında kalan çocuklar ve torunlar — kişinin ardından kalan çocukları ve torunları · ardında çocuk veya soy bırakmadı
  عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)
- **B005** birbirinin ardından gelme ve yerini alma — öncekinin ardından gelen ve onun yerini alan · ardıl, bir başkasının ardından gelen · gece ile gündüzün sırayla birbirinin yerini alması · sırayla nöbet değiştiren gece ve gündüz görevlileri · binme veya çalışma sırası, nöbet
  كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)
- **B006** sonuç ve varılan son durum — son, sonuç, varılan nihai durum · karşılık veya sonuç; kimi kullanımda iyi karşılık · buna yol açtı, ardından bunu doğurdu
  أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)
- **B007** suçtan sonra verilen kötü karşılık — ceza, cezalandırma · onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz
  عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)
- **B008** ardından izleyip yeniden inceleme — hak istemek veya itiraz etmek için ardından izleyen kişi · onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur · haberi veya işi yeniden dönüp araştırmak
  المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)
- **B009** aynı tür işi yeniden yapma — aynı tür işi yeniden yapma · atın bir koşudan sonra yeniden ve daha iyi koşması · bir otlak türünden ötekine dönüşümlü geçen deve sürüsü · kuşun yükselişiyle alçalışı arasındaki hareket evresi · ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü
  التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)
- **B010** bedel, satış başvurusu ve elde tutma güvencesi — tutsağın veya bir şeyin yerine alınan bedel · satılan maldan doğan başvuru hakkı ve sorumluluk · malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur
  أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)
- **B011** geride kalan son parça ya da iz — ağır hastalıktan kalan belirti · kapta kalan son yemek suyu · soyluluk ve güzellikten kişide kalan görünür iz
  العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)
- **B012** sarp dağ geçidi ve kayalık çıkıntı — dik ve zorlu dağ yolu veya geçidi · kuyu ya da dağ yüzündeki dışarı taşan kaya
  العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)
- **B013** kartal ve ona benzetilen büyük sancak — kartal, güçlü yırtıcı kuş · kartala benzetilen büyük sancak veya bayrak · korkunç ve ağır bela
  العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)
- **B014** özel adlandırma kümesi — erkek kişi adı · erkek keklik ve ona benzetilen at
  يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)
- **B015** bitkinin sararıp kurumaya yaklaşması [kalıp] — bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak
  عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)

## خ س ر (root_000409): 65:9 خُسْرًا

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

## ل ب ب (root_001338): 65:10 ٱلْأَلْبَٰبِ

- **B001** yerinde kalıp bağlılığını sürdürme — bir yerde kalıp oraya yerleşmek · bir yerde kalmak · bir işe bağlı kalmak · sevgiyle yakın durup bağlı kalmak · buyruğa tekrar tekrar karşılık verip bağlı kalma sözü · çağrıya bağlılık ve boyun eğmeyle karşılık verme · bir evin öteki evin karşısında bulunması · çağrıya karşılık veren ve bağlı kalan kimse
  ألب بالمكان إذا أقام به (maqayis;sihah)؛ رجل لب بهذا الأمر إذا لازمه (maqayis;sihah)؛ لبيك أي أنا مقيم على طاعتك (maqayis;sihah)؛ لب بالمكان وألب به إذا أقام به (jamhara;tahdhib;mufradat)؛ إجابة لك بعد إجابة (tahdhib)؛ اللب الطاعة وأصله من الإقامة (tahdhib)؛ داري تلب دارك أي تحاذيها (sihah)
- **B002** sevecenlikle acıyıp gözetme — sevecenlik ve acıma · koyunun yavrusunu dudaklarıyla yalayıp gözetmesi · acıyan ve yumuşak davranan kimse
  لبلب من الشيء أشفق (maqayis)؛ اللبلبة الرقة على الولد (sihah)؛ لبلبت الشاة على ولدها إذا لحسته (sihah)؛ اللبلبة الشفقة على الإنسان (tahdhib)؛ فعل الشاة بولدها إذا لحسته بشفتيها (tahdhib)
- **B003** bir şeyin özü ve seçkin iç bölümü — öz, iç bölüm veya seçkin kısım · bir şeyin özü ve arı bölümü · soyun arı ve seçkin kesimi · develerin en seçkinleri · develerin seçkinleri ya da boğaz kesim yeri çevreleri
  اللُّب معروف من كل شيء وهو خالصه (maqayis)؛ لب كل شيء خالصه (jamhara;sihah)؛ خالص كل شيء لبابه (maqayis)؛ لب النخل قلبها (sihah)؛ لب الجوز واللوز ما في جوفه (sihah)؛ اللباب الخالص من كل شيء (tahdhib)؛ لباب الإبل خيارها (tahdhib)؛ لب الطعام خالصه (mufradat)
- **B004** us, özellikle arı ve sağlam düşünme gücü — us; özellikle arı ve sağlam düşünme gücü · düşünme ve anlama güçleri · iyi anlayan ve sağlam düşünen kimse · anlayıp doğru düşünebilir duruma gelmek · sağlam düşünme ve anlayışlı olma
  سمى العقل لبا (maqayis)؛ رجل لبيب أي عاقل (maqayis;sihah)؛ لب الرجل إذا صار لبيبا (jamhara)؛ اللب العقل والجمع الألباب (sihah)؛ لب الرجل ما جعل في قلبه من العقل (tahdhib)؛ العقل الخالص من الشوائب (mufradat)؛ كل لب عقل وليس كل عقل لبا (mufradat)
- **B005** boyun altı ile üst göğsün birleştiği bölge — develerin seçkinleri ya da boğaz kesim yeri çevreleri · boyun altı, boğaz kesim yeri veya kolyenin durduğu göğüs bölgesi · kolye yeri ya da hayvanın göğsüne geçirilen kayış · birine boyun altı ile üst göğüs arasından vurmak · birinin giysisini göğsünde toplayıp onu çekmek · giysisini göğsünde sıkıca bağlayıp hazırlanmak
  اللَّبّة موضع القلادة من الصدر (maqayis;sihah)؛ اللَّبّة باطن العنق (jamhara)؛ اللَّبّة المنحر (sihah;tahdhib)؛ اللبب موضع القلادة من الصدر (maqayis;sihah)؛ لببت الرجل ضربت لبته (maqayis;mufradat)؛ لببت فلانا إذا جمعت ثيابه عند صدره ونحره (sihah;tahdhib)؛ متلببا به أي تحزم بثوبه عند صدره (tahdhib)؛ لبب الفرس (maqayis)؛ ما يشد على صدر الدابة (sihah)
- **B006** kumun incelip ovaya bağlanan yakın ucu [kalıp] — kumun dağa veya kum sırtına yakın, incelen uç bölümü
  اللبب من الرمل ما كان قريبا من جبل متصلا بسهل (maqayis)؛ اللبب ما استرق من الرمل (sihah)؛ اللبب من الرمل ما كان قريبا من حبل الرمل (tahdhib)
- **B007** ağaca sarılan, sağaltımda kullanılan ot — ağaca sarılarak büyüyen ve sağaltımda kullanılan ot
  اللبلاب نبت (maqayis)؛ اللبلاب نبت يلتوي على الشجر (sihah)؛ اللبلاب بقلة معروفة يتداوى بها (tahdhib)
- **B008** ince duygunun kaynağı sayılan kalp damarları — ince duygunun kaynağı sayılan kalp damarları
  بنات ألبب عروق في القلب يكون منها الرقة (sihah)
- **B009** yarık üstlüğe benzetilen giysi — yarık üstlüğe benzetilen bir giysi
  اللبيبة ثوب كالبقيرة (sihah)
- **B010** bolluk, esenlik ve güven içinde olma [kalıp] — bolluk, genişlik ve güven içinde olmak
  فلان في لبب رخي إذا كان في حال واسعة (sihah)؛ في سعة وخصب وأمن (tahdhib)؛ في سعة (mufradat)
- **B011** koyun sürüsünün toplu gürültüsü — koyun sürüsünün toplu sesleri ve gürültüsü
  لبالب الغنم جلبتها وأصواتها (sihah)

## ذ ك ر (root_000516): 65:10 ذِكْرًا

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

## ت ل و (root_000186): 65:11 يَتْلُوا۟

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

## ECHO ت ل ل (root_000185): for 65:11 يَتْلُوا۟: withheld observed target; not identity

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

## ء ي ي (root_000074): 65:11 ءَايَٰتِ

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

## ع م ل (root_001046): 65:11 وَعَمِلُوا۟, 65:11 وَيَعْمَلْ

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

## ص ل ح (root_000876): 65:11 ٱلصَّٰلِحَٰتِ, 65:11 صَٰلِحًا

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

## ن و ر (root_001564): 65:11 ٱلنُّورِ

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

## د خ ل (root_000464): 65:11 يُدْخِلْهُ

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

## ج ن ن (root_000266): 65:11 جَنَّٰتٍ

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

## ج ر ي (root_000240): 65:11 تَجْرِى

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

## ت ح ت (root_000177): 65:11 تَحْتِهَا

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ن ه ر (root_001559): 65:11 ٱلْأَنْهَٰرُ

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

## خ ل د (root_000429): 65:11 خَٰلِدِينَ

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

## ء ب د (root_000004): 65:11 أَبَدًا

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

## ح س ن (root_000323): 65:11 أَحْسَنَ

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

## خ ل ق (root_000434): 65:12 خَلَقَ

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

## س ب ع (root_000669): 65:12 سَبْعَ

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

## س م و (root_000745): 65:12 سَمَٰوَٰتٍ

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

## ECHO و س م (root_001650): for 65:12 سَمَٰوَٰتٍ: withheld observed target; not identity

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

## ء ر ض (root_000025): 65:12 ٱلْأَرْضِ

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

## م ث ل (root_001397): 65:12 مِثْلَهُنَّ

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

## ع ل م (root_001040): 65:12 لِتَعْلَمُوٓا۟, 65:12 عِلْمًۢا

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

## ح و ط (root_000372): 65:12 أَحَاطَ

- **B001** fiziksel olarak çevresini sarma — bir şeyin çevresini fiziksel olarak sardı · çevresine duvar ördü · bir yeri çevreleyen duvar · yiyecek için yapılmış çevrili saklama yeri · atlar kişinin çevresini sardı
  هو الشيء يطيف بالشيء (maqayis)؛ احتاطت الخيل بفلان وأحاطت به أي أحدقت (ayn;sihah;tahdhib)؛ الحائط لأنه يحوط ما فيه وحوطت حائطا (ayn;tahdhib)؛ الحائط الجدار الذي يحوط بالمكان (mufradat)؛ الحواطة حظيرة تتخذ للطعام (maqayis;sihah)
- **B002** koruyup gözetme — onu koruyup gözetti · koruma, gözetme ve sürekli ilgilenme · güvenli yolu seçerek önlem alma · sana karşı şefkat ve yakınlık besliyor · alıkonulmanız dışında · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  حطت الرجل أحوطه حوطا إذا حفظته (jamhara)؛ حاطه حيطة إذا تعاهده (ayn;tahdhib)؛ كلأه ورعاه (sihah)؛ الحياطة الحفظ والاحتياط استعمال ما فيه الحياطة (mufradat)؛ تستعمل في المنع (mufradat)؛ مع فلان حيطة لك أي تحنن وتعطف (sihah)
- **B003** eşeğin sürüsünü bir araya toplaması [kalıp] — eşek kendi sürüsünü toplayıp bir araya sürdü
  الحمار يحوط عانته يجمعها (maqayis;ayn;sihah;tahdhib)
- **B004** bir şeyi bütünüyle bilme veya elde etme [kalıp] — onu bütün yönleriyle eksiksiz bildi · şeyin tamamını elde edip denetim altına aldı · hakkında eksiksiz bilgi edinmediği şey
  كل من أحرز شيئا كله وبلغ علمه أقصاه فقد أحاط به (ayn;tahdhib)؛ أحاط به علما (sihah)؛ الإحاطة بالشيء علما هي أن تعلم وجوده وجنسه وقدره وكيفيته (mufradat)
- **B005** çevresinde dönme veya dolaylı yoldan razı etmeye çalışma — o işin çevresinde dönüp duruyorum · istemediği bir şeyi ondan elde etmek için dolaylı yollardan uğraştı
  أنا أحوط حول ذلك الأمر أي أدور (sihah)؛ حاوطت فلانا محاوطة إذا داورته في أمر تريده منه وهو يأباه (tahdhib)
- **B006** karşı konulmaz bir güçle kuşatılıp yıkıma sürüklenme [kalıp] — sonunu getirecek bir gücün altında kaldı · ürünü yok olup bozuldu · karşı koyamayacakları bir güçle kuşatıldılar
  أحيط بفلان إذا دنا هلاكه فهو محاط به (tahdhib)؛ أصابه ما أهلكه وأفسده (tahdhib)؛ أحيط بهم فذلك إحاطة بالقدرة (mufradat)
- **B007** yuvarlak veya hilal biçimli gümüş süs — yuvarlak gümüş süs veya boncuklu iki renkli ipteki gümüş hilal · çocuğa gümüş hilal biçimli süs taktı · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  الحوط شيء مستدير تعلقه المرأة على جبينها من فضة (maqayis)؛ الحوط خيط مفتول من لونين أحمر وأسود وهلال من فضة (tahdhib)؛ أن يحلي صبيه بالحوط وهو هلال من فضة (tahdhib)
- **B008** eksik para tutarını tamamlayan ek miktar — eksik para tutarını tamamlayan ek miktar
  الدراهم إذا نقصت في الفرائض أو غيرها هلم حوطها؛ الحوط ما يتم به دراهمه



===== _commentary/v16/work/s065/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s065/reader_a_pilot.md)

# s065 Semantic Channel Discovery

## Parent Channels

### 1. Counted Thresholds and Lawful Transition
- Semantic invariant: A change of state becomes governable when its duration is counted, its limit is visible, and action is taken at the reached threshold rather than before or after it.
- Surface relation: direct; 65:1-4 anchors the channel in `ع د د` (waiting/count), `ح ص ي` (enumerate), `ء ج ل` and `ب ل غ` (term reached), `ث ل ث` and `ش ه ر` (three months), and `ح د د` (limits).
- Surprising reach: The lexical field turns legal time into a material apparatus of pebbles, weights, balanced loads, appointments, and sky stations.

#### Subchannel A. The Counted Waiting Interval
- Reading type: surface-primary
- Scene or process: A finite interval is enumerated, recurs through known appointments, and remains inside a defined limit until its endpoint.
- Active motifs: exhaustive enumeration (`quranic:root_000332:B002/m01`); counting a set (`quranic:root_000989:B001/m01`); the legally counted waiting period (`quranic:root_000989:B003/m01`); recurrence at known appointed times (`quranic:root_000989:B005/m01`); the number three (`quranic:root_000203:B001/m01`); a month known by its moon (`quranic:root_000823:B001/m01`); a fixed term (`quranic:root_000016:B001/m01`); a quantity brought to its limit (`quranic:root_001205:B001/m01`); a demarcating boundary (`quranic:root_000002:B001/m01`); duration as a span of time (`quranic:root_001700:B002/m01`).
- Ayah anchors: 65:1 `ح ص ي` (أَحْصُ), `ع د د` (عِدَّتِ/عِدَّةَ), `ح د د` (حُدُودُ/حُدُودَ); 65:2 `ء ج ل` (أَجَلَ), `ي و م` (يَوْمِ); 65:3 `ق د ر` (قَدْرًا); 65:4 `ع د د` (عِدَّتُ), `ث ل ث` (ثَلَٰثَةُ), `ش ه ر` (أَشْهُرٍ), `ء ج ل` (أَجَلُ); 65:10 `ع د د` (أَعَدَّ).
- Synthesis: Enumeration does more than summarize elapsed time. Repeated appointments make duration trackable, the term supplies its endpoint, and the boundary prevents either party from treating transition as instantaneous or indefinite.

#### Subchannel B. Reach, Then Retain or Part
- Reading type: surface-primary
- Scene or process: At the reached endpoint, two alternatives are weighed and an existing bond is either held responsibly or released into an actual separation.
- Active motifs: reaching a temporal or practical terminus (`quranic:root_000151:B001/m01`); deliberating between two alternatives (`quranic:root_000991:B008/m01`); holding and preserving (`quranic:root_001424:B001/m01`); separating two parties (`quranic:root_001148:B001/m01`); scattering a union, including separating spouses (`quranic:root_001148:B002/m01`); a divorce that cuts off return (`quranic:root_000170:B012/m01`); release from a tie (`quranic:root_000946:B001/m01`); dissolution of marriage (`quranic:root_000946:B002/m01`); legal release from prohibition or liability (`quranic:root_000946:B005/m01`); passage outside a former state (`quranic:root_000400:B001/m01`); the later or other party (`quranic:root_000019:B001/m01`); what follows after (`quranic:root_000131:B002/m01`).
- Ayah anchors: 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ), `خ ر ج` (تُخْرِجُ/يَخْرُجْ), `ب ع د` (بَعْدَ), `ب ي ن` (مُّبَيِّنَةٍ); 65:2 `ب ل غ` (بَلَغْ), `م س ك` (أَمْسِكُ), `ف ر ق` (فَارِقُ), `ع د ل` (عَدْلٍ), `ء خ ر` (ءَاخِرِ); 65:11 `خ ر ج` (يُخْرِجَ).
- Synthesis: The endpoint is a decision point, not a mere expiration. Retention and parting are weighed as parallel dispositions of the bond: one preserves it, while the other must end both the union and its residual claim rather than preserve control under the name of separation.

#### Subchannel C. Succession, Residual Right, and the New State
- Reading type: mixed
- Scene or process: Companionship ends, but a trailing right or residue follows the former relation into the state that comes after it.
- Active motifs: orderly succession (`quranic:root_001033:B005/m01`); an action's final outcome (`quranic:root_001033:B006/m01`); a remaining trace (`quranic:root_001033:B011/m01`); a debt or right remaining after what preceded it (`quranic:root_000186:B003/m01`); abandonment after companionship (`quranic:root_000186:B005/m01`); becoming a new condition after separation (`quranic:root_000526:B006/m01`); return to a final issue or meaning (`quranic:root_000067:B002/m01`); a new occurrence after nonoccurrence (`quranic:root_000299:B001/m01`); causing a thing to become a new state (`quranic:root_000248:B002/m01`); an event present in time (`quranic:root_001332:B001/m01`); postponement to a later time (`quranic:root_000019:B002/m01`).
- Ayah anchors: 65:1 `ح د ث` (يُحْدِثُ); 65:2 `ج ع ل` (يَجْعَل), `ك و ن` (كَانَ), `ء خ ر` (ءَاخِرِ); 65:4 `ء و ل` (أُو۟لَٰتُ); 65:9 `ع ق ب` (عَٰقِبَةُ), `ك و ن` (كَانَ), `ذ و ق` (ذَاقَتْ); 65:11 `ت ل و` (يَتْلُوا۟).
- Synthesis: Transition retains legal and relational texture: companionship may end while a debt, right, or trace still follows. The prior bond therefore conditions what comes next without imprisoning either party in it, and the aftermath can become a genuinely different state.

#### Subchannel D. Counters, Weights, and Sky Marks
- Reading type: latent/lexical
- Scene or process: Time and quantity become visible through countable objects, standard weights, balanced counterparts, appointments, and celestial stations.
- Active motifs: pebbles used as countable units (`quranic:root_000332:B001/m01`); the known ounce-weight (`quranic:root_001677:B004/m01`); one load balancing another (`quranic:root_000991:B004/m01`); a coin of equal weight (`quranic:root_001273:B015/m01`); the lunar month (`quranic:root_000823:B001/m01`); a sign and appointed time (`quranic:root_000051:B005/m01`); a mark that guides or distinguishes (`quranic:root_001040:B002/m01`); a lunar mansion (`quranic:root_000925:B004/m01`); an encircling crown or moon station (`quranic:root_001315:B005/m01`).
- Ayah anchors: 65:1 `ح ص ي` (أَحْصُ), `ء م ر` (أَمْرًا), `و ق ي` (ٱتَّقُ); 65:2 `ع د ل` (عَدْلٍ), `ق و م` (أَقِيمُ); 65:3/12 `ك ل ل` (كُلِّ); 65:4 `ش ه ر` (أَشْهُرٍ); 65:6 `ض ي ق` (تُضَيِّقُ); 65:12 `ع ل م` (تَعْلَمُ/عِلْمًا).
- Synthesis: The waiting period is lexically materialized as something that can be counted, weighed, balanced, scheduled, and read from a marked sky. Precision is therefore not administrative excess but the means by which an otherwise invisible interval becomes publicly actionable.

#### Subchannel E. When Courtship Reopens
- Reading type: mixed
- Scene or process: Conjugal entry is followed by dissolution and a counted interval; once release is real, the woman's social future becomes visible to new suitors.
- Active motifs: conjugal entry into marriage (`quranic:root_000464:B002/m01`); dissolution of marriage (`quranic:root_000946:B002/m01`); the legally counted waiting period (`quranic:root_000989:B003/m01`); a divorce that cuts off return (`quranic:root_000170:B012/m01`); legal release from prohibition or liability (`quranic:root_000946:B005/m01`); a divorced or widowed woman approached by suitors (`quranic:root_000563:B009/m01`); a woman putting aside her veil (`quranic:root_001657:B009/m01`).
- Ayah anchors: 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ), `ع د د` (عِدَّتِ/عِدَّةَ), `ب ي ن` (مُّبَيِّنَةٍ); 65:4 `ع د د` (عِدَّتُ), `و ض ع` (يَضَعْ); 65:6 `و ض ع` (يَضَعْ), `ب ي ن` (بَيْنَكُم); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا); 65:11 `د خ ل` (يُدْخِلْ), `ب ي ن` (مُبَيِّنَٰتٍ); 65:12 `ب ي ن` (بَيْنَهُنَّ).
- Synthesis: The network supplies the social consequence of a completed endpoint. Divorce is not only departure from a prior bond; after its protected interval, it removes the former relation's exclusive claim on the woman's future and makes a new relational field possible.

### 2. Protected Dwelling and Ethical Enclosure
- Semantic invariant: An enclosure is sound when it gives vulnerable persons room, safety, and continuity; the same enclosing power becomes corrupt when it merely hides injury or truth.
- Surface relation: direct; 65:1 and 65:6 anchor residence in `ب ي ت` and `س ك ن`, while 65:1-5 repeatedly anchors protective restraint in `و ق ي`; 65:11-12 extend enclosure into gardens and comprehensive surrounding.
- Surprising reach: Domestic shelter opens onto shields, curtains, burial houses, and the contrast between reparative covering and deceptive concealment.

#### Subchannel A. Residence, Household, and Belonging
- Reading type: mixed
- Scene or process: A physical dwelling gathers a household, arrests displacement, and fits its resident well enough to become a source of calm.
- Active motifs: abode and shelter (`quranic:root_000166:B001/m01`); the people of a house (`quranic:root_000166:B002/m01`); the marital house (`quranic:root_000166:B010/m01`); household, dependents, and kin defined by mutual return (`quranic:root_000067:B003/m01`); inhabiting or assigning a dwelling (`quranic:root_000726:B002/m01`); cessation of motion in settled stability (`quranic:root_000726:B001/m01`); household residents (`quranic:root_000726:B003/m01`); a beloved place of inward calm (`quranic:root_000726:B004/m01`); a fixed station (`quranic:root_000726:B009/m01`); a place or bed that fails to fit and settle its occupant (`quranic:root_001470:B003/m01`); place and social standing (`quranic:root_001332:B002/m01`); abode or rank (`quranic:root_001492:B003/m01`); an actual, though unspecified, place (`quranic:root_000375:B001/m01`).
- Ayah anchors: 65:1 `ب ي ت` (بُيُوتِ); 65:2 `ك و ن` (كَانَ), `ء و ل` (أُو۟لَٰتُ); 65:3 and 65:6 `ح ي ث` (حَيْثُ); 65:4/10 `ء و ل` (أُو۟لَٰتُ/أُو۟لِى); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:6 `س ك ن` (أَسْكِنُ/سَكَن).
- Synthesis: Housing carries site, membership, mutual return, and fit. A nominal place can still reject its occupant like an unstable saddle or inhospitable bed; the instruction to house therefore asks whether displacement actually stops and a livable station of belonging is restored. A surface anchor is unavailable for `ن ب و` (`quranic:root_001470:B003/m01`) because that root is listed as missing from `surface_context`.

#### Subchannel B. Perimeter as Care
- Reading type: latent/lexical
- Scene or process: A boundary surrounds what is vulnerable, closes the dangerous edge of a dwelling, and preserves a viable interior.
- Active motifs: sensory enclosure by wall or ring (`quranic:root_000372:B001/m01`); guardianship and careful preservation (`quranic:root_000372:B002/m01`); a barrier placed between a thing and harm (`quranic:root_001677:B001/m01`); placing oneself within protection (`quranic:root_001677:B002/m01`); a defensive shield (`quranic:root_000266:B008/m01`); a tent-like protective screen (`quranic:root_001315:B006/m01`); a roof left without a guarding parapet (`quranic:root_000015:B003/m01`); a person exposed with no screen from the sky (`quranic:root_000994:B004/m01`); covering an exposed object (`quranic:root_001307:B001/m01`); restriction that prevents harmful entry or exit (`quranic:root_000002:B002/m01`).
- Ayah anchors: 65:1 `ح د د` (حُدُودُ/حُدُودَ), `و ق ي` (ٱتَّقُ); 65:2/4/5/10 `و ق ي` (يَتَّقِ/ٱتَّقُ); 65:3/12 `ك ل ل` (كُلِّ); 65:5/6 `ء ج ر` (أَجْرًا/أُجُورَ); 65:5 `ك ف ر` (يُكَفِّرْ); 65:8/10 `ع ذ ب` (عَذَّبْ/عَذَابًا); 65:11 `ج ن ن` (جَنَّٰتٍ); 65:12 `ح و ط` (أَحَاطَ).
- Synthesis: The perimeter is not primarily punitive. Wall, screen, shield, and parapet make an interior safe, while the unguarded roof exposes its resident directly to the sky. Divine limits and domestic restrictions are thus care-functions whose legitimacy depends on the hazard they actually avert.

#### Subchannel C. The Empty House and the Last Abode
- Reading type: latent/lexical
- Scene or process: A once-inhabited house empties, a body is lodged in a grave-house, and temporary residence is contrasted with enduring abode.
- Active motifs: a house emptied of its people (`quranic:root_000004:B003/m01`); remaining without departure (`quranic:root_000004:B006/m01`); the grave named as a house (`quranic:root_000166:B007/m01`); covering and interring the dead (`quranic:root_000266:B009/m01`); an isolated settlement or grave (`quranic:root_001307:B012/m01`); abode and final station (`quranic:root_001492:B003/m01`); fixed, prolonged permanence (`quranic:root_000429:B001/m01`); unbounded duration (`quranic:root_000004:B001/m01`).
- Ayah anchors: 65:1 `ب ي ت` (بُيُوتِ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:11 `ج ن ن` (جَنَّٰتٍ), `خ ل د` (خَٰلِدِينَ), `ء ب د` (أَبَدًا), `ك ف ر` is attested at 65:5 (يُكَفِّرْ).
- Synthesis: Removal from a house is lexically shadowed by the house that becomes vacant and by the grave understood as lodging. Against these diminished dwellings, permanent residence acquires force: present housing duties matter precisely because every human station is vulnerable to vacancy and replacement.

#### Subchannel D. Covering that Repairs or Deceives
- Reading type: mixed
- Scene or process: One covering effaces injury and prevents recurrence; another hides truth while corruption remains active underneath.
- Active motifs: expiation that covers an offense as though it had not been done (`quranic:root_001307:B009/m01`); a bad act requiring remediation (`quranic:root_000755:B001/m01`); self-placement behind a moral guard (`quranic:root_001677:B002/m01`); concealment or denial of truth (`quranic:root_001307:B003/m01`); a displayed entrance with a hidden exit, the mechanism of hypocrisy (`quranic:root_001537:B004/m02`); corruption concealed in an interior (`quranic:root_000464:B004/m01`).
- Ayah anchors: 65:5 `ك ف ر` (يُكَفِّرْ), `س و ء` (سَيِّـَٔاتِ), `و ق ي` (يَتَّقِ); 65:6/7 `ن ف ق` (أَنفِقُ/يُنفِقْ); 65:11 `د خ ل` (يُدْخِلْ).
- Synthesis: Reparative covering changes the standing of the harm; deceptive covering only changes its visibility. The contrast pressures every protected interior, including the household, to be judged by whether injury is actually removed or merely made inaccessible to witnesses.

### 3. Gestation, Delivery, and New Kinship
- Semantic invariant: A hidden bodily development reaches a timed release, becomes publicly legible in birth, and generates new obligations of nourishment, payment, and relation.
- Surface relation: direct; 65:4 and 65:6 explicitly connect menstruation, pregnancy, term, delivery, nursing, and compensation.
- Surprising reach: The branch network fills the surface timeline with fetal concealment, labor pain, afterbirth, nursing teeth, milk-flow, foster relation, and caregiving roles.

#### Subchannel A. Reproductive Clock and Hidden Load
- Reading type: mixed
- Scene or process: Bodily signs determine uncertainty and duration across cessation with age, irregular bleeding, and concealed fetal development.
- Active motifs: menstrual blood and its appointed time (`quranic:root_000379:B001/m01`); bleeding that persists beyond its ordinary interval (`quranic:root_000379:B002/m01`); the cloth used to absorb menstrual blood (`quranic:root_000379:B003/m01`); expectation cut off in despair (`quranic:root_001690:B001/m01`); old age reaching a terminal bodily state (`quranic:root_000981:B002/m01`); doubt and uneasy uncertainty (`quranic:root_000616:B001/m01`); pregnancy as an inward load (`quranic:root_000357:B002/m01`); the fetus hidden in the womb (`quranic:root_000266:B007/m01`); the fixed term (`quranic:root_000016:B001/m01`); the counted waiting period (`quranic:root_000989:B003/m01`); months known by their moons (`quranic:root_000823:B001/m01`).
- Ayah anchors: 65:2/4 `ء ج ل` (أَجَلَ/أَجَلُ); 65:4 `ح ي ض` (مَحِيضِ/يَحِضْ), `ي ء س` (يَئِسْ), `ر ي ب` (ٱرْتَبْ), `ح م ل` (أَحْمَالِ/حَمْلَ), `ع د د` (عِدَّتُ), `ش ه ر` (أَشْهُرٍ); 65:8 `ع ت و` (عَتَتْ); 65:11 `ج ن ن` (جَنَّٰتٍ).
- Synthesis: The waiting rule is grounded in a body whose state may have ceased with age, become irregular, or remain hidden in development. Cloth, blood, womb, fetus, month, and term form one evidentiary clock: legal time answers embodied uncertainty instead of abstracting it away.

#### Subchannel B. Labor, Release, and Afterbirth
- Reading type: mixed
- Scene or process: Labor tightens into pain, the load is put down, and bodily material exits as signs of completed delivery.
- Active motifs: contractions and the pain of labor (`quranic:root_000946:B008/m01`); obstructed or difficult childbirth (`quranic:root_001012:B006/m01`); putting down the pregnancy in birth (`quranic:root_001657:B002/m01`); childbirth and postpartum blood (`quranic:root_001533:B005/m01`); afterbirth and uterine discharge (`quranic:root_000994:B009/m01`); the membrane covering a newborn's head and hands at emergence (`quranic:root_001424:B010/m01`); material emerging with the child as a birth-sign (`quranic:root_000822:B006/m01`); blood, pus, or discharge emerging from within (`quranic:root_001550:B005/m01`).
- Ayah anchors: 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ); 65:2 `ش ه د` (أَشْهِدُ/شَّهَٰدَةَ), `م س ك` (أَمْسِكُ); 65:4/6 `و ض ع` (يَضَعْ); 65:6 `ع س ر` (تَعَاسَرْ); 65:8 `ع ذ ب` (عَذَّبْ/عَذَابًا), `ن ك ر` (نُّكْرًا); 65:1/7 `ن ف س` (نَفْسَ/نَفْسًا).
- Synthesis: The lexical convergence of divorce-release and labor-release is not a claim of identity; it is a functional analogy. Both transitions require pain to be carried to a real endpoint, a load to be relinquished, and completion to be materially recognizable rather than merely declared.

#### Subchannel C. Nursing, Fosterage, and Compensated Care
- Reading type: mixed
- Scene or process: Milk sustains the newborn, repeated feeding creates a kin-like relation, and caregiving receives an acknowledged wage.
- Active motifs: suckling from breast or udder (`quranic:root_000568:B001/m01`); milk-kinship equivalent to family relation (`quranic:root_000568:B002/m01`); the front teeth used by a nursing child (`quranic:root_000568:B004/m01`); abundant, successive milk-flow (`quranic:root_000563:B006/m01`); increase of milk and offspring (`quranic:root_001694:B006/m01`); compensation for work or contract (`quranic:root_000015:B001/m01`); food that enters and sustains the body (`quranic:root_000560:B002/m01`); the stepchild and the adult who raises the child (`quranic:root_000532:B005/m01`); tender care figured by a ewe licking its young (`quranic:root_001338:B002/m01`).
- Ayah anchors: 65:5/6 `ء ج ر` (أَجْرًا/أُجُورَ); 65:6 `ر ض ع` (أَرْضَعْ/تُرْضِعُ); 65:7/11 `ر ز ق` (رِزْقُ/رِزْقًا), `ي س ر` (يُسْرًا at 65:4/7); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا); 65:1/8 `ر ب ب` (رَبَّ/رَبِّ); 65:10 `ل ب ب` (أَلْبَٰبِ).
- Synthesis: Nursing is not an incidental service after separation. It is a bodily transfer of sustenance that can create durable social relation; payment recognizes that the labor belongs to the care-scene rather than disappearing into assumed household duty.

#### Subchannel D. The Child Relation Outlives the Couple
- Reading type: mixed
- Scene or process: A child follows the mother, remains as posterity, and continues to bind caregivers even when conjugal relation or verified lineage is absent.
- Active motifs: offspring following their mothers (`quranic:root_000186:B006/m01`); surviving children and descendants (`quranic:root_001033:B004/m01`); the womb-tie that holds people in relation (`quranic:root_001424:B009/m01`); a foundling or child of uncertain lineage (`quranic:root_000357:B005/m01`); a dependent, orphan, or person carried by another (`quranic:root_001315:B002/m01`); the bond between parties (`quranic:root_000170:B003/m01`); milk-kinship equivalent to family relation (`quranic:root_000568:B002/m01`); the stepchild and adult foster-carer (`quranic:root_000532:B005/m01`).
- Ayah anchors: 65:1/6/11/12 `ب ي ن` (مُّبَيِّنَةٍ/بَيْنَ/مُبَيِّنَٰتٍ); 65:1/8 `ر ب ب` (رَبَّ/رَبِّ); 65:2 `م س ك` (أَمْسِكُ); 65:3/12 `ك ل ل` (كُلِّ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:6 `ر ض ع` (أَرْضَعْ/تُرْضِعُ); 65:9 `ع ق ب` (عَٰقِبَةُ); 65:11 `ت ل و` (يَتْلُوا۟).
- Synthesis: Divorce can end the couple without ending the child's relation to either care or kin. The foundling and milk-kin cases make the pressure sharper: dependency itself can generate durable responsibility even where lineage is uncertain or care is supplied by someone outside the former pair.

### 4. Carrying, Balancing, and Discharging Trust
- Semantic invariant: Responsibility behaves like a load: it must be accepted by a capable bearer, balanced by support, and delivered rather than abandoned or passed indefinitely.
- Surface relation: indirect; 65:3 anchors entrustment in `و ك ل`, 65:4-7 anchors physical and imposed loads in `ح م ل` and `ك ل ف`, and 65:8-11 anchors carried communication in `ر س ل`.
- Surprising reach: Pregnancy and command are joined not by topic but by a shared mechanics of load, carrier, counterweight, support-frame, agent, and accountable handoff.

#### Subchannel A. Entrusted Load and Surety
- Reading type: mixed
- Scene or process: A burden or right is placed with a responsible party who must preserve it, stand for it, and not let mutual dependence dissolve accountability.
- Active motifs: an entrusted message, obligation, or guilt borne by a person (`quranic:root_000357:B003/m01`); surety for a debt or penalty (`quranic:root_000357:B004/m01`); an imposed burden requiring exertion (`quranic:root_001314:B003/m01`); legal or personal guarantee (`quranic:root_001332:B003/m01`); delegating an affair (`quranic:root_001681:B001/m01`); the capable keeper, guarantor, or sufficient agent (`quranic:root_001681:B006/m01`); a right or liability that follows its holder (`quranic:root_000186:B004/m01`); a deposit placed with another (`quranic:root_001657:B010/m01`); standing over an affair in care and governance (`quranic:root_001273:B004/m01`); security, trust, and safekeeping (`quranic:root_000054:B001/m01`).
- Ayah anchors: 65:2/10/11 `ء م ن` (يُؤْمِنُ/ءَامَنُ/يُؤْمِنۢ), `ق و م` (أَقِيمُ at 65:2), `ك و ن` (كَانَ at 65:2); 65:3 `و ك ل` (يَتَوَكَّلْ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:7 `ك ل ف` (يُكَلِّفُ); 65:11 `ت ل و` (يَتْلُوا۟), `و ض ع` is attested at 65:4/6 (يَضَعْ).
- Synthesis: Entrustment does not mean that a task becomes ownerless. Guarantee, deposit, stewardship, and carried obligation all preserve a traceable bearer. This sharpens the distinction between relying on a sufficient guardian and using reliance to evade one's assigned duty.

#### Subchannel B. The Load-Bearing Frame
- Reading type: latent/lexical
- Scene or process: A carried weight is stabilized by a mount, counterload, upright members, and a frame that transfers force without collapse.
- Active motifs: carrying an exposed load (`quranic:root_000357:B001/m01`); a mount, litter, or carrying apparatus (`quranic:root_000357:B006/m01`); a counterload balanced on the other side (`quranic:root_000991:B004/m01`); a carrier or bearing tool (`quranic:root_000067:B008/m01`); an upright structural member (`quranic:root_001273:B012/m01`); crosspieces bearing a house-pole (`quranic:root_001222:B008/m01`); the wooden frame of a saddle (`quranic:root_001029:B009/m01`); a heavy beam, stick, or bundle (`quranic:root_001619:B004/m01`); the working legs of an animal (`quranic:root_001046:B010/m01`).
- Ayah anchors: 65:2/4/10 `ء و ل` (أُو۟لَٰتُ/أُو۟لِى); 65:2 `ع د ل` (عَدْلٍ), `ق و م` (أَقِيمُ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:8 `ق ر ي` (قَرْيَةٍ), `و ب ل` at 65:9 (وَبَالَ); 65:5 `ع ظ م` (يُعْظِمْ); 65:11 `ع م ل` (عَمِلُ/يَعْمَلْ).
- Synthesis: Support is distributed rather than magical: load, opposite load, carrier, legs, crossbeam, and saddle frame each take a role. The scene gives concrete form to proportional obligation: asking one member to bear everything destroys the very structure meant to carry the weight.

#### Subchannel C. Message as a Delivered Burden
- Reading type: mixed
- Scene or process: A report is carried by an authorized intermediary along a route and discharged through delivery to its recipients.
- Active motifs: dispatch and release in contrast to holding back (`quranic:root_000563:B001/m01`); conveying a message to its destination (`quranic:root_000151:B002/m01`); messenger and carried communication (`quranic:root_000563:B002/m01`); consequential report brought from elsewhere (`quranic:root_001464:B002/m01`); message borne as an entrusted load (`quranic:root_000357:B003/m01`); an agent, runner, or guarantor (`quranic:root_000240:B003/m01`); a keeper who is sufficient for the commissioned affair (`quranic:root_001681:B006/m01`); sending or bringing something down to its recipients (`quranic:root_001492:B002/m01`).
- Ayah anchors: 65:2/3 `ب ل غ` (بَلَغْ/بَٰلِغُ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا); 65:11 `ج ر ي` (تَجْرِى), `ن ب ء` is anchored at 65:1 (نَّبِىُّ); 65:3 `و ك ل` (يَتَوَكَّلْ).
- Synthesis: The message-scene joins semantic content to logistics. Authority does not eliminate mediation: a report must be released, carried by a bearer, routed to recipients, and discharged in completed delivery. Recitation and command are thereby framed as fulfilled carriage, not disembodied information.

#### Subchannel D. From Mandate to Executed Work
- Reading type: mixed
- Scene or process: An affair becomes a command, is prepared and delegated through an office, and reaches completion as deliberate work by an appointed agent.
- Active motifs: an affair or case requiring disposition (`quranic:root_000051:B001/m01`); command as request and obligation (`quranic:root_000051:B002/m01`); authority and appointed office (`quranic:root_000051:B003/m01`); preparing means for a coming matter (`quranic:root_000989:B002/m01`); approaching an affair properly and becoming ready (`quranic:root_000009:B003/m01`); resolving and rising to undertake it (`quranic:root_001273:B003/m01`); delegating an affair (`quranic:root_001681:B001/m01`); putting a person or instrument to work (`quranic:root_001046:B002/m01`); appointment to an administered work (`quranic:root_001046:B003/m01`); intentional action (`quranic:root_001046:B001/m01`); beginning and persisting in an act (`quranic:root_000248:B004/m01`); managing an affair through reform (`quranic:root_000067:B004/m01`).
- Ayah anchors: 65:1/3-6/8-9/12 `ء م ر` (أَمْرًا/أَمْرِ/أْتَمِرُ); 65:1/4/10 `ع د د` (عِدَّتِ/عِدَّةَ/عِدَّتُ/أَعَدَّ); 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ); 65:2 `ق و م` (أَقِيمُ); 65:2-4/7 `ج ع ل` (يَجْعَل/جَعَلَ); 65:2/4/10 `ء و ل` (أُو۟لَٰتُ/أُو۟لِى); 65:3 `و ك ل` (يَتَوَكَّلْ); 65:11 `ع م ل` (عَمِلُ/يَعْمَلْ).
- Synthesis: Command is not self-executing. The network separates the affair, mandate, authority, preparation, delegation, office, intentional act, and persistence, so responsibility remains traceable from the one who commissions work to the one who actually performs it.

### 5. Provision as Calibrated Circulation
- Semantic invariant: Sustenance remains just and life-giving when it is apportioned to actual capacity, transmitted as due compensation, and kept moving through channels of storage, growth, and care.
- Surface relation: direct; 65:3-7 and 65:11 repeatedly anchor provision, means, outlay, wage, capacity, constriction, and ease in `ر ز ق`, `ن ف ق`, `ء ج ر`, `و س ع`, `و ج د`, `ق د ر`, `ع س ر`, and `ي س ر`.
- Surprising reach: Economic provision materializes as hydrology, irrigation, seed-cover, flowering, pasture, milk-flow, and balanced household ecology rather than as an undifferentiated wealth domain.

#### Subchannel A. Means, Capacity, and Proportional Outlay
- Reading type: surface-primary
- Scene or process: A due outlay is scaled to actual means and the support needed to keep life standing, without turning possible depletion into a pretext for withholding.
- Active motifs: an apportioned share or benefit (`quranic:root_000560:B001/m01`); bodily nourishment (`quranic:root_000560:B002/m01`); expenditure on self and dependents (`quranic:root_001537:B002/m01`); goods or provisions reaching exhaustion (`quranic:root_001537:B001/m01`); capacity and tolerance (`quranic:root_001647:B002/m01`); material means and ample living (`quranic:root_001647:B003/m01`); practical enlargement that removes hardship (`quranic:root_001647:B005/m01`); found means and wealth (`quranic:root_001626:B003/m01`); provision narrowed to a small measure (`quranic:root_001205:B004/m01`); insolvency and straitened means (`quranic:root_001012:B002/m01`); opening and ease after difficulty (`quranic:root_001694:B001/m01`); prosperity and solvency (`quranic:root_001694:B003/m01`); sufficiency that answers need (`quranic:root_000318:B003/m01`); subsistence sufficient for continued life (`quranic:root_000151:B003/m01`); livelihood as the support by which life stands (`quranic:root_001273:B009/m01`); giving or bringing a due thing (`quranic:root_000009:B002/m01`).
- Ayah anchors: 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ); 65:2 `ق و م` (أَقِيمُ); 65:2/3 `ب ل غ` (بَلَغْ/بَٰلِغُ), `ح س ب` at 65:3/8 (يَحْتَسِبُ/حَسْبُ/حَاسَبْ/حِسَابًا); 65:3/7/11 `ر ز ق` (يَرْزُقْ/رِزْقُ/رِزْقًا); 65:3/7/12 `ق د ر` (قَدْرًا/قُدِرَ/قَدِيرٌ); 65:6/7 `ن ف ق` (أَنفِقُ/يُنفِقْ), `ع س ر` (تَعَاسَرْ/عُسْرٍ), `و ج د` (وُجْدِ), `و س ع` (سَعَةٍ/سَعَتِ), `ي س ر` (يُسْرًا).
- Synthesis: Capacity is neither a pretext for withholding nor an instruction to spend into collapse. Allotment, possible exhaustion, livelihood-support, narrow measure, sufficiency, and ease form a proportional rule: obligation follows real capacity while the system actively seeks a route from scarcity toward viability.

#### Subchannel B. Wage, Valuation, and Reciprocal Compensation
- Reading type: mixed
- Scene or process: Labor produces a recognized claim that is valued, paid, and circulated rather than absorbed without acknowledgment.
- Active motifs: wage or contractual compensation (`quranic:root_000015:B001/m01`); the worker's pay (`quranic:root_001046:B004/m01`); an offered fee for a completed task (`quranic:root_000248:B005/m01`); a continuing stipend or grant (`quranic:root_000240:B006/m01`); a levy or known outgoing (`quranic:root_000400:B003/m01`); income entering an estate (`quranic:root_000464:B006/m01`); a due tax or payment rendered (`quranic:root_000009:B008/m01`); an equivalent value or substitute (`quranic:root_000991:B003/m01`); appraisal and pricing (`quranic:root_001273:B010/m01`).
- Ayah anchors: 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ); 65:2 `ع د ل` (عَدْلٍ), `ق و م` (أَقِيمُ), `ج ع ل` (يَجْعَل); 65:2/11 `خ ر ج` (مَخْرَجًا/يُخْرِجَ); 65:5/6 `ء ج ر` (أَجْرًا/أُجُورَ); 65:11 `ج ر ي` (تَجْرِى), `د خ ل` (يُدْخِلْ), `ع م ل` (عَمِلُ/يَعْمَلْ).
- Synthesis: Compensation is a conversion mechanism: care-work becomes an acknowledged claim, valuation makes the claim commensurable, and payment moves resources to the bearer of the work. This prevents family obligation from becoming invisible extraction.

#### Subchannel C. Reservoir, Channel, and Released Water
- Reading type: latent/lexical
- Scene or process: Water descends or arrives, is gathered in a basin, held without loss, and then released through a channel to sustain land and bodies.
- Active motifs: cutting or directing a watercourse (`quranic:root_000009:B004/m01`); floodwater arriving from another region (`quranic:root_000009:B005/m01`); a broad cistern collecting well, canal, or rainwater (`quranic:root_000016:B007/m01`); a rock basin or newly dug well (`quranic:root_000434:B011/m01`); abundant gathered water (`quranic:root_000532:B013/m01`); a perennial well (`quranic:root_000989:B004/m01`); a deep source with much water (`quranic:root_001040:B005/m01`); gathering water in a settled basin (`quranic:root_001222:B002/m01`); a bowl, trough, or channel that receives it (`quranic:root_001222:B004/m01`); ground or lining that holds water (`quranic:root_001424:B004/m01`); a river channel cut through earth (`quranic:root_001559:B001/m01`); opening and widening a passage until it flows (`quranic:root_001559:B003/m01`); continuous flow (`quranic:root_000240:B001/m01`); rain descending as provision (`quranic:root_000560:B003/m01`); water sufficient to sustain life (`quranic:root_001533:B008/m01`); sweet, palatable water (`quranic:root_000994:B001/m01`).
- Ayah anchors: 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ); 65:2/4 `ء ج ل` (أَجَلَ/أَجَلُ); 65:3/7/11 `ر ز ق` (يَرْزُقْ/رِزْقُ/رِزْقًا); 65:8 `ق ر ي` (قَرْيَةٍ), `ر ب ب` (رَبِّ); 65:10 `ع د د` (أَعَدَّ); 65:11 `ج ر ي` (تَجْرِى), `ن ه ر` (أَنْهَٰرُ); 65:12 `خ ل ق` (خَلَقَ), `ع ل م` (تَعْلَمُ/عِلْمًا); `م س ك` is anchored at 65:2 (أَمْسِكُ), `ن ف س` at 65:1/7 (نَفْسَ/نَفْسًا), and `ع ذ ب` at 65:8/10 (عَذَّبْ/عَذَابًا).
- Synthesis: Provision is not merely possessed; it is routed. The reservoir must retain water, but retention serves a later release into field, river, and drink. This hydrological mechanism makes the ethical distinction between prudent storage and sterile withholding especially sharp.

#### Subchannel D. Covered Seed to Mature Yield
- Reading type: latent/lexical
- Scene or process: Seed is covered, protected through early growth, pollinated and flowered, then bears fruit before eventual withering.
- Active motifs: a farmer covering seed with soil (`quranic:root_001307:B008/m01`); the calyx or sheath covering fruit (`quranic:root_001307:B010/m01`); fertile, well-grown soil (`quranic:root_000025:B002/m01`); young or short palms (`quranic:root_000248:B006/m01`); palm shoots (`quranic:root_000568:B005/m01`); pollinating tall palms (`quranic:root_000946:B014/m01`); a tree flowering (`quranic:root_001564:B004/m01`); crop and fruit yield (`quranic:root_000009:B007/m01`); fruit borne as a plant's load (`quranic:root_000357:B002/m02`); dense, vigorous vegetation (`quranic:root_000266:B011/m01`); a stem yellowing toward dryness (`quranic:root_001033:B015/m01`); a plant that remains green (`quranic:root_000532:B012/m01`).
- Ayah anchors: 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ), `ط ل ق` at 65:1 (طَلَّقْ/طَلِّقُ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:5 `ك ف ر` (يُكَفِّرْ); 65:6 `ر ض ع` (أَرْضَعْ/تُرْضِعُ); 65:8 `ر ب ب` (رَبِّ); 65:9 `ع ق ب` (عَٰقِبَةُ); 65:11 `ج ن ن` (جَنَّٰتٍ), `ن و ر` (نُّورِ); 65:12 `ء ر ض` (أَرْضِ), `ج ع ل` is attested at 65:2-4/7.
- Synthesis: Yield depends on a sequence of functional restraints: burial under soil, enclosure by a sheath, patient growth, pollination, and only then fruit. The scene resists treating increase as immediate acquisition; provision matures through protected stages and can still be lost through neglect or exhaustion.

#### Subchannel E. Pasture, Milk, and Household Ecology
- Reading type: latent/lexical
- Scene or process: Livestock are kept near pasture and water, released to graze, gathered for care, and converted into milk and offspring that sustain a household.
- Active motifs: holding livestock in pasture (`quranic:root_000016:B008/m01`); feed sufficient to keep a group settled (`quranic:root_000726:B010/m01`); keeping camels around pasture and water (`quranic:root_001657:B007/m01`); animals released for grazing (`quranic:root_000946:B006/m01`); a laboring she-camel separating from the herd (`quranic:root_001148:B008/m01`); repeated milk-flow (`quranic:root_000563:B006/m01`); nursing the young (`quranic:root_000568:B001/m01`); increase in milk and offspring (`quranic:root_001694:B006/m01`); a young lamb (`quranic:root_000357:B009/m01`); a female that bears every year (`quranic:root_000004:B004/m01`); a ewe recently delivered and kept close for milk (`quranic:root_000532:B009/m01`).
- Ayah anchors: 65:2/4 `ء ج ل` (أَجَلَ/أَجَلُ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:6 `ر ض ع` (أَرْضَعْ/تُرْضِعُ), `س ك ن` (أَسْكِنُ/سَكَن), `و ض ع` (يَضَعْ); 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ); 65:2 `ف ر ق` (فَارِقُ); 65:4/7 `ي س ر` (يُسْرًا); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا), `ر ب ب` (رَبِّ at 65:8); 65:11 `ء ب د` (أَبَدًا).
- Synthesis: Release and restraint alternate according to function: animals are released to feed but kept within access to water and care; birth separates one animal from the herd but creates milk and new dependence. The scene offers a concrete ecology for post-separation provision, where freedom, location, nourishment, and continued care remain interdependent.

#### Subchannel F. The Milking Sound Withheld from a Claimant
- Reading type: latent/lexical
- Scene or process: A householder can prepare food openly for a guest or suppress the sound of milking so that a guest, dependent, or claimant cannot ask for a share.
- Active motifs: secretly suckling livestock so a guest or claimant cannot hear milking (`quranic:root_000568:B003/m01`); honoring a guest with gathered food (`quranic:root_001222:B003/m01`); provision prepared for an arriving guest (`quranic:root_001492:B005/m01`); withholding wealth through avarice (`quranic:root_001424:B002/m01`); miserliness carried beyond ordinary ugliness (`quranic:root_001134:B005/m01`); a small reserve that keeps its holder alive (`quranic:root_001424:B003/m01`); wealth and dependents gathered in one household (`quranic:root_001222:B011/m01`); a dependent or orphan carried as another's burden (`quranic:root_001315:B002/m01`); giving with willing ease (`quranic:root_000563:B010/m01`).
- Ayah anchors: 65:1 `ف ح ش` (فَٰحِشَةٍ); 65:2 `م س ك` (أَمْسِكُ); 65:3/12 `ك ل ل` (كُلِّ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:6 `ر ض ع` (أَرْضَعْ/تُرْضِعُ); 65:8 `ق ر ي` (قَرْيَةٍ), `ر س ل` (رُسُلِ); 65:11 `ر س ل` (رَّسُولًا).
- Synthesis: The hidden milking image identifies a precise failure of provision: the resource exists, but its signal is deliberately silenced so that need cannot become a claim. The life-preserving reserve marks the other side of the distinction, separating prudent retention from concealment designed to defeat a dependent's access.

### 6. From Constriction to a Governed Way Out
- Semantic invariant: Relief is a change in affordance: pressure is reduced, an outlet becomes traversable, and motion is guided so that release does not become disorientation.
- Surface relation: direct; 65:2, 65:4, 65:6, and 65:7 explicitly join `خ ر ج`, `ض ي ق`, `ع س ر`, `ي س ر`, and `و س ع` in a pressure-to-passage sequence.
- Surprising reach: The way out becomes a tunnel with an outlet, a road with a fork and endpoint, a horse controlled through rein and gait, and a vessel stabilized by its rudder.

#### Subchannel A. Pressure, Venting, and Room
- Reading type: mixed
- Scene or process: Spatial, emotional, and economic pressure become bearable when an opening, margin, or practical allowance is created.
- Active motifs: lack of spatial room (`quranic:root_000925:B001/m01`); chest-constriction and inability to bear (`quranic:root_000925:B002/m01`); narrow livelihood and restricted spending (`quranic:root_000925:B003/m01`); difficulty opposed to ease (`quranic:root_001012:B001/m01`); obstructive conflict and complication (`quranic:root_001012:B004/m01`); an opening into ease (`quranic:root_001694:B001/m01`); physical spaciousness (`quranic:root_001647:B001/m01`); practical latitude that removes hardship (`quranic:root_001647:B005/m01`); venting a constricted condition (`quranic:root_001533:B002/m01`); room, distance, and respite (`quranic:root_001533:B015/m01`); opening and widening until flow becomes possible (`quranic:root_001559:B003/m01`).
- Ayah anchors: 65:6 `ض ي ق` (تُضَيِّقُ), `ع س ر` (تَعَاسَرْ); 65:7 `ع س ر` (عُسْرٍ), `و س ع` (سَعَةٍ/سَعَتِ), `ن ف س` (نَفْسًا), `ي س ر` (يُسْرًا); 65:11 `ن ه ر` (أَنْهَٰرُ).
- Synthesis: Constriction appears in several media but retains one mechanism: too little room for body, breath, resources, or agreement. Relief therefore requires an operative enlargement, not simply an optimistic description of the same blocked condition.

#### Subchannel B. Outlet through a Concealed Conduit
- Reading type: latent/lexical
- Scene or process: An interior connects to the outside through a passage whose outlet makes real departure possible.
- Active motifs: emergence from an enclosure or state (`quranic:root_000400:B001/m01`); bringing a hidden thing into visibility (`quranic:root_000400:B002/m01`); a subterranean tunnel with a functioning outlet (`quranic:root_001537:B003/m01`); an entrance paired with a concealed exit (`quranic:root_001537:B004/m01`); entering an interior (`quranic:root_000464:B001/m01`); separation after prior connection (`quranic:root_000170:B001/m01`); release from a tie (`quranic:root_000946:B001/m01`); a public road, route, or convergence of paths (`quranic:root_000009:B010/m01`).
- Ayah anchors: 65:1/6/7 `ء ت ي` (يَأْتِي/ـَٔاتُ/ءَاتَىٰ); 65:1/2/11 `خ ر ج` (تُخْرِجُ/يَخْرُجْ/مَخْرَجًا/يُخْرِجَ); 65:1/6/11/12 `ب ي ن` (مُّبَيِّنَةٍ/بَيْنَ/مُبَيِّنَٰتٍ); 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ); 65:6/7 `ن ف ق` (أَنفِقُ/يُنفِقْ); 65:11 `د خ ل` (يُدْخِلْ).
- Synthesis: An exit is defined by connectivity, not by naming an outside. Tunnel, entrance, hidden egress, and emergence form a complete passage-mechanism. This makes the promised outlet concrete while also exposing the danger of arrangements that display openness but keep the effective exit concealed.

#### Subchannel C. Clear Road, Fork, and Destination
- Reading type: latent/lexical
- Scene or process: A traveler follows an established road, encounters a branching point, and reaches a marked destination.
- Active motifs: a clear road that takes a traveler where intended (`quranic:root_001464:B007/m01`); a guiding road (`quranic:root_001470:B005/m01`); a well-used path (`quranic:root_001046:B011/m01`); tracking successive stretches of route (`quranic:root_001222:B005/m01`); a road-fork (`quranic:root_001148:B006/m01`); a public thoroughfare (`quranic:root_000009:B010/m01`); a visible tract of land (`quranic:root_000170:B007/m01`); following an established model or way (`quranic:root_001397:B010/m01`); arrival at the ultimate endpoint (`quranic:root_000076:B001/m01`); reaching the destination (`quranic:root_000151:B001/m01`).
- Ayah anchors: 65:1 `ن ب ء` (نَّبِىُّ), `ب ي ن` (مُّبَيِّنَةٍ), and `ء ت ي` (يَأْتِي); 65:2 `ب ل غ` (بَلَغْ), `ف ر ق` (فَارِقُ); 65:8 `ق ر ي` (قَرْيَةٍ); 65:11 `ع م ل` (عَمِلُ/يَعْمَلْ), `م ث ل` is anchored at 65:12 (مِثْلَ). Surface anchors are unavailable for `ن ب و` (`quranic:root_001470:B005/m01`) and `ء ل ي` (`quranic:root_000076:B001/m01`) because both roots are listed as missing from `surface_context`.
- Synthesis: The path image supplies more than generic guidance. It distinguishes a route from open terrain, a fork from an endpoint, and patterned travel from wandering. A legitimate way out must therefore be intelligible enough to follow and complete.

#### Subchannel D. Release under Rein and Rudder
- Reading type: latent/lexical
- Scene or process: Forward movement is enabled by measured release while gait, hoof, direction, and stabilizer keep the traveler from losing control.
- Active motifs: extending the rein to increase a horse's run (`quranic:root_000151:B007/m01`); unimpeded forward movement (`quranic:root_000946:B003/m01`); running at speed (`quranic:root_000993:B002/m01`); a wide and forceful stride (`quranic:root_001647:B006/m01`); compliant, light gait (`quranic:root_001694:B005/m01`); a mount that lags by relying on another (`quranic:root_001681:B005/m01`); guarding an injured hoof from rough ground (`quranic:root_001677:B003/m01`); a ship's rudder or stern stabilizer (`quranic:root_000726:B008/m01`); deviation from the proper course (`quranic:root_000991:B006/m01`); urging a mount into speed (`quranic:root_001657:B003/m01`).
- Ayah anchors: 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ), `ع د و` (يَتَعَدَّ); 65:2 `ب ل غ` (بَلَغْ), `ع د ل` (عَدْلٍ); 65:3 `و ك ل` (يَتَوَكَّلْ); 65:4/6 `و ض ع` (يَضَعْ); 65:6 `س ك ن` (أَسْكِنُ/سَكَن); 65:7 `و س ع` (سَعَةٍ/سَعَتِ), `ي س ر` (يُسْرًا); 65:1-5/10 `و ق ي` (ٱتَّقُ/يَتَّقِ).
- Synthesis: Release is not the opposite of governance. Rein, gait, protected hoof, course correction, and rudder show that movement becomes safer when freedom and steering operate together. The analogy usefully pressures both detention disguised as care and abandonment disguised as freedom.

### 7. Truth Made Public and Actionable
- Semantic invariant: Knowledge becomes socially binding when it moves from perception into visible sign, intelligible statement, present witness, and accountable acknowledgment.
- Surface relation: direct; 65:1-2 and 65:10-12 repeatedly anchor clarification, testimony, recitation, reminder, sign, messenger, and knowledge in `ب ي ن`, `ش ه د`, `ذ ك ر`, `ء ي ي`, `ر س ل`, and `ع ل م`.
- Surprising reach: Evidence is assembled as a route from hidden state to landmark, spoken testimony, carried report, and public recognition, with fabrication and disguised exits as its structural opposite.

#### Subchannel A. Present Witness and Explicit Proof
- Reading type: mixed
- Scene or process: A person is present, knows what occurred, renders it in speech, and supplies marks by which the claim can be recognized.
- Active motifs: presence with direct observation (`quranic:root_000822:B001/m01`); testimony delivered from knowledge (`quranic:root_000822:B002/m01`); the tongue as witness (`quranic:root_000822:B005/m01`); an indicator that testifies to a condition (`quranic:root_000822:B008/m01`); visible disclosure and clear proof (`quranic:root_000170:B004/m01`); speech or sign that exposes meaning (`quranic:root_000170:B005/m01`); recognition through trace or mark (`quranic:root_001002:B003/m01`); confession and acknowledgment (`quranic:root_001002:B009/m01`); visible features by which a face or place is known (`quranic:root_001002:B013/m01`); knowledge opposed to ignorance (`quranic:root_001040:B001/m01`); a distinguishing marker (`quranic:root_001040:B002/m01`); direct knowing (`quranic:root_000473:B001/m01`); investigating or seeking a report (`quranic:root_000318:B010/m01`).
- Ayah anchors: 65:1/6/11/12 `ب ي ن` (مُّبَيِّنَةٍ/بَيْنَ/مُبَيِّنَٰتٍ); 65:1 `د ر ي` (تَدْرِى); 65:2 `ش ه د` (أَشْهِدُ/شَّهَٰدَةَ), `ع ر ف` (مَعْرُوفٍ); 65:3/8 `ح س ب` (يَحْتَسِبُ/حَسْبُ/حَاسَبْ/حِسَابًا); 65:6 `ع ر ف` (مَعْرُوفٍ); 65:12 `ع ل م` (تَعْلَمُ/عِلْمًا).
- Synthesis: Testimony is a composite act: presence grounds knowledge, the tongue makes it public, visible marks permit recognition, and acknowledgment closes the gap between fact and responsibility. Witnessing thus prevents a private transition from becoming an unverifiable exercise of power.

#### Subchannel B. Revelation as Carried and Recited Message
- Reading type: mixed
- Scene or process: A consequential report descends, is borne by a messenger, follows in ordered recitation, and reaches its recipient as accepted admonition.
- Active motifs: messenger and message (`quranic:root_000563:B002/m01`); a consequential report conveyed from elsewhere (`quranic:root_001464:B002/m01`); the prophetic bearer who reports from God (`quranic:root_001464:B003/m01`); one element following another in sequence (`quranic:root_000186:B001/m01`); retaining and recalling what might be forgotten (`quranic:root_000516:B003/m01`); making a thing present on the tongue (`quranic:root_000516:B004/m01`); a reminder that restores attention (`quranic:root_000516:B009/m01`); warning counsel that recalls consequences and softens the heart (`quranic:root_001663:B001/m01`); conveying communication to its endpoint (`quranic:root_000151:B002/m01`); a manifest sign (`quranic:root_000074:B003/m01`); sending something down to recipients (`quranic:root_001492:B002/m01`); speech that makes meaning clear (`quranic:root_000170:B005/m01`).
- Ayah anchors: 65:1 `ن ب ء` (نَّبِىُّ), `ب ي ن` (مُّبَيِّنَةٍ); 65:2 `و ع ظ` (يُوعَظُ); 65:2/3 `ب ل غ` (بَلَغْ/بَٰلِغُ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا); 65:10 `ذ ك ر` (ذِكْرًا); 65:11 `ت ل و` (يَتْلُوا۟), `ء ي ي` (ءَايَٰتِ), `ب ي ن` (مُبَيِّنَٰتٍ).
- Synthesis: Message, bearer, sequential delivery, clarification, memory, and admonition form one communication process. The report is actionable because it is not left at its source: it arrives, is voiced in order, recalls consequences, and is received as a reason to change conduct.

#### Subchannel C. Landmark, Appointment, and Orienting Light
- Reading type: mixed
- Scene or process: Visible marks identify a boundary, announce an appointed point, and orient a traveler toward the right route.
- Active motifs: a sign and appointed time (`quranic:root_000051:B005/m01`); a landmark or marked boundary (`quranic:root_001040:B002/m01`); a beacon, minaret, or road-marker (`quranic:root_001564:B005/m01`); a raised crest visible at distance (`quranic:root_001002:B002/m01`); public appearance and notoriety (`quranic:root_000823:B002/m01`); an overt sign (`quranic:root_000074:B003/m01`); a demarcating limit (`quranic:root_000002:B001/m01`); a fixed endpoint (`quranic:root_000016:B001/m01`); a clear road leading to its destination (`quranic:root_001464:B007/m01`).
- Ayah anchors: 65:1 `ء م ر` (أَمْرًا), `ح د د` (حُدُودُ/حُدُودَ), `ن ب ء` (نَّبِىُّ); 65:2/4 `ء ج ل` (أَجَلَ/أَجَلُ); 65:4 `ش ه ر` (أَشْهُرٍ), `ع ر ف` is anchored at 65:2/6 (مَعْرُوفٍ); 65:11 `ء ي ي` (ءَايَٰتِ), `ن و ر` (نُّورِ); 65:12 `ع ل م` (تَعْلَمُ/عِلْمًا).
- Synthesis: A rule becomes navigable when its limits, times, and route are perceptible. Appointment and landmark join temporality to space, while light makes the marks readable. The channel therefore connects clear law with practical orientation rather than mere promulgation.

#### Subchannel D. Fabricated Report and Disguised Exit
- Reading type: latent/lexical
- Scene or process: False speech manufactures an event, assumes borrowed authority, and hides the route by which its maker evades accountability.
- Active motifs: inventing false speech or narrative (`quranic:root_000434:B007/m01`); falsely claiming prophetic authority (`quranic:root_001464:B004/m01`); saying a lie about another (`quranic:root_000186:B009/m01`); concealing or denying truth (`quranic:root_001307:B003/m01`); displaying one entrance while hiding another exit (`quranic:root_001537:B004/m02`); denial and refusal of recognition (`quranic:root_001550:B001/m01`); altering a thing until it is no longer recognized (`quranic:root_001550:B004/m01`); corruption kept inside an apparently sound exterior (`quranic:root_000464:B004/m01`).
- Ayah anchors: 65:1 `ن ب ء` (نَّبِىُّ); 65:5 `ك ف ر` (يُكَفِّرْ); 65:6/7 `ن ف ق` (أَنفِقُ/يُنفِقْ); 65:8 `ن ك ر` (نُّكْرًا); 65:11 `ت ل و` (يَتْلُوا۟), `خ ل ق` at 65:12 (خَلَقَ), `د خ ل` (يُدْخِلْ).
- Synthesis: Falsehood is not only incorrect content. It is an engineered mismatch among exterior, interior, authority, and escape route. That mechanism is the negative image of testimony, where the witness, statement, sign, and responsibility remain aligned.

### 8. Repair at the Point of Fracture
- Semantic invariant: Repair acknowledges a break or misalignment, restores fit among the parts, and re-establishes a workable relation without pretending that no fracture occurred.
- Surface relation: direct; 65:2 and 65:6 anchor right dealing, justice, testimony, and consultation, while 65:11 anchors rectifying action in `ص ل ح`.
- Surprising reach: Social reconciliation is materially reframed through bone-setting, counterweight, straightening, polishing, tightened bonds, and the draining of a hidden lesion.

#### Subchannel A. Social Settlement and Right Relation
- Reading type: mixed
- Scene or process: Estranged parties negotiate a recognized settlement, preserve testimony, and realign conduct with justice.
- Active motifs: repair opposed to corruption (`quranic:root_000876:B001/m01`); reconciliation that removes mutual estrangement (`quranic:root_000876:B002/m01`); fittingness for a person or circumstance (`quranic:root_000876:B003/m01`); conduct recognized as good by reason and custom (`quranic:root_001002:B005/m01`); justice in judgment and testimony (`quranic:root_000991:B001/m01`); straightening a thing into balance (`quranic:root_000991:B005/m01`); the bond or connection between parties (`quranic:root_000170:B003/m01`); a pact, covenant, or protected compact (`quranic:root_000532:B011/m01`); consultation and considered agreement (`quranic:root_000051:B007/m01`); mutual placement of an agreed matter (`quranic:root_001657:B011/m01`); reciprocal dealing between people (`quranic:root_001046:B005/m01`); testimony rendered from knowledge (`quranic:root_000822:B002/m01`); uprightness and rectitude (`quranic:root_001273:B008/m01`).
- Ayah anchors: 65:1/6/11/12 `ب ي ن` (مُّبَيِّنَةٍ/بَيْنَ/مُبَيِّنَٰتٍ); 65:1/3-6/8-9/12 `ء م ر` (أَمْرًا/أَمْرِ/أْتَمِرُ); 65:1/8 `ر ب ب` (رَبَّ/رَبِّ); 65:2 `ش ه د` (أَشْهِدُ/شَّهَٰدَةَ), `ع د ل` (عَدْلٍ), `ق و م` (أَقِيمُ), `ع ر ف` (مَعْرُوفٍ); 65:6 `ع ر ف` (مَعْرُوفٍ), `و ض ع` is anchored at 65:4/6 (يَضَعْ); 65:11 `ع م ل` (عَمِلُ/يَعْمَلْ), `ص ل ح` (صَّٰلِحَٰتِ/صَٰلِحًا).
- Synthesis: Reconciliation is neither forced reunion nor unstructured compromise. It is a witnessed process of consultation, covenant, fit, recognized conduct, and straightened relation. The branch network thus locates repair in procedure and mutual commitment as much as in intention.

#### Subchannel B. Setting, Balancing, and Polishing
- Reading type: latent/lexical
- Scene or process: A damaged or uneven object is measured, set, counterbalanced, tightened, and polished back into service.
- Active motifs: setting a broken bone that healed crooked (`quranic:root_000015:B002/m01`); a load that balances its counterpart (`quranic:root_000991:B004/m01`); straightening an object (`quranic:root_000991:B005/m01`); restoring upright alignment (`quranic:root_001273:B008/m01`); equal weight without excess (`quranic:root_001273:B015/m01`); measuring material before cutting (`quranic:root_000434:B001/m01`); polishing a blade or a corroded heart (`quranic:root_000299:B007/m01`); tightening a bond or fastening (`quranic:root_000782:B001/m01`); repairing, nurturing, and bringing to completion (`quranic:root_000532:B002/m01`); managing an affair by reforming it (`quranic:root_000067:B004/m01`).
- Ayah anchors: 65:2 `ع د ل` (عَدْلٍ), `ق و م` (أَقِيمُ); 65:4/6/10 `ء و ل` (أُو۟لَٰتُ/أُو۟لِى); 65:5/6 `ء ج ر` (أَجْرًا/أُجُورَ); 65:8 `ر ب ب` (رَبِّ), `ش د د` (شَدِيدًا); 65:1 `ح د ث` (يُحْدِثُ); 65:12 `خ ل ق` (خَلَقَ).
- Synthesis: Repair is a disciplined sequence: diagnose the displacement, measure the parts, restore balance, secure the join, then remove corrosion. The surprising bone-setting sense of `ء ج ر` lets compensation itself resonate with making a fracture usable again.

#### Subchannel C. Draining Hidden Pathology
- Reading type: latent/lexical
- Scene or process: A swelling or lesion becomes visible, discharges what is trapped inside, and the body returns toward stable function.
- Active motifs: recovery when fever or disease departs (`quranic:root_001148:B010/m01`); convalescence after illness (`quranic:root_001397:B012/m01`); pain subsiding after a recurring attack (`quranic:root_000946:B010/m01`); swelling or distension (`quranic:root_001470:B006/m01`); a boil or lesion emerging on the body (`quranic:root_000400:B004/m01`); corrupt discharge leaving the interior (`quranic:root_001550:B005/m01`); an ulcer worsening through retained pus (`quranic:root_000025:B011/m01`); opening a passage so material can flow (`quranic:root_001559:B003/m01`).
- Ayah anchors: 65:1 `ط ل ق` (طَلَّقْ/طَلِّقُ), `خ ر ج` (تُخْرِجُ/يَخْرُجْ); 65:2 `ف ر ق` (فَارِقُ); 65:8 `ن ك ر` (نُّكْرًا); 65:11 `م ث ل` is anchored at 65:12 (مِثْلَ), `ن ه ر` (أَنْهَٰرُ); 65:12 `ء ر ض` (أَرْضِ). A surface anchor is unavailable for `ن ب و` (`quranic:root_001470:B006/m01`) because that root is listed as missing from `surface_context`.
- Synthesis: This is repair by truthful exposure: a hidden pressure must surface and drain before recovery can begin. As an analogy for social fracture, it rejects cosmetic settlement that closes over retained injury.

#### Subchannel D. Grievance, Record, and Review
- Reading type: mixed
- Scene or process: An injured party states a grievance, petitions an authority, supplies a documented right, and can pursue investigation and review toward equitable redress.
- Active motifs: a grievance seeking equity from a wrongdoer (`quranic:root_000967:B003/m01`); petitioning a governor or judge against injury (`quranic:root_000993:B005/m01`); a deed or certificate recording a right (`quranic:root_000516:B008/m01`); testimony rendered from knowledge (`quranic:root_000822:B002/m01`); justice in judgment and testimony (`quranic:root_000991:B001/m01`); practical accountability and public inspection (`quranic:root_000318:B006/m01`); following a judgment to question, claim, object, or review (`quranic:root_001033:B008/m01`); investigating or seeking a report (`quranic:root_000318:B010/m01`); harshly pressing an insolvent debtor (`quranic:root_001012:B003/m01`).
- Ayah anchors: 65:1 `ظ ل م` (ظَلَمَ), `ع د و` (يَتَعَدَّ); 65:2 `ش ه د` (أَشْهِدُ/شَّهَٰدَةَ), `ع د ل` (عَدْلٍ); 65:3/8 `ح س ب` (يَحْتَسِبُ/حَسْبُ/حَاسَبْ/حِسَابًا); 65:6/7 `ع س ر` (تَعَاسَرْ/عُسْرٍ); 65:9 `ع ق ب` (عَٰقِبَةُ); 65:10 `ذ ك ر` (ذِكْرًا).
- Synthesis: Witnessing is completed here by recourse. The claim becomes inspectable through record and testimony, and review keeps authority answerable after an initial decision. The insolvent-debtor motif also limits the claimant: redress must recover a right without turning the process itself into coercive injury.

### 9. Boundary Crossing Becomes Felt Consequence
- Semantic invariant: Exceeding a limit converts an abstract violation into damaged relation, coercive force, measurable loss, and an aftermath experienced by bodies and communities.
- Surface relation: direct; 65:1 names limits, transgression, wrongdoing, and manifest indecency, while 65:8-10 names disobedience, reckoning, punishment, tasting, consequence, and loss.
- Surprising reach: A legal boundary hardens into iron edge and armed point, while communal loss appears as the once-inhabited settlement reduced to an empty house and residue.

#### Subchannel A. Crossing the Line and Misplacing the Right
- Reading type: mixed
- Scene or process: A marked limit is crossed, a thing or right is put where it does not belong, and another party bears deliberate harm.
- Active motifs: a separating limit (`quranic:root_000002:B001/m01`); transgression and unjust aggression (`quranic:root_000993:B001/m01`); excess beyond proper measure (`quranic:root_001134:B002/m01`); proud refusal of obedience (`quranic:root_000981:B001/m01`); placing an act in the wrong time or location (`quranic:root_000967:B004/m01`); withholding or imprisoning another's right (`quranic:root_000967:B008/m01`); reciprocal or intentional injury (`quranic:root_000907:B002/m01`); wrong that reason or law demands be stopped (`quranic:root_001550:B006/m01`); manifest badness (`quranic:root_000755:B001/m01`).
- Ayah anchors: 65:1 `ح د د` (حُدُودُ/حُدُودَ), `ع د و` (يَتَعَدَّ), `ف ح ش` (فَٰحِشَةٍ), `ظ ل م` (ظَلَمَ); 65:5 `س و ء` (سَيِّـَٔاتِ); 65:6 `ض ر ر` (تُضَآرُّ); 65:8 `ع ت و` (عَتَتْ), `ن ك ر` (نُّكْرًا).
- Synthesis: Violation is specified as a role error: boundary crossed, right withheld, place or time misused, and harm imposed. This precision prevents transgression from becoming a vague moral label detached from the party made to bear it.

#### Subchannel B. When the Boundary Becomes an Armed Edge
- Reading type: latent/lexical
- Scene or process: A hard material is sharpened, mounted on a shaft, fastened with sinew, and turned into a point capable of enforcement or injury.
- Active motifs: iron and resistant hardness (`quranic:root_000002:B004/m01`); a cutting or piercing edge (`quranic:root_000002:B005/m01`); arming a shaft with a spearhead (`quranic:root_000051:B011/m01`); hard, forceful sharpness (`quranic:root_000516:B002/m01`); the tip of a spear or blade (`quranic:root_001222:B012/m01`); a pointed horn or comb-like tool (`quranic:root_000473:B004/m01`); the working shaft immediately behind a spearhead (`quranic:root_001046:B009/m01`); tightening a fastening (`quranic:root_000782:B001/m01`); white sinew used to bind weapons and bowstrings (`quranic:root_001033:B001/m01`).
- Ayah anchors: 65:1 `ح د د` (حُدُودُ/حُدُودَ), `ء م ر` (أَمْرًا), `د ر ي` (تَدْرِى); 65:8 `ق ر ي` (قَرْيَةٍ), `ش د د` (شَدِيدًا); 65:9 `ع ق ب` (عَٰقِبَةُ); 65:10 `ذ ك ر` (ذِكْرًا); 65:11 `ع م ل` (عَمِلُ/يَعْمَلْ).
- Synthesis: The sharp-edge scene is a transformation of boundary into force. Demarcation itself protects, but once opposition escalates, hardness, point, shaft, and binding assemble an instrument that can wound. The reach warns how quickly lawful restraint can be converted into coercion.

#### Subchannel C. Tasting, Reckoning, and Loss
- Reading type: mixed
- Scene or process: Conduct is calculated, returned as a heavy and bodily experienced result, and registered as loss or deterrent example.
- Active motifs: learning an event by undergoing it (`quranic:root_000526:B002/m01`); a heavy, harmful aftermath (`quranic:root_001619:B002/m01`); an outcome the body cannot comfortably absorb (`quranic:root_001619:B003/m01`); painful punishment (`quranic:root_000994:B005/m01`); severe force or suffering (`quranic:root_000782:B002/m01`); the final consequence of an action (`quranic:root_001033:B006/m01`); punishment following fault (`quranic:root_001033:B007/m01`); general diminution (`quranic:root_000409:B001/m01`); commercial loss of capital (`quranic:root_000409:B002/m01`); short measure or deficient weight (`quranic:root_000409:B003/m01`); reckoning and calculation (`quranic:root_000318:B001/m01`); a person or people becoming a public story (`quranic:root_000299:B004/m01`); a saying circulated as a proverb (`quranic:root_001397:B003/m01`); exemplary punishment that deters others (`quranic:root_001397:B002/m01`); an event made into a lesson (`quranic:root_001397:B011/m01`); a day understood as crisis or great event (`quranic:root_001700:B003/m01`).
- Ayah anchors: 65:1 `ح د ث` (يُحْدِثُ); 65:3/8 `ح س ب` (يَحْتَسِبُ/حَسْبُ/حَاسَبْ/حِسَابًا); 65:8/10 `ش د د` (شَدِيدًا), `ع ذ ب` (عَذَّبْ/عَذَابًا); 65:9 `ذ و ق` (ذَاقَتْ), `و ب ل` (وَبَالَ), `ع ق ب` (عَٰقِبَةُ), `خ س ر` (خُسْرًا); 65:2 `ي و م` (يَوْمِ); 65:12 `م ث ل` (مِثْلَ).
- Synthesis: Consequence becomes cognitive, somatic, economic, and public: it is known by tasting, felt as weight, calculated as account, recorded as deficit, and retold until the actors themselves become a cautionary saying. Accountability therefore persists beyond the first experience of cost.

#### Subchannel D. From Inhabited Settlement to Residue
- Reading type: mixed
- Scene or process: A gathered community loses its viable order, its houses empty, and only remnant and isolated place remain.
- Active motifs: people gathered in a settled community (`quranic:root_001222:B001/m01`); the inhabited house (`quranic:root_000166:B001/m01`); a dwelling emptied of its people (`quranic:root_000004:B003/m01`); an isolated village or grave-place (`quranic:root_001307:B012/m01`); destruction, banishment, or removal from good (`quranic:root_000131:B004/m01`); residue left after an event (`quranic:root_001033:B011/m01`); diminution and loss (`quranic:root_000409:B001/m01`); a heavy harmful aftermath (`quranic:root_001619:B002/m01`); a calamity descending on a group (`quranic:root_001492:B006/m01`).
- Ayah anchors: 65:1 `ب ي ت` (بُيُوتِ), `ب ع د` (بَعْدَ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:8 `ق ر ي` (قَرْيَةٍ); 65:9 `و ب ل` (وَبَالَ), `ع ق ب` (عَٰقِبَةُ), `خ س ر` (خُسْرًا); 65:11 `ء ب د` (أَبَدًا); 65:5 `ك ف ر` (يُكَفِّرْ).
- Synthesis: The punished settlement is not an abstract collective. It is an inhabited arrangement whose failure can be read in emptied houses and residual traces. This communal scale reflects back on the household: repeated injustice can unmake the very dwelling and society that law was meant to preserve.

#### Subchannel E. Coercion that Manufactures Defiance
- Reading type: mixed
- Scene or process: Pressure is applied before consent or readiness, escalates through harsh speech and compulsion, and drives a formerly compliant person into the breach later named as disobedience.
- Active motifs: carrying or compelling a person into an affair (`quranic:root_000831:B003/m01`); taking property or speech before consent and preparation (`quranic:root_001012:B008/m01`); harsh verbal rebuke (`quranic:root_001559:B004/m01`); compulsion into what is hated or harmful (`quranic:root_000907:B003/m01`); forcing an obedient person into disobedience (`quranic:root_001307:B007/m01`); departure from one's group, origin, or obedience (`quranic:root_000400:B006/m01`); proud refusal to obey (`quranic:root_000981:B001/m01`).
- Ayah anchors: 65:1/2/11 `خ ر ج` (تُخْرِجُ/يَخْرُجْ/مَخْرَجًا/يُخْرِجَ); 65:3/12 `ش ي ء` (شَىْءٍ); 65:5 `ك ف ر` (يُكَفِّرْ); 65:6 `ض ر ر` (تُضَآرُّ), `ع س ر` (تَعَاسَرْ); 65:7 `ع س ر` (عُسْرٍ); 65:8 `ع ت و` (عَتَتْ); 65:11 `ن ه ر` (أَنْهَٰرُ).
- Synthesis: The causal order matters. A party can create the very breach later cited against the other by seizing before readiness, using verbal pressure, and compelling harmful conduct. This pressures accountability to distinguish autonomous defiance from disobedience manufactured by coercive power.

### 10. Inner Steadiness before an Unseen Future
- Semantic invariant: Uncertain outcomes are met by disciplined discernment, responsible entrustment, and composure that makes room for action without pretending to control what is not known.
- Surface relation: direct; 65:1 names not knowing what may arise, 65:3 names reliance and sufficiency, 65:4 names doubt, and 65:10 addresses people of pure intellect.
- Surprising reach: Trust is tested against weak dependency and mutual shirking, while composure is embodied as a settled dwelling, an expanded chest, breath after pressure, and deliberate pace.

#### Subchannel A. Doubt, Discernment, and Penetrating Judgment
- Reading type: mixed
- Scene or process: An uncertain observer distinguishes conjecture from knowledge by recognition, rational steadiness, and farsighted judgment.
- Active motifs: perturbing doubt and suspicion (`quranic:root_000616:B001/m01`); direct knowledge (`quranic:root_000473:B001/m01`); pure and discerning intellect (`quranic:root_001338:B004/m01`); rational steadiness and sound judgment (`quranic:root_000332:B003/m01`); conjecture held in the mind (`quranic:root_000318:B002/m01`); knowledge opposed to ignorance (`quranic:root_001040:B001/m01`); recognition through a trace (`quranic:root_001002:B003/m01`); shrewdness and acuity (`quranic:root_001550:B002/m01`); deep or far-reaching judgment (`quranic:root_000131:B008/m01`); inward intention and reflective mind (`quranic:root_001533:B013/m01`).
- Ayah anchors: 65:1 `د ر ي` (تَدْرِى), `ب ع د` (بَعْدَ), `ح ص ي` (أَحْصُ), `ن ف س` (نَفْسَ); 65:2/6 `ع ر ف` (مَعْرُوفٍ); 65:3/8 `ح س ب` (يَحْتَسِبُ/حَسْبُ/حَاسَبْ/حِسَابًا); 65:4 `ر ي ب` (ٱرْتَبْ); 65:8 `ن ك ر` (نُّكْرًا); 65:10 `ل ب ب` (أَلْبَٰبِ); 65:12 `ع ل م` (تَعْلَمُ/عِلْمًا).
- Synthesis: Uncertainty is not answered by impulsive certainty. The branch scene distinguishes suspicion, estimate, recognition, rational steadiness, and deep judgment, allowing the unknown future to remain unknown while present obligations are still decided intelligently.

#### Subchannel B. Entrustment without Shirking
- Reading type: mixed
- Scene or process: A person delegates what exceeds personal control to a sufficient keeper while continuing to carry the portion that remains assigned.
- Active motifs: entrusting an affair to another (`quranic:root_001681:B001/m01`); active reliance (`quranic:root_001681:B002/m01`); the sufficient keeper and guarantor (`quranic:root_001681:B006/m01`); security and trustworthiness (`quranic:root_000054:B001/m01`); conviction that settles the heart (`quranic:root_000054:B002/m01`); a weak dependent who abandons his own affair (`quranic:root_001681:B003/m01`); mutual reliance by which a task is lost (`quranic:root_001681:B004/m01`); standing over an affair in care (`quranic:root_001273:B004/m01`); carrying an entrusted obligation (`quranic:root_000357:B003/m01`); steadfast response and repeated obedience (`quranic:root_001338:B001/m01`).
- Ayah anchors: 65:2/10/11 `ء م ن` (يُؤْمِنُ/ءَامَنُ/يُؤْمِنۢ), `ق و م` (أَقِيمُ at 65:2); 65:3 `و ك ل` (يَتَوَكَّلْ); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:10 `ل ب ب` (أَلْبَٰبِ).
- Synthesis: Reliance has a built-in contrast case. Trust in a sufficient keeper stabilizes action; dependence on an incapable party, or reciprocal waiting for someone else to act, makes the affair disappear. The channel therefore reads reliance as disciplined allocation of agency, not passivity.

#### Subchannel C. Composure that Creates Room
- Reading type: mixed
- Scene or process: Distress settles when the inner space becomes habitable, pressure is vented, and action proceeds with patience and deliberateness.
- Active motifs: a beloved refuge in which the self becomes calm (`quranic:root_000726:B004/m01`); a patient, composed self (`quranic:root_001002:B010/m01`); relief that vents distress (`quranic:root_001533:B002/m01`); room and respite (`quranic:root_001533:B015/m01`); deliberateness and unhurried conduct (`quranic:root_000563:B004/m01`); ease and interpersonal openness (`quranic:root_000563:B007/m01`); opening after difficulty (`quranic:root_001694:B001/m01`); mindful self-protection (`quranic:root_001677:B002/m01`); despair as the cutting off of expectation (`quranic:root_001690:B001/m01`); a hidden heart or inward core (`quranic:root_000266:B010/m01`); a thought settled in the heart (`quranic:root_000429:B004/m01`); chest-constriction as the opposite state (`quranic:root_000925:B002/m01`).
- Ayah anchors: 65:1-5/10 `و ق ي` (ٱتَّقُ/يَتَّقِ); 65:2/6 `ع ر ف` (مَعْرُوفٍ); 65:4 `ي ء س` (يَئِسْ), `ي س ر` (يُسْرًا); 65:6 `س ك ن` (أَسْكِنُ/سَكَن), `ض ي ق` (تُضَيِّقُ); 65:7 `ن ف س` (نَفْسًا), `ي س ر` (يُسْرًا); 65:8/11 `ر س ل` (رُسُلِ/رَّسُولًا); 65:11 `ج ن ن` (جَنَّٰتٍ), `خ ل د` (خَٰلِدِينَ).
- Synthesis: Composure is spatial and kinetic: an interior settles, breath returns, room opens, and pace becomes deliberate. This is neither emotional suppression nor indefinite delay; it is the condition in which a pressured decision can be made without reproducing the pressure as harm.

### 11. Layered Creation and Descending Order
- Semantic invariant: Creation is organized as related levels, measures, and passages through which command, rain, light, knowledge, and life-giving flow move without escaping comprehensive order.
- Surface relation: direct; 65:11-12 names gardens, flowing rivers, permanence, seven heavens, corresponding earth, descending command, total power, and encompassing knowledge.
- Surprising reach: The cosmic statement becomes an architecture of upper and lower levels, measured fabrication, weather circulation, and a permanent garden whose flow resolves the surah's recurrent problems of shelter and provision.

#### Subchannel A. Upper, Lower, Between, and Descent
- Reading type: surface-primary
- Scene or process: Multiple upper and lower levels correspond across an interval, while something ordered descends and takes its proper place among them.
- Active motifs: the lower earth opposed to sky (`quranic:root_000025:B001/m01`); what is above and overshadows (`quranic:root_000745:B004/m01`); the region beneath (`quranic:root_000177:B001/m01`); the number seven (`quranic:root_000669:B001/m01`); correspondence and likeness (`quranic:root_001397:B001/m01`); the interval between distinct sides (`quranic:root_000170:B002/m01`); descent from above (`quranic:root_001492:B001/m01`); placing each thing in its proper rank (`quranic:root_001492:B004/m01`); assigning a thing a state or rank (`quranic:root_000248:B002/m01`); totality that gathers all parts (`quranic:root_001315:B003/m01`).
- Ayah anchors: 65:1/6/11/12 `ب ي ن` (مُّبَيِّنَةٍ/بَيْنَ/مُبَيِّنَٰتٍ); 65:2-4/7 `ج ع ل` (يَجْعَل/جَعَلَ); 65:3/12 `ك ل ل` (كُلِّ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:11 `ت ح ت` (تَحْتِ); 65:12 `ء ر ض` (أَرْضِ), `س م و` (سَمَٰوَٰتٍ), `س ب ع` (سَبْعَ), `م ث ل` (مِثْلَ).
- Synthesis: The cosmos is not represented as an undifferentiated expanse. Upper, lower, interval, correspondence, rank, and descent form a relational architecture. The descending command belongs to this ordered placement rather than appearing as an interruption from outside it.

#### Subchannel B. Creation by Measure and Comprehensive Knowledge
- Reading type: mixed
- Scene or process: An object is conceived in measure, brought into existence, given form, and surrounded by complete knowledge and power.
- Active motifs: measuring and proportioning before making (`quranic:root_000434:B001/m01`); originating created existence (`quranic:root_000434:B002/m01`); completed form and balanced shape (`quranic:root_000434:B003/m01`); making or originating an object (`quranic:root_000248:B001/m01`); bringing a new event into being (`quranic:root_000299:B001/m01`); occurrence in time (`quranic:root_001332:B001/m01`); existence after nonexistence (`quranic:root_001626:B002/m01`); a determinate quantity and limit (`quranic:root_001205:B001/m01`); effective power (`quranic:root_001205:B003/m01`); deliberative ordering and calculation (`quranic:root_001205:B005/m01`); knowledge that reaches a thing from all sides (`quranic:root_000372:B004/m01`); direct knowledge (`quranic:root_001040:B001/m01`); an entity that can be known and reported (`quranic:root_000831:B001/m01`); totality gathering every part (`quranic:root_001315:B003/m01`).
- Ayah anchors: 65:1 `ح د ث` (يُحْدِثُ); 65:2/6/9 `ك و ن` (كَانَ/كُ); 65:2-4/7 `ج ع ل` (يَجْعَل/جَعَلَ); 65:3/12 `ش ي ء` (شَىْءٍ), `ق د ر` (قَدْرًا/قَدِيرٌ), `ك ل ل` (كُلِّ); 65:6 `و ج د` (وُجْدِ); 65:12 `خ ل ق` (خَلَقَ), `ح و ط` (أَحَاطَ), `ع ل م` (تَعْلَمُ/عِلْمًا).
- Synthesis: Measure is both prior design and continuing limit. Creation moves from proportion to existence to formed shape, while encompassing knowledge prevents any part from becoming unaccounted for. This cosmic scale reinforces the surah's smaller insistence that terms, resources, and obligations also be measured.

#### Subchannel C. Descent as Weather and Circulating Provision
- Reading type: mixed
- Scene or process: Cloud gathers, rain descends, the sky clears, water flows through channels, and light opens the world to life.
- Active motifs: rain or other things descending from above (`quranic:root_001492:B001/m01`); sending provision downward (`quranic:root_001492:B002/m01`); rain named as sustenance (`quranic:root_000560:B003/m01`); heavy rain (`quranic:root_001619:B001/m01`); a dark cloud bearing a load of water (`quranic:root_000357:B010/m01`); layered rain-cloud (`quranic:root_000532:B008/m01`); sky, cloud, and rain overhead (`quranic:root_000745:B004/m01`); cloud emerging and sky clearing (`quranic:root_000400:B005/m01`); continuous flow (`quranic:root_000240:B001/m01`); river cutting a channel (`quranic:root_001559:B001/m01`); illumination (`quranic:root_001564:B001/m01`); dawn opening and spreading like breath (`quranic:root_001533:B009/m01`).
- Ayah anchors: 65:1/2/11 `خ ر ج` (تُخْرِجُ/يَخْرُجْ/مَخْرَجًا/يُخْرِجَ); 65:3/7/11 `ر ز ق` (يَرْزُقْ/رِزْقُ/رِزْقًا); 65:4/6 `ح م ل` (أَحْمَالِ/حَمْلٍ/حَمْلَ); 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:8 `ر ب ب` (رَبِّ); 65:9 `و ب ل` (وَبَالَ); 65:11 `ج ر ي` (تَجْرِى), `ن ه ر` (أَنْهَٰرُ), `ن و ر` (نُّورِ); 65:12 `س م و` (سَمَٰوَٰتٍ); `ن ف س` is anchored at 65:1/7 (نَفْسَ/نَفْسًا).
- Synthesis: Descending order is materially productive: a cloud carries its water-load, rain releases it, the sky clears, and channels continue the flow into river and light-opened life below. The scene links command, burden, and provision through a shared pattern of ordered descent and discharge.

#### Subchannel D. Enduring Garden beneath Flowing Rivers
- Reading type: surface-primary
- Scene or process: A sheltered garden receives continuous water below it and becomes a permanent, well-provisioned abode.
- Active motifs: a garden enclosed by its trees (`quranic:root_000266:B003/m01`); water in continuous motion (`quranic:root_000240:B001/m01`); the region beneath (`quranic:root_000177:B001/m01`); a river-channel (`quranic:root_001559:B001/m01`); stable, enduring permanence (`quranic:root_000429:B001/m01`); unbounded duration (`quranic:root_000004:B001/m01`); nourishment reaching the body (`quranic:root_000560:B002/m01`); beneficent action and increase beyond strict equivalence (`quranic:root_000323:B002/m01`); illuminating light (`quranic:root_001564:B001/m01`); provision prepared for the arriving guest (`quranic:root_001492:B005/m01`).
- Ayah anchors: 65:5/10/12 `ن ز ل` (أَنزَلَ/يَتَنَزَّلُ); 65:11 `ج ن ن` (جَنَّٰتٍ), `ج ر ي` (تَجْرِى), `ت ح ت` (تَحْتِ), `ن ه ر` (أَنْهَٰرُ), `خ ل د` (خَٰلِدِينَ), `ء ب د` (أَبَدًا), `ح س ن` (أَحْسَنَ), `ر ز ق` (رِزْقًا), `ن و ر` (نُّورِ).
- Synthesis: The final garden gathers the report's recurrent mechanisms into one scene: enclosure without confinement, residence without eviction, water without exhaustion, provision without withholding, and duration without an abruptly broken term. Its permanence is thus the resolved form of the surah's temporary houses, measured transitions, and vulnerable flows.


