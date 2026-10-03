Surah: 90. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S90 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s090/surah.r2/text.md =====
# Surah 90

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/s090/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق س م (root_001226): 90:1 أُقْسِمُ

- **B001** yüz güzelliği — güzellik, güzel görünüş · eksiksiz güzellik · yüz, özellikle yüzün güzel bölümü · yakışıklı ya da güzel yaradılışlı erkek · güzel yüzlü · yüzü güzel ve uyumlu · güzel yüz · güzel yüzlü kadın · güzel
  القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)
- **B002** şiddetli öğle sıcağı veya vakti — şiddetli öğle sıcağı veya öğle sıcağı vakti
  والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)
- **B003** paylara ayırma ve ayrılmış pay — bir şeyi parçalara veya paylara ayırmak · paylara ayırma · pay, kişiye düşen bölüm · bölüştürme, paylaşma · arazi veya evleri paylaştıran kimse · birlikte paylaşan ortak · öteki araziden ayrılmış arazi · az suyu eşit paylaştırmaya yarayan taş · kişilere ayrılmış paylar · ayırma ve dağıtma · zaman onları ayırıp dağıttı
  تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)
- **B004** yemin etme ve öldürme davasında paylaştırılan yeminler — yemin · yemin etti · ona yemin etti veya onunla antlaştı · Tanrı adına karşılıklı yemin ettiler · öldürme davasında yakınlara paylaştırılan yeminler
  اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)
- **B005** işaretli ok çekerek karar arama [kalıp] — işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme
  الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)
- **B006** işi ölçüp biçme; kaygıyla zihnin dağılması — işini ölçüp biçiyor ve nasıl yapacağını düşünüyor · kaygının dağıttığı zihin · kaygılar yüzünden düşüncesi dağılmış
  أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)
- **B007** yalıtık adlandırmalar — giysiyi ilk kez katlayıp kat izlerini oluşturan kimse · iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at
  القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)
- **B008** düşman ile Müslümanlar arasındaki ateşkes — düşman ile Müslümanlar arasındaki ateşkes
  القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)

## ب ل د (root_000148): 90:1 ٱلْبَلَدِ, 90:2 ٱلْبَلَدِ

- **B001** sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan — yerleşilmiş ya da boş, sınırları belirli yer · yerler, yöreler · mezarlık, mezar veya toprak · açık, çıplak alan
  البلد معروف والبلدة أيضا والبلاد جمع بلد (jamhara)؛ البلد كل موضع مستحيز من الأرض عامر أو غير عامر أو خال أو مسكون (tahdhib)؛ البلد المكان المحيط المحدود المتأثر باجتماع قطانه وإقامتهم فيه (mufradat)؛ البلد المقبرة ويقال هو نفس القبر وربما جاء البلد يعني به التراب (tahdhib)؛ من البلد وهو الفضاء البراز (maqayis)
- **B002** göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma — boğazın altındaki göğüs çukuru ve çevresi · göğüs · deve çökerken göğsünü yere koydu
  بلدة النحر وسطه (jamhara)؛ البلدة الصدر وفلان واسع البلدة أي واسع الصدر (sihah)؛ البلدة بلدة النحر وهي الثغرة وما حولها (tahdhib)؛ سميت الكركرة بلدة لذلك وربما استعير ذلك لصدر الإنسان (mufradat)؛ الأصل الصدر ويقال وضعت الناقة بلدتها بالأرض إذا بركت (maqayis)
- **B003** kaşların arasındaki açıklık ve kaşları birleşmemiş olma — kaşların arasındaki açık ve temiz bölge · kaşları birleşmemiş
  ربما سميت البلجة بلدة (jamhara)؛ البلدة والبلدة نقاوة ما بين الحاجبين ورجل أبلد أي أبلج بين البلد (sihah)؛ الأبلد من الرجال الذي ليس بمقرون وهي البلدة والبلدة (tahdhib)؛ البلدة البلجة ما بين الحاجبين تشبيها بالبلد لتمددها (mufradat)؛ الأبلد الذي ليس بمقرون الحاجبين يقال لما بين حاجبيه بلدة (maqayis)
- **B004** yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı — Ay durağı veya yıldızsız gök bölgesi · göksel aslanın göğüs bölgesi
  البلدة منزل من منازل القمر (jamhara)؛ البلدة من منازل القمر وهي ستة أنجم من القوس (sihah)؛ البلدة في السماء موضع لا نجوم فيه بين النعائم وسعد الذابح (tahdhib)؛ البلدة منزل من منازل القمر (mufradat)؛ البلدة النجم يقولون هو بلدة الأسد أي صدره (maqayis)
- **B005** şaşkınlıkla duraksama; metaneti yitirip boyun eğme — şaşkınlığa düşüp kararsızca duraksamak · bir işte şaşırıp ne yapacağını bilememek · metaneti yitirip sinme ve boyun eğme
  تبلد الرجل من هذا إذا لحقته حيرة فضرب بيده على بلدة نحره (jamhara)؛ تبلد أي تردد متحيرا (sihah)؛ المتبلد الذي يتردد متحيرا (tahdhib)؛ التبلد نقيض التجلد وهو استكانة وخضوع (tahdhib)؛ قيل للمتحير بلد في أمره وأبلد وتبلد (mufradat)؛ تبلد الرجل إذا وضع يده على صدره عند تحيره في الأمر (maqayis)
- **B006** bedende, deride veya başka bir yüzeyde kalan iz — bedende veya başka bir yüzeyde kalan iz; izler
  البلد الأثر في البدن وغيره والجمع أبلاد (jamhara)؛ البلد الأثر والجمع أبلاد (sihah)؛ البلد الأثر بالجسد وجمعه أبلاد (tahdhib)؛ ولاعتبار الأثر قيل بجلده بلد أي أثر وجمعه أبلاد (mufradat)؛ البلد الأثر وجمعه أبلاد (maqayis)
- **B007** kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma — zeka, kavrayış ve atılganlık düşüklüğü · ağır kavrayışlı; yarışta geri kalan · işte ve cömertlikte gerileyip güçsüzleşti
  رجل بليد بين البلادة ضد النحرير (jamhara)؛ البلادة ضد الذكاء وقد بلد بالضم فهو بليد (sihah)؛ أبلد الرجل إذا كانت دابته بليدة (sihah)؛ البلادة نقيض النفاذ والمضاء في الأمور (tahdhib)؛ فرس بليد إذا تأخر عن الخيل السوابق (tahdhib)؛ بلد إذا نكس في العمل وضعف حتى في الجود (tahdhib)؛ لكثرة وجود البلادة فيمن كان جلف البدن (mufradat)
- **B008** iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı — iri ve kaba yapılı · enli; deve için sert ve dayanıklı
  رجل أبلد غليظ الخلق (jamhara)؛ الأبلد الرجل العظيم الخلق والبلندى العريض والمبلندى من الجمال الصلب الشديد (sihah)؛ رجل أبلد عبارة عن عظيم الخلق (mufradat)
- **B009** bir yerde kalıp ikamet etme ve orada oturan kişi — bir yerde kalıp ikamet etmek · bir yerde oturan, sakin
  بلد بالمكان أقام به فهو بالد (sihah)؛ بلدت بالمكان أبلد بلودا أي أقمت به (tahdhib)؛ بلد لزم البلد (mufradat)؛ البالد قياسا المقيم بالبلد (maqayis)
- **B010** kendini yere atıp yapışma; yere yapışık eski havuz — kendini yere atmak veya yere yapışmak · yere yapışık eski havuz
  بلد تبليدا ضرب بنفسه الأرض وأبلد لصق بالأرض (sihah)؛ المبلد الحوض القديم ههنا وأراد ملبد فقلب وهو اللاصق بالأرض (tahdhib)؛ بلد الرجل بالأرض إذا لزق بها (maqayis)؛ مبلد بين موماة يذكر حوضا لاصقا بالأرض (maqayis)
- **B011** kılıç veya sopalarla karşılıklı vuruşma — kılıç veya sopalarla karşılıklı dövüşme
  المبالدة مثل المباطلة (sihah)؛ المبالدة كالمبالطة بالسيوف والعصي إذا تجالدوا بها (tahdhib)؛ المبالدة بالسيوف مثل المبالطة وقال بعضهم اشتق من الأول كأنهم لزموا الأرض فقاتلوا عليها (maqayis)
- **B012** deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası — deve kuşunun yumurta çukuru · deve kuşunun bırakıp gittiği yumurta
  البلد أدحي النعام يقال هو أذل من بيضة البلد أي من بيضة النعام التي تتركها (sihah)

## ح ل ل (root_000351): 90:2 حِلٌّۢ

- **B001** düğümü çözme [kalıp] — düğümü açıp çözmek
  حللت العقدة أحلها حلا (maqayis;ayn;tahdhib); فتحتها فانحلت (sihah); أصل الحل حل العقدة (mufradat)
- **B002** bir yere konup yerleşme — bir yere inip konaklamak · konak yeri ya da bağlama göre varış veya vade noktası · topluluğun konakladığı yer · konmuş topluluk ya da topluluğun konduğu yer · sık sık bir yere konan topluluk · sık konaklanan, konmaya elverişli yer · az olmayan ya da başka yoruma göre üzerine konaklanmamış
  وحل نزل (maqayis); المحل نقيض المرتحل والمحلة منزل القوم (ayn;tahdhib); الحلة القوم الحلول والحلة موضع (jamhara); حل بالمكان حلا وحلولا ومحلا (sihah); الحلة القوم النازلون والمحلة مكان النزول (mufradat)
- **B003** yasağın kalkması ve izinli duruma gelme — yasak olmayan, izin verilmiş · kutsal bölge veya törensel yasak dışında olma durumu · törensel yasak ya da koruma anlaşması altında olmayan kişi · bir şeyi izinli kılmak · bir şeyi izinli saymak
  الحلال ضد الحرام (maqayis); الحل الحلال نفسه ورجل حل من الإحرام (ayn); الحل بالكسر الحلال والحل ما جاوز الحرم وأحللت له الشيء واستحل الشيء (sihah); الحل الرجل الحلال والمحل الذي لا عهد له ولا حرمة (tahdhib); عن حل العقدة استعير حل الشيء حلالا وأحل الله كذا (mufradat)
- **B004** vadesi gelme veya gerçekleşme — konak yeri ya da bağlama göre varış veya vade noktası · borcun vadesi gelmek · hakkın yerine getirilmesi zorunlu olmak · ceza zorunlu hale gelmek ya da inmek · kurbanlık kesileceği yere ya da zamana ulaşmak
  وحل الدين وجب (maqayis); حل عليه الحق يحل محلا وحلت العقوبة عليه وجبت (ayn); حل العذاب أي وجب ويحل أي نزل وحل الدين يحل حلولا (sihah); من يحل فمعناه يجب ومن قرأ فيحل فمعناه فينزل ومحل الهدي (tahdhib); حل الدين وجب أداؤه وبلغ الأجل محله (mufradat)
- **B005** anttan çıkma ve en az gereği yerine getirme [kalıp] — ant bağını çözecek en az miktar · anttan istisna ya da çözücü bir işlemle çıkma · aşırıya kaçmadan hafifçe vurmak · az olmayan ya da başka yoruma göre üzerine konaklanmamış
  حللت اليمين تحليلا وتحلة وتحلة القسم (maqayis); التحليل والتحلة من اليمين وضربته ضربا تحليلا (ayn); تحلل في يمينه أي استثنى وما فعلته إلا تحلة القسم (sihah); أصل هذا من تحليل اليمين ثم يجعل ذلك مثلا للتقليل (tahdhib); تحلة أيمانكم أي ما تنحل به عقدة أيمانكم وتحليل أي شيء يسير (mufradat)
- **B006** eş veya birlikte oturan yakın kişi — erkek eş ya da birlikte oturan komşu · kadın eş ya da birlikte oturan komşu kadın
  حليل المرأة بعلها وحليلة المرء زوجه وكل من نازلك وجاورك فهو حليل (maqayis); الحليل والحليلة الزوج والمرأة لأنهما يحلان في موضع واحد (ayn); الحليل الزوج والحليلة الزوجة ولمن يحاله في دار واحدة (sihah); الحليل والحليلة الزوجان وكل من نازلك أو جاورك فهو حليلك (tahdhib); الحليل الزوج وإما لنزوله معه والحليلة الزوجة (mufradat)
- **B007** en az iki parçalık giysi takımı — birlikte giyilen iki ya da daha çok parçalık giysi takımı
  الحلة معروفة وهي لا تكون إلا ثوبين (maqayis); الحلة إزار ورداء ولا يقال لها حلة حتى تكون ثوبين (ayn); الحلل برود اليمن والحلة إزار ورداء (sihah); الحلة إزار ورداء لا تسمى حلة حتى تكون ثوبين (tahdhib); الحلة إزار ورداء (mufradat)
- **B008** idrar veya süt çıkış kanalı — idrarın ya da sütün çıktığı kanal
  الإحليل مخرج البول ومخرج اللبن من الضرع (maqayis;ayn;sihah); الإحليل مخرج اللبن وإحليل الذكر ثقبه الذي يخرج منه البول (tahdhib); الإحليل مخرج البول لكونه محلول العقدة (mufradat)
- **B009** doğum olmadan memeye süt inmesi [kalıp] — koyunun doğurmadan sütü inmek · doğurmadan memesine süt inmiş koyun
  أحلت الشاة إذا نزل اللبن في ضرعها من غير نتاج (maqayis;ayn;sihah;mufradat); المحال الغنم التي ينزل اللبن في ضروعها من غير نتاج وأحل المال إذا نزل دره (tahdhib)
- **B010** yeni doğmuş oğlak veya küçük koyun yavrusu — oğlak ya da annesinin karnı yarılarak çıkarılan küçük yavru · küçük koyun yavrusu
  الحلان الجدي يشق له عن بطن أمه (maqayis); الحلان الجدي والذي يشق عنه بطن أمه (ayn); الحلان الجدي (sihah); الحلان الجدي الذي يبقر عنه بطن أمه والحلام والحلان واحد وهو ما يولد من الغنم صغيرا (tahdhib)
- **B011** yerinden kaldırma veya yerinden ayrılma [kalıp] — topluluğu yerinden kaldırıp uzaklaştırmak · deveyi özel bir çağrıyla yürütmek · bulunduğu yerden ayrılmak ya da kımıldamak
  تحلحل عن مكانه إذا زال (maqayis); حلحلت القوم أزلتهم عن موضعهم وحلحلت بالإبل إذا قلت حل (ayn); حلحلت القوم أي أزعجتهم وتحلحل عن مكانه أي زال (sihah); حلحلت بالإبل إذا قلت لها حل وحلحلت القوم إذا أزلتهم (tahdhib)
- **B012** sağlam karakterli ve yiğit önder — sağlam duruşlu, yiğit ve eli açık önder
  الحلاحل السيد وهو من الباب ليس بمنغلق محرم كالبخيل (maqayis); الحلاحل السيد الشجاع (ayn); الحلاحل السيد الركين (sihah;tahdhib)
- **B013** taşınabilir yol ve konak takımı — yol yükü ya da kadınların kullandığı yolculuk taşıtı · istenen yerde konmaya yarayan taşınabilir araç takımı
  الحلال متاع الرحل والحلال مركب من مراكب النساء (maqayis); الحلال متاع رحل البعير والمحلتان القدر والرحى والمحلات القدر والرحى والدلو والشفرة والفأس والقداحة والقربة (sihah); الحلال متاع الرحل والمحلات أدوات حل حيث شاء (tahdhib)
- **B014** deve veya atta arka ayak bileği gevşekliği — deve veya atın arka ayak bileğindeki zayıflık ve gevşeklik · arka ayak bileği gevşek ve zayıf deve veya at
  الحلل في البعير ضعف في عرقوبه والأحل الذي في رجله استرخاء (sihah); إذا كان في عرقوبي البعير ضعف فهو أحل وبه حلل وفرس أحل وحلله ضعف نساه ورخاوة كعبيه (tahdhib)
- **B015** susam yağı — susam yağı
  الحل دهن السمسم (sihah)

## ECHO ح ل ي (root_000353): for 90:2 حِلٌّۢ: withheld observed target; not identity

- **B001** takı, süsleme parçası ve bunları takma — kadının taktığı ziynet eşyaları · takı veya nesneye eklenen süsleme parçası · kadın takılarını taktı · bileziklerle süslendi · takı takmış ve süslenmiş kadın
  الحلي حلى المرأة (maqayis)؛ الحلي كل حلية حليت به امرأة أو سيفا أو نحوه والجميع حلي (ayn)؛ الحلي جمع الحلي؛ يحلون فيها من أساور؛ وحلوا أساور؛ في الحلية (mufradat)
- **B002** nitelik ve yüzü betimleme — nitelik veya betimleyici özellik · bir erkeğin yüzünü betimleme
  هذه حلية الشيء أي صفته؛ حلية السيف (maqayis)؛ الحلية تحليتك وجه الرجل إذا وصفته (ayn)
- **B003** birinden iyilik görmek [kalıp] — birinden iyilik görmek
  حلي منه بخير يحلى حلى مقصور إذا أصاب خيرا (ayn)
- **B004** bir ot türünün kurusu ve ekin benzeri bitki — bir ot türünün kurusu ve ekine benzeyen bitki
  الحلي يبيس النصي وكل نبات يشبه نبات الزرع (ayn)

## ECHO  (): for 90:2 حِلٌّۢ: non-dominant observed target (1 occ.); not identity

- () no Turkish dictionary entry

## و ل د (root_001683): 90:3 وَوَالِدٍ, 90:3 وَلَدَ

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

## خ ل ق (root_000434): 90:4 خَلَقْنَا

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

## ء ن س (root_000059): 90:4 ٱلْإِنسَٰنَ

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

## ك ب د (root_001280): 90:4 كَبَدٍ

- **B001** karaciğer — karaciğer · birinin karaciğerine isabet ettirmek · karaciğer ağrısı veya hastalığı
  الكبد معروفة (maqayis;jamhara;tahdhib;mufradat)؛ الأكباد جمع كبد وهي اللحمة السوداء في البطن (ayn)؛ الكبد والكبد واحدة الأكباد (sihah)؛ موضعها من ظاهر يسمى كبدا (ayn;tahdhib)؛ كبدت الرجل أصبت كبده (maqayis;sihah;mufradat)؛ الكباد وجع الكبد (maqayis;jamhara;sihah;tahdhib)
- **B002** zorluk çekme ve çetinliğe dayanma — şiddetli zorluk ve meşakkat · zorluk ve meşakkat içinde · çetin bir işi güçlük içinde göğüslemek · güçlük çekerek göğüsleme · gecenin dehşetine ve güçlüğüne dayanmak · elle çevrilen zahmetli değirmen taşı
  أصل صحيح يدل على شدة في شيء وقوة (maqayis)؛ الكبد وهي المشقة (maqayis;mufradat)؛ وكابدت الأمر قاسيته في مشقة (maqayis)؛ كابدت الشيء مكابدة وكبادا وهو مقاساتك إياه في مشقة (jamhara)؛ كابدت الأمر إذا قاسيت شدته (sihah)؛ مكابدة الأمر معاناته ومشقته (tahdhib)؛ الكبد الشدة (jamhara;sihah;tahdhib)؛ الكبداء الرحا التي تدار باليد سميت كبداء لما في إدارتها من المشقة (tahdhib)
- **B003** bir şeyin ortası, o ortaya yönelme ve bir işi amaçlama [kalıp] — göğün ortası · göğün küçük orta bölgesi · güneş göğün ortasına geldi · yıldız göğün ortasına geldi · kâğıdın ortası · işe yönelmek ve onu amaçlamak · çölün orta ve ana bölümüne yönelmek
  كبد السماء وسطها (maqayis;sihah;mufradat)؛ تكبدت الشمس إذا صارت في كبد السماء (maqayis;sihah;mufradat)؛ كل شيء توسط شيئا فقد تكبده (jamhara)؛ كبد كل شيء وسطه (tahdhib)؛ وضعه في كبد القرطاس (tahdhib)؛ تكبد الفلاة إذا قصد وسطها ومعظمها (tahdhib)
- **B004** yayın kabzası ve okun dayandığı üst bölümü [kalıp] — yayın kabzası veya okun dayandığı kabza üstü · kabzası kalın ve avucu dolduran yay
  كبد القوس مقبضها (maqayis;sihah)؛ الكبد كبد القوس وهو مقبضها حيث يقع السهم على كبد القوس (ayn)؛ قوس كبداء يملأ عجسها كف الرامي (jamhara)؛ كبد القوس فويق مقبضها حيث يقع السهم (tahdhib)؛ قوس كبداء غليظة الكبد شديدتها (tahdhib)
- **B005** içeceğin koyulaşıp pıhtılaşması [kalıp] — sütün koyulaşıp pıhtılaşması · karaciğere benzer yoğunlukta pıhtılaşmış süt
  تكبد اللبن غلظ وخثر (maqayis;sihah)؛ تكبد اللبن وغيره من الشراب إذا غلظ وخثر (jamhara)؛ اللبن المتكبد الذي يخثر حتى يصير كأنه كبد يترجرج (tahdhib)
- **B006** orta bölümü iri, geniş veya çıkıntılı olma — orta bölgesi çıkıntılı, iri veya geniş karınlı · orta bölgesi iri veya belirgin olan dişil varlık
  الأكبد الذي نهد موضع كبده (maqayis)؛ الأكبد الناهد موضع الكبد (ayn;tahdhib)؛ الأكبد الواسع الجوف فرس أكبد والأنثى كبداء (jamhara)؛ الأكبد الضخم الوسط (sihah)؛ امرأة كبداء بينة الكبد (sihah)؛ رملة كبداء عظيمة الوسط وناقة كبداء كذلك (tahdhib)
- **B007** kara karaciğerli düşmanlar [kalıp] — kara karaciğerli düşmanlar
  يقال للأعداء سود الأكباد (sihah;tahdhib)؛ كأن العداوة أحرقت أكبادهم فاسودت (tahdhib)؛ الكبد معدن العداوة (tahdhib)
- **B008** bir kimseye ulaşmak için yolculuğa çıkmak [kalıp] — bilgi veya başka bir amaç için birinin yanına yolculuk etmek
  فلان تضرب إليه أكباد الإبل أي يرحل إليه في طلب العلم وغيره (sihah)
- **B009** dik ve düzgün yaratılmış olma [kalıp] — dik, düzgün ve dengeli yaratılmış halde
  خلقناه منتصبا معتدلا (tahdhib)؛ الكبد الاستواء والاستقامة (tahdhib)

## ح س ب (root_000318): 90:5 أَيَحْسَبُ, 90:7 أَيَحْسَبُ

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

## ق د ر (root_001205): 90:5 يَقْدِرَ

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

## ء ح د (root_000017): 90:5 أَحَدٌ, 90:7 أَحَدٌ

- **B001** tek ve eşi olmayan olma — bir tane; tek ve eşsiz · yalnız bir, yalnız bir
  أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)
- **B002** hiç kimse — olumsuzlukta hiç kimse
  لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)
- **B003** bir sayısı, onlu kuruluşları ve on bire çıkarma — saymanın başlangıcındaki bir · on bir, on bir dişil biçimi ve yirmi bir · onları on bire çıkarmak
  أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)
- **B004** iki kişiden biri, ilk olan ve haftanın ilk günü — ikinizden biri · Pazar günü · Pazar günleri
  أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)
- **B005** tek başına kalma ve birer birer gelme — tek başına kalmak; işi yalnız üstlenmek · birer birer, ayrı ayrı
  ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)
- **B006** Medine'deki belirli bir dağın özel adı — Medine'deki dağın özel adı
  أحد جبل بالمدينة (sihah)

## ق و ل (root_001272): 90:6 يَقُولُ

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

## ECHO ق ل ل (root_001251): for 90:6 يَقُولُ: withheld observed target; not identity

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

## ه ل ك (root_001596): 90:6 أَهْلَكْتُ

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

## م و ل (root_001457): 90:6 مَالًا

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ل ب د (root_001340): 90:6 لُّبَدًا

- **B001** üst üste yığılıp keçeleşme — keçeleşmiş saç ya da yün malzemesi · keçeleşmiş malzemeden bir parça · serilen ya da giyilen keçe örtüler · yağmurda giyilen keçe giysi · aslanın sık ve yığılmış yelesi · ata keçe örtü bağlamak · eyere keçe yapmak veya koymak · saçın toplanıp birbirine yapışması · dinsel hazırlık sırasında saçı yapışkan bir maddeyle sabitleme · yağmur veya çiyle yer yüzeyinin sıkışıp yapışması · yaprakların üst üste yığılması · yamalı giysi veya örtü · bir şeyi başka bir şeye sıkıca yapıştırıp üst üste bindirmek
  أصل يدل على تكرس الشيء بعضه فوق بعض (maqayis)؛ اللبد وهو معروف (maqayis)؛ اللبد واحد اللبود واللبدة أخص منه (sihah)؛ كل شعر أو صوف يتلبد فهو لبد ولبدة (tahdhib)؛ لبد الشعر (mufradat)؛ الأسد ذو لبدة (maqayis;sihah;tahdhib;mufradat)؛ ألبدت الفرس وألبدت السرج (sihah;tahdhib;mufradat)؛ اللبادة ما يلبس منها للمطر (sihah)؛ اللبادة لباس من لبود وهذه اللبود التي تفترش (tahdhib)؛ تلبدت الأرض بالمطر ولبد الندى الأرض (sihah;tahdhib)؛ التبد الورق أي تلبد بعضه على بعض (sihah)؛ إذا رقع الثوب فهو ملبد وملبود وكساء ملبد أي مرقع (tahdhib)؛ التلبيد أن يجعل المحرم في رأسه شيئا من صمغ ليتلبد شعره (sihah;tahdhib)
- **B002** üst üste binen kalabalık veya yığılmış çokluk — üst üste binecek kadar sıkışmış kalabalık · çok ve yığılmış mal varlığı
  صار الناس عليه لبدا إذا تجمعوا عليه (maqayis)؛ يقول أهلكت مالا لبدا أي جما (sihah)؛ الناس لبد أي مجتمعون (sihah)؛ اللبد الكثير ومال لبد كثير وقد لبد بعضه ببعض (tahdhib)؛ كادوا يكونون عليه لبدا والمعنى أن يسقطوا عليه ومعنى لبدا يركب بعضهم بعضا (tahdhib)؛ يكونون عليه لبدا أي مجتمعة (mufradat)؛ مالا لبدا أي كثيرا متلبدا (mufradat)
