Surah: 109. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S109 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s109/surah.r2/text.md =====
# Surah 109

- 109:1 قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ
- 109:2 لَآ أَعْبُدُ مَا تَعْبُدُونَ
- 109:3 وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- 109:4 وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
- 109:5 وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
- 109:6 لَكُمْ دِينُكُمْ وَلِىَ دِينِ


===== _commentary/v16/work/s109/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272): 109:1 قُلْ

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

## ECHO ق ل ل (root_001251): for 109:1 قُلْ: withheld observed target; not identity

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

## ك ف ر (root_001307): 109:1 ٱلْكَٰفِرُونَ

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

## ع ب د (root_000973): 109:2 أَعْبُدُ, 109:2 تَعْبُدُونَ, 109:3 عَٰبِدُونَ, 109:3 أَعْبُدُ, 109:4 عَابِدٌ, 109:4 عَبَدتُّمْ, 109:5 عَٰبِدُونَ, 109:5 أَعْبُدُ

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

## د ي ن (root_000504): 109:6 دِينُكُمْ, 109:6 دِينِ

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)



===== _commentary/v16/work/s109/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s109/reader_a_pilot.md)

# s109 Semantic Channel Discovery

## Parent Channels

### 1. Sovereignty, Service, and Reversed Allegiance
- Semantic invariant: Authority becomes visible through rank, service, obedience, ownership, and the power to redirect another person's allegiance.
- Surface relation: indirect; 109:1 `قُلْ` opens an authoritative address, 109:2-5 repeatedly distinguish worship acts and worshippers, and 109:6 `دِينُكُمْ` / `دِينِ` assigns each side its religious relation.
- Surprising reach: The worship contrast expands into coronation, civic order, chattel status, bowed ceremony, and coerced disobedience.

