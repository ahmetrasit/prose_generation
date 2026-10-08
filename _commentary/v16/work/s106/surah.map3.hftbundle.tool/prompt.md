Surah: 106. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S106 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), earlier readers' channel review (channels.md) and activation hypotheses (hft.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not delegate, browse or inspect files; run only the command the header describes.

The channel review and the HFT records are proposals by earlier readers. Ignore their judgements: grades,
strength or confidence labels, reading types, words such as "surprising", "exploratory" or "latent", and every
statement of what a reading may or may not do. Make your own judgement from the surah's words, the dictionary
phrases and the Quran. Do not rediscover what they already assembled: start from their chains, test each one
against the dictionary phrases and the text, and join, extend, split or correct them. Where their wording
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
4. `## Not carried`. Each channel subchannel and each HFT record you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s106/surah.r2.hftbundle/text.md =====
# Surah 106

- 106:1 لِإِيلَٰفِ قُرَيْشٍ
- 106:2 إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ
- 106:3 فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- 106:4 ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ


===== _commentary/v16/work/s106/surah.r2.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ل ف (root_000045): 106:1 لِإِيلَٰفِ, 106:2 إِۦلَٰفِهِمْ

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

## ر ح ل (root_000551): 106:2 رِحْلَةَ

- **B001** yolculuk etmek — yolculuk edip gitmek · yola çıkıp ilerlemek · acele etmeden yola çıkmak · yolculuğa çıkma · yolculukta yönelinen yer · yola çıkıp ilerleme
  أصل واحد يدل على مضي في سفر (maqayis)؛ ارتحل البعير رحلة أي سار فمضى (ayn)؛ أردت الرحلة إلى موضع أي الارتحال (jamhara)؛ رحل فلان وارتحل وترحل بمعنى والاسم الرحيل (sihah)؛ الرحلة اسم ارتحال القوم للمسير (tahdhib)؛ الرحلة الارتحال (mufradat)
- **B002** deve binek takımı — deveye bağlanan binek takımı · deriden yapılmış eyer benzeri binek · eyer benzeri deri binekler
  الرحالة السرج (maqayis)؛ الراحلة المركب من الإبل (ayn)؛ الرحل معروف رحل البعير (jamhara)؛ الرحل أيضا رحل البعير وهو أصغر من القتب (sihah)؛ الرحل مركب للبعير والرحالة نحوه (tahdhib)؛ الرحل ما يوضع على البعير للركوب (mufradat)
- **B003** deveye binek takımını bağlamak [kalıp] — deveye binek takımını koyup bağlamak · devenin sırtına binek takımını koymak
  رحلت بعيري أرحله رحلا (ayn)؛ رحلت البعير أرحله رحلا أي جعلت عليه رحلا (jamhara)؛ رحلت البعير أرحله رحلا إذا شددت على ظهره الرحل (sihah)؛ رحلت البعير أرحله رحلا إذا شددت عليه الرحل (tahdhib)؛ أرحلت البعير وضعت عليه الرحل (mufradat)
- **B004** kişinin evi ve ev eşyası — kişinin evi, barınağı ve ev eşyası
  هذا رحل الرجل لمنزله ومأواه (maqayis)؛ رحل الرجل منزله ومسكنه (ayn)؛ رحل الرجل منزله (jamhara)؛ الرحل مسكن الرجل وما يستصحبه من الاثاث (sihah)؛ الرحل في غير هذا منزل الرجل ومسكنه وبيته (tahdhib)؛ يعبر به عما يجلس عليه في المنزل وجمعه رحال (mufradat)
- **B005** yolculuğa uygun güçlü deve — yolculuğa uygun seçkin deve · binilip yolculuk edilebilen deve · yolculukta binilecek hayvan · binek takımını ve yolculuğu taşıyacak güçlü erkek deve · yolda ilerlemeye dayanıklı güçlü dişi deve · develerin zayıflıktan sonra güçlenip yolculuğa dayanması · çok sayıda binek devesi olan kişi · şişman veya güçlü, yolculuğa uygun deve
  الراحلة المركب من الإبل ذكرا كان أو أنثى وأرحلت الإبل سمنت بعد هزال فأطاقت الرحلة (maqayis)؛ بعير رحيل إذا كان قويا على حمل الرحل (jamhara)؛ الراحلة الناقة التي تصلح لأن ترحل وكذلك الرحول (sihah)؛ الراحلة كل بعير نجيب جواد سواء كان ذكرا أو أنثى (tahdhib)؛ الراحلة البعير الذي يصلح للارتحال (mufradat)
- **B006** yolculuk durağı veya yol aşaması — yolculuk durağı veya iki durak arasındaki aşama · yolcunun geçici olarak konakladığı yer
  قد يكون المرتحل اسم الموضع الذي تحل فيه (ayn)؛ المرحلة الموضع الذي تنزل به من حيث ترتحل (jamhara)؛ المرحلة واحدة المراحل بينه وبين كذا مرحلة (sihah)؛ المرحلة المنزل يرتحل منها وما بين المنزلين مرحلة (tahdhib)
- **B007** birini yerinden göndermek — birini yerinden gönderip uzaklaştırmak · birini bulunduğu yerden çıkarıp göndermek
  رحله إذا أظعنه من مكانه (maqayis)؛ رحلته بالتشديد إذا أظعنته من مكانه وأرسلته (sihah)؛ الترحيل والإرحال بمعنى الإشخاص والإزعاج (tahdhib)؛ رحلته أظعنته أي أزلته عن مكانه (mufradat)
- **B008** yolculuğa yardım edip binek sağlamak — birinin yolculuğuna yardım etmek · birine yolculuk için binek vermek · kendisinden yolculuk için binek sağlamasını istemek
  راحل فلان فلانا إذا عاونه على رحلته وأرحله أعطاه راحلة (maqayis)؛ راحلت فلانا إذا عاونته على رحلته وأرحلته إذا أعطيته راحلة واسترحله أي سأله أن يرحل له (sihah)؛ أرحلته أنا (tahdhib)؛ راحله عاونه على رحلته (mufradat)
- **B009** birini binek gibi kullanmak veya eziyetine dayanmak — birine hoşlanmadığı şeyi yüklemek · onun eziyetine sabretmek · birinin sırtına çıkıp onu binek gibi kullanmak
  يرحل فلانا بما يكره (maqayis)؛ رحلته بمكروه أرحله أي ركبته بها (ayn)؛ رحلت له نفسي إذا صبرت على أذاه (sihah)؛ رحلت فلانا بسيفي إذا علوته وارتحل فلان فلانا إذا علا ظهره وركبه (tahdhib)
- **B010** binek takımı desenli dokuma — binek takımı resimleriyle desenlenmiş kumaş veya üstlük · desenli dokuma yaygılar
  المرحل ضرب من برود اليمن وتكون عليه صور الرحال والرحال الطنافس الحيرية (maqayis)؛ المرحل ضرب من برود اليمن لأن عليه تصاوير رحل (ayn)؛ الرحال أيضا الطنافس الحيرية ومرط مرحل إزار خز فيه علم (sihah)؛ المرحل ضرب من برود اليمن لما عليه من تصاوير الرحل (tahdhib)؛ المرحل برد عليه صورة الرحال (mufradat)
- **B011** sırtı farklı renkli hayvan — sırtı veya binek yeri gövdesinden farklı renkli hayvan · sırt bölgesi gövdesinden farklı renkli koyun
  لما ابيض ظهره من الدواب أرحل (maqayis)؛ فرس أرحل إذا كان في موضع ملبده بياض من البلق (jamhara)؛ الأرحل من الخيل الأبيض الظهر ومن الغنم الأسود الظهر والرحلاء من الشاء (sihah)؛ إذا كان الفرس أبيض الظهر فهو أرحل (tahdhib)
- **B012** kalıplaşmış dolaylı iffetsizlik suçlaması [kalıp] — kişinin annesine yönelik kalıplaşmış dolaylı iffetsizlik suçlaması
  في القذف يا ابن ملقى أرحل الركبان (maqayis)؛ تقذف أحدهم وتكني فتقول يا ابن ملقى أرحل الركبان (ayn)؛ منه قولهم في القذف يا ابن ملقى أرحل الركبان (sihah)؛ العرب تكني عن القذف للرجل بقولهم يا ابن ملقى أرحل الركبان (tahdhib)

## ش ت و (root_000776): 106:2 ٱلشِّتَآءِ

- **B001** kış dönemi — kış · bir kış; tek bir kış dönemi · kışlar · kışlık; kışa ait · kışın ilk yarısı · kış günü
  الشتاء خلاف الصيف (maqayis)؛ الشتاء معروف والواحدة شتوة (ayn;tahdhib)؛ الشتاء معروف، هو جمع شتوة، وجمع الشتاء أشتية (sihah)؛ رحلة الشتاء والصيف (mufradat)؛ جعلوا الشتاء نصفين فالشتوي أوله والربيع آخره (tahdhib)
- **B002** kışa girme, kışlama ve kışlak — kışlamak; kışı geçirmek · topluluk kışa girdi · kış onları bastırdı; kışa yakalandılar · belirli bir yerde kışı geçirdim · belirli bir yerde kışladım · kışlak; kışlama yeri, zamanı veya eylemi · kışlak; kışlama yeri, zamanı veya eylemi · o bölgede kışı geçirdik · o bölgeyi kışın otlattık · kışlaklarımız; kışın kaldığımız yerler
  الموضع المشتاة والمشتى (maqayis;ayn;tahdhib)؛ الفعل شتا يشتو (ayn;tahdhib)؛ أشتى القوم إذا دخلوا في الشتاء وشتوا إذا أصابهم الشتاء (maqayis)؛ شتوت بموضع كذا وتشتيت أقمت به الشتاء (sihah)؛ المشتى والمشتاة للوقت والموضع والمصدر (mufradat)؛ شتونا بالصمان وشتينا الصمان وهذه مشاتينا ومصايفنا ومرابعنا (tahdhib)
- **B003** kış yağmuru — kış yağmuru · kış yağmuru
  الشتى على فعيل والشتوى مطر الشتاء (sihah)؛ الشتي المطر الذي يقع في الشتاء (tahdhib)
- **B004** kıtlık ve açlığa uğrama — kıtlık; açlık · kıtlığa uğramış, açlık çeken insanlar · topluluk kıtlığa uğradı
  العرب تسمي القحط شتاء؛ أراد بالشتاء المجاعة؛ الناس إذ ذاك مرملون مشتون؛ أشتى القوم فهم مشتون إذا أصابتهم مجاعة (tahdhib)
- **B005** engebeli veya sert yer ya da vadinin başı — engebeli veya sert yer · vadinin başı
  الشتا الموضع الخشن؛ الشتا صدر الوادي (tahdhib)

## ص ي ف (root_000899): 106:2 وَٱلصَّيْفِ

- **B001** yaz mevsimi ve yaza özgülük — yaz; ilkbahardan sonra gelen ve kışın karşısında duran mevsim · yaz günü ve yaz gecesi; yaza veya yaz sıcağına bağlı gün ve gece · yazlık; yaza ait veya yaz döneminde gerçekleşen
  الصيف وهو الزمان بعد الربيع الآخر (maqayis)؛ الصيف ربع من أرباع السنة (ayn;tahdhib)؛ الصيف واحد فصول السنة (sihah)؛ الصيف الفصل المقابل للشتاء (mufradat)؛ يوم صائف وليلة صائفة (maqayis;ayn;sihah)
- **B002** yaz yağmuru ve onunla yetişen ot — yazın ya da ilkbaharın ardından yağan yağmur · tek bir yaz yağmuru; bol bir yaz sağanağı · yaz yağmuru veya yazın yetişen ot ve bitki · topluluğun yaz yağmuruna kavuşması; yaz yağmuruna kavuştuk · toprağa yaz yağmuru yağması ve toprağın bu yağmurdan etkilenmesi
  المطر الذي يأتي فيه الصَّيف (maqayis)؛ الصَّيف المطر الذي يجيء بعد الربيع (ayn)؛ الصَّيف أيضا المطر الذي يجئ في الصَّيف (sihah)؛ الكلأ الذي ينبت في الصَّيف صيفي وكذلك المطر (tahdhib)؛ سمي المطر الآتي في الصَّيف صيفا (mufradat)
