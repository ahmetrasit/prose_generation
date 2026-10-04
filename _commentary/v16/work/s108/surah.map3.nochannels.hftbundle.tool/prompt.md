Surah: 108. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), hft.md (its records are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S108 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), earlier readers' activation hypotheses (hft.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not use tools, delegate, browse or inspect files.

The HFT records are proposals by earlier readers. Ignore their judgements: grades,
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
4. `## Not carried`. Each HFT record you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s108/surah.r2.nochannels.hftbundle/text.md =====
# Surah 108

- 108:1 إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ
- 108:2 فَصَلِّ لِرَبِّكَ وَٱنْحَرْ
- 108:3 إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ


===== _commentary/v16/work/s108/surah.r2.nochannels.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ط و (root_001028): 108:1 أَعْطَيْنَٰكَ

- **B001** elle uzanıp alma — elle alma · bir şeyi elle alma · yapraklara erişmek için ön ayaklarını kaldıran ceylan
  العطو التناول باليد (maqayis;ayn;tahdhib)؛ عطوت الشيء تناولته باليد (sihah)؛ الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق (ayn)؛ الظباء تتطالل إذا رفعت أيديها لتتناول ورق الشجر (tahdhib)
- **B002** verme, karşılıklı elden geçirme ve verilen şey — verme, elden uzatma · karşılıklı elden verme veya el değiştirme · kılıcı sırayla birbirine verip elde tutma veya sallama · verilen şey · birine verilen şey · birine verilen şeyler · verilen şeylerin çoğul adı · çok veren kimse · malı ne çok veriyor!
  منه اشتق الإعطاء والمعاطاة المناولة والعطاء اسم لما يعطى وهي العطية (maqayis)؛ العطاء اسم لما يعطى وأعطية وأعطيات (ayn)؛ أعطاه مالا يعطيه إعطاء والاسم العطاء والعطية الشيء المعطى (sihah)؛ الإعطاء مأخوذ من هذا والمعاطاة المناولة والعطاء اسم لما يعطى (tahdhib)؛ المعاطاة أن يستقبل رجل رجلا ومعه سيف فيقول أرني سيفك فيعطيه فيهزه هذا ساعة وهذا ساعة (tahdhib)
- **B003** birinin işini görüp istediğini uzatma — çocuğun yakınlarının işini görüp istediklerini uzatması · onun işini görüp bakımını üstlenme · işimi görüyor
  عاطى الصبي أهله إذا عمل وناول ما أرادوا (maqayis)؛ هو يعطيني ويعاطيني إذا كان يخدمك (sihah)؛ عطيته وعاطيته أي خدمته وقمت بأمره ومن يعطيك أي من يتولى خدمتك (tahdhib)
- **B004** hakkı olmadan el uzatma ve gözü pekçe işe girişme — hakkı olmayan veya alınması uygun görülmeyen şeye el uzatma · bir işe girip onunla uğraşma · gözü pekçe eyleme girişip deveyi yaralama · aracı, dayanağı veya yeterliği olmadan erişilmez işe kalkışma
  التعاطي تناول ما ليس له بحق ويتعاطى ظلم فلان وفتعاطى فعقر وعاط بغير أنواط (maqayis)؛ تعاطاه تناوله وفلان يتعاطى كذا أي يخوض فيه وفتعاطى فعقر (sihah)؛ التعاطي تناول ما لا يجوز تناوله وفتعاطى الشقي عقر الناقة فبلغ ما أراد وتعاطيه جرأته ويتعاطى معالي الأمور ورفيعها ويتعاطى أمرا قبيحا (tahdhib)
- **B005** insanlardan bir şey isteme — bir şey verilmesini isteme · bir şey verilmesini isteme · insanlardan bir şey isteme
  استعطى وتعطى سأل العطاء (sihah)؛ يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم (tahdhib)
- **B006** direnmeden uyma ve kolay bükülme — devenin direnmeyip yönlendirmeye uyması · kolay bükülen yumuşak yay · gerilirken direnmeyen yumuşak yay · boyun eğip başını biniciye çevir
  أعطى البعير إذا انقاد ولم يستعصب (sihah)؛ قوس عطوى مواتية سهلة (sihah)؛ قوس معطية لينة ليست بكزة ولا ممتنعة (tahdhib)؛ أعط فيعوج رأسه إلى راكبه (tahdhib)
- **B007** karşılıklı çekişmede yenme — karşılıklı çekişmede onu yenme
  تعاطينا فعطوته أي غلبته (sihah)

## ك ث ر (root_001286): 108:1 ٱلْكَوْثَرَ

- **B001** çokluk ve sayıca artma — çokluk; sayının artması ve azlığın karşıtı · bir şey çoğaldı, sayısı arttı · çok, sayıca fazla · bir şeyi çoğaltmak · bir şeyden çokça edinmek veya onu çok saymak · malın ya da durumun azı ve çoğu · pek çok, çok büyük sayıda
  الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)
- **B002** çokluk yarışı ve çoklukla üstün gelme — onlarla çokluk yarışına girdik ve onları sayıca geçtik · mal, sayı veya güç bakımından çokluk yarışı ve övünme · çokluk yarışında yenilmiş
  كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)
- **B003** kişiye bağlı çokluk nitelemeleri [kalıp] — malı çok kişi · çok konuşan kadın veya erkek · iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi · başkasının malıyla kendini varlıklı göstermek
  رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)
- **B004** özel ırmak veya bol iyilik — cennetteki özel ırmak · bol veya büyük iyilik · iyiliği ve bağışı bol, cömert önder
  الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)
- **B005** kabarıp yükselen yoğun toz — kabarıp yükselen yoğun toz · son derece çoğalmak
  الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)
- **B006** hurma ağacının iç göbeği — hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü · meyve veya hurma göbeği için el kesme cezası yoktur · hurma ağacı çiçek sürgünü verdi
  الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)
- **B007** bir araya toplanma — bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir
  الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)

## ص ل و (root_000879): 108:2 فَصَلِّ

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

