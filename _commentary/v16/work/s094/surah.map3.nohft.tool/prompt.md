Surah: 94. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S94 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s094/surah.r2/text.md =====
# Surah 94

- 94:1 أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- 94:2 وَوَضَعْنَا عَنكَ وِزْرَكَ
- 94:3 ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- 94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ
- 94:5 فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- 94:6 إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- 94:7 فَإِذَا فَرَغْتَ فَٱنصَبْ
- 94:8 وَإِلَىٰ رَبِّكَ فَٱرْغَب


===== _commentary/v16/work/s094/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ر ح (root_000784): 94:1 نَشْرَحْ

- **B001** gizli anlamı açıklayıp anlaşılır kılma — açıklama; gizli anlamı ortaya çıkarma
  شرحت الكلام وغيره شرحا إذا بينته (maqayis)؛ الشرح البيان اشرح أي بين (ayn)؛ شرحت لك الأمر إذا أوضحته وكشفته (jamhara)؛ شرحت الغامض إذا فسرته (sihah)؛ شرح مسألة مشكلة إذا بينها والشرح البيان والفهم (tahdhib)؛ شرح المشكل من الكلام بسطه وإظهار ما يخفى من معانيه (mufradat)
- **B002** eti kesip yayarak parça veya dilim elde etme — eti kesme ya da yayma · eti parçalara ayırma ya da inceltme · et parçası · ince et dilimi ya da et parçası · yayvan, yağlı et parçası · kesilmiş ya da yayılmış et · kurutulmuş halde getirilen ceylan parçası · kesilmiş ya da yayılmış et
  اشتقاقه من تشريح اللحم (maqayis)؛ الشرح والتشريح قطع اللحم على العظام والقطعة شرحة (ayn)؛ الشريحة من اللحم القطعة المرققة وكل قطعة من اللحم شرحة وشريحة (jamhara)؛ ومنه تشريح اللحم والقطعة منه شريحة وكل سمين من اللحم ممتد فهو شريحة وشريح (sihah)؛ الشرح والتشريح قطع اللحم عن العضو وكل قطعة شرحة والتصفيف نحو من التشريح (tahdhib)؛ أصل الشرح بسط اللحم ونحوه (mufradat)
- **B003** iyiliği ve gerçeği kabule açılan içsel ferahlık — genişlik ve ferahlık · iç dünyayı iyiliği veya gerçeği kabul edecek biçimde genişletme
  الشرح السعة وشرح الله صدره للإسلام أي وسعه (ayn)؛ شرح الله صدره فانشرح إذا اتسع لقبول الخير (jamhara)؛ شرح الله صدره للاسلام فانشرح (sihah)؛ شرح الله صدره فانشرح أي وسع صدره لقبول الحق فاتسع (tahdhib)؛ شرح الصدر أي بسطه بنور إلهي وسكينة (mufradat)
- **B004** belirli biçimde cinsel birleşme, bekâreti bozma ve örtmece organ adı — kadını sırtüstü yatırarak onunla cinsel ilişkiye girme · kadınlarla belirli bir biçimde cinsel ilişkiye girme · bekâreti cinsel birleşmeyle bozma · kadın cinsel organı için örtmece ad
  ربما سمي فرج المرأة شريحا كناية (jamhara)؛ شرح جاريته إذا سلقها على قفاها ثم غشيها ويشرحون النساء شرحا والشرح افتضاض الأبكار (tahdhib)
- **B005** dünya malını geniş ölçüde edinme isteği [kalıp] — dünya malına yönelip onu geniş ölçüde edinmek isteme
  أكان الأنبياء يشرحون إلى الدنيا يريد كانوا ينبسطون إليها ويرغبون في اقتنائها رغبة واسعة (tahdhib)
- **B006** koruma ve koruyucu gözetimi — koruma ve gözetme · koruyucu ya da ekin bekçisi
  الشارح الحافظ؛ الشرح الحفظ؛ الشارح في كلام أهل اليمن الذي يحفظ الزرع من الطيور وغيرها (tahdhib)

## ص د ر (root_000849): 94:1 صَدْرَكَ

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

## و ض ع (root_001657): 94:2 وَوَضَعْنَا

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

## و ز ر (root_001643): 94:2 وِزْرَكَ

- **B001** koruyucu sığınak — koruyucu sığınak; sığınılan dağ veya güvenli yer
  الوزر الملجأ (maqayis;sihah)؛ الوزر الجبل يلجأ إليه (ayn)؛ الجبل الذي يلتجأ إليه وكل ما التجأت إليه وتحصنت به (tahdhib)؛ الملجأ الذي يلتجأ إليه من الجبل (mufradat)
- **B002** ağır yük ve ahlaki sorumluluk — ağır yük; kişiyi bağlayan ahlaki sorumluluk · bir şeyi yüklenip taşımak · kötülük işlemek ya da onun yükünü taşımak · üzerinde kötülük ve sorumluluk yükü bulunan · savaşın doğurduğu kötülükler ya da savaşanların sorumluluk yükleri
  الآخر الثقل في الشيء (maqayis)؛ الوزر حمل الرجل إذا بسط ثوبه فجعل فيه المتاع وحمله (maqayis)؛ الوزر الحمل الثقيل من الإثم (ayn)؛ الوزر الإثم والثقل والكارة (sihah)؛ قد وزرت الشيء أي حملته والآثام تسمى أوزارا (tahdhib)؛ الوزر الثقل ويعبر بذلك عن الإثم (mufradat)
- **B003** silah ve savaş donanımı — silah ve korunma aracı · savaş silahları ve donanımı
  الوزر السلاح والجمع أوزار (maqayis)؛ أوزار الحرب آلتها (ayn;mufradat)؛ الوزر السلاح (sihah)؛ الأوزار ههانا السلاح وآلة الحرب (tahdhib)
- **B004** yük paylaşan güvenilir yönetici yardımcısı — hükümdarın iş yükünü paylaşan başyardımcı ve danışman · yönetici başyardımcılığı görevi · birini yönetici başyardımcısı yapmak · birine işinde yardım etmek
  الوزير سمي به لأنه يحمل الثقل عن صاحبه (maqayis)؛ الوزير الذي يستوزره الملك فيستعين برأيه (ayn)؛ الوزير الموازر لأنه يحمل عنه وزره (sihah)؛ وزير الخليفة الذي يعتمد على رأيه ويلتجئ إليه (tahdhib)؛ الوزير المتحمل ثقل أميره والموازرة المعاونة (mufradat)
- **B005** ele geçirip alıkoymak veya götürmek — bir şeyi ele geçirip alıkoymak veya alıp götürmek · bir şeyi ele geçirmek ve denetimine almak · bir şeyi alıp götürmek ya da kendine ayırmak · topluluğun paylarını alıp götürme
  أوزر فلان الشيء أحرزه (maqayis)؛ وزرت الشيء أحرزته (sihah)؛ لا توزر حظوظة القوم وقد أوزر الشيء ذهب به واغتباه ويقال قد استوزره (tahdhib)
- **B006** birini yenmek — birini yenmek, ona üstün gelmek
  وزرته غلبته (maqayis)؛ وزرت فلانا غلبته (sihah)
- **B007** bele sarılan giysiyi kuşanmak — bele sarılan alt giysisini kuşanmak
  اتزر الرجل ركب الموزر وهو افتعل منه (sihah)؛ الاتزار فهو من الوزر يقال اتزرت وما اتجرت ووزرت أيضا (tahdhib)

## ECHO ز و ر (root_000654): for 94:2 وِزْرَكَ: withheld observed target; not identity

- **B001** yönünden sapma ve yana eğilme — yönünden sapma, yana eğilme · bir şeyden yana dönüp uzaklaşmak · bir şeyden yana sapıp yönünü değiştirmek · doğrultusundan sapmış veya yana eğri · bakışı veya duruşu yana eğik
  أصل واحد يدل على الميل والعدول (maqayis)؛ الزور الميل (maqayis)؛ مفازة زوراء أي مائلة عن القصد والسمت (ayn)؛ الزور بالتحريك الميل وهو الصعر (sihah)؛ تزاور عنه تزاورا كله بمعنى عدل عنه وانحرف (sihah)؛ الزوراء البئر البعيدة العقر (sihah)؛ الزوراء القدح (sihah)؛ القوس زوراء لميلها (sihah)؛ تتزاور عن كهفهم أي تميل (mufradat)
- **B002** gerçekten sapmış yalan veya batıl nesne — yalan ve batıl · yalan söz · tanrılaştırılıp tapınılan batıl nesne
  الزور الكذب لأنه مائل عن طريقة الحق (maqayis)؛ الصنم زور (maqayis)؛ الزور قول الكذب وشهادة الباطل (ayn)؛ الزور الكذب (sihah)؛ الزور أيضا الزون وهو كل شيء يتخذ ربا ويعبد من دون الله (sihah)؛ قيل للكذب زور لكونه مائلا عن جهته (mufradat)؛ يسمى الصنم زورا (mufradat)
- **B003** birini görmek için yanına gitme — birini görmeye gitmek · ziyaretçi · ziyaretçiler veya ziyaretçi topluluğu · ziyaret · ziyaret ettirmek · ziyarete çağırmak · birbirini ziyaret etmek · ziyaret veya ziyaret yeri · ziyaretçiyi ağırlama · kadınlarla sık görüşüp sohbet eden erkek
  الزائر لأنه إذ زارك فقد عدل عن غيرك (maqayis)؛ التزوير كرامة الزائر (maqayis)؛ الزور الذي يزورك واحدا كان أو جميعا (ayn)؛ زرته أزوره زورا وزيارة وزوارة (sihah)؛ التزوير كرامة الزائر (sihah)؛ الزير من الرجال الذي يحب محادثة النساء ومجالستهن سمي بذلك لكثرة زيادته لهن (sihah)؛ زرت فلانا تلقيته بزوري أو قصدت زوره (mufradat)؛ رجل زائر وقوم زور (mufradat)