- **B003** yazı bir yerde geçirme, yaza girme ve yaza bağlı yer ya da faaliyet — yazı bir yerde geçirmek; yazlamak · yazlamak veya yazı geçirmek için bir yer tutmak · yaz mevsimine girmek · yazın kalınan yer; yazlık konaklama yeri · yaz dönemine bağlı işlem veya kiralama · yazın yapılan askerî sefer · topluluğun yazlık erzağı veya geçimliği · bu şeyin yazlık ihtiyacımı karşılaması
  عاملته مصايفة أي زمان الصَّيف (maqayis)؛ صاف القوم في مصيفهم إذا أقاموا في مكان صيفتهم (ayn)؛ غزوة صائفة (ayn;sihah;tahdhib)؛ صاف بالمكان أي أقام به الصَّيف واصطاف مثله والموضع مصيف ومصطاف (sihah)؛ صائفة القوم ميرتهم في الصَّيف (sihah)؛ صافوا حصلوا في الصَّيف وأصافوا دخلوا فيه (mufradat)؛ استأجرته مصايفة (tahdhib)
- **B004** babanın ileri yaşında doğan çocuk ve bu doğum — babanın ileri yaşında doğan çocuklar veya bunlardan biri · bir erkeğin ileri yaşta çocuk sahibi olması
  الصيفيون أولاد الرجل بعد كبره (maqayis)؛ أصاف الرجل أي ولد له على الكبر وولده صيفي (sihah)؛ أصاف الرجل فهو مصيف إذا ولد له بعدما يسن وولده صيفيون (tahdhib)
- **B005** bir şeyden sapma veya onu başka yöne çevirme — bir şeyden sapmak veya yönünü ondan çevirmek · okun hedeften sapması · okun hedef çizgisinden sapması ve bu sapma · eğri bir su yatağı · Tanrı'nın birinin kötülüğünü benden uzaklaştırması
  صاف عن الشيء إذا عدل عنه (maqayis)؛ صاف السهم عن الهدف يصيف صيفا إذا مال (maqayis)؛ الصيفوفة ميل السهم عن الرمية وصاف يصيف (ayn)؛ المصيف المعوج من مجاري الماء وأصله من صاف أي عدل (sihah)؛ أصاف الله عني شر فلان أي صرفه وعدل به (sihah)؛ صاف السهم عن الغرض يصيف إذا عدل عنه (tahdhib)
- **B006** fırsatı kaçırmayı ve tamamlanmayı anlatan, yaz sözcüklü iki kalıplaşmış söz — Fırsatı zamanında değerlendirmedin. · Baharın tamamlayıcısı yazdır; iş böylece eksiksiz biter.
  الصَّيف ضيعت اللبن؛ تمام الربيع الصَّيف

## ع ب د (root_000973): 106:3 فَلْيَعْبُدُوا۟

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

## ر ب ب (root_000532): 106:3 رَبَّ

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

## ECHO ر ب و (root_000537): for 106:3 رَبَّ: withheld observed target; not identity

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

## ب ي ت (root_000166): 106:3 ٱلْبَيْتِ

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

## ط ع م (root_000934): 106:4 أَطْعَمَهُم

- **B001** tatma, yeme ve yenilen besin — tat, lezzet · yemek veya tadına bakmak · yiyecek, besin · özellikle buğday · tadına bakma ve iştahını yoklama · doyuran ve besleyen yiyecek ya da su · yeme isteği veya iştah çekici şey · çok yiyen, obur
  أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)
- **B002** başkasını beslemek veya beslenmeyi istemek — yiyecek vermek, doyurmak · kendisini doyurmasını istemek
  الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)
- **B003** söz istemek veya takılan imama söz vermek [kalıp] — benden konuşmamı istedi · imam okuyuşta takılırsa sözü hatırlatın
  استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)
- **B004** geçim, bol ikram ve tahsis edilmiş gelir — geçimi yerinde · rızkı açık, kazançlı · çok ikram eden · geçim veya kazanç kaynağı · kazancı temiz veya kötü · araziyi birine geçim payı olarak ayırdı
  رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)
- **B005** olgunlaşıp tat kazanmak [kalıp] — ağacın meyvesi olgunlaşıp tat kazandı · tulumda hoş tat kazanmış süt
  للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)
- **B006** avı kazandıran araç, uzuv veya kişi — av getiren yay · avcı kuşun öndeki kalın parmağı · avdan yana talihli, avı bol
  قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)
- **B007** ilikte yağı beliren, biraz semiz hayvan — iliğinde yağ bulunan deve · biraz semiz, orta yağlı
  المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)
- **B008** akıl, değer ve düzelmeye açıklık niteliği [kalıp] — akıllı ve sağlam yargılı · aklı, devinimi veya değeri yok · terbiye kabul etmez, uslanmaz
  ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)
- **B009** atın ağız bölümü ve koşma talebi — atın burun altı ve dudak çevresi · attan koşmasını istedi
  مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)
- **B010** eklenen şeyin tutması [kalıp] — dala aşı yaptı ve aşı tuttu · gözüne küçük bir yabancı cisim girdi
  أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)
- **B011** gücü yetmek [kalıp] — ona gücü yetti
  الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)
- **B012** boğazından yakalayıp sıkmak [kalıp] — boğazından yakalayıp sıktı
  أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)
- **B013** ağız ağıza temas etmek — ağız ağıza temas etme
  التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)
- **B014** oluşumu ardışık olmak [kalıp] — oluşumu birbirini izleyen bölümlerden kurulu
  متطاعم الخلق أي متتابع الخلق (tahdhib)

## ج و ع (root_000278): 106:4 جُوعٍ

- **B001** midenin boş kalmasından doğan açlık — açlık · acıkmak · aç kimse · aç kadın · çok aç kimse · aç kadın · aç kimseler · açlar · bir kez açlık çekme · sürekli aç görünen ya da sık sık azar azar yiyen kimse
  الجوع ضد الشبع (maqayis;jamhara;sihah)؛ الجوع اسم جامع للمخمصة (ayn)؛ الجوع اسم للمخمصة (tahdhib)؛ الألم الذي ينال الحيوان من خلو المعدة من الطعام (mufradat)؛ الجوعة المرة من الجوع (jamhara;sihah;tahdhib)؛ المستجيع الذي يأكل كل ساعة الشيء بعد الشيء (tahdhib)
- **B002** yaygın açlık dönemi — yaygın açlık dönemi · açlık yılı
  عام مجاعة ومجوعة (maqayis;sihah)؛ المجاعة عام فيه جوع (ayn;tahdhib)؛ المجاعة عبارة عن زمان الجدب (mufradat)
- **B003** aç bırakma ya da bilerek aç kalma — onu aç bıraktı · onu aç bıraktı · başkasını aç bırakma · birini aç bırakma · bilerek aç kalmak · sağaltım için doyuncaya kadar yememek
  أجعته وجوعته فجاع يجوع (ayn;tahdhib)؛ المتعدي الإجاعة والتجويع (ayn)؛ أجاعه وجوعه (sihah)؛ تجوع أي تعمد الجوع (sihah)؛ تجوع للدواء أي لا تستوف الطعام (tahdhib)
- **B004** yapıya göre özlem, kap boşluğu ya da karın inceliği [kalıp] — seninle buluşmayı çok özledim · kabı dolu değil · karnı ince kadın
  جعت إلى لقائك وعطشت إلى لقائك؛ جائع القدر إذا لم تكن قدره ملأى؛ امرأة جائعة الوشاح إذا كانت ضامرة البطن

## ء م ن (root_000054): 106:4 وَءَامَنَهُم

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## خ و ف (root_000447): 106:4 خَوْفٍۭ

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



===== _commentary/v16/work/s106/surah.r2.hftbundle/channels.md =====
(source: latent_activation/network/v3/reviews/s106/reader_a_pilot.md)

# S106 Semantic Channel Discovery

## Parent Channels

### 1. Seasonal Mobility and Settlement
- Semantic invariant: Repeated travel becomes an organized cycle through seasonal timing, equipment, staged lodging, attachment to place, and interruption of passage.
- Surface relation: direct; 106:1-2 centers إِيلَٰفِ قُرَيْشٍ and إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ.
- Surprising reach: The journey frame extends from customary attachment to domestication, forced removal, failed mounts, and saddle-shaped visual signs.

#### Subchannel A. The Accustomed Seasonal Itinerary
- Reading type: mixed
- Scene or process: A recurring winter-and-summer route becomes familiar to its travelers and part of an established communal rhythm.
- Active motifs: familiar attachment `ء ل ف:B005/m01`; domesticated familiarity `ء ل ف:B005/m02`; departure and travel `ر ح ل:B001/m01`; winter season `ش ت و:B001/m01`; summer season `ص ي ف:B001/m01`; summer as a deadline of neglect or fulfilled need `ص ي ف:B006/m01`
- Ayah anchors: 106:1 إِيلَٰفِ; 106:2 إِۦلَٰفِهِمْ, رِحْلَةَ, ٱلشِّتَآءِ, ٱلصَّيْفِ
- Synthesis: Repetition turns departure into an accustomed itinerary: people, places, and even domestic creatures can become familiar through continued association. Winter and summer mark the route's alternating phases, while the summer proverb recasts the season as the point when preparation either bears fruit or proves neglected.

#### Subchannel B. Outfitting and Assisting the Journey
- Reading type: latent/lexical
- Scene or process: A traveler equips a capable animal, secures its saddle, and receives practical help for departure.
- Active motifs: camel saddle `ر ح ل:B002/m01`; saddling `ر ح ل:B003/m01`; strong journey mount `ر ح ل:B005/m01`; journey assistance or provision of a mount `ر ح ل:B008/m01`; reliable carrier `ء م ن:B001/m04`
- Ayah anchors: 106:2 رِحْلَةَ; 106:4 ءَامَنَهُم
- Synthesis: Mobility depends on a fitted saddle, the act of securing it, a mount able to bear the route, and aid that supplies or sustains that mount. Reliability extends the security root into the animal infrastructure of safe passage.

#### Subchannel C. Stages, Quarters, and Abiding
- Reading type: mixed
- Scene or process: Movement alternates with temporary stages, portable lodging, seasonal quarters, approach, and prolonged residence.
- Active motifs: lodging or home `ر ح ل:B004/m01`; carried household effects `ر ح ل:B004/m02`; stage between departures `ر ح ل:B006/m01`; entering or residing through winter `ش ت و:B002/m01`; winter quarters `ش ت و:B002/m02`; summer residence `ص ي ف:B003/m01`; abiding in place `ر ب ب:B007/m01`; persistence and duration `ر ب ب:B007/m02`; approach to a stopping place `ر ب ب:B007/m03`
- Ayah anchors: 106:2 رِحْلَةَ, ٱلشِّتَآءِ, ٱلصَّيْفِ; 106:3 رَبَّ
- Synthesis: The route is articulated by places where travelers approach, unload, remain, and later depart. Seasonal residence gives movement a durable rhythm, while portable effects allow a temporary station to function as a home.

#### Subchannel D. Forced and Broken Passage
- Reading type: latent/lexical
- Scene or process: A journey is disrupted when a person is displaced, burdened, or stranded by a failed or resistant mount.
- Active motifs: forced removal from place `ر ح ل:B007/m01`; harmful riding or imposed burden `ر ح ل:B009/m01`; mount failure and interrupted travel `ع ب د:B011/m01`; recalcitrant camel `ع ب د:B011/m02`
- Ayah anchors: 106:2 رِحْلَةَ; 106:3 فَلْيَعْبُدُوا۟
- Synthesis: The orderly itinerary reverses into involuntary movement or immobilization. Excess burden, an exhausted carrier, or a resisting animal breaks the relation between traveler, mount, and destination.

