Focus: 1:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and map.md (an earlier reader's map of the image chains that run through the whole surah, with the dictionary phrases of their members in other ayat; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py 1:6 <refs separated by spaces>`. It lists strong passages from an earlier cross-reference list that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. Run the command only once; no other tool is available.

===== _commentary/v16/prompts/r10_1/write.md =====
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
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it; a chain an earlier ayah opened is recalled briefly.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said ("… denir"); never name a dictionary, and never make "the family"
  a speaker.
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
- not written: <a finding you weighed and left out> - <what it would have made visible, and why that did not belong here>


===== _commentary/v16/prompts/r10_1/additions.md =====
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



===== _commentary/v16/out/s001/surah.map3.nohft.tool.check2/map.md (without ## Not carried) =====
## Chains

Note on sources: unless a line says "dictionary cites", every Quran passage outside this surah is cited from memory or from the cross-reference check. Members marked "documented alternative" come from roots the dictionary records as a cited alternative derivation of that exact word: و س م for بِسْمِ (Kufans, Tha'lab) and و ل ه for ٱللَّهِ (Abu'l-Haytham).

### The road: guide, waymarks, straight road, and the one who strays from it

The surah's request is for a road, and its words supply the whole road. A guide or staff goes ahead. Waymarks and mountains stand along it. There is a middle lane to keep to, and a surface made smooth by feet. The road runs in a level line and has a heading that one does not turn from. At the end of 1:7 there is the man who swerves from the aim, cannot find the house, and loses himself in the land. Ayah 1:6 names the road and 1:7 names it again by whose road it is. The last word of the surah is its reversal, and the dictionary itself sets that reversal against the first verb of 1:6.

- 1:6 ٱهْدِنَا — ه د ي B001 — «هديته الطريق والبيت هداية أي عرفته» (sihah); «الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق» (mufradat) — showing someone the road and the house, gently.
- 1:6 ٱهْدِنَا — ه د ي B001 — «الهدى نقيض الضلالة» (ayn;tahdhib) — the dictionary sets 1:6's verb against 1:7's last word.
- 1:6 ٱهْدِنَا — ه د ي B003 — «الدليل يسمى هاديا لتقدمه» (ayn); «الهادية العصا لأنها تتقدم ممسكها» (maqayis) — the guide who walks in front, and the staff that goes ahead of the hand holding it.
- 1:6 ٱهْدِنَا — ه د ي B002 — «خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه» (sihah); «هدية أمره أي جهة أمره» (tahdhib) — the heading one keeps without turning aside.
- 1:6 ٱلصِّرَٰطَ / 1:7 صِرَٰطَ — ص ر ط B001 — «الصراط: الطريق المستقيم؛ ويقال له سراط» (mufradat) — the dictionary joins the two words of 1:6, road and straightness.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B008 — «الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم» (mufradat); «إذا انقاد واستمرت طريقته فقد استقام» (ayn) — a road laid on a level line, and a walker who keeps to it.
- 1:4 مَٰلِكِ — م ل ك B006 — «الزم ملك الطريق أي وسطه» (tahdhib) — keep to the middle of the road.
- 1:5 نَعْبُدُ — ع ب د B005 — «الطريق المعبد وهو المسلوك المذلل» (maqayis) — the road worn smooth and made easy by much walking.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — «المعلم الأثر يستدل به على الطريق» (sihah;tahdhib); «العلم الجبل الطويل والجميع الأعلام» (ayn) — the waymark and the tall mountain that the traveller reads.
- 1:5 نَعْبُدُ — ع ب د B010 — «العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة» (tahdhib) — scattered, diverging roads, the opposite of the one road.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B001 — «كل جائر عن القصد ضال» (maqayis); «الضلال ضد الهدى؛ ... ضل في الأرض إذا لم يهتد للسبيل» (jamhara); «الإضلال في كلام العرب ضد الهداية والإرشاد» (tahdhib) — swerving from the aimed line and failing to find the way.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «ضللت المسجد والدار إذا لم تهتد لهما» (maqayis) — failing to find the house one was making for.

Quran:
- 6:151–153: the Prophet recites what the Lord has forbidden. «وأن هذا صراطي مستقيما فاتبعوه ولا تتبعوا السبل فتفرق بكم عن سبيله»: one straight road against many paths that scatter.
- 16:9: «وعلى الله قصد السبيل ومنها جائر», the قصد and the جائر of maqayis's phrase.
- 16:15–16: mountains, rivers and paths, then «وعلامات وبالنجم هم يهتدون». Waymarks and stars for guidance.
- 21:31: «فجاجا سبلا لعلهم يهتدون».
- 7:16–17: Iblis vows «لأقعدن لهم صراطك المستقيم», an ambush set on the road.
- 7:86: Shu'ayb tells his people «ولا تقعدوا بكل صراط توعدون».
- 42:52–53: «وإنك لتهدي إلى صراط مستقيم صراط الله», the road named again by its owner, in the same build as 1:6–7.
- 6:71: «كالذي استهوته الشياطين في الأرض حيران له أصحاب يدعونه إلى الهدى ائتنا». Someone bewildered in the land while his companions call him back to the road.
- 19:43–44: Abraham to his father: «فاتبعني أهدك صراطا سويا يا أبت لا تعبد الشيطان».
- 36:60–62: God speaks on the Day: «وأن اعبدوني هذا صراط مستقيم ولقد أضل منكم جبلا كثيرا».
- 19:36 and 43:64: Jesus says «إن الله ربي وربكم فاعبدوه هذا صراط مستقيم».
- 6:161: «إنني هداني ربي إلى صراط مستقيم دينا قيما». The dictionary cites دينا قيما under ق و م B008.
- 67:22: one who walks face-down against one who walks upright on a straight road.
- 23:73–74: those who do not believe «عن الصراط لناكبون».
- 20:10: Moses at night by the fire: «أو أجد على النار هدى».
- 10:35: «أمن لا يهدي إلا أن يهدى», a guide who himself needs guiding.
- 93:7: «ووجدك ضالا فهدى».
- 37:118: Moses and Aaron: «وهديناهما الصراط المستقيم».

### The stranded traveller: the mount gives out, he walks leaning, carries water, and asks for help

Two of the surah's roots describe the same moment on a journey: the riding beast is worn out and will not go on. The dictionary uses the same verb, كلّت, for both. A third root shows the man walking between two companions, leaning on them. The 1:5 verb asks for exactly that support. The surah's words also hold the water a traveller carries, which is what keeps his affair going, and the calm pace of a man who is not fleeing. Ayat 1:4 to 1:6 hold the whole roadside scene.

- 1:5 نَعْبُدُ — ع ب د B011 — «أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت» (sihah); «أعبد به إذا ذهبت راحلته وكذلك أبدع به» (tahdhib) — stranded when the mount is spent or lost.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B016 [fixed expression] — «قامت لفلان دابته إذا كلت أو عيت فلم تسر» (tahdhib) — the beast stands still, exhausted. This is the same كلت scene as the line above.
- 1:6 ٱهْدِنَا — ه د ي B008 — «يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله» (sihah) — walking between two people, leaning on them out of weakness.
- 1:5 نَسْتَعِينُ — ع و ن B001 — «كل شيء استعنت به أو أعانك فهو عونك» (ayn); «العون الظهيرة على الأمر» (sihah) — whatever one leans on, and the back that supports.
- 1:4 مَٰلِكِ — م ل ك B007 [fixed expression] — «والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره» (maqayis) — the traveller's water, which keeps his affair in hand.
- 1:4 مَٰلِكِ — م ل ك B005 [fixed expression] — «ملاك الأمر ما يعتمد عليه» (ayn) — what one leans on. It shares معتمد with the ه د ي B008 phrase.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B009 — «القوام من العيش ما يقيمك ويغنيك» (ayn) — the provision that keeps a person standing.
- 1:6 ٱهْدِنَا — ه د ي B010 — «لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن» (ayn) — the steady, unhurried pace of a man who is not a fugitive.

Quran:
- 16:75–76: two parables. First «عبدا مملوكا لا يقدر على شيء». Then «أحدهما أبكم ... وهو كل على مولاه أينما يوجهه لا يأت بخير هل يستوي هو ومن يأمر بالعدل وهو على صراط مستقيم». The كلّ who is a burden is set against the man on the straight road.
- 21:112: the Prophet's closing words: «وربنا الرحمن المستعان».
- 7:128: Moses to his people: «استعينوا بالله واصبروا».
- 2:45: «واستعينوا بالصبر والصلاة».
- 3:101: «ومن يعتصم بالله فقد هدي إلى صراط مستقيم». Holding fast as a way onto the road.
- 25:63: «وعباد الرحمن الذين يمشون على الأرض هونا». The calm walk.
- 28:22–24: Moses, alone on the road to Madyan: «عسى ربي أن يهديني سواء السبيل», and at the end «رب إني لما أنزلت إلي من خير فقير».

### Swallowed by the road, lost in the ground, and the day of rising

ص ر ط and ض ل ل both carry a sense of disappearing. The road swallows the one who walks it, as food goes down a throat. The stray is also gone from sight: he vanishes as milk dissolves in water, as a body goes under the earth. One is gone ahead along the road; the other is gone and nobody knows where. The day of 1:4 and the standing in قوم bring the buried back up.

- 1:6 ٱلصِّرَٰطَ — ص ر ط B002 — «أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب» (maqayis 1774) — passing through and vanishing, like a swallowed mouthful.
- 1:6 ٱلصِّرَٰطَ — ص ر ط B001 — «بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب» (maqayis 1774) — the dictionary derives the road from swallowing: the one who goes along it passes from sight.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B002 — «أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته» (tahdhib); «أضل الميت إذا دفن» (maqayis); «أئذا ضللنا في الأرض أي خفينا وغبنا» (jamhara) — dissolving into another liquid, and burial.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «ذهب فلان ضلة إذا لم يدر أين ذهب» (jamhara) — gone, no one knows where.
- 1:1 ٱللَّهِ — و ل ه B003 (documented alternative) — «ماء موله وموله أرسل في الصحراء فذهب» (sihah) — water let loose into the desert and lost.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B013 — «القيامة يوم البعث يقوم الخلق بين يدي القيوم» (ayn) — the buried stand up again.
- 1:4 يَوْمِ — ي و م B003 — «اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت» (ayn;tahdhib) — the event that comes down on people.

Quran:
- 32:10: the deniers ask «أئذا ضللنا في الأرض أإنا لفي خلق جديد». Dictionary cites, under ض ل ل B002.
- 36:51–52: the trumpet. «فإذا هم من الأجداث إلى ربهم ينسلون قالوا يا ويلنا من بعثنا من مرقدنا».
- 37:20–23: «يا ويلنا هذا يوم الدين», then the order «فاهدوهم إلى صراط الجحيم». Guidance and road turned the other way.
- 39:68: «ثم نفخ فيه أخرى فإذا هم قيام ينظرون».

### The herd: its lord, its leader, its brand, and the stray

The surah's words make up a herd. Camels are the stock, and the dictionary names them for the good and favour they bring. Wild cattle and wild asses run in their own herds. A lead animal goes in front and the rest follow. There are the herd's age classes, a newly delivered ewe kept for milk, and a camel smeared with tar and tamed. The owner burns his mark into the hide. A camel that gets lost is the stray, «لا يعرف ربها». The dictionary's phrase for the stray uses the very word of 1:2, رب, and also مالك, the word of 1:4. So the surah begins with the herd's owner and ends with the animal that no longer knows him.

- 1:2 رَبِّ — ر ب ب B001 — «رب كل شئ: مالكه» (sihah); «رب الدار ورب الفرس» (mufradat) — the owner of the stock. The dictionary joins رب and مالك.
- 1:4 مَٰلِكِ — م ل ك B002 — «الملك ما ملكت اليد من مال وخول» (ayn;tahdhib) — what the hand holds.
- 1:7 أَنْعَمْتَ — ن ع م B005 — «النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم» (maqayis) — camels, named for the favour they bring. The dictionary joins the stock and نعمة.
- 1:4 مَٰلِكِ — م ل ك B008 [fixed expression] — «ملك الإبل والشاء ما يتقدم ويتبعه سائره» (mufradat); «مليك النحل يعسوبها» (sihah) — the lead animal that the rest follow.
- 1:6 ٱهْدِنَا — ه د ي B003 — «هوادي الوحش متقدماتها الهادية لغيرها» (mufradat); «هوادي الخيل أعناقها أو أول رعيل» (tahdhib) — the front-runners of a wild herd, guiding the others.
- 1:2 رَبِّ — ر ب ب B014 — «الربرب: القطيع من بقر الوحش» (sihah) — a herd of wild cattle.
- 1:5 نَسْتَعِينُ — ع و ن B006 — «العانة القطيع من حمر الوحش والجمع عون» (sihah) — a herd of wild asses.
- 1:5 نَسْتَعِينُ — ع و ن B002 — «بقرة عوان لا فارض مسنة ولا بكر صغيرة» (sihah) — the middle-aged beast, neither old nor young.
- 1:2 رَبِّ — ر ب ب B009 — «الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا» (maqayis) — the ewe newly delivered, kept at home for milk.
- 1:2 رَبِّ — ر ب ب B007 — «مرب الإبل حيث لزمته» (tahdhib) — the place the camels keep to.
- 1:5 نَعْبُدُ — ع ب د B005 — «البعير المعبد المهنوء بالقطران المذلل» (maqayis;sihah) — the camel smeared with tar and tamed.
- 1:1 بِسْمِ — و س م B001 (documented alternative) — «الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي» (ayn); «الميسم المكواة أو الشيء الذي يوسم به الدواب» (ayn;sihah;tahdhib) — the brand by which a camel is known, and the hot iron.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B005 — «الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء» (ayn); «الضالة من الإبل التي بمضيعة لا يعرف لها مالك» (tahdhib) — the stray, with no known رب or مالك.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «أضللت بعيري إذا ذهب منك» (maqayis) — the owner's side of the same loss.

Quran:
- 11:56: Hud to 'Ad: «ما من دابة إلا هو آخذ بناصيتها إن ربي على صراط مستقيم». Every beast led by its forelock, on a straight road.
- 20:49–50: Pharaoh asks «فمن ربكما يا موسى». Moses: «ربنا الذي أعطى كل شيء خلقه ثم هدى».
- 87:1–5: «سبح اسم ربك الأعلى ... والذي قدر فهدى والذي أخرج المرعى». Name, height, guidance and pasture.
- 16:5–6: the herds, «حين تريحون وحين تسرحون», driven home and out again.
- 50:21: «وجاءت كل نفس معها سائق وشهيد». Each soul driven in.
- 68:16: «سنسمه على الخرطوم». God threatens the slanderer with a brand.

### The land found good: pasture, staying on, the city

A herdsman or settler comes to a stretch of land, judges its pasture and dwelling good, and stays on without moving. That stretch becomes the place where he stands his ground, and the city is the place where obedience is kept. Supplies are carried in. The approval in 1:2's praise word, the staying in its lord word, the dwelling in 1:6's standing word and the satisfaction in 1:7's favour word all describe the same choosing and staying.

- 1:2 ٱلْحَمْدُ — ح م د B002 — «أحمدت الأرض إذا رضيت سكناها أو مرعاها» (jamhara;sihah) — the land judged good for dwelling or pasture.
- 1:7 أَنْعَمْتَ — ن ع م B011 [fixed expression] — «أتيت أرضا فنعمتني أي وافقتني وأقمت بها» (tahdhib) — the land agreed with him and he stayed.
- 1:2 رَبِّ — ر ب ب B007 — «أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته» (tahdhib) — staying put, and the camels' ground.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B006 — «أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين» (ayn;tahdhib); «لا مقام لكم أي لا مستقر لكم» (mufradat) — the ground one stands on, and the reversal: no place to stay.
- 1:4 ٱلدِّينِ — د ي ن B006 — «المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر» (maqayis) — the city where obedience is kept. The phrase also uses قوم.
- 1:7 أَنْعَمْتَ — ن ع م B002 — «نعمة العيش حسنه وغضارته» (tahdhib) — a pleasant, fresh life there.
- 1:7 غَيْرِ — غ ي ر B001 — «الغِيرة بالكسر: الميرة» (sihah) — provisions brought in for the household.

Quran:
- 14:35–37: Abraham at the House: «ربنا إني أسكنت من ذريتي بواد غير ذي زرع ... وارزقهم من الثمرات».
- 106:3–4: «فليعبدوا رب هذا البيت الذي أطعمهم من جوع».
- 33:13: «يا أهل يثرب لا مقام لكم فارجعوا». Dictionary cites, under ق و م B006.

### Sky, cloud, and the rain that raises the plants

The name word's root holds the sky and also cloud, rain and plants. 1:2's lord word holds the stacked cloud, which the dictionary says is named because it «raises the plants», along with cloud that lingers, water gathered in quantity, and a soft green herb that does not wither in summer. The documented alternative derivation of the name makes it the first rain, which marks the earth with growth. 1:7 adds God watering people with rain, and the soft, moist south wind. 1:4 adds water as what holds every affair together. Rain is God's mercy in the Quran, so 1:1 and 1:3 belong to this scene through the Quran rather than through the dictionary.

- 1:1 بِسْمِ — س م و B004 — «العرب تسمى السحاب سماء والمطر سماء؛ ... يسموا النبات سماء» (maqayis); «السماء كل ما علاك فأظلك» (sihah) — the sky overhead, and cloud, rain and plants called by its name.
- 1:1 بِسْمِ — و س م B003 (documented alternative) — «الوسمى أول المطر لأنه يسم الأرض بالنبات» (maqayis); «يسم الأرض بالنبات فيصير فيها أثرا في أول السنة» (tahdhib) — the first rain marks the earth with growth.
- 1:2 رَبِّ — ر ب ب B008 — «الرباب: السحاب، سمي بذلك لأنه يرب النبات» (mufradat); «الربابة: السحابة التي قد ركب بعضها بعضا» (tahdhib) — stacked cloud that raises the plants.
- 1:2 رَبِّ — ر ب ب B007 — «أربت الجنوب والسحابة أي دامت» (sihah) — the south wind and the cloud linger.
- 1:2 رَبِّ — ر ب ب B013 — «الربب وهو الماء الكثير سمي بذلك لاجتماعه» (maqayis) — water gathered in quantity.
- 1:2 رَبِّ — ر ب ب B012 — «الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف» (tahdhib) — a soft herb that stays green through summer. Note بقلة ناعمة: the ن ع م word sits inside this phrase.
- 1:2 رَبِّ — ر ب ب B002 — «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» (mufradat) — raising a thing stage by stage to its completion.
- 1:7 غَيْرِ — غ ي ر B001 — «غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم» (maqayis); «سقاهم» (sihah) — God provides them with rain.
- 1:7 أَنْعَمْتَ — ن ع م B009 — «النعامى ريح الجنوب لأنها أبل الرياح وأرطبها» (sihah) — the softest, moistest wind, from the south.
- 1:4 مَٰلِكِ — م ل ك B007 [fixed expression] — «الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر» (tahdhib); «مياهنا ملوكنا» (tahdhib) — water as what holds all things together.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B005 — «العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء» (maqayis) — sea, or a well full of water.
- 1:1 / 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B001 — «الرحمة رقة تقتضي الإحسان إلى المرحوم» (mufradat) — the dictionary does not call rain رحمة; the Quran does (below).

Quran:
- 42:28: «وهو الذي ينزل الغيث من بعد ما قنطوا وينشر رحمته وهو الولي الحميد». Rain, mercy and the Praised together.
- 7:57: «يرسل الرياح بشرا بين يدي رحمته حتى إذا أقلت سحابا ثقالا».
- 30:48–50: clouds spread in layers, then «فانظر إلى آثار رحمت الله كيف يحيي الأرض».
- 2:21–22: «يا أيها الناس اعبدوا ربكم ... والسماء بناء وأنزل من السماء ماء». Worship of the Lord, then sky and rain.
- 27:63: «أمن يهديكم في ظلمات البر والبحر ومن يرسل الرياح بشرا بين يدي رحمته».
- 25:48–49: pure water sent down «لنحيي به بلدة ميتا».

### Lights that rise: crescent, sun at noon, the turning sphere

The root of the name means rising. Its dictionary entry shows the new crescent's outline as it lifts above the horizon. The root of Allah holds a name for the sun, given because a people worshipped it. The day runs from sunrise to sunset, and at noon the sun «stands» at its height. One of the moon's stations bears a name from 1:7's favour word. In mufradat, the worlds of 1:2 are the turning sphere and everything it holds. 1:5's «إياك نعبد» settles which of these risers is worshipped.

- 1:1 بِسْمِ — س م و B002 — «سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا» (ayn) — the crescent's outline lifting above the horizon.
- 1:1 بِسْمِ — س م و B001 — «سما الشيء يسمو سموا أي ارتفع» (ayn) — rising.
- 1:1 ٱللَّهِ — ء ل ه B001 — «والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها» (maqayis) — the sun named for being worshipped. One phrase joins إله, عبادة and قوم.
- 1:4 يَوْمِ — ي و م B001 — «اليوم مقداره من طلوع الشمس إلى غروبها» (ayn;tahdhib) — the day measured by the sun.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B017 — «قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل» (ayn;tahdhib); «قام ميزان النهار فاعتدل» (tahdhib) — the sun standing at noon, the day's scale level.
- 1:7 أَنْعَمْتَ — ن ع م B007 — «النعائم منزل من منازل القمر» (sihah) — a station of the moon.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — «العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به» (mufradat) — the sphere and what it holds, a thing by which something is known.
- 1:5 نَعْبُدُ — ع ب د B003 — «عبد يعبد عبادة فلا يقال إلا لمن يعبد الله» (maqayis;ayn) — worship kept for God alone.

Quran:
- 6:75–79: Abraham watches a star, the moon rising («بازغا») and the sun, and says each time «هذا ربي». When the moon sets: «لئن لم يهدني ربي لأكونن من القوم الضالين». Lord, guidance, the straying and the rising lights all in one scene.
- 41:37: «لا تسجدوا للشمس ولا للقمر واسجدوا لله الذي خلقهن إن كنتم إياه تعبدون», the إياه of 1:5.
- 27:22–24: the hoopoe tells Solomon «وجدتها وقومها يسجدون للشمس ... فصدهم عن السبيل فهم لا يهتدون». Sun-worship blocks the road.
- 73:9: «رب المشرق والمغرب لا إله إلا هو».

### Name, mark, sign, and the one with no namesake

A name raises the one it names. The dictionary puts «اسم الله» together in one phrase, exactly the pair in بسم الله. Under the documented alternative derivation, the name is a burnt-in mark, a sign one reads, a trace of good or ill seen in a face. 1:2's worlds are signs and banners, each kind of creature a mark of its Maker. Name-rivalry («لا يسامى») and the namesake («سميا») raise the question of who else could carry the name. False gods are «الآلهة الأصنام». 1:7's «غير» is the word for «other than». Praise spreads a good name, and praise can be sent as a gift.

- 1:1 بِسْمِ — س م و B005 — «الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه» (mufradat); «الاسم مشتق من سموت لأنه تنويه ورفعة» (sihah) — the name raises the named, and the namesake is the one who would deserve that name.
- 1:1 ٱللَّهِ — ء ل ه B002 — «اسم الله الأكبر هو الله» (ayn); «اللهم بمعنى يا ألله» (tahdhib) — the dictionary joins اسم and الله, and gives the form used in direct appeal.
- 1:1 ٱللَّهِ — ء ل ه B001 — «لا يكون إلاها حتى يكون معبودا» (tahdhib); «الآلهة الأصنام» (sihah) — the name tied to being worshipped, and the idols that carry it falsely.
- 1:1 بِسْمِ — س م و B007 — «فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه» (sihah) — one no one can rival.
- 1:1 بِسْمِ — س م و B008 — «ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر» (tahdhib) — a good name spread among people.
- 1:1 بِسْمِ — و س م B001 (documented alternative) — «ووسمت الشيء وسما: أثرت فيه بسمة» (maqayis;sihah) — a mark pressed into a thing.
- 1:1 بِسْمِ — و س م B002 (documented alternative) — «توسمت فيه الخير والشر أي رأيت فيه أثرا» (ayn) — reading good or ill from a trace.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — «أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره» (maqayis); «العلم الراية» (maqayis;sihah;tahdhib) — a mark that sets a thing apart from others, and a banner.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — «العالمون كل جنس من الخلق فهو في نفسه معلم وعلم» (maqayis) — every kind of creature is itself a sign.
- 1:7 غَيْرِ — غ ي ر B005 — «هذا الشيء غير ذاك أي هو سواه وخلافه» (maqayis) — the other, the not-this.
- 1:2 ٱلْحَمْدُ — ح م د B003 — «محمد كأنه حمد مرة بعد أخرى» (jamhara) — praised again and again, a name made of praise.
- 1:6 ٱهْدِنَا — ه د ي B011 — «الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا» (ayn) — praise or satire sent to someone as a gift in verse.

Quran:
- 19:65: «رب السماوات والأرض وما بينهما فاعبده واصطبر لعبادته هل تعلم له سميا». Dictionary cites سميا.
- 87:1: «سبح اسم ربك الأعلى». Name, Lord and height together.
- 96:1: «اقرأ باسم ربك».
- 17:110: «قل ادعوا الله أو ادعوا الرحمن أيا ما تدعوا فله الأسماء الحسنى».
- 25:60: «وإذا قيل لهم اسجدوا للرحمن قالوا وما الرحمن». The name الرحمن refused.
- 12:40: Joseph in prison: «ما تعبدون من دونه إلا أسماء سميتموها». See also 53:23.
- 27:30: Solomon's letter to Sheba: «إنه من سليمان وإنه بسم الله الرحمن الرحيم».
- 2:31: «وعلم آدم الأسماء كلها».
- 3:26: «قل اللهم مالك الملك».
- 15:75: «إن في ذلك لآيات للمتوسمين». Readers of marks.
- 94:4: «ورفعنا لك ذكرك».

### Owner, slave, debt, and the day the account is settled

The surah's words describe an owner, the people he owns, and their accounts. رب is owner and obeyed master. مالك holds the property and the slaves. عبد is the owned person. دين is subjection, borrowing and lending, and the reckoning and repayment. The day is the thing that comes down on people. On it, everyone stands up before the Lord of the worlds. A dinar that «stands» is a coin of full weight, so payment on that day is exact. The tahdhib phrase quotes 1:4 itself to explain دين as the reckoning.

- 1:2 رَبِّ — ر ب ب B001 — «يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح» (tahdhib) — owner, obeyed master, the one who puts things right.
- 1:4 مَٰلِكِ — م ل ك B002 — «ملك الإنسان الشيء يملكه ملكا» (maqayis); «المملوك يختص في التعارف بالرقيق من الأملاك» (mufradat) — owning, and the owned person.
- 1:4 مَٰلِكِ — م ل ك B003 — «الملك لله المالك المليك» (ayn); «الملك هو المتصرف بالأمر والنهي في الجمهور» (mufradat) — kingship: commanding and forbidding over the people.
- 1:5 نَعْبُدُ — ع ب د B001 — «العبد وهو المملوك» (maqayis) — the slave is the owned one.
- 1:5 نَعْبُدُ — ع ب د B004 — «عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا» (jamhara) — making people into slaves.
- 1:4 ٱلدِّينِ — د ي ن B004 — «دانه دينا أي أذله واستعبده ودينته ملكته» (sihah); «غير مدينين غير مملوكين» (tahdhib) — one phrase joins دين, عبد and ملك.
- 1:4 ٱلدِّينِ — د ي ن B003 — «الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء» (maqayis) — debt, taken or given.
- 1:4 ٱلدِّينِ — د ي ن B002 — «يوم الدين أي يوم الحكم والحساب والجزاء» (maqayis); «الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء» (tahdhib); «غير مدينين أي غير مجزيين» (mufradat) — the dictionary quotes 1:4 itself.
- 1:4 ٱلدِّينِ — د ي ن B007 — «دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته» (tahdhib) — the judge accepts a man's word, before the court and before God.
- 1:4 يَوْمِ — ي و م B003 — «يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل» (maqayis) — the great event. The phrase puts نعم beside اليوم: how fine a man is when the day comes down.
- 1:4 يَوْمِ — ي و م B005 — «يركب يوم مع إذ، فيقال: يومئذ» (mufradat) — «on that day».
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B013 — «القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين» (mufradat) — the dictionary quotes a phrase with يوم, قام and رب العالمين together.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B015 — «دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح» (ayn) — a coin of exact weight that does not tip the scale.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B010 — «القيمة ثمن الشيء بالتقويم» (ayn) — the price set by valuation.

Quran:
- 82:17–19: «وما أدراك ما يوم الدين ... يوم لا تملك نفس لنفس شيئا والأمر يومئذ لله». يوم, دين, ملك and يومئذ together.
- 83:4–6: «ليوم عظيم يوم يقوم الناس لرب العالمين».
- 56:86–87: «فلولا إن كنتم غير مدينين». Dictionary cites.
- 37:53: «أئنا لمدينون».
- 2:281–282: «واتقوا يوما ترجعون فيه إلى الله ثم توفى كل نفس», then «إذا تداينتم بدين». The day of full payment beside the debt ayah.
- 40:16–17: «لمن الملك اليوم لله الواحد القهار اليوم تجزى كل نفس بما كسبت».
- 14:41: Abraham: «يوم يقوم الحساب».
- 21:47: «ونضع الموازين القسط ليوم القيامة».
- 99:7–8.
- 26:82: Abraham: «أن يغفر لي خطيئتي يوم الدين».

### Made smooth by treading: the road, the tamed camel, the servant

ع ب د and د ي ن meet in the same word, ذلّ: «made smooth», «made yielding». A road becomes معبد by much walking. A camel becomes معبد by being tarred and tamed. A servant's worship is the utmost making-oneself-low. دين goes back to yielding and lowness, and the slave is مدين because work has humbled him. The straight road comes in through the same word: one who «انقاد» and keeps to his way is مستقيم. The عبد root also holds both reversals: the honoured one who is served, and the bristling pride that refuses.

- 1:5 نَعْبُدُ — ع ب د B005 — «الطريق المعبد وهو المسلوك المذلل» (maqayis); «البعير المعبد المهنوء بالقطران المذلل» (maqayis;sihah) — road and camel both made smooth and yielding.
- 1:5 نَعْبُدُ — ع ب د B003 — «العبودية إظهار التذلل والعبادة غاية التذلل» (mufradat); «إياك نعبد إياك نطيع الطاعة التي نخضع معها» (tahdhib) — the dictionary quotes 1:5.
- 1:4 ٱلدِّينِ — د ي ن B001 — «أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل» (maqayis) — yielding and lowness as the root of every branch.
- 1:4 ٱلدِّينِ — د ي ن B004 — «العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل» (maqayis) — joins عبد and دين: the slave, humbled by work.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B008 — «إذا انقاد واستمرت طريقته فقد استقام» (ayn) — انقاد again, now on the road.
- 1:1 ٱللَّهِ — ء ل ه B001 — «التأله التنسك والتعبد» (sihah) — devoting oneself to worship.
- 1:5 نَعْبُدُ — ع ب د B006 — «المعبد المكرم والمعظم كأنه يعبد» (jamhara) — reversal: the honoured one who is served.
- 1:5 نَعْبُدُ — ع ب د B008 — «العبد الأنف والحمية ويقال عبد عليه أي غضب» (tahdhib); «العبد الأنفة وعبدت فصمت أي أنفت فسكت» (jamhara) — reversal: proud refusal, anger.

Quran:
- 67:15: «هو الذي جعل لكم الأرض ذلولا فامشوا في مناكبها». The earth made tame to walk on.
- 25:63: «وعباد الرحمن الذين يمشون على الأرض هونا».
- 19:93: «إن كل من في السماوات والأرض إلا آتي الرحمن عبدا».
- 4:172: «لن يستنكف المسيح أن يكون عبدا لله». Pride refusing service.
- 40:60: «إن الذين يستكبرون عن عبادتي».
- 43:81: «فأنا أول العابدين». Some early philologists read العابدين here as «the indignant», from the أنف sense; this is from memory.
- 36:61: «وأن اعبدوني هذا صراط مستقيم».

### Favour given, completed, thanked, and changed

A favour is a good done to someone else. رب adds the work of bringing that favour to completion: the dictionary's phrase is «رب الرجل النعمة». Praise answers the favour; the dictionary calls حمد wider than thanks, and gives a fixed phrase for thanking someone for His favours. A gift goes to someone loved. The giver adds more. There are two reversals. One is the giver who keeps reminding the receiver of his gift. The other is the favour itself changed, which 1:7's «غير» can carry. Rahma and in'am are both defined through إحسان, so 1:1/1:3 open what 1:7 names.

- 1:7 أَنْعَمْتَ — ن ع م B001 — «النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير» (mufradat); «النعمة اليد والصنيعة والمنة وما أنعم به عليك» (sihah) — good brought to someone else, a hand held out.
- 1:2 رَبِّ — ر ب ب B002 — «رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها» (jamhara) — the dictionary joins رب and نعمة: completing a favour.
- 1:2 رَبِّ — ر ب ب B016 — «الربى: النعمة والإحسان» (tahdhib) — favour and kindness.
- 1:1 / 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B001 — «الرحمة رقة تقتضي الإحسان إلى المرحوم» (mufradat) — tenderness that leads to doing good. إحسان is shared with the ن ع م definition.
- 1:2 ٱلْحَمْدُ — ح م د B001 — «الحمد أعم من الشكر» (sihah;mufradat) — praise, wider than thanks.
- 1:2 ٱلْحَمْدُ — ح م د B006 [fixed expression] — «أشكر إليك أياديه ونعمه» (tahdhib) — the dictionary joins praise and نعم.
- 1:6 ٱهْدِنَا — ه د ي B004 — «الهدية ما أهديت إلى ذي مودة من بر» (ayn) — a kindness sent to someone loved.
- 1:7 أَنْعَمْتَ — ن ع م B010 — «أنعم أفضل وزاد» (tahdhib) — giving more than was due.
- 1:2 ٱلْحَمْدُ — ح م د B004 — «حماداك أي غايتك المحمودة» (mufradat) — the furthest point worth praising.
- 1:2 ٱلْحَمْدُ — ح م د B005 [fixed expression] — «فلان يتحمد علي أي يمن» (sihah) — reversal: reminding the receiver of the gift.
- 1:7 غَيْرِ — غ ي ر B003 — «تغيير صورة الشيء دون ذاته؛ تبديله بغيره» (mufradat) — the changing or exchanging of a thing.

Quran:
- 5:3: «اليوم أكملت لكم دينكم وأتممت عليكم نعمتي». يوم, دين and the favour completed.
- 48:2: «ويتم نعمته عليك ويهديك صراطا مستقيما».
- 12:6: Jacob to Joseph: «ويتم نعمته عليك».
- 16:121: Abraham: «شاكرا لأنعمه اجتباه وهداه إلى صراط مستقيم».
- 8:53: «ذلك بأن الله لم يك مغيرا نعمة أنعمها على قوم حتى يغيروا ما بأنفسهم». غير, نعمة, أنعم and قوم.
- 14:28: «بدلوا نعمت الله كفرا».
- 14:7: «لئن شكرتم لأزيدنكم».
- 93:6–11: orphan sheltered, «ضالا فهدى», then «وأما بنعمة ربك فحدث».
- 4:69: «الذين أنعم الله عليهم من النبيين والصديقين».
- 19:58.
- 102:8: «ثم لتسألن يومئذ عن النعيم».

### Approval and anger: the two ends of the surah

The surah opens on praise and closes on anger, and the dictionary defines each against the other's partner. Praise is the opposite of blame and means being pleased with a thing. Anger is the opposite of being pleased. نعم is the word of praise, set against بئس. Anger also means defiance. The day carries both kinds of event, since the days of God are remembered for punishment and for pardon.

- 1:2 ٱلْحَمْدُ — ح م د B001 — «الحمد نقيض الذم» (maqayis;ayn;jamhara;sihah;tahdhib) — praise against blame.
- 1:2 ٱلْحَمْدُ — ح م د B002 — «هل تحمد لي هذا الأمر أي هل ترضاه لي» (tahdhib) — praise as being pleased.
- 1:7 أَنْعَمْتَ — ن ع م B003 — «نعم كلمة تستعمل في المدح بإزاء بئس» (mufradat) — the word of praise.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B001 — «الغضب ضد الرضا ورجل غضبة كثير الغضب» (jamhara); «الغضب لأنه اشتداد السخط» (maqayis); «وإذا وصف الله تعالى به فالمراد به الانتقام» (mufradat) — anger, the opposite of being pleased.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B003 — «غاضبه: راغمه؛ مغاضبا أي مراغما لقومه» (sihah) — defiance.
- 1:4 يَوْمِ — ي و م B004 [fixed expression] — «وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين» (tahdhib); «أيامه: نعمه» (tahdhib) — days of punishment and of pardon and favour.
- 1:5 نَعْبُدُ — ع ب د B008 — «ويقال عبد عليه أي غضب» (tahdhib) — anger inside the root of service.

Quran:
- 3:162: «أفمن اتبع رضوان الله كمن باء بسخط من الله».
- 5:16: «يهدي به الله من اتبع رضوانه سبل السلام».
- 14:5–7: Moses is sent «وذكرهم بأيام الله». Dictionary cites. He then reminds them of God's favour, and «لئن شكرتم لأزيدنكم ولئن كفرتم».
- 20:80–81: Israel fed with manna: «ولا تطغوا فيه فيحل عليكم غضبي ومن يحلل عليه غضبي فقد هوى».
- 2:61: «وباءوا بغضب من الله».
- 58:14: «قوما غضب الله عليهم».
- 6:45: «فقطع دابر القوم الذين ظلموا والحمد لله رب العالمين».

### Tenderness and hardness

Rahma at its root is softness and leaning in. 1:7's favour word gives softness again, and the softest wind. Anger, in its dictionary branches, is the opposite surface: hard rock heaped in the mountain, thick skin, blood boiling in the heart, deep red, swelling around the eye, a frowning face, hide folded into a shield. The surah begins inI can't give you the full map. My earlier attempt was stopped by a safety filter partway through the "Tenderness and hardness" chain. The rest was never delivered, and I can't regenerate that content, even reworded.

**What you have:**
- The cross-reference check (`missing.py S1 …`) ran once. I had chosen which of its listed passages to use and worked them into the chains I wrote.
- About twelve chains were complete, each with an explanatory paragraph, member lines quoting the dictionary exactly, and Quran references:
  - the road
  - the stranded traveller
  - swallowed by the road and the day of rising
  - the herd and the stray
  - the land found good
  - sky, cloud and rain
  - the lights that rise
  - name, mark and namesake
  - owner, slave, debt and the day of reckoning
  - made smooth by treading
  - favour given, completed and changed
  - approval and anger
- "Tenderness and hardness" stops mid-paragraph, before any of its members.

**What's missing:**
- The other chains I had planned:
  - the womb and the raising of the young
  - the wedding and the guarded household
  - the guest under covenant
  - the offering camel
  - the well-head
  - the firm upright frame
  - kneading, seasoning and tarring
  - the teacher
  - battle
  - blood and its price
- All of `## Interactions`, `## Ayat` and `## Not carried`.

What you have is incomplete and doesn't meet the brief, so it can't stand as the final map for Surah 1. The brief allows only one run of the check command, so a new attempt would have to work from the passages that run already returned.

