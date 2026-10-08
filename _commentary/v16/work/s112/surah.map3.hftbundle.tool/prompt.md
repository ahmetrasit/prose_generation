Surah: 112. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S112 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s112/surah.r2.hftbundle/text.md =====
# Surah 112

- 112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 112:2 ٱللَّهُ ٱلصَّمَدُ
- 112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
- 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ


===== _commentary/v16/work/s112/surah.r2.hftbundle/dictionary.md =====
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



===== _commentary/v16/work/s112/surah.r2.hftbundle/channels.md =====
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


===== _commentary/v16/work/s112/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 112

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 112:1

## spoken identity
- reading: A commissioned utterance that publicly identifies the referent as Allah and predicates absolute oneness.
- mechanism: The imperative externalizes a compact identification. The pronoun holds up the referent, the fixed divine name identifies him, and ahad predicates absolute oneness. The claim is therefore a repeatable public act, not only private recognition.
- trace:
  - 112:1 **قُلْ** ق و ل B001: Articulated utterance supplies the public speech act through which the identification is voiced.
  - 112:1 **ٱللَّهُ** ء ل ه B002: The fixed divine name supplies stable identification rather than an unnamed member of a class.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness supplies the predicate that closes the spoken identification.

## creedal alignment
- reading: The speaker is recruited to voice a worship-defining conviction: the worshipped referent is absolutely one.
- mechanism: The doctrine branch of qawl and the worship branch of ilah coactivate. Saying the clause becomes more than neutral reportage: it voices a held orientation toward the worshipped one, with absolute oneness as its content.
- trace:
  - 112:1 **قُلْ** ق و ل B013: Qawl as held doctrine lets the commanded saying function as avowal rather than detached quotation.
  - 112:1 **ٱللَّهُ** ء ل ه B001: Worship and the worshipped one give the avowal a relational orientation.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness is the doctrine being voiced about the worshipped referent.

## definitional limit
- reading: The whole utterance acts as a compressed boundary on recognition: the named referent is to be conceived under absolute oneness.
- mechanism: The definition branch of qawl makes the clause behave like a verbal boundary. The name is not unpacked into ancestry, parts, or a class; the short predicate limits recognition of its referent to absolute oneness.
- trace:
  - 112:1 **قُلْ** ق و ل B016: Qawl as a definition supplies the limiting function assigned to the commanded formulation.
  - 112:1 **ٱللَّهُ** ء ل ه B002: The fixed name is the item whose recognition is being bounded.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute one supplies the concise defining limit rather than one incidental quality.

## orienting terminus
- reading: Oneness is also asymmetrical orientation: all directed dependence can terminate in this one referent, who is not one dependent among others.
- mechanism: The repeated divine name keeps the same referent in view, while samad as the relied-upon destination turns oneness into a geometry of dependence. Many acts of worship, need, or intention can converge on one terminus without making that terminus one item among the many.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness supplies the focus predicate that is recast as singular terminus.
  - 112:2 **ٱللَّهُ** ء ل ه B001: The worshipped-one relation supplies agents whose devotion can be directed toward the repeated referent.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Directed approach toward a relied-upon destination supplies the convergent dependency structure.

## nonporous integrity
- reading: Ahad can also be heard as indivisible, non-porous integrity, with no internal lack or opening that would make the One dependent on exchange.
- mechanism: The compact-solid, sealed-stopper, and enduring-hardness images activate a material analogy for ahad. Oneness becomes non-porous integrity: no cavity suggests no internal lack, no opening suggests no required ingress or egress, and endurance keeps that integrity from being temporary.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness is the focus predicate receiving the material integrity analogy.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact solidity without a cavity supplies an image of integrity without internal lack.
  - 112:2 **ٱلصَّمَدُ** ص م د B003: A tightly sealing stopper supplies the boundary image of blocked ingress and egress.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Endurance under hardness makes the proposed integrity persistent rather than episodic.

## no derivation chain
- reading: The One is outside every source-result chain: neither producing by self-division nor produced from an antecedent.
- mechanism: The active and passive negations block opposite directions of production. With walad also imaging anything obtained or newly produced from something, ahad shifts from a count to causal non-derivation: the One is neither partitioned into a result nor a result extracted from a prior source.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness supplies the focus claim that is recast as freedom from derivational chains.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: The occurrence of birth supplies the concrete production event denied in both grammatical directions.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: A thing obtained or newly produced from another generalizes the denial from genealogy to derivation.

