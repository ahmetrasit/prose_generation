Surah: 94. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S94 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s094/surah.r2.hftbundle/text.md =====
# Surah 94

- 94:1 أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- 94:2 وَوَضَعْنَا عَنكَ وِزْرَكَ
- 94:3 ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- 94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ
- 94:5 فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- 94:6 إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- 94:7 فَإِذَا فَرَغْتَ فَٱنصَبْ
- 94:8 وَإِلَىٰ رَبِّكَ فَٱرْغَب


===== _commentary/v16/work/s094/surah.r2.hftbundle/dictionary.md =====
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



===== _commentary/v16/work/s094/surah.r2.hftbundle/channels.md =====
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


===== _commentary/v16/work/s094/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 94

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 94:1

## clarified inner source
- reading: A claim that the inward source of response was opened into intelligibility, so action can issue from a clarified interior.
- mechanism: The chest is construed as the inward source from which speech and action issue. شرح opens what is hidden until it becomes intelligible, so the intervention makes that source both spacious and legible.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening a hidden meaning into clarity supplies the operation: an opaque interior is rendered intelligible.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest fixes that clarified interior in an embodied site rather than an abstract faculty.
  - 94:1 **صَدْرَكَ** ص د ر B004: A source from which actions issue turns the chest into the generative interior being clarified.

## material unfolding
- reading: An embodied unbinding or spreading of the bodily front, with relief imagined as altered material geometry.
- mechanism: The construction permits an embodied geometry: constricted material at the front of the torso is spread, thinned, or unfolded. Relief is therefore not only a mental state but a change in how pressure occupies the body.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading and slicing flesh contributes a material operation of opening surface and redistributing thickness.
  - 94:1 **صَدْرَكَ** ص د ر B001: The anatomical chest supplies the bodily material and load-bearing front on which that operation is imagined.

## guarded capacity
- reading: Opening establishes protected capacity: the source becomes usable without being abandoned to exposure.
- mechanism: Opening need not mean leaving the interior exposed. It can establish a protected generative enclosure: capacity is made usable while what is young or vulnerable within it is kept from loss.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B006: Guarding crops or young palms contributes preservation as the way newly available capacity is kept viable.
  - 94:1 **صَدْرَكَ** ص د ر B004: The originating source supplies the protected generative center whose future acts are being preserved.

## expanded desire
- reading: The motivational source gains a larger capacity to incline and act, without yet specifying where that desire should point.
- mechanism: The opening enlarges motivational range. The chest is not merely calmed; its power to incline, choose, and send action outward is expanded, although the focus ayah alone leaves the desired object unspecified.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B005: Expansive inclination toward something supplies a widening of desire rather than only a widening of space.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which acts issue makes expanded inclination operational: desire can become conduct.

## load transfer
- reading: The chest is decompressed by relocation of a load, possibly restoring an unwarped bodily stance.
- mechanism: The next ayah supplies downward placement and a heavy load. Coupled with the bodily-material baseline, expansion becomes a load-transfer operation: the chest ceases to be compressed because weight is placed away from the addressee. The non-dominant mapped branch adds a tilted chest, making the relief potentially postural unwarping.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Material spreading supplies the chest's change of geometry under released pressure.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily front supplies the site that had borne compression and can visibly open after unloading.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something in a lower or settled place contributes the downward relocation that releases pressure.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy load supplies the compressive mass whose removal makes expansion mechanically intelligible.
  - 94:2 **وِزْرَكَ** و ز ر B004: The split-root image of a chest's tilt contributes a postural symptom that unloading can reverse.

## front back release
- reading: The whole torso is a load-bearing shell: opening its front is the counterpart to arresting or reversing failure at its back.
- mechanism: The creak of a back under weight and the explicit rear of the body turn chest and back into a coupled shell. شرح is now pressure-release across a whole load-bearing torso: expansion at the front answers strain approaching audible structural failure at the back.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading bodily material provides the pressure-releasing change at the front of the torso.
  - 94:1 **صَدْرَكَ** ص د ر B001: The anatomical chest supplies the front half of the coupled load-bearing structure.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints or back under weight makes the hidden strain audible and marks proximity to failure.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The back as counterpart to the belly supplies the rear surface mechanically coupled to the opened chest.
  - 94:3 **ظَهْرَكَ** ظ ه ر B006: Strengthening by a back or support makes the rear not just anatomy but the structure expected to carry load.

## public issuance
- reading: The opening is an upstream communicative intervention: a clarified source can issue a signal that is amplified and socially carried.
- mechanism: The focus chest can be a source from which acts issue, while شرح makes hidden content clear. Raising as broadcasting and mention as speech on tongues create a transmission path: an opened, clarified interior becomes the upstream condition for an outward signal that can circulate.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B001: Clarifying hidden meaning supplies intelligible content capable of being communicated.
  - 94:1 **صَدْرَكَ** ص د ر B004: The originating source supplies the interior point from which the public output can issue.
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Broadcasting a report contributes the outward amplification stage of the mechanism.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention running on the tongue supplies the social medium in which inward clarity becomes circulation.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Honor and repute supply the durable public consequence of amplified mention.

## coexisting aperture
- reading: Chest expansion is enlarged carrying-and-moving capacity in which constriction and an opening can coexist.
- mechanism: Difficulty supplies constriction and twisting, while ease supplies an opening after difficulty. Because the pair is stated with accompaniment and then repeated, chest-opening changes from completed removal of pressure into an aperture available in the presence of pressure: constriction remains named, but it no longer occupies all available capacity.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening what was closed or obscure supplies an aperture through which a constricted situation can become traversable and intelligible.
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Twisting, opposition, and imposed difficulty contribute the constrictive geometry that still remains present.
  - 94:5 **يُسْرًا** ي س ر B001: Opening and ease after difficulty supply the counter-space that appears without denying the constriction.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Repeated hardship preserves the pressure term rather than narrating its disappearance.
  - 94:6 **يُسْرًا** ي س ر B005: Lightness and compliant movement add mobility within pressure, not merely a later static reward.

## clearance for upright exertion
- reading: The opened chest is renewable capacity: it can be cleared, set upright, and expended in another committed effort.
- mechanism: Emptying a vessel after occupation followed by setting something upright or accepting exhausting exertion gives opening a cycle. The chest is cleared not for permanent vacancy but so capacity can be erected, committed, and spent again.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading bodily material supplies increased working room rather than an inert feeling.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest supplies the container-like capacity that can be occupied, cleared, and used again.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel contributes active clearance of previously occupied capacity.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Erecting something upright and prominent contributes renewed stance and commitment after clearance.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Exhausting toil contributes the expenditure for which opened capacity is made available.

## vectorized desire
- reading: Its desire-space is widened and then vectorized toward the nurturing, completing رب; opening becomes reorientation and cultivation of appetite.
- mechanism: The baseline expansion of inclination is initially objectless. رغبة supplies a vector toward or away and also spatial breadth; رب supplies nurture, repair, and completion, while its non-dominant mapped root adds feeding and growth. The opened chest thus becomes cultivated desire-space whose breadth is directed rather than indiscriminate.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B005: Expansive inclination supplies the motivational capacity that the later imperative can orient.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which acts issue makes directed desire consequential rather than merely felt.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Inclination toward or away supplies the directional vector missing from the focus-only desire model.
  - 94:8 **فَٱرْغَب** ر غ ب B002: Breadth, a wide cavity, or spatial extension turns desire into a roomy field that can receive direction.
  - 94:8 **رَبِّكَ** ر ب ب B002: Repair, nurture, and completion supply the governing relation under which expanded inclination is cultivated.
  - 94:8 **رَبِّكَ** ر ب ب B005: The split-root image of feeding and growth contributes development rather than mere enlargement of appetite.

## partitioned load
- reading: Expansion may work analytically: cut an overwhelming whole into portions that can be allocated, understood, and borne.
- mechanism: 
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Slicing and spreading flesh supplies the operation that breaks an undifferentiated mass into manageable surfaces.
  - 94:1 **صَدْرَكَ** ص د ر B006: A portion of something supplies the resulting units into which pressure or obligation can be divided.
  - 94:5 **يُسْرًا** ي س ر B007: Lots and division of a slaughtered animal contribute an allocation mechanism by which shares replace one crushing whole.

## reopened seam
- reading: The chest may be reopened along a constrictive seam: some prior closure or integration is parted so the body can carry life again.
- mechanism: 
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading bodily material supplies the seam-like opening operation.
  - 94:1 **صَدْرَكَ** ص د ر B001: The anatomical chest keeps the reopening image attached to the focus rather than becoming a free-standing repair metaphor.
  - 94:3 **أَنقَضَ** ن ق ض B004: Returning to openness after being joined supplies the possibility that a prior closure became constrictive and had to part again.

## rising breath
- reading: The opening can be somatically heard and felt as a chest chamber admitting a fuller, rising breath that carries directed longing.
- mechanism: 
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading bodily material supplies physical enlargement of the breathing chamber.
  - 94:1 **صَدْرَكَ** ص د ر B001: The anatomical chest supplies the respiratory site in which expansion can be felt.
  - 94:8 **رَبِّكَ** ر ب ب B004: Rising and swelling breath contributes the bodily event made possible by the opened chest.
  - 94:8 **فَٱرْغَب** ر غ ب B002: A wide cavity or spatial extension reinforces the chest as an expanded chamber that can carry rising breath.


# Focus 94:2

## spatial unloading
- reading: We physically unload from you what had occupied the position of a heavy carried load, setting it somewhere other than on its bearer.
- mechanism: The two dominant branch images form a load-transfer scene: a heavy thing formerly borne by the addressee is deliberately set down off that bearer. Relief is therefore spatial and material before it is psychological.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting an object down or into a settled place supplies the downward displacement and endpoint of the event.
  - 94:2 **وِزْرَكَ** و ز ر B002: A heavy carried load supplies the object whose bearer-position is changed.

