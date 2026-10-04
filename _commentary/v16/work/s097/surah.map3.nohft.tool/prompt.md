Surah: 97. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S97 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), an earlier reader's channel review (channels.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not use tools, delegate, browse or inspect files.

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

===== _commentary/v16/work/s097/surah.r2/text.md =====
# Surah 97

- 97:1 إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ
- 97:2 وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ
- 97:3 لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ
- 97:4 تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ
- 97:5 سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ


===== _commentary/v16/work/s097/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ز ل (root_001492): 97:1 أَنزَلْنَٰهُ, 97:4 تَنَزَّلُ

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

## ل ي ل (root_001392): 97:1 لَيْلَةِ, 97:2 لَيْلَةُ, 97:3 لَيْلَةُ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ق د ر (root_001205): 97:1 ٱلْقَدْرِ, 97:2 ٱلْقَدْرِ, 97:3 ٱلْقَدْرِ

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

## د ر ي (root_000473): 97:2 أَدْرَىٰكَ

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

## ECHO د ر ر (root_000469): for 97:2 أَدْرَىٰكَ: withheld observed target; not identity

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

## خ ي ر (root_000452): 97:3 خَيْرٌ

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

## ء ل ف (root_000045): 97:3 أَلْفِ

- **B001** bin sayısı ve bine tamamlama — bilinen bin sayısı; çoğulu binler · bir topluluğu bin kişiye tamamlamak veya onların bin kişi olması · para miktarını bin değerine ulaştırmak
  الألف معروف والجمع الآلاف (maqayis)؛ الألف عدد والجمع ألوف وآلاف (sihah)؛ والألف من العدد معروف (tahdhib)؛ الألف العدد المخصوص (mufradat)؛ آلفت القوم صيرتهم ألفا (maqayis;sihah)؛ آلفت الدراهم أي بلغت بها الألف (mufradat)
- **B002** birleştirip düzenlemek — bir şeyin parçalarını birbirine katmak veya bağlamak · iki şeyin arasını birleştirmek veya ayrılıktan sonra toplamak · farklı parçalardan düzenlenmiş bütün
  انضمام الشيء إلى الشيء (maqayis)؛ كل شيء ضممت بعضه إلى بعض فقد ألفته تأليفا (maqayis)؛ ألفت بين الشيئين تأليفا (sihah)؛ ألفت بينهم تأليفا إذا جمعت بينهم بعد تفرق (tahdhib)؛ ألفت الشيء وصلت بعضه ببعض ومنه تأليف الكتب (tahdhib)؛ اجتماع مع التئام (mufradat)؛ المؤلف ما جمع من أجزاء مختلفة ورتب ترتيبا (mufradat)
- **B003** gönlünü kazanmak — gönülleri yakınlık ve destekle kazanılmaya çalışılan kimseler · birini yakınlık, ilgi veya destekle kazanmak
  تألفته على الإسلام ومنه المؤلفة قلوبهم (sihah)؛ والمؤلفة قلوبهم هؤلاء قوم من سادة العرب أمر الله نبيه بتألفهم أي بمقاربتهم وإعطائهم من الصدقات (tahdhib)؛ والمؤلفة قلوبهم هم الذين يتحرى فيهم بتفقدهم (mufradat)
- **B004** mevsimlik yolculuk düzeni — belirli topluluğun kış ve yaz yolculuklarını bağlama, hazırlama veya güvenceye alma ifadesi
  لإيلاف قريش (maqayis;mufradat)؛ لتؤلف قريش رحلة الشتاء والصيف أي تجمع بينهما (sihah)؛ لتؤلف قريش الرحلتين فيتصلا ولا ينقطعا (tahdhib)؛ يؤلفون يهيئون ويجهزون (tahdhib)؛ يؤلفون يجيرون (tahdhib)؛ لهم إلف وليس لكم إيلاف (tahdhib)
- **B005** ünsiyet ve alışma — alışılan, tanıdık ve ünsiyet duyulan kişi veya şey · bir yere alışmak, orada kalmayı sürdürmek · bir kimseyle ünsiyet kurmak · bir eve veya yere alışmış kuşlar
  ألفت الشيء آلفه والألفة مصدر الائتلاف (maqayis)؛ إلفك وأليفك الذي تألفه (maqayis)؛ آلفت المكان والقوم (maqayis)؛ أوالف الطير التي بمكة (maqayis)؛ فلان قد ألف هذا الموضع يألفه إلفا (sihah)؛ ألفت الشيء وآلفته بمعنى واحد أي لزمته (tahdhib)؛ ألفت فلانا إذا أنست به (tahdhib)؛ أوالف الحمام دواجنها التي تألف البيوت (tahdhib)؛ يقال للمألوف إلف وأليف (mufradat)؛ أوالف الطير ما ألفت الدار (mufradat)
- **B006** alfabe işareti adı — alfabedeki belirli yazı ve ses işaretinin adı ve teknik türleri
  الألف من حروف التهجي (mufradat)؛ أصول الألفات ثلاثة (tahdhib)؛ الألف الفاصلة (tahdhib)؛ ألف العبارة (tahdhib)؛ الألف اللينة (tahdhib)؛ هذه ألف مؤلفة (tahdhib)

## ش ه ر (root_000823): 97:3 شَهْرٍ

- **B001** ayın ilk görünümüne göre belirlenen otuz günlük süre — ay; ayın ilk görünümüyle belirlenen yaklaşık otuz günlük süre · aylar; birden çok ayın sayısı veya süresi · aylar topluluğu · ay ay yapılan işlem veya aylık anlaşma · bir yerde bir ay kalmak · üzerinden bir ay geçmek veya yeni aya girmek · güz dönemi ile kış arasındaki ay
  الشهر الهلال ثم سمي كل ثلاثين يوما باسم الهلال (maqayis); الشهر والأشهر عدد والشهور جماعة (ayn;tahdhib); الشهر واحد الشهور (sihah); مدة مشهورة بإهلال الهلال (mufradat); المشاهرة المعاملة شهرا بشهر (ayn;tahdhib); أشهرنا بالمكان إذا أقمنا به شهرا (maqayis;sihah;mufradat); دخلنا في الشهر (sihah)
- **B002** insanlar arasında belirginleşip yaygın biçimde bilinme — herkesçe bilinme, tanınmışlık; kötü bağlamda dillere düşme · adı duyulmak, insanlar arasında tanınır hâle gelmek · tanınmış, herkesçe bilinen
  الشهرة وضوح الأمر (maqayis;sihah); ظهور الشيء في شنعة حتى يشهره الناس (ayn;tahdhib); شهر فلان واشتهر يقال في الخير والشر (mufradat); الشهرة الفضيحة (tahdhib); مشهور ومشهر (ayn;tahdhib)
- **B003** kılıcı kınından çekip görünür hâle getirme [kalıp] — kılıcını kınından çekip görünür hâle getirmek · silahı üzerlerine çekip kaldırmak
  شهر سيفه إذا انتضاه (maqayis); شهر سيفه إذا انتضاه فرفعه على الناس (ayn;tahdhib); شهر سفيه أي سله (sihah); شهر علينا السلاح (ayn;tahdhib)

## م ل ك (root_001444): 97:4 ٱلْمَلَٰٓئِكَةُ

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

## ر و ح (root_000609): 97:4 وَٱلرُّوحُ

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

## ء ذ ن (root_000022): 97:4 بِإِذْنِ

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

## ر ب ب (root_000532): 97:4 رَبِّهِم

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

## ECHO ر ب و (root_000537): for 97:4 رَبِّهِم: withheld observed target; not identity

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

## ك ل ل (root_001315): 97:4 كُلِّ

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

## ء م ر (root_000051): 97:4 أَمْرٍ

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

## س ل م (root_000737): 97:5 سَلَٰمٌ

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

## ط ل ع (root_000945): 97:5 مَطْلَعِ