## outside genealogy
- reading: Ahad names one who is outside genealogical membership and succession, not a lone survivor within a lineage.
- mechanism: Parent and offspring images form a social genealogy in which identity and standing pass along a lineage. Denial of both positions makes the focus ahad not the last solitary member of a divine family but a referent outside the family structure itself.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B005: Isolation supplies the focus-side possibility of being alone, which the context revises from lone member to nonmember.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B001: Offspring from lineage supplies the descending kinship position denied to the referent.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B002: Parents by birth supply the ascending kinship position denied to the referent.

## positive negative ahad
- reading: The first ahad establishes a one-sided field: absolute oneness is positively affirmed of Allah while every possible counterpart is denied across time.
- mechanism: The same lexeme changes force across the frame: positively predicated ahad marks absolute oneness in 112:1, while ahad under negation exhausts every eligible candidate in 112:4. Temporal presence and counterpart matching make the back-projection precise: one is affirmed; any equal at any time is exhaustively denied.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Positive absolute oneness supplies the initial predicate whose scope is later sharpened.
  - 112:4 **يَكُن** ك و ن B001: Occurrence or presence in time extends the denial across possible temporal instantiation.
  - 112:4 **كُفُوًا** ك ف ء B001: Matching and counterpart relation specify the class of candidate being denied.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Negative exhaustive anyone removes every possible bearer of counterpart status.

## unplaced in rank
- reading: Allah is not commensurably placed on a hierarchy at all, because no coordinate rank can hold an equal.
- mechanism: Place or standing from kawn combines with matching from kufu to activate a status-space model. The focus One is not merely highest on a shared ladder; no counterpart occupies a corresponding place from which equal comparison could be made.
- trace:
  - 112:1 **ٱللَّهُ** ء ل ه B002: The fixed divine name anchors the status claim to the same identified referent.
  - 112:1 **أَحَدٌ** ء ح د B005: Isolation supplies separation from coordinate members of a common rank.
  - 112:4 **يَكُن** ك و ن B002: Place and standing supply the imagined hierarchy or coordinate position.
  - 112:4 **كُفُوًا** ك ف ء B001: Matching supplies the equal position whose existence the clause denies.

## minimal speech
- reading: The proposition's extreme verbal smallness can itself enact concentration: language is reduced until only referent, name, and absolute one remain.
- mechanism: 
- trace:
  - 112:1 **قُلْ** ق و ل B001: The dominant speech branch keeps the activation attached to an actual command to utter.
  - 112:1 **قُلْ** ق و ل B001: The non-dominant split target supplies fewness as an exploratory image of verbal reduction.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute one makes the reduced utterance converge on a single terminal predicate.

## not new or owned
- reading: The named One is also faintly heard as neither newly arrived nor held under another's ownership.
- mechanism: 
- trace:
  - 112:1 **ٱللَّهُ** ء ل ه B001: The worshipped-one relation makes subordination to an owner a status-reversing possibility.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness anchors the proposed freedom from acquired or dependent status.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B004: The branch's newborn-or-owned image activates temporal newness and possession as contained secondary denials.

## irreversible comparison
- reading: No reversible comparison can map another term onto Allah and return an equivalent; the One is not only unequal but non-interchangeable.
- mechanism: 
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness supplies the focus claim recast as resistance to reversible comparison.
  - 112:4 **كُفُوًا** ك ف ء B001: Matching supplies the ordinary comparison relation against which the outlier operates.
  - 112:4 **كُفُوًا** ك ف ء B002: Turning and reversal supply the exploratory image of mapping one side back onto another.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone removes every candidate that could complete the proposed reversible comparison.


# Focus 112:2

## resort terminal
- reading: Allah is presented functionally as the terminal destination of directed need and reliance.
- mechanism: The worshipped referent and the one intentionally resorted to combine into a directed dependency structure: affairs and needs move toward this referent and terminate in reliance there rather than being passed onward.
- trace:
  - 112:2 **ٱللَّهُ** ء ل ه B001: The worshipped one supplies the relational pole that the predicate identifies more precisely.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Intentional resort to a relied-on one supplies the directed motion and makes that pole the endpoint for affairs and needs.

