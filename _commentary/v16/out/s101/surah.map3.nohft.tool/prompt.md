Surah: 101. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S101 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s101/surah.r2/text.md =====
# Surah 101

- 101:1 ٱلْقَارِعَةُ
- 101:2 مَا ٱلْقَارِعَةُ
- 101:3 وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/s101/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ر ع (root_001219): 101:1 ٱلْقَارِعَةُ, 101:2 ٱلْقَارِعَةُ, 101:3 ٱلْقَارِعَةُ

- **B001** bir şeye vurmak veya çarpmak — vurmak, çarpmak veya vurarak uyarmak · kaptakini sonuna kadar içince kabın alnına değmesi · hayvana vurmak için kullanılan değnek · taş kırmaya yarayan balta benzeri araç · ateş yakmak için kullanılan çakma aracı
  القاف والراء والعين معظم الباب ضرب الشيء (maqayis)؛ كل شيء ضربته فقد قرعته (ayn)؛ قرعت الباب أقرعه قرعا (sihah)؛ قرع راحلته أي ضربها بسوطه (tahdhib)؛ القرع ضرب شيء على شيء (mufradat)
- **B002** kılıçlarla karşılıklı çarpışmak — savaşta kılıçlarla karşılıklı dövüşme · dövüşte karşı karşıya gelen rakip
  مقارعة الأبطال قرع بعضهم بعضا (maqayis)؛ المقارعة والقراع المضاربة بالسيف في الحرب (ayn)؛ قريعك الذي يقارعك (sihah)؛ القراع والمقارعة المضاربة بالسيوف (tahdhib)
- **B003** damızlık erkeğin dişiyle çiftleşmesi ve dişinin erkeği istemesi — erkek hayvanın dişiye çiftleşmek için çıkması · çiftleşme için ayrılmış damızlık erkek · dişi deve veya sığırın çiftleşmek istemesi
  القريع الفحل لأنه يقرع الناقة (maqayis)؛ القريع من الإبل الفحل (ayn)؛ قرع الفحل الناقة يقرعها قرعا وقراعا (sihah)؛ استقرعت الناقة إذا اشتهت الضراب (tahdhib)
- **B004** kura çekmek ve kurayla paylaştırmak — kura veya kurada çıkan pay · aralarında kura çektirmek · kura çekerek seçmek veya paylaştırmak
  الإقراع والمقارعة هي المساهمة (maqayis)؛ أقرع القوم وتقارعوا بينهم والاسم القرعة (ayn)؛ أقرعت بينهم من القرعة واقترعوا وتقارعوا بمعنى (sihah)؛ أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه (tahdhib)
- **B005** sarsıcı büyük felaket veya dünyanın sonundaki hesap günü — büyük felaket veya dünyanın sonundaki hesap günü · Kuran'dan korkuya karşı okunan koruyucu bölümler
  القارعة الشديدة من شدائد الدهر والقارعة القيامة (maqayis)؛ القارعة القيامة والقارعة الشدة (ayn)؛ القارعة الشديدة من شدائد الدهر وهي الداهية (sihah)؛ النازلة الشديدة تنزل عليهم بأمر عظيم (tahdhib)؛ القارعة ما القارعة (mufradat)
- **B006** öğütle yola gelmek; durdurmak veya azarlamak — öğüt dinleyip vazgeçmek · doğru olana geri dönüp boyun eğmek · alıkoymak ve caydırmak · sertçe azarlama ve kınama · pişmanlıktan dişine vurmak
  رجل قرع إذا كان يقبل مشورة المشير (maqayis)؛ أقرعت إلى الحق إقراعا رجعت (maqayis)؛ فلان لا يقرع إقراعا إذا كان لا يقبل المشورة والنصيحة (sihah)؛ التقريع التعنيف (sihah)؛ فلان لا يقرع أي لا يرتدع (tahdhib)؛ أقرعته إذا كففته (tahdhib)
- **B007** seçilmiş önder veya bir şeyin en iyi bölümü; en iyisini vermek — güvenilen önder veya başkan · seçilmiş kişi veya önder · malın en iyi ve seçkin bölümü · evin sıcak veya soğukta en iyi yeri · ona malının en iyi bölümünü vermek
  القريع وهو السيد سمى بذلك لأنه يعول عليه في الأمور (maqayis)؛ أقرع فلان فلانا أعطاه خير ماله وخيار المال قرعته (maqayis)؛ القريعة وهو خير بيت في الربع (maqayis)؛ المقروع المختار للفحلة والمقروع السيد (sihah)؛ قريعة البيت خير موضع فيه (tahdhib)؛ القريعة والقرعة خيار المال (tahdhib)
- **B008** saç ya da örtü kaybı; bir yerin boş veya bitkisiz kalması — bir hastalık yüzünden saçların dökülmesi · saçı hastalık nedeniyle dökülmüş; kel · deri veya tüy hastalığına tutulmuş yavru deve · avlu veya hayvan barınağının boş kalması · bitki yetiştirmeyen veya otlatılıp çıplak kalmış arazi · açıkta kalan cinsel bölge · başında tüy bulunmayan iri yılan
  مما شذ عن هذا الأصل القرع وفصيل مقرع والقرع أيضا ذهاب الشعر من الرأس (maqayis)؛ القرع ذهاب شعر الرأس من داء (ayn)؛ الأقرع الذي ذهب شعر رأسه من آفة (sihah)؛ قرع الفناء إذا خلا من الغاشية (sihah)؛ أرض قرعة لا تنبت شيئا (tahdhib)؛ أصبحت الرياض قرعا قد جردتها المواشي (tahdhib)
- **B009** kabak meyvesi — kabak meyvesi
  القرع حمل اليقطين الواحدة قرعة (ayn)؛ القرع حمل اليقطين الواحدة قرعة (sihah)؛ القرع حمل اليقطين (tahdhib)
- **B010** yolun açık üst kesimi veya evin önü — yolun açık veya üst kesimi; evin önündeki açık alan
  قارعة الدار ساحتها وقارعة الطريق أعلاه (sihah)؛ قرعاء الدار ساحتها (tahdhib)؛ قارعة الطريق ساحتها وقارعة الطريق أعلاه (tahdhib)
- **B011** sert ve dayanıklı; kazınıp pürüzsüzleştirilmiş — sert ve dayanıklı · çakılla ovulmuş kap veya kabuğu soyulmuş dal · sertleşmiş toynak veya işkembe
  القراع الصلب الشديد (sihah)؛ ترس أقرع إذا كان صلبا وهو القراع أيضا (tahdhib)؛ قدح أقرع وهو الذي حك بالحصى (tahdhib)؛ مكان أقرع شديد صلب (tahdhib)
- **B012** yiyecek veya hurma konan torba ya da kap — yiyecek koymaya yarayan küçük veya geniş torba · hurma toplamak için kullanılan kap
  القرعة الجراب الواسع يلقى فيه الطعام (tahdhib)؛ القرعة الجراب الصغير وجمعها قرع (tahdhib)؛ المقرع وعاء يجبى فيه التمر (tahdhib)؛ قرع فلان في مقرعه كله السقاء والزق (tahdhib)

## د ر ي (root_000473): 101:3 أَدْرَىٰكَ, 101:10 أَدْرَىٰكَ

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

## ECHO د ر ر (root_000469): for 101:3 أَدْرَىٰكَ, 101:10 أَدْرَىٰكَ: withheld observed target; not identity

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

## ي و م (root_001700): 101:4 يَوْمَ

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

## ك و ن (root_001332): 101:4 يَكُونُ, 101:5 وَتَكُونُ

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

## ء ن س (root_000059): 101:4 ٱلنَّاسُ

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

## ف ر ش (root_001143): 101:4 كَٱلْفَرَاشِ

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

## ب ث ث (root_000083): 101:4 ٱلْمَبْثُوثِ

- **B001** dagitip yaymak — bir seyi dagitip yaymak veya aciga cikarmak · atlari saldiriya yaymak veya av kopeklerini ava salmak · yayilip dagilmak · cok ve daginik; yayilmis veya savrulmus · toplanmamis, etrafa sacilmis hurma · yiyecegi veya hurmayi alt ust edip birbirinin ustune atmak · yaratilmislari veya hayvanlari yeryuzune yayip cogaltmak
  تفريق الشيء وإظهاره؛ بثوا الخيل؛ بث الصياد كلابه؛ خلق الخلق وبثهم في الأرض؛ وزرابي مبثوثة؛ تمر بث؛ بثثت الطعام والتمر (maqayis)؛ بث الخيل؛ كل شيء فرقته؛ انبث الجراد؛ كالفراش المبثوث؛ تمر بث (jamhara)؛ فانبث أي انتشر؛ تمر بث؛ منثورا متفرقا؛ الغبار إذا هيجته (sihah)؛ تفريقك الأشياء؛ بثوا الخيل؛ بث الصياد كلابه؛ بثت البسط؛ مبثوثة كثيرة؛ غبارا منتشرا؛ وبث منهما رجالا كثيرا ونساء أي نشر وكثر (tahdhib)؛ التفريق وإثارة الشيء كبث الريح التراب؛ بثثته فانبث؛ وبث فيها؛ كالفراش المبثوث (mufradat)
- **B002** icindekini acip dile getirmek — haberi veya sozu yaymak, duyurmak · birine sirrini acmak ve onu haberdar etmek · insanin icinde tasidigi keder, gam veya sikinti · yoksullugunu ve duskunlugunu birine sikayet etmek · gizli bir kusur, sevgi veya isin durumunu yoklayip anlamaya calisma
  بثثت الحديث أي نشرته؛ البث من الحزن؛ يشتكى ويبث ويظهر؛ أبث فلان شقوره وفقوره؛ وأبثثتك مكتومي (maqayis)؛ بثثته سري وأبثثته؛ البث ما يجده الرجل في نفسه من كرب أو غم (jamhara)؛ بث الخبر وأبثه؛ نشره؛ أبثثتك سري؛ أظهرته لك؛ البث الحال والحزن؛ أظهرت لك بثي (sihah)؛ البث الحزن الذي تفضي به إلى صاحبك؛ أبثثت فلانا سري؛ أطلعته عليه؛ لا يولج الكف ليعلم البث (tahdhib)؛ بث النفس ما انطوت عليه من الغم والسر؛ غمي الذي أبثه عن كتمان (mufradat)