#### Subchannel E. Saddle Forms Beyond Riding
- Reading type: latent/lexical
- Scene or process: The visual outline of travel gear is transferred to textiles and animal coat markings.
- Active motifs: saddle-patterned cloth `ر ح ل:B010/m01`; saddle-shaped white marking `ر ح ل:B011/m01`
- Ayah anchors: 106:2 رِحْلَةَ
- Synthesis: The saddle becomes a recognizable form independent of its transport function. Its silhouette can organize woven ornament or name the contrasting patch on an animal's back where a rider would sit.

### 2. Provision, Scarcity, and Ecological Renewal
- Semantic invariant: Sustenance moves through seasonal work, acquisition, feeding, deprivation, rain-driven growth, preservation, hunting, and predation.
- Surface relation: direct; 106:2 names winter and summer, while 106:4 presents أَطْعَمَهُم مِّن جُوعٍ.
- Surprising reach: Food imagery expands into revenue, deliberate restraint, fertile weather, thickened materials, hunting instruments, and maritime command.

#### Subchannel A. Seasonal Earning and Distribution
- Reading type: mixed
- Scene or process: Seasonal activity generates livelihood and revenue that can be accumulated gradually and redistributed as food.
- Active motifs: summer work and provisioning `ص ي ف:B003/m02`; incremental acquisition `ق ر ش:B004/m01`; livelihood and provision `ط ع م:B004/m01`; income-producing estate or revenue `ط ع م:B004/m03`; feeding another `ط ع م:B002/m01`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:2 ٱلصَّيْفِ; 106:4 أَطْعَمَهُم
- Synthesis: Productive activity is timed to a season, gathered piece by piece, stabilized as livelihood or revenue, and completed socially when one person feeds another. Acquisition and distribution are consecutive phases of one provisioning process.

#### Subchannel B. Communal Famine and Relief
- Reading type: mixed
- Scene or process: Seasonal failure empties stomachs, widens into collective famine, and is answered by available food.
- Active motifs: food and nourishment `ط ع م:B001/m02`; empty-belly hunger `ج و ع:B001/m01`; communal famine `ج و ع:B002/m01`; imposed hunger `ج و ع:B003/m01`; winter famine `ش ت و:B004/m01`; famine-year gathering `ق ر ش:B003/m01`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:2 ٱلشِّتَآءِ; 106:4 أَطْعَمَهُم, جُوعٍ
- Synthesis: Hunger begins as bodily emptiness but can become a public condition in which a harsh year gathers people and livestock around dwindling resources. Feeding reverses that movement from environmental scarcity to bodily deprivation.

#### Subchannel C. Chosen Hunger and Figurative Emptiness
- Reading type: latent/lexical
- Scene or process: Hunger is voluntarily induced or projected onto longing, an unfilled vessel, and a slender body.
- Active motifs: deliberate therapeutic restraint `ج و ع:B003/m02`; hunger as longing for encounter `ج و ع:B004/m01`; empty pot `ج و ع:B004/m02`; slender abdomen `ج و ع:B004/m03`
- Ayah anchors: 106:4 جُوعٍ
- Synthesis: The hunger schema can be controlled for treatment, experienced as desire, recognized in an unfilled container, or read from bodily thinness. Absence of intake becomes a shared state across intention, emotion, vessel, and body.

#### Subchannel D. Rain, Water, Greenery, and Ripening
- Reading type: latent/lexical
- Scene or process: Seasonal rain gathers into water, sustains enduring vegetation, and brings fruit to flavor and maturity.
- Active motifs: winter rain `ش ت و:B003/m01`; summer rain `ص ي ف:B002/m01`; summer pasture produced by rain `ص ي ف:B002/m02`; layered raincloud `ر ب ب:B008/m01`; persistent plant-nurturing rain `ر ب ب:B008/m02`; abundant gathered water `ر ب ب:B013/m01`; evergreen plant `ر ب ب:B012/m01`; fruit ripening and bearing `ط ع م:B005/m01`
- Ayah anchors: 106:2 ٱلشِّتَآءِ, ٱلصَّيْفِ; 106:3 رَبَّ; 106:4 أَطْعَمَهُم
- Synthesis: Clouds accumulate, rain falls in its season, water gathers, vegetation remains green, and fruit acquires edible maturity. The scene links weather to nourishment through a continuous ecological sequence.

#### Subchannel E. Keeping, Concentrating, and Fattening Food
- Reading type: latent/lexical
- Scene or process: Food is held overnight, cooled or aged in a vessel, concentrated into a thick extract, and embodied as animal fat.
- Active motifs: one-night provision `ب ي ت:B005/m01`; overnight-kept liquid `ب ي ت:B006/m01`; thick syrup or residue `ر ب ب:B006/m01`; fattened livestock `ط ع م:B007/m01`; tasting `ط ع م:B001/m01`
- Ayah anchors: 106:3 ٱلْبَيْتِ, رَبَّ; 106:4 أَطْعَمَهُم
- Synthesis: Provision is not only acquired but temporally transformed. A night's keeping cools or settles liquids, concentration preserves edible substance, and accumulated nourishment becomes perceptible as flavor and animal fat.

#### Subchannel F. Hunting Instruments and Procurement
- Reading type: latent/lexical
- Scene or process: A bow, trained animal, or specialized bodily implement procures game for its owner.
- Active motifs: game-procuring bow `ط ع م:B006/m01`; trained hunting animal `ط ع م:B006/m02`; game-procuring finger `ط ع م:B006/m03`
- Ayah anchors: 106:4 أَطْعَمَهُم
- Synthesis: The food root names distinct hunting instruments by their common outcome: each brings game to its owner. Provision is realized through directed capture rather than cultivation or trade.

#### Subchannel G. Maritime Command and Predation
- Reading type: latent/lexical
- Scene or process: A prepared vessel crosses waters governed by a shipmaster while a dominant sea creature occupies the same environment.
- Active motifs: sea predator `ق ر ش:B005/m01`; shipmaster `ر ب ب:B017/m01`; tarred or coated ship `ع ب د:B005/m03`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:3 رَبَّ, فَلْيَعْبُدُوا۟
- Synthesis: Maritime passage combines command, a vessel made serviceable by coating, and a predator that dominates other sea creatures. Human control of the ship is set against animal dominance within the water itself.

### 3. Household Formation and Dependent Care
- Semantic invariant: A house gathers inhabitants, forms kin relations, receives dependents, and continues itself through marriage, guardianship, and new life.
- Surface relation: direct; 106:3 names رَبَّ هَٰذَا ٱلْبَيْتِ.
- Surprising reach: The dwelling extends to the grave, while household continuity includes stepchildren, late offspring, and a newly birthing ewe kept near home.

#### Subchannel A. Dwelling and Final Dwelling
- Reading type: mixed
- Scene or process: A house shelters the living and, by analogy, the grave houses the dead.
- Active motifs: dwelling and shelter `ب ي ت:B001/m01`; grave-house `ب ي ت:B007/m01`
- Ayah anchors: 106:3 ٱلْبَيْتِ
- Synthesis: The house is defined by shelter and inhabitation. The same spatial relation extends to the grave as the deceased person's final place of residence.

#### Subchannel B. Marriage, Household, and Stepchild
- Reading type: latent/lexical
- Scene or process: Marriage establishes a household whose membership can include children received from an earlier union.
- Active motifs: household members `ب ي ت:B002/m01`; marriage and household formation `ب ي ت:B010/m01`; foster child or stepchild `ر ب ب:B005/m01`
- Ayah anchors: 106:3 ٱلْبَيْتِ, رَبَّ
- Synthesis: Building a house with a spouse creates a social unit rather than only a structure. The stepchild motif expands that unit through incorporation and care rather than birth alone.

#### Subchannel C. Guardianship and New Life
- Reading type: latent/lexical
- Scene or process: A caregiver tends a dependent whose arrival may be late, recent, or marked by maternal residence near the house.
- Active motifs: caregiver, guardian, or nurse `ر ب ب:B005/m02`; child born in a parent's old age `ص ي ف:B004/m01`; newly birthing ewe kept home for milk `ر ب ب:B009/m01`; freshness and youth `ر ب ب:B009/m02`
- Ayah anchors: 106:2 ٱلصَّيْفِ; 106:3 رَبَّ
- Synthesis: Care links human guardianship with animal maternity. Late offspring and recent birth both renew the household, while remaining near home allows the dependent to be fed and protected.

### 4. Lordship, Service, and Relational Obligation
- Semantic invariant: Authority binds lord and worshipper, owner and dependent, teacher and learner, covenant partners, and entrusted parties.
- Surface relation: direct; 106:3 commands فَلْيَعْبُدُوا۟ رَبَّ, and 106:4 adds the security relation in ءَامَنَهُم.
- Surprising reach: The authority frame ranges from divine worship to chattel domination, progressive nurture, learned guidance, trusted deposits, and pledged protection.

#### Subchannel A. Divine Lordship and Worship
- Reading type: surface-primary
- Scene or process: Worshippers answer the sovereignty of the Lord with obedient, humbled devotion.
- Active motifs: divine Lordship `ر ب ب:B001/m01`; worship and submissive obedience `ع ب د:B003/m01`
- Ayah anchors: 106:3 فَلْيَعْبُدُوا۟, رَبَّ
- Synthesis: Lordship supplies the governing role and worship supplies the answering action. The relation is completed when recognized sovereignty becomes enacted obedience.

#### Subchannel B. Possession, Chattel Status, and Subjugation
- Reading type: latent/lexical
- Scene or process: A possessor claims authority over another person and can reduce that person to owned or compelled service.
- Active motifs: owner or master `ر ب ب:B001/m02`; possession relation `ذ و و:B001/m01`; chattel slavery `ع ب د:B001/m01`; enslaving or subjugating `ع ب د:B004/m01`
- Ayah anchors: 106:3 فَلْيَعْبُدُوا۟, رَبَّ, هَٰذَا
- Synthesis: Grammatical possession becomes a social relation when a master claims a dependent as property. The servitude root distinguishes the resulting status from the action that imposes it.

#### Subchannel C. Nurture, Completion, and Learned Guidance
- Reading type: latent/lexical
- Scene or process: A responsible authority raises a dependent gradually and cultivates knowledge through a learned guide.
- Active motifs: progressive raising and nurture `ر ب ب:B002/m02`; learned scholar or sage `ر ب ب:B003/m01`
- Ayah anchors: 106:3 رَبَّ
- Synthesis: Authority can operate through formation rather than coercion. The caregiver brings a dependent toward completion, while the learned figure cultivates understanding and disciplined relation to the Lord.

#### Subchannel D. Covenant, Trust, and Faith
- Reading type: mixed
- Scene or process: Parties enter protection through a pledge, entrust valued things, and answer reliable word with assent or faith.
- Active motifs: covenant and pledged protection `ر ب ب:B011/m01`; entrusted deposit and trust `ء م ن:B001/m03`; assent to a report or promise `ء م ن:B002/m01`; religious faith `ء م ن:B002/m02`; favor or beneficence `ر ب ب:B016/m03`
- Ayah anchors: 106:3 رَبَّ; 106:4 ءَامَنَهُم
- Synthesis: Covenant creates an obligation to protect, trust places something under another's care, and assent receives a word as reliable. Favor supplies the benevolent outcome of a relation governed by fidelity rather than force.

### 5. Security, Fear, and Loss
- Semantic invariant: Security is defined against anticipated harm, manufactured fear, visible alarm, competitive intimidation, and the erosion that leaves grief behind.
- Surface relation: direct; 106:4 places ءَامَنَهُم in explicit opposition to خَوْفٍ.
- Surprising reach: Fear moves from an inward expectation to a displayed state, a tactic of domination, and a process of gradual diminution.

