Surah: 112. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S112 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s112/surah.r2/text.md =====
# Surah 112

- 112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 112:2 ٱللَّهُ ٱلصَّمَدُ
- 112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
- 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ


===== _commentary/v16/work/s112/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272): 112:1 قُلْ

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

## ECHO ق ل ل (root_001251): for 112:1 قُلْ: withheld observed target; not identity

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

## ء ل ه (root_000047): 112:1 ٱللَّهُ, 112:2 ٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 112:1 ٱللَّهُ, 112:2 ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ء ح د (root_000017): 112:1 أَحَدٌ, 112:4 أَحَدٌۢ

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

## ص م د (root_000882): 112:2 ٱلصَّمَدُ

- **B001** dayanak alarak bir hedefe yönelme — amaç edinme ve dayanarak yönelme · onu amaçlayıp ona dayanarak yöneldi · işlerde kendisine başvurulan en üstün kişi · işlerde kendisine yönelinen kişi veya amaçlanan şey · amaçlanıp gidilen ev · kulların dua ve istekle yöneldiği yüce varlığın adı
  الصمد القصد وصمدته صمدا (maqayis); وصمدت قصدت وصمدت صمد كذا أي قصدت قصده واعتمدته (ayn); صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود (sihah); الصمد السيد الذي قد انتهى سؤدده والذي يصمد إليه الأمر وصمدت صمد هذا الأمر أي قصدت قصده واعتمدته (tahdhib); الصمد السيد الذي يصمد إليه في الأمر وصمده قصد معتمدا عليه قصده (mufradat)
- **B002** içi boş olmayan katı bütünlük — sert veya yüksek ve kalın yer · içi boş ve yüzeyi yarık olmayan katı şey · içi boş olmayan · yere sağlam oturmuş düz kaya · dağın kalın bölümünden alçalıp düzleşen ağaçlı arazi
  الصلابة في الشيء والصمد كل مكان صلب (maqayis); المصمت الذي ليس بأجوف والصمدة صخرة راسية (ayn); الصمد المكان المرتفع الغليظ والمصمد لغة في المصمت وهو الذي لا جوف له (sihah); المصمت الذي لا جوف له والمكان المرتفع الغليظ والمصمد الصلب الذي ليس فيه خدد والشديد من الأرض (tahdhib); الصمد الذي ليس بأجوف (mufradat)
- **B003** şişe ağzı tıkacı — şişe ağzı tıkacı · şişeye tıkaç takıp ağzını kapatmak
  الصماد عفاص القارورة وصمدتها صمدا (ayn); الصماد عفاص القارورة (sihah); الصماد سداد القارورة والصماد عفاص القارورة وقد صمدتها أصمدها (tahdhib)
- **B004** başı sarık dışındaki bezle sarma — başını sarık dışındaki bir bezle sardı · sarık olmayan bez baş sargısı
  صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو منديل أو ثوب ما خلا العمامة وهي الصماد (tahdhib)
- **B005** bir işin başında durup ona özen gösterme — bir işin başında durup ona özen gösteren
  إني على صمادة من أمر إذا أشرف عليه وحفلت به (tahdhib)
- **B006** değnekle vurma [kalıp] — ona değnekle vurdu
  صمده بالعصا صمدا إذا ضربه بها (tahdhib)
- **B007** kalıcı ve sürekli olma — sürekli ve yok oluştan sonra da kalan · soğuk ve kıtlıkta dayanıp sütü kesilmeyen dişi deve
  الصمد الدائم والدائم الباقي بعد فناء خلقه وناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل (tahdhib)

## و ل د (root_001683): 112:3 يَلِدْ, 112:3 يُولَدْ

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

## ك و ن (root_001332): 112:4 يَكُن

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

## ك ف ء (root_001305): 112:4 كُفُوًا

- **B001** denk olma ve aynı ölçüde karşılık verme — konum, soy, mal veya savaş gücü bakımından denk ve eş · denk, eş, aynı düzeyde olan · özellikle evlilikte düzey ve durum uygunluğu, denklik · denk ya da karşı koyabilecek güç · bir davranışa veya iyiliğe dengiyle karşılık verme · eşitlik ve karşılıklı denklik · kan bedeli ve karşılık cezası bakımından eşit sayılmak · değer ve yaş bakımından birbirine eşit iki koyun · mızrakla iki atlıya birbiri ardınca yönelmek · güneşin karşısına gölge sağlayan bir siper koymak
  الكفء المثل (maqayis)؛ التكافؤ التساوي (maqayis)؛ هذا كفء له أي مثله في الحسب والمال والحرب (ayn)؛ المكافأة مجازاة النعم (ayn)؛ الكفئ النظير (sihah)؛ كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له (sihah;tahdhib)؛ كافأت الرجل أي فعلت به مثل ما فعل بي (tahdhib)؛ فلان كفء لفلان في المناكحة أو في المحاربة (mufradat)؛ نكافىء بهما عنا عين الشمس (tahdhib)؛ كافأ الرجل بين فارسين برمحه (tahdhib)