- **B003** arastirip aciga cikarmak [kalıp] — haberi yaymak veya tozu kaldirip savurmak · bir isi arastirip yoklamak veya aciga cikarmak
  بثبثت الخبر بثبثة نشرته؛ وكذلك الغبار إذا هيجته (sihah)؛ بثبثت الأمر إذا فتشت عنه وتخبرته؛ بثبثوه أي كشفوه؛ الأصل فيه بثثوه فأبدلوا (tahdhib)

## ج ب ل (root_000217): 101:5 ٱلْجِبَالُ

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

## ع ه ن (root_001056): 101:5 كَٱلْعِهْنِ

- **B001** elde ve kullanıma hazır bulunma — elde bulunan, erişilebilir, yerleşik · eldeki, hemen kullanılabilen veya eskiden beri sahip olunan mal · istediğini ona tez elden verdi · o yerde kaldı ve yerleşti
  العاهن المال الذي يتروح على أهله وهو العتيد الحاضر (maqayis); عاهن إذا كان في يدك تقدر عليه (maqayis); اعهن له أي عجل له (maqayis); مال عاهن يغدو من عند أهله ويروح عليهم (ayn); من عاهن ماله وآهنه أي من تلاده (sihah); العاهن الحاضر المقيم الثابت (sihah); عهن بالمكان أقام به (sihah); العاهن الطعام الحاضر والشراب الحاضر (tahdhib); خذ من عاهن المال وآهنه أي من عاجله وحاضره (tahdhib)
- **B002** kopmadan kırılıp sarkma — kırılmış, ezilip sarkmış; kişi için gevşek ve tembel · çubukta kopma olmadan oluşan kırılma · çubuğu koparmadan kırdı
  قضيب عاهن أي متكسر منهصر (maqayis); عهنة وذلك انكسار من غير بينونة (maqayis); عهنت القضيب أعهنه عهنا (maqayis); العهنة انكسار في قضيب من غير بينونة (ayn); قضيب عاهن أي منكسر (ayn); سمي الفقير عاهنا لانكساره (ayn); فلان عاهن أي مسترخ كسلان (tahdhib); أصل العاهن أن يتقصف القضيب من الشجرة ولا يبين منها فيبقى معلقا مسترخيا (tahdhib)
- **B003** boyalı yün — çeşitli renklere boyanmış yün · bazı kaynaklarda her türlü yün · bir parça yün · yünler veya yün parçaları
  العهن الصوف المصبوغ (maqayis;mufradat); العهن المصبوغ ألوانا من الصوف (ayn); كل صوف عهن (ayn); القطعة عهنة والجمع عهون (ayn); العهن الصوف والقطعة منه عهنة والجمع عهون (sihah); العهن الصوف المصبوغ ألوانا وجمعه عهون (tahdhib); لكل صوف عهن والقطعة عهنة (tahdhib); تخصيص العهن لما فيه من اللون (mufradat)
- **B004** hurmanın merkeze yakın taze yaprakları — hurmanın merkeze en yakın taze yaprakları · hurmanın merkeze yakın yaprakları kurudu · insanın uzuvları bu yapraklara benzetilerek adlandırılır
  عواهن النخل ما يلي قلب النخلة من الجريد (maqayis); السعفات التي تلي القلبة العواهن لأنها رطبة لم تشتد (maqayis); العواهن السعف الذي يقرب من لب النخلة (ayn); العواهن السعفات اللواتي يلين القلبة (sihah;tahdhib); ومنه سمي جوارح الإنسان عواهن (sihah); عهنت عواهن النخل إذا يبست (sihah;tahdhib)
- **B005** deve rahmindeki damarlar veya iç bölüm — dişi devenin rahmindeki damarlar veya iç bölüm
  العواهن عروق في رحم الناقة (maqayis;sihah;tahdhib); عواهنها موضع رحمها من باطن كعواهن النخل (tahdhib)
- **B006** doğruluğunu önemsemeden gelişigüzel konuşmak — sözü doğruluğunu önemsemeden ve düşünmeden ortaya atmak
  يلقي الكلام على عواهنه إذا لم يبال كيف تكلم (maqayis); من دون يقين (maqayis); رمى فلان بالكلام على عواهنه إذا لم يبال أصاب أم أخطأ (sihah;tahdhib); يحدس الكلام على عواهنه وهو أن يتعسف الكلام ولا يتأتى (tahdhib); أورده من غير فكر وروية (mufradat)
- **B007** malı iyi gözetip yöneten [kalıp] — malı iyi gözetip yöneten kimse
  فلان عهن مال إذا كان حسن القيام عليه (sihah); إنه لعهن مال إذا كان حسن القيام عليه (tahdhib)
- **B008** birinden iyilik ya da haber çıkması — 
  عهن من فلان خير أو خبر أنا أشك في ذلك يعهن عهونا إذا خرج منه
- **B009** kırmızı çiçekli kır bitkisi veya çiçeği — kırmızı çiçekli kır bitkisi veya onun kırmızı çiçeği
  رأيت في البادية شجرة لها وردة حمراء يسمونها العهنة
- **B010** palmiye meyve salkımının dip sapı — palmiye meyve salkımının dip sapı
  العهان والإهان والعرهون والعرجون والفتاق والعسق والطريدة واللعين والضلع والعرجد واحد; والكل أصل الكباسة
- **B011** bir şey hakkında bilgi sahibi olmak — 
  عهنت على كذا أعهن، المعنى أي أثبى منه معرفة

## ن ف ش (root_001534): 101:5 ٱلْمَنفُوشِ

- **B001** yün ya da pamuğu açıp kabartma — yün ya da pamuğu dövüp didikleyerek veya yayarak açıp kabartma · yün ya da pamuğu açıp kabartma · didiklenip kabartılarak yayılmış yün
  نفش الصوف وهو أن يطرق حتى يتنفش (maqayis)؛ النفش مدك الصوف حتى ينتفش بعضه عن بعض (ayn;tahdhib)؛ نفشت القطن والصوف وعهن منفوش والتنفيش مثله (sihah)؛ النفش نشر الصوف كالعهن المنفوش (mufradat)
- **B002** gevşekçe yayılıp kabarma — gevşekçe yayılmış ve kabarık; kılı ya da tüyü dikleşmiş · kabarıp yayılmış; kılı ya da tüyü dikleşmiş · kuşun kanatlarını açıp yayması · sırtlanın ya da kuşun korku veya titremeyle kılını ya da tüyünü kabartması · yüze doğru yayılıp genişlemiş burun ucu
  نفش الطائر جناحيه (maqayis)؛ كل شيء تراه منتشرا رخو الجوف فهو منتفش (ayn;tahdhib)؛ تنفش الضبعان أو بعض الطير إذا نفش شعره وريشه (ayn;tahdhib)؛ انتفشت الهرة وتنفشت أي ازبأرت (sihah)
- **B003** hayvanların gece çobansız otlağa dağılıp otlaması — deve ve koyunların gece çobansız ya da sahibinin bilgisi dışında otlağa dağılıp otlaması · hayvanların gece çobansız otlağa yayılıp otlaması · develeri gece çobansız otlamaya salmak · gece otlakta çobansız dolaşıp otlayan develer
  نفشت الإبل ترددت وانتشرت بلا راع (maqayis)؛ إبل نوافش ترددت بالليل في المراعي بلا راع وأنفشوا إبلهم أرسلوها بالليل (ayn)؛ نفشت الإبل والغنم أي رعت ليلا بلا راع ولا يكون النفش إلا بالليل (sihah)؛ أن تنتشر الإبل بالليل فترعى وتفرقت في المرعى من غير علم صاحبها (tahdhib)؛ نفش الغنم انتشارها والإبل النوافش المترددة ليلا في المرعى بلا راع (mufradat)

## ث ق ل (root_000202): 101:6 ثَقُلَتْ

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

## و ز ن (root_001645): 101:6 مَوَٰزِينُهُۥ, 101:8 مَوَٰزِينُهُۥ

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

## ع ي ش (root_001067): 101:7 عِيشَةٍ

- **B001** yaşam ve yaşayış durumu — yaşam · yaşadı · Tanrı ona hoşnut olacağı bir yaşam verdi · yaşayış biçimi · iyi bir yaşayış · övgüye değer bir yaşayış · dar ve sıkıntılı yaşam · durumu iyi olan kimse
  العيش الحياة (maqayis;ayn;sihah); العيش الحياة المختصة بالحيوان (mufradat); عيشة صالحة وراضية وصدق وسوء وضنك (maqayis;sihah;tahdhib;mufradat); رجل عائش حاله حسنة (maqayis;tahdhib)
- **B002** geçim araçları, ortamı ve geçinme uğraşı — yaşamı sağlayan yiyecek ve içecek · geçim kaynağı · geçim kaynakları · geçim aracı veya geçinilen yer · gündüz, geçim arama zamanı · yeryüzü, geçim sağlanan yer · geçim · geçinme yollarını sağlamak için çabalama · geçinebilecek kadar olanağa sahip olma · geçim · o topluluğun geçimliği süttür
  المعيشة ما يعاش به (maqayis;ayn;tahdhib); المطعم والمشرب وما يكون به الحياة (maqayis;ayn;tahdhib); كل شيء يعاش به أو فيه فهو معاش (maqayis;ayn); كل شيء يعاش به فهو معاش (tahdhib); ما يتعيش منه (mufradat); التعيش تكلف أسباب المعيشة (sihah); يتعيشون إذا كانت لهم بلغة من عيش (maqayis;tahdhib)

## ر ض و (root_000569): 101:7 رَّاضِيَةٍ

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ECHO ر ض ي (root_000570): for 101:7 رَّاضِيَةٍ: withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)

## خ ف ف (root_000427): 101:8 خَفَّتْ

- **B001** ağırlığın veya yükün az olması ve azaltılması — ağırlığı azalmak · az ağırlıklı, taşıması kolay · ağırlık, yük veya güçlük azlığı · ağırlığını azaltmak · yükünü azaltmak · ağırlığı az bulmak · durumu kolaylaşıp yükü azalmak · taşınması kolay eşya · dile kolay gelen söz
  خف الشيء يخف خفة وهو خفيف (maqayis;sihah)؛ الخفة خفة الوزن وخفة الحال (ayn;tahdhib)؛ التخفيف ضد التثقيل واستخفه خلاف استثقله (sihah)؛ خففه تخفيفا وتخفف تخففا وخف المتاع وكلام خفيف على اللسان (mufradat)؛ خفوا في السجود ولا ترسل نفسك إرسالا ثقيلا (tahdhib)