## delegated load
- reading: The burden was taken out of your sole charge and reassigned into a supporting arrangement that can bear it with or for you.
- mechanism: The burden is redistributed into an arrangement of assigned bearers or support. What leaves the addressee can continue to exist as a responsibility, but no longer as a solitary load.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B006: Assigned people, soldiers, or loads supply an organized destination for what is moved off the addressee.
  - 94:2 **وِزْرَكَ** و ز ر B004: The helper or minister who carries another's weight supplies delegated load-bearing rather than simple deletion.

## disarmament
- reading: Your conflict-loadout was taken off you and laid down, changing the ayah into a scene of de-escalation or demobilization.
- mechanism: The same syntax that depicts unloading can depict decommissioning: equipment carried for conflict is taken off and laid down, ending a state of armed readiness.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something down supplies the concrete act of laying aside equipment.
  - 94:2 **وِزْرَكَ** و ز ر B003: The gear of war supplies a specific load and turns unloading into disarmament.

## delivery
- reading: A burden you had carried was brought to term and delivered from you, making relief a difficult threshold that can produce a new condition.
- mechanism: Removal can be a delivery rather than subtraction: a long-carried weight reaches a threshold, separates from its bearer, and opens a new phase. The result is not necessarily nothingness; something may emerge from the release.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B002: Laying down a pregnancy in birth supplies release through culmination and separation from a bearer.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy carried load supplies the gestational weight that can be brought to delivery.

## economic abatement
- reading: A weight standing against you was abated and taken off your account, with the image retaining the possibility that another side absorbs the loss.
- mechanism: The burden behaves like a liability written down through a loss borne elsewhere. This preserves a cost rather than pretending that relief is costless.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B004: Reduction of trading capital through loss supplies the concrete logic of an abatement or write-down.
  - 94:2 **وِزْرَكَ** و ز ر B002: A heavy burden supplies the obligation-like debit removed from the addressee.
  - 94:2 **وِزْرَكَ** و ز ر B005: Securing and taking something away supplies the transfer side of the write-down rather than pure disappearance.

## refuge detachment
- reading: Your own refuge was detached from you; the focus alone leaves open whether this is dangerous exposure or liberation from a defensive enclosure.
- mechanism: Read with عَنكَ, the act becomes unsettling: an owned refuge is detached from the addressee. Focus-only evidence does not decide whether this is deprivation, exposure, or release from a defensive dependence.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting something away from its former bearer supplies the detachment of a protective object.
  - 94:2 **وِزْرَكَ** و ز ر B001: Refuge or fortified shelter supplies the surprising object removed from the addressee.

## opened source reconfiguration
- reading: An opened action-generating interior is relieved of what loaded it, so the removal changes what can issue from the person as well as how the person feels.
- mechanism: The preceding opening of the chest, especially the chest as an origin from which acts issue, moves the burden scene inward. The removal can alter the generating center of action rather than merely subtract an external package.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting something out of its prior place supplies removal from an interior source once access is opened.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies what obstructs or loads the interior center.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and making meaning clear supplies access and intelligibility rather than a merely closed interior.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest supplies the interior location immediately prepared before the unloading.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which actions issue turns that location into a causal center whose output can change.

## back load diagnosis
- reading: The burden is known by the deformation it produces: it loads the back until the frame audibly protests, and its removal prevents breakdown.
- mechanism: The next ayah gives a mechanical symptom and its site: the load makes the back or its joints creak under strain. The focus act is therefore not generic consolation but an intervention before a load-bearing structure fails.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting down supplies the relieving operation performed on an overstrained bearer.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy load supplies the force acting on the body.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints and back under weight supply an audible diagnostic of overload.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back supplies the exact load-bearing structure under stress.

## unrigged war harness
- reading: A fitted conflict apparatus is unbound from your back and laid down, making peace a bodily de-rigging rather than a mere change of intention.
- mechanism: War gear from the focus is joined to the context's carried equipment and the undoing of a tightly constructed thing. Disarmament becomes an unrigging operation: bindings are undone and the apparatus is taken off the back.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting an object down supplies the endpoint after equipment is removed.
  - 94:2 **وِزْرَكَ** و ز ر B003: Weapons and war equipment specify the load as a conflict apparatus.
  - 94:3 **أَنقَضَ** ن ق ض B001: Undoing something tightly bound supplies the release of straps, fastenings, or an assembled rig.
  - 94:3 **ظَهْرَكَ** ظ ه ر B005: Mounts and carried equipment locate the apparatus on a transport or load-bearing back.

## vertical exchange
- reading: Only the degrading load is lowered away; the bearer's standing is simultaneously elevated, so unloading restores rather than reduces social stature.
- mechanism: The paired first-person-plural acts distribute verticality selectively: the load and its degrading downward pressure are put down, while the addressee's public standing and remembered name are raised. Relief is an exchange of what occupies the high and low positions.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B005: Lowness of rank and humbling supply the social danger carried by the downward verb.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies what is selected for downward removal rather than the person being lowered.
  - 94:4 **وَرَفَعْنَا** ر ف ع B002: Elevation of rank supplies the upward social counter-movement.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Honor and public repute specify what is raised in the social field.

## ease within hardship
- reading: The difficult situation may remain, but its crushing load is taken off so that an opening and maneuverability coexist with it.
- mechanism: The repeated pairing of hardship with ease prevents burden-removal from meaning the abolition of every difficult condition. It creates an opening and lighter movement within a still-present hardship: the bearer-load relation changes even when the terrain does not.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting the load down supplies a local change in carriage rather than disappearance of the surrounding conditions.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden distinguishes a removable load from hardship as the larger environment.
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity supply the continuing resistant condition.
  - 94:5 **يُسْرًا** ي س ر B005: Lightness and tractable movement supply operational freedom inside the difficult condition.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: The repeated severe condition resists reading relief as a one-time erasure of hardship.
  - 94:6 **يُسْرًا** ي س ر B001: Opening and ease after constriction supply the renewed possibility generated around the load.

## difficult delivery
- reading: The burden is delivered through constricted labor into an opening, so relief is a generative passage whose difficulty is not denied.
- mechanism: The focus childbirth branch meets a context branch for obstructed or difficult birth and a repeated opening into ease. The burden is delivered through labor: release is costly, thresholded, and potentially generative rather than instantaneous subtraction.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B002: Childbirth supplies the act of laying down a carried pregnancy.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies the carried weight brought to the threshold of separation.
  - 94:5 **ٱلْعُسْرِ** ع س ر B006: Difficult childbirth supplies labor, obstruction, and risk within the release process.
  - 94:5 **يُسْرًا** ي س ر B001: Opening into ease supplies passage through the obstruction.
  - 94:6 **ٱلْعُسْرِ** ع س ر B006: Repetition keeps the labor-image active rather than treating it as a momentary pang.
  - 94:6 **يُسْرًا** ي س ر B001: Repeated opening and ease make successful passage, not painless avoidance, the counterpart to labor.

## insolvency write down
- reading: A liability crushing someone of limited means is written down from that person's side, restoring usable capacity while acknowledging that remission has a cost.
- mechanism: Economic branches align into an insolvency scene: a person of straitened means carries a liability, capital is reduced to abate it, and ease appears as renewed sufficiency. The cost is transferred or recognized, not magically erased.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B004: Capital reduction through loss supplies the write-down operation.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies the debtor-like obligation.
  - 94:5 **ٱلْعُسْرِ** ع س ر B002: Lack of means supplies the condition that makes an obligation crushing and abatement necessary.
  - 94:5 **يُسْرًا** ي س ر B003: Sufficiency and wealth supply the restored capacity produced by relief.
  - 94:6 **ٱلْعُسْرِ** ع س ر B002: Repeated straitened means make the economic condition persistent rather than incidental.
  - 94:6 **يُسْرًا** ي س ر B003: Repeated sufficiency supplies durable capacity rather than a fleeting reprieve.

## unload to restand
- reading: The old crushing load is removed to empty capacity and restore an upright stance for a new exertion that is chosen and directed.
- mechanism: The later conditional sequence gives unloading a telos. A vessel is emptied, then the addressee is told to set upright and enter effort: putting the old load down clears capacity and posture for a new, chosen exertion rather than terminal rest.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting the old load down supplies the first half of a posture-and-capacity reset.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy load supplies what must cease occupying the bearer's capacity.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel supply cleared capacity after the prior load.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright supplies the reversal from loaded-down posture to active stance.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Effort and weariness keep the new upright stance from being mistaken for effortless repose.

## refuge reorientation
- reading: A self-possessed defensive recourse is taken out of the addressee's orbit so reliance can be redirected toward a sovereign and nurturing center.
- mechanism: The final directional command supplies a possible destination for reliance. Detachment from 'your refuge' can be a release from owned defensive recourse so desire and dependence can turn toward a sovereign, nurturing master; the alarming deprivation becomes a transfer of orientation.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting away supplies detachment from a previously possessed defensive position.
  - 94:2 **وِزْرَكَ** و ز ر B001: Refuge or mountain shelter supplies the owned recourse from which the addressee is detached.
  - 94:8 **رَبِّكَ** ر ب ب B001: Sovereignty and mastery supply a new center of dependence beyond the addressee's own refuge.
  - 94:8 **رَبِّكَ** ر ب ب B002: Nurturing, repairing, and bringing to completion make the new orientation protective rather than merely subordinating.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies the explicit vector that relocates reliance.

## body axis correction
- reading: A distorting load or crookedness spanning chest and back is taken off, allowing the bodily axis to open and realign.
- mechanism: 
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting something away supplies correction by removing a distorting element from the body.
  - 94:2 **وِزْرَكَ** و ز ر B004: The chest and chest-crookedness image supplies a frontal bend or torsion latent in the focus noun.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest activates the frontal half of the latent body axis.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints under load supplies the symptom of a frame twisted or compressed by weight.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The back supplies the rear half of the chest-to-back load-bearing axis.

