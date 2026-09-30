Focus: 1:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and map.md (an earlier reader's map of the image chains that run through the whole surah, with the dictionary phrases of their members in other ayat; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py 1:6 <refs separated by spaces>`. Judge what it returns, then write your final output. Run it only once; no other tool is available.

===== _commentary/v16/prompts/r10/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran; do not use tools. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. A theme is what the ayah's
words, read together, show, not a lesson drawn from them. Write the reading as
those themes: a word, a family image or a Quran passage enters where it
grounds, expands, complicates or joins a theme, developed as far as that work
needs. A family is never walked through for its own sake, and an image is not
left out for being rare or technical, or for sitting in another ayah's chain,
if it does work for a theme.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each image
  comes from: the word, the family's Arabic phrase that carries the image,
  then its work in the theme. Speak of the word's family, never of what
  dictionaries say.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give the speaker, the situation and the wording the connection needs.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan",
  "bildiğim kadarıyla", branch IDs, workflow language). What comes from memory
  rather than the supplied texts goes in the ledger.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran, hadith or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning}
The gloss gives the ayah's word by its meaning here, a family image by that
image. Cite Quran passages with exact refs, e.g. (2:255), no ranges; copy Quran
Arabic from the supplied text where it is supplied.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one line per item:
- memory: <what came from memory> (<ref or source>)
- not written: <finding, chain or passage considered> - <why it did no work for a theme, or where its evidence failed>


===== _commentary/v16/prompts/r10/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/1_6/DM.r3/context.md =====
# 1:6 — focus

ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

Anchor translation (canonical reading, reference only):

Bizi doğru yola ilet.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱهْدِنَا | هَدَى | ه د ي | V;PRON |
| 2 | ٱلصِّرَٰطَ | صِرَٰط | ص ر ط | DET;N |
| 3 | ٱلْمُسْتَقِيمَ | مُّسْتَقِيم | ق و م | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 1 — full text (context; no pericope)

- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ◀ focus ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ


===== _commentary/v16/work/1_6/DM.r3/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ه د ي (root_001583) — identity root of ٱهْدِنَا (w1)

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

## ص ر ط (root_000858) — identity root of ٱلصِّرَٰطَ (w2)

- **B001** yol, özellikle düz yol — yol, özellikle düz yol · yol veya düz yol · yol
  الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)
- **B002** geçişte gözden kaybolmak; özellikle yiyeceği yutmak — yiyeceği boğazdan geçirip gözden kaybolacak biçimde yutmak · kolayca yutulan pelte kıvamlı tatlı · geniş boğazlı
  أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب؛ السرطراط على فعلال الفالوذ لأنه يسترط (maqayis 1774)؛ السرطم: الواسع الحلق، والميم فيه زائدة، وإنما هو من سرط، إذا بلع (maqayis السرطم)
- **B003** vuruşta kesip ilerleyen kılıç — vuruşta kesip ilerleyen kılıç
  والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)

## ق و م (root_001273) — identity root of ٱلْمُسْتَقِيمَ (w3)

- **B001** erkekler topluluğu ve yakın çevresi — aslen erkeklerden oluşan topluluk · bir erkeğin yandaşları ve yakın soy çevresi · topluluklar; çoğulun çoğulu
  القوم الرجال دون النساء؛ قوم كل رجل شيعته وعشيرته (ayn;tahdhib)؛ القوم الرجال دون النساء؛ ربما دخل النساء فيه على سبيل التبع (sihah)؛ القوم جماعة الرجال في الأصل دون النساء؛ وفي عامة القرآن أريدوا به والنساء جميعا (mufradat)؛ القوم جمع امرئ ولا يكون ذلك إلا للرجال؛ وربما استعير في غيرهم (maqayis)
- **B002** ayağa kalkma ve dik durma — ayağa kalkmak veya dikilmek · bir kez ayağa kalkma; iki bölüm arasındaki ayakta duruş · kökleri üzerinde dikili kalmış
  القومة ما بين الركعتين من القيام؛ قمت قياما؛ منها هامد ومنها قائم (ayn;tahdhib)؛ قام الرجل قياما؛ القومة المرة الواحدة؛ قامت الدابة وقفت (sihah)؛ قيام بالشخص إما بتسخير أو اختيار؛ ساجدا وقائما؛ تركتموها قائمة على أصولها (mufradat)؛ قام قياما والقومة المرة الواحدة إذا انتصب (maqayis)
- **B003** bir işe kararlılıkla girişme [kalıp] — bu işi üstlenip kararlılıkla girişti
  قام بمعنى العزيمة؛ قام بهذا الأمر إذا اعتنقه؛ قيام عزم (maqayis)؛ القيام الذي هو العزم؛ إذا قمتم إلى الصلاة (mufradat)
- **B004** sürekli gözetip yönetme — işi gözeten, koruyan ve yürüten kişi · topluluğun işlerini yöneten kişi · her şeyi sürekli yöneten ve koruyan · onu taşıyamadı veya buna gücü yetmedi
  قيم القوم من يسوس أمرهم ويقومهم؛ القائم في الملك ونحوه الحافظ؛ القيوم (ayn)؛ قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم؛ القيوم اسم من أسماء الله (sihah)؛ قيم القوم الذي يقومهم ويسوس أمرهم؛ القائم بالأمر؛ القيوم القائم على كل شيء (tahdhib)؛ قيام للشيء هو المراعاة للشيء والحفظ له؛ قوامين لله؛ القيوم القائم الحافظ لكل شيء (mufradat)؛ قام بهذا الأمر إذا اعتنقه؛ قوام الدين والحق أي به يقوم (maqayis)
- **B005** sürdürüp gereğini yerine getirme [kalıp] — bir şeyi sürdürmek, işler halde tutmak veya gereğini yerine getirmek · ibadetin ya da kitabın gereklerini eksiksiz uygulamak
  أقام الشيء أي أدامه؛ يقيمون الصلاة (sihah)؛ أقمت الشيء وقومته فقام بمعنى استقام؛ إقام الصلاة (tahdhib)؛ إقامة الشيء توفية حقه؛ تقيموا التوراة والإنجيل؛ أقيموا الصلاة؛ مقيم الصلاة (mufradat)
- **B006** bir yerde kalma ve kalınan yer — bir yerde yerleşip kalmak · ayak basılan veya kalınan yer ya da süre; oturum veya toplanmış topluluk
  أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين؛ المقام والمقامة الموضع الذي تقيم فيه (ayn;tahdhib)؛ المقامة الإقامة؛ المقامة المجلس والجماعة من الناس؛ المقام موضع القيام أو الإقامة (sihah)؛ المقام يكون مصدرا واسم مكان القيام وزمانه؛ المقامة الإقامة؛ لا مقام لكم أي لا مستقر لكم (mufradat)
- **B007** başkasının yerini ve işlevini alma [kalıp] — onun yerine geçti veya adına görev yaptı
  القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)؛ قام فلان مقام فلان إذا ناب عنه؛ يقومان مقامهما (mufradat)؛ أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك (maqayis)
- **B008** düzgünlük, denge ve doğru yoldan sapmama — düzgün ve dengeli olmak; doğru yoldan ayrılmamak · düzgün, dengeli ve doğru
  رمح قويم ورجل قويم؛ القيمة الملة المستقيمة؛ إذا انقاد واستمرت طريقته فقد استقام (ayn)؛ الاستقامة الاعتدال؛ استقام له الأمر؛ قومت الشيء فهو قويم أي مستقيم؛ القوام العدل؛ دينا قيما (sihah)؛ الاستقامة على الطاعة؛ القيم هو المستقيم؛ أقوم كلاما أي أعدل كلاما (tahdhib)؛ الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم؛ دينا قيما أي ثابتا (mufradat)
- **B009** ayakta tutan dayanak ve geçim temeli — bir şeyi ayakta tutan dayanak, düzen ve geçim temeli
  هذا الأمر لا قومية له أي لا قوام له؛ القوام من العيش ما يقيمك ويغنيك؛ القيام العماد؛ قوام كل شيء ما استقام به (ayn)؛ قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه؛ جعل الله لكم قياما (sihah)؛ قوام الأمر وملاكه؛ تقيمكم فتقومون بها؛ قوام الجسم تمامه؛ قوام كل شيء ما استقام به (tahdhib)؛ القيام والقوام اسم لما يقوم به الشيء؛ جعلها مما يمسككم؛ قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم (mufradat)؛ قوام الدين والحق أي به يقوم (maqayis)
- **B010** değer biçme ve belirlenen bedel — değer biçmeyle belirlenen bedel · malın değerini belirlemek veya ulaştığı bedeli bildirmek
  القيمة ثمن الشيء بالتقويم؛ تقاوموا فيما بينهم (ayn)؛ قومت السلعة؛ استقمت السلعة؛ القيمة واحدة القيم (sihah)؛ القيمة ثمن الشيء بالتقويم؛ تقاوموه فيما بينهم؛ استقمت المتاع أي قومته؛ قامت الأمة مائة دينار أي بلغت قيمتها (tahdhib)؛ تقويم السلعة بيان قيمتها (mufradat)؛ قومت الشيء تقويما؛ أصل القيمة الواو (maqayis)