- **B001** güneşin, ayın, yıldızın veya tanın doğması; doğuş olayı ve yeri [kalıp] — güneşin, tanın, yıldızın ya da ayın doğması · güneşin doğduğu yer veya yön · tanın sökmesi; tan vakti ya da tanın belirdiği yer
  المطلع الموضع الذي تطلع عليه الشمس؛ والمطلع مصدر من طلع (ayn)؛ طلعت الشمس والكوكب طلوعا ومطلعا؛ والمطلع موضع طلوعها (sihah)؛ طلعت الشمس؛ وكذلك طلع الفجر والنجم والقمر؛ المطلع بالفتح هو الطلوع والمطلع بالكسر هو الموضع (tahdhib)؛ طلع الشمس طلوعا ومطلعا؛ والمطلع موضع الطلوع (mufradat)؛ أصل واحد صحيح يدل على ظهور وبروز؛ طلعت الشمس طلوعا ومطلعا؛ والمطلع موضع طلوعها (maqayis)
- **B002** bir topluluğun karşısına çıkmak; ayrı kuruluşta onlardan gözden kaybolmak [kalıp] — topluluğun karşısına çıkmak, yanına gelmek ya da baskın verircesine belirmek; sınırlı bir aktarımda gözden kaybolmak · onların yanından ayrılıp gözden kaybolmak
  طلع علينا فلان يطلع طلوعا إذا هجم (ayn)؛ طلعت على القوم إذا أتيتهم؛ طلعت عنهم إذا غبت عنهم (sihah)؛ يقال طلع فلان علينا من بعيد؛ طلعت على صاحبي إذا أقبلت عليه؛ طلعت على القوم إذا غبت عنهم حتى لا يروك (tahdhib)؛ وعنه استعير طلع علينا فلان واطلع؛ وطلعت عنه غبت (mufradat)؛ طلع علينا فلان إذا هجم (maqayis)
- **B003** bir şeyi öğrenmek ya da başkasına gösterip bildirmek; görüşünü yoklamak [kalıp] — bir şeye yukarıdan bakmak veya iç yüzünü bütünüyle öğrenmek · başkasına bir işi ya da saklı sözü gösterip bildirmek · başını dışarı çıkarıp görünür kılmak · birinin görüşünü öğrenmek için ne düşündüğünü araştırmak · bir şeyi inceleyip içinde ne bulunduğunu öğrenmek
  أطلع فلان رأسه أظهره؛ اطلع أشرف على الشيء؛ أطلع غيره إطلاعا؛ أطلعني طلع هذا الأمر حتى علمته كله؛ استطلعت رأيه (ayn)؛ اطلعت على باطن أمره؛ طالعت الشيء أي اطلعت عليه؛ أطلعتك على سري؛ استطلعت رأي فلان (sihah)؛ اطلع فلان إذا أشرف على شيء؛ أطلع غيره؛ استطلعت رأي فلان إذا نظرت ما رأيه؛ أطلعني فلان (tahdhib)؛ اطلع؛ أطلع الغيب؛ أطلعتك على كذا؛ واستطلعت رأيه (mufradat)؛ أطلعتك على الأمر إطلاعا؛ أطلعتك طلعه؛ استطلعت رأي فلان إذا نظرت ما الذي يبرز إليك منه (maqayis)
- **B004** düşmanı gözlemek için önden gönderilen gözcü veya gözcü birliği — düşmanı gözlemek için önden gönderilen gözcü kişi veya birlik · önden gönderilen gözcü toplulukları
  الطليعة قوم يبعثون ليطلعوا طلع العدو؛ الطلائع الجماعات في السرية (ayn)؛ طليعة الجيش من يبعث ليطلع طلع العدو (sihah)؛ طليعة القوم الذين يبعثون ليطلعوا طلع العدو (tahdhib)؛ وطليعة الجيش أول من يطلع (mufradat)؛ وطليعة الجيش من يطلع طلع العدو (maqayis)
- **B005** palmiye ağacının kapalı çiçek salkımı; salkımın veya ekinin belirmesi — palmiye ağacının henüz açılmamış çiçek salkımı · kılıf içindeki tek bir palmiye çiçek salkımı · palmiye ağacının çiçek salkımını çıkarması · ekinin belirip görünmesi
  الطلع طلع النخلة الواحدة طلعة؛ وأطلعت النخلة؛ وطلع الزرع بدا (ayn)؛ والطلع طلع النخلة؛ واطلع النخل إذا خرج طلعه (sihah)؛ طلع الزرع إذا بدا؛ وأطلعت النخلة إذا أخرجت طلعها؛ الطلع كفراها قبل أن تنشق (tahdhib)؛ تشبيها بالطلوع قيل طلع النخل؛ لها طلع نضيد؛ وقد أطلعت النخل (mufradat)؛ والطلع طلع النخلة؛ وقد أطلعت النخلة (maqayis)
- **B006** dağa çıkma ve çıkış yolu; bir işin yaklaşım yönü veya ürkütücü eşiği [kalıp] — dağa tırmanıp çıkmak · dağa çıkılan yol veya dağa erişilen yön · bir işin ele alınacağı yön veya giriş yolu · yüksekten bakınca önünde açılan ağır durumun ürkütücülüğü
  طلعت الجبل أي علوته؛ المطلع المأتى؛ موضع الإطلاع من إشراف إلى انحدار (sihah)؛ طلعت الجبل إذا علوته؛ المطلع موضع الاطلاع من إشراف إلى الانحدار؛ وقد يكون المطلع المصعد؛ مطلع هذا الجبل مصعده ومأتاه؛ ما لهذا الأمر مطلع أي وجه ولا مأتى (tahdhib)؛ والمطلع المأتى؛ أين مطلع هذا الأمر أي مأتاه؛ هول المطلع (maqayis)
- **B007** bir alanı sınırına kadar doldurma; ayrı aktarımda güneşin gördüğü yeryüzü [kalıp] — yeryüzünü dolduracak çokluk; başka bir aktarımda güneşin gördüğü yeryüzü · avucu dolduran şey; özellikle gövdesi avucu dolduran yay · ağzına kadar dolu kap veya su gözü · ölçü kabını taşacak kadar doldurmak
  الطلاع ما طلعت عليه الشمس؛ وطلاع الأرض ملء الأرض؛ وقوس طلاع إذا كان عجسها يملأ الكف (ayn)؛ طلاع الشيء ملؤه؛ طلاع الأرض ملؤها؛ قوس طلاع الكف (sihah)؛ طلاع الأرض ملؤها حتى يطالع أعلى الأرض؛ طلاع الأرض ما طلعت عليه الشمس؛ قدح طلاع ممتلىء؛ عين طلاعة ممتلئة (tahdhib)؛ الطلاع ما طلعت عليه الشمس والإنسان؛ وقوس طلاع الكف ملء الكف (mufradat)؛ الطلاع ما طلعت عليه الشمس من الأرض؛ قوس طلاع الكف إذا كان عجسها يملأ الكف (maqayis)
- **B008** bir şeye istekle yönelme; bir görünüp bakıp bir gizlenme [kalıp] — bir şeye sürekli ve güçlü biçimde yönelen iç istek · bir görünüp bakıp bir geri çekilerek gizlenen kadın
  إن نفسك لطلعة إلى هذا الأمر؛ أي تتطلع إليه؛ وامرأة طلعة قبعة تنظر ساعة وتتنحى أخرى (ayn)؛ وتطلعت إلى ورود كتابك؛ ونفس طلعة؛ وامرأة طلعة (sihah)؛ نفسك لطلعة إلى هذا الأمر؛ وإنها لتطلع إليه أي لتنازع إليه؛ وامرأة طلعة قبعة تنظر ساعة ثم تختبىء ساعة (tahdhib)؛ امرأة طلعة قبعة تظهر رأسها مرة وتستر أخرى (mufradat)؛ ونفس طلعة تتطلع للشيء؛ وامرأة طلعة إذا كانت تكثر الإطلاع (maqayis)