## speech composition release
- reading: The inward strain of composing and straightening speech is taken off you, allowing clarified meaning to pass onto the tongue and circulate publicly.
- mechanism: 
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting a task down supplies release from a privately carried communicative labor.
  - 94:2 **وِزْرَكَ** و ز ر B006: Preparing and straightening speech before utterance supplies the specific burden being carried inwardly.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarifying meaning supplies intelligibility before expression.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention running on the tongue supplies successful outward utterance.
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Broadcasting news supplies circulation beyond the speaker once the inward labor is relieved.

## textile harness unbinding
- reading: The burden behaves like a padded, string-bound rig fitted to the back: its construction is undone and the apparatus is taken off piece by piece.
- mechanism: 
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B008: Placing cotton into a sewn garment supplies padding and construction around a body-borne load.
  - 94:2 **وِزْرَكَ** و ز ر B008: String or flax supplies the thread or binding element of the constructed load.
  - 94:3 **أَنقَضَ** ن ق ض B001: Undoing a tightly made construction supplies unsewing or releasing the binding.
  - 94:3 **ظَهْرَكَ** ظ ه ر B005: Carried equipment supplies the body-borne rig whose padding and ties are dismantled.

## vector reorientation
- reading: Relief changes direction: a deflecting bend is removed from you so desire can be steered toward its named endpoint.
- mechanism: 
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Setting aside supplies removal of a deflecting trajectory from the person.
  - 94:2 **وِزْرَكَ** و ز ر B001: Turning aside and deviation supply the directional defect latent in the focus object.
  - 94:8 **رَبِّكَ** ر ب ب B001: Sovereign mastery supplies the endpoint named by the final directional phrase.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies the positive steering operation after deviation is removed.


# Focus 94:3

## audible load
- reading: The burden made the body's supporting frame announce its strain: the verse gives an acoustic, near-failure measure of its force.
- mechanism: A weight does not merely rest on the back; it loads the body until its supporting joints audibly register strain. The sound is evidence of force nearing the body's carrying limit.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: The literal image of a back or joints creaking under weight supplies the audible stress signal in the mechanism.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back opposite the belly supplies the load-bearing body part on which the force is registered.

## unmade backing
- reading: A load was undoing the addressee's means of being supported, bodily and potentially relational, from the structure outward.
- mechanism: The burden acts structurally: it unfastens the very support by which the addressee remains braced. This can coexist with the anatomical reading while extending the back into capacity, aid, or a support system.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B001: Undoing a firm rope, knot, or structure supplies the action of dismantling an organized support rather than merely pressing it.
  - 94:3 **ظَهْرَكَ** ظ ه ر B006: Backing and assistance supply the functional support that the burden threatens to unmake.

## journey worn carrier
- reading: The burden had turned the addressee into a journey-worn carrier whose load-bearing reserve was being spent over distance and time.
- mechanism: The addressee is momentarily imaged as a carrier depleted by repeated journeys. The back is not passive anatomy but transport infrastructure whose strength has been consumed by what it carries.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B002: The camel worn down by travel supplies cumulative depletion rather than a single instant of pressure.
  - 94:3 **ظَهْرَكَ** ظ ه ر B005: The load-bearing mount supplies the carrier role assigned to the possessed back.

## reopened surface
- reading: The burden reopened a previously closed vulnerability in the body's outer frame, making the strain recurrent rather than merely acute.
- mechanism: Pressure reopens what had once closed or settled across the body's outer supporting surface. This gives the verse a relapse model: strain can reactivate an old seam rather than create damage from nothing.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B004: A wound or settled matter reopening after closure supplies the relapse mechanism.
  - 94:3 **ظَهْرَكَ** ظ ه ر B003: The upper or outer surface supplies the bodily plane across which the reopened seam is imagined.

## front back redistribution
- reading: The focus is the rear half of a whole-torso reconfiguration: inner/front capacity opens while the former load is exposed through the back's strain.
- mechanism: The opened chest and the creaking back become a paired torso transformation: capacity is expanded at the front or inner source of action while pressure is registered at the rear support. Relief is therefore a redistribution of capacity and load, not a denial that the load was real.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking under weight supplies the stressed rear response that is set against opening.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back supplies the rear load-bearing pole of the torso pairing.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarifying supplies expansion, functioning here as increased interior capacity.
  - 94:1 **صَدْرَكَ** ص د ر B001: The chest and its connected anatomy supply the front bodily pole paired with the focus back.

## retrospective unloading
- reading: The burden has been taken down, while the focus preserves the body's audible record of what that burden had been doing.
- mechanism: The immediately preceding lowering of a heavy load makes the focus clause diagnostic and retrospective. The back's creak identifies how severe the removed burden had been; it need not describe damage still being inflicted.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: The creak under weight functions as a measurable trace left by the burden.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back supplies the bearing surface from which the severity of the former load is inferred.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Placing something lower or in a settled position supplies the downward removal operation.
  - 94:2 **وِزْرَكَ** و ز ر B002: The literal heavy load identifies what had exerted the force heard in the focus.

## carrier loading protocol
- reading: The focus preserves an entire carrier history—mounting, cargo, repeated travel, and depletion—inside the burdened back.
- mechanism: The focus-only carrier model expands into a pack-animal loading scene: a neck lowers for mounting, a heavy load is borne, travel consumes the carrier, and the load-bearing back reaches exhaustion. The sequence materializes burden as a transport protocol rather than a static object.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B002: The camel worn down by journeys supplies cumulative transport fatigue.
  - 94:3 **ظَهْرَكَ** ظ ه ر B005: The mount or spare load animal supplies the back's carrier function.
  - 94:2 **وَوَضَعْنَا** و ض ع B013: A camel lowering its neck to be ridden supplies the loading and mounting posture.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy load supplies the cargo that links posture, journey, and exhaustion.

## vertical exchange
- reading: The focus marks the conversion point where downward bodily pressure gives way to an elevation that does not have to be carried on the back.
- mechanism: The focus becomes the hinge of a vertical exchange: crushing force is removed from the bodily back, while public standing or remembered presence is raised. What is elevated is not the old load but a different, non-crushing form of visibility.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking under weight supplies the downward bodily cost from which the exchange begins.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The back supplies the bodily plane that had been forced downward.
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: Literal elevation supplies the reversal from downward loading to upward movement.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Honor and public repute supply the non-material thing raised in place of the burden.

## co present strain and opening
- reading: The creak is the sound of a limit under pressure that is simultaneously being given an opening; strain and passage remain co-present.
- mechanism: Repeated co-presence of difficulty and opening prevents the creaking back from being only a terminal-break image. The strain can be real and near the limit while an opening or easier passage is already alongside it.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking under weight supplies severe, presently registered strain.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back keeps the revised model anchored in the focus body's carrying limit.
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity name the resistant condition corresponding to the focus strain.
  - 94:5 **يُسْرًا** ي س ر B001: Opening and ease after resistance supply a passage that coexists with the loaded state.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: The repeated difficulty image keeps the strain present rather than deleting it.
  - 94:6 **يُسْرًا** ي س ر B001: The repeated opening image makes accompaniment, not a single later rescue, structurally salient.

## torsion to compliance
- reading: The burden deforms the back through resistant twisting, and ease names the return of compliant movement as well as relief.
- mechanism: Difficulty activates as twisting or kinking, while ease activates as light compliance in motion. The undone back can therefore be read mechanically as a frame distorted by torque whose relief is restored range of movement, not merely an improved feeling.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B001: Undoing a firm construction supplies loss of structural integrity under deformation.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back supplies the articulated frame subjected to deformation.
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Twisting and crooked resistance supply torque as the specific form of difficulty.
  - 94:5 **يُسْرًا** ي س ر B005: Lightness and compliant movement supply restored mobility as the form of ease.

## upright redeployment
- reading: Relief removes the buckling kind of load so the same body can stand into purposeful, even tiring, work.
- mechanism: After an imposed load is emptied away, the same body is set upright into chosen exertion. The focus distinguishes two kinds of difficulty: weight that buckles and speaks through the back, versus effort into which the relieved person deliberately stands.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: The involuntary creak under imposed weight supplies the exhausted state from which redeployment begins.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The back supplies the bodily support that can move from buckling pressure to upright action.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel supplies clearance of one load or occupation.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright and conspicuous supplies the recovered posture and deliberate re-engagement.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Exhausting labor supplies the fact that relief redirects effort rather than abolishing it.

## reoriented backing
- reading: The failure of finite backing becomes the occasion for reorienting reliance toward a support characterized by repair and continuance.
- mechanism: The exploratory reading of the back as support is carried into a relational transfer. A burden had been undoing finite backing; desire is then directed toward enduring, repairing lordship. The focus becomes a crisis of what or who can reliably bear and restore.
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B001: Undoing what was firmly constructed supplies the failure of finite support.
  - 94:3 **ظَهْرَكَ** ظ ه ر B006: Backing and assistance supply the support relation placed under threat.
  - 94:8 **رَبِّكَ** ر ب ب B002: Repair, nurture, and completion supply a restorative alternative to the support being undone.
  - 94:8 **رَبِّكَ** ر ب ب B007: Abiding and continuance supply durability lacking in the threatened finite backing.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies the directional transfer of reliance.

## pressure sound to public voice
- reading: The sequence moves from a back forced to sound by pressure to a mention intentionally made audible: bodily noise is displaced by public voice.
- mechanism: 
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: The creak of a loaded back supplies a forced bodily utterance produced by pressure.
  - 94:4 **وَرَفَعْنَا** ر ف ع B010: Raising the voice supplies intentional audibility after the body's involuntary sound.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention moving on the tongue supplies meaningful public speech as the transformed sound.