- **B004** göğsün üst veya orta bölümü ve buradaki eğrilik — göğsün üst veya orta bölümü · göğsü eğri · göğsü eğri olduğu için düzeltilen deve · devenin göğsüne bağlanan kayış veya hayvanın ağzını çevirmeye yarayan araç
  الزور وسط الصدر (ayn)؛ الزور ميل في وسط الصدر (ayn)؛ كلب أزور استدق جوشن زوره (ayn)؛ الزيار سفاف يشد به الرحل إلى صدر البعير (ayn)؛ الزور أعلى الصدر (sihah)؛ الزور في صدر الفرس دخول إحدى الفهدتين وخروج الأخرى (sihah)؛ الزيار ما يزير به البيطار الدابة (sihah)؛ الزور أعلى الصدر (mufradat)؛ الزور ميل في الزور (mufradat)؛ الزور القوي الشديد من الزور وهو أعلى الصدر شاذ عن الأصل (maqayis)
- **B005** başvurulan önder veya dayanak — topluluğun önderi veya işlerini yöneten kişi · dayanacağı görüşü veya başvuracağı mercii yok
  لرئيس القوم وصاحب أمرهم الزوير وذلك أنهم يعدلون عن كل أحد إليه (maqayis)؛ رجل ليس له زور أي ليس له صيور يرجع إليه (maqayis)؛ ماله زور ولا صيور أي رأي يرجع إليه (sihah)؛ الزوير زعيم القوم (sihah)
- **B006** önceden hazırlayıp düzeltme ve süsleme — bir şeyi zihninde hazırlamak · sözü konuşmadan önce düzeltip düzenlemek · bir şeyi düzeltip güzelleştirme veya yalanı süsleme
  زور الشيء في نفسه هيأه (maqayis)؛ الإنسان يزور كلاما أي يقومه قبل أن يتكلم به (ayn)؛ لم يشتق تزوير الكلام منه ولكن من تزوير الصدر (ayn)؛ التزوير تزيين الكذب (sihah)؛ زورت الشيء حسنته وقومته (sihah)
- **B007** şiddetli yol alış — şiddetli yol alış
  الزور مثال الهجف السير الشديد (sihah)
- **B008** ince tel veya kiriş; ayrıca keten — 
  الزير من الأوتار الدقيق؛ والزير الكتان (sihah)

## ن ق ض (root_001543): 94:3 أَنقَضَ

- **B001** kurulu bütünü çözme, geçersiz kılma veya karşı savla çürütme — kurulmuş bir bütünü çözme veya sökme · antlaşmayı ya da bağlayıcı sözü bozma · pekiştirilmiş yeminleri bozma · sökülmüş yapı, ip veya kumaş parçası · sökülmüş kıl ipi veya ipekli dokuma sökme işi · ipekli dokuma söken usta · söz veya şiirle karşı çıkıp çürütme · önceki bir şiiri veya sözü çürüten karşı şiir ya da yazı · aynı durumda birlikte doğru olamayan iki önerme
  يدل على نكث شيء؛ نقضت الحبل والبناء؛ نقض العهد؛ المناقضة في الشعر (maqayis)؛ إفساد ما أبرمت من حبل أو بناء؛ النقاض الذي ينقض الدمقس (ayn;tahdhib)؛ ما نقض من ثوب صوف أو إبريسيم فهو نقض ونكث (tahdhib)؛ نقض البناء والحبل والعهد؛ المناقضة في القول (sihah)؛ نقضت البناء والحبل والعقد؛ استعير نقض العهد؛ لا تنقضوا الأيمان؛ المناقضة في الكلام والشعر (mufradat)
- **B002** yolculukların gücünü tükettiği deve — yolculukların güçten düşürdüğü deve · yolculukların güçten düşürdüğü dişi deve veya binek hayvanı
  البعير المهزول نقض كأن الأسفار نقضته (maqayis)؛ الجمل والناقة اللذان هزلتهما الأسفار (ayn;tahdhib)؛ البعير الذي أضناه السفر وكذلك الناقة (sihah)؛ البعير المهزول (mufradat)
- **B003** yer mantarı çıkışıyla yarılan toprak yüzü — yer mantarının çıkışıyla yarılmış toprak yüzü · toprağın yer mantarı çıkarken yarılıp açılması
  النقض منتقض الكمأة من الأرض (maqayis;ayn)؛ الموضع الذي ينتقض عن الكمأة؛ تنقضت الأرض عن الكمأة أي تفطرت (sihah)؛ نقضت وجه الأرض نقضا فانتقضت الأرض (tahdhib)؛ منتقض الأرض من الكمأة نقض (mufradat)
- **B004** iyileşme veya toparlanma sonrası yeniden bozulma — iyileşme veya toparlanma sonrası yeniden bozulma · kapanmış çıbanın yeniden açılması · iyileşmiş yaranın yeniden açılıp bozulması · toparlanmış işin veya sınır düzeninin yeniden bozulması
  انتقضت القرحة (maqayis;mufradat)؛ الانتقاض أن يعود الجرح بعد البرء وكذلك انتقاض الأمور والثغور (ayn)؛ الانتقاض الانتكاث (sihah)؛ انتقض الجرح بعد البرء؛ انتقض الأمر بعد التئامه؛ انتقض أمر الثغر (tahdhib)
- **B005** baskı altındaki eklem veya yük aracının gıcırtısı — eklem, parmak, kaburga veya yüklü sırt gıcırtısı · çekme kupasının emilirken çıkardığı ses · yükün sırtı ses çıkaracak kadar ağırlaştırması · yük taşıma düzenekleri ile eyerlerin gıcırtısı · kemiklerinin ses çıkarması
  صوت المفاصل نقيضها (maqayis)؛ النقيض صوت الأصابع والمفاصل والأضلاع؛ نقيض المحجمة صوتها (ayn)؛ أنقض الحمل ظهره أي أثقله؛ النقيض صوت المحامل والرحال (sihah)؛ الظهر إذا أثقله حمله سمع له نقيض؛ كل صوت لمفصل أو إصبع أو ضلع فهو نقيض (tahdhib)؛ أنقض ظهرك؛ نقيض المفاصل صوتها (mufradat)
- **B006** ince hayvan sesi veya hayvan yönlendiren dil şaklatması — tavuğun ses çıkarması · kartalın ses çıkarması · yavru kuşun ince ötmesi · genç deveyi yönlendirmeye yarayan dil şaklatması · keçileri çağıran dil sesi · dilin ucunu üst damağa değdirip eşek için ses çıkarma · sakızın çiğnenirken çıkardığı ses · deve yavrularının sesleri · civcivlerin sesleri veya bunlara benzeyen sesler
  أنقضت الدجاجة صوتت؛ الإنقاض زجر القعود (maqayis)؛ أنقضت بالحمار؛ أصوات الفراريج والعقاب (ayn)؛ أنقضت العقاب وكذلك الدجاجة؛ الانقاض أصوات صغار الابل؛ أنقضت بالمعز إنقاضا دعوت بها (sihah)؛ أنقضت إنقاضا بالمعز إذا دعوته؛ أنقض الفرخ؛ أصوات أواخر الميس إنقاض الفراريج؛ أنقضت بالحمار (tahdhib)؛ انتقضت الدجاجة صوتت؛ الإنقاض صوت لزجر القعود (mufradat)
- **B007** türü belirtilmemiş bir bitki — bir bitki adı
  النقاض نبات (ayn;tahdhib)
- **B008** aygırın organını salıp tam sertleşememesi [kalıp] — aygırın organını salıp tam sertleşememesi
  في نوادر الأعراب: نقض الفرس ورفض إذا أدلى ولم يستحكم إنعاظه (tahdhib)

## ظ ه ر (root_000970): 94:3 ظَهْرَكَ

- **B001** açığa çıkıp belirginleşmek — açığa çıkmak, belirip anlaşılır olmak · görünür ve dışta olan
  ظهر الشيء إذا انكشف وبرز (maqayis)؛ الظهور بدو الشيء الخفي (ayn;tahdhib)؛ ظهر الشيء ظهورا تبين (sihah)؛ أن يحصل شيء على ظهر الأرض فلا يخفى (mufradat)
- **B002** sırt ve arka yüz — sırt; karın ya da ön tarafın karşıtı olan arka yüz · sırtı güçlü kimse · sırtı ağrıyan veya incinmiş kimse · birinin sırtına vurmak veya zarar vermek · kolları arkada bağlayan veya yere düşüren tutuş
  ظهر الإنسان خلاف بطنه (maqayis)؛ الظهر خلاف البطن من كل شيء (ayn;sihah;tahdhib)؛ الظهر الجارحة وجمعه ظهور (mufradat)؛ رجل مظهر شديد الظهر ورجل ظهر يشتكي ظهره (maqayis;sihah;tahdhib;mufradat)
- **B003** yüksek ya da dışta kalan yüz — yerin yüksek veya açıkta kalan yüzü · dış ya da üst yüz; astarın karşıtı
  الظهر من الأرض ما غلط وارتفع (ayn;tahdhib)؛ الظاهرة كل أرض غليظة مشرفة (ayn)؛ الظواهر أشراف الأرض (sihah;tahdhib)؛ ظهر الأرض وبطنها (mufradat)؛ الظهارة خلاف البطانة (ayn;sihah;tahdhib)
- **B004** öğle vakti ve ona bağlı eylemler — öğle vakti ve o vakitte kılınan namaz · gün ortası veya öğle sıcağı · öğle vaktine girmek veya o sırada yol almak · hayvanların her gün öğleyin suya gelmesi
  وقت الظهر والظهيرة أظهر أوقات النهار (maqayis)؛ الظهر ساعة الزوال وصلاة الظهر والظهيرة حد انتصاف النهار (ayn;tahdhib)؛ الظهر بعد الزوال والظهيرة الهاجرة (sihah)؛ صلاة الظهر والظهيرة وقت الظهر وأظهر فلان حصل في ذلك الوقت (mufradat)؛ الظاهرة أن ترد كل يوم ظهرا (sihah;tahdhib)
