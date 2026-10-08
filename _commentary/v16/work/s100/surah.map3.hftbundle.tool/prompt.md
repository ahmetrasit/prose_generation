Surah: 100. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S100 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s100/surah.r2.hftbundle/text.md =====
# Surah 100

- 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/s100/surah.r2.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع د و (root_000993): 100:1 وَٱلْعَٰدِيَٰتِ

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

## ECHO ع د د (root_000989): for 100:1 وَٱلْعَٰدِيَٰتِ: withheld observed target; not identity

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

## ECHO ع و د (root_001058): for 100:1 وَٱلْعَٰدِيَٰتِ: withheld observed target; not identity

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

## ض ب ح (root_000901): 100:1 ضَبْحًا

- **B001** tilki sesi ve ona benzetilen sesler — tilki, gece kuşu ya da koşan atın özel sesini çıkarmak · tilki, gece kuşları ve kurt sesi ile yankı · bu özel sesi çıkaran · atlar koşarken ağızlarından veya soluklarından kişneme dışı ses çıkarmak
  صوت الثعلب وصوته الضباح (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الهام تضبح والبوم والذئب والصدى (ayn;jamhara;tahdhib)؛ صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة (ayn;sihah;tahdhib;mufradat)
- **B002** ön bacakları uzatarak koşma [kalıp] — at ön bacaklarını uzatarak yürümek veya koşmak · deve yürürken ön bacaklarını ileri uzatmak
  هو عدو فوق التقريب وأصله ضبع (maqayis)؛ ضبح الفرس وضبع إذا حرك ضبعيه في مشيه (jamhara)؛ ضبحت الخيل مثل ضبعت وهو السير (sihah;tahdhib)؛ مد الضبع في العدو والعدو الخفيف (mufradat)
- **B003** üst bölümünü ateşle yakma ve ateşten etkilenme — değneğin üst bölümünü ateşle yakma · değneğin üst bölümünden bir parçayı ateşte yakmak · ateşte yanmış, ateşten etkilenmiş veya ateşle doğrultulmuş · ateşle doğrultulmuş veya ateşin etkisi altında kalmış
  الضبح إحراق أعالي العود بالنار (maqayis;ayn;tahdhib;mufradat)؛ حجارة القداحة مضبوحة (maqayis;ayn;sihah;tahdhib)؛ كل شيء مسته النار فقد ضبحته (ayn)؛ قدح ضبيح ومضبوح إذا قوم بالنار (jamhara)
- **B004** siyaha doğru kararma — rengin hafifçe siyaha dönmesi · güneş rengini değiştirip koyulaştırdı
  الانضباح تغير اللون إلى السواد (maqayis)؛ انضبح لونه أي تغير إلى السواد قليلا (sihah)؛ ضبحته الشمس وضبته إذا غيرت لونه وكذلك النار (tahdhib)
- **B005** kül — kül
  الضبح الرماد (maqayis;sihah;tahdhib)

## و ر ي (root_001642): 100:2 فَٱلْمُورِيَٰتِ

- **B001** iç organları bozan ya da akciğeri tutan hastalık — iç organları ya da akciğeri tutan hastalık · içi hastalıktan bozuldu; irin içini yedi · içi bu hastalıkla bozulmuş kimse · akciğeri tutan hastalık · akciğerinden yaraladı · yara, onu yoklayana bu hastalığı geçirdi
  الورى داء يداخل الجسم (maqayis)؛ وري جوف فلان فهو موري إذا فسد من داء يصيبه (jamhara)؛ ورى القيح جوفه يريه وريا: أكله (sihah)؛ الورى داء يصيب الرجل والبعير في أجوافهما (tahdhib)؛ الوارية داء يأخذ في الرئة (ayn;tahdhib)
- **B002** çakmaktan ateş çıkarma ve sönük ateşi harlama — çakmaktan ateş çıktı · sönük ateşi harlayıp yükseltti · ateş yakmaya yarayan araç
  ورى الزند خرجت ناره (maqayis;jamhara;sihah;mufradat)؛ إذا أخرج الزند النار قيل وري الزند يري (tahdhib)؛ أوريت النار إذا كانت خامدة فأججتها (ayn)؛ أريت النار تأرية إذا رفعتها (tahdhib)
- **B003** çakmak benzetmesiyle başarma, yardım görme ya da savunma [kalıp] — giriştiği işte başarıya ulaşan · sende yardım, içten öğüt ve cömertlik buldum · onu destekledi ve savundu
  ورت بك زنادي إذا أنجده وأعانه (jamhara)؛ وريت بك زنادي أي رأيت منك ما أحب من النصح والنجابة والسماحة (ayn)؛ لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب (tahdhib;mufradat)؛ لوريت عن مولاك أي نصرته ودفعت عنه (tahdhib)
- **B004** yağlı ve semiz olma; iliğin dolgunlaşması — yağlı ve semiz · semiz dişi deve · kemik iliği dolup yoğunlaştı
  اللحم الواري: السمين (maqayis;mufradat)؛ الواري الشحم السمين والوري مثله (ayn)؛ ناقة وارية بغير همز: سمينة (jamhara)؛ وري المخ إذا اكتنز وناقة وارية أي سمينة ولحم وري أي سمين (sihah)
- **B005** gizleme, gizlenme ve başka anlam gösterme — şeyi gizleyip gözden sakladı · gizlendi, gözden kayboldu · haberi gizleyip başka bir anlamı öne çıkarma · niyetini gizlemek için başka bir şey söyledi
  التورية إخفاء الخبر وعدم إظهار السر تقول وريته تورية (ayn)؛ واريت الشيء أي أخفيته وتوارى هو أي استتر (sihah)؛ التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره (tahdhib)؛ واريت كذا إذا سترته وتوارى استتر (mufradat)
- **B006** konuma göre arka, ön, öte ya da öbür yan — arka, ön, öte ya da öbür yan · geri çekil; yana açıl
  وراءك يكون من خلف ويكون من قدام (maqayis)؛ وراء ممدود خلاف قدام (ayn)؛ وراء بمعنى خلف وقد يكون بمعنى قدام وهي من الأضداد (sihah)؛ الوراء الخلف ويكون الأمام وبما وراءه أي بما سواه (tahdhib)؛ وراء زيد كذا لمن خلفه ويقال لما كان قدامه أو في أي جانب من الجدار (mufradat)
- **B007** torun — torun, özellikle oğlun oğlu
  الوراء ولد الولد (maqayis;sihah;mufradat)؛ الوراء ممدود ولد الولد (ayn)؛ الوراء ابن الابن (tahdhib)
- **B008** yeryüzündeki bütün yaratılmışlar — yeryüzündeki yaratılmışlar
  الورى: الخلق (maqayis;sihah;tahdhib)؛ الورى مقصور الأنام الذي على ظهر الأرض (ayn)؛ الورى الأنام الذين على وجه الأرض في الوقت (mufradat)
- **B009** sapıklık çakmağından kıvılcım çıkarmaya çalışma [kalıp] — sapıklık çakmağından kıvılcım çıkarmaya çalışıyor
  فلان يستوري زناد الضلالة

## ق د ح (root_001203): 100:2 قَدْحًا

- **B001** ateş çıkarmak ve ateş çakma araçları — ateş çakmak · çakma aracını vurarak ateş çıkarmak · ateş çakmaya yarayan metal parça · ateş çıkarmaya yarayan çakmak taşı · çakmak taşı veya ateş çıkarma aracı
  قدحت النار (maqayis;sihah)؛ قدحت النار أقدحها قدحا من الزند وغيره (jamhara)؛ المقدح الحديدة التي يقدح بها والقداح الحجر الذي تورى منه النار (ayn)؛ المقدحة ما تقدح به النار والقداحة والقداح الحجر الذي يوري النار (sihah)
- **B002** çentik açmak ve oluşan kusur — bir nesnede çentik veya ezik oluşturmak · içindeki bozukluğu çıkarmak için kemiği metal aletle oymak · ağaç ve kemiklerdeki kusur izleri · ağaçtaki çatlak
  يدل أحدهما على شيء كالهزم في الشيء (maqayis)؛ القدح فعلك إذا قدحت الشيء (maqayis)؛ قدحت العظم إذا نقرته بحديدة (jamhara)؛ القوادح الوصوم في العيدان والعظام (jamhara)؛ القادح الصدع في العود (sihah)
- **B003** birinin soyuna dil uzatmak [kalıp] — birinin soyuna dil uzatmak
  قدح في نسبه طعن (maqayis)؛ قدحت في نسب الرجل إذا طعنت فيه (jamhara)؛ قدحت في نسبه إذا طعنت (sihah)
- **B004** ağaç ve dişte kemirilme ya da çürüme — ağaçta veya dişte oluşan kemirilme ve çürük · ağacı ve dişi yiyen kurtçuk · dişte beliren kara leke · dişlerdeki kusur ve kara lekeler
  القدح تأكل يقع في الشجر والأسنان (maqayis)؛ القادحة الدودة تأكل الشجرة (maqayis)؛ القدح أكال يقع في الشجر وفي الأسنان (ayn)؛ القادحة الدودة التي تأكل الشجرة والسن (ayn)؛ قدح العود إذا وقع فيه الأكال وكذلك السن (jamhara)؛ القادح في الأسنان سواد يظهر فيها (jamhara)؛ قدح الدود في الأسنان والشجر (sihah)
- **B005** sıvıyı elle ya da kepçeyle alma; bunun aracı, miktarı, kalıntısı ve kuyusu — tencere dibinde kalan ve güçlükle alınan yemek artığı · tenceredekini kepçeyle almak · çorbayı kepçeyle almak · çorbayı kepçeyle almak · kepçe · bir kepçe çorba · elle su çekilen kuyu
  الأصل الآخر القديح ما يبقى في أسفل القدر فيغرف بجهد (maqayis)؛ قدحت القدر غرفت ما فيها (maqayis)؛ ركى قدوح تغرف باليد (maqayis;jamhara;sihah)؛ القديح ما يبقى في أسفل القدر فيعرف بجهد (ayn)؛ وقدحت ما في القدر إذا اغترفته (jamhara)؛ المقدحة المغرفة (jamhara)؛ وقدحت المرق غرفته (sihah)؛ القدحة الغرفة (sihah)
- **B006** içecek kabı, yapımcısı ve yapım işi — içecek tası · içecek kabı yapan usta · içecek kabı yapımcılığı
  القدح من الآنية من هذا (maqayis)؛ القداح متخذ الأقداح وصنعته القداحة (ayn)؛ القدح معروف اسم يجمع صغار الأقداح وكبارها (jamhara)؛ القدح واحد الأقداح التي للشرب (sihah)
- **B007** uçsuz ve tüysüz ok gövdesi; talih oyunu oku — uç ve tüy takılmamış ok gövdesi · talih oyununda kullanılan oklardan biri
  القدح وهو السهم بلا نصل ولا قذذ (maqayis)؛ القدح الواحد من قداح الميسر (maqayis)؛ القدح السهم قبل أن يراش وينصل (ayn)؛ القدح قدح السهم العود بلا نصل ولا قذذ (jamhara)؛ القدح الواحد من قداح الميسر (jamhara)؛ القدح بالكسر السهم قبل أن يراش ويركب نصله (sihah)؛ وقدح الميسر أيضا (sihah)
- **B008** yalıtık adlandırmalar [kalıp] — atı çubuk gibi ince olana dek zayıflatmak · çubuk gibi ince, zayıf at · gözü içeri çökmek · gözdeki bozuk sıvıyı çıkarmak · içeri çökmüş göz
  قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح (maqayis)؛ قدحت العين غارت (maqayis)؛ قدحت العين أخرجت ماءها الفاسد (maqayis)؛ قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح (jamhara)؛ قدحت عين الفرس وكذلك عين البعير إذا غارت (jamhara)؛ قدحت العين إذا أخرجت منها الماء الفاسد (sihah)؛ وقدحت عينه وقدحت أيضا مخففة إذا غارت (sihah)؛ وقدح فرسه تقديحا ضمره (sihah)
- **B009** bitkinin körpe uç yaprakları — bitkinin körpe uçları ve taze yaprakları · tek bir körpe bitki ucu
  القداح أرآد رخصة من الفسفسة (ayn)؛ القداح أطراف النبت من الورق الغض (jamhara)
- **B010** bir işi düşünüp nasıl yürütüleceğini tasarlamak [kalıp] — bir işi düşünüp nasıl yürütüleceğini tasarlamak
  الإنسان يقتدح الأمر إذا نظر فيه ودبر (ayn)

## غ ي ر (root_001119): 100:3 فَٱلْمُغِيرَٰتِ

- **B001** yarar sağlayıp durumunu iyileştirme — aileyi geçindiren azık ve ihtiyaç payı · aileye geçimlik ve yarar sağlama · ailesine geçimlik sağladı ve yarar dokundurdu · ona yarar sağladı ve ihtiyacını giderdi · Tanrı onlara yağmur verip durumlarını iyileştirdi · yağmur toprağı suladı · sulanmış toprak · sulanmış toprak · yük takımlarını düzeltiyorlar · devesinin yükünü indirip durumunu düzeltti · hayvanı rahatlatmak için yük takımını düzenleyen kişi
  الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)
- **B002** cana karşılık ceza yerine kabul edilen kan bedeli — bana kan bedelini ödedi · kan bedeli · cana karşılık ceza yerine kabul edilen kan bedeli
  غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)
- **B003** biçimini değiştirme veya yerine başkasını koyma — şeyi değiştirdi ve öncekinden farklı hale getirdi · biçimini değiştirme veya yerine başkasını koyma · durumundan ayrılıp farklı hale geldi · yanlış olanı doğru olanla değiştirip giderdi · onunla alışverişte karşılıklı değiş tokuş yaptı · yerine konan karşılık
  الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)
- **B004** eşini veya ailesini kıskanarak koruma duygusu — eşini veya ailesini kıskanarak koruma duygusu · eşini veya ailesini kıskanıp sakındı · eşine veya ailesine karşı kıskanç ve korumacı · eşine veya ailesine karşı kıskanç erkek · eşine veya ailesine karşı kıskanç kadın · eşine veya ailesine karşı çok kıskanç kişi · eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi
  الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)
- **B005** başka olma, dışta bırakma veya olumsuzlama — başka, aynı olmayan veya aykırı · dışında, dışta bırakarak · değil, olmayan · doğru olmayan, yanlış · biri öteki olmayan iki şey · şeyler birbirinden farklılaştı
  هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)

## ص ب ح (root_000839): 100:3 صُبْحًا

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

## ث و ر (root_000210): 100:4 فَأَثَرْنَ

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

## ECHO ء ث ر (root_000011): for 100:4 فَأَثَرْنَ: withheld observed target; not identity

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

## ن ق ع (root_001544): 100:4 نَقْعًا

- **B001** suyun birikmesi ve suda bekletmeye bağlı adlandırmalar — suyun kendi yerinde toplanıp durulması ve uzun süre kalması · suda bir süre beklemek; su için bir yerde toplanmak · bir şeyin suda bekletildiği kap veya yer · suda bekletilen ilaç, kuru üzüm ya da boya karışımı · kuru üzümün suda pişirilmeden bekletilmesiyle yapılan içecek · suyun toplandığı havuz veya suyu bol kuyu · kuyu ya da kaynaktan çıkıp henüz kaba alınmamış artık su · yemeğin yağlı küçük çukuru veya suyun akıp toplandığı yer · inanan kişinin canının ağzında toplandığı ya da çıktığı biçiminde iki türlü yorumlanan söz
  نقع الماء في منقعه استقر (maqayis)؛ نقع الماء في منقعة السيل اجتمع فيها وطال مكثه (ayn)؛ استنقع الماء إذا اجتمع وكذلك نقع ينقع نقوعا (tahdhib)؛ النقيع الحوض ينقع فيه التمر (maqayis)؛ النقيع البئر الكثيرة الماء (maqayis;tahdhib)؛ نقع البئر فضل مائه (tahdhib)؛ النقوع ما نقع في الماء كدواء أو نبيذ (maqayis)؛ أنقعت الدواء في الماء (ayn)؛ النقوع ما أنقعت من شيء (tahdhib)؛ صبغ فلان ثوبه بنقوع وهو صبغ يجعل فيه من أفواه الطيب (tahdhib)؛ المنقع والمنقعة إناء ينقع فيه الشيء (ayn;tahdhib)؛ الأنقوعة وقبة الثريد وكل شيء سال إليه الماء (ayn;tahdhib)
- **B002** susuzluğu giderme; içe sindirip rahatlama — susuzluğu gideren su · su içip susuzluğunu bütünüyle gidermek · haberi yeterli bulup kabul etmek ve onunla içini rahatlatmak · görüşü güven veren ve insanın içini rahatlatan kişi · bir yudumdan sonra yüreğin ya da kişinin değişmesini anlatan, susuzluğun giderilmesiyle bağlantısı kesin olmayan söz
  ماء ناقع كأنه استقر قراره فكسر الغلة (maqayis)؛ الماء ينقع العطش (ayn)؛ نقعت بالماء إذا شرب حتى يروى (tahdhib)؛ نقع الماء غلته إذا أروى عطشه (tahdhib)؛ ما نقعت بخبره نقوعا (ayn)؛ ما نقعت بخبره أي لم أشتف به (tahdhib)؛ فلان منقع أي يشتفى برأيه (tahdhib)؛ نقعت بذاك نفسي أي اطمأنت إليه ورويت به (tahdhib)
- **B003** dönüş veya evlilik yemeği; kesilmiş deve; soğutulmuş katıksız süt — yolculuktan dönen kişi veya evlilik için hazırlanan yemek · paylaştırmadan önce kesilen ya da belli sayıda hayvan yerine sayılan deve · soğutulmuş katıksız süt
  النقيعة الطعام يتخذ للقادم من السفر (maqayis)؛ النقيعة الجزور تنقع عن عدة إبل (maqayis)؛ النقيعة المحض من اللبن (maqayis)؛ النقيعة هي العبيطة من الإبل وهي جزور (ayn)؛ النقيعة ما صنعه الرجل عند قدومه من السفر (tahdhib)؛ النقيعة طعام الملاك (tahdhib)؛ النقيعة ما نحر من النهب قبل القسم (tahdhib)؛ النقيعة المحض من اللبن يبرد (tahdhib)
- **B004** toz, özellikle havaya kalkmış toz — toz, özellikle havaya kalkmış veya kaldırılmış toz
  والنقع الغبار (ayn)؛ النقع في غير هذا الغبار (tahdhib)؛ النقع الغبار المرتفع (tahdhib)
- **B005** yüksek sesle bağırma ve sesi sürdürme — bağırma veya yüksek ses · sesini art arda sürdürmek ve devam ettirmek · deve kuşunun sesi · sahip olmadığı şeylerle övünüp yüksekten atan adam · yasta sesi yükseltmeyi, yanaklara vurmayı ya da giysi yakasını yırtmayı yasaklayan, yorumu tartışmalı söz
  النقيع الصراخ وهو النقع أيضا (maqayis)؛ نقع الصوت ارتفع (maqayis)؛ النقع صوت النعامة (maqayis)؛ نقع الصوت إذا ارتفع (ayn)؛ نقع بصوته وأنقع صوته إذا تابعه (ayn)؛ النقع رفع الصوت (tahdhib)؛ النقع الصراخ المرتفع (tahdhib)؛ نقع الصارخ بصوته وأنقع صوته إذا تابعه وأدامه (tahdhib)؛ النقاع الرجل يتكثر بما ليس عنده كأنه يصيح به (maqayis)
- **B006** dişlerde toplanıp kalmış zehir; kalıcı ölüm ve öldürme — yılanın dişlerinde toplanmış ve kalıcı zehir · sürekli ve geri dönüşsüz ölüm · inanan kişinin canının ağzında toplandığı ya da öldürülme anlamıyla çıktığı biçiminde iki türlü yorumlanan söz
  ونقع السم في ناب الحية في أنيابها السم ناقع اجتمع فيه (ayn)؛ سم ناقع ثابت (tahdhib)؛ النقيع السم الثابت (tahdhib)؛ سم منقوع ونقيع وناقع (tahdhib)؛ موت ناقع دائم (tahdhib)؛ وقد نقعه إذا قتله (tahdhib)
- **B007** ince killi, verimli ve engebesiz düz arazi — ince ve verimli killi, düz ve engebesiz arazi ya da yer tabanları
  النقاع واحدها نقع وهي الأرض الحرة الطين الطيبة التي لا حزونة فيها ولا ارتفاع ولا انهباط (tahdhib)؛ النقاع قيعان الأرض (tahdhib)
- **B008** işlerin yollarını yordamını deneyerek öğrenmiş kişi — işleri tekrar tekrar deneyip yollarını yordamını öğrenmiş kişi için söylenen söz
  هو شراب بأنقع أي معاود للأمر مرة بعد مرة (maqayis)؛ إن فلانا لشراب بأنقع يضرب مثلا للرجل الذي قد جرب الأمور وعرفها ومارسها حتى خبرها (tahdhib)؛ الأنقع جمع النقع وهو كل ماء مستنقع من ماء عد أو غدير (tahdhib)
- **B009** ağır ve çirkin sözlerle sövmek — ona ağır ve çirkin sözlerle sövmek
  نقعه بالشتم إذا شتمه شتما قبيحا (tahdhib)

## و س ط (root_001646): 100:5 فَوَسَطْنَ

- **B001** adil ve seçkin orta olma — adil, seçkin ve aşırılıktan uzak ölçülü olma · en adil veya topluluğun en seçkinlerinden · topluluğunda soyu seçkin ve konumu yüksek kişi
  بناء صحيح يدل على العدل والنصف، وأعدل الشيء أوسطه (maqayis)؛ فلان وسيط الحسب في قومه (ayn)؛ الوسط من كل شيء أعدله، أمة وسطا أي عدلا (sihah)؛ وسطا عدلا، خيارا، أوسط قومه أي من خيارهم (tahdhib)؛ يستعمل استعمال القصد المصون عن الإفراط والتفريط، فيمدح به نحو السواء والعدل والنصفة (mufradat)
- **B002** uçlar veya parçalar arasındaki orta yer — iki uç veya parçalar arasındaki orta yer · kolyenin ortasındaki değerli taş · orta parmak · sıralamadaki yerine göre orta sayılan ibadet · iki kent arasındaki konumundan adını alan şehir
  النصف، ضربت وسط رأسه، وسط القوم (maqayis)؛ الوسط مخففا يكون موضعا للشيء، اسما لما بين طرفي كل شيء، واسطة القلادة جوهرة تكون في وسط الكرس المنظوم (ayn)؛ الأصبع الوسطى، واسطة القلادة، واسط بلد سمي بالقصر بين الكوفة والبصرة (sihah)؛ ما كان يبين جزء من جزء فهو وسط، وسط الدار، واسطة القلادة (tahdhib)؛ وسط الشيء ما له طرفان، الصلاة الوسطى بين الركعتين وبين الأربع أو بين صلاة الليل والنهار (mufradat)
- **B003** ortaya girme veya ortaya yerleştirme — topluluğun ortasına girip aralarında yer almak · bir şeyi ortaya yerleştirmek
  وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم (ayn)؛ وسطت القوم أسطهم وسطا وسطة أي توسطتهم، التوسيط أن تجعل الشيء في الوسط (sihah)؛ أوسطت القوم ووسطتهم وتوسطتهم بمعنى واحد إذا دخلت وسطهم (tahdhib)
- **B004** iyi ile kötü arasında orta nitelikte — iyi ile kötü arasında, kimi bağlamda iyinin altında
  شيء وسط أي بين الجيد والردئ (sihah)؛ يقال فيما له طرف محمود وطرف مذموم، ويكنى به عن الرذل، فلان وسط من الرجال تنبيها أنه قد خرج من حد الخير (mufradat)
- **B005** insanlar arasında aracılık etme [kalıp] — insanlar arasında aracılık etmek
  التوسط بين الناس، من الوساطة (sihah)
- **B006** ortasından kesip ikiye ayırma — bir şeyi ortasından kesip iki yarıya ayırmak
  التوسيط قطع الشيء نصفين (sihah)
- **B007** özel adlandırma kümesi — benzer küçük bir çadırdan daha büyük kıl çadırı · sütüyle kabı dolduran deve
  الوسوط بيت من بيوت الشعر أكبر من المظلة، ويقال الوسوط من النوق كالصفوف تملأ الإناء (maqayis)

## ج م ع (root_000259): 100:5 جَمْعًا

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

## ء ن س (root_000059): 100:6 ٱلْإِنسَٰنَ

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

## ر ب ب (root_000532): 100:6 لِرَبِّهِۦ, 100:11 رَبَّهُم

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

## ECHO ر ب و (root_000537): for 100:6 لِرَبِّهِۦ, 100:11 رَبَّهُم: withheld observed target; not identity

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

## ك ن د (root_001321): 100:6 لَكَنُودٌ

- **B001** keserek bağlantıyı sona erdirme — bir şeyi, özellikle ip gibi somut bir nesneyi kesmek · teşekkür etmeyi ve karşılık vermeyi bırakmak · babasından ayrılmak ve onunla bağını kesmek
  أصل صحيح واحد يدل على القطع (maqayis)؛ كند الحبل يكنده كندا (maqayis)؛ يكند الشكر أي يقطعه (maqayis)؛ كنده أي قطعه (sihah)
- **B002** gördüğü iyiliği bilmezlik — gördüğü iyilikleri unutan, sıkıntıları sayan, tek başına yiyen, kölesini döven ve yardımını esirgeyen iyilikbilmez kimse · sevgiye, yakınlığa ve sürdürülen ilişkiye karşılık vermeyen kadın
  الكنود الكفور للنعمة (maqayis;ayn)؛ كند كنودا أي كفر النعمة فهو كنود (sihah)؛ لكفور بالنعمة (tahdhib)؛ يعد المصائب وينسى النعم (tahdhib)؛ امرأة كند وكنود أي كفور للمواصلة (tahdhib)؛ كنود كفور للمودة (tahdhib)؛ يأكل وحده ويضرب عبده ويمنع رفده (ayn)؛ كفور لنعمته (mufradat)
- **B003** hiçbir bitki yetiştirmeyen toprak [kalıp] — üzerinde hiçbir bitki yetişmeyen toprak
  الأرض الكنود وهي التي لا تنبت (maqayis)؛ أرض كنود لا تنبت شيئا (sihah)؛ أرض كنود إذا لم تنبت شيئا (mufradat)
- **B004** Yemen'den bir topluluk ile atasının adı — Yemen'den bir topluluğun ve onun atası sayılan kişinin adı
  سمى كندة فيما زعموا لأنه كند أباه أي فارقه (maqayis)؛ كندة أبوحي من اليمن وهو كندة بن ثور (sihah)

## ش ه د (root_000822): 100:7 لَشَهِيدٌ

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

## ح ب ب (root_000286): 100:8 لِحُبِّ

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

## خ ي ر (root_000452): 100:8 ٱلْخَيْرِ

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

## ش د د (root_000782): 100:8 لَشَدِيدٌ

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

## ع ل م (root_001040): 100:9 يَعْلَمُ

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

## ب ع ث ر (root_000130): 100:9 بُعْثِرَ

- **B001** toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma — toprağı altüst edip gömülüyü ortaya çıkarmak; örtülü şeyi çıkarıp açığa kavuşturmak · gömülüyü ortaya çıkarmak için toprağı altüst etme
  بعثره بعثرة إذا قلب التراب عنه (ayn)؛ بعثر ما في القبور أثير وأخرج؛ بعثرت الشيء إذا استخرجته وكشفته (sihah)؛ قلب ترابها وأثير ما فيها (mufradat)
- **B002** eşyayı dağıtıp altüst etme [kalıp] — eşyasını ayırıp dağıtmak ve parçalarını birbirinin üstüne gelecek biçimde altüst etmek
  بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض
- **B003** havuzu yıkıp altını üste çevirme [kalıp] — havuzunu yıkıp alt bölümünü üste gelecek biçimde ters çevirmek
  بعثرت حوضي أي هدمته وجعلت أسفله أعلاه

## ق ب ر (root_001195): 100:9 ٱلْقُبُورِ

- **B001** ölüyü gömme, ona gömü yeri sağlama ve gömü yeri — ölünün gömüldüğü yer; gömüt · ölüyü gömmek ve gömü yerine koymak · ölüyü gömü yerine koyma işi · ölüye gömü yeri sağlamak, gömülmesine izin vermek veya onu gömülecek duruma getirmek · ölü için gömü yeri hazırlama ve onu gömülmeye layık sayılanlar arasına koyma · onu gömmemize izin ver · ölüyü kendi eliyle gömen kimse · gömütlerin bulunduğu yer; mezarlık · gömüt yeri veya gömütlerin bulunduğu yer · gömme işi · ölüye gömü yeri veren · gömütler; mezarlıklar · mezarlığa veya gömüt yerine ilişkin · gömüt kazısında sana yardım eden kişi
  القبر قبر الميت (maqayis)؛ القبر مدفن الإنسان (tahdhib)؛ القبر مقر الميت (mufradat)؛ قبرت الميت أي دفنته (jamhara;sihah;tahdhib)؛ أقبرته جعلت له مكانا يقبر فيه (maqayis;mufradat)؛ المقبرة موضع القبور (ayn;jamhara;tahdhib;mufradat)
