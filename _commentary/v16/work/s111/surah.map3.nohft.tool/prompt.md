Surah: 111. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S111 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s111/surah.r2/text.md =====
# Surah 111

- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/s111/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ت ب ب (root_000172): 111:1 تَبَّتْ, 111:1 وَتَبَّ

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع

## ي د ي (root_001693): 111:1 يَدَآ

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

## ECHO ء ي د (root_000071): for 111:1 يَدَآ: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## ء ب و (root_000007): 111:1 أَبِى

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ل ه ب (root_001379): 111:1 لَهَبٍ, 111:3 لَهَبٍ

- **B001** alev dili, ateşin tutuşması ve tutuşturulması — alev, ateş dili ve yanış · ateşten görünen alev · alevlenme ve yanma · ateşin yanması; alevsiz kor kızıllığı · ateş tutuştu ve alevlendi · ateşi tutuşturdu
  ارتفاع لسان النار (maqayis)؛ اللهب لهب النار (maqayis;jamhara;sihah)؛ اشتعال النار الذي قد خلص من الدخان (ayn;tahdhib)؛ التهبت النار وتلهبت وألهبتها (sihah;tahdhib)؛ اللهب اضطرام النار (mufradat)
- **B002** susuzluk ve susayana ya da kızgın zemine bağlı yakıcı sıcaklık — susuzluk · susuzluk ve susayana vuran sıcaklık · güneşte kızmış zeminin kavurucu sıcağı · susamış erkek · susamış kadın
  للعطشان لهبان (maqayis)؛ لهبان الحر في الرمضاء (ayn;tahdhib)؛ يستعمل اللهاب في النار والعطش جميعا (jamhara)؛ اللهبة العطش ورجل لهبان وامرأة لهبى (sihah;tahdhib)؛ اللهاب في الحر الذي ينال العطشان (mufradat)
- **B003** yükselen güçlü parıltı ve alevsi toz ya da duman — alev gibi yükselen parlak toz veya duman · ışığı yükselip güçlü biçimde parlayan her şey
  كل شيء ارتفع ضوؤه ولمع لمعانا شديدا (maqayis)؛ اللهب الغبار الساطع (maqayis;tahdhib)؛ يقال للدخان وللغبار لهب (mufradat)
- **B004** atın coşkun ve toz kaldıran şiddetli koşusu — at şiddetle ve coşkuyla koştu · şiddetle koşup toz kaldıran at · atın şiddetli koşusu ve atılışı
  فرس ملهب إذا أثار الغبار وله ألهوب (maqayis;tahdhib)؛ ألهب الفرس إذا عدا عدوا شديدا (jamhara)؛ ألهب الفرس إذا اضطرم جريه والاسم الألهوب (sihah)؛ فرس ملهب شديد العدو والألهوب العدو الشديد (mufradat)
- **B005** dağ yarığı, dağlar arası derin açıklık veya sarp dağ yüzü — 
  اللهب الشعب الصغير في الجبل (jamhara)؛ اللهب الفرجة والهواء يكون بين الجبلين (sihah)؛ اللهب وجه من الجبل كالحائط لا يستطاع ارتقاؤه (tahdhib)؛ اللهب مهواة ما بين كل جبلين (tahdhib)
- **B006** alevle ilişkili kişi, topluluk ve yer adları — alevle ilişkilendirilmiş bir künye · alevle ilişkilendirilmiş bir boy veya topluluk adı · bir yer adı · bir yer adı · bir kişi adı · bir kabile adı · bir vadi adı
  بنو لهب بطن من العرب (maqayis)؛ لَهاب موضع واللهباء موضع ولهبان اسم واللهبة قبيلة وبنو لهب قبيلة (jamhara)؛ كني أبو لهب به (sihah)؛ بنو لهب حي من العرب اللهبيون (tahdhib)؛ تبت يدا أبي لهب (mufradat)
- **B007** şimşeğin boşluksuz art arda çakması [kalıp] — şimşek arada boşluk bırakmadan art arda çaktı
  ألهب البرق إلهابا وإلهابه تداركه حتى لا يكون بين البرقتين فرجة (tahdhib)
- **B008** çarpıcı güzel kişi veya çok kıllı erkek — çarpıcı derecede güzel · çok kıllı erkek
  الملهب الرائع الجمال والملهب الكثير الشعر من الرجال (tahdhib)

## غ ن ي (root_001110): 111:2 أَغْنَىٰ

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

## م و ل (root_001457): 111:2 مَالُهُۥ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ك س ب (root_001296): 111:2 كَسَبَ

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

## ص ل ي (root_000880): 111:3 سَيَصْلَىٰ

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ECHO ص ل و (root_000879): for 111:3 سَيَصْلَىٰ: withheld observed target; not identity

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## ن و ر (root_001564): 111:3 نَارًا

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

## م ر ء (root_001409): 111:4 وَٱمْرَأَتُهُۥ

- **B001** insan; erkek veya kadın kişi — erkek; bağlama göre kişi · kadın · kadın sözünün değişik söylenişi · kadın sözünün ünlüsü değişen söylenişi · bir kişiye veya İmruülkays'a bağlanan
  يقال امرؤ وامرآن وقوم امرىء؛ وامرأة تأنيث امرىء (maqayis;ayn)؛ المرء الرجل؛ هذه مرأة صالحة ومرة (sihah)؛ امرأة تأنيث امرىء؛ المرء؛ قام امرؤ وضربت امرأ ومررت بامرىء (tahdhib)؛ يقال مرء ومرأة وامرؤ وامرأة (mufradat)
- **B002** erdemli kişilik olgunluğu — erdemli kişilik olgunluğu · erdemli kişilik olgunluğuna erişti · erdemli olgunluğu edinmeye çalıştı · bizim eksiklerimizi öne sürerek kendine erdem payı çıkarıyor · görünüşü ve huyu beğenilen erkek
  المروة كمال الرجولية (maqayis)؛ والمروءة كمال الرجولية؛ مرؤ الرجل وتمرأ إذا تكلف المروءة (ayn;tahdhib)؛ المروءة الإنسانية؛ مرؤ الرجل صار ذا مروءة؛ يتمرأ بنا (sihah)؛ العفة والحرفة؛ المروءة ألا تفعل في السر أمرا وأنت تستحي أن تفعله جهرا؛ المريء الرجل المقبول في خلقه وخلقه (tahdhib)
- **B003** yiyene uygun gelip kolay sindirilme [kalıp] — mideye dokunmadan kolayca sindirilen yemek · yiyene iyi gelip kolay sindirilen yemek · yemek bana iyi geldi · yemek bana uygun geldi · yemeği rahatça yiyip sindirdim · yemeği kolay sindirilir buldum
  المراءة مصدر الشيء المريء الذي يستمرأ؛ مرأني الطعام وامرأني (maqayis)؛ مرؤ الطعام وهو مريء بين المراءة؛ استمرأ (ayn)؛ مرؤ الطعام يمرؤ مراءة صار مريئا؛ مرأني الطعام؛ أمرأني الطعام؛ طعام ممرئ؛ مرئت الطعام استمرأته (sihah)؛ مرئت الطعام استمرأته؛ ما كان مريئا؛ هذا يمرىء الطعام؛ أمرأني الطعام إمراء؛ طعام ممرىء (tahdhib)