- **B003** yerinden ayrılmadan kalma veya yüzeye yapışma — bir yerde kalmak ve oradan ayrılmamak · bir yerde yerleşip sabit kalmak · evinden ayrılmayan ve yolculuk etmeyen kimse · evinden dışarı çıkmayan kimse · yere yapışmak veya yerde sabit kalmak · kuşun yere çöküp yapışık durması · sağım kabını memeye sıkıca bastırmak
  ألبد بالمكان أقام به واللبد الرجل لا يفارق منزله (maqayis)؛ من ألبد بالمكان إذا أقام (maqayis-cont)؛ ألبد بالمكان أقام به (sihah;tahdhib;mufradat)؛ اللبد أيضا الذي لا يسافر ولا يبرح (sihah)؛ لبد الشيء بالأرض لبودا تلبد بها أي لصق (sihah)؛ تلبد الطائر بالأرض أي جثم عليها (sihah)؛ السمانى وهي لابدة بالأرض أي لاصقة (tahdhib)؛ الملبد أيضا اللاصق بالأرض (tahdhib)؛ ألبد ألصق العلبة بالضرع (tahdhib)؛ لبد بالأرض لبودا (maqayis)
- **B004** küçük torba ve tuluma keçe kılıf geçirme — küçük heybe türü torba veya tuluma dikilen keçe kılıf · su tulumunu küçük torba ya da keçe kılıfın içine geçirmek
  اللبيد الجوالق (maqayis)؛ ألبدت القربة إذا صيرتها فيه (maqayis;maqayis-cont)؛ اللبيد الجوالق الصغير (sihah)؛ ألبدت القربة جعلتها في لبيد وهو الجوالق الصغير (sihah;tahdhib;mufradat)؛ اللبيد لبد يخاط عليه (tahdhib)
- **B005** devenin kuyruğuyla yapışık atık tabakası oluşturması — devenin kuyruğuyla dışkısını sağrısına yapıştırması · kuyruk hareketiyle dışkısı uyluklarına yapışmış erkek deve
  ألبد البعير إذا ضرب بذنبه على عجزه وقد ثلط عليه فيصير على عجزه كاللبدة (maqayis;maqayis-cont)؛ ألبد البعير إذا ضرب بذنبه على عجزه وقد ثلط عليه وبال فيصير على عجزه لبدة من ثلطه وبوله (sihah)؛ الملبد الفحل من الإبل يضرب فخذيه بذنبه فيلصق بهما ثلطه وبعره (tahdhib)؛ ألبد البعير صار ذا لبد من الثلط (mufradat)
- **B006** develerin semirmeye hazırlanması veya aşırı ottan sıkıntılanması [kalıp] — develerin baharla iyi görünüp semirmeye hazırlanması · develerin fazla veya sert ottan göğüs ve boğaz sıkıntısı çekmesi · fazla ot yemekten sıkıntılanmış deve veya deve topluluğu
  ألبدت الإبل إذا تهيأت للسمن (maqayis;maqayis-cont)؛ ألبدت الإبل إذا أخرج الربيع ألوانها وأوبارها وتهيأت للسمن (sihah;tahdhib)؛ لبدت الإبل إذا دغصت من الصليان وهو التواء في حيازيمها وفي غلاصمها (sihah;tahdhib)؛ هذه إبل لبادى وناقة لبدة (sihah;tahdhib)؛ لبدت الإبل لبدا أكثرت من الكلإ حتى أتعبها (mufradat)؛ قد يكنى بذلك عن حسنه لدلالة ذلك منه على خصبه وسمنه (mufradat)
- **B007** hiçbir şeyi olmamak [kalıp] — hiçbir şeyi veya ne az ne çok herhangi bir varlığı olmamak
  ما له سبد ولا لبد السبد الشعر واللبد الصوف أي ما له شيء (sihah)؛ ما له سبد ولا لبد ومعناه ما له قليل ولا كثير وقيل السبد من الشعر واللبد من الصوف (tahdhib)؛ ما له سبد ولا لبد (mufradat)
- **B008** kartala ve şaire verilmiş iki özel ad — belirli bir anlatıdaki son kartalın özel adı · belirli bir kabileye mensup şairin özel adı
  لبد آخر نسور لقمان (maqayis)؛ لبد آخر نسور لقمان (sihah;tahdhib;mufradat)؛ لبيد اسم شاعر من بني عامر (sihah)

## ر ء ي (root_000531): 90:7 يَرَهُۥٓ

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

## ECHO ر و ي (root_000615): for 90:7 يَرَهُۥٓ: withheld observed target; not identity

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

## ج ع ل (root_000248): 90:8 نَجْعَل

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

## ع ي ن (root_001069): 90:8 عَيْنَيْنِ

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

## ل س ن (root_001355): 90:9 وَلِسَانًا

- **B001** konuşma organı ve söyleyiş gücü — konuşma organı olan dil ve onun söyleyiş gücü · konuşma organı anlamındaki dilin çoğulu · konuşma organı anlamındaki dilin çoğulu
  اللسان معروف وهو مذكر والجمع ألسن (maqayis)؛ اللسان ما ينطق يذكر ويؤنث والألسن والألسنة (ayn)؛ اللسان جارحة الكلام (sihah)؛ اللسان يذكر ويؤنث وجمعه ألسن وألسنة (tahdhib)؛ اللسان الجارحة وقوتها (mufradat)
- **B002** birine sözle sataşma — birine sözle sataşmak veya çıkışmak · bana sözle sataştı veya üzerime geldi
  لسنته إذا أخذته بلسانك (maqayis)؛ لسن فلان فلانا يلسنه أي أخذه بلسانه (ayn)؛ لسنته إذا أخذته بلسانك (sihah)؛ لسنت الرجل ألسنه لسنا إذا أخذته بلسانك (tahdhib)
- **B003** açık ve etkili konuşma yetkinliği — açık, düzgün ve etkili konuşma yetkinliği · açık ve etkili konuşan · daha açık, etkili ve gerekçesi güçlü konuşan
  اللسن جودة اللسان والفصاحة (maqayis)؛ رجل لسن بين اللسن (ayn)؛ اللسن الفصاحة وقد لسن فهو لسن وألسن (sihah)؛ رجل لسن بين اللسن إذا كان ذا بيان وفصاحة (tahdhib)؛ أفصح وأبين كلاما وأقدر على الحجة (mufradat)
- **B004** dil ucunu andıran ince ve uzunca biçim — ucu dil gibi olan; ince ve hafif uzun · ön ucu dil biçiminde, ince ve uzunca ayakkabı · ince ve hafif uzun ayak
  أصل يدل على طول لطيف غير بائن ونعل ملسنة على صورة اللسان وقدم ملسنة فيها لطافة وطول يسير (maqayis)؛ شيء ملسن جعل طرفه كطرف اللسان (ayn)؛ الملسن من النعال الذي فيه طول ولطافة على هيئة اللسان وامرأة ملسنة القدمين (sihah)؛ نعل ملسنة إذا جعل طرف مقدمها كطرف اللسان (tahdhib)
- **B005** dil ucunun kesilmesi — kişinin dil ucunu kesmek · dilinin ucu kesilmiş kişi
  لسن الرجل أي قطع طرف لسانه فهو ملسون (ayn)
- **B006** bir topluluğun dili ve konuşması — bir topluluğun dili ve konuşması · bir topluluğun konuştuğu dil · söz, sözcük, haber veya ileti · topluluk adına konuşan kişi, topluluğun sözcüsü · insanların kişi hakkında söylediği övgü · farklı diller ve konuşma sesleri
  اللسن اللغة ويعبر بالرسالة عن اللسان (maqayis)؛ اللسان الكلام (ayn)؛ يكنى بها عن الكلمة واللسن اللغة لكل قوم لسن (sihah)؛ لكل قوم لسن أي لغة ولسان الناس عليك ثناؤهم ولسان بني عامر الكلمة أو الخبر (tahdhib)؛ لكل قوم لسان ولسن أي لغة واختلاف الألسنة إشارة إلى اختلاف اللغات والنغمات (mufradat)
- **B007** ödünç yavruyla dişi devenin sütünü indirtme — ödünç yavruya süt tattırıp onu uzaklaştırarak dişi devenin sütünü indirtme · bu işlem için ödünç yavru verilen yavrusuz dişi deve
  التلسين أن يعير الرجل الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis)؛ التلسين أن يعير الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis-routing)؛ الخلية من الإبل يقال لها المتلسنة وهو التلسن (tahdhib)
- **B008** iletiyi ulaştırma — iletiyi ulaştırma · o kişiden veya o kişiye haberi benim için ilet · o kişiyle ilgili sözü benim için ilet
  يعبر بالرسالة عن اللسان (maqayis)؛ الإلسان إبلاغ الرسالة وألسني فلانا وألسن لي فلانا كذا أي أبلغ لي (tahdhib)
- **B009** lifi ezip şeritlere ayırarak büküme hazırlama — lifi ezip ince şeritler hâline getirerek büküme hazırlamak · lifi ezip ince şeritlere ayırarak büküme hazırlama
  لسنت الليف إذا مشنته ثم جعلته فتائل مهيأة للفتل ويسمى ذلك التلسين (tahdhib)
- **B010** yalancı — yalancı; kullanımı tartışmalı
  الملسون الكذاب (sihah)؛ يقولون الملسون الكذاب وهذا مشتق من اللسان (maqayis)؛ الملسون الكذاب قال الشيخ لا أعرفه (tahdhib)

## ش ف ه (root_000804): 90:9 وَشَفَتَيْنِ

- **B001** dudak; dudak yapısı ve dudaksıl sesler — dudak; ağız kenarındaki organ · dudaklar · küçük dudak · organ adının eski son sessizini koruyan biçimi · dudakları kapanmayan adam · iri dudaklı adam · dudaksıl harfler; dudaklarla çıkarılan üç belirli harf
  الشفة حذفت منها الهاء وتصغيرها شفيهة والجميع الشفاه (ayn;tahdhib)؛ رجل أشفى إذا كان لا تنضم شفتاه (sihah)؛ رجل شفاهي عظيم الشفتين (sihah)؛ الحروف الشفهية الباء والفاء والميم (sihah)
- **B002** yüz yüze konuşma; olumsuz kalıplarda tek söz — yüz yüze konuşma; doğrudan sözlü iletişim · ona tek söz söylemedim · ondan tek söz işitmedim
  المشافهة بالكلام المواجهة من فيك إلى فيه (ayn)؛ المشافهة المخاطبة من فيك إلى فيه (sihah)؛ ما كلمته ببنت شفة أي بكلمة (sihah)؛ ما سمعت منه ذات شفة أي كلمة (tahdhib)
- **B003** meşgul etme; yoğun taleple tüketme veya kıtlaştırma — meşguliyet; uğraş · beni bundan alıkoydu · otlağı ve suyu senin kullanımından alıkoyuyoruz; ikisinde de fazlalık yok · ısrarlı istekleriyle beni tüketti · insanların üşüşerek azalttığı veya azlığından kullanımı engellenen su · insanların üşüştüğü veya çoğu tüketilmiş sular · az yiyecek · insanların istekleriyle elindekiler tüketilmiş adam · çok kalabalık bir ailen oldu ya da soru ve sözle bunaltıldın · bizden uzak, başkalarının yoğun talepleriyle meşgul · insanlardan az isteyen · o kişinin iyiliğinden sana düşen hiçbir şeyi meşgul edip tüketmedim
  ماء مشفوة أي مطلوب مسؤول وهو الذي كثر عليه الناس وأنفدوه إلا أقله (ayn)؛ طعام مشفوه أي قليل (ayn)؛ الشفه الشغل (sihah)؛ شفهني عن كذا أي شغلني (sihah)؛ خفيف الشفة أي قليل السؤال للناس (sihah)؛ رجل مشفوه إذا كثر سؤال الناس إياه حتى نفذ ما عنده (sihah)؛ ماء مشفوه وهو الذي كثر عليه الناس (tahdhib)؛ ما شفهت عليك من خير فلان شيئا (tahdhib)؛ فلان مشفوة عنا أي مشغول عنا مكثور عليه (tahdhib)؛ كان مشفوها أي كان قليلا (tahdhib)
- **B004** insanlar arasındaki iyi ad ve övgü [kalıp] — insanlar arasında iyi bir adı ve övgüsü var · insanların senin hakkındaki sözü ve övgüsü güzel
  له في الناس شفة أي ثناء حسن (sihah)؛ شفة الناس عليك لحسنة أي ذكرهم لك وثناءهم عليك حسن (tahdhib)

## ه د ي (root_001583): 90:10 وَهَدَيْنَٰهُ

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

## ECHO ه د د (root_001580): for 90:10 وَهَدَيْنَٰهُ: withheld observed target; not identity

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

## ن ج د (root_001473): 90:10 ٱلنَّجْدَيْنِ

- **B001** yüksek arazi — yüksek, sert veya engebeli arazi · yüksekliğiyle bilinen bölge · alçak yerden yüksek bölgeye çıkmak veya o bölgeye girmek · yüksek veya belirgin yol
  النون والجيم والدال أصل واحد يدل على اعتلاء وقوة وإشراف (maqayis)؛ النجد ما خالف الغور (ayn)؛ أصل النجد العلو من الأرض (jamhara)؛ النجد ما ارتفع من الأرض (sihah)؛ النجد المرتفع من الأرض (tahdhib)؛ النجد المكان الغليظ الرفيع (mufradat)
- **B002** belirginleşip açıklığa çıkma — iş açıklığa kavuştu ve belirginleşti · yolu iyi bilen kılavuz
  وأمر نجد واضح وطريق نجد هاد (ayn)؛ نجد الأمر نجودا فهو ناجد إذا وضح واستبان (tahdhib)؛ أنباء القرون التي مضت وأخبار غيب في القيامة تنجد أي تظهر (tahdhib)
- **B003** güç, cesaret ve destek — güçlü, cesur ve kararlı · cesaret, güç ve yardım · yardım isteyip yardım görmek · karşı karşıya gelip savaşmak · güçsüzlükten veya hastalıktan sonra güçlenmek
  نجد الرجل ينجد نجدة إذا صار شجاعا (maqayis)؛ استنجدته فأنجدني أي استغثته فأغاثني (maqayis)؛ رجل نجد أي ماض في أمره وشجاعته (ayn)؛ رجل نجد بين النجدة إذا كان جلدا قويا (jamhara)؛ استنجد فلان قوي بعد ضعف (sihah)؛ ناجدت فلانا بارزته بالقتال (tahdhib)؛ استنجدته طلبت نجدته فأنجدني (mufradat)
- **B004** işi hızlı ve başarıyla yürütme [kalıp] — bir işi hızlı ve başarıyla yürüten
  هو نجد في الحاجة أي خفيف فيها (maqayis)؛ رجل نجد أي ماض في أمره (ayn)؛ رجل نجد في الحاجة إذا كان ناجيا فيها أي سريعا (sihah)؛ رجل نجد في الحاجة إذا كان ناجحا فيها ناجيا (tahdhib)
- **B005** bunaltıcı sıkıntı ve güçlük — bunaltıcı sıkıntı, keder, darlık veya acı · sıkıntıya düşmüş veya güçlük altında kalmış · ağır güçlük veya maddi yük
  لاقى فلان نجدة أي شدة أمرا عاله (maqayis)؛ النجد الكرب والغم وهو منجود أي مكروب (ayn)؛ نجد الرجل فهو منجود إذا كرب من حر أو غم أو ضيق أو وجع (jamhara)؛ المنجود المكروب (sihah)؛ نجدتها ورسلها عسرها ويسرها (tahdhib)؛ قيل للمكروب والمغلوب منجود (mufradat)
- **B006** ter veya terleme — çalışma, korku veya sıkıntıdan çıkan ter
  النجد العرق (maqayis)؛ النجد العرق ونجد نجدا (ayn)؛ النجد العرق أيضا (jamhara)؛ نجد الرجل بالكسر ينجد نجدا أي عرق من عمل أو كرب (sihah)؛ نجد الرجل ينجد إذا عرق من عمل أو كرب (tahdhib)؛ النجد العرق (mufradat)
- **B007** uzun ve yüksek görünüşlü hayvan — uzun, yüksek görünüşlü veya sürüde öne çıkan hayvanlar
  النجود المشرفة من حمر الوحش (maqayis)؛ ناقة نجود تناجد الإبل فتغزر إذا غزرن (ayn)؛ النجود من حمر الوحش التي لا تحمل ويقال هي الطويلة المشرفة (sihah)؛ النجود الطويلة من الحمر (tahdhib)؛ النجود من الإبل التي تبرك على المكان المرتفع (tahdhib)
- **B008** evi kumaş ve döşemelerle süsleme — evi süsleyen kumaş, perde ve döşemelik eşya · evi kumaş ve döşemelerle süsleme · döşek, yastık ve yaygı ustası
  النجد ما نجد به البيت من متاع والتنجيد التزيين (maqayis)؛ بيت منجد ونجوده ستور تشد على حيطانه وسقوفه (ayn)؛ نجدت البيت تنجيدا إذا زينته وزخرفته (jamhara)؛ النجد ما ينجد به البيت من المتاع أي يزين (sihah)؛ بيت منجد إذا كان مزينا بالثياب والفرش (tahdhib)؛ النجاد ما يرفع به البيت (mufradat)
- **B009** omuzdan taşınan kılıç askısı — kılıcı omuzdan taşıyan askı kayışları · omuz çevresinde duran süslü kolyeler
  النجاد حمائل السيف لأنه يعلو العاتق (maqayis)؛ نجاد السيف محملاه اللذان طرفاهما في الابزيمين (ayn)؛ النجاد ما وقع على العاتق من حمالة السيف (jamhara)؛ النجاد حمائل السيف (sihah)؛ المناجد قلائد من لؤلؤ وذهب (tahdhib)؛ نجاد السيف ما يرفع به من السير (mufradat)
- **B010** deneyimle güçlenmiş kişi — deneyim kazanmış ve yaşadıklarıyla güçlenmiş
  المنجد الذي نجده الدهر إذا عرف وجرب (maqayis)؛ منجد مجرب قد نجده الدهر أي جرب وعرف (sihah)؛ منجد وهو الذي قد جرب الأمور وقاساها (tahdhib)؛ نجده الدهر أي قواه وشدده وذلك بما رأى فيه من التجربة (mufradat)
- **B011** içecek süzgeci veya kabı — içecek süzgeci veya içecek kabı; kimi aktarımlarda belirli bir sıvı
  الناجود الراووق نفسه (ayn)؛ الناجود كل إناء يجعل فيه الشراب (sihah)؛ الناجود هو الراووق نفسه (tahdhib)؛ الناجود الدم والناجود الخمر والناجود الزعفران (tahdhib)؛ الناجود الراووق وهو شيء يعلق فيصفى به الشراب (mufradat)
- **B012** yerleşik sakin — bir yerde oturan ve kalan kişi
  الناجد الساكن المقيم (ayn)

## ق ح م (root_001202): 90:11 ٱقْتَحَمَ

- **B001** düşünmeden tehlikeye atılma veya sokma — bir işe deneyimsizce ve düşünmeden atılmak · korkutucu bir güçlüğün ortasına dalma · yüksekten aşağı düşmek veya yolunu bilmeden bir şeye girmek · atın binicisini yüzüstü atması ya da tehlikeye götürmesi · kendini düşünmeden bir şeye sokmak · dişi deve sürüsüne salınmadan kendiliğinden giren erkek deve · bir işe atılanlar veya dişi deve sürüsüne kendiliğinden giren develer · sıraya girmek
  قحم في الأمور قحوما رمى بنفسه فيها من غير دربة (maqayis)؛ رميه بنفسه في نهر أو وهدة أو في أمر من غير روية (ayn)؛ انقحم الرجل انقحاما واقتحم اقتحاما إذا هوى من علو إلى سفل أو دخل في شيء من غير هداية (jamhara)؛ قحم في الأمر قحوما رمى بنفسه فيه من غير روية (sihah)؛ الاقتحام توسط شدة مخيفة (mufradat)؛ قحم فلان نفسه في كذا من غير روية (mufradat)؛ قحم الفرس فارسه (maqayis;ayn;sihah;mufradat)؛ المقحام الفحل الذي يقتحم الشول من غير إرسال فيها (maqayis;ayn;sihah)
- **B002** tehlikeli engel, büyük güçlük veya kötü sonuç — yolun güç ve tehlikeli kesimleri · yıkıma götüren tehlike veya herkesin göze alamayacağı büyük iş · insanın başına gelen yıkıcı tehlikeler ve ağır belalar · çekişmenin kişiyi istemediği yere sürükleyen ağır sonuçları
  قحم الطريق مصاعبه (maqayis;sihah)؛ القحمة الأمر العظيم لا يركبها كل أحد (ayn)؛ سميت المهالك قحما (jamhara)؛ القحمة المهلكة (sihah)؛ للخصومة قحم (maqayis;ayn;jamhara;sihah)
- **B003** göçebeleri yerleşik bölgelere süren kuraklık yılı — göçebeleri yerleşik bölgelere süren çetin kuraklık yılı · çöl göçebelerini kıtlıkla vurup yerleşik bölgelere süren yıl · kurak yıl göçebeleri çölden yerleşik bölgeye indirdi · çölde yaşayanlar kuraklığa uğrayıp kırsal bölgeye girdiler
  القحمة السنة تقحم الأعراب بلاد الريف (maqayis)؛ وقحمة الأعراب سنة جدبة تتقحم عليهم أو تقحم الأعراب بلاد الريف (ayn)؛ أقحمت السنة الأعراب إذا حطتهم من البدو إلى الحضر (jamhara)؛ السنة المقحمة المجدبة (jamhara)؛ القحمة السنة الشديدة (sihah)
- **B004** ileri yaşlı, kimi kullanımda bunamış kişi [kalıp] — yaşlanmak, ileri yaşa varmak · yaşlı, kimi bağlamda bunamış erkek · ileri yaşlı kadın
  قحم قحوما إذا كبر (ayn)؛ القحم الشيخ الخرف والقحمة الشيخة (ayn)؛ شيخ قحم وعجوز قحمة إذا أسنا (jamhara)؛ شيخ قحم أي هم مثل قحل (sihah)
- **B005** iki yaş evresini bir yılda geçen deve — iki yaş ve diş evresini bir yılda tamamlayan deve · normalde ardışık iki yaş basamağını tek yılda geçen deve
  القحم البعير يثني ويربع في سنة واحدة فيقحم سنا على سن (maqayis)؛ المقحم البعير الذي يربع ويثنى في سنة واحدة فتقتحم سن (ayn)؛ المقحم البعير الذي يطرح سنين في سن (jamhara)؛ المقحم البعير الذي يربع ويثني في سنة واحدة فيقحم سنا على سن (sihah)
- **B006** sürücüsüz ilerleyen deve veya çölden ayrılmamış kişi [kalıp] — çölde otlatıcısı ve sürücüsü olmadan ilerleyen deve · çölde yetişmiş ve oradan hiç ayrılmamış kişi
  بعير مقحم يقحم في مفازة من غير مسيم ولا سائق (ayn)؛ أعرابي مقحم أي نشأ في المفازة لم يخرج منها (ayn)
- **B007** gözde küçümseme veya görünüşünden yaşını büyük sayma [kalıp] — gözümde küçüldü; onu küçümsedim · gözün küçük yaştakini heybeti ve güzelliği yüzünden yaşından büyük sayması
  اقتحمته عيني ازدرته (sihah)؛ وقد يكون الذي تقحمه عينك صغيرا فترفعه فوق سنه لعظمه وحسنه (sihah)

## ع ق ب (root_001033): 90:11 ٱلْعَقَبَةَ, 90:12 ٱلْعَقَبَةُ

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

## د ر ي (root_000473): 90:12 أَدْرَىٰكَ

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

## ECHO د ر ر (root_000469): for 90:12 أَدْرَىٰكَ: withheld observed target; not identity

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

## ف ك ك (root_001173): 90:13 فَكُّ

- **B001** kapalıyı açıp iç içe geçmişi ayırma — kapalı şeyi açmak, kurtarmak veya serbest bırakmak · birbirine geçmiş iki şeyi ayırma · iki çeneyi birbirinden ayırmak
  أصل صحيح يدل على تفتح وانفراج (maqayis)؛ فككت الشيء فانفك ككتاب مختوم تفك خاتمه وكما تفك الحنكين تفصل بينهما (ayn;tahdhib)؛ فككت الشئ خلصته وكل مشتبكين فصلتهما فقد فككتهما (sihah)؛ الفكك التفريج (mufradat)؛ كل شيء أطلقته فقد فككته (tahdhib)
- **B002** rehni veya esaret altındakini bağından kurtarma — rehni bağlılığından kurtarmak · rehni çözme veya onu çözmek için verilen şey · rehni ya da tutsağı kurtarmaya yarayan şey · kölelikten özgürlüğüne kavuşturmak · ceylanın tuzağa düştükten sonra kurtulması
  فكاك الرهن وهو فتحه من الانغلاق (maqayis)؛ الفكاك الشيء الذي تفك به رهنا أو أسيرا وفككت رقبة فلان أعتقته (ayn)؛ فك الرهن وافتكه وفك الرقبة أي أعتقها (sihah)؛ فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن (tahdhib)؛ فك الرهن تخليصه وفك الرقبة عتقها (mufradat)؛ أفك الظبي من الحبالة إذا وقع فيه ثم انفلت (tahdhib)
- **B003** ayrılma; olumsuz yapıda sürüp gitme — bir şeyden ayrılmak veya uzaklaşmak · ayrılan, uzaklaşan veya sona erenler · yapmayı sürdürmek, bırakmamak
  لا ينفك يفعل ذلك بمعنى لا يزال (maqayis)؛ ما انفك فلان قائما أي ما زال قائما (sihah)؛ منفكين أي منتهين أو زائلين أو مفارقين (tahdhib)؛ منفكين أي لم يكونوا متفرقين وما انفك يفعل كذا نحو ما زال (mufradat)