- **B009** bir insanın görülüşü ve göz önündeki görünüşü — bir insanın yüzü, genel görünüşü veya görülüşü
  والطلعة الرؤية؛ ما أحسن طلعته أي رؤيته؛ حيا الله طلعتك (ayn)؛ والطلعة الرؤية (sihah)؛ طلعته رؤيته؛ يقال حيا الله طلعتك (tahdhib)؛ وطلعة الإنسان رؤيته لأنها تطلع (maqayis)
- **B010** okun nişan alınan yerin üstünden geçip arkasına düşmesi [kalıp] — yükselip nişan alınan yerin üstünden geçerek arkasına düşen ok · attığı ok nişan alınan yerin üstünden geçmek
  وأطلع الرامي أي جاز سهمه من فوق الغرض (sihah)؛ والطالع من السهام الذي يقع وراء الهدف؛ يسجد للطالع؛ شخص سهمه فارتفع عن الرمية (tahdhib)؛ ورمى فلان فأطلع وأشخص إذا مر سهمه برأس الغرض (maqayis)
- **B011** kusmak ve kusmuk — kusmak · kusmuk
  وأطلع أي قاء؛ والطلعاء القيء (sihah)؛ أطلع الرجل إطلاعا إذا قاء؛ الطولع الطلعاء وهو القيء (tahdhib)؛ ومن الباب الطلعاء القيء؛ يقال أطلع إذا قاء (maqayis)
- **B012** çevresindeki palmiye ağaçlarını boyca aşma; uzun boylu erkek — yanındaki palmiye ağaçlarından daha uzun olan palmiye · uzun boylu adam
  نخلة مطلعة إذا طالت النخيل (sihah)؛ نخلة مطلعة إذا طالت النخلة التي بحذائها فكانت أطول منها (tahdhib)؛ الهطلع الرجل الطويل زيدت فيه الهاء من طلع (maqayis)

## ف ج ر (root_001132): 97:5 ٱلْفَجْرِ

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



===== _commentary/v16/work/s097/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s097/reader_a_pilot.md)

# s097 Semantic Channel Discovery

## Parent Channels

### 1. Determination, Arrangement, and Authorized Action
- Semantic invariant: An affair becomes actionable by being assessed, fitted, assembled, and then carried out under permission and command.
- Surface relation: direct; الْقَدْرِ (97:1-3), أَنزَلْنَاهُ (97:1), and تَنَزَّلُ، إِذْنِ، رَبِّهِم، أَمْرٍ (97:4) enact measured sending under authority.
- Surprising reach: The same ordering pattern extends to composition, beneficial selection, nurture, and estate stewardship.

#### Subchannel A. Deliberating and Fitting an Affair
- Reading type: mixed
- Scene or process: A matter is considered, its parts assembled around a mainstay, and each part put in its suitable place.
- Active motifs: measured deliberation (ق د ر:B005/m01); fitting and preparation (ق د ر:B005/m02); affair or circumstance (ء م ر:B001/m01); consultation (ء م ر:B007/m01); assembly after separation (ء ل ف:B002/m01); proper placement (ن ز ل:B004/m01); governing mainstay (م ل ك:B005/m01)
- Ayah anchors: الْقَدْرِ (97:1-3); أَلْفِ (97:3); أَمْرٍ، الْمَلَائِكَةُ (97:4); أَنزَلْنَاهُ (97:1) and تَنَزَّلُ (97:4)
- Synthesis: Deliberation supplies the measure, consultation tests it, assembly joins the components, and the mainstay holds the resulting arrangement together. Ordered placement completes the process by assigning each component its appropriate station.

#### Subchannel B. Permissioned Command and Complete Dispatch
- Reading type: surface-primary
- Scene or process: A sovereign command grants leave and sends an ordered charge downward in its entirety.
- Active motifs: permission to act (ء ذ ن:B004/m01); binding command (ء م ر:B002/m01); lordship (ر ب ب:B001/m01); sovereignty (م ل ك:B003/m01); complete inclusion (ك ل ل:B003/m01); sending and delivery (ن ز ل:B002/m01); recurring angelic descent (ن ز ل:B002/m03)
- Ayah anchors: إِذْنِ، أَمْرٍ، رَبِّهِم، الْمَلَائِكَةُ، كُلِّ، تَنَزَّلُ (97:4); أَنزَلْنَاهُ (97:1)
- Synthesis: Authority originates the command, permission opens the route for action, and descent delivers the charge. The language of totality makes the dispatch comprehensive rather than fragmentary.

#### Subchannel C. Selecting the Beneficial Course
- Reading type: mixed
- Scene or process: Deliberation compares alternatives and chooses the course marked by benefit and excellence.
- Active motifs: evaluative planning (ق د ر:B005/m01); choosing the better option (خ ي ر:B003/m01); beneficial good (خ ي ر:B001/m01); selected excellence (خ ي ر:B002/m01)
- Ayah anchors: الْقَدْرِ (97:1-3); خَيْرٌ (97:3)
- Synthesis: Measure is not only quantitative: it becomes a decision procedure. Reflection distinguishes alternatives, while خير supplies both the criterion of benefit and the outcome of selection.

#### Subchannel D. Stewardship and Collateral Inheritance
- Reading type: latent/lexical
- Scene or process: A caretaker orders property and responsibility for a household whose succession runs through collateral kin.
- Active motifs: gradual nurture and completion (ر ب ب:B002/m01); collateral kinship and inheritance (ك ل ل:B004/m01); property under disposition (م ل ك:B002/m01); planned apportionment (ق د ر:B005/m02)
- Ayah anchors: رَبِّهِم، كُلِّ، الْمَلَائِكَةُ (97:4); الْقَدْرِ (97:1-3)
- Synthesis: Nurture establishes custodial responsibility, ownership supplies the estate, and collateral kinship defines the succession problem. Measured preparation turns those relations into an apportioned household order.

### 2. Knowledge, Hearing, and Disclosure
- Semantic invariant: Hidden or unknown content becomes available through learning, attentive reception, authorization, inspection, or public announcement.
- Surface relation: direct; أَدْرَىٰكَ (97:2) poses knowledge as access, while إِذْنِ and أَمْرٍ (97:4) connect reception to authorized action.
- Surprising reach: Disclosure ranges from scholarship and proclamation to bodily peeking, visible aspect, and reconnaissance.

#### Subchannel A. Learning and Public Proclamation
- Reading type: mixed
- Scene or process: Knowledge is acquired, taught, and converted into a call that reaches a public audience.
- Active motifs: knowing and teaching (د ر ي:B001/m01); acquired knowledge (ء ذ ن:B003/m01); proclamation by a call (ء ذ ن:B003/m02); learned sage (ر ب ب:B003/m01); public visibility (ش ه ر:B002/m01)
- Ayah anchors: أَدْرَىٰكَ (97:2); إِذْنِ، رَبِّهِم (97:4); شَهْرٍ (97:3)
- Synthesis: Private cognition becomes communicable knowledge through the learned figure, then crosses into public space through proclamation. شهرة supplies the final state in which what was known is now manifest among people.

#### Subchannel B. Listening, Leave, and Compliance
- Reading type: mixed
- Scene or process: A hearer attends to a command, receives leave, and either complies intelligently or follows without independent judgment.
- Active motifs: attentive listening and acceptance (ء ذ ن:B002/m01); granted permission (ء ذ ن:B004/m01); obligatory command (ء م ر:B002/m01); compliant dependent follower (ء م ر:B008/m01)
- Ayah anchors: إِذْنِ، أَمْرٍ (97:4)
- Synthesis: The ear-to-action sequence moves from reception to authorization and then obedience. The follower motif introduces a role reversal within the same frame: compliance can express disciplined acceptance or the absence of independent counsel.