- **B004** yemek borusu — yemek borusu
  والمريء رأس المعدة والكرش اللازق بالحلقوم (maqayis)؛ المريء رأس المعدة والكرش اللازق بالحلقوم وهو مجرى الشراب والطعام (ayn)؛ مرئ الجزور والشاة للمتصل بالحلقوم الذي يجري فيه الطعام والشراب (sihah)؛ مرؤ بوزن مرع وهو الذي يجري فيه الطعام والشراب ويدخل فيه؛ الشجر ما لصق بالحلقوم والمريء (tahdhib)
- **B005** yemek yeme veya özel olayda yemek verme — neden yemek yemiyorsun · yemek yedim · ev yapımı veya evlilik dolayısıyla yemek verme
  ما لك لا تمرأ أي ما لك لا تطعم؛ وقد مرأت أي طعمت؛ والمرء الإطعام على بناء دار أو تزويج

## م ر ء (root_001410): 111:4 وَٱمْرَأَتُهُۥ

- **B001** insan; erkek veya kadın kişi — insan; bağlama göre erkek · kadın · kadın sözünün değişik söylenişi · onun karısı sözünün değişik söylenişi
  يقال امرؤ وامرآن وقوم امرىء؛ وامرأة تأنيث امرىء (maqayis)؛ امرأة ، تأنيث امرىء؛ يقال : هي امرأته ، وهي مرأته ، وهي مرته؛ يحول بين المرء وقلبه (tahdhib)
- **B002** erdemli kişilik olgunluğu — erdemli kişilik olgunluğu · erdemli olgunluğa erişti veya erişmeye çalıştı · erdemli olgunluğu edinmeye çalıştı
  والمروة كمال الرجولية وهي مهموزة مشددة ولا يبنى منه فعل (maqayis)؛ المروءة : كمال الرجولية؛ وقد مرؤ الرجل ، وتمرأ ، إذا تكلف المروءة؛ من المروءة : مرؤ الرجل يمرؤ مروءة (tahdhib)
- **B003** yiyene uygun gelip kolay sindirilme — yemeğin yiyene uygun gelme durumu · hafif ve kolay sindirilen yemek · yemeği rahatça yiyip sindirdim · yemek bana iyi geldi · yemek bana uygun geldi · yemek sana iyi gelir · yemek hafif ve kolay sindirilir oldu · yiyene iyi gelip kolay sindirilen yemek
  والمراءة مصدر الشىء المرىء الذي يستمرأ؛ مرأني الطعام وامرأني (maqayis)؛ مرئت الطعام : استمرأته؛ ما كان الطعام مريئا؛ أمرأني الطعام إمراء؛ مرؤ الطعام يمرؤ مراءة؛ المريء : الطعام الخفيف (tahdhib)
- **B004** yemek yeme veya özel olayda yemek verme — yemek yedi · ev yapımı veya evlilik dolayısıyla yemek verme
  ما لك لا تمرأ ؟ أي ما لك لا تطعم ؟ وقد مرأت ، أي طعمت؛ والمرء : الإطعام على بناء دار ، أو تزويج (tahdhib)
- **B005** yemek borusu — yemek borusu
  والمرىء رأس المعدة والكرش اللازق بالحلقوم (maqayis)؛ المريء ، بالهمز غير مشددة؛ وهو الذي يجري فيه الطعام والشراب ويدخل فيه؛ ما لصق بالحلقوم والمريء (tahdhib)
- **B006** görünüşü ve huyu beğenilen erkek [kalıp] — görünüşü ve huyu beğenilen erkek
  وما كان الرجل مريئا؛ المريء : الرجل المقبول في خلقه وخلقه (tahdhib)

## ح م ل (root_000357): 111:4 حَمَّالَةَ

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

## ح ط ب (root_000335): 111:4 ٱلْحَطَبِ

- **B001** yakacak odun ve odun toplama — yakacak odun · odun toplamak · kendisi için odun arayıp toplamak · birisi için odun toplayıp getirmek · odun toplayan kişi · odun toplayan kişi · odun toplayıp satan kişi · odun toplayanlar topluluğu · odunu bol yer · kuru diken veya odun yiyen dişi deve · bağın odunluk dallarını kesme vakti gelmek · bağın üst dalları odun için kesilecek duruma gelmek · bağdan kesilen odunluk üst dallar
  الحطب معروف (maqayis;ayn;jamhara;sihah;tahdhib)؛ ما يعد للإيقاد (mufradat)؛ حطبت واحتطبت إذا جمعته (sihah)؛ حطبت فلانا إذا احتطبت له (tahdhib)؛ مكان حطيب كثير الحطب (maqayis;jamhara;sihah;mufradat)؛ ناقة محاطبة تأكل الشوك اليابس (maqayis;sihah)؛ قد استحطب عنبكم فاحطبوه حطبا (tahdhib)
- **B002** sözünü karıştırıp gereksizce uzatan kimse [kalıp] — sözünü karıştıran, çok veya uzun konuşan kimse
  يقال للمخلط في كلامه حاطب ليل (maqayis;ayn;sihah;tahdhib;mufradat)؛ المسهب كحاطب الليل (jamhara)؛ المكثار كحاطب ليل (tahdhib)
- **B003** laf taşıyıp kötülük körükleme — laf taşıma ve birini başkasına kötüleme · birini başkasına çekiştirip hakkında söz taşımak · laf taşımanın kinayeli anlatımı · laf taşıyıp insanlar arasındaki kötülüğü körüklemek
  حطب فلان بفلان سعى به (maqayis;ayn;tahdhib;mufradat)؛ حمالة الحطب كناية عن النميمة (maqayis;tahdhib;mufradat)؛ الحطب في القرآن النميمة (ayn)؛ يوقد بالحطب الجزل كناية عن ذلك (mufradat)
- **B004** kuru odun gibi çok zayıf kimse — çok zayıf adam · çok zayıf kimse
  الأحطب الشديد الهزال وكذلك الحطب كأنه شبه بالحطب اليابس (maqayis)؛ يقال للشديد الهزال حطب (ayn)؛ الحطب الرجل الشديد الهزال والأحطب مثله (sihah)

## ج ي د (root_000284): 111:5 جِيدِهَا

- **B001** boyun; boynun önü, uzunluğu ve güzelliği — boyun veya boynun ön kısmı · boyun uzunluğu · boyunlar · uzun boyunlu veya güzel boyunlu erkek · uzun ya da güzel boyunlu kadın · güzel boyunlu kadın · boynu güzel kadın
  الجيم والياء والدال أصل واحد وهو العنق (maqayis)؛ الجيد مقدم العنق (ayn)؛ الجيد العنق (jamhara)؛ الجيد طول الجيد والجيداء الطويلة الجيد (maqayis)؛ رجل أجيد وامرأة جيداء حسنة الجيد إذا كانت طويلة العنق (jamhara)؛ امرأة جيدانة حسنة الجيد (ayn)

## ح ب ل (root_000291): 111:5 حَبْلٌ

- **B001** bağlama ve yedme ipi — ip veya yular · ağaca çıkma ipi · ip · ip gibi örülmüş ya da kıvrılmış saç
  الحبل الرسن (ayn;tahdhib)؛ الحبل معروف (jamhara;mufradat)؛ الحبل الرسن معروف والجمع حبال (maqayis)؛ الحابول الكر الذي يصعد به إلى النخل (jamhara;sihah)؛ المحبل الحبل (tahdhib)؛ محبل الشعر كأن كل قرن من قرون رأسه حبل (tahdhib)