- **B004** çene kemiği ve çenelerin birleşme bölgesi — çene kemiği · iki çene ve ağzın iki yanındaki birleşme bölgeleri · ağız-burun çıkıntısında iki çenenin birleştiği yer · yaşlılıktan çeneleri ayrılmış ihtiyar
  الفكان ملتقى الشدقين (maqayis;ayn;mufradat)؛ الفك اللحي (sihah)؛ انكسر أحد فكيه أي لحييه (tahdhib)؛ الأفك مجمع الخطم وهو مجمع الفكين (ayn;tahdhib)
- **B005** eklemin gevşeyip yerinden ayrılması — ayağı ekleminden ayrıldı · omuz ekleminin gevşeyip ayrılması veya ayağın çıkması · elini ekleminden çıkardım · omzu gevşeyip ekleminden ayrılmış kimse
  انفكت قدمه أي انفرجت (maqayis)؛ الفك انفراج المنكب عن مفصله ضعفا (maqayis)؛ الفكك انفراج المنكب عن مفصله ضعفا أو استرخاء (ayn)؛ انفكت قدمه أو إصبعه إذا انفرجت وزالت والفكك انفساخ القدم (sihah)؛ فككت يده فكا إذا أزال المفصل (tahdhib)؛ الفكك انفراج المنكب عن مفصله ضعفا (mufradat)
- **B006** düşünce ve davranışta gevşek, tutarsız aptallık — onda kadınsı sayılan bir gevşeklik var · düşünce veya tavırda gevşeklik ve aptallık · aptal · aptalca ve tutarsız davranmak · bilip bilmeden konuşan, yanlışı doğrusundan çok aptal
  في فلان فكك أي أناثة واستراخاء (ayn)؛ الفكة الحمق والاسترخاء وما كنت فاكا فأنت فاك تاك أي أحمق (sihah)؛ فلان فكة أي استرخاء في رأيه وأحمق فاك وهاك (tahdhib)
- **B007** hayvanda doğum, çiftleşme isteği veya zayıflığa bağlı çözülme [kalıp] — doğumu yaklaşmış, sağrı bağları gevşeyip memesi büyümüş dişi deve · çiftleşmeye istekli olup aygırı geri çevirmeyen kısrak · zayıflıktan bitkin dişi veya erkek deve
  ناقة متفككة إذا أقربت فاسترخى صلواها وعظم ضرعها ودنا نتاجها؛ ذهب بعضهم بتفكك الناقة إلى شدة ضبعتها؛ المتفككة من الخيل الوديق التي لا تمتنع على الفحل؛ الفاك المعيي هزالا ناقة فاكة وجمل فاك
- **B008** Yoksulların Tası denen yuvarlak yıldız kümesi — Yoksulların Tası denen yuvarlak yıldız kümesi
  الفكة النجوم المستديرة التي إلى جانب بنات نعش وهي قصعة المساكين (ayn)؛ الفكة كواكب مستديرة خلف السماك الرامح (sihah)؛ الفكة النجوم المستديرة التي يسميها الصبيان قصعة المساكين (tahdhib)
- **B009** çocuğun ağzına ilaç koyma [kalıp] — çocuğun ağzına ilaç koymak
  فككت الصبي جعلت الدواء في فيه

## ر ق ب (root_000584): 90:13 رَقَبَةٍ

- **B001** gözeterek beklemek — bir şeyi gözleyip beklemek · beklemek, gözlemek · gerçekleşmesini gözleyerek beklemek · Tanrı'dan çekinip buyruğunu gözetmek
  رقبت أرقب رقبة ورقبانا (maqayis); رقبت الشيء أرقبه أي انتظرت والترقب تنظر الشيء وتوقعه (ayn;tahdhib); ارتقبته ارتقابا إذا انتظرته (jamhara); الرقيب المنتظر ورصدته والترقب الانتظار والارتقاب (sihah); راقب الله في أمره أي خافه (sihah)
- **B002** koruyup gözeten görevli — koruyucu, muhafız · topluluğun bekçisi · ordunun öncü gözcüsü · topluluğun geride kalan eşyasını bekleyen değersiz görevli
  الرقيب وهو الحافظ (maqayis;ayn;sihah;mufradat); رقيب القوم حارسهم يحرس القوم (tahdhib); رقيب الجيش طليعتهم (tahdhib)
- **B003** yüksek gözetleme yeri — yüksek gözetleme yeri · dağ başı veya kale gözetleme yeri · yüksek gözetleme yerleri
  المرقب المكان العالي يقف عليه الناظر (maqayis); يشرف على رقبة يحرس القوم (ayn); المراقب واحدها مرقب وهي المرابي (jamhara); المرقب والمرقبة الموضع المشرف يرتفع عليه الرقيب (sihah); المرقبة هي المنظرة في رأس جبل أو حصن والمراقب ما ارتفع من الأرض (tahdhib)
- **B004** boyun ve kişi yerine kullanılan boyun — boynun arka tabanı · kişi veya köleleştirilmiş kimse · kalın boyunlu · insanın veya hayvanın boynuna ip geçirmek · köleleştirilmiş birini özgür bırakmak · özgürlük sözleşmesi yapan köleleştirilmiş kişiler için · tutsağı serbest bırakmak
  اشتقاق الرقبة لأنها منتصبة (maqayis); الرقبة أصل مؤخر العنق والأرقب والرقباني الغليظ الرقبة والإعطاء في الرقاب أي في المكاتبين (ayn); الرقبة معروفة وأعتق رقبة وفككت رقبة ورقبت الرجل والدابة إذا طرحت في رقبته حبلا (jamhara); الرقبة مؤخر أصل العنق والرقبة المملوك (sihah); في الرقاب هم المكاتبون وأعتق الله رقبته (tahdhib); الرقبة اسم للعضو المعروف ثم يعبر بها عن الجملة واسما للمماليك (mufradat)
- **B005** sağ kalma koşullu taşınmaz bağışı — sağ kalma veya geri dönüş koşullu taşınmaz bağışı · bir evi sağ kalma koşuluyla vermek
  أرقبت فلانا هذه الدار (maqayis); الرقبى أن يعطي الرجل دارا أو أرضا (jamhara); أرقبته دارا أو أرضا إذا أعطيته إياها فكانت للباقي منكما (sihah); أصل الرقبى من المراقبة كأن كل واحد منهما يرقب موت صاحبه (tahdhib)
- **B006** oyun denetçisi veya üçüncü oyun oku — oklarla oynanan talih oyununun pay denetçisi · talih oyununun üçüncü oku
  الرقيب الموكل في الميسر بالضريب والرقيب السهم الثالث (maqayis); رقيب الميسر الأمين الموكل بالضريب والرقيب السهم الثالث (ayn;tahdhib); الرقيب الرجل المشرف على أصحاب الميسر (jamhara); الرقيب الموكل بالضريب والثالث من سهام الميسر (sihah)
- **B007** karşı yıldız — başka bir yıldız doğarken batan karşı yıldız · Ülker batarken doğan karşı yıldız
  الرقيب النجم الذي ينوء من المشرق فيغيب رقيبه في المغرب ورقيب الثريا (jamhara); رقيب النجم الذي يغيب بطلوعه (sihah); رقيب الثريا رأس الإكليل لا يطلع أبدا حتى تغيب (tahdhib)
- **B008** çocukları yaşamayan ebeveyn — çocukları yaşamayan veya hiçbir çocuğunu kendinden önce kaybetmemiş kişi
  الرقوب المرأة التي لا يعيش لها ولد (maqayis;jamhara;sihah); الرقوب من الأرامل والشيوخ الذي لا ولد له ولا يستطيع الكسب ولم يقدم من ولده شيئا (ayn); الرقوب الذي لم يقدم من ولده شيئا ومعناه في كلامهم على فقد الأولاد (tahdhib)
- **B009** belirli bir sonucu bekleyen — eşinin ölümünü veya bir yardımı bekleyen kadın · kalabalık çekilene kadar suya yaklaşmayan dişi deve
  المرأة التي ترقب موت زوجها لترثه الرقوب والناقة التي ترقب متى تنصرف الإبل عن الماء (maqayis); الأرملة رقوب لأنها تترقب معروفا (ayn); الرقوب المرأة التي ترقب موت زوجها لترثه والرقوب من الإبل التي لا تدنو من الحوض (sihah); الرقوب الناقة التي لا تدنو إلى الحوض مع الزحام (tahdhib)
- **B010** zararlı bir yılan türü — zararlı bir yılan türü
  الرقيب ضرب من الحيات وجمعه رقب ورقيبات (ayn); الرقيب ضرب من الحيات خبيث والجمع الرقيبات والرقب (tahdhib)
- **B011** avcı siperi — avcının arkasına saklandığı siper
  الرقيبة كل ما استترت به لترمي صيدا (jamhara)
- **B012** öz malından vermek [kalıp] — malının öz kısmından
  أعطى من رقبة ماله أي من خالصه (jamhara)
- **B013** doğrudan baba çizgisi dışından miras almak [kalıp] — yan akrabadan mal veya doğrudan babalar dışından saygınlık miras almak
  ورث فلان مالا عن رقبة أي عن كلالة وورث مجدا عن رقبة إذا لم يكن آباؤه أمجادا (tahdhib)
- **B014** iki harften birini düşürme kuralı — şiir ölçüsünde iki harften birinin düşüp diğerinin kalması
  المراقبة في أجزاء الشعر عند التجزئة بين حرفين هو أن يسقط أحدهما ويثبت الآخر (tahdhib)
- **B015** sonda veya arkada kalan — bir şeyin sonu veya arkada kalan bölümü · kişinin ardından kalan çocukları veya akrabaları
  رقيب الرجل خلفه من ولده أو عشيرته ورقيب كل شيء آخره ورقيب الغبار (tahdhib)

## ط ع م (root_000934): 90:14 إِطْعَٰمٌ

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

## ي و م (root_001700): 90:14 يَوْمٍ

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

## س غ ب (root_000710): 90:14 مَسْغَبَةٍ

- **B001** açlık; özellikle yorgunlukla ağırlaşan açlık ve kıtlık — acıkmak; bazı kullanımlarda açlıktan yorulmak · kıtlık, şiddetli açlık · aç, acıkmış kimse · çok aç, açlıktan bitkin · açlık; bazı kaynaklarda yorgunlukla birlikte açlık · açlık · açlık · aç kadın
  أصل واحد يدل على الجوع والمسغبة المجاعة وسغب يسغب سغوبا وهو ساغب وسغبان (maqayis)؛ الساغب الجائع وسغب يسغب سغوبا ومسغبة (ayn)؛ سغب الرجل إذا جاع ولا يكون السغب إلا الجوع مع التعب والمصدر السغابة والسغوب والسغب (jamhara)؛ سغب أي جاع فهو ساغب وسغبان وامرأة سغبى ويتيم ذو مسغبة أي ذو مجاعة (sihah)؛ السغب وهو الجوع مع التعب ويقال سغب سغبا وسغوبا وهو ساغب وسغبان (mufradat)

## ي ت م (root_001692): 90:15 يَتِيمًا

- **B001** babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma — insanda babasız, hayvanda annesiz kalma · babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu · çocuk babasını yitirip babasız kaldı · Tanrı onu babasız bıraktı · çocukları babasız bıraktı · babasını yitirmiş çocuklar · babasını yitirmiş çocuklar · çocukları babasız kalmış kadın · çocukları babasız kalmış kadın · onları babasız bıraktı · çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi · babasını yitirmiş çocuklar topluluğu
  اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)
- **B002** tek kalmış ya da benzeri zor bulunan şey — tek başına veya eşi zor bulunan · tek başına duran veya benzeri olmayan şiir dizesi · tek ve eşi zor bulunan inci · tek başına duran kumluk veya dişil varlık
  لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)
- **B003** dalgınlık ve gerekeni eksik yapma — dalgınlık ve gerekeni eksik yapma · gidişinde dalgınlık veya eksik davranış yok
  اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)
- **B004** yavaşlama veya gecikme — gidişinde yavaşlama var · yavaşlama ve gecikme
  في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)
- **B005** evlilikle sona erip ermediği tartışmalı kadın adlandırması [kalıp] — evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın · kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz
  المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)

## ق ر ب (root_001212): 90:15 مَقْرَبَةٍ

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

## س ك ن (root_000726): 90:16 مِسْكِينًا

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

## ت ر ب (root_000178): 90:16 مَتْرَبَةٍ

- **B001** toprak ve toprağa bağlı kullanımlar — toprak ve toprağın değişik adları · yerin kendisi veya toprağın kendisi · yer toprağının yüzü veya toprak yapısı · bir şeyin toprağa bulanması · bir şeyi toprakla bulamak veya düzeltmek · bir şeyin üzerine toprak koymak · toprak taşıyan rüzgar · ölünün toprakla örtülü gömü yeri
  التراب وهو التيرب والتوراب (maqayis)؛ التراب والتيرب والتورب كله من أسماء التراب (jamhara)؛ الترباء الأرض نفسها (maqayis;sihah;mufradat)؛ ترب الشيء أصابه التراب (sihah)؛ تترب إذا تلوث في التراب (tahdhib)؛ ريح تربة جاءت بالتراب (maqayis;sihah;mufradat)؛ تربة الميت رمسه (jamhara)
- **B002** toprağa düşmüş yoksulluk — toprağa yapışmış gibi yoksullaşmak · yoksulluk, düşkünlük ve geçim darlığı · yoksulluktan toprağa yapışmış düşkün kimse · görünüşte yoksulluk dileği olan kalıplaşmış söz · az mal sahibi olma
  ترب الرجل إذا افتقر كأنه لصق بالتراب (maqayis;sihah;mufradat)؛ المتربة الفقر (jamhara)؛ مسكين ذو متربة أي لاصق بالتراب (sihah;mufradat)؛ رجل ترب فقير (tahdhib)؛ تربت يداك (sihah;tahdhib;mufradat)
- **B003** varlıklı hale gelmek — varlıklı olmak ve malı çoğalmak · çok mal sahibi olma
  أترب إذا استغنى كأنه صار له من المال بقدر التراب (maqayis;sihah;mufradat)؛ أترب الرجل إذا استغنى (jamhara)؛ أترب الرجل فهو مترب إذا كثر ماله (tahdhib)؛ التتريب كثرة المال (tahdhib)
- **B004** yaşıt ve denk arkadaş — yaşıt, birlikte yetişmiş arkadaş veya denk kişi · yaşıtlar veya denk kişiler
  الترب الخدن والجمع أتراب (maqayis)؛ الترب اللدة الذي ينشأ معك والجمع أتراب (jamhara)؛ هذه ترب هذه أي لدتها وهن أتراب (sihah)؛ أترابا أي أمثالا وهما تربان (tahdhib)؛ أتراب أي لدات تنشأن معا (mufradat)
- **B005** göğsün kolye yeri — göğüs kemikleri veya göğüste kolye yeri · göğüste kemik uçlarının denk durduğu bölge
  التريب الصدر عند تساوي رءوس العظام (maqayis)؛ التريبة مجال القلادة في الصدر والجمع الترائب (jamhara)؛ التريبة واحدة الترائب وهي عظام الصدر ما بين الترقوة إلى الثندؤة (sihah)؛ الترائب موضع القلادة من الصدر (tahdhib)؛ الترائب ضلوع الصدر الواحدة تريبة (mufradat)
- **B006** parmak uçları — parmak uçları; tekili parmak ucu
  التربات وهي الأنامل الواحدة تربة (maqayis)؛ التربات الأنامل الواحدة تربة (sihah)
- **B007** belirli bir bitki — belirli bir bitki adı
  التربة وهو نبت (maqayis)؛ التربة ضرب من النبت (jamhara)؛ التربة أيضا نبت (sihah)
- **B008** belirli yer adları — belirli bir yerin adı; yüzey biçimi burada üretilmez · belirli bir yer veya vadinin adı; yüzey biçimi burada üretilmez · belirli bir yerin adı; yüzey biçimi burada üretilmez
  يترب موضع قريب من اليمامة (jamhara;sihah)؛ تربة موضع لا تدخله الألف واللام (jamhara)؛ تربة واد من أودية اليمن (tahdhib)؛ تربان موضع معروف (jamhara)
- **B009** uysal deve — uysal ve kolay yönetilir deve
  جمل تربوت وناقة تربوت أي ذلول (sihah)؛ بعير تربوت إذا كان ذلولا وناقة تربوت كذلك (tahdhib)

## ك و ن (root_001332): 90:17 كَانَ

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

## ء م ن (root_000054): 90:17 ءَامَنُوا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## و ص ي (root_001656): 90:17 وَتَوَاصَوْا۟, 90:17 وَتَوَاصَوْا۟

- **B001** bir şeyi başka şeyle bağlama veya bitişik sürdürme — bir şeyi başka bir şeye bağlamak veya onunla bitiştirmek · geceyi gündüze ekleyerek işi kesintisiz sürdürmek · bitki örtüsü birbirine bağlı ve kesintisiz olan arazi · bitkinin bir kısmının başka kısmıyla birleşip kesintisiz olması · birbirine bağlı ve kesintisiz bitki · arazinin bitki örtüsünün birbirine bağlanıp kesintisiz olması · başka bir çöl alanına bitişen çöl · soyu, sebebi ve görünüş yolu başka biriyle bağlantılı olan kişi
  أصل يدل على وصل شيء بشيء (maqayis)؛ ووصيت الشيء وصلته (maqayis)؛ وصيت الليلة باليوم وصلتها (maqayis)؛ تواصى النبت إذا اتصل (jamhara;sihah)؛ أرض واصية متصلة النبات (sihah;mufradat)؛ فلاة واصية يتصل بفلاة أخرى (tahdhib)؛ وصى الشيء يصي إذا اتصل ووصاه غيره وصله (tahdhib)
- **B002** başkasına bırakılan iş talimatı — başkasına yapılması için verilen öğütlü iş talimatı · vasiyet; ölümden sonra uygulanması istenen talimat veya bırakılan istek · birine yapılacak işi bildirmek veya öğütlü talimat vermek · talimat veya bırakılan istek anlamındaki ad · bırakılan talimatı yürütme görevi veya bu görevde bulunma · talimatı veya isteği bırakan kişi · vasi; bırakılan talimatı yerine getirmekle görevlendirilen kişi · kendisine söylenen şeyi unutmasından kaygı duyulan kimse için kullanılan söz · birini bırakılan talimatı yürütmekle görevlendirmek
  الوصية من هذا القياس كأنه كلام يوصى أي يوصل (maqayis)؛ وصيته توصية وأوصيته إيصاء (maqayis;sihah;mufradat)؛ الوصاة كالوصية (ayn;jamhara;tahdhib)؛ الوصاية مصدر الوصي (ayn;sihah)؛ الوصية بعد الموت (ayn)؛ الوصية ما أوصيت به (ayn;tahdhib)؛ أوصيت له بشئ وأوصيت إليه إذا جعلته وصيك (sihah)؛ الوصي الموصي والموصى إليه جميعا (jamhara)؛ التقدم إلى الغير بما يعمل به مقترنا بوعظ (mufradat)
- **B003** birbirine öğüt veya talimat iletmek — birbirine öğüt vermek veya yapılacak şeyi karşılıklı bildirmek; bağlamına göre karşılıklı bağlantı kurmak
  تواصى القوم إذا تواصلوا (jamhara)؛ تواصى القوم أي أوصى بعضهم بعضا (sihah)؛ تواصى القوم إذا أوصى بعضهم إلى بعض (mufradat)
- **B004** otlağın sürüye bolca elverişli olması — otlağın otlayan hayvanlara uygun gelip onlara bol ve rahat yem sağlaması
  إذا أطاع المرعى للسائمة فأصابته رغدا قيل وصى لها المرتع يصي وصيا (ayn;tahdhib)

## ص ب ر (root_000840): 90:17 بِٱلصَّبْرِ

- **B001** kendini tutarak dayanma — kendini tutarak dayanma · kendimi o işte tuttum · kendini zorlayarak dayanma · çaba göstererek dayan · dayanma gücü yüksek kişi · her defasında çabayla dayanan kişi
  الصبر نقيض الجزع (ayn;jamhara;tahdhib)؛ الصبر حبس النفس عن الجزع (sihah)؛ صبرت نفسي أي حبستها (maqayis;tahdhib)؛ حبس النفس على ما يقتضيه العقل والشرع (mufradat)
- **B002** zorla alıkoyma — onu zorla alıkoydu · öldürülmek üzere bağlı tutma · ölümü beklemek üzere alıkonmuş canlı · yetkili önünde zorla ettirilen ant · ona bütün gücüyle ant içirdi
  المصبورة المحبوسة على الموت (maqayis;sihah)؛ الصبر نصب الإنسان للقتل (ayn;tahdhib)؛ صبرت يمينه أي حلفته (ayn;maqayis;tahdhib)؛ قتل صبر ويمين صبر (sihah;tahdhib)؛ الصبر الإكراه (tahdhib)
- **B003** yükümlülüğe güvence veren kişi — yükümlülüğe güvence veren kişi · onun yükümlülüğüne güvence verdim · bana bir güvence veren kişi bul · topluluğun işlerinde yanında duran kişi
  الصبير هو الكفيل (maqayis;sihah)؛ صبرت بفلان إذا كفلت به فأنا به صبير (tahdhib)؛ صبير القوم الذي يصبر لهم ويكون معهم في أمورهم (ayn)
- **B004** üst ya da yan sınır — şeyin üstü ya da yanı · kabın çevre yanları · mezarın çevre yanları · üst ya da yan sınırına kadar · bahçenin en üst bölümü
  صبر كل شيء أعلاه (maqayis;ayn;tahdhib)؛ أصبار الإناء نواحيه (maqayis;ayn;sihah)؛ أصبار القبر نواحيه (ayn;tahdhib)؛ الصبر جانب الشيء (tahdhib)
- **B005** sert taş ve taşlı arazi — sert ve kalın taş · sert ve düz taşlar · taşlar ya da kaba yüksekçe arazi · çok engebeli olmayan çakıllı yer · katı kaya yüzeyi ya da taşlık alan
  الصبرة من الحجارة ما اشتد وغلظ (maqayis;ayn;tahdhib)؛ الصبارة الحجارة (sihah;tahdhib)؛ الصبر الأرض التي فيها حصباء (maqayis;sihah;tahdhib)؛ أم صبار الحرة أو الصفاة (maqayis;sihah;tahdhib)
- **B006** çıkışsız ağır durum — savaş ya da ağır yıkım · çıkış yolu olmayan büyük sıkıntı
  وقع القوم في أم صبور إذا وقعوا في أمر عظيم (maqayis)؛ أم صبار الحرب والداهية الشديدة (ayn)؛ وقع القوم في أم صبور أي في أمر شديد (sihah)؛ أم صبور أمر لا منفذ له عنه (tahdhib)
- **B007** kışın ayazı — kışın şiddetli soğuğu
  صبارة الشتاء شدة برده (sihah)؛ أتيته في صبارة الشتاء أي في شدة البرد (tahdhib)
- **B008** acı ağaç özü — acı ağaç özü ve bundan yapılan ilaç
  الصبر بكسر الباء عصارة شجرة (ayn;tahdhib)؛ الصبر هذا الدواء المر (sihah)
- **B009** demirhindi meyvesi — demirhindi meyvesi
  الصبار حمل شجرة طعمه أشد حموضة من المصل (ayn;tahdhib)؛ الصبار التمر الهندي (tahdhib)
- **B010** katmanlı beyaz bulut — üst üste yığılmış beyaz bulut · yoğun bulutun üstündeki düz bulut · beyaz bulutlar
  الصبر سحاب مستو فوق السحاب الكثيف (ayn)؛ الصبير السحاب الأبيض (sihah;tahdhib)؛ السحاب الأبيض الذي يصبر بعضه فوق بعض درجا (sihah;tahdhib)؛ الاصبار السحائب البيض (sihah)
- **B011** sofra yaygısı ya da yiyecek yığını — yiyeceğin altına serilen geniş ince yaygı · üst üste konmuş yiyecek yığını · malı tartmadan ya da ölçmeden topluca aldım · düğün yemeğinin üstüne konduğu ince yaygı
  صبير الخوان رقاقته العريضة تبسط تحت ما يؤكل من الطعام (ayn;tahdhib)؛ الصبرة من الطعام بعضه فوق بعض (ayn;tahdhib)؛ اشتريت الشيء صبرة أي بلا وزن ولا كيل (sihah)
- **B012** öldürmeye karşılık ölüm cezası — öldürmeye karşılık ölüm cezası istesin · yetkili onu önceki öldürmeye karşılık öldürdü
  فليصطبر معناه فليقتص (tahdhib)؛ أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود (tahdhib)
- **B013** ateşe götüren işlerde pervasızlık — ateşi hak edecek işleri yapmaya ne kadar da gözü pekler
  الصبر الجرأة ومنه فما أصبرهم على النار (tahdhib)؛ لغة بمعنى الجرأة (mufradat)؛ ما أعملهم بعمل أهل النار (mufradat)
- **B014** kendini tutarak bekleme — kendini tutarak bekleme · yöneticinin hükmünün gerçekleşmesini bekle
  يعبر عن الانتظار بالصبر لما كان حق الانتظار أن لا ينفك عن الصبر (mufradat)؛ فاصبر لحكم ربك أي انتظر حكمه (mufradat)
- **B015** kendini tutma türü olarak oruç — oruç, kendini tutmanın bir türüdür · oruç ayı
  سمي الصوم صبرا لكونه كالنوع له (mufradat)؛ صيام شهر الصبر (mufradat)
- **B016** bir Arap boyunun adı — belirli bir Arap topluluğuna bağlı boyun adı
  الصبر أيضا بطن من غسان (sihah)
- **B017** dağ ya da dağların orta kesimi — dağ · dağların orta kesimi
  الصبير الأقدر وهو الوسط من الجبال (tahdhib)؛ الصبير الجبل (tahdhib)
- **B018** şişe tıkacı ve tıkama — şişe tıkacı ya da kapakçığı · kabın ağzını tıkaçla kapattı
  أصبر سد رأس الحوجلة بالصبار وهو السداد (tahdhib)؛ الصبار صمام القارورة (tahdhib)

## ر ح م (root_000552): 90:17 بِٱلْمَرْحَمَةِ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ص ح ب (root_000844): 90:18 أَصْحَٰبُ, 90:19 أَصْحَٰبُ

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

## ي م ن (root_001698): 90:18 ٱلْمَيْمَنَةِ