- **B002** eğmek, ters çevirmek veya yönünden döndürmek — kabı baş aşağı çevirip içindekini dökmek · bir şeyi düz konumundan eğmek · yayın ucunu eğip onu atış için dik tutmamak · tabağı kendine doğru eğerek içindekini dökmek · bir topluluğu gitmek istediği yönden başka yöne çevirmek · yürürken sağa sola sallanmak · yüzü düşmüş ve rengi solmuş olmak · rengi değişmiş olmak · geri dönmek veya bozguna uğrayıp çekilmek
  أكفأت الشيء إذا أملته (maqayis;tahdhib)؛ كفأت القصعة والإناء (ayn)؛ كفأت الإناء إذا كببته (sihah;tahdhib)؛ كفأت القوم إذا صرفتهم إلى غيره (sihah;tahdhib)؛ تكفأت المرأة في مشيتها (sihah)؛ تكفأ تكفؤا (tahdhib)؛ مكفأ الوجه كاسف اللون (ayn;tahdhib)؛ الإكفاء قلب الشيء كأنه إزالة المساواة (mufradat)
- **B003** şiirde dize sonu uyumsuzluğu — şiirde dize sonlarının harf, ses veya çekim bakımından uyuşmaması
  الإكفاء في الشعر (maqayis;ayn;sihah;tahdhib;mufradat)؛ أن ترفع قافية وتخفض أخرى (maqayis)؛ الاختلاط في القوافي (ayn)؛ يخالف بين قوافيه بعضها ميم وبعضها نون (sihah)؛ اختلاف إعراب القوافي (tahdhib)
- **B004** çadırın arkasına dikilen kumaş örtü — bir veya iki parçadan dikilip çadırın arkasına konan kumaş örtü · çadıra arka örtü hazırlayıp yerleştirmek
  الكفاء شقتان تنصح إحداهما بالأخرى (maqayis)؛ الكفاء شقة أو ثنتان ينصح إحداهما بالأخرى (ayn)؛ الكفاء بالكسر والمد شقة أو شقتان (sihah)؛ أكفأت البيت فهو مكفأ إذا عملت له كفاء (tahdhib)؛ الكفاء لشقة تنصح بالأخرى فيجلل بها مؤخر البيت (mufradat)
- **B005** bir yıllık ürün, yavru ve hayvansal yarar payı — hurmanın bir yıllık ürünü veya develerin bir yıllık yavru, süt ve yün yararı · develerin bir yıllık yavru ve diğer yararlarını sahibinden istemek · bir hurma ağacının bir yıllık ürününü istemek · develerin süt, yün veya yavrularını bir yıllığına birine vermek · deve sürüsünü yıllara göre dönüşümlü yavrulayan iki gruba ayırmak
  الكفأة وهي حمل النخلة سنتها (maqayis)؛ يقال ذلك في نتاج الإبل أيضا (maqayis)؛ سألته نتاج إبله سنة (maqayis;ayn;tahdhib)؛ الكفأة من الإبل نتاج سنة (ayn)؛ أكفأت إبلي كفأتين (sihah;tahdhib)؛ أعطاني لبنها ووبرها وأولادها سنة (sihah)؛ سألته ثمرها سنة (tahdhib)؛ يقال لنتاج الإبل ليست تامة كفأة (mufradat)



===== _commentary/v16/work/s112/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s112/reader_a_pilot.md)

# S112 Semantic Channel Discovery

## Parent Channels

### 1. Singular Identity and Relational Comparison
- Semantic invariant: An entity is located as absolutely one, universally unmatched, relatively equal, or operationally separate.
- Surface relation: direct; 112:1 `أحد` states singularity, while 112:4 `كفوا أحد` excludes any counterpart.
- Surprising reach: The comparison field extends into marital and martial fitness, reciprocal recompense, and solitary procession.