- **B002** bağlayıcı söz ve güvence — söz, güvence ve bağlılık bağı · birinden koruma sözü almak · Tanrı'ya yönelten ve birlik sağlayan dayanak · Tanrı'dan ve insanlardan gelen söz ve güvence
  الحبل العهد والأمان والحبل التواصل (ayn)؛ الحبل العهد والحبل الأمان وأخذت بحبل من فلان أي عهدا وأمانا (jamhara)؛ الحبل العهد والأمان وهو مثل الجوار والحبل الوصال (sihah)؛ الحبل العهد والأمان والحبل التواصل والعهد والذمة (tahdhib)؛ استعير للوصل ولكل ما يتوصل به إلى شيء ويقال للعهد حبل (mufradat)؛ المحمول عليه الحبل وهو العهد ويريد الأمان وعهود الخفارة (maqayis)
- **B003** uzun kum sırtı — uzun ve yüksek kum sırtı
  الحبل الرمل الطويل الضخم (ayn)؛ يقال للرمل يستطيل حبل (sihah)؛ الحبل من الرمل المجتمع الكثير العالي والحبل رمل يستطيل ويمتد (tahdhib)؛ الحبل المستطيل من الرمل (mufradat)؛ الحبل القطعة من الرمل يستطيل (maqayis)
- **B004** ip biçimli damar veya bağ — omuz ile kol arasındaki sinir veya bağ · boyundaki ana damar · koldaki damar · yakınında, kolayca elinin altında · atın bacak damarları · atın veya başka bir binek hayvanının bileği
  حبل العاتق وصلة ما بين العاتق والمنكب وحبل الوريد عرق (ayn;tahdhib)؛ حبل الذراع معروف وهذا الأمر على حبل ذراعك أي ممكن لك (jamhara)؛ حبل الوريد عرق في العنق وحبل الذراع في اليد وهو على حبل ذراعك أي في القرب منك (sihah)؛ حبال الفرس عروق قوائمه والمحتبل رسغها (tahdhib)؛ شبه به من حيث الهيئة حبل الوريد وحبل العاتق (mufradat)؛ الحبل حبل العاتق ومحتبله أرساغه (maqayis)
- **B005** avı yakalayan ipli tuzak — avı tuzak kurarak yakalamak · avı ipli tuzakla yakalamak · ipli av tuzağı · av tuzağını kuran kişi · tuzağa yakalanmış av · ölüme götüren tuzaklar ve nedenler · kötülüğe sürükleyen ayartma tuzakları · ortalığın karışması veya her yandan korku gelmesi
  الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه (ayn)؛ الحبالة شرك الصائد والصيد محبول ومحتبل إذا وقع في الحبالة وأنا بين حابل ونابل (jamhara)؛ الحبالة التي يصاد بها والحابل الذي ينصب الحبالة والمحبول الوحشي الذي نشب في الحبالة واحتبله أي اصطاده بالحبالة واختلط الحابل بالنابل (sihah)؛ الحبل مصدر حبلت الصيد واحتبلته إذا نصبت له حبالة فنشب فيها والحبالة المصيدة وثار حابلهم على نابلهم (tahdhib)؛ الحبالة خصت بحبل الصائد والنساء حبائل الشيطان والمحتبل والحابل صاحب الحبالة (mufradat)؛ الحبالة حبالة الصائد واحتبل الصيد إذا صاده بالحبالة (maqayis)
- **B006** gebelik ve karındaki yavru — gebelik veya karındaki yavru · kadın gebe kaldı · gebe dişi · karındaki yavrunun ilerideki yavrusu · gebeliğin başladığı zaman veya yer · yavrunun rahimde yerleştiği bölüm
  حبلت المرأة حبلا فهي حبلى وحبل الحبلة ولد الولد الذي في البطن (ayn)؛ حبلت من الإنس وغيرهم وربما سمي ما في البطن بعينه حبلا والمحبل وقت الحبل وحبل الحبلة ما يكون في بطن الناقة التي هي في بطن أمها (jamhara)؛ الحبل الحمل وقد حبلت المرأة فهي حبلى وحبل الحبلة نتاج النتاج وولد الجنين وكان ذلك في محبل فلان أي في وقت حبل أمه به (sihah)؛ حبلت المرأة تحبل حبلا وهي حبلى وحبل الحبلة ولد الولد الذي في البطن والمحبل موضع الحبل (tahdhib)؛ الحبل وهو الحمل وذلك أن الأيام تمتد به (maqayis)؛ المهبل مستقر الولد من الرحم وهو من باب الإبدال وأصله محبل (maqayis)
- **B007** asma sürgünü ve bitkisel adlar — asma veya asma sürgünü · dikenli ağaçların meyvesi · bölgesel dilde fasulye · bu bitkiyi otlayan kertenkele
  الحبلة طاقة من قضبان الكرم والحبل نوع من الشجر مثل السمر (ayn)؛ الحبلة الكرم والأحبل الذي يسمى اللوبياء لغة يمانية (jamhara)؛ الحبلة ثمر العضاه والحبلة القضيب من الكرم وضب حابل يرعى الحبلة (sihah)؛ الكرمة حبلة والحبلة طاق من قضبان الكرم والحبلة ثمر السمر وثمر العضاه والأحبل اللوبياء (tahdhib)؛ الكرم يقال له حبلة وحبلة لأنه في نباته كالأرشية والحبلة ثمر العضاة (maqayis)
- **B008** kolyeye takılan süs parçası — kolyeye takılan süs parçası
  الحبلة ضرب يصاغ من الحلي (jamhara)؛ الحبلة أيضا حلى يجعل في القلائد وقلائد من حبلة وسلوس (sihah)؛ الحبلة حلي كان يجعل في القلائد في الجاهلية وقلائد من حبلة وسلوس (tahdhib)؛ الحبلة اسم لما يجعل في القلادة (mufradat)؛ الحبلة حلي يجعل في القلائد ولعله مشبه بثمره (maqayis)
- **B009** yer adı ve at yarışı başlangıç alanı — kaynaklarda adı verilen belirli bir yer · bir kentteki yarış alanının başlangıç bölümü · atların yarıştan önce beklediği başlangıç yeri
  الحبل موضع بالبصرة على شاطىء النهر (ayn)؛ الحبل موضع والحبل موقف خيل الحلبة قبل أن تطلق وبه سمي حبل البصرة (jamhara)؛ حبل موضع في شعر لبيد (tahdhib)
- **B010** biçime bağlı adlandırmalar — belirli bir topluluğa mensup · kaynaklarda adı verilen bir topluluk · bir erkek adı
  فلان الحبلي منسوب إلى حي من اليمن (ayn)؛ بنو الحبلى بطن من العرب (jamhara)؛ حبال اسم رجل (sihah)؛ الحبلي منسوب إلى حي من اليمن وبنو الحبلى من الأنصار وحبلوي وحبلي وحبلاوي (tahdhib)
- **B011** ağır bela — ağır bela veya çıkmaza düşüren olay · bilgili, uyanık ve keskin kavrayışlı adam
  الحبل الداهية والجمع حبول (jamhara)؛ الحبل بالكسر الداهية والجمع الحبول (sihah)؛ الحبل الرجل العالم الفطن الداهي والحبل الداهية وجمعه حبول (tahdhib)؛ الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة (maqayis)
- **B012** yerinden kaçmayan cesur kişi — yerinde duran, kaçmayan cesur kişi; aslan · ölüm için kullanılan kalıplaşmış niteleme
  رجل حبيل براح إذا كان شجاعا ويسمى به الأسد أيضا (jamhara)؛ يقال للواقف مكانه كالأسد لا يفر حبيل براح (sihah)؛ يقال للموت حبيل براح (tahdhib)؛ للواقف مكانه لا يفر حبيل براح كأنه محبول وزعم ناس أن الأسد يقال له حبيل براح (maqayis)