- **B001** uğur ve iyilik getirme, bunları umma — uğur, iyilik artışı ve mutluluk · uğurlu ve iyilik getiren · topluluğuna uğur ve iyilik getirdi · uğur ve iyilik getiren kimse · onu uğurlu sayıp iyilik umdu · onun görüşünü uğurlu sayıp iyilik umuyor · mutluluk ve iyi yazgı sahipleri · mutluluğa ve Tanrı'ya yakınlığa ulaştıran araç sayılan Kara Taş
  واليمن البركة وهو ميمون (maqayis)؛ يمن الرجل فهو ميمون والميمن الذي أتى باليمن والبركة (ayn)؛ اليمن البركة وتيمنت به تبركت (sihah)؛ اليمن نظير البركة ويمن الرجل فهو ميمون (tahdhib)؛ أصحاب اليمين أصحاب السعادات والميامن واستعير اليمين للتيمن والسعادة (mufradat)
- **B002** sağ el ve sağ yön — sağ el veya sağ yön · yanındakileri sağa götür · sağ taraf veya sağ yön · solun karşıtı olan sağ taraf · sağa doğru ilerledi · iki sağ eliyle verdiği azık · sağ eller
  فاليمين يمين اليد (maqayis)؛ واليمين اليد اليمنى والأيمان جمعه (ayn)؛ اليمنة خلاف اليسرة والأيمن والميمنة خلاف الأيسر والميسرة (sihah)؛ يقال لليد اليمنى يمين وأخذ فلان يمينا وأخذ يسارا ويامن بأصحابك (tahdhib)؛ اليمين أصله الجارحة والميمنة ناحية اليمين (mufradat)
- **B003** kutsal tanıklı ant ve söz güvencesi — ant veya kutsal tanıklı söz güvencesi · antlar ve bağlayıcı sözler · Tanrı adına ant olsun · senin adına ant olsun · Tanrı adına edilen ant · Tanrı adına ant olsun diyen kısaltılmış söz
  واليمين الحلف (maqayis)؛ واليمين من القسم والأيمان جماعته وأيمن حرف وضع للقسم (ayn)؛ اليمين القسم الجمع أيمن وأيمان وأيمن الله اسم وضع للقسم (sihah)؛ الأصل يمين الله وأيمن الله وليمنك (tahdhib)؛ اليمين في الحلف مستعار من اليد (mufradat)
- **B004** güç, savunma ve güçlü doğruluk dayanağı — güç, yetki veya doğruluğun güçlü tarafı · dinî gerekçe veya doğruluk yönünden · güçle veya doğruluğa dayanarak · güç kullanarak engelledi ve savdı
  اليمين القوة (maqayis)؛ واليمين القوة وعن اليمين من قبل الدين (sihah)؛ باليمين أي بالقوة وقيل بالقوة والحق وتخدعوننا بأقوى الأسباب من قبل الدين (tahdhib)؛ لأخذنا منه باليمين أي منعناه ودفعناه (mufradat)
- **B005** Yemen ülkesi, halkı ve ona aidiyet — Yemen ülkesi veya Yemen yönü · Yemenli veya Yemen'e ait · Yemenli veya Yemen'e ait · Yemenli kadın veya Yemen'e ait dişil varlık · Yemenli kadın veya Yemen yönünden olan · Yemen dokumasından yapılmış örtü · Yemen'e mensup oldu · Yemen yönüne gitti veya Yemen'e vardı
  وكذلك اليمن وهو بلد ورجل يماز وسيف يمان (maqayis)؛ واليمن أرض وجيل من الناس واليمن ما كان على يمين القبلة (ayn)؛ اليمن بلاد للعرب والنسبة إليها يمنى ويمان وتيمن تنسب إلى اليمن واليمنة البردة من برود اليمن (sihah)؛ تيامن القوم وأيمنوا إذا أتوا اليمن وقولهم رجل يمان منسوب إلى اليمن واليمنة ضرب من برود اليمين (tahdhib)
- **B006** antlaşma bağı veya kesin sahiplik bildiren sağ el sözleri — aranda antlaşma bulunan bağlı kişi · kesin sahip olduğum ve tasarrufumda bulunan şey
  ومولى اليمين هو من بينك وبينه معاهدة وملك يميني أنفذ وأبلغ من قولهم في يدي (mufradat)
- **B007** ölmek; mezarda sağ yana yatırılmayla ilişkilendirilen kullanım — öldü; mezarda sağ yanına yatırılmasıyla ilişkilendirilen kullanım
  والتيمن الموت يقال تيمن فلان تيمنا إذا مات والأصل فيه أنه يوسد يمينه إذا مات في قبره (tahdhib)

## ك ف ر (root_001307): 90:19 كَفَرُوا۟

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

## ء ي ي (root_000074): 90:19 بِـَٔايَٰتِنَا

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

## ش ء م (root_000772): 90:19 ٱلْمَشْـَٔمَةِ

- **B001** sol yan; sola yönelme veya yöneltme — sol taraf; sağın karşısındaki yan · topluluğu sola yöneltti · sol taraf · yanındakileri sola götür · sağa ve sola baktı · soldakiler
  أصل واحد يدل على الجانب اليسار (maqayis)؛ المشأمة وهي خلاف الميمنة (maqayis)؛ شأمت القوم يسرتهم (ayn;tahdhib)؛ المشأمة الميسرة وكذلك الشأمة وشائم بأصحابك أي خذ بهم شأمة أي ذات الشمال ونظرت يمنة وشأمة (sihah;tahdhib)؛ الأشائم نقيض الأيامن (sihah)؛ الأشائم كالأيامن والأيامن كالأشائم (tahdhib)
- **B002** belirli ülke ve bölge; ona mensubiyet veya oraya gidiş — kaynaklarda adı geçen ülke ve bölge · bu bölgeden olan veya bu bölgeye mensup erkek · bu bölgeden olan veya bu bölgeye mensup kadın · bu bölgeye mensup oldu · bu bölgeye doğru gitti · bu bölgeye vardı
  الشأم أرض عن مشأمة القبلة (maqayis)؛ الشأم أرض سميت به لأنها من مشأمة القبلة (ayn;tahdhib)؛ الشأم بلاد يذكر ويؤنث ورجل شأمي وشآم وشامي وامرأة شأمية وشآمية (sihah)؛ رجل شآم إذا نسب إلى الشأم (tahdhib)؛ تشاءم الرجل إذا أخذ نحو الشأم وأشأم إذا أتى الشأم (sihah;tahdhib)
- **B003** uğursuzluk; uğursuz sayılma veya uğursuzluk getirme — uğursuzluk; kötü talih · uğursuz sayılan; uğursuzluk getiren · onlar için uğursuz oldu · yakınlarına veya topluluğuna uğursuzluk getirdi · uğursuz sayılan kuş · uğursuzluk getirdiğine inanılan kuşlar · uğursuz; uğursuzluk · uğursuz sayılan topluluk · onu uğursuz saydılar · kişinin uğursuzluğu dilindedir
  رجل مشئوم من الشؤم (maqayis)؛ المشأمة من الشوم ويقال رجل مشؤوم وشأم فلان أصحابه إذا أصابهم شؤم من قبله وطائر أشأم وطير أشأم وجرت لهم طير الأشائم (ayn)؛ الشؤم نقيض اليمن ورجل مشوم ومشئوم وشأم فلان على قومه يشأمهم إذا جر عليهم الشؤم وقوم مشائيم وتشاءموا به (sihah)؛ أشأم كل امرىء بين لحييه وغلمان أشأم أي غلمان شؤم (tahdhib)

## ن و ر (root_001564): 90:20 نَارٌ

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

## و ص د (root_001653): 90:20 مُّؤْصَدَةٌۢ

- **B001** bitiştirerek sıkıca kapatma — kapıyı örtüp sıkıca kapatmak · kapıyı örtüp sıkıca kapatmak · örtülmüş ve kapalı · örtülmüş ve sıkıca kapatılmış
  أصل يدل على ضم شيء إلى شيء (maqayis)؛ أوصدت الباب أغلقته والموصد المطبق (maqayis)؛ أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة (sihah)؛ أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة (mufradat)
- **B002** eve bağlı avlu veya kapı — evin avlusu veya kapısı
  الوصيد الفناء لاتصاله بالربع (maqayis)؛ الوصيد فناء البيت والوصيد الباب (ayn)؛ الوصيد الفناء (sihah)
- **B003** dağdaki taş hayvan barınağı — dağda hayvanlar için yapılan taş oda veya çevirmelik · dağda böyle bir taş barınak kurmak
  الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل (sihah)؛ الوصيدة حجرة تجعل للمال في الجبل (mufradat)
- **B004** kökleri birbirine yakın bitki — kökleri birbirine yakın bitki
  الوصيد النبت المتقارب الأصول (maqayis)؛ الوصيد النبات المتقارب الاصول (sihah)؛ الوصيد المتقارب الأصول (mufradat)

## ECHO ء ص د (root_000036): for 90:20 مُّؤْصَدَةٌۢ: withheld observed target; not identity

- **B001** kuşatıp kapatma — kapatıp örten şey · kuşatıp kapatma · üzerlerine kapattı · kapıyı kapattı · üzerlerine kapatılmış ateş · kapatıp örten şey için kullanılan ad
  شيء يشتمل على الشيء (maqayis); الإِصد والإِصاد والوصاد بمنزلة المطبق (ayn); أصدت عليهم وأوصدته (ayn); نار مُؤصدة أي مطبقة (ayn); آصدت الباب إذا أغلقته (sihah)
- **B002** çevrili barınak — içindekileri çevreleyen barınak veya ağıl
  الحظيرة أُصيدة سميت بذلك لاشتمالها على ما فيها (maqayis); الأُصيدة كالحظيرة لغة في الوصيدة (sihah)
- **B003** kız çocuklarının giydiği küçük veya içe giyilen gömlek — kız çocuklarının giydiği küçük veya içe giyilen gömlek · küçük iç gömleği olan kız · ona küçük iç gömleğini giydirdi
  الأُصدة قميص صغير يلبسه الصبايا (maqayis); صبية ذات مُؤصد (maqayis); الأُصدة قميص يلبس تحت الثوب وتلبسه صغار الجواري (sihah); أصدته تأصيدا (sihah)
- **B004** avlu — avlu
  الأَصيد لغة في الوصيد وهو الفناء (sihah)
- **B005** dağlar arasındaki çukur alan — belirli bir yer adı · dağlar arasındaki çukur alan
  ذات الأَصاد موضع (sihah); الأَصاد ردهة بين أجبل (sihah)



===== _commentary/v16/work/s090/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s090/reader_a_pilot.md)

# S090 Semantic Channel Discovery

## Parent Channels

### 1. Boundaries, Enclosures, and Release
- Semantic invariant: A boundary can seal, contain, admit, or release what is held within it.
- Surface relation: direct; 90:13 `فَكُّ رَقَبَةٍ` opens a bond, while 90:20 `مُّؤْصَدَةٌ` closes the terminal enclosure.
- Surprising reach: The same boundary logic extends from doors and stone pens to bottle stoppers, sanctuary limits, pledges, and bodily joints.

#### Subchannel A. Sealed Threshold and Forecourt
- Reading type: mixed
- Scene or process: A door is shut tightly, joining the barrier to the forecourt that controls entry.
- Active motifs: sealed door `و ص د:B001/m01`; enclosing closure `ء ص د:B001/m01`; attached forecourt or door `و ص د:B002/m01`; enclosing forecourt `ء ص د:B004/m01`; vessel stopper `ص ب ر:B018/m01`
- Ayah anchors: 90:20 `مُّؤْصَدَةٌ` (و ص د); 90:17 `صَّبْرِ` (ص ب ر); no independent surface occurrence for ء ص د
- Synthesis: Closure is both an action and a built threshold. The shut door, its forecourt, and the stopper all regulate passage by completing an aperture, giving the final fire an architectural as well as punitive enclosure.

#### Subchannel B. Stone Pen in the Mountain
- Reading type: latent/lexical
- Scene or process: A hard mountain hollow is built into a stone enclosure that holds livestock or property.
- Active motifs: stone livestock pen `و ص د:B003/m01`; containing corral `ء ص د:B002/m01`; hard gravelly stone `ص ب ر:B005/m01`; rain-holding rock hollow `خ ل ق:B011/m01`; low enclosing wall `ك ف ر:B013/m02`
- Ayah anchors: 90:20 `مُّؤْصَدَةٌ` (و ص د); 90:17 `صَّبْرِ` (ص ب ر); 90:4 `خَلَقْنَا` (خ ل ق); 90:19 `كَفَرُوا` (ك ف ر)
- Synthesis: The scene joins natural hardness to deliberate containment: a rocky depression or mountain chamber becomes a pen whose low stone walls hold what has been gathered inside.

#### Subchannel C. Unfastening and Disentanglement
- Reading type: mixed
- Scene or process: A knot, seal, or interlocked pair is opened and its joined parts separate.
- Active motifs: untying a knot `ح ل ل:B001/m01`; opening a sealed object `ف ك ك:B001/m01`; separating interlocked parts `ف ك ك:B001/m02`; departure from attachment `ف ك ك:B003/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: Release begins as a mechanical operation: tension is undone, a closure opens, and joined elements part. This concrete sequence supplies the action grammar behind the surah's emancipatory release.

#### Subchannel D. Ransom, Pledge, and Captive Release
- Reading type: surface-primary
- Scene or process: A person or pledged asset is freed from the bond that holds it.
- Active motifs: redemption of a pledge `ف ك ك:B002/m01`; freeing a captive or enslaved person `ف ك ك:B002/m02`; neck standing for the enslaved person `ر ق ب:B004/m02`; substitute held under guarantee `ع ق ب:B010/m01`; guarantor who remains liable `ص ب ر:B003/m01`
- Ayah anchors: 90:13 `فَكُّ رَقَبَةٍ` (ف ك ك, ر ق ب); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:17 `صَّبْرِ` (ص ب ر)
- Synthesis: The captive and the collateral share a condition of being held under another's claim. Redemption removes that claim, while guarantee and substitution describe the liability that must be answered before release is complete.

#### Subchannel E. Sacred Limit and Lawful Exit
- Reading type: mixed
- Scene or process: A protected limit is crossed only when prohibition, covenant, or consecrated status is released.
- Active motifs: lawful permission `ح ل ل:B003/m01`; crossing beyond a sanctuary limit `ح ل ل:B003/m02`; offering reaching its appointed place `ح ل ل:B004/m03`; sanctuary offering `ه د ي:B005/m01`; approach through devotion `ق ر ب:B005/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: Lawfulness is spatial and procedural: the protected boundary, the consecrated offering, and its arrival at the proper place determine when restraint ends and access becomes permitted.

### 2. Terrain, Passage, and Settlement
- Semantic invariant: Land is organized by routes, heights, habitations, and dangerous spaces that shape movement and staying.
- Surface relation: direct; the `بَلَد` of 90:1-2, the two `نَّجْدَيْنِ` of 90:10, and the `عَقَبَة` of 90:11-12 form an explicit geography of settlement and ascent.
- Surprising reach: Terrain also reaches graves, mountain hollows, nomadic disorientation, ground-hugging basins, travel gear, and a small attendant boat.

#### Subchannel A. Steep Pass and Hazardous Ascent
- Reading type: surface-primary
- Scene or process: A traveler commits to a steep, projecting mountain route whose difficulty cannot be bypassed.
- Active motifs: steep mountain pass `ع ق ب:B012/m01`; covered mountain saddle `ك ف ر:B013/m01`; plunging into danger `ق ح م:B001/m01`; road peril few will undertake `ق ح م:B002/m01`; inescapable ordeal `ص ب ر:B006/m01`
- Ayah anchors: 90:11 `ٱقْتَحَمَ ٱلْعَقَبَةَ` (ق ح م, ع ق ب); 90:12 `ٱلْعَقَبَةُ` (ع ق ب); 90:19 `كَفَرُوا` (ك ف ر); 90:17 `صَّبْرِ` (ص ب ر)
- Synthesis: The pass is both topography and ordeal. Its covered saddle and projecting rise demand entry into danger, and the lack of an easy outlet turns ascent into a sustained act rather than a single step.

#### Subchannel B. Elevated Road and Clear Guidance
- Reading type: surface-primary
- Scene or process: A raised, visible road functions as a guide toward a chosen direction.
- Active motifs: elevated clear road `ن ج د:B001/m01`; evident guiding route `ن ج د:B002/m01`; gentle direction to road and truth `ه د ي:B001/m01`; orientation and manner of travel `ه د ي:B002/m01`
- Ayah anchors: 90:10 `هَدَيْنَٰهُ ٱلنَّجْدَيْنِ` (ه د ي, ن ج د)
- Synthesis: Height makes the route legible, and guidance makes it actionable. The two roads therefore combine visible terrain with directed conduct.

#### Subchannel C. Mountain Core, Ridge, and Named Height
- Reading type: latent/lexical
- Scene or process: A mountain is apprehended through its center, ridge, hollow, and named identity.
- Active motifs: mountain and its middle `ص ب ر:B017/m01`; central mass `ك ب د:B003/m01`; mountain hollow `ء ص د:B005/m01`; Mount Uhud `ء ح د:B006/m01`
- Ayah anchors: 90:17 `صَّبْرِ` (ص ب ر); 90:4 `كَبَدٍ` (ك ب د); 90:5, 90:7 `أَحَدٌ` (ء ح د); no independent surface occurrence for ء ص د
- Synthesis: These motifs give height internal structure: a central mass rises into a ridge, contains hollows, and can become a named landmark. Uhud supplies the proper-name culmination of that mountain image.

#### Subchannel D. Inhabited Land and Stable Dwelling
- Reading type: mixed
- Scene or process: People descend into a bounded place, inhabit it, and become its settled residents.
- Active motifs: bounded land or town `ب ل د:B001/m01`; alighting and settling `ح ل ل:B002/m01`; inhabiting a home `س ك ن:B002/m01`; dwelling site or layer `س ك ن:B009/m01`; place and established position `ك و ن:B002/m01`; remaining in the town `ب ل د:B009/m01`; resident inhabitant `ن ج د:B012/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:2 `حِلٌّ` (ح ل ل); 90:16 `مِسْكِينًا` (س ك ن); 90:17 `كَانَ` (ك و ن); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د)
- Synthesis: Settlement is a sequence of arrival, location, residence, and persistence. A bounded site becomes a social place when descent into it is followed by inhabitation and continued presence across its dwellings or layers.

#### Subchannel E. Wilderness, Remoteness, and Disorientation
- Reading type: latent/lexical
- Scene or process: A traveler or nomad moves through remote waste, circles without direction, and risks destruction.
- Active motifs: uninhabited wilderness `ب ل د:B001/m02`; remote village, grave, or cut-off place `ك ف ر:B012/m01`; deadly waste or chasm `ه ل ك:B006/m01`; desert traveler without driver `ق ح م:B006/m01`; circling in bewilderment `ه ل ك:B010/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:19 `كَفَرُوا` (ك ف ر); 90:6 `أَهْلَكْتُ` (ه ل ك); 90:11 `ٱقْتَحَمَ` (ق ح م)
- Synthesis: Outside settled land, movement loses its markers. The undriven desert passage, circling bewilderment, and remote cut-off place form a coherent scene of exposure without orientation.

#### Subchannel F. Ground Contact, Burial, and Staying Put
- Reading type: mixed
- Scene or process: Bodies, basins, and residents lower themselves to the earth and remain attached to it.
- Active motifs: soil and dust `ت ر ب:B001/m01`; grave within bounded land `ب ل د:B001/m03`; grave sides `ص ب ر:B004/m03`; striking or clinging to ground `ب ل د:B010/m01`; staying and adhering `ل ب د:B003/m01`; camel breast lowered in kneeling `ب ل د:B002/m02`
- Ayah anchors: 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:17 `صَّبْرِ` (ص ب ر); 90:6 `لُّبَدًا` (ل ب د)
- Synthesis: Grounding ranges from habitation to burial and animal posture, but the operation remains the same: descent ends in sustained contact with earth, while the grave's sides define the final bounded space.

#### Subchannel G. Small-Vessel Passage
- Reading type: latent/lexical
- Scene or process: A small attendant boat is stabilized and steered alongside a larger journey.
- Active motifs: small tender or skiff `ق ر ب:B011/m01`; rudder that stills the vessel `س ك ن:B008/m01`; travel equipment for repeated encampment `ح ل ل:B013/m01`; movement toward a needed destination `ن ج د:B004/m01`
- Ayah anchors: 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:16 `مِسْكِينًا` (س ك ن); 90:2 `حِلٌّ` (ح ل ل); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د)
- Synthesis: The tender, rudder, and portable gear form a complete mobility scene: a small craft carries immediate needs while controlled steering keeps passage from becoming drift.

### 3. Perception, Signs, and Surveillance
- Semantic invariant: Perception turns visible forms into knowledge, protection, warning, or public evidence.
- Surface relation: direct; 90:7 asks whether anyone saw, 90:8 names the two eyes, and 90:19 names denied signs.
- Surprising reach: Perception extends to spies, mirrors, evil-eye injury, dreams, menstrual and gestational signs, banners, and target appraisal.

#### Subchannel A. Direct Sight and Eyewitness Knowledge
- Reading type: surface-primary
- Scene or process: An eye encounters an object or a facing group directly and converts mutual visibility into certain knowledge.
- Active motifs: seeing eye `ع ي ن:B001/m01`; eyewitness encounter `ع ي ن:B002/m01`; sensory sight `ر ء ي:B001/m01`; mutually visible facing groups `ر ء ي:B004/m01`; noticing by sight or hearing `ء ن س:B002/m01`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:7 `يَرَهُ` (ر ء ي); 90:4 `ٱلْإِنسَٰنَ` (ء ن س)
- Synthesis: The scene moves from organ to encounter to cognition. Direct or reciprocal visibility is not merely optical; it is the basis for certainty that an act or opposing group has been witnessed.

#### Subchannel B. Protective Eye and Harmful Gaze
- Reading type: latent/lexical
- Scene or process: The gaze either keeps a person under care or inflicts injury through hostile attention.
- Active motifs: protective and honoring eye `ع ي ن:B003/m01`; evil-eye injury `ع ي ن:B004/m01`; guarding accompaniment `ص ح ب:B002/m01`; vigilant guard `ر ق ب:B002/m01`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Attention is ethically reversible. The same focused gaze can preserve, honor, and guard, or become an assault that damages what it fixes upon.

#### Subchannel C. Pupil, Mirror, and Reflected Person
- Reading type: latent/lexical
- Scene or process: A person appears as a small image in the pupil or as a visible form in a mirror.
- Active motifs: human image in the pupil `ء ن س:B005/m01`; mirror and facial appearance `ر ء ي:B006/m01`; wide-eyed beauty `ع ي ن:B016/m01`; visible form `خ ل ق:B003/m01`
- Ayah anchors: 90:4 `ٱلْإِنسَٰنَ`, `خَلَقْنَا` (ء ن س, خ ل ق); 90:7 `يَرَهُ` (ر ء ي); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Reflection miniaturizes the human form without losing recognizability. Pupil, mirror, face, and formed appearance make seeing a scene in which the observer also receives an image of a person.

#### Subchannel D. Scout, Spy, and Lookout
- Reading type: latent/lexical
- Scene or process: An observer occupies a vantage, gathers news, and protects a group through advance warning.
- Active motifs: waiting surveillance `ر ق ب:B001/m01`; guard or scout `ر ق ب:B002/m01`; elevated lookout `ر ق ب:B003/m01`; spy or advance observer `ع ي ن:B005/m01`; seeking news `ح س ب:B010/m01`
- Ayah anchors: 90:13 `رَقَبَةٍ` (ر ق ب); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:5, 90:7 `أَيَحْسَبُ` (ح س ب)
- Synthesis: The role map is complete: a lookout occupies height, watches and waits, then returns intelligence that allows the guarded community to act.

#### Subchannel E. Visible Sign, Banner, and Beacon
- Reading type: mixed
- Scene or process: A conspicuous object is raised or illuminated so a group can recognize identity and direction.
- Active motifs: visible sign or grouped letters `ء ي ي:B003/m01`; raised flag `ر ء ي:B011/m01`; raptor-shaped banner `ع ق ب:B013/m02`; road beacon or tower `ن و ر:B005/m01`
- Ayah anchors: 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:7 `يَرَهُ` (ر ء ي); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:20 `نَارٌ` (ن و ر)
- Synthesis: Sign, flag, and beacon share deliberate visibility. Each concentrates meaning into a form placed where it can orient collective attention.

#### Subchannel F. Dream, Apparition, and Bodily Indicator
- Reading type: latent/lexical
- Scene or process: An otherwise hidden state becomes legible through a dream, apparition, stain, or bodily change.
- Active motifs: dream image `ر ء ي:B003/m01`; appearing jinn companion `ر ء ي:B008/m01`; menstrual indicator `ر ء ي:B007/m01`; visible animal pregnancy `ر ء ي:B010/m01`; eye-like notch or mark `ع ي ن:B009/m01`
- Ayah anchors: 90:7 `يَرَهُ` (ر ء ي); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: These are diagnostic appearances rather than ordinary objects of sight. Each visible token points beyond itself to sleep, spirit presence, bodily cycle, pregnancy, or hidden structure.

#### Subchannel G. Disclosure and Target Appraisal
- Reading type: mixed
- Scene or process: Something is deliberately shown, recognized, and assessed before action.
- Active motifs: causing another to see `ر ء ي:B012/m01`; knowledge and instruction `د ر ي:B001/m01`; eye's appraisal of size or worth `ق ح م:B007/m01`; intentional targeting of a person's sign `ء ي ي:B002/m01`
- Ayah anchors: 90:7 `يَرَهُ` (ر ء ي); 90:12 `أَدْرَىٰكَ` (د ر ي); 90:11 `ٱقْتَحَمَ` (ق ح م); 90:19 `ءَايَٰتِنَا` (ء ي ي)
- Synthesis: Disclosure makes an object available for judgment; appraisal then estimates its scale or value, and targeting converts that estimate into directed attention.

### 4. Speech, Reputation, and Discursive Action
- Semantic invariant: Speech moves from bodily articulation to social circulation, attribution, negotiation, and authoritative formulation.
- Surface relation: direct; 90:6 foregrounds saying, 90:9 names tongue and lips, and 90:17 depicts reciprocal counsel.
- Surprising reach: Speech can become a circulating reputation, an appropriated saying, fabricated authorship, political rule, or an inward doctrine never voiced.