#### Subchannel A. Granted Safety Against Apprehension
- Reading type: surface-primary
- Scene or process: An exposed community receives safety and safe conduct that quiet anticipated harm.
- Active motifs: secure calm `ء م ن:B001/m01`; granting safe conduct `ء م ن:B001/m02`; apprehensive fear `خ و ف:B001/m01`
- Ayah anchors: 106:4 ءَامَنَهُم, خَوْفٍ
- Synthesis: Fear projects a coming injury from its signs, while security removes that expectation and establishes protected movement or residence. Granting safety turns an inner state into a social guarantee.

#### Subchannel B. Producing, Displaying, and Contesting Fear
- Reading type: latent/lexical
- Scene or process: One party induces fear, the affected person visibly manifests it, and rivals struggle over who dominates or fears more.
- Active motifs: intimidation or caution through fear `خ و ف:B002/m01`; contest and dominance in fear `خ و ف:B003/m01`; visible fear `خ و ف:B005/m01`
- Ayah anchors: 106:4 خَوْفٍ
- Synthesis: Fear becomes an interaction rather than a private emotion. It can be deliberately produced as warning or coercion, read from the body, and used to rank opponents within a contest of dominance.

#### Subchannel C. Diminution and the Aftermath of Loss
- Reading type: latent/lexical
- Scene or process: Something is progressively taken away until its absence produces grief, regret, or wounded attachment.
- Active motifs: gradual diminution `خ و ف:B004/m01`; grief and regret after loss `ع ب د:B008/m02`
- Ayah anchors: 106:3 فَلْيَعْبُدُوا۟; 106:4 خَوْفٍ
- Synthesis: Threat is recast as attrition: the feared object is not struck once but reduced over time. The emotional aftermath appears as sorrow or regret when the diminished good is finally lost.

### 6. Assembly, Quantity, and Dispersion
- Semantic invariant: Separate elements can be joined into wholes, counted at scale, gathered as living or functional sets, or scattered again in multiple directions.
- Surface relation: indirect; 106:1-2 anchors the channel in إِيلَٰفِ and قُرَيْشٍ, while 106:3 contributes the collective senses of رَبَّ and فَلْيَعْبُدُوا۟.
- Surprising reach: Joining reaches from composition and communal gathering to thousands, allied masses, gambling arrows, herds, and dispersing roads.

#### Subchannel A. Joining and Dispersing Parts
- Reading type: latent/lexical
- Scene or process: Separate elements are drawn together into an integrated whole, while groups or routes can reverse that motion and scatter.
- Active motifs: joining after separation `ء ل ف:B002/m01`; gathering from different directions `ق ر ش:B001/m01`; groups or roads dispersing in every direction `ع ب د:B010/m01`
- Ayah anchors: 106:1 إِيلَٰفِ, قُرَيْشٍ; 106:2 إِۦلَٰفِهِمْ; 106:3 فَلْيَعْبُدُوا۟
- Synthesis: Gathering and joining converge on centripetal movement from plurality toward a whole. Dispersion supplies the structural reversal, sending a previously coherent set outward along divergent paths.

#### Subchannel B. Thousands, Multitudes, and Gathered Sets
- Reading type: latent/lexical
- Scene or process: Quantity becomes visible as a thousand, a massed community, a set of arrows, or a herd.
- Active motifs: thousand-count `ء ل ف:B001/m01`; multitudes and allied groups `ر ب ب:B004/m01`; gathered gambling arrows `ر ب ب:B010/m02`; animal herd `ر ب ب:B014/m01`
- Ayah anchors: 106:1 إِيلَٰفِ; 106:2 إِۦلَٰفِهِمْ; 106:3 رَبَّ
- Synthesis: Abstract number receives concrete collective forms. Human groups, bundled arrows, and herds each turn multiplicity into a bounded set that can be counted, moved, or acted upon as one.

### 7. Language, Reference, and Responsive Exchange
- Semantic invariant: Letters and composed lines become speech through reference, questioning, attention, response, prayer, and handoff.
- Surface relation: indirect; 106:1-2 supplies the ألف root, 106:3 contains هَٰذَا and بَيْتِ, and 106:4 contains ٱلَّذِىٓ and the أمن root.
- Surprising reach: Lexical imagery moves from alphabetic signs and metrical composition to deixis, relative linkage, ritual response, and an imperative of transfer.

#### Subchannel A. Letters and the Composed Line
- Reading type: latent/lexical
- Scene or process: Individual letters and ordered verbal parts are assembled into a bounded metrical line.
- Active motifs: letter alif `ء ل ف:B006/m01`; ordered composition of diverse parts `ء ل ف:B002/m02`; poetic line `ب ي ت:B003/m01`; letter ha `ه ا ء:B006/m01`
- Ayah anchors: 106:1 إِيلَٰفِ; 106:2 إِۦلَٰفِهِمْ; 106:3 هَٰذَا, بَيْتِ
- Synthesis: The alphabet supplies discrete signs, composition orders them, and the poetic house gathers words, sounds, and meanings under meter. The spatial image of a house thus becomes a textual unit.

#### Subchannel B. Deixis, Relation, and Inquiry
- Reading type: mixed
- Scene or process: A speaker directs attention, points to an entity, links a relative clause, or asks what is meant.
- Active motifs: relative linker `ذ و و:B002/m01`; demonstrative pointing `ذ و و:B003/m01`; interrogative "what" `ذ و و:B004/m01`; relative "what/that which" `ذ و و:B004/m02`; attention opener `ه ا ء:B002/m01`; interrogative substitute `ه ا ء:B004/m01`; grammatical particle `ر ب ب:B015/m01`
- Ayah anchors: 106:3 هَٰذَا, رَبَّ; 106:4 ٱلَّذِىٓ
- Synthesis: Attention and pointing establish a referent; relative forms attach further description; interrogation opens a slot for an unknown referent. The particles organize how speaker, listener, and mentioned entity are related in discourse.

#### Subchannel C. Prayer, Answer, and Handoff
- Reading type: latent/lexical
- Scene or process: A call or prayer receives a spoken answer, while an imperative accompanies the physical act of giving something to another.
- Active motifs: "Amen" as a request for response `ء م ن:B003/m01`; answer or call-response `ه ا ء:B003/m01`; offer and "take" imperative `ه ا ء:B001/m01`
- Ayah anchors: 106:3 هَٰذَا; 106:4 ءَامَنَهُم
- Synthesis: Prayer projects a desired answer, the response particle voices availability to a caller, and the handoff formula joins speech to transfer. In each case an utterance completes an exchange initiated by another party.

### 8. Material Integration, Repair, and Breach
- Semantic invariant: Materials and parts acquire form through joining, knotting, layering, coating, containment, collision, or forced entry.
- Surface relation: indirect; the participating roots occur in 106:1-4 through إِيلَٰفِ, رَبَّ, بَيْتِ, فَلْيَعْبُدُوا۟, أَطْعَمَهُم, خَوْفٍ, and قُرَيْشٍ.
- Surprising reach: The same structural field includes grafted branches, paved roads, leather containers, perfume equipment, interlocked spears, cracked bone, and an eye admitting a speck.

#### Subchannel A. Grafting, Knotting, and Successive Formation
- Reading type: latent/lexical
- Scene or process: A new element is accepted into a living stock, a knot holds joined parts, and form develops through successive continuity.
- Active motifs: accepted graft `ط ع م:B010/m01`; secure knot `ر ب ب:B016/m02`; successive formation `ط ع م:B014/m01`
- Ayah anchors: 106:3 رَبَّ; 106:4 أَطْعَمَهُم
- Synthesis: Integration can be organic, mechanical, or developmental. The graft survives because the host accepts the join, the knot preserves tension between parts, and successive formation extends continuity through time.

#### Subchannel B. Repairing, Smoothing, and Coating
- Reading type: latent/lexical
- Scene or process: A material is completed or made serviceable by repair, smoothing, paving, or treatment with a concentrated substance.
- Active motifs: repair and completion `ر ب ب:B002/m01`; treating material with thick residue `ر ب ب:B006/m02`; paved or smoothed road `ع ب د:B005/m01`; tar-coated animal `ع ب د:B005/m02`
- Ayah anchors: 106:3 رَبَّ, فَلْيَعْبُدُوا۟
- Synthesis: Repair restores a whole, coating protects or conditions a surface, and paving turns rough ground into a usable route. Each operation converts resistant material into a stable functional form.

#### Subchannel C. Specialized Receptacles
- Reading type: latent/lexical
- Scene or process: A container is shaped around the substance or instrument it must carry, hold, or heat.
- Active motifs: leather honey-gathering bag `خ و ف:B006/m01`; water-carrier's leather bag or garment `خ و ف:B006/m02`; leather arrow case `ر ب ب:B010/m01`; perfume brazier `ع ب د:B012/m01`
- Ayah anchors: 106:3 رَبَّ, فَلْيَعْبُدُوا۟; 106:4 خَوْفٍ
- Synthesis: Honey or water, arrows, and perfume each demand a specialized receptacle. The container's material and shape are determined by whether its contents must be transported, bundled, or heated.

#### Subchannel D. Collision, Fracture, and Forced Entry
- Reading type: latent/lexical
- Scene or process: Contact escalates from interlocking weapons to bodily compression, bone fracture, or a foreign particle entering the eye.
- Active motifs: interlocking spears `ق ر ش:B006/m01`; bone-cracking wound `ق ر ش:B008/m01`; throat grip and choking `ط ع م:B012/m01`; eye admitting a speck `ط ع م:B010/m02`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:4 أَطْعَمَهُم
- Synthesis: These motifs share a boundary under pressure. Spears occupy the same space, a grip compresses the throat, a blow breaches bone without crushing it, and a speck crosses the eye's surface.

### 9. Capacity, Judgment, and Controlled Motion
- Semantic invariant: Effective action depends on durable strength, available capacity, sound judgment, responsiveness to correction, and bodily control of motion.
- Surface relation: indirect; 106:2 contributes the travel setting, 106:3 the service root, and 106:4 the security and food roots.
- Surprising reach: The food root extends from physical ability to reason, value, teachability, the horse's mouth, and the cue that releases speed.

#### Subchannel A. Need, Ability, and Durable Readiness
- Reading type: latent/lexical
- Scene or process: A need is met by sufficient ability, bodily stoutness, and material durability.
- Active motifs: need `ر ب ب:B016/m01`; ability `ط ع م:B011/m01`; bodily strength or stoutness `ع ب د:B007/m01`; durable cloth or material `ع ب د:B007/m02`
- Ayah anchors: 106:3 رَبَّ, فَلْيَعْبُدُوا۟; 106:4 أَطْعَمَهُم
- Synthesis: Need defines the task, capacity makes action possible, bodily strength sustains exertion, and durable material withstands repeated use. Readiness appears as resistance to failure across person, animal, and object.

#### Subchannel B. Reason, Value, and Receptivity to Reform
- Reading type: latent/lexical
- Scene or process: A person is evaluated by judgment, effective vitality or worth, and the ability to receive correction.
- Active motifs: reason and practical judgment `ط ع م:B008/m01`; value or vitality `ط ع م:B008/m02`; receptivity to discipline and reform `ط ع م:B008/m03`
- Ayah anchors: 106:4 أَطْعَمَهُم
- Synthesis: Capacity is cognitive and ethical as well as physical. Sound judgment directs conduct, vitality gives action weight, and receptivity allows instruction to alter future behavior.

#### Subchannel C. Equine Cue and Acceleration
- Reading type: latent/lexical
- Scene or process: Contact at the horse's mouth becomes a cue for rapid forward motion with minimal delay.
- Active motifs: horse muzzle or lips `ط ع م:B009/m01`; urging a horse to run `ط ع م:B009/m02`; little delay `ع ب د:B009/m01`; swift running `ع ب د:B009/m02`
- Ayah anchors: 106:3 فَلْيَعْبُدُوا۟; 106:4 أَطْعَمَهُم
- Synthesis: The anatomical control point at the mouth is linked to the request for speed. A responsive animal converts the cue into acceleration, joining bodily interface, command, and rapid outcome.