#### Subchannel A. Crowned Voice and Honored Ruler
- Reading type: latent/lexical
- Scene or process: A titled ruler is crowned, speaks with social force, and receives honor and service.
- Active motifs: effective local ruler (`ق و ل:B004/m01`); titled woman (`ق و ل:B004/m02`); crown (`ك ف ر:B015/m01`); coronation (`ك ف ر:B015/m02`); honored or served superior (`ع ب د:B006/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: The ruler motif supplies the speaking office, coronation marks that office visibly, and the honored superior completes the hierarchy through received service. The feminine title preserves the same ranked social role with a different bearer.

#### Subchannel B. Bowed Service and Devotional Allegiance
- Reading type: mixed
- Scene or process: Worship is enacted as directed service, with bodily lowering expressing the worshipper's chosen allegiance.
- Active motifs: devotional worship (`ع ب د:B003/m01`); bowed salute with lowered head or hand to chest (`ك ف ر:B014/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: The repeated worship relation acquires a bodily counterpart in the bowed salute. Action and posture together form a scene of allegiance rather than a merely abstract profession.

#### Subchannel C. Chattel Hierarchy and Coerced Labor
- Reading type: latent/lexical
- Scene or process: Dominion reduces a person to owned status and compels work under humiliating control.
- Active motifs: chattel slave (`ع ب د:B001/m01`); saleable human property (`ع ب د:B001/m02`); making someone a slave (`ع ب د:B004/m01`); coercing slave-like labor (`ع ب د:B004/m02`); humiliating compulsion (`د ي ن:B004/m01`); dominion and ownership (`د ي ن:B004/m02`)
- Ayah anchors: 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Ownership supplies the legal relation, enslavement supplies the transition into that relation, and coerced labor supplies its lived operation. The scene turns the vocabulary of service into a complete hierarchy of possessor, possessed person, compulsion, and work.

#### Subchannel D. Civic Obedience and Betrayed Benefit
- Reading type: latent/lexical
- Scene or process: A settlement organizes obedience to rulers, while ingratitude breaks the reciprocal bond between received benefit and civic loyalty.
- Active motifs: city as the seat of rule (`د ي ن:B006/m01`); civic obedience to authority (`د ي ن:B006/m02`); concealment or denial of a benefit (`ك ف ر:B004/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: The city is defined by enacted obedience rather than buildings alone. Ingratitude reverses that organizing relation by receiving a benefit while withholding its acknowledgment, turning a moral failure into a breach of polity.

#### Subchannel E. Coerced Reversal of Allegiance
- Reading type: mixed
- Scene or process: An already obedient person is pressured away from devotion and into disobedience.
- Active motifs: obedient submission (`د ي ن:B001/m01`); submission to a worldly power (`ع ب د:B003/m02`); compelling the obedient to disobey (`ك ف ر:B007/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: The scene begins with an established relation of obedience. A rival power then acts on that relation, redirecting submission until obedience becomes rebellion and allegiance changes object.

### 2. Judgment, Trust, and Liability
- Semantic invariant: Claims and obligations pass through speech, entrusted judgment, reckoning, and acts that create or discharge liability.
- Surface relation: indirect; 109:1 `قُلْ` supplies the speech act, while 109:6 `دِينُكُمْ` / `دِينِ` opens the lexical movement from religious commitment to judgment, recompense, and obligation.
- Surprising reach: A fruit sheath figures the interval before judgment yields its outcome, while speed figures the rapid removal of an offense.

#### Subchannel A. Ruling Speech and Religious Attribution
- Reading type: latent/lexical
- Scene or process: A fluent speaker advances a ruling, testimony is credited, and an authoritative declaration assigns another person a religious status.
- Active motifs: eloquent or prolific speaker (`ق و ل:B003/m01`); arrogated judgment over another (`ق و ل:B010/m01`); crediting testimony in judgment or oath (`د ي ن:B007/m01`); declaring someone an unbeliever (`ك ف ر:B006/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Eloquence supplies the speaking participant, judicial credit supplies the procedure, and ruling speech produces an attributed status. The declaration therefore acts upon a person socially rather than merely describing an idea.

#### Subchannel B. Entrusted Conscience and Solicitous Stewardship
- Reading type: latent/lexical
- Scene or process: Responsibility is delegated to a person's conscience and carried out through sustained, sincere care.
- Active motifs: entrusting a person to conscience or religion (`د ي ن:B007/m02`); sincere care for a matter (`ق و ل:B015/m01`)
- Ayah anchors: 109:1 `قُلْ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Delegation transfers the decision inward, while solicitude governs how the entrusted person tends the matter. Together they form a fiduciary scene of trust, conscience, and responsible attention.

#### Subchannel C. Reckoning Ripening Inside an Enclosure
- Reading type: latent/lexical
- Scene or process: A case remains contained through reckoning until its recompense emerges, as fruit develops inside a sheath.
- Active motifs: judgment and reckoning (`د ي ن:B002/m01`); recompense or repayment (`د ي ن:B002/m02`); fruit sheath or calyx (`ك ف ر:B010/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: The sheath and the reckoning share a containing function: each holds a developing outcome before disclosure. Recompense corresponds to the fruit that finally emerges from the period of enclosure.

#### Subchannel D. Negotiated Debt Becoming Bondage
- Reading type: latent/lexical
- Scene or process: Negotiation creates a deferred financial obligation that can harden into the debtor's bonded status.
- Active motifs: negotiation over an affair (`ق و ل:B009/m01`); financial debt or loan (`د ي ن:B003/m01`); deferred transaction (`د ي ن:B003/m02`); debt-bound servant (`د ي ن:B004/m03`)
- Ayah anchors: 109:1 `قُلْ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Speech establishes the terms, deferment creates the outstanding claim, and unpaid liability transforms a financial relation into a social condition. The movement from agreement to bondage gives obligation a concrete human outcome.

#### Subchannel E. Swift Expiation and Discharged Offense
- Reading type: latent/lexical
- Scene or process: An offense is covered over through expiation without prolonged delay.
- Active motifs: expiation that covers an offense (`ك ف ر:B009/m01`); brief delay (`ع ب د:B009/m01`); swift motion (`ع ب د:B009/m02`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Expiation changes the standing of the offense by making it as though covered from the account. Brief delay and swift movement add a temporal mechanism: remediation follows the wrong without lingering.

### 3. Declaration, Belief, and Separation
- Semantic invariant: Speech makes commitments visible, distinguishes positions, and turns doctrinal difference into social boundaries, dispersal, and emotional consequence.
- Surface relation: direct; 109:1 `قُلْ` addresses `ٱلْكَٰفِرُونَ`, 109:2-5 oppose the two sides through repeated worship clauses, and 109:6 `دِينُكُمْ` / `دِينِ` states the final separation.
- Surprising reach: Spoken declaration extends into inner propositions, logical definition, nonverbal indication, circulating rumor, divergent roads, indignation, and regret.

#### Subchannel A. Public Declaration of Distinct Worship
- Reading type: surface-primary
- Scene or process: An articulated address names its audience, repeatedly distinguishes the two worship relations, and closes by assigning each side its religion.
- Active motifs: articulated speech (`ق و ل:B001/m01`); tongue as the instrument of speech (`ق و ل:B002/m01`); denial of truth or unbelief (`ك ف ر:B003/m01`); devotional worship (`ع ب د:B003/m01`); religion or religious way (`د ي ن:B001/m02`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Speech and tongue provide the act and instrument of declaration. The named audience, reciprocal worship clauses, and final allocation of religion convert doctrinal difference into an explicit relation between two communities.

#### Subchannel B. Inner, Conjectural, and Doctrinal Saying
- Reading type: latent/lexical
- Scene or process: A proposition begins inwardly, can be framed as conjecture, and can settle into a declared doctrinal position.
- Active motifs: unspoken inner proposition (`ق و ل:B012/m01`); statement functioning as conjecture (`ق و ل:B011/m01`); doctrinal belief or school (`ق و ل:B013/m01`)
- Ayah anchors: 109:1 `قُلْ`
- Synthesis: The three senses trace a semantic transformation within saying: thought exists before utterance, receives a modal status as conjecture, and becomes a durable position when adopted as doctrine.

#### Subchannel C. Fabricated Speech as Concealed Ingratitude
- Reading type: latent/lexical
- Scene or process: A speaker invents or falsely attributes words in order to deny an acknowledged benefit.
- Active motifs: fabricated speech (`ق و ل:B005/m01`); false attribution to a speaker (`ق و ل:B005/m02`); ingratitude that conceals a benefit (`ك ف ر:B004/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`
- Synthesis: Fabrication supplies the false utterance, false attribution shifts responsibility for it, and ingratitude supplies the object being obscured. The result is denial performed through manipulated speech.

#### Subchannel D. Definition, Indication, and Disavowal Boundaries
- Reading type: latent/lexical
- Scene or process: Signs and definitions mark a conceptual limit, and disavowal turns that limit into a social separation.
- Active motifs: a thing indicating its own state (`ق و ل:B014/m01`); logical definition (`ق و ل:B016/m01`); disavowal or severed association (`ك ف ر:B005/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`
- Synthesis: Indication allows a thing to communicate without ordinary speech, while definition fixes what belongs inside a category. Disavowal applies the same boundary-making operation to affiliation, stating what and whom one no longer shares.

#### Subchannel E. Circulating Talk and Factional Dispersal
- Reading type: mixed
- Scene or process: Doctrinal talk circulates among people as communities and their paths separate in multiple directions.
- Active motifs: circulating public talk (`ق و ل:B007/m01`); scattered groups (`ع ب د:B010/m01`); divergent roads (`ع ب د:B010/m02`); denial of truth or unbelief (`ك ف ر:B003/m01`); religion or religious way (`د ي ن:B001/m02`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Circulating discourse carries the difference through the social field. Scattered groups and diverging roads give that difference a spatial form, with each community proceeding along its own religious course.

#### Subchannel F. Doctrinal Naming, Indignation, and Regret
- Reading type: latent/lexical
- Scene or process: A doctrinal attribution provokes zeal or anger and can end in grief or regret when affiliation is lost.
- Active motifs: doctrinal position (`ق و ل:B013/m01`); declaring someone an unbeliever (`ك ف ر:B006/m01`); pride, zeal, or anger (`ع ب د:B008/m01`); grief or regret at loss (`ع ب د:B008/m02`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Naming a doctrinal position alters social standing and triggers protective zeal. When the boundary produces separation or loss, the same emotional field turns from indignation toward sorrow and regret.

### 4. Covering, Containment, and Transformation
- Semantic invariant: A covering can hide, contain, protect, cultivate, or isolate according to what lies beneath it and what outcome the enclosure serves.
- Surface relation: indirect; 109:1 `ٱلْكَٰفِرُونَ` carries the concealment sense into the address, while 109:1 `قُلْ` and 109:6 `دِينُكُمْ` / `دِينِ` connect enclosure to inward thought and customary action.
- Surprising reach: The same operation spans cloth over armor, cloud over sun, engulfing darkness or water, fruit calyx, buried seed, grave, mountain pass, and wall.

#### Subchannel A. Obscuring Layers and Engulfing Media
- Reading type: latent/lexical
- Scene or process: A layer or surrounding medium removes an object, light source, or horizon from view.
- Active motifs: physical covering (`ك ف ر:B001/m01`); celestial obscuration (`ك ف ر:B001/m02`); enveloping darkness (`ك ف ر:B002/m01`); vast sea or river (`ك ف ر:B002/m02`); sunset or disappearance (`ك ف ر:B002/m03`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`
- Synthesis: Cloth, cloud, darkness, and vast water differ in material but share the same spatial operation: the surrounding layer exceeds the visible object and hides it. Sunset supplies the resulting disappearance at the horizon.

#### Subchannel B. Thought Held Like Fruit in Its Sheath
- Reading type: latent/lexical
- Scene or process: An inward proposition remains unexpressed as a developing fruit remains enclosed by its calyx.
- Active motifs: unspoken inner proposition (`ق و ل:B012/m01`); fruit sheath or calyx (`ك ف ر:B010/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`
- Synthesis: The calyx provides a concrete container and the inward proposition provides concealed content. Both scenes preserve something formed but not yet exposed, making disclosure analogous to fruit emerging from its sheath.

#### Subchannel C. Covered Seed and Customary Cultivation
- Reading type: latent/lexical
- Scene or process: A cultivator repeatedly places seed beneath soil so concealment initiates growth rather than erasure.
- Active motifs: farmer covering seed with earth (`ك ف ر:B008/m01`); customary or habitual practice (`د ي ن:B005/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:6 `دِينُكُمْ` / `دِينِ`
- Synthesis: Covering is the operative step of sowing, and customary practice turns that step into a recurring cycle. What disappears beneath the soil is being prepared for later emergence.

#### Subchannel D. Remote Places Behind Terrain and Walls
- Reading type: latent/lexical
- Scene or process: Distance and physical enclosure separate a settlement, grave, or passage from ordinary human access.
- Active motifs: remote tract (`ك ف ر:B012/m01`); isolated village (`ك ف ر:B012/m02`); grave (`ك ف ر:B012/m03`); mountain mass (`ك ف ر:B013/m02`); low boundary wall (`ك ف ر:B013/m03`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`
- Synthesis: Remoteness supplies social separation, while mountain and wall supply physical screening. The village and grave become two forms of set-apart place, one inhabited and one funerary.

### 5. Routes, Carriers, and Interrupted Circulation
- Semantic invariant: Movement depends on prepared surfaces and carriers, then branches or stops when the route, vehicle, animal, or bearer changes state.
- Surface relation: none
- Surprising reach: Paved roads and pitch-coated vessels extend into resistant mounts, failed journeys, circulating rumor, and speech drawn into private possession.

#### Subchannel A. Prepared Road Through a Sheltered Pass
- Reading type: latent/lexical
- Scene or process: A leveled, traveled road makes a concealed mountain passage usable.
- Active motifs: paved or trodden road (`ع ب د:B005/m01`); sheltered mountain pass (`ك ف ر:B013/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: The pass supplies difficult terrain and the prepared road supplies the human intervention that makes traversal regular. Concealment and leveling therefore cooperate in a single route scene.

#### Subchannel B. Pitch-Coated Vessel in Engulfing Waters
- Reading type: latent/lexical
- Scene or process: A vessel is sealed with pitch so it can move through a vast sea or river.
- Active motifs: pitch-coated vessel (`ع ب د:B005/m03`); vast sea or river (`ك ف ر:B002/m02`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Pitching prepares the hull as a water-resistant carrier, while the sea or great river supplies the engulfing setting. The material treatment is functional: it enables passage through the medium that surrounds the vessel.

#### Subchannel C. Prepared but Resistant Mount
- Reading type: latent/lexical
- Scene or process: A treated mount is readied for travel and speed but can resist handling and refuse the route.
- Active motifs: tar-treated camel (`ع ب د:B005/m02`); swift running (`ع ب د:B009/m02`); resistant or difficult camel (`ع ب د:B011/m02`)
- Ayah anchors: 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Treatment and speed describe the intended readiness of the carrier; resistance reverses that readiness at the level of agency. The mount can be materially prepared without becoming behaviorally compliant.

#### Subchannel D. Speech in Transit and Carrier Breakdown
- Reading type: latent/lexical
- Scene or process: Talk circulates between people, may be pulled into one speaker's possession, and stops when its carrier fails in a remote place.
- Active motifs: circulating public talk (`ق و ل:B007/m01`); appropriating a saying to oneself (`ق و ل:B006/m01`); journey broken by an exhausted or lost mount (`ع ب د:B011/m01`); remote tract (`ك ف ر:B012/m01`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Public talk behaves like material in transit: it moves through a network and can be diverted into private ownership. The exhausted carrier and remote setting then supply a concrete mechanism for interrupted circulation.

## Standalone Subchannels

### S1. Camphor and the Perfume Brazier
- Reading type: latent/lexical
- Scene or process: Aromatic material from the camphor plant is prepared and released through a perfume brazier.
- Active motifs: camphor fragrance (`ك ف ر:B011/m01`); camphor plant (`ك ف ر:B011/m03`); perfume brazier (`ع ب د:B012/m01`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`; 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: The plant supplies the aromatic substance and the brazier supplies the tool that heats or presents it. Together they form a compact scene of material, instrument, and released scent.

### S2. Camphor-Named Spring
- Reading type: latent/lexical
- Scene or process: A spring in the garden is identified through the camphor name.
- Active motifs: camphor-named spring (`ك ف ر:B011/m02`)
- Ayah anchors: 109:1 `ٱلْكَٰفِرُونَ`
- Synthesis: This sense shifts camphor from aromatic substance to a named water source, producing a distinct landscape scene rather than a perfumery scene.

### S3. Conjecture About a Remote Settlement
- Reading type: latent/lexical
- Scene or process: A speaker forms a supposition concerning an absent or isolated village.
- Active motifs: statement functioning as conjecture (`ق و ل:B011/m01`); isolated village (`ك ف ر:B012/m02`)
- Ayah anchors: 109:1 `قُلْ` / `ٱلْكَٰفِرُونَ`
- Synthesis: Conjectural speech supplies the uncertain cognitive act, while the remote settlement supplies an object beyond immediate inspection. Distance explains why the proposition remains supposition rather than direct report.

### S4. Solidity Across Body and Material
- Reading type: latent/lexical
- Scene or process: One quality of force and durability appears as animal vitality and as the lasting strength of cloth.
- Active motifs: force, hardness, and durability (`ع ب د:B007/m01`); robust camel (`ع ب د:B007/m02`); strong cloth (`ع ب د:B007/m03`)
- Ayah anchors: 109:2 `أَعْبُدُ` / `تَعْبُدُونَ`; 109:3 `عَٰبِدُونَ` / `أَعْبُدُ`; 109:4 `عَابِدٌ` / `عَبَدتُّمْ`; 109:5 `عَٰبِدُونَ` / `أَعْبُدُ`
- Synthesis: Bodily robustness and textile durability share resistance to weakness, wear, or collapse. The channel is a cross-entity analogy of sustained material strength.

### S5. Ball-Striking Implement
- Reading type: latent/lexical
- Scene or process: A shaped stick serves as the tool for striking a ball in play.
- Active motifs: ball-striking stick (`ق و ل:B008/m01`)
- Ayah anchors: 109:1 `قُلْ`
- Synthesis: The motif forms a complete tool-action-object scene: the implement is defined by the impact it delivers to the ball.