#### Subchannel A. Absolute Oneness and Exhaustive Exclusion
- Reading type: surface-primary
- Scene or process: Positive singular identity is paired with negative quantification over every possible member of a class.
- Active motifs: absolute unity `ء ح د:B001/m01`; emphatic repeated one `ء ح د:B001/m02`; exhaustive negative “any one” `ء ح د:B002/m01`
- Ayah anchors: 112:1 `أحد`; 112:4 `أحد`
- Synthesis: The positive use fixes an identity as one without qualification, and emphatic repetition intensifies that unity. In a negative frame, the same lexical field expands from one individual to anyone whatsoever, making singularity and exhaustive exclusion complementary operations.

#### Subchannel B. Counterpart, Fitness, and Recompense
- Reading type: mixed
- Scene or process: Two parties are tested for parity, then aligned through fitness, opposition, or an equivalent return.
- Active motifs: equal counterpart `ك ف ء:B001/m01`; marital or martial fitness `ك ف ء:B001/m02`; recompense in kind `ك ف ء:B001/m03`; paired correspondence `ك ف ء:B001/m04`
- Ayah anchors: 112:4 `كفوا`
- Synthesis: Counterpart relation becomes a mechanism of comparison: parties may be equal, suitably matched, opposed on equal terms, or answered with like for like. The surface denial of a counterpart therefore opens onto a wider lexical system of parity and reciprocal balance.

#### Subchannel C. Acting and Arriving Singly
- Reading type: latent/lexical
- Scene or process: A collective resolves into independent actors or a sequence of isolated arrivals.
- Active motifs: acting alone `ء ح د:B005/m01`; arriving one by one `ء ح د:B005/m02`
- Ayah anchors: 112:1 `أحد`; 112:4 `أحد`
- Synthesis: Singularity becomes an enacted social arrangement rather than only an attribute: participants separate, act independently, and appear as successive individuals.

### 2. Origination and Lineage
- Semantic invariant: A source gives rise to an outcome through biological birth, causal production, or derivation.
- Surface relation: direct; 112:3 `يلد` and `يولد` activate both directions of the birth relation.
- Surprising reach: Biological descent extends into coined speech, derived language, mixed provenance, and the general coming-to-be of events.

#### Subchannel A. Parents, Parturition, and Offspring
- Reading type: surface-primary
- Scene or process: Parent roles, the act and timing of birth, and the resulting child form one generational scene.
- Active motifs: offspring or descendant `و ل د:B001/m01`; father `و ل د:B002/m01`; mother `و ل د:B002/m02`; parental pair `و ل د:B002/m03`; human parturition `و ل د:B003/m01`; impending birth `و ل د:B003/m02`; newborn child `و ل د:B004/m01`; birth-age term extended to a young female slave `و ل د:B004/m02`
- Ayah anchors: 112:3 `يلد`, `يولد`
- Synthesis: The two surface verbs evoke a complete generational frame even while negating it: progenitors, delivery, its temporal threshold, and offspring. The newborn designation also reaches into household status through its use for a young female slave, carrying an age-marked term beyond the biological event.

#### Subchannel B. Causal Products and Coming-to-be
- Reading type: latent/lexical
- Scene or process: Something arises from a source, enters occurrence, and may bear the marks of innovation or mixed provenance.
- Active motifs: causal generation `و ل د:B005/m01`; coined speech `و ل د:B005/m02`; derived or locally formed provenance `و ل د:B005/m03`; occurrence and presence `ك و ن:B001/m01`; temporal coming-to-be `ك و ن:B001/m02`
- Ayah anchors: 112:3 `يلد`, `يولد`; 112:4 `يكن`
- Synthesis: Birth is generalized into source-to-result causation. A thing may be produced by another, a saying may be newly coined, and a person or language may emerge in a mixed or local form; the existence root supplies the outcome as an event that has come to be.

### 3. Number, Order, and Temporal Position
- Semantic invariant: Discrete units are counted, ordered, distributed, compared by age, or arranged in recurring time.
- Surface relation: direct; 112:1 and 112:4 anchor `أحد`, while 112:3 `يلد` and 112:4 `كفوا` supply indirect temporal extensions.
- Surprising reach: The one-unit field reaches eleven, Sunday, one-by-one arrival, remembered youth, and alternating annual herd production.