### 10. Honor, Intrusion, and Communal Boundaries
- Semantic invariant: Communities define belonging through ancestry, titled status, hospitality, exclusion, reputation, accusation, and insult.
- Surface relation: indirect; 106:1 names قُرَيْشٍ, 106:2 names the journey, 106:3 the house and service relation, and 106:4 the act of feeding.
- Surprising reach: A named lineage opens into noble houses, honorifics, honored service, the uninvited eater, denunciation, and a saddle-based insult.

#### Subchannel A. Named Lineage and Honored Status
- Reading type: mixed
- Scene or process: A named community locates status in ancestry, a noble house, inherited titles, and public honor.
- Active motifs: Quraysh as tribe and lineage name `ق ر ش:B002/m01`; noble house and ancestry `ب ي ت:B008/m01`; titular attribution `ذ و و:B001/m02`; honored or revered person `ع ب د:B006/m01`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:3 فَلْيَعْبُدُوا۟, هَٰذَا, ٱلْبَيْتِ
- Synthesis: Tribal naming identifies communal descent, the noble house concentrates that descent into a status-bearing lineage, and titles make rank linguistically visible. Honor is completed when others treat the ranked person as one to be served or revered.

#### Subchannel B. Hospitality, Request, and the Interloper
- Reading type: latent/lexical
- Scene or process: A host's provision attracts a requester whose participation may cross the boundary into uninvited consumption.
- Active motifs: generous hospitality `ط ع م:B004/m02`; requesting food `ط ع م:B002/m02`; freeloader or interloper `ق ر ش:B009/m01`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:4 أَطْعَمَهُم
- Synthesis: Feeding establishes host and recipient roles. A request can be answered within that frame, while the interloper enters without recognized standing and exposes the social boundary around shared provision.

#### Subchannel C. Denunciation, Insult, and Indignation
- Reading type: latent/lexical
- Scene or process: Speech attacks standing by informing against someone, stirring conflict, or casting an insulting lineage formula, provoking proud anger.
- Active motifs: denunciation and tale-bearing `ق ر ش:B007/m01`; agitation between parties `ق ر ش:B007/m02`; saddle-based insult `ر ح ل:B012/m01`; proud indignation `ع ب د:B008/m01`
- Ayah anchors: 106:1 قُرَيْشٍ; 106:2 رِحْلَةَ; 106:3 فَلْيَعْبُدُوا۟
- Synthesis: Reputation is damaged indirectly through speech that exposes, incites, or degrades ancestry. Indignation is the answering emotion when a person's standing or affiliation is publicly attacked.

## Standalone Subchannels

### S1. Mouth-to-Mouth Reciprocity
- Reading type: latent/lexical
- Scene or process: Two mouths meet in a reciprocal contact associated with kissing or the behavior of birds.
- Active motifs: mouth-to-mouth contact `ط ع م:B013/m01`
- Ayah anchors: 106:4 أَطْعَمَهُم
- Synthesis: The food root moves from taking nourishment into the mouth to direct exchange between mouths. The scene preserves reciprocity and intimate contact without reducing it to ordinary eating.

### S2. Rough Terrain and Deflected Courses
- Reading type: latent/lexical
- Scene or process: A traveler or moving object encounters rough ground, misses its intended line, or follows a crooked watercourse.
- Active motifs: rough place or head of a wadi `ش ت و:B005/m01`; deviation from an aim `ص ي ف:B005/m01`; crooked watercourse `ص ي ف:B005/m02`
- Ayah anchors: 106:2 ٱلشِّتَآءِ, ٱلصَّيْفِ
- Synthesis: Terrain and trajectory meet in the problem of a course that does not remain straight. Rough ground can redirect movement, just as an arrow veers from its target or water bends through an irregular channel.

### S3. Night Residence and Concealed Action
- Reading type: latent/lexical
- Scene or process: Night provides both a period of staying and cover for secret planning or attack.
- Active motifs: night residence or activity `ب ي ت:B004/m01`; covert night planning or assault `ب ي ت:B004/m02`
- Ayah anchors: 106:3 ٱلْبَيْتِ
- Synthesis: The house root marks what is done or endured overnight, then sharpens that temporal setting into clandestine deliberation and hostile arrival under darkness.


===== _commentary/v16/work/s106/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 106

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 106:1

## habituated attachment
- reading: An open causal or purposive heading about an acquired disposition to remain attached, with possessor and producer still unresolved.
- mechanism: The focus can name repeated acclimation that turns a person, place, or practice into something familiar and stayable. Focus-only, both Quraysh's habituated attachment and the habituating of Quraysh remain live.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Familiar attachment and habitual staying supply the affective-temporal core: recurrence settles Quraysh into an enduring relation.

## composed collective
- reading: Quraysh are actively composed, or have a composite arrangement made for them, out of parts that could otherwise remain separate.
- mechanism: Joining after separation makes īlāf an active composition rather than a mood of concord. Distinct people, practices, or relations are fitted together so that Quraysh exists or functions as a coherent social body.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining differentiated parts after separation supplies the constructive operation and makes Quraysh the composed whole or its beneficiary.

## seasonal mobility habituated
- reading: Attachment can be a portable habit: Quraysh become at home in a recurrent pattern of movement.
- mechanism: The immediate echo of the focus noun is specified by a journey bracketed by winter and summer. Familiarity therefore becomes a learned cycle that domesticates mobility itself: repeated departure across opposed seasons acquires the steadiness normally associated with staying.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Habitual attachment anchors the focus as an acquired steadiness rather than a one-time agreement.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: The repeated attachment branch assigns that steadiness specifically to their recurring practice.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Actual movement in travel supplies the mobile activity that habituation renders familiar.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B001: Winter supplies one recurring temporal pole of the travel cycle.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer supplies the opposed recurring pole, closing the cycle rather than naming an isolated trip.

## itinerary composition
- reading: The joined parts may also be the operational pieces of a route whose reliable composition sustains that collective.
- mechanism: Joining, fastening a travel load, stopping, and resuming across the seasonal pair recast īlāf as an itinerary assembled from heterogeneous operations. The cohesion of Quraysh is also logistical: loads, legs, stations, and times are fitted into a repeatable whole.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Composition after separation anchors the focus as an arrangement whose parts must be fitted together.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: The repeated composition branch carries the focus operation into the journey specification.
  - 106:2 **رِحْلَةَ** ر ح ل B003: Fastening the travel gear supplies deliberate preparation and binding at the start of each leg.
  - 106:2 **رِحْلَةَ** ر ح ل B004: A place of stopping supplies the station that segments motion into an organized itinerary.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B001: Winter gives one temporal compartment into which the itinerary is fitted.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer gives the complementary compartment and makes the arrangement cyclic.

## affiliation as counterhazard
- reading: Īlāf may be the resilience mechanism that makes recurrent travel possible precisely because the cycle can injure, empty, or deflect.
- mechanism: Harmful riding, a famine-marked winter, and summer deviation expose a hostile edge inside the otherwise ordinary seasonal journey. On this reading, īlāf is a counterforce that keeps participants attached and on course through bodily cost, scarcity, and drift.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Persistent attachment supplies the counterforce that can outlast adverse travel conditions.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining after separation supplies the collective integrity threatened by hazard and drift.
  - 106:2 **رِحْلَةَ** ر ح ل B009: Riding accompanied by harm supplies bodily cost within the journey mechanism.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B004: Winter associated with famine supplies a seasonal scarcity pressure.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B005: Deviation from the intended course supplies the risk of directional or normative drift.

## benefit becomes allegiance
- reading: Their acquired stability is a received good whose proper endpoint is allegiance to the Lord centered on the house.
- mechanism: The imperative of submissive obedience follows the īlāf sequence, while lordship tied to a sheltering house supplies the recipient of that response. The focus phrase changes from a self-sufficient social achievement into a received condition that generates allegiance.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Habituated attachment supplies the benefit or condition whose source and demanded response are disclosed later.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Humble obedience supplies the responsive act into which received attachment is converted.
  - 106:3 **رَبَّ** ر ب ب B001: Lordship, ownership, and sovereignty identify the authority to whom the allegiance is redirected.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter and dwelling give lordship a concrete center associated with protection and stable return.

## cohesion as cultivated passage
- reading: Cohesion is an infrastructure repeatedly smoothed, repaired, nurtured, and oriented around shelter.
- mechanism: Leveling and smoothing under service, together with repair, nurture, and completion under lordship, make composition a maintained process. Centered on shelter, īlāf becomes social-spatial infrastructure continually made passable, repaired, and brought to completion.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining parts supplies the infrastructure whose continuity requires active maintenance.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B005: Leveling and smoothing supply the work of removing roughness so a social or spatial passage can hold.
  - 106:3 **رَبَّ** ر ب ب B002: Repair, nurture, and completion supply the governing maintenance that keeps the joined arrangement viable.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: A sheltering dwelling supplies the stable node toward which maintained passage and social return are oriented.

## covenanted household federation
- reading: Quraysh may be the result of a pledged joining of related households whose shared allegiance keeps plurality together.
- mechanism: A covenant branch under the dominant lord mapping, a related-households branch under the non-dominant split mapping, and house-as-family make Quraysh's joining legible as a compact among kin households. Obedience functions as the allegiance that holds the federation around one center.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining after separation supplies the federating operation among distinct household units.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Submissive obedience supplies the shared allegiance that can bind the compact.
  - 106:3 **رَبَّ** ر ب ب B011: A covenant or pledged bond supplies the formal relation joining the parties.
  - 106:3 **رَبَّ** ر ب ب B007: The preserved non-dominant mapping contributes a household of paternal relatives as the possible social units of federation.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: Household and dependents supply the nested family units gathered under the singular house.

## affiliation produced by provision and security
- reading: Familiarity is materially and affectively produced: bodies must be provisioned and expectations of harm quieted before relations can become habitual.
- mechanism: Feeding answers bodily emptiness and securing answers anticipated harm; together they supply material and affective preconditions for habituated attachment. Īlāf becomes a produced capacity to stay, trust, and repeat relations, not merely a preexisting custom.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Familiar attachment supplies the settled condition whose enabling causes become visible in the final context.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Giving food to others supplies the active material provision that permits repeated social attachment.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and sound condition broaden feeding into the durable material base of the relation.
  - 106:4 **جُوعٍ** ج و ع B001: An empty belly supplies the concrete deficit that provision reverses.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: A heart stilled in safety and confidence supplies the affective condition in which attachment can persist.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Alarm at expected harm supplies the prospective threat that security removes.

## composition against double depletion
- reading: Īlāf also names the continued wholeness of that composition when hunger and fear would subtract from it.
- mechanism: Joining after separation is threatened by two subtractive processes: hunger hollows and thins from within, while fear diminishes by taking away. Livelihood restores material fullness and security stills expectation, so īlāf reads as preservation of collective integrity against double attrition.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Composition supplies the collective integrity that depletion could loosen or fragment.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and sound condition supply restoration of the collective's material capacity.
  - 106:4 **جُوعٍ** ج و ع B004: Figurative emptiness and thinning supply an inward erosion of the joined body.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled safety supplies resistance to the anticipatory pressure that can disperse a group.
  - 106:4 **خَوْفٍۭ** خ و ف B004: Diminution that takes from a thing supplies the second, subtractive mode of collective loss.

## trust compact
- reading: Īlāf can be a trust-bearing compact that makes repeated contact possible by quieting both expected and mutually generated fear.
- mechanism: Safety carries both settled confidence and trusted assent, while fear can be induced and mutually contested. Against that relational field, familiar attachment becomes a trust compact that interrupts escalation of intimidation, not merely passive absence of danger.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Familiar attachment supplies the durable relation that confidence stabilizes.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining supplies the compact form through which separate parties can coordinate.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled confidence supplies the inward effect of a functioning trust relation.
  - 106:4 **وَءَامَنَهُم** ء م ن B002: Assent trusted by the heart supplies an interpersonal or epistemic dimension beyond physical protection.
  - 106:4 **خَوْفٍۭ** خ و ف B002: Causing fear in another supplies one side of a relational intimidation loop.
  - 106:4 **خَوْفٍۭ** خ و ف B003: Mutual contest in fear supplies escalation between parties that a compact must interrupt.