## compact integrity
- reading: Their dependence terminates in one pictured as integrally full: support is not obtained by first repairing an interior deficiency.
- mechanism: A material analogy overlays the social image of a relied-on chief: dependability is pictured as compact integrity with no cavity or internal lack through which support would have to be received. The analogy concerns structure, not divine anatomy.
- trace:
  - 112:2 **ٱللَّهُ** ء ل ه B002: The fixed divine name holds the concrete analogy to this particular referent rather than to an unnamed solid object.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact, non-hollow solidity supplies the image of integral support that does not depend on filling an inner lack.

## sealing closure
- reading: The predicate pictures the point at which recourse is sealed and the chain of referral closes.
- mechanism: By material analogy, the predicate does more than name a destination: it marks closure. Resort reaches one capable of containing an affair and stopping leakage or indefinite referral beyond that point.
- trace:
  - 112:2 **ٱللَّهُ** ء ل ه B001: The worshipped referent supplies the personal pole to which the sealing image is predicated.
  - 112:2 **ٱلصَّمَدُ** ص م د B003: A tight stopper supplies containment and closure, functioning as an analogy for an affair that does not leak into further dependencies.

## enduring supply
- reading: Allah's permanence is read dynamically as support whose continuance is not exhausted by adverse or barren conditions.
- mechanism: Dependability becomes tested continuity rather than static permanence: the branch's creature enduring cold and drought while continuing its yield makes الصمد evoke support that does not cease when conditions become scarce or severe.
- trace:
  - 112:2 **ٱللَّهُ** ء ل ه B001: The worshipped one supplies the recipient of dependence whose reliability is being characterized.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Lasting through cold and drought while continuing provision supplies resilient continuity as the reason reliance holds under pressure.

## attentive threshold
- reading: The approached one is also pictured as attentively poised over the affair for which recourse is made.
- mechanism: The branch changes the relied-on endpoint from remote rank into attentive proximity: an affair brought to the Samad is pictured as already under concentrated regard at its threshold.
- trace:
  - 112:2 **ٱللَّهُ** ء ل ه B001: The worshipped referent anchors the otherwise idiomatic image as a claim about the divine relation to an affair.
  - 112:2 **ٱلصَّمَدُ** ص م د B005: Being on the verge of an affair and occupied with it supplies attentive immediacy to the endpoint of recourse.

## speech as definition
- reading: Allah al-Samad is also a commanded public definition that fixes the endpoint of recourse in speech.
- mechanism: The command to speak activates saying as both indication and delimiting definition. The compact nominal equation in 112:2 therefore functions not only as information but as a publicly uttered boundary for where reliance is to terminate.
- trace:
  - 112:1 **قُلْ** ق و ل B014: A thing's 'saying' as its indication makes the commanded utterance point beyond sound to the relation asserted in the focus.
  - 112:1 **قُلْ** ق و ل B016: Saying a thing as defining its limit makes the utterance set a conceptual boundary around the focus predicate.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Resort to the relied-on destination supplies the relation that the spoken definition publicly fixes.

## repeated referent
- reading: The predicate is locked to the same named worshipped referent identified immediately before it.
- mechanism: Repetition of the same divine name across 112:1 and 112:2 creates a tight referential bridge: the worshipped one just identified is precisely the one now predicated as the destination of resort, preventing الصمد from drifting into a generic class of chiefs.
- trace:
  - 112:1 **ٱللَّهُ** ء ل ه B001: The worshipped referent is introduced in the preceding equation and supplies the repeated identity carried into the focus.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: The destination relied upon supplies the new relation predicated of that repeated referent.

## single convergence
- reading: Al-Samad configures recourse as convergence on one endpoint with no coordinate remainder.
- mechanism: Unity before the focus and exhaustive negation at the close reshape resort into a topology of convergence: many affairs can be directed, but they do not terminate at several coordinate destinations. The one endpoint is also left without any residual competing instance.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B001: Oneness and unity supply a single pole toward which the focus predicate's directed resort can converge.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive negation removes any leftover instance that could serve as a coordinate endpoint.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Intentional resort supplies the many directed paths whose convergence is reorganized by the two context occurrences.