#### Subchannel A. Cardinal Composition and Calendar Order
- Reading type: mixed
- Scene or process: A single unit enters arithmetic composition, ordinal position, and calendrical naming.
- Active motifs: cardinal one `ء ح د:B003/m01`; compound eleven `ء ح د:B003/m02`; first in a construct `ء ح د:B004/m01`; Sunday as the named day `ء ح د:B004/m02`
- Ayah anchors: 112:1 `أحد`; 112:4 `أحد`
- Synthesis: The unit “one” can be counted, combined with ten, or recast as first. Its ordinal force also names Sunday, linking numerical structure to the recurring order of the week.

#### Subchannel B. One-by-one Distribution
- Reading type: latent/lexical
- Scene or process: Members of a group are serialized as separate arrivals.
- Active motifs: successive individual arrival `ء ح د:B005/m02`
- Ayah anchors: 112:1 `أحد`; 112:4 `أحد`
- Synthesis: Number becomes distributive motion: the group is not merely counted but presented as a sequence of single persons, each occupying a distinct turn.

#### Subchannel C. Coevality and Remembered Youth
- Reading type: latent/lexical
- Scene or process: People are positioned in time either as age-peers or through an elder’s contrast between present age and former youth.
- Active motifs: coeval or age-peer `و ل د:B006/m01`; elder defined by “I was in my youth” `ك و ن:B005/m01`
- Ayah anchors: 112:3 `يلد`, `يولد`; 112:4 `يكن`
- Synthesis: One relation synchronizes two lives at the same age, while the other folds a single life across past and present. Together they form a temporal comparison scene of co-presence and retrospection.

#### Subchannel D. Annual Birth and Alternating Yield
- Reading type: latent/lexical
- Scene or process: Animal birth and agricultural or pastoral products are organized into yearly, alternating production cycles.
- Active motifs: animal parturition `و ل د:B003/m03`; annual crop or camel yield `ك ف ء:B005/m01`; yearly milk, wool, and offspring return `ك ف ء:B005/m02`; alternating camel birth cohorts `ك ف ء:B005/m03`
- Ayah anchors: 112:3 `يلد`, `يولد`; 112:4 `كفوا`
- Synthesis: Reproduction becomes scheduled yield. Births, fruit, milk, wool, and offspring are reckoned by year, while dividing camels into two cohorts turns recurrence into an alternating management system.

### 4. Orientation, Authority, and Care
- Semantic invariant: Participants direct worship, need, allegiance, responsibility, or concern toward an asymmetrically positioned figure.
- Surface relation: direct; 112:1-2 `الله` identifies the addressed and worshipped figure, and 112:2 `الصمد` names the one sought and relied upon.
- Surprising reach: Devotional orientation expands into civic rank, sponsorship, negotiation, doctrinal submission, and solicitude under adversity.

#### Subchannel A. Worship and the Invoked Divine Name
- Reading type: mixed
- Scene or process: A worshipper directs devotion toward one made the object of worship and addresses the divine name in oath or invocation.
- Active motifs: devotional worship `ء ل ه:B001/m01`; worshipped entity `ء ل ه:B001/m02`; making an object worshipped `ء ل ه:B001/m03`; divine name `ء ل ه:B002/m01`; oath formula `ء ل ه:B002/m02`; vocative invocation `ء ل ه:B002/m03`
- Ayah anchors: 112:1 `الله`; 112:2 `الله`
- Synthesis: The divine name occupies both relational poles: it identifies the worshipped object and provides the form by which a speaker swears or calls. The lexical field also exposes the social act that constitutes something as an object of worship.

#### Subchannel B. Sought Patron and Directed Reliance
- Reading type: surface-primary
- Scene or process: A person deliberately turns toward a dependable patron for affairs and needs.
- Active motifs: aiming toward and relying upon `ص م د:B001/m01`; lord or patron sought for needs `ص م د:B001/m02`
- Ayah anchors: 112:2 `الصمد`
- Synthesis: Direction and dependence form one action: the seeker chooses a destination because the figure approached is the one on whom affairs and needs can rest.

#### Subchannel C. Responsible Authority and Negotiation
- Reading type: latent/lexical
- Scene or process: A ranked authority gives operative speech, sponsors a dependent, oversees an affair, and negotiates its disposition.
- Active motifs: chieftain whose word carries force `ق و ل:B004/m01`; rank or standing `ك و ن:B002/m02`; establishment in position `ك و ن:B002/m03`; sponsorship and guarantee `ك و ن:B003/m01`; oversight of an affair `ص م د:B005/m01`; attentive concern for it `ص م د:B005/m02`; negotiation `ق و ل:B009/m01`
- Ayah anchors: 112:1 `قل`; 112:2 `الصمد`; 112:4 `يكن`
- Synthesis: Rank is converted into responsibility. The authoritative speaker can negotiate an affair, stand over it attentively, and guarantee another person, joining verbal force to institutional care.