## distributed stopover hospitality
- reading: Attachment may be regenerated piecemeal through hospitable stopovers that make a mobile cycle temporarily domestic.
- mechanism: An inter-journey stopping place, one-night provision, and feeding others can be composed into a chain of hospitable nodes. On this reading, īlāf is the repeatable social protocol that makes travel intermittently home-like; attachment is distributed across stops rather than fixed in one residence.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Composition supplies the linking of separate stops into one traversable social network.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Habitual attachment supplies the home-like familiarity repeatedly produced at network nodes.
  - 106:2 **رِحْلَةَ** ر ح ل B006: A lodging between journeys supplies the intermediate node rather than a final destination.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B005: Provision sufficient for a night supplies the minimum hospitality that turns a stop into temporary dwelling.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Feeding another supplies the host action that reproduces the stopover protocol.

## grafted affiliation
- reading: Their joining may resemble a graft: contact alone is insufficient, and sustained nourishment lets the inserted relation take and grow.
- mechanism: 
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining separate things supplies the social union to be reimagined through a material graft.
  - 106:3 **رَبَّ** ر ب ب B005: The non-dominant mapping's feeding and growth supply the developmental process by which a union becomes viable.
  - 106:4 **أَطْعَمَهُم** ط ع م B010: Nourishing a branch until it accepts a graft supplies the concrete analogy of attachment taking through provision.

## ecological attunement
- reading: Quraysh may also be attuned to a provision-bearing ecology whose alternating seasonal pulses mature what sustains the cycle.
- mechanism: 
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B005: Habituation supplies sustained attunement to a recurring cycle.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B003: Winter rain supplies one pulse in the environmental cycle.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B002: Summer rain supplies a second, contrasting pulse rather than a merely dry calendar label.
  - 106:3 **رَبَّ** ر ب ب B008: A rain-bearing cloud supplies the mediating source that links season to provision.
  - 106:4 **أَطْعَمَهُم** ط ع م B005: Fruit reaching ripeness and taking flavor supplies the productive endpoint of seasonal water.

## nested aggregate
- reading: Quraysh can be imagined formally as a scaled aggregate: persons within households and households within one composed collective.
- mechanism: 
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B001: Hundreds gathered into a thousand supply a nested scale model in which many smaller units register as one larger whole.
  - 106:3 **رَبَّ** ر ب ب B010: A receptacle gathering separate arrow shafts supplies a one-container-many-members geometry.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: Household members supply plausible nested social units within the larger named collective.


# Focus 106:2

## habituated seasonal return
- reading: A winter-summer movement repeated until mobility itself becomes their familiar mode of attachment and continuity.
- mechanism: Repeated departure across the two seasonal poles becomes familiar attachment: movement is not a one-off trip but a practiced mode of continuity.
- trace:
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: Familiar attachment and habituated staying make recurrent movement a settled collective habit.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Going forth toward a destination supplies the concrete repeated motion carried by that habit.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B001: Winter supplies one recurring temporal pole of the practiced movement.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer supplies the opposed recurring pole that closes the annual rhythm.

## composed seasonal circuit
- reading: A composed circuit whose winter quarters, summer operations, and intermediate stages function as interlocking parts.
- mechanism: Distinct stages, quarters, and season-bound actions are joined into one circuit; coherence is an achieved arrangement of heterogeneous parts.
- trace:
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Joining separated parts into a composition turns the two seasons and journey stages into one organized system.
  - 106:2 **رِحْلَةَ** ر ح ل B006: A stopping stage between departures supplies the modular units from which the circuit is assembled.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B002: Wintering and winter quarters make the cold season a situated phase rather than a bare date.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B003: Summer residence and season-bound action provide the complementary operational phase.

## portable stage system
- reading: A portable stage-system moves mounts, equipment, lodging, and seasonal work together, preserving continuity through relocation.
- mechanism: The journey transports its own apparatus and provisional dwelling; seasonal continuity depends on mounts, gear, lodging, and readiness moving together.
- trace:
  - 106:2 **رِحْلَةَ** ر ح ل B002: Saddle gear makes the journey materially equipped rather than abstract motion.
  - 106:2 **رِحْلَةَ** ر ح ل B004: Dwelling space and travelling belongings make mobility capable of carrying a provisional home.
  - 106:2 **رِحْلَةَ** ر ح ل B005: A mount made fit after weakness supplies the readiness condition for sustaining the mobile system.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B002: Winter quarters provide one temporary emplacement for the travelling household.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B003: Summering provides the alternate emplacement and season-specific activity.

## seasonal asymmetry exchange
- reading: The seasonal circuit is a resilience mechanism joining periods of privation and yield so that their asymmetry can be survived.
- mechanism: The circuit joins unequal seasonal conditions: winter can image famine and rough exposure, while summer can image rain and yield. Travel mediates between deficit and replenishment.
- trace:
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Composition joins unlike seasonal conditions into a compensating whole.
  - 106:2 **رِحْلَةَ** ر ح ل B006: Journey stages provide the transfer mechanism between the unequal conditions.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B004: Winter as famine or scarcity supplies the deficit pole of the seasonal exchange.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B002: Summer rain with its pasture and growth supplies a possible replenishing pole.

## repetition recursive cohesion
- reading: The repeated wording exposes a feedback loop: collective joining makes the circuit possible, and practicing the circuit continually remakes that joining.
- mechanism: The immediate recurrence of the same noun makes cohesion recursive: an already named joining or familiarity is specified again as their relation to the seasonal journey, so the circuit both depends on and reproduces attachment.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: The first joining image frames the following line as specification of what is being composed.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: The suffixed recurrence shifts composition into their habituated attachment to the journey.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Concrete departure is the repeated practice through which attachment can be renewed.

## service reorients mobility
- reading: The competence is deliberately left open toward submissive response: successful routine is occasion and obligation, not its own endpoint.
- mechanism: The following turn to submissive service prevents the seasonal system from closing around its own efficiency; habituated mobility becomes a condition that calls for directed response.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Submissive worship and obedience supply the directed response into which the travel routine is made to culminate.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: Habituated attachment supplies the settled condition being ethically reoriented.
  - 106:2 **رِحْلَةَ** ر ح ل B001: The journey supplies the practical achievement that no longer reads as self-justifying.

## stewarded completion
- reading: The circuit is a repeatedly repaired and completed arrangement whose continuity depends on ongoing stewardship.
- mechanism: Repair, nurture, completion, and persistence recast the composed circuit as something continually maintained; its coherence is stewarded rather than merely assembled once.
- trace:
  - 106:3 **رَبَّ** ر ب ب B002: Repair, cultivation, and completion supply ongoing maintenance for the seasonal system.
  - 106:3 **رَبَّ** ر ب ب B007: Staying, residence, and duration give the maintained circuit temporal persistence.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Composition supplies the multi-part arrangement that requires maintenance.
  - 106:2 **رِحْلَةَ** ر ح ل B006: Successive stages make completion an iterative process across the route.

## growth cycle split root
- reading: The itinerary can also be imagined as a cultivated seasonal organism, fed by alternating conditions and growing through repeated composition.
- mechanism: The packet's non-dominant ر ب و mapping activates growth beside the focus ayah's seasonal rain potentials: the journey can be carried as a cultivated cycle that increases and matures, not only as governed motion.
- trace:
  - 106:3 **رَبَّ** ر ب ب B005: Nourishment and growth from the non-dominant mapped root supply an organic development model.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Joining different parts gives the growing cycle an articulated structure.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B003: Winter rain supplies one input into the cycle's nourishment.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B002: Summer rain, pasture, and vegetation supply a second seasonal growth phase.

## house anchors mobile home
- reading: Portable seasonal dwellings orbit a fixed household center, turning mobility into an anchored rhythm of leaving and returning.
- mechanism: A fixed refuge and household center polarize the mobile dwelling potential of رِحْلَةَ; the circuit becomes departure and return around an anchor rather than indefinite displacement.
- trace:
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter and dwelling supply the fixed spatial anchor against which mobility is measured.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: The household sense makes the anchor social as well as architectural.
  - 106:2 **رِحْلَةَ** ر ح ل B004: Travelling belongings and provisional dwelling provide the mobile counterpart to the fixed house.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B002: Winter quarters supply one temporary satellite of the anchored household.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B003: Summer residence supplies the alternate satellite and completes the oscillation.

## supply chain fills lack
- reading: The composed itinerary reads as a relay that carries livelihood into seasonal emptiness, converting a calendar circuit into provision infrastructure.
- mechanism: Livelihood and a time of generalized hunger sharpen the winter-famine baseline into a supply mechanism: composed route stages move sustenance across seasonal vacancies.
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood, provision, and good condition supply the positive material flow carried by the route.
  - 106:4 **جُوعٍ** ج و ع B002: A period of widespread hunger scales lack from an individual stomach to a systemic seasonal condition.
  - 106:4 **جُوعٍ** ج و ع B004: Emptiness and thinning provide the vacancy that the supply flow must fill.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Composition connects sources, stages, and seasons into a distributive chain.
  - 106:2 **رِحْلَةَ** ر ح ل B006: Journey stages give the supply flow a relay structure.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B004: Winter famine aligns one focus-season with the systemic lack named afterward.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B002: Summer rain and pasture supply a possible yield pole feeding the relay.

## security revises habituation
- reading: Familiarity is stored evidence of protected passage: each journey negotiates expected harm and loss, and each survival deepens trust.
- mechanism: Habituation acquires an affective and risk-bearing underside: repeated travel can settle the heart only because anticipated harm and attrition are held at bay, yet the causal direction may also run from repeated safe passage to trust.
- trace:
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Stillness of heart in security and trust supplies the affective state behind familiar movement.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Fear as expectation of harm supplies the forward-looking risk shadowing every departure.
  - 106:4 **خَوْفٍۭ** خ و ف B004: Diminution or attrition turns danger into possible material loss, not feeling alone.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: Familiar attachment is reread as trust sedimented by survivable repetition.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Actual departure is the exposure across which security or fear becomes consequential.

## double reversal engine
- reading: Recurrence has a directional function: the seasonal circuit repeatedly converts material vacancy and anticipated danger into sustenance and trust.
- mechanism: The two seasonal poles become a transformation engine when read beside the paired reversals of 106:4: the circuit repeatedly carries emptiness toward sustenance and anticipated harm toward settled trust.
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Giving food supplies the first positive transformation enacted upon lack.
  - 106:4 **جُوعٍ** ج و ع B001: An empty stomach supplies the concrete negative state from which the first transformation begins.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Secure stillness and trust supply the second positive endpoint.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Expected harm supplies the negative state from which the second transformation begins.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Composition binds the two transformations into one repeated operating system.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B001: Winter supplies one alternating temporal chamber of the transformation cycle.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer supplies the complementary chamber that makes the process recurrent.

## levelled rough corridor
- reading: The journey can be carried as a corridor continually made serviceable: gear is fastened and rough seasonal terrain is disciplined into passage.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B005: Making level and tractable supplies an engineering image for disciplined passage.
  - 106:2 **رِحْلَةَ** ر ح ل B003: Fastening the saddle supplies the preparatory act that makes passage operational.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B005: A rough place or valley front supplies the resistant terrain to be crossed.

## grafted route network
- reading: The itinerary resembles a grafted network: joined, fastened junctions accept and carry nourishment so the whole circuit can grow.
- mechanism: 
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B010: Feeding a branch and accepting a graft supply the image of a living junction that carries nourishment.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B002: Joining separated parts supplies the route network's connective principle.
  - 106:2 **رِحْلَةَ** ر ح ل B003: Fastening travel gear supplies the mechanical analogue of securing each junction.
  - 106:3 **رَبَّ** ر ب ب B005: Nourishment and growth let the joined route behave like a living network rather than a static chain.