## uncomposed integrity
- reading: It becomes an exploratory image of integral unity whose reliability is not produced by cooperating internal parts.
- mechanism: The counting-and-composition branch of أحد presses the compact, non-hollow image of الصمد into a mereological question. Read against asserted unity and final exhaustive negation, compactness can suggest integrity not assembled from independently sustaining pieces.
- trace:
  - 112:1 **أَحَدٌ** ء ح د B003: The one as a unit in counting and composition introduces the live question of whether unity is aggregate or integral.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive negation prevents an unmentioned constituent or peer from casually remaining outside the unity claim.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact solidity without a hollow supplies the material analogy for integrity without an interior dependency.

## nonderived nonemanating
- reading: The Samad's endurance is non-genealogical and non-derivative: it neither arrives from a producer nor continues by producing a successor.
- mechanism: The paired active and passive birth negations turn compact endurance into causal independence in both directions. The Samad is neither a product derived from an upstream source nor a source that secures continuity by issuing a downstream successor.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: The event of birth supplies the concrete incoming and outgoing transitions canceled by the paired verbal forms.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: Something obtained or newly produced from something else generalizes lineage into derivation and lets the two negations test causal dependence.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact integrity supplies the focus anchor that is recast as having neither an originating deficit nor a generated continuation.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Lasting continuance supplies the persistence that no predecessor or offspring is needed to maintain.

## temporal invariance
- reading: The Samad's unmatched reliability is read across temporal occurrence, not as a temporary configuration.
- mechanism: The context branch of coming to presence in time tests the focus's enduring support against temporal occurrence. The closing negation allows no time at which a counterpart comes to be, so the Samad's singular reliability is not a temporary unmatched phase.
- trace:
  - 112:4 **يَكُن** ك و ن B001: Occurrence or presence in time supplies the temporal field across which the negated counterpart fails to appear.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Lasting endurance supplies the focus claim that is strengthened from persistence under hardship to persistence without a temporal peer-phase.

## asymmetric dependence
- reading: The Samad is the terminal pole of a non-reciprocal dependency field for which no matching pole exists.
- mechanism: Resort establishes directed dependence toward the Samad; the negated equal counterpart removes any peer that could mirror or reciprocate that relation. The result is not merely maximal rank but an asymmetric dependency network with one terminal pole.
- trace:
  - 112:4 **كُفُوًا** ك ف ء B001: Equality and matching opposition supply the possible coordinate pole that the context explicitly negates.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Directed resort and reliance supply the dependency arrows whose symmetry would require such a matching pole.

## split root load bearing
- reading: At the split-root fringe, the command activates the Samad as independently rising under and sustaining the loads that recourse directs there.
- mechanism: 
- trace:
  - 112:1 **قُلْ** ق و ل B004: Independently carrying and rising under a load supplies a dynamic load-bearing image from the packet's secondary root mapping.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact solidity supplies the stable structure capable of receiving the load-bearing activation.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Endurance under severity turns carrying from a static pose into sustained support under adverse conditions.

## bound attention
- reading: As an exploratory recitational image, the phrase also binds inward attention around a single dependable focus.
- mechanism: 
- trace:
  - 112:1 **قُلْ** ق و ل B012: Unvoiced saying within oneself supplies an interior recitation-space behind the overt command.
  - 112:2 **ٱلصَّمَدُ** ص م د B004: Wrapping the head with a cloth supplies a bodily image of binding and gathering attention around the predicate.

## sealed derivation
- reading: Through the sealing image, the Samad is the boundary at which origin-and-offshoot referral closes rather than passing through.
- mechanism: 
- trace:
  - 112:2 **ٱلصَّمَدُ** ص م د B003: The tightly fitted stopper supplies a concrete image of a boundary that closes passage and referral.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: Something derived or newly produced from another supplies the causal throughput canceled in both directions by the context.

## unturnable orientation
- reading: At the kinetic fringe, no counterforce can tilt, reverse, or redirect the trajectory of recourse away from the Samad.
- mechanism: 
- trace:
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Intending and resorting to the relied-on one supplies a directed trajectory toward the focus referent.
  - 112:4 **كُفُوًا** ك ف ء B002: Tilting, overturning, and diverting supply the possible counterforce that would bend or reverse that trajectory.