- **B013** yalıtık adlandırmalar — geniş veya dar yaradılışlı · öfke, su veya içkiyle dolmuş · ağırlık · içecekten kaynaklanan karın şişliği
  واسع الحبل وضيق الحبل كضيق الخلق وواسع الخلق ورجل حبلان إذا امتلأ غيظا ورجل حبلان من الماء والشراب إذا امتلأ ريا والحبل الثقل والحبال انتفاخ البطن من الشراب والنبيذ ورجل حبلان وامرأة حبلانة وفلان حبلان على فلان أي غضبان وبه حبل أي غضب وغم (tahdhib)
- **B014** o sırada [kalıp] — o sırada, o vakit
  أتيته على حبالة ذاك أي على حين ذاك (tahdhib)
- **B015** yazılı kayıt; başka yoruma göre gebelik başlangıcı — yazılı kayıt; başka yoruma göre gebeliğin yeri veya başlangıcı
  المحبل الكتاب فمن كسر الباء عنى به الكتاب ومن لم يكسر الباء فإنه يريد وأمه حبلى (jamhara)؛ خط له ذلك في المحبل أي كتب له الموت حين حبلت به أمه والمحبل موضع الحبل (tahdhib)

## م س د (root_001422): 111:5 مَّسَدٍۭ

- **B001** bükülü lif veya ip; ipi ustaca bükme — hurma lifi veya yaprağından, deve tüyünden ya da derisinden yapılmış lif veya ip · ipi sağlam ve düzgün biçimde bükmek · bükülü lifsi malzemeden yapılmış ip · iyi bükülmüş ip
  أصل صحيح يدل على جدل شيء وطية (maqayis)؛ المسد ليف يتخذ من جريد النخل (maqayis;ayn;mufradat)؛ المسد حبل يتخذ من أوبار الإبل (maqayis;tahdhib)؛ حبل من ليف أو خوص وقد يكون من جلود الإبل أو من أوبارها (sihah;tahdhib)؛ مسدت الحبل أي أجدت فتله (sihah;tahdhib)
- **B002** ip gibi sıkı ve düzgün beden; eti sıkılaştırma — ip gibi sıkı, ince ve düzgün yapılı · beden yapısı güzel ve sıkı · üst etini sıkılaştırıp güçlendirmek
  امرأة ممسودة مجدولة الخلق كالحبل الممسود (maqayis;mufradat)؛ جارية ممسودة مطوية ممشوقة (ayn;tahdhib)؛ رجل ممسود أي مجدول الخلق (sihah;tahdhib)؛ يمسد أعلى لحمه ويأرمه أي يشده (sihah;tahdhib)
- **B003** gece boyunca durmadan ve güçlüğe göğüs gererek yol alma — gece boyunca durmadan ve güçlüğe katlanarak yol alma
  المسد إدآب السير في الليل (ayn;sihah;tahdhib)؛ يكابد الليل عليها مسدا (ayn;tahdhib)؛ جعل الليث الدأب مسدا لأنه يمسد خلق من يدأب فيطويه ويضمره (tahdhib)
- **B004** yağ veya bal tulumu — yağ veya bal konan deri tulum
  المساد نحي السمن أو العسل (ayn)؛ المساد لغة في المساب وهو نحي السمن وسقاء العسل (sihah)؛ المساد نحي يجعل فيه سمن وعسل (tahdhib)
- **B005** demir mil — demirden yapılmış mil veya eksen
  المسد المحور إذا كان من حديد (ayn)
- **B006** siyah ince deri — siyah ince deri
  المساد الرق الأسود (tahdhib)
- **B007** saçın düzgün yapısı ve güzel görünüşü [kalıp] — saçın düzgün yapısı ve güzel görünüşü
  فلان أحسن مساد شعر من فلان يريد أحسن قوام شعر (tahdhib)



===== _commentary/v16/work/s111/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s111/reader_a_pilot.md)

# S111 Semantic Channel Discovery

## Parent Channels

### 1. Agency, Property, and Consequence
- Semantic invariant: Human capacity becomes visible through hands that acquire, control, transfer, and answer for what they do.
- Surface relation: direct; 111:1 (`تبت`, `يدا`) assigns ruin to the hands, while 111:2 (`أغنى`, `ماله`, `كسب`) denies the saving utility of property and acquisition.
- Surprising reach: The same hand that marks culpable action can also denote favor, direct exchange, skilled work, and protective aid.

#### Subchannel A. Hands, Earnings, and Failed Sufficiency
- Reading type: surface-primary
- Scene or process: A person's acts and acquisitions are gathered under the agency of his hands, yet neither accumulated property nor earned gain averts destruction.
- Active motifs: ruin and loss `ت ب ب:B001/m01`; deeds attributed to the hands `ي د ي:B009/m01`; self-directed earning `ك س ب:B001/m01`; accumulated property `م و ل:B001/m01`; sufficiency and utility `غ ن ي:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `يدا`); 111:2 (`أغنى`, `ماله`, `كسب`)
- Synthesis: The hands function as the accountable source of action, while wealth and earning are the expected means of self-preservation. Their failure to suffice turns economic agency into an outcome-bearing scene: what was acquired remains attached to the agent but cannot rescue him from the ruin attached to his own hands.

#### Subchannel B. Power, Possession, and Submission
- Reading type: latent/lexical
- Scene or process: Strength establishes control, control becomes possession and command, and the subordinate party yields a hand in obedience or pledge.
- Active motifs: strength of hand `ي د ي:B002/m01`; possession in hand `ي د ي:B004/m01`; commanding authority `ي د ي:B005/m01`; surrendered or pledged hand `ي د ي:B006/m01`; possessive attribution `ذ و و:B001/m01`; settled and continuing order `ت ب ب:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `يدا`); 111:3 (`ذات`)
- Synthesis: A hand supplies the capacity to hold and rule, while possessive attribution identifies what falls within that sphere. Submission completes the social mechanism by converting another hand into an acknowledgment of the established order.

#### Subchannel C. Transfer, Favor, and Protective Aid
- Reading type: latent/lexical
- Scene or process: Goods or benefits pass from one agent to another through direct transfer, benefaction, and an assisting hand.
- Active motifs: favor bestowed by hand `ي د ي:B003/m01`; hand-to-hand exchange `ي د ي:B007/m01`; gain procured for another `ك س ب:B002/m01`; practical sufficiency `غ ن ي:B002/m01`; supporting and protecting hand `ي د ي:B016/m01`
- Ayah anchors: 111:1 (`يدا`); 111:2 (`أغنى`, `كسب`)
- Synthesis: Acquisition is not confined to self-enrichment: it can be redirected as a benefit secured for someone else. The favoring, exchanging, and protecting hand forms a transfer scene in which agency is measured by what it places within another person's reach.

#### Subchannel D. Skilled Labor and Accumulated Means
- Reading type: mixed
- Scene or process: Manual skill produces gain, and repeated gain becomes stored property and material independence.
- Active motifs: skilled handcraft `ي د ي:B015/m01`; self-directed earning `ك س ب:B001/m01`; accumulated property `م و ل:B001/m01`; material wealth `غ ن ي:B001/m01`; independence from need `غ ن ي:B001/m02`
- Ayah anchors: 111:1 (`يدا`); 111:2 (`أغنى`, `ماله`, `كسب`)
- Synthesis: The skilled hand supplies the productive operation, earning records its return, and property preserves that return as durable means. Against the surface denial of wealth's saving force, the lexical scene isolates the ordinary labor-to-capital sequence whose expected protection fails.