## emergence through pressure
- reading: At the exploratory edge, pressure cracks an outer layer at the point where obstructed emergence finds an opening.
- mechanism: 
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B003: Earth cracking open for a truffle supplies pressure-linked emergence through a formerly closed surface.
  - 94:3 **ظَهْرَكَ** ظ ه ر B003: The upper or outer surface supplies the layer through which emergence occurs.
  - 94:5 **ٱلْعُسْرِ** ع س ر B006: Obstructed or difficult birth supplies emergence under resistance.
  - 94:5 **يُسْرًا** ي س ر B001: Opening after difficulty supplies the passage by which what is hidden can come through.

## asymmetrical torso torque
- reading: The burden pulls the chest/back axis out of alignment, so the back's creak records torsion as well as weight.
- mechanism: 
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking under weight supplies the mechanical symptom of the torso's distortion.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back supplies the rear member of the distorted torso axis.
  - 94:2 **وِزْرَكَ** و ز ر B004: The chest's lean or skew supplies asymmetry, changing force from simple downward weight into torque across the torso.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Lowering the load supplies the corrective release of the skewing force.

## released breath as aspiration
- reading: At the exploratory edge, unloading releases the compressed torso's rising breath, and that bodily rise becomes directed aspiration.
- mechanism: 
- trace:
  - 94:3 **أَنقَضَ** ن ق ض B005: The loaded back's creak supplies bodily compression at the start of the analogy.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The anatomical back anchors the analogy in a physically loaded torso.
  - 94:8 **رَبِّكَ** ر ب ب B004: Breath rising and swelling supplies physiological release after compression.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward a destination converts released upward breath into directed aspiration.


# Focus 94:4

## exalted renown
- reading: We elevated the standing inhering in your very mention, making each mention bear heightened honor for you.
- mechanism: A status-elevation branch of ر ف ع and a renown branch of ذ ك ر converge on a social-valuational lift: the thing raised is not the body but the standing carried whenever the addressee is mentioned.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B002: Elevation of rank supplies the vertical value-axis on which the addressee's standing is raised.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Honorable reputation supplies the social object that can occupy the higher rank.

## public circulation
- reading: We caused your mention to travel outward and remain publicly audible, multiplying the occasions on which it is voiced.
- mechanism: Elevation becomes propagation rather than only prestige: mention is made public, carried onward, and given greater audibility across speakers.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Publicizing and relaying a report turns upward movement into outward circulation.
  - 94:4 **وَرَفَعْنَا** ر ف ع B010: Vocal height gives the circulation an audible register rather than a purely reputational one.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention running on tongues supplies the transmissible content whose reach and audibility increase.

## retrievable remembrance
- reading: We lifted remembrance of you into durable cognitive reach, so it can be recalled and reactivated rather than sink into forgetting.
- mechanism: What lies low or latent is lifted into availability: remembrance is brought above the threshold of forgetting and made easy to recover in mind.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: Literal upward displacement supplies a cognitive topology from latent depth to accessible prominence.
  - 94:4 **ذِكْرَكَ** ذ ك ر B003: Recall after or against forgetting identifies the raised object as renewed mental presence.
  - 94:4 **ذِكْرَكَ** ذ ك ر B009: The reminder branch makes that mental presence reproducible through cues, not merely a one-time recollection.

## opened source to expression
- reading: Your mention was raised as the outward, publicly voiced issue of an interior that had first been opened to meaning.
- mechanism: The opened and clarified interior is also the source from which acts issue; the later raised mention can therefore be read as outward expression generated by an inwardly opened source. Public circulation is revised from externally conferred publicity into an inside-to-outside movement of articulability.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Public transmission supplies the outward endpoint of the interior-to-expression movement.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Voiced mention supplies the expressive product that moves from interior source to public tongue.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarifying meaning supplies an interior operation that makes expression possible.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which actions issue turns the chest into the mechanism's generative interior.

## load lift reversal
- reading: We completed a load-to-lift reversal: weight that bent your back was taken down, while the social weight of your mention was raised.
- mechanism: A heavy load is set down from a back that audibly strains, followed by the raising of mention. The sequence creates a vertical redistribution: oppressive weight leaves the private bearer while valued weight rises in the public object of mention.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: Physical upward displacement supplies the lifting half of the down/up reversal.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Renown converts the lifted element from bodily load into socially valued prominence.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Placing something lower supplies the downward motion opposed by the focus ayah's lift.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy-load branch identifies what the lowering action removes from the addressee.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints or back under weight supplies evidence of load beyond sustainable bearing.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The bodily back supplies the private load-bearing surface from which oppressive weight is removed.

## reputational rectification
- reading: We first displaced a false or crooked account attached to you and then raised a corrected mention into public circulation.
- mechanism: The non-dominant split inventory for و ز ر activates deviation and false discourse. Read beside setting-down and public mention, this yields a reputational repair model: distorted speech is displaced before the addressee's mention is amplified.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Broadcasting a report supplies the later amplification stage whose content must first be distinguished from distortion.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Speech about the addressee supplies the discourse field in which correction and renewed circulation occur.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something down supplies the removal or demotion of the distorted account.
  - 94:2 **وِزْرَكَ** و ز ر B002: The split-root image of false and baseless speech supplies the reputational obstruction that is set aside.

## co present resilience
- reading: Your mention was raised into a resilient availability that can accompany adversity, bearing an opening within pressure without denying the pressure.
- mechanism: The repeated pairing of difficulty with an opening revises elevation from a post-crisis trophy into a resource that can coexist with constraint. Raised remembrance remains available inside hardship rather than proving that hardship has vanished.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B002: Elevated standing supplies a benefit whose coexistence with continuing difficulty must be explained.
  - 94:4 **ذِكْرَكَ** ذ ك ر B003: Recoverable remembrance supplies an inwardly available resource during constraint, not only an external reputation after it.
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity supply the constraint within which raised remembrance remains operative.
  - 94:5 **يُسْرًا** ي س ر B001: An opening into ease supplies the concurrent affordance carried within the constraint.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: The repeated severity image prevents the reading from treating elevation as simple erasure of hardship.
  - 94:6 **يُسْرًا** ي س ر B001: The repeated opening image makes availability under pressure durable rather than momentary.

## sonic enactment
- reading: Your mention is raised anew whenever cleared time is turned into an act of elevated voice.
- mechanism: After a cleared interval, the imperative whose inventory includes raising the voice in song activates a performed reading of 94:4. Raised mention is not only a fact reported about reputation; it becomes an event repeatedly enacted in voiced remembrance.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B010: Vocal height supplies the acoustic dimension of the focus ayah's raising.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention on the tongue supplies the verbal material that can be audibly performed.
  - 94:7 **فَرَغْتَ** ف ر غ B001: Clearance after occupation supplies the temporal opening in which renewed voicing can occur.
  - 94:7 **فَٱنصَبْ** ن ص ب B009: A song or chant that raises the voice supplies the surprising performative trigger for audible mention.

## directional waymarker
- reading: Your raised remembrance is an elevated waymarker: conspicuous for your benefit, yet functionally directing desire toward your Lord rather than terminating it on you.
- mechanism: An erected marker, sovereign destination, and directed desire recast raised remembrance as a waymarker rather than a terminal monument. Its prominence has a routing function: attention encountered at the raised mention is sent onward toward the Lord.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: Elevation makes the reminder visible enough to function as a marker in a directional field.
  - 94:4 **ذِكْرَكَ** ذ ك ر B009: The reminder branch supplies the signifying object that points beyond its own prominence.
  - 94:7 **فَٱنصَبْ** ن ص ب B003: An erected boundary or water-place marker supplies the concrete wayfinding analogy.
  - 94:8 **رَبِّكَ** ر ب ب B001: Sovereignty and mastery identify the destination to which the marker's prominence is subordinated.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies the directional motion that the raised reminder channels.

## juridical attestation
- reading: We advanced for you a claim-bearing memorial into recognized standing, as though your mention were formally presented and attested.
- mechanism: 
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B004: Bringing a person or case before authority supplies the act of formal presentation.
  - 94:4 **ذِكْرَكَ** ذ ك ر B008: A documentary instrument of right supplies the presented object and its claim-bearing force.

## kinetic propagation
- reading: We gave your voiced mention a raised gait, enabling it to travel lightly and persistently through obstructed conditions.
- mechanism: 
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B003: An intensified but controlled gait supplies the propagation speed and persistence of the mention.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Tongue-borne mention supplies what moves from speaker to speaker.
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Twisting, obstruction, and imposed difficulty supply resistant terrain for the mention's movement.
  - 94:5 **يُسْرًا** ي س ر B005: Light, tractable motion supplies the changed gait by which mention crosses that resistance.

## reservoir release
- reading: Elevation can also preserve remembrance in a charged reserve, releasing it at a fitting opening rather than spending it in constant display.
- mechanism: 
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B007: Withholding milk in a reservoir supplies controlled retention rather than immediate outward flow.
  - 94:4 **ذِكْرَكَ** ذ ك ر B003: Mental retention and renewed recall supply the content preserved in reserve.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel supplies the later release phase of the reservoir model.


# Focus 94:5

## concurrent opening
- reading: A ready opening accompanies the definite hardship while it is still operative.
- mechanism: The two opposed branch images are joined by accompaniment rather than an explicit after-sequence: the bounded hard condition and a ready opening occupy the same interval.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity supply the resistant condition that is present, not merely remembered.
  - 94:5 **يُسْرًا** ي س ر B001: Ease as a ready opening supplies an available passage within the hard condition.

## margin of means
- reading: Even inside a condition of shortage there is an accompanying margin of means, readiness, or accommodation.
- mechanism: Straitened means do not occupy the whole field: a presently usable margin of means and lenient possibility coexists with insolvency.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B002: Financial straitness makes hardship a concrete shortage of available means.
  - 94:5 **يُسْرًا** ي س ر B003: Prosperity and means provide a counter-margin of usable capacity inside scarcity.
  - 94:5 **يُسْرًا** ي س ر B001: Lenient dealing widens the economic model from possession to practicable accommodation.