# Focus 112:3

## bidirectional birth closure
- reading: A two-way closure of birth relation: no descendant proceeds from the subject, and the subject proceeds from no progenitor.
- mechanism: The voice reversal closes both orientations of one birth relation. The subject is denied the parent or producer position, the offspring or product position, and participation in the event that would connect those positions.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B001: Born offspring supplies the relation's descendant endpoint, which the passive clause denies for the subject and the active clause denies as an output from the subject.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B002: Parents by birth relation supplies the complementary progenitor endpoint, making the two clauses a closure of both kinship directions.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: Birth and delivery supplies the event linking parent and born one; repeated negation blocks the event with the subject on either side.

## nonderived nongenerative
- reading: The subject is neither a source of derivative being nor a derivative whose identity depends on an originating source.
- mechanism: The generated-or-derived branch lifts the pair beyond literal delivery into provenance. Active voice denies that the subject generates a derivative; passive voice denies that the subject is itself generated or derivative. This remains a branch-led extension, not a replacement for the birth sense.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: A thing generated, newly produced, or derived supplies a non-biological source-result relation that the two voices negate in opposite directions.

## outside birth cohort
- reading: The subject also resists classification by birth cohort or by a generation descending from it.
- mechanism: The same-birth-age branch makes birth a coordinate that groups beings into cohorts. Denying birth removes that coordinate for the subject; denying begetting prevents a later cohort from being organized as the subject's issue.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B006: A peer defined by shared birth-age supplies cohort placement; the passive clause removes such placement and the active clause removes downstream generational placement.

## spoken predicate boundary
- reading: A publicly enacted rule against assigning either side of generative lineage to the subject.
- mechanism: The command to utter, together with branches for attribution and definition, turns the focus from an unframed biographical report into a performed boundary on what may be said of the subject. The two birth directions identify the prohibited attribution precisely.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B002: Parent roles by birth give the concrete relational attribution that the commanded utterance rejects in both directions.
  - 112:1 **قُلْ** ق و ل B001: Producing speech by vocal utterance makes the later negations part of an enacted public saying rather than only an inward conclusion.
  - 112:1 **قُلْ** ق و ل B005: Saying or attributing what was not supplies the danger of fictive lineage attribution that the focus verbally blocks.
  - 112:1 **قُلْ** ق و ل B016: A saying that states a thing's limit makes the paired negations function as a verbal delimitation of the subject.

## worship relation not birth relation
- reading: The verse preserves worship relation while refusing to recode that relation as parenthood or offspring.
- mechanism: Naming the subject through the worshipped relation keeps a real subject-other relation in view while the focus rejects genealogy as its grammar. The change is not from relation to isolation, but from reproductive reciprocity to worship orientation.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B002: Parent roles by birth supply the reciprocal family relation that is denied as a model for the named subject.
  - 112:1 **ٱللَّهُ** ء ل ه B001: Worship and the worshipped supply a distinct relational axis through which the subject is first identified.
  - 112:2 **ٱللَّهُ** ء ل ه B001: The repeated worshipped-name immediately before the focus keeps that non-genealogical relation active as both birth directions are denied.

## unity exhausts lineage
- reading: Undivided unity admits no lineage slot, and exhaustive negation leaves no one available as a concealed ascendant or descendant.
- mechanism: Unity before the focus and exhaustive negation after it bracket the mirrored birth clauses. A birth relation requires distinct relata occupying source and offspring slots; the bracket closes both slots and then refuses any residual member who could fill a counterpart position.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B001: Born offspring supplies one distinct lineage participant whose emergence from the subject is denied.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: Birth as an event supplies the differentiating transition that would establish separate lineage positions.
  - 112:1 **أَحَدٌ** ء ح د B001: Oneness and unity supply the positive frame against which multiplying lineage positions becomes incongruent.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive negation closes the domain after the focus so that no unmentioned lineage or counterpart participant remains.