- **B002** hızla yola çıkmak — topluluk hızla yola çıktı · konaktan hızlı ayrılış, yola çıkma vakti · topluluğun binekleri hızlıydı · hızlı deve kuşu
  خف القوم ارتحلوا (maqayis)؛ الخفوف سرعة السير من المحلة وحان الخفوف وخف القوم إذا ارتحلوا مسرعين (ayn;tahdhib)؛ أخف القوم إذا كانت دوابهم خفافا (sihah)؛ خفوا عن منازلهم ارتحلوا منها في خفة (mufradat)؛ الخفانة النعامة السريعة (ayn)
- **B003** sayısı veya ölçülen payı az olmak — topluluğun sayısı azaldı · kalabalıkları azaldı · arkadaşlarından küçük bir topluluk içinde · ölçülen iyi işleri az geldi
  خرج فلان في خف من أصحابه أي في جماعة قليلة وخف القوم خفوفا أي قلوا وقد خفت زحمتهم (sihah)؛ فمن خفت موازينه إشارة إلى كثرة الأعمال الصالحة وقلتها (mufradat)
- **B004** kararlılığını yitirip ölçüsüzce yönelmek — kişinin düşüncesiz ve ölçüsüz davranması · çabuk coşan, yerinde duramayan · sevinç onu hareketlendirdi · seni kararından oynatmasın · bilgisizliğini kullanıp yanlış yola sürükledi
  وخفة الرجل طيشه وخفته في عمله (ayn;tahdhib)؛ خفيف القلب في توقده فهو خفاف (ayn;tahdhib)؛ الخفيف فيمن يطيش (mufradat)؛ لا يستخفنك أي لا يزعجنك ويزيلنك عن اعتقادك (mufradat)؛ استخفه الفرح إذا ارتاح لأمر (tahdhib)؛ استخفه فلان إذا استجهله فحمله على اتباعه في غيه (tahdhib)
- **B005** aşağılayıp değersiz saymak — onu aşağılayıp değersiz saydı · hakkımı önemsemedi
  استخف به أهانه (sihah)؛ استخف فلان بحقي إذا استهان به (tahdhib)
- **B006** deve ayağı ucu veya kapalı ayak giysisi — devenin tabanlı ayak ucu · ayağa giyilen kapalı ayak giysisi · sandaldan daha kalın ayak giysisi · deve türünden yarış hayvanı · deve veya deve kuşunun ayak ucu
  الخف مجمع فرسن البعير (ayn;tahdhib)؛ الخف ما يلبسه الإنسان (ayn;tahdhib)؛ الخف واحد أخفاف البعير والخف واحد الخفاف التي تلبس والخف في الأرض أغلظ من النعل (sihah)؛ الخف فمن الباب لأن الماشي يخف وهو لابسه وخف البعير منه أيضا (maqayis)؛ الخف الملبوس وخف النعامة والبعير تشبيها بخف الإنسان (mufradat)؛ لا سبق إلا في خف أو نصل أو حافر فالخف الإبل ها هنا (tahdhib)
- **B007** uyup boyun eğmek — ona uyup boyun eğdi · dişi eşekler erkek eşeğe uydu · hizmetine çevikçe koştu · topluluğunu kendisiyle birlikte harekete geçirip kendine uydurdu
  خف فلان لفلان إذا أطاعه وانقاد له وخفت الأتن لعيرها إذا أطاعته (tahdhib)؛ استخف قومه فأطاعوه أي حملهم أن يخفوا معه أو وجدهم خفافا في أبدانهم وعزائمهم (mufradat)
- **B008** develerin birbirini izleyerek art arda gelmesi [kalıp] — develerin birbirini izlediği tek sıra halinde
  جاءت الإبل على خف واحد إذا تبع بعضها بعضا مقطورة كانت أو غير مقطورة (tahdhib)
- **B009** köpek sesi veya giysi hışırtısı; kanat çırparak uçan kuş — köpeklerin çıkardığı ses · yeni gömleği hareket ettirip hışırtı çıkarmak · kanatlarını çırparak uçan kuş
  أصوات الكلاب فيقال لها الخفخفة فهو قريب من الباب (maqayis)؛ خفخف إذا حرك قميصه الجديد فسمعت له خفخفة أي صوتا (tahdhib)؛ الخفخوف الطائر الذي يصفق بجناحيه إذا طار (tahdhib)

## ء م م (root_000053): 101:9 فَأُمُّهُۥ

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

## ه و ي (root_001609): 101:9 هَاوِيَةٌ

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

## ن و ر (root_001564): 101:11 نَارٌ

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

## ح م ي (root_000358): 101:11 حَامِيَةٌۢ

- **B001** ısınma ve ısıtma — ısındı, sıcaklığı arttı · demiri ateşte ısıttı · at koşudan ısınıp terledi · altın ve gümüşü ısıtma, bu işlemden iyi çıkma
  حمي الشيء يحمى حميا إذا سخن (ayn)؛ الحامية الحارة (ayn)؛ حمى النهار وحمي التنور أي اشتد حره (sihah)؛ أحميت الحديد في النار فهو محمى (sihah)؛ الحمي الحرارة المتولدة من الجواهر المحمية كالنار والشمس ومن القوة الحارة في البدن (mufradat)؛ حمي الفرس إذا عرق يحمى حميا وحمى الشد مثله (ayn;tahdhib)؛ هذا الذهب والفضة لحسن الحماء أي خرج من الحماء حسنا (ayn;tahdhib)
- **B002** koruma ve uzak tutma — onu korudu, yaklaşanı savdı · otlatmaya kapalı korunan yer · yeri korunan ve girilmez alan yaptı · hastaya zararlı yiyeceği yasakladı · hasta sakıncalı yiyeceklerden uzak durdu · insanlar ondan sakınıp uzak durdu · onu savundu ve korudu · yanındakileri ya da kendini koruyan kişi veya topluluk
  حميت القوم حماية وكل شيء دفعت عنه فقد حميته (ayn)؛ الحمى موضع فيه كلأ يحمى من الناس أن يرعى (ayn;tahdhib)؛ حميته حماية إذا دفعت عنه (sihah)؛ هذا شيء حمى أي محظور لا يقرب (sihah)؛ حميت المريض حمية منعته أكل ما يضره (ayn)؛ حاميت عنه محاماة وحماء (sihah)؛ تحاماه الناس أي توقوه واجتنبوه (sihah)؛ حمى أهله في القتال حماية (tahdhib)
- **B003** gücenme ve öfkelenme — onuruna yedirememe, gücenme ve öfke · ona öfkelendi · onurlu, aşağılanmayı kabul etmeyen
  حميت من هذا الشيء أحمى منه حمية أي أنفت أنفا وغضبا (ayn)؛ حميت عن كذا حمية ومحمية إذا أنفت منه وداخلك عار وأنفة (sihah)؛ حميت عليه غضبت (sihah)؛ حمى فلان أنفه يحميه حمية ومحمية (tahdhib)؛ عبر عن القوة الغضبية إذا ثارت وكثرت بالحمية (mufradat)
- **B004** kocanın yakınları — kocanın babası, erkek kardeşi ya da başka bir erkek yakını · kadının kocası tarafından gelen yakınları · kadının kayınvalidesi · kocanın erkek yakınıyla baş başa kalmak ölüm kadar tehlikelidir
  الحمو أبو الزوج وأخو الزوج وكل من ولي الزوج من ذي قرابته فهم أحماء المرأة وأم زوجها حماتها (ayn;tahdhib)؛ حماة المرأة أم زوجها (sihah;tahdhib)؛ كل شيء من قبل الزوج مثل الأب والأخ فهم الأحماء واحدهم حما (sihah)؛ الأحماء من قبل الزوج والأختان من قبل المرأة (tahdhib)؛ الحمو الموت (tahdhib)؛ أحماء المرأة كل من كان من قبل زوجها (mufradat)
- **B005** dokunulmaz sayılan damızlık erkek deve — binilmeyen, kırkılmayan ve otlaktan alıkonmayan damızlık erkek deve · damızlık geçmişi nedeniyle sırtı dokunulmaz sayılan erkek deve
  الحامي الفحل من الإبل الذي طال مكثه عندهم (sihah)؛ إذا لقح ولد ولده فقد حمى ظهره فلا يركب ولا يجز له وبر ولا يمنع من مرعى (sihah)؛ ولا حام قيل هو الفحل إذا ضرب عشرة أبطن كأن يقال حمى ظهره فلا يركب (mufradat)
- **B006** kara ve kötü kokulu balçık — kara ve kötü kokulu balçık · kara balçık, akarsu ya da kuyudan çıkarılan balçık · balçıklı pınar · kuyunun balçığını çıkardı
  الحمأ الطين الأسود المنتن (ayn)؛ يسمى الطين الذي نبث من النهر الحمأة (ayn)؛ عين حمئة أي ذات حمأة (ayn;mufradat)؛ الحمأة والحمأ طين أسود منتن (mufradat)؛ حمأت البئر أخرجت حمأتها وأحمأتها جعلت فيها حما (mufradat)
- **B007** sokucu hayvan zehrinin yakıcı etkisi — sokan ya da ısıran canlının zehri ve yakıcı etkisi · akrebin zehri ve verdiği zarar, iğnesi değil
  الحُمَة سم كل شيء يلدغ أو يلسع (ayn;tahdhib)؛ حمة العقرب سمها وضرها (sihah)؛ الحمة مخففة حرارة السم وليست كما تسمي العامة حمة العقرب إبرتها (jamhara)؛ هي فوعة السم أي حرارته وفورته (jamhara)؛ بسم العقرب الحمة والحمة (tahdhib)
- **B008** etkinin keskinliği ve şiddeti — içkinin ilk yükselişi, sıcaklığı ve içene yayılan etkisi · ağrının kabaran keskinliği · şeyin sertliği ve şiddeti
  الحميا بلوغ الخمر من شاربها (ayn)؛ حميا الكأس أول سورتها (sihah)؛ حموة الألم سورته (sihah)؛ حميا الكأس يعني سورتها (tahdhib)؛ الحميا دبيب الشراب (tahdhib)؛ حميا الشيء حدته وشدته (tahdhib)؛ حميا الكأس سورتها وحرارتها (mufradat)