### 2. Binding, Covenant, and Capture
- Semantic invariant: An extended attachment joins things together, secures a relation, or closes around a target as a constraint.
- Surface relation: direct; 111:5 (`حبل`, `مسد`) presents a cord and its twisted material, with 111:4 (`حمالة`) supplying the adjacent action of bearing.
- Surprising reach: A physical line can become a covenant that protects, a trust that must be carried, or a snare whose connection is hostile rather than sustaining.

#### Subchannel A. Twisted Line, Tether, and Load Attachment
- Reading type: mixed
- Scene or process: Fibrous material is twisted into a line that can tether, lead, climb, suspend, or secure a carried object.
- Active motifs: tethering rope and rein `ح ب ل:B001/m01`; braided cord `م س د:B001/m01`; twisting of fibrous material `م س د:B001/m02`; carrying strap or suspension `ح م ل:B006/m01`; visible load-bearing `ح م ل:B001/m01`
- Ayah anchors: 111:4 (`حمالة`); 111:5 (`حبل`, `مسد`)
- Synthesis: Twisting converts loose fiber into tensile cord, and the finished line converts force into attachment. The same assembly can lead an animal, support a climber, suspend equipment, or bind a load to its bearer.

#### Subchannel B. Covenant Carried as Trust
- Reading type: latent/lexical
- Scene or process: A bond grants security or access, then becomes an entrusted charge whose bearer must uphold its terms.
- Active motifs: covenant and protected bond `ح ب ل:B002/m01`; connective means of access `ح ب ل:B002/m02`; entrusted charge `ح م ل:B003/m01`; culpable burden `ح م ل:B003/m02`; indemnity and financial liability `ح م ل:B004/m01`; surety and guarantee `ح م ل:B004/m02`; pledged submission `ي د ي:B006/m01`; protective alliance `ي د ي:B016/m01`
- Ayah anchors: 111:1 (`يدا`); 111:4 (`حمالة`); 111:5 (`حبل`)
- Synthesis: The cord's joining function becomes a social bond: it gives access, protection, or safe conduct while placing a charge on the person who bears it. Guarantee and pledged hand make the relation enforceable, whereas betrayal turns the same carried trust into culpable weight.

#### Subchannel C. Snare, Pitfall, and Cunning Capture
- Reading type: latent/lexical
- Scene or process: A concealed line or trap intercepts a quarry, while cunning reproduces the mechanism at the level of human danger.
- Active motifs: hunting snare `ح ب ل:B005/m01`; figurative deadly entanglement `ح ب ل:B005/m02`; set hunting trap `ص ل ي:B005/m01`; cunning ruse `ح ب ل:B011/m02`; hand caught in a snare `ي د ي:B001/m02`; predatory limbs `ك س ب:B003/m01`
- Ayah anchors: 111:1 (`يدا`); 111:2 (`كسب`); 111:3 (`سيصلى`); 111:5 (`حبل`)
- Synthesis: The line is arranged before contact, the quarry's own movement closes the trap, and predatory limbs complete the seizure. Cunning extends this physical mechanism into a social pitfall in which apparent connection becomes the means of capture.

### 3. Fire, Heat, and Kindled Conflict
- Semantic invariant: Combustible matter is gathered and ignited, producing flame, heat, and effects that can spread through bodies or social relations.
- Surface relation: direct; 111:3 (`سيصلى`, `نارا`, `لهب`) names exposure to flaming fire, and 111:4 (`حمالة الحطب`) supplies a bearer and fuel.
- Surprising reach: Carrying firewood extends into carrying slander, so material ignition and the outbreak of feud share a single fuel-bearing process.

#### Subchannel A. Fuel Gathering and Ignition
- Reading type: surface-primary
- Scene or process: Firewood is collected and borne to a fire, where kindling converts prepared fuel into active flame.
- Active motifs: combustible firewood `ح ط ب:B001/m01`; gathering and carrying fuel `ح ط ب:B001/m02`; visible load-bearing `ح م ل:B001/m01`; kindling a fire `ص ل ي:B004/m01`; flame and ignition `ل ه ب:B001/m01`; burning fire `ن و ر:B002/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:3 (`سيصلى`, `نارا`); 111:4 (`حمالة`, `الحطب`)
- Synthesis: Fuel begins as material selected and assembled into a portable load. Bearing places it at the fire, kindling initiates combustion, and flame is the visible outcome of the completed supply chain.

#### Subchannel B. Entering Flame and Enduring Scorch
- Reading type: surface-primary
- Scene or process: A body meets or enters a burning environment and undergoes flame, parching heat, and thirst.
- Active motifs: entering or encountering fire `ص ل ي:B003/m01`; burning fire `ن و ر:B002/m01`; scorching heat `ل ه ب:B002/m02`; heat-driven thirst `ل ه ب:B002/m01`; active flame `ل ه ب:B001/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:3 (`سيصلى`, `نارا`)
- Synthesis: The scene moves from approach to immersion: fire is first encountered, then its flame surrounds the subject, and bodily experience resolves into scorch and thirst. The lexical heat states make the surface entry into fire a sustained exposure rather than a momentary contact.