- **B005** yük bineği ve yedek deve — yük taşıyan binek veya deve topluluğu · gerektiğinde kullanılmak üzere hazır tutulan deve
  الركاب الظهر لأن الذي يحمل منها الشيء ظهورها (maqayis)؛ الظهر الركاب تحمل الأثقال في السفر (ayn;tahdhib)؛ الظهر الركاب وبنو فلان مظهرون (sihah)؛ يعبر عن المركوب بالظهر وظهري معد للركوب (mufradat)؛ البعير الظهري العدة للحاجة (sihah;tahdhib)
- **B006** yardım edip güçlendirmek — yardımcı, destekçi · yardımlaşma ve destek olma · ondan yardım alıp güçlenmek
  الظهير المعين كأنه أسند ظهره إلى ظهرك (maqayis)؛ الظهير العون والمظاهر المعاون وهما يتظاهران أي يتعاونان (ayn)؛ الظهير المعين والمظاهرة المعاونة والتظاهر التعاون واستظهر به استعان به (sihah)؛ ظهير في معنى ظهراء أي أعوان وظاهروا أي عاونوا (tahdhib)؛ ظاهرته عاونته وما له منهم من ظهير أي معين (mufradat)
- **B007** üzerine çıkmak veya üstün gelmek [kalıp] — üstün gelmek veya üzerinde güç kurmak · damın veya yüzeyin üstüne çıkmak
  الظهور الغلبة (maqayis)؛ الظهور الظفر بالشيء (ayn;tahdhib)؛ ظهرت على الرجل غلبته وظهرت البيت علوته (sihah)؛ ظهر على الحائط وعلى السطح وظهر على الشيء إذا غلبه وعلاه (tahdhib)؛ ظهر عليه غلبه وليظهره على الدين كله (mufradat)
- **B008** bilgiye ulaşıp öğrenmek [kalıp] — bir şeyi öğrenmek veya bulup ortaya çıkarmak
  ظهرت على كذا إذا اطلعت عليه (maqayis)؛ والله أظهرنا عليه أي أطلعنا (ayn)؛ أظهرني الله على ما سرق مني أي أعثرني عليه وظهرت على الأمر (tahdhib)؛ فلا يظهر على غيبه أحدا أي لا يطلع عليه (mufradat)
- **B009** çıkık göz — çökük gözün karşıtı olan çıkık göz
  الظاهرة العين الجاحظة (maqayis)؛ الظاهرة العين الجاحظة وهي خلاف الغائرة (ayn)؛ الظاهرة من العيون الجاحظة (sihah)؛ العين الظاهرة التي ملأت نقرة العين وهي خلاف الغائرة (tahdhib)
- **B010** eşe yönelik benzetmeli yasaklama sözü — kocanın eşini kendisine yasak saydığını bildiren geleneksel söz · eşini annesinin sırtına benzeterek kendisine yasak sayma sözü
  الظهار قول الرجل لامرأته أنت علي كظهر أمي (maqayis;sihah;mufradat)؛ مظاهرة الرجل امرأته إذا قال هي علي كظهر أمي أو كظهر ذات رحم محرم (ayn)؛ وأوجبت الكفارة على من ظاهر من امرأته (tahdhib)
- **B011** kanadın dış tüyleri — kanadın dıştan görünen tüyleri veya tüy sapının sırt yönündeki parçası
  الظهار من الريش ما يظهر منه في الجناح (maqayis)؛ الظهار من الريش الذي يظهر من ريش الطائر وهو في الجناح (ayn;tahdhib)؛ الظهار ما جعل من ظهر عسيب الريشة والظهران الجانب القصير من الريش (sihah;tahdhib)
- **B012** geriye atıp önemsememek — arkaya atılıp unutulan şey · bir isteği önemsemeyip geriye atmak
  الظهري كل شيء تجعله بظهر أي تنساه (maqayis)؛ الظهري الشيء تنساه وتغفل عنه (ayn;tahdhib)؛ لا تجعل حاجتي بظهر أي لا تنسها (sihah)؛ ظهرت بكذا أي خلفته ولم ألتفت إليه (mufradat)
- **B013** ayıbı kişiden uzak olmak [kalıp] — ayıbı sana yapışmayan, senden uzak söz veya durum
  أمر ظاهر عنك عاره أي زائل (maqayis;sihah)؛ ظهر عني هذا العيب أي نبا عني ولم يعلق بي (tahdhib)؛ تلك شكاة ظاهر عنك عارها (maqayis;sihah;tahdhib)
- **B014** ev eşyası ve yedek mallar — ev eşyası ve gerektiğinde yararlanılan mallar
  الظهرة متاع البيت وأحسب هذه مستعارة من الظهر أيضا لأن الإنسان يستظهر بها (maqayis)؛ الظهرة بالتحريك متاع البيت (sihah)؛ الظهرة ما في البيت من المتاع والثياب (tahdhib)
- **B015** kara yolu ve dıştaki yüksek kesim — deniz yolunun karşıtı olan kara yolu · Mekke'nin dış veya yüksek kesimlerinde yaşayan Kureyşliler
  طريق الظهر (ayn;sihah;tahdhib)؛ سلكنا الظهر يريدون طريق البر (maqayis)؛ قريش الظواهر سموا بذلك لأنهم ينزلون ظاهر مكة (maqayis;sihah;tahdhib)؛ ظاهرة الجبل أعلاه وظاهرة كل شيء أعلاه (tahdhib)
- **B016** güç alınan destekçi topluluğu — kişinin güç aldığı yardımcıları ve yakın topluluğu
  جاء فلان في ظهرته وناهضته أي قومه (maqayis;sihah)؛ الظهرة ظهر الرجل وأنصاره (tahdhib)؛ الظهراء أعوان النبي (tahdhib)
- **B017** topluluk veya zaman sınırları arasında [kalıp] — aralarında, topluluğun ortasında · iki gün veya iki zaman sınırı arasında
  أنا بين ظهرانيهم وظهريهم (ayn)؛ نازل بين ظهريهم وظهرانيهم (sihah)؛ نزل فلان بين ظهرينا وظهرانينا وأظهرنا (tahdhib)؛ بين الظهرانين معناه في اليومين أو في الأيام (sihah;tahdhib)
- **B018** bir konuyu her yönüyle incelemek [kalıp] — bir konuyu evirip çevirerek her yönüyle incelemek
  قلبت الأمر ظهرا لبطن (ayn;tahdhib)
- **B019** ezberleyip bellekten söylemek — kitaba bakmadan, ezberden · ezberlemek ve kitaba bakmadan okumak
  تكلمت بذلك عن ظهر غيب (ayn;tahdhib)؛ ظهر القلب حفظ من غير كتاب (ayn;tahdhib)؛ استظهر الشيء أي حفظه وقرأه ظاهرا (sihah)؛ حمل القرآن على ظهر لسانه (tahdhib)
- **B020** iki katmanı üst üste getirmek [kalıp] — iki giysiyi veya iki zırhı üst üste getirmek
  ظاهر بين ثوبين أي طارق بينهما وطابق (sihah)؛ ظاهر فلان بين ثوبين وبين درعين إذا طابق بينهما (tahdhib)
- **B021** yedek hazırlayıp güvence sağlamak — gerektiğinde kullanılmak üzere hazır tutulan deve · yedek hazırlayarak önlem almak ve güvence sağlamak
  البعير الظهري العدة للحاجة (sihah;tahdhib)؛ الاستظهار في كلامهم الاحتياط والاستيثاق (tahdhib)؛ استظهر ببعيرين ظهريين محتاطا بهما (tahdhib)
- **B022** birbirine sırt çevirip uzaklaşmak — birbirine sırt çevirip uzaklaşmak
  تظاهر القوم إذا تدابروا (maqayis;sihah)؛ كل واحد منهما أدبر عن صاحبه وجعل ظهره إليه (maqayis)
- **B023** karşılıksız veya artandan vermek [kalıp] — karşılık beklemeden, kendiliğinden vermek · geçim gereklerinden artan bolluktan vermek
  عن ظهر يد معناه ابتداء من غير مكافأة (tahdhib)؛ ما كان عن ظهر غنى عن فضل عيال (tahdhib)
- **B024** bir şeyle övünmek [kalıp] — bir şeyle övünmek ve onu övünç dayanağı yapmak
  ظهرت به أي افتخرت به (tahdhib)؛ واظهر ببزته أي افخر به على غيره (tahdhib)

## ر ف ع (root_000582): 94:4 وَرَفَعْنَا

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

## ذ ك ر (root_000516): 94:4 ذِكْرَكَ

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

## ع س ر (root_001012): 94:5 ٱلْعُسْرِ, 94:6 ٱلْعُسْرِ

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

## ي س ر (root_001694): 94:5 يُسْرًا, 94:6 يُسْرًا

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

## ف ر غ (root_001147): 94:7 فَرَغْتَ

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

## ن ص ب (root_001507): 94:7 فَٱنصَبْ

- **B001** dikme, dik durma ve yükselme — bir şeyi dikmek veya dik konuma kaldırmak · boynuzları dik olan · boynuzu dik veya göğsü yüksek dişi hayvan · havaya yükselmiş toz · perdeyi kaldırmak · kuş avlamak için tuzak kurmak · kazanın üzerine konduğu demir destek · dikili direk veya sütun
  أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)
- **B002** tapınma veya adak kesme taşı — tapınılan veya üzerinde adak kesilen dikili taş · tapınılan ya da adak kesilen dikili taşlar
  النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)
- **B003** sınır işareti veya kuyu-havuz taşı — dikili işaret veya havuz kenarı taşı · kuyu ya da havuz ağzının çevresine dizilen taşlar · taşlardan kurulmuş havuz · topluluk veya sınır için dikilmiş işaret
  النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)