- **B009** bacağın içindeki kabarık kas parçası — bacağın içindeki kabarık et ya da kas parçası · atın bacağının eninde bulunan iki et parçası
  الحمأة لحمة منتبرة في باطن الساق (ayn)؛ الحماة عضلة الساق (sihah)؛ في ساق الفرس حماتان وهما اللحمتان اللتان في عرض الساق (sihah)؛ الحماة لحمة منتبرة في باطن الساق (tahdhib)؛ الحماتان اللحمتان اللتان في عرض الساق (tahdhib)
- **B010** toynağın iki yan kenarı — toynağın ortadaki bölümünün sağ ve solundaki iki parça · toynağın sağ ve sol yan kenarları
  الحاميتان ما عن يمين السنبك وشماله (sihah;tahdhib)؛ الحوامي وهي حروفها من عن يمين وشمال (tahdhib)
- **B011** kuyu duvarını ören ağır taşlar — kuyu duvarını örmekte kullanılan taş · kuyu örgüsünü sağlamlaştıran büyük ve ağır kayalar
  الحامية الحجارة يطوى بها البئر (ayn;tahdhib)؛ الحوامي عظام الحجارة وثقالها (tahdhib)؛ الحوامي صخر عظام تجعل في مآخير الطي (tahdhib)؛ حجارة الركية كلها حوام (tahdhib)
- **B012** kararıp kara bir görünüm alma — karardı, kara bir görünüm aldı · üst üste yığılmış kara bulut
  احمومى الشيء فهو محموم واحمومى الليل والسحاب وذلك من السواد (ayn)؛ احمومى الشيء فهو محموم يوصف به الأسود من نحو الليل والسحاب (tahdhib)؛ المحمومي من السحاب الأسود المتراكم (tahdhib)



===== _commentary/v16/work/s101/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s101/reader_a_pilot.md)

# s101 Semantic Channel Discovery

## Parent Channels

### 1. Impact Across Resistant Boundaries
- Semantic invariant: Directed force meets a resistant surface and produces displacement, penetration, fracture, or an opened interior.
- Surface relation: direct; 101:1-3 القارعة (ق ر ع) names the striking event, while 101:9 هاوية (ه و ي) supplies the downward or opened destination.
- Surprising reach: The catastrophic blow extends into cranial anatomy, sharp implements, excavation resistance, and stone lining.