## adaptive summer deviation
- reading: Summer also casts a lexical shadow of timing and deviation: the circuit survives by knowing when a stage must bend away from its expected line to prevent loss.
- mechanism: 
- trace:
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B005: Turning aside from an aim supplies a detour image within the seasonal route.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B006: Proverbial missed timing or completed need turns summer into a decision threshold.
  - 106:2 **رِحْلَةَ** ر ح ل B006: Successive journey stages provide points at which timing and direction can be revised.
  - 106:4 **خَوْفٍۭ** خ و ف B004: Possible diminution supplies the loss pressure that can make rerouting adaptive.


# Focus 106:3

## devotional allegiance
- reading: A communal transfer of obedient allegiance to the owner-authority specifically disclosed through this sheltering House.
- mechanism: Submissive worship, sovereign ownership, and shelter form a relational chain: the group is summoned to place its obedience under the authority responsible for this particular protected center.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Submissive worship supplies the commanded act and makes allegiance, not mere acknowledgment, the operative relation.
  - 106:3 **رَبَّ** ر ب ب B001: Lordship, ownership, and obeyed authority identify the recipient as master of the relation.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter and dwelling make the House the concrete protected center through which that authority is recognized.

## nurtured household
- reading: The verse summons a tended household to serve the one whose continuing care makes it a coherent household.
- mechanism: The focus can describe a maintained social organism rather than a command attached to architecture: the Lord repairs and develops, the House names a household, and worship is the household's responsive service.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Devoted obedience turns the plural command into the household's responsive practice.
  - 106:3 **رَبَّ** ر ب ب B002: Repair, stagewise nurture, and completion make the Lord an active maintainer rather than a static title.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: Household and dependents shift the deictic House from masonry to an affiliated human collective.

## mastery relocated
- reading: The command also reassigns the household's deepest dependence away from proximate masters and toward the House's Lord.
- mechanism: A miniature hierarchy is exposed and then relocated: owned dependence and household membership are not erased, but ultimate mastery over them is assigned to the Lord of the House rather than to an intra-house human owner.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B001: Owned or unfree status supplies the social depth of dependence latent beneath the worship verb.
  - 106:3 **رَبَّ** ر ب ب B001: Mastery and ownership receive that dependence and concentrate authority in the named Lord.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: The household branch locates the authority question inside a network of members and dependents.

## honor transferred
- reading: The command redirects the House's prestige upward, making lineage honor derivative of honoring its Lord.
- mechanism: The imperative can stage a transfer of prestige: the honored lineage-house is not itself the final object of magnification; honor passes through the deictic House to its Lord.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B006: Honoring and magnifying provide an exploratory affective register for the commanded worship.
  - 106:3 **رَبَّ** ر ب ب B001: Sovereign lordship marks the proper terminus of the transferred honor.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B008: The noble lineage-house supplies the competing prestige center that the syntax subordinates to its Lord.

## material service center
- reading: Worship retains that sense but acquires an embodied service-shadow: sustaining a passable, protected center under its maintainer.
- mechanism: Without replacing the ordinary worship sense, the focus carries a material undertone: devoted service can include making and keeping the approach, vessel, or center usable under the care of the one who maintains it.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B005: Subduing and smoothing a physical surface contributes the branch-distant image of service that makes passage possible.
  - 106:3 **رَبَّ** ر ب ب B002: Repair and upkeep assign continuing maintenance to the Lord-side of the mechanism.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: The sheltering dwelling is the durable center whose accessibility and integrity matter.

## affiliative service
- reading: Its worship is itself a communal technology of affiliation, repeatedly joining members into a familiar House-centered collective.
- mechanism: Repeated joining and habituated companionship activate the social potential of the plural service command: worship becomes a practice that continually composes people into a familiar household around one House and one Lord.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Shared submissive practice provides the repeated action through which affiliation can be enacted.
  - 106:3 **رَبَّ** ر ب ب B002: Nurturing and completion make social cohesion something maintained over time.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: The household image gives the joined collective a human form rather than reducing the House to a site.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining one thing to another supplies the compositional operation that gathers the plural subjects.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: Familiarity, companionship, and persistence turn one-time gathering into durable social attachment.

## house as journey hinge
- reading: The House becomes the maintained hinge of recurring mobility, and worship includes an embodied commitment to the protected route-center.
- mechanism: Travel and an intermediate lodging place turn the fixed House into a hinge in a mobile system. The material service-shadow of worship now concerns keeping a protected node and its approaches usable across departures and returns.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B005: The passable-surface image lets devoted service acquire a material route-maintenance undertone.
  - 106:3 **رَبَّ** ر ب ب B002: Repair and administration assign the mobile system a sustaining governor.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter gives movement a stable place of protection and return.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Going forth in travel supplies the outward motion against which the House becomes a fixed hinge.
  - 106:2 **رِحْلَةَ** ر ح ل B006: A lodging between journeys supplies the relay-node image that functionally links House and route.

## season spanning fidelity
- reading: It asks for season-spanning fidelity: stable service to the lasting Lord of the fixed shelter through alternating conditions.
- mechanism: The opposed seasons activate a temporal reading: a lasting Lord and fixed shelter hold together a collective whose conditions alternate. Worship becomes fidelity repeated across a complete environmental cycle rather than a one-time payment.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Devoted obedience supplies the repeatable practice carried through changing conditions.
  - 106:3 **رَبَّ** ر ب ب B007: Staying, clinging, and duration provide the invariant counterweight to seasonal alternation.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: The sheltering House supplies the fixed spatial center of the temporal cycle.
  - 106:2 **ٱلشِّتَآءِ** ش ت و B001: Winter supplies one environmental phase and its distinctive exposure.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer completes the alternating pair and expands the command across the year.

## two lacks repaired
- reading: The House is the visible node of a continuously repaired ecology, and worship answers the Lord who fills material lack and halts affective and social depletion.
- mechanism: Livelihood fills bodily and social emptiness while security arrests anticipated loss. Together they instantiate the Lord's nurturing and completing action, so the House becomes a lived ecology of provision and refuge rather than a self-sufficient monument.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worshipful obedience is the response generated by the paired acts of care.
  - 106:3 **رَبَّ** ر ب ب B002: Repair, nurture, and completion unify provision and protection as two modes of lordly maintenance.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter becomes effective refuge only when supplied and secured.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and well-being broaden feeding from an isolated meal to a maintained material condition.
  - 106:4 **جُوعٍ** ج و ع B004: Emptiness and wasting supply the deficit that material care reverses.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled confidence supplies the positive interior state produced by protection.
  - 106:4 **خَوْفٍۭ** خ و ف B004: Loss that takes away from a thing makes fear an erosive deficit as well as an emotion.

## service enabled by care
- reading: The imperative addresses subjects first rendered capable and steady by care, so worship is enabled agency rather than tribute wrung from deprivation.
- mechanism: A capacity branch within feeding activates the strength branch within service. Provision and settled confidence can therefore be read as enabling conditions for worship: the Lord first makes the subjects able and stable enough to answer the command.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worship remains the commanded response whose conditions of possibility are being reconstructed.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B007: Strength and solidity supply a latent state of empowered rather than depleted service.
  - 106:3 **رَبَّ** ر ب ب B002: Nurture gives the Lord the role of developing the subjects' ability to respond.
  - 106:4 **أَطْعَمَهُم** ط ع م B011: Ability or capacity lets feeding signify endowed agency rather than calories alone.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled confidence removes the destabilization that would obstruct willing service.

## protective not coercive mastery
- reading: The context differentiates the House's Lord from a coercive master: this authority creates calm and removes fear, enabling devoted rather than terrorized submission.
- mechanism: The focus's social grammar of master, dependent, and household is revised by the contrast between producing security and producing fear. Legitimate lordship is characterized as removing coercive fear, not using fear to manufacture slave-like service.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B004: The image of reducing another to slave-like status exposes coercion as a possible but rejected model of mastery.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Submissive worship remains the actual commanded relation, now differentiated from coerced subjugation.
  - 106:3 **رَبَّ** ر ب ب B001: Ownership and authority pose the question of what kind of master the Lord is.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: The household branch makes the quality of authority socially consequential for members and dependents.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Security and inner calm positively characterize the Lord's exercise of authority.
  - 106:4 **خَوْفٍۭ** خ و ف B002: Causing fear supplies the coercive counter-model that the securing action reverses.

## scattering reversed into convergence
- reading: The instruction carries a counter-image in which scattered routes and groups are repeatedly converged into House-centered service.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B010: Scattering into multiple directions supplies the latent condition that communal worship reverses.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: One sheltering center supplies the destination and container of convergence.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining supplies the centripetal operation that counters dispersal.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Travel supplies the multiple outward trajectories that can be reoriented toward the House.

## stranding shadow
- reading: Worship is shadowed by remembered vulnerability to breakdown: allegiance answers the caretaker of a House that functions as repair, refuge, and recovery between risky movements.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B011: Breakdown and being cut off supply the failure-state from which the commanded relation is read as resilient dependence.
  - 106:3 **رَبَّ** ر ب ب B002: Repair and care supply the agency that answers breakdown.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter supplies the recovery node for a vulnerable traveler.
  - 106:2 **رِحْلَةَ** ر ح ل B009: Travel undertaken with harm activates the concrete risk of failure on the route.
  - 106:2 **رِحْلَةَ** ر ح ل B006: A lodging between journeys gives repair and recovery a spatial station.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Security and settled confidence mark successful emergence from the route's vulnerability.

## surplus as rival lord
- reading: The imperative can polemically deny sovereignty to the surplus generated around that circulation: serve the House's Lord, not increase, circulation, or institutional prestige as though any were lord.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worship supplies the allegiance that can be redirected away from an economic rival.
  - 106:3 **رَبَّ** ر ب ب B003: Transactional increase supplies the non-dominant rival image activated inside the lord-root mapping.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B008: The prestigious lineage-house supplies a social institution that could absorb credit for generated increase.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Recurring travel supplies circulation from which the reader tentatively infers an economic system.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and good condition supply the material yield whose ultimate source is disputed.

## grafted household
- reading: The House can be imagined as a nurtured, graft-capable household in which shared service composes belonging beyond a merely inherited enclosure.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Shared devotion supplies the practice through which non-identical members can belong together.
  - 106:3 **رَبَّ** ر ب ب B005: Fostered-child and step-family relations supply a model of nurtured belonging not reducible to direct descent.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B002: The household branch provides the social body into which affiliation can incorporate members.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining distinct things supplies the general operation of incorporation.
  - 106:4 **أَطْعَمَهُم** ط ع م B010: A branch accepting a graft supplies the material analogy for a joined member taking within a living whole.

## house at the scale of one night
- reading: It also contracts to the scale of surviving one more night: the Lord of this House is encountered in recurrent shelter and enough food for embodied dependents.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worship supplies the recurring response to care experienced at an immediate human timescale.
  - 106:3 **رَبَّ** ر ب ب B002: Continuing nurture turns provision into repeated maintenance rather than a single gift.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B005: Provision sufficient for one night compresses the House's grandeur to the recurring threshold of subsistence.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Feeding another supplies the concrete act that meets the overnight need.
  - 106:4 **جُوعٍ** ج و ع B001: An empty belly defines the immediate bodily limit that provision crosses.

## security as trustful assent
- reading: Because the Lord's shelter removes anticipated harm, worship can be heard as trustful assent arising from security rather than obedience haunted by fear.
- mechanism: 
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Submissive worship supplies the relation whose affective quality is revised.
  - 106:3 **رَبَّ** ر ب ب B001: Lordly authority supplies the object toward whom trust or fear may orient the worshipper.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter gives trust a concrete environment of experienced protection.
  - 106:4 **وَءَامَنَهُم** ء م ن B002: Heart-settling assent supplies a trust resonance within the act of being secured.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Anticipatory dread supplies the affective condition that security removes.


# Focus 106:4