## samad terminal not relay
- reading: The subject is a stable terminus of recourse, not a derived relay between an origin behind it and a successor after it.
- mechanism: The one toward whom recourse is directed and who persists under severity becomes a terminal, stable center rather than a relay in a chain of derivation and succession. Passive birth would put a source behind the subject; active begetting would put a successor beyond it. The focus blocks both extensions.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: Generated or derived existence supplies the backward provenance and forward production that would make the subject one link in a chain.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Directed recourse toward a dependable objective supplies an asymmetrical center at which dependence terminates.
  - 112:2 **ٱلصَّمَدُ** ص م د B007: Persistence and remaining firm supply continuity that contrasts with generational replacement.

## no temporal becoming
- reading: At no temporal point does the subject come to be as a generated result or enter a generative lineage role.
- mechanism: The later denial of occurrence or presence in time echoes the focus's negating construction and temporalizes its two voices. Birth and generation become states the subject never enters: neither arriving as generated nor becoming a generator in a lineage sequence.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: Birth and delivery supply bounded events whose occurrence for or from the subject is denied.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: Generation and derivation supply changes of provenance or status that can be tested against temporal becoming.
  - 112:4 **يَكُن** ك و ن B001: A thing's occurrence and presence in time supplies the temporal field over which the focus's denied birth states are extended.

## reversed relation without counterpart
- reading: The verse turns one relation around the subject and cancels it in both orientations, leaving neither reciprocal counterpart nor birth-defined peer.
- mechanism: The focus itself flips the same relation from active to passive. The context branches for like-for-like correspondence and turning-over make that grammatical reversal visible as a relational test: whichever way the birth relation is turned, no matching counterparty appears.
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B001: Born offspring supplies the counterpart produced when the birth relation is read outward from the subject.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B006: A same-birth-age peer supplies the latent comparison class that the later denial of an equivalent sharpens.
  - 112:4 **كُفُوًا** ك ف ء B001: Matching and like-for-like correspondence supply the counterpart test applied to parent, offspring, and birth-peer positions.
  - 112:4 **كُفُوًا** ك ف ء B002: Tilting, turning, and reversing supply a formal image for the active-to-passive flip of the same focus root.

## solid without birth passage
- reading: In a contained material image, there is no cavity or passage by which another emerges from the subject or the subject emerges from another.
- mechanism: 
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: Birth and delivery supply the passage-event that the material images recast spatially.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Dense solidity without a cavity supplies an image of no interior from which offspring could emerge and no interior through which the subject emerged.
  - 112:2 **ٱلصَّمَدُ** ص م د B003: A tightly sealing stopper supplies closure of an opening, reinforcing the image of blocked ingress and egress for birth.

## outside reproductive cycle
- reading: The subject stands outside recurrent cycles that produce, date, and replace one generation with another.
- mechanism: 
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: Birth as an event supplies reproduction as the transition by which a new generation appears.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B006: A same-birth-age peer supplies the cohort created by recurrence of birth within a cycle.
  - 112:4 **يَكُن** ك و ن B001: Occurrence in time supplies the temporal dimension needed for recurring generations.
  - 112:4 **كُفُوًا** ك ف ء B005: The turn of a year and its produce supply a recurrent yield-cycle against which the focus's nonparticipation in reproductive succession can be pictured.

## split root self standing
- reading: As a deliberately contained split-root echo, the subject is not carried into derived being by another but stands without transferred provenance.
- mechanism: 
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: Generated or derived existence supplies the provenance relation against which self-standing can contrast.
  - 112:1 **قُلْ** ق و ل B004: The non-dominant split branch supplies bearing a load and rising independently; obliquely, it activates a self-standing rather than carried-or-derived reading.

## birth and subjection
- reading: As a form-distant social echo, it also resists imagining the subject as born into subjection or as producing dependents whose relation is ownership-like.
- mechanism: 
- trace:
  - 112:3 **يَلِدْ يُولَدْ** و ل د B004: A young born one or slave term supplies a form-distant overlap between birth status, youth, and social dependency.
  - 112:1 **ٱللَّهُ** ء ل ه B001: Worship and the worshipped supply a live asymmetrical relation that need not be modeled as ownership or inherited subordination.
  - 112:4 **يَكُن** ك و ن B004: Submission through abasement supplies the social state that the slave-term branch brings into tension with the named worship relation.


# Focus 112:4