## maneuverability inside resistance
- reading: Ease may be the capacity to move pliantly through resistance that remains present.
- mechanism: Ease is recast from removal of the obstacle to maneuverability inside it: resistance remains, but the agent acquires compliance, traction, and a path of motion.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Opposition and entanglement supply a field that obstructs or twists movement.
  - 94:5 **يُسْرًا** ي س ر B005: Light and pliant movement supplies adaptive mobility as the operative form of ease.

## interior operating room
- reading: Ease can be an enlarged interior operating room that is already active while hardship presses.
- mechanism: The prior opening of the chest relocates yusr from an external event to increased interior room at the source of action; hardship and ease can therefore coexist in one person as pressure and expanded capacity.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Severity supplies the pressure under which the interior capacity matters.
  - 94:5 **يُسْرًا** ي س ر B001: A ready opening names the usable room activated inside the person.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarifying supply the expansion operation that makes a passage available.
  - 94:1 **نَشْرَحْ** ش ر ح B005: Desire spreading toward something gives the opening an affective and directional interior dimension.
  - 94:1 **صَدْرَكَ** ص د ر B004: The origin from which actions issue locates ease in an expanded capacity to act.

## unloading vector
- reading: Ease is already present as the burden's active lowering and redistribution.
- mechanism: A heavy load and the act of lowering it form one process. Under مَعَ, yusr is the unloading vector already acting on the burden, not only the empty state after it is gone.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Severity names the experienced load-bearing condition.
  - 94:5 **يُسْرًا** ي س ر B001: Readiness and opening become the progressive release created as the load is lowered.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something into a lower or settled position supplies the downward relief operation.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies the object on which the easing operation works.

## deflection and realignment
- reading: Hardship can be a weight-induced deflection, while ease is regained alignment and maneuverability under load.
- mechanism: The split inventory lets the burden be seen both as weight and as deviation. Joined to the focus roots' entanglement and pliant motion, hardship bends the path while ease is the ability to realign and continue.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Entanglement and twisting make hardship a distorted route rather than only an amount of pain.
  - 94:5 **يُسْرًا** ي س ر B005: Pliant movement supplies the adaptive realignment that preserves forward motion.
  - 94:2 **وِزْرَكَ** و ز ر B002: The dominant mapped branch contributes the weight that forces the path out of shape.
  - 94:2 **وِزْرَكَ** و ز ر B001: The non-dominant mapped branch contributes inclination and deviation as a spatial model of burden.

## back as burden and support
- reading: One load-bearing structure can register hardship and furnish its support at the same time.
- mechanism: The back is simultaneously where weight becomes audibly severe and the structure by which support is supplied. This turns accompaniment into a load-bearing relation: the same stressed site carries both hardship and its assisting capacity.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Severity names the body's threshold of strain.
  - 94:5 **يُسْرًا** ي س ر B001: A ready opening becomes available support rather than mere future comfort.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints or back under weight make hidden strain perceptible at its limit.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The literal back fixes burden and assistance at one bodily site.
  - 94:3 **ظَهْرَكَ** ظ ه ر B006: Strength gained through a back or helper supplies the counterforce carried by that same site.

## fissure as aperture
- reading: Hardship's own fracture line may disclose the aperture through which ease becomes available.
- mechanism: Entanglement is not simply lifted; its stressed joining reopens, and what was hidden comes to the surface. Ease is the aperture produced or disclosed at hardship's fracture line.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B004: Entanglement supplies the tightly joined configuration that resists passage.
  - 94:5 **يُسْرًا** ي س ر B001: The ready opening supplies the aperture that becomes usable.
  - 94:3 **أَنقَضَ** ن ق ض B004: A joined thing reopening supplies fracture as an opening operation.
  - 94:3 **ظَهْرَكَ** ظ ه ر B001: Emergence and disclosure make the opening visible rather than importing a separate rescue.

## recognized standing
- reading: Ease may also be restored standing, public credit, or an acknowledged claim that enlarges agency before wealth changes.
- mechanism: The economic baseline expands into a social-legal one: easing can consist in elevated standing, circulating recognition, or an accredited claim even while material straitness remains.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B002: Straitened means preserve the material hardship that recognition does not automatically erase.
  - 94:5 **ٱلْعُسْرِ** ع س ر B003: Pressure on an insolvent debtor supplies the legal-social relation in which standing matters.
  - 94:5 **يُسْرًا** ي س ر B003: Means provide the baseline resource sense that is revised into recognized capacity.
  - 94:4 **وَرَفَعْنَا** ر ف ع B002: Elevation of rank supplies restoration of public standing as a form of easing.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Honor and reputation supply socially circulating credit.
  - 94:4 **ذِكْرَكَ** ذ ك ر B008: A document of right supplies the exploratory possibility of an acknowledged claim or entitlement.

## renewed accompaniment
- reading: The accompaniment is reiterated as a renewable relation in which the hardship does not exhaust possible openings.
- mechanism: The full branch pair recurs in 94:6. Repetition makes accompaniment durable and renewable: a named hardship does not exhaust the arrival of fresh, non-totalized openings.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: The definite severe condition supplies the stable side of the repeated relation.
  - 94:5 **يُسْرًا** ي س ر B001: The indefinite ready opening supplies a non-exhausted instance of possibility.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Repeated severity carries the same bounded hardship into a second assertion.
  - 94:6 **يُسْرًا** ي س ر B001: Repeated opening renews the availability of ease rather than closing it as a single event.

## capacity recommissioned
- reading: Ease is freed and pliant capacity that can be recommissioned into chosen exertion.
- mechanism: The opening of yusr behaves like capacity emptied from one occupation and immediately stood up for deliberate exertion. Ease is usable bandwidth and freedom of deployment, not idleness or the abolition of effort.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty remains compatible with the new task, preventing ease from meaning effortlessness.
  - 94:5 **يُسْرًا** ي س ر B001: Readiness supplies freed capacity available for a next act.
  - 94:5 **يُسْرًا** ي س ر B005: Pliant movement turns available capacity into responsive execution.
  - 94:7 **فَرَغْتَ** ف ر غ B001: Vacancy after occupation supplies the release of capacity from a completed engagement.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Emptying a vessel gives released capacity a concrete container-and-flow mechanism.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright converts emptied capacity into a newly established stance.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Exhausting toil keeps strenuous effort inside the post-ease field.

## directed cultivated spaciousness
- reading: Ease is spacious, cultivated capacity whose desire can be oriented toward completion.
- mechanism: Yusr becomes a developmental and directional space: it is cultivated toward completion, enlarged, and oriented to an endpoint. The relief is not an ungoverned opening but room whose desire and growth acquire direction.
- trace:
  - 94:5 **يُسْرًا** ي س ر B001: A ready opening supplies the space that can be cultivated and directed.
  - 94:5 **يُسْرًا** ي س ر B003: Breadth of means makes the opening productive rather than merely empty.
  - 94:8 **رَبِّكَ** ر ب ب B002: Repair, nurture, and completion supply the dominant developmental governance of the opening.
  - 94:8 **رَبِّكَ** ر ب ب B005: The non-dominant mapped branch contributes nourishment and growth as an exploratory developmental texture.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies a vector that determines how available room is used.
  - 94:8 **فَٱرْغَب** ر غ ب B002: A wide cavity or spatial extension gives yusr's opening a literal spacious analogue.

## delivery contains increase
- reading: Hardship can be labor that is already carrying the emergence and nourishment of what it delivers.
- mechanism: 
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B006: Difficult childbirth makes hardship a constricted process of bringing forth.
  - 94:5 **يُسْرًا** ي س ر B006: Productive increase in milk and offspring supplies emergence and sustenance as the accompanying ease.
  - 94:2 **وَوَضَعْنَا** و ض ع B002: Laying down a burden through childbirth links release to delivery rather than simple disappearance.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel gives delivery a container-transition image.
  - 94:8 **رَبِّكَ** ر ب ب B005: The split-root nourishment and growth image carries what emerges into development.

## shared left substrate
- reading: Both can inhabit one lateral field, with ease arising through a changed orientation or use within the same condition.
- mechanism: 
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B005: Left-sidedness gives hardship one lateral embodiment.
  - 94:5 **يُسْرًا** ي س ر B004: The same left-side field gives ease an overlapping rather than opposite spatial substrate.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies reorientation as the operation that differentiates one shared field.

## distributed seams
- reading: Hardship arrives as a train of episodes while ease appears as distinct seams traced through that train.
- mechanism: 
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B011: Scattering and one-after-another movement turn hardship into a distributed train of episodes.
  - 94:5 **يُسْرًا** ي س ر B008: Separated lines or marks make ease visible as discrete seams rather than a total replacement.
  - 94:6 **ٱلْعُسْرِ** ع س ر B011: The repeated distributed image extends the hardship pattern across successive beats.
  - 94:6 **يُسْرًا** ي س ر B008: The repeated marking image supports more than one distinguishable seam of ease.

## cast and apportioned share
- reading: As a contained image, the hard setup and cast already include an apportioning process through which a usable share emerges.
- mechanism: 
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B013: The stick game supplies a hard setup in which an erected obstacle is engaged by a cast.
  - 94:5 **يُسْرًا** ي س ر B007: Lots and division into shares supply an apportioned outcome inside the constrained game.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting an object upright and prominent completes the physical game apparatus.
  - 94:8 **رَبِّكَ** ر ب ب B010: A container gathering lots supplies the device from which apportioned possibilities are drawn.


# Focus 94:6