- **B002** gizli, alçakta veya içe gömülü kalma — çukurda ve gözden ırak arazi · ürünü yapraklarının arasında saklı duran hurma ağacı · hoş kokulu ağacın içinde gevşeyip aşınmış oyuk bölüm · üzerinde yarıksız ve deliksiz kapalı bir zarla doğan çocuk
  أصل صحيح يدل على غموض في شيء وتطامن (maqayis)؛ أرض قبور غامضة (maqayis;jamhara;tahdhib)؛ نخلة قبور وكبوس يكون حملها في سعفها (maqayis;jamhara;tahdhib)؛ القبر موضع متأكل مسترخى في العود الذي يتطيب به وهو جوفه (ayn)؛ ولد مقبورا لأن عليه جلدة مصمتة ليس فيها شق ولا ثقب (tahdhib)
- **B003** belirli bir kuş türünün adı — belirli bir kuş türünün tekil adı · aynı kuşun adı veya çoğul biçimi · aynı kuş adının değişik söylenişi · aynı kuş için kullanılan başka bir ad biçimi
  القبرة واحدة القبر وهو ضرب من الطير (sihah)؛ القنبراء لغة فيها (sihah)؛ يقال للقنبرة قبرة وقبر (tahdhib)
- **B004** burun ucu ve öfkeli gelişte burnun belirginleşmesi — burun ucu · çıkıntılı burnun baş kısmı için kullanılan küçültme biçimi · burnu öne çıkmış biçimde öfkeli gelmek · burnu kabarmış halde öfkeli gelmek
  جاء فلان رامعا قبراه ورامعا أنفه إذا جاء مغضبا (tahdhib)؛ جاءنا فخا قبراه (tahdhib)؛ القبراة أيضا طرف الأنف (tahdhib)؛ القبيرة تصغير القبرة وهي رأس القنفاء (tahdhib)
- **B005** gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma — ölmek · gömülerde saklı olanların dirilişte veya sırlar açığa çıkarken ortaya çıkarılması · gömülmüşçesine gizli · bilgisizliğe gömülmüş · ölü hükmünde olanlar
  حتى زرتم المقابر كناية عن الموت (mufradat)؛ إذا بعثر ما في القبور إشارة إلى حال البعث (mufradat)؛ أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة (mufradat)؛ الكافر والجاهل ما دام في الدنيا فهو مقبور (mufradat)؛ من في القبور أي الذين هم في حكم الأموات (mufradat)

## ح ص ل (root_000330): 100:10 وَحُصِّلَ

- **B001** toplama ve elde kalanı ortaya koyma — bir şeyi derleyip sonucunu çıkarma · ötekiler gittikten sonra geriye kalıp sabitleşme · hesap veya iş sonunda ortaya çıkan sonuç · sözü özüne ve sonucuna indirgeme · içindekileri açığa çıkarıp bir araya getirme
  أصل واحد منقاس وهو جمع الشيء (maqayis)؛ حصلت الشيء تحصيلا (maqayis;sihah)؛ حصل يحصل حصولا أي بقي وثبت وذهب ما سواه من حساب أو عمل (ayn)؛ تحصيل الكلام رده إلى محصوله (sihah)؛ أظهر ما فيها وجمع أو إظهار الحاصل من الحساب (mufradat)
- **B002** özünü ayırıp çıkarma — özlü veya değerli kısmı ayırıp çıkarma · taş veya maden toprağından değerli metal çıkaran kişi · maden toprağını işleyip değerli kısmını çıkaran kadın · ayrılıp elde edilen özlü veya değerli kısım
  أصل التحصيل استخراج الذهب أو الفضة من الحجر أو من تراب المعدن (maqayis)؛ التحصيل تمييز ما يحصل (ayn)؛ المحصلة المرأة التي تحصل تراب المعدن (sihah)؛ التحصيل إخراج اللب من القشور كإخراج الذهب من حجر المعدن والبر من التبن (mufradat)
- **B003** geride kalan artık — bir şeyin geriye kalan bölümü · geriye kalanlar, artıklar · tahıl kaldırıldıktan sonra harmanda kalan süprüntü · posa ve geride kalan ince döküntü
  بقي وثبت وذهب ما سواه فهو حاصل (ayn)؛ حاصل الشيء ومحصوله بقيته والحصائل البقايا (sihah)؛ الحصالة ما يبقى في الأندر من الحب بعد ما يرفع الحب وهو الكناسة (sihah)؛ قيل للحثالة الحصيل (mufradat)
- **B004** kuş kursağı — kuşlarda besinin toplandığı kursak · kuşların kursakları · uzun boyunlu, iri bir deniz kuşu · göbeğinin üstündeki karın bölümü büyümüş koyun · kuşun boynunu büküp kursağını dışarı çıkarması · kursağını doldurma
  حوصلة الطائر لأنه يجمع فيها (maqayis)؛ حوصلة الطائر معروف والحوصلة طير ويجمع حواصل والحوصل الشاة واحونصل الطير (ayn)؛ الحوصلة واحدة حواصل الطير وقد حوصل أي ملأ حوصلته (sihah)؛ حوصلة الطير ما يحصل فيه الغذاء (mufradat)
- **B005** erken evredeki hurma koruğu — sertleşmemiş, salkım dalları henüz belirginleşmemiş hurma koruğu · bu erken evredeki tek bir hurma meyvesi · hurma ağacının bu erken evrede meyve vermeye başlaması
  الحصل البلح قبل أن يشتد ويظهر ثفاريقه الواحدة حصلة لأنه حصل من النخلة (maqayis)؛ الحصل أيضا البلح قبل أن يشتد وتظهر ثفاريقه الواحدة حصلة وقد أحصل النخل (sihah)
- **B006** toprak yiyen atın karın ağrısı çekmesi [kalıp] — atın toprak yemesi yüzünden karın ağrısı çekmesi
  مما شذ عن الباب وما أدري مم اشتقاقه قولهم حصل الفرس إذا اشتكى بطنه عن أكل التراب (maqayis)؛ حصل الفرس حصلا إذا اشتكى بطنه من أكل تراب النبت (sihah)؛ حصل الفرس إذا اشتكى بطنه عن أكله (mufradat)

## ص د ر (root_000849): 100:10 ٱلصُّدُورِ

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

## خ ب ر (root_000387): 100:11 لَّخَبِيرٌۢ

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



===== _commentary/v16/work/s100/surah.r2.hftbundle/channels.md =====
(source: latent_activation/network/v3/reviews/s100/reader_a_pilot.md)

# s100 Semantic Channel Discovery

## Parent Channels

### 1. Propulsive Force and Incursion
- Semantic invariant: Stored bodily force becomes directed motion, audible strain, a raised trace, and penetration into a gathered body.
- Surface relation: direct; 100:1 `عَادِيَاتِ` and `ضَبْحًا`, 100:3 `صُبْحًا`, 100:4 `أَثَرْنَ` and `نَقْعًا`, and 100:5 `وَسَطْنَ` and `جَمْعًا`.
- Surprising reach: The charge is legible not only as displacement but through breath, alarm, dust, and the gathering of separate strides into momentum.