- **B004** yorgunluk ve yıpratıcı sıkıntı — yorgunluk, bitkinlik, zahmet ve sıkıntı · hastalığın verdiği bitkinlik · beni yordu ve huzursuz etti · yorucu veya yorgunluk içindeki
  النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)
- **B005** belirlenmiş pay — pay veya bir şeyden ayrılan belirli bölüm · pay
  النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)
- **B006** temel veya sabit başvuru noktası — bir şeyin temeli ve dönülen başvuru noktası · bıçağın sapı veya arka bölümü · mal için mali yükümlülük doğuran alt miktar · köken, soy ve aileden gelen saygınlık · güneşin battığı ve döndüğü yer
  نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)
- **B007** dil bilgisinde yükleme konumu [kalıp] — çekimde üst konumun karşıtı olan yükleme konumu · yükleme konumuna getirilmiş sözcük
  في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)
- **B008** birine savaş veya düşmanlıkla karşı çıkma — birine savaş veya düşmanlıkla karşı çıkmak · ona düşman olmak veya düşmanlık yöneltmek
  ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)
- **B009** özel bir şarkı veya ezgi türü — yolcuların söylediği özel ezgi türü · hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi · yolcu ezgisini söyledi
  النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)
- **B010** yolculuğu yumuşak sürdürme veya artırma — gün boyunca yumuşak biçimde ilerlediler · yol alışlarını yükseltip artırdılar
  نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)

## ر ب ب (root_000532): 94:8 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 94:8 رَبِّكَ: withheld observed target; not identity

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

## ر غ ب (root_000575): 94:8 فَٱرْغَب

- **B001** isteyerek yönelmek veya istemeyip yüz çevirmek — istek, yöneliş ve isteme · bir şeyi istemek ve ona yönelmek · bir şeye istekle yönelmek · bir şeyi istememek ve ondan yüz çevirmek · istenen ve aranan şey · istenmeyen ve kaçınılan şey · onu bilerek terk eden · ondan uzaklaşma yolu veya imkanı · ona istek duymak · birini bir şeyi istemeye özendirmek · isteğim ve dileğim sanadır
  الرغبة في الشيء الإرادة له؛ رغبت عنه إذا لم ترده (maqayis)؛ إليك الرغباء ومنك النعماء وأنا رغيب عنه إذا تركته عمدا (ayn)؛ رغبت في الشيء إذا ملت إليه ورغبت عنه إذا صددت عنه (jamhara)؛ رغبت في الشئ إذا أردته ورغبت عن الشئ إذا لم ترده وزهدت فيه (sihah)؛ رغب فيه وإليه يقتضي الحرص عليه ورغب عنه اقتضى صرف الرغبة عنه والزهد فيه (mufradat)
- **B002** iç hacim, alan veya hareket açıklığı bakımından genişlik — içi geniş veya geniş hacimli · geniş havuz · içi geniş su tulumu · geniş adımlı veya geniş koşulu at · geniş arazi veya ancak bol yağmurda su akıtan yumuşak toprak · genişlemek veya arazinin geniş ve yumuşak hale gelmesi · bir yerin veya nehrin adı · bu genişlik anlamından türemiş bir yer adı
  الشيء الرغيب الواسع الجوف وحوض رغيب وسقاء رغيب وفرس رغيب الشحوة والرغاب الأرض الواسعة (maqayis)؛ رجل رغيب واسع الجوف أكول وحوض رغيب أي واسع (ayn)؛ فرس رغيب الشحوة كثير الأخذ بقوائمه من الأرض وموضع رغيب واسع ومواضع رغاب (jamhara)؛ حوض رغيب وسقاء رغيب وفرس رغيب الشحوة والرغاب الأرض اللينة التي لا تسيل إلا من مطر كثير (sihah)؛ أصل الرغبة السعة في الشيء وحوض رغيب وفلان رغيب الجوف وفرس رغيب العدو (mufradat)
- **B003** yemede aşırı istek ve oburluk — obur ve çok yiyen adam · oburluk ve yeme düşkünlüğü
  رجل رغيب واسع الجوف أكول وفي الحديث الرغب شؤم (ayn)؛ رجل رغيب نهم شديد الأكل (jamhara)؛ الرغب بالضم الشره وقد رغب بالضم رغبا فهو رغيب (sihah)
- **B004** bol ve istenen bağış — çok ve istenen bağış; çoğulda bol bağışlar
  الرغيبة العطاء الكثير والجمع رغائب (maqayis)؛ رغيبة أي مرغوب فيها وجمعها رغائب (ayn)؛ الرغيبة العطاء الكثير الذي يرغب في مثله والجمع رغائب (jamhara)؛ الرغيبة العطاء الكثير والجمع الرغائب (sihah)؛ الرغيبة العطاء الكثير إما لكونه مرغوبا فيه وإما لسعته (mufradat)



===== _commentary/v16/work/s094/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s094/reader_a_pilot.md)

# S094 Semantic Channel Discovery

## Parent Channels

### 1. Constraint, Strain, and Release
- Semantic invariant: A constraining load produces bodily, material, or economic pressure until it is lowered, opened, or met by ease and capacity.
- Surface relation: direct; 94:2 وَضَعْنَا/وِزْرَكَ, 94:3 أَنقَضَ/ظَهْرَكَ, and 94:5-6 ٱلْعُسْرِ/يُسْرًا.
- Surprising reach: The same pressure-and-release pattern extends from a creaking back to insolvency, obstruction, and moral burden.

#### Subchannel A. The Loaded Torso and Setting Down
- Reading type: mixed
- Scene or process: A burden presses on the torso until it is lowered and the load-bearing frame is released.
- Active motifs: setting down a load `و ض ع:B001/m01`; heavy burden `و ز ر:B002/m01`; guilt borne as weight `و ز ر:B002/m02`; chest `ص د ر:B001/m01`; back `ظ ه ر:B002/m01`; creaking under weight `ن ق ض:B005/m01`
- Ayah anchors: 94:1 صَدْرَكَ; 94:2 وَضَعْنَا/وِزْرَكَ; 94:3 أَنقَضَ/ظَهْرَكَ
- Synthesis: The chest and back form one load-bearing body, the burden can be both material and culpable, and its removal reverses the creaking strain produced by sustained weight.

#### Subchannel B. Hardness Opening into Ease
- Reading type: mixed
- Scene or process: A hard condition resists passage before becoming workable and easy.
- Active motifs: hardship and severity `ع س ر:B001/m01`; material or personal hardness `ذ ك ر:B002/m01`; opening and ease `ي س ر:B001/m01`
- Ayah anchors: 94:4 ذِكْرَكَ; 94:5-6 ٱلْعُسْرِ/يُسْرًا
- Synthesis: Difficulty behaves like hardness in a material or a person, while ease is the opening by which resistance gives way to readiness.

#### Subchannel C. Insolvency, Exaction, and Restored Means
- Reading type: latent/lexical
- Scene or process: Loss and creditor pressure narrow a debtor's means, while affluence and surplus reopen economic room.
- Active motifs: insolvency `ع س ر:B002/m01`; harsh demand on a debtor `ع س ر:B003/m01`; capital loss or discount `و ض ع:B004/m01`; confiscation `ص د ر:B005/m01`; affluence `ي س ر:B003/m01`; giving from surplus `ظ ه ر:B023/m01`
- Ayah anchors: 94:1 صَدْرَكَ; 94:2 وَضَعْنَا; 94:3 ظَهْرَكَ; 94:5-6 ٱلْعُسْرِ/يُسْرًا
- Synthesis: Property can be diminished, exacted, or confiscated until the debtor is confined by scarcity; restored means and surplus reverse that confinement and enable unreciprocated giving.

#### Subchannel D. Obstruction and Usable Capacity
- Reading type: latent/lexical
- Scene or process: A tangled or resistant undertaking is met by sufficient power, preparation, and ease.
- Active motifs: obstruction and complication `ع س ر:B004/m01`; prevention `ء ل ي:B009/m01`; ability and capacity `ء ل ي:B011/m01`; precautionary reserve `ظ ه ر:B021/m01`; readiness and facilitation `ي س ر:B001/m01`
- Ayah anchors: 94:3 ظَهْرَكَ; 94:5-6 ٱلْعُسْرِ/يُسْرًا; 94:8 إِلَىٰ
- Synthesis: Resistance bends an undertaking away from completion, whereas reserve, capacity, and facilitation supply the means to straighten its course.

### 2. Attention, Effort, and Directed Desire
- Semantic invariant: Available attention and strength are gathered around an undertaking, an object of desire, or a governing endpoint.
- Surface relation: direct; 94:7 فَرَغْتَ/فَٱنصَبْ and 94:8 إِلَىٰ/رَبِّكَ/فَٱرْغَب.
- Surprising reach: Emptiness after completion is not mere cessation; it becomes the cleared space for renewed effort and focused inclination.

#### Subchannel A. Completion and Deliberate Re-engagement
- Reading type: mixed
- Scene or process: Finishing one occupation clears attention for a newly chosen task pursued with effort rather than slackness.
- Active motifs: freedom after work `ف ر غ:B001/m01`; deliberate devotion to one matter `ف ر غ:B006/m01`; toil and exhaustion `ن ص ب:B004/m01`; exertion `ء ل ي:B010/m01`; absence of slackness `ء ل ي:B008/m01`; hurried work `م ع ع:B004/m01`
- Ayah anchors: 94:5-6 مَعَ; 94:7 فَرَغْتَ/فَٱنصَبْ; 94:8 إِلَىٰ
- Synthesis: Completion empties the field of prior work, deliberate focus fills it again, and the contrast between sustained exertion and haste defines how the new undertaking proceeds.