## ECHO ص ل ي (root_000880): for 108:2 فَصَلِّ: withheld observed target; not identity

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

## ر ب ب (root_000532): 108:2 لِرَبِّكَ

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

## ECHO ر ب و (root_000537): for 108:2 لِرَبِّكَ: withheld observed target; not identity

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

## ن ح ر (root_001479): 108:2 وَٱنْحَرْ

- **B001** boyun kökü ile üst göğüs arasındaki ön bölge — boyun kökü ile üst göğüs arasındaki ön bölge · boyun köküyle birleşen üst göğüs bölgeleri · kesme işleminin uygulandığı üst göğüs noktası · atın göğsündeki iki damar · insan ve devedeki iki köprücük kemiği · atın boğaz altındaki dairesel tüy işareti
  النحر للإنسان وغيره والجمع نحور (maqayis)؛ النحر ذبحك البعير بطعنة في النحر حيث يبدو الحلقوم من أعلى الصدر (ayn;tahdhib)؛ مجال القلادة من الصدر (jamhara)؛ موضع القلادة من الصدر وهو المنحر (sihah;mufradat)؛ الناحران عرقان في صدر الفرس (maqayis;sihah)؛ الناحرتان الترقوتان من الإبل والناس (tahdhib)
- **B002** deveyi üst göğsünden saplayarak kesmek — deveyi üst göğsünden saplayarak kesmek · Kurban Bayramı'nın ilk günü · çok sayıda semiz deve kesip ikram eden cömert kişi · adamı boyun kökü ile üst göğsün birleştiği yerden vurmak
  النحر البزل في النحر ونحرت البعير نحرا (maqayis)؛ النحر ذبحك البعير بطعنة في النحر حيث يبدو الحلقوم من أعلى الصدر (ayn;tahdhib)؛ نحر البعير (jamhara;mufradat)؛ النحر في اللبة مثل الذبح في الحلق (sihah)؛ يوم النحر يوم الأضحى (ayn;tahdhib)؛ يوم النحر الذي ينحر فيه (jamhara)؛ رجل منحار يوصف بالجود (sihah)
- **B003** karşısında veya önünde bulunmak [kalıp] — adamın karşısına geçmek · bir evin başka bir evin karşısında bulunması · bir evin yolun karşısında bulunması · ordunun önünde · evlerin karşı karşıya bulunması
  هذه الدار تنحر تلك الدار إذا استقبلتها (ayn)؛ دار بني فلان تنحر الطريق أي تقابله (jamhara)؛ أقبل فلان في نحر الجيش أي في أوله (jamhara)؛ نحرت الرجل إذا صرت في نحره (sihah)؛ منازله تناحر هذا ينحر هذا أي قبالته (tahdhib)
- **B004** bir şey için kıyasıya çekişmek [kalıp] — bir şeyi kaçırmamak için kıyasıya çekişmek · savaşta birbirine saldırmak
  انتحروا على الشيء تشاحوا عليه حرصا كأن كل واحد منهم يريد نحر صاحبه (maqayis)؛ إذا تشاح القوم على أمر قيل انتحروا وتناحروا من شدة حرصهم (ayn)؛ انتحر القوم على الشيء إذا تشاحوا عليه حرصا وتناحروا في القتال (sihah)؛ انتحروا عليه من شدة حرصهم (tahdhib)؛ انتحروا على كذا تقاتلوا تشبيها بنحر البعير (mufradat)
- **B005** kendi boğazını keserek yaşamına son vermek [kalıp] — kendi boğazını keserek yaşamına son vermek
  انتحر الرجل أي نحر نفسه (sihah)
- **B006** günün başı ya da ayın başlangıç veya bitiş sınırı — günün başlangıcı · ayın son günü veya son gecesi · ayın başlangıcı ya da son günü · ayın sonundaki hilaller veya geceler
  النحيرة آخر يوم من الشهر لأنه ينحر الذي يدخل (maqayis)؛ الليلة تنحر الشهر أي أول ليلة منه (jamhara)؛ استقبل نحر النهار أي أوله (jamhara)؛ نحر النهار أوله (sihah)؛ النحيرة آخر يوم من الشهر وآخر ليلة من الشهر (sihah;tahdhib)؛ نحيرة لأنها تنحر الهلال أي تستقبله (tahdhib)؛ نحرة الشهر ونحيره أوله وقيل آخر يوم من الشهر (mufradat)
- **B007** ibadette göğsü dik tutmak, yöneltmek veya eli göğse koymak — ibadet sırasında doğrulup göğsünü dik tutmak · ibadet sırasında üst göğsü dik ve öne açık tutma
  إذا انتصب الإنسان في صلاته فنهد قيل قد نحر (ayn;tahdhib)؛ ضع يدك على نحرك (jamhara;mufradat)؛ استقبل القبلة بنحرك (tahdhib)؛ النحرة انتصاب الرجل في الصلاة بإزاء المحراب (tahdhib)
- **B008** bilgili, deneyimli ve işinin ustası kişi — bilgili, deneyimli ve işinin ustası kişi
  العالم بالشيء المجرب نحرير (maqayis)؛ النحرير العالم المتقن (sihah)؛ النحرير الرجل الطبن الفطن في كل شيء وجمعه النحارير (tahdhib)؛ النحرير العالم بالشيء والحاذق به (mufradat)
- **B009** bulutun bol suyla birden boşalması [kalıp] — bulutun çok miktarda suyu birden boşaltması · yağmurun kesilmiş bir gövdeden akar gibi dökülmesi
  السحاب إذا انعق بماء كثير قد انتحر انتحارا (tahdhib)؛ كأنه منحور (tahdhib)

## ش ن ء (root_000820): 108:3 شَانِئَكَ