#### Subchannel C. Inspection, Appearance, and Visible Aspect
- Reading type: latent/lexical
- Scene or process: An observer seeks access to a concealed condition until a person, view, or fact comes into sight.
- Active motifs: inspecting an inner matter (ط ل ع:B003/m01); appearing before a group (ط ل ع:B002/m01); repeated peeking and visual desire (ط ل ع:B008/m01); visible aspect or visage (ط ل ع:B009/m01); public emergence (ش ه ر:B002/m01)
- Ayah anchors: مَطْلَعِ (97:5); شَهْرٍ (97:3)
- Synthesis: Looking begins as an effort to uncover what is hidden, becomes repeated visual approach, and resolves in a visible aspect. Publicity scales that local act of seeing into collective recognition.

### 3. Number, Duration, and Proportion
- Semantic invariant: Measure bounds phenomena as count, temporal span, fitted form, or restricted capacity.
- Surface relation: direct; الْقَدْرِ (97:1-3) and أَلْفِ شَهْرٍ (97:3) explicitly couple valuation with numerical and calendrical scale.
- Surprising reach: Numerical measure extends into crowds, bodily build, property limits, need, and burden.

#### Subchannel A. Thousand, Multitude, and Totality
- Reading type: surface-primary
- Scene or process: A counted thousand expands into assembled multitudes and an encompassing whole.
- Active motifs: the number one thousand (ء ل ف:B001/m01); calendrical month (ش ه ر:B001/m01); bounded quantity (ق د ر:B001/m01); gathered multitudes (ر ب ب:B004/m01); collective groups (ك ل ل:B009/m01); encompassing totality (ك ل ل:B003/m01)
- Ayah anchors: أَلْفِ، شَهْرٍ (97:3); الْقَدْرِ (97:1-3); رَبِّهِم، كُلِّ (97:4)
- Synthesis: ألف supplies exact count, شهر turns it into duration, and قدر frames the comparison as bounded magnitude. The group and totality motifs show the same arithmetic logic at collective scale.

#### Subchannel B. Appointed Span and Single Occurrence
- Reading type: mixed
- Scene or process: A marked interval is bounded by an appointed limit and can be counted as one occurrence within a larger cycle.
- Active motifs: appointed limit or term (ق د ر:B001/m02); sign and fixed time (ء م ر:B005/m01); the nearest or current night (ل ي ل:B003/m01); one instance of descent (ن ز ل:B010/m01); calendar calculation (ق د ر:B005/m03)
- Ayah anchors: الْقَدْرِ، لَيْلَةِ/لَيْلَةُ (97:1-3); أَمْرٍ، تَنَزَّلُ (97:4)
- Synthesis: A term establishes the boundary, a sign identifies it, and deixis locates the relevant night. The single-descent motif makes an event countable inside the calculated span.

#### Subchannel C. Fitted Stature and Bodily Proportion
- Reading type: latent/lexical
- Scene or process: A body is read through balanced fit, width, height, chest, and articulated extremities.
- Active motifs: proportionate fit (ق د ر:B006/m01); medium stature (ق د ر:B006/m02); bodily spread or width (ر و ح:B009/m01); compact stout build (ك ل ل:B008/m01); projecting height (ط ل ع:B012/m01); chest (ك ل ل:B007/m01); finger and foot joints (س ل م:B010/m01)
- Ayah anchors: الْقَدْرِ (97:1-3); الرُّوحُ، كُلِّ (97:4); مَطْلَعِ، سَلَامٌ (97:5)
- Synthesis: Proportion acts as the invariant across otherwise contrasting forms: medium, broad, compact, tall, axial, and jointed. Each motif locates fit in a different bodily dimension.

#### Subchannel D. Narrowed Resources and Constrained Capacity
- Reading type: latent/lexical
- Scene or process: Property and agency contract under scarcity, producing need, burden, and an obligation that must be restored.
- Active motifs: constricted provision (ق د ر:B004/m01); property under control (م ل ك:B002/m01); pressing need (ر ب ب:B016/m01); tight knot (ر ب ب:B016/m02); dependent burden (ك ل ل:B002/m01); restitution of a due right (ر و ح:B006/m01)
- Ayah anchors: الْقَدْرِ (97:1-3); الْمَلَائِكَةُ، رَبِّهِم، كُلِّ، الرُّوحُ (97:4)
- Synthesis: Constriction reduces available property and turns dependency into weight. Need tightens the relation further, while restitution names the action that releases the obligation.

### 4. Night, Darkness, and Dawn
- Semantic invariant: A bounded dark interval contains nocturnal activity, holds a state of peace, and ends through rupture and rising light.
- Surface relation: direct; لَيْلَةِ الْقَدْرِ (97:1-3) is the governing interval, and سَلَامٌ هِيَ حَتَّىٰ مَطْلَعِ الْفَجْرِ (97:5) gives its state and endpoint.
- Surprising reach: Darkness also takes the form of an enclosing canopy or cloud-crown lit from within.

#### Subchannel A. Dark Interval and Nocturnal Practice
- Reading type: surface-primary
- Scene or process: Night establishes the setting for actions, journeys, and evening return.
- Active motifs: night and its darkness (ل ي ل:B001/m01); acting or traveling by night (ل ي ل:B002/m01); the present night (ل ي ل:B003/m01); evening movement and return (ر و ح:B005/m01)
- Ayah anchors: لَيْلَةِ/لَيْلَةُ (97:1-3); الرُّوحُ (97:4)
- Synthesis: The night is both a temporal container and a mode of action. Nocturnal practice fills that interval, while evening return gives it directional rhythm.

#### Subchannel B. Dawn as Rupture and Rising Light
- Reading type: surface-primary
- Scene or process: Darkness is split open and light rises from the breach.
- Active motifs: dawn light (ف ج ر:B002/m01); broad splitting and release (ف ج ر:B001/m01); rising luminary and point of emergence (ط ل ع:B001/m01); night darkness (ل ي ل:B001/m01)
- Ayah anchors: الْفَجْرِ، مَطْلَعِ (97:5); لَيْلَةِ/لَيْلَةُ (97:1-3)
- Synthesis: Fajr supplies both the concrete dawn and the mechanics of opening; طلوع supplies upward appearance. Together they make dawn a transition generated by rupture rather than a mere timestamp.

#### Subchannel C. Peace Extending to the Dawn Boundary
- Reading type: surface-primary
- Scene or process: Safety and reconciliation fill the night until the marked point of dawn.
- Active motifs: freedom from harm (س ل م:B001/m01); peace opposed to conflict (س ل م:B004/m01); night interval (ل ي ل:B001/m01); dawn endpoint (ف ج ر:B002/m01); rising boundary (ط ل ع:B001/m01)
- Ayah anchors: سَلَامٌ، مَطْلَعِ، الْفَجْرِ (97:5); لَيْلَةِ/لَيْلَةُ (97:1-3)
- Synthesis: سلام defines the condition maintained inside the night, while مطلع الفجر supplies its terminal boundary. The reconciliation sense enlarges personal safety into a social suspension of conflict.

#### Subchannel D. Enclosing Cloud, Canopy, and Flash
- Reading type: latent/lexical
- Scene or process: Layered cloud closes around the dark sky like a crown or canopy, then flashes from within.
- Active motifs: encircling cloud-crown (ك ل ل:B005/m02); layered rain cloud (ر ب ب:B008/m01); protective canopy (ك ل ل:B006/m01); cloud flashing like exposed teeth (ك ل ل:B011/m02); night darkness (ل ي ل:B001/m01)
- Ayah anchors: كُلِّ، رَبِّهِم (97:4); لَيْلَةِ/لَيْلَةُ (97:1-3)
- Synthesis: Enclosure links crown, canopy, and layered cloud into one sky architecture. The lightning motif interrupts that enclosure with a brief internal disclosure.