## co present opening
- reading: Within the identified hardship there is already an as-yet-indefinite opening by which it can be inhabited or traversed.
- mechanism: Hardship supplies the encompassing constrained condition while ease supplies an opening or readiness already operating inside that condition; the relation is simultaneous before it is sequential.
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity supply the constraining condition within which the relational construction works.
  - 94:6 **يُسْرًا** ي س ر B001: Ready opening and ease supply an affordance located with, not only after, the constraint.

## local dose of ease
- reading: A slight but usable easing can coexist with a hardship that still names the whole situation.
- mechanism: The hard condition may occupy the whole named field while ease appears locally as a slight interval, margin, or dose; co-presence does not require equal size.
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity provide the large-scale field experienced as hardship.
  - 94:6 **يُسْرًا** ي س ر B002: Littleness supplies the possibility that the accompanying ease is small yet operationally real.

## means inside straitness
- reading: Even within constricted means, some means-to-act accompanies the shortage and prevents it from being a closed totality.
- mechanism: Scarcity is not treated as absolute emptiness: a margin of solvency, resource, or capacity can remain present inside financial or material straitness.
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B002: Straitness of means turns hardship into a concrete resource constraint.
  - 94:6 **يُسْرًا** ي س ر B003: Prosperity and means supply the usable resource margin accompanying that constraint.

## readiness instead of force
- reading: Hardness can be intensified by premature forcing, while a ready and responsive way through it is already available.
- mechanism: Part of hardness may arise from taking, speaking, or moving before preparation; ease is the co-present alternative of waiting for readiness and moving responsively.
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B008: Riding or taking before readiness supplies a mechanism in which mistimed force produces hardness.
  - 94:6 **يُسْرًا** ي س ر B001: Becoming ready and open supplies the alternative timing by which the same affair becomes tractable.
  - 94:6 **يُسْرًا** ي س ر B005: Pliant, responsive movement supplies the practical behavior of ease rather than mere comfort.

## opened inner capacity
- reading: Ease can be an internally opened capacity for action that accompanies an externally hard circumstance.
- mechanism: Opening at the bodily and agentive source turns abstract ease into expanded working capacity inside the person who still occupies hardship.
- trace:
  - 94:6 **يُسْرًا** ي س ر B001: Ready opening anchors the changed reading in the focus word for ease.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarification supply an expansion operation rather than a later replacement event.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which actions issue locates that expansion at the point where agency begins.

## load reconfiguration
- reading: Ease is a changed load-bearing relation—lowering, support, and mobility—that can operate while the hard task remains.
- mechanism: The context supplies a mechanical chain of lowering a heavy load from a back that audibly strains; ease becomes altered load placement and recovered compliance while the demanding terrain can remain.
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity anchor the still-demanding condition after the load relation changes.
  - 94:6 **يُسْرًا** ي س ر B005: Pliant movement supplies the regained mobility produced by better load distribution.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something into a lower or settled position supplies the load-transfer operation.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy burden supplies the force whose placement matters.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints or back under weight supplies the observable failure signal of excessive loading.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The back supplies the load-bearing surface on which strain and relief can coexist.

## recurrent reopening
- reading: Ease is the repeated recoverability of an opening within a condition that can tighten again.
- mechanism: Two distinct opening images make ease dynamic: an initial expansion can be followed by closure or strain and then by reopening, so ease is recoverable rather than a single irreversible switch.
- trace:
  - 94:6 **يُسْرًا** ي س ر B001: Ready opening anchors the recurrent process in the focus word.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarification supply the first expansion in the sequence.
  - 94:3 **أَنقَضَ** ن ق ض B004: Reopening after closure supplies recurrence and reversibility rather than a one-time transition.

## socially distributed ease
- reading: Ease may also be socially distributed capacity: a name carried, heard, and supported while personal hardship remains.
- mechanism: Raising and circulating mention activate a social channel of ease: recognition, audibility, and standing can increase the range of action even when private difficulty persists.
- trace:
  - 94:6 **يُسْرًا** ي س ر B003: Expanded means anchor social standing as a possible form of usable ease.
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: Broadcasting news supplies outward propagation rather than merely vertical elevation.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention running on tongues supplies the network through which recognition circulates.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: Repute and honor supply the social capital created by that circulation.

## iterated openings
- reading: The hard field can be met by repeatedly renewed openings; ease behaves as a pattern of access, not a one-use event.
- mechanism: The adjacent re-predication turns co-presence into an iterative pattern: the same named hardship is met by a freshly asserted, indefinite opening rather than exhausted by one occurrence.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: The first occurrence supplies the recurring field of difficulty.
  - 94:5 **يُسْرًا** ي س ر B001: The first ease occurrence supplies one ready opening within that field.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: The repeated hardship keeps the difficult field present rather than narrating its disappearance.
  - 94:6 **يُسْرًا** ي س ر B001: The repeated ease renews the opening and makes recurrence visible.

## released capacity for exertion
- reading: Ease is freed capacity: enough openness to stand up, choose a new task, and exert oneself again.
- mechanism: Vacancy after occupation feeds directly into standing up and exerting oneself, revising ease from terminal rest into released capacity that can be committed to another demanding act.
- trace:
  - 94:6 **يُسْرًا** ي س ر B001: Readiness and opening anchor ease as newly available capacity.
  - 94:7 **فَرَغْتَ** ف ر غ B001: Vacancy after occupation supplies the release of capacity.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright and conspicuous supplies renewed directed engagement.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Exhausting toil keeps effort inside the semantic field that follows ease.

## oriented cultivable growth
- reading: Ease is capacity that can be nurtured, enlarged, and given direction toward its sustaining source.
- mechanism: Nurture, growth, spatial breadth, and directed desire turn ease into a cultivable vector: capacity increases by being oriented toward a sustaining source rather than remaining undirected comfort.
- trace:
  - 94:6 **يُسْرًا** ي س ر B003: Prosperity and means anchor the changed reading in an increase of usable capacity.
  - 94:8 **رَبِّكَ** ر ب ب B002: Repair, nurture, and completion supply the process by which capacity is cultivated.
  - 94:8 **رَبِّكَ** ر ب ب B005: The non-dominant mapped branch of feeding and growth keeps literal increase live within the split inventory.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire directed toward or away supplies the vector that channels available capacity.
  - 94:8 **فَٱرْغَب** ر غ ب B002: Breadth and spatial extension supply room for that directed growth.

## free volume
- reading: Ease can be imagined as free volume opened inside the same loaded system, permitting breath, movement, and renewed work.
- mechanism: 
- trace:
  - 94:6 **يُسْرًا** ي س ر B001: Ready opening anchors free capacity in the focus word for ease.
  - 94:1 **نَشْرَحْ** ش ر ح B002: Spreading and cutting flesh supply a deliberately material image of making internal room.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest supplies the bounded container in which expansion is imagined.
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a vessel supplies vacant volume after prior occupation.
  - 94:8 **فَٱرْغَب** ر غ ب B002: A wide cavity or spatial extension supplies the resulting breadth.

## lateral reorientation
- reading: A branch-distant spatial echo lets ease appear as turning or changing aspect within the same terrain, not merely reducing its quantity.
- mechanism: 
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B005: The left side and left-handedness turn hardship's root into one lateral orientation.
  - 94:6 **يُسْرًا** ي س ر B004: The left side, left hand, and turning left make ease's root converge on the same lateral field.
  - 94:2 **وِزْرَكَ** و ز ر B001: The non-dominant split branch of inclination and turning supplies reorientation as a way of changing the load relation.
  - 94:3 **ظَهْرَكَ** ظ ه ر B018: Turning a matter back-to-belly supplies a full change of aspect without changing the underlying matter.

## apportioned ease
- reading: Ease may arise by apportioning a constrained whole into usable shares, so better distribution accompanies scarcity without first abolishing it.
- mechanism: 
- trace:
  - 94:6 **ٱلْعُسْرِ** ع س ر B002: Straitness of means supplies the scarcity problem that requires allocation.
  - 94:6 **يُسْرًا** ي س ر B007: Lots and division into shares supply allocation as a way to produce usable portions from one constrained whole.
  - 94:8 **رَبِّكَ** ر ب ب B010: The container that gathers lots supplies coordination of the distributive process.


# Focus 94:7

## release to chosen strain
- reading: Whenever an occupation releases you, convert the newly free capacity immediately into chosen exertion.
- mechanism: Freedom after occupation is treated as newly available capacity, and the following imperative immediately spends that capacity in effort. Completion is therefore a transfer point rather than a terminal rest.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B001: Freedom or emptiness after occupation supplies the released capacity at the first side of the relay.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Weariness and strenuous toil supply the costly effort into which that released capacity is converted.

## empty then erect
- reading: Empty the occupied space, then use the clearance to establish a visible, upright form of action.
- mechanism: The first verb can image contents being poured out of a vessel; the second can image something being fixed upright and made salient. The verse then becomes a clear-and-establish operation: removal creates the room in which a new stance or work can be installed.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out and emptying a container supplies active evacuation rather than passive leisure.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright and prominent supplies the constructive form that follows evacuation.

## exclusive attention fixed
- reading: When attention has been cleared and made single, establish that devotion on a fixed, upright footing.
- mechanism: The condition is not only that a prior task has ended; it can mark attention becoming exclusive. The imperative answers that concentration by giving it stable footing, measure, and outward form.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B006: Deliberately turning and devoting oneself to a matter supplies exclusive attention.
  - 94:7 **فَٱنصَبْ** ن ص ب B006: A fixed base, origin, or threshold supplies durable footing and measure for the devoted action.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Upright prominent placement turns inward concentration into an established stance.

## opened interior issues into stance
- reading: Gather the already opened interior around one purpose, then let action issue from it as an upright stance.
- mechanism: The opened chest is also an interior origin from which action issues. This revises focus-only clearance into an inside-to-outside movement: gathered attention proceeds from an expanded source and becomes an upright stance.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B006: Deliberate turning gathers the cleared interior around one matter.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Upright prominence gives the gathered interior an embodied and outwardly legible stance.
  - 94:1 **نَشْرَحْ** ش ر ح B001: Opening and clarification make the prior interior change an enabling expansion, not merely the end of a task.
  - 94:1 **صَدْرَكَ** ص د ر B004: The source from which actions issue locates the expansion upstream of the focus imperative.