- **B001** nefret edip uzak durma — birinden nefret etti ve ona düşmanlık besledi · nefret ve düşmanlık · nefret anlamındaki hafifletilmiş söyleyiş · nefret · nefret eden veya düşmanlık besleyen kimse · senden nefret eden ve sana düşmanlık besleyen kimse · birbirlerinden nefret ettiler · senden nefret eden kimse hakkında söylenen kinayeli söz · nefret etme · bir topluluğa duyulan nefret
  أصل يدل على البغضة والتجنب للشيء؛ شنئ فلان فلانا إذا أبغضه (maqayis#2749;maqayis#2750)؛ شنيء يشنأ شنأة وشنآنا أي أبغض (ayn)؛ الشنآن البغض وتشانؤوا أي تباغضوا (sihah)؛ الشانيء المبغض والشنء البغضة (tahdhib)؛ شنئته تقذرته بغضا له وشنآن قوم أي بغضهم (mufradat)
- **B002** tiksinip uzak durma — ondan nefret ettiği için tiksindi · pislikten tiksinip uzak durma · bir şeyden tiksinip uzak duran kimse · bu nitelemeden türetildiği belirtilen bir Yemen topluluğunun adı · aynı topluluk adının farklı söylenişi · söz konusu topluluğa mensup
  الشنوءة وهي التقزز (maqayis#2749;maqayis#2750)؛ الشنوءة التقزز وهو التباعد من الأدناس (sihah)؛ الرجل الشنوءة الذي يتقزز من الشيء (tahdhib)؛ شنئته تقذرته بغضا له (mufradat)
- **B003** belirli yapılarda kabul etme veya aradan çıkarma [kalıp] — onu kabul edip doğruladı · hakkını tanıyıp kendi elinden çıkardı · hükümdarı aralarından çıkardılar
  شنئت للأمر وبه إذا أقررت (maqayis#2749;maqayis#2750)؛ شنئ به أي أقر (sihah)؛ شنئت حقك أي أقررت به وأخرجته من عندي؛ شنئوا الملك أي أخرجوه من عندهم (tahdhib)
- **B004** sevilmeyen, kötü huylu veya çirkin olma — insanların sevmediği veya görünüşü çirkin kimse · görünüşü çirkin kimse · güzel olsa bile sevilmeyen kimse · sevilmeyen, kötü huylu kimse · sevilmeyen kadın
  رجل مشناء إذا كان يبغضه الناس (maqayis#2749;maqayis#2750)؛ رجل شناءة وشنائية مبغض سيء الخلق (ayn)؛ رجل مشنأ أي قبيح المنظر والمشناء مثله (sihah)؛ المشنيئة البغيضة ورجل مشناء إذا كان قبيح المنظر (tahdhib)

## ب ت ر (root_000080): 108:3 ٱلْأَبْتَرُ

- **B001** tamamlanmadan kesip koparma — bir seyi tamamlanmadan kesmek veya kokten koparmak · kuyruk gibi bir parcayi kesip koparma · kesilip kopma, ayrilma · keskin, kesip gecen kilic · kuyrugu kesilmis
  بترت الشيء بترا قطعته قبل الإتمام (sihah); الانبتار الانقطاع (sihah); البتر قطع الذنب ونحوه إذا استأصلته (tahdhib); البتر استئصال القطع (tahdhib); سيف باتر وبتار قطاع (tahdhib); يستعمل في قطع الذنب (mufradat); أصل واحد وهو القطع قبل أن تتمه، والسيف الباتر القطاع (maqayis)
- **B002** soyu veya iyi etkisi kesilmis olma — soyu, adi veya hayir etkisi kesilmis · hayri az sayilan iki varlik · hayir etkisi kesilmis is · onu soyu veya iyi izi kesilmis duruma getirdi · hayirla anilmasi kesilmis adam
  الأبتر الذي لا عقب له (sihah); كل أمر انقطع من الخير أثره فهو أبتر (sihah); الأبتران العبد والعير لقلة خيرهما (sihah); المنقطع العقب والمنقطع عنه كل خير (tahdhib); أجري قطع العقب مجراه فقيل فلان أبتر إذا لم يكن له عقب (mufradat); إن شانئك هو الأبتر أي المقطوع الذكر (mufradat); الرجل الذي لا عقب له أبتر وكل من انقطع من الخير أثره فهو أبتر (maqayis)
- **B003** eksik acilisli soz veya is [kalıp] — ovgu ve dua ile acilmamis hitap · Tanri anmasiyla baslamayan is eksik sayilir
  خطب زياد خطبته البتراء لأنه لم يحمد الله فيها ولم يصل على النبي (sihah); خطبة بتراء لما لم يذكر فيها اسم الله (mufradat); كل أمر لا يبدأ فيه بذكر الله فهو أبتر (mufradat); خطبته البتراء لأنه لم يفتتحها بحمد الله تعالى والصلاة على النبي (maqayis)
- **B004** akrabalik bagini koparma — akrabalik bagini koparan kisi
  رجل أباتر للذي يقطع رحمه (sihah); رجل أباتر يقطع رحمه (mufradat); رجل أباتر يقطع رحمه يبترها (maqayis)
- **B005** kusluk gunesi ve o vakitte namaz kilma — bu kullanimda gunes · isinlar belirginlestigi kusluk aninda namaz kilmak
  أبتر إذا صلى الضحى حين تقضب الشمس؛ تقضب أي يخرج شعاعها كالقضبان؛ حين تبهر البتيراء الأرض؛ البتيراء الشمس (tahdhib)
- **B006** kisa ve toplu yapili olma — kisa ve toplu yapili kisi
  بحتر وهو القصير المجتمع الخلق؛ منحوت من كلمتين من الباء والتاء والراء؛ كأنه حرم الطول فبتر خلقه؛ والكلمة الثانية الحاء والتاء والراء (maqayis)



===== _commentary/v16/work/s108/surah.r2.nochannels.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 108

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 108:1

## transferred plenitude
- reading: A multiplying plenitude has been decisively placed with the addressee.
- mechanism: Handing-over combines with numerical increase so that the focus does not merely announce that much good exists: it presents multiplying plenty as already transferred into the addressee's reach.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Literal handing-over supplies a completed donor-to-recipient transfer and makes the plenty recipient-directed.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Abundance and numerical increase supply content that can keep multiplying rather than a merely honorific object.

## comparative preponderance
- reading: The gift creates bestowed preponderance in contests of number, wealth, speech, or standing.
- mechanism: The focus roots both contain outdoing images: one in mutual dealing and the other through number, wealth, or standing. Their conjunction makes the gift an intervention in a comparative field, granting preponderance rather than only adding possessions.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Giving keeps the advantage bestowed rather than seized by the recipient.
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B007: Outdoing in reciprocal dealing supplies one side of a contest whose balance can be reversed.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B002: Outnumbering and rivalry in abundance turn quantity into comparative social force.

## concentrated fecundity
- reading: The object can be a concentrated fertile source whose compact gathering unfolds into abundance.
- mechanism: Palm pith or inflorescence and clustering recast abundance as a compact generative node. What is handed over need not be an already expanded heap; it can be a concentrated source from which plurality unfolds.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handing-over makes the compact source itself the bestowed object.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B006: Palm pith or inflorescence supplies a small fertile structure carrying future proliferation.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B007: Clustering supplies concentrated gathering as the organization of the latent abundance.

## reciprocal return
- reading: The transferred plenty initiates a giver-recipient circuit in which abundance returns as directed praise.
- mechanism: Prayer as praise directed to the sovereign source turns the one-way transfer into a responsive circuit. The recipient is not the terminal storage point of abundance; reception generates a return of praise without cancelling the asymmetry of the original gift.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handing-over establishes the descending movement from giver to recipient.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Multiplying abundance is what enters and sustains the response circuit.
  - 108:2 **فَصَلِّ** ص ل و B002: Prayer, praise, and mercy supply the upward or returning response to reception.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship, ownership, and sovereignty identify the source toward whom the response is directed.

## nurtured multiplication
- reading: The completed giving places the recipient inside a sustained process of nourished, maturing multiplication.
- mechanism: The dominant mapped root contributes repair, nurture, and completion, while the non-dominant split contributes feeding and growth. Together with the focus's fertile palm structure, they make abundance a provision brought toward maturity, not an inert stock dropped all at once.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handing-over marks the growth-bearing provision as genuinely bestowed.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B006: Palm pith or inflorescence supplies an organic locus whose abundance appears through maturation.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Repair, upbringing, and completion supply sustained cultivation toward a finished state.
  - 108:2 **لِرَبِّكَ** ر ب ب B005: The non-dominant mapped branch of feeding and growth intensifies the organic increase mechanism.

## ritual throughput
- reading: Abundance is enabling throughput whose fullness is displayed by worshipful and material release.
- mechanism: Specified worship, sovereign ownership, and slaughter at the throat redirect abundance from retention into embodied expenditure. The gift becomes enabling surplus whose realized form includes praise and costly release toward its source.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: The handed-over gift supplies what can subsequently be put into responsive action.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Abundance supplies surplus sufficient for outward expenditure rather than anxious hoarding.
  - 108:2 **فَصَلِّ** ص ل و B003: The specific act of worship gives the response a formal, enacted channel.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Sovereign ownership prevents the expenditure from becoming an aimless loss and orients it to the source.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Throat-slaughter supplies the material release through which retained provision becomes an embodied offering.

## threshold continuity
- reading: Abundance means a self-renewing continuity that can meet thresholds without being cut off at them.
- mechanism: A boundary of time facing another boundary and a thing cut before completion form a contrast between meeting an edge and losing continuation. Anchored in numerical increase, the focus gift becomes renewable continuity: it can reach a limit without being exhausted there.
- trace:
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Increase supplies the capacity to continue beyond a presently visible amount.
  - 108:2 **وَٱنْحَرْ** ن ح ر B006: One temporal boundary facing another supplies encounter with a limit rather than automatic termination.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting supplies the opposed failure in which a process cannot cross its edge into completion.

## severance reversal
- reading: The focus grants durable good, mention, and generative aftermath whose attempted severance rebounds as the adversary's own discontinuity.
- mechanism: Hostile distancing is paired with cutoff of posterity, mention, and good, but the emphatic predication assigns cutoff to the hater. This retroactively broadens the focus gift from countable plenty into durable transmission and relocates scarcity from the recipient to the adversarial relation.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Completed handing-over makes the recipient's endowment antecedent to and insulated from the hostile verdict.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B003: Abundance attached to a person, speech, or claims opens a social and reputational dimension beyond material count.
  - 108:3 **شَانِئَكَ** ش ن ء B002: Disgust and distancing supply the adversary's attempted social separation from the recipient and gift.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Cutoff of descendants, mention, and good specifies the continuity whose absence is reassigned to the hater.

## adversarial disclosure
- reading: Hostile speech can unwittingly disclose and multiply the recipient's mention while its own truncating project fails.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B007: Outdoing in reciprocal dealing supplies a reversal in which an adversarial move can be made to serve the recipient.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B003: Abundance attached to speech or claims makes circulation of mention a valid focus-level form of increase.
  - 108:3 **شَانِئَكَ** ش ن ء B003: Acknowledging truth and bringing it out supplies the paradox whereby hostility exposes what it contests.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting supplies the failed adversarial aim whose attempt instead increases disclosure.

## cloud release
- reading: The gift can be modeled as gathered provision whose abundance becomes real by releasing itself into flow.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handing-over supplies the crossing from a gathered source into recipient-accessible flow.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B007: Clustering supplies condensation or gathering before release.
  - 108:2 **لِرَبِّكَ** ر ب ب B008: The cloud image supplies an overhead carrier in which provision gathers.
  - 108:2 **لِرَبِّكَ** ر ب ب B013: Abundant water supplies the material content accumulated in that carrier.
  - 108:2 **وَٱنْحَرْ** ن ح ر B009: A cloud discharging itself with water supplies the release event that converts stored concentration into distributed plenty.

## obligation load
- reading: Abundance entrusts the recipient with greater capacity, and therefore greater exposure to worship, service, and legitimate claims.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B003: Attending to needs and handing over what is wanted turns reception into a capacity for service.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B003: Many demands or claims attaching to a person make abundance generate relational obligations.
  - 108:2 **فَصَلِّ** ص ل و B001: The non-dominant mapped image of worship as binding duty gives the entrusted capacity an obligatory response.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship and ownership place the service obligation inside a governing relation rather than social demand alone.


# Focus 108:2

## dedicated ritual pair
- reading: It reads as one dedicated circuit: disciplined bodily worship is joined to costly material release, and both are kept under the Lord's claim.
- mechanism: Prescribed, maintained prayer and throat-front sacrifice form two embodied expenditures under one owner and beneficiary. The first orders the worshipper's body; the second releases a valued animal or meal, so the coordination joins ritual form to costly outward action.
- trace:
  - 108:2 **فَصَلِّ** ص ل و B003: The prescribed-worship image supplies the bounded ritual form and serves as the inward and bodily pole of the paired response.
  - 108:2 **فَصَلِّ** ص ل و B001: The split-root image of binding, maintained worship adds durability rather than treating the first imperative as a momentary gesture.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship, ownership, and authority supply the single direction of both acts and block their conversion into self-display.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Slaughter at the throat-front supplies the concrete costly act, while its generosity scope makes that act the outward pole of worship.

## nurture answered by generosity
- reading: It can also sound relational: answer the one who has cultivated and completed you with praise-bearing worship and costly generosity.
- mechanism: The Lord is not only an authority but one who repairs, nurtures, and completes. Prayer can therefore voice praise and mercy, while slaughter can enact generosity; together they answer cultivation with acknowledgment and material beneficence.
- trace:
  - 108:2 **فَصَلِّ** ص ل و B002: Supplication, praise, and mercy make the first imperative an acknowledging and blessing-bearing response.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Repair, nurture, and staged completion recast the Lord relation as prior formative care that calls for a response.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: The sacrificial throat-cut remains concrete, and its associated generosity turns the second imperative into material beneficence.

## exposed frontality
- reading: They also form a frontality event: order the body, expose its front, and face the Lord directly, with sacrifice still retained as the primary act of the second imperative.
- mechanism: Prayer supplies an ordered bodily stance; the second root exposes the throat-front and also names direct facing. Without replacing sacrifice, these branches add a spatial reading in which the worshipper places the vulnerable front of the embodied self directly before the Lord.
- trace:
  - 108:2 **فَصَلِّ** ص ل و B001: Binding ritual postures supply the ordered body whose orientation is at stake.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship supplies the one before whom the body's orientation and exposure are directed.
  - 108:2 **وَٱنْحَرْ** ن ح ر B001: The upper chest and throat-front image supplies bodily vulnerability and makes the second imperative an exposure of the front.
  - 108:2 **وَٱنْحَرْ** ن ح ر B003: The direct-facing image turns that exposed front into a spatial stance before the Lord.

## received gift becomes return
- reading: The preceding transfer gives that answer a concrete occasion: received good is converted into directed praise and costly generosity.
- mechanism: A prior act of handing over makes the focus's opening consequence concrete. Praise-bearing prayer and generous sacrifice now answer a received benefit; the response is directed back to the nurturing Lord without reducing worship to repayment.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: The handing-over image supplies the prior transfer that makes the focus imperatives responsive rather than unprompted.
  - 108:2 **فَصَلِّ** ص ل و B002: Praise, blessing, and mercy supply the acknowledging form of the response to what was handed over.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Nurture and completion identify the Lord relation as an ongoing source of benefit, not a one-time transaction.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Sacrificial slaughter and its generosity scope make gratitude materially costly and outward-moving.

## recipient as steward
- reading: The recipient becomes a steward: what enters the hand is re-acknowledged as the Lord's and is allowed to move outward through worship and sacrifice.
- mechanism: The same root inventory holds taking into the hand and handing onward. Joined to the Lord's ownership and sacrifice's generosity, that bidirectionality makes the recipient a steward through whom a gift passes, not its terminal owner.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B001: Taking or receiving by hand supplies the recipient's initial possession of what arrives.
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handing over reverses the hand's direction and activates onward transfer as the gift's possible next movement.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: The ownership image keeps ultimate title with the Lord and makes the human recipient a custodian rather than an absolute possessor.
  - 108:2 **فَصَلِّ** ص ل و B003: Prescribed worship supplies the accountable form by which custody is acknowledged.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Generous sacrificial slaughter gives onward transfer a concrete social and material outlet.

## abundance breaks rival counting
- reading: Under abundance, sacrifice becomes anti-hoarding expenditure: value rises by being directed and shared, while competitive counting loses jurisdiction.
- mechanism: Abundance carries both numerical growth and competitive outnumbering. The non-dominant growth branch mapped under the focus's Lord token and the generosity of slaughter jointly reverse scarcity arithmetic: expending a gift need not mean being diminished, and worship refuses to turn abundance into rank.
- trace:
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Growth in number supplies abundance as increase rather than a fixed stock that expenditure can only reduce.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B002: Competitive outnumbering exposes the rival arithmetic that the focus's directed worship can refuse.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: The split-root image of increase and rising makes growth a live secondary resonance inside the Lord-directed phrase.
  - 108:2 **فَصَلِّ** ص ل و B003: Prescribed worship relocates value from public numerical rank to faithful performance.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Generous slaughter supplies an expenditure that can turn plenty into shared benefit instead of a hoarded score.

## abundance as outflow
- reading: Abundance becomes a flow regime: receive from the nurturing source, voice blessing, and pour material good onward rather than becoming its reservoir.
- mechanism: Handed-over abundance activates a hydrological chain already latent in the focus roots: nurturing low cloud, collected water, and a cloud pouring itself out. Prayer's mercy register and the second imperative's outpouring branch make the worshipper a conduit who answers inflow with blessing and material outflow.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: The handing-over image supplies inflow into the recipient and begins the transfer sequence.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Numerical growth supplies the pressure of more-than-contained abundance that can overflow.
  - 108:2 **فَصَلِّ** ص ل و B002: Mercy, blessing, and praise make prayer the non-material stream that can pass onward.
  - 108:2 **لِرَبِّكَ** ر ب ب B008: The low persistent cloud supplies a nurturing reservoir poised above what it sustains.
  - 108:2 **لِرَبِّكَ** ر ب ب B013: Abundant collected water supplies stored provision and links lordly nurture to a gathered resource.
  - 108:2 **وَٱنْحَرْ** ن ح ر B009: The cloud pouring itself out supplies the release phase and lets the second imperative image abundance becoming flow.

## hostility redirects frontality
- reading: In the presence of hatred, that frontality becomes a disciplined redirection: do not let the antagonist dictate a throat-to-throat answer; face and act for the Lord.
- mechanism: The later hater activates both direct-facing and throat-to-throat contention inside the second focus root. The purpose phrase then decides the vector: the worshipper's body and costly act face the Lord, not the antagonist, so prayer and sacrifice interrupt reciprocal hostility without erasing the threat.
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B001: Hatred and enmity supply the opposing agent who could otherwise capture the worshipper's attention and response.
  - 108:3 **شَانِئَكَ** ش ن ء B002: Disgust and distancing sharpen hostility as a relation of repulsion rather than mere disagreement.
  - 108:2 **وَٱنْحَرْ** ن ح ر B003: Direct facing supplies the spatial possibility of confronting either the Lord or the antagonist.
  - 108:2 **وَٱنْحَرْ** ن ح ر B004: Throat-to-throat contention supplies the retaliatory symmetry that remains possible but is rerouted by the purpose phrase.
  - 108:2 **فَصَلِّ** ص ل و B003: Prescribed worship gives the body a non-retaliatory action to perform under pressure.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship fixes the destination of attention and action, preventing the hater from becoming the governing addressee.

## hostility forces disclosure
- reading: They are also disclosure under pressure: allegiance is made visible by practiced worship rather than by answering the hater in kind.
- mechanism: A remote branch of the hostility root images acknowledgment and bringing truth out. Coupled with prayer as praise, lord-formed knowledge, and mastery in the second focus root, opposition can abductively function as the pressure under which allegiance becomes visible rather than as the object of argument.
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B003: Acknowledging and bringing truth out supplies the paradoxical disclosure image activated by the hostile agent.
  - 108:2 **فَصَلِّ** ص ل و B002: Praise and supplication give disclosed allegiance a voiced devotional form.
  - 108:2 **لِرَبِّكَ** ر ب ب B003: Knowledge formed through lordly care supplies the truth-content that pressure can make visible.
  - 108:2 **وَٱنْحَرْ** ن ح ر B008: Mastery as cutting through supplies an enacted competence that embodies the disclosure rather than merely asserting it.

## complete cut opposes truncation
- reading: The following truncation image differentiates it: the focus commands a deliberate, completing release at a boundary, while sterile cutting-before-completion belongs to the antagonist.
- mechanism: The context distinguishes two kinds of cutting. The focus's throat-cut is deliberate, properly located, joined to maintained worship, and directed to the one who completes; the later root names cutting something before completion. Sacrifice is therefore not undifferentiated destruction but a consummating release opposed to sterile truncation.
- trace:
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Cutting before completion supplies the failed or premature cut against which the focus's deliberate cut can be contrasted.
  - 108:2 **فَصَلِّ** ص ل و B001: Binding and maintaining prescribed worship place the second act inside a complete devotional form.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Repair, nurture, and completion supply the governing telos that distinguishes fulfillment from truncation.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: The precisely located sacrificial throat-cut supplies the intentional cut that releases value within the completed rite.
  - 108:2 **وَٱنْحَرْ** ن ح ر B006: The time-boundary image places sacrifice at a threshold, making the cut transitional rather than merely annihilating.

## worship makes continuity
- reading: Against cessation, the rites become continuity-making: maintained worship, completed nurture, and threshold-crossing carry allegiance and good beyond the immediate moment.
- mechanism: Cessation of posterity, mention, and good activates the focus roots' contrary capacities: maintained prayer, lasting attachment, nurture, and a boundary crossed rather than a line terminated. The imperatives become continuity-making practices, while cutoff is assigned elsewhere.
- trace:
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Cessation of posterity, remembrance, and good supplies the threatened endpoint against which continuity becomes visible.
  - 108:2 **فَصَلِّ** ص ل و B001: Maintained binding worship supplies recurrence and durable practice rather than a one-off performance.
  - 108:2 **لِرَبِّكَ** ر ب ب B007: Staying, clinging, and lasting supply persistence within the Lord relation.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Nurture through completion supplies continuity as a process carried to maturity.
  - 108:2 **وَٱنْحَرْ** ن ح ر B006: The edge where one time meets another supplies transition across a boundary rather than terminal stoppage.

## flow gains cutoff contrast
- reading: The later cutoff gives that conduit a contrastive necessity: prayer and sacrifice keep good transmissible, whereas the antagonist's mode terminates transmission and remembrance.
- mechanism: Gathered abundance and cessation sharpen the hydrological model into a polarity. Collected water that pours outward images continuity through release; cutting off mention and good images failed transmission. Prayer and sacrifice can therefore act as openings that keep received good in motion.
- trace:
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B007: Gathering a thing supplies abundance as concentration that can either remain closed or become available for release.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting supplies interruption of a process before its gathered potential reaches completion.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Cessation of remembrance and good supplies the social consequence of blocked transmission.
  - 108:2 **فَصَلِّ** ص ل و B002: Mercy and blessing supply a voiced flow of good that can continue beyond the worshipper.
  - 108:2 **لِرَبِّكَ** ر ب ب B013: Collected abundant water supplies the reservoir whose value depends on eventual transmission.
  - 108:2 **وَٱنْحَرْ** ن ح ر B009: The cloud pouring itself out supplies the opening by which gathered provision continues as benefit.

## back to front merism
- reading: As a lexical-body echo, it spans the worshipper from rear flank to exposed chest, suggesting the whole embodied self placed under the Lord's direction.
- mechanism: 
- trace:
  - 108:2 **فَصَلِّ** ص ل و B005: The back-haunch and rear-flank image supplies the body's posterior limit.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship supplies the center of dedication around which the whole body is read.
  - 108:2 **وَٱنْحَرْ** ن ح ر B001: The upper chest and throat-front image supplies the body's anterior and vulnerable limit.

## provisioning table
- reading: As a contained material analogy, it becomes a provisioning table: abundance is processed, enriched, slaughtered, and handed into household hospitality.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B003: Service and handing provision to one's household supply the social destination of prepared abundance.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B006: The palm-heart image materializes abundance as edible plant provision.
  - 108:2 **فَصَلِّ** ص ل و B008: The pounding-stone image supplies processing of seed or perfume as the preparation stage.
  - 108:2 **لِرَبِّكَ** ر ب ب B006: Thick syrup and treating food or vessels supply preservation and enrichment under the Lord token.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Generous slaughter supplies the meat and costly culmination of the provisioning sequence.

## follower to vanguard
- reading: As an exploratory rank topology, prayer keeps close behind the leader and the second command moves the follower into an exposed front when hostility appears.
- mechanism: 
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B001: Hatred and enmity supply the pressure under which following may require exposed action.
  - 108:2 **فَصَلِّ** ص ل و B007: The racer just behind the leader supplies disciplined close-following as the initial position.
  - 108:2 **لِرَبِّكَ** ر ب ب B001: Lordship and obeyed authority supply the leader whose direction governs movement.
  - 108:2 **وَٱنْحَرْ** ن ح ر B003: The direct front, including the front of an army, supplies the exposed position into which faithful action moves.

## hospitality makes kin
- reading: As a social outlier, lordly care, a shared worship place, and generous food make and sustain relation, directly opposing the context's image of severed kin.
- mechanism: 
- trace:
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B004: Severing kin supplies the social anti-model of relations cut rather than sustained.
  - 108:2 **لِرَبِّكَ** ر ب ب B005: The fostered-child and step-family image supplies care that can create durable relation beyond simple descent.
  - 108:2 **فَصَلِّ** ص ل و B007: Places of worship supply a shared social location in which relation can be gathered and maintained.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Generous sacrificial slaughter supplies hospitality capable of materially sustaining a household or community.

## heat straightens growth
- reading: As a split-root formation analogy, abundance is subjected to straightening discipline, nurtured into shape, and carried across a decisive threshold.
- mechanism: 
- trace:
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Growth in number supplies the initial expansion that still requires form and direction.
  - 108:2 **فَصَلِّ** ص ل و B004: Heating and turning a stick to straighten it supplies formative pressure rather than destructive burning.
  - 108:2 **لِرَبِّكَ** ر ب ب B005: The non-dominant nurture-and-growing branch supplies guided maturation under the Lord-directed phrase.
  - 108:2 **وَٱنْحَرْ** ن ح ر B006: The front edge of a time period supplies the threshold at which formed growth passes into a new phase.


# Focus 108:3

## hostility rebounds as cutoff
- reading: The hater's attempt to cancel the addressee rebounds as the hater's own failure to continue or leave good effect.
- mechanism: The judgment is not an unrelated insult added to hostility. The construction turns the consequence back onto hostility's bearer: the one who tries to negate the addressee is himself denied continuation in posterity, mention, good effect, or an undertaking brought to completion.
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B001: Hatred and enmity supply the hostile relation whose negating force is reversed onto its bearer.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Loss of posterity, mention, and good effect makes the predicate a verdict on failed continuation rather than only physical mutilation.

## aversion performs self severance
- reading: His own disgusted distancing performs the severance named by the predicate.
- mechanism: Aversive withdrawal is itself the cutting action. By recoiling from the addressee, the hater does not merely feel dislike but removes himself from a relation before its possibilities can mature, making the predicate an enacted result of his posture.
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B002: Disgusted avoidance contributes the motion of recoiling and supplies the mechanism of self-exclusion.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting turns withdrawal into an interrupted relation rather than a static emotional state.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B004: Severed kinship gives the withdrawal a social form: the hater cuts a bond and thereby occupies the severed side.

## failed stigma returns to evaluator
- reading: It reverses a stigmatizing gaze: the hostile label fails to adhere to its target and exposes the labeler's own noncontinuance.
- mechanism: The unpleasant-description branch lets hostility operate as stigmatizing evaluation. The focus construction refuses the hater's assignment of defect and makes the act of hostile description disclose the evaluator's own lack of enduring good or mention.
- trace:
  - 108:3 **شَانِئَكَ** ش ن ء B004: The branch supplies adverse characterization, allowing hatred to function as an attempted social label.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Cut-off mention and good effect relocate the lasting reputational defect onto the hostile evaluator.

## grant turns hostility into conceded claim
- reading: The prior grant makes him legible as a counterclaimant whose opposition concedes the addressee's right and fails before completion.
- mechanism: Once a grant has been handed to the addressee, the rare acknowledgment-and-release branch of ش ن ء can activate a contest over entitlement. The hater becomes an unsuccessful counterclaimant who must yield the right he contests, while his challenge is the thing cut short.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Actual handing over establishes a completed transfer and therefore a possible contested entitlement.
  - 108:3 **شَانِئَكَ** ش ن ء B003: Acknowledging and releasing a right supplies the surprising concession role for the hostile agent.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Cutting before completion makes the opponent's counterclaim, rather than the grant, the aborted undertaking.

## received abundance opens continuity channel
- reading: It describes relational exclusion from a received good that continues to multiply beyond the hater's reach.
- mechanism: Handover plus numerical growth forms a source-recipient-future circuit. Against that circuit, the focus predicate no longer means only that the hater possesses little; it means that hostility has no access to the multiplying transmission of good, mention, and effect.
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handover establishes the directional path by which good reaches the addressee.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Abundance and numerical growth extend the received good forward rather than leaving it a one-time possession.
  - 108:3 **شَانِئَكَ** ش ن ء B001: Enmity marks the relation that cannot enter or cancel the transmission circuit.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Cut-off mention and good effect specify what exclusion from the expanding circuit costs the hater.

## numerical contest becomes temporal
- reading: They are rival measures of success: current numerical pressure is defeated by the addressee's future continuity and the hater's vanishing effect.
- mechanism: The outnumbering branch turns the contrast into a contest over scale, but the focus predicate changes the axis from present headcount to future persistence. A hostile party may possess many voices or claims now, yet loses the contest if its mention and good effect do not continue.
- trace:
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B002: Outnumbering supplies an explicit competitive measure rather than undifferentiated plenty.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B003: Multiplicity in companions, speech, or demands supplies the possible present social noise of the contest.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Loss of mention and good effect moves the decisive count from present quantity to persistence through time.

## worship enters completion and growth
- reading: The hater occupies a failed trajectory: opposition cannot mature, while the addressee's responsive practice is nurtured into continuity.
- mechanism: The commanded act is directed into a field of worship, nurture, completion, and growth. That field converts the focus predicate from a generic fate into a contrast of trajectories: responsive alignment is formed and carried onward, while the hostile project is interrupted before attaining its end.
- trace:
  - 108:2 **فَصَلِّ** ص ل و B003: Specific worship supplies the responsive practice that follows reception of the gift.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Nurture, repair, and completion supply the process by which a received good is brought to maturity.
  - 108:2 **لِرَبِّكَ** ر ب ب B005: The non-dominant mapped root contributes feeding and growth, keeping a second live route from lordly nurture to developing continuity.
  - 108:3 **شَانِئَكَ** ش ن ء B001: Hostility supplies the counter-trajectory that tries to obstruct the formed response.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting names the failure of the hostile trajectory to reach completion.

## following procession reframes posterity
- reading: Posterity also becomes succession: being followed in responsive practice and good effect, a chain from which the hater is absent.
- mechanism: The image of a runner following the one ahead, joined to abiding duration, recasts continuity as a procession rather than only biological descent. The addressee's response can be followed, repeated, and carried onward; the hater is the one who cannot take or transmit a place in that sequence.
- trace:
  - 108:2 **فَصَلِّ** ص ل و B006: Following the previous runner supplies a serial model in which continuity consists of taking one's place after another.
  - 108:2 **لِرَبِّكَ** ر ب ب B007: Abiding and duration stabilize the procession as repeated continuity rather than a single act.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Interrupted posterity, mention, and good effect identify the hater as unable to continue in the sequence.

## purposeful cut exposes premature cut
- reading: It marks specifically an untimely and fruitless interruption, contrasted with a deliberate cut integrated into a completed act.
- mechanism: The context places a commanded, directed chest-cut beside nurture and completion. This distinguishes a purposeful act that consummates a response from the focus root's cutting-before-completion: the hater is not condemned for every kind of cutting but for an abortive, nonfruitful interruption.
- trace:
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Completion supplies the telic frame within which the commanded cut can belong to a finished response.
  - 108:2 **وَٱنْحَرْ** ن ح ر B002: Piercing the camel at the chest supplies a concrete, agentive cut performed under command.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Cutting something short before completion supplies the contrasting failed and untimely severance.

## facing body opposes aversive retreat
- reading: It is also spatially enacted: the one who recoils from encounter breaks the bond and leaves himself on the severed side.
- mechanism: The chest-facing-chest branch gives the context a bodily geometry of exposed encounter. Against it, the hater's disgusted recoil becomes a refusal to face relation, and severed kinship is the social result of that retreat.
- trace:
  - 108:2 **وَٱنْحَرْ** ن ح ر B003: Chest facing chest supplies frontal presence and embodied encounter.
  - 108:3 **شَانِئَكَ** ش ن ء B002: Disgusted avoidance supplies the opposite motion of recoil and distance.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B004: Severing kinship turns bodily retreat into a broken social bond.

## hostile heat becomes formative pressure
- reading: As a contained material analogy, hostile pressure can be absorbed into the addressee's formation while the hostile undertaking itself fails to finish.
- mechanism: 
- trace:
  - 108:2 **فَصَلِّ** ص ل و B004: The non-dominant split branch supplies heating that straightens or sets a thing, making pressure potentially formative.
  - 108:2 **لِرَبِّكَ** ر ب ب B002: Nurture and completion constrain the heat image toward formation rather than destruction.
  - 108:3 **شَانِئَكَ** ش ن ء B001: Enmity supplies the adversarial pressure whose intended effect is being reversed.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B001: Premature cutting confines failure to the hostile undertaking rather than to the addressee's formation.

## household circulation vs kin severance
- reading: Cutoff may describe refusal of a circulating household bond: benefit moves through relation while hostility severs its bearer from the network.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B003: Service and handing to family supply circulation of benefit through a household relation.
  - 108:2 **لِرَبِّكَ** ر ب ب B007: The non-dominant mapped branch supplies an extended household of close kin as the social network.
  - 108:3 **شَانِئَكَ** ش ن ء B001: Enmity supplies the antagonistic relation that refuses household circulation.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B004: Severing kinship makes the hater's exclusion a broken network tie rather than only lack of descendants.

## cloud release models distributed abundance
- reading: In the contained ecological analogy, the hater is a severed route outside a gathered-and-released flow whose effects keep spreading.
- mechanism: 
- trace:
  - 108:1 **أَعْطَيْنَٰكَ** ع ط و B002: Handover supplies transfer from a source toward a recipient.
  - 108:1 **ٱلْكَوْثَرَ** ك ث ر B001: Growth in abundance supplies the expanding effect of what is transferred.
  - 108:2 **لِرَبِّكَ** ر ب ب B008: The cloud branch supplies gathered capacity held before release.
  - 108:2 **وَٱنْحَرْ** ن ح ر B009: A cloud pouring out water supplies release and distribution from the gathered source.
  - 108:3 **ٱلْأَبْتَرُ** ب ت ر B002: Interrupted good effect identifies the hater as detached from the distributed consequences of abundance.