- **B011** insanın boyu ve düzgün beden yapısı — insanın boyu ve beden uzunluğu · düzgün ve güzel boy; beden yapısı
  القامة مقدار قيام الرجل؛ قوام الجسم تمامه وطوله (ayn)؛ قوام الرجل قامته وحسن طوله؛ قامة الإنسان قده (sihah)؛ القامة قامة الرجل؛ حسن القامة والقمة والقومية؛ قوام الجسم تمامه (tahdhib)؛ تقويم الإنسان في أحسن تقويم؛ انتصاب القامة (mufradat)؛ القوام الطول الحسن؛ القومية القوام والقامة (maqayis)
- **B012** düzeneğin dik, taşıyıcı veya tutulan parçası — kuyu makarası veya ona bağlı donanım · kuyu başındaki insan biçimli yapı diye aktarılmış, fakat yanlış sayılmış yorum · kılıç sapı veya yatak, masa ve hayvanın dik duran parçası · çiftçinin elinde tuttuğu ahşap parça
  القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر؛ قائم السيف مقبضه؛ قائمة السرير والخوان والدابة (ayn)؛ القامة البكرة بأداتها؛ قائم السيف وقائمته مقبضه؛ القائمة واحدة قوائم الدواب؛ المقوم الخشبة التي يمسكها الحراث (sihah)؛ القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة؛ قائم السيف مقبضه وما سوى ذلك فهو قائمة (tahdhib)؛ القامة البكرة بأداتها (maqayis)
- **B013** ölülerin diriltildiği ve insanların yargı için kalktığı gün — ölülerin diriltildiği ve insanların yargı için ayağa kalktığı son gün
  القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)؛ يوم القيامة معروف (sihah)؛ القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم (tahdhib)؛ القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين (mufradat)
- **B014** karşılıklı direnip mücadele etme [kalıp] — ona karşı durup mücadele etmek; tarafların birbirine karşı koyması
  قاومته في كذا أي نازلته (ayn)؛ قاومه في المصارعة وغيرها؛ تقاوموا في الحرب أي قام بعضهم لبعض (sihah)؛ ما زلت أقاوم فلانا في هذا الأمر أي أنازله (tahdhib)
- **B015** tam ve denk ağırlıktaki para — ölçün ağırlığa tam denk gelen, ağır basmayan para
  دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)؛ دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح (tahdhib)
- **B016** donup akmama veya yorulup ilerleyememe [kalıp] — su dondu veya akmaz halde kaldı · binek hayvanı durdu veya yorulup yürüyemedi
  قام الماء جمد؛ قامت الدابة وقفت (sihah)؛ قامت لفلان دابته إذا كلت أو عيت فلم تسر (tahdhib)
- **B017** güneşin tam tepede olduğu öğle ortası — güneşin ortada, günün iki yarısının dengede olduğu öğle vakti
  قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn;tahdhib)؛ قام ميزان النهار إذا انتصف؛ قام ميزان النهار فاعتدل (tahdhib)
- **B018** pazarın canlanıp satışların artması [kalıp] — pazar canlandı ve mallar alıcı buldu
  قامت السوق نفقت (sihah)؛ قامت السوق إذا نفقت ونامت إذا كسدت (tahdhib)
- **B019** bir beden bölümünün kişiye ağrı vermesi [kalıp] — sırtım veya gözlerim ağrıdı
  قام بي ظهري أي أوجعني؛ قامت بي عيناي؛ كل ما أوجعك من جسدك فقد قام بك (tahdhib)
- **B020** koyunun bacaklarını tutan hastalık — koyunun bacaklarını tutup onu ayağa kaldıran hastalık
  القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)؛ أخذها قوام وهو داء يأخذها في قوائمها تقوم منه (tahdhib)
- **B021** göz bebeği sağlamken görme yetisinin kaybolması — göz bebeği sağlam kaldığı halde görmeyen göz
  عين قائمة ذهب بصرها والحدقة صحيحة (ayn)؛ العين القائمة أن يذهب بصرها والحدقة صحيحة (tahdhib)

## ECHO ه د د (root_001580) — for ٱهْدِنَا (w1): withheld observed target; not identity

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