#### Subchannel C. Carried Slander as Social Fuel
- Reading type: mixed
- Scene or process: Harmful speech is borne from person to person until it kindles hostility between them.
- Active motifs: bearing a message `ح م ل:B001/m02`; slanderous carrying `ح ط ب:B003/m01`; kindling social harm `ح ط ب:B003/m02`; feud and enmity `ن و ر:B007/m01`; flame and ignition `ل ه ب:B001/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:3 (`نارا`); 111:4 (`حمالة`, `الحطب`)
- Synthesis: Speech functions as a transported load and each delivery adds fuel to an interpersonal fire. The resulting feud is not merely compared with combustion; it follows the same sequence of collection, carriage, ignition, and spread.

### 4. Household Continuity and Social Identity
- Semantic invariant: A household persists by forming unions, provisioning shared life, generating children, nurturing them, and locating them within a named descent group.
- Surface relation: direct; 111:1 (`أبي`) and 111:4 (`امرأته`) mark family relations, while 111:2 (`ماله`, `كسب`) supplies the household's material register.
- Surprising reach: Terms for flame and cord also produce personal names, lineage labels, gestation, and descent, linking physical continuity with continuity of identity.

#### Subchannel A. Marriage, Dwelling, and Ceremonial Provision
- Reading type: mixed
- Scene or process: A union is established through marriage, marked by feeding, and sustained by residence, ample living, and material means.
- Active motifs: marriage and bridal establishment `غ ن ي:B006/m01`; socially self-sufficient married woman `غ ن ي:B005/m01`; ceremonial feeding `م ر ء:B004/m02`; settled dwelling `غ ن ي:B004/m01`; ample living `ي د ي:B014/m01`; material wealth `غ ن ي:B001/m01`; household property `م و ل:B001/m01`
- Ayah anchors: 111:1 (`يدا`); 111:2 (`أغنى`, `ماله`); 111:4 (`امرأته`)
- Synthesis: Marriage initiates the household, feeding publicly marks its establishment, and dwelling turns the event into continued shared life. Ample means and property provide the ordinary material conditions under which that continuity is expected to hold.

#### Subchannel B. Conception, Gestation, and Birth
- Reading type: latent/lexical
- Scene or process: A woman contains and bears an inner load until the body opens for birth.
- Active motifs: gestation in the womb `ح ب ل:B006/m01`; internal pregnancy `ح م ل:B002/m01`; birth opening at the lower back `ص ل ي:B006/m02`; woman as participant `م ر ء:B001/m02`
- Ayah anchors: 111:3 (`سيصلى`); 111:4 (`امرأته`, `حمالة`); 111:5 (`حبل`)
- Synthesis: The cord root supplies conception and pregnancy, while bearing names the fetus as an internal load. The anatomical birth opening completes the process by moving contained life from gestation into delivery.

#### Subchannel C. Parenthood, Nurture, and Uncertain Descent
- Reading type: mixed
- Scene or process: A parent originates and raises a child, while a carried or found child can enter society with descent still unresolved.
- Active motifs: fatherhood `ء ب و:B001/m01`; feeding and raising the dependent `ء ب و:B001/m02`; carried child of uncertain lineage `ح م ل:B005/m01`; human person `م ر ء:B001/m01`; kinship attribution `ذ و و:B001/m02`
- Ayah anchors: 111:1 (`أبي`); 111:3 (`ذات`); 111:4 (`امرأته`, `حمالة`)
- Synthesis: Parenthood combines origination with sustained care, making nurture rather than mere biological source part of the relation. The carried child reverses the scene: bodily presence is secure, but the kinship link by which society places that child remains unsettled.

#### Subchannel D. Names, Lineage, and Affiliation
- Reading type: latent/lexical
- Scene or process: Persons and groups are located through personal names, descent labels, possessive titles, and affiliations.
- Active motifs: lineage or nisba name `ح ب ل:B010/m01`; personal naming `ح ب ل:B010/m02`; proper name or title from flame `ل ه ب:B006/m01`; lineage or place name from flame `ل ه ب:B006/m02`; possessive title `ذ و و:B001/m03`; paternal relation `ء ب و:B001/m01`
- Ayah anchors: 111:1 (`أبي`, `لهب`); 111:3 (`ذات`, `لهب`); 111:5 (`حبل`)
- Synthesis: Paternal relation supplies one axis of identity, while titles, personal names, and descent labels make that relation socially legible. The surface name built from `لهب` participates in a wider naming mechanism in which ordinary lexical images become durable identifiers.

### 5. Growth, Food, and Nourishment
- Semantic invariant: Living matter flowers and bears produce, then enters systems of animal feeding, processing, storage, ingestion, and bodily sufficiency.
- Surface relation: indirect; 111:4 (`حمالة الحطب`) and 111:5 (`حبل`, `مسد`) provide plant, carrying, and container roots, while 111:2 (`أغنى`, `كسب`) supplies sufficiency and processed yield.
- Surprising reach: Pregnancy and earning roots reappear as fruit-bearing and pressed oil residue, joining biological production to food production.

#### Subchannel A. Flowering, Fruiting, and Vine Material
- Reading type: latent/lexical
- Scene or process: A vine or tree extends shoots, flowers, bears fruit, and leaves woody cuttings.
- Active motifs: vine and plant shoots `ح ب ل:B007/m01`; edible fruit or bean growth `ح ب ل:B007/m02`; blossom and flowering `ن و ر:B004/m01`; fruit-bearing `ح م ل:B002/m02`; woody vine cuttings `ح ط ب:B001/m03`
- Ayah anchors: 111:3 (`نارا`); 111:4 (`حمالة`, `الحطب`); 111:5 (`حبل`)
- Synthesis: Extension produces the plant body, flowering marks reproductive readiness, and bearing converts growth into fruit. The cut woody remainder then moves from living vine into usable material, preserving the whole cycle from shoot to residue.

#### Subchannel B. Flock Feeding and Animal Care
- Reading type: latent/lexical
- Scene or process: Fodder plants and processing byproducts feed herd animals whose age, movement, marking, and illness require attention.
- Active motifs: camel-fodder plant `ص ل ي:B010/m01`; young lamb `ح م ل:B009/m01`; thorn-foraging animal `ح ط ب:B001/m04`; pressed oilcake `ك س ب:B004/m01`; livestock scent sickness `ء ب و:B003/m01`; aged or sore-backed pack animal `ت ب ب:B003/m02`; fire-branding of livestock `ن و ر:B002/m02`; skittish animal flight `ن و ر:B006/m02`
- Ayah anchors: 111:1 (`تبت`, `أبي`); 111:2 (`كسب`); 111:3 (`سيصلى`, `نارا`); 111:4 (`حمالة`, `الحطب`)
- Synthesis: Plant growth and press residue become feed, while the lamb and foraging camel supply the herd participants. Branding identifies the animals, skittish movement complicates handling, and scent-borne sickness introduces the practical vulnerability of the managed flock.

#### Subchannel C. Grinding, Storage, Feeding, and Digestion
- Reading type: latent/lexical
- Scene or process: Food is reduced on a grinding surface, stored in a skin vessel, served, swallowed through the esophagus, and judged by its digestibility and sufficiency.
- Active motifs: grinding slab `ص ل ي:B009/m01`; cooking or roasting by fire `ص ل ي:B004/m02`; pressed oil residue `ك س ب:B004/m01`; skin vessel for fat or honey `م س د:B004/m01`; eating `م ر ء:B004/m01`; ceremonial feeding `م ر ء:B004/m02`; esophagus `م ر ء:B005/m01`; palatable food `م ر ء:B003/m01`; easy digestion `م ر ء:B003/m02`; bodily sufficiency `غ ن ي:B002/m01`
- Ayah anchors: 111:2 (`أغنى`, `كسب`); 111:3 (`سيصلى`); 111:4 (`امرأته`); 111:5 (`مسد`)
- Synthesis: Mechanical reduction and storage prepare food for a social act of serving and a bodily act of ingestion. Palatability, passage, digestion, and sufficiency describe successive tests by which stored material becomes actual nourishment.

### 6. Embodied Structure, Appearance, and Character
- Semantic invariant: A person is configured through linked anatomy, bodily condition, visible presentation, and the conduct by which that presentation becomes social character.
- Surface relation: direct; 111:1 (`يدا`), 111:4 (`امرأته`), and 111:5 (`جيدها`) name body and person, with 111:5 (`حبل`, `مسد`) supplying the structural analogies.
- Surprising reach: Tendons, dry wood, braided cord, and flame become models for bodily linkage, emaciation, slender form, hair, and striking beauty.

#### Subchannel A. Neck, Hand, Tendons, and Internal Passage
- Reading type: mixed
- Scene or process: Limbs and neck connect through cord-like vessels and supports, while an internal passage carries food through the upper body.
- Active motifs: anatomical hand `ي د ي:B001/m01`; neck and its front `ج ي د:B001/m01`; veins and tendons `ح ب ل:B004/m01`; esophagus `م ر ء:B005/m01`; back and tail-base anatomy `ص ل ي:B006/m01`
- Ayah anchors: 111:1 (`يدا`); 111:3 (`سيصلى`); 111:4 (`امرأته`); 111:5 (`جيدها`, `حبل`)
- Synthesis: The body appears as a connected structure rather than a list of parts: cord-like tissues join and stabilize its exterior, while the esophagus forms an interior conduit. Hand, neck, and back locate that network across the body's working frame.

#### Subchannel B. Frailty, Dryness, and Internal Pressure
- Reading type: latent/lexical
- Scene or process: Age, weakness, emaciation, thirst, and abdominal fullness alter the body's strength and shape.
- Active motifs: human age and frailty `ت ب ب:B003/m01`; dry-wood emaciation `ح ط ب:B004/m01`; inner breadth or constriction `ح ب ل:B013/m01`; abdominal swelling and fullness `ح ب ل:B013/m02`; corded or slender physique `م س د:B002/m01`; heat-driven thirst `ل ه ب:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `لهب`); 111:3 (`لهب`); 111:4 (`الحطب`); 111:5 (`حبل`, `مسد`)
- Synthesis: Dryness and age reduce bodily capacity, while fullness or constriction produces pressure from within. Cord and dry wood provide opposing shape analogies: one draws the body tight and slender, the other leaves it depleted and brittle.