## relieved load becomes chosen strain
- reading: Once crushing weight has been removed, answer relief with self-directed effort and an upright stance, not with either inertia or re-subjection.
- mechanism: A heavy load is put down from a back that had audibly yielded under it. Against that relief sequence, فَٱنصَبْ cannot be reduced to restoration of the same crushing burden: it becomes a chosen exertion that also lets the relieved body stand upright.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B001: Freedom after occupation supplies the state produced when the oppressive load no longer occupies the addressee.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Strain and toil preserve genuine cost in the new action, preventing relief from becoming inertia.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Upright erection supplies bodily recovery and active stance after the back's compression.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: Putting something into a lower or settled place supplies the downward removal that precedes renewed action.
  - 94:2 **وِزْرَكَ** و ز ر B002: The heavy carried load identifies the prior strain as imposed weight rather than freely assumed effort.
  - 94:3 **أَنقَضَ** ن ق ض B005: Creaking joints and back under weight supply the bodily failure mode from which relief releases the addressee.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The literal back fixes the load-and-uprighting mechanism in bodily posture.

## elevated mention becomes voiced installation
- reading: When deliberately available, establish and raise an audible act of mention alongside the verse's demand for effort.
- mechanism: The raising of mention activates a less expected branch of ن ص ب: raised-voice song or chant. Coupled with deliberate availability, the focus imperative can carry an audible, publicly projected act alongside bodily toil.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B006: Deliberate devotion supplies focused availability for an intentional vocal act.
  - 94:7 **فَٱنصَبْ** ن ص ب B009: A raised-voice song or riders' chant supplies the unexpected audible realization of the imperative.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Prominent upright placement keeps the vocal act anchored as something established and projected.
  - 94:4 **وَرَفَعْنَا** ر ف ع B010: Raising the voice supplies the acoustic upward motion that activates the focus root's chant branch.
  - 94:4 **ذِكْرَكَ** ذ ك ر B004: Mention running on the tongue supplies vocal content rather than undirected sound.

## ease as recurring working clearance
- reading: Recognize each opening that arrives within continuing difficulty as a launch window for renewed, self-directed exertion.
- mechanism: The doubled co-presence of difficulty and ease makes فَرَغْتَ a local opening inside an unfinished field of hardship, not necessarily the final disappearance of difficulty. فَٱنصَبْ turns each such opening into the next cycle of effort.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B001: Freedom after occupation supplies a bounded interval of availability rather than requiring total historical completion.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: Toil and strain convert each available interval into another active cycle.
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: Difficulty and severity supply the continuing resistant field in which a clearance appears.
  - 94:5 **يُسْرًا** ي س ر B001: Opening and ease supply the first explicitly named release within that resistant field.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: Repeated difficulty keeps the mechanism iterative rather than allowing a single final escape.
  - 94:6 **يُسْرًا** ي س ر B005: Lightness and compliant movement make the second ease an actionable opening, not merely an abstract consolation.

## directed axis toward lord
- reading: Clear and collect attention, establish a durable upright stance, and let the next verse aim that stance toward the Lord.
- mechanism: The next imperative supplies a destination and a directed desire. It strengthens the focus-only devotion model by turning فَٱنصَبْ into the installation of an oriented axis: cleared attention becomes an upright, sustained stance whose vector is toward the Lord.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B006: Deliberate turning to one matter supplies the collection of attention before it receives a destination.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Setting something upright and prominent supplies the stance or axis that can be directionally aimed.
  - 94:7 **فَٱنصَبْ** ن ص ب B003: An erected marker or boundary stone supplies an orienting point rather than objectless exertion.
  - 94:8 **رَبِّكَ** ر ب ب B001: Lordship, ownership, and sovereignty identify the governing destination of the established stance.
  - 94:8 **رَبِّكَ** ر ب ب B007: Abiding and persistence give the orientation duration rather than a momentary gesture.
  - 94:8 **فَٱرْغَب** ر غ ب B001: Desire turning toward or away supplies the directional vector and makes its chosen orientation consequential.

## hydraulic boundary
- reading: Release what occupied the vessel, then give the released capacity an erected edge so it acquires direction instead of dissipating.
- mechanism: 
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B002: Pouring out a vessel supplies release as directed flow rather than simple cessation.
  - 94:7 **فَٱنصَبْ** ن ص ب B003: Erected stones around a cistern supply the boundary that contains and shapes what release makes available.
  - 94:8 **فَٱرْغَب** ر غ ب B002: A wide cavity or spatial extension enlarges the receiving space in the material mechanism.

## split chest realignment
- reading: After release from compressive occupation, open and realign the chest-back axis into an upright stance.
- mechanism: 
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B001: Release after occupation supplies freedom from the condition that held the body compressed.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Upright erection supplies the corrective endpoint of the bodily realignment.
  - 94:1 **صَدْرَكَ** ص د ر B001: The bodily chest supplies the front plane whose opening can be registered as posture.
  - 94:2 **وِزْرَكَ** و ز ر B004: The non-dominant mapped image of a chest's slope supplies the oblique posture to be corrected.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The literal back completes the front-back bodily axis on which the realignment occurs.

## cultivated upright growth
- reading: Clear the occupied capacity so disciplined cultivation can raise a new form from it.
- mechanism: 
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B002: Emptying a vessel supplies cleared capacity in which development can occur.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: Upright prominence supplies the visible emergence produced by cultivation.
  - 94:8 **رَبِّكَ** ر ب ب B005: The non-dominant mapped branch of feeding and growth supplies the developmental process between clearance and emergence.

## spacious easy march
- reading: Use released room to enter a sustained, light-footed march whose endurance is itself the exertion.
- mechanism: 
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B003: Breadth in gait, movement, or path supplies room for sustained forward motion.
  - 94:7 **فَٱنصَبْ** ن ص ب B010: A full-day easy march supplies duration and steady pacing rather than a short convulsion of effort.
  - 94:6 **يُسْرًا** ي س ر B005: Lightness and compliance in motion reinforce the possibility that renewed exertion can be sustainable and fluid.


# Focus 94:8

## directional desire under lordship
- reading: Recenter the whole direction of wanting under your Rabb's authority; the command regulates desire's vector before it specifies any desired object.
- mechanism: Desire can turn toward or away, while Rabb can name ownership and authority. The prepositional endpoint therefore governs the vector of wanting itself rather than merely naming one wanted object.
- trace:
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal image of lordship, ownership, and authority makes the endpoint the governor of desire rather than one item within its field.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal reversibility of desire toward or away supplies a vector that the focus construction fixes toward Rabb and, by implication, away from rival endpoints.

## desire as consent to formation
- reading: Long toward the One who forms and completes you, so aspiration includes consent to being repaired, reared, and brought to completion.
- mechanism: If Rabb is the one who repairs, nurtures, administers, and completes stage by stage, then turning desire toward this Rabb can be willing exposure to formation, not only appetite for benefits.
- trace:
  - 94:8 **رَبِّكَ** ر ب ب B002: The literal image of repair, nurture, and gradual completion supplies the formative agency toward which the imperative directs the addressee.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal inclination toward an object functions here as voluntary alignment with the Rabb's ongoing formative work.

## capacious persistent aspiration
- reading: Make and maintain a broad capacity that leans toward your Rabb; aspiration becomes an enduring spatial posture.
- mechanism: The imperative can spatialize desire as a broad interior capacity held in a durable orientation: not a brief wish, but room made and kept open toward Rabb.
- trace:
  - 94:8 **فَٱرْغَب** ر غ ب B002: The literal image of breadth, a capacious hollow, or extended ground supplies the widened interior space of aspiration.
  - 94:8 **رَبِّكَ** ر ب ب B007: The literal image of staying, clinging, lasting, and drawing near turns broad desire into a maintained proximity rather than a passing impulse.

## giver over desirable gift
- reading: Let bounty awaken desire without becoming its terminus: the longing passes through the gift and settles on the Rabb who governs and completes.
- mechanism: The command does not erase longing for gifts; it relocates the terminus of that longing from bounty to the authoritative, nurturing giver.
- trace:
  - 94:8 **فَٱرْغَب** ر غ ب B004: The literal image of abundant desirable giving keeps bounty within the semantic field while exposing the risk of stopping desire at the gift.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal image of ownership and lordship relocates desire's terminus from possessed bounty to the one who owns and governs it.
  - 94:8 **رَبِّكَ** ر ب ب B002: The literal image of nurture and completion makes the giver desirable as a continuing relation, not merely as a source of consumable rewards.

## opened source becomes desiderative capacity
- reading: The chest is opened as the source and capacity of action, and «فارغب» is the final release of that enlarged interior in a vector toward Rabb.
- mechanism: The first ayah can describe an opening that specifically lets desire spread, and the chest can be the source from which acts issue. The final imperative then reads as the downstream act of an interior source deliberately enlarged at the opening of the sequence.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B005: The literal image of desire spreading toward something supplies an aperture-and-expansion mechanism that anticipates the focus's directed wanting.
  - 94:1 **صَدْرَكَ** ص د ر B004: The literal image of an origin from which actions issue locates the opened chest as the upstream source of the later imperative.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal toward-or-away motion of desire supplies the downstream vector produced by the reconfigured source.
  - 94:8 **فَٱرْغَب** ر غ ب B002: The literal image of capaciousness makes the opening an enlargement of room for aspiration rather than generic emotional relief.