#### Subchannel A. Tongue, Lips, and Face-to-Face Speech
- Reading type: surface-primary
- Scene or process: Breath and articulation pass through tongue and lips into spoken address between persons.
- Active motifs: organ of speech `ل س ن:B001/m01`; lips `ش ف ه:B001/m01`; mouth-to-mouth address `ش ف ه:B002/m01`; spoken utterance `ق و ل:B001/m01`; tongue as speech instrument `ق و ل:B002/m01`
- Ayah anchors: 90:9 `لِسَانًا وَشَفَتَيْنِ` (ل س ن, ش ف ه); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: The channel assembles the speaker's apparatus, the produced utterance, and the interpersonal setting in which speech passes directly from one mouth to another.

#### Subchannel B. Eloquence, Verbal Attack, and Silencing
- Reading type: latent/lexical
- Scene or process: A skilled tongue presses an argument or attack until injury or cutting removes its force.
- Active motifs: eloquence and argumentative fluency `ل س ن:B003/m01`; verbal assault `ل س ن:B002/m01`; prolific speaker `ق و ل:B003/m01`; cutting the tongue-tip `ل س ن:B005/m01`
- Ayah anchors: 90:9 `لِسَانًا` (ل س ن); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Speech is treated as an exercised capacity that can dominate a contest. The cut tongue supplies the bodily reversal of that power: articulation is stopped at its instrument.

#### Subchannel C. Message Relay and Shared Language
- Reading type: mixed
- Scene or process: A message is carried through a language and delivered from one person to another.
- Active motifs: language and verbal message `ل س ن:B006/m01`; relaying a message `ل س ن:B008/m01`; reciprocal counsel `و ص ي:B003/m01`; circulating speech `ق و ل:B007/m01`
- Ayah anchors: 90:9 `لِسَانًا` (ل س ن); 90:17 `تَوَاصَوْا` (و ص ي); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Language supplies the code, relay supplies transmission, and reciprocal counsel supplies the social network. Speech becomes a durable relation rather than a single utterance.

#### Subchannel D. Reputation, Praise, and Ostentation
- Reading type: latent/lexical
- Scene or process: Conduct becomes visible talk, producing either earned praise or performative display.
- Active motifs: good public mention `ش ف ه:B004/m01`; speech circulating among people `ق و ل:B007/m01`; action performed to be seen `ر ء ي:B005/m01`; inherited honor and memorable deeds `ح س ب:B004/m01`
- Ayah anchors: 90:9 `شَفَتَيْنِ` (ش ف ه); 90:6 `يَقُولُ` (ق و ل); 90:7 `يَرَهُ` (ر ء ي); 90:5, 90:7 `أَيَحْسَبُ` (ح س ب)
- Synthesis: Public standing is produced by a loop between action, visibility, and retelling. Praise records recognized worth, while ostentation tries to manufacture the same outcome by staging the act for observers.

#### Subchannel E. Fabrication, Attribution, and Appropriated Speech
- Reading type: latent/lexical
- Scene or process: Words are invented, falsely assigned, or pulled into a speaker's possession.
- Active motifs: fabricated discourse `خ ل ق:B007/m01`; false attribution of words `ق و ل:B005/m01`; appropriating a saying `ق و ل:B006/m01`; generated or coined expression `و ل د:B005/m02`; falling into a valley of falsehood `ه ل ك:B011/m01`
- Ayah anchors: 90:4 `خَلَقْنَا` (خ ل ق); 90:6 `يَقُولُ`, `أَهْلَكْتُ` (ق و ل, ه ل ك); 90:3 `وَلَدَ` (و ل د)
- Synthesis: Authorship is the contested object. Fabrication creates what was not said, false attribution assigns it to another, and appropriation draws existing speech into one's own claim; the valley image gives continued falsehood a path into which the speaker falls.

#### Subchannel F. Negotiation, Rule, and Formal Position
- Reading type: latent/lexical
- Scene or process: Parties exchange statements until a ruling, doctrine, or definition fixes the matter.
- Active motifs: negotiation `ق و ل:B009/m01`; imposing a ruling `ق و ل:B010/m01`; doctrinal position `ق و ل:B013/m01`; signification `ق و ل:B014/m01`; formal definition `ق و ل:B016/m01`
- Ayah anchors: 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Discursive action progresses from bargaining to determination. A position may become a doctrine, a sign may be read as speaking, and a definition closes the exchange by fixing a conceptual boundary.

### 5. Question, Reference, and Language Form
- Semantic invariant: Language directs attention by selecting a referent, opening a question, locating it in time, or marking the form of address.
- Surface relation: indirect; interrogative framing appears at 90:5, 90:7, and 90:12, demonstrative `هَٰذَا` at 90:1-2, and relational `ذِي/ذَا` at 90:14-16.
- Surprising reach: The network reaches pronoun supports, vocatives, explanatory particles, alphabetic names, oath-openers, and poetic meter.

#### Subchannel A. Interrogative Selection and Requested Answer
- Reading type: mixed
- Scene or process: A speaker selects an unknown referent and asks the addressee to identify or state it.
- Active motifs: interrogative and selective `أي` `ء ي ي:B004/m01`; compound `ماذا` question `ذ و و:B004/m01`; interrogative `ها` replacing alif `ه ا ء:B004/m01`; attention-seeking `أرأيتك` `ر ء ي:B013/m01`; inquiry that elicits knowledge `د ر ي:B001/m02`
- Ayah anchors: 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:14 `ذِي`, 90:15-16 `ذَا` (ذ و و); 90:7 `يَرَهُ` (ر ء ي); 90:12 `أَدْرَىٰكَ` (د ر ي); interrogative frames at 90:5, 90:7, 90:12; related `هَٰذَا` at 90:1-2 (ه ا ء)
- Synthesis: Selection, attention, and requested knowledge form one discourse event: the speaker isolates a matter, turns the addressee toward it, and demands an answer.

#### Subchannel B. Demonstrative and Pronominal Pointing
- Reading type: mixed
- Scene or process: A form points to a present or conceptual object and anchors a pronoun to it.
- Active motifs: demonstrative `ذا` `ذ و و:B003/m01`; pronoun support `إيا` `ء ي ي:B005/m01`; relative connector `ذو` `ذ و و:B002/m01`; attention-opening `ها` `ه ا ء:B002/m01`
- Ayah anchors: 90:1-2 `هَٰذَا` (ه ا ء); 90:14 `ذِي`, 90:15-16 `ذَا` (ذ و و); 90:19 `ءَايَٰتِنَا` (ء ي ي)
- Synthesis: Pointing is assembled from an alert, a deictic center, and a referring form. Together they bring an object into shared attention and maintain its grammatical identity.

#### Subchannel C. Temporal and Quantitative Question
- Reading type: latent/lexical
- Scene or process: Inquiry asks either when an event will occur or how many instances are involved.
- Active motifs: temporal `أيان` `ء ي ي:B006/m01`; large-number `كأين` `ء ي ي:B007/m01`; duration rather than calendar day `ي و م:B002/m01`; counted unit `ء ح د:B003/m01`
- Ayah anchors: 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:14 `يَوْمٍ` (ي و م); 90:5, 90:7 `أَحَدٌ` (ء ح د)
- Synthesis: Time and quantity are parallel unknowns. Both require a bounded unit, then open that unit to questions of occurrence, duration, or multiplicity.

#### Subchannel D. Vocative, Response, and Explanation
- Reading type: latent/lexical
- Scene or process: A call gains attention, receives an answer, and is followed by an explanatory reformulation.
- Active motifs: near or distant vocative `ء ي ي:B008/m01`; answering or answering a call `ه ا ء:B003/m01`; explanatory `أي` `ء ي ي:B009/m01`; handover command `ها` `ه ا ء:B001/m01`
- Ayah anchors: 90:19 `ءَايَٰتِنَا` (ء ي ي); related deictic `هَٰذَا` at 90:1-2 (ه ا ء)
- Synthesis: The discourse sequence is call, response, clarification, and transfer. It turns attention into an exchange in which meaning or an object is handed to the addressee.

#### Subchannel E. Letter, Sound, and Poetic Alternation
- Reading type: latent/lexical
- Scene or process: Speech is analyzed into a named letter, arranged into verse, and governed by alternating metrical positions.
- Active motifs: letter-name `هاء` `ه ا ء:B006/m01`; lip-formed letters `ش ف ه:B001/m02`; poetic exchange of praise or satire `ه د ي:B011/m01`; metrical alternation `ر ق ب:B014/m01`; poet-name Labid `ل ب د:B008/m01`
- Ayah anchors: 90:9 `شَفَتَيْنِ` (ش ف ه); 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:13 `رَقَبَةٍ` (ر ق ب); 90:6 `لُّبَدًا` (ل ب د); related `هَٰذَا` at 90:1-2 (ه ا ء)
- Synthesis: Language becomes an explicit craft: articulation supplies phonetic material, meter regulates alternation, and poetic exchange directs the finished speech toward another person.

#### Subchannel F. Personal and Place Names
- Reading type: latent/lexical
- Scene or process: Ordinary lexical forms become proper names that identify a person, poet, mountain, or locality.
- Active motifs: Jacob as a personal name `ع ق ب:B014/m01`; poet-name Labid `ل ب د:B008/m01`; Mount Uhud `ء ح د:B006/m01`; localities named Yathrib, Turba, or Turban `ت ر ب:B008/m01`; al-Ja'la as a place name `ج ع ل:B011/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:6 `لُّبَدًا` (ل ب د); 90:5, 90:7 `أَحَدٌ` (ء ح د); 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:8 `نَجْعَل` (ج ع ل)
- Synthesis: Proper naming fixes reference by attaching a lexical form to one recognized bearer. The same operation identifies individuals, authored speech, a mountain, and inhabited places.

### 6. Creation, Form, and Transformation
- Semantic invariant: Making moves from measure and design through embodied form to changed state and generated result.
- Surface relation: direct; 90:4 names creation, 90:8 names making, and 90:3 names generation.
- Surprising reach: Formation includes inward character, aptitude, generated language, smooth stone, and the persistence implied by "beginning to do."

#### Subchannel A. Measured Design and Creation
- Reading type: surface-primary
- Scene or process: A thing is measured, designed, and then brought into existence.
- Active motifs: prior measuring and design `خ ل ق:B001/m01`; originating creation `خ ل ق:B002/m01`; making or producing `ج ع ل:B001/m01`; bounded measure and term `ق د ر:B001/m01`
- Ayah anchors: 90:4 `خَلَقْنَا` (خ ل ق); 90:8 `نَجْعَل` (ج ع ل); 90:5 `يَقْدِرَ` (ق د ر)
- Synthesis: Creation is not an unstructured event. Measure supplies proportion, design supplies intelligible form, and making realizes what was first delimited.

#### Subchannel B. Outward Form and Inward Character
- Reading type: mixed
- Scene or process: A formed body presents a visible shape while carrying an inward disposition.
- Active motifs: complete visible form `خ ل ق:B003/m01`; inward character `خ ل ق:B004/m01`; robust coarse physique `ب ل د:B008/m01`; body's protruding middle `ك ب د:B006/m01`; short stout build with obstinate character `ج ع ل:B012/m01`; closely joined bodily build `ط ع م:B014/m01`
- Ayah anchors: 90:4 `خَلَقْنَا`, `كَبَدٍ` (خ ل ق, ك ب د); 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:8 `نَجْعَل` (ج ع ل); 90:14 `إِطْعَٰمٌ` (ط ع م)
- Synthesis: Form has two registers: the body's proportions and the character expressed through conduct. Robustness, stoutness, joined bodily structure, prominence, and obstinacy show how visible physique and attributed disposition can be described together.

#### Subchannel C. Aptitude and Receptivity
- Reading type: latent/lexical
- Scene or process: A person or material is disposed toward an action and either receives or resists correction.
- Active motifs: readiness or worthiness `خ ل ق:B005/m01`; capacity to receive reform `ط ع م:B008/m02`; dull weakness `ه د ي:B009/m01`; loose, incoherent judgment `ف ك ك:B006/m01`
- Ayah anchors: 90:4 `خَلَقْنَا` (خ ل ق); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: Aptitude is a latent fit between a person and a task. Receptive judgment can be shaped by correction, while dullness and loosened judgment mark failure of that fit.

#### Subchannel D. Transformation, Commencement, and Generated Result
- Reading type: latent/lexical
- Scene or process: An existing thing is put into a new state, begins an action, and produces a derived outcome.
- Active motifs: transforming into a condition `ج ع ل:B002/m01`; beginning or persisting in action `ج ع ل:B004/m01`; occurrence in time `ك و ن:B001/m01`; generated outcome `و ل د:B005/m01`
- Ayah anchors: 90:8 `نَجْعَل` (ج ع ل); 90:17 `كَانَ` (ك و ن); 90:3 `وَلَدَ` (و ل د)
- Synthesis: Change is presented as a process rather than a static label: transformation establishes a condition, commencement sustains its operation, and generation names what emerges from it.

### 7. Birth, Descent, and Life Stage
- Semantic invariant: Life is organized by parentage, delivery, dependency, maturation, aging, and loss of caregivers.
- Surface relation: direct; 90:3 names parent and offspring, while 90:15 names the orphan.
- Surprising reach: The life-course network includes postpartum pain, near birth, age peers, a son becoming his father's companion, precocious animal aging, widowhood, and childlessness.

#### Subchannel A. Parent, Offspring, and Posterity
- Reading type: surface-primary
- Scene or process: Parents generate offspring who remain as descendants after them.
- Active motifs: offspring `و ل د:B001/m01`; father and mother as parents `و ل د:B002/m01`; surviving descendants `ع ق ب:B004/m01`; kinship by descent `ق ر ب:B003/m01`
- Ayah anchors: 90:3 `وَالِدٍ وَمَا وَلَدَ` (و ل د); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: Generation establishes a line rather than an isolated birth. Parentage creates the child, descent carries that relation forward, and posterity preserves it beyond the first generation.

#### Subchannel B. Womb, Delivery, and Postpartum Pain
- Reading type: latent/lexical
- Scene or process: A fetus develops in the womb, while bodily closure or loosening governs whether approaching delivery can occur and what pain follows it.
- Active motifs: womb as container of offspring `ر ح م:B003/m01`; imperforate reproductive closure likened to smooth rock `خ ل ق:B012/m01`; body loosening around birth `ف ك ك:B007/m02`; occurrence of birth `و ل د:B003/m01`; nearness of delivery `ق ر ب:B012/m01`; postpartum uterine pain `ر ح م:B004/m01`
- Ayah anchors: 90:17 `مَرْحَمَةِ` (ر ح م); 90:4 `خَلَقْنَا` (خ ل ق); 90:13 `فَكُّ` (ف ك ك); 90:3 `وَلَدَ` (و ل د); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: The scene follows a reproductive sequence of containment, bodily opening, approaching term, delivery, and aftermath. Imperforate closure supplies the obstructed contrast to the loosening required for birth.

#### Subchannel C. Newborn Dependency and Lost Care
- Reading type: mixed
- Scene or process: A newly born child depends on a caregiver and becomes exposed when that protecting parent is lost.
- Active motifs: newborn child or young dependent `و ل د:B004/m01`; orphaned child `ي ت م:B001/m01`; protective accompaniment `ص ح ب:B002/m01`; delayed care reaching the orphan `ي ت م:B004/m02`
- Ayah anchors: 90:3 `وَلَدَ` (و ل د); 90:15 `يَتِيمًا` (ي ت م); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: Dependency gives orphanhood its social force. The newborn needs accompaniment, and the orphan is defined by the interruption or delay of that care.

#### Subchannel D. Age Peers and Maturing Companionship
- Reading type: latent/lexical
- Scene or process: Those born in the same period grow as peers, and a son matures until he can accompany his father.
- Active motifs: age peers raised together `ت ر ب:B004/m01`; coeval by birth `و ل د:B006/m01`; son reaching companionable adulthood `ص ح ب:B005/m01`; noble full siblings `ع ي ن:B015/m02`
- Ayah anchors: 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:3 `وَلَدَ` (و ل د); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Shared age becomes shared social capacity. Peers mature together, while the child-parent relation changes when the son can stand beside the father as a companion.

#### Subchannel E. Old Age, Childlessness, and Spousal Solitude
- Reading type: latent/lexical
- Scene or process: Aging can end in frailty, lack of surviving children, or a woman left without a spouse.
- Active motifs: decrepit old age `ق ح م:B004/m01`; old man recalling former life `ك و ن:B005/m01`; parent without surviving child `ر ق ب:B008/m01`; woman without spouse `ي ت م:B005/m01`
- Ayah anchors: 90:11 `ٱقْتَحَمَ` (ق ح م); 90:17 `كَانَ` (ك و ن); 90:13 `رَقَبَةٍ` (ر ق ب); 90:15 `يَتِيمًا` (ي ت م)
- Synthesis: The late-life scene is defined by altered dependency and absence. Physical decline is compounded when descendants or a spouse no longer sustain the household relation.

### 8. Kinship, Household, and Companionship
- Semantic invariant: Social proximity is created by descent, co-residence, chosen intimacy, and shared group membership.
- Surface relation: direct; 90:15 names near kin, 90:17 commands mercy, and 90:18-19 names companion-groups.
- Surprising reach: Companionship reaches marriage, household inhabitants, confidants, comforting objects, noble siblings, and present witnesses.

#### Subchannel A. Kinship and Womb-Tie
- Reading type: surface-primary
- Scene or process: Near relatives recognize and maintain a relation grounded in common descent.
- Active motifs: kinship tie `ر ح م:B002/m01`; near relative `ق ر ب:B003/m01`; possessor or person characterized by relation `ذ و و:B001/m01`; compassion toward kin `ر ح م:B001/m01`
- Ayah anchors: 90:17 `مَرْحَمَةِ` (ر ح م); 90:15 `ذَا مَقْرَبَةٍ` (ذ و و, ق ر ب)
- Synthesis: Biological relation becomes a social obligation through recognition and compassion. The relational `ذو` construction identifies the person by the tie that calls care into action.

#### Subchannel B. Marriage and Cohabiting Household
- Reading type: latent/lexical
- Scene or process: Spouses enter a shared dwelling and become each other's household companions.
- Active motifs: husband and wife as cohabitants `ح ل ل:B006/m01`; household residents `س ك ن:B003/m01`; bride delivered to her spouse `ه د ي:B006/m01`; marital approach `ق ر ب:B007/m02`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:16 `مِسْكِينًا` (س ك ن); 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: Marriage is rendered as movement into shared place: the bride is brought, approach becomes intimacy, and co-residence establishes a household.

#### Subchannel C. Confidant, Solace, and Intimate Company
- Reading type: latent/lexical
- Scene or process: A chosen companion removes estrangement and becomes a trusted source of comfort.
- Active motifs: companionship that removes loneliness `ء ن س:B003/m01`; intimate confidant `ء ن س:B006/m02`; continuing companion `ص ح ب:B001/m01`; object or person in whom the soul rests `س ك ن:B004/m01`
- Ayah anchors: 90:4 `ٱلْإِنسَٰنَ` (ء ن س); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:16 `مِسْكِينًا` (س ك ن)
- Synthesis: Intimacy is a change of state from estrangement to repose. The companion is not merely adjacent but actively makes the other feel settled.

#### Subchannel D. Cohort, Sibling, and Present Community
- Reading type: mixed
- Scene or process: Peers, siblings, and present household members constitute a visible social body.
- Active motifs: coeval cohort `ت ر ب:B004/m01`; full siblings `ع ي ن:B015/m02`; people presently assembled `ع ي ن:B017/m01`; human community opposed to wildness `ء ن س:B001/m01`
- Ayah anchors: 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:4 `ٱلْإِنسَٰنَ` (ء ن س)
- Synthesis: Community becomes perceptible through shared age, shared parentage, and shared presence. These relations turn separate persons into an identifiable cohort.

### 9. Wealth, Provision, and Deprivation
- Semantic invariant: Material life moves between accumulation, livelihood, feeding, hunger, and the loss of means.
- Surface relation: direct; 90:6 names spent wealth, 90:14 feeding in famine, and 90:16 the destitute person in dust.
- Surprising reach: Provision includes wages, hospitality revenue, food heaps, relentless demand, animal appetite, and the idiom of possessing neither hair nor felt.

#### Subchannel A. Accumulated Wealth and Dense Abundance
- Reading type: surface-primary
- Scene or process: Property is acquired and amassed until it appears as a compact pile or crowd.
- Active motifs: acquisition and abundance of wealth `م و ل:B001/m01`; wealth piled densely `ل ب د:B002/m01`; prosperity figured as abundant soil `ت ر ب:B003/m01`; present capital `ع ي ن:B011/m01`
- Ayah anchors: 90:6 `مَالًا لُّبَدًا` (م و ل, ل ب د); 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Abundance is given both economic and spatial form. Wealth becomes present capital, then accumulates visibly as material laid layer upon layer.

#### Subchannel B. Livelihood, Wage, and Hospitality
- Reading type: mixed
- Scene or process: Work or productive property yields income that can sustain a household and host others.
- Active motifs: livelihood and hospitality revenue `ط ع م:B004/m01`; wage assigned for work `ج ع ل:B005/m01`; sufficiency and adequate provision `ح س ب:B003/m01`; repeated requests that deplete supplies `ش ف ه:B003/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:8 `نَجْعَل` (ج ع ل); 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:9 `شَفَتَيْنِ` (ش ف ه)
- Synthesis: Provision has an acquisition side and a distribution side. Wage and productive income create sufficiency; hospitality and repeated demand test how long that sufficiency lasts.

#### Subchannel C. Feeding During Famine
- Reading type: surface-primary
- Scene or process: Food is deliberately transferred to a hungry person during a severe day of scarcity.
- Active motifs: feeding another `ط ع م:B002/m01`; hunger with exhaustion `س غ ب:B001/m01`; severe event or day `ي و م:B003/m01`; distress and constriction `ن ج د:B005/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ فِى يَوْمٍ ذِى مَسْغَبَةٍ` (ط ع م, ي و م, س غ ب); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د)
- Synthesis: The scene joins need, timing, and response. Feeding matters because famine has turned an ordinary day into a constricted event in which the recipient cannot secure food unaided.

#### Subchannel D. Appetite, Food Heap, and Competition
- Reading type: latent/lexical
- Scene or process: Food is amassed, approached by appetite, and contested by those pressing toward it.
- Active motifs: eating and tasting `ط ع م:B001/m01`; piled provisions `ص ب ر:B011/m02`; ravenous competition `ه ل ك:B012/m01`; dense crowding `ل ب د:B002/m02`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:17 `صَّبْرِ` (ص ب ر); 90:6 `أَهْلَكْتُ`, `لُّبَدًا` (ه ل ك, ل ب د)
- Synthesis: The prepared food heap becomes the center of a social pressure field. Appetite draws bodies inward, and abundance can paradoxically produce crowding and rivalry.

#### Subchannel E. Poverty, Dust, and Dependence
- Reading type: surface-primary
- Scene or process: Loss of means lowers a person toward the ground and forces dependence on others.
- Active motifs: poverty figured as clinging to dust `ت ر ب:B002/m01`; destitution and abasement `س ك ن:B006/m01`; petitioner seeking a sponsor `ه ل ك:B004/m01`; having neither little nor much `ل ب د:B007/m01`
- Ayah anchors: 90:16 `مِسْكِينًا ذَا مَتْرَبَةٍ` (س ك ن, ت ر ب); 90:6 `أَهْلَكْتُ`, `لُّبَدًا` (ه ل ك, ل ب د)
- Synthesis: Poverty is embodied as lowered posture, bare ground, and absent property. Dependence follows because the destitute person must seek the sustaining relation no longer supplied by possessions.

### 10. Trust, Liability, and Legal Continuity
- Semantic invariant: Social and economic obligations persist through trust, debt, guarantee, testament, inheritance, and exchange.
- Surface relation: direct; 90:13 gives the release of a bound person, and 90:17 gives trusted belief and reciprocal injunction.
- Surprising reach: Obligation extends to survivorship gifts, collateral inheritance, delayed payment, ready cash, credit sales, and the "neck" or principal of property.

#### Subchannel A. Security, Trust, and Entrustment
- Reading type: mixed
- Scene or process: Fear is stilled because a reliable person guards what has been entrusted.
- Active motifs: security and trustworthy custody `ء م ن:B001/m01`; guarding accompaniment `ص ح ب:B002/m01`; guardian or watchman `ر ق ب:B002/m01`; guarantor's continuing presence `ص ب ر:B003/m01`
- Ayah anchors: 90:17 `ءَامَنُوا` (ء م ن); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:13 `رَقَبَةٍ` (ر ق ب); 90:17 `صَّبْرِ` (ص ب ر)
- Synthesis: Trust is operational rather than merely emotional: custody is accepted, guarding continues, and a responsible person remains answerable for the entrusted object or person.

#### Subchannel B. Debt, Term, and Due Penalty
- Reading type: latent/lexical
- Scene or process: A debt, right, offering, or penalty reaches the point at which it must be discharged.
- Active motifs: debt or right becoming due `ح ل ل:B004/m01`; fixed amount and term `ق د ر:B001/m01`; penalty following an offense `ع ق ب:B007/m01`; final consequence `ع ق ب:B006/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:5 `يَقْدِرَ` (ق د ر); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب)
- Synthesis: Liability matures through time. Measure fixes the obligation, arrival at its term makes it due, and consequence or penalty follows if the claim remains unanswered.

#### Subchannel C. Surety, Substitute, and Payment Hold
- Reading type: latent/lexical
- Scene or process: A guarantor or substitute stands in place of another while goods or payment remain held.
- Active motifs: personal surety `ص ب ر:B003/m01`; substitute and warranty `ع ق ب:B010/m01`; standing as another's guarantor `ك و ن:B003/m01`; redemption of collateral `ف ك ك:B002/m01`
- Ayah anchors: 90:17 `صَّبْرِ`, `كَانَ` (ص ب ر, ك و ن); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: Substitution redistributes risk without dissolving it. The guarantor carries the claim until payment, delivery, or redemption releases the held property.