#### Subchannel C. Neck Adornment, Hair, and Visible Beauty
- Reading type: latent/lexical
- Scene or process: A graceful neck carries ornament, while hair, garment, bodily form, and modest bearing compose an admired appearance.
- Active motifs: graceful long neck `ج ي د:B001/m02`; necklace ornament `ح ب ل:B008/m01`; striking beauty `ل ه ب:B008/m01`; abundant hair `ل ه ب:B008/m02`; well-formed hair `م س د:B007/m01`; beautiful young woman `غ ن ي:B005/m02`; roomy garment `ي د ي:B014/m02`; modest aversion `ن و ر:B006/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:2 (`أغنى`); 111:3 (`نارا`); 111:5 (`جيدها`, `حبل`, `مسد`)
- Synthesis: The neck is both anatomical support and a display surface for jewelry, while hair, garment, and proportion extend that display across the person. Modest withdrawal supplies a behavioral frame around visible allure, joining presentation to social demeanor.

#### Subchannel D. Manliness, Acceptable Character, and Steadfast Bearing
- Reading type: latent/lexical
- Scene or process: A person cultivates recognized virtue, remains acceptable in appearance and conduct, and bears hardship without collapse.
- Active motifs: complete manly virtue `م ر ء:B002/m01`; cultivated performance of virtue `م ر ء:B002/m02`; acceptable character `م ر ء:B006/m01`; pleasing appearance `م ر ء:B006/m02`; strenuous bearing `ح م ل:B007/m01`; supporting and protecting hand `ي د ي:B016/m01`
- Ayah anchors: 111:1 (`يدا`); 111:4 (`امرأته`, `حمالة`)
- Synthesis: Character is presented as something both possessed and enacted: the person takes on difficult weight, maintains social acceptability, and uses strength in protection. Visible bearing and ethical bearing therefore become two aspects of the same recognized personhood.

### 7. Utterance, Invocation, and Discourse
- Semantic invariant: Speech positions an addressee or referent, modulates the voice, and changes social relations through blessing, curse, song, inquiry, or harmful report.
- Surface relation: direct; 111:1 repeats `تبت` as a declaration or invocation of ruin and contains `أبي`, while the remaining lexical modes arise through roots at 111:2-4.
- Surprising reach: Gathering mixed wood at night becomes a model for indiscriminate or overabundant speech, while carrying wood becomes the circulation of slander.

#### Subchannel A. Paternal Address, Ruin-Curse, and Blessing
- Reading type: mixed
- Scene or process: A speaker addresses a father figure or invokes an outcome, with curse and blessing occupying opposite directions of efficacious speech.
- Active motifs: paternal form of address `ء ب و:B002/m01`; curse or prayer for ruin `ت ب ب:B001/m02`; blessing, mercy, and intercession `ص ل ي:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `أبي`); 111:3 (`سيصلى`)
- Synthesis: Vocative address establishes the interpersonal target, after which invocation seeks to alter that target's state. Ruin and blessing form a polarity within the same speech mechanism: one calls down loss, the other directs mercy or benefit.

#### Subchannel B. Song and Voiced Recitation
- Reading type: latent/lexical
- Scene or process: The voice is shaped into song or softened, affective recitation and can enter a ritual setting.
- Active motifs: singing and melody `غ ن ي:B003/m01`; modulated recitation `غ ن ي:B003/m02`; ritual prayer `ص ل ي:B001/m01`; blessing and intercession `ص ل ي:B002/m01`
- Ayah anchors: 111:2 (`أغنى`); 111:3 (`سيصلى`)
- Synthesis: Vocal modulation transforms ordinary speech into patterned sound, while prayer gives that patterned voice an address and purpose. Song, softened reading, and blessing meet as controlled uses of breath and tone.

#### Subchannel C. Mixed Speech, Slander, and Feud
- Reading type: mixed
- Scene or process: Unselective speech gathers good and bad material together, then malicious report carries selected harm between people and produces enmity.
- Active motifs: indiscriminate or verbose speech `ح ط ب:B002/m02`; slanderous carrying `ح ط ب:B003/m01`; bearing a message `ح م ل:B001/m02`; feud and hostility `ن و ر:B007/m01`
- Ayah anchors: 111:3 (`نارا`); 111:4 (`حمالة`, `الحطب`)
- Synthesis: The night gatherer supplies the discourse model of collecting without discrimination. Once such material is carried toward particular people, mixture becomes slander and the social outcome hardens into feud.

#### Subchannel D. Pointing, Questioning, and Relative Linkage
- Reading type: latent/lexical
- Scene or process: Deictic and relative forms point out an entity, ask what it is, or connect it to a descriptive clause.
- Active motifs: relative connector `ذ و و:B002/m01`; demonstrative pointing `ذ و و:B003/m01`; interrogative “what” `ذ و و:B004/m01`; relative “what/which” `ذ و و:B004/m02`
- Ayah anchors: 111:3 (`ذات`)
- Synthesis: Pointing first makes a referent available, inquiry requests its identification, and relative linkage attaches further information to it. These operations form a compact discourse mechanism for locating and elaborating an entity.

### 8. Place, Time, and Ordered Movement
- Semantic invariant: Scenes become navigable by fixing an occasion, marking what lies ahead, identifying a place, and ordering one mover behind another.
- Surface relation: none
- Surprising reach: Flame becomes the image of a dust-raising gallop, while the prayer root names the racer immediately following the leader.