#### Subchannel A. Accelerating Charge
- Reading type: mixed
- Scene or process: A running mount extends its gait, pants under exertion, gathers speed, and turns that accumulated force into a charge.
- Active motifs: running/coursing (`ع د و:B002/m01`); extended-limb gait (`ض ب ح:B002/m01`); panting breath (`ض ب ح:B001/m01`); forceful charge (`ش د د:B003/m01`); gathered momentum (`ج م ع:B010/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`, `ضَبْحًا`; 100:5 `جَمْعًا`; 100:8 `شَدِيدٌ`
- Synthesis: Running supplies the forward action, extended gait and panting give it an animal mechanism, and gathered motion explains how successive strides become a forceful charge.

#### Subchannel B. Dawn Assault and Alarm
- Reading type: mixed
- Scene or process: A hostile movement arrives in the morning while repeated cries announce the assault and orient it toward an opposing group.
- Active motifs: wrongful incursion (`ع د و:B001/m01`); enemy relation (`ع د و:B003/m01`); morning assault (`ص ب ح:B004/m01`); alarm cry (`ص ب ح:B004/m02`); raised repeated cry (`ن ق ع:B005/m01`); gathered host (`ج م ع:B002/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:3 `صُبْحًا`; 100:4 `نَقْعًا`; 100:5 `جَمْعًا`
- Synthesis: The morning is both the time of attack and the setting for an alarm. Hostility gives the movement its social target, while the repeated cry turns the incursion into a publicly perceived event.

#### Subchannel C. Dust Plume and Center Penetration
- Reading type: surface-primary
- Scene or process: Rapid movement agitates settled earth, raises a dust plume, and carries the movers into the middle of an assembled group.
- Active motifs: stirring earth from place (`ث و ر:B002/m01`); raised dust (`ن ق ع:B004/m01`); entry into the middle (`و س ط:B003/m01`); assembled group (`ج م ع:B002/m01`)
- Ayah anchors: 100:4 `أَثَرْنَ`, `نَقْعًا`; 100:5 `وَسَطْنَ`, `جَمْعًا`
- Synthesis: Agitation produces the visible dust outcome, while entry into the middle completes the spatial process: movement begins outside the group and terminates inside its center.

### 2. Ignition, Light, and Combustion Trace
- Semantic invariant: Contact releases latent fire, fire becomes visible light, and burning leaves altered surfaces and residue.
- Surface relation: direct; 100:2 `مُورِيَاتِ` and `قَدْحًا`, with lexical extensions anchored at 100:1 `ضَبْحًا`, 100:3 `صُبْحًا`, 100:8 `حُبِّ`, and 100:10 `حُصِّلَ`.
- Surprising reach: The successful firestick also extends to successful aid, so ignition becomes a model for an undertaking made effective through assistance.

#### Subchannel A. Flint-to-Fire Mechanism
- Reading type: mixed
- Scene or process: A striking tool meets a fire-bearing material, exposes its hidden flame, and marks the end of the implement with heat.
- Active motifs: striking fire (`ق د ح:B001/m01`); latent fire emerging (`و ر ي:B002/m01`); charred firestick tip (`ض ب ح:B003/m01`); successful firestick or aid (`و ر ي:B003/m01`)
- Ayah anchors: 100:1 `ضَبْحًا`; 100:2 `مُورِيَاتِ`, `قَدْحًا`
- Synthesis: The striker supplies impact, the fire-bearing material supplies concealed energy, and the charred tip records successful contact. The success-and-aid sense carries the same mechanism into social action: help makes an effort catch.

#### Subchannel B. Spark Becoming Lamp
- Reading type: latent/lexical
- Scene or process: Small, weak sparks become perceptible against the larger function of a lamp or dawn light.
- Active motifs: weak unusable sparks (`ح ب ب:B011/m01`); lamp or luminary (`ص ب ح:B005/m01`); kindled hidden fire (`و ر ي:B002/m01`)
- Ayah anchors: 100:2 `مُورِيَاتِ`; 100:3 `صُبْحًا`; 100:8 `حُبِّ`
- Synthesis: The spark is momentary and slight, while the lamp stabilizes fire into usable illumination. Their contrast distinguishes mere emission from sustained light.

#### Subchannel C. Blackening and Ash
- Reading type: latent/lexical
- Scene or process: Heat darkens an exposed surface and reduces burned material to an ashen remainder.
- Active motifs: heat-blackened surface (`ض ب ح:B004/m01`); ash (`ض ب ح:B005/m01`); combustion remainder (`ح ص ل:B003/m02`)
- Ayah anchors: 100:1 `ضَبْحًا`; 100:10 `حُصِّلَ`
- Synthesis: Blackening is the intermediate visible state and ash the terminal residue. The remainder sense places combustion inside the wider pattern of what persists after other material has been removed.

### 3. Water Collection, Surface, and Use
- Semantic invariant: Water settles into receptive ground, develops a layered surface, and then moves into bodies or vessels as drink.
- Surface relation: indirect; the contributing roots occur at 100:3 `صُبْحًا`, 100:4 `أَثَرْنَ` and `نَقْعًا`, 100:6 and 100:11 `رَبّ`, 100:8 `حُبِّ`, 100:9 `يَعْلَمُ`, 100:10 `صُدُورِ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: Cloud, algae, bubbles, and quenching describe successive positions above, upon, and within gathered water.

#### Subchannel A. Lowland Catchment and Abundant Water
- Reading type: latent/lexical
- Scene or process: Soft low ground receives water, a pool holds it in place, and the collected volume becomes a well, sea, or abundant sweet resource.
- Active motifs: soft low catchment (`خ ب ر:B002/m01`); standing pool (`ن ق ع:B001/m01`); abundant or sweet water (`ر ب ب:B013/m01`); sea or water-rich well (`ع ل م:B005/m01`)
- Ayah anchors: 100:4 `نَقْعًا`; 100:6, 100:11 `رَبّ`; 100:9 `يَعْلَمُ`; 100:11 `خَبِيرٌ`
- Synthesis: Receptive terrain is the setting, settling is the process, and abundant stored water is the outcome. The well and sea senses scale the same collection principle from bounded source to immense body.

#### Subchannel B. Cloud, Film, Bubble, and Wave
- Reading type: latent/lexical
- Scene or process: Moisture gathers above as layered cloud and upon water as algae, bubbles, ripples, or waves.
- Active motifs: rising cloud or water spread (`ث و ر:B001/m02`); algae on the surface (`ث و ر:B007/m01`); bubbles and water tracks (`ح ب ب:B008/m01`); layered rain cloud (`ر ب ب:B008/m01`)
- Ayah anchors: 100:4 `أَثَرْنَ`; 100:6, 100:11 `رَبّ`; 100:8 `حُبِّ`
- Synthesis: The motifs form a vertical surface system: cloud layers hold moisture above, algae rests on the water, and bubbles or waves articulate motion across its face.

#### Subchannel C. Quenching, Filling, and Departure
- Reading type: latent/lexical
- Scene or process: A drink is offered in the morning, thirst is quenched, body or vessel reaches fullness, and the drinker departs the water source.
- Active motifs: quenching thirst (`ن ق ع:B002/m01`); drinking to fullness (`ح ب ب:B006/m01`); morning drink (`ص ب ح:B003/m01`); departure from a watering place (`ص د ر:B003/m01`)
- Ayah anchors: 100:3 `صُبْحًا`; 100:4 `نَقْعًا`; 100:8 `حُبِّ`; 100:10 `صُدُورِ`
- Synthesis: Morning drink names the occasion, quenching names the bodily change, fullness marks completion, and departure closes the watering sequence.

### 4. Bounded Contents and Selective Drawing
- Semantic invariant: A receptacle gathers discrete contents and permits them to be stored, served, gripped, or drawn out.
- Surface relation: indirect; the roots occur at 100:2 `قَدْحًا`, 100:4 `نَقْعًا`, 100:5 `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:8 `حُبِّ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: The same hand-to-container geometry connects jars and cups with the leather holder and hand-drawn shafts used for lots.

#### Subchannel A. Storage and Serving Vessels
- Reading type: latent/lexical
- Scene or process: Liquids or food are held in a soaking vessel, large skin, jar, pot, and drinking cup, then made available for use.
- Active motifs: bounded soaking place or vessel (`ن ق ع:B001/m02`); large waterskin (`خ ب ر:B004/m01`); storage jar (`ح ب ب:B007/m01`); large pot (`ج م ع:B012/m01`); drinking cup (`ق د ح:B006/m01`)
- Ayah anchors: 100:2 `قَدْحًا`; 100:4 `نَقْعًا`; 100:5 `جَمْعًا`; 100:8 `حُبِّ`; 100:11 `خَبِيرٌ`
- Synthesis: The vessels differ in scale and use but share one scene signature: contents are bounded, preserved, and positioned for soaking, storage, or serving.

#### Subchannel B. Lot Arrows in Hand and Holder
- Reading type: latent/lexical
- Scene or process: Unmarked shafts are collected in a leather holder and one is removed by a closed hand, like a scoop drawing from the bottom of a vessel.
- Active motifs: lot-arrow shaft (`ق د ح:B007/m01`); leather lot-arrow holder (`ر ب ب:B010/m01`); closed fist or grip (`ج م ع:B005/m01`); scooping or drawing from a vessel (`ق د ح:B005/m01`)
- Ayah anchors: 100:2 `قَدْحًا`; 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`
- Synthesis: The holder gathers the shafts, the hand performs selection, and the drawing sense supplies the removal action. The mechanism is a bounded set converted into a single outcome by extraction.

### 5. Cultivation, Harvest, and Prepared Nourishment
- Semantic invariant: Living material moves from seed and cultivated growth through separation and residue into food prepared for storage or hospitality.
- Surface relation: indirect; contributing roots occur across 100:1 `عَادِيَاتِ`, 100:2 `قَدْحًا`, 100:3 `مُغِيرَاتِ`, 100:4 `أَثَرْنَ` and `نَقْعًا`, 100:5 `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:7 `شَهِيدٌ`, 100:8 `حُبِّ`, 100:9 `بُعْثِرَ`, 100:10 `حُصِّلَ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: The roots of love, testimony, lordship, and running extend into grain, honeycomb, plant care, and late-season herbage.

#### Subchannel A. Seed, Palm, and Green Shoot
- Reading type: latent/lexical
- Scene or process: Seed gives rise to mixed palm growth, unripe fruit, tender tips, evergreen vegetation, and later summer browse.
- Active motifs: grain or seed (`ح ب ب:B001/m01`); mixed palm cultivar (`ج م ع:B011/m01`); unripe date fruit (`ح ص ل:B005/m01`); evergreen plant (`ر ب ب:B012/m01`); tender shoot tips (`ق د ح:B009/m01`); summer herbage (`ع د و:B011/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:2 `قَدْحًا`; 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:8 `حُبِّ`; 100:10 `حُصِّلَ`
- Synthesis: Seed is the material origin, cultivar and shoot describe growth, the unripe date marks an intermediate fruit stage, and evergreen or summer vegetation extends the cycle across seasons.

#### Subchannel B. Tilling, Watering, and Nurture
- Reading type: latent/lexical
- Scene or process: A cultivator stirs soil, supplies water and provisions, and raises the productive thing gradually toward completion.
- Active motifs: soil stirring (`ث و ر:B002/m03`); cultivator and sharecropper (`خ ب ر:B003/m01`); provisioning or watering (`غ ي ر:B001/m01`); gradual nurture (`ر ب ب:B002/m01`)
- Ayah anchors: 100:3 `مُغِيرَاتِ`; 100:4 `أَثَرْنَ`; 100:6, 100:11 `رَبّ`; 100:11 `خَبِيرٌ`
- Synthesis: Soil disturbance prepares the setting, the cultivator supplies agency, watering sustains the process, and nurture names the gradual movement toward a finished crop.

#### Subchannel C. Separation, Grain, and Residue
- Reading type: latent/lexical
- Scene or process: Harvested material is scattered for handling, grain is gathered, the useful kernel is extracted, and chaff or residue remains.
- Active motifs: scattering material (`ب ع ث ر:B002/m01`); gathering material (`ج م ع:B001/m01`); grain (`ح ب ب:B001/m01`); extracting the kernel (`ح ص ل:B002/m01`); chaff or remainder (`ح ص ل:B003/m01`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:8 `حُبِّ`; 100:9 `بُعْثِرَ`; 100:10 `حُصِّلَ`
- Synthesis: Scattering and gathering are complementary operations rather than opposites: they loosen the mixed material so that the kernel can be distinguished from what remains.

#### Subchannel D. Curd, Syrup, Honey, and Welcome Food
- Reading type: latent/lexical
- Scene or process: Solid dairy, thick condiment, comb honey, milk, and slaughtered food are assembled into a prepared meal for arrival or hospitality.
- Active motifs: dried-curd lump (`ث و ر:B005/m01`); thick syrup or paste (`ر ب ب:B006/m01`); honey in comb (`ش ه د:B007/m01`); welcome meal (`ن ق ع:B003/m01`); hospitality slaughter (`ن ق ع:B003/m02`); chilled pure milk (`ن ق ع:B003/m03`)
- Ayah anchors: 100:4 `أَثَرْنَ`, `نَقْعًا`; 100:6, 100:11 `رَبّ`; 100:7 `شَهِيدٌ`
- Synthesis: The motifs occupy distinct food roles: curd is a solid staple, syrup a dressing, honey a sweet stored in wax, and milk or slaughtered meat the substance of a welcoming meal.

### 6. Herd Continuity, Birth, and Fosterage
- Semantic invariant: A living group persists through herd formation, reproductive stages, maturation, descent, and delegated care.
- Surface relation: indirect; roots occur at 100:2 `مُورِيَاتِ`, 100:3 `صُبْحًا`, 100:4 `أَثَرْنَ`, 100:5 `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:7 `شَهِيدٌ`, and 100:8 `حُبِّ` and `شَدِيدٌ`.
- Surprising reach: Herd vocabulary passes into human household structure through foster children, caretakers, grandchildren, and signs of maturity.

#### Subchannel A. Cattle and Herd Cohort
- Reading type: latent/lexical
- Scene or process: Bulls and other livestock form a bounded herd containing animals of different size and activity.
- Active motifs: bull or male cattle (`ث و ر:B004/m01`); livestock herd (`ر ب ب:B014/m01`); grouped animals (`ج م ع:B002/m01`); small or lean animal (`ح ب ب:B010/m01`); camel remaining at its resting place (`ص ب ح:B008/m01`)
- Ayah anchors: 100:3 `صُبْحًا`; 100:4 `أَثَرْنَ`; 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:8 `حُبِّ`
- Synthesis: The herd is the collective setting, the bull and small animal occupy differentiated member roles, and the resting camel adds a state of managed immobility within the cohort.

#### Subchannel B. Pregnancy, Birth Signs, and Maturity
- Reading type: latent/lexical
- Scene or process: Pregnancy advances to recent birth, bodily traces register delivery or puberty, and the young body reaches completeness and mature strength.
- Active motifs: retained pregnancy (`ج م ع:B007/m01`); recently lambed ewe (`ر ب ب:B009/m01`); afterbirth (`ش ه د:B006/m01`); puberty sign (`ش ه د:B006/m02`); mature strength (`ش د د:B004/m01`); bodily wholeness (`ج م ع:B009/m01`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:7 `شَهِيدٌ`; 100:8 `شَدِيدٌ`
- Synthesis: Pregnancy supplies the initial state, afterbirth marks delivery, puberty signs mark a later threshold, and wholeness with mature strength gives the developmental outcome.

#### Subchannel C. Union, Descent, and Fostered Care
- Reading type: latent/lexical
- Scene or process: Sexual union opens a line of descent that includes pregnancy, grandchildren, a fostered child, and the adult who assumes care.
- Active motifs: sexual union (`ج م ع:B006/m01`); pregnancy (`ج م ع:B007/m01`); grandchild (`و ر ي:B007/m01`); fostered child (`ر ب ب:B005/m01`); fosterer or nurse (`ر ب ب:B005/m02`); gradual child-rearing (`ر ب ب:B002/m01`)
- Ayah anchors: 100:2 `مُورِيَاتِ`; 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`
- Synthesis: Biological continuation and social care occupy separate roles in one lineage scene. Descent produces the child relation, while fosterage transfers day-to-day nurture to another adult.

### 7. Knowing and Making Hidden States Legible
- Semantic invariant: Perception, testimony, signs, excavation, and extraction convert concealed states into knowable or manifest ones.
- Surface relation: direct; 100:7 `شَهِيدٌ`, 100:9 `يَعْلَمُ`, `بُعْثِرَ`, and `قُبُورِ`, 100:10 `حُصِّلَ` and `صُدُورِ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: The disclosure pattern spans sensory recognition, speech, body marks, reflected images, graves, mineral casings, and the contents of chests.

#### Subchannel A. Perception, Knowledge, and Expertise
- Reading type: mixed
- Scene or process: A person sees, hears, or senses something, recognizes it as knowledge, and develops inward expertise or learned mastery.
- Active motifs: sensory recognition (`ء ن س:B002/m01`); knowledge and recognition (`ع ل م:B001/m01`); inward expertise (`خ ب ر:B001/m01`); learned scholar (`ر ب ب:B003/m01`)
- Ayah anchors: 100:6 `إِنسَانَ`, `رَبِّ`; 100:9 `يَعْلَمُ`; 100:11 `رَبَّهُم`, `خَبِيرٌ`
- Synthesis: Sensory contact initiates cognition, knowledge stabilizes recognition, inward expertise reaches beneath appearances, and the scholar embodies cultivated command of that knowledge.

#### Subchannel B. Testimony, Report, and Utterance
- Reading type: mixed
- Scene or process: Known content is converted into a decisive report and made outwardly present through testimony and the speaking tongue.
- Active motifs: testimony or decisive declaration (`ش ه د:B002/m01`); report or news (`خ ب ر:B001/m02`); speaking tongue or expression (`ش ه د:B005/m01`); recognized knowledge (`ع ل م:B001/m01`)
- Ayah anchors: 100:7 `شَهِيدٌ`; 100:9 `يَعْلَمُ`; 100:11 `خَبِيرٌ`
- Synthesis: Knowledge supplies the content, report gives it propositional form, testimony commits a speaker to it, and the tongue makes the inner state publicly accessible.

#### Subchannel C. Mark, Indicator, and Reflected Person
- Reading type: latent/lexical
- Scene or process: A mark identifies an object or route, an indicator reveals time or condition, and the pupil carries a visible image of the person before it.
- Active motifs: identifying mark or banner (`ع ل م:B002/m01`); condition-bearing indicator (`ش ه د:B008/m01`); human image in the pupil (`ء ن س:B005/m01`); visible complexion (`ص ب ح:B006/m01`)
- Ayah anchors: 100:3 `صُبْحًا`; 100:6 `إِنسَانَ`; 100:7 `شَهِيدٌ`; 100:9 `يَعْلَمُ`
- Synthesis: Mark and indicator are conventional signs, complexion is a bodily sign, and the pupil is a reflective sign. Each makes an otherwise absent identity or condition available at a surface.

#### Subchannel D. Exhumation and Extraction
- Reading type: mixed
- Scene or process: Covered ground is agitated, a grave or hollow is opened, and a concealed body or valuable core is brought out.
- Active motifs: turning soil to uncover (`ب ع ث ر:B001/m01`); burial enclosure (`ق ب ر:B001/m01`); hidden hollow (`ق ب ر:B002/m01`); concealed thing (`و ر ي:B005/m01`); agitation that exposes (`ث و ر:B002/m02`); extracting a precious core (`ح ص ل:B002/m02`)
- Ayah anchors: 100:2 `مُورِيَاتِ`; 100:4 `أَثَرْنَ`; 100:9 `بُعْثِرَ`, `قُبُورِ`; 100:10 `حُصِّلَ`
- Synthesis: Burial and concealment define the initial enclosure, agitation and turning break that enclosure, and extraction names the final transfer of hidden contents into view.

#### Subchannel E. Interior Collection and Final Disclosure
- Reading type: surface-primary
- Scene or process: What is dispersed within the chest is gathered into a determinate result and becomes fully known.
- Active motifs: manifested result (`ح ص ل:B001/m01`); bodily chest or breast (`ص د ر:B001/m01`); inward expertise (`خ ب ر:B001/m01`); knowledge (`ع ل م:B001/m01`)
- Ayah anchors: 100:9 `يَعْلَمُ`; 100:10 `حُصِّلَ`, `صُدُورِ`; 100:11 `خَبِيرٌ`
- Synthesis: The chest is the interior container, collection converts its dispersed contents into a result, and knowledge reaches that result without remaining at the outward surface.

### 8. Assembly, Center, and Command
- Semantic invariant: Separate persons become a collective organized by a place, a center, a front, and a directing authority.
- Surface relation: direct; 100:5 `وَسَطْنَ` and `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:7 `شَهِيدٌ`, and 100:10 `صُدُورِ`.
- Surprising reach: Spatial precedence at the middle and front scales into social precedence, including lordship and the chief of sailors.

#### Subchannel A. Multitude, Meeting Place, and Summons
- Reading type: mixed
- Scene or process: Dispersed persons are summoned to a shared place, become present together, and form a multitude or confederated group.
- Active motifs: gathering people (`ج م ع:B001/m02`); crowd or community (`ج م ع:B002/m01`); assembly place or time (`ج م ع:B004/m01`); summons to assemble (`ج م ع:B004/m02`); multitude or confederation (`ر ب ب:B004/m01`); witnessed presence (`ش ه د:B001/m01`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:7 `شَهِيدٌ`
- Synthesis: Summons initiates movement, the meeting place supplies a common setting, presence establishes participation, and the multitude is the resulting social body.

#### Subchannel B. Entry into the Center
- Reading type: surface-primary
- Scene or process: An actor crosses from the edge of a group into its middle and occupies the position between its sides.
- Active motifs: middle position (`و س ط:B002/m01`); entering the middle (`و س ط:B003/m01`); gathered group (`ج م ع:B002/m01`)
- Ayah anchors: 100:5 `وَسَطْنَ`, `جَمْعًا`
- Synthesis: The group supplies the bounded field, the middle supplies the target position, and entry supplies the transition from outside to inside.

#### Subchannel C. Foremost Position and Reinforced Authority
- Reading type: mixed
- Scene or process: A master occupies the foremost or central position and reinforces the order governed from it.
- Active motifs: lordship or mastery (`ر ب ب:B001/m01`); foremost position (`ص د ر:B002/m01`); governing center (`و س ط:B002/m01`); reinforcement of rule (`ش د د:B001/m02`)
- Ayah anchors: 100:5 `وَسَطْنَ`; 100:6, 100:11 `رَبّ`; 100:8 `شَدِيدٌ`; 100:10 `صُدُورِ`
- Synthesis: Front and center provide the spatial model, lordship supplies the governing relation, and reinforcement describes how that relation is made durable.

#### Subchannel D. Maritime Command and Sectional Allocation
- Reading type: latent/lexical
- Scene or process: A chief of sailors presides while a whole is divided and distinguished into portions.
- Active motifs: chief of sailors (`ر ب ب:B017/m01`); bisection (`و س ط:B006/m01`); portion or section (`ص د ر:B006/m01`)
- Ayah anchors: 100:5 `وَسَطْنَ`; 100:6, 100:11 `رَبّ`; 100:10 `صُدُورِ`
- Synthesis: Maritime leadership supplies the directing role, bisection supplies the operation, and the portion supplies its result, yielding a compact scene of division under command.

### 9. Covenant, Opposition, and Settlement
- Semantic invariant: Relations between parties are bound as pacts, opposed as enmity, argued through claims, and restored through judgment or mediation.
- Surface relation: indirect; the contributing roots occur at 100:1 `عَادِيَاتِ`, 100:3 `مُغِيرَاتِ`, 100:5 `وَسَطْنَ` and `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:7 `شَهِيدٌ`, 100:8 `شَدِيدٌ`, 100:10 `صُدُورِ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: Roots used on the surface for running, gathering, and entering the middle become the roles of foe, ally, claimant, and mediator.

#### Subchannel A. Binding Pact and Alliance
- Reading type: latent/lexical
- Scene or process: Parties join around a matter, bind themselves by covenant, and reinforce the resulting alliance.
- Active motifs: covenant or pact (`ر ب ب:B011/m01`); joining another on a matter (`ج م ع:B013/m01`); binding and reinforcement (`ش د د:B001/m01`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:8 `شَدِيدٌ`
- Synthesis: Joining creates the aligned parties, the pact defines their obligation, and binding gives that obligation durability.

#### Subchannel B. Hostility and Covenant Rupture
- Reading type: latent/lexical
- Scene or process: A former or possible relation becomes enmity, crosses into aggression, and is severed by departure or broken obligation.
- Active motifs: enemy relation (`ع د و:B003/m01`); transgressive aggression (`ع د و:B001/m01`); severing a relation (`ك ن د:B001/m02`); forceful attack (`ش د د:B003/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:6 `كَنُودٌ`; 100:8 `شَدِيدٌ`
- Synthesis: Enmity supplies the social opposition, aggression realizes it as action, and severing names the broken continuity between parties.

#### Subchannel C. Claim, Testimony, and Restitution
- Reading type: latent/lexical
- Scene or process: An injured party seeks a ruling, testimony and inward knowledge establish the matter, property is assessed or confiscated, and compensation settles the claim.
- Active motifs: appeal for redress (`ع د و:B005/m01`); testimony (`ش ه د:B002/m01`); inward knowledge of the case (`خ ب ر:B001/m01`); confiscation or assessed payment (`ص د ر:B005/m01`); indemnity or blood-money (`غ ي ر:B002/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:3 `مُغِيرَاتِ`; 100:7 `شَهِيدٌ`; 100:10 `صُدُورِ`; 100:11 `خَبِيرٌ`
- Synthesis: The claimant initiates adjudication, testimony and knowledge determine the case, and confiscation or indemnity converts judgment into material settlement.

#### Subchannel D. Mediation between Parties
- Reading type: latent/lexical
- Scene or process: An intermediary enters between opposed sides and works toward renewed agreement.
- Active motifs: mediation (`و س ط:B005/m01`); alliance around a matter (`ج م ع:B013/m01`); covenant (`ر ب ب:B011/m01`); opposing party (`ع د و:B003/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:5 `وَسَطْنَ`, `جَمْعًا`; 100:6, 100:11 `رَبّ`
- Synthesis: Opposition supplies the two sides, the mediator occupies the relational middle, and alliance or covenant supplies the sought outcome.

#### Subchannel E. Defamation, Insult, and Displayed Anger
- Reading type: latent/lexical
- Scene or process: Conflict is verbalized as lineage attack and coarse insult, while anger becomes visible in the face.
- Active motifs: defamation of lineage (`ق د ح:B003/m01`); coarse insult (`ن ق ع:B009/m01`); tongue as expression (`ش ه د:B005/m01`); nose-tip display of anger (`ق ب ر:B004/m01`)
- Ayah anchors: 100:2 `قَدْحًا`; 100:4 `نَقْعًا`; 100:7 `شَهِيدٌ`; 100:9 `قُبُورِ`
- Synthesis: The tongue supplies the expressive tool, defamation and insult supply the hostile acts, and the angered face supplies their bodily counterpart.

### 10. Value, Preference, and Reciprocity
- Semantic invariant: A valued good draws attachment and choice, while generosity and nurture create an obligation that can be answered or denied.
- Surface relation: direct; 100:6 `رَبِّ` and `كَنُودٌ`, 100:8 `حُبِّ`, `خَيْرِ`, and `شَدِيدٌ`, and 100:11 `رَبَّهُم`.
- Surprising reach: Moral good expands into concrete gift, provision, watering, and care, while ingratitude is figured as withholding and severance.

#### Subchannel A. Intense Attachment to the Good
- Reading type: surface-primary
- Scene or process: A person recognizes something as good or beneficial, prefers it, and holds that attachment with intensity.
- Active motifs: love and preference (`ح ب ب:B002/m01`); beneficial good (`خ ي ر:B001/m01`); intensity or force (`ش د د:B002/m01`)
- Ayah anchors: 100:8 `حُبِّ`, `خَيْرِ`, `شَدِيدٌ`
- Synthesis: The good supplies the valued object, love supplies the enduring relation to it, and intensity describes the force of that attachment.

#### Subchannel B. Choice, Excellence, and the Mean
- Reading type: latent/lexical
- Scene or process: Alternatives are compared, the better is selected, and judgment locates a just mean between excess and deficiency.
- Active motifs: choosing the better (`خ ي ر:B003/m01`); excellence (`خ ي ر:B002/m01`); just or balanced mean (`و س ط:B001/m01`); middling rank (`و س ط:B004/m01`); substitution or change (`غ ي ر:B003/m01`)
- Ayah anchors: 100:3 `مُغِيرَاتِ`; 100:5 `وَسَطْنَ`; 100:8 `خَيْرِ`
- Synthesis: Change presents alternatives, choice selects among them, excellence names the upper value, and the mean regulates selection by relation to both extremes.

#### Subchannel C. Benefaction and Broken Return
- Reading type: mixed
- Scene or process: A lord or caretaker grants provision and nurture, but the recipient withholds acknowledgment and severs the expected return.
- Active motifs: lordship or mastery (`ر ب ب:B001/m01`); gradual nurture (`ر ب ب:B002/m01`); generosity or gift (`خ ي ر:B005/m01`); provision and repair (`غ ي ر:B001/m01`); ingratitude and withholding (`ك ن د:B002/m01`)
- Ayah anchors: 100:3 `مُغِيرَاتِ`; 100:6 `رَبِّ`, `كَنُودٌ`; 100:8 `خَيْرِ`; 100:11 `رَبَّهُم`
- Synthesis: Mastery and nurture define the benefactor's role, gift and provision define what moves toward the recipient, and ingratitude reverses the relation by withholding its expected acknowledgment.

### 11. Material Cohesion and Disruption
- Semantic invariant: Material wholes are bound, cut, inverted, scattered, and gathered into a new result.
- Surface relation: direct; 100:5 `جَمْعًا` and `وَسَطْنَ`, 100:6 `كَنُودٌ` and `رَبّ`, 100:8 `شَدِيدٌ`, 100:9 `بُعْثِرَ` and `قُبُورِ`, and 100:10 `حُصِّلَ`.
- Surprising reach: The eschatological scattering and collection sequence also yields a concrete mechanics of knots, shackles, fractures, and inverted basins.

#### Subchannel A. Knot, Bond, and Shackle
- Reading type: latent/lexical
- Scene or process: Separate parts are tightened into a durable knot and restraint closes hands or limbs against movement.
- Active motifs: tightened bond (`ش د د:B001/m01`); firm knot (`ر ب ب:B016/m01`); hand-and-neck shackle (`ج م ع:B008/m01`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`; 100:8 `شَدِيدٌ`
- Synthesis: Tightening is the operation, the knot is its stable structure, and the shackle applies that structure to bodily restraint.

#### Subchannel B. Cutting, Fracture, Hollowing, and Inversion
- Reading type: latent/lexical
- Scene or process: A whole is severed or bisected, a nick opens its surface, a hollow weakens its interior, and inversion overturns the remaining structure.
- Active motifs: severing (`ك ن د:B001/m01`); bisection (`و س ط:B006/m01`); nick or crack (`ق د ح:B002/m01`); internal hollow (`ق ب ر:B002/m01`); inverted or demolished basin (`ب ع ث ر:B003/m01`)
- Ayah anchors: 100:2 `قَدْحًا`; 100:5 `وَسَطْنَ`; 100:6 `كَنُودٌ`; 100:9 `بُعْثِرَ`, `قُبُورِ`
- Synthesis: Severing and bisection divide from outside, nicking initiates a local break, hollowing removes inner support, and inversion completes structural collapse.

#### Subchannel C. Scatter, Gather, and Result
- Reading type: mixed
- Scene or process: A collected set is dispersed, its pieces are gathered again, and their remainder or outcome is made determinate.
- Active motifs: scattering possessions (`ب ع ث ر:B002/m01`); gathering material (`ج م ع:B001/m01`); collected outcome (`ح ص ل:B001/m02`)
- Ayah anchors: 100:5 `جَمْعًا`; 100:9 `بُعْثِرَ`; 100:10 `حُصِّلَ`
- Synthesis: Scattering changes one whole into many pieces, gathering reverses their spatial separation, and collection fixes what the rearrangement has yielded.

### 12. Terrain, Orientation, and Staying
- Semantic invariant: Places are differentiated by hardness, level, edge, middle, facing, and the capacity to hold a body in position.
- Surface relation: indirect; roots occur at 100:1 `عَادِيَاتِ`, 100:2 `مُورِيَاتِ`, 100:3 `صُبْحًا`, 100:4 `نَقْعًا`, 100:5 `وَسَطْنَ`, 100:6 `إِنسَانَ`, `رَبّ`, and `كَنُودٌ`, 100:8 `حُبِّ`, 100:9 `قُبُورِ`, and 100:11 `خَبِيرٌ`.
- Surprising reach: Valley banks and hard ground scale into a human-facing side, an opposite side beyond a barrier, and a body or cloud that remains fixed in place.

#### Subchannel A. Soft Basin, Flat Plain, and Hard Ground
- Reading type: latent/lexical
- Scene or process: A traveler or animal moves across a terrain gradient from soft depression through level clay to hard uneven and barren ground.
- Active motifs: soft low ground (`خ ب ر:B002/m01`); terrain depression (`ق ب ر:B002/m02`); level clay plain (`ن ق ع:B007/m01`); hard uneven ground (`ع د و:B010/m01`); barren soil (`ك ن د:B003/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:4 `نَقْعًا`; 100:6 `كَنُودٌ`; 100:9 `قُبُورِ`; 100:11 `خَبِيرٌ`
- Synthesis: Softness and depression describe receptive ground, the plain removes vertical obstruction, hardness introduces resistance, and barrenness names the land's failed productive outcome.

#### Subchannel B. Edge, Middle, Facing Side, and Beyond
- Reading type: latent/lexical
- Scene or process: An observer locates a thing by its bank or edge, its middle, the side facing a person, and the side behind or beyond a barrier.
- Active motifs: bank or edge (`ع د و:B009/m01`); middle position (`و س ط:B002/m01`); human-facing side (`ء ن س:B004/m01`); behind, before, or beyond (`و ر ي:B006/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:2 `مُورِيَاتِ`; 100:5 `وَسَطْنَ`; 100:6 `إِنسَانَ`
- Synthesis: Edge and middle locate a thing within a field, the human-facing side makes orientation observer-relative, and beyond locates what lies across the intervening boundary.

#### Subchannel C. Residence and Immobilized Animal
- Reading type: latent/lexical
- Scene or process: A body remains at a place through duration, routine, exhaustion, illness, or difficult ground.
- Active motifs: staying or enduring (`ر ب ب:B007/m01`); disabled camel remaining in place (`ح ب ب:B005/m01`); camel lingering at its morning rest (`ص ب ح:B008/m01`); hard unsettled ground (`ع د و:B010/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:3 `صُبْحًا`; 100:6, 100:11 `رَبّ`; 100:8 `حُبِّ`
- Synthesis: Staying supplies the durable state, the two camel motifs distinguish incapacity from routine delay, and difficult ground supplies a setting that reinforces immobility.

### 13. Bodily Interiors, Surfaces, and Health
- Semantic invariant: The body contains hidden cores, presents identifying surfaces, and registers damage or illness through visible and transmissible changes.
- Surface relation: direct; 100:8 `حُبِّ`, 100:10 `صُدُورِ`, with lexical extensions anchored at 100:1 `عَادِيَاتِ` and `ضَبْحًا`, 100:2 `مُورِيَاتِ` and `قَدْحًا`, 100:3 `صُبْحًا`, 100:4 `نَقْعًا`, 100:6 `إِنسَانَ`, 100:7 `شَهِيدٌ`, and 100:9 `يَعْلَمُ`.
- Surprising reach: Eye and tongue represent the person, while moral interiority is given a physical counterpart in the heart's dark core and the contents of the chest.

#### Subchannel A. Person Reflected in Eye and Tongue
- Reading type: latent/lexical
- Scene or process: The pupil receives a visible human image while the tongue renders the person's inner content as expression.
- Active motifs: human image in the pupil (`ء ن س:B005/m01`); tongue or outward expression (`ش ه د:B005/m01`)
- Ayah anchors: 100:6 `إِنسَانَ`; 100:7 `شَهِيدٌ`
- Synthesis: Eye and tongue are paired representational surfaces: one reflects the person's form and the other externalizes the person's speech.

#### Subchannel B. Mouth, Teeth, Color, and Defect
- Reading type: latent/lexical
- Scene or process: The mouth presents ordered white teeth and facial color, while canker, cleft, or darkening interrupts that visible integrity.
- Active motifs: ordered teeth (`ح ب ب:B009/m01`); tooth or tree canker (`ق د ح:B004/m01`); upper-lip cleft (`ع ل م:B004/m01`); altered dark color (`ض ب ح:B004/m02`); bright or reddish complexion (`ص ب ح:B006/m01`)
- Ayah anchors: 100:1 `ضَبْحًا`; 100:2 `قَدْحًا`; 100:3 `صُبْحًا`; 100:8 `حُبِّ`; 100:9 `يَعْلَمُ`
- Synthesis: Ordered teeth and bright complexion establish visible integrity; canker, cleft, and darkening describe distinct ways that integrity is marked or damaged.

#### Subchannel C. Heart Core within the Chest
- Reading type: mixed
- Scene or process: A dark central point of the heart lies enclosed within the broader chest interior.
- Active motifs: dark core of the heart (`ح ب ب:B004/m01`); chest or breast (`ص د ر:B001/m01`)
- Ayah anchors: 100:8 `حُبِّ`; 100:10 `صُدُورِ`
- Synthesis: The chest is the enclosing bodily region and the heart-core is its concentrated interior point, giving inward attachment a precise anatomical depth.

#### Subchannel D. Internal Disease, Contagion, and Poison
- Reading type: latent/lexical
- Scene or process: Disease occupies lung or gut, passes between bodies, weakens an animal, and culminates in a fixed or killing poison.
- Active motifs: internal lung or gut disease (`و ر ي:B001/m01`); transmitted disease (`ع د و:B006/m01`); settled or killing poison (`ن ق ع:B006/m01`); sick camel immobilized (`ح ب ب:B005/m01`); emaciated horse or sunken eye (`ق د ح:B008/m01`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:2 `مُورِيَاتِ`, `قَدْحًا`; 100:4 `نَقْعًا`; 100:8 `حُبِّ`
- Synthesis: Internal disease supplies the originating condition, contagion supplies transmission, wasting and immobility supply bodily outcomes, and poison gives the process a concentrated lethal form.

### 14. Grammatical Reference and Derivation
- Semantic invariant: Language locates referents, excludes alternatives, quantifies occurrence, and derives states or outcomes from a source.
- Surface relation: indirect; roots occur at 100:1 `عَادِيَاتِ`, 100:3 `مُغِيرَاتِ` and `صُبْحًا`, 100:5 `جَمْعًا`, 100:6 and 100:11 `رَبّ`, 100:7 `ذَٰلِكَ`, and 100:10 `حُصِّلَ` and `صُدُورِ`.
- Surprising reach: Physical otherness, possession, front, source, and gathered remainder become operations of reference, exception, derivation, and result.

#### Subchannel A. Otherness, Exception, and Quantification
- Reading type: latent/lexical
- Scene or process: A statement sets an item apart from a class, marks it as other, and qualifies the frequency or quantity of what remains.
- Active motifs: bypass or exception (`ع د و:B004/m01`); otherness or exclusion (`غ ي ر:B005/m01`); quantifying particle (`ر ب ب:B015/m01`); totalized collectivity (`ج م ع:B009/m02`)
- Ayah anchors: 100:1 `عَادِيَاتِ`; 100:3 `مُغِيرَاتِ`; 100:5 `جَمْعًا`; 100:6, 100:11 `رَبّ`
- Synthesis: Exception removes an item from the asserted field, otherness names the contrast, totality defines the larger set, and the particle modulates how often or how many instances are asserted.

#### Subchannel B. Relative, Demonstrative, and Interrogative Reference
- Reading type: latent/lexical
- Scene or process: A discourse identifies a referent by relation, points it out, or asks which thing is intended.
- Active motifs: relative connector (`ذ و و:B002/m01`); demonstrative pointer (`ذ و و:B003/m01`); interrogative referent (`ذ و و:B004/m01`)
- Ayah anchors: 100:7 `ذَٰلِكَ`
- Synthesis: Relative reference links a referent to a clause, demonstration points to it, and interrogation opens its identity as a question; all three organize access to the same discourse object.

#### Subchannel C. Source, Becoming, and Result
- Reading type: latent/lexical
- Scene or process: An expression begins from a verbal source, passes into a changed state, and resolves into a gathered result.
- Active motifs: verbal source or infinitive (`ص د ر:B004/m01`); becoming a state (`ص ب ح:B010/m01`); resultant outcome (`ح ص ل:B001/m03`)
- Ayah anchors: 100:3 `صُبْحًا`; 100:10 `حُصِّلَ`, `صُدُورِ`
- Synthesis: Source supplies grammatical origin, becoming supplies transition, and result supplies the state reached after the transition.

## Standalone Subchannels

### S1. Hunting by Lure and Pursuit
- Reading type: latent/lexical
- Scene or process: A hunter draws quarry from cover, follows successive prey, and operates among animal calls, a falcon, and a hyena.
- Active motifs: lure from a burrow (`خ ي ر:B006/m01`); successive quarry (`ع د و:B008/m01`); falcon (`ع ل م:B006/m01`); male hyena (`ع ل م:B007/m01`); animal call or echo (`ض ب ح:B001/m02`)
- Ayah anchors: 100:1 `عَادِيَاتِ`, `ضَبْحًا`; 100:8 `خَيْرِ`; 100:9 `يَعْلَمُ`
- Synthesis: The lure initiates emergence, pursuit orders prey in sequence, the falcon supplies a hunting agent, and the hyena and animal cries populate the quarry landscape.

### S2. Morning Cycle and Timed Arrival
- Reading type: mixed
- Scene or process: Dawn opens a cycle of morning arrival, drinking or activity, possible morning sleep, and the later rise of full day.
- Active motifs: dawn (`ص ب ح:B001/m01`); morning arrival (`ص ب ح:B002/m01`); morning sleep (`ص ب ح:B007/m01`); specified recurring morning (`ص ب ح:B009/m01`); high day (`ش د د:B005/m01`)
- Ayah anchors: 100:3 `صُبْحًا`; 100:8 `شَدِيدٌ`
- Synthesis: The repeated root supplies a temporal framework rather than one event: dawn is the boundary, arrival and sleep are alternative morning actions, and high day is the later state.

### S3. Companionship and the Intimate
- Reading type: latent/lexical
- Scene or process: Familiar presence removes isolation and establishes a companion, confidant, or specially preferred person.
- Active motifs: companionship that removes loneliness (`ء ن س:B003/m01`); intimate or confidant (`ء ن س:B006/m01`); affectionate preference (`ح ب ب:B002/m01`)
- Ayah anchors: 100:6 `إِنسَانَ`; 100:8 `حُبِّ`
- Synthesis: Familiarity changes the initial state of estrangement, companionship supplies sustained presence, and preference narrows that relation to a trusted intimate.

### S4. Names across Place, People, and Constellation
- Reading type: latent/lexical
- Scene or process: A single name identifies a mountain or place, a tribe or people, and a celestial sign, while another name fixes a distinct tribal identity.
- Active motifs: Thawr as place, people, or constellation (`ث و ر:B006/m01`); Kinda as tribal name (`ك ن د:B004/m01`); tribal confederation (`ر ب ب:B004/m02`)
- Ayah anchors: 100:4 `أَثَرْنَ`; 100:6 `كَنُودٌ`, `رَبِّ`; 100:11 `رَبَّهُم`
- Synthesis: Proper naming carries identity across geographic, social, and celestial referents, while the confederation sense supplies the collective entity that a tribal name can denote.


===== _commentary/v16/work/s100/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 100

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 100:1

## kinetic breath
- reading: Those whose rapid forward extension becomes audible as forced breath.
- mechanism: A plural body in rapid motion stretches forward and forces breath through mouth and chest; the second word makes exertion audible rather than merely naming speed.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ض ب ح B002: ön bacakları uzatarak koşma / عدو ممدود الضبعين) — 

## boundary overrun
- reading: Boundary-crossers whose overrun is heard in their breath, with hostile and non-hostile crossing still coexisting.
- mechanism: Running is read functionally as the act that carries an agent across a boundary. The panting is then the bodily cost or audible signature of overrun, not a neutral speed effect.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:1 w **?** (ع د و B004: aşma, dışarıda bırakma ve öteye geçirme / المجاوزة والاستثناء والصرف) — 
  - 100:1 w **?** (ع د و B003: düşmanlık ve düşman / العَدُوّ والعداوة) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## habituated return
- reading: Practised returners repeatedly spending their remaining strength until service is audible.
- mechanism: The plural can be heard not only as runners but as practised returners: repeated work has become disposition, yet each cycle remains bodily expensive.
- trace:
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ع د و B008: gücü kalmış yaşlı deve / عود مسن فيه بقايا قوة) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## prepared succession
- reading: Prepared, countable units advancing successively in a coordinated run.
- mechanism: The plural is reconstructed as a prepared, countable series rather than an undifferentiated mass. Successive units follow in one run, each contributing a pulse of movement and breath.
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 
  - 100:1 w **?** (ع د و B008: iki avı peş peşe ele geçirme / العِداء في تعاقب الصيد) — 
  - 100:1 w **?** (ض ب ح B002: ön bacakları uzatarak koşma / عدو ممدود الضبعين) — 

## motion scorch
- reading: Running with a latent material arc from heat-touch to blackening and ash.
- mechanism: The focus can carry a dormant thermo-material reading: rapid movement is not only heard but leaves matter heat-touched. The direction from motion to scorching is a provisional reader inference, not supplied by the focus alone.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 
  - 100:1 w **?** (ض ب ح B005: kül / الرماد) — 

## seasonal hard route
- reading: Habitual seasonal travelers panting along an old route over hard summer ground.
- mechanism: A seasonal travel circuit is possible: habitual movers traverse an old, hard route after spring, breathing under environmental strain. This remains form-distant but is internally functional rather than a loose list of landscape images.
- trace:
  - 100:1 w **?** (ع د و B010: sert, kuru ve engebeli yer / العَدْواء في صلابة المكان واضطرابه) — 
  - 100:1 w **?** (ع د و B011: develerin otladığı yaz yeşermesi / العَدَوِيّة من نبات الصيف) — 
  - 100:1 w **?** (ع د و B009: eski yol ve köklü geçmiş / قدم وطريق عود) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## strike ignition
- reading: Kinetic agents whose exertion begins a motion-to-ignition chain; breath and heat remain co-present.
- mechanism: The latent scorch reading of ضَبْحًا becomes a process model. The focus supplies rapid motion and scorchable heat-effect; 100:2 supplies fire hidden in a striker and its successful emergence through striking. I infer, but the packet does not state, the arrow motion or repeated contact → ignition.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## temporal threshold
- reading: Agents crossing and changing a temporal state, with hostile overrun still available but no longer exhaustive.
- mechanism: The boundary-crossing baseline becomes temporal and transformative. عَٰدِيَٰتِ still supplies passing beyond; 100:3 adds altered form and first light. The runners can therefore be read as carrying an event across a phase boundary, from one state of the scene into another at dawn.
- trace:
  - 100:1 w **?** (ع د و B004: aşma, dışarıda bırakma ve öteye geçirme / المجاوزة والاستثناء والصرف) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## residual trail
- reading: A passage reconstructed from emitted breath and a spreading material trail that survives the bodies' passing.
- mechanism: The focus agents become trace-producing bodies. Breath is the first short-lived residue; later motion raises and spreads dust, while the non-dominant ء ث ر mapping activates a lasting mark that points backward to what passed. The packet supplies motion, spread, dust, and mark; I infer that these residues form one evidentiary trail.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## coordinated penetration
- reading: A timed formation concentrating its parts to enter the middle of a gathered body.
- mechanism: The prepared-succession baseline gains a destination and formation geometry. Countable, readied runners do not merely move together: they enter the middle of a gathered body while their separate units gather force into one advance.
- trace:
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 
  - 100:1 w **?** (ع د و B008: iki avı peş peşe ele geçirme / العِداء في تعاقب الصيد) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 

## service ingratitude
- reading: Practised bearers of benefit whose audible expenditure throws human severance and ingratitude into relief.
- mechanism: The abrupt human proposition activates the non-dominant habituation and returned-benefit branches of عَٰدِيَٰتِ. The focus plurality can now function as a contrastive image of trained expenditure and benefit, set against the human who cuts the bond and denies nurture. The packet supplies the two poles; I infer the contrast between them.
- trace:
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ع د و B006: kişiye dönen yarar ve iyilik / عائدة ومعروف يرجع) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## embodied witness
- reading: Panting and trail as a distributed testimony: body and terrain disclose what occurred.
- mechanism: The residual-trail model becomes testimony. The focus breath is an involuntary bodily mark, the dust/trace points backward to passage, and 100:7 supplies both present witnessing and a sign that bears witness. The verse can therefore be read as swearing by bodies that testify through what exertion makes them emit.
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## desire as charge
- reading: A bodily diagram of desire: inward attachment tightens, accelerates pursuit of perceived good, and can terminate in withholding.
- mechanism: The physical charge in 100:1 becomes an enacted model of attachment. Love stays in the heart, perceived good supplies the object, and severity both binds and intensifies a charge or run. I infer an analogy: desire moves the human as forcefully as the opening plurality moves through terrain.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## forward return
- reading: The outbound phase of a larger return-to-destination cycle in which concealed states are reversed into disclosure.
- mechanism: The non-dominant return and destination branches of عَٰدِيَٰتِ become structurally consequential when concealed contents are overturned and disclosed. Forward rushing is no longer purely outbound: the larger sequence bends motion toward a return in which what was lowered and hidden comes back into exposure.
- trace:
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ع د و B002: dönüş yeri ve son varış / مصير ومرجع ومعاد) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## interior exhales
- reading: Breath as the body's involuntary opening: an interior source becomes audible through the exertion it generates.
- mechanism: ضَبْحًا is re-read as an inside becoming audible outside. 100:10 supplies the chest, the source from which acts issue, and extraction of a valuable core from its covering. The opening pant is therefore not decorative sound: it is involuntary disclosure of the interior state that produces motion.
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## known service
- reading: Visible expenditure and hidden orientation held together as a fully known service relation.
- mechanism: The service-versus-ingratitude reading closes as an assessed relation. The focus's practised return and returned benefit stand before the nurturer who knows the inward reality of the matter. This does not identify the runners; it changes their expenditure from spectacle into a legible act whose source and return are known.
- trace:
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ع د و B006: kişiye dönen yarar ve iyilik / عائدة ومعروف يرجع) — 
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## redress run
- reading: Urgent agents crossing distance to secure redress, repair, or provision.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B005: yetkiliden hakkını almasını isteme / العَدْوى في طلب الإنصاف) — 
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 

## transmitted fire
- reading: Mobile carriers of a latent activation that crosses contact boundaries and ignites what it reaches.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B006: hastalığın bulaşması / العَدْوى في انتقال الداء) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## watering route
- reading: A recurrent seasonal circuit over hard, sparse land toward quenching water and away from its source, with panting as ecological cost.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B010: sert, kuru ve engebeli yer / العَدْواء في صلابة المكان واضطرابه) — 
  - 100:1 w **?** (ع د و B011: develerin otladığı yaz yeşermesi / العَدَوِيّة من نبات الصيف) — 
  - 100:1 w **?** (ع د و B009: eski yol ve köklü geçmiş / قدم وطريق عود) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ن ق ع B002: susuzluğu giderme; içe sindirip rahatlama / ماء ينقع الغلة ويروي) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## useless spark
- reading: A warning image of intense expenditure whose bright sparks may yield only ash or dross rather than useful good.
- mechanism: 
- trace:
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B005: kül / الرماد) — 
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## counted pulses
- reading: A rhythmic series of strides, breaths, or agents whose dispersed expenditures accumulate into a disclosed total.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B005: belirli zaman ve bilinen aralıklarla geri gelme / عداد الوقت ومعاودته) — 
  - 100:1 w **?** (ع د و B008: iki avı peş peşe ele geçirme / العِداء في تعاقب الصيد) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 

## rising breath split
- reading: Rising, swelling breath as embodied evidence that even powerful motion depends on a sustained body and relation.
- mechanism: 
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:6 w **?** (ر ب ب B004: soluğu yükselip sıkışmak / تصعد النفس وانتفاخه) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 

## exertive panting run
- reading: The focus is already acoustic and bodily: motion is heard as strained breath.
- mechanism: The dominant ع د و running branch supplies rapid motion, while ض ب ح supplies the audible breath or mouth-sound produced by that exertion.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## boundary overrun
- reading: The runners are boundary-crossers whose speed has moral or spatial trespass built into it.
- mechanism: The same root that gives running also carries overstepping, aggression, and crossing a limit, so the motion can be read as an incursion rather than neutral speed.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:1 w **?** (ع د و B004: aşma, dışarıda bırakma ve öteye geçirme / المجاوزة والاستثناء والصرف) — 

## heat charred motion
- reading: The sound carries a latent burn-image: speed produces a scorched, darkened trace.
- mechanism: ض ب ح unexpectedly contains scorching, blackening, and ash; the panting may be the surface of heat-contact rather than only an animal sound.
- trace:
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 

## mustered counted band
- reading: The plural can also feel mustered, counted, and readied for a coming action.
- mechanism: The non-dominant mapped root ع د د allows the plural runners to be heard as a reckoned or prepared unit, not merely individual bodies in motion.
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 

## habitual returning charge
- reading: The rushing may be a recurrent, trained, returnable habit of force.
- mechanism: The non-dominant ع و د inventory recasts the action as recurrence, habituation, and return, so the run is an accustomed pattern rather than a single burst.
- trace:
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 

## spark revises breath into ignition
- reading: Panting is read as a heat-threshold: the moving bodies strike the world into sparks and scorch.
- mechanism: The next ayah supplies hidden fire brought out by striking; this makes the focus ضَبْحًا oscillate between panting and the first scorch of ignition.
- trace:
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## dawn state change incursion
- reading: The first ayah becomes the opening pressure of an event that changes a social or spatial scene at dawn.
- mechanism: Morning arrival plus alteration makes the running an event that changes a scene at the day-boundary; the focus overrun becomes a dawn incursion rather than raw speed.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## motion becomes trace cloud
- reading: The focus action becomes readable through what it leaves behind: sound, disturbed ground, and dust-mark.
- mechanism: The context turns motion into residue: stirring dislodges matter, dust rises, and the non-dominant أثر mapping makes the event legible by its remaining mark.
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## penetrating the gathered center
- reading: The runners cross limits and arrive inside a gathered center, making the first ayah the start of penetration.
- mechanism: The context supplies entry into the middle of a gathered body; this sharpens ع د و as crossing into a collective center, not merely running along a path.
- trace:
  - 100:1 w **?** (ع د و B004: aşma, dışarıda bırakma ve öteye geçirme / المجاوزة والاستثناء والصرف) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 

## moral mirror of kinetic excess
- reading: The strenuous bodies become a visible analogue for a human interior that overruns bounds, cuts relation, and is tightened by possessive love.
- mechanism: The human-Lord-ingratitude-witness cluster converts outward overrun into an interior moral pattern: breathless force mirrors a human creature cut off from benefaction and tightened by love of gain.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## excavation inverts the surface charge
- reading: Their surface disturbance prefigures a deeper reversal where buried and chest-held realities are forcibly disclosed.
- mechanism: Later uncovering reverses the opening direction: the charge disturbs surface matter, while graves and breasts are overturned so hidden contents become known and extracted.
- trace:
  - 100:1 w **?** (ع د و B009: boyunca uzanan yan ve kıyı / العَداء والعُدوة في الجانب والطوار) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 

## redress before the expert owner
- reading: The charge also becomes a movement of complaint, testimony, and exposed evidence toward an authoritative knower.
- mechanism: The focus root's rarely retained redress branch becomes live when the context introduces Lordship, witnessing, and expert knowledge; the opening charge can be evidence moving toward adjudication.
- trace:
  - 100:1 w **?** (ع د و B005: yetkiliden hakkını almasını isteme / العَدْوى في طلب الإنصاف) — 
  - 100:6 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## contagion of drive
- reading: Their excess can be read as a transmissible condition whose real site is the chest.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B006: hastalığın bulaşması / العَدْوى في انتقال الداء) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## water soft earth countercurrent
- reading: A suppressed hydrological reading coexists: the same scene may conceal water, soaking, and soft ground under the charge.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B004: kaynağı kesilmeyen kalıcı su ve su yeri / الماء العد) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 

## ancient returning road
- reading: The burst may be the latest pass along an old, habituated road of return.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B009: eski yol ve köklü geçmiş / قدم وطريق عود) — 
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## kinetic breath
- reading: The focus becomes an acoustic-kinetic event: bodies rush until their breath itself is the sworn evidence.
- mechanism: Before context, the most stable mechanism is embodied acceleration: movement is intense enough to become audible respiration, so the ayah is not static oath-labeling but a felt body in motion.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running/hastening supplies the overt kinetic body and makes the subject a moving force.
  - 100:1 **ضَبْحًا** ض ب ح B001: Audible panting supplies the sound emitted by that force and turns motion into breath.
  - 100:1 **ضَبْحًا** ض ب ح B002: Extended running confirms that the sound belongs to exertive forward drive rather than detached noise.

## boundary aggression
- reading: The runners become threshold-crossers: speed is already charged with aggression and hostile approach.
- mechanism: The same running root can be read socially and legally: haste is not neutral travel but a pressure that crosses a boundary and approaches an enemy relation.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Overstepping into injustice turns motion into boundary-violation and gives the rush an aggressive edge.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B003: Enemy/enmity supplies a social target for the rush and prevents the motion from being merely athletic.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting makes the aggressive crossing bodily and urgent rather than abstract.

## material heat shadow
- reading: Panting also opens a scorched-material register: exertion can be heard, heated, blackened, and left as residue.
- mechanism: A latent material reading sits under the audible one: panting can be accompanied by heat, blackening, or burnt residue, so the oath body has a combustion-shadow even before the later fire cue.
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B003: Scorched upper wood gives the focus sound a material heat-image that can later ignite into fire.
  - 100:1 **ضَبْحًا** ض ب ح B004: Darkening by fire or sun marks the body as visibly affected by heat, not only audibly strained.
  - 100:1 **ضَبْحًا** ض ب ح B005: Ash supplies the endpoint of the heat chain and keeps a residue-reading available.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running/hastening remains the anchoring force that could generate the heat.

## split prepared return
- reading: The motion also hovers as mustered, countable, and habitual: a prepared rush that can recur as character.
- mechanism: Without leaving the focus, the rushing plural can be felt as prepared units or a repeated habit: not a single spontaneous burst, but an already readied, countable, recurring motion.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Prepared equipment/readiness recasts the runners as mustered force rather than raw motion.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Counting supplies plurality as countable units and opens a reckoning register.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habitual return turns the rush into a repeated pattern that can diagnose settled disposition.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting keeps this prepared or repeated motion embodied in the focus.

## fire friction revises breath
- reading: The focus bodies run as frictional engines: breath, heat, and spark are one escalating mechanism.
- mechanism: The next oath unit turns the focus from mere breath into a friction system: hidden fire is brought out by striking, so rushing bodies become converters of motion into spark.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running/hastening supplies the kinetic input that can be converted into ignition.
  - 100:1 **ضَبْحًا** ض ب ح B003: Scorched material supplies the focus-side bridge from breath to heat.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Hidden fire emerging from a fire-stick supplies the latent energy that the focus motion can release.
  - 100:2 **قَدْحًا** ق د ح B001: Fire kindled by striking supplies the contact mechanism that revises panting into frictional production.

## dawn incursion boundary
- reading: The focus rush becomes threshold violence: panting pressure crosses into first light and makes aggression visible.
- mechanism: The morning incursion cue strengthens the boundary-aggression baseline: the rush now arrives at a temporal threshold where darkness changes into visibility and hostile motion becomes an intrusion.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Overstepping into injustice anchors the rush as a boundary breach.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B003: Enemy/enmity supplies the social field into which the rush enters.
  - 100:3 **فَٱلْمُغِيرَٰتِ** غ ي ر B003: Change or substitution supplies the threshold effect: the scene shifts state as the rush arrives.
  - 100:3 **صُبْحًا** ص ب ح B001: First daylight supplies the time when hidden motion becomes visible exposure.
  - 100:3 **صُبْحًا** ص ب ح B002: Morning arrival supplies the event-shape of an incursion at dawn.

## dust becomes evidence
- reading: Panting becomes the first trace in a chain of residues: sound is joined by dust, mark, and followable evidence.
- mechanism: The dust verse converts breath into environmental trace. Motion no longer vanishes as sound; it stirs a medium and leaves a visible, followable sign of passage.
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B001: Audible panting anchors the event as emitted trace from the moving body.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running/hastening supplies the force that disturbs the ground.
  - 100:4 **فَأَثَرْنَ** ث و ر B001: Rising and outward spread supplies the dust-cloud expansion caused by the rush.
  - 100:4 **فَأَثَرْنَ** ث و ر B002: Stirring a thing from its place supplies the physical displacement mechanism.
  - 100:4 **فَأَثَرْنَ** ث و ر B003: A remaining mark supplies the evidentiary side of the same disturbance.
  - 100:4 **نَقْعًا** ن ق ع B004: Raised dust supplies the visible medium in which the focus motion is preserved.

## center breach of collective
- reading: The focus rush becomes interior breach: it crosses an edge, enters the middle, and presses into a gathered collective.
- mechanism: The rush reaches not just a path but the interior of a gathered body. The focus boundary-crossing reading becomes spatially exact: it penetrates from edge to center and interrupts collective formation.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Passing beyond supplies the crossing from outside into an interior zone.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B009: Side or edge supplies the starting boundary that the rush leaves behind.
  - 100:5 **فَوَسَطْنَ** و س ط B003: Entering or making something central supplies the spatial endpoint of the rush.
  - 100:5 **جَمْعًا** ج م ع B002: An assembled group supplies the collective body that is breached.
  - 100:5 **جَمْعًا** ج م ع B013: Coming together for a purpose supplies social coordination that the rush disrupts.

## moral appetite reversal
- reading: The focus rush also images human appetite: a habitual overdrive that cuts gratitude and tightens around desired good.
- mechanism: The declarative human section does not cancel the rush; it turns the rush into a diagnostic image for human disposition. The same overdriven motion reappears as severance from the Lord, self-witness, and tight attachment to desired good.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Overstepping anchors the moral transfer from physical breach to relational breach.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habitual recurrence lets the rush become character rather than one event.
  - 100:6 **ٱلْإِنسَٰنَ** ء ن س B001: Human appearance supplies the subject to whom the oath-scene is applied.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B001: Lordship and ownership supply the violated relation against which the rush is judged.
  - 100:6 **لَكَنُودٌ** ك ن د B002: Ingratitude for favor supplies the moral name for the boundary-crossing impulse.
  - 100:7 **لَشَهِيدٌ** ش ه د B001: Presence with witnessing supplies self-implicating evidence rather than external accusation only.
  - 100:8 **لِحُبِّ** ح ب ب B002: Heart-fast love supplies the inner attachment that drives the rush.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Desired benefit supplies the object toward which the appetite runs.
  - 100:8 **لَشَدِيدٌ** ش د د B001: Binding or tightening supplies the mechanism by which love becomes hard compulsion.

## forensic uncovering reverses surface
- reading: The focus becomes a surface symptom whose full truth is revealed only when buried ground and chest-origins are turned inside out.
- mechanism: The final disclosure sequence reverses the focus scene. What began as outward rush, breath, dust, and surface force becomes the uncovering of what was buried and what issued from the chest.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Passing beyond anchors the transition from surface motion to crossing into hidden interiors.
  - 100:1 **ضَبْحًا** ض ب ح B001: Breath anchors the inner bodily register that later disclosure can expose.
  - 100:9 **يَعْلَمُ** ع ل م B001: Disclosure to knowledge supplies the cognitive endpoint of the trace.
  - 100:9 **بُعْثِرَ** ب ع ث ر B001: Turning earth and exposing what was buried supplies the ground-level reversal of the earlier dust.
  - 100:9 **ٱلْقُبُورِ** ق ب ر B002: Hiddenness and sinking supply what the earlier rush could not itself reveal.
  - 100:10 **وَحُصِّلَ** ح ص ل B002: Extracting the precious inner part from a covering supplies the interiorizing counterpart to raised dust.
  - 100:10 **ٱلصُّدُورِ** ص د ر B004: The origin from which acts issue supplies the moral source behind the rush.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inner matter supplies final inspection of the hidden motive.

## pathological breath inside
- reading: The panting can also flicker as an inner consumption made audible before it is exposed.
- mechanism: 
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting supplies the audible breath that can become symptom.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B001: A consuming lung or inward disease supplies the pathological interior shadow of breath.
  - 100:10 **ٱلصُّدُورِ** ص د ر B001: The chest as organ locates the breath-shadow inside the body.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inner matter contains the symptom as something inspected, not merely heard.

## counted prepared reckoning
- reading: The runners can also appear as prepared, counted, recurrent units whose final result will be gathered and shown.
- mechanism: 
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Prepared equipment recasts the rush as mustered and already arranged.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Counting supplies the possibility that the plural is a numbered set under reckoning.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habitual repetition makes the prepared rush recur as a settled pattern.
  - 100:2 **قَدْحًا** ق د ح B007: Lots or arrow-staves supply a risky counting device that can reframe the rush as apportioned outcome.
  - 100:5 **جَمْعًا** ج م ع B001: Gathering scattered things supplies the collecting operation for numbered units.
  - 100:10 **وَحُصِّلَ** ح ص ل B001: Showing the final result supplies the reckoning endpoint.

## ash and useless sparks
- reading: The rush can also leave a fragile residue: sparks flare, blacken, and collapse toward ash.
- mechanism: 
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B003: Scorched wood anchors the heat-reading directly in the focus.
  - 100:1 **ضَبْحًا** ض ب ح B005: Ash supplies the humbling residue left after heat and motion spend themselves.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire emerging from a stick supplies ignition for the focus's scorched underside.
  - 100:2 **قَدْحًا** ق د ح B001: Striking fire supplies the practical source of sparks.
  - 100:8 **لِحُبِّ** ح ب ب B011: Tiny useless sparks supply a diminished counterimage to the charged oath energy.

## embodied haste
- reading: A plurality whose speed is measured in forced, audible breath: motion rendered as embodied expenditure.
- mechanism: Rapid sustained running forces breath into an audible rhythm. The second term does not merely decorate speed; it converts invisible velocity into bodily evidence.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## boundary breach
- reading: An extended onrush that carries bodies across a limit, leaving the identity and justice of the breach open.
- mechanism: Extension of the running body is the means by which a limit is crossed. This produces an incipient breach model even before the context supplies a destination.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:1 w **?** (ض ب ح B002: ön bacakları uzatarak koşma / عدو ممدود الضبعين) — 

## habituated return
- reading: A rehearsed, recurrent exertion whose breath exposes acquired discipline and persistence.
- mechanism: Breath is cyclic, and practiced exertion is built from cycles. The movers may therefore be heard not as a one-off burst but as agents trained by repeated departure and return.
- trace:
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## near combustion
- reading: The exertion sits at the threshold where motion becomes heat and leaves a darkened material trace.
- mechanism: The focus-only pairing can be read as energy conversion: extreme motion approaches heat, scorching, and dark residue. The packet does not supply friction as a cause; that directional bridge is the reader's material analogy.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 

## ignition chain
- reading: Breath and scorching become the first perceptible threshold in an energy chain that culminates in emitted sparks.
- mechanism: The next paired action supplies latent fire emerging and ignition by striking. This converts the focus's near-combustion analogy into a sequence: strenuous motion and contact precede spark production. The packet supplies motion, hidden fire, and kindling; the reader supplies the arrow from the first action to the second.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## incursion topology
- reading: An edge-to-center incursion: first-light motion breaches a limit, displaces matter into a dust wake, and reaches an assembled center.
- mechanism: The packet orders transformation/raiding at morning, displacement of dust, and entry into the middle of a gathered body. That sequence gives the focus's bound-crossing a destination and geometry: edge-to-center penetration whose motion changes the surrounding medium.
- trace:
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## trace to testimony
- reading: The opening action produces testimony: breath and wake are outward marks through which concealed motive, force, or origin becomes knowable.
- mechanism: A non-dominant packet mapping turns the raised effect into a remaining trace; later branches supply witnessing signs, marks that guide knowledge, overturning concealment, extracting an interior kernel, acts issuing from the chest, and knowledge of the inside. The focus's breath can thus be revised from mere accompaniment into involuntary evidence: strenuous action writes outward signs of hidden force.
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## moral counterimage
- reading: Their breath-cost becomes morally diagnostic: either a counterimage of total responsiveness or a mirror exposing how human intensity is bound to acquisition.
- mechanism: The focus displays bodies spending force to the point of audible breath. The later human is supplied as cut off and ungrateful toward sustaining nurture, while love remains in the heart and is tightly bound to perceived benefit. The reader infers a counterimage: outward disciplined expenditure versus inward possessive attachment.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 

## hidden interior exposed
- reading: The panting is an emitted interior: hidden force becomes a witnessing sound before later interiors are fully extracted and known.
- mechanism: The packet repeatedly supplies something covered or inward that becomes perceptible: hidden fire emerges, a sign witnesses, a kernel is extracted, actions issue from the chest, and the inside is known. This strengthens a reading of ضَبْحًا as the body's involuntary exteriorization of an inner condition.
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## return and muster
- reading: Alongside that scene, the plurality can echo a recurrent return: dispersed bodies recalled, assembled, and carried toward exposure and reckoning.
- mechanism: The focus's non-dominant ع و د and ع د د mappings supply return, destination, counting, and preparedness. Context supplies assembly, uncovering graves, collecting the resultant total, and interior knowledge. Together they activate a strange but coherent reversal: the initial outward rush can echo a prepared multitude being recalled and mustered toward final exposure.
- trace:
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ع د و B002: dönüş yeri ve son varış / مصير ومرجع ومعاد) — 
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## counted ready cohort
- reading: A counted, readied cohort whose force emerges when separately prepared units synchronize into one motion.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 

## edge to basin route
- reading: The opening maps a difficult route: movement follows a bank or edge, labors over hard uneven ground, descends toward a basin, and penetrates its middle.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B009: boyunca uzanan yan ve kıyı / العَداء والعُدوة في الجانب والطوار) — 
  - 100:1 w **?** (ع د و B010: sert, kuru ve engebeli yer / العَدْواء في صلابة المكان واضطرابه) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:4 w **?** (ن ق ع B007: ince killi, verimli ve engebesiz düz arazi / نقاع الأرض القيعان السهلة) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 

## residual strength
- reading: Panting can disclose residual strength: capacity persisting through age, depletion, or repeated labor rather than effortless youthful velocity.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B008: gücü kalmış yaşlı deve / عود مسن فيه بقايا قوة) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:8 w **?** (ش د د B002: güç, katılık ve çetinlik / شدة القوة والصلابة) — 

## breath ash cycle
- reading: The sound can carry a whole expenditure arc: expelled breath, kindled heat, blackening, and finally ash—the body and matter both spending stored force.
- mechanism: 
- trace:
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 
  - 100:1 w **?** (ض ب ح B005: kül / الرماد) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## audible exertion
- reading: An oath by motion made perceptible as collective, involuntary breath under load.
- mechanism: Extended running drives breath into an audible collective pulse, so the movers are presented from inside their expenditure of force rather than by species or destination.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running and coursing supply the rapid locomotion that generates the line's bodily load.
  - 100:1 **ضَبْحًا** ض ب ح B001: The panting cry makes otherwise invisible exertion acoustically present.
  - 100:1 **ضَبْحًا** ض ب ح B002: Running with the forelimbs extended gives the sound a full-stride mechanical source.

## boundary overrun
- reading: Forceful passage over a limit, with breath sounding the violence of the crossing.
- mechanism: The run is not neutral transit: it presses past a limit, and its rough breath is the audible cost or signature of breaching that threshold.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Exceeding a limit turns speed into transgressive passage.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B009: The side or border image supplies the spatial threshold being crossed.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting renders the boundary crossing as strenuous and bodily rather than abstract.

## returning drill
- reading: A practiced, repeated sortie whose outward force carries an implicit return.
- mechanism: The plural movers enact a trained circuit: departure already contains return, and repeated exertion turns a single rush into habit, drill, or recurrent sortie.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Return after departure bends the apparent one-way run into a circuit.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habit, training, and persistence make the circuit recurrent and disciplined.
  - 100:1 **ضَبْحًا** ض ب ح B002: Full-stride running prevents recurrence from becoming a merely abstract temporal notion.

## counted cadence
- reading: A prepared serial array whose expenditure arrives in countable pulses.
- mechanism: Plural bodies become a prepared serial array, and the repeated pant becomes an audible cadence by which expenditure can be counted.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Enumeration lets the plural movers register as countable units.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Preparation of equipment turns the units into an array readied for action.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B005: Recurring time supplies cadence rather than a static inventory.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting converts the latent count into successive audible beats.

## ignition train
- reading: The panting run is the first phase of energy conversion, with motion becoming ignition and spent residue.
- mechanism: The next line's concealed fire and striking reawaken ض ب ح's burn and ash branches: locomotor effort becomes a mobile ignition train in which contact externalizes stored energy as spark and residue.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Coursing supplies the moving energy source.
  - 100:1 **ضَبْحًا** ض ب ح B003: Burning the upper ends of wood gives the focus sound a dormant combustion edge.
  - 100:1 **ضَبْحًا** ض ب ح B005: Ash supplies the spent residue of the released energy.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire emerging from a fire-stick provides stored energy becoming visible.
  - 100:2 **قَدْحًا** ق د ح B001: Striking to kindle fire supplies the contact event that releases the latent energy.

## dawn phase change
- reading: A threshold action that changes the world's phase from hidden night into exposed morning.
- mechanism: Change and dawn turn the focus's boundary crossing into a temporal phase transition: the movers do not merely traverse space but carry a scene across the edge from concealment toward visibility.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Exceeding a limit supplies the crossing action.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B009: The side or border branch spatializes the threshold that dawn temporalizes.
  - 100:3 **فَٱلْمُغِيرَٰتِ** غ ي ر B003: Changing a form or replacing one state with another supplies phase transformation.
  - 100:3 **صُبْحًا** ص ب ح B001: First daylight supplies the temporal boundary and the arrival of visibility.

## environmental wake
- reading: Their passage writes itself into the environment as dust, sound, and a followable after-trace.
- mechanism: Motion propagates beyond the movers: it raises and spreads matter, leaves a sign that can be followed, and amplifies bodily sound into an environmental wake of dust and noise.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running supplies the initiating displacement.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting begins the wake as a local acoustic emission.
  - 100:4 **فَأَثَرْنَ** ث و ر B001: A thing rising and spreading openly expands local force into the surrounding medium.
  - 100:4 **فَأَثَرْنَ** ث و ر B003: The non-dominant mapped image of a lasting sign turns disturbance into a readable trace.
  - 100:4 **نَقْعًا** ن ق ع B004: Raised dust gives the wake visible material volume.
  - 100:4 **نَقْعًا** ن ق ع B005: A raised voice scales the focus pant into a broader field of sound.

## collective penetration
- reading: Distributed bodies phase-lock into a collective ram whose convergence enables entry into a center.
- mechanism: The plural runners synchronize until their distributed motion behaves like one collected force, then convert that convergence into penetration of a center.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Coursing supplies the individual velocity to be coordinated.
  - 100:1 **ضَبْحًا** ض ب ح B002: Extended full-stride running gives the collected force bodily reach and thrust.
  - 100:5 **فَوَسَطْنَ** و س ط B003: Entering or placing in the middle supplies the penetration target.
  - 100:5 **جَمْعًا** ج م ع B010: Gathering strength or motion until its parts catch up supplies synchronization into one force.

## covenant contrast
- reading: That costly persistence becomes a relational counter-image to the human who cuts himself from nurture and covenant.
- mechanism: The shift to the visible human, nurturing or covenantal lordship, and severance refunctions the practiced exertion as a relational comparator: sustained embodied response stands beside human refusal of sustaining relation.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habit, training, and persistence supply disciplined repeated response.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting makes the cost of that embodied response impossible to idealize away.
  - 100:6 **ٱلْإِنسَٰنَ** ء ن س B001: The manifest human opposed to wildness identifies the new relational subject.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B002: Nurture, repair, and completion supply the sustaining side of the relation.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B011: Covenant and pledge sharpen nurture into reciprocal obligation.
  - 100:6 **لَكَنُودٌ** ك ن د B001: Cutting and separation supply the human rupture of relation.
  - 100:6 **لَكَنُودٌ** ك ن د B002: Ingratitude names the failed reciprocity that the exertion now measures.

## breath witness
- reading: Panting is the body's involuntary witness, making concealed expenditure evidentially audible.
- mechanism: Panting becomes indexical testimony: the body emits a sign that proves the force working through it before any verbal witness is introduced.
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B001: The panting cry is an involuntary bodily datum.
  - 100:7 **لَشَهِيدٌ** ش ه د B001: Presence with direct observation supplies the evidentiary stance.
  - 100:7 **لَشَهِيدٌ** ش ه د B008: A witnessing mark turns emitted sound into evidence of its hidden cause.

## desire charge
- reading: Their charge images how attachment to gain tightens inwardly and then spends the body outwardly.
- mechanism: Attachment to perceived benefit binds the inner subject and recruits outward force; the hard run becomes a psychomotor diagram in which desire tightens into charge.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running supplies desire's outward vector and speed.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting measures how completely the motive has recruited the body.
  - 100:8 **لِحُبِّ** ح ب ب B002: Love adhering to the heart supplies durable inner attachment.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Inclination toward perceived benefit supplies the attractive object.
  - 100:8 **لَشَدِيدٌ** ش د د B001: Tightening a knot converts attraction into binding constraint.
  - 100:8 **لَشَدِيدٌ** ش د د B003: A forceful charge or run reconnects inner binding to the focus's physical acceleration.

## return disclosure
- reading: An outward rush already shadowed by final return, reversal of the ground, and exposure of what motion seemed to leave behind.
- mechanism: The packet's return mapping for ٱلْعَادِيَاتِ is activated by overturned graves and unveiled knowledge: forward surface motion folds into a compelled return whose hidden terminus is opened.
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Return after departure reverses the apparent one-way vector.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Destination and final return enlarge the circuit from repeated sortie to ultimate terminus.
  - 100:9 **يَعْلَمُ** ع ل م B001: Disclosure to a knower supplies the epistemic result of reversal.
  - 100:9 **بُعْثِرَ** ب ع ث ر B001: Turning earth and exposing what was buried supplies the vertical reversal.
  - 100:9 **ٱلْقُبُورِ** ق ب ر B002: Concealment and depression supply the hidden terminus that the reversal opens.

## inner assay
- reading: Breath is the first exterior symptom in a trace that ultimately exposes the inward source of action.
- mechanism: The opening pant becomes the exterior layer of an evidentiary assay: bodily output reveals exertion, later extraction reaches the source from which acts issue, and inward knowledge reaches what outward traces only indicate.
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting is the outward symptom from which the assay begins.
  - 100:10 **وَحُصِّلَ** ح ص ل B002: Extracting a kernel or precious interior from its covering supplies inward analysis.
  - 100:10 **ٱلصُّدُورِ** ص د ر B004: The source from which actions issue identifies the hidden causal interior.
  - 100:11 **رَبَّهُم** ر ب ب B003: Lordly knowledge places the assay within a complete knowing relation.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inward reality completes what external symptoms only begin to disclose.

## acceleration ecology
- reading: Acceleration becomes a disturbance ecology that externalizes heat, dark residue, dust, and possible infertility.
- mechanism: 
- trace:
  - 100:1 **ضَبْحًا** ض ب ح B003: Burning upper wood supplies localized scorching inside the focus inventory.
  - 100:1 **ضَبْحًا** ض ب ح B004: Blackening supplies a visible transformation caused by spent heat.
  - 100:1 **ضَبْحًا** ض ب ح B005: Ash supplies residual matter after combustion.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire becoming external activates the focus's dormant scorching sequence.
  - 100:4 **نَقْعًا** ن ق ع B004: Raised dust carries the disturbance from contact point into atmosphere.
  - 100:6 **لَكَنُودٌ** ك ن د B003: Land that does not grow supplies a possible endpoint of repeated scorching and particulate disturbance.

## motion reckoning
- reading: Each expenditure becomes a counted entry accumulating toward a disclosed total.
- mechanism: 
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B001: Enumeration makes each mover or exertion pulse an entry.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B005: Recurring time turns separate entries into an accumulating cadence.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting makes the cadence sensorially countable.
  - 100:5 **جَمْعًا** ج م ع B001: Gathering dispersed things into one total supplies accumulation.
  - 100:10 **وَحُصِّلَ** ح ص ل B001: Collecting until the outcome appears converts accumulated pulses into a final resultant.

## contagious appetite
- reading: Breath-bearing motion images acquisitive appetite as an inward-consuming condition that propagates through vectors.
- mechanism: 
- trace:
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B006: Transmission of disease changes movement from transit into propagation.
  - 100:1 **ضَبْحًا** ض ب ح B001: Breath gives the propagation model a bodily carrier and symptom.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B001: Disease consuming the interior or lung activates a pathological reading of the pant.
  - 100:8 **لِحُبِّ** ح ب ب B002: Love adhering to the heart supplies the inward appetite that can propagate.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Inclination toward perceived benefit supplies the appetite's transmissible orientation.


# Focus 100:2

## bl ignition
- reading: The agents are defined by converting repeated contact into the appearance of a fire that was present but inaccessible.
- mechanism: Plural agents apply contact that makes a previously hidden fire emerge; the second word specifies the striking operation rather than merely adding a second fire image.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## bl disclosive score
- reading: The spark is a disclosure event produced by breaching a cover, while the scored substrate preserves evidence of the contact.
- mechanism: The strike is also a breach: it scores a covering surface, and the brief emission is evidence that something hidden lay behind it. Light and damage coexist rather than cancel one another.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 

## bl successful take
- reading: Agents make a difficult possibility take through planned probing, aid, and successful activation.
- mechanism: The physical catching of fire supports an operational analogy: deliberate probing makes an undertaking catch, and aid converts an inert possibility into effective action.
- trace:
  - 100:2 w **?** (و ر ي B003: çakmak benzetmesiyle başarma, yardım görme ya da savunma / زند يقدح نجاحا أو نصرة) — 
  - 100:2 w **?** (ق د ح B010: bir işi düşünüp nasıl yürütüleceğini tasarlamak / اقتداح الأمر بالنظر والتدبير) — 

## bl interior corrosion
- reading: A visible surface event can be the symptom of an unseen consuming process, so brightness does not guarantee health or benefit.
- mechanism: Instead of treating every emission as healthy ignition, the focus can carry a diagnostic shadow: surface scoring may disclose a process already consuming the inside.
- trace:
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:2 w **?** (ق د ح B004: ağaç ve dişte kemirilme ya da çürüme / أكال الشجر والسن) — 

## kinetic ignition
- reading: A phase transition in which strenuous locomotion is converted into contact, heat, and visible sparks.
- mechanism: The preceding running and breath-sound images turn the focus strike into energy conversion: sustained bodily motion culminates in contact that releases latent fire.
- trace:
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ض ب ح B002: ön bacakları uzatarak koşma / عدو ممدود الضبعين) — 

## iterative pulse
- reading: Counted, recurrent contacts accumulate until a latent capacity crosses the threshold into flame.
- mechanism: The non-dominant mappings of عَٰدِيَٰتِ activate counting and return. They recast قَدْحًا as an iterative pulse: many strokes recur, accumulate, and only then make hidden fire take.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 

## artificial dawn
- reading: The spark is a local threshold of visibility, an artificial dawn that begins a change of state.
- mechanism: The spark becomes a small, made dawn. Its function is not only heat but transition: it changes the visible regime by bringing a lamp-like point of light into a still-concealed field.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 

## trace and plume
- reading: The spark is the first visible index in a causal cascade that leaves a mark and launches a plume, moving from revelation back toward obscurity.
- mechanism: The strike has two residues: a scored, readable mark and an outwardly spreading plume. The bright trace briefly reveals its cause, while the stirred dust can then obscure the field.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## convergent penetration
- reading: Sparks mark the threshold at which coordinated, accumulated motion breaches an exterior and reaches the middle of a concentration.
- mechanism: Many contacts converge on a gathered body. The focus score becomes a boundary event whose flash signals successful passage from an outer edge into a concentrated middle.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 

## aid then severance
- reading: The taking of fire also models received enablement: a capacity is brought to success, then its beneficiary denies and severs the sustaining relation.
- mechanism: The fire-stick idiom of successful aid acquires a relational cost. A capacity is nurtured until it takes, but the beneficiary then cuts the relation and denies the enabling gift.
- trace:
  - 100:2 w **?** (و ر ي B003: çakmak benzetmesiyle başarma, yardım görme ya da savunma / زند يقدح نجاحا أو نصرة) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## involuntary witness
- reading: The spark is involuntary testimony: hidden contact becomes visible at once and remains legible in the mark it leaves.
- mechanism: A flash and a score jointly witness an otherwise hidden collision. The spark is involuntary testimony in real time; the mark remains after the flash as material testimony.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## sterile spark
- reading: Sparks prove activation but not value: intense, binding desire may generate display without useful fire.
- mechanism: The context distinguishes ignition from usefulness. Intense attachment can bind and drive the agent, yet produce only spectacular sparks that do not become beneficial fire.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 

## exhumed latency
- reading: The strike performs a miniature exhumation, forcing pre-existing hidden content through its cover and into knowability.
- mechanism: Striking a fire-stick becomes a miniature exhumation. A cover is breached, what was buried inside is forced out, and the emergence makes previously unavailable content knowable.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## interior assay
- reading: The spark is an assay result: external pressure makes an interior disclose its substance and causal disposition.
- mechanism: The focus strike becomes an assay. An external contact elicits a sign from within; later extraction separates inner substance from covering, identifies the source from which acts issue, and places the result under knowledge of the interior.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## lot container
- reading: As a contained material analogy, agents can also be imagined as bringing one concealed possibility out of a gathered set of lots.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 

## corrosive core
- reading: Brightness or scoring may be a symptom thrown off by a dark process consuming an interior core.
- mechanism: 
- trace:
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:2 w **?** (ق د ح B004: ağaç ve dişte kemirilme ya da çürüme / أكال الشجر والسن) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 

## tender emergence
- reading: In an ecological side-reading, activation breaks a resistant surface and brings tender latent growth into view, with barren non-emergence as its negative case.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B009: bitkinin körpe uç yaprakları / رخص أطراف النبت) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 

## hidden fire by strike
- reading: A process-image: latent force is locked inside matter and becomes visible only through impact.
- mechanism: A hidden fire is made manifest by a forceful strike; the participle names agents whose action draws latent flame out of resistant matter.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## wounding mark
- reading: The line can also show impact leaving a diagnostic wound: light appears as the surface evidence of inner harm.
- mechanism: The strike may not merely illuminate; it may score, puncture, or blemish the struck surface, making the spark a visible sign of damage.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 

## successful kindling
- reading: Spark-making becomes a figure for an undertaking made to catch: impact plus planning yields result.
- mechanism: A fire-stick that catches becomes a model for achieving an intended result; the strike is an act of considering, testing, and making an enterprise take.
- trace:
  - 100:2 w **?** (و ر ي B003: çakmak benzetmesiyle başarma, yardım görme ya da savunma / زند يقدح نجاحا أو نصرة) — 
  - 100:2 w **?** (ق د ح B010: bir işi düşünüp nasıl yürütüleceğini tasarlamak / اقتداح الأمر بالنظر والتدبير) — 

## kinetic combustion
- reading: 100:2 is the thermal consequence of the previous rushing body: breath, speed, and contact turn latent fire outward.
- mechanism: The prior rushing and panting make 100:2 less like hand-kindling and more like combustion generated by speed, breath, stretched bodies, heat, and abrasive contact.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 

## dawn raid reveal
- reading: Sparks become the first visible breach of concealment, a flash that changes night-hidden motion into exposed morning action.
- mechanism: The following morning and change/alteration cues turn the spark into a threshold-flash: not campfire stability, but a brief ignition at the moment a hidden night condition becomes morning action.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 

## dust and trace
- reading: The spark is a trace-event: impact makes matter speak, first as fire, then as dust and retained mark.
- mechanism: The next ayah turns ignition into a chain reaction: impact throws sparks, then agitation raises dust and leaves a readable trace. The focus fire is no longer only luminous; it is the first sign of matter being disturbed.
- trace:
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## penetrating center
- reading: 100:2 becomes the opening impact in a movement from edge to center, from isolated strike to penetration of a gathered body.
- mechanism: The center-and-gathering cues make the sparks read as entry-technology: impact opens a way into the middle of a collected mass rather than merely lighting its edges.
- trace:
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:5 w **?** (ج م ع B013: bir işte başkasıyla birleşip destek olma / ممالأة واجتماع مع غيرك على أمر) — 

## moral combustion
- reading: Spark-making also becomes an image for the human interior: an impact reveals ingrained ingratitude and intense love of gain.
- mechanism: The human, Lord, ingratitude, love, benefit, and intensity cues convert the focus spark into an inner moral flare: the same impact that produces light also reveals a cut bond and a hard, love-driven attachment.
- trace:
  - 100:2 w **?** (و ر ي B003: çakmak benzetmesiyle başarma, yardım görme ya da savunma / زند يقدح نجاحا أو نصرة) — 
  - 100:2 w **?** (ق د ح B003: birinin soyuna dil uzatmak / طعن في النسب) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## evidentiary flash
- reading: The spark becomes testimony: hidden material, when struck, emits evidence of what it contains.
- mechanism: Witness and inner-knowing cues make the flash evidentiary: 100:2 is a moment when hidden material gives off a sign available to testimony and divine expertise.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## resurrection interior
- reading: 100:2 becomes a miniature apocalypse of extraction: what is covered inside bodies and earth will be struck open, turned out, and known.
- mechanism: The later opening of graves and extraction from chests strongly reverses the focus image: striking fire is an early miniature of the final act in which covered interiors are broken open and their contents made known.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## qadah lots under rabb
- reading: A faint alternative imagines qadah as lots/shafts gathered under a containing رب-field, making the spark-scene brush against selection, allotment, and reckoning.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 
  - 100:11 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 

## plant tip from dust water
- reading: A weird co-reading sees the focus as emergence from hidden substrate: not only spark tips, but fresh tips from moistened earth.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B009: bitkinin körpe uç yaprakları / رخص أطراف النبت) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 

## inward decay spark
- reading: The spark is also the flash by which inner corrosion is diagnosed when the chest-cover is opened.
- mechanism: 
- trace:
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:2 w **?** (ق د ح B004: ağaç ve dişte kemirilme ya da çürüme / أكال الشجر والسن) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 

## bm impact ignition
- reading: The focus line is a compact causality scene: hidden energy becomes visible at the instant of impact.
- mechanism: The focus-only reading is a two-part ignition machine: latent fire is present but unseen, and impact makes it appear.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Concealed fire inside a fire-tool supplies the latent energy carried by word 1.
  - 100:2 **قَدْحًا** ق د ح B001: Striking fire out supplies the impact that turns latent energy into visible flash.

## bm successful initiation
- reading: The line can also signal successful launch: the action catches and becomes operational.
- mechanism: The focus roots allow ignition to mean effective activation: an intended action catches, succeeds, and begins to work.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: A fire-tool that takes successfully turns word 1 into achieved activation rather than mere light.
  - 100:2 **قَدْحًا** ق د ح B010: Considering and managing an affair lets the strike function as deliberate initiation.

## bm scored concealment
- reading: Ignition also becomes incision: the focus line can mark the first damaging opening of what was covered.
- mechanism: A second focus-only model treats the blow as a breach in a cover: what matters is not flame alone but a surface being marked open.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Covering and concealment supply the hidden layer from which the reading starts.
  - 100:2 **قَدْحًا** ق د ح B002: Scoring or flawing a thing supplies the breach that makes concealed material vulnerable.

## cd kinetic charge
- reading: 100:2 becomes the flash produced by a racing, breathing body at the point of collision.
- mechanism: The preceding motion and breath make the focus ignition bodily and kinetic: the spark is generated within a rushing sequence, not in a static tool scene.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire supplies what the rushing sequence can draw out.
  - 100:2 **قَدْحًا** ق د ح B001: Impact supplies the exact conversion from motion into flash.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Running supplies sustained acceleration as the physical condition of the strike.
  - 100:1 **ضَبْحًا** ض ب ح B001: Panting sound adds breath and strain, making the spark part of a living force-field.
  - 100:1 **ضَبْحًا** ض ب ح B003: Scorching at upper ends lets the panting line touch the focus fire through edge-burn.

## cd prepared repetition split
- reading: The spark becomes the visible tip of preparation and repeated trained impact.
- mechanism: The split mapping of the first context root keeps a non-dominant repeated/prepared-action layer alive, changing the focus from one spark into a rehearsed series of strikes.
- trace:
  - 100:2 **قَدْحًا** ق د ح B001: Striking fire out anchors the repeated-action model in the focus word.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Prepared equipment turns the motion before the focus line into readiness for impact.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: Habitual return supplies repetition, so the spark reads as practiced recurrence.

## cd dawn state change
- reading: The spark becomes a threshold signal by which a hidden force changes into a visible incursion.
- mechanism: The next line makes the focus spark a threshold event: impact changes the state of the scene as night-hidden force moves into morning exposure.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Concealment supplies the hidden side that the dawn transition can undo.
  - 100:2 **قَدْحًا** ق د ح B001: The fire-strike supplies the flashing hinge between hidden and exposed states.
  - 100:3 **فَٱلْمُغِيرَٰتِ** غ ي ر B003: Change or substitution converts the spark into an agent of altered scene-state.
  - 100:3 **فَٱلْمُغِيرَٰتِ** غ ي ر B005: Otherness and exception make the force crossing into the scene feel socially disruptive.
  - 100:3 **صُبْحًا** ص ب ح B001: First daylight supplies the reveal-frame in which the focus flash becomes legible.
  - 100:3 **صُبْحًا** ص ب ح B005: Lamp imagery echoes the focus flame and shifts it from spark to illumination.

## cd dust aftertrace
- reading: The spark becomes the first visible wound in matter, followed by trace and dust.
- mechanism: The later dust and trace cues make the focus impact productive of residue: the flash is one phase in a chain of disturbance, mark, and suspended matter.
- trace:
  - 100:2 **قَدْحًا** ق د ح B002: Scoring or flawing supplies the material contact point that can leave a trace.
  - 100:4 **فَأَثَرْنَ** ث و ر B002: Stirring something from its place extends the focus impact into displacement.
  - 100:4 **فَأَثَرْنَ** ث و ر B003: A remaining mark lets the split target read the spark as an aftertrace, not only instant light.
  - 100:4 **نَقْعًا** ن ق ع B004: Raised dust supplies the visible residue that continues after the flash.

## cd center of mass
- reading: Impact becomes a point of insertion into the center of a collective formation.
- mechanism: Entering the middle of a gathered mass turns the focus impact into a tactical point: the spark is the leading edge that opens a collective body.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: Successful kindling or aid lets the focus flash function as effective entry.
  - 100:2 **قَدْحًا** ق د ح B007: The shaft or lot image makes the focus strike feel pointed and insertive.
  - 100:5 **فَوَسَطْنَ** و س ط B003: Entering or making something middle supplies the spatial destination of the impact.
  - 100:5 **جَمْعًا** ج م ع B002: A gathered group supplies the collective body that receives the spark-like entry.
  - 100:5 **جَمْعًا** ج م ع B010: Force gathering itself intensifies the flash into concentrated momentum.

## cd backfire ingratitude
- reading: The focus spark displays force turned against relation: helped energy becomes cutting ingratitude.
- mechanism: The moral pivot makes the physical spark an analogy for relation: energy maintained by a benefactor turns into a cutting, ungrateful force against its source.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: Successful aid supplies the positive dependency that can be betrayed.
  - 100:2 **قَدْحًا** ق د ح B003: Aspersive injury turns the physical blow into relational damage.
  - 100:6 **ٱلْإِنسَٰنَ** ء ن س B001: The human category supplies the moral subject onto which the focus mechanics transfer.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B002: Nurture and completion supply the benefactor-relation that makes the backfire culpable.
  - 100:6 **لَكَنُودٌ** ك ن د B001: Cutting and separation convert the focus strike into a severed relation.
  - 100:6 **لَكَنُودٌ** ك ن د B002: Ingratitude supplies the ethical name for the severing.

## cd self witness mark
- reading: The focus flash becomes self-incriminating evidence: the blow writes a visible sign.
- mechanism: Witnessing activates the scored-concealment baseline: the strike leaves or exposes a sign, so the focus flash becomes evidence, not only event.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Concealment supplies what must be witnessed through a sign.
  - 100:2 **قَدْحًا** ق د ح B002: A score or flaw supplies the mark that can testify.
  - 100:7 **لَشَهِيدٌ** ش ه د B001: Presence with seeing makes the focus mark inspectable.
  - 100:7 **لَشَهِيدٌ** ش ه د B008: A witnessing sign turns the spark or scar into evidence of the hidden state.

## cd desire friction
- reading: The focus ignition also names an interior economy of desire: attachment tightens until it throws sparks.
- mechanism: The desire line interiorizes the ignition: love of benefit tightens, binds, and rubs until latent appetite flashes outward as action.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Hidden fire supplies the inner appetite before it appears.
  - 100:2 **قَدْحًا** ق د ح B001: Impact supplies the frictional release of that appetite.
  - 100:8 **لِحُبِّ** ح ب ب B002: Heart-bound love supplies the interior attachment that needs ignition.
  - 100:8 **لِحُبِّ** ح ب ب B004: The heart-core image localizes the hidden fire inside the person.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Useful good supplies the object toward which the spark of desire moves.
  - 100:8 **لَشَدِيدٌ** ش د د B001: Binding and tightening supply the pressure that makes desire strike.
  - 100:8 **لَشَدِيدٌ** ش د د B006: Miserly intensity turns the focus spark toward acquisitive constriction.

## cd unburial disclosure
- reading: 100:2 becomes a miniature disclosure-event: a covered interior is struck open before the full unburial scene.
- mechanism: The final disclosure scene turns focus ignition into an apocalypse of covers: what was hidden below or behind a surface is struck, overturned, and made knowable.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Covering and hiding supply the concealed condition that final disclosure reverses.
  - 100:2 **قَدْحًا** ق د ح B002: Scoring or opening supplies the initial breach in a closed surface.
  - 100:9 **يَعْلَمُ** ع ل م B001: Uncovering to the knower supplies the epistemic endpoint of the flash.
  - 100:9 **يَعْلَمُ** ع ل م B002: A distinguishing sign connects the focus spark-scar to knowledge.
  - 100:9 **بُعْثِرَ** ب ع ث ر B001: Overturning earth and exposing buried things expands the focus breach to the grave-field.
  - 100:9 **بُعْثِرَ** ب ع ث ر B003: Turning bottom to top makes the focus impact a full inversion, not a small scratch.
  - 100:9 **ٱلْقُبُورِ** ق ب ر B001: Burial supplies the covered object that answers the focus concealment branch.
  - 100:9 **ٱلْقُبُورِ** ق ب ر B002: Sunken obscurity intensifies the hiddenness that the focus strike prefigures breaching.

## cd chest extraction
- reading: The focus line also anticipates inner assay: hidden motive is struck into visibility like fire from a covered source.
- mechanism: The inward extraction line pulls the focus fire into the chest: hidden motive is treated like a kernel or result drawn from its container by an exposing strike.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire supplies the inner content before extraction.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Hiddenness supplies the cover around the inner content.
  - 100:2 **قَدْحًا** ق د ح B001: Striking fire supplies the extraction-like force that brings inner material out.
  - 100:10 **وَحُصِّلَ** ح ص ل B001: Gathering a result until it appears supplies the final outcome of disclosure.
  - 100:10 **وَحُصِّلَ** ح ص ل B002: Extracting a kernel from its cover maps directly onto the hidden-fire mechanism.
  - 100:10 **ٱلصُّدُورِ** ص د ر B001: The bodily chest supplies the inward container for the focus latent content.
  - 100:10 **ٱلصُّدُورِ** ص د ر B004: The source from which actions issue turns the spark into a disclosure of motives.

## cd expert owner
- reading: The spark reveals hiddenness for accountability before an expert owner, not because the owner lacked knowledge.
- mechanism: The closing owner/expert frame changes the focus from discovery for an observer into display before one who already knows the inner matter.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Concealment supplies what appears to need exposure.
  - 100:2 **قَدْحًا** ق د ح B001: The fire-strike supplies public manifestation rather than divine discovery.
  - 100:11 **رَبَّهُم** ر ب ب B001: Ownership and lordship supply the authority before whom the hidden spark is displayed.
  - 100:11 **رَبَّهُم** ر ب ب B002: Sustaining and completing reactivates the benefactor relation from the moral pivot.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inner matter means the focus exposure is evidentiary for judgment, not needed for information.

## internal caries
- reading: A shadow reading makes it dark and internal: hidden corruption eats until exposure.
- mechanism: 
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B001: An inward-eating ailment makes hidden fire resemble internal corrosion.
  - 100:2 **قَدْحًا** ق د ح B004: Decay in wood or teeth turns the strike into gnawing damage rather than bright flame.
  - 100:1 **ضَبْحًا** ض ب ح B004: Blackened discoloration bridges burn-mark and pathological darkening.
  - 100:10 **ٱلصُّدُورِ** ص د ر B001: The chest container keeps the inward-damage reading tied to the surah's interior turn.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inner matter contains the disease-like image as disclosure of hidden condition.

## lot and gain
- reading: The focus can faintly echo a lot-like instrument of acquisitive risk, later morally exposed.
- mechanism: 
- trace:
  - 100:2 **قَدْحًا** ق د ح B007: A shaft or lot lets the focus object become an instrument of risk and allocation.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: Successful activation supplies the hoped-for gain behind the risky instrument.
  - 100:5 **جَمْعًا** ج م ع B005: A closed hand or gathered grip makes the allocation image tactile.
  - 100:8 **لِحُبِّ** ح ب ب B002: Heart-bound love supplies the attachment that makes the risk desirable.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Useful benefit supplies the imagined prize.
  - 100:8 **لَشَدِيدٌ** ش د د B006: Miserly intensity keeps the gain-reading morally tense.
  - 100:11 **رَبَّهُم** ر ب ب B010: A container that gathers lots makes the outlier materially coherent inside the packet.

## useless tiny sparks
- reading: The focus spark can be degraded into desire's sterile glitter: bright, intense, and unprofitable.
- mechanism: 
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Hidden fire anchors the outlier in the focus ignition field.
  - 100:2 **قَدْحًا** ق د ح B001: Striking out fire anchors the flash-event.
  - 100:8 **لِحُبِّ** ح ب ب B011: A useless spark-like fire miniaturizes the grand focus ignition into sterile glitter.
  - 100:8 **لَشَدِيدٌ** ش د د B006: Miserly intensity explains why the little flash gives no generous benefit.

## ignition 01
- reading: Agents whose forceful contact converts hidden potential into a visible, active event.
- mechanism: Contact is not merely luminous description. A blow or frictional act supplies the condition under which hidden fire crosses from latency into visibility.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## mark exposure 02
- reading: A contact-event that writes a mark on a cover and makes a concealed interior legible.
- mechanism: A strike alters a covering surface by leaving a mark; that rupture can expose what the surface had kept out of sight. The focus can therefore stage disclosure through abrasion as well as ignition.
- trace:
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 

## yield aid 03
- reading: A worked source yielding aid, success, or a usable remainder.
- mechanism: The action can be modeled as productive extraction: an implement is worked until it yields a useful result. The spark is then one instance of a more abstract conversion from stored resource to obtained benefit.
- trace:
  - 100:2 w **?** (و ر ي B003: çakmak benzetmesiyle başarma, yardım görme ya da savunma / زند يقدح نجاحا أو نصرة) — 
  - 100:2 w **?** (ق د ح B005: sıvıyı elle ya da kepçeyle alma; bunun aracı, miktarı, kalıntısı ve kuyusu / غرف ما في القدر) — 

## corrosive 04
- reading: A latent consuming process becoming perceptible through the wound, darkening, or cavity it produces.
- mechanism: Instead of an instant outward spark, the focus can weakly activate a slow inward combustion analogue: hidden consumption announces itself through damage.
- trace:
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:2 w **?** (ق د ح B004: ağaç ve dişte kemirilme ya da çürüme / أكال الشجر والسن) — 

## kinetic hinge 11
- reading: The focus is the conversion hinge where sustained bodily motion becomes visible ignition and then propagating disturbance.
- mechanism: The context turns B-IGNITION-01 into a causal hinge in a motion sequence. Extended running plus audible exertion supplies energy; the focus converts repeated contact into ignition; then image-changing arrival at morning, stirred dust, and entry into a gathered body register escalating consequences. The packet supplies the stages, while I infer that the spark is the threshold linking locomotion to collective penetration.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## corrosion wake 12
- reading: The flare also exposes a consuming process whose wake can be blackening, useless sparks, barrenness, or dregs.
- mechanism: B-CORROSIVE-04 gains a full residue-chain. The packet offers disease transfer, scorched wood, blackening, ash, barren separation, useless sparks, and remainder after sorting. I infer a common direction from active consumption to a damaged or unproductive residue. The focus's flash can thus carry a shadow reading: every ignition leaves an interior or material cost.
- trace:
  - 100:1 w **?** (ع د و B006: hastalığın bulaşması / العَدْوى في انتقال الداء) — 
  - 100:1 w **?** (ض ب ح B003: üst bölümünü ateşle yakma ve ateşten etkilenme / إحراق أعالي العود) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 
  - 100:1 w **?** (ض ب ح B005: kül / الرماد) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## disclosure chain 13
- reading: Striking becomes the first legible breach in a larger process by which altered surfaces testify to buried causes and concealed interiors.
- mechanism: B-MARK-EXPOSURE-02 expands from a surface scratch into an epistemic disclosure chain. A changed image leaves a surviving sign; that sign guides recognition; buried and lowered material is overturned; an inner valuable content is extracted from its wrapper; and the origin from which action issues becomes inwardly known. The packet supplies concealment, marks, excavation, extraction, and inner knowledge; I infer that the focus's strike is the first inscription in this later unmasking process.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## benefit severance 14
- reading: A nurtured source is made to yield benefit, but attachment and withholding can sever the yield from acknowledgment of its source.
- mechanism: B-YIELD-AID-03 becomes relational rather than merely instrumental. Nurture and completion supply the source of benefit; cutting and ingratitude break the return relation; heart-bound desire, useful good, and tight withholding redirect the yielded resource toward possession; final gathering reveals the actual remainder. I infer the directional arrow 'source gives or develops → recipient extracts → recipient withholds or severs'; the packet supplies each relation but not that causal ordering.
- trace:
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 

## lot return 15
- reading: Repeated prepared casts produce a selected and witnessed result: ignition becomes procedural disclosure under reckoning.
- mechanism: The split mappings activate a procedural reading that would disappear if only dominant roots were retained. The focus قَدْحًا can be a gaming lot or bare arrow shaft, while non-dominant mappings of عَٰدِيَٰتِ supply counting/preparation and recurrence. A ر ب ب branch supplies the receptacle gathering lots; witness and identifying mark supply verification. I infer repeated drawing and return from these supplied pieces; this is a branch-network activation, not a proposed surface translation.
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B002: gelecekteki bir iş için hazırlama ve hazır bulundurma / تهيئة العدة) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 

## germinal emergence 16
- reading: Prepared contact with a receptive medium brings a tender latent life across its cover into visible emergence.
- mechanism: A dormant ecological model appears around the focus branch 'tender plant tips.' Seed, nurture/growth, soft or worked soil, unripe fruit, and the counterfactual barren ground let قَدْحًا be heard as delicate emergence rather than violent striking. The packet supplies growth materials and failure conditions; I infer that the agents of مُورِيَٰتِ bring a latent vitality across a cover into visible growth, analogically parallel to hidden fire emerging from a stick.
- trace:
  - 100:2 w **?** (ق د ح B009: bitkinin körpe uç yaprakları / رخص أطراف النبت) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:10 w **?** (ح ص ل B005: erken evredeki hurma koruğu / بلح حصل من النخلة قبل اشتداده) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## counted lots
- reading: Repeated casting from a prepared set generates an outcome that can be counted, marked, and witnessed.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 

## genealogical spark
- reading: An uttered challenge ignites a dispute over descent that extends through descendants and requires social testimony.
- mechanism: 
- trace:
  - 100:2 w **?** (و ر ي B007: torun / ولد الولد يأتي من وراء الابن) — 
  - 100:2 w **?** (ق د ح B003: birinin soyuna dil uzatmak / طعن في النسب) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:6 w **?** (ر ب ب B005: bakımla kurulan üvey aile bağı / ربيب وربيبة ورابة) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 

## tender spark
- reading: A prepared medium yields a soft, sustained emergence from latent interior to visible tip.
- mechanism: 
- trace:
  - 100:2 w **?** (ق د ح B009: bitkinin körpe uç yaprakları / رخص أطراف النبت) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 

## latent ignition
- reading: Agents repeatedly make concealed fire take through forceful contact.
- mechanism: A striker does not manufacture fire from nothing; repeated contact makes a hidden capacity take and become visible.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Hidden fire emerging from a fire-stick supplies the latent capacity and the causative act of releasing it.
  - 100:2 **قَدْحًا** ق د ح B001: Striking out fire supplies the contact operation and its visible fiery result.

## revealing score
- reading: The action scores a cover so that a concealed condition flashes into evidence.
- mechanism: Impact opens or marks a surface, and the mark makes an otherwise hidden condition legible.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Covering and withdrawal from sight supplies the concealed state that the causative form reverses.
  - 100:2 **قَدْحًا** ق د ح B002: Scoring, splitting, or flawing supplies the revealing breach and the durable mark.

## successful operation
- reading: Capable agents make an undertaking catch through aided, deliberate engagement.
- mechanism: The fire-making construction can model an operation that succeeds because counsel, aid, and decisive examination make it catch.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: A fire-stick taking as success, counsel, aid, or defense supplies achieved efficacy rather than flame alone.
  - 100:2 **قَدْحًا** ق د ح B010: Considering and planning an affair supplies the deliberate operation through which efficacy is obtained.

## kinetic friction chain
- reading: Practiced rushing is converted at contact into a flash that marks and enables a changed operational phase.
- mechanism: The focus becomes the contact-conversion hinge between sustained rushing and a changed morning state: exertion reaches impact, impact releases latent fire, and the released flash precedes the incursion.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire emerging supplies the conversion product of the surrounding motion.
  - 100:2 **قَدْحًا** ق د ح B001: Striking supplies the contact event that converts motion into sparks.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B002: Extended running supplies sustained kinetic input before the focus impact.
  - 100:1 **وَٱلْعَٰدِيَٰتِ** ع د و B004: The split mapping's habit and repetition sharpen the running into a practiced recurrent cycle.
  - 100:1 **ضَبْحًا** ض ب ح B001: Audible panting makes bodily exertion, rather than abstract motion, materially present.
  - 100:3 **فَٱلْمُغِيرَٰتِ** غ ي ر B003: Change of form or substitution frames the spark as a phase transition in the sequence.
  - 100:3 **صُبْحًا** ص ب ح B001: First daylight supplies the newly visible temporal field reached after the flash.

## ignition as cascade threshold
- reading: The sparks are an ignition threshold whose brief flash predicts displacement, obscuration, penetration, and collective concentration.
- mechanism: The spark is no longer the climax; it is the smallest visible threshold in a cascade that dislodges matter, leaves a trace, raises an obscuring medium, penetrates a center, and reconstitutes dispersed force as one body.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Emergence of hidden fire supplies the first visible threshold in the cascade.
  - 100:2 **قَدْحًا** ق د ح B001: The strike supplies the initiating impulse.
  - 100:4 **فَأَثَرْنَ** ث و ر B002: Moving a thing from its place extends ignition into material displacement.
  - 100:4 **فَأَثَرْنَ** ث و ر B003: The split mapping's remaining trace turns the brief spark into a readable sign of what passed.
  - 100:4 **نَقْعًا** ن ق ع B004: Raised dust supplies the expanding medium produced after the initial contact.
  - 100:5 **فَوَسَطْنَ** و س ط B003: Entry into the middle supplies directed penetration rather than diffuse commotion.
  - 100:5 **جَمْعًا** ج م ع B010: Parts gathering their strength supplies the coherent collective force reached by the sequence.

## aid becomes witness
- reading: Successful ignition is borrowed capacity whose visible use can testify either to received aid or to severance from its source.
- mechanism: The focus's success-and-aid branch becomes morally reversible: nurtured capacity catches and succeeds, but its use can cut itself from its source, so the visible result becomes a sign testifying to the beneficiary's relation to the giver.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B003: The fire-stick that takes through aid or counsel supplies enabled success.
  - 100:2 **قَدْحًا** ق د ح B010: Planning an affair supplies intentional use of the enabled capacity.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B002: Nurturing, repairing, and completing supplies the prior enabling relation.
  - 100:6 **لَكَنُودٌ** ك ن د B001: Cutting and separation supply the beneficiary's reversal away from that relation.
  - 100:6 **لَكَنُودٌ** ك ن د B002: Ingratitude for favor identifies the social-moral failure enacted by the cut.
  - 100:7 **لَشَهِيدٌ** ش ه د B008: A witnessing sign turns outwardly successful action into evidence of its source-relation.

## futile acquisitive sparks
- reading: Spark production can also image desire-driven expenditure that flashes intensely yet withholds useful fire.
- mechanism: A second fire valuation appears: not every spark becomes useful flame. Desire bound tightly around supposed good can generate brilliant but sterile emissions, activity that flashes without yielding benefit.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Emergent sparks supply the visible energetic output whose value is now questioned.
  - 100:2 **قَدْحًا** ق د ح B001: Repeated striking supplies effort capable of producing flash without durable utility.
  - 100:8 **لِحُبِّ** ح ب ب B011: Sparks from a small fire that give no benefit directly supplies the sterile-flash counterimage.
  - 100:8 **ٱلْخَيْرِ** خ ي ر B001: Inclination toward beneficial good supplies the utility criterion the sparks may fail.
  - 100:8 **لَشَدِيدٌ** ش د د B001: A tightened knot supplies desire's constriction around its object.
  - 100:8 **لَشَدِيدٌ** ش د د B006: Severe withholding supplies the social form of energetic acquisition without beneficial release.

## strike as disclosure protocol
- reading: The strike is a miniature disclosure technology: breach, overturn, extract, and render a hidden source evidentially visible.
- mechanism: The focus compresses a disclosure protocol: a covered interior is struck or probed, the cover is overturned, the hidden core or residue is extracted, and the resulting mark becomes knowable as evidence of the source from which actions issue.
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B005: Covering something out of sight supplies the concealed initial state that مُورِيَات reverses.
  - 100:2 **قَدْحًا** ق د ح B002: Scoring or splitting supplies the invasive opening that makes the interior legible.
  - 100:2 **قَدْحًا** ق د ح B005: Drawing difficult residue from a vessel or well supplies extraction after opening.
  - 100:9 **يَعْلَمُ** ع ل م B001: Disclosure of a thing to a knower supplies the endpoint of the protocol.
  - 100:9 **بُعْثِرَ** ب ع ث ر B001: Turning soil and uncovering what is buried supplies forceful reversal of the cover.
  - 100:9 **ٱلْقُبُورِ** ق ب ر B002: Obscurity and depression supply the deeply concealed condition acted upon.
  - 100:10 **وَحُصِّلَ** ح ص ل B002: Extracting a kernel or precious content from its casing supplies selective recovery of the interior.
  - 100:10 **ٱلصُّدُورِ** ص د ر B004: The source from which actions issue locates the concealed interior as behavior's origin.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B001: Knowledge of inward reality confirms that disclosure reaches beneath reportable surface appearance.

## lot and accounting
- reading: It can faintly echo a cast lot whose hidden import flashes forth within a witnessed accounting.
- mechanism: The rare lot branch of قَدْح and the lordship branch of a holder gathering lots activate a juridical-divinatory overlay: one cast piece is gathered into an accountable outcome whose significance is witnessed and disclosed.
- trace:
  - 100:2 **قَدْحًا** ق د ح B007: The arrow-shaft or gaming lot supplies a cast token whose outcome awaits reading.
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: A hidden result flashing into visibility supplies the lot's moment of manifestation.
  - 100:6 **لِرَبِّهِۦ** ر ب ب B010: A holder that gathers lots supplies the container and ordering frame for multiple tokens.
  - 100:7 **لَشَهِيدٌ** ش ه د B002: Declaration grounded in knowledge supplies witnessed interpretation of the manifest result.
  - 100:9 **يَعْلَمُ** ع ل م B001: A thing becoming disclosed to a knower supplies epistemic resolution.
  - 100:10 **وَحُصِّلَ** ح ص ل B001: Gathering until the resultant total appears supplies accounting rather than isolated chance.

## tender emergence ecology
- reading: The agents elicit tender life from a resistant substrate, with emergence valued by whether it matures and reproduces.
- mechanism: 
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B002: Latent fire brought forth supplies a generalized emergence-from-hiddenness mechanism.
  - 100:2 **قَدْحًا** ق د ح B009: Tender tips and fresh soft leaves supply the fragile emergent object.
  - 100:6 **لَكَنُودٌ** ك ن د B003: Land that does not grow supplies the resistant substrate from which emergence is uncertain.
  - 100:8 **لِحُبِّ** ح ب ب B001: A seed that grows and bears seed supplies reproductive continuity after emergence.
  - 100:10 **وَحُصِّلَ** ح ص ل B005: Dates formed before becoming firm supply an immature later stage of the tender tip.
  - 100:11 **لَّخَبِيرٌۢ** خ ب ر B003: Cultivating and repairing land supplies the enabling practice that links substrate to growth.

## internal corrosion probe
- reading: At the exploratory edge, it images invasive contact exposing a slow inward corrosion through the defect and residue it leaves.
- mechanism: 
- trace:
  - 100:2 **فَٱلْمُورِيَٰتِ** و ر ي B001: Illness eating the belly or lung supplies concealed internal consumption and the possibility of a probing wound.
  - 100:2 **قَدْحًا** ق د ح B004: Decay eating wood or teeth supplies slow corrosion that produces an outwardly discoverable defect.
  - 100:10 **وَحُصِّلَ** ح ص ل B003: Residue left after lifting or separation supplies diagnostic remainder.
  - 100:10 **ٱلصُّدُورِ** ص د ر B001: The bodily chest supplies the interior site in which the corrosive image is localized.


# Focus 100:3

## dawn incursion
- reading: A dawn-incursion collective identified by its power to alter the configuration it enters.
- mechanism: A collective arrives at the vulnerable opening of day and changes an already arranged situation. Dawn is both timing and tactical threshold; alteration is the event's functional result.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## threshold illumination
- reading: The incursion itself is a dawn-like conversion from concealment to a newly visible condition.
- mechanism: The phrase can stage a phase transition: an obscured state is replaced by a lit, manifest one. Morning is not merely when the agents act; its opening and lamp imagery specify what their changing achieves.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 
  - 100:3 w **?** (ص ب ح B010: bir duruma gelmek / أصبح بمعنى صار) — 

## morning provision repair
- reading: Dawn actors arrive with water, provision, or repair and change a depleted field into a sustained one.
- mechanism: Instead of hostile entrants, the feminine plural can be carried experimentally as morning bringers whose arrival changes lack into supply or disrepair into fitness. The model is branch-distant from the raid reading but has a two-root functional circuit: arrive, water or provision, and thereby alter.
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B002: günün başında gelmek / الإتيان صباحا) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 

## alarm protection
- reading: The plural may instead be responders changed into protective motion by a dawn alarm.
- mechanism: An alarm at dawn mobilizes a protective collective. On this reading, the change is a rapid switch from ordinary repose to guarding those within a threatened boundary.
- trace:
  - 100:3 w **?** (غ ي ر B004: eşini veya ailesini kıskanarak koruma duygusu / الغَيْرة على الأهل) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## running boundary
- reading: The culminating threshold-crossing phase of an embodied, accelerating collective whose breath already makes its approach perceptible.
- mechanism: Running supplies locomotion; extended exertion and audible breath make it bodily; limit-crossing gives that motion a threshold. These packet elements strengthen the focus incursion model, while the reader infers that crossing a spatial limit at the opening of day is what permits the focus collective to alter a settled arrangement.
- trace:
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ض ب ح B002: ön bacakları uzatarak koşma / عدو ممدود الضبعين) — 

## latent ignition
- reading: Activators strike a threshold where concealed energy becomes visible, making the dawn incursion a phase conversion as well as a spatial entry.
- mechanism: The packet supplies fire hidden in a striker and the act that successfully elicits it. The reader maps that material conversion onto the focus roots: مُغِيرَٰتِ becomes an activating collective, and صُبْحًا becomes the visible phase reached when concealed potential is released.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## trace and dust
- reading: Its alteration writes a temporary archive into the environment: displaced matter both manifests the event and testifies that it occurred.
- mechanism: The dominant mapping supplies matter stirred up and spread; the non-dominant mapping supplies a surviving mark that indicates a prior event; dust supplies the visible medium. The focus collective therefore changes a scene twice: causally by displacing matter and epistemically by leaving an aftermath through which its passage can be read.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## center reconfiguration
- reading: It reaches the organizing middle of a gathered body and changes that body from the inside.
- mechanism: Entering or making a middle supplies a trajectory; a gathered plurality supplies the target topology. The reader infers that reaching the center interrupts the relations that made the aggregate one body, so the focus change is not generic damage but reconfiguration from within.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## repair vs severance
- reading: Its repair becomes a relational counter-image: received nurture is carried forward into exertion and benefit, whereas the human cuts himself off from the source of nurture.
- mechanism: The focus provision/repair model meets a nurturer who repairs and brings to completion, a non-dominant nourishment-and-growth image, and a human condition named by cutting off and ingratitude. The packet supplies both poles; the reader infers an antithesis: morning agents sustain a circuit of received care, while the human severs that circuit despite being able to perceive it.
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## self witnessing dawn
- reading: Dawn converts their effects into witnessing signs; the changed scene itself makes the event present.
- mechanism: Presence-with-seeing and a sign that bears witness connect to the focus's dawn opening and lamp. The reader infers that morning is when the changed scene becomes self-evidencing: the event is present through its visible effects, not only through an external report.
- trace:
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## desire as drive
- reading: It can also diagram desire in motion: an inwardly knotted attachment accelerates outward toward what it treats as beneficial.
- mechanism: Love lodged in the heart supplies attachment; beneficial good supplies the attractive object; knotting supplies binding; the charge or run supplies outward force. The reader infers a drive train from inward fixation to outward incursion, so the focus motion can mirror rather than merely precede the later human condition.
- trace:
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 

## exhumation second dawn
- reading: It prefigures a second dawn-like operation: coverings are overturned, hidden contents become signs, and obscurity changes into unavoidable knowledge.
- mechanism: Knowledge supplies disclosure, burial supplies concealment and downwardness, and overturning soil supplies the operation that exposes what was hidden. These cues revise the focus threshold model: dawn becomes an epistemic exhumation, a forced change from covered and low to manifest and knowable.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## inside out reversal
- reading: Their inward vector is later reversed: what was gathered and covered in the human center is changed into an outwardly manifest result.
- mechanism: Extraction of a core from its covering combines with the chest as the source from which actions issue. The reader reverses the earlier vector: the focus collective enters a gathered center, but this later operation makes an interior center issue outward. The common focus anchor is change of configuration; the direction can coexist in both senses.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## manifestation not information
- reading: Morning models manifestation inside an already comprehensively known field: hidden reality changes status for the scene and its participants, not for the expert knower.
- mechanism: Lordship supplies encompassing governance, while expertise supplies knowledge of report and inner reality. The reader infers that the dawn-to-disclosure sequence does not inform an ignorant knower; it changes what is hidden into what is manifest within an already known field.
- trace:
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## compensation after alarm
- reading: The raid/alarm can initiate a second kind of change: injury passes through redress, mediation, testimony, and covenant into compensation substituted for retaliation.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B002: cana karşılık ceza yerine kabul edilen kan bedeli / الغَيْر في الدية) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 
  - 100:1 w **?** (ع د و B005: yetkiliden hakkını almasını isteme / العَدْوى في طلب الإنصاف) — 
  - 100:5 w **?** (و س ط B005: insanlar arasında aracılık etme / الوساطة بين الناس) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:11 w **?** (ر ب ب B011: bağlayıcı söz ve güvence / ربابة عهد وميثاق) — 

## chromatic combustion
- reading: Its frictional passage can be imagined as manufacturing dawn materially: blackness, ash, latent fire, and striking turn into red-bright morning.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B006: kızılımsı parlak güzellik / الصُّبْحة والصباحة) — 
  - 100:1 w **?** (ض ب ح B004: siyaha doğru kararma / تغير اللون إلى السواد) — 
  - 100:1 w **?** (ض ب ح B005: kül / الرماد) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## return after departure
- reading: Its dawn-change can carry a remote return topology: departure, concealment, and renewed emergence culminate in a transformed coming-back.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B010: bir duruma gelmek / أصبح بمعنى صار) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ع د و B002: dönüş yeri ve son varış / مصير ومرجع ومعاد) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 

## hydrological repair
- reading: A coexisting branch reads the collective as morning water-bringers whose passage changes dry or disordered land into a nurtured, productive field.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 
  - 100:4 w **?** (ن ق ع B002: susuzluğu giderme; içe sindirip rahatlama / ماء ينقع الغلة ويروي) — 
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## focus raid as state change at dawn
- reading: Dawn is the moment when active agents convert a prior state into another state through incursion.
- mechanism: The participial plural supplies agents; غ ي ر supplies alteration/substitution, while ص ب ح supplies the morning-raid alarm. Focus-only, the line reads as agents whose arrival at dawn changes a situation.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## focus otherness threshold
- reading: Morning is itself the hinge of alterity: the agents enact the world's becoming otherwise.
- mechanism: The focus can be heard less as battle and more as transition: morning makes night other than itself, and the agents belong to that boundary-change.
- trace:
  - 100:3 w **?** (غ ي ر B005: başka olma, dışta bırakma veya olumsuzlama / السوى والخلاف والاستثناء والنفي) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## focus provisioning morning
- reading: A weaker but anchored baseline sees morning agents that alter a condition by provisioning or watering.
- mechanism: A branch-distant focus-only reading joins غ ي ر's provision/repair/watering with ص ب ح's morning drink or watering. The participle can then carry morning arrival that changes need into supply.
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 

## breath runners strengthen raid
- reading: It becomes the arrival-point of a moving, breathing force already under acceleration.
- mechanism: The preceding line supplies running bodies and audible exertion. That changes 100:3 from abstract alteration at dawn into the third step of a kinetic sequence: running, panting, then dawn-incursion.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## spark reframes dawn as ignition
- reading: Morning is what the sequence ignites: a hidden force becomes light and thereby changes the scene.
- mechanism: The spark roots before the focus make morning less a neutral clock-time and more a flare: hidden fire is struck out, then the focus appears at dawn as an event that changes visibility.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## dust and trace retroactivate effects
- reading: The focus is an unseen cause whose reality is inferred from stirred matter and lasting trace.
- mechanism: The following dust line sends evidence backward into the focus. 100:3 is no longer only the moment of entry; it becomes the cause whose effects rise, spread, and remain legible as dust and trace.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## center of gathering spatializes change
- reading: Change is a spatial reconfiguration: agents cross from edge to center inside a gathered body.
- mechanism: The center/gathering line spatializes the focus. The dawn agents do not simply appear; they alter the configuration by entering the middle of a collected mass.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## human ingratitude internalizes the raid
- reading: The focus also becomes a figure for the human who converts nurture into estrangement and cuts the bond of gratitude.
- mechanism: The moral pivot activates a changed reading in which external dawn-change becomes an internal relational change: the human cuts or alters the bond to the Lord who owns, repairs, and nurtures.
- trace:
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:3 w **?** (غ ي ر B005: başka olma, dışta bırakma veya olumsuzlama / السوى والخلاف والاستثناء والنفي) — 

## witness makes dawn evidentiary
- reading: Dawn makes the event testify: visibility becomes evidence against or about the subject.
- mechanism: The witness cue turns the light of morning into proof. The focus event is not only seen; it makes something testify by presence, mark, and disclosure.
- trace:
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## desire for good reopens provision branch
- reading: It becomes a motivated rush toward benefit: provision, goods, and possessive intensity are latent in the dawn motion.
- mechanism: The love-of-good line reactivates the focus root's provision branch. The dawn incursion can now be read as energy drawn toward benefit, goods, or possessive acquisition, not only toward combat.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 

## excavation recasts dawn as disclosure
- reading: It is also an image of disclosure: hidden matter is forced out into morning-like knowability.
- mechanism: The later scene of graves overturned and breasts extracted sends a larger disclosure pattern back to 100:3. The dawn incursion becomes a small-scale rehearsal of hidden things forced into the open.
- trace:
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## expert repair soft earth revives non martial focus
- reading: A live secondary reading sees morning change as expert repair, watering, and cultivation under the Lord's knowledge.
- mechanism: The final Lord/expert cue unexpectedly reopens the focus-only provisioning model: ربّ supplies repair and nurturing, while خبير's non-dominant earth images supply soft/wet land and cultivation. That makes the morning change look like expert care of terrain, not only assault.
- trace:
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 

## provisioning watering not raid only
- reading: They may also be morning providers/repairers whose change is benefit, watering, and cultivated restoration.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## legal substitution and mediation
- reading: A strange legal echo makes the dawn-change a substitutionary event: violence and grievance are converted toward compensation or mediation.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B002: cana karşılık ceza yerine kabul edilen kan bedeli / الغَيْر في الدية) — 
  - 100:1 w **?** (ع د و B005: yetkiliden hakkını almasını isteme / العَدْوى في طلب الإنصاف) — 
  - 100:5 w **?** (و س ط B005: insanlar arasında aracılık etme / الوساطة بين الناس) — 
  - 100:2 w **?** (ق د ح B002: çentik açmak ve oluşan kusur / نقر الشيء وعيبه) — 

## non dominant athar trace reading
- reading: It can be read indirectly: dawn reveals traces by which the change is known after the event.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ث و ر B004: izinden giderek takip etmek / السير على إثر سابق) — 
  - 100:3 w **?** (ص ب ح B005: ışık veren lamba / المصباح والسراج) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## dawn incursion
- reading: Coordinated dawn-incursors whose arrival abruptly changes the state of what they enter.
- mechanism: The agents make a sudden incursive alteration at the conventional time of a morning raid: motion is encoded as an event that changes the condition of a place or group, not merely as travel.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## threshold transformation
- reading: Agents of a threshold event: as morning becomes, they make another state become.
- mechanism: Dawn is read as a threshold and the plural agents as operators of transition: their action and the world's passage into morning are superposed, so temporal change becomes causal change.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (ص ب ح B010: bir duruma gelmek / أصبح بمعنى صار) — 

## morning arrival
- reading: A coordinated first-light arrival recognized by the change it effects.
- mechanism: The line foregrounds timed arrival: a group reaches its object at first light, with the change-root making arrival consequential rather than merely locative.
- trace:
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B002: günün başında gelmek / الإتيان صباحا) — 

## provisioning counterreading
- reading: Morning agents who alter conditions through provision, watering, and repair.
- mechanism: A formally available but context-free counter-reading treats the plural as morning providers or repairers: they arrive with sustenance, water, or restored travel equipment and thereby improve a household, land, or company.
- trace:
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:3 w **?** (ص ب ح B003: günün başındaki içecek ve içme / الصبوح) — 

## breath driven charge
- reading: A breath-driven high-speed charge culminating in a dawn incursion.
- mechanism: The preceding running and audible breath give the dawn incursion a bodily engine: sustained exertion precedes and enables the state-changing arrival.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## ignition at threshold
- reading: Impact-activated agents make the dawn threshold flare into a changed field of action.
- mechanism: Latent fire drawn out by striking becomes an analogue for the focus event: the agents do not merely arrive when light exists; their impact appears to ignite the transition into visibility and action.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## dust counterdawn
- reading: The incursion changes dawn itself into a counter-dawn, raising a veil just as light should disclose.
- mechanism: The incursion changes dawn in a paradoxical direction: motion raises and spreads dust, so the time of increasing visibility becomes a scene of self-produced obscurity.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## center penetration
- reading: Agents breach a collected body's center at dawn and alter it from the inside.
- mechanism: The changed state gains exact spatial topology: the agents pass from exterior approach to the middle of a collected body, converting arrival into penetration and disruption from within.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## benefaction ingratitude tension
- reading: A weakened literal reading but a live moral foil: provision and repair expose the recipient's severing ingratitude.
- mechanism: The provision/repair baseline survives as a moral counter-current but is weakened as the literal event model: nurturing completion is answered by severance and ingratitude, making beneficial change less likely as the immediate action yet more resonant as what the human relation fails to reciprocate.
- trace:
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 

## desire mobilized
- reading: An outward change-event that can betray how inward attachment to valued good becomes mobilized force.
- mechanism: The external dawn charge becomes a legible enactment of an inward attachment: abiding love of valued good tightens into force and then writes a visible sign in the altered world.
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## dawn as exhumation
- reading: A local hidden-to-exposed reversal that can prefigure the later overturning of buried contents into knowledge.
- mechanism: The dawn threshold becomes a small-scale analogue of forced disclosure: as buried contents are overturned into knowledge, the incursive morning changes hiddenness into exposure.
- trace:
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## outer charge inner extraction
- reading: The visible charge is only the outer layer of a change-event whose action-producing interior will be extracted and known.
- mechanism: The focus event acquires an inward counterpart: external agents force a changed field at dawn, while later collection extracts the valuable core from the action-producing interior and makes its hidden condition fully known.
- trace:
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## recurrent drill
- reading: A trained, habitual cycle of morning interventions, each repetition producing change.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:3 w **?** (ص ب ح B009: gün başı zaman kalıbı / ظروف الصباح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## compensatory raid
- reading: A dawn mobilization inside a contested logic of redress, retaliation, and compensatory substitution.
- mechanism: 
- trace:
  - 100:3 w **?** (غ ي ر B002: cana karşılık ceza yerine kabul edilen kan bedeli / الغَيْر في الدية) — 
  - 100:1 w **?** (ع د و B005: yetkiliden hakkını almasını isteme / العَدْوى في طلب الإنصاف) — 
  - 100:3 w **?** (ص ب ح B004: günün başında baskın / يوم الصباح) — 

## trace makes event
- reading: The incursion becomes an event by leaving a changed, witness-bearing trace after the agents pass.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 

## morning stasis breached
- reading: The active dawn agents are legible against a latent morning stasis that their arrival abruptly breaks.
- mechanism: 
- trace:
  - 100:3 w **?** (ص ب ح B008: gün doğana dek çöken deve / الناقة المصباح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) —


# Focus 100:4

## hft1004 b01 dislodged plume
- reading: Their passage or impact dislodges settled ground into a raised dust plume; the ayah profiles a compact cause-to-material-result event.
- mechanism: The plural agents disturb material from a settled position and thereby make dust rise. The packet supplies stirring and raised dust; I supply the causal arrow from their motion through the referent of بِهِۦ to a visible plume.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## hft1004 b02 burst into visibility
- reading: The ayah foregrounds a sudden visibility event: latent ground becomes an outward-spreading atmospheric body.
- mechanism: The event is not only displacement but emergence: something previously low, still, or latent bursts outward until it becomes visibly distributed as dust. The shift from concealment or stillness to spread is packet-supplied; treating the dust as that emerging matter is my synthesis.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## hft1004 b03 transient index
- reading: Dust writes their passage into the air: a temporary trace that indicates an event beyond what is directly visible.
- mechanism: On the non-dominant mapped root, the dust is not merely what motion makes but a remaining sign that points back to motion already occurring. The packet supplies the sign and dust images; I infer that a plume can function as an index of movers even when they are partly unseen.
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## hft1004 b04 settling reversed
- reading: The ayah can be carried as a reversal of settlement: gathered matter is forced out of rest and into suspension.
- mechanism: One focus root activates dislodging while the other activates water or material that gathers and remains. Their juxtaposition supports a reversible-medium model: force interrupts settlement and turns a low, gathered state into suspension. This reversal is inferred, not stated.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 

## hft1004 b05 acoustic surge
- reading: A coexisting reading hears the event as a rising, sustained din generated by the charge.
- mechanism: The two focus roots can couple a surge into confrontation with a raised, sustained cry. This produces an audible rather than particulate reading: the agents cause a swelling din through the same event. The morphology does not force this branch pairing, so it remains coexistent and exploratory.
- trace:
  - 100:4 w **?** (ث و ر B003: saldırgan biçimde kabarıp karşı koyma / هيجان إلى مواجهة أو غضب) — 
  - 100:4 w **?** (ن ق ع B005: yüksek sesle bağırma ve sesi sürdürme / نقع الصوت المرتفع) — 

## hft1004 d01 rhythmic kinetic engine
- reading: Audibly exerting runners operate as a rhythmic kinetic engine whose repeated impacts build and sustain the plume.
- mechanism: Running and audible exertion turn the baseline disturbance into a repeated-contact engine. The packet supplies running and breath-sound; I infer rhythmic impacts that cumulatively dislodge ground and sustain the plume.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## hft1004 d02 ignition and self veiling
- reading: The dust is the second half of a reveal/conceal machine: impact exposes latent fire, then movement raises a screen that can hide its own agents.
- mechanism: The sequence first releases hidden fire by striking and then releases hidden ground as dust. A second accepted branch of the fire root introduces covering, allowing a reversal: one impact makes light while its continuing motion makes a veil. The reveal-then-conceal arrow is my inference.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 

## hft1004 d03 dawn visibility threshold
- reading: Dust is also an optical state change: at first light it redraws boundaries, reveals motion, and simultaneously reduces visual access.
- mechanism: Morning supplies a visibility threshold, while change supplies transformation of appearance. The plume therefore changes from generic material residue into an optical event that redraws the scene precisely as light begins to disclose it.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## hft1004 d04 dispersal penetrates gathering
- reading: The plume belongs to an inverse geometry: matter disperses outward as the agents drive inward, potentially carrying their own obscuring envelope into a gathered center.
- mechanism: The sequence opposes two organizations of matter: ground is dispersed upward as dust while the agents move inward toward the center of a gathered body. The repeated بِهِۦ permits, but does not require, the further inference that the plume accompanies or enables penetration as an envelope.
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## hft1004 d05 barren yield
- reading: The ground's dry yield becomes a live material analogue for failed reciprocity: what has been sustained or tended returns barrenness and dust rather than fruit.
- mechanism: The discourse's human pivot activates a material analogy: ground that has the capacity to be tended or completed yields only dust under force, like barren land that does not grow and a human who cuts off acknowledgement of received good. The packet supplies cultivation, barrenness, ingratitude, and clay-flat images; the mapping from terrain to reciprocity is mine.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B007: ince killi, verimli ve engebesiz düz arazi / نقاع الأرض القيعان السهلة) — 
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## hft1004 d06 self witnessing trace
- reading: The plume is self-incriminating testimony: the act manufactures a present mark that bears witness to the force and direction that made it.
- mechanism: Witnessing changes the non-dominant trace baseline from a mere residue into testimony. The dust is a mark present with the event and capable of indicating what produced it, even if the clause's witness referent remains unresolved.
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 

## hft1004 d07 appropriation wake
- reading: The plume can also record motive: an outward wake generated by inward attachment that drives toward exclusive possession.
- mechanism: The non-dominant focus mapping carries exclusive possession as well as residual trace. Later heart-bound love of beneficial good under the image of tight or miserly intensity activates the dust as the visible wake of acquisitive drive. This does not replace the physical plume; it gives that plume a social-affective motor.
- trace:
  - 100:4 w **?** (ث و ر B006: başkalarını dışlayarak kendine ayırmak / استبداد المرء بالشيء لنفسه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## hft1004 d08 unquenched dryness
- reading: Naqʿ becomes a material paradox of appetite: the root can promise quenching, yet the driven action produces only airborne dryness and therefore no settled satisfaction.
- mechanism: The focus noun contains a live opposition between water that settles thirst and raised dry dust. Later love, fullness, benefit, and intensity turn that opposition into an appetite model: forceful pursuit produces a dry naqʿ that cannot perform the root's quenching possibility. The non-quenching arrow is inferred.
- trace:
  - 100:4 w **?** (ن ق ع B002: susuzluğu giderme; içe sindirip rahatlama / ماء ينقع الغلة ويروي) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:8 w **?** (ح ب ب B006: suyla dolmak veya doldurup dolulaştırmak / الري حتى الامتلاء) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B002: güç, katılık ve çetinlik / شدة القوة والصلابة) — 

## hft1004 d09 micro exhumation
- reading: Surface disturbance becomes a small-scale rehearsal of ground reversal: what normally covers is made to rise, anticipating soil that yields what it concealed.
- mechanism: Later overturning of soil and uncovering what is buried scales up the focus disturbance. The raised dust becomes a small, present rehearsal of a larger inversion in which ground no longer contains what it covered. The scale and anticipatory relation are reader-supplied.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 

## hft1004 d10 forensic guidance
- reading: Dust does both: it blocks direct sight while functioning as a forensic guide to the hidden event.
- mechanism: Knowledge as a distinguishing mark sharpens the focus's trace branch. Dust can obscure direct sight while still guiding an observer toward the action that made it; hiddenness and evidence therefore coexist rather than cancel each other.
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## hft1004 d11 surface sifting interior
- reading: The plume becomes the lifted residue of a rough sifting process, contrasted with the later exact extraction of the inward source and its consequential core.
- mechanism: Later extraction of a core from its covering and identification of the source from which acts issue recast the focus disturbance as a crude sifting operation. Dust is the lifted residue of disturbed surface matter; the later operation extracts and gathers what is inwardly consequential. The residue/core alignment is inferred.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## hft1004 d12 veil does not block knowing
- reading: Dust is an observer-relative veil, not erasure: it blocks direct sight, leaves evidence, and does not obstruct knowledge of the agents' inward reality.
- mechanism: The final knowledge-of-interiors cue changes the plume's concealment function from absolute hiding to observer-relative veiling. Dust can block human sight yet remain a trace, while sovereign inner knowledge is not occluded by the medium. The epistemic asymmetry is inferred from the branch pairing and repeated prepositional relation.
- trace:
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## hft1004 o01 audible plume
- reading: They also raise an audible plume: exertion and confrontation swell into a sustained din that occupies space like dust.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B003: saldırgan biçimde kabarıp karşı koyma / هيجان إلى مواجهة أو غضب) — 
  - 100:4 w **?** (ن ق ع B005: yüksek sesle bağırma ve sesi sürdürme / نقع الصوت المرتفع) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## hft1004 o02 sterile spark economy
- reading: Their brilliance can coexist with sterility: intense motion spends itself into sparks and dust while the question of actual benefit remains open.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 

## hft1004 o03 released hazard
- reading: Disturbance may be carried as release of a settled hazard: the cloud is dangerous because force has mobilized what was fixed.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B006: dişlerde toplanıp kalmış zehir; kalıcı ölüm ve öldürme / سم ناقع ثابت أو قاتل) — 

## hft1004 o04 terrain assay
- reading: The plume can be read as a substrate assay: impact reveals whether the traversed ground is dry and barren, clayey and basin-like, or soft with retained water.
- mechanism: 
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B007: ince killi, verimli ve engebesiz düz arazi / نقاع الأرض القيعان السهلة) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) —


# Focus 100:5

## bl penetrated collective center
- reading: The movers penetrate from the collective's edge into its interior center; جَمْعًا is a spatially organized body, not just nearby people.
- mechanism: The verbal middle-branch supplies ingress rather than static centrality, while the group-branch supplies an assembled body. Together they form a topological event: plural movers pass from an edge into the interior zone of a collective.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## bl concentrated momentum
- reading: The middle is the convergence point at which previously distributed motion becomes a single concentrated force.
- mechanism: A middle between sides supplies a point of maximum inward reach, and gathering motion supplies concentration. The packet gives the two images; I infer that reaching the center marks the culmination of converging momentum.
- trace:
  - 100:5 w **?** (و س ط B002: uçlar veya parçalar arasındaki orta yer / موضع الوسط بين الأطراف) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 

## bl entry reconfigures whole
- reading: The entry reaches the organizing middle of a collected whole and may alter how its previously distributed parts hold together.
- mechanism: The collective need not be a passive, already fixed target. The جمع branch exposes an active relation between scattered parts and a collected whole; entry into its middle can therefore be read as contact with the organizing point of that whole. The claim that ingress may reconfigure it is my inferred arrow.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 

## bl interposition in concert
- reading: A coexisting social reading appears: the movers interpose within a coalition at the point where its divided intentions have become concerted resolve.
- mechanism: Two social branches coexist with the physical reading: وسط can act between parties, and جمع can collect divided opinions into one resolve. Their conjunction permits an interposition into the decision-center of an alliance. This is form-distant from the most direct verbal construal, so it remains exploratory rather than replacing physical ingress.
- trace:
  - 100:5 w **?** (و س ط B005: insanlar arasında aracılık etme / الوساطة بين الناس) — 
  - 100:5 w **?** (ج م ع B003: düşünüp kesin bir tutuma bağlanma / عزم محكم جمع الرأي بعد تفرقه) — 

## bl center as faultline
- reading: The center is also the gathered whole's faultline: penetration there carries the possibility of bisection and loss of integrity.
- mechanism: One accepted وسط branch makes the middle the line at which a thing is divided into halves, while جمع can mark intact totality. Their tension permits the center to be a faultline: reaching it threatens the integrity that جَمْعًا names. The cutting sense is associated with a derived form in the branch scope, which limits confidence but does not erase the activation.
- trace:
  - 100:5 w **?** (و س ط B006: ortasından kesip ikiye ayırma / قطع الشيء نصفين) — 
  - 100:5 w **?** (ج م ع B009: eksiksiz bütünlük / اكتمال الشيء كله بلا تفرق أو نقص) — 

## cd boundary overrun
- reading: Their exertive run overruns the body's outer limit and carries them into its defended center; spatial ingress acquires the live valence of transgression.
- mechanism: Running supplies rapid approach, panting supplies embodied exertion, and the co-present transgression branch makes a limit available. I infer that the focus movement does not merely occupy a center: it overruns a boundary and reaches the defended interior of the assembled body.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ع د و B001: hakkı aşan saldırganlık / مجاوزة الحد والظلم) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## cd ignition to concentrated ingress
- reading: Their momentum is shown as generated through impact, released from latency, and gathered until center-entry becomes its concentrated discharge.
- mechanism: Latent fire emerging from a striker and fire produced by striking provide an impact-to-release process. Coupled to جَمْعًا as gathered force, the focus becomes the culmination of energy repeatedly generated and concentrated before it enters the middle.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## cd concealed plan executed
- reading: The same event can be the execution phase of a concealed, deliberated, and collectively resolved design.
- mechanism: A second, coexisting activation uses hiding-behind rather than fire, and devising-by-deliberation rather than striking. Those branches meet the focus branch of concerted resolve: center-entry becomes execution of a prepared, concealed plan inside another collective.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B003: düşünüp kesin bir tutuma bağlanma / عزم محكم جمع الرأي بعد تفرقه) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B010: bir işi düşünüp nasıl yürütüleceğini tasarlamak / اقتداح الأمر بالنظر والتدبير) — 

## cd dawn phase change
- reading: At the dawn threshold, entry into the center is the phase-change by which an intact gathered configuration becomes another configuration.
- mechanism: Image-changing at first daylight turns the approach into a threshold event. The packet gives transformation, dawn, middle-entry, and intactness; I infer that contact with the center changes the configuration of the gathered whole, rather than merely changing the movers' location.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B009: eksiksiz bütünlük / اكتمال الشيء كله بلا تفرق أو نقص) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 

## cd self generated cover
- reading: The movers first alter the environment, then enter the collective's center through or by means of the disturbance they generated.
- mechanism: The movers stir material from its place and produce raised dust immediately before the focus. The repeated بِهِۦ construction links production and ingress. I infer, without fixing the pronoun's antecedent, that the generated disturbance can function as a medium or cover enabling penetration of the assembled center.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## cd whole with relational cut
- reading: It can also furnish the topology of the next claim: apparent gathered wholeness surrounds a center where a sustaining relation has been cut by ingratitude.
- mechanism: The context pivots from an outer gathered whole to the visible human in relation to a sustaining, completing lord, then names cutting and ingratitude. This activates an inverse interior model: a body may appear gathered and penetrable at its center while its sustaining relation is already severed from within.
- trace:
  - 100:5 w **?** (و س ط B002: uçlar veya parçalar arasındaki orta yer / موضع الوسط بين الأطراف) — 
  - 100:5 w **?** (ج م ع B009: eksiksiz bütünlük / اكتمال الشيء كله بلا تفرق أو نقص) — 
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## cd obscuring dust as testimony
- reading: The penetration writes its own testimony into the disturbed environment: the dust hides the movers now but marks their path afterward.
- mechanism: The non-dominant accepted mapping of أَثَرْ supplies a remaining trace, dust supplies a disturbed mark, and witness supplies observed presence plus a sign. The dust can therefore do two things at once: obscure the entrants while preserving testimony that center-entry occurred.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## cd desire occupies accumulative center
- reading: It also becomes an affective center: persistent desire reaches the heart's core and binds scattered goods into one compelling accumulation.
- mechanism: Heart-attachment and the heart's dark core relocate the focus topology inward; useful good supplies the attractor, while binding and intensity compact the attachment. Because focus جمع B001 includes collecting wealth or things from dispersion, the external penetration can coexist with a retrospective image of desire reaching and binding an accumulative human center.
- trace:
  - 100:5 w **?** (و س ط B002: uçlar veya parçalar arasındaki orta yer / موضع الوسط بين الأطراف) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B002: güç, katılık ve çetinlik / شدة القوة والصلابة) — 

## cd convergence reversed into exposure
- reading: It is the convergent half of a reversible topology: movement goes inward and parts gather, then concealed interiors are turned outward and their contents dispersed into knowledge.
- mechanism: Focus جمع gathers dispersed parts and focus وسط moves inward; the later branches invert both vectors by overturning concealment, exposing buried material, and scattering goods. The focus therefore becomes the convergent half of a reversible topology whose later half moves contents outward into disclosure.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## cd center entry as inner assay
- reading: It also prefigures an inner assay: access the center, collect dispersed contents until a resultant appears, extract the core from its covering, and make the generative interior fully known.
- mechanism: ح ص ل supplies both collecting until a resultant appears and extracting a precious core from its envelope; ص د ر supplies the source from which actions issue; خ ب ر supplies knowledge of the interior. These cues turn focus center plus collection into an assay-like operation: reach the interior, aggregate what is there, and expose its resultant to complete sovereign knowledge.
- trace:
  - 100:5 w **?** (و س ط B002: uçlar veya parçalar arasındaki orta yer / موضع الوسط بين الأطراف) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## returning incursion cycle
- reading: The focus can be carried as one inward phase of a recurrent circuit: depart, gather motion, return, and re-enter a center.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 

## faultline release
- reading: Its center is the faultline where penetration can split integrity, after which formerly gathered contents separate and scatter.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B006: ortasından kesip ikiye ayırma / قطع الشيء نصفين) — 
  - 100:5 w **?** (ج م ع B009: eksiksiz bütünlük / اكتمال الشيء كله بلا تفرق أو نقص) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 

## hydraulic convergence
- reading: A cross-domain model reads distributed flow gathering force, entering and settling in a middle, then departing again through permeable ground.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B010: parçaları toplanıp tamamlanma / استجماع القوة أو السير حتى تتلاحق أجزاؤه) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 

## seed in barren center
- reading: A botanical outlier depicts seed-grown life set into a center where barren ground tests whether nourishment can become an immature yield.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B011: adı bilinmeyen çekirdekten yetişme hurma ağacı / نخل دقل اجتمع من النوى لا يعرف اسمه) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:10 w **?** (ح ص ل B005: erken evredeki hurma koruğu / بلح حصل من النخلة قبل اشتداده) — 

## gathered lots as projectile formation
- reading: They can be imaged as discrete shafts or lots first gathered into a containing formation and then deployed toward the center.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 

## contained life brought out
- reading: A containment outlier reads the middle as a protected interior holding latent life or intact content until it is brought out and made perceptible.
- mechanism: 
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B007: çocuğu karnındayken ölen veya el değmemiş kalan kadın / حال المرأة أو الأنثى التي بقي حملها أو عذرها معها) — 
  - 100:7 w **?** (ش ه د B006: doğum ve erginlik belirtisi / الخارج عند الولادة والإدراك) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) —


# Focus 100:6

## relational nonreciprocity
- reading: The socially constituted human fails reciprocity precisely within the bond of lordship, favor, and affection that sustains him.
- mechanism: The human is the familiar, social being; Rabb supplies ownership and authority; kanūd supplies ingratitude toward favor and affection. The result is not generic bad character but failed reciprocity inside a constitutive relation.
- trace:
  - 100:6 w **?** (ء ن س B003: yabancılık duymadan yakınlık ve rahatlık hissetme / الأنس الذي يزيل الوحشة) — 
  - 100:6 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## nurture severance
- reading: Kanūd is a severing response to the very process that repairs, raises, and completes the human.
- mechanism: Rabb is the one who repairs, nurtures, and completes; kanūd is cutting and separation. The human-facing side of insān sharpens the irony: the subject is grammatically turned toward the nurturer while functionally severing the channel of formation.
- trace:
  - 100:6 w **?** (ء ن س B004: insana dönük yan / الجانب الإنسي المقبل على الإنسان) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 

## barren recipient
- reading: The human is like tended ground that absorbs formative inputs yet gives no answering growth toward its cultivator.
- mechanism: The focus can be modeled agriculturally: Rabb tends and brings growth, whereas kanūd is land that does not produce. The moral failure becomes failed yield after received cultivation, not merely missing verbal thanks.
- trace:
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 

## perceptual refusal
- reading: The focus permits the sharper paradox of a perceiving, self-reflective being who sees enough to recognize yet refuses relational acknowledgment.
- mechanism: The subject is not merely uninformed. The insān inventory evokes perceiving and even a self-image in the eye, while kanūd evokes refusal of acknowledgment. The tension permits a reflexive reading: one capable of seeing signs and seeing oneself nevertheless withholds recognition.
- trace:
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ء ن س B005: göz bebeğinde görülen küçük yansıma / إنسان العين وصورة الإنسان في السواد) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## covenant cut
- reading: It reports an intimate favor-bond being breached from the human side.
- mechanism: The Rabb relation can cast a covenantal shadow: an intimate human relation is established, then kanūd both cuts it and denies its favor. This does not replace lordship with 'covenant'; it adds breach as a live relational mechanism.
- trace:
  - 100:6 w **?** (ء ن س B006: belirli sözlerde kişinin kendisi veya seçilmiş yakını / ابن الإنس للنفس والصفوة) — 
  - 100:6 w **?** (ر ب ب B011: bağlayıcı söz ve güvence / ربابة عهد وميثاق) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## kinetic breach
- reading: Kanūd becomes a forceful act-pattern: the human accelerates into a relation or whole and parts it from within.
- mechanism: The ordered motion supplies an engine for the focus cut: running with audible exertion proceeds into the middle of something gathered, where the middle-root also offers division into halves. I infer that this motion enacts, rather than merely accompanies, the severing force of kanūd.
- trace:
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (و س ط B006: ortasından kesip ikiye ayırma / قطع الشيء نصفين) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 

## reveal conceal oscillation
- reading: Kanūd is latent but not inaccessible: exertion strikes it into signs, even as the human's own activity raises a veil over those signs.
- mechanism: A concealed fire is struck into appearance; morning opens visibility; something is stirred and spread outward; then raised dust alters or occludes the image. Against insān as visible and perceptive, kanūd becomes a latent condition that activity repeatedly exposes and re-veils.
- trace:
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (و ر ي B005: gizleme, gizlenme ve başka anlam gösterme / ستر الشيء وجعله وراء الظهور) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## habitual asymmetry
- reading: It names a rehearsed asymmetry: sustaining benefit repeatedly returns while the human repeatedly withholds relational return.
- mechanism: The non-dominant ع و د mapping contributes habit and a returning benefit; the closing repetition of Rabb contributes sustained nurture and duration. I infer recurrence: benefits and care return, yet the human's severing nonresponse also hardens into a repeated disposition.
- trace:
  - 100:6 w **?** (ر ب ب B007: bir yerde kalıp sürme / لزوم وإقامة ودوام) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 
  - 100:1 w **?** (ع د و B006: kişiye dönen yarar ve iyilik / عائدة ومعروف يرجع) — 
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (ر ب ب B007: bir yerde kalıp sürme / لزوم وإقامة ودوام) — 

## self witness
- reading: One coexisting reading makes the human and his traces witnesses against the denial: the perceiver carries the evidence of what he refuses to acknowledge.
- mechanism: The perceiving human and the reflected human in the pupil meet witness as presence/viewing and as a sign, then knowledge as disclosure and a distinguishing mark. One live reading is self-attestation: the human's own perception, embodied signs, and acts witness the kanūd condition.
- trace:
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ء ن س B005: göz bebeğinde görülen küçük yansıma / إنسان العين وصورة الإنسان في السواد) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 

## divine expert witness
- reading: A coexisting reading makes it the Rabb's expert diagnosis of a relational condition whose inward basis is fully known.
- mechanism: A competing reading keeps the witness external to the human: witness can be declaration grounded in knowledge, and the closing repetition of Rabb is joined to expert knowledge of the inward matter. The focus assertion then reads as an informed diagnosis by the same Rabb toward whom kanūd is directed.
- trace:
  - 100:6 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## displaced attachment
- reading: Kanūd is misdirected attachment: the human loves and grips the received good so tightly that the giver-directed bond is denied.
- mechanism: The context denies that kanūd is simple lovelessness. Love is present and lodged in the heart, but it fastens around useful good and gift; شدت supplies both a tightened bond and avarice. I infer a competition of bonds: attachment to what is received displaces acknowledgment of the giver.
- trace:
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## exhumed interior
- reading: Kanūd is the buried, action-generating orientation inside the chest, recoverable by an ordered disclosure that strips away its coverings.
- mechanism: The later sequence supplies an epistemic excavation: what is hidden low is overturned, the kernel is extracted from its covering, the chest is the source from which acts issue, and the interior is expertly known. Kanūd shifts from visible conduct to the buried generator of conduct.
- trace:
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## cultivated non yield
- reading: The context activates an entire ecology: the human receives water, seed, gift, and cultivation yet remains non-yielding toward the one who nurtures him.
- mechanism: The baseline barren-land reading gains a full cultivation cycle: provision, watering, and repair; seed and gift; extraction of kernel or residue; then knowledge and working of soft earth. I infer that Rabb's nurture is input and the human's kanūd is failed yield despite that input.
- trace:
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:3 w **?** (غ ي ر B001: yarar sağlayıp durumunu iyileştirme / الصلاح والمنفعة بالميرة والسقي والإصلاح) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## fragmentation recollection
- reading: Kanūd fragments relation and benefit, but the context imagines those fragments later recollected until the human's resultant remainder becomes visible.
- mechanism: The context alternates wholeness, dispersal, and collection: parts become a complete gathered thing, goods are scattered and overturned, then everything is collected until its result and residue appear. Kanūd as cutting becomes fragmentation whose pieces are later recollected into an inspectable total.
- trace:
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:5 w **?** (ج م ع B009: eksiksiz bütünlük / اكتمال الشيء كله بلا تفرق أو نقص) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## lots receptacle accounting
- reading: He treats received portions like chance lots gathered without a giver-relation, while the sequence later gathers those portions into a disclosed result.
- mechanism: 
- trace:
  - 100:6 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 

## panting self inflation
- reading: The charging human swells with exertive breath and self-expansion at the same moment that he cuts the sustaining relation.
- mechanism: 
- trace:
  - 100:6 w **?** (ر ب ب B004: soluğu yükselip sıkışmak / تصعد النفس وانتفاخه) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 

## contagious interior corrosion
- reading: It is an inward corrosion of social humanity that can propagate through a gathered direction while remaining fully visible to inward expertise.
- mechanism: 
- trace:
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:1 w **?** (ع د و B006: hastalığın bulaşması / العَدْوى في انتقال الداء) — 
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) —


# Focus 100:7

## bsl 01 direct presence
- reading: The subject is present to the matter indicated by ذَٰلِكَ and witnesses it from direct proximity.
- mechanism: The witness is present with the matter and sees it directly. Its force comes from participation or immediate observation, not from receiving a report.
- trace:
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 

## bsl 02 knowledge testimony
- reading: The subject bears articulate, knowledge-based testimony concerning that matter.
- mechanism: Knowledge is converted into a decisive declaration, acknowledgement, or proof-bearing judgment. The witness does not merely perceive; it makes what is known evidentially available.
- trace:
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 

## bsl 03 visible expression
- reading: The subject's own expression can speak evidentially about the subject, even before deliberate confession.
- mechanism: An expression can testify about its source independently of a formal declaration. The subject's outward articulation is therefore capable of exposing the subject.
- trace:
  - 100:7 w **?** (ش ه د B005: ifade eden dil / اللسان الشاهد) — 

## bsl 04 witnessing sign
- reading: The subject can be a standing evidentiary sign whose condition testifies without a separate speech act.
- mechanism: A visible condition functions indexically: it points beyond itself to the state that produced it. Witnesshood can thus reside in what the subject is or displays, not only in what the subject says.
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## involuntary breath testimony
- reading: The subject can betray the matter through an involuntary bodily utterance generated by its own action.
- mechanism: Rushing generates panting, and the generated sound discloses the exertion that caused it. The focus witness can therefore be involuntary bodily output: action gives the body a 'tongue' that testifies about its own state.
- trace:
  - 100:7 w **?** (ش ه د B005: ifade eden dil / اللسان الشاهد) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## elicited latent sign
- reading: The subject carries latent testimony that an encounter can strike into visibility.
- mechanism: Fire is present but hidden in the striking-material until contact draws it out. By analogy, witnesshood can be latent in the subject and become visible only when an event strikes, tests, or agitates it.
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## forensic wake
- reading: The subject can be read as the trace-bearing aftermath of action: changed matter itself testifies to what passed.
- mechanism: The incursion alters a scene; morning supplies visibility; disturbance lifts material into a dust-cloud; and the non-dominant ء ث ر mapping supplies a remaining mark of what passed. An event thus writes a forensic wake that continues to witness after the mover has gone.
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 

## witness from within
- reading: The subject witnesses from inside the collective event and is implicated in what it sees.
- mechanism: Entry into the middle of an assembled body creates an internal vantage. The witness is not detached at the perimeter; it knows through being embedded in the event's crowded center.
- trace:
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B002: bir araya gelmiş insan topluluğu / جماعة اجتمعت أو أخلاط ضمتها الجهة) — 

## self indicting severance
- reading: The human is a self-implicating witness to his own severance and ingratitude toward the source that nurtures and completes him.
- mechanism: The immediately named human can perceive, stands in a relation of nurture and completion to a lord, yet is characterized by severance and ingratitude. His own condition therefore supplies knowledge-based evidence against his relational denial: the recipient's cut-off posture testifies to the gift-relation it refuses.
- trace:
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## desire as confession
- reading: The subject's tightly rooted love of perceived benefit is the confession: attachment itself visibly verifies the matter.
- mechanism: Abiding love occupies the heart's dark core and is tightened like a bond around what is perceived as beneficial. This durable inner attachment produces an outward pattern; the subject's intensity is itself the expression that confirms the prior claim of witnesshood.
- trace:
  - 100:7 w **?** (ش ه د B005: ifade eden dil / اللسان الشاهد) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 

## proleptic excavated witness
- reading: The subject is already a witness in latent status, even though a future overturning will make the evidence publicly legible.
- mechanism: What is obscure and lowered in graves is turned over and uncovered, becoming available to knowledge. The present nominal 'witness' can therefore be proleptic: the subject already carries evidentiary status whose visibility will be forced by a later excavation.
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## inner archive extracted
- reading: The subject carries an inner archive: the source of actions can be gathered and extracted into testimony about the subject.
- mechanism: The breast is treated as an origin from which actions issue, while taḥṣīl gathers dispersed contents into an appearing result and extracts a core from its envelope. The subject's witnesshood becomes archival: the inner source retains action-generating orientations until they are consolidated into evidence.
- trace:
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## two tier knowing
- reading: The context weights the human as self-witness and reserves explicitly named, inwardly comprehensive expertise for the Lord; the two readings coexist as nested rather than interchangeable.
- mechanism: The final ayah explicitly names the Lord as sovereign and attributes knowledge of the report and the matter's interior to Him. This differentiates two epistemic levels: the human is witness through self-presence, expression, or trace, while the Lord comprehends the inward reality of that witness. A divine subject for 100:7 remains grammatically imaginable in isolation but is contextually weakened rather than silently erased.
- trace:
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## counted recurrence
- reading: A countable, practiced recurrence becomes cumulative testimony: the pattern witnesses more strongly than any isolated act.
- mechanism: 
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 

## sterile spark confession
- reading: The desire's bright but non-benefiting output becomes its adverse witness: what flares as 'good' may expose its own sterility.
- mechanism: 
- trace:
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 

## comb and extraction
- reading: The subject is a comb-like bearer of concentrated testimony: inward content remains enclosed until an extraction makes it available.
- mechanism: 
- trace:
  - 100:7 w **?** (ش ه د B007: petekli bal / الشَّهْد في الشمع) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## emergence with attendant traces
- reading: The transition emits or brings along its own verifying traces; emergence itself arrives with a witness.
- mechanism: 
- trace:
  - 100:7 w **?** (ش ه د B006: doğum ve erginlik belirtisi / الخارج عند الولادة والإدراك) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) —


# Focus 100:8

## bound attachment
- reading: He is tightly fastened to what he takes to be good; the verse profiles the tenacity of the bond, not merely a large quantity of affection.
- mechanism: The three focus roots yield a relational mechanism: something judged beneficial attracts preference, preference clings, and the doubled lām construction culminates in a predicate of tight fastening. شَدِيدٌ therefore describes not only degree but how firmly the subject is bound to the desired good.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 

## miserly gift
- reading: He clings severely to bounty and is tight-fisted with what could circulate as a gift.
- mechanism: A received or available gift becomes an object of possessive attachment. Because the ش د د inventory permits severity as miserliness, the predicate can diagnose retention: love of giving-as-object becomes unwillingness to let the gift pass onward.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 

## forceful pursuit
- reading: He drives hard toward the option he prefers; شَدِيدٌ can profile pursuit as well as feeling.
- mechanism: Selection supplies a target, attachment supplies directional preference, and the charge branch of ش د د converts that preference into pursuit. The predicate can therefore be kinetic: desire does not merely sit in the subject but drives him toward the preferred outcome.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 

## hidden heart core
- reading: The verse locates a tightly bound valuation in the heart's kernel, presenting love as a hidden causal core.
- mechanism: The selected good is lodged at the heart's inner kernel and held there by a tightened bond. This produces an inward-causal reading: the verse identifies a compact motive at the subject's core from which conduct can issue.
- trace:
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 

## exertive drive
- reading: The context gives that pursuit lungs and effort: love of the preferred good is a drive capable of sustaining a hard run.
- mechanism: Running plus audible breath gives the focus-only charge model a bodily cost. The packet supplies motion and panting; I infer that the preference named in 100:8 can function as the drive that sustains exertion. شَدِيدٌ becomes force expended under attachment, not a static emotional measurement.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 

## ignited attachment
- reading: Love is also latent combustible energy: it can be struck into forceful action, yet its sparks may prove spectacular and non-beneficial despite being directed toward what is called good.
- mechanism: The context supplies a latent fire brought out by striking. I assign the directional arrow: a contact or friction event activates an inward attachment into visible energetic output. The remote ح ب ب spark branch adds a disturbing qualification: brilliance can be weak or useless even when its declared object is خَيْر.
- trace:
  - 100:8 w **?** (ح ب ب B011: yararsız zayıf kıvılcım veya gece ışıldayan böcek / نار الحباحب شرر لا ينتفع به) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B002: güç, katılık ve çetinlik / شدة القوة والصلابة) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 

## incursive accumulation
- reading: His attachment drives an incursive movement into the center of concentration; the desired good is imagined as something to reach, penetrate, and gather.
- mechanism: Displacement produces a cloud, entry reaches a center, and scattered parts are gathered. The packet supplies that trajectory; I infer that the selected good in 100:8 can occupy the role of the concentrated object toward which attachment drives. The reading changes from pursuit in open space to forceful penetration and accumulation.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B003: saldırıya atılma ve hızla koşma / شد الحملة والعدو) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 

## self monopolizing choice
- reading: He preferentially selects and gathers what he calls good under an exclusive claim for himself; miserliness is the closure of a choice-and-collection mechanism.
- mechanism: The packet's non-dominant ء ث ر mapping for أَثَرْ supplies self-monopolization, while the next ayah supplies gathering. Joined to خَيْر as choosing and شَدِيد as miserliness, these cues revise attachment into exclusive appropriation: the subject selects what is better, gathers it, and reserves it for himself.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:4 w **?** (ث و ر B006: başkalarını dışlayarak kendine ayırmak / استبداد المرء بالشيء لنفسه) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 

## gift relation severed
- reading: He preserves the bounty-side of a relation while cutting the giver-side: intense attachment to the gift and ingratitude toward nurture are one asymmetric mechanism.
- mechanism: The context places nurture and completion beside cutting and ingratitude for favor or affection. Those supplied relations revise the focus gift model: the subject adheres to the benefit while severing reciprocity with its nurturing giver. شَدِيد as miserliness is therefore relational asymmetry, not just private greed.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 

## severity as evidence
- reading: The strength of that valuation is itself a witnessing mark: what grips the heart becomes evidence of what the subject has chosen and of the relation he has cut.
- mechanism: The near-parallel وَإِنَّهُ ... لَشَهِيدٌ and وَإِنَّهُ ... لَشَدِيدٌ frames place testimony beside severity. The packet supplies a witnessing sign; I infer that the severe bond to the selected good is itself the sign that makes the preceding relational failure legible. A private motive becomes evidence.
- trace:
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 

## forensic heart kernel
- reading: That bond is the buried causal kernel of conduct: the later sequence overturns its cover, extracts it from the action-producing chest, and renders its inward selection fully knowable.
- mechanism: The post-focus sequence moves from knowing, through overturning what is hidden, to extracting an inner kernel from the chests and knowing the affair's inside. Those packet elements revise the heart-core baseline into a forensic mechanism: the tightly bound selection named in 100:8 is the buried causal kernel that later exposure isolates.
- trace:
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## recurrent desire loop
- reading: The attachment is a trained return-path: the subject repeatedly selects the same valued object until preference becomes a fastened habit.
- mechanism: 
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B003: daha iyi olanı seçme / طلب الخير بالاختيار والاستخارة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:1 w **?** (ع د و B004: tekrarla alışkanlık ve yatkınlık kazanma / عادة ودرَبة ومواظبة) — 

## hoarded seed barrenness
- reading: He binds up the seed of good so tightly that its gift-potential never enters nurture: possessive love turns fertile possibility into barren retention.
- mechanism: 
- trace:
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 

## surplus cut from nurture
- reading: He loves surplus as surplus: increase is detached from the nurturing relation that produced benefit and retained under a one-way, miserly bond.
- mechanism: 
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B003: belirli işlem biçimleriyle sınırlı anapara fazlalığı / زيادة الربا في المعاملة) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 

## good as coaxing lure
- reading: The direction can reverse: the presented good lures the hidden attachment into the open, revealing what the subject is tightly bound to when concealment is overturned.
- mechanism: 
- trace:
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B006: bir geçidi tıkayıp hayvanı yuvasından çıkarma / استدراج الحيوان من جحره) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) —


# Focus 100:9

## unveiling threshold
- reading: A challenge about an impending epistemic threshold: the one who can defer recognition now will confront disclosure when burial is physically reversed.
- mechanism: The rhetorical أَفَلَا and temporal إِذَا place knowing at an event-threshold: earth is overturned, the buried are disclosed, and what was unavailable becomes clear to a knower. The packet supplies disclosure and burial; I infer that the event changes the knower's epistemic position.
- trace:
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 

## container reversal
- reading: The entire architecture of concealment fails: below becomes above, enclosed contents lose their ordering, and knowledge arrives through that catastrophic topological reversal.
- mechanism: The graves are not only locations but hidden, inward-sunk enclosures. بُعْثِرَ contributes both disordered scattering and the geometry of a basin whose bottom is made its top. I infer that knowing follows a collapse of the distinctions inside/outside and below/above.
- trace:
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ب ع ث ر B003: havuzu yıkıp altını üste çevirme / هدم الحوض وقلب أسفله أعلاه) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 

## trace identification
- reading: Knowing may require identifying and reconstructing what upheaval has disordered from the marks by which the hidden is made legible.
- mechanism: Scattering can reduce immediate order even while hidden contents surface. The distinguishing-mark branch of ع ل م allows knowing to be reconstructive: identities or histories are followed through signs generated or exposed by disturbance. This does not replace ordinary knowing; it specifies one way disclosure becomes legible.
- trace:
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## return boundary
- reading: The event becomes a reversal of terminal departure: a bodily crossing is run back, and the grave's one-way boundary proves permeable.
- mechanism: The dominant ع د و image supplies rapid outward traversal, while its non-dominant mapped ع و د image supplies return after departure. Panting makes the traversal embodied. Attached to burial and upturning, these cues activate a reversible-boundary model: the grave is a crossed limit whose apparently one-way departure is run back. The packet supplies motion, return, burial, and uncovering; I infer that they form one directional cycle.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 

## ignition dawn
- reading: Upturning behaves like struck fire passing into dawn: concealment is converted into manifestation, so the event changes not only location but the object's mode of appearance.
- mechanism: Latent fire emerges when struck; the next pair supplies changed form and first light. Attached to the focus's hidden grave, upturning, and coming-clear, the event is no longer mere removal of a cover. It is an activation sequence in which impact makes a concealed capacity manifest and dawn stabilizes it as visibility. The packet gives the stages; I infer the ignition-to-disclosure arrow.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## dust trace
- reading: Exposure first produces a dusted, disordered archive; knowing is the work of following surviving marks through the disturbance.
- mechanism: Stirring something from its place raises dust, which can obscure at the very moment of exposure. The split ء ث ر mapping contributes a surviving mark that points back to what was. Joined to the focus's distinguishing-mark branch of knowledge and disordered scattering, this yields a paradoxical evidentiary model: upheaval does not give pristine sight; it creates a disturbed field from which traces must be read.
- trace:
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 

## scatter assembly
- reading: Their old compartments are broken so that the separately hidden are transferred toward a common center; scattering is destructive of one order and preparatory for another.
- mechanism: Entering a center and gathering dispersed parts counterpose a shared middle to the focus's sealed graves and scattered contents. I infer a transfer between organizations: grave-upturning destroys compartmentalized enclosure, but scattering is not the final state; it relocates what was separately buried into a common, centered field.
- trace:
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 

## relational self witness
- reading: How can a perceptive, self-witnessing beneficiary live as though he does not know? The later opening turns relational denial into exposed, mark-bearing evidence.
- mechanism: Human perception, a nurturing/completing Lord, ingratitude, and self-witness recast the focus question. The problem is not simply missing information: the addressed human can perceive and is present to evidence, yet lives a relational severance from the source of nurture. Grave-upturning externalizes what self-witness already makes difficult to call innocent ignorance. Pronoun continuity and the direction from witness to culpability are reader inferences.
- trace:
  - 100:6 w **?** (ء ن س B002: görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma / إيناس الشيء برؤية أو إحساس أو سماع) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 

## desire confinement
- reading: Physical exhumation also becomes the disclosure of a tightly lodged orientation: desire had hidden in an inner core while luring conduct outward, and burial cannot keep that organizing attachment concealed.
- mechanism: Love clings to the heart's dark core, severity tightens like a knot, and one accepted خ ي ر image lures an animal from its burrow. Attached to the focus's inward-hidden grave and its forced uncovering, these cues activate a second, coexisting confinement: attachment hides within and nevertheless draws conduct outward. Grave-opening can therefore expose the organizing desire carried into burial, while the literal grave reading remains intact.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B006: bir geçidi tıkayıp hayvanı yuvasından çıkarma / استدراج الحيوان من جحره) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 

## outer inner assay
- reading: Grave-opening only de-containerizes the outward record; the paired next operation gathers and extracts the inward source, producing a two-direction assay of exterior and interior.
- mechanism: The near-parallel passive constructions oppose two operations: graves are scattered open, while what is in breasts is gathered until its result appears and its core is extracted. Since the breast branch marks the source from which acts issue, I infer a two-stage assay: external containers are disrupted, then interior causes are distilled. The event in 100:9 is therefore the first, outward half of disclosure rather than its endpoint.
- trace:
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## asymmetric knowing
- reading: It stages two simultaneous epistemologies: human recognition is questioned and may be forced by exposure, while the sovereign knower already reaches the inward reality that excavation will manifest.
- mechanism: The final assertion places lordship beside knowledge of reports and inward realities. This answers the focus's questioned human knowing with a second epistemic position: grave-upturning may cause or force human recognition, but it does not create the Lord's access. I infer a contrast between belated exposed knowing and prior comprehensive interior knowing, while retaining both as coexisting readings.
- trace:
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 

## fluid container failure
- reading: The burial system fails like an inverted basin: recessed containers turn over and their pooled contents pour into exposure, so knowing follows irreversible loss of enclosure.
- mechanism: 
- trace:
  - 100:9 w **?** (ع ل م B005: deniz ya da suyu bol kuyu / ماء كثير مجتمع في عيلم) — 
  - 100:9 w **?** (ب ع ث ر B003: havuzu yıkıp altını üste çevirme / هدم الحوض وقلب أسفله أعلاه) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 

## seed latency
- reading: Burial can also be carried as a latency chamber: earth-held contents are released in a seed-like transition from hidden placement to outward manifestation.
- mechanism: 
- trace:
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 

## burrow lure
- reading: A coexisting affective reading appears: what the person loved had already been drawing the hidden self into outward evidence, and the final earth-opening completes that exposure.
- mechanism: 
- trace:
  - 100:8 w **?** (خ ي ر B006: bir geçidi tıkayıp hayvanı yuvasından çıkarma / استدراج الحيوان من جحره) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 

## vertical split root
- reading: The event becomes a polarity reversal: what was depressed and hidden is driven into elevation as the bottom is made top.
- mechanism: 
- trace:
  - 100:11 w **?** (ر ب ب B001: artmak veya yükselmek / زيادة وعلو) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:9 w **?** (ب ع ث ر B003: havuzu yıkıp altını üste çevirme / هدم الحوض وقلب أسفله أعلاه) —


# Focus 100:10

## resultant gist
- reading: What issued diffusely from each inner source is consolidated there into its intelligible resultant or gist.
- mechanism: The packet supplies collection until a resultant becomes clear and an origin from which acts issue. I infer a reverse operation: dispersed issuances are reduced back to the governing result or gist resident at their source.
- trace:
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## inner assay
- reading: The chest is subjected to an inner assay that extracts and distinguishes its kernel, not merely displays an undifferentiated contents-list.
- mechanism: The packet supplies a covered bodily interior and the extraction of kernel or precious material from husk, stone, or earth. I infer an assay rather than bare opening: the interior is processed so that what has value or explanatory weight is distinguished from its covering.
- trace:
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 

## residual source
- reading: Once outward conduct has departed, its inner source is separated down to the motive or residue that did not leave with the acts.
- mechanism: The packet supplies outward departure from a source and a remainder left after removal or separation. I infer a temporal model: after conduct has gone out from the breasts, the final operation isolates what remained there as the durable motive, sediment, or dregs.
- trace:
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## inside to fore
- reading: The inside is promoted into the foremost, determining result; latent priority becomes explicit priority.
- mechanism: The construction places مَا فِى, what is inside, under an operation whose destination is a clear حاصل, while the containing root also carries the image of the forepart. I infer a spatial-status reversal: what was interior is made foremost, first, and publicly determinative.
- trace:
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B002: ön, üst ya da başlangıç bölümü / المقدّم والأعلى والأول) — 

## returned tally
- reading: Its outward issuances come back as countable entries and are resolved into a returned account at their source.
- mechanism: The packet's split mapping for عَٰدِيَٰتِ supplies, alongside running, non-dominant images of counting and return after departure. Joined to focus collection and صدور as departure, these activate a loop in which what ran or issued outward returns as a countable resultant. This is an activation from supplied alternatives, not a claim that the surface lexeme straightforwardly means both counting and return.
- trace:
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 

## kinetic assay
- reading: It becomes the culmination of a kinetic processing sequence: latent content is struck into manifestation, disturbed, penetrated to its center, and recollected as an extracted result.
- mechanism: The ordered context supplies a chain of running, latent fire released by striking, alteration at first light, displacement into a dust cloud, penetration to the middle, and gathering. I infer that this external action-chain is a material analogue for حُصِّلَ: concealed inner material is not calmly displayed but forced through friction, disturbance, penetration, and recollection until its kernel is available.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B002: yerinden kaldırıp harekete geçirme / إثارة الشيء وتحريكه من موضعه) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 

## forensic source
- reading: The latent inner source is reconstructed from the surviving marks and testimony of what issued from it; حُصِّلَ is evidentiary assembly as well as disclosure.
- mechanism: A non-dominant mapped branch at 100:4 supplies a remaining trace; later cues supply a witnessing sign, a mark that guides recognition, and knowledge of an affair's interior. With the breasts as the source of acts and حُصِّلَ as reduction to a clear gist, these activate forensic reconstruction: dispersed traces are assembled backward into the latent source-pattern that generated them.
- trace:
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:7 w **?** (ش ه د B008: durumu gösteren belirti / العلامة الشاهدة) — 
  - 100:9 w **?** (ع ل م B002: ayırt edici ve yol gösterici işaret / أثر يميز الشيء ويهدي إليه) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## winnowed seed
- reading: The chest's buried growth is winnowed: useful kernel and residual dregs are both made explicit as products of one separation.
- mechanism: Gathering dispersed matter, a seed or grain that grows, useful good, overturned earth, and obscured burial form a material field around the focus branches of kernel-extraction and threshing-floor residue. I infer a winnowing mechanism: buried or mixed inner growth is gathered, unearthed, and separated into usable kernel and refuse. The context supplies the images; their combination into a threshing sequence is mine.
- trace:
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## relational yield
- reading: It discloses the actual yield of a nurture-relation: whether received cultivation became reciprocal growth or a cut-off, barren remainder.
- mechanism: The clause identifies the visible human in relation to a Lord whose branches include nurture, completion, and growth, then predicates cutting, ingratitude, and barren soil. Joined to حُصِّلَ as outcome and residue, this activates a relational yield: the breasts disclose what nurture actually produced, including a severed or sterile remainder. The packet does not state the growth-to-yield arrow; I infer it from the branch combination.
- trace:
  - 100:6 w **?** (ء ن س B001: insan türü ve bu türden bir kişi / ظهور الإنسان المخالف للتوحش والجن) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## bound preference
- reading: They yield the governing attachment: a tightly bound valuation at the inner core that gives otherwise scattered acts their direction.
- mechanism: Love is supplied as an attachment lodged in the heart's kernel, خير as inclination toward perceived benefit, and شدة as both a tied bond and intense withholding. With the breast as the source of acts, I infer a motivational topology: حُصِّلَ isolates the tightly bound preference that organizes conduct, not a miscellaneous set of secret propositions.
- trace:
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B001: arzulanan iyilik / الميل إلى الخير النافع) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 

## inverse excavation
- reading: They undergo inverse but complementary disclosures: the outer is broken apart and scattered, while the inner is gathered and resolved into its decisive kernel.
- mechanism: 100:9 supplies overturning earth, uncovering what is buried, and scattering possessions; its مَا فِى ٱلْقُبُورِ construction closely precedes the focus's مَا فِى ٱلصُّدُورِ. The paired passives activate complementary operations rather than synonyms: outer enclosures are disaggregated and inverted, while inner material is gathered, resolved, and assayed. I infer the polarity scatter outside → collect inside.
- trace:
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ب ع ث ر B002: eşyayı dağıtıp altüst etme / تبديد المتاع وقلب بعضه على بعض) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 

## water source sediment
- reading: The breast is a source-reservoir after its outward flow has departed, and the final operation reveals the motive-sediment that settled behind.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B004: kaynağı kesilmeyen kalıcı su ve su yeri / الماء العد) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:10 w **?** (ص د ر B003: geldiği yerden ayrılıp dönme / الصُّدور عن المورد) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## appetite crop
- reading: They preserve an intake-history: what appetite repeatedly selected and accumulated is inventoried like grain in an inner crop.
- mechanism: 
- trace:
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:10 w **?** (ح ص ل B004: kuş kursağı / موضع يجتمع فيه الطعام في جوف الطائر) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 

## arrested fruit
- reading: The focus exposes the developmental condition of inward fruit—matured, still soft and nascent, or arrested despite nourishment.
- mechanism: 
- trace:
  - 100:6 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:8 w **?** (ش د د B004: güç ve sağduyu bakımından olgunluğa erişme / بلوغ الأشد) — 
  - 100:10 w **?** (ح ص ل B005: erken evredeki hurma koruğu / بلح حصل من النخلة قبل اشتداده) — 
  - 100:10 w **?** (ص د ر B001: göğüs bölgesi / الصدر الجارحة وما يتصل بها) — 

## settled liability
- reading: The inward account is settled as liability: knowledgeable testimony resolves what giving or withholding makes the person answerable for.
- mechanism: 
- trace:
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 
  - 100:10 w **?** (ص د ر B005: para ödeme ve güvence yükümlülüğü koyma / المصادرة على مال) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) —


# Focus 100:11

## sovereign inward knowledge
- reading: On that day, the one who already owns and governs their relation is certainly acquainted with their inward reality, not merely their visible record.
- mechanism: Lordship supplies authority and ownership over the same plural referent picked up by بِهِمْ, while خبير supplies knowledge of an affair's interior rather than its appearance. The clause therefore joins jurisdiction to penetration: the knower is not an external reporter but the one whose claim already encompasses the persons known.
- trace:
  - 100:11 w **?** (ر ب ب B001: sahip olup yönetme / ربوبية وملك وسيادة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## nurture as long experiment
- reading: The caretaker who has brought them along stage by stage is, at that culmination, already testedly acquainted with what that formation became.
- mechanism: The nurture-and-completion branch of رب makes the relation diachronic; the tested-inner-knowledge branch of خبر makes knowledge the intimate result of having continuously tended the subject. The reader supplies the arrow from prolonged care to tested acquaintance, while the packet supplies both endpoints.
- trace:
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## abiding nearness
- reading: The predicate can also be heard as the inward knowledge of one whose lordly relation has stayed with them throughout.
- mechanism: A branch of رب contributes durative staying or drawing near, and خبير contributes inward acquaintance. Their conjunction permits a reading of knowledge by abiding attendance rather than remote surveillance; this is a relational overlay, not a replacement for lordship.
- trace:
  - 100:11 w **?** (ر ب ب B007: bir yerde kalıp sürme / لزوم وإقامة ودوام) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## cultivator hidden yield
- reading: The nurturer is also like a cultivator who knows the hidden ground and what its growth will yield.
- mechanism: The non-dominant رب mapping supplies rearing and growth, while خبر supplies water-holding soil and the tiller/sharecropper. The reader analogically joins these material images: one who raises a crop knows the ground's concealed condition and eventual yield. This is form-distant but remains doubly anchored in the two focus roots.
- trace:
  - 100:11 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 

## running counted return
- reading: يَوْمَئِذٍ can mark the return-point where every outward course is recovered as a countable inward history already known to Him.
- mechanism: The opening ع د و cue is split across running, counting, and returning inventories. Holding all three mapped roots together changes the final day from a static timestamp into the point where outbound trajectories return as countable histories before the inwardly knowing Lord. The packet supplies the three images; the conversion of motion into reckoning is the reader's abductive arrow.
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ع د و B001: sayma, sayı ve sayıya göre bir topluluğa katma / إحصاء المعدود) — 
  - 100:1 w **?** (ع د و B001: geri dönme ve yeniden yapma / رجوع بعد انصراف وتثنية بعد بدء) — 
  - 100:1 w **?** (ع د و B002: dönüş yeri ve son varış / مصير ومرجع ومعاد) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## forensic effect chain
- reading: خبير also crowns a forensic sequence: latent causes emit signs, scattered effects are gathered, and the Lord knows both the inward cause and the persons behind the trace.
- mechanism: The ordered cues form an evidentiary cascade: latent fire is struck out, a dawn threshold changes visibility, disturbance spreads, dust remains, and agents enter a gathered center. The non-dominant أثر branch explicitly supplies a surviving sign of what happened. This strengthens خبير from generic inward knowledge into knowledge capable of reading hidden cause through emitted effects while still knowing the agents themselves.
- trace:
  - 100:2 w **?** (و ر ي B002: çakmaktan ateş çıkarma ve sönük ateşi harlama / نار كامنة تخرج من الزند) — 
  - 100:2 w **?** (ق د ح B001: ateş çıkarmak ve ateş çakma araçları / إيراء النار بالقدح) — 
  - 100:3 w **?** (غ ي ر B003: biçimini değiştirme veya yerine başkasını koyma / تغيير الصورة أو إبدال الشيء بغيره) — 
  - 100:3 w **?** (ص ب ح B001: günün ilk aydınlığı / الصبح وأول النهار) — 
  - 100:4 w **?** (ث و ر B001: gizlilikten çıkıp belirerek yayılma / انبعاث الشيء وانتشاره ظاهرا) — 
  - 100:4 w **?** (ث و ر B003: geride kalan belirti veya iz / علامة باقية تدل على ما كان) — 
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:5 w **?** (و س ط B003: ortaya girme veya ortaya yerleştirme / الدخول أو الجعل في الوسط) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## nurture versus severance
- reading: The final رَبَّهُم means the care-bond persists even across the human's cutting, barren response, and خبير knows that failed reciprocity from inside its whole history.
- mechanism: The person is situated within human familiarity and an explicit رب relation, then described through branches of cutting, ingratitude, and barren ground. This revises the nurturant baseline into a failed-reciprocity model: sustained care meets a response that severs relation and yields no growth. رَبَّهُم in the focus then reinstates the possessive bond that the human response does not successfully erase.
- trace:
  - 100:6 w **?** (ء ن س B003: yabancılık duymadan yakınlık ve rahatlık hissetme / الأنس الذي يزيل الوحشة) — 
  - 100:6 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:6 w **?** (ك ن د B001: keserek bağlantıyı sona erdirme / القطع والانفصال) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:11 w **?** (ر ب ب B002: adım adım yetiştirip tamamlama / إصلاح وتربية وإتمام) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## attachment knot inside
- reading: The benefactor knows the inward knot by which love of His gift clings to the heart, hardens into withholding, and becomes denial of the gift relation.
- mechanism: Love is supplied as something clinging to the heart and even its dark core; شديد supplies a tightened knot and miserliness; خير supplies gift, while كنود supplies denial of gift. The reader infers a transformation: attachment to the benefaction tightens into possessiveness and thereby negates gratitude to the benefactor. The focus خبير now knows the internal knot, not only the outward refusal.
- trace:
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:8 w **?** (ح ب ب B002: sevgi ve yeğleme / المحبة الملازمة للقلب) — 
  - 100:8 w **?** (ح ب ب B004: kalbin içindeki kara öz / حبة القلب سويداؤه) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B001: bağlayıp sağlamlaştırma / شد العقد والوثاق) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:11 w **?** (ر ب ب B016: gereksinim, sıkı düğüm veya iyilik / رُبَى حاجة وعقدة ونعمة) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## epistemic asymmetry
- reading: خبير is the asymmetrical climax: testimony sees, event-triggered knowing receives disclosure, but the Lord is already testedly acquainted with the interior from which the disclosed result comes.
- mechanism: The context stages three epistemic modes: witnessing by presence and articulation, knowing when something becomes uncovered, and extracting a resultant. The focus then selects خبير, whose supplied scope reaches tested inner character rather than outward appearance. The reader infers a hierarchy, without requiring a fixed antecedent for every pronoun: final divine acquaintance exceeds both testimony and event-triggered recognition.
- trace:
  - 100:7 w **?** (ش ه د B001: hazır bulunup görme / الحضور مع المشاهدة) — 
  - 100:7 w **?** (ش ه د B002: bilgiye dayalı tanıklık / البيان بعلم) — 
  - 100:9 w **?** (ع ل م B001: bilme ve gerçeğini kavrama / انكشاف الشيء للعارف) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## double excavation outer inner
- reading: The day performs a double excavation—outer person and inner source—then بِهِمْ recomposes both as whole persons whose casing, core, acts, and origins are already inwardly known.
- mechanism: Two containers are opened in sequence. Soil is overturned to uncover what was buried; then the chests are processed until their kernel or resultant appears. The صدر branch identifies the chest as an origin from which acts issue, so the second opening is causal, not merely another inventory. The final بِهِمْ gathers outer remains and inner sources into whole persons known by the Lord.
- trace:
  - 100:9 w **?** (ب ع ث ر B001: toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma / قلب التراب وكشف المدفون) — 
  - 100:9 w **?** (ب ع ث ر B003: havuzu yıkıp altını üste çevirme / هدم الحوض وقلب أسفله أعلاه) — 
  - 100:9 w **?** (ق ب ر B001: ölüyü gömme, ona gömü yeri sağlama ve gömü yeri / مواراة الميت في القبر) — 
  - 100:9 w **?** (ق ب ر B002: gizli, alçakta veya içe gömülü kalma / غموض الشيء وتطامنه) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ص د ر B004: eylem türetme temeli; çıkış yeri veya zamanı / الأصل الذي تصدر عنه الأفعال) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## cultivation harvest result
- reading: The context gives that analogy a temporal arc: nurture meets barren ground or viable seed, final processing separates kernel from residue, and خبير knows the true yield of the life tended.
- mechanism: Context converts the focus-only cultivator analogy into a full growth-and-harvest mechanism. Human response can be non-growing ground; حب can be a seed that grows and bears grain; final processing extracts the kernel or leaves residue. The Lord/cultivator's خبير knowledge is thus of what the tended life actually yielded. The agricultural arrow is inferred, but every material station is packet-supplied.
- trace:
  - 100:11 w **?** (ر ب ب B005: besleyip büyütmek ve yetişmek / تغذية ونشوء) — 
  - 100:11 w **?** (خ ب ر B003: üründen pay karşılığı ortakçılık ve bunu yapan çiftçi / إصلاح الأرض بالمخابرة) — 
  - 100:6 w **?** (ك ن د B003: hiçbir bitki yetiştirmeyen toprak / الأرض التي لا تنبت) — 
  - 100:8 w **?** (ح ب ب B001: tane, tohum ve taneye benzeyen tek parça / الحبة التي تنبت وتحمل الحب) — 
  - 100:10 w **?** (ح ص ل B002: özünü ayırıp çıkarma / استخراج اللب أو النفيس من غلافه) — 
  - 100:10 w **?** (ح ص ل B003: geride kalan artık / البقية والحثالة بعد الرفع أو الفصل) — 

## somatic diagnostic
- reading: خبير resembles a diagnostician of the inward condition: outward exertion and breath disclose symptoms, but His acquaintance reaches the hidden source beneath them.
- mechanism: 
- trace:
  - 100:1 w **?** (ع د و B002: yaya ya da atla koşma / العَدْو والحَضْر) — 
  - 100:1 w **?** (ض ب ح B001: tilki sesi ve ona benzetilen sesler / صوت الضباح) — 
  - 100:2 w **?** (و ر ي B001: iç organları bozan ya da akciğeri tutan hastalık / داء يأكل الجوف أو يصيب الرئة) — 
  - 100:11 w **?** (ر ب ب B004: soluğu yükselip sıkışmak / تصعد النفس وانتفاخه) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## quiver of trajectories
- reading: As a contained-bundle analogy, the Lord gathers the many launched courses into one day without losing inward knowledge of any individual course.
- mechanism: 
- trace:
  - 100:11 w **?** (ر ب ب B010: kura oklarını toplayan kap / ربابة تجمع القداح) — 
  - 100:2 w **?** (ق د ح B007: uçsuz ve tüysüz ok gövdesi; talih oyunu oku / عود السهم والقدح في الميسر) — 
  - 100:5 w **?** (ج م ع B001: dağınık parçaları bir araya toplama / ضم المتفرق حتى يصير شيئا مجموعا) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) — 

## hydraulic retention
- reading: In a hydraulic reversal, surface dust can obscure while low ground silently receives and retains; خبير becomes an image of knowledge held beneath turbulence.
- mechanism: 
- trace:
  - 100:4 w **?** (ن ق ع B004: toz, özellikle havaya kalkmış toz / نقع الغبار المثار) — 
  - 100:4 w **?** (ن ق ع B001: suyun birikmesi ve suda bekletmeye bağlı adlandırmalar / استقرار الماء وما ينقع فيه) — 
  - 100:11 w **?** (ر ب ب B008: katmanlı asılı bulut kümesi / رباب السحاب) — 
  - 100:11 w **?** (خ ب ر B002: gevşek, alçak ve su tutan arazi veya su birikintisi / لين الأرض ومائها) — 

## covenant surplus account
- reading: The Lord knows a breached benefaction-covenant from within: gift was converted into withheld surplus, and the final day exposes the relation's true resultant.
- mechanism: 
- trace:
  - 100:11 w **?** (ر ب ب B011: bağlayıcı söz ve güvence / ربابة عهد وميثاق) — 
  - 100:11 w **?** (ر ب ب B016: gereksinim, sıkı düğüm veya iyilik / رُبَى حاجة وعقدة ونعمة) — 
  - 100:11 w **?** (ر ب ب B003: belirli işlem biçimleriyle sınırlı anapara fazlalığı / زيادة الربا في المعاملة) — 
  - 100:6 w **?** (ك ن د B002: gördüğü iyiliği bilmezlik / كفران النعمة والمودة) — 
  - 100:8 w **?** (خ ي ر B005: cömertlik ve armağan verme / الكرم والهبة) — 
  - 100:8 w **?** (ش د د B006: eli sıkılık / شدة البخل) — 
  - 100:10 w **?** (ح ص ل B001: toplama ve elde kalanı ortaya koyma / جمع الشيء حتى يظهر حاصله) — 
  - 100:11 w **?** (خ ب ر B001: bilgi edinme, bildirme ve deneyerek iç yüzü tanıma / العلم بالخبر وباطن الأمر) —