## exhaustive counterpart noninstantiation
- reading: At no time can any candidate enter a reciprocal matching, suitability, or oppositional relation with Him; the counterpart relation itself never obtains.
- mechanism: Temporal predication opens a possible relation of equal matching or reciprocal opposition, while negative exhaustive 'anyone' closes that relation over every candidate. The negation targets not only a resembling object but the occurrence of a peer relation at all.
- trace:
  - 112:4 **يَكُن** ك و ن B001: Being or temporal occurrence supplies the relation whose instantiation is denied.
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart and matching response make the denied relation reciprocal, suitable, or oppositional rather than merely similar.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Negative exhaustive anyone ranges the denial over every possible claimant.

## no comparable station
- reading: There is no station of parity beside Him that anyone could occupy.
- mechanism: The denied copular relation can be spatialized or socialized as occupying a station. Equality is then exclusion from a comparable position or rank, not only denial of shared qualities.
- trace:
  - 112:4 **يَكُن** ك و ن B002: Place, position, or rank turns being into occupancy of a station.
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart specifies the prohibited station as one of parity.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone prevents every candidate from occupying that parity-position.

## no overturning counterforce
- reading: No one can arise as an overturning or diverting counter-force against Him.
- mechanism: A branch-distant reading hears the counterpart term as a facing force capable of turning or diverting. Exhaustive negation then blocks not only an equal peer but any counter-force that could overturn or redirect Him.
- trace:
  - 112:4 **يَكُن** ك و ن B001: Occurrence supplies the possible arising of a counter-force.
  - 112:4 **كُفُوًا** ك ف ء B002: Tilting, overturning, and diverting recast a counterpart as an effective turning force.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone extends the denial to every imagined counter-force.

## spoken boundary against fabricated peers
- reading: The focus also regulates speech about Him: every assertion assigning a counterpart attributes a relation that never obtained.
- mechanism: The opening command to speak activates both attribution of what was not and speech as definition or delimitation. Applied to the focus negation, the statement becomes a public boundary on predication: assigning a peer is not merely inaccurate comparison but speech that attributes an unreal relation.
- trace:
  - 112:4 **يَكُن** ك و ن B001: Negated being supplies the unreal predication that the commanded utterance addresses.
  - 112:4 **كُفُوًا** ك ف ء B001: The equal counterpart is the content whose attribution is placed outside the valid boundary.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone leaves no exceptional subject for such an attribution.
  - 112:1 **قُلْ** ق و ل B005: Saying or attributing what was not makes peer-language a fabricated ontological assignment.
  - 112:1 **قُلْ** ق و ل B016: Saying a thing's limit makes the commanded utterance draw a category boundary around valid predication.

## worship relation without second recipient
- reading: No one can share a matching relational office as a second endpoint of worship.
- mechanism: The repeated divine name activates worship and the worshipped as a directed relation. The focus counterpart denial can therefore be read functionally: no second recipient occupies a matching endpoint of worship, and no reciprocal peer shares that relational office.
- trace:
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart and mutual matching define the second relational endpoint being denied.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone excludes every possible co-recipient.
  - 112:1 **ٱللَّهُ** ء ل ه B001: Worship and the worshipped supply the directed relation in which counterpart status would function.
  - 112:2 **ٱللَّهُ** ء ل ه B001: Repetition of the worshipped referent stabilizes the single endpoint before the focus denies a peer.

## the one not one of a class
- reading: The final 'any one' empties every peer class, so the opening One cannot mean one counted member, one-of-many, or first among comparables.
- mechanism: The same root first presents affirmative absolute oneness and finally appears as exhaustive anyone under negation. Counting and one-of branches remain available at the focus, so the return empties the comparison set: the earlier One is neither one counted member nor the first item of a class of peers.
- trace:
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart defines the comparison class that the final negation empties.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Negative exhaustive anyone searches the whole candidate set and finds no member.
  - 112:4 **أَحَدٌۢ** ء ح د B003: One in counting exposes the rejected possibility that divine oneness is a numeral inside a series.
  - 112:4 **أَحَدٌۢ** ء ح د B004: First or one-of exposes the rejected possibility that the One heads or belongs to a peer class.
  - 112:1 **أَحَدٌ** ء ح د B001: Absolute oneness supplies the affirmative pole that the final exhaustive negation protects from numerical reduction.