#### Subchannel B. Inclination, Aversion, and Appetite
- Reading type: latent/lexical
- Scene or process: Desire expands toward a wanted object, intensifies as appetite, or turns away in aversion.
- Active motifs: inclination toward an object `ر غ ب:B001/m01`; aversion from an object `ر غ ب:B001/m02`; expansive worldly desire `ش ر ح:B005/m01`; voracious appetite `ر غ ب:B003/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:8 فَٱرْغَب
- Synthesis: رغبة supplies a directional force that can approach or withdraw, while شرح renders its acquisitive form as an inner expansion and appetite renders it bodily.

#### Subchannel C. Aspiration toward a Governing End
- Reading type: surface-primary
- Scene or process: A desiring subject turns toward an endpoint defined by lordship.
- Active motifs: endpoint and attained limit `ء ل ي:B001/m01`; divine lordship `ر ب ب:B001/m01`; desire directed toward `ر غ ب:B001/m01`
- Ayah anchors: 94:8 إِلَىٰ/رَبِّكَ/فَٱرْغَب
- Synthesis: The endpoint is not an empty destination: it is the Lord toward whom رغبة is oriented, so direction, authority, and aspiration form one complete relation.

### 3. Presence in Perception and Memory
- Semantic invariant: What is hidden or absent becomes present through appearance, discovery, recollection, or preservation.
- Surface relation: indirect; 94:1 نَشْرَحْ, 94:3 ظَهْرَكَ, and 94:4 ذِكْرَكَ.
- Surprising reach: The back-root links visible emergence and investigative discovery with the opposite act of placing something behind oneself and forgetting it.

#### Subchannel A. Appearance, Discovery, and Examination
- Reading type: latent/lexical
- Scene or process: An initially hidden matter becomes visible, is found, and is turned through its aspects for understanding.
- Active motifs: visible emergence `ظ ه ر:B001/m01`; discovery and finding `ظ ه ر:B008/m01`; examining a matter from every side `ظ ه ر:B018/m01`
- Ayah anchors: 94:3 ظَهْرَكَ
- Synthesis: Appearance supplies the perceptible object, discovery brings the knower into contact with it, and examination turns that object until its several faces are understood.

#### Subchannel B. Recollection, Reminder, and Forgetting
- Reading type: latent/lexical
- Scene or process: A remembered matter is retained in the heart, renewed by a reminder, or lost by being cast behind the subject.
- Active motifs: recollection after absence `ذ ك ر:B003/m01`; reminder `ذ ك ر:B009/m01`; memorization by heart `ظ ه ر:B019/m01`; placing behind and forgetting `ظ ه ر:B012/m01`; preservation `ش ر ح:B006/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:3 ظَهْرَكَ; 94:4 ذِكْرَكَ
- Synthesis: Memory keeps an object inwardly present, reminders restore that presence, and forgetting reverses the process by moving the object behind the field of attention.

### 4. Rank, Stewardship, and Power
- Semantic invariant: Vertical and load-bearing relations become social relations of elevation, rule, assistance, dominance, and defeat.
- Surface relation: direct; 94:4 رَفَعْنَا/ذِكْرَكَ, with indirect extensions from 94:2 وَضَعْنَا/وِزْرَكَ, 94:3 ظَهْرَكَ, and 94:8 رَبِّكَ.
- Surprising reach: Raising a name extends into presenting a case before authority, commanding a vessel, carrying a ruler's burden, and prevailing over an opponent.

#### Subchannel A. Public Elevation and Abasement
- Reading type: mixed
- Scene or process: A person's standing rises through reputation and honor or falls through abasement and attached shame.
- Active motifs: elevation of rank `ر ف ع:B002/m01`; honorable repute `ذ ك ر:B007/m01`; lowered status or humility `و ض ع:B005/m01`; pride and boasting `ظ ه ر:B024/m01`; reproach falling away `ظ ه ر:B013/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 ظَهْرَكَ; 94:4 رَفَعْنَا/ذِكْرَكَ
- Synthesis: Rank is treated as vertical position: reputation raises, abasement lowers, pride displays the raised state, and the removal of reproach releases the person from a contrary social weight.

#### Subchannel B. Authority and Burden-sharing Aides
- Reading type: latent/lexical
- Scene or process: A ruler, owner, or captain directs an ordered domain while ministers and helpers carry part of its burden.
- Active motifs: ownership and mastery `ر ب ب:B001/m02`; captain of sailors `ر ب ب:B017/m01`; minister who carries another's load `و ز ر:B004/m01`; supporting ally `ظ ه ر:B006/m01`; body of supporters `ظ ه ر:B016/m01`; presenting a person or case to authority `ر ف ع:B004/m01`
- Ayah anchors: 94:2 وِزْرَكَ; 94:3 ظَهْرَكَ; 94:4 رَفَعْنَا; 94:8 رَبِّكَ
- Synthesis: Command is distributed through a hierarchy: the master or captain governs, a matter is advanced before authority, and aides make rule sustainable by bearing delegated weight.

#### Subchannel C. Ascendancy and Defeat
- Reading type: latent/lexical
- Scene or process: Sufficient power produces elevation over an opponent, while the defeated party is overcome.
- Active motifs: prevailing and rising over `ظ ه ر:B007/m01`; overcoming a person `و ز ر:B006/m01`; power and ability `ء ل ي:B011/m01`
- Ayah anchors: 94:2 وِزْرَكَ; 94:3 ظَهْرَكَ; 94:8 إِلَىٰ
- Synthesis: Capacity becomes positional superiority, and superiority culminates in mastery over the opposing person.

### 5. Established Forms and Their Undoing
- Semantic invariant: Physical, social, and healed forms acquire stability through placement or binding and lose it through dismantling, breach, or reopening.
- Surface relation: direct; 94:2 وَضَعْنَا, 94:3 أَنقَضَ, 94:4 رَفَعْنَا, and 94:7 فَٱنصَبْ.
- Surprising reach: The undoing of a rope or building shares a precise structural pattern with breaching a covenant and reopening a healed wound.

#### Subchannel A. Raising, Erecting, and Dismantling
- Reading type: latent/lexical
- Scene or process: Components are placed, raised into an upright form, and then loosened or dismantled.
- Active motifs: placement and establishment `و ض ع:B001/m02`; physical raising `ر ف ع:B001/m01`; erecting an upright object `ن ص ب:B001/m01`; unfastening rope, cloth, or building `ن ق ض:B001/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 أَنقَضَ; 94:4 رَفَعْنَا; 94:7 فَٱنصَبْ
- Synthesis: Placement gives components a site, raising and erection give them organized form, and نقض reverses that organization by separating what had been made firm.

#### Subchannel B. Covenant, Record, and Entrusted Property
- Reading type: latent/lexical
- Scene or process: An obligation is sworn, recorded, negotiated, or entrusted and can then be breached or forcibly reclaimed.
- Active motifs: oath `ء ل ي:B007/m01`; covenant `ر ب ب:B011/m01`; deed of right `ذ ك ر:B008/m01`; negotiated agreement `و ض ع:B011/m01`; deposit placed in trust `و ض ع:B010/m01`; breach of oath or covenant `ن ق ض:B001/m02`; confiscation `ص د ر:B005/m01`
- Ayah anchors: 94:1 صَدْرَكَ; 94:2 وَضَعْنَا; 94:3 أَنقَضَ; 94:4 ذِكْرَكَ; 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: Speech creates the obligation, a deed preserves it, agreement or deposit locates rights between parties, and breach or confiscation reverses that ordered possession.

#### Subchannel C. Repair, Fixed Base, and Reopening
- Reading type: latent/lexical
- Scene or process: A damaged or weak form is completed around a stable base but may split open again after apparent settlement.
- Active motifs: repair and completion `ر ب ب:B002/m01`; fixed base, handle, or origin `ن ص ب:B006/m01`; weakly consolidated form `و ض ع:B012/m01`; wound reopening after healing `ن ق ض:B004/m01`; settled matter becoming unstable again `ن ق ض:B004/m02`; firm knot `ر ب ب:B016/m02`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 أَنقَضَ; 94:7 فَٱنصَبْ; 94:8 رَبِّكَ
- Synthesis: Repair gathers a form around an anchoring base or knot, weak consolidation threatens that integrity, and renewed opening returns the form to instability.

### 6. Conflict, Defense, and Allegiance
- Semantic invariant: Confrontation organizes weapons, sound, refuge, allies, and bodily motion, while defeat or abandonment dissolves that organization.
- Surface relation: indirect; 94:2 وِزْرَكَ, 94:3 أَنقَضَ/ظَهْرَكَ, 94:5-6 مَعَ/يُسْرًا, 94:7 فَٱنصَبْ, and 94:8 إِلَىٰ.
- Surprising reach: Battle is represented not only by weapons and hostility but by roaring sound, reserve supplies, turned backs, opportunistic companionship, and unanswered blood.

#### Subchannel A. Armament, Hostility, and Battle Clamor
- Reading type: latent/lexical
- Scene or process: Armed opponents confront one another amid raised calls and the tumult of battle.
- Active motifs: war equipment `و ز ر:B003/m01`; confronting enmity `ن ص ب:B008/m01`; battle clamor `م ع ع:B001/m02`; raised voice `ر ف ع:B010/m01`; calls and cries `ن ق ض:B006/m02`
- Ayah anchors: 94:2 وِزْرَكَ; 94:3 أَنقَضَ; 94:4 رَفَعْنَا; 94:5-6 مَعَ; 94:7 فَٱنصَبْ
- Synthesis: Weapons supply the material apparatus, نصب fixes the hostile relation face to face, and raised cries turn the confrontation into an audible collective event.