### 5. Descent, Position, and Reception
- Semantic invariant: Downward movement resolves into delivery, stationing, welcome, or disruptive arrival.
- Surface relation: direct; أَنزَلْنَاهُ (97:1) and تَنَزَّلُ الْمَلَائِكَةُ وَالرُّوحُ (97:4) foreground sending and repeated descent.
- Surprising reach: The descent family also organizes rank, hospitality, and sudden communal calamity.

#### Subchannel A. Sending and Repeated Descent
- Reading type: surface-primary
- Scene or process: Something is sent from above, arrives below, and may descend repeatedly rather than once.
- Active motifs: downward movement and arrival (ن ز ل:B001/m01); sending and delivery (ن ز ل:B002/m01); revelatory sending (ن ز ل:B002/m02); repeated angelic descent (ن ز ل:B002/m03); one descent-event (ن ز ل:B010/m01)
- Ayah anchors: أَنزَلْنَاهُ (97:1); تَنَزَّلُ، الْمَلَائِكَةُ، الرُّوحُ (97:4)
- Synthesis: The root alternates causative sending with self-movement downward. Revelation, angelic arrival, and the countable descent-event are distinct roles within the same vertical process.

#### Subchannel B. Station, Rank, and Proper Placement
- Reading type: mixed
- Scene or process: Arrival is completed by assigning a thing its dwelling, rank, or fitting position.
- Active motifs: dwelling or station (ن ز ل:B003/m01); rank or standing (ن ز ل:B003/m02); placement in the proper station (ن ز ل:B004/m01); bounded measure (ق د ر:B001/m01); fitting preparation (ق د ر:B005/m02)
- Ayah anchors: أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); الْقَدْرِ (97:1-3)
- Synthesis: Descent does not end at motion; it establishes position. Measure selects the appropriate station, while منزلة allows the same spatial logic to become social rank.

#### Subchannel C. Guest Arrival and Prepared Provision
- Reading type: latent/lexical
- Scene or process: A guest arrives to find food, generosity, and eager service already prepared.
- Active motifs: guest provision (ن ز ل:B005/m01); arriving guest (ن ز ل:B005/m02); cooking vessel and stew (ق د ر:B007/m01); generous gift (خ ي ر:B005/m01); gushing bounty (ف ج ر:B005/m01); eager generosity (ر و ح:B010/m01)
- Ayah anchors: أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); الْقَدْرِ (97:1-3); خَيْرٌ (97:3); الْفَجْرِ، الرُّوحُ (97:5 and 97:4)
- Synthesis: Arrival activates a reception scene: the vessel holds the meal, generosity supplies it, and eager service moves it toward the guest. The gushing image turns provision into abundance rather than bare sufficiency.

#### Subchannel D. Calamity and Sudden Mass Arrival
- Reading type: latent/lexical
- Scene or process: A large force appears suddenly and descends upon a community as a disruptive event.
- Active motifs: descending calamity (ن ز ل:B006/m01); sudden mass influx (ف ج ر:B003/m01); appearing or attacking a group (ط ل ع:B002/m02); gathered multitude (ر ب ب:B004/m01)
- Ayah anchors: أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); الْفَجْرِ، مَطْلَعِ (97:5); رَبِّهِم (97:4)
- Synthesis: The scene combines vertical arrival, abrupt multiplicity, and collective exposure. A neutral multitude becomes a calamity through the speed and force of its appearance.

### 6. Sovereignty, Capacity, and Guidance
- Semantic invariant: Control rests on the ability to hold, own, direct, and sustain people, property, structures, or journeys.
- Surface relation: direct; رَبِّهِم، الْمَلَائِكَةُ، إِذْنِ، أَمْرٍ (97:4) place agency within a hierarchy of lordship and delegated action.
- Surprising reach: Sovereign control recurs concretely as structural cohesion, route knowledge, water security, herd leadership, and nautical command.

#### Subchannel A. Lordship, Kingship, and Effective Capacity
- Reading type: mixed
- Scene or process: A ruler possesses the capacity and jurisdiction to originate and direct an affair.
- Active motifs: lordship and mastery (ر ب ب:B001/m01); kingship and sovereignty (م ل ك:B003/m01); effective ability (ق د ر:B003/m01); office of command (ء م ر:B003/m01)
- Ayah anchors: رَبِّهِم، الْمَلَائِكَةُ، أَمْرٍ (97:4); الْقَدْرِ (97:1-3)
- Synthesis: Lordship names the superior relation, kingship its public jurisdiction, capacity its operative force, and command its institutional form. The four motifs form a single authority frame rather than four isolated titles.

#### Subchannel B. Ownership, Wealth, and Disposition
- Reading type: latent/lexical
- Scene or process: An owner holds property, possesses the means to act, and may convert increase into controlled wealth.
- Active motifs: ownership and disposal (م ل ك:B002/m01); possession and means (ق د ر:B003/m02); growth of wealth or people (ء م ر:B004/m01); generous abundance (خ ي ر:B005/m01)
- Ayah anchors: الْمَلَائِكَةُ، أَمْرٍ (97:4); الْقَدْرِ (97:1-3); خَيْرٌ (97:3)
- Synthesis: Capacity becomes economic when it is attached to property and disposable means. Growth and generosity then mark two possible movements of wealth: accumulation and outward gift.

#### Subchannel C. Cohesion, Mainstay, and Solid Build
- Reading type: latent/lexical
- Scene or process: A structure or body remains upright because a mainstay binds strong material into a compact whole.
- Active motifs: cohesion and strengthening (م ل ك:B001/m01); essential mainstay (م ل ك:B005/m01); hard stone (س ل م:B007/m01); compact stout build (ك ل ل:B008/m01); effective strength (ق د ر:B003/m01)
- Ayah anchors: الْمَلَائِكَةُ، كُلِّ (97:4); سَلَامٌ (97:5); الْقَدْرِ (97:1-3)
- Synthesis: Cohesion supplies the binding action, the mainstay supplies axial stability, and stone supplies resistant material. The body-build motif transfers the same mechanics from architecture to anatomy.

#### Subchannel D. Route, Water, Leader, and Captain
- Reading type: latent/lexical
- Scene or process: A traveling group follows a leader along a viable route secured by water and higher navigation.
- Active motifs: centerline of road or valley (م ل ك:B006/m01); water that secures a journey (م ل ك:B007/m01); leading animal followed by the herd (م ل ك:B008/m01); master of sailors (ر ب ب:B017/m01); staying-place for animals (ر ب ب:B007/m02)
- Ayah anchors: الْمَلَائِكَةُ، رَبِّهِم (97:4)
- Synthesis: Guidance is materially grounded: the route must be legible, water must sustain the party, and a leader must set direction. The captain extends the same logistics from land and herd movement to navigation.

### 7. Transfer, Covenant, and Household Care
- Semantic invariant: Social relations are stabilized by controlled transfer of persons, property, obligation, or care.
- Surface relation: indirect; إِذْنِ، أَمْرٍ، رَبِّهِم، الْمَلَائِكَةُ (97:4) and سَلَامٌ (97:5) provide the lexical anchors for authorization, control, and settlement.
- Surprising reach: Handover spans capture, advance payment, covenant, inheritance, marriage, and fosterage.

#### Subchannel A. Authorized Handover and Captivity
- Reading type: latent/lexical
- Scene or process: Authority permits a person or matter to be handed over into another party's custody.
- Active motifs: handing over and relinquishing (س ل م:B012/m01); taking captive (س ل م:B013/m01); permission (ء ذ ن:B004/m01); custody and mastery over a person (م ل ك:B002/m02); binding command (ء م ر:B002/m01)
- Ayah anchors: سَلَامٌ (97:5); إِذْنِ، الْمَلَائِكَةُ، أَمْرٍ (97:4)
- Synthesis: Permission and command legitimate the transfer; تسليم describes the act, and captivity names its coercive outcome. Ownership language fixes the resulting custodial relation.