## convergent dependence without counternode
- reading: All resort can converge toward Him, but no reciprocal need and no second coequal endpoint can face Him.
- mechanism: The one aimed toward as the relied-upon endpoint creates a directed topology of dependence. The focus denies an equal counterpart, so convergence toward Him is not balanced by a reciprocal dependency or by a second terminal node; overseeing concern likewise has no coequal office.
- trace:
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart and mutual matching supply the reciprocal node whose existence is denied.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone prevents a second terminal or coequal node.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: Movement toward the relied-upon intended one supplies convergence and fixes the direction of dependence.
  - 112:2 **ٱلصَّمَدُ** ص م د B005: Overseeing a matter with active concern supplies an office that the focus leaves without a coequal sharer.

## no peer can emerge by derivation
- reading: No causal or temporal process can generate, derive, or install anyone as an equal.
- mechanism: Birth as an occurrence and a thing arising from another introduces causal production through time. The repeated negation closes both directions of that production before the focus denies any temporal occurrence of an equal; peerlessness is therefore diachronic and process-resistant, not a snapshot.
- trace:
  - 112:4 **يَكُن** ك و ن B001: Being and temporal occurrence turn peerlessness into a claim across possible emergence in time.
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart identifies the outcome that no process can produce.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone quantifies over every possible product or emergent claimant.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: The event of birth supplies a concrete process by which a new candidate might otherwise come to be.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: A thing obtained from or newly produced by another generalizes the blocked route from biological birth to derivation.

## no genealogical or coeval comparison class
- reading: No vertical lineage can locate Him and no lateral birth cohort exists within which anyone could count as His peer.
- mechanism: Lineage supplies parent-child axes, while the same birth root also supplies a peer of the same birth-age. Denial in both generational directions removes ancestry and descent, and the focus denial removes the lateral cohort in which equal comparison would normally be established.
- trace:
  - 112:4 **كُفُوًا** ك ف ء B001: Equal counterpart turns a birth cohort or lineage neighbor into the lateral class being excluded.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone empties every genealogical and coeval candidate position.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B001: A born member of lineage supplies the descendant axis of a comparison graph.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B002: Parents by birth supply the ancestral axis denied by the passive reversal.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B006: A peer of the same birth-age supplies the lateral cohort in which parity would ordinarily be tested.

## no external surety or load bearer
- reading: No one stands behind Him as guarantor, underwriter, or independent bearer; the direction of reliance runs toward Him.
- mechanism: 
- trace:
  - 112:4 **يَكُن** ك و ن B003: Suretyship or undertaking responsibility recasts the denied predicate as external backing.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone denies every possible guarantor or bearer.
  - 112:1 **قُلْ** ق و ل B004: Independent lifting and rising under a load activates the concrete image of an external bearer.
  - 112:2 **ٱلصَّمَدُ** ص م د B001: The relied-upon endpoint reverses support: others turn toward Him rather than bearing Him.

## no completing cover or stop
- reading: No external piece, cover, or complement is needed to close, complete, or structurally answer Him.
- mechanism: 
- trace:
  - 112:4 **كُفُوًا** ك ف ء B004: A rear tent-cover supplies an external piece that closes or completes a dwelling.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone rules out every candidate completing piece.
  - 112:2 **ٱلصَّمَدُ** ص م د B002: Compact solidity without a hollow removes the opening that an external complement might fill.
  - 112:2 **ٱلصَّمَدُ** ص م د B003: A tightly sealed bottle-stop sharpens the image of closure without an added counterpart.

## no generated yield or breeding lot
- reading: Nothing can be assigned to Him as generated yield, derivative output, offspring lot, or coeval production cohort.
- mechanism: 
- trace:
  - 112:4 **كُفُوًا** ك ف ء B005: Yearly produce and a breeding allotment recast the denied counterpart as generated yield or cohort.
  - 112:4 **أَحَدٌۢ** ء ح د B002: Exhaustive anyone prevents any product or offspring claimant from entering that slot.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B003: The event of birth activates production as a concrete process.
  - 112:3 **يَلِدْ يُولَدْ** و ل د B005: A thing newly obtained from another generalizes offspring into derived output.