#### Subchannel D. Testament, Executor, and Aftermath
- Reading type: mixed
- Scene or process: A person's instruction is connected to an executor who carries it beyond the speaker's death.
- Active motifs: testament and appointed executor `و ص ي:B002/m01`; continuing connection `و ص ي:B001/m01`; aftermath and outcome `ع ق ب:B006/m01`; remaining trace `ع ق ب:B011/m01`
- Ayah anchors: 90:17 `تَوَاصَوْا` (و ص ي); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب)
- Synthesis: A testament is speech designed to survive its source. The executor provides continuity, while aftermath and remaining trace describe the world in which the instruction must still operate.

#### Subchannel E. Survivorship, Inheritance, and Capital
- Reading type: latent/lexical
- Scene or process: Property passes to survivors, descendants, or collateral heirs and is distinguished as principal capital.
- Active motifs: survivorship gift `ر ق ب:B005/m01`; collateral inheritance `ر ق ب:B013/m01`; descendant or successor `ر ق ب:B015/m01`; choice property `ر ق ب:B012/m01`; present cash `ع ي ن:B011/m01`; credit sale `ع ي ن:B012/m01`
- Ayah anchors: 90:13 `رَقَبَةٍ` (ر ق ب); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: The legal scene follows assets across time and form: a gift is conditioned on survival, inheritance identifies the next holder, and exchange distinguishes present principal from deferred credit.

### 11. Counsel, Endurance, Mercy, and Protection
- Semantic invariant: Vulnerable persons and difficult actions are sustained through reciprocal instruction, self-command, compassion, and protective presence.
- Surface relation: direct; 90:17 joins belief to mutual counsel in patience and mercy.
- Surprising reach: Care appears as a companion who removes fear, a guarantor who stays, a warning against relapse, and a guard who preserves another through watchfulness.

#### Subchannel A. Reciprocal Counsel
- Reading type: surface-primary
- Scene or process: Members of a community repeatedly direct one another toward conduct they must sustain together.
- Active motifs: reciprocal injunction `و ص ي:B003/m01`; message relay `ل س ن:B008/m01`; negotiated discussion `ق و ل:B009/m01`; continuing companionship `ص ح ب:B001/m01`
- Ayah anchors: 90:17 `تَوَاصَوْا` (و ص ي); 90:9 `لِسَانًا` (ل س ن); 90:6 `يَقُولُ` (ق و ل); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: Counsel is a circulating social process. Advice is voiced, relayed, considered with others, and maintained by companions who remain present to one another.

#### Subchannel B. Patience, Stillness, and Composure
- Reading type: surface-primary
- Scene or process: A person restrains panic and remains steady through a condition that invites agitation or retreat.
- Active motifs: holding the self from distress `ص ب ر:B001/m01`; stillness after movement `س ك ن:B001/m01`; calm bearing without flight `ه د ي:B010/m01`; ordeal with no easy outlet `ص ب ر:B006/m01`
- Ayah anchors: 90:17 `صَّبْرِ` (ص ب ر); 90:16 `مِسْكِينًا` (س ك ن); 90:10 `هَدَيْنَٰهُ` (ه د ي)
- Synthesis: Patience is embodied as regulated motion. The self does not scatter, the body does not flee, and composure maintains direction inside an inescapable trial.

#### Subchannel C. Mercy and Protective Care
- Reading type: surface-primary
- Scene or process: Compassion recognizes another's vulnerability and acts to preserve that person.
- Active motifs: tenderness and beneficent mercy `ر ح م:B001/m01`; sincere concern for a matter or person `ق و ل:B015/m01`; protective accompaniment `ص ح ب:B002/m01`; guarding and preservation `ر ق ب:B002/m01`; trusted security `ء م ن:B001/m01`
- Ayah anchors: 90:17 `مَرْحَمَةِ`, `ءَامَنُوا` (ر ح م, ء م ن); 90:6 `يَقُولُ` (ق و ل); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Mercy becomes concrete through sincere concern, presence, and guarding. Feeling for another leads to accompaniment, and accompaniment creates the security in which the vulnerable person can remain safe.

#### Subchannel D. Correction, Neglect, and Relapse
- Reading type: latent/lexical
- Scene or process: Counsel attempts to correct a person who may neglect the task, resist reform, or turn back after beginning.
- Active motifs: receptivity to correction `ط ع م:B008/m02`; negligence and shortfall `ي ت م:B003/m01`; retreat on the heel `ع ق ب:B003/m01`; reciprocal counsel `و ص ي:B003/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:15 `يَتِيمًا` (ي ت م); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:17 `تَوَاصَوْا` (و ص ي)
- Synthesis: Reform is a contested transition. Advice meets a recipient whose response may be receptive, negligent, or a reversal back along the path already entered.

#### Subchannel E. Exertion, Sweat, and Exhaustion
- Reading type: mixed
- Scene or process: A worker or traveler undertakes a severe task, sweats under effort or fear, and expends strength until exhaustion.
- Active motifs: hardship and sustained struggle `ك ب د:B002/m01`; sweat from labor, distress, or fear `ن ج د:B006/m01`; self-expenditure to exhaustion `ه ل ك:B009/m01`; road peril few will undertake `ق ح م:B002/m01`
- Ayah anchors: 90:4 `كَبَدٍ` (ك ب د); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:6 `أَهْلَكْتُ` (ه ل ك); 90:11 `ٱقْتَحَمَ` (ق ح م)
- Synthesis: Endurance is legible through bodily cost. Difficulty demands continued effort, sweat registers that effort, and exhaustion marks the point at which the task or road has consumed the traveler's available strength.

### 12. Belief, Oath, and Ritual
- Semantic invariant: Commitment is expressed through assent, sworn speech, expiation, responsive prayer, and offerings brought near.
- Surface relation: direct; 90:1 opens with an oath, 90:17 names belief, and 90:19 names denial of signs.
- Surprising reach: Ritual commitment reaches oath-release by a token act, "amen" as an answering formula, camouflaged sin erased by covering, and the offering's arrival at its lawful place.

#### Subchannel A. Assent, Doctrine, and Denial
- Reading type: surface-primary
- Scene or process: A proposition is inwardly assented to as truth or rejected despite its signs.
- Active motifs: settled assent `ء م ن:B002/m01`; denial and concealment of truth `ك ف ر:B003/m01`; attributing unbelief to another `ك ف ر:B006/m01`; doctrinal position `ق و ل:B013/m01`; visible sign `ء ي ي:B003/m01`
- Ayah anchors: 90:17 `ءَامَنُوا` (ء م ن); 90:19 `كَفَرُوا بِـَٔايَٰتِنَا` (ك ف ر, ء ي ي); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Belief and denial are opposing responses to a meaningful sign. Doctrine gives the response an articulated form, assent or rejection locates it in the heart, and accusation assigns that rejected status to another person.

#### Subchannel B. Ingratitude and Disavowal
- Reading type: latent/lexical
- Scene or process: A benefit or affiliation is first received, then denied, repudiated, or treated as though it carried no claim.
- Active motifs: covering a benefit with ingratitude `ك ف ر:B004/m01`; disavowing an affiliation `ك ف ر:B005/m01`; destruction through misuse `ه ل ك:B001/m01`; public claim of expenditure `ق و ل:B007/m02`
- Ayah anchors: 90:19 `كَفَرُوا` (ك ف ر); 90:6 `أَهْلَكْتُ`, `يَقُولُ` (ه ل ك, ق و ل)
- Synthesis: Disavowal breaks the expected relation between benefit and acknowledgment. The act may consume what was given while speech attempts to control how that consumption is publicly understood.

#### Subchannel C. Oath, Testimony, and Sworn Right Hand
- Reading type: surface-primary
- Scene or process: A speaker invokes an oath and binds the truth of a statement to sworn testimony.
- Active motifs: sworn oath `ق س م:B004/m01`; oath by the right hand `ي م ن:B003/m01`; oath-opening affirmation `ء ي ي:B010/m01`; allotted oaths in a blood claim `ق س م:B004/m02`
- Ayah anchors: 90:1 `أُقْسِمُ` (ق س م); 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:19 `ءَايَٰتِنَا` (ء ي ي)
- Synthesis: Oath speech creates a binding relation between speaker, claim, and consequence. The right hand and distributed testimony give that relation bodily and communal form.

#### Subchannel D. Oath Release and Expiation
- Reading type: latent/lexical
- Scene or process: A binding oath or fault is discharged by a prescribed act that covers and removes its claim.
- Active motifs: token act releasing an oath `ح ل ل:B005/m01`; expiation that erases wrongdoing `ك ف ر:B009/m01`; penalty following breach `ع ق ب:B007/m01`; right-hand obligation `ي م ن:B003/m02`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:19 `كَفَرُوا` (ك ف ر); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:18 `ٱلْمَيْمَنَةِ` (ي م ن)
- Synthesis: Release does not deny that a bond existed. A specified act answers the oath or fault, preventing its punitive consequence by satisfying the outstanding claim.

#### Subchannel E. Prayer Response and Amen
- Reading type: latent/lexical
- Scene or process: A supplication is voiced, answered, and affirmed with a formula requesting fulfillment.
- Active motifs: saying amen for response `ء م ن:B003/m01`; answering a caller `ه ا ء:B003/m01`; vocative call `ء ي ي:B008/m01`; gift offered in affection `ه د ي:B004/m01`
- Ayah anchors: 90:17 `ءَامَنُوا` (ء م ن); 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:10 `هَدَيْنَٰهُ` (ه د ي); related `هَٰذَا` at 90:1-2 (ه ا ء)
- Synthesis: The ritual exchange has a caller, an answer, and an affirming formula. The gift motif extends the same reciprocal movement from spoken request to tangible offering.

#### Subchannel F. Sacrifice and Nearness
- Reading type: latent/lexical
- Scene or process: An offering is selected, brought toward the sanctuary, and presented as an act of devotion.
- Active motifs: sanctuary offering `ه د ي:B005/m01`; devotional approach and sacrifice `ق ر ب:B005/m01`; offering reaching its appointed place `ح ل ل:B004/m03`; release from consecrated status `ح ل ل:B003/m03`
- Ayah anchors: 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:2 `حِلٌّ` (ح ل ل)
- Synthesis: Ritual nearness is a directed journey. The offering moves toward a protected place, arrives at its due location, and thereby completes the devotional act.

### 13. Measure, Capacity, and Deliberation
- Semantic invariant: Action depends on counting, delimiting, possessing power, enduring constraint, and choosing after reflection.
- Surface relation: direct; 90:5-7 joins supposition, power, singularity, and unseen accountability.
- Surprising reach: Measure also governs astronomical calculation, medium quality, coordinated horse footfall, adequacy, and expansive quantification under negation.

#### Subchannel A. Counting and Reckoning
- Reading type: mixed
- Scene or process: Units are counted and brought into an account that can be reviewed.
- Active motifs: counting and reckoning `ح س ب:B001/m01`; bounded amount and term `ق د ر:B001/m01`; single counted unit `ء ح د:B003/m01`; day as a countable span `ي و م:B001/m01`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:5 `يَقْدِرَ`, `أَحَدٌ` (ق د ر, ء ح د); 90:14 `يَوْمٍ` (ي و م)
- Synthesis: Counting creates accountability by turning acts and durations into bounded units. Measure fixes their limits so that reckoning can compare what was claimed with what occurred.

#### Subchannel B. Approximation, Proportion, and Fit
- Reading type: latent/lexical
- Scene or process: A thing is judged by how nearly it fills a measure, occupies a middle range, or fits its intended form.
- Active motifs: approximate amount or fullness `ق ر ب:B016/m01`; medium quality `ق ر ب:B016/m02`; proportionate fit `ق د ر:B006/m01`; distributed share `ق س م:B003/m01`
- Ayah anchors: 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:5 `يَقْدِرَ` (ق د ر); 90:1 `أُقْسِمُ` (ق س م)
- Synthesis: Approximation is not vagueness but measured nearness to a target. Fit, quality, fullness, and allotted share all compare an actual object with an implicit standard.

#### Subchannel C. Power, Ability, and Ownership
- Reading type: surface-primary
- Scene or process: A person possesses sufficient control to perform an act or hold property.
- Active motifs: effective power and possession `ق د ر:B003/m01`; ability to accomplish a task `ط ع م:B011/m01`; strength and enforceable right `ي م ن:B004/m01`; choice property `ر ق ب:B012/m01`
- Ayah anchors: 90:5 `يَقْدِرَ` (ق د ر); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Capacity joins agency to control over resources. The person can act because power, right, and property are available to be exercised.

#### Subchannel D. Constriction and Reduced Provision
- Reading type: latent/lexical
- Scene or process: Resources or room for action are narrowed to a small, difficult measure.
- Active motifs: constricted provision `ق د ر:B004/m01`; distress and tightness `ن ج د:B005/m01`; poverty and weakness `س ك ن:B006/m01`; hunger with exhaustion `س غ ب:B001/m01`
- Ayah anchors: 90:5 `يَقْدِرَ` (ق د ر); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:16 `مِسْكِينًا` (س ك ن); 90:14 `مَسْغَبَةٍ` (س غ ب)
- Synthesis: Constraint is the negative image of capacity. Provision shrinks, distress occupies the remaining space, and hunger makes the loss of practical options bodily.

#### Subchannel E. Planning, Opinion, and Deliberation
- Reading type: mixed
- Scene or process: A person moves from uncertain supposition through gathered experience and comparison toward a formed intention.
- Active motifs: uncertain supposition `ح س ب:B002/m01`; saying construed as supposition `ق و ل:B011/m01`; experience acquired through time `ن ج د:B010/m01`; reflective planning `ق د ر:B005/m01`; divided attention among alternatives `ق س م:B006/m01`; reasoned opinion `ر ء ي:B002/m01`; practical oversight `ح س ب:B006/m01`; inner unspoken thought `ق و ل:B012/m01`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:6 `يَقُولُ` (ق و ل); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:5 `يَقْدِرَ` (ق د ر); 90:1 `أُقْسِمُ` (ق س م); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: Deliberation moves from uncertainty toward commitment. Experience, perception, and inner speech supply possible courses, divided attention compares them, and planning converts judgment into a prepared intention.

#### Subchannel F. Sufficiency and Universal Scope
- Reading type: mixed
- Scene or process: A statement tests whether something is enough or whether any possible person falls within its scope.
- Active motifs: adequacy and sufficiency `ح س ب:B003/m01`; universal person under negation `ء ح د:B002/m01`; numerous instances `ء ي ي:B007/m01`; signification `ق و ل:B014/m01`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ`, `أَحَدٌ` (ح س ب, ء ح د); 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Sufficiency and universality set opposite boundaries: one asks whether the available amount reaches a threshold, while the other expands reference until no eligible person remains outside it.

### 14. Conflict, Peril, and Retribution
- Semantic invariant: Conflict exposes agents to danger, organized violence, hostility, restraint, and answering punishment.
- Surface relation: direct; 90:11 presents perilous incursion, 90:13 a bound neck, and 90:20 terminal confinement in fire.
- Surprising reach: The conflict field includes sword-and-stick duels, blackened livers as enmity, ceasefire, forced oaths, retaliation, and protected asylum.

#### Subchannel A. Perilous Incursion and Exposure
- Reading type: surface-primary
- Scene or process: A person enters a danger whose terrain and consequences may overwhelm the entrant.
- Active motifs: rash entry into danger `ق ح م:B001/m01`; great road peril `ق ح م:B002/m01`; casting oneself into destruction `ه ل ك:B002/m01`; deadly waste or chasm `ه ل ك:B006/m01`
- Ayah anchors: 90:11 `ٱقْتَحَمَ` (ق ح م); 90:6 `أَهْلَكْتُ` (ه ل ك)
- Synthesis: Incursion crosses the boundary between deliberation and exposure. Once entered, the dangerous route or chasm can no longer be treated as a distant possibility.

#### Subchannel B. Sword, Stick, and Close Combat
- Reading type: latent/lexical
- Scene or process: Opponents close distance and strike with swords, sticks, or a club-like implement.
- Active motifs: dueling with swords and sticks `ب ل د:B011/m01`; courage and aid in combat `ن ج د:B003/m01`; striking-stick or bat `ق و ل:B008/m01`; hard central grip `ك ب د:B004/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:6 `يَقُولُ` (ق و ل); 90:4 `كَبَدٍ` (ك ب د)
- Synthesis: The combat scene combines bodily courage, held implement, and sustained proximity. The grip mediates force from the fighter into sword, stick, or club.

#### Subchannel C. Hostility, Feud, and Truce
- Reading type: latent/lexical
- Scene or process: Enmity takes hold between groups and is then suspended by an agreed ceasefire.
- Active motifs: deep hostility figured as black livers `ك ب د:B007/m01`; feud or enmity `ن و ر:B007/m01`; negotiated truce `ق س م:B008/m01`; companion-group alignment `ص ح ب:B001/m02`
- Ayah anchors: 90:4 `كَبَدٍ` (ك ب د); 90:20 `نَارٌ` (ن و ر); 90:1 `أُقْسِمُ` (ق س م); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: Feud is a durable relation between aligned groups, not a single clash. Truce does not erase that relation but regulates it by suspending hostile action.

#### Subchannel D. Punishment, Retaliation, and Forced Restraint
- Reading type: mixed
- Scene or process: An offense is answered by punitive force, including detention, execution, or retaliatory payment.
- Active motifs: punishment after wrongdoing `ع ق ب:B007/m01`; retaliatory execution `ص ب ر:B012/m01`; forced detention for execution or oath `ص ب ر:B002/m01`; punishment becoming due `ح ل ل:B004/m02`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:17 `صَّبْرِ` (ص ب ر); 90:2 `حِلٌّ` (ح ل ل)
- Synthesis: Retribution follows an ordered sequence: offense establishes liability, force restrains the offender, and punishment is carried out as the answering consequence.

#### Subchannel E. Captive, Asylum, and Protected Passage
- Reading type: mixed
- Scene or process: A vulnerable entrant seeks protected status, while a captive awaits release from hostile control.
- Active motifs: asylum seeker under protection `ه د ي:B007/m01`; captive `ه د ي:B007/m02`; freeing a captive `ف ك ك:B002/m02`; grant of security `ء م ن:B001/m02`
- Ayah anchors: 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:13 `فَكُّ` (ف ك ك); 90:17 `ءَامَنُوا` (ء م ن)
- Synthesis: Protection changes the legal meaning of movement. The asylum seeker crosses into safety by covenant, while the captive crosses out of coercion through release.

### 15. Body Core, Landmarks, and Orientation
- Semantic invariant: The body is mapped through central organs, chest structures, jaws, limbs, sides, and extremities.
- Surface relation: direct; 90:4 names `كَبَد`, 90:8-9 eyes, tongue, and lips, and 90:13 the neck-person.
- Surprising reach: Body mapping reaches bow grips, necklace sites, vessel sockets, animal hocks, eye-like notches, and the human-facing side of paired objects.

#### Subchannel A. Liver, Lung, and Bodily Center
- Reading type: mixed
- Scene or process: Internal organs occupy a central torso whose swelling or pain becomes externally legible.
- Active motifs: liver and its illness `ك ب د:B001/m01`; lung and its complaint `ر ء ي:B009/m01`; central mass `ك ب د:B003/m01`; protruding middle `ك ب د:B006/m01`
- Ayah anchors: 90:4 `كَبَدٍ` (ك ب د); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: The body is organized around a vulnerable core. Liver, lung, center, and bodily protrusion connect hidden organs to felt or visible signs of strain.

#### Subchannel B. Chest, Clavicle, and Necklace Site
- Reading type: latent/lexical
- Scene or process: The upper torso is read as a hollow framed by breastbone and clavicles and marked by where a necklace rests.
- Active motifs: chest and throat hollow `ب ل د:B002/m01`; clavicles and upper breast `ت ر ب:B005/m01`; necklace position `ت ر ب:B005/m02`; chest-centered submission `ب ل د:B005/m02`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:16 `مَتْرَبَةٍ` (ت ر ب)
- Synthesis: Anatomy and ornament share one surface. The bones frame the chest, the necklace traces that frame, and the hand-to-chest gesture turns it into a site of embodied response.

#### Subchannel C. Jaw, Mouth, and Throat
- Reading type: mixed
- Scene or process: Jaws open around the mouth while throat pressure regulates speech, food, breath, or restraint.
- Active motifs: paired jaws `ف ك ك:B004/m01`; lips `ش ف ه:B001/m01`; throat seized in choking `ط ع م:B012/m01`; neck as bodily passage `ر ق ب:B004/m01`; head's resting place on the neck `س ك ن:B009/m02`; tongue as articulator `ل س ن:B001/m01`
- Ayah anchors: 90:13 `فَكُّ رَقَبَةٍ` (ف ك ك, ر ق ب); 90:9 `شَفَتَيْنِ`, `لِسَانًا` (ش ف ه, ل س ن); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:16 `مِسْكِينًا` (س ك ن)
- Synthesis: The mouth is a shared passage for language, nourishment, and breath, set below the head where it rests on the neck. Jaw opening enables those functions; constriction at the throat reverses them.

#### Subchannel D. Heel, Tendon, and Weak Hock
- Reading type: latent/lexical
- Scene or process: Tendons hold the rear foot and ankle under tension, while looseness produces an unstable gait.
- Active motifs: hard tendon or bowstring sinew `ع ق ب:B001/m01`; heel and rear foot `ع ق ب:B002/m01`; loose hock or ankle `ح ل ل:B014/m01`; dislocated or relaxed joint `ف ك ك:B005/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:2 `حِلٌّ` (ح ل ل); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: Stability depends on maintained tension. Tendon and heel carry the load, while loosened hock or separated joint converts support into weakness.

#### Subchannel E. Side, Flank, Fingertip, and Palm
- Reading type: latent/lexical
- Scene or process: The body is oriented by the side that faces the person, the flank at the waist, and the tactile extremity of hand and finger.
- Active motifs: human-facing side `ء ن س:B004/m01`; flank and waist `ق ر ب:B015/m01`; fingertip `ت ر ب:B006/m01`; human figure or fingertip in the palm `ء ن س:B005/m02`
- Ayah anchors: 90:4 `ٱلْإِنسَٰنَ` (ء ن س); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:16 `مَتْرَبَةٍ` (ت ر ب)
- Synthesis: These landmarks orient touch and proximity. Side and flank establish bodily direction, while palm and fingertip provide the fine point of contact with the surrounding world.

### 16. Appearance, Marking, and Ornament
- Semantic invariant: Bodies and objects become socially legible through proportion, color, trace, and adornment.
- Surface relation: indirect; the body parts of 90:8-9 and the visible-accountability frame of 90:7 provide the surface base.
- Surprising reach: Appearance includes an open brow, tawny animal color, skin disease, scars, sword straps, scabbards, crowns, and noble full siblings.

#### Subchannel A. Brow, Facial Beauty, and Wide Eyes
- Reading type: latent/lexical
- Scene or process: Facial openness, proportion, and eye shape produce a recognizable ideal of beauty.
- Active motifs: clear space between the brows `ب ل د:B003/m01`; distributed facial beauty `ق س م:B001/m01`; wide and beautiful eyes `ع ي ن:B016/m01`; pleasing mirror appearance `ر ء ي:B006/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:1 `أُقْسِمُ` (ق س م); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: Beauty is read through intervals and proportions: the clear brow frames the face, the eyes widen its expression, and the mirror makes the whole arrangement available for appraisal.

#### Subchannel B. Complexion, Tawny Redness, and Skin Change
- Reading type: latent/lexical
- Scene or process: Color in skin, hair, or hide identifies health, disease, and animal appearance.
- Active motifs: mixed white-red or dusty complexion `ح س ب:B009/m01`; tawny-red animal hue `ص ح ب:B008/m01`; skin mark `ب ل د:B006/m01`; pallor or disease resembling leprosy `ح س ب:B009/m02`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:1-2 `ٱلْبَلَدِ` (ب ل د)
- Synthesis: Color is diagnostic as well as decorative. Hue identifies the animal or person, while a changed patch can indicate disease or a lasting bodily event.

#### Subchannel C. Scar, Imprint, and Trace
- Reading type: latent/lexical
- Scene or process: Contact leaves a visible mark that preserves the history of pressure, passage, or injury.
- Active motifs: bodily mark `ب ل د:B006/m01`; facial sign `ر ء ي:B006/m02`; heel-track and trail `ع ق ب:B002/m02`; eye-like notch `ع ي ن:B009/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:7 `يَرَهُ` (ر ء ي); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: A trace converts past contact into present evidence. Scar, track, notch, and facial sign are all surfaces that retain an event after its cause has moved on.

#### Subchannel D. Necklace, Scabbard, and Crown
- Reading type: latent/lexical
- Scene or process: Worn and carried objects mark the body, protect weapons, and display rank.
- Active motifs: sword strap `ن ج د:B009/m01`; necklace resembling the sword-strap position `ن ج د:B009/m02`; necklace site on the chest `ت ر ب:B005/m02`; sword or knife scabbard `ق ر ب:B010/m01`; royal crown `ك ف ر:B015/m01`
- Ayah anchors: 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:19 `كَفَرُوا` (ك ف ر)
- Synthesis: Ornament and equipment share the body as their support. Necklace and baldric cross the chest, the scabbard encloses the weapon, and the crown makes authority visible at the head.

### 17. Animal Reproduction and Husbandry
- Semantic invariant: Domestic animals are managed through mating, birth, lactation, pasture, body condition, and trained behavior.
- Surface relation: indirect; the active senses are lexical extensions of roots appearing across 90:2-3, 90:7, 90:13-17.
- Surprising reach: The husbandry scene includes visible pregnancy, milk descending without birth, newborn goats, mating heat, fodder lodged in the throat, dung crust, weak hocks, and a camel waiting at water.

#### Subchannel A. Mating, Pregnancy, and Approaching Birth
- Reading type: latent/lexical
- Scene or process: An animal enters mating heat, conceives, and develops visible signs as delivery approaches.
- Active motifs: female animal seeking the male `ج ع ل:B009/m01`; pregnancy becoming visible `ر ء ي:B010/m01`; nearness of animal delivery `ق ر ب:B012/m01`; pre-birth loosening and emaciation `ف ك ك:B007/m01`
- Ayah anchors: 90:8 `نَجْعَل` (ج ع ل); 90:7 `يَرَهُ` (ر ء ي); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: Reproduction is tracked through observable transitions: desire initiates mating, pregnancy enlarges the body, and loosening signals that birth is near.