#### Subchannel B. Refuge and Defensive Reserve
- Reading type: latent/lexical
- Scene or process: A threatened party withdraws to a defensible place and relies on stored means and preventative preparation.
- Active motifs: refuge or mountain stronghold `و ز ر:B001/m01`; household reserve `ظ ه ر:B014/m01`; precautionary provision `ظ ه ر:B021/m01`; prevention `ء ل ي:B009/m01`
- Ayah anchors: 94:2 وِزْرَكَ; 94:3 ظَهْرَكَ; 94:8 إِلَىٰ
- Synthesis: Refuge supplies protective space, while reserve goods and prior precaution turn that space into sustained security rather than momentary escape.

#### Subchannel C. Alliance, Desertion, and Opportunistic Conformity
- Reading type: latent/lexical
- Scene or process: Helpers combine around a party, then fracture when companions turn their backs or attach themselves only to the victor.
- Active motifs: supporting ally `ظ ه ر:B006/m01`; group of supporters `ظ ه ر:B016/m01`; ministerial assistance `و ز ر:B004/m01`; mutual back-turning `ظ ه ر:B022/m01`; alignment with whoever prevails `م ع ع:B005/m01`
- Ayah anchors: 94:2 وِزْرَكَ; 94:3 ظَهْرَكَ; 94:5-6 مَعَ
- Synthesis: Aid creates a load-sharing alliance, whereas back-turning breaks reciprocal orientation and opportunistic conformity replaces loyalty with attachment to present power.

#### Subchannel D. Directed Strike and Downward Turn
- Reading type: latent/lexical
- Scene or process: A weapon or limb turns downward and drives a broad thrust toward the opponent's face.
- Active motifs: downward twist `ي س ر:B009/m01`; face-level thrust `ي س ر:B009/m02`; broad blow or thrust `ف ر غ:B003/m02`
- Ayah anchors: 94:5-6 يُسْرًا; 94:7 فَرَغْتَ
- Synthesis: The motifs combine direction, amplitude, and target into one compact combat movement: a downward turn that opens into a broad, face-directed strike.

#### Subchannel E. Unavenged Blood after Dispersion
- Reading type: latent/lexical
- Scene or process: Violent conflict disperses the parties and leaves shed blood without a claimant or answering vengeance.
- Active motifs: blood left unavenged `ف ر غ:B004/m01`; groups departing in scattered succession `ع س ر:B011/m01`; battle tumult `م ع ع:B001/m02`
- Ayah anchors: 94:5-6 مَعَ/ٱلْعُسْرِ; 94:7 فَرَغْتَ
- Synthesis: Clamor marks the violent event, dispersion removes the collective able to answer it, and the blood consequently passes without requital.

### 7. Reproductive and Domestic Life
- Semantic invariant: Embodied life moves through sexual union, conception, difficult delivery, postpartum nurture, and socially marked bodily presentation.
- Surface relation: direct; 94:2 وَضَعْنَا, with indirect extensions from 94:1 نَشْرَحْ, 94:3 ظَهْرَكَ, 94:4 ذِكْرَكَ/رَفَعْنَا, and 94:5-6 ٱلْعُسْرِ/يُسْرًا.
- Surprising reach: The birth scene extends into fosterage, milk retention, veiling, marital formulae, body shaping, and visible bodily marks.

#### Subchannel A. Sexual Opening, Conception, and Male Offspring
- Reading type: latent/lexical
- Scene or process: Sexual opening and intercourse lead to emitted seed and the sexed identity of offspring.
- Active motifs: intercourse `ش ر ح:B004/m01`; defloration `ش ر ح:B004/m02`; female sexual anatomy `ش ر ح:B004/m03`; semen `ف ر غ:B005/m01`; male sex or male offspring `ذ ك ر:B001/m01`; boyhood `ي س ر:B011/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:4 ذِكْرَكَ; 94:5-6 يُسْرًا; 94:7 فَرَغْتَ
- Synthesis: The motifs form a reproductive sequence from sexual access and emission to the designation of a male child and his early life stage.

#### Subchannel B. Difficult Delivery and Recent Birth
- Reading type: mixed
- Scene or process: Pregnancy reaches a difficult labor, the burden is delivered, and mother and newborn enter the immediate postpartum state.
- Active motifs: giving birth and laying down pregnancy `و ض ع:B002/m01`; difficult labor `ع س ر:B006/m01`; recent lambing or birth `ر ب ب:B009/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:5-6 ٱلْعُسْرِ; 94:8 رَبِّكَ
- Synthesis: وضع converts pregnancy from a carried state into delivery, عسر names the resistance of labor, and the recent-birth motif supplies its immediate outcome.

#### Subchannel C. Postpartum Milk and Foster Care
- Reading type: latent/lexical
- Scene or process: A newborn is kept under care while milk and offspring increase or milk is retained in the udder.
- Active motifs: fostered child `ر ب ب:B005/m01`; caregiver or foster guardian `ر ب ب:B005/m02`; milk and offspring abundance `ي س ر:B006/m01`; retained milk or colostrum `ر ف ع:B007/m01`; postpartum ewe kept near home for milk `ر ب ب:B009/m01`
- Ayah anchors: 94:4 رَفَعْنَا; 94:5-6 يُسْرًا; 94:8 رَبِّكَ
- Synthesis: Guardianship supplies the social relation, the postpartum animal supplies the domestic setting, and abundant or retained milk supplies the material of continued nurture.

#### Subchannel D. Veiling and Marital Body Analogy
- Reading type: latent/lexical
- Scene or process: A woman's bodily visibility is regulated by removal of the veil and by a marital utterance that invokes the prohibited maternal back.
- Active motifs: removing a woman's veil `و ض ع:B009/m01`; marital ẓihār formula `ظ ه ر:B010/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 ظَهْرَكَ
- Synthesis: One motif changes bodily visibility through uncovering, while the other changes marital relation through a spoken analogy to the maternal back; both organize access to the female body.

#### Subchannel E. Shaped and Marked Bodily Surfaces
- Reading type: latent/lexical
- Scene or process: Bodily contour is augmented, protrudes, or bears visible lines and identifying marks.
- Active motifs: feminine body padding `ر ف ع:B008/m01`; buttock and adjoining flesh `ء ل ي:B015/m01`; protruding eye `ظ ه ر:B009/m01`; palm lines and thigh brand `ي س ر:B008/m01`
- Ayah anchors: 94:3 ظَهْرَكَ; 94:4 رَفَعْنَا; 94:5-6 يُسْرًا; 94:8 إِلَىٰ
- Synthesis: Padding alters contour, the haunch supplies the shaped body region, and protrusion or inscribed lines make bodily form legible at the surface.

### 8. Journeying and Mounted Motion
- Semantic invariant: A traveler prepares a mount, enters motion, follows a route, endures its conditions, and reaches a halt or destination.
- Surface relation: indirect; 94:1 صَدْرَكَ, 94:2 وَضَعْنَا, 94:3 أَنقَضَ/ظَهْرَكَ, 94:4 رَفَعْنَا, 94:5-6 ٱلْعُسْرِ/يُسْرًا/مَعَ, 94:7 فَٱنصَبْ, and 94:8 إِلَىٰ/رَبِّكَ.
- Surprising reach: Travel joins bodily accommodation, animal training, speed, route geography, noon heat, ominous time, and raised chant.

#### Subchannel A. Mounting, Carrying, and Travel Wear
- Reading type: latent/lexical
- Scene or process: A riding animal lowers itself for mounting, bears the rider or load, and may be exhausted by repeated journeys.
- Active motifs: pack or riding animal `ظ ه ر:B005/m01`; camel lowering its neck for the rider `و ض ع:B013/m01`; riding before training `ع س ر:B008/m01`; girding and riding `و ز ر:B007/m01`; travel-worn camel `ن ق ض:B002/m01`
- Ayah anchors: 94:2 وَضَعْنَا/وِزْرَكَ; 94:3 أَنقَضَ/ظَهْرَكَ; 94:5-6 ٱلْعُسْرِ
- Synthesis: Mounting begins with bodily accommodation, girding secures the rider, the animal's back becomes transport, and premature or repeated use explains resistance and exhaustion.