## released load becomes available capacity
- reading: The burden is removed so crushed carrying-space can become spacious directed desire; «فارغب» names the active use of relief rather than another weight.
- mechanism: A heavy load is put down after making the back audibly strain. Against that bodily subtraction, the capacious branch of desire makes the final imperative a use of released carrying-space, not a fresh demand laid on the same back.
- trace:
  - 94:2 **وَوَضَعْنَا** و ض ع B001: The literal image of putting something down in a lower or settled place supplies the decisive transfer off the addressee.
  - 94:2 **وِزْرَكَ** و ز ر B002: The literal heavy load identifies what had occupied and compressed the addressee's finite capacity.
  - 94:3 **أَنقَضَ** ن ق ض B005: The literal creaking of joints or back under weight renders the burden as a mechanism of near-failure rather than an abstract concern.
  - 94:3 **ظَهْرَكَ** ظ ه ر B002: The literal bodily back gives the load a concrete bearing surface whose release can be contrasted with inwardly chosen aspiration.
  - 94:8 **فَٱرْغَب** ر غ ب B002: The literal image of a broad hollow or extended capacity turns unloading into newly available room for desire.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal vector of inclination gives the released capacity an active destination instead of leaving it merely vacant.

## corrected tilt becomes arrival
- reading: The removal also images the straightening of a bent vector, so desire becomes purposeful approach and arrival at Rabb.
- mechanism: The packet's non-dominant mapped inventory lets the removed burden resonate with tilt or deviation and with a visitor's purposeful coming. The focus can then be heard as a corrected vector: what had bent movement aside is removed so desire can aim toward and arrive at Rabb.
- trace:
  - 94:2 **وِزْرَكَ** و ز ر B001: The literal image of leaning and deviation recasts the burden as a skew in orientation that must be corrected.
  - 94:2 **وِزْرَكَ** و ز ر B003: The literal image of visiting and purposeful coming supplies arrival as the positive motion made possible after the skew is removed.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal toward-or-away vector of desire is the focus anchor whose direction can be straightened from deviation into approach.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal image of lordship and authority provides the destination at which corrected, purposeful movement terminates.

## public elevation is returned not consumed
- reading: Return the appetite awakened by public elevation to Rabb: reputation is a bestowed sign, not the endpoint that desire should consume and amplify.
- mechanism: Raised, broadcast reputation is an especially plausible rival object for desire. By ending at «your Rabb», the focus converts bestowed public elevation into a reason to return desire to its source rather than seek ever more circulation of the self.
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B005: The literal broadcasting of news makes elevation socially circulatory and exposes publicity as a possible appetite.
  - 94:4 **ذِكْرَكَ** ذ ك ر B007: The literal image of honor and reputation identifies the elevated social good that could capture desire.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal capacity of desire to turn toward or away supplies the reversal from self-circulating renown toward Rabb.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal image of ownership and authority marks Rabb, rather than public reputation, as the governing endpoint.

## ease is companion not destination
- reading: While hardship and ease accompany one another, refuse to make either escape or relief the terminus; hold desire at Rabb through both.
- mechanism: The doubled construction keeps severity and opening in one repeated frame. Because the focus directs desire to Rabb, neither hardship as the thing to escape nor ease as desirable bounty becomes the terminus; both become the lived medium in which direction is maintained.
- trace:
  - 94:5 **ٱلْعُسْرِ** ع س ر B001: The literal image of difficulty and severity supplies the constricting condition within which orientation must remain live.
  - 94:5 **يُسْرًا** ي س ر B001: The literal opening and ease after difficulty supplies relief while keeping it within the hardship frame rather than making it the final endpoint.
  - 94:6 **ٱلْعُسْرِ** ع س ر B001: The repeated literal severity prevents the first assurance from simply deleting hardship from the mechanism.
  - 94:6 **يُسْرًا** ي س ر B001: The repeated literal opening makes ease a durable accompaniment and not a single prize after which direction can lapse.
  - 94:8 **فَٱرْغَب** ر غ ب B004: The literal image of abundant desirable bounty exposes how easily ease could become desire's object rather than its context.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal directional flexibility of desire allows the focus endpoint to displace both flight from hardship and fixation on ease.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal authority of Rabb supplies the stable endpoint while circumstances alternate or coexist.

## emptied vessel is refilled as orientation
- reading: Completion empties a vessel of attention, exertion sets it upright, and «فارغب» directs the newly open capacity toward Rabb before vacancy can scatter it.
- mechanism: The immediately preceding roots can image a vessel poured empty and something set upright. The focus's capacious desire then supplies a directed refill of attention: completion creates vacancy, disciplined exertion stabilizes it, and aspiration prevents the open capacity from diffusing.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B002: The literal pouring and emptying of a vessel supplies the newly vacant container of attention after completion.
  - 94:7 **فَٱنصَبْ** ن ص ب B001: The literal setting of something upright and prominent supplies stabilization and readiness for the emptied capacity.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: The literal toil that exhausts a person prevents the upright vessel model from becoming passive receptivity without disciplined effort.
  - 94:8 **فَٱرْغَب** ر غ ب B002: The literal broad hollow or capacious vessel supplies the interior volume that completion has opened.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal inclination toward an endpoint gives the open volume a vector and keeps vacancy from becoming dispersal.
  - 94:8 **رَبِّكَ** ر ب ب B002: The literal image of nurture and completion makes Rabb both the one who brings a phase to fullness and the destination of the capacity released afterward.

## aspiration runs through recurrent labor
- reading: Carry longing toward Rabb as the continuous axis through each cycle of completion, renewed intention, and strenuous work.
- mechanism: Vacancy after one occupation, renewed intention, and exhausting labor make a recurrent work-cycle. The Rabb branch of staying and the desire branch of direction move aspiration inside that cycle as its durable axis rather than reserving it for leisure after work.
- trace:
  - 94:7 **فَرَغْتَ** ف ر غ B001: The literal vacancy after occupation marks a transition point rather than permanent release from action.
  - 94:7 **فَرَغْتَ** ف ر غ B006: The literal intention toward a matter turns the vacant interval into renewed purposive engagement.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: The literal exhausting toil keeps the renewed engagement materially strenuous rather than merely contemplative.
  - 94:8 **رَبِّكَ** ر ب ب B007: The literal image of staying, clinging, lasting, and drawing near supplies continuity across successive episodes of work.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal directed inclination supplies the stable orientation carried through vacancy, intention, and toil.

## received acts become answering desire
- reading: The addressee's desire is an answering movement toward the Rabb already encountered as opener, unloader, raiser, and gradual completer.
- mechanism: Opening, putting down the burden, and raising the addressee's mention form a pattern of prior action upon the addressee. Read through Rabb as nurture and completion, the final imperative becomes reciprocal: desire answers a formative agency already experienced across the window.
- trace:
  - 94:1 **نَشْرَحْ** ش ر ح B001: The literal opening and clarification supplies the first formative act performed for the addressee.
  - 94:2 **وَوَضَعْنَا** و ض ع B001: The literal putting down into a lower or settled place supplies the formative act of unloading what had pressed on the addressee.
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: The literal raising of a thing supplies the complementary upward act that restores and elevates the addressee.
  - 94:8 **رَبِّكَ** ر ب ب B002: The literal image of repair, administration, nurture, and completion gathers the prior opening, unloading, and raising into a coherent Rabb-like agency.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal turn of desire toward something supplies the answering movement from the formed addressee back toward the formative Rabb.

## split rabb as rising breath
- reading: The opened, laboring body releases a rising breath of desire toward Rabb, so aspiration is somatically enacted as well as inwardly intended.
- mechanism: 
- trace:
  - 94:1 **صَدْرَكَ** ص د ر B001: The literal bodily chest supplies the organ through which an imagistic breath of aspiration can be enacted.
  - 94:7 **فَٱنصَبْ** ن ص ب B004: The literal exhausting toil supplies the bodily condition that produces labored or rising breath.
  - 94:8 **رَبِّكَ** ر ب ب B004: The literal image of panting or breath swelling upward supplies an embodied rising motion at the focus endpoint.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal directed inclination converts rising breath from a bodily symptom into a contained image of aspiration toward Rabb.

## erected object corrected by endpoint
- reading: Whatever form is erected or enacted in worship, desire must pass beyond the installed means and terminate at Rabb; the endpoint guards ritual orientation.
- mechanism: 
- trace:
  - 94:7 **فَٱنصَبْ** ن ص ب B002: The literal image of an erected stone for worship or slaughter raises the possibility that an installed ritual means could capture attention.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal toward-or-away vector of desire lets the final endpoint correct any fixation on the erected form.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal image of lordship and ownership identifies the authority beyond the installed ritual object at which desire must terminate.

## covenantal return of bestowed name
- reading: The raised name behaves like an entrusted deed within a pact, and directed desire becomes the addressee's return of fidelity rather than consumption of status.
- mechanism: 
- trace:
  - 94:4 **وَرَفَعْنَا** ر ف ع B001: The literal raising of a thing supplies the bestowed elevation whose use now calls for an answering relation.
  - 94:4 **ذِكْرَكَ** ذ ك ر B008: The literal deed or document of a right recasts elevated mention as something entrusted and answerable rather than merely enjoyed.
  - 94:8 **رَبِّكَ** ر ب ب B011: The literal covenant, pact, or protection agreement supplies a binding relational frame for «your Rabb».
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal turn of inclination supplies the addressee's active return-performance within the covenantal frame.

## ravenous appetite transmuted
- reading: Do not merely suppress appetite; transfer its full hunger toward Rabb, where its intensity is governed and its former objects are displaced.
- mechanism: 
- trace:
  - 94:8 **فَٱرْغَب** ر غ ب B003: The literal image of ravenous appetite or greed supplies an unsettling intensity and near-insatiability to the act of wanting.
  - 94:8 **فَٱرْغَب** ر غ ب B001: The literal capacity of desire to turn toward or away converts raw appetite into a redirectable force rather than endorsing its former objects.
  - 94:8 **رَبِّكَ** ر ب ب B001: The literal authority and ownership of Rabb disciplines the appetite's object and keeps intensity under governance.