#### Subchannel B. Advance Payment and Deferred Delivery
- Reading type: latent/lexical
- Scene or process: A buyer advances value under an agreement for goods or provision to be delivered later.
- Active motifs: advance payment (س ل م:B005/m01); transferable property (م ل ك:B002/m01); prepared provision (ن ز ل:B005/m01); business conducted at night (ل ي ل:B002/m01)
- Ayah anchors: سَلَامٌ (97:5); الْمَلَائِكَةُ (97:4); أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); لَيْلَةِ/لَيْلَةُ (97:1-3)
- Synthesis: The transaction separates payment from delivery while binding both in one obligation. Nocturnal practice supplies the setting, and prepared provision supplies the deferred object.

#### Subchannel C. Covenant, Reconciliation, and Estate Succession
- Reading type: latent/lexical
- Scene or process: A binding pact settles relations and governs the passage of property through collateral kin.
- Active motifs: covenant and protected relation (ر ب ب:B011/m01); reconciliation (س ل م:B004/m01); collateral inheritance (ك ل ل:B004/m01); estate property (م ل ك:B002/m01); planned apportionment (ق د ر:B005/m02)
- Ayah anchors: رَبِّهِم، كُلِّ، الْمَلَائِكَةُ (97:4); سَلَامٌ (97:5); الْقَدْرِ (97:1-3)
- Synthesis: Covenant creates the binding social frame, reconciliation removes active conflict, and inheritance tests how that frame survives a death. Planned disposition carries the estate through the collateral relation.

#### Subchannel D. Marriage, Fosterage, and Household Nurture
- Reading type: latent/lexical
- Scene or process: A marriage contract forms a household in which a caregiver raises a child brought from an earlier union.
- Active motifs: marriage contract (م ل ك:B004/m01); foster child or stepchild (ر ب ب:B005/m01); caregiver standing over the child (ر ب ب:B005/m02); gradual nurture (ر ب ب:B002/m01)
- Ayah anchors: الْمَلَائِكَةُ، رَبِّهِم (97:4)
- Synthesis: Contract creates the household boundary, while fosterage defines a non-biological relation within it. Nurture supplies the ongoing action that makes the legal relation a lived one.

### 8. Constructed Means of Holding and Directed Movement
- Semantic invariant: An artifact organizes matter or motion by enclosing contents, providing a handle, or furnishing a staged route.
- Surface relation: indirect; الْقَدْرِ (97:1-3), إِذْنِ، الرُّوحُ (97:4), and سَلَامٌ، مَطْلَعِ (97:5) anchor the lexical transformations into vessels, handles, airflow, and ascent.
- Surprising reach: Abstract measure, permission, spirit, peace, and emergence converge in concrete implements.

#### Subchannel A. Pot, Stew, Thickener, and Herb
- Reading type: latent/lexical
- Scene or process: A cook tends a measured vessel whose contents are thickened and seasoned.
- Active motifs: cooking pot (ق د ر:B007/m01); cooked stew (ق د ر:B007/m02); cook or butcher attending the pot (ق د ر:B007/m03); thick syrup or sediment (ر ب ب:B006/m01); preserving or correcting with syrup (ر ب ب:B006/m02); basil or crop leaf (ر و ح:B012/m01)
- Ayah anchors: الْقَدْرِ (97:1-3); رَبِّهِم، الرُّوحُ (97:4)
- Synthesis: The pot supplies the bounded workspace, the cook controls transformation, the thickener changes consistency, and the herb changes flavor or fragrance. قدر's abstract boundedness becomes a literal vessel.

#### Subchannel B. Pail, Ear-Handle, and Moving Air
- Reading type: latent/lexical
- Scene or process: A handled container is lifted and worked while air moves around or through the apparatus.
- Active motifs: single-handled pail (س ل م:B011/m01); vessel ear or handle (ء ذ ن:B001/m02); wind or moving air (ر و ح:B003/m01); air-working device or vent (ر و ح:B003/m02); bounded vessel (ق د ر:B007/m01)
- Ayah anchors: سَلَامٌ (97:5); إِذْنِ، الرُّوحُ (97:4); الْقَدْرِ (97:1-3)
- Synthesis: The ear-handle is the point of human grip, the pail is the load-bearing container, and moving air supplies an environmental or mechanical force. The assembly is unified by controlled transport through an attached part.

#### Subchannel C. Ladder, Rungs, and Vantage
- Reading type: latent/lexical
- Scene or process: A constructed stair provides staged ascent to a higher point of access or observation.
- Active motifs: ladder and means of ascent (س ل م:B006/m01); upward route and overlook (ط ل ع:B006/m01); present-night setting (ل ي ل:B003/m01); ordered positioning (ن ز ل:B004/m01)
- Ayah anchors: سَلَامٌ، مَطْلَعِ (97:5); لَيْلَةِ/لَيْلَةُ (97:1-3); أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4)
- Synthesis: Ordered placement creates the rungs, the ladder converts them into a route, and the overlook is the attained function. The night setting turns the tool into a means of access through darkness.

### 9. Weather, Water, Growth, and Animal Cycles
- Semantic invariant: Air, water, vegetation, animals, and benefit circulate through recurring processes of descent, emergence, increase, and return.
- Surface relation: indirect; الرُّوحُ and تَنَزَّلُ (97:4), together with مَطْلَعِ الْفَجْرِ (97:5), provide the surface anchors for wind, descent, opening, and emergence.
- Surprising reach: The cycle extends from cloud and sprout to settlement water, tanning material, herd movement, breeding, and generosity.

#### Subchannel A. Wind, Cloud, Rain, and Sprouting
- Reading type: latent/lexical
- Scene or process: Wind gathers layered cloud, rain descends, water opens the ground, and new growth appears.
- Active motifs: wind and breeze (ر و ح:B003/m01); layered rain cloud (ر ب ب:B008/m01); descending rain (ن ز ل:B001/m02); water bursting through an opening (ف ج ر:B001/m02); plant emergence (ط ل ع:B005/m01); budding after dormancy (ر و ح:B017/m01)
- Ayah anchors: الرُّوحُ، رَبِّهِم، تَنَزَّلُ (97:4); الْفَجْرِ، مَطْلَعِ (97:5)
- Synthesis: The motifs form a causal weather sequence rather than a loose nature cluster. Air organizes cloud, descent supplies rain, fissure releases water, and طلوع and تروح name the resulting emergence.

#### Subchannel B. Water Abundance and Sustainable Settlement
- Reading type: latent/lexical
- Scene or process: Released water gathers until it can sustain travel, encampment, and continued life.
- Active motifs: abundant gathered water (ر ب ب:B013/m01); water securing a journey or camp (م ل ك:B007/m01); complete fullness (ط ل ع:B007/m01); gushing release (ف ج ر:B001/m02)
- Ayah anchors: رَبِّهِم، الْمَلَائِكَةُ (97:4); مَطْلَعِ، الْفَجْرِ (97:5)
- Synthesis: Gushing marks supply, fullness marks accumulation, and the travel-water motif marks function. Water becomes socially decisive when it allows a group to hold its position.

#### Subchannel C. Sprouts, Fragrant Leaves, and Craft Bark
- Reading type: latent/lexical
- Scene or process: Plants emerge and persist, supplying fragrance, edible or useful leaves, and bark for craft.
- Active motifs: palm spathe or young growth (ط ل ع:B005/m01); evergreen plant (ر ب ب:B012/m01); basil and crop leaf (ر و ح:B012/m01); tanning tree and bark (س ل م:B008/m01); renewed foliage (ر و ح:B017/m01)
- Ayah anchors: مَطْلَعِ، سَلَامٌ (97:5); رَبِّهِم، الرُّوحُ (97:4)
- Synthesis: Emergence and persistence define the plant cycle, while fragrance, leaf, and bark distinguish its products. The scene moves from living growth to human use without leaving the same material chain.