## double release
- reading: The verse stages a coordinated transfer of one collective out of bodily lack and threat-expectation into nourishment and settled trust.
- mechanism: A single agent actively reverses two coupled deficits: bodily emptiness is answered by intake, while anticipatory harm is answered by settled safety. The parallel syntax makes nourishment and security mutually interpreting forms of release rather than unrelated favors.
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Giving food supplies the concrete first intervention and makes the subject an active feeder of the plural object.
  - 106:4 **جُوعٍ** ج و ع B001: The empty-stomach image defines the embodied deficit from which the first intervention releases them.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled security and trust supply the positive state produced by the second causative.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Anticipation of harm supplies the second deficit, making safety a release from an active horizon of threat.

## systemic viability
- reading: The agent establishes collective viability by replacing famine conditions with livelihood and stopping the erosion associated with insecurity.
- mechanism: The first causative can establish livelihood rather than merely deliver a portion, and hunger can name a famine-time. In parallel, safety arrests the attritional taking-away latent in fear. The pair therefore restores the material and social conditions under which a collective remains viable.
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Provision, livelihood, and good condition enlarge feeding from a meal into a durable material basis.
  - 106:4 **جُوعٍ** ج و ع B002: The famine-time image enlarges hunger from an individual sensation into a collective temporal condition.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Safe-conduct and reliability make security an enduring social condition, not only a passing feeling.
  - 106:4 **خَوْفٍۭ** خ و ف B004: The image of diminishing by taking away recasts feared harm as attrition that security prevents.

## inner outer reanimation
- reading: The paired causatives reanimate both embodied agency and inward trust, moving the group from displayed depletion and alarm into responsiveness.
- mechanism: Material lack, longing, visible fear, and inward trust form a psychosomatic sequence. Feeding reanimates a depleted collective's responsiveness and sense of worth; securing them allows alarm displayed on the body to settle into confidence.
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B008: Discernment, worth, and responsiveness make feeding a possible restoration of agency as well as intake.
  - 106:4 **جُوعٍ** ج و ع B004: Emptiness and longing widen hunger into an affective lack that can drain collective responsiveness.
  - 106:4 **وَءَامَنَهُم** ء م ن B002: Trusting assent supplies the inward stabilization produced alongside outward protection.
  - 106:4 **خَوْفٍۭ** خ و ف B005: Visible manifestation of fear gives the threatened condition a bodily surface that can be calmed.

## alif social composition
- reading: Food and safety help keep forming the group as a familiar, durable association rather than merely serving isolated members.
- mechanism: Repeated joining and familiarity recast the plural recipients as a collective continually composed through stable relations. Feeding and security now do social work: they keep bodies together long enough for repeated association to become dependable cohesion.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining one thing to another supplies the compositional image by which separate recipients become a maintained collective.
  - 106:2 **إِۦلَٰفِهِمْ** ء ل ف B005: Familiarity, sociability, and continued association turn composition into a repeated and affectively settled bond.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Feeding supplies the shared material practice that can preserve association.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Trust and security supply the relational stability in which familiarity can persist.

## journey mobile corridor
- reading: Provision and safe-conduct form a corridor that makes repeated departure, transit, stopping, and return viable.
- mechanism: Travel, fastening a saddle, and the station between trips convert the paired gifts into mobile infrastructure. Livelihood has to be carried or renewed along a route, while security becomes reliable passage through exposed intervals.
- trace:
  - 106:2 **رِحْلَةَ** ر ح ل B001: Going forth in travel moves hunger and fear from a static domestic scene onto an exposed route.
  - 106:2 **رِحْلَةَ** ر ح ل B003: Fastening the saddle supplies the practical preparation through which provision and protection become journey-enabling.
  - 106:2 **رِحْلَةَ** ر ح ل B006: A station between journeys supplies a recurrent node where feeding and security must be renewed.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and provision become the material flow that supports repeated movement.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Safe-conduct and reliability turn security into confidence that passage and return can recur.

## seasonal resilience
- reading: The two acts maintain a collective through a repeating annual ecology of scarcity and exposure.
- mechanism: The opposed seasons make the verse calendar-scale. Winter's explicit famine branch activates hunger as a recurrent season of scarcity, while summer completes a full cycle; feeding and securing become resilience maintained across changing environmental pressures.
- trace:
  - 106:2 **ٱلشِّتَآءِ** ش ت و B004: Winter-famine directly couples a named season to the hunger condition in the focus ayah.
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B001: Summer-time supplies the opposite seasonal pole and closes the annual cycle.
  - 106:4 **جُوعٍ** ج و ع B002: Famine-time lets hunger denote a broad period rather than a momentary pang.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood supplies continuity of provision across the seasonal alternation.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled safety supplies continuity on the threat side of the same cycle.

## worship as enabled response
- reading: Food and safety are simultaneously reasons for worship and the release from hunger-driven or fear-driven compulsion that makes responsive worship possible.
- mechanism: The imperative of worship before the relative clause makes provision and security intelligible as grounds for responsive obedience. Because the benefits remove hunger and fear, the response is not extracted by those pressures; the same acts that warrant worship also create room for it to be offered from stability.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worship and humble obedience supply the response toward which the two focus acts are retrospectively oriented.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Feeding removes material compulsion and supplies a concrete reason for responsive obedience.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Safety and trust remove coercive fear and supply the settled condition of the response.
  - 106:4 **خَوْفٍۭ** خ و ف B002: Fear-induction supplies the coercive alternative that the securing causative reverses.

## level ground for agency
- reading: They prepare the material and affective ground on which the recipients regain capacity to act and worship.
- mechanism: A branch of the worship root images leveling and making traversable. Activated beside feeding as capacity and security as settled trust, it suggests that the two gifts prepare level ground on which responsible action can occur.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B005: Leveling and smoothing supply the terrain analogy for removing impediments to action.
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B003: Worship and humble obedience identify the action made possible on that prepared ground.
  - 106:4 **أَطْعَمَهُم** ط ع م B011: Capacity over something lets feeding register as restored ability rather than caloric transfer alone.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled trust supplies the non-obstructed affective ground for agency.

## rabb sustaining completion
- reading: The Lord's characteristic governance continuously repairs, matures, provisions, and protects the collective.
- mechanism: The agent identified in the relative clause is framed by lordship as repair, nurture, completion, and continuance. Feeding and security thus become the ongoing work of bringing a dependent collective toward viable completeness, not isolated emergency interventions.
- trace:
  - 106:3 **رَبَّ** ر ب ب B002: Repair, nurture, and completion supply the governing process into which feeding and securing fit.
  - 106:3 **رَبَّ** ر ب ب B007: Remaining, dwelling, and duration make the governing process continuous rather than episodic.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood is the material maintenance dimension of sustained nurture.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Reliable safety is the protective maintenance dimension of the same process.

## rabb split growth
- reading: Nourishment and protected duration let the collective ripen, grow, and reproduce its form.
- mechanism: The non-dominant mapped root activates nourishment and growth, which meets focus branches of ripening and successive formation. On this reading, feeding and security do more than preserve an already finished group: they create the conditions in which its form can mature and continue.
- trace:
  - 106:3 **رَبَّ** ر ب ب B005: The split-root image of nourishment and growth supplies a developmental rather than merely sovereign frame.
  - 106:4 **أَطْعَمَهُم** ط ع م B005: Ripening and taking on flavor make feeding a condition of maturation.
  - 106:4 **أَطْعَمَهُم** ط ع م B014: Successive formation makes nourishment support continuity of collective form.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Security supplies the protected interval in which maturation and continued formation can occur.

## covenantal safe conduct
- reading: The two outcomes can also be carried through a divinely sustained ecology of bonds, livelihood, and safe passage.
- mechanism: Joining, journeying, covenant, livelihood, and safe-conduct combine into a governance model. The beneficent agent may be read as sustaining the agreements and reliable relations through which a mobile collective can obtain provision and pass without predation; divine action remains primary, while the packet leaves its mediation open.
- trace:
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining supplies the network-forming relation needed for coordinated passage and exchange.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Travel supplies the exposed movement whose material and security needs the network must answer.
  - 106:3 **رَبَّ** ر ب ب B011: A bond or covenant supplies a concrete social instrument for stabilizing obligations.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Livelihood and revenue make feeding the material yield of a functioning network.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Safe-conduct, trust, and reliability make securing them the network's protective guarantee.

## house refuge larder
- reading: The House becomes a model or hub in which nourishment and refuge are coordinated for a vulnerable collective.
- mechanism: Shelter and a night's provision concentrate the paired reliefs in one concrete hub. The House becomes a spatial model of a protected larder: it gathers vulnerable bodies, answers recurring intake, and encloses them against exposure.
- trace:
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter and dwelling supply the enclosing spatial function that corresponds to security.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B005: A night's sustenance supplies the recurring domestic unit that corresponds to feeding.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Giving food fills the provisioning function of the hub.
  - 106:4 **جُوعٍ** ج و ع B001: Bodily emptiness is the recurring need answered inside the provisioning space.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: A place of safety and settled trust fills the refuge function of the same hub.

## hospitality and honor
- reading: They are received into a regime of hospitality in which provision and safe-conduct also establish dignity and trusted standing.
- mechanism: Honor branches around worship and house activate a hospitality economy: abundant feeding and trusted protection do not merely preserve life but confer standing. The commanded response can then coexist with a reading of reciprocal honoring rather than bare submission.
- trace:
  - 106:3 **فَلْيَعْبُدُوا۟** ع ب د B006: Honoring and magnifying supply a reciprocal register alongside humble worship.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B008: A house of honor supplies the social space in which provision and protection confer standing.
  - 106:4 **أَطْعَمَهُم** ط ع م B004: Good condition and generous provision turn feeding into maintained dignity, not survival alone.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Trust and safe-conduct supply the protected status of those received under honor.

## grafted collective
- reading: As a contained material analogy, nourishment and security let a joined collective take, survive, and become continuous with a sustaining whole.
- mechanism: 
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B010: A graft accepting insertion supplies the material analogy of a vulnerable attachment taking within a living stock.
  - 106:1 **لِإِيلَٰفِ** ء ل ف B002: Joining supplies the social operation corresponding to grafted incorporation.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Security supplies the stable environment in which the joined element can take and endure.

## release of constriction
- reading: The paired reliefs can be felt as reopening two constricted channels: intake blocked by deprivation and action constricted by fear.
- mechanism: 
- trace:
  - 106:4 **أَطْعَمَهُم** ط ع م B012: The seized and squeezed throat supplies the negative bodily state that feeding reverses by reopening intake.
  - 106:4 **جُوعٍ** ج و ع B001: The empty stomach keeps the image tied to actual bodily deprivation rather than free metaphor.
  - 106:4 **خَوْفٍۭ** خ و ف B005: Fear visibly manifest on the body supplies a parallel affective constriction.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Settled safety supplies release and bodily-affective easing on the second side.

## route kept on course
- reading: Security also resonates as preservation of directed movement: threat does not force the recurrent route off course.
- mechanism: 
- trace:
  - 106:2 **وَٱلصَّيْفِ** ص ي ف B005: Deviation from an intended course supplies the latent failure mode that secure passage prevents.
  - 106:2 **رِحْلَةَ** ر ح ل B001: Travel gives that possible deviation a concrete route on which to operate.
  - 106:4 **خَوْفٍۭ** خ و ف B001: Anticipated harm supplies the pressure that could divert or halt movement.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: Safe-conduct supplies continuity toward the intended destination.

## provisioned protective container
- reading: As a tightly contained image-schema, the collective is both filled from within by provision and covered from without by refuge.
- mechanism: 
- trace:
  - 106:4 **خَوْفٍۭ** خ و ف B006: The carrier's pouch or cover supplies a concrete enclosing schema latent at the fear root.
  - 106:3 **ٱلْبَيْتِ** ب ي ت B001: Shelter scales the enclosing schema from a carried cover to collective refuge.
  - 106:4 **أَطْعَمَهُم** ط ع م B002: Feeding supplies what is placed within and sustained by the enclosure.
  - 106:4 **وَءَامَنَهُم** ء م ن B001: A place of safety validates the enclosure's protective function.