#### Subchannel B. Gait, Speed, and Compliance
- Reading type: latent/lexical
- Scene or process: Rider and animal move through degrees of acceleration, breadth of stride, lifted tail, and easy responsiveness.
- Active motifs: intensified gait `ر ف ع:B003/m01`; urging a mount to run `و ض ع:B003/m01`; spacious stride or path `ف ر غ:B003/m01`; light compliant movement `ي س ر:B005/m01`; raised or bent tail in running `ع س ر:B009/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:4 رَفَعْنَا; 94:5-6 ٱلْعُسْرِ/يُسْرًا; 94:7 فَرَغْتَ
- Synthesis: The rider initiates acceleration, the animal answers with an extended and compliant gait, and the lifted tail becomes the visible sign of running effort.

#### Subchannel C. Departure, Route, Lodging, and Destination
- Reading type: latent/lexical
- Scene or process: Travelers leave a watering place, take the overland route, continue through the country, lodge, and approach an endpoint.
- Active motifs: departure from water or land `ص د ر:B003/m01`; egress from a matter or place `ص د ر:B003/m02`; traveling upward through country `ر ف ع:B011/m01`; daylong gentle travel `ن ص ب:B010/m01`; overland road and outskirts `ظ ه ر:B015/m01`; lodging and staying `ر ب ب:B007/m01`; endpoint `ء ل ي:B001/m01`
- Ayah anchors: 94:1 صَدْرَكَ; 94:3 ظَهْرَكَ; 94:4 رَفَعْنَا; 94:7 فَٱنصَبْ; 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: Departure opens the itinerary, road and sustained travel carry the group beyond settlement, lodging interrupts the course, and the endpoint gives the journey its terminal orientation.

#### Subchannel D. Noon Heat and the Ominous Day
- Reading type: latent/lexical
- Scene or process: A group travels through midday and severe heat under the shadow of a difficult or ill-omened day.
- Active motifs: severe heat `م ع ع:B002/m01`; travel through heat `م ع ع:B002/m02`; noon `ظ ه ر:B004/m01`; ill-omened day `ع س ر:B010/m01`; daylong travel `ن ص ب:B010/m01`
- Ayah anchors: 94:3 ظَهْرَكَ; 94:5-6 مَعَ/ٱلْعُسْرِ; 94:7 فَٱنصَبْ
- Synthesis: Midday fixes the temporal setting, oppressive heat supplies the environmental resistance, and the ominous day colors the traveler's full-day passage.

#### Subchannel E. Raised Travel Chant
- Reading type: latent/lexical
- Scene or process: Mounted travelers coordinate movement through a song or chant projected in a raised voice.
- Active motifs: travel song or camel chant `ن ص ب:B009/m01`; raised voice `ر ف ع:B010/m01`
- Ayah anchors: 94:4 رَفَعْنَا; 94:7 فَٱنصَبْ
- Synthesis: The chant belongs to the moving riders, while رفع supplies the vocal elevation that lets its rhythm carry across the journey.

### 9. Cultivation, Care, and Living Yield
- Semantic invariant: Sustained tending gathers dependents, knowledge, land, and herds into conditions where they can mature or produce.
- Surface relation: indirect; 94:1 نَشْرَحْ, 94:2 وَضَعْنَا, 94:3 أَنقَضَ/ظَهْرَكَ, 94:4 رَفَعْنَا/ذِكْرَكَ, 94:5-6 ٱلْعُسْرِ/يُسْرًا, and 94:8 رَبِّكَ.
- Surprising reach: The root of lordship extends through child-rearing and cultivated learning to rain-fed vegetation, guarded crops, harvest, herds, and pasture.

#### Subchannel A. Fosterage and Gradual Nurture
- Reading type: latent/lexical
- Scene or process: A guardian takes charge of a dependent and brings that person or thing toward completion stage by stage.
- Active motifs: gradual nurture and completion `ر ب ب:B002/m02`; fostered child `ر ب ب:B005/m01`; caregiver or custodian `ر ب ب:B005/m02`
- Ayah anchors: 94:8 رَبِّكَ
- Synthesis: The dependent is defined by being under care, the caregiver supplies continuing oversight, and رب names the gradual process by which incompleteness becomes maturity.

#### Subchannel B. Knowledge Cultivated and Preserved
- Reading type: latent/lexical
- Scene or process: A scholar cultivates knowledge and self, preserves what is learned, and keeps it available for recollection.
- Active motifs: learned or wise servant of the Lord `ر ب ب:B003/m01`; cultivating knowledge and self `ر ب ب:B003/m02`; preservation `ش ر ح:B006/m01`; retained recollection `ذ ك ر:B003/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:4 ذِكْرَكَ; 94:8 رَبِّكَ
- Synthesis: Learning is treated as husbandry of both knowledge and knower, with preservation and recollection carrying the cultivated result forward.

#### Subchannel C. Rain, Vegetation, Guarding, and Harvest
- Reading type: latent/lexical
- Scene or process: Layered cloud and abundant water sustain green growth, which emerges from the earth, is guarded, and is lifted after harvest.
- Active motifs: layered rain cloud `ر ب ب:B008/m01`; rain nurturing vegetation `ر ب ب:B008/m02`; abundant fresh water `ر ب ب:B013/m01`; evergreen plant `ر ب ب:B012/m01`; earth splitting for a truffle `ن ق ض:B003/m01`; earth's raised surface `ظ ه ر:B003/m01`; guarding crops or young palms `ش ر ح:B006/m02`; lifting harvest to the threshing floor `ر ف ع:B006/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:3 أَنقَضَ/ظَهْرَكَ; 94:4 رَفَعْنَا; 94:8 رَبِّكَ
- Synthesis: Water and enduring cloud provide the growing condition, the earth opens to release produce, guarding preserves it, and lifting the cut crop completes the agricultural cycle.

#### Subchannel D. Herd Aggregation and Pasture
- Reading type: latent/lexical
- Scene or process: Animals gather as a herd, remain near water and forage, or move away in scattered succession.
- Active motifs: herd of wild cattle or camels `ر ب ب:B014/m01`; grazing and staying near water `و ض ع:B007/m01`; forage and grazing place `و ض ع:B007/m02`; scattered or successive animal groups `ع س ر:B011/m01`; abundant water `ر ب ب:B013/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:5-6 ٱلْعُسْرِ; 94:8 رَبِّكَ
- Synthesis: Water and forage hold the animals in an aggregated pastoral scene, while scattered departure supplies the contrasting motion by which the herd loses cohesion.

### 10. Provision, Containment, and Distribution
- Semantic invariant: Capacity receives material abundance, while need, appetite, gift, and assigned shares determine how contents circulate.
- Surface relation: indirect; 94:1 صَدْرَكَ, 94:3 ظَهْرَكَ, 94:5-6 ٱلْعُسْرِ/يُسْرًا, 94:7 فَرَغْتَ/فَٱنصَبْ, and 94:8 إِلَىٰ/رَبِّكَ/فَٱرْغَب.
- Surprising reach: Spatial breadth becomes vessel capacity, then social generosity; the same field includes appetite, favors, surplus, fixed thresholds, and apportioned meat.

#### Subchannel A. Wide Vessels and Flowing Contents
- Reading type: latent/lexical
- Scene or process: A broad vessel or stone-edged basin receives plentiful liquid and releases it through pouring or an outlet.
- Active motifs: wide-bellied vessel or basin `ر غ ب:B002/m01`; pouring and emptying a vessel `ف ر غ:B002/m01`; vessel outlet `ف ر غ:B002/m02`; abundant water `ر ب ب:B013/m01`; stones forming a pool rim `ن ص ب:B003/m02`; thick syrup or oil residue `ر ب ب:B006/m01`
- Ayah anchors: 94:7 فَرَغْتَ/فَٱنصَبْ; 94:8 رَبِّكَ/فَٱرْغَب
- Synthesis: Breadth provides capacity, the rim defines the container, abundant or thick contents fill it, and pouring converts stored provision into directed flow.

#### Subchannel B. Need, Appetite, and Generous Giving
- Reading type: latent/lexical
- Scene or process: Need or appetite meets a desirable gift drawn from abundance and surplus.
- Active motifs: need `ر ب ب:B016/m01`; voracious appetite `ر غ ب:B003/m01`; abundant desirable gift `ر غ ب:B004/m01`; favors `ء ل ي:B006/m01`; gift `ء ل ي:B012/m01`; bounty and benefaction `ر ب ب:B016/m03`; giving from surplus `ظ ه ر:B023/m01`; affluence `ي س ر:B003/m01`
- Ayah anchors: 94:3 ظَهْرَكَ; 94:5-6 يُسْرًا; 94:8 إِلَىٰ/رَبِّكَ/فَٱرْغَب
- Synthesis: Appetite and need define the recipient side of provision, while wealth, favor, and surplus define a giver able to supply an abundant and desired good.

#### Subchannel C. Portions, Fixed Shares, and Division
- Reading type: latent/lexical
- Scene or process: A whole is separated into named portions whose recipients or thresholds are fixed.
- Active motifs: portion of a whole `ص د ر:B006/m01`; assigned share `ن ص ب:B005/m01`; fixed quantitative threshold `ن ص ب:B006/m02`; division of a slaughtered camel by arrows `ي س ر:B007/m02`; collected allotment arrows `ر ب ب:B010/m02`
- Ayah anchors: 94:1 صَدْرَكَ; 94:5-6 يُسْرًا; 94:7 فَٱنصَبْ; 94:8 رَبِّكَ
- Synthesis: The whole becomes a set of portions, a fixed measure governs eligibility, and allotment arrows assign the resulting shares to participants.

### 11. Ritualized Play and Sacrifice
- Semantic invariant: Erected markers, stones, arrows, and divided bodies organize rule-bound acts of play, allotment, or sacrifice.
- Surface relation: indirect; 94:1 نَشْرَحْ, 94:5-6 ٱلْعُسْرِ/يُسْرًا, 94:7 فَرَغْتَ/فَٱنصَبْ, and 94:8 رَبِّكَ.
- Surprising reach: The same upright apparatus can serve as a target, a lot mechanism, or a blooded ritual surface.

#### Subchannel A. Gambling Arrows and Allotted Shares
- Reading type: latent/lexical
- Scene or process: Players draw or cast arrows kept in a dedicated container, and the outcome determines shares.
- Active motifs: gambling by arrows `ي س ر:B007/m01`; arrow container `ر ب ب:B010/m01`; collected allotment arrows `ر ب ب:B010/m02`; assigned share `ن ص ب:B005/m01`
- Ayah anchors: 94:5-6 يُسْرًا; 94:7 فَٱنصَبْ; 94:8 رَبِّكَ
- Synthesis: The container assembles the game pieces, the arrows generate the lot, and the result is converted into a participant's designated share.

#### Subchannel B. The Erected Target Game
- Reading type: latent/lexical
- Scene or process: An upright wooden marker is struck or uprooted by a thrown implement.
- Active motifs: throwing game with an erected post `ع س ر:B013/m01`; erected marker or boundary stone `ن ص ب:B003/m01`; broad blow or thrust `ف ر غ:B003/m02`
- Ayah anchors: 94:5-6 ٱلْعُسْرِ; 94:7 فَرَغْتَ/فَٱنصَبْ
- Synthesis: The post supplies a stable target, the thrown blow supplies the operation, and successful uprooting provides the game's visible outcome.

#### Subchannel C. Altar, Pouring, and Divided Flesh
- Reading type: latent/lexical
- Scene or process: A standing stone receives slaughter, poured blood, and cut flesh.
- Active motifs: standing stone for worship or slaughter `ن ص ب:B002/m01`; pouring out vessel contents `ف ر غ:B002/m01`; cutting and spreading flesh `ش ر ح:B002/m01`; division of the slaughtered animal `ي س ر:B007/m02`
- Ayah anchors: 94:1 نَشْرَحْ; 94:5-6 يُسْرًا; 94:7 فَرَغْتَ/فَٱنصَبْ
- Synthesis: The stone fixes the ritual site, slaughter supplies blood and flesh, pouring marks the surface, and cutting or division distributes the animal body.

### 12. Language as Structured Relation
- Semantic invariant: Speech makes meaning explicit through explanation, naming, repetition, relational particles, derivation, and inflection.
- Surface relation: direct; 94:1 نَشْرَحْ, 94:4 رَفَعْنَا/ذِكْرَكَ, 94:5-6 مَعَ, 94:7 فَٱنصَبْ, and 94:8 إِلَىٰ.
- Surprising reach: Physical raising, setting upright, originating, and undoing recur as technical operations of case, derivation, and contradiction.

#### Subchannel A. Explanation and Naming
- Reading type: mixed
- Scene or process: An obscure matter is opened into intelligible form and then made referable in speech.
- Active motifs: explanation and clarification `ش ر ح:B001/m01`; speaking, naming, or making known `ذ ك ر:B004/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:4 ذِكْرَكَ
- Synthesis: شرح discloses the structure of the matter, while ذكر gives that disclosed content a spoken or named presence.