#### Subchannel A. Occasion, Anteriority, and Continuity
- Reading type: latent/lexical
- Scene or process: An event is fixed to a particular occasion, approached through what lies ahead, and understood as settled or continuing.
- Active motifs: temporal occasion `ح ب ل:B014/m01`; anterior or imminent position `ي د ي:B008/m01`; settled continuity `ت ب ب:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `يدا`); 111:5 (`حبل`)
- Synthesis: Occasion supplies the temporal point, anteriority organizes approach to it, and continuity describes what persists once the event or order is established. Together they form a minimal sequence from imminence to settled duration.

#### Subchannel B. Dwellings, Waymarks, and Starting Positions
- Reading type: latent/lexical
- Scene or process: A traveler or competitor is located by dwelling, landscape ridge, visible marker, named place, and a fixed station before departure.
- Active motifs: dwelling and former habitation `غ ن ي:B004/m01`; elongated sand ridge `ح ب ل:B003/m01`; route marker or boundary `ن و ر:B005/m01`; elevated beacon `ن و ر:B005/m02`; named place `ح ب ل:B009/m01`; race starting station `ح ب ل:B009/m02`
- Ayah anchors: 111:2 (`أغنى`); 111:3 (`نارا`); 111:5 (`حبل`)
- Synthesis: Dwelling provides a stable point of residence, ridges and beacons make the surrounding terrain legible, and the starting station fixes a departure point. The same spatial system can orient travel or organize a formal race.

#### Subchannel C. Leader, Follower, and Blazing Gallop
- Reading type: latent/lexical
- Scene or process: A leading racer passes first, a second competitor follows immediately behind, and forceful running raises a flame-like plume of dust.
- Active motifs: second-place follower `ص ل ي:B007/m01`; blazing gallop and raised dust `ل ه ب:B004/m01`; anterior position `ي د ي:B008/m01`; race starting station `ح ب ل:B009/m02`; continuing course `ت ب ب:B002/m01`
- Ayah anchors: 111:1 (`تبت`, `يدا`, `لهب`); 111:3 (`سيصلى`, `لهب`); 111:5 (`حبل`)
- Synthesis: The starting station releases an ordered field, anteriority identifies the leader, and the next racer is defined by close following. The dust plume converts speed into a visible trace, making sequence perceptible across the course.

### 9. Material Work, Tools, and Transport
- Semantic invariant: Human force is transmitted through shaped implements, rotating parts, attachments, and carrying gear to cut, grind, move, or fabricate material.
- Surface relation: direct; 111:1 (`يدا`), 111:4 (`حمالة`), and 111:5 (`حبل`, `مسد`) present the hand, bearing action, line, and material from which tool assemblies can extend.
- Surprising reach: Roots whose surface senses concern ruin and fire also name cutting and heat-straightening, turning destructive force into controlled manufacture.

#### Subchannel A. Cutting, Grinding, and Rotating Assembly
- Reading type: latent/lexical
- Scene or process: A hand controls a handled implement or workpiece while cutting, grinding, and rotation transform material.
- Active motifs: cutting action `ت ب ب:B004/m01`; broad grinding slab `ص ل ي:B009/m01`; iron axle `م س د:B005/m01`; handle or projecting end `ي د ي:B013/m01`
- Ayah anchors: 111:1 (`تبت`, `يدا`); 111:3 (`سيصلى`); 111:5 (`مسد`)
- Synthesis: The handle couples the worker to the implement, the axle sustains repeatable rotation, and the slab receives pressure and abrasion. Cutting and grinding are distinct operations, but both depend on a stable interface between manual force and resistant material.

#### Subchannel B. Load-Bearing Gear and Conveyance
- Reading type: mixed
- Scene or process: Ropes, straps, mounts, and vehicles attach a load to a bearer or carry people and goods from one place to another.
- Active motifs: visible load-bearing `ح م ل:B001/m01`; conveyance by mount, vessel, or current `ح م ل:B001/m03`; carrying strap or suspension `ح م ل:B006/m01`; mount or litter `ح م ل:B006/m02`; tethering rope `ح ب ل:B001/m01`; handle or attachment end `ي د ي:B013/m01`
- Ayah anchors: 111:1 (`يدا`); 111:4 (`حمالة`); 111:5 (`حبل`)
- Synthesis: Strap and rope first secure an object to the carrying system; mount, litter, or vessel then supplies displacement. The channel joins attachment and transport as successive mechanical functions rather than treating carrying as unaided bodily effort.

#### Subchannel C. Twisting, Heat-Shaping, and Skilled Manufacture
- Reading type: latent/lexical
- Scene or process: Raw fiber or a crooked workpiece is reshaped through twisting, controlled heat, and practiced manual skill.
- Active motifs: twisting fibrous material `م س د:B001/m02`; heat-straightening a rod `ص ل ي:B004/m03`; skilled handcraft `ي د ي:B015/m01`; braided finished cord `م س د:B001/m01`
- Ayah anchors: 111:1 (`يدا`); 111:3 (`سيصلى`); 111:5 (`مسد`)
- Synthesis: Twisting aligns loose fibers into a strong cord, while heat makes a rigid piece temporarily correctable. Skilled handling governs both transformations, converting unstable or misshapen material into a serviceable object.

### 10. Night Work and Endurance
- Semantic invariant: Darkness obscures selection and direction, so work and travel become tests of judgment, effort, and steadfastness.
- Surface relation: indirect; 111:4 (`الحطب`, `حمالة`) supplies the gathering and bearing frame, while 111:5 (`حبل`, `مسد`) supplies danger, steadfastness, and arduous night travel lexically.
- Surprising reach: The failure to distinguish wood in darkness becomes a discourse image for mixing sound and unsound material in speech.

#### Subchannel A. Blind Gathering and Hidden Calamity
- Reading type: latent/lexical
- Scene or process: A wood gatherer works without sight, collects indiscriminately, and risks an unseen calamity while a steadfast figure holds position.
- Active motifs: night wood-gatherer `ح ط ب:B002/m01`; ensnaring calamity `ح ب ل:B011/m01`; steadfast brave figure `ح ب ل:B012/m01`
- Ayah anchors: 111:4 (`الحطب`); 111:5 (`حبل`)
- Synthesis: Darkness removes the gatherer's power to inspect what enters the bundle, making ordinary collection a route into danger. The steadfast figure supplies the counter-response: remaining fixed when concealment would otherwise provoke confusion or flight.

#### Subchannel B. Arduous Night Travel
- Reading type: latent/lexical
- Scene or process: A traveler presses through the night under sustained effort and refuses to abandon the course.
- Active motifs: arduous night journey `م س د:B003/m01`; strenuous bearing `ح م ل:B007/m01`; steadfast brave figure `ح ب ل:B012/m01`
- Ayah anchors: 111:4 (`حمالة`); 111:5 (`حبل`, `مسد`)
- Synthesis: Night travel combines duration, obscured direction, and bodily strain. Bearing names the effort required to continue, while steadfastness converts endurance from passive suffering into maintained forward purpose.

## Standalone Subchannels

### S1. Water-Bearing Storm and Unbroken Lightning
- Reading type: latent/lexical
- Scene or process: A dark cloud carries abundant water while repeated lightning illuminates the sky without an interval.
- Active motifs: water-laden storm cloud `ح م ل:B010/m02`; rain and storm-bearing sky `ح م ل:B010/m03`; unbroken lightning `ل ه ب:B007/m01`; illumination `ن و ر:B001/m01`; elevated radiance `ل ه ب:B003/m01`; Aries as a celestial marker `ح م ل:B010/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:3 (`نارا`); 111:4 (`حمالة`)
- Synthesis: Bearing transfers the logic of an inner load to a cloud heavy with water. Continuous lightning repeatedly reveals that load-bearing sky, while Aries locates the storm image within a larger celestial order.

### S2. Ritual Prayer and Worship Places
- Reading type: latent/lexical
- Scene or process: Worshippers perform an ordered prayer within a designated sacred place marked by an elevated beacon or minaret.
- Active motifs: obligatory ritual prayer `ص ل ي:B001/m01`; blessing and intercession `ص ل ي:B002/m01`; house of worship `ص ل ي:B008/m01`; elevated beacon or minaret `ن و ر:B005/m02`
- Ayah anchors: 111:3 (`سيصلى`, `نارا`)
- Synthesis: The prayer supplies the repeated bodily and vocal act, the worship place contains its community, and the elevated marker makes that place publicly locatable. Blessing extends the rite outward from performance toward its intended beneficiary.

### S3. Soot, Kohl, Tattoo, and Coating
- Reading type: latent/lexical
- Scene or process: Heat produces a dark residue that is stored or prepared and then applied to the body as pigment or coating.
- Active motifs: rising smoke plume `ل ه ب:B003/m02`; soot pigment for kohl or tattoo `ن و ر:B008/m01`; lime coating `ن و ر:B009/m01`; skin vessel for fat or honey `م س د:B004/m01`; pressed oily residue `ك س ب:B004/m01`
- Ayah anchors: 111:1, 111:3 (`لهب`); 111:2 (`كسب`); 111:3 (`نارا`); 111:5 (`مسد`)
- Synthesis: Smoke supplies the dark particulate material, oily or fatty matter provides a medium and storage context, and application converts the preparation into a visible bodily mark. Kohl, tattoo pigment, and lime coating differ in finish but share the process of preparing and laying a substance onto a surface.