#### Subchannel B. Delivery and Newborn Livestock
- Reading type: latent/lexical
- Scene or process: A young goat, lamb, or similar animal is delivered, separated from the mother, and recognized as newborn stock.
- Active motifs: newborn goat or lamb `ح ل ل:B010/m01`; animal delivery `و ل د:B003/m02`; body opening around birth `ف ك ك:B007/m02`; postpartum uterine trouble `ر ح م:B004/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:3 `وَلَدَ` (و ل د); 90:13 `فَكُّ` (ف ك ك); 90:17 `مَرْحَمَةِ` (ر ح م)
- Synthesis: Delivery creates both a new dependent animal and a changed maternal body. Separation at birth is followed by care for the newborn and attention to postpartum complications.

#### Subchannel C. Udder, Duct, and Milk Descent
- Reading type: latent/lexical
- Scene or process: Milk moves through an udder or breast duct, sometimes descending with spring rather than immediate birth.
- Active motifs: milk outlet or duct `ح ل ل:B008/m02`; milk descending into the udder `ح ل ل:B009/m01`; milk taking flavor `ط ع م:B005/m02`; borrowed young used to induce milk `ل س ن:B007/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:9 `لِسَانًا` (ل س ن)
- Synthesis: Lactation is a managed flow. The duct supplies the passage, seasonal or induced descent fills the udder, and flavor signals the resulting milk's condition.

#### Subchannel D. Pasture, Fodder, and Fattening
- Reading type: latent/lexical
- Scene or process: Suitable pasture keeps animals in place, feeds them heavily, and brings them into fat condition.
- Active motifs: pasture fitting the herd `و ص ي:B004/m01`; sustaining pasture `س ك ن:B010/m01`; fodder lodged as animals feed `ل ب د:B006/m01`; animal fatness `ط ع م:B007/m01`
- Ayah anchors: 90:17 `تَوَاصَوْا` (و ص ي); 90:16 `مِسْكِينًا` (س ك ن); 90:6 `لُّبَدًا` (ل ب د); 90:14 `إِطْعَٰمٌ` (ط ع م)
- Synthesis: The scene links environment to body condition. Fit pasture reduces the need to move, concentrated feeding fills the animal, and fatness records successful provision.

#### Subchannel E. Camel Condition, Waiting, and Weak Hock
- Reading type: latent/lexical
- Scene or process: A handler reads a camel's tractability, waiting behavior, age, hind-leg weakness, and bodily contamination.
- Active motifs: docile camel `ت ر ب:B009/m01`; camel waiting back from water `ر ق ب:B009/m01`; weak hock `ح ل ل:B014/m01`; precocious animal age `ق ح م:B005/m01`; dung-and-urine crust `ل ب د:B005/m01`
- Ayah anchors: 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:13 `رَقَبَةٍ` (ر ق ب); 90:2 `حِلٌّ` (ح ل ل); 90:11 `ٱقْتَحَمَ` (ق ح م); 90:6 `لُّبَدًا` (ل ب د)
- Synthesis: Husbandry depends on close observation of behavior and body. Waiting at the trough, docility, age change, weak joints, and crusted hide each guide how the animal is handled.

### 18. Hunting, Tracking, and Animal Pursuit
- Semantic invariant: Pursuit joins concealment, target selection, predatory tools, and the reading of tracks.
- Surface relation: indirect; the lexical scene draws on seeing at 90:7-8, the difficult approach at 90:11-12, and the neck-release image at 90:13.
- Surprising reach: Hunting connects a concealed archer, a pointed comb or horn, a raptor, a banner shaped by visibility, and the spoor left at the rear.

#### Subchannel A. Concealed Hunter and Hunting Blind
- Reading type: latent/lexical
- Scene or process: A hunter approaches under cover, waits behind a screen, and uses a tool that yields prey.
- Active motifs: stalking under animal cover `د ر ي:B003/m01`; hunting blind `ر ق ب:B011/m01`; hunting bow that yields game `ط ع م:B006/m01`; patient waiting `ر ق ب:B001/m01`
- Ayah anchors: 90:12 `أَدْرَىٰكَ` (د ر ي); 90:13 `رَقَبَةٍ` (ر ق ب); 90:14 `إِطْعَٰمٌ` (ط ع م)
- Synthesis: The hunt depends on delayed visibility. Cover and blind conceal the hunter, waiting holds the moment, and the hunting implement converts concealment into capture.

#### Subchannel B. Targeting, Raid, and Visual Appraisal
- Reading type: latent/lexical
- Scene or process: A target is identified by its sign, approached deliberately, and appraised before attack.
- Active motifs: deliberate targeting or raid `د ر ي:B002/m01`; targeting a person's visible sign `ء ي ي:B002/m01`; eye's appraisal of scale `ق ح م:B007/m01`; sensory sight `ر ء ي:B001/m01`
- Ayah anchors: 90:12 `أَدْرَىٰكَ` (د ر ي); 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:11 `ٱقْتَحَمَ` (ق ح م); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: Pursuit begins before physical approach. The hunter fixes identity through a sign, estimates the target, and only then commits to movement.

#### Subchannel C. Raptor, Standard, and Predatory Reach
- Reading type: latent/lexical
- Scene or process: A raptor is trained or recognized as a hunting partner, while its elevated visibility also lends its form to a standard.
- Active motifs: hunting raptor `ع ق ب:B013/m01`; raptor-like banner `ع ق ب:B013/m02`; trained raptor that provides food `ط ع م:B006/m02`; raised visible standard `ر ء ي:B011/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: The raptor's height and striking reach support two connected roles: hunter and visible emblem. Both depend on a form recognized at distance.

#### Subchannel D. Heel, Track, and Pursuing Trace
- Reading type: latent/lexical
- Scene or process: A pursuer follows the rear trace left by a person, animal, or moving group.
- Active motifs: heel and following track `ع ق ب:B002/m02`; rear successor and dust trail `ر ق ب:B015/m02`; seeking news along a trace `ح س ب:B010/m01`; sensory sight `ر ء ي:B001/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:13 `رَقَبَةٍ` (ر ق ب); 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:7 `يَرَهُ` (ر ء ي)
- Synthesis: Tracking reads absence as evidence. Heel marks and trailing dust preserve direction, allowing the observer to reconstruct movement after the quarry has passed.

### 19. Plants, Fruit, and Cultivation
- Semantic invariant: Cultivation joins seed, rooted attachment, ripening, withering, and flowering fragrance.
- Surface relation: indirect; plant senses extend roots occurring at 90:13-20, especially release, feeding, counsel, consequence, covering, and fire/light.
- Surprising reach: The plant network includes graft acceptance, an eye-speck analogy, close-rooted growth, dwarf palms, tamarind-like sour fruit, fruit sheaths, seed covering, and camphor.

#### Subchannel A. Seed, Sapling, and Rooted Growth
- Reading type: latent/lexical
- Scene or process: Seed is covered in soil, a young plant emerges, and close roots establish it in place.
- Active motifs: seed covered by the cultivator `ك ف ر:B008/m01`; soil `ت ر ب:B001/m01`; sapling or plant `ت ر ب:B007/m01`; dwarf palm `ج ع ل:B006/m01`; close-rooted vegetation `و ص د:B004/m01`
- Ayah anchors: 90:19 `كَفَرُوا` (ك ف ر); 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:8 `نَجْعَل` (ج ع ل); 90:20 `مُّؤْصَدَةٌ` (و ص د)
- Synthesis: Cultivation begins in concealment. Seed is placed under soil, then the emerging plant establishes a compact root system that holds it to the ground.

#### Subchannel B. Grafting and Accepted Attachment
- Reading type: latent/lexical
- Scene or process: A branch from one tree is joined to another and succeeds only if the host accepts the connection.
- Active motifs: grafting a branch `ط ع م:B010/m01`; joining one thing to another `و ص ي:B001/m01`; close-rooted attachment `و ص د:B004/m01`; receptivity to reform `ط ع م:B008/m02`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:17 `تَوَاصَوْا` (و ص ي); 90:20 `مُّؤْصَدَةٌ` (و ص د)
- Synthesis: The graft is a precise model of successful relation: connection is made, the host receives it, and continuity is proven by new growth.

#### Subchannel C. Ripening Fruit and Protective Sheath
- Reading type: latent/lexical
- Scene or process: Fruit develops flavor while a sheath protects it until maturity.
- Active motifs: fruit ripening and acquiring flavor `ط ع م:B005/m01`; fruit or palm sheath `ك ف ر:B010/m01`; sour red-seeded fruit `ص ب ر:B009/m01`; fruiting tree `ج ع ل:B006/m02`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:19 `كَفَرُوا` (ك ف ر); 90:17 `صَّبْرِ` (ص ب ر); 90:8 `نَجْعَل` (ج ع ل)
- Synthesis: Maturation joins enclosure and sensory change. The sheath covers the developing fruit; ripeness is recognized when flavor and visible seed or color emerge.

#### Subchannel D. Yellowing, Withering, and Dry Stem
- Reading type: latent/lexical
- Scene or process: A plant passes from fruiting into yellow leaf, dry stem, and remaining trace.
- Active motifs: yellowing and drying plant `ع ق ب:B015/m01`; dry plant remainder `ع ق ب:B011/m03`; fruit sheath opening or drying `ك ف ر:B010/m01`; sour fruit nearing dry maturity `ص ب ر:B009/m02`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:19 `كَفَرُوا` (ك ف ر); 90:17 `صَّبْرِ` (ص ب ر)
- Synthesis: Withering is a temporal consequence visible in plant matter. Color fades, the stem hardens, and the dry remainder records the completed growth cycle.

#### Subchannel E. Flower, Fragrance, and Camphor
- Reading type: latent/lexical
- Scene or process: A tree flowers and releases a fragrance that is gathered or applied as perfume.
- Active motifs: tree blossom `ن و ر:B004/m01`; camphor perfume `ك ف ر:B011/m01`; camphor plant `ك ف ر:B011/m03`; perfumed coating `خ ل ق:B010/m01`; flowing spring `ع ي ن:B006/m01`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:19 `كَفَرُوا` (ك ف ر); 90:4 `خَلَقْنَا` (خ ل ق); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Flowering makes scent available; camphor and perfumed coating preserve and transfer it. The spring-source image adds a second mode of fragrance emerging from a hidden origin.

### 20. Water, Vessels, and Filtration
- Semantic invariant: Water is found, carried, leaked, surfaced, filtered, and retained through a set of natural and crafted containers.
- Surface relation: indirect; the lexical water scenes are anchored mainly by eye, nearness, dwelling, accumulated material, and creation roots.
- Surprising reach: Water appears as a spring, a leaking skin, algae on a surface, a beetle-filled pool, a strainer, a rock basin, and a night journey toward a watering place.

#### Subchannel A. Spring and Visible Source
- Reading type: latent/lexical
- Scene or process: Water emerges from a source and becomes visible as a flowing spring.
- Active motifs: flowing spring `ع ي ن:B006/m01`; spring associated with camphor `ك ف ر:B011/m02`; visible disclosure `ر ء ي:B012/m01`; nearby water `ق ر ب:B001/m02`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:19 `كَفَرُوا` (ك ف ر); 90:7 `يَرَهُ` (ر ء ي); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: A hidden source declares itself through flowing visibility. Nearness matters because the spring converts remote need into accessible water.

#### Subchannel B. Waterskin, Leak, and Casing
- Reading type: latent/lexical
- Scene or process: Water is carried in a skin whose thin point may leak and whose outer casing protects it.
- Active motifs: waterskin container `ق ر ب:B009/m01`; leaking aperture in skin `ع ي ن:B007/m01`; sewn casing around a waterskin `ل ب د:B004/m01`; hide retaining hair `ص ح ب:B006/m01`
- Ayah anchors: 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:6 `لُّبَدًا` (ل ب د); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: The vessel is an assembly of hide, seam, casing, and vulnerable aperture. Its purpose is defeated by leakage, so carrying water depends on maintaining the integrity of every layer.

#### Subchannel C. Water Surface, Algae, and Beetle Habitat
- Reading type: latent/lexical
- Scene or process: Standing water develops a surface growth and supports small creatures within it.
- Active motifs: algae covering water `ص ح ب:B007/m01`; water crowded with beetles `ج ع ل:B008/m01`; compacted surface layer `ل ب د:B001/m02`; still water or calm surface `س ك ن:B001/m02`
- Ayah anchors: 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:8 `نَجْعَل` (ج ع ل); 90:6 `لُّبَدًا` (ل ب د); 90:16 `مِسْكِينًا` (س ك ن)
- Synthesis: The water body becomes a layered habitat. Stillness permits algae to spread, compact surface matter forms, and beetles inhabit the resulting environment.

#### Subchannel D. Strainer, Vessel, and Residue
- Reading type: latent/lexical
- Scene or process: Liquid is poured through a strainer into a vessel, leaving sediment or residue behind.
- Active motifs: strainer and receiving vessel `ن ج د:B011/m01`; cooking or liquid vessel `ق د ر:B007/m01`; vessel brim and sides `ص ب ر:B004/m02`; physical sediment residue `ع ق ب:B011/m02`; thickened drink `ك ب د:B005/m01`
- Ayah anchors: 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:5 `يَقْدِرَ` (ق د ر); 90:17 `صَّبْرِ` (ص ب ر); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:4 `كَبَدٍ` (ك ب د)
- Synthesis: Filtration separates flow from remainder. The strainer directs usable liquid into the vessel, its brim marks fullness, and thickness or residue identifies what the filtering process retains.

#### Subchannel E. Rock Basin, Well, and Retained Rain
- Reading type: latent/lexical
- Scene or process: A natural or built depression collects rain and holds it against stone and earth.
- Active motifs: rain-holding rock hollow `خ ل ق:B011/m01`; recently dug well `خ ل ق:B011/m02`; old ground-level basin `ب ل د:B010/m02`; hard rock and gravel `ص ب ر:B005/m01`; projecting well stone `ع ق ب:B012/m02`
- Ayah anchors: 90:4 `خَلَقْنَا` (خ ل ق); 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:17 `صَّبْرِ` (ص ب ر); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب)
- Synthesis: Retention converts terrain into a vessel. Hollow, stone rim, and ground-level basin cooperate to keep rain from immediately escaping.

#### Subchannel F. Night Journey to Water
- Reading type: latent/lexical
- Scene or process: People and animals travel urgently toward a watering place and carry water away in skins.
- Active motifs: night approach to water `ق ر ب:B008/m01`; waterskin `ق ر ب:B009/m01`; portable travel gear `ح ل ل:B013/m01`; camel waiting at the crowded source `ر ق ب:B009/m02`
- Ayah anchors: 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:2 `حِلٌّ` (ح ل ل); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Water organizes movement before and after arrival. Urgent approach brings the herd to the source, waiting regulates access, and the filled skin extends the water's reach beyond the site.

### 21. Cooking, Taste, Medicine, and Surface Treatment
- Semantic invariant: Substances are transformed, tested, ingested, or applied through heat, taste, mouth, and bodily surface.
- Surface relation: indirect; the lexical processes extend the feeding root at 90:14, opening at 90:13, bodily form at 90:4, and fire at 90:20.
- Surprising reach: The material scene includes a pot-lifting cloth, stew residue, bitter aloe, medicine placed in a child's mouth, choking, kissing, tattoo smoke, lime paste, and sesame oil.

#### Subchannel A. Pot, Heat, and Cooked Stew
- Reading type: latent/lexical
- Scene or process: Food is cooked in a pot, removed from heat with a cloth, and leaves a thick residue.
- Active motifs: cooking pot and stew `ق د ر:B007/m01`; cloth used to lower a hot pot `ج ع ل:B007/m01`; pot residue `ع ق ب:B011/m02`; thickened drink or liquid `ك ب د:B005/m01`
- Ayah anchors: 90:5 `يَقْدِرَ` (ق د ر); 90:8 `نَجْعَل` (ج ع ل); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:4 `كَبَدٍ` (ك ب د)
- Synthesis: The cooking assembly has container, heat-handling tool, changing contents, and remainder. Thickness and residue record the transformation after the pot is removed from the fire.

#### Subchannel B. Taste, Flavor, and Practical Value
- Reading type: mixed
- Scene or process: A substance or person is tested by taste, flavor, or the capacity to yield useful value.
- Active motifs: tasting and eating `ط ع م:B001/m01`; recognizable flavor `ط ع م:B005/m03`; intelligence and practical value `ط ع م:B008/m01`; quality or excellence `ع ي ن:B014/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Taste becomes a model of discernment. Flavor identifies mature food, while "having taste" extends sensory discrimination into intelligence, worth, and capacity for reform.

#### Subchannel C. Child Dosing and Bitter Medicine
- Reading type: latent/lexical
- Scene or process: A caregiver opens a child's mouth and places a measured medicinal substance inside.
- Active motifs: child patient `ف ك ك:B009/m01`; medicine placed in the mouth `ف ك ك:B009/m02`; bitter aloe medicine `ص ب ر:B008/m01`; bounded quantity `ق د ر:B001/m01`
- Ayah anchors: 90:13 `فَكُّ` (ف ك ك); 90:17 `صَّبْرِ` (ص ب ر); 90:5 `يَقْدِرَ` (ق د ر)
- Synthesis: Treatment joins caregiver, patient, dose, and entry route. Bitterness explains resistance, while measured mouth delivery ensures the medicine reaches the child.

#### Subchannel D. Throat Seizure and Choking
- Reading type: latent/lexical
- Scene or process: An assailant seizes the throat and compresses the breathing passage between neck and jaws.
- Active motifs: throat as the seized point `ط ع م:B012/m01`; forceful compression `ط ع م:B012/m02`; paired jaws `ف ك ك:B004/m01`; neck as bodily passage `ر ق ب:B004/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:13 `فَكُّ رَقَبَةٍ` (ف ك ك, ر ق ب)
- Synthesis: Choking is a localized coercive action. The grip fixes on the throat, compression closes the passage, and the surrounding neck and jaw anatomy define the vulnerable point.

#### Subchannel E. Mouth-to-Mouth Contact
- Reading type: latent/lexical
- Scene or process: Two mouths meet in reciprocal contact or a kiss.
- Active motifs: mouth-to-mouth insertion or kiss `ط ع م:B013/m01`; lips as contact surface `ش ف ه:B001/m01`; paired jaws `ف ك ك:B004/m01`
- Ayah anchors: 90:14 `إِطْعَٰمٌ` (ط ع م); 90:9 `شَفَتَيْنِ` (ش ف ه); 90:13 `فَكُّ` (ف ك ك)
- Synthesis: The interaction is defined by reciprocal oral contact. Lips supply the exposed surface, the paired jaws frame each mouth, and the contact itself distinguishes the scene from speech or forced throat pressure.

#### Subchannel F. Kohl, Tattoo, and Imprinted Skin
- Reading type: latent/lexical
- Scene or process: Smoke or pigment is applied to a punctured or marked surface to create kohl or a lasting tattoo.
- Active motifs: tattoo smoke or kohl pigment `ن و ر:B008/m01`; bodily mark `ب ل د:B006/m01`; eye-like puncture or notch `ع ي ن:B009/m01`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Pigment enters through a deliberately altered surface. Puncture receives the material, smoke or kohl fixes color, and the resulting mark persists as a visible trace.

#### Subchannel G. Lime, Oil, and Perfumed Coating
- Reading type: latent/lexical
- Scene or process: A prepared substance is spread over skin or another surface to remove hair, soften, or perfume it.
- Active motifs: applied lime or depilatory paste `ن و ر:B009/m01`; sesame oil `ح ل ل:B015/m01`; perfumed coating `خ ل ق:B010/m01`; smooth prepared surface `خ ل ق:B008/m01`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:2 `حِلٌّ` (ح ل ل); 90:4 `خَلَقْنَا` (خ ل ق)
- Synthesis: These treatments act by spreading a material film. Oil softens, lime strips, perfume scents, and polishing prepares the surface to receive the application evenly.

### 22. Textiles, Hides, and Furnishing
- Semantic invariant: Fibers and skins are prepared, layered, worn, cased, or arranged to furnish bodies and dwellings.
- Surface relation: indirect; the lexical scene grows from compacted abundance at 90:6, speech-organ roots at 90:9, and division at 90:1.
- Surprising reach: Textile work includes felt, patched cloth, hair-retaining hide, a girl's undergarment, worn fabric, prepared palm fiber, first folds, cushions, curtains, and a food mat.

#### Subchannel A. Felt, Wool, and Hair-Retaining Hide
- Reading type: latent/lexical
- Scene or process: Hair or wool is retained, compacted, and worked into felt, patches, or a protected hide.
- Active motifs: felted wool and patched material `ل ب د:B001/m01`; hide retaining hair or fleece `ص ح ب:B006/m01`; compacting layers `ل ب د:B001/m02`; animal hair and wool contrast `ل ب د:B007/m02`
- Ayah anchors: 90:6 `لُّبَدًا` (ل ب د); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: The process begins with fiber still attached to hide or gathered loose, then uses pressure and layering to produce a dense, durable material.

#### Subchannel B. Garment, Undergarment, and Worn Cloth
- Reading type: latent/lexical
- Scene or process: Cloth is assembled into layered clothing, worn next to the body, and eventually loses its nap through use.
- Active motifs: garment ensemble `ح ل ل:B007/m01`; girl's undergarment `ء ص د:B003/m01`; cloth covering armor or a weapon `ك ف ر:B001/m01`; worn cloth stripped of nap `خ ل ق:B009/m01`; first fold of cloth `ق س م:B007/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:19 `كَفَرُوا` (ك ف ر); 90:4 `خَلَقْنَا` (خ ل ق); 90:1 `أُقْسِمُ` (ق س م); no independent surface occurrence for ء ص د
- Synthesis: Folding and layering turn cloth into clothing or a protective covering. Proximity to the body distinguishes the undergarment, cloth can cover carried armor, and wear records continued use over time.

#### Subchannel C. Fiber Preparation and Twisting
- Reading type: latent/lexical
- Scene or process: Palm fiber is combed or stripped, divided into strands, and prepared for twisting.
- Active motifs: preparing fiber into strands `ل س ن:B009/m01`; tongue-shaped narrow strand `ل س ن:B004/m01`; compacted fiber `ل ب د:B001/m02`; comb or dressing tool `د ر ي:B004/m02`
- Ayah anchors: 90:9 `لِسَانًا` (ل س ن); 90:6 `لُّبَدًا` (ل ب د); 90:12 `أَدْرَىٰكَ` (د ر ي)
- Synthesis: Fiber work changes an irregular mass into aligned, narrow elements. Combing and division prepare strands whose tongue-like shape permits twisting into cord.

#### Subchannel D. Cushion, Curtain, and Food Mat
- Reading type: latent/lexical
- Scene or process: A dwelling is furnished with cushions, hangings, and a broad layer placed beneath food.
- Active motifs: small cushion `ح س ب:B008/m01`; furnishing a house with textiles `ن ج د:B008/m01`; food mat or broad wafer `ص ب ر:B011/m01`; felt floor covering `ل ب د:B001/m03`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:17 `صَّبْرِ` (ص ب ر); 90:6 `لُّبَدًا` (ل ب د)
- Synthesis: Furnishing converts prepared textile into an inhabited interior. Floor layer, cushion, hanging, and food mat organize rest, privacy, and eating within the home.

### 23. Light, Weather, and the Sky
- Semantic invariant: Celestial and atmospheric phenomena make direction, time, heat, water, and exposure visible.
- Surface relation: direct; 90:20 names fire, 90:10 presents visible routes, and 90:14 names a severe day of hunger.
- Surprising reach: The sky includes a road beacon, lunar mansion, round star cluster, noon heat, persistent rain, stacked white cloud, rainless cloud, winter cold, and drought-driven migration.

#### Subchannel A. Light, Fire, and Brand
- Reading type: surface-primary
- Scene or process: Fire emits light, provides a visible focus, and can leave a brand on an animal.
- Active motifs: illumination `ن و ر:B001/m01`; burning fire `ن و ر:B002/m01`; fire-brand mark `ن و ر:B002/m02`; hearth-like solace `س ك ن:B004/m02`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:16 `مِسْكِينًا` (س ك ن)
- Synthesis: Fire joins visibility and contact. At a distance it illuminates and comforts; applied to the body it becomes a lasting identifying brand.

#### Subchannel B. Beacon, Boundary Marker, and Tower
- Reading type: latent/lexical
- Scene or process: A high visible marker defines land and guides travelers.
- Active motifs: road beacon or minaret `ن و ر:B005/m01`; elevated clear route `ن ج د:B001/m01`; evident guide `ن ج د:B002/m01`; raised lookout `ر ق ب:B003/m01`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Elevation and light cooperate to make a marker legible. The beacon both locates a boundary and supplies orientation along the route.

#### Subchannel C. Sun Disk, Noon Heat, and Daylight
- Reading type: latent/lexical
- Scene or process: The sun's visible disk governs a hot daytime interval.
- Active motifs: solar disk `ع ي ن:B008/m01`; noon heat `ق س م:B002/m01`; daylight span `ي و م:B001/m01`; central sun position `ك ب د:B003/m02`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:1 `أُقْسِمُ` (ق س م); 90:14 `يَوْمٍ` (ي و م); 90:4 `كَبَدٍ` (ك ب د)
- Synthesis: Disk, central position, heat, and day form one solar scene. The sun's location supplies both the visible measure of time and the felt intensity of noon.