===== _commentary/v16/out/s001/surah.map3.nohft/map.md (without ## Not carried) =====
## Chains

### The road: guide ahead, a line laid straight, the lost beside it

A traveller asks to be led. The guide walks in front, the road is a straight line, waymarks stand along it, and its trodden middle is kept. It is the known way of those who went before. Off the road, paths scatter, the land bewilders, and the one who veers cannot find the house the road leads to. The chain runs 1:6 اهدنا → الصراط المستقيم → 1:7 صراط الذين → الضالين. The dictionary joins the two words of 1:6: "الصراط: الطريق المستقيم" (mufradat). It also joins the first and last requests of the passage as opposites: "الضلال ضد الهدى" (jamhara) and "الهدى نقيض الضلالة" (ayn;tahdhib). The two halves mirror each other: "هديته الطريق والبيت" (sihah) against "ضللت المسجد والدار إذا لم تهتد لهما" (maqayis).

- 1:6 ٱهْدِنَا — ه د ي B001 — "هديته الطريق والبيت هداية أي عرفته" (sihah); "الهداية دلالة بلطف؛ تعريف الطرق" (mufradat) — making the road and the house at its end known.
- 1:6 ٱهْدِنَا — ه د ي B003 — "الدليل يسمى هاديا لتقدمه" (ayn); "الهادية العصا لأنها تتقدم ممسكها" (maqayis) — the guide who walks ahead; the staff that goes before its holder.
- 1:6 ٱهْدِنَا — ه د ي B002 — "هدى هدي فلان أي سار سيرته" (sihah); "هدية فلان وهديه أي طريقته" (mufradat) — walking another's way, which is what 1:7 صراط الذين asks for.
- 1:6 ٱلصِّرَٰطَ, 1:7 صِرَٰطَ — ص ر ط B001 — "الصراط والسراط والزراط: الطريق" (sihah); "الصراط: الطريق المستقيم؛ ويقال له سراط" (mufradat) — the road itself.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B008 — "الاستقامة في الطريق الذي يكون على خط مستو" (mufradat); "إذا انقاد واستمرت طريقته فقد استقام" (ayn) — the road as a level, unbroken line.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — "المعلم الأثر يستدل به على الطريق" (sihah;tahdhib); "العلم الجبل الطويل" (ayn) — the waymark and the mountain seen from the road.
- 1:4 مَٰلِكِ — م ل ك B006 — "الزم ملك الطريق أي وسطه" (tahdhib) — keeping to the road's middle.
- 1:5 نَعْبُدُ — ع ب د B005 — "الطريق المعبد وهو المسلوك المذلل" (maqayis) — the road trodden smooth by walkers.
- 1:5 نَعْبُدُ — ع ب د B010 — "العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة" (tahdhib) — the diverging roads, the reverse of the one road.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B001 — "ضل في الأرض إذا لم يهتد للسبيل" (jamhara); "كل جائر عن القصد ضال" (maqayis) — the one who veers off the way.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — "ضللت المسجد والدار إذا لم تهتد لهما" (maqayis) — failing to reach the house the road leads to.
- 1:1 ٱللَّهِ (documented alternative و ل ه) — و ل ه B001 — "البلاد التي توله الإنسان أي تحيره" (sihah) — the land that bewilders.

Quran passages:
- 6:153 — Allah's commands, recited by the Prophet (scene opens 6:151 "قل تعالوا أتل ما حرم ربكم عليكم"): "وأن هذا صراطي مستقيما فاتبعوه ولا تتبعوا السبل فتفرق بكم عن سبيله". One straight road set against scattering paths.
- 6:71 — the Prophet told to answer the idolaters: "كالذي استهوته الشياطين في الأرض حيران له أصحاب يدعونه إلى الهدى ائتنا". A man bewildered in the land while companions call him to the road.
- 5:77 — to the People of the Book: "قد ضلوا من قبل وأضلوا كثيرا وضلوا عن سواء السبيل". Straying from the road's middle.
- 36:60–61 — Allah to the children of Adam: "ألم أعهد إليكم يا بني آدم ... وأن اعبدوني هذا صراط مستقيم".
- 19:36 — ʿĪsā in the cradle: "وإن الله ربي وربكم فاعبدوه هذا صراط مستقيم".

### The failing mount and the hand that holds up

The road has its failures. The mount tires, halts and gives out, and the rider is stranded. A weak man walks swaying and leaning on two others. Someone unloads the traveller's saddle and sets his state right, and the walker goes on calmly, not in the rush of a rout. In the surah, نستعين (1:5) stands directly before the request for the road (1:6).

- 1:5 نَعْبُدُ — ع ب د B011 — "أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت" (sihah); "أعبد به إذا ذهبت راحلته" (tahdhib) — stranded when the mount fails.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B016 [fixed expression] — "قامت لفلان دابته إذا كلت أو عيت فلم تسر" (tahdhib) — the mount halts from exhaustion.
- 1:6 ٱهْدِنَا — ه د ي B008 — "يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله" (sihah) — walking held up by two.
- 1:5 نَسْتَعِينُ — ع و ن B001 — "كل شيء استعنت به أو أعانك فهو عونك" (ayn); "العون الظهيرة على الأمر" (sihah) — the backing one leans on.
- 1:7 غَيْرِ — غ ي ر B001 — "حط عنه رحله وأصلح من شأنه" (tahdhib); "يصلحون الرحال" (sihah) — unloading the saddle and setting the traveller right.
- 1:6 ٱهْدِنَا — ه د ي B010 — "لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن" (ayn) — the calm gait once the traveller is set right.

Quran and hadith:
- 28:21–24 — Mūsā fleeing alone toward Madyan (scene opens 28:21 "فخرج منها خائفا يترقب"): 28:22 "عسى ربي أن يهديني سواء السبيل"; 28:24 "رب إني لما أنزلت إلي من خير فقير".
- From memory, hadith: the Prophet in his last illness went out "يهادى بين رجلين" (Bukhārī).
- From memory, hadith: the man whose mount escaped in a waterless land and who despaired until it returned (Muslim). This also stages the herd chain's lost mount.

### The herd: owner, lead beast, legs and neck, the stray

Animals gather in a herd under an owner. The lead beast goes in front and the rest follow. A beast is carried by its legs and led by its neck. The stray camel stays in a place of loss, its owner unknown, and a company scatters. The dictionary joins three of the surah's roots in one phrase: "ملك الدابة قوائمها وهاديها" (sihah;tahdhib), and "جاءنا تقوده ملكه يعني قوائمه وهاديه" (tahdhib). That is ملك (1:4), قوائم (ق و م, 1:6) and هادي (1:6). It also joins the stray and the owner: "الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها" (ayn). That is الضالين (1:7) and رب (1:2).

- 1:2 رَبِّ — ر ب ب B001 — "رب الدار ورب الفرس" (mufradat); "ورب كل شيء مالكه" (jamhara) — the owner of the beast.
- 1:2 رَبِّ — ر ب ب B014 — "الربرب: القطيع من بقر الوحش" (sihah); "يجوز أن يضم إلى الباب الثالث لتجمعه" (maqayis) — the herd, named for its gathering.
- 1:5 نَسْتَعِينُ — ع و ن B006 — "العانة القطيع من حمر الوحش" (sihah) — a herd of wild asses.
- 1:7 أَنْعَمْتَ — ن ع م B005 — "النعم الإبل لما فيه من الخير والنعمة" (maqayis) — camels, named from favour.
- 1:4 مَٰلِكِ — م ل ك B008 [fixed expression] — "ملك الإبل والشاء ما يتقدم ويتبعه سائره" (mufradat); "مليك النحل يعسوبها" (sihah) — the lead beast the rest follow.
- 1:6 ٱهْدِنَا — ه د ي B003 — "هوادي الوحش متقدماتها الهادية لغيرها" (mufradat); "الهادي العنق" (sihah) — the forward animals, and the neck that leads.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B012 — "القائمة واحدة قوائم الدواب" (sihah) — the legs that carry it.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B005 — "الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء" (ayn) — the stray.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — "أضل بعيره إذا أفلت فذهب" (ayn) — the camel slipping loose.
- 1:7 أَنْعَمْتَ — ن ع م B008 [fixed expression] — "شالت نعامتهم إذا تفرقوا" (maqayis) — the company scattering.

Quran passages:
- 12:39 — Yūsuf to his prison companions: "أأرباب متفرقون خير أم الله الواحد القهار". Scattered lords against the one.
- 16:5–6 — Allah on livestock: "والأنعام خلقها لكم ... ولكم فيها جمال حين تريحون وحين تسرحون". Herds driven out and brought home.

### Owner, king and the owned servant

The owner holds what his hand possesses and the king commands. The owned man is humbled and subjected. The city is where the ruler is obeyed. Reversed, the servant's root also names the one who is served. The dictionary joins the words of 1:2, 1:4 and 1:5:
- "ورب كل شيء مالكه" (jamhara) joins رب and مالك.
- "العبد وهو المملوك" (maqayis) joins عبد and ملك.
- "دانه دينا أي أذله واستعبده ودينته ملكته" (sihah) joins دين, عبد and ملك.
- "غير مدينين غير مملوكين" (tahdhib) joins غير, دين and ملك.

- 1:2 رَبِّ — ر ب ب B001 — "يكون الرب: السيد المطاع" (tahdhib); "رببت القوم: سستهم" (sihah) — the obeyed master who governs.
- 1:4 مَٰلِكِ — م ل ك B002 — "الملك ما ملكت اليد من مال وخول" (ayn;tahdhib); "المملوك يختص في التعارف بالرقيق من الأملاك" (mufradat) — what the hand holds, including people.
- 1:4 مَٰلِكِ — م ل ك B003 — "والاسم الملك لأن يده فيه قوية صحيحة" (maqayis); "الملك هو المتصرف بالأمر والنهي في الجمهور" (mufradat) — the king who commands and forbids.
- 1:4 ٱلدِّينِ — د ي ن B004 — "المدين والمدينة العبد والأمة" (mufradat); "دنت القوم أدينهم إذا أذللتهم" (tahdhib) — subjection.
- 1:4 ٱلدِّينِ — د ي ن B006 — "المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر" (maqayis) — the city of obedience.
- 1:5 نَعْبُدُ — ع ب د B001 — "العبد خلاف الحر والجمع عبيد" (sihah) — the owned man.
- 1:5 نَعْبُدُ — ع ب د B004 — "عبدت العبيد وأعبدتهم أي صيرتهم عبيدا" (tahdhib) — making slaves.
- 1:5 نَعْبُدُ — ع ب د B002 — "العبد الإنسان حرا أو رقيقا هو عبد الله" (ayn); "تفرقة ما بين عباد الله والعبيد المملوكين" (maqayis) — every person as Allah's servant.
- 1:5 نَعْبُدُ — ع ب د B006 — "المعبد أي معظما مخدوما" (tahdhib) — the reversal: the one who is served.

Quran passages:
- 16:75 — Allah's parable: "ضرب الله مثلا عبدا مملوكا لا يقدر على شيء".
- 114:1–3 — the Prophet told to seek refuge: "قل أعوذ برب الناس ملك الناس إله الناس".
- 56:86–87 — Allah to deniers at the moment of death (scene opens 56:83 "فلولا إذا بلغت الحلقوم"): "فلولا إن كنتم غير مدينين ترجعونها".
- 3:26 — the Prophet told to pray: "قل اللهم مالك الملك".

### The worshipped one and the humbled worshipper

Allah is God because He is worshipped. The worshipper lowers himself the way a road is trodden down and a camel is tarred and tamed. Obedience becomes habit. The alternative derivation adds the heart's yearning. The dictionary joins الله (1:1) and نعبد (1:5): "فالإله الله تعالى لأنه معبود" (maqayis). It quotes 1:5 itself: "إياك نعبد إياك نطيع الطاعة التي نخضع معها" (tahdhib). It joins دين with الله and عبد: "الدين لله طاعته والتعبد له" (tahdhib).

- 1:1 ٱللَّهِ, 1:2 لِلَّهِ — ء ل ه B001 — "فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد" (maqayis); "لا يكون إلاها حتى يكون معبودا" (tahdhib) — the one worshipped.
- 1:5 نَعْبُدُ — ع ب د B003 — "العبودية إظهار التذلل والعبادة غاية التذلل" (mufradat); "تعبدت للرجل إذا تذللت له" (jamhara) — the act of lowering oneself.
- 1:5 نَعْبُدُ — ع ب د B005 — "البعير المعبد المهنوء بالقطران المذلل" (maqayis;sihah); "طريق معبد أي مذلل" (jamhara;mufradat) — the concrete humbling of a tamed camel and a trodden road.
- 1:4 ٱلدِّينِ — د ي ن B001 — "وهو جنس من الانقياد والذل" (maqayis); "فالدين الطاعة" (maqayis;sihah) — being led and yielding.
- 1:4 ٱلدِّينِ — د ي ن B005 — "العادة يقال لها دين" (maqayis) — obedience worn into habit.
- 1:1 ٱللَّهِ (documented alternative و ل ه) — و ل ه B001 — "ولهت إليه تله أن تحن إليه" (tahdhib); "الوله ذهاب العقل والتحير من شدة الوجد" (sihah) — the heart's yearning toward him.

Quran passages:
- 19:64–65 — the angels' words (scene opens 19:64 "وما نتنزل إلا بأمر ربك"): "رب السماوات والأرض وما بينهما فاعبده واصطبر لعبادته هل تعلم له سميا".
- 20:14 — Allah to Mūsā at the fire (scene opens 20:9): "إنني أنا الله لا إله إلا أنا فاعبدني".

### Name, mark and brand

A name raises its bearer and makes a thing known. A brand burned on a camel marks it, and a face is read for its signs. Each kind of creation is a mark by which something is known. A mark sets one thing apart from another. No one bears His name as an equal. The surah opens on a name (بسم) and closes by setting apart with غير. The dictionary joins بسم and الله: "اسم الله الأكبر هو الله" (ayn;tahdhib). Maqayis defines the mark by "غير": "أثر بالشيء يتميز به عن غيره".

- 1:1 بِسْمِ — س م و B005 — "الاسم ما يعرف به ذات الشيء وأصله سمو" (mufradat); "أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى" (maqayis) — the name that makes a thing known.
- 1:1 بِسْمِ — س م و B001 — "أصله من السمو وهو الذي به رفع ذكر المسمى" (mufradat) — the name raises its bearer.
- 1:1 بِسْمِ — س م و B005, B007 — "سميا أي نظيرا له يستحق اسمه" (mufradat); "فلان لا يسامى" (sihah) — the equal who does not exist; none can rise against him.
- 1:1 بِسْمِ — س م و B008 — "ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر" (tahdhib) — a name gone out among people.
- 1:1 ٱللَّهِ — ء ل ه B002 — "اسم الله الأكبر هو الله" (ayn;tahdhib); "فخص بالباري تعالى" (mufradat) — a name reserved to one.
- 1:1 بِسْمِ (documented alternative و س م) — و س م B001 — "الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها" (ayn); "الميسم المكواة" (ayn;sihah;tahdhib) — the brand and the branding iron.
- 1:1 بِسْمِ (documented alternative و س م) — و س م B002 — "توسمت فيه الخير والشر أي رأيت فيه أثرا" (ayn) — reading the mark.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — "أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره" (maqayis) — the distinguishing mark.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — "العالمون كل جنس من الخلق فهو في نفسه معلم وعلم" (maqayis); "وهو في الأصل اسم لما يعلم به" (mufradat) — each kind of creation as a mark.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B001 — "علمت الشيء عرفته" (sihah;tahdhib) — knowing by the mark.
- 1:7 غَيْرِ — غ ي ر B005 — "هذا الشيء غير ذاك أي هو سواه وخلافه" (maqayis) — the setting-apart that sorts the three companies of 1:7.

Quran passages:
- 2:31 — Allah teaching Adam (scene opens 2:30 "وإذ قال ربك للملائكة"): "وعلم آدم الأسماء كلها".
- 87:1 — "سبح اسم ربك الأعلى". Name, Lord and height together.
- 55:78 — "تبارك اسم ربك ذي الجلال والإكرام".
- 48:29 — "سيماهم في وجوههم من أثر السجود". The mark left by worship.
- 68:16 — threat against a slanderer: "سنسمه على الخرطوم".
- 15:75 — after Lūṭ's town: "إن في ذلك لآيات للمتوسمين".

### The sky of worship: sun, crescent, zenith, sphere

The sky arches overhead. The sun rises and sets and stands at the zenith. The crescent lifts above the horizon and the moon passes through its stations. Some worshipped the sun. The rising and setting of these bodies raise the question of who is Lord, and whose guidance keeps a person from straying.

- 1:1 ٱللَّهِ — ء ل ه B001 — "والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها" (maqayis) — the sun that some worshipped.
- 1:1 بِسْمِ — س م و B004 — "السماء كل ما علاك فأظلك" (sihah) — the sky overhead.
- 1:1 بِسْمِ — س م و B002 — "سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا" (ayn) — the crescent rising above the horizon.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — "العالم اسم للفلك وما يحويه" (mufradat) — the sphere and what it holds.
- 1:4 يَوْمِ — ي و م B001 — "اليوم مقداره من طلوع الشمس إلى غروبها" (ayn;tahdhib) — sunrise to sunset.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B017 — "قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل" (ayn;tahdhib) — the sun standing at the zenith.
- 1:7 أَنْعَمْتَ — ن ع م B007 — "والنعائم منزل من منازل القمر" (sihah) — a station of the moon.

Quran passages:
- 6:75–79 — Ibrāhīm watching the night sky (scene opens 6:75 "وكذلك نري إبراهيم ملكوت السماوات والأرض"). 6:77: "فلما رأى القمر بازغا قال هذا ربي فلما أفل قال لئن لم يهدني ربي لأكونن من القوم الضالين".
- 41:37 — "لا تسجدوا للشمس ولا للقمر واسجدوا لله الذي خلقهن إن كنتم إياه تعبدون".
- 27:24 — the hoopoe on Sabaʾ (scene opens 27:20): "وجدتها وقومها يسجدون للشمس من دون الله ... فهم لا يهتدون".

### Womb, birth and rearing

The womb holds and grows the young. A ewe newly delivered is kept at home for milk, or ails after the birth. A child is reared stage by stage, by a parent or a foster parent. A mother parted from her young is frantic. Kin are those who came out of one womb. The name repeated in 1:1 and 1:3 carries the womb. رب (1:2) carries the newly delivered ewe and the rearing.

- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B003 — "الرحم بيت منبت الولد ووعاؤه في البطن" (ayn;tahdhib) — the womb as the house where the child grows.
- 1:1, 1:3 — ر ح م B002 — "استعير الرحم للقرابة لكونهم خارجين من رحم واحدة" (mufradat) — kin from one womb.
- 1:1, 1:3 — ر ح م B001 — "ورحمة الضعيف والتعطف عليه" (tahdhib) — tender care for the weak.
- 1:1, 1:3 — ر ح م B004 — "ناقة رحوم إذا اشتكت رحمها في عقب الولادة" (jamhara); "والرحام أن تلد الشاة ثم لا تلقي سلاها" (tahdhib) — the mother's body after birth.
- 1:2 رَبِّ — ر ب ب B009 — "الربى: الشاة التي وضعت حديثا" (sihah); "الشاة الربي التي تحتبس في البيت للبن" (maqayis) — the newly delivered ewe.
- 1:2 رَبِّ — ر ب ب B002 — "التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام" (mufradat); "رب فلان ولده؛ رباه" (sihah) — rearing stage by stage.
- 1:2 رَبِّ — ر ب ب B005 — "الراب والرابة بأحد الزوجين إذا تولى تربية الولد" (mufradat) — the foster parent.
- 1:1 ٱللَّهِ (documented alternative و ل ه) — و ل ه B002, B001 — "التوليه أن يفرق بين المرأة وولدها" (maqayis;sihah); "لا تجعل والها وذلك في السبايا" (sihah); "ناقة واله إذا اشتد وجدها على ولدها" (sihah) — the mother parted from her young, among captives.

Quran and hadith:
- 17:23–24 — Allah's decree and the child's prayer: "وقضى ربك ألا تعبدوا إلا إياه وبالوالدين إحسانا ... وقل رب ارحمهما كما ربياني صغيرا".
- 3:6 — "هو الذي يصوركم في الأرحام كيف يشاء".
- 4:1 — "واتقوا الله الذي تساءلون به والأرحام".
- 28:7–13 — Mūsā's mother (scene opens 28:7 "وأوحينا إلى أم موسى"): 28:10 "وأصبح فؤاد أم موسى فارغا"; 28:13 "فرددناه إلى أمه كي تقر عينها".
- From memory, hadith: the captive woman who found her child, "لله أرحم بعباده من هذه بولدها" (Bukhārī); and "الرحم شجنة من الرحمن".

### Water: cloud, rain and plant above, the well below

Layered cloud stays and rains, and the first rain brands the earth with plants. A soft, moist south wind blows. Allah waters people and sets them right, and certain plants stay green through summer. Below is the full well with its crossbeam and pulley. Water carried keeps the traveller's affair going. Water let loose runs off and is lost. The dictionary joins غير and الله: "غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم" (maqayis). It joins the roots of المستقيم and أنعمت in one phrase: "القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة" (tahdhib).

- 1:1 بِسْمِ — س م و B004 — "العرب تسمى السحاب سماء والمطر سماء" ; "يسموا النبات سماء" (maqayis) — cloud, rain and plant all called "sky".
- 1:1 بِسْمِ (documented alternative و س م) — و س م B003 — "الوسمى أول المطر لأنه يسم الأرض بالنبات" (maqayis) — the first rain branding the ground with green.
- 1:2 رَبِّ — ر ب ب B008 — "الرباب: السحاب، سمي بذلك لأنه يرب النبات" (mufradat); "الربابة: السحابة التي قد ركب بعضها بعضا" (tahdhib) — layered cloud that rears the plants.
- 1:2 رَبِّ — ر ب ب B007 — "أربت السحابة: دامت" (mufradat) — the cloud that stays.
- 1:2 رَبِّ — ر ب ب B013 — "الربب وهو الماء الكثير سمي بذلك لاجتماعه" (maqayis) — gathered water.
- 1:2 رَبِّ — ر ب ب B012 — "اسم لعدة من النبات لا تهيج في الصيف" (tahdhib) — plants green through summer.
- 1:7 أَنْعَمْتَ — ن ع م B009 — "النعامى ريح الجنوب لأنها أبل الرياح وأرطبها" (sihah) — the moist south wind.
- 1:7 غَيْرِ — غ ي ر B001 — "غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم" (maqayis); "سقاهم" (sihah) — rain that sets people right.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B005 — "العيلم الركية الكثيرة الماء" (sihah) — the full well.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B012 — "القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة" (tahdhib) — the pulley hung from the crossbeam.
- 1:7 أَنْعَمْتَ — ن ع م B007 — "النعامة الخشبة المعترضة على الزرنوقين" (sihah) — the crossbeam over the well.
- 1:4 مَٰلِكِ — م ل ك B007 [fixed expression] — "والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره" (maqayis); "مياهنا ملوكنا" (tahdhib) — water that keeps a traveller's affair.
- 1:1 ٱللَّهِ (documented alternative و ل ه) — و ل ه B003 — "ماء موله وموله أرسل في الصحراء فذهب" (sihah) — the reversal: water let loose and lost.

Quran passages:
- 7:57 — "وهو الذي يرسل الرياح بشرا بين يدي رحمته حتى إذا أقلت سحابا ثقالا سقناه لبلد ميت".
- 30:48–50 — scene opens 30:48 "الله الذي يرسل الرياح فتثير سحابا"; 30:50 "فانظر إلى آثار رحمت الله كيف يحيي الأرض بعد موتها".
- 42:28 — "وهو الذي ينزل الغيث من بعد ما قنطوا وينشر رحمته وهو الولي الحميد". Rain, mercy and praise together.
- 28:23–24 — Mūsā at the water of Madyan (scene opens 28:23 "ولما ورد ماء مدين"). From memory, tradition: he lifted the stone from the well mouth.

### What keeps a thing standing

A thing stands by what holds it together: firmly kneaded dough, a wall's cohesion, the heart holding the body. The same holds for the mainstay of an affair and of a livelihood, a waterskin strengthened with syrup, a tarred ship, a tight knot, and palms left standing on their roots. The dictionary joins the roots of مالك and المستقيم: "قوام الأمر ملاكه" (sihah), "قوام الأمر وملاكه" (tahdhib). It defines قوام by استقام: "قوام كل شيء ما استقام به" (ayn).

- 1:4 مَٰلِكِ — م ل ك B001 — "أصل صحيح يدل على قوة في الشيء وصحة" (maqayis); "ملكت العجين إذا شددت عجنه" (sihah); "حائط ليس له ملاك أي تماسك" (mufradat) — dough kneaded firm; a wall that holds.
- 1:4 مَٰلِكِ — م ل ك B005 [fixed expression] — "القلب ملاك الجسد" (ayn;sihah;mufradat); "ملاك الأمر ما يعتمد عليه" (ayn) — the heart and the mainstay.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B009 — "قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه" (sihah); "القوام من العيش ما يقيمك ويغنيك" (ayn) — the pillar of an affair and of a livelihood.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B002 — "تركتموها قائمة على أصولها" (mufradat) — standing on its roots.
- 1:5 نَعْبُدُ — ع ب د B007 — "العبدة وهي القوة والصلابة" (maqayis); "ما لثوبك عبدة أي قوة" (sihah) — firmness of stuff.
- 1:5 نَعْبُدُ — ع ب د B005 — "المعبدة السفينة المقيرة" (sihah;tahdhib) — a ship made sound with tar.
- 1:2 رَبِّ — ر ب ب B006 — "رب فلان نحيه إذا جعل فيه الرب ومتنه به" (tahdhib); "سقاء مربوب إذا أصلح بالرب" (jamhara) — a skin strengthened with thick syrup.
- 1:2 رَبِّ — ر ب ب B016 — "الربى: العقدة المحكمة" (tahdhib) — the tight knot.
- 1:5 نَسْتَعِينُ — ع و ن B001 — "العون الظهيرة على الأمر" (sihah) — the prop behind the affair.

Quran passages:
- 18:77 — Mūsā and al-Khiḍr (scene opens 18:77 "فانطلقا حتى إذا أتيا أهل قرية"): "فوجدا فيها جدارا يريد أن ينقض فأقامه".
- 4:5 — "أموالكم التي جعل الله لكم قياما".
- 5:97 — "جعل الله الكعبة البيت الحرام قياما للناس والشهر الحرام والهدي والقلائد".
- 35:41 — "إن الله يمسك السماوات والأرض أن تزولا".

### Favour completed and praise returned

A benefactor extends a hand of good and completes it, then adds more. The receiver praises again and again, recounts the favours to others, and sends praise as a gift. Reversed, the giver counts his favour against the receiver. The chain runs from 1:2 الحمد to 1:7 أنعمت. The dictionary joins them: "أحمد إليك الله ... أشكر إليك أياديه ونعمه" (ayn;tahdhib). It joins رب and نعمة: "رب الرجل النعمة يربها ربا ... إذا تممها" (jamhara). Mufradat defines both رحمة and إنعام by إحسان.

- 1:7 أَنْعَمْتَ — ن ع م B001 — "النعمة اليد والصنيعة والمنة وما أنعم به عليك" (sihah); "والإنعام إيصال الإحسان إلى الغير" (mufradat) — the hand of good reaching another.
- 1:1, 1:3 — ر ح م B001 — "الرحمة رقة تقتضي الإحسان إلى المرحوم" (mufradat) — tenderness that issues in good done.
- 1:2 رَبِّ — ر ب ب B002 — "رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها" (jamhara); "رب فلان الصنيعة إذا أتمها وأصلحها" (tahdhib) — completing the favour.
- 1:2 رَبِّ — ر ب ب B016 — "الربى: النعمة والإحسان" (tahdhib) — favour itself.
- 1:7 أَنْعَمْتَ — ن ع م B010 — "فعل كذا وأنعم أي زاد" (sihah;mufradat) — adding more.
- 1:2 ٱلْحَمْدُ — ح م د B001 — "الحمد نقيض الذم" (maqayis;ayn;jamhara;sihah;tahdhib); "الحمد أعم من الشكر" (sihah;mufradat); "التحميد كثرة حمد الله بحسن المحامد" (ayn;tahdhib) — praise answering the favour.
- 1:2 ٱلْحَمْدُ — ح م د B006 [fixed expression] — "أحمد إليك الله أي معك" (ayn;tahdhib); "أشكر إليك أياديه ونعمه" (tahdhib) — recounting His favours to another.
- 1:7 أَنْعَمْتَ — ن ع م B003 — "نعم كلمة تستعمل في المدح بإزاء بئس" (mufradat) — a word of praise, like حمد set against blame.
- 1:2 ٱلْحَمْدُ — ح م د B003 — "محمد كأنه حمد مرة بعد أخرى" (jamhara) — praised time after time.
- 1:2 ٱلْحَمْدُ — ح م د B004 — "حماداك أي غايتك المحمودة" (mufradat) — the furthest praiseworthy limit.
- 1:6 ٱهْدِنَا — ه د ي B011, B004 — "الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا" (ayn); "الهدية ما أهديت إلى ذي مودة من بر" (ayn) — praise sent as a gift.
- 1:2 ٱلْحَمْدُ — ح م د B005 [fixed expression] — "فلان يتحمد علي أي يمن" (sihah) — the reversal: the giver who counts his favour.

Quran passages:
- 27:18–19 — Sulaymān in the valley of the ants (scene opens 27:18): "رب أوزعني أن أشكر نعمتك التي أنعمت علي وعلى والدي".
- 5:3 — "وأتممت عليكم نعمتي".
- 14:7 — Mūsā reminding his people: "لئن شكرتم لأزيدنكم".
- 93:11 — "وأما بنعمة ربك فحدث".
- 2:264 — the reversal: "لا تبطلوا صدقاتكم بالمن والأذى".

### The good ground where one stays

A traveller finds land good for dwelling and pasture. It suits him, so he stays and does not leave. A settled place, and a life soft and easy.

- 1:2 ٱلْحَمْدُ — ح م د B002 — "أحمدت الأرض إذا رضيت سكناها أو مرعاها" (jamhara;sihah) — finding the land good.
- 1:7 أَنْعَمْتَ — ن ع م B011 [fixed expression] — "أتيت أرضا فنعمتني أي وافقتني وأقمت بها" (tahdhib) — the land suits him and he stays.
- 1:7 أَنْعَمْتَ — ن ع م B002 — "نعمة العيش حسنه وغضارته" (tahdhib) — a soft life.
- 1:2 رَبِّ — ر ب ب B007 — "أرب فلان بالمكان إذا أقام به فلم يبرحه" (tahdhib); "مرب الإبل حيث لزمته" (sihah) — staying put.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B006 — "المقام والمقامة الموضع الذي تقيم فيه" (ayn;tahdhib) — the place of staying.

Quran passages:
- 35:34–35 — the people of the Garden: "وقالوا الحمد لله الذي أذهب عنا الحزن ... الذي أحلنا دار المقامة من فضله".
- 39:74 — the same speakers: "وقالوا الحمد لله الذي صدقنا وعده وأورثنا الأرض".
- 44:25–27 — the reversal, Pharaoh's people leaving it all behind: "كم تركوا من جنات وعيون وزروع ومقام كريم ونعمة كانوا فيها فاكهين".

### Led to its place: offering, bride, protected client

هدي is conveying something to where it belongs. The marked beast is led to the sanctuary at the appointed gathering and slaughtered with Allah's name spoken over it. The bride is conveyed to her husband under a contract. The stranger who comes seeking protection holds a sanctity like the offering's and is bound by covenant. The dictionary joins هدي and نعم: "الهدي ما يهدى إلى الحرم من النعم" (sihah). It joins the client to the offering: "الرجل الذي له حرمة كحرمة هدي البيت" (sihah). It joins the bride to the captive: "كالأسيرة عند زوجها" (tahdhib).

- 1:6 ٱهْدِنَا — ه د ي B005 — "الهدي ما يهدى إلى الحرم من النعم"; "حتى يبلغ الهدى محله" (sihah) — the beast led to its place.
- 1:7 أَنْعَمْتَ — ن ع م B005 — "النعم واحد الأنعام وهي المال الراعية" (sihah) — the livestock offered.
- 1:1 بِسْمِ (documented alternative و س م) — و س م B004, B001 — "موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه" (sihah); "الميسم المكواة أو الشيء الذي يوسم به الدواب" (ayn;sihah;tahdhib) — the appointed gathering and the marked beasts.
- 1:6 ٱهْدِنَا — ه د ي B006 — "أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها" (tahdhib) — the bride conveyed.
- 1:4 مَٰلِكِ — م ل ك B004 — "ملكت المرأة تزوجتها" (sihah); "الإملاك التزويج" (ayn) — the marriage contract.
- 1:6 ٱهْدِنَا — ه د ي B007 — "الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا" (tahdhib) — the client who seeks refuge.
- 1:2 رَبِّ — ر ب ب B011 — "الربابة: العهد والميثاق؛ الأربة أهل الميثاق" (sihah) — the covenant.
- 1:5 نَسْتَعِينُ — ع و ن B001 — "والاستعانة طلب العون" (mufradat) — the asking.

Quran passages:
- 22:34–36 — Allah on the rites (scene opens 22:34 "ولكل أمة جعلنا منسكا ليذكروا اسم الله على ما رزقهم من بهيمة الأنعام"); 22:36 "والبدن جعلناها لكم من شعائر الله ... فاذكروا اسم الله عليها صواف".
- 2:196 — "حتى يبلغ الهدي محله".
- 9:6 — "وإن أحد من المشركين استجارك فأجره حتى يسمع كلام الله ثم أبلغه مأمنه". The client conveyed to his place of safety.
- 4:21 — of wives: "وأخذن منكم ميثاقا غليظا".
- 7:172 — "ألست بربكم قالوا بلى".

### The Day: rising before the King

The day of the great event comes. Creation rises and stands before the ever-standing King who owns the day. Angels stand in ranks. Account and recompense follow. The dictionary quotes 1:4 itself: "الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء" (tahdhib). Mufradat quotes 83:6, which joins قوم with رب العالمين (1:2): "يوم يقوم الناس لرب العالمين".

- 1:4 يَوْمِ — ي و م B003 — "اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت" (ayn;tahdhib); "اليوم الشديد: يوم ذو أيام" (ayn;tahdhib) — the day of the great event.
- 1:4 ٱلدِّينِ — د ي ن B002 — "يوم الدين أي يوم الحكم والحساب والجزاء" (maqayis) — judgment, account and recompense.
- 1:4 مَٰلِكِ — م ل ك B003 — "الملكوت ملك الله وملكوت الله سلطانه" (ayn) — the kingship.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B013 — "القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم" (tahdhib); "يوم يقوم الناس لرب العالمين" (mufradat) — creation rising to its feet.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B004 — "القيوم القائم على كل شيء" (tahdhib) — the one standing over all things.
- 1:4 مَٰلِكِ — م ل ك B009 — "الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك" (tahdhib) — the angels.

Quran passages:
- 83:4–6 — Allah on the defrauders (scene opens 83:1 "ويل للمطففين"): "يوم يقوم الناس لرب العالمين".
- 82:17–19 — "وما أدراك ما يوم الدين ... يوم لا تملك نفس لنفس شيئا والأمر يومئذ لله".
- 40:16 — "لمن الملك اليوم لله الواحد القهار".
- 78:38 — "يوم يقوم الروح والملائكة صفا".
- 89:22 — "وجاء ربك والملك صفا صفا".
- From memory, hadith: the ṣirāṭ as a bridge set over Hell on that day.

### Debt, weight and blood-price

Debts fall due and are paid back. Goods are priced. A full-weight dinar does not tip the scale, and at noon the day's own balance stands level. Blood is answered by blood-price, or it is lost unavenged.

- 1:4 ٱلدِّينِ — د ي ن B003 — "الدين واحد الديون وتداينوا تبايعوا بالدين" (sihah); "دنت الرجل أقرضته" (tahdhib) — the debt.
- 1:4 ٱلدِّينِ — د ي ن B002 — "الدين الجزاء والمكافأة" (sihah) — repayment in kind.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B010 — "القيمة ثمن الشيء بالتقويم" (ayn;tahdhib) — the price.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B015 — "دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح" (tahdhib) — the full-weight coin.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B017 — "قام ميزان النهار فاعتدل" (tahdhib) — the level balance.
- 1:7 غَيْرِ — غ ي ر B002, B003 — "غارني الرجل إذا وداك من الدية والاسم الغِيرة" (sihah); "قود فغير إلى الدية" (maqayis); "غايرت الرجل أي عارضته بالبيع وبادلته" (sihah) — blood-price in place of retaliation; exchange.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — "ذهب دمه ضلة إذا لم يثأر به" (jamhara) — blood lost unanswered.

Quran passages:
- 2:282 — Allah to the believers: "إذا تداينتم بدين إلى أجل مسمى فاكتبوه ... أن تضل إحداهما فتذكر إحداهما الأخرى".
- 17:35 — "وأوفوا الكيل إذا كلتم وزنوا بالقسطاس المستقيم".
- 21:47 — "ونضع الموازين القسط ليوم القيامة".
- 2:178 — "فاتباع بالمعروف وأداء إليه بإحسان".
- 4:92 — "ودية مسلمة إلى أهله".

### The days of Allah: favour to some, anger on others

The days of Allah are remembered: favour on some peoples, punishment on others such as ʿĀd and Thamūd, and pardon on still others. 1:7 sorts past companies the same way: those favoured, those under anger, those astray. The road asked for is the road of the favoured. The dictionary joins أيام, الله and نعمة: "إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها" (mufradat).

- 1:4 يَوْمِ — ي و م B004 [fixed expression] — "وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين" (tahdhib); "أيامه: نعمه" (tahdhib) — the remembered days.
- 1:4 يَوْمِ — ي و م B002 — "مدة من الزمان أي مدة كانت" (mufradat) — an era.
- 1:7 أَنْعَمْتَ — ن ع م B001 — "نعمة الله منه وعطاؤه" (tahdhib) — favour on those who went before.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B001 — "وإذا وصف الله تعالى به فالمراد به الانتقام" (mufradat) — punishment.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B001 — "ضل الكافر غاب عن الحجة" (tahdhib) — the company that lost its way.
- 1:6 ٱهْدِنَا — ه د ي B002 — "هدى هدي فلان أي سار سيرته" (sihah) — walking the way of the favoured.

Quran and hadith:
- 14:5–6 — Mūsā sent to his people: "وذكرهم بأيام الله"; "اذكروا نعمة الله عليكم إذ أنجاكم من آل فرعون".
- 4:69 — scene opens "ومن يطع الله والرسول": "فأولئك مع الذين أنعم الله عليهم من النبيين والصديقين والشهداء والصالحين".
- 19:58 — "أولئك الذين أنعم الله عليهم من النبيين ... وممن هدينا واجتبينا".
- 2:61 — Banū Isrāʾīl (scene opens 2:61 "وإذ قلتم يا موسى لن نصبر"): "وباءوا بغضب من الله".
- 5:60 — "من لعنه الله وغضب عليه".
- 5:77 — "قد ضلوا من قبل".
- From memory, hadith (ʿAdī b. Ḥātim, Tirmidhī): المغضوب عليهم identified as the Jews, الضالين as the Christians.

### Soft and hard: mercy and ease against anger

Mercy is softness and tenderness. Ease is a soft life and a soft wind. Anger is the heart's blood boiling for vengeance. It is also hard piled rock, thick red skin, a frowning face, wounded pride with grief, and a husband's jealousy over his household. The surah sets الرحمن الرحيم (1:1, 1:3) against المغضوب (1:7), with غير standing beside it.

- 1:1, 1:3 — ر ح م B001 — "أصل واحد يدل على الرقة والعطف والرأفة" (maqayis) — thinness, softness, leaning toward.
- 1:7 أَنْعَمْتَ — ن ع م B002 — "نعم الشيء صار ناعما لينا" (sihah) — becoming soft.
- 1:7 أَنْعَمْتَ — ن ع م B009 — "النعامي الريح اللينة" (maqayis) — the soft wind.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B001 — "الغضب ثوران دم القلب إرادة الانتقام" (mufradat); "الغضب ضد الرضا" (jamhara); "الغضب لأنه اشتداد السخط" (maqayis) — the heart's blood boiling.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B004 — "الغضبة الصخرة الصلبة المتراكمة في الجبل" (ayn) — hard piled rock.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B005 — "رجل غضاب إذا كان غليظ الجلد؛ رجل غضب إذا كان أحمر غليظا" (jamhara) — thick, red skin.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B007 — "امرأة غضوب أي عبوس" (sihah) — the frowning face.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B003 — "مغاضبا أي مراغما لقومه" (sihah) — leaving one's people in anger.
- 1:5 نَعْبُدُ — ع ب د B008 — "العبد بالتحريك الغضب والأنف" (sihah); "والعبد الحزن والوجد" (tahdhib) — wounded pride and grief.
- 1:7 غَيْرِ — غ ي ر B004 — "الغَيرة بالفتح مصدر قولك غار الرجل على أهله" (sihah) — jealousy over one's household.

Quran and hadith:
- 3:159 — Allah to the Prophet after Uḥud: "فبما رحمة من الله لنت لهم ولو كنت فظا غليظ القلب لانفضوا من حولك".
- 2:74 — Banū Isrāʾīl after the cow: "ثم قست قلوبكم من بعد ذلك فهي كالحجارة أو أشد قسوة".
- 7:150–154 — Mūsā returning to the calf (scene opens 7:150 "ولما رجع موسى إلى قومه غضبان أسفا"):
  - 7:151 "رب اغفر لي ولأخي وأدخلنا في رحمتك وأنت أرحم الراحمين"
  - 7:152 "سينالهم غضب من ربهم"
  - 7:154 "ولما سكت عن موسى الغضب أخذ الألواح وفي نسختها هدى ورحمة"
- 21:87 — "وذا النون إذ ذهب مغاضبا".
- From memory, hadith: "إن رحمتي سبقت غضبي"; and "إن الله يغار".

### Going out of sight: swallowed, buried, dissolved

Food swallowed passes out of sight. By one derivation, whoever goes along the road passes out of view ahead. The dead are buried out of sight in the earth. Milk is lost in water, a thing is lost from memory, and a blade passes into the blow. Both roads of 1:6–1:7, the one asked for and the one fallen from, are defined in the dictionary by غيب:
- ص ر ط: "يدل على غيبة في مر وذهاب" (maqayis 1774).
- ض ل ل: "أصل الضلال الغيبوبة" (tahdhib).

- 1:6 ٱلصِّرَٰطَ — ص ر ط B002 — "أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب" (maqayis 1774) — swallowed out of sight.
- 1:6 ٱلصِّرَٰطَ, 1:7 صِرَٰطَ — ص ر ط B001 — "بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب" (maqayis 1774; reported as some scholars' view) — the walker passing from view along the road.
- 1:6 ٱلصِّرَٰطَ — ص ر ط B003 — "والسراط السيف القاطع الماضي في الضريبة" (maqayis 1774) — the blade going through.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B002 — "أصل الضلال الغيبوبة؛ ضل الماء في اللبن" (tahdhib); "أضل الميت إذا دفن" (maqayis;sihah); "أئذا ضللنا في الأرض أي خفينا وغبنا" (sihah) — buried in the earth, dissolved in milk.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — "ذهب فلان ضلة إذا لم يدر أين ذهب" (jamhara) — gone, no one knows where.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B004 [fixed expression] — "أن تضل إحداهما أي تغيب عن حفظها" (tahdhib) — gone from memory.
- 1:1 ٱللَّهِ (documented alternative و ل ه) — و ل ه B003 — "عين مولهة إذا أرسل ماؤها فذهب في الصحارى" (maqayis) — a spring's water run off into the desert.

Quran passages:
- 32:10–11 — the deniers' question and its answer: "وقالوا أإذا ضللنا في الأرض أإنا لفي خلق جديد ... قل يتوفاكم ملك الموت الذي وكل بكم ثم إلى ربكم ترجعون".
- 2:282 — "أن تضل إحداهما فتذكر إحداهما الأخرى".

## Interactions

- Road × Herd: ه د ي B003 (guide ahead / beast's neck) and ض ل ل B003, B005 (the lost camel) are shared. "الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها" (ayn) puts the stray off the road, away from its owner.
- Herd × Owner: رب is both the beast's owner ("رب الدار ورب الفرس") and the master of men ("السيد المطاع"). 12:39 "أأرباب متفرقون" joins lordship and scattering.
- Road × Mount: 28:21–24 stages both. Mūsā travels alone, asks "أن يهديني سواء السبيل", then asks for help.
- Road × Worship: ع ب د B005 "طريق معبد أي مذلل" is the trodden road and the humbling in one phrase. 36:61 and 19:36 "فاعبدوه هذا صراط مستقيم" join worship and the straight road.
- Road × Days of Allah: ه د ي B002 "سار سيرته" — the road asked for is the way of the favoured company of 1:7.
- Road × Going out of sight: both roads are defined by غيب (maqayis 1774 for صرط; tahdhib for ضلل).
- Sky × Road × Worship: 6:77 "لئن لم يهدني ربي لأكونن من القوم الضالين". Ibrāhīm speaks under the rising moon, and 41:37 adds "إياه تعبدون".
- Owner × Day: 82:19 "يوم لا تملك نفس لنفس شيئا والأمر يومئذ لله". مالك يوم الدين is quoted in tahdhib under دين B002.
- Owner × Debt: د ي ن carries subjection (B004) and debt (B003). "غير مدينين" is glossed both "غير مجزيين" (mufradat) and "غير مملوكين" (tahdhib).
- Day × Debt: 83:1–6 opens with the short-weighers and ends "يوم يقوم الناس لرب العالمين". 21:47 sets the scales "ليوم القيامة".
- Debt × Going out of sight: 2:282 holds "تداينتم بدين" and "أن تضل إحداهما" in one ayah.
- Name × Led to its place: 22:34–36 names Allah over the offered الأنعام. و س م B004 "لأنه معلم يجتمع إليه" joins the gathering to علم.
- Name × Worship: 19:65 "فاعبده ... هل تعلم له سميا" joins عبد, علم and سمي.
- Womb × Favour × Soft/hard: رحمة is "رقة" (maqayis) that "تقتضي الإحسان" (mufradat). إنعام is "إيصال الإحسان" and نعمة is "ناعما لينا".
- Womb × Owner × Worship: 17:23–24 holds "ألا تعبدوا إلا إياه", "رب ارحمهما" and "ربياني".
- Water × Favour × Soft/hard: 42:28 joins الغيث, رحمته and الحميد. ن ع م B009 is the soft south wind.
- Water × Standing: م ل ك B007 "الماء ملاك الأشياء" (tahdhib) — water as mainstay.
- Standing × Led to its place: 5:97 "قياما للناس ... والهدي والقلائد".
- Good ground × Favour: ح م د B002 and ن ع م B011 are twin phrases for finding a land good. 35:34–35 joins "الحمد لله" with "دار المقامة".
- Soft/hard × Days of Allah: 7:150–154 stages anger, mercy and "هدى ورحمة" in one scene. غضب "ضد الرضا" stands opposite the favoured company.
- Mount × Herd: the lost-mount hadith (from memory) has the traveller's camel escape in the desert and then be found.

## Ayat

**1:1** بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- Name: بسم is the name that makes known and raises; the brand (alternative وسم); "none rivals"; اسم joined to الله ("اسم الله الأكبر هو الله"). Scene: a name raises and makes known, a brand marks a beast, each kind of creation is a mark, the mark sets one thing apart, none bears His name as equal.
- Worship: الله is the one worshipped; the heart's yearning (alternative وله). Scene: the worshipped one is God because worshipped; the worshipper humbles himself like a trodden road and a tamed camel; obedience becomes habit.
- Sky: سماء overhead; the crescent lifting; الإلاهة, the sun some worshipped. Scene: under the sky the sun rises, sets and stands at noon, the crescent lifts, the moon passes its stations; who is Lord?
- Womb: رحمن/رحيم carry the womb, kin from one womb, the ailing mother; وله is the mother parted from her young. Scene: the womb grows the young, the ewe newly delivered or ailing, the child reared stage by stage, the bereft mother frantic.
- Water: سماء as cloud, rain and plant; الوسمي branding the ground; water let loose and lost (وله). Scene: layered cloud stays and rains, the first rain greens the earth, a soft south wind, the full well with crossbeam and pulley, water that keeps the traveller, water lost in the desert.
- Favour: رحمة is tenderness issuing in good done. Scene: a hand of good extended and completed, praise returned again and again; reversed, the giver who counts his favour.
- Soft/hard: رحمة as رقة. Scene: mercy soft and tender, ease soft; against it anger's boiling blood, hard rock, thick skin, frown, pride, jealousy.
- Led to its place: موسم, the gathering, and ميسم, the brand (alternative وسم). Scene: the marked beast led to the House under the Name at the gathering; the bride conveyed under contract; the client under covenant.
- Road: وله as the land that bewilders. Scene: the guide walks ahead on the one straight road past waymarks, along its trodden middle; off it paths scatter and the lost wanders bewildered.
- Going out of sight: وله as a spring's water run off. Scene: swallowed, buried, dissolved, forgotten; the walker passing from view along the road.

**1:2** ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- Favour: الحمد answers favour; recounting His favours; رب completes the favour. Scene: as above.
- Good ground: أحمدت الأرض; رب as staying put. Scene: a land found good for dwelling and pasture, stayed in, soft living.
- Owner: رب as owner and obeyed master. Scene: the owner-king holds and commands, the owned man is humbled, the city obeys; reversed, the one served.
- Herd: رب of the beast; ربرب, the gathered herd. Scene: the herd follows its lead beast on legs and neck under an owner; the stray wanders, owner unknown; companies scatter.
- Womb: ربى, the newly delivered ewe; rearing; foster parent. Scene: as above.
- Water: رباب cloud "يرب النبات"; lasting cloud; gathered water; العيلم well. Scene: as above.
- Standing: رب syrup strengthening a skin; the tight knot. Scene: a thing stands by dough kneaded firm, wall cohesion, heart, mainstay, tarred ship, knot.
- Name: العالمين as marks and signs; knowing. Scene: as above.
- Sky: العالم as the sphere and what it holds. Scene: as above.
- Road: علم as waymark and mountain. Scene: as above.
- Worship: لله, the one worshipped. Scene: as above.
- Led to its place: ربابة, the covenant. Scene: as above.
- Day: "يوم يقوم الناس لرب العالمين" (mufradat). Scene: the great day comes, creation rises before the ever-standing King, angels in ranks, account and recompense.

**1:3** ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- Womb: the repeated name returns to the womb, to kin from one womb, and to care for the weak, now standing between رب العالمين and مالك يوم الدين. Scene: the womb grows the young, the ewe newly delivered or ailing, the child reared stage by stage, the bereft mother frantic.
- Favour: tenderness that issues in good done ("رقة تقتضي الإحسان"). Scene: a hand of good extended and completed, praise returned again and again; reversed, the giver who counts his favour.
- Soft/hard: رقة, set in advance against المغضوب of 1:7. Scene: mercy soft and tender, ease soft; against it anger's boiling blood, hard rock, thick skin, frown, pride, jealousy.

**1:4** مَٰلِكِ يَوْمِ ٱلدِّينِ
- Day: يوم as the great event; الدين as judgment, account and recompense; مالك as kingship and the angels. Scene: the great day comes, creation rises before the ever-standing King, angels in ranks, account and recompense.
- Owner: ملك as possession and command; دين as subjection; المدينة where the ruler is obeyed. Scene: the owner-king holds and commands, the owned man is humbled, the city obeys; reversed, the one served.
- Worship: دين as yielding and obedience, and as habit. Scene: the worshipped one is God because worshipped; the worshipper humbles himself like a trodden road and a tamed camel; obedience becomes habit.
- Debt: دين as debt and repayment. Scene: debts fall due and are paid, goods priced, the full coin does not tip, the day's balance stands level; blood answered by blood-price or lost unavenged.
- Days of Allah: يوم as the remembered days of favour and punishment, and as an era. Scene: days of favour on some peoples, punishment on ʿĀd and Thamūd, pardon on others; the road asked for is the favoured one's.
- Road: ملك الطريق, the road's middle. Scene: the guide walks ahead on the one straight road past waymarks, along its trodden middle; off it paths scatter and the lost wanders bewildered.
- Herd: ملك as the lead beast, "ملك الدابة قوائمها وهاديها". Scene: the herd follows its lead beast on legs and neck under an owner; the stray wanders, owner unknown; companies scatter.
- Water: الماء ملك أمره. Scene: layered cloud stays and rains, the first rain greens the earth, a soft south wind, the full well with crossbeam and pulley, water that keeps the traveller, water lost in the desert.
- Standing: ملاك as cohesion; the heart as the body's ملاك. Scene: a thing stands by dough kneaded firm, wall cohesion, heart, mainstay, tarred ship, knot.
- Sky: يوم from sunrise to sunset. Scene: under the sky the sun rises, sets and stands at noon, the crescent lifts, the moon passes its stations; who is Lord?
- Led to its place: إملاك, the marriage contract. Scene: the marked beast led to the House under the Name at the gathering; the bride conveyed under contract; the client under covenant.

**1:5** إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- Worship: نعبد as the utmost lowering of oneself; the tamed camel and the trodden road. Tahdhib quotes this very ayah: "إياك نعبد إياك نطيع". Scene: the worshipped one is God because worshipped; the worshipper humbles himself like a trodden road and a tamed camel; obedience becomes habit.
- Owner: عبد as the owned man, the enslaved, Allah's servant, and the one served. Scene: the owner-king holds and commands, the owned man is humbled, the city obeys; reversed, the one served.
- Road: the trodden road (معبد); the scattered roads (عباديد). Scene: the guide walks ahead on the one straight road past waymarks, along its trodden middle; off it paths scatter and the lost wanders bewildered.
- Mount: أعبد به, stranded when the mount fails; نستعين, the backing one leans on. Scene: the mount tires and halts, the rider is stranded, walks leaning on two, asks for backing, is unloaded and set right, goes on calmly.
- Herd: عانة, the herd of wild asses. Scene: the herd follows its lead beast on legs and neck under an owner; the stray wanders, owner unknown; companies scatter.
- Standing: عبدة as firmness; the tarred ship; عون as the prop. Scene: a thing stands by dough kneaded firm, wall cohesion, heart, mainstay, tarred ship, knot.
- Soft/hard: عبد as anger, pride and grief. Scene: mercy soft and tender, ease soft; against it anger's boiling blood, hard rock, thick skin, frown, pride, jealousy.
- Led to its place: الاستعانة, the asking of one who seeks refuge. Scene: the marked beast led to the House under the Name at the gathering; the bride conveyed under contract; the client under covenant.

**1:6** ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- Road: هدي as making the road known, the guide ahead, walking another's way; صراط as the road; مستقيم as the level line. Mufradat joins the two words: "الصراط: الطريق المستقيم". Scene: the guide walks ahead on the one straight road past waymarks, along its trodden middle; off it paths scatter and the lost wanders bewildered.
- Mount: walking held up by two (يهادي); the mount halting (قامت دابته); the calm gait. Scene: the mount tires and halts, the rider is stranded, walks leaning on two, asks for backing, is unloaded and set right, goes on calmly.
- Herd: هوادي, the forward animals and the neck; قوائم, the legs. Scene: the herd follows its lead beast on legs and neck under an owner; the stray wanders, owner unknown; companies scatter.
- Led to its place: هدي as the offering, the bride, the protected client. Scene: the marked beast led to the House under the Name at the gathering; the bride conveyed under contract; the client under covenant.
- Standing: قوام as mainstay; standing on its roots. Scene: a thing stands by dough kneaded firm, wall cohesion, heart, mainstay, tarred ship, knot.
- Water: قامة, the pulley. Scene: layered cloud stays and rains, the first rain greens the earth, a soft south wind, the full well with crossbeam and pulley, water that keeps the traveller, water lost in the desert.
- Sky: قائم الظهيرة, the sun at its zenith. Scene: under the sky the sun rises, sets and stands at noon, the crescent lifts, the moon passes its stations; who is Lord?
- Day: القيامة and القيوم. Scene: the great day comes, creation rises before the ever-standing King, angels in ranks, account and recompense.
- Debt: قيمة, the price; the full-weight dinar; the level balance. Scene: debts fall due and are paid, goods priced, the full coin does not tip, the day's balance stands level; blood answered by blood-price or lost unavenged.
- Good ground: مقام, the place of staying. Scene: a land found good for dwelling and pasture, stayed in, soft living.
- Favour: إهداء, praise sent as a gift. Scene: a hand of good extended and completed, praise returned again and again; reversed, the giver who counts his favour.
- Going out of sight: سرط, swallowing; the walker passing from view on the road; the blade going through. Scene: swallowed, buried, dissolved, forgotten; the walker passing from view along the road.

**1:7** صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- Road: the road of those who went before; الضالين as those veered off, unable to find the house. Scene: the guide walks ahead on the one straight road past waymarks, along its trodden middle; off it paths scatter and the lost wanders bewildered.
- Days of Allah: the three companies — favoured, under anger, astray. Scene: days of favour on some peoples, punishment on ʿĀd and Thamūd, pardon on others; the road asked for is the favoured one's.
- Favour: أنعمت as the hand of good; أنعم as adding more; نعم as a word of praise. Scene: a hand of good extended and completed, praise returned again and again; reversed, the giver who counts his favour.
- Soft/hard: نعمة as softness; المغضوب as boiling blood, rock, thick skin, frown; غيرة as jealousy. Scene: mercy soft and tender, ease soft; against it anger's boiling blood, hard rock, thick skin, frown, pride, jealousy.
- Herd: النعم, the camels; الضالة, the stray with owner unknown; شالت نعامتهم, the company scattering. Scene: the herd follows its lead beast on legs and neck under an owner; the stray wanders, owner unknown; companies scatter.
- Mount: غير as unloading the saddle and setting right. Scene: the mount tires and halts, the rider is stranded, walks leaning on two, asks for backing, is unloaded and set right, goes on calmly.
- Water: غارهم الله بالغيث; النعامى, the south wind; النعامة, the well's crossbeam. Scene: layered cloud stays and rains, the first rain greens the earth, a soft south wind, the full well with crossbeam and pulley, water that keeps the traveller, water lost in the desert.
- Sky: النعائم, a station of the moon. Scene: under the sky the sun rises, sets and stands at noon, the crescent lifts, the moon passes its stations; who is Lord?
- Good ground: نعّمتني, the land suits me and I stay; نعمة العيش. Scene: a land found good for dwelling and pasture, stayed in, soft living.
- Led to its place: النعم, the offered livestock. Scene: the marked beast led to the House under the Name at the gathering; the bride conveyed under contract; the client under covenant.
- Debt: غيرة, the blood-price, and exchange; ضلة, blood lost unanswered. Scene: debts fall due and are paid, goods priced, the full coin does not tip, the day's balance stands level; blood answered by blood-price or lost unavenged.
- Name: غير as the other, set apart by its mark. Scene: a name raises and makes known, a brand marks a beast, each kind of creation is a mark, the mark sets one thing apart, none bears His name as equal.
- Going out of sight: ضلال as غيبوبة — buried, dissolved in milk, gone no one knows where, forgotten. Scene: swallowed, buried, dissolved, forgotten; the walker passing from view along the road.