#### Subchannel D. Evening Return of a Guided Herd
- Reading type: latent/lexical
- Scene or process: A habituated herd follows its leader back to a station as evening enters.
- Active motifs: evening return of livestock (ر و ح:B005/m01); herd of cattle or camels (ر ب ب:B014/m01); leading animal followed by the rest (م ل ك:B008/m01); animal station or abiding place (ر ب ب:B007/m02); habituated domestic animals (ء ل ف:B005/m02); current night (ل ي ل:B003/m01)
- Ayah anchors: الرُّوحُ، رَبِّهِم، الْمَلَائِكَةُ (97:4); أَلْفِ، لَيْلَةُ (97:3)
- Synthesis: Habituation keeps the animals together, leadership gives direction, and evening return closes movement at the station. The current-night motif supplies the temporal threshold of the scene.

#### Subchannel E. Breeding, Birth, and Young Animals
- Reading type: latent/lexical
- Scene or process: Maturation leads to mating capacity, emission, birth, and the protected early life of the young.
- Active motifs: stallion maturation (ر و ح:B018/m01); recently delivered ewe (ر ب ب:B009/m01); newborn freshness (ر ب ب:B009/m02); young lamb (ء م ر:B009/m01); reproductive emission (ن ز ل:B009/m01)
- Ayah anchors: الرُّوحُ، رَبِّهِم، أَمْرٍ، تَنَزَّلُ (97:4)
- Synthesis: The active motifs occupy successive roles in one reproductive cycle: mature sire, emission, mother after birth, and young offspring. Freshness marks the state shared by birth and early life.

#### Subchannel F. Growth, Bounty, and Generous Initiative
- Reading type: latent/lexical
- Scene or process: Increase accumulates as blessing and then flows outward through energetic generosity.
- Active motifs: growth and blessing (ء م ر:B004/m01); abundant benefaction (خ ي ر:B005/m01); gushing generosity (ف ج ر:B005/m01); energetic readiness to give (ر و ح:B010/m01); blessing or favor (ر ب ب:B016/m03)
- Ayah anchors: أَمْرٍ، الرُّوحُ، رَبِّهِم (97:4); خَيْرٌ (97:3); الْفَجْرِ (97:5)
- Synthesis: Growth names accumulation, blessing its favorable state, zeal its activating force, and generosity its outward release. The gushing image connects material increase to social benefaction.

### 10. Body, Life, and Recovery
- Semantic invariant: Vital presence inhabits an articulated body whose senses, energy, and visible features move between vigor, fatigue, rest, and death.
- Surface relation: indirect; الرُّوحُ (97:4), سَلَامٌ and مَطْلَعِ (97:5), and كُلِّ (97:4) anchor the lexical extensions into life, bodily integrity, and visible form.
- Surprising reach: Cosmic and social vocabulary resolves into ears, chest, palm, joints, face, smile, illness, and recovery.

#### Subchannel A. Vital Spirit and Articulated Body
- Reading type: mixed
- Scene or process: Life animates a body organized around chest, extremities, joints, and sensory organs.
- Active motifs: life-giving spirit (ر و ح:B001/m01); chest (ك ل ل:B007/m01); palm (ر و ح:B014/m01); finger and foot joints (س ل م:B010/m01); anatomical ear (ء ذ ن:B001/m01); bodily mainstay (م ل ك:B005/m02)
- Ayah anchors: الرُّوحُ، كُلِّ، إِذْنِ، الْمَلَائِكَةُ (97:4); سَلَامٌ (97:5)
- Synthesis: Spirit supplies animation, the chest and mainstay organize the core, and palm, joints, and ear articulate action and perception. The scene turns abstract life into a structured living body.

#### Subchannel B. Fatigue, Rest, Health, and Death
- Reading type: latent/lexical
- Scene or process: Exertion dulls body and senses, rest restores them, health marks release from harm, and death becomes final release.
- Active motifs: dulled edge or faculty (ك ل ل:B001/m01); bodily fatigue (ك ل ل:B001/m02); weakened hearing or sight (ك ل ل:B001/m03); rest and recovered breath (ر و ح:B007/m01); bodily safety (س ل م:B001/m01); death as release (ر و ح:B016/m01); descending catarrhal episode (ن ز ل:B010/m02)
- Ayah anchors: كُلِّ، الرُّوحُ (97:4); سَلَامٌ (97:5); أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4)
- Synthesis: Fatigue is represented as loss of sharpness across limbs and senses. Rest reverses that loss, safety names restored integrity, and the language of release carries the sequence to death.

#### Subchannel C. Face, Grooming, and the Flash of a Smile
- Reading type: latent/lexical
- Scene or process: A face is brought into view, groomed, and animated by a smile that exposes the teeth.
- Active motifs: visible visage (ط ل ع:B009/m01); pointed grooming comb (د ر ي:B004/m02); smiling with visible teeth (ك ل ل:B011/m01); public appearance (ش ه ر:B002/m01)
- Ayah anchors: مَطْلَعِ (97:5); أَدْرَىٰكَ (97:2); كُلِّ (97:4); شَهْرٍ (97:3)
- Synthesis: Grooming prepares the visible aspect, appearance brings it before others, and the smile makes visibility active through exposed teeth. Publicity scales the face-to-face event into a recognized presence.

### 11. Pursuit, Weapons, and Conflict
- Semantic invariant: Contest unfolds through concealment, targeting, reconnaissance, weapon preparation, encounter, and either violated peace or reconciliation.
- Surface relation: indirect; أَدْرَىٰكَ (97:2), شَهْرٍ (97:3), أَمْرٍ (97:4), and سَلَامٌ، مَطْلَعِ الْفَجْرِ (97:5) carry the lexical branches that form the conflict scenes.
- Surprising reach: Knowledge becomes stalking, appearance becomes attack, and peace stands as the reversible outcome of duel and sacrilege.

#### Subchannel A. Concealed Stalking and Luring Quarry
- Reading type: latent/lexical
- Scene or process: A hunter hides behind cover, manipulates the quarry's exit, and waits for its appearance.
- Active motifs: concealed stalking (د ر ي:B003/m01); luring an animal from its burrow (خ ي ر:B006/m01); alighting into position (ن ز ل:B001/m03); quarry appearing from concealment (ط ل ع:B002/m01)
- Ayah anchors: أَدْرَىٰكَ (97:2); خَيْرٌ (97:3); أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); مَطْلَعِ (97:5)
- Synthesis: Concealment defines the hunter's role, the lure alters the quarry's path, alighting fixes the attack position, and appearance supplies the decisive opening.

#### Subchannel B. Targeted Raid and Positional Approach
- Reading type: latent/lexical
- Scene or process: A raiding party selects a target, approaches it deliberately, and establishes a position before sudden arrival.
- Active motifs: purposeful raid or targeting (د ر ي:B002/m01); attacking appearance (ط ل ع:B002/m02); ordered positioning (ن ز ل:B004/m01); measured range or extent (ق د ر:B001/m01); staying in place (ر ب ب:B007/m01)
- Ayah anchors: أَدْرَىٰكَ (97:2); مَطْلَعِ (97:5); أَنزَلْنَاهُ (97:1), تَنَزَّلُ، رَبِّهِم (97:4); الْقَدْرِ (97:1-3)
- Synthesis: Target selection and measured approach precede contact. Positioning and staying convert movement into tactical readiness, while sudden appearance completes the raid.