#### Subchannel D. Solicitude in Adversity
- Reading type: latent/lexical
- Scene or process: Sincere concern is directed toward someone or something in a bad condition.
- Active motifs: sincere care `ق و ل:B015/m01`; adverse condition `ك و ن:B006/m01`
- Ayah anchors: 112:1 `قل`; 112:4 `يكن`
- Synthesis: The speech root shifts from utterance to committed concern, while the existence root supplies the distressed state that calls forth that concern. Care is defined here by sustained attention to adversity.

#### Subchannel E. Doctrine and Submission
- Reading type: latent/lexical
- Scene or process: A person adopts a doctrinal position and embodies allegiance through submission.
- Active motifs: belief or school affiliation `ق و ل:B013/m01`; submissive posture `ك و ن:B004/m01`
- Ayah anchors: 112:1 `قل`; 112:4 `يكن`
- Synthesis: A “saying” becomes a held doctrine rather than a spoken sentence, and the adopted position becomes a social posture of yielding to what one follows.

### 5. Speech, Thought, and Semantic Form
- Semantic invariant: Meaning moves among vocal delivery, inward conception, source attribution, public circulation, and formal predication.
- Surface relation: direct; 112:1 `قل` initiates vocal declaration, while 112:4 `يكن` supplies a predicative frame.
- Surprising reach: Saying extends to the tongue as instrument, silent thought, rumor, false attribution, nonverbal signs, and logical definition.

#### Subchannel A. Vocal Delivery and Speaker Capacity
- Reading type: surface-primary
- Scene or process: A speaker externalizes language through the tongue, with fluency or abundance characterizing the speaker.
- Active motifs: vocalized saying `ق و ل:B001/m01`; tongue as speech instrument `ق و ل:B002/m01`; fluent or loquacious speaker `ق و ل:B003/m01`
- Ayah anchors: 112:1 `قل`
- Synthesis: Thought becomes audible through a bodily instrument, and repeated facility in that act becomes a stable quality of the person who speaks.

#### Subchannel B. Inner Proposition and Supposition
- Reading type: latent/lexical
- Scene or process: A proposition remains inward or operates as a supposition before any public utterance.
- Active motifs: unexpressed inner speech `ق و ل:B012/m01`; proposition functioning as supposition `ق و ل:B011/m01`
- Ayah anchors: 112:1 `قل`
- Synthesis: Saying is detached from sound and retained as mental content. That content can then function as a judgment or hypothesis, especially in questioning, without first becoming voiced speech.

#### Subchannel C. Speech Ownership, Falsification, and Circulation
- Reading type: latent/lexical
- Scene or process: A statement is fabricated, assigned to a speaker, appropriated by another, and released into public circulation.
- Active motifs: fabricated falsehood `ق و ل:B005/m01`; attribution of unsaid words `ق و ل:B005/m02`; appropriation of a saying to oneself `ق و ل:B006/m01`; circulating report or reputation `ق و ل:B007/m01`; recurring gossip `ق و ل:B007/m02`
- Ayah anchors: 112:1 `قل`
- Synthesis: The scene tracks a proposition through contested ownership. It may be invented, imposed on someone who did not say it, drawn toward oneself, and finally dispersed among people as favorable or unfavorable report.

#### Subchannel D. Signification, Definition, and Predication
- Reading type: mixed
- Scene or process: Content is made knowable through a thing’s indication, a logical boundary, or a predicative construction.
- Active motifs: nonverbal indication `ق و ل:B014/m01`; logical definition or limit `ق و ل:B016/m01`; copular, emphatic, or exceptive predication `ك و ن:B001/m03`
- Ayah anchors: 112:1 `قل`; 112:4 `يكن`
- Synthesis: “Saying” can be performed by a thing that signifies without speech or by a definition that fixes conceptual limits. The predicative use of being supplies the grammatical operation that asserts, emphasizes, or excludes within a proposition.

### 6. Material Solidity, Closure, and Shelter
- Semantic invariant: A space, container, body, or dwelling is stabilized by dense matter or a fitted closure.
- Surface relation: indirect; 112:2 `الصمد`, 112:4 `يكن` and `كفوا`, and 112:1/4 `أحد` provide the lexical anchors for the concrete constructions.
- Surprising reach: The material field spans cavityless rock, Mount Uhud, a bottle stopper, a bound head, and sewn tent panels.