#### Subchannel B. Reporting, Raised Voice, and Repetition
- Reading type: latent/lexical
- Scene or process: A message is projected publicly, voiced loudly, and may be repeated in speech or writing.
- Active motifs: broadcasting a report `ر ف ع:B005/m01`; raised voice `ر ف ع:B010/m01`; repeated use of “with” `م ع ع:B006/m01`; repeated written inscription `م ع ع:B006/m02`
- Ayah anchors: 94:4 رَفَعْنَا; 94:5-6 مَعَ
- Synthesis: Reporting supplies the communicative act, vocal elevation supplies reach, and repetition stabilizes the expression across oral and written media.

#### Subchannel C. Relational Particles and Collective Reference
- Reading type: latent/lexical
- Scene or process: Function words locate an entity, qualify a proposition, or refer to a plurality.
- Active motifs: “to” used in the sense of “at” `ء ل ي:B002/m01`; particle rubba and its variants `ر ب ب:B015/m01`; collective relative expression `ء ل ي:B004/m01`
- Ayah anchors: 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: The relational item locates, the particle modulates a proposition, and the collective expression binds plural referents into a single grammatical role.

#### Subchannel D. Derivation, Case, and Contradiction
- Reading type: latent/lexical
- Scene or process: A word is traced to its source, assigned grammatical position, or set against another statement.
- Active motifs: grammatical source or infinitive `ص د ر:B004/m01`; nominative case `ر ف ع:B012/m01`; accusative case `ن ص ب:B007/m01`; contradiction in speech or poetry `ن ق ض:B001/m03`
- Ayah anchors: 94:1 صَدْرَكَ; 94:3 أَنقَضَ; 94:4 رَفَعْنَا; 94:7 فَٱنصَبْ
- Synthesis: The source grounds derivation, رفع and نصب place the word within an inflectional structure, and contradiction performs a semantic undoing between utterances.

### 13. Collective Arrangement and Place
- Semantic invariant: Multiple units are joined, situated, bounded, or dispersed as social and spatial formations.
- Surface relation: indirect; 94:1 صَدْرَكَ, 94:2 وَضَعْنَا, 94:3 ظَهْرَكَ, 94:5-6 مَعَ/ٱلْعُسْرِ/يُسْرًا, and 94:8 إِلَىٰ/رَبِّكَ.
- Surprising reach: Grammatical accompaniment becomes social aggregation, while settlement, outskirts, boundaries, and turned backs describe the formation and breakup of groups.

#### Subchannel A. Accompaniment, Plurality, and Being Among
- Reading type: latent/lexical
- Scene or process: Separate persons or things are added together and occupy a shared collective field.
- Active motifs: accompaniment and addition `ء ل ي:B003/m01`; collective relative plurality `ء ل ي:B004/m01`; crowds or large groups `ر ب ب:B004/m01`; being among a people `ظ ه ر:B017/m01`
- Ayah anchors: 94:3 ظَهْرَكَ; 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: Addition forms the group, plural reference names it as a unit, and being among its members supplies the participant's internal position.

#### Subchannel B. Settlement, Locality, and Boundary
- Reading type: latent/lexical
- Scene or process: A population is placed in a locality whose center, outskirts, and marked limits organize residence.
- Active motifs: settled transferred people or registered garrison `و ض ع:B006/m01`; tribe or named place `ع س ر:B012/m01`; named locality `ي س ر:B010/m01`; overland outskirts `ظ ه ر:B015/m01`; erected boundary marker `ن ص ب:B003/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 ظَهْرَكَ; 94:5-6 ٱلْعُسْرِ/يُسْرًا; 94:7 فَٱنصَبْ
- Synthesis: Placement establishes the population, names stabilize the locality, outskirts define its exterior, and markers make its limits materially visible.

#### Subchannel C. Dispersion, Egress, and Turned Backs
- Reading type: latent/lexical
- Scene or process: A collective leaves its shared position, scatters in succession, or fractures through mutual disengagement.
- Active motifs: scattered or successive groups `ع س ر:B011/m01`; egress from a place `ص د ر:B003/m02`; mutual back-turning `ظ ه ر:B022/m01`; opportunistic alignment with the prevailing party `م ع ع:B005/m01`
- Ayah anchors: 94:1 صَدْرَكَ; 94:3 ظَهْرَكَ; 94:5-6 مَعَ/ٱلْعُسْرِ
- Synthesis: Egress starts the separation, scattered succession dissolves compact form, and turned backs or shifting allegiance complete the social fracture.

### 14. Material Cutting, Curing, and Layering
- Semantic invariant: Raw organic or textile material is transformed by cutting, curing, padding, superposition, and possible unraveling.
- Surface relation: indirect; 94:1 نَشْرَحْ, 94:2 وَضَعْنَا, 94:3 أَنقَضَ/ظَهْرَكَ, and 94:8 إِلَىٰ/رَبِّكَ.
- Surprising reach: A tanning tree and thick curing substance join sliced flesh, quilted cotton, layered armor, and unravelled cloth in one material-work field.

#### Subchannel A. Cutting and Curing Flesh or Hide
- Reading type: latent/lexical
- Scene or process: Animal material is cut into spread pieces or treated with plant and thick curing substances.
- Active motifs: cutting and spreading flesh `ش ر ح:B002/m01`; thin or dried meat slice `ش ر ح:B002/m02`; green tanning tree `ء ل ي:B005/m01`; thick curing syrup or residue `ر ب ب:B006/m02`; haunch flesh `ء ل ي:B015/m01`
- Ayah anchors: 94:1 نَشْرَحْ; 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: The animal body supplies flesh or hide, cutting opens and thins the material, and plant or concentrated substances preserve and transform it.

#### Subchannel B. Quilting, Armor Layering, and Unraveling
- Reading type: latent/lexical
- Scene or process: Cotton is placed and stitched into cloth, garments or armor are superposed, and the assembled fabric can be pulled apart.
- Active motifs: cotton padding and stitching `و ض ع:B008/m01`; superposed garments or armor `ظ ه ر:B020/m01`; unraveling rope or cloth `ن ق ض:B001/m01`
- Ayah anchors: 94:2 وَضَعْنَا; 94:3 أَنقَضَ/ظَهْرَكَ
- Synthesis: Placement and stitching build an insulated layer, superposition increases protective thickness, and unraveling reverses the assembly at its joins.

## Standalone Subchannels

### S1. Left-side Orientation and Directional Turn
- Reading type: latent/lexical
- Scene or process: A body or implement is distinguished by its left side and by a turn toward a lower direction.
- Active motifs: left-handedness and the left side `ع س ر:B005/m01`; leftward side or movement `ي س ر:B004/m01`; downward twist `ي س ر:B009/m01`
- Ayah anchors: 94:5-6 ٱلْعُسْرِ/يُسْرًا
- Synthesis: The opposed hardship/ease roots converge lexically on the left side, while the downward twist converts laterality into directed bodily motion.

### S2. Delay, Duration, and Brevity
- Reading type: latent/lexical
- Scene or process: An interval can persist, be delayed, remain recent, or contract into brief duration.
- Active motifs: lingering and detention `ء ل ي:B013/m01`; continued duration `ر ب ب:B007/m02`; recentness and youth `ر ب ب:B009/m02`; brief or small interval `ي س ر:B002/m01`
- Ayah anchors: 94:5-6 يُسْرًا; 94:8 إِلَىٰ/رَبِّكَ
- Synthesis: Duration supplies the temporal field, delay lengthens it, recentness locates an event near its beginning, and brevity contracts its extent.

### S3. Aloeswood Fumigation
- Reading type: latent/lexical
- Scene or process: Aromatic wood is consumed as incense to perfume a space through smoke.
- Active motifs: aloeswood incense stick `ء ل ي:B014/m01`
- Ayah anchors: 94:8 إِلَىٰ
- Synthesis: The lexical object carries its own complete use-scene: a material stick becomes fragrant smoke through fumigation.

### S4. Cord for Lifting a Fetter
- Reading type: latent/lexical
- Scene or process: A cord or thread raises a prisoner's restraint to permit controlled movement.
- Active motifs: fetter-lifting cord `ر ف ع:B009/m01`
- Ayah anchors: 94:4 رَفَعْنَا
- Synthesis: The cord acts as a compact lifting mechanism between the restrained limb and the weight of the fetter.

### S5. Feather Vane and Shaft
- Reading type: latent/lexical
- Scene or process: A feather's rear shaft material forms a vane in a wing or fitted arrow.
- Active motifs: rear feather or vane component `ظ ه ر:B011/m01`
- Ayah anchors: 94:3 ظَهْرَكَ
- Synthesis: The motif isolates a concrete object-part relation in which material taken from the feather's back becomes a functional flight surface.