#### Subchannel A. Blow, Descent, and Dispersive Impact
- Reading type: mixed
- Scene or process: A blow or downward cast strikes a target and sends what was gathered into scattered motion.
- Active motifs: striking or knocking (ق ر ع:B001/m01); reaching or striking with hand or weapon (ه و ي:B003/m01); casting down (ه و ي:B003/m02); scattering after impact (ب ث ث:B001/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 مبثوث (ب ث ث); 101:9 هاوية (ه و ي)
- Synthesis: The قارعة is read through the concrete action of one thing striking another. The hand or weapon descends toward its object, and the impact converts cohesion into broadcast fragments or bodies.

#### Subchannel B. Cranial Breach and Gaping Wound
- Reading type: latent/lexical
- Scene or process: A strike crosses the outer head, reaches a thin cranial layer, and leaves an opened wound.
- Active motifs: head-strike (ق ر ع:B001/m01); cranial and bone plates (ف ر ش:B010/m01); wound reaching the bone layer (ف ر ش:B011/m01); brain or cranial membrane (ء م م:B003/m01); wound reaching the brain (ء م م:B003/m02); opened wound-mouth (ه و ي:B007/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:9 أمّه (ء م م) and هاوية (ه و ي)
- Synthesis: The striking action becomes a bodily penetration scene: force breaks through the head, reaches the thin supporting layer, and exposes the deeper cranial center as a gaping interior.

#### Subchannel C. Hard Ground, Pointed Tool, and Stabilized Edge
- Reading type: latent/lexical
- Scene or process: A sharpened implement meets an unyielding substrate, while stonework fixes the edge of the opening.
- Active motifs: hard ground that stops digging (ج ب ل:B005/m01); hard stripped surface (ق ر ع:B011/m01); pointed horn or implement (د ر ي:B004/m01); stones lining a well (ح م ي:B011/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:3,10 أَدْرَىٰ (د ر ي); 101:5 الجبال (ج ب ل); 101:11 حامية (ح م ي)
- Synthesis: Resistance, cutting point, and lining form one excavation mechanism. The solid layer halts ordinary digging, the pointed edge concentrates force, and large stones preserve the boundary once an opening is made.

### 2. Release Into Distributed Motion
- Semantic invariant: A compact body, flock, fiber mass, or ordered group opens into loose, repeated, or directionless movement.
- Surface relation: direct; 101:4 الفراش المبثوث (ف ر ش، ب ث ث) and 101:5 العهن المنفوش (ع ه ن، ن ف ش) present two successive dispersal images.
- Surprising reach: The same release pattern joins moth flight, carded wool, roaming livestock, and a bird spreading itself over its young.

#### Subchannel A. Moth-Swarm Scattering
- Reading type: surface-primary
- Scene or process: Light flying bodies flutter toward a stimulus and lose collective order as they spread.
- Active motifs: flying moth (ف ر ش:B005/m01); fluttering toward light or fire (ف ر ش:B005/m02); scattering and broadcast spread (ب ث ث:B001/m01); agitated lightness (خ ف ف:B004/m01)
- Ayah anchors: 101:4 الفراش and مبثوث (ف ر ش، ب ث ث); 101:8 خفّت (خ ف ف)
- Synthesis: The human multitude takes the motion signature of moths: light, agitated bodies converge on a luminous center while simultaneously dispersing into an ungoverned swarm.

#### Subchannel B. Carded Wool and Unmade Fabric
- Reading type: surface-primary
- Scene or process: Dyed wool is beaten or teased until a compact textile mass becomes loose fiber.
- Active motifs: dyed wool (ع ه ن:B003/m01); carding and teasing wool (ن ف ش:B001/m01); fiber separation (ب ث ث:B001/m02); tightly made weave (ج ب ل:B007/m01)
- Ayah anchors: 101:4 مبثوث (ب ث ث); 101:5 العهن and المنفوش (ع ه ن، ن ف ش); 101:5 الجبال (ج ب ل)
- Synthesis: A contrast between tight fabrication and fiber release structures the scene. What could be spun or woven is worked backward into separated, buoyant strands, matching the mountains' loss of compact form.

#### Subchannel C. Night-Roaming Herd
- Reading type: latent/lexical
- Scene or process: Livestock leave ordered containment, spread through pasture at night, and move in a following procession.
- Active motifs: livestock dispersing at night without a shepherd (ن ف ش:B003/m01); young or low-bearing livestock (ف ر ش:B004/m01); camels following one another (خ ف ف:B008/m01); long part of the night (ه و ي:B006/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 المنفوش (ن ف ش); 101:8 خفّت (خ ف ف); 101:9 هاوية (ه و ي)
- Synthesis: The release of animals has a temporal and processional shape: a herd spreads beyond supervision during the night, yet individual animals still trail one another through the pasture.

#### Subchannel D. Wing-Spreading and Brooding
- Reading type: latent/lexical
- Scene or process: A bird opens and fluffs its wings close to the ground, either fluttering or covering its young.
- Active motifs: wing-spreading near the ground (ف ر ش:B006/m01); brooding over chicks (ف ر ش:B006/m02); feather fluffing (ن ف ش:B002/m01); outward spread (ب ث ث:B001/m01)
- Ayah anchors: 101:4 الفراش and مبثوث (ف ر ش، ب ث ث); 101:5 المنفوش (ن ف ش)
- Synthesis: Distributed motion also serves care rather than disorder. Feathers open, wings flatten toward the ground, and the same spreading gesture that describes flutter can become a protective cover over offspring.

### 3. Measure as Outcome, Form, and Rank
- Semantic invariant: Comparison against a measure converts physical quantity into judgment, proportion, social worth, or a determined form.
- Surface relation: direct; 101:6 ثقلت موازينه and 101:8 خفت موازينه (ث ق ل، خ ف ف، و ز ن) state the decisive heavy-light contrast.
- Surprising reach: The scale extends from reckoning into demography, bodily proportion, leadership, preciousness, and intellectual steadiness.

#### Subchannel A. Scales That Determine Outcome
- Reading type: surface-primary
- Scene or process: Deeds or values are placed in a balance, become heavy or light, and determine the resulting condition.
- Active motifs: physical and moral heaviness (ث ق ل:B001/m01, ث ق ل:B001/m02); light weight or load (خ ف ف:B001/m01); weighing and estimation (و ز ن:B001/m01); just balance and reckoning (و ز ن:B002/m01)
- Ayah anchors: 101:6 ثقلت and موازينه (ث ق ل، و ز ن); 101:8 خفّت and موازينه (خ ف ف، و ز ن)
- Synthesis: Weight is both mechanism and verdict. The balance compares what is presented, heaviness gives it consequence, and lightness marks insufficiency within the same act of reckoning.

#### Subchannel B. Quantity, Scarcity, and Multitude
- Reading type: latent/lexical
- Scene or process: A population or amount is estimated as abundant, standard, or deficient.
- Active motifs: known weight or standard measure (ث ق ل:B004/m01); appraisal or estimation (و ز ن:B001/m02); small amount or few persons (خ ف ف:B003/m01, خ ف ف:B003/m02); multitude like a mountain (ج ب ل:B002/m01)
- Ayah anchors: 101:5 الجبال (ج ب ل); 101:6 ثقلت and موازينه (ث ق ل، و ز ن); 101:8 خفّت (خ ف ف)
- Synthesis: The physical scale generalizes into counting a collective. Mountain-like abundance occupies one end of the comparison, while lightness names a reduced crowd or diminished amount.

#### Subchannel C. Worth, Eminence, and Chosen Rank
- Reading type: latent/lexical
- Scene or process: A person or possession acquires weight, is selected as the best, and becomes socially elevated.
- Active motifs: precious or weighty thing (ث ق ل:B005/m01); eminent person (ث ق ل:B005/m02); social worth (و ز ن:B007/m01); selected chief or best portion (ق ر ع:B007/m01); leaders likened to mountains (ج ب ل:B012/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:6 ثقلت and موازينه (ث ق ل، و ز ن); 101:8 موازينه (و ز ن)
- Synthesis: Measured weight becomes rank. The valuable object and weighty person share a scale of consequence; selection raises one candidate above others, and mountain imagery gives that rank visible height and stability.

#### Subchannel D. Proportioned Creation and Embodied Form
- Reading type: latent/lexical
- Scene or process: A created body receives measured proportion, innate constitution, stature, and material thickness.
- Active motifs: balanced created form (و ز ن:B008/m01); innate constitution (ج ب ل:B004/m01); stature and bodily form (ء م م:B006/m01); good constitution (ء م م:B006/m02); bodily thickness and frame (ج ب ل:B003/m01)
- Ayah anchors: 101:5 الجبال (ج ب ل); 101:6,8 موازينه (و ز ن); 101:9 أمّه (ء م م)
- Synthesis: Weighing becomes formation rather than verdict. Proportion fixes the creature's measure, innate nature supplies its pattern, and stature and bodily thickness realize that pattern in visible form.

### 4. Time Becoming Event
- Semantic invariant: A span of time gains structure by being bounded, prolonged, filled by an occurrence, or recognized as a decisive event.
- Surface relation: direct; 101:4 يوم (ي و م) frames the transformations, and 101:4-5 يكون/تكون (ك و ن) present their coming into occurrence.
- Surprising reach: Noon can be a balance, a day can be a battle or calamity, and an event can culminate in acknowledgment.

#### Subchannel A. Bounded Day and Extended Interval
- Reading type: mixed
- Scene or process: Daylight supplies a bounded unit that can stretch into an unspecified period or a long portion of night.
- Active motifs: daylight day (ي و م:B001/m01); duration or age (ي و م:B002/m01); long interval or night portion (ه و ي:B006/m01); delayed span (ء م م:B008/m01); midday balance (و ز ن:B004/m01)
- Ayah anchors: 101:4 يوم (ي و م); 101:6,8 موازينه (و ز ن); 101:9 هاوية (ه و ي); 101:9 أمّه (ء م م)
- Synthesis: The ordinary day anchors several scales of duration. Its midpoint is imagined as a poised balance, while its lexical field can widen to an age, a delay, or an extended passage through night.

#### Subchannel B. Calamity Entering Existence
- Reading type: mixed
- Scene or process: A great occurrence arrives in time, becomes the prevailing condition, and can unfold as adversity or conflict.
- Active motifs: calamitous day or event (ي و م:B003/m01); occurrence in time (ك و ن:B001/m01); adverse condition (ك و ن:B006/m01); feud arising among people (ن و ر:B007/m01)
- Ayah anchors: 101:4 يوم and يكون (ي و م، ك و ن); 101:5 تكون (ك و ن); 101:11 نار (ن و ر)
- Synthesis: Time is not a neutral container here: the day is the event itself. Coming-to-be gives the calamity presence, adverse condition gives it experiential force, and the feud sense shows how an occurrence can become a collective rupture.

#### Subchannel C. Detection, Knowledge, and Admission of an Event
- Reading type: mixed
- Scene or process: An occurrence is sensed, understood, communicated, and finally acknowledged.
- Active motifs: visual detection (ء ن س:B002/m01); auditory detection (ء ن س:B002/m02); knowledge (د ر ي:B001/m01); informing another (د ر ي:B001/m02); acknowledgment or admission (ء م ه:B002/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); no direct surface occurrence for ء ن س or ء م ه
- Synthesis: The event moves through stages of cognition: perception supplies an initial signal, knowledge organizes it, communication transfers it, and admission turns inward recognition into an explicit response.

### 5. Centers That Generate, Hold, and Receive
- Semantic invariant: A center can be an origin, parent, womb, prepared enclosure, collecting vessel, or final place of return.
- Surface relation: direct; 101:9 أمّه هاوية (ء م م، ه و ي) fuses motherhood or origin with a receiving abyss.
- Surprising reach: Maternal nurture connects with nests, provisions, gestation, breeding, sacks, and the release of stored contents.

#### Subchannel A. Mother as Origin and Destination
- Reading type: mixed
- Scene or process: A maternal source gathers dependents and also names the place to which one returns or is delivered.
- Active motifs: mother or parent (ء م م:B001/m01); origin or source (ء م م:B002/m01); center and point of return (ء م م:B002/m03); lexical mother-base (ء م ه:B004/m01); abyss or receiving depth (ه و ي:B002/m02)
- Ayah anchors: 101:9 أمّه and هاوية (ء م م، ه و ي); no direct surface occurrence for ء م ه
- Synthesis: The mother sense and the origin-center sense converge on return. What first generates and gathers can also name the receiving destination, allowing the abyss to function as an inverted maternal center.

#### Subchannel B. Nurturer, Nest, and Available Provision
- Reading type: latent/lexical
- Scene or process: A caregiver prepares an enclosure and keeps the food or means of life immediately available within it.
- Active motifs: feeding and rearing (ء م م:B001/m02); prepared nest or dwelling (ف ر ش:B002/m02); present and accessible provision (ع ه ن:B001/m01); means of livelihood (ع ي ش:B002/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 العهن (ع ه ن); 101:7 عيشة (ع ي ش); 101:9 أمّه (ء م م)
- Synthesis: Care is spatial as well as social. The nurturer lays out a protected place, places sustenance within reach, and turns the enclosure into a functioning habitat rather than a passive container.

#### Subchannel C. Womb, Pregnancy, and Breeding
- Reading type: latent/lexical
- Scene or process: Reproduction joins the breeding male, the receptive womb, its internal vessels, and the burden of gestation.
- Active motifs: breeding or mounting by a male (ق ر ع:B003/m01); womb vessels or womb-place (ع ه ن:B005/m01); pregnancy as carried weight (ث ق ل:B007/m01); protected breeding camel (ح م ي:B005/m01); young livestock (ف ر ش:B004/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:5 العهن (ع ه ن); 101:6 ثقلت (ث ق ل); 101:11 حامية (ح م ي)
- Synthesis: The scene follows generation from mating to gestation. The male's reproductive action meets the womb's internal structure, pregnancy converts conception into sustained weight, and the livestock frame carries the process toward offspring.

#### Subchannel D. Receptacle, Spread Surface, and Release
- Reading type: latent/lexical
- Scene or process: A vessel gathers material, opens onto a laid surface, and releases its contents into distribution.
- Active motifs: sack or collecting receptacle (ق ر ع:B012/m01); gathering center (ء م م:B002/m02); laying out a surface (ف ر ش:B001/m01); spreading stored contents (ب ث ث:B001/m02)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش and مبثوث (ف ر ش، ب ث ث); 101:9 أمّه (ء م م)
- Synthesis: Containment and dispersal form a single mechanism. Material first acquires a center in the vessel, then the vessel is opened over a prepared surface and its contents cease to be a compact store.

### 6. Orientation Through Leaders, Marks, and Aims
- Semantic invariant: A selected center or standard organizes direction, alignment, imitation, destination, and responsible action.
- Surface relation: indirect; 101:1-3 القارعة (ق ر ع), 101:3,10 أَدْرَىٰ (د ر ي), 101:5 الجبال (ج ب ل), and 101:9 أمّه (ء م م) carry the roots whose latent senses form the directional frame.
- Surprising reach: A leader can function like a road marker, guide-line, construction standard, chosen lot, or steward of measured resources.

#### Subchannel A. Leader, Exemplar, and Beacon
- Reading type: latent/lexical
- Scene or process: A selected leader stands visibly ahead, is followed as a model, and marks the route for others.
- Active motifs: leader or exemplar (ء م م:B009/m01); selected chief or best member (ق ر ع:B007/m01); leaders and scholars as mountains (ج ب ل:B012/m01); beacon or route marker (ن و ر:B005/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:9 أمّه (ء م م); 101:11 نار (ن و ر)
- Synthesis: Selection, elevation, and visibility produce guidance. The chief is chosen from the group, stands with mountain-like prominence, and becomes a marker by which those behind can orient themselves.

#### Subchannel B. Guide-Line and Constructed Alignment
- Reading type: latent/lexical
- Scene or process: A line, board, or other standard is placed first so later work can be aligned and woven or built against it.
- Active motifs: guide-line or construction standard (ء م م:B009/m02); alignment between two things (و ز ن:B003/m01); skillful tight weaving (ج ب ل:B007/m01); visible road or house forecourt (ق ر ع:B010/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:6,8 موازينه (و ز ن); 101:9 أمّه (ء م م)
- Synthesis: Exemplarity becomes a material procedure. The first line or support establishes direction, comparison keeps each later element parallel, and the resulting fabric or structure inherits the standard's order.

#### Subchannel C. Aim, Lot, and Destination
- Reading type: latent/lexical
- Scene or process: Intention fixes a target, a lot selects among alternatives, and movement is directed toward the chosen place.
- Active motifs: intention and deliberate aim (ء م م:B012/m01); directing a projectile (ء م م:B012/m02); lot or apportioned choice (ق ر ع:B004/m01); seeking a target or place (د ر ي:B002/m01); place or position (ك و ن:B002/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:3,10 أَدْرَىٰ (د ر ي); 101:4-5 يكون/تكون (ك و ن); 101:9 أمّه (ء م م)
- Synthesis: Selection and intention converge on directed action. The lot identifies one possibility, the will adopts it as a target, and spatial position turns that abstract choice into a destination.

#### Subchannel D. Stewardship of Weighty Resources
- Reading type: latent/lexical
- Scene or process: A capable person is chosen to guard valuable property, judge its use, and answer for it.
- Active motifs: competent stewardship of wealth (ع ه ن:B007/m01); chosen chief (ق ر ع:B007/m01); precious or weighty property (ث ق ل:B005/m01); sound and settled judgment (و ز ن:B005/m01); sponsorship or responsibility (ك و ن:B003/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4-5 يكون/تكون (ك و ن); 101:5 العهن (ع ه ن); 101:6 ثقلت and موازينه (ث ق ل، و ز ن)
- Synthesis: Authority is defined by care rather than position alone. Valuable material requires a selected custodian whose judgment is steady and whose role makes him answerable for preservation and allocation.

### 7. Directed Pursuit and Rapid Passage
- Semantic invariant: Intention becomes motion through concealment, targeting, route choice, speed, encounter, and defensive response.
- Surface relation: indirect; 101:3,10 أَدْرَىٰ (د ر ي), 101:8 خفّت (خ ف ف), and 101:9 هاوية (ه و ي) anchor lexical senses of seeking, swift travel, casting, and descent.
- Surprising reach: The network moves from a hunter hidden behind a mount to raids, mountain entry, swooping flight, and a night-moving herd.

#### Subchannel A. Concealed Hunter and Skittish Prey
- Reading type: latent/lexical
- Scene or process: A hunter hides behind an animal, approaches without alarming prey, and casts or reaches at the decisive moment.
- Active motifs: concealment for hunting (د ر ي:B003/m01); tame animal or reassuring companion (ء ن س:B003/m02); skittish flight from approach (ن و ر:B006/m01); reaching or casting with hand or weapon (ه و ي:B003/m01); hoof or foot of the mount (خ ف ف:B006/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:8 خفّت (خ ف ف); 101:9 هاوية (ه و ي); 101:11 نار (ن و ر); no direct surface occurrence for ء ن س
- Synthesis: Pursuit depends on managing visibility and alarm. The mount masks the hunter, its familiar presence delays the prey's flight, and the concealed approach ends in a sudden cast or reach.

#### Subchannel B. Raid Toward a Defended Target
- Reading type: latent/lexical
- Scene or process: A party chooses a place, advances toward it as a raid, and meets protection or exclusion at the target.
- Active motifs: raid or hostile seeking (د ر ي:B002/m02); deliberate target (ء م م:B012/m01); place or position (ك و ن:B002/m01); taking a path (ف ر ش:B007/m02); defense and prevention of approach (ح م ي:B002/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:4 الفراش and يكون (ف ر ش، ك و ن); 101:5 تكون (ك و ن); 101:9 أمّه (ء م م); 101:11 حامية (ح م ي)
- Synthesis: The raid is a directed conflict scene rather than motion alone. Intention fixes the destination, the route carries the attackers toward it, and protection defines the target by controlling who may approach.

#### Subchannel C. Swift Travel, Swoop, and Mountain Entry
- Reading type: latent/lexical
- Scene or process: A traveler or animal moves rapidly, enters rough high terrain, and may descend or swoop with concentrated speed.
- Active motifs: rapid departure or travel (خ ف ف:B002/m01); swift animal motion (خ ف ف:B002/m02); fast descent, run, or swoop (ه و ي:B008/m01); entry into mountains (ج ب ل:B006/m01); hard stripped terrain (ق ر ع:B011/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:8 خفّت (خ ف ف); 101:9 هاوية (ه و ي)
- Synthesis: Speed is shaped by terrain. Light rapid movement carries the traveler into the mountains, while the swoop sense compresses distance vertically and the hard surface gives the passage a resistant ground.

#### Subchannel D. Processional Herd Through Night
- Reading type: latent/lexical
- Scene or process: Animals move one behind another through an extended night interval after dispersing from supervision.
- Active motifs: following camel procession (خ ف ف:B008/m01); livestock dispersing at night (ن ف ش:B003/m01); young herd animals (ف ر ش:B004/m01); extended night interval (ه و ي:B006/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 المنفوش (ن ف ش); 101:8 خفّت (خ ف ف); 101:9 هاوية (ه و ي)
- Synthesis: Dispersal and procession coexist: the herd leaves controlled pasture, yet its members preserve a serial relation as they travel through the night.

### 8. Rebalancing Relations Between Wills
- Semantic invariant: Social relations change when participants accept, negotiate, appease, correct, overcome, obey, or guarantee one another.
- Surface relation: direct; 101:7 راضية (ر ض و) supplies the acceptance pole, while 101:1-3 القارعة (ق ر ع) contributes latent contest, lot, and rebuke senses.
- Surprising reach: Satisfaction can become reciprocal settlement, corrective speech, rivalry, or legally answerable commitment.

#### Subchannel A. Acceptance and Satisfied Life
- Reading type: surface-primary
- Scene or process: Aversion ceases, acceptance settles, and the accepted condition becomes a satisfying mode of life.
- Active motifs: acceptance opposed to displeasure (ر ض و:B001/m01); abundant or sought satisfaction (ر ض و:B002/m01); accepted state (ر ض ي:B001/m01); condition of living (ع ي ش:B001/m02)
- Ayah anchors: 101:7 راضية and عيشة (ر ض و، ع ي ش); no direct surface occurrence for ر ض ي
- Synthesis: Satisfaction is both relation and condition. Acceptance removes resistance to what is given, and that settled relation becomes the quality of the life being lived.

#### Subchannel B. Reciprocal Agreement and Shared Lot
- Reading type: latent/lexical
- Scene or process: Members of a group allocate a matter, accept one another's share, and seal the arrangement by reciprocal undertaking.
- Active motifs: mutual satisfaction (ر ض و:B003/m01); drawing or allocating lots (ق ر ع:B004/m01); community joined by one matter (ء م م:B004/m01); reciprocal covenant (ء م ه:B005/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:7 راضية (ر ض و); 101:9 أمّه (ء م م); no direct surface occurrence for ء م ه
- Synthesis: The lot converts uncertainty into an allocation, but the social result depends on mutual acceptance. Community and covenant transform the selected share into a durable agreement.

#### Subchannel C. Placation, Correction, and Return
- Reading type: latent/lexical
- Scene or process: Displeasure is met by effortful appeasement and corrective speech until the hearer turns back or complies.
- Active motifs: seeking another's satisfaction (ر ض و:B004/m01); rebuke that causes retreat (ق ر ع:B006/m01); preparing or smoothing the way (ف ر ش:B001/m02); compliance and obedience (خ ف ف:B007/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:7 راضية (ر ض و); 101:8 خفّت (خ ف ف)
- Synthesis: Reconciliation has both verbal and spatial imagery. Rebuke interrupts the wrong course, appeasement removes resistance, and smoothing the way makes return and compliance possible.

#### Subchannel D. Rivalry and Overcoming
- Reading type: latent/lexical
- Scene or process: Two parties contest an issue, persist against one another, and end with one prevailing.
- Active motifs: armed or personal contest (ق ر ع:B002/m01); overcoming a rival (ر ض و:B005/m01); prevailing in contention (ر ض ي:B002/m01); mutual persistence in dispute (ه و ي:B009/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:7 راضية (ر ض و); 101:9 هاوية (ه و ي); no direct surface occurrence for ر ض ي
- Synthesis: The acceptance field reverses into competitive mastery. Mutual persistence holds the parties in conflict until contest resolves the relation by giving one will precedence.

#### Subchannel E. Obedience, Guarantee, and Responsibility
- Reading type: latent/lexical
- Scene or process: A participant accepts direction, stands surety for another, and assumes continuing responsibility.
- Active motifs: obedient relation (ر ض و:B006/m01); guarantor or surety (ر ض و:B006/m03); guarantee relation (ر ض ي:B004/m03); compliance (خ ف ف:B007/m01); sponsorship or responsibility (ك و ن:B003/m01)
- Ayah anchors: 101:4-5 يكون/تكون (ك و ن); 101:7 راضية (ر ض و); 101:8 خفّت (خ ف ف); no direct surface occurrence for ر ض ي
- Synthesis: Acceptance becomes obligation when it binds future action. Obedience aligns conduct with another's direction, while surety makes that alignment answerable on another person's behalf.

### 9. Heat, Light, and Inscribed Trace
- Semantic invariant: Thermal or luminous intensity changes bodies and surfaces by heating, revealing, marking, darkening, or leaving residue.
- Surface relation: direct; 101:11 نار حامية (ن و ر، ح م ي) unites flame with intensified heat.
- Surprising reach: Fire extends into perception, heated tools, venom, tattoo pigment, dark clouds, mud, and water traces.

#### Subchannel A. Flame and Intensified Heat
- Reading type: surface-primary
- Scene or process: A visible fire burns with increasing heat and transfers that heat to its surroundings or to worked material.
- Active motifs: flame or kindled fire (ن و ر:B002/m01); intense heat (ح م ي:B001/m01); heating iron or a tool (ح م ي:B001/m02); illumination produced by fire (ن و ر:B001/m01)
- Ayah anchors: 101:11 نار and حامية (ن و ر، ح م ي)
- Synthesis: Fire joins visibility and temperature in one source. Its light announces its presence, while its heat acts on bodies and materials beyond the flame itself.

#### Subchannel B. Illumination and Detection
- Reading type: mixed
- Scene or process: Light makes an object perceptible, after which sight or hearing becomes knowledge.
- Active motifs: illumination (ن و ر:B001/m01); visual detection (ء ن س:B002/m01); auditory detection (ء ن س:B002/m02); knowledge gained (د ر ي:B001/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:11 نار (ن و ر); no direct surface occurrence for ء ن س
- Synthesis: Illumination is the external condition for recognition, while sensing is the receiving operation. What appears or sounds is converted from signal into understood content.

#### Subchannel C. Point, Venom, and Pigmented Mark
- Reading type: latent/lexical
- Scene or process: A sharp point pierces a surface, introduces a heated substance or dark pigment, and leaves a visible bodily trace.
- Active motifs: pointed implement (د ر ي:B004/m01); heat of venom or sting (ح م ي:B007/m01); soot used after skin-pricking for tattoo or cosmetic mark (ن و ر:B008/m01); red flower image (ع ه ن:B009/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:5 العهن (ع ه ن); 101:11 نار and حامية (ن و ر، ح م ي)
- Synthesis: Penetration, heat, and color form an inscription mechanism. A point opens the skin, an active substance enters or is spread over it, and red or dark coloration makes the event persist as a mark.

#### Subchannel D. Darkened Medium and Residual Surface
- Reading type: latent/lexical
- Scene or process: Air, water, or earth becomes dark and dense, then leaves a visible deposit or dried trace on the surface.
- Active motifs: blackened night or cloud mass (ح م ي:B012/m01); black foul mud (ح م ي:B006/m01); dried trace after water recedes (ف ر ش:B009/m01); residual water or surface bubbles (ف ر ش:B009/m02)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:11 حامية (ح م ي)
- Synthesis: Obscuration is material as well as atmospheric. Darkness accumulates overhead, mud thickens below, and receding liquid records its former presence as a skin, residue, or bubble field.

### 10. Shell, Lining, Opening, and Void
- Semantic invariant: Bodies and places are organized by outer surfaces, supporting layers, bounded openings, and the empty spaces those boundaries contain.
- Surface relation: indirect; 101:5 الجبال (ج ب ل), 101:9 هاوية (ه و ي), and 101:1-3 القارعة (ق ر ع) anchor solidity, depth, surface exposure, and forecourt senses.
- Surprising reach: Mountain and abyss imagery extends into wells, skull plates, muscles, hoof edges, door courts, bald ground, and hollow interiors.

#### Subchannel A. Mountain Mass, Hard Substrate, and Well Lining
- Reading type: mixed
- Scene or process: A high solid mass becomes an unyielding ground, and large stones are arranged to preserve a hollow cut through it.
- Active motifs: high solid mountain mass (ج ب ل:B001/m01); hard substrate stopping excavation (ج ب ل:B005/m01); stone lining of a well (ح م ي:B011/m01); hard smooth surface (ق ر ع:B011/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:11 حامية (ح م ي)
- Synthesis: Solidity and hollow construction are complementary. The mountain-like substrate resists penetration, but once opened, a ring of stone converts that breach into a stable, usable depth.

#### Subchannel B. Bodily Plates, Muscle, and Hoof Edges
- Reading type: latent/lexical
- Scene or process: Thin hard layers and thicker soft components assemble into a supported bodily mechanism.
- Active motifs: thin cranial or bone plate (ف ر ش:B010/m01); thin metal or mechanical plate (ف ر ش:B010/m02); skin, scalp, or bone layer (ج ب ل:B003/m02); protruding calf muscle (ح م ي:B009/m01); paired sides of the hoof (ح م ي:B010/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 الجبال (ج ب ل); 101:11 حامية (ح م ي)
- Synthesis: The body is rendered as layered construction. Thin plates provide interface and protection, muscle supplies volume and motion, and paired hoof edges organize contact with the ground.

#### Subchannel C. Forecourt, Route, and Gaping Entrance
- Reading type: latent/lexical
- Scene or process: An exposed court opens onto a route, presents a visible entrance, and can be marked for approach.
- Active motifs: road or house forecourt (ق ر ع:B010/m01); taking a path (ف ر ش:B007/m02); gaping opening or hollow interior (ه و ي:B007/m01); visible route marker (ن و ر:B005/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:9 هاوية (ه و ي); 101:11 نار (ن و ر)
- Synthesis: The forecourt mediates outside and inside. The route reaches an exposed frontage, the opening admits passage into a hollow interior, and the marker keeps the approach legible.

#### Subchannel D. Bared Surface and Empty Interior
- Reading type: latent/lexical
- Scene or process: Covering disappears from head, land, enclosure, or heart, exposing a bare surface and the void behind it.
- Active motifs: baldness, denudation, or emptied enclosure (ق ر ع:B008/m01, ق ر ع:B008/m02); air or void (ه و ي:B001/m01); emptied heart without steadiness (ه و ي:B001/m02); dry stripped wood (ج ب ل:B008/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:5 الجبال (ج ب ل); 101:9 هاوية (ه و ي)
- Synthesis: Loss of covering produces both visual exposure and structural emptiness. Bald ground, dry wood, and the vacant interior share a movement from occupied or clothed form to uncovered void.

### 11. Human Collectivity, Nature, and Transmission
- Semantic invariant: Human identity is formed through bodily nature, membership in a collective, inherited practice, and the transmission of knowledge across a lifetime.
- Surface relation: indirect; 101:4 الناس, indexed under ن و س, supplies the human collective, while 101:5 الجبال (ج ب ل), 101:9 أمّه (ء م م), and 101:3,10 أَدْرَىٰ (د ر ي) anchor the latent formation and transmission senses.
- Surprising reach: A people can be mountain-like in number, a creed can function as a followed road, and an elder's remembered life can preserve non-written knowledge.

#### Subchannel A. Human Community and Multitude
- Reading type: mixed
- Scene or process: Individual humans become a named community whose scale ranges from a small group to a mountain-like multitude.
- Active motifs: human being or human collective (ء ن س:B001/m01); community joined by one matter (ء م م:B004/m01); great multitude (ج ب ل:B002/m01); few persons or reduced crowd (خ ف ف:B003/m01)
- Ayah anchors: 101:5 الجبال (ج ب ل); 101:8 خفّت (خ ف ف); 101:9 أمّه (ء م م); no direct surface occurrence for ء ن س, while الناس occurs at 101:4 under ن و س
- Synthesis: The scene moves between person, group, and scale. Shared affiliation turns humans into a community, while mountain abundance and numerical lightness describe expansion and contraction of that collective.

#### Subchannel B. Innate Nature and Human Form
- Reading type: latent/lexical
- Scene or process: A person begins from an unlearned natural condition and receives an embodied, proportioned constitution.
- Active motifs: innate disposition (ج ب ل:B004/m01); created nature (ج ب ل:B004/m02); primordial non-book condition (ء م م:B007/m02); balanced created form (و ز ن:B008/m01); bodily stature (ء م م:B006/m01)
- Ayah anchors: 101:5 الجبال (ج ب ل); 101:6,8 موازينه (و ز ن); 101:9 أمّه (ء م م)
- Synthesis: Human identity begins before acquired convention. Innate disposition supplies the pattern, measured creation gives it proportion, and stature makes that native constitution bodily visible.

#### Subchannel C. Creed as Followed Way
- Reading type: latent/lexical
- Scene or process: A community receives a creed or customary path, learns it, and follows an authoritative transmitter.
- Active motifs: creed or religious tradition (ء م م:B005/m01); followed way and obedience (ء م م:B005/m02); informing another (د ر ي:B001/m02); leader or exemplar (ء م م:B009/m01); reciprocal undertaking (ء م ه:B005/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:9 أمّه (ء م م); no direct surface occurrence for ء م ه
- Synthesis: Tradition is a directed social transmission. Knowledge is communicated, an exemplar embodies the path, and communal undertaking turns what is taught into a practice that can be followed.

#### Subchannel D. Elder, Memory, and Non-Written Transmission
- Reading type: latent/lexical
- Scene or process: An aged speaker looks back on earlier life and carries knowledge without relying on writing.
- Active motifs: elder defined by recollection of former youth (ك و ن:B005/m01); nonwriter or nonreader (ء م م:B007/m01); knowledge (د ر ي:B001/m01); informing another (د ر ي:B001/m02); extended lifetime (ي و م:B002/m01)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:4 يوم and يكون (ي و م، ك و ن); 101:5 تكون (ك و ن); 101:9 أمّه (ء م م)
- Synthesis: The elder's repeated “I was” turns elapsed life into testimony. Knowledge persists through memory and speech even where textual literacy is absent.

### 12. Conditions of Living and Provision
- Semantic invariant: Life takes shape through available resources, prepared habitation, protection, satisfaction, deprivation, or subordinate service.
- Surface relation: direct; 101:7 عيشة راضية (ع ي ش، ر ض و) names the fulfilled condition, while 101:4-5 يكون/تكون (ك و ن) supplies the broader field of states.
- Surprising reach: Provision connects with bedding and protection, while adverse condition extends into poverty, contempt, submission, and bonded status.

#### Subchannel A. Immediate Livelihood and Protected Habitat
- Reading type: latent/lexical
- Scene or process: Food and other means of living are kept ready inside a prepared and defended dwelling.
- Active motifs: present accessible provision (ع ه ن:B001/m01); livelihood and subsistence (ع ي ش:B002/m01); prepared bedding or household furnishing (ف ر ش:B002/m01); protection and exclusion of harm (ح م ي:B002/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 العهن (ع ه ن); 101:7 عيشة (ع ي ش); 101:11 حامية (ح م ي)
- Synthesis: Sustenance requires arrangement. Resources must be available, the dwelling must be fitted for use, and protection preserves both inhabitants and provisions from interruption.

#### Subchannel B. Blessed and Satisfying Life
- Reading type: mixed
- Scene or process: A favorable condition supplies the goods of life and is received with settled satisfaction.
- Active motifs: blessing or good condition (ء م م:B010/m01); life and living condition (ع ي ش:B001/m01, ع ي ش:B001/m02); abundant satisfaction (ر ض و:B002/m01)
- Ayah anchors: 101:7 عيشة and راضية (ع ي ش، ر ض و); 101:9 أمّه (ء م م)
- Synthesis: Well-being joins circumstance and response. Blessing names the favorable state, life is its field of realization, and satisfaction is the participant's settled relation to it.

#### Subchannel C. Poverty, Adversity, and Diminished Standing
- Reading type: latent/lexical
- Scene or process: Material slackness becomes a bad condition in which a person or right is treated as small and negligible.
- Active motifs: slackness or poverty (ع ه ن:B002/m02); adverse condition (ك و ن:B006/m01); contempt or humiliation (خ ف ف:B005/m01); disregard of a right (خ ف ف:B005/m02); lowly or slight standing (ء م م:B013/m01)
- Ayah anchors: 101:4-5 يكون/تكون (ك و ن); 101:5 العهن (ع ه ن); 101:8 خفّت (خ ف ف); 101:9 أمّه (ء م م)
- Synthesis: Diminution moves from resources to status. Poverty weakens material capacity, adverse condition fixes that weakness as a mode of life, and contempt translates it into social devaluation.

#### Subchannel D. Submission and Bonded Service
- Reading type: latent/lexical
- Scene or process: A subordinate person yields, obeys direction, and occupies a socially dependent role.
- Active motifs: submission or abasement (ك و ن:B004/m01); obedience and compliance (خ ف ف:B007/m01); bondmaid or young female servant (ء م م:B014/m01); obedient relation (ر ض ي:B004/m01)
- Ayah anchors: 101:4-5 يكون/تكون (ك و ن); 101:8 خفّت (خ ف ف); 101:9 أمّه (ء م م); no direct surface occurrence for ر ض ي
- Synthesis: Subordination is expressed both as bodily yielding and durable social position. Compliance performs the relation, while bonded status makes it continuing rather than momentary.

### 13. Hidden Content Entering Knowledge or Speech
- Semantic invariant: What is concealed in an event, mind, or social relation becomes perceptible, communicable, disclosed, corrected, or distorted in utterance.
- Surface relation: direct; 101:3 and 101:10 أَدْرَىٰ (د ر ي) foreground knowing, while 101:1-3 القارعة (ق ر ع) supplies a latent signal or rebuke that reaches a hearer.
- Surprising reach: Disclosure ranges from sensed alarm and reported news to poured-out grief, slander, rebuke, impaired hearing, and vacuous speech.

#### Subchannel A. Signal, Sensation, and Knowledge
- Reading type: mixed
- Scene or process: An external strike, light, sound, or felt alarm produces perception and becomes understood information.
- Active motifs: audible or felt knock (ق ر ع:B001/m01); visual detection (ء ن س:B002/m01); auditory detection (ء ن س:B002/m02); felt alarm (ء ن س:B002/m03); knowledge (د ر ي:B001/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:3,10 أَدْرَىٰ (د ر ي); no direct surface occurrence for ء ن س
- Synthesis: The hidden event first announces itself as impact or sensation. Perception receives the signal through sight, hearing, or inward alarm, and knowledge identifies what that signal means.

#### Subchannel B. Disclosure, Investigation, and Unrestrained Speech
- Reading type: latent/lexical
- Scene or process: Concealed information is brought out, examined, and then spread in speech without restraint.
- Active motifs: revealing news or a secret (ب ث ث:B002/m01); investigating and uncovering a matter (ب ث ث:B003/m01); unrestrained speech (ف ر ش:B012/m01); slanderous speech (ف ر ش:B012/m02); speech cast without deliberation (ع ه ن:B006/m01)
- Ayah anchors: 101:4 مبثوث and الفراش (ب ث ث، ف ر ش); 101:5 العهن (ع ه ن)
- Synthesis: Disclosure begins as the opening of something hidden, but its social trajectory depends on restraint. Investigation can clarify the matter; uncontrolled spreading can instead turn it into careless or harmful speech.

#### Subchannel C. Grief Poured Out to a Confidant
- Reading type: latent/lexical
- Scene or process: Internal grief is disclosed to a trusted companion whose presence removes isolation.
- Active motifs: pouring out grief and distress (ب ث ث:B002/m02); intimate or chosen companion (ء ن س:B006/m02); companionship that removes loneliness (ء ن س:B003/m01); inner self or psyche (ء ن س:B006/m01)
- Ayah anchors: 101:4 مبثوث (ب ث ث); no direct surface occurrence for ء ن س
- Synthesis: Broadcasting becomes intimate rather than public. What is compressed within the self is released in speech to a chosen listener, and companionship changes disclosure into relief from isolation.

#### Subchannel D. Rebuke, Hearing, and Sound Judgment
- Reading type: latent/lexical
- Scene or process: Corrective speech reaches a listener, overcomes impaired reception, and calls for a steady judgment and acknowledgment.
- Active motifs: rebuke that turns the hearer back (ق ر ع:B006/m01); impaired hearing (ث ق ل:B009/m01); settled and weighty judgment (و ز ن:B005/m01); acknowledgment (ء م ه:B002/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:6 ثقلت and موازينه (ث ق ل، و ز ن); no direct surface occurrence for ء م ه
- Synthesis: Correction succeeds only when forceful speech becomes heard and weighed. The rebuke breaks through resistance, judgment tests its truth, and acknowledgment completes the listener's return.

### 14. Plant Growth, Fiber, and Hollowing
- Semantic invariant: Organic materials move through growth, branching, fabrication, drying, loosening, and hollowing.
- Surface relation: indirect; 101:5 العهن المنفوش (ع ه ن، ن ف ش) supplies the fiber transformation, while 101:1-3 القارعة (ق ر ع) carries the latent gourd sense.
- Surprising reach: Palm anatomy, flowering plants, woven cloth, dry wood, gourd fruit, and empty speech share transformations of filled and hollow form.

#### Subchannel A. Blossom, Spreading Growth, and Palm Frond
- Reading type: latent/lexical
- Scene or process: A plant puts out visible bloom, spreads close to the ground, and organizes new growth around a central palm heart.
- Active motifs: flower or blossom (ن و ر:B004/m01); spreading crop or plant (ف ر ش:B008/m01); fronds near the palm heart (ع ه ن:B004/m01); base of the date cluster (ع ه ن:B010/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 العهن (ع ه ن); 101:11 نار (ن و ر)
- Synthesis: Growth moves outward from a center. The cluster base and inner fronds define plant architecture, spreading vegetation occupies the surrounding surface, and blossom makes maturation visible.

#### Subchannel B. Weave, Wool, and Fiber Release
- Reading type: latent/lexical
- Scene or process: Organic fiber is gathered into a tight fabric and can later be teased back into loose strands.
- Active motifs: dyed wool (ع ه ن:B003/m01); skilled tight weaving (ج ب ل:B007/m01); laying fiber or cloth out (ف ر ش:B001/m01); carding wool apart (ن ف ش:B001/m01)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 الجبال, العهن, and المنفوش (ج ب ل، ع ه ن، ن ف ش)
- Synthesis: Fabrication and dissolution are inverse operations on the same material. Weaving gathers and tensions fibers into structure; laying out and carding release that structure into a spread mass.

#### Subchannel C. Gourd, Dry Wood, and Withering
- Reading type: latent/lexical
- Scene or process: A fruit-bearing plant matures around a hollow form while surrounding wood or brush dries and loses vitality.
- Active motifs: gourd or squash fruit (ق ر ع:B009/m01); dry wood (ج ب ل:B008/m01); small brush or twigs (ف ر ش:B008/m02); black mud as growth medium (ح م ي:B006/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:5 الجبال (ج ب ل); 101:11 حامية (ح م ي)
- Synthesis: The plant scene contrasts retained fruit-form with environmental depletion. The gourd preserves a rounded hollow body as twigs and wood dry, while dark earth remains the material base from which growth arose.

#### Subchannel D. Hollow Fruit and Empty Utterance
- Reading type: latent/lexical
- Scene or process: A hollow plant-form becomes an analogy for speech that has shape and spread but lacks substantive content.
- Active motifs: gourd or hollow squash (ق ر ع:B009/m01); vain or nonsensical speech (ه و ي:B010/m01); speech thrown out without deliberation (ع ه ن:B006/m01); broadcasting an utterance (ب ث ث:B002/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 مبثوث (ب ث ث); 101:5 العهن (ع ه ن); 101:9 هاوية (ه و ي)
- Synthesis: Exterior form and interior content are pulled apart. The gourd supplies the image of a bounded hollow body, while careless or vain speech supplies verbal form that circulates without corresponding substance.

## Standalone Subchannels

### S1. Pupil, Reflected Figure, and Visual Defect
- Reading type: latent/lexical
- Scene or process: A human likeness appears in the dark center of the eye, while defect or obscuration disrupts that visual field.
- Active motifs: reflected human figure in the pupil (ء ن س:B005/m01); bodily defect (ء م م:B015/m01); blackening or dark clouding (ح م ي:B012/m01)
- Ayah anchors: 101:9 أمّه (ء م م); 101:11 حامية (ح م ي); no direct surface occurrence for ء ن س
- Synthesis: The pupil is both organ and image-bearing surface: it contains the tiny human figure seen by an observer. Defect and darkening alter that capacity to receive or display a visible form.

### S2. Woman Within Household Appraisal
- Reading type: latent/lexical
- Scene or process: A woman is located within household kinship and described through stature, bodily form, composure, and dependent status.
- Active motifs: short-statured woman (و ز ن:B006/m01); full-bodied woman and dignified composure (ث ق ل:B008/m01, ث ق ل:B008/m02); bondmaid or young female servant (ء م م:B014/m01); relatives by marriage (ح م ي:B004/m01)
- Ayah anchors: 101:6 ثقلت and موازينه (ث ق ل، و ز ن); 101:8 موازينه (و ز ن); 101:9 أمّه (ء م م); 101:11 حامية (ح م ي)
- Synthesis: Bodily appraisal and social placement meet in one household frame. Stature and composure describe visible presence, marriage kin define relational position, and bonded status marks dependence within that setting.

### S3. Named Mountain and Topographic Identity
- Reading type: latent/lexical
- Scene or process: A mountain becomes a proper name, a place of affiliation, and a fixed topographic reference.
- Active motifs: Radwa as mountain-name (ر ض و:B007/m01); the same name in the parallel root family (ر ض ي:B003/m01); high solid mountain (ج ب ل:B001/m01); alignment beside a mountain (و ز ن:B003/m01)
- Ayah anchors: 101:5 الجبال (ج ب ل); 101:6,8 موازينه (و ز ن); 101:7 راضية (ر ض و); no direct surface occurrence for ر ض ي
- Synthesis: Physical prominence becomes identity. The mountain's stable mass supports naming and affiliation, while alignment places persons or objects in relation to that named landmark.

### S4. Interrogative Choice and Adversative Turn
- Reading type: latent/lexical
- Scene or process: Discourse presents an alternative, interrupts it with a turn, and redirects the hearer toward knowledge.
- Active motifs: alternative interrogative (ء م م:B016/m01); adversative shift (ء م م:B016/m02); seeking or conveying knowledge (د ر ي:B001/m01, د ر ي:B001/m02)
- Ayah anchors: 101:3,10 أَدْرَىٰ (د ر ي); 101:9 أمّه (ء م م)
- Synthesis: The interrogative opens competing possibilities, while the adversative use rejects or redirects the first line of thought. Knowledge is the discourse goal toward which that turn points.

### S5. Palm Core, Frond, and Extremity Analogy
- Reading type: latent/lexical
- Scene or process: Plant parts arranged around a central palm core are mapped onto bodily or tool-like extremities.
- Active motifs: fronds beside the palm heart (ع ه ن:B004/m01); base of a date cluster (ع ه ن:B010/m01); fingertip or palm figure (ء ن س:B005/m02); thin plate or paired mechanical piece (ف ر ش:B010/m02)
- Ayah anchors: 101:4 الفراش (ف ر ش); 101:5 العهن (ع ه ن); no direct surface occurrence for ء ن س
- Synthesis: A central stalk with radiating fronds supplies a structural analogy for hand, finger, and thin paired components. Position and attachment, rather than shared substance, hold the comparison together.

### S6. Applied Lime and Stripped Surface
- Reading type: latent/lexical
- Scene or process: A coating is spread over a body or exterior surface, removes covering, and leaves the underlying plane smooth and exposed.
- Active motifs: applied depilatory lime (ن و ر:B009/m01); denuded or bald surface (ق ر ع:B008/m01); scraped smooth material (ق ر ع:B011/m01); spreading a layer (ف ر ش:B001/m01)
- Ayah anchors: 101:1-3 القارعة (ق ر ع); 101:4 الفراش (ف ر ش); 101:11 نار (ن و ر)
- Synthesis: Application and stripping form one surface-treatment sequence. A material is laid over the exterior, covering is removed, and the result is a newly exposed, smoothed plane.