#### Subchannel A. Cavityless Solidity and Anchored Terrain
- Reading type: latent/lexical
- Scene or process: Dense, cavityless matter forms hard ground, fixed rock, and elevated terrain located in a definite place.
- Active motifs: compact solidity without a cavity `ص م د:B002/m01`; hard or elevated place `ص م د:B002/m02`; anchored rock and severe ground `ص م د:B002/m03`; place or location `ك و ن:B002/m01`; Mount Uhud `ء ح د:B006/m01`
- Ayah anchors: 112:1 `أحد`; 112:2 `الصمد`; 112:4 `يكن`, `أحد`
- Synthesis: Solidity scales from material texture to landscape. Dense matter becomes hard ground and fixed rock, location gives it spatial placement, and Mount Uhud supplies the fully named elevated setting.

#### Subchannel B. Stoppered Vessel
- Reading type: latent/lexical
- Scene or process: A fitted plug closes and secures the mouth of a bottle.
- Active motifs: bottle stopper `ص م د:B003/m01`; act of stoppering `ص م د:B003/m02`
- Ayah anchors: 112:2 `الصمد`
- Synthesis: The object and operation form a compact containment mechanism: a closure is made for the vessel and then set in place to seal it.

#### Subchannel C. Fabric Closures for Body and Dwelling
- Reading type: latent/lexical
- Scene or process: Cloth is fitted and fastened to stabilize the head or close the rear of a shelter.
- Active motifs: binding the head with cloth `ص م د:B004/m01`; sewn rear tent panels `ك ف ء:B004/m01`
- Ayah anchors: 112:2 `الصمد`; 112:4 `كفوا`
- Synthesis: The same functional pattern operates at two scales. A cloth secures the body, while one or two sewn panels close and shape the back of a tent or dwelling.

### 7. Applied Force and Response
- Semantic invariant: External pressure produces impact, redirection, visible yielding, or sustained resistance.
- Surface relation: indirect; 112:1 `قل`, 112:2 `الصمد`, and 112:4 `كفوا` and `أحد` anchor the latent tool, action, motion, and setting senses.
- Surprising reach: A game stick and a staff blow join Mount Uhud, redirected travelers, swaying vessels, a changed face, and a drought-enduring milk camel.

#### Subchannel A. Striking and Redirection
- Reading type: latent/lexical
- Scene or process: Applied force strikes a target or changes the orientation and course of an object or group.
- Active motifs: staff blow `ص م د:B006/m01`; game stick used to strike `ق و ل:B008/m01`; tilting, inversion, or upending `ك ف ء:B002/m01`; tilting a bow or dish `ك ف ء:B002/m02`; diverting a group `ك ف ء:B002/m03`; swaying motion `ك ف ء:B002/m04`; Mount Uhud as setting `ء ح د:B006/m01`
- Ayah anchors: 112:1 `قل`, `أحد`; 112:2 `الصمد`; 112:4 `كفوا`, `أحد`
- Synthesis: Two wooden implements supply the tool-and-impact pattern, while the motion field supplies its possible effects: tilting, overturning, diversion, and sway. Mount Uhud gives the construction a concrete geographic setting for the staff-strike scene.

#### Subchannel B. Bodily Yielding and Endurance
- Reading type: latent/lexical
- Scene or process: Pressure produces either visible bodily disturbance or continued functioning through severe conditions.
- Active motifs: downcast face or changed color `ك ف ء:B002/m05`; persistence and survival `ص م د:B007/m01`; camel enduring cold and drought while maintaining milk `ص م د:B007/m02`
- Ayah anchors: 112:2 `الصمد`; 112:4 `كفوا`
- Synthesis: The two outcomes contrast yielding with resistance. One body registers disturbance in face and color; the enduring camel remains productive through cold and drought, turning persistence into sustained life under pressure.

## Standalone Subchannels

### S1. Composed Speech with Rhyme Mismatch
- Reading type: latent/lexical
- Scene or process: A composed poem or speech is evaluated for formal correspondence, and its rhyme fails to align.
- Active motifs: composed verbal form `ق و ل:B001/m02`; rhyme mismatch in letters, vowels, or inflection `ك ف ء:B003/m01`
- Ayah anchors: 112:1 `قل`; 112:4 `كفوا`
- Synthesis: Structured language supplies the verbal artifact, while rhyme mismatch identifies a defect in its patterned ending. The result is a complete scene of poetic composition assessed through formal correspondence.