#### Subchannel D. Lunar Mansion and Round Star Cluster
- Reading type: latent/lexical
- Scene or process: Celestial objects occupy named stations and are counted or recognized by shape.
- Active motifs: lunar mansion and sky void `ب ل د:B004/m01`; round star cluster `ف ك ك:B008/m01`; astronomical reckoning `ح س ب:B001/m02`; opposing star in rising and setting `ر ق ب:B007/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:13 `فَكُّ`, `رَقَبَةٍ` (ف ك ك, ر ق ب); 90:5, 90:7 `أَيَحْسَبُ` (ح س ب)
- Synthesis: Astronomy organizes the sky through station, opposition, number, and visible shape. A void becomes a mansion because recurring celestial positions make it identifiable.

#### Subchannel E. Rain, Layered Cloud, and Catchment
- Reading type: latent/lexical
- Scene or process: Cloud gathers in layers, releases persistent rain, and fills a stone catchment.
- Active motifs: persistent rain or rain-cloud `ع ي ن:B010/m01`; layered white cloud `ص ب ر:B010/m01`; rain-holding rock hollow `خ ل ق:B011/m01`; stilling of rain or wind `س ك ن:B001/m03`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:17 `صَّبْرِ` (ص ب ر); 90:4 `خَلَقْنَا` (خ ل ق); 90:16 `مِسْكِينًا` (س ك ن)
- Synthesis: The atmospheric process has accumulation, release, reception, and cessation. Stacked cloud supplies rain, the hollow retains it, and stillness marks the end of the weather event.

#### Subchannel F. Drought, Migration, and Winter Cold
- Reading type: mixed
- Scene or process: Failed rain and severe temperature expose people and animals, forcing movement toward relief.
- Active motifs: rainless land or year `ه ل ك:B005/m01`; drought driving nomads to settled land `ق ح م:B003/m01`; severe winter cold `ص ب ر:B007/m01`; famine hunger `س غ ب:B001/m01`
- Ayah anchors: 90:6 `أَهْلَكْتُ` (ه ل ك); 90:11 `ٱقْتَحَمَ` (ق ح م); 90:17 `صَّبْرِ` (ص ب ر); 90:14 `مَسْغَبَةٍ` (س غ ب)
- Synthesis: Climate becomes social pressure. Drought removes pasture and food, cold increases exposure, and migration carries affected people from open land toward settled provision.

#### Subchannel G. Celestial Cover and Darkness
- Reading type: latent/lexical
- Scene or process: Cloud, night, or sunset spreads across the sky and hides a previously visible light.
- Active motifs: cloud or celestial covering `ك ف ر:B001/m02`; dark night or sunset as enveloping cover `ك ف ر:B002/m01`; layered cloud `ص ب ر:B010/m01`; solar disk `ع ي ن:B008/m01`
- Ayah anchors: 90:19 `كَفَرُوا` (ك ف ر); 90:17 `صَّبْرِ` (ص ب ر); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: Concealment is an atmospheric process: cloud accumulates, darkness or sunset spreads, and the solar or stellar light disappears beneath the covering layer.

### 24. Time, Recurrence, and Consequence
- Semantic invariant: Events are situated in spans, awaited, repeated, succeeded, and known by what remains after them.
- Surface relation: direct; 90:14 names a day, 90:17 marks a subsequent state, and 90:18-20 present final group outcomes.
- Surprising reach: Temporal order reaches Sunday, waiting in place, repeated prayer or pasture, alternating successors, pot residue, lingering illness, and a bad overnight state.

#### Subchannel A. Day, Duration, and Event
- Reading type: surface-primary
- Scene or process: A bounded day can expand into an indefinite duration or stand for a severe event.
- Active motifs: daylight unit `ي و م:B001/m01`; temporal duration `ي و م:B002/m01`; event or calamity `ي و م:B003/m01`; occurrence in time `ك و ن:B001/m01`
- Ayah anchors: 90:14 `يَوْمٍ` (ي و م); 90:17 `كَانَ` (ك و ن)
- Synthesis: "Day" supplies a temporal container whose scale changes with use. It can mark ordinary daylight, an extended span, or the event that defines the span.

#### Subchannel B. First, Sunday, and Calendar Order
- Reading type: latent/lexical
- Scene or process: A named day occupies the first position in an ordered weekly sequence.
- Active motifs: first or Sunday `ء ح د:B004/m01`; single day unit `ي و م:B001/m01`; counted one `ء ح د:B003/m01`; solar day `ع ي ن:B008/m02`
- Ayah anchors: 90:5, 90:7 `أَحَدٌ` (ء ح د); 90:14 `يَوْمٍ` (ي و م); 90:8 `عَيْنَيْنِ` (ع ي ن)
- Synthesis: The calendar scene combines ordinal position, counted unity, and solar duration. Sunday is both a name and the first member of a repeating series.

#### Subchannel C. Waiting and Imminence
- Reading type: mixed
- Scene or process: A watcher pauses while an expected arrival or event draws near.
- Active motifs: waiting and delay `ء ي ي:B001/m01`; watchful expectation `ر ق ب:B001/m01`; imminent time `ق ر ب:B002/m01`; delayed movement `ي ت م:B004/m01`
- Ayah anchors: 90:19 `ءَايَٰتِنَا` (ء ي ي); 90:13 `رَقَبَةٍ` (ر ق ب); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:15 `يَتِيمًا` (ي ت م)
- Synthesis: Waiting measures the interval between present lack and expected arrival. Imminence shortens that interval, while delay prolongs it despite the object's nearness.

#### Subchannel D. Succession, Repetition, and Connected Cycles
- Reading type: latent/lexical
- Scene or process: One action or occupant follows another, and the sequence returns in repeated cycles.
- Active motifs: succession and alternation `ع ق ب:B005/m01`; repeated action `ع ق ب:B009/m01`; joining night to day `و ص ي:B001/m02`; successor at the rear `ر ق ب:B015/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:17 `تَوَاصَوْا` (و ص ي); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Continuity can be linear or cyclical. A successor fills the previous position, while repeated work, prayer, pasture, or day-night connection makes return part of the order.

#### Subchannel E. Ending, Aftereffect, and Remaining Trace
- Reading type: mixed
- Scene or process: An action reaches its end and leaves a result, residue, illness, or condition behind.
- Active motifs: ending and consequence `ع ق ب:B006/m01`; residue and aftereffect `ع ق ب:B011/m01`; destruction or disappearance `ه ل ك:B001/m01`; bad resulting state `ك و ن:B006/m01`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:6 `أَهْلَكْتُ` (ه ل ك); 90:17 `كَانَ` (ك و ن)
- Synthesis: Outcome is read through what remains after the initiating act is over. Residue, illness, bad state, or disappearance gives consequence a concrete temporal signature.

### 25. Unity, Individuality, and Presence
- Semantic invariant: Persons and things are distinguished as one, any, solitary, present, or self-identical.
- Surface relation: direct; 90:4 names humanity, 90:5 and 90:7 use `أَحَد`, and 90:17-19 sort persons into present communities.
- Surprising reach: Identity reaches unique pearls and poems, an image in the pupil, the essence of an object, a confidant as "one's own person," and universal reference under negation.

#### Subchannel A. Absolute Unity
- Reading type: surface-primary
- Scene or process: A referent is asserted as one without division or peer.
- Active motifs: unity and singular oneness `ء ح د:B001/m01`; offspring as one member `و ل د:B001/m01`; selfsame essence `ع ي ن:B013/m01`; complete visible form `خ ل ق:B003/m01`
- Ayah anchors: 90:5, 90:7 `أَحَدٌ` (ء ح د); 90:3 `وَلَدَ` (و ل د); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:4 `خَلَقْنَا` (خ ل ق)
- Synthesis: Unity identifies a whole as itself. Formation supplies coherence, essence secures identity, and numerical one excludes division within the named referent.

#### Subchannel B. Anyone Under Negation
- Reading type: surface-primary
- Scene or process: Negation expands from one possible person to every person who could occupy the role.
- Active motifs: universal person in negative scope `ء ح د:B002/m01`; no human present `ء ن س:B001/m02`; no present eye or household member `ع ي ن:B017/m02`; exhaustive idiom "in every case" `ه ل ك:B008/m01`
- Ayah anchors: 90:5, 90:7 `أَحَدٌ` (ء ح د); 90:4 `ٱلْإِنسَٰنَ` (ء ن س); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:6 `أَهْلَكْتُ` (ه ل ك)
- Synthesis: The grammatical singular becomes semantically exhaustive. By denying even one eligible witness, the expression denies the entire class.

#### Subchannel C. Solitude and Unique Object
- Reading type: latent/lexical
- Scene or process: A person or object stands apart from companions or lacks any comparable peer.
- Active motifs: acting or arriving alone `ء ح د:B005/m01`; unique pearl, poem, or isolated thing `ي ت م:B002/m01`; remote or cut-off place `ك ف ر:B012/m01`; remaining without spouse `ي ت م:B005/m01`
- Ayah anchors: 90:5, 90:7 `أَحَدٌ` (ء ح د); 90:15 `يَتِيمًا` (ي ت م); 90:19 `كَفَرُوا` (ك ف ر)
- Synthesis: Solitude can be deprivation or distinction. The same separation that leaves a person without relation can make an object rare because no equal stands beside it.

#### Subchannel D. Human Presence, Self, and Possessor
- Reading type: mixed
- Scene or process: A human appears as a present self who possesses attributes, relations, or companions.
- Active motifs: human presence opposed to wildness or spirit `ء ن س:B001/m01`; one's own self or intimate `ء ن س:B006/m01`; essence of the thing `ع ي ن:B013/m01`; possessor characterized by relation `ذ و و:B001/m01`; present people or household `ع ي ن:B017/m01`
- Ayah anchors: 90:4 `ٱلْإِنسَٰنَ` (ء ن س); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:14 `ذِي`, 90:15-16 `ذَا` (ذ و و)
- Synthesis: Presence joins ontology to social grammar. The self is identifiable as an essence, appears among people, and is further specified by what or whom it possesses.

### 26. Direction, Regional Affiliation, and Portent
- Semantic invariant: Orientation assigns sides, routes, regions, and moral or auspicious value.
- Surface relation: direct; 90:10 gives two directed roads, while 90:18-19 contrast right and left groupings.
- Surprising reach: Direction reaches Yemen and Syria, Ghassan affiliation, vanguard and heel, burial on the right side, blessing, ill omen, and regional rulership.

#### Subchannel A. Right and Left Orientation
- Reading type: surface-primary
- Scene or process: A person or group is assigned to the right or left side of an oriented field.
- Active motifs: right hand and right side `ي م ن:B002/m01`; left side `ش ء م:B001/m01`; human-facing side `ء ن س:B004/m01`; directional route `ه د ي:B002/m01`
- Ayah anchors: 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:19 `ٱلْمَشْـَٔمَةِ` (ش ء م); 90:4 `ٱلْإِنسَٰنَ` (ء ن س); 90:10 `هَدَيْنَٰهُ` (ه د ي)
- Synthesis: Right and left are relational positions rather than isolated labels. A facing body and a chosen route establish the frame in which each side acquires meaning.

#### Subchannel B. Blessing and Ill Omen
- Reading type: mixed
- Scene or process: Directional sides become signs of favorable or harmful outcome.
- Active motifs: blessing and good fortune `ي م ن:B001/m01`; ill omen `ش ء م:B003/m01`; visible sign `ء ي ي:B003/m01`; consequence `ع ق ب:B006/m01`
- Ayah anchors: 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:19 `ٱلْمَشْـَٔمَةِ`, `ءَايَٰتِنَا` (ش ء م, ء ي ي); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب)
- Synthesis: Portent reads orientation prospectively. A side or sign is interpreted as announcing the kind of consequence toward which the person is moving.

#### Subchannel C. Yemen, Syria, and Ghassan Affiliation
- Reading type: latent/lexical
- Scene or process: A person or group is identified by regional direction, country, or tribal affiliation.
- Active motifs: Yemen and affiliation to it `ي م ن:B005/m01`; Syria and movement toward it `ش ء م:B002/m01`; Ghassan clan name `ص ب ر:B016/m01`; Himyarite chief or ruler `ق و ل:B004/m01`
- Ayah anchors: 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:19 `ٱلْمَشْـَٔمَةِ` (ش ء م); 90:17 `صَّبْرِ` (ص ب ر); 90:6 `يَقُولُ` (ق و ل)
- Synthesis: Direction becomes social identity when regions supply names for people, clans, and offices. Yemen, Syria, Ghassan, and the Himyarite title locate affiliation within a geographic field.

#### Subchannel D. Vanguard, Rear, and Right-Side Burial
- Reading type: latent/lexical
- Scene or process: A moving body is oriented from leading front to following heel, and a dead body is finally laid on its right.
- Active motifs: vanguard or front point `ه د ي:B003/m01`; heel and rear `ع ق ب:B002/m01`; death laid on the right side `ي م ن:B007/m01`; burial soil `ت ر ب:B001/m02`
- Ayah anchors: 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:18 `ٱلْمَيْمَنَةِ` (ي م ن); 90:16 `مَتْرَبَةٍ` (ت ر ب)
- Synthesis: Orientation persists across movement and death. The front leads, the heel follows, and burial fixes the body's final side against the soil.

### 27. Governance, Worth, and Public Standing
- Semantic invariant: Communities distinguish leaders, administrators, honored lineages, and valued persons or property.
- Surface relation: indirect; the accountability claims of 90:5-7 and group designations of 90:18-19 provide the social frame.
- Surprising reach: Standing includes a steadfast chief, royal intimates, a Himyarite title, inherited honor, full siblings, municipal supervision, best-quality goods, and principal capital.

#### Subchannel A. Chief, Courtier, and Royal Intimate
- Reading type: latent/lexical
- Scene or process: A ruler or chief exercises standing through trusted people admitted near the seat of authority.
- Active motifs: steadfast chief `ح ل ل:B012/m01`; Himyarite chief or ruler `ق و ل:B004/m01`; favored courtier `ق ر ب:B004/m01`; crowned ruler `ك ف ر:B015/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:6 `يَقُولُ` (ق و ل); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:19 `كَفَرُوا` (ك ف ر)
- Synthesis: Rank is organized by controlled nearness. The chief occupies the center, courtiers gain privileged access, and title or crown renders the hierarchy publicly visible.

#### Subchannel B. Lineage, Honor, and Noble Siblings
- Reading type: latent/lexical
- Scene or process: A person's standing is inherited and recognized through ancestors, deeds, and full sibling lineage.
- Active motifs: ancestral honor and memorable deeds `ح س ب:B004/m01`; nobles of the community `ع ي ن:B015/m01`; collateral inherited distinction `ر ق ب:B013/m01`; surviving descendants `ع ق ب:B004/m01`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:8 `عَيْنَيْنِ` (ع ي ن); 90:13 `رَقَبَةٍ` (ر ق ب); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب)
- Synthesis: Public honor is a temporal social asset. Ancestors establish it, siblings define its line, and descendants or collateral heirs carry it onward.

#### Subchannel C. Administration, Supervision, and Objection
- Reading type: latent/lexical
- Scene or process: An official inspects conduct, manages public affairs, and answers challenges to a judgment.
- Active motifs: practical administration and moral oversight `ح س ب:B006/m01`; authoritative ruling `ق و ل:B010/m01`; reconsideration and objection `ع ق ب:B008/m01`; watching officer `ر ق ب:B002/m02`
- Ayah anchors: 90:5, 90:7 `أَيَحْسَبُ` (ح س ب); 90:6 `يَقُولُ` (ق و ل); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:13 `رَقَبَةٍ` (ر ق ب)
- Synthesis: Governance is a cycle of inspection, decision, and reconsideration. Supervision gathers the matter, ruling acts on it, and objection tests whether the decision will stand.

#### Subchannel D. Excellence, Principal, and Medium Quality
- Reading type: latent/lexical
- Scene or process: Goods or persons are ranked as choice, principal, or intermediate in quality.
- Active motifs: best or choice item `ع ي ن:B014/m01`; choice property `ر ق ب:B012/m01`; medium quality and price `ق ر ب:B016/m02`; accumulated property `م و ل:B001/m01`; social rank or standing `ك و ن:B002/m02`
- Ayah anchors: 90:8 `عَيْنَيْنِ` (ع ي ن); 90:13 `رَقَبَةٍ` (ر ق ب); 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:6 `مَالًا` (م و ل); 90:17 `كَانَ` (ك و ن)
- Synthesis: Valuation separates the best item from ordinary property, distinguishes the principal asset from an approximate middle quality, and extends assessed worth into public standing.

### 28. Motion, Transport, and Gait
- Semantic invariant: Movement is controlled through pace, support, equipment, relocation, and the body's relation to the ground.
- Surface relation: indirect; the routes and ascent of 90:10-12 supply the surface movement frame.
- Surprising reach: Motion includes a horse's coordinated footfall, muzzle-prompted run, supported swaying, coquettish gait, camel travel for knowledge, dislodging an encampment, and persistent adhesion.

#### Subchannel A. Horse Pace and Coordinated Footfall
- Reading type: latent/lexical
- Scene or process: A rider prompts a horse into a measured gait whose hind and forefeet coordinate.
- Active motifs: paced horse run `ق ر ب:B014/m01`; muzzle area used to cue running `ط ع م:B009/m01`; coordinated foot placement `ق د ر:B006/m02`; favored prepared mount `ق ر ب:B013/m01`
- Ayah anchors: 90:15 `مَقْرَبَةٍ` (ق ر ب); 90:14 `إِطْعَٰمٌ` (ط ع م); 90:5 `يَقْدِرَ` (ق د ر)
- Synthesis: Training regulates speed through bodily cues and repeated placement. The result is neither uncontrolled flight nor stillness but a measured, usable pace.

#### Subchannel B. Supported Sway and Composed Bearing
- Reading type: latent/lexical
- Scene or process: A weak or stylized walker sways, leans on companions, and may recover a calm bearing.
- Active motifs: supported swaying walk `ه د ي:B008/m01`; broken or coquettish sway `ه ل ك:B003/m01`; calm, unhurried bearing `ه د ي:B010/m01`; companion support `ص ح ب:B004/m01`
- Ayah anchors: 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:6 `أَهْلَكْتُ` (ه ل ك); 90:18-19 `أَصْحَٰبُ` (ص ح ب)
- Synthesis: Gait reveals both condition and social support. Sway may signal weakness or display; leaning companions stabilize it, and composed bearing restores directional control.

#### Subchannel C. Dislodging, Relocation, and Adherence
- Reading type: latent/lexical
- Scene or process: A person, herd, or object is moved from a place, while another remains attached and refuses displacement.
- Active motifs: dislodging people or camels `ح ل ل:B011/m01`; separation from attachment `ف ك ك:B003/m01`; continued persistence `ف ك ك:B003/m02`; staying and clinging `ل ب د:B003/m01`; settled residence `ب ل د:B009/m01`
- Ayah anchors: 90:2 `حِلٌّ` (ح ل ل); 90:13 `فَكُّ` (ف ك ك); 90:6 `لُّبَدًا` (ل ب د); 90:1-2 `ٱلْبَلَدِ` (ب ل د)
- Synthesis: Relocation is understood against resistance to movement. Dislodging breaks place-attachment, while clinging and residence preserve it.

#### Subchannel D. Camel Travel and Portable Equipment
- Reading type: latent/lexical
- Scene or process: Camels carry people and gear across distance toward a sought destination.
- Active motifs: striking camel livers in travel `ك ب د:B008/m01`; portable encampment equipment `ح ل ل:B013/m01`; effective progress on an errand `ن ج د:B004/m01`; direction and travel manner `ه د ي:B002/m01`
- Ayah anchors: 90:4 `كَبَدٍ` (ك ب د); 90:2 `حِلٌّ` (ح ل ل); 90:10 `ٱلنَّجْدَيْنِ`, `هَدَيْنَٰهُ` (ن ج د, ه د ي)
- Synthesis: Long movement depends on animal power, portable equipment, and maintained direction. The journey is measured by purposeful progress rather than mere displacement.

### 29. Compliance, Hesitation, and Loss of Agency
- Semantic invariant: Agency can be yielded willingly, weakened by dullness, suspended by confusion, or withdrawn through skittish avoidance.
- Surface relation: direct; 90:16-17 contrast abasement with settled belief and action, while 90:18-19 assign persons to opposed group outcomes.
- Surprising reach: The channel reaches trained animals, bowed posture, circling bewilderment, delayed charity, loose judgment, chastity figured as skittishness, and heavy weak movement.

#### Subchannel A. Docility, Training, and Obedience
- Reading type: latent/lexical
- Scene or process: A previously difficult person or animal yields to guidance and follows another's direction.
- Active motifs: submission after difficulty `ص ح ب:B003/m01`; docile camel `ت ر ب:B009/m01`; bowed compliance `ك ف ر:B014/m01`; directed conduct `ه د ي:B002/m01`
- Ayah anchors: 90:18-19 `أَصْحَٰبُ` (ص ح ب); 90:16 `مَتْرَبَةٍ` (ت ر ب); 90:19 `كَفَرُوا` (ك ف ر); 90:10 `هَدَيْنَٰهُ` (ه د ي)
- Synthesis: Training converts resistance into coordinated following. The body lowers or yields, and guidance becomes effective because the subject now accepts direction.

#### Subchannel B. Bewilderment and Abased Submission
- Reading type: mixed
- Scene or process: Distress removes orientation, causing a person to circle, lower the body, and submit.
- Active motifs: confusion with hand to chest `ب ل د:B005/m01`; circling in the wilderness `ه ل ك:B010/m01`; poverty and abasement `س ك ن:B006/m01`; submissive state `ك و ن:B004/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:6 `أَهْلَكْتُ` (ه ل ك); 90:16 `مِسْكِينًا` (س ك ن); 90:17 `كَانَ` (ك و ن)
- Synthesis: Loss of direction becomes loss of agency. Circling cannot produce progress, distress lowers posture, and submission replaces chosen movement.

#### Subchannel C. Dullness, Lag, and Delayed Action
- Reading type: latent/lexical
- Scene or process: Weak judgment or heavy motion prevents timely progress and delays the good expected from a person.
- Active motifs: dullness and lag `ب ل د:B007/m01`; slow weak person `ه د ي:B009/m01`; loose judgment `ف ك ك:B006/m01`; delayed progress `ي ت م:B004/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:10 `هَدَيْنَٰهُ` (ه د ي); 90:13 `فَكُّ` (ف ك ك); 90:15 `يَتِيمًا` (ي ت م)
- Synthesis: Lag joins cognition and movement. The person neither judges firmly nor advances promptly, so intended action arrives late or not at all.

#### Subchannel D. Skittish Withdrawal and Chaste Refusal
- Reading type: latent/lexical
- Scene or process: A person or animal recoils from an approach and preserves distance through refusal.
- Active motifs: skittish or chaste withdrawal `ن و ر:B006/m01`; coercion that drives obedience into disobedience `ك ف ر:B007/m01`; retreat on the heel `ع ق ب:B003/m01`; separation from attachment `ف ك ك:B003/m01`; guarded waiting `ر ق ب:B001/m01`
- Ayah anchors: 90:20 `نَارٌ` (ن و ر); 90:19 `كَفَرُوا` (ك ف ر); 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:13 `فَكُّ رَقَبَةٍ` (ف ك ك, ر ق ب)
- Synthesis: Withdrawal is an active boundary-making response, whether self-chosen or induced by coercion. The subject turns back, breaks contact, and watches from distance rather than continuing in the prior obedience.

## Standalone Subchannels

### S1. Bow Assembly from Sinew, Grip, and Point
- Reading type: latent/lexical
- Scene or process: A bow is assembled from tension-bearing sinew, a thick central grip, and a pointed component used to direct the shot.
- Active motifs: tendon or bowstring `ع ق ب:B001/m01`; thick bow grip `ك ب د:B004/m01`; pointed horn or comb `د ر ي:B004/m01`; arrowhead or leading point `ه د ي:B003/m02`
- Ayah anchors: 90:11-12 `ٱلْعَقَبَةَ` (ع ق ب); 90:4 `كَبَدٍ` (ك ب د); 90:12 `أَدْرَىٰكَ` (د ر ي); 90:10 `هَدَيْنَٰهُ` (ه د ي)
- Synthesis: The bow scene is mechanically complete: sinew stores tension, the central grip receives the archer's force, and the pointed leading element gives that force direction.

### S2. Ostrich Nest, Egg, and Chick
- Reading type: latent/lexical
- Scene or process: An ostrich lays in a ground nest and produces a chick from the egg left there.
- Active motifs: ostrich nest and egg `ب ل د:B012/m01`; ostrich chick `ج ع ل:B010/m01`; animal birth `و ل د:B003/m02`; ground dust `ت ر ب:B001/m01`
- Ayah anchors: 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:8 `نَجْعَل` (ج ع ل); 90:3 `وَلَدَ` (و ل د); 90:16 `مَتْرَبَةٍ` (ت ر ب)
- Synthesis: The scene joins ground hollow, egg, birth, and young animal. Unlike an enclosure built to hold livestock, the nest is a reproductive site made in open earth.

### S3. Allotted Share and Gambling Supervision
- Reading type: latent/lexical
- Scene or process: Shares are divided under an overseer, with a designated arrow and principal stake governing the allocation.
- Active motifs: division into allotted shares `ق س م:B003/m01`; gambling overseer and third arrow `ر ق ب:B006/m01`; choice property `ر ق ب:B012/m01`; unmeasured food or goods heap `ص ب ر:B011/m02`
- Ayah anchors: 90:1 `أُقْسِمُ` (ق س م); 90:13 `رَقَبَةٍ` (ر ق ب); 90:17 `صَّبْرِ` (ص ب ر)
- Synthesis: The allocation scene has stake, portions, device, and supervisor. Division converts the common heap into individual outcomes, while the overseer and arrow regulate how those outcomes are assigned.

### S4. Stick-and-Ball Contest
- Reading type: latent/lexical
- Scene or process: A player uses a dedicated stick to strike the game object in a compact contest.
- Active motifs: striking stick or bat `ق و ل:B008/m01`; struck game-piece `ق و ل:B008/m02`; close stick combat analogy `ب ل د:B011/m02`; effective power `ق د ر:B003/m01`
- Ayah anchors: 90:6 `يَقُولُ` (ق و ل); 90:1-2 `ٱلْبَلَدِ` (ب ل د); 90:5 `يَقْدِرَ` (ق د ر)
- Synthesis: The branch image contains a complete recreational mechanism: implement, struck object, player action, and controlled force. Its resemblance to combat remains secondary to the game operation.

### S5. Smith, Knife, and Carried Blade
- Reading type: latent/lexical
- Scene or process: A smith produces a blade that is carried by strap and sheath and used to still an animal in slaughter.
- Active motifs: smith affiliation `ه ل ك:B007/m01`; knife that stills the slaughtered animal `س ك ن:B007/m01`; sword strap `ن ج د:B009/m01`; blade scabbard `ق ر ب:B010/m01`
- Ayah anchors: 90:6 `أَهْلَكْتُ` (ه ل ك); 90:16 `مِسْكِينًا` (س ك ن); 90:10 `ٱلنَّجْدَيْنِ` (ن ج د); 90:15 `مَقْرَبَةٍ` (ق ر ب)
- Synthesis: Craft, carriage, enclosure, and use form a single blade lifecycle. The smith makes the implement, strap and scabbard secure it in travel, and the knife's action ends the animal's movement.