#### Subchannel C. Scout, Quiver, and Armed Projectile
- Reading type: latent/lexical
- Scene or process: A scout observes the opponent while weapons are drawn, fitted with points, stored, and launched.
- Active motifs: reconnaissance scout (ط ل ع:B004/m01); unsheathed weapon (ش ه ر:B003/m01); fitted spearpoint (ء م ر:B011/m01); sharpened point (د ر ي:B004/m01); quiver and gathered arrows (ر ب ب:B010/m01); arrow overshooting its mark (ط ل ع:B010/m01)
- Ayah anchors: مَطْلَعِ (97:5); شَهْرٍ (97:3); أَمْرٍ، رَبِّهِم (97:4); أَدْرَىٰكَ (97:2)
- Synthesis: Reconnaissance supplies information, unsheathing announces readiness, the point arms the shaft, and the quiver organizes projectiles. The overshooting arrow records the possible failure of measured launch.

#### Subchannel D. Duel, Violated Sanctuary, and Reconciliation
- Reading type: mixed
- Scene or process: Opponents descend into formal combat, breach a protected boundary, and remain capable of returning to peace.
- Active motifs: descending to duel (ن ز ل:B007/m01); peace and reconciliation (س ل م:B004/m01); transgressive breach (ف ج ر:B004/m01); sacrilegious battle (ف ج ر:B006/m01); beneficial alternative to harm (خ ي ر:B001/m01)
- Ayah anchors: أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4); سَلَامٌ، الْفَجْرِ (97:5); خَيْرٌ (97:3)
- Synthesis: Duel gives conflict a reciprocal encounter, while فجور marks the crossing of a moral or protected boundary. سلام reverses that trajectory through reconciliation, with خير naming the beneficial alternative.

### 12. Composition, Naming, and Lexical Framing
- Semantic invariant: Language organizes meaning through letters, grammatical particles, ordered composition, public naming, deixis, and figurative appellation.
- Surface relation: indirect; أَلْفِ (97:3), لَيْلَةِ/لَيْلَةُ (97:1-3), شَهْرٍ (97:3), and إِذْنِ (97:4) activate lexical branches that move from utterance into writing and naming.
- Surprising reach: A numerical ألف becomes a grapheme, a night becomes a woman's name and a wine epithet, and notoriety turns an event into a public name.

#### Subchannel A. Alif, Grammar, and Ordered Composition
- Reading type: latent/lexical
- Scene or process: Letters and particles are arranged into a composed whole whose parts occupy deliberate positions.
- Active motifs: alif as grapheme (ء ل ف:B006/m01); grammatical particle rubba (ر ب ب:B015/m01); textual composition (ء ل ف:B002/m02); deliberate arrangement (ق د ر:B005/m02); ordered placement (ن ز ل:B004/m01); complete assembly (ك ل ل:B003/m01)
- Ayah anchors: أَلْفِ (97:3); رَبِّهِم، كُلِّ (97:4); الْقَدْرِ (97:1-3); أَنزَلْنَاهُ (97:1), تَنَزَّلُ (97:4)
- Synthesis: The grapheme and particle provide linguistic components; composition joins them, measure orders them, and placement fixes their sequence. Totality names the finished text as a structured whole.

#### Subchannel B. Proclamation, Publicity, and Notorious Appellation
- Reading type: latent/lexical
- Scene or process: A remarkable event is announced, becomes widely visible, and acquires a public or notorious name.
- Active motifs: public call (ء ذ ن:B003/m02); fame or notoriety (ش ه ر:B002/m01); extraordinary or outrageous affair (ء م ر:B006/m01); historical naming of sacrilegious battles (ف ج ر:B006/m02)
- Ayah anchors: إِذْنِ، أَمْرٍ (97:4); شَهْرٍ (97:3); الْفَجْرِ (97:5)
- Synthesis: The call initiates circulation, publicity broadens it, and enormity gives people a reason to preserve the event by name. The named battles show notoriety becoming historical appellation.

#### Subchannel C. Present Night, Layla, and Wine Epithet
- Reading type: latent/lexical
- Scene or process: Temporal deixis becomes a proper name, which in turn becomes a figurative name for wine.
- Active motifs: nearest or present night (ل ي ل:B003/m01); Layla as a personal name (ل ي ل:B004/m01); Umm Layla as wine epithet (ل ي ل:B004/m02); wine called al-rah (ر و ح:B015/m01)
- Ayah anchors: لَيْلَةِ/لَيْلَةُ (97:1-3); الرُّوحُ (97:4)
- Synthesis: The lexical chain moves from a temporal referent to a personal name and then to a beverage epithet. The independent wine sense of روح completes the figurative naming relation.

## Standalone Subchannels

### S1. Familiarity, Staying, and Home
- Reading type: latent/lexical
- Scene or process: Repeated residence makes a place familiar until it functions as an owned or settled home.
- Active motifs: familiarity and habitual attachment (ء ل ف:B005/m01); staying and duration (ر ب ب:B007/m01); dwelling or home (ن ز ل:B003/m01); possession of a place (م ل ك:B002/m01)
- Ayah anchors: أَلْفِ (97:3); رَبِّهِم، الْمَلَائِكَةُ، تَنَزَّلُ (97:4); أَنزَلْنَاهُ (97:1)
- Synthesis: Staying supplies repetition, familiarity supplies the resulting attachment, and dwelling gives that attachment a location. Possession turns habitual residence into settled control.

### S2. Odor Absorbed and Released by Substance
- Reading type: latent/lexical
- Scene or process: A material acquires another substance's scent and later presents it as fragrance or stench.
- Active motifs: perceived odor (ر و ح:B004/m01); transfer of scent between substances (ر و ح:B004/m02); cooked contents (ق د ر:B007/m02); thick syrup or residue (ر ب ب:B006/m01)
- Ayah anchors: الرُّوحُ، رَبِّهِم (97:4); الْقَدْرِ (97:1-3)
- Synthesis: The thick or cooked material acts as a carrier, scent transfer changes its state, and smell is the perceiver's access to that change. Fragrance and stench are opposite outcomes of the same mechanism.

### S3. Upward Expulsion from a Bounded Body
- Reading type: latent/lexical
- Scene or process: Contents rise abruptly from an internal container and are expelled.
- Active motifs: vomiting or rising emesis (ط ل ع:B011/m01); vessel-like containment (ق د ر:B007/m01); thick internal contents (ر ب ب:B006/m01); sudden disruptive onset (ف ج ر:B003/m01)
- Ayah anchors: مَطْلَعِ، الْفَجْرِ (97:5); الْقَدْرِ (97:1-3); رَبِّهِم (97:4)
- Synthesis: The body is structured as a vessel, its contents as thick matter, and emesis as upward emergence. Sudden onset supplies the force and timing of expulsion.

### S4. The “Sound” Snake-Bitten Person
- Reading type: latent/lexical
- Scene or process: A harmed person is called sound either as an auspicious reversal or because the person has surrendered to the affliction.
- Active motifs: snake-bitten patient (س ل م:B009/m01); auspicious naming by the opposite state (س ل م:B009/m02); surrender to the affliction (س ل م:B009/m03)
- Ayah anchors: سَلَامٌ (97:5)
- Synthesis: The subchannel is a discourse relation built from contradiction: the name of safety marks actual injury. Its two internal explanations preserve either hoped-for recovery or completed submission.

### S5. Alternating Exertion and Restored Capacity
- Reading type: latent/lexical
- Scene or process: Workers alternate turns so that effort, rest, and renewed energy can sustain a task.
- Active motifs: alternation between workers or tasks (ر و ح:B008/m01); effective capacity (ق د ر:B003/m01); vigor and force (ر و ح:B011/m01); eager initiative (ر و ح:B010/m01); restorative rest (ر و ح:B007/m01)
- Ayah anchors: الرُّوحُ (97:4); الْقَدْرِ (97:1-3)
- Synthesis: Alternation distributes exertion, rest renews the worker, and capacity returns as force and initiative. The result is a repeatable labor cycle rather than a single burst of effort.


