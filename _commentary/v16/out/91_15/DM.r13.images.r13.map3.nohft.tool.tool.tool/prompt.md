Focus: 91:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
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
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
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
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/91_15/D.r13/context.md =====
# 91:15 — focus

وَلَا يَخَافُ عُقْبَٰهَا

Anchor translation (canonical reading, reference only):

O, bunun sonucundan korkmaz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَلَا | لَا |  | CONJ;NEG |
| 2 | يَخَافُ | خَافَ | خ و ف | V |
| 3 | عُقْبَٰهَا | عُقْبَى | ع ق ب | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 ◀ focus وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## خ و ف (root_000447) — identity root of يَخَافُ (w2)

- **B001** bir belirtiye dayanarak kötü bir şey bekleme korkusu — korku · korkmak · korku hali · korku halleri · korku ve sakınma · korkan kimse · çok korkan adam · korkan topluluk · korkan topluluk · kork! · onun başına bir şey gelmesinden korkmak
  الخوف ضد الأمن خاف يخاف خوفا (jamhara خفو)؛ والخيفة مثل الخوف والجمع خيف (jamhara خيف)؛ خاف الرجل يخاف خوفا وخيفة ومخافة فهو خائف؛ والخيفة الخوف والجمع خيف وأصله الواو (sihah)؛ الخوف توقع مكروه عن أمارة مظنونة أو معلومة ويضاد الخوف الأمن (mufradat)؛ أصل واحد يدل على الذعر والفزع؛ خفت الشيء خوفا وخيفة (maqayis 992)؛ الخيف فجمع خيفة وليس من هذا الباب وقد ذكر في باب الواو بعد الخاء (maqayis 1001)؛ الخيفة الخوف (ayn)
- **B002** korku doğurma ya da korkulur kılma — korkutma veya korkuyla sakındırma · başkasını korkutma · korkutucu · korkulan veya tehlikeli · insanların korktuğu tehlikeli yol · Tanrı'nın korku uyandırarak sakındırması
  ومنه التخويف والإخافة؛ طريق مخوف يخافه الناس ومخيف يخيف الناس؛ خوفت الرجل جعلت فيه الخوف؛ خوفت الرجل أي صيرته بحال يخافه الناس (ayn)؛ الإخافة التخويف؛ وجع مخيف أي يخيف من رآه؛ طريق مخوف لأنه لا يخيف وإنما يخيف فيه قاطع الطريق (sihah)؛ التخويف من الله تعالى هو الحث على التحرز؛ ذلك يخوف الله به عباده؛ الشيطان يخوف أولياءه (mufradat)
- **B003** korkuda yarışıp ötekinden daha çok korkma — korkuda yarışıp ötekinden daha çok korkmak
  خاوفه فخافه يخوفه غلبه بالخوف أي كان أشد خوفا منه (sihah)؛ خاوفني فلان فخفته أي كنت أشد خوفا منه (maqayis)
- **B004** bir şeyden alarak eksiltme — bir şeyi eksiltip ondan bir bölüm almak
  والتخوف التنقص (ayn)؛ وتخوفه أي تنقصه (sihah)؛ تخوفناهم أي تنقصناهم تنقصا اقتضاه الخوف منه (mufradat)؛ تخوفت الشيء أي تنقصته فهو الصحيح الفصيح إلا أنه من الإبدال والأصل النون من التنقص (maqayis)
- **B005** korkunun kişide dışa vurması — korkunun kişide dışa vurması
  والتخوف ظهور الخوف من الإنسان (mufradat)
- **B006** arıcı ya da su taşıyıcısının deri torbası veya üstlüğü — arıcı veya su taşıyıcısının deri torbası, kabı ya da üstlüğü · aynı eşyanın küçük biçimi
  الخافة تصغيرها خويفة واشتقاقها من الخوف وهي جبة يلبسها العسال والسقاء والخافة العيبة (ayn)؛ الخافة خريطة من أدم يشتار فيها العسل (sihah)

## ع ق ب (root_001033) — identity root of عُقْبَٰهَا (w3)

- **B001** bağlama ve kiriş yapımında kullanılan sert beyaz tendon — kiriş yapılan sert beyaz tendon · ayak bileklerinin arkasındaki gergin tendon · oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak
  العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)
- **B002** topuk ve hemen arkasında kalan iz — topuk, ayağın arka bölümü · topuklar · ardınca çok kişi yürüyen, çok izlenen · birinin hemen ardından, onun izinden
  العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)
- **B003** dönüp geri çekilmek [kalıp] — dönüp geri çekilmek · geri dönmedi, arkasına bakmadı veya beklemedi
  ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)
- **B004** ardında kalan çocuklar ve torunlar — kişinin ardından kalan çocukları ve torunları · ardında çocuk veya soy bırakmadı
  عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)
- **B005** birbirinin ardından gelme ve yerini alma — öncekinin ardından gelen ve onun yerini alan · ardıl, bir başkasının ardından gelen · gece ile gündüzün sırayla birbirinin yerini alması · sırayla nöbet değiştiren gece ve gündüz görevlileri · binme veya çalışma sırası, nöbet
  كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)
- **B006** sonuç ve varılan son durum — son, sonuç, varılan nihai durum · karşılık veya sonuç; kimi kullanımda iyi karşılık · buna yol açtı, ardından bunu doğurdu
  أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)
- **B007** suçtan sonra verilen kötü karşılık — ceza, cezalandırma · onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz
  عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)
- **B008** ardından izleyip yeniden inceleme — hak istemek veya itiraz etmek için ardından izleyen kişi · onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur · haberi veya işi yeniden dönüp araştırmak
  المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)
- **B009** aynı tür işi yeniden yapma — aynı tür işi yeniden yapma · atın bir koşudan sonra yeniden ve daha iyi koşması · bir otlak türünden ötekine dönüşümlü geçen deve sürüsü · kuşun yükselişiyle alçalışı arasındaki hareket evresi · ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü
  التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)
- **B010** bedel, satış başvurusu ve elde tutma güvencesi — tutsağın veya bir şeyin yerine alınan bedel · satılan maldan doğan başvuru hakkı ve sorumluluk · malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur
  أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)
- **B011** geride kalan son parça ya da iz — ağır hastalıktan kalan belirti · kapta kalan son yemek suyu · soyluluk ve güzellikten kişide kalan görünür iz
  العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)
- **B012** sarp dağ geçidi ve kayalık çıkıntı — dik ve zorlu dağ yolu veya geçidi · kuyu ya da dağ yüzündeki dışarı taşan kaya
  العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)
- **B013** kartal ve ona benzetilen büyük sancak — kartal, güçlü yırtıcı kuş · kartala benzetilen büyük sancak veya bayrak · korkunç ve ağır bela
  العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)
- **B014** özel adlandırma kümesi — erkek kişi adı · erkek keklik ve ona benzetilen at
  يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)
- **B015** bitkinin sararıp kurumaya yaklaşması [kalıp] — bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak
  عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:15, and ## Buluşmalar) =====
## Gökte el değiştiren ışık: açılan ve örtülen yüz

Arapçada kelimelerin çoğu üç harfli bir kökten türer. Aynı kökten gelen kelimeler birbirinden çok farklı şeylere ad olabilir, ama aralarında ortak bir sahne taşırlar. Aşağıda bir kelimenin ailesinden getirilen her imge, o kelimenin ayetteki anlamının yanında duyulur. İmge bu anlamın yerine geçmez.

Surenin ilk dört ayeti dört ayrı şeye yemin ediyor gibi görünür: güneş, ay, gündüz, gece. Oysa dört ayetin de sonundaki "-hâ" zamiri hep aynı yere döner, yani güneşe. Birinci ayet güneşi kendi ışığıyla anar: {ar:وَٱلشَّمْسِ وَضُحَىٰهَا, tr:ve'ş-şemsi ve duhâhâ, gloss:güneşe ve kuşluğuna andolsun, source:91:1}. Güneş hem bir disktir hem de o diskten yayılan aydınlık: {ar:الشمس يقال للقرصة وللضوء المنتشر عنها, tr:eş-şemsu yukâlu li'l-kursati ve li'd-dav'i'l-munteşiri anhâ, gloss:güneş hem diske hem de ondan yayılan ışığa denir, source:"ش م س,B001"}. Kuşluk da o ışığın açılıp yayılmasıdır: {ar:الضحى انبساط الشمس وامتداد النهار, tr:ed-duhâ inbisâtu'ş-şemsi ve'mtidâdu'n-nehâr, gloss:kuşluk, güneşin yayılması ve gündüzün uzamasıdır, source:"ض ح و,B001"}. Bu yayılma ölçülü basamaklarla sayılır: {ar:ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء, tr:dahvetu'n-nehâri ba'de tulû'i'ş-şems, summe ba'dehu'd-duhâ, summe ba'dehu'd-dahâ', gloss:güneş doğduktan sonra önce dahve, sonra duhâ, sonra dahâ gelir, source:"ض ح و,B001"}. Kısacası ilk ayette güneş kendi aydınlığını yayan bir kaynak olarak durur.

İkinci ayet ayı kendi ışığıyla değil, sırasıyla tanımlar: {ar:وَٱلْقَمَرِ إِذَا تَلَىٰهَا, tr:ve'l-kameri izâ telâhâ, gloss:onu izlediğinde aya andolsun, source:91:2}. Fiil bir peşinden gelmeyi anlatır: {ar:تلاه تبعه متابعة, tr:telâhu tebi'ahu mutâba'aten, gloss:onu izledi, ardı sıra peşinden gitti, source:"ت ل و,B001"}. Üçüncü ayette ilişki ters döner: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Gündüz, güneşin ışığından başka bir şey değildir: {ar:النهار ضياء ما بين طلوع الفجر إلى غروب الشمس, tr:en-nehâru diyâun mâ beyne tulû'i'l-fecri ilâ gurûbi'ş-şems, gloss:gündüz, tan yerinin ağarmasından güneşin batışına kadarki aydınlıktır, source:"ن ه ر,B002"}. Yine de güneşi görünür kılan, güneşten gelen bu aydınlıktır. Fiilin kökü örtünün kalkıp şeyin ortaya çıkmasını anlatır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey'i ve burûzuhu, gloss:bir şeyin örtüsünün açılması ve ortaya çıkması, source:"ج ل و,B001"}. Arap dili bu ayeti de tam böyle okur: {ar:والنهار إذا جلاها إذا بين الشمس, tr:ve'n-nehâri izâ cellâhâ: izâ beyyene'ş-şemse, gloss:"gündüz onu açığa çıkardığında", yani güneşi belirgin kıldığında, source:"ج ل و,B007"}. Dördüncü ayette gece aynı yüzü kapatır: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰهَا, tr:ve'l-leyli izâ yağşâhâ, gloss:onu örttüğünde geceye andolsun, source:91:4}. Kökün işi bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullu alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam bir kök, source:"غ ش و,B001"}.

Düz bir anlatım "güneşe, aya, gündüze ve geceye andolsun" der ve geçer. Fiiller ise tek bir yüzün dört türlü ele alındığını gösterir: yayılır, izlenir, açılır, örtülür. Kur'an bu düzeni başka yerlerde de sahneler. Yâsîn Suresi'nde Allah işaretlerini sayarken hiçbir cismin sırasını bozmadığını söyler: {ar:لَا ٱلشَّمْسُ يَنۢبَغِى لَهَآ أَن تُدْرِكَ ٱلْقَمَرَ وَلَا ٱلَّيْلُ سَابِقُ ٱلنَّهَارِ, tr:le'ş-şemsu yenbağî lehâ en tudrike'l-kamera ve le'l-leylu sâbiku'n-nehâr, gloss:ne güneşin aya yetişmesi yaraşır ne de gece gündüzü geçebilir, source:36:40}. Göklerle yeri altı günde yaratan Rabbi anlatan ayette örtme işi bir kovalamacaya dönüşür: {ar:يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا, tr:yuğşi'l-leyle'n-nehâra yatlubuhu hasîsâ, gloss:geceyi, onu hızla kovalayan gündüzün üstüne örter, source:7:54}. Hemen ardından gelen sure aynı çifti iki yeminle açar: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye andolsun, source:92:1} ve {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp parladığında gündüze andolsun, source:92:2}. Nâziât Suresi'nde Allah, dirilişi inkâr edenlere yaratılmalarının mı daha zor olduğunu, yoksa göğün mü olduğunu sorar. Orada kuşluk, gecenin içinden çıkarılan bir şey gibi anlatılır: {ar:وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا, tr:ve ağtaşe leylehâ ve ahrace duhâhâ, gloss:gecesini karanlık kıldı, kuşluğunu çıkardı, source:79:29}.

Bu gök sahnesi dördüncü ayette bitmez. Surenin sonraki kelimeleri aynı gökten anlamlar taşır. Yedinci ayetteki "nefs" kelimesinin kökü sabahın nefes almasını da adlandırır: {ar:تنفس الصبح أي تبلج وتنفس النهار إذا زاد, tr:teneffese's-subhu ey teballece, ve teneffese'n-nehâru izâ zâde, gloss:sabah nefes aldı, yani ağardı; gündüz nefes aldı, yani uzadı, source:"ن ف س,B009"}. Kur'an aynı fiili bir yeminde kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. Yine yedinci ayetteki "sevvâhâ" fiilinin ailesinde ayın tamamlandığı gece vardır: {ar:السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر, tr:es-sevâ'u memdûdun, leyletu selâse aşrate ve fîhâ yestevi'l-kamer, gloss:sevâ', ayın on üçüncü gecesidir; o gece ay dolgunlaşır, source:"س و ي,B012"}. Kur'an da dolunaya yemin eder: {ar:وَٱلْقَمَرِ إِذَا ٱتَّسَقَ, tr:ve'l-kameri izâ't-tesak, gloss:dolunay olduğunda aya andolsun, source:84:18}. Altıncı ayetteki "tahâhâ" fiili de yükselmiş, ışığı yayılmış ayı adlandırır: {ar:القمر الطاحي أي المرتفع والطاحي أيضا المنبسط, tr:el-kameru't-tâhî, eyi'l-murtefi', ve't-tâhî eyzan el-munbesit, gloss:tâhî ay, yükselmiş ay demektir; tâhî yayılmış anlamına da gelir, source:"ط ح و,B008"}. Sekizinci ayetteki "fucûr" kelimesinin kökü şafağın adıdır: {ar:الفجر حمرة الشمس في سواد الليل وهما فجران, tr:el-fecru humretu'ş-şemsi fî sevâdi'l-leyl, ve humâ fecrân, gloss:fecr, gecenin karasındaki güneş kızıllığıdır; iki fecr vardır, source:"ف ج ر,B002"}. Şafak bu adı geceyi yardığı için alır: {ar:قيل للصبح فجر لكونه فجر الليل, tr:kîle li's-subhi fecrun li-kevnihî fecera'l-leyl, gloss:sabaha fecr denmesi, geceyi yarmış olmasındandır, source:"ف ج ر,B002"}. Kur'an Allah'ı bu yarışın sahibi olarak anar: {ar:فَالِقُ ٱلْإِصْبَاحِ, tr:fâliku'l-isbâh, gloss:sabahı yarıp çıkaran, source:6:96}. On beşinci ayetteki "ukbâhâ" kelimesinin ailesinde ise gece ile gündüzün nöbetleşmesi vardır: {ar:الليل والنهار يتعاقبان, tr:el-leylu ve'n-nehâru yeteâkabân, gloss:gece ile gündüz birbirini izler, source:"ع ق ب,B005"}. Kur'an bu nöbeti şöyle anlatır: {ar:جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ, tr:ce'ale'l-leyle ve'n-nehâra hilfeten, gloss:geceyi ve gündüzü birbirinin ardınca gelen kıldı, source:25:62}. Böylece sure, gökte başlayan nöbetin sözcükleri içinde ilerler ve yine bir "ardınca gelme" kelimesiyle kapanır.

Açma ve örtme işi gökte kalmaz. Kuşluk kelimesinin kendisi de açıkta durmayı anlatır: {ar:ضحا الطريق إذا بدا وظهر, tr:dahâ't-tarîku izâ bedâ ve zahara, gloss:yol göründüğünde ve ortaya çıktığında "dahâ" denir, source:"ض ح و,B002"}; {ar:فعل ذلك ضاحية أي ظاهرا بينا, tr:fe'ale zâlike dâhiyeten, ey zâhiren beyyinen, gloss:bunu dâhiye olarak yaptı, yani açıkça, göz önünde yaptı, source:"ض ح و,B002"}. Gecenin örtüsü de kalbe taşınır: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâvetu mâ ğaşiye'l-kalbe min rayni't-tab', gloss:ğışâve, kalbi kaplayan mühür pasıdır, source:"غ ش و,B001"}. Kur'an inkârcılar için aynı kelimeyi kullanır: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:ve alâ ebsârihim ğışâvetun, gloss:gözlerinin üstünde bir perde vardır, source:2:7}.

Sekizinci ayette bu iki iş nefsin içine yerleşir: {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona hem yoldan çıkışını hem korunuşunu ilham etti, source:91:8}. Fucûr, şafağın geceyi yardığı kökten gelir. Ama burada yarılan şey karanlık değil, bir perdedir: {ar:الفجور شق ستر الديانة, tr:el-fucûru şakku sitri'd-diyâne, gloss:fucûr, din perdesini yırtmaktır, source:"ف ج ر,B004"}. Gökte yarılma ışık getirir; nefiste ise koruyucu örtüyü parçalar. Takvâ bunun karşısında yerinde tutulan bir örtüdür: {ar:كل ما وقى شيئا فهو وقاء له ووقاية, tr:kullu mâ vakâ şey'en fe-huve vikâun lehu ve vikâye, gloss:bir şeyi koruyan her şey onun için vikâ ve vikâyedir, source:"و ق ي,B001"}. Kökün en somut örneği, dış örtü ile saç arasında duran ince bezdir: {ar:وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها, tr:vikâyetu'l-mer'e, ve hiye'l-hırkatu'lletî beyne cilbâbihâ ve şa'rihâ, gloss:kadının vikâyesi, cilbabı ile saçı arasındaki bez parçasıdır, source:"و ق ي,B001"}. Böylece surede iki tür örtü ve iki tür açılış belirir. Gecenin örtüsü düzenin parçasıdır, takvânın örtüsü korur. Gündüzün açması gösterir, fucûrun açması yırtar.

Dokuzuncu ve onuncu ayetler bu çifti nefsin kaderine bağlar: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad efleha men zekkâhâ, gloss:onu arındırıp büyüten kurtuluşa ermiştir, source:91:9}; {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp gizleyen eli boş kalmıştır, source:91:10}. İkinci fiil gizlemektir: {ar:دساها أي أخفاها, tr:dessâhâ, ey ahfâhâ, gloss:dessâhâ, onu gizledi demektir, source:"د س و,B001"}. Gizleme burada kişinin kendine yöneliktir: {ar:دس فلان نفسه إذا أخفاها وأخملها, tr:dessâ fulânun nefsehu izâ ahfâhâ ve ahmelehâ, gloss:biri kendini gizleyip adını sönük bıraktığında bu fiil kullanılır, source:"د س و,B001"}. Fiil açıkça büyütmenin karşıtı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, "zekâ" fiilinin zıddıdır; o kişi büyüyen değil, gizlenendir, source:"د س و,B002"}. Arap dilinde bu fiil, harflerden biri dönüşmüş bir "dessese" olarak da açıklanır: {ar:دسّسها, tr:dessesehâ, gloss:onu gömdü, toprağa itip gizledi, source:"memory"}. Bu, iki kökün aynı olduğunu göstermez. Yalnızca bir türeyiş yolunu gösterir. Kur'an, iki harfli bu ikinci kökün fiilini bir saklanma sahnesinde kullanır. Allah, kendisine kız çocuğu müjdelenen ve yüzü kararan bir babayı anlatır. Bu adam halktan gizlenir, {ar:يَتَوَٰرَىٰ مِنَ ٱلْقَوْمِ, tr:yetevârâ mine'l-kavm, gloss:halktan saklanır, source:16:59}, ve kendine sorar: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Kişinin kendini saklaması ile başkasını toprağa itmesi orada tek bir sahnede birleşir. Onuncu ayetteki nefis de böylece güneşin tersine götürülür: açıktan kuytuya, görünürden gömülüye.

Semûd'a gelince açılan şey bir işaret, kapanan şey de bir azaptır. Allah, Semûd'a verdiği dişi deveyi gözleri açan bir işaret olarak anar: {ar:وَءَاتَيْنَا ثَمُودَ ٱلنَّاقَةَ مُبْصِرَةًۭ, tr:ve âteynâ Semûde'n-nâkate mubsıraten, gloss:Semûd'a göz açan bir işaret olarak dişi deveyi verdik, source:17:59}. Onlar ise gündüzün değil gecenin tarafını seçtiler: {ar:فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ, tr:fe'stehabbu'l-amâ ale'l-hudâ, gloss:körlüğü doğru yola tercih ettiler, source:41:17}. Gecenin fiili bir halkın üstüne serilen cezanın da fiilidir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa kaplayıp hepsini saran bir ceza, source:"غ ش و,B002"}. Kur'an kendini güvende sananlara aynı kelimeyle seslenir: {ar:أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:en te'tiyehum ğâşiyetun min azâbi'llâh, gloss:Allah'ın azabından onları kaplayacak bir şeyin gelmesinden, source:12:107}. Necm Suresi'nde Allah helak ettiği toplulukları sayar: {ar:وَثَمُودَا۟ فَمَآ أَبْقَىٰ, tr:ve Semûde fe-mâ ebkâ, gloss:Semûd'u da geride hiçbir şey bırakmadı, source:53:51}. Aynı dizinin sonunda tersyüz edilmiş şehir için yine örtme fiili gelir: {ar:فَغَشَّىٰهَا مَا غَشَّىٰ, tr:fe-ğaşşâhâ mâ ğaşşâ, gloss:onu örten örttü, source:53:54}. On dördüncü ayetteki "demdeme aleyhim" sözü dilde yok etmeyi anlatır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}. Arap dili aynı fiili "üstlerine kapattı" diye de açıklar: {ar:أطبق عليهم, tr:etbaka aleyhim, gloss:üstlerine kapandı, source:"memory"}. Suçun fiili bile örtü taşır. Devenin ayaklarını kesmek anlamındaki "akr" kelimesi, güneşin gözünü örten bir bulutun da adıdır: {ar:العقر غيم ينشأ من قبل العين فيغشى عين الشمس, tr:el-ukru ğaymun yenşe'u min kıbeli'l-ayn, fe-yağşâ ayne'ş-şems, gloss:ukr, ufkun bir yönünden yükselip güneşin gözünü örten buluttur, source:"ع ق ر,B018"}.

Kaynaklar: 91:1 ٱلشَّمْسِ ش م س B001; 91:1 ضُحَىٰهَا ض ح و B001; 91:1 ضُحَىٰهَا ض ح و B002; 91:2 تَلَىٰهَا ت ل و B001; 91:3 ٱلنَّهَارِ ن ه ر B002; 91:3 جَلَّىٰهَا ج ل و B001; 91:3 جَلَّىٰهَا ج ل و B007; 91:4 يَغْشَىٰهَا غ ش و B001; 91:4 يَغْشَىٰهَا غ ش و B002; 91:6 طَحَىٰهَا ط ح و B008; 91:7 نَفْسٍۢ ن ف س B009; 91:7 سَوَّىٰهَا س و ي B012; 91:8 فُجُورَهَا ف ج ر B002; 91:8 فُجُورَهَا ف ج ر B004; 91:8 تَقْوَىٰهَا و ق ي B001; 91:10 دَسَّىٰهَا د س و B001; 91:10 دَسَّىٰهَا د س و B002; 91:14 فَدَمْدَمَ د م د م B001; 91:14 فَعَقَرُوهَا ع ق ر B018; 91:15 عُقْبَٰهَا ع ق ب B005

## Dişi devenin bedeni

Surenin birçok kelimesi bir dişi deveyle uğraşmanın dilinden gelir. Merkezde devenin kendisi durur: {ar:ناقة ونوق, tr:nâkatun ve nûk, gloss:nâka, dişi deve; çoğulu nûk, source:"ن و ق,B002"}. On ikinci ayetin fiili de deve sürmenin dilindendir: {ar:بعثت الناقة إذا أثرتها, tr:ba'astu'n-nâkate izâ eseartuhâ, gloss:dişi deveyi kaldırdığımda "ba'astu" derim, source:"ب ع ث,B001"}. İşin tamamı şöyle anlatılır: {ar:بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته, tr:ba'astu'l-ba'îra fe'nbe'ase izâ halaltu ıkâlehû ve erseltuh, ev kâne bârikan fe-esertuh, gloss:deveyi kaldırdım, o da kalktı; yani köstekini çözüp saldım ya da çökmüşse ayağa kaldırdım, source:"ب ع ث,B001"}. Deve sürücüsünün fiilinde iki taraf vardır: biri kaldırır, deve kalkar. On ikinci ayette ise kaldıran yoktur, yalnızca kalkan vardır. Köstekten kurtulan, en bedbaht adamdır ve kalkışı devenin üstüne yönelir.

İkinci ayetteki fiil, devenin ardından yürüyen yavruyu adlandırır: {ar:تلو الناقة ولدها الذي يتلوها, tr:tilvu'n-nâkati veleduhe'llezî yetlûhâ, gloss:devenin tilvu, onu izleyen yavrusudur, source:"ت ل و,B006"}. Ay güneşi, yavrunun anasını izlediği gibi izler. Elçinin adının kökü de devenin yürüyüşünü anlatır: {ar:ناقة رسلة لينة المفاصل, tr:nâkatun resletun leyyinetu'l-mefâsıl, gloss:resle deve, eklemleri yumuşak devedir, source:"ر س ل,B003"}; {ar:ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا, tr:nâkatun resletun sehletu's-seyr, ve ibilun merâsîlu munbe'isetun inbi'âsen sehlen, gloss:resle deve, yürüyüşü kolay devedir; merâsîl develer, kolayca harekete geçen develerdir, source:"ر س ل,B003"}. Sekizinci ayetteki fiil memedeki yavruyu taşır, on üçüncü ayetteki kelime devenin suyunu. Bu sahne yukarıdaki iki imgede gösterildi.

On dördüncü ayette devenin bedenine yönelen fiil gelir. Bu fiil eşek arısı sokması gibi bir dokunuş değildir; ayağı biçmektir: {ar:عقر البعير كسف عرقوبه ثم جعل النحر عقرا, tr:akru'l-ba'îri kesfu urkûbih, summe cu'ile'n-nahru akran, gloss:deveyi akr etmek, topuk kirişini kesmektir; sonra boğazlamaya da akr denmiştir, source:"ع ق ر,B002"}. Kesilen kirişin adı on beşinci ayetteki kelimenin kökündendir: {ar:العرقوب عقب موتر خلف الكعبين والراء زائدة, tr:el-urkûbu akabun mûterun halfe'l-ka'beyn, ve'r-râu zâide, gloss:urkûb, iki aşık kemiğinin arkasında gerilmiş bir kiriştir; içindeki "r" harfi fazladan gelmiştir, source:"ع ق ب,B001"}; {ar:العقب العصب الذي تعمل منه الأوتار, tr:el-akabu'l-asabu'llezî tu'melu minhu'l-evtâr, gloss:akab, yay kirişlerinin yapıldığı sinirdir, source:"ع ق ب,B001"}. Topuğun kendisi de aynı köktendir: {ar:العقب مؤخر القدم, tr:el-akibu mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. On dördüncü ayetteki günah kelimesinin kökü de hayvanın arka tarafını adlandırır: {ar:ذنب وهو مؤخر الدواب, tr:zenebun, ve huve mu'ahharu'd-devâbb, gloss:zeneb, hayvanların arka ucudur, kuyruğudur, source:"ذ ن ب,B002"}. Ayakları biçen kılıç tam bu arka tarafa iner.

Kur'an devenin hikâyesini birkaç yerde anlatır. Allah Salih'e şöyle der: {ar:إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ, tr:innâ mursilu'n-nâkati fitneten lehum fe'rtakıbhum ve'stabir, gloss:onları sınamak için dişi deveyi gönderiyoruz; sen onları gözle ve sabret, source:54:27}. Burada deve "gönderilir", ve fiil elçinin adının köküyle kurulur. Ardından o tek adam bıçağa uzanır: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Salih'in uyarısında devenin otlama hakkı da vardır, dokunma yasağı da: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın, ona kötülükle dokunmayın, source:7:73}. Şuarâ Suresi'nde ise devirmenin hemen ardından pişmanlık gelir: {ar:فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ, tr:fe-akarûhâ fe-asbahû nâdimîn, gloss:ayaklarını biçtiler ve pişman oldular, source:26:157}. Düz bir anlatım "deveyi öldürdüler" der. Fiil ise işin yerini gösterir: önce topuğa, sonra yere yapılan bir iş. Kelimelerin dağılımı da bir sıra gösterir. Kaldırılan, izlenen, rahat yürüyen ve sulanan bir deve, sonunda arkasından biçilir. Bu ardından gelen kelimeler, son ayette suçun ardından gelecek olanı haber verir.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B006; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:13 نَاقَةَ ن و ق B002; 91:13 رَسُولُ ر س ل B003; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 عُقْبَٰهَا ع ق ب B001; 91:15 عُقْبَٰهَا ع ق ب B002

## Gönderilen ve peşine düşülen

Surenin başında doğru bir izleme vardır: ay güneşi izler. İzleme fiilinin bir kolu, vahyedilmiş kitabı izlemeyi anlatır: {ar:التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام, tr:et-tilâvetu tahtessu bi'ttibâ'i kutubi'llâhi'l-munzele, târeten bi'l-kırâe ve târeten bi'l-irtisâm, gloss:tilâvet, Allah'ın indirdiği kitapları izlemeye mahsustur; bazen okuyarak, bazen izine uyarak, source:"ت ل و,B002"}. İkinci ayetteki ayın işi, on üçüncü ayette elçinin getirdiği sözü izlemenin ölçüsü olur.

Elçinin adının kökü, salıvermeyi ve uzanmayı anlatır: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbi'âsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir kök, source:"ر س ل,B001"}; {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:irsâl, tutmanın karşıtıdır, source:"ر س ل,B001"}. Elçi taşıdığı sözün adıyla da anılır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة, tr:er-rasûlu yukâlu li'l-kavli'l-mutehammel, ve târeten li-mutehammili'l-kavli ve'r-risâle, gloss:resûl, taşınan söze de, sözü ve mesajı taşıyana da denir, source:"ر س ل,B002"}. Gönderme fiili ile on ikinci ayetin fiili aynı aileye bağlanır: {ar:ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, nahvu erselnâ rusulenâ, gloss:"her ümmete bir elçi ba'as ettik" sözü, "elçilerimizi irsâl ettik" gibidir, source:"ب ع ث,B002"}. Kur'an'daki karşılığı bir ayette göndermeyi, inkârı ve sonucu birlikte toplar: {ar:وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, gloss:andolsun, her ümmete bir elçi gönderdik, source:16:36}. Aynı ayet şöyle biter: {ar:فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ, tr:fe'nzurû keyfe kâne âkıbetu'l-mukezzibîn, gloss:yalanlayanların sonunun nasıl olduğuna bakın, source:16:36}. On ikinci ayette ise fiil, göndereni olmayan bir kalkış biçiminde gelir. Allah'ın göndermesine karşılık bir adam kendini gönderir.

Bu adam kavmin başındadır ve kavmin en bedbahtıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hılâfu's-seâde, gloss:şikve, mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kavim de onun peşine düşer. On dördüncü ayetteki "zenb" kelimesinin bir kolu bu izleyenlerin adıdır: {ar:ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء, tr:zenebu'r-raculi etbâ'uh, ve ezenâbu'l-kavmi etbâ'u'r-ruesâ', gloss:adamın kuyruğu, ona uyanlardır; kavmin kuyrukları, reislere uyanlardır, source:"ذ ن ب,B003"}. On beşinci ayetteki kelimenin kökü de birinin izinden gelmeyi anlatır: {ar:العاقب الذي يجيء في أثر صاحبه, tr:el-âkıbu'llezî yecîu fî eseri sâhibih, gloss:âkıb, arkadaşının izinden gelendir, source:"ع ق ب,B005"}. İzlenmesi gereken elçi ise yalanlanır: {ar:كذبته نسبته إلى الكذب, tr:kezzebtuhû: nesebtuhû ile'l-kezib, gloss:onu yalanladım, yani ona yalan isnat ettim, source:"ك ذ ب,B002"}. Kavmin elçiye cevabı söze karşı söz olarak gelir. Elçi "ve kâle", "dedi ki" diye konuşur: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl, konuşmadan gelir, source:"ق و ل,B001"}.

Kur'an Semûd'un bu reddini kendi sözleriyle aktarır. Bir insanı izlemeyi küçümserler: {ar:أَبَشَرًۭا مِّنَّا وَٰحِدًۭا نَّتَّبِعُهُۥٓ, tr:e beşeren minnâ vâhiden nettebi'uh, gloss:aramızdan tek bir insana mı uyacağız, source:54:24}. Ve onu yalancılıkla suçlarlar: {ar:بَلْ هُوَ كَذَّابٌ أَشِرٌۭ, tr:bel huve kezzâbun eşir, gloss:hayır, o şımarık bir yalancıdır, source:54:25}. Aynı sure, tek bir adamın ardına düşüldüğü sahneyle sürer: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Elçiye uymayı reddedenler, kendi seçtikleri adamı izler. A'râf Suresi'nde de büyüklenen ileri gelenler müminlere sorar: {ar:أَتَعْلَمُونَ أَنَّ صَٰلِحًۭا مُّرْسَلٌۭ مِّن رَّبِّهِۦ, tr:e ta'lemûne enne Sâlihan murselun min rabbih, gloss:Salih'in Rabbi tarafından gönderildiğini mi biliyorsunuz, source:7:75}. Deveyi biçtikten sonra da alay ederler: {ar:إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ, tr:in kunte mine'l-murselîn, gloss:eğer gönderilenlerdensen, source:7:77}. Şuarâ Suresi'nde de anlatım bir yalanlamayla açılır: {ar:كَذَّبَتْ ثَمُودُ ٱلْمُرْسَلِينَ, tr:kezzebet Semûdu'l-murselîn, gloss:Semûd gönderilenleri yalanladı, source:26:141}. Salih'in kendini tanıtması da şudur: {ar:إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ, tr:innî lekum rasûlun emîn, gloss:ben size gönderilmiş güvenilir bir elçiyim, source:26:143}. Neml Suresi bu izleyiciliğin içindeki bir çekirdekten bahseder: {ar:وَكَانَ فِى ٱلْمَدِينَةِ تِسْعَةُ رَهْطٍۢ, tr:ve kâne fi'l-medîneti tis'atu rahtin, gloss:şehirde dokuz kişilik bir çete vardı, source:27:48}. Elçinin son sözü, taşıdığı yükü teslim ettiğidir: {ar:لَقَدْ أَبْلَغْتُكُمْ رِسَالَةَ رَبِّى, tr:le-kad eblağtukum risâlete rabbî, gloss:Rabbimin mesajını size ulaştırdım, source:7:79}. Düz bir anlatım "yalanladılar" der. Bu imge ise iki izleme hattı çizer: biri gökte ve doğru, ay güneşin ardından gider; öteki yerde ve yanlış, kavim kendi en bedbahtının ardından gider. Birinde sıra korunur, ötekinde başa geçen, peşindekileri yıkıma götürür.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B001; 91:2 تَلَىٰهَا ت ل و B002; 91:11 كَذَّبَتْ ك ذ ب B002; 91:12 ٱنۢبَعَثَ ب ع ث B002; 91:12 أَشْقَىٰهَا ش ق و B001; 91:13 فَقَالَ ق و ل B001; 91:13 رَسُولُ ر س ل B001; 91:13 رَسُولُ ر س ل B002; 91:14 فَكَذَّبُوهُ ك ذ ب B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B003; 91:15 عُقْبَٰهَا ع ق ب B005

## Suç ve topuğundaki

On dördüncü ve on beşinci ayetler bir bedenin arka ucunda kapanır. "Zenb" ile "ukbâ" ayrı köklerden gelir, ama ikisi de bir şeyin son ucunu adlandırır. Zenb kuyruktur: {ar:ذنب كل شيء آخره, tr:zenebu kulli şey'in âhiruh, gloss:her şeyin zenebi, onun son ucudur, source:"ذ ن ب,B002"}. Ukbâ da sondur: {ar:عاقبة كل شيء آخره والعقبى جزاء الأمر, tr:âkıbetu kulli şey'in âhiruh, ve'l-ukbâ cezâu'l-emr, gloss:her şeyin âkıbeti onun sonudur; ukbâ da bir işin karşılığıdır, source:"ع ق ب,B006"}. Günah, sonucuyla tanımlanır: {ar:يستعمل في كل فعل يستوخم عقباه, tr:yusta'melu fî kulli fi'lin yustevhamu ukbâh, gloss:sonu ağır gelen, sindirilemeyen her iş için kullanılır, source:"ذ ن ب,B001"}. Ceza da günahın ardından gelen ikinci şey olarak adını alır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet ukûbeten li-ennehâ tekûnu âhiran ve sâniye'z-zenb, gloss:cezaya ukûbe denmesi, en sonda ve günahın ikincisi olarak gelmesindendir, source:"ع ق ب,B007"}. İki kök tek bir cümlede de buluşur: {ar:العقاب العقوبة وقد عاقبته بذنبه, tr:el-ıkâbu'l-ukûbe, ve kad âkabtuhû bi-zenbih, gloss:ıkâb cezadır; onu günahıyla cezalandırdım, source:"ع ق ب,B007"}. Bu, on dördüncü ayetin "bi-zenbihim" sözüyle on beşinci ayetin "ukbâhâ" sözünün dilde birbirine bağlı iki parça olduğunu gösterir.

Suçu cezalandıran, malın sahibidir. On dördüncü ayet Rab der: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey': mâlikuh, gloss:her şeyin rabbi, onun sahibidir, source:"ر ب ب,B001"}. On üçüncü ayette deve "Allah'ın devesi" diye anılmıştı. Sahibinin malına el uzatılmış, sahibi de karşılığı vermiştir. Gecenin fiili bu karşılığın biçimini verir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa saran bir ceza, source:"غ ش و,B002"}. Ceza, on beşinci ayetin kökünden, gecenin örtüsüyle gelir.

On beşinci ayet sonucu hiç kimsenin geri çeviremeyeceğini söyler: {ar:وَلَا يَخَافُ عُقْبَٰهَا, tr:ve lâ yehâfu ukbâhâ, gloss:o, bunun sonundan korkmaz, source:91:15}. Ayetin öznesi, bir önceki ayetin öznesi olan Rabdir. Korku, bir işaretten zarar beklemektir: {ar:الخوف توقع مكروه عن أمارة مظنونة أو معلومة, tr:el-havfu tevakku'u mekrûhin an emâratin maznûnetin ev ma'lûme, gloss:korku, sanılan ya da bilinen bir işaretten hoşa gitmeyen bir şey beklemektir, source:"خ و ف,B001"}. Ama Allah'ın korkutması bir uyarıdır, kendisi korkmaz: {ar:التخويف من الله تعالى هو الحث على التحرز, tr:et-tahvîfu mina'llâhi teâlâ huve'l-hassu ale't-teharruz, gloss:Allah'ın korkutması, sakınmaya teşviktir, source:"خ و ف,B002"}. Kur'an deveyi tam olarak böyle bir korkutma olarak anar: {ar:وَمَا نُرْسِلُ بِٱلْءَايَٰتِ إِلَّا تَخْوِيفًۭا, tr:ve mâ nursilu bi'l-âyâti illâ tahvîfâ, gloss:işaretleri ancak korkutmak için göndeririz, source:17:59}. "Ukbâ" kökünün bir kolu, bir hükmün ardına düşüp hak arayanı adlandırır: {ar:المعقب الذي يتتبع عقب إنسان في طلب حق, tr:el-mu'akkıbu'llezî yetetebba'u akibe insânin fî talebi hakk, gloss:mu'akkıb, hak istemek için birinin topuğu ardınca izleyendir, source:"ع ق ب,B008"}; {ar:لا معقب لحكمه أي لا راد لقضائه, tr:lâ mu'akkıbe li-hukmih, ey lâ râdde li-kadâih, gloss:hükmünün ardına düşen yoktur, yani kararını geri çevirecek yoktur, source:"ع ق ب,B008"}. Kur'an bu sözü kendi diliyle söyler: {ar:وَٱللَّهُ يَحْكُمُ لَا مُعَقِّبَ لِحُكْمِهِۦ, tr:va'llâhu yahkumu lâ mu'akkibe li-hukmih, gloss:Allah hükmeder; O'nun hükmünün ardına düşüp onu bozacak yoktur, source:13:41}. Bir başka yerde aynı gerçeği şöyle söyler: {ar:لَا يُسْـَٔلُ عَمَّا يَفْعَلُ وَهُمْ يُسْـَٔلُونَ, tr:lâ yus'elu ammâ yef'alu ve hum yus'elûn, gloss:O yaptığından sorgulanmaz, onlar sorgulanır, source:21:23}.

Kur'an Semûd'un sonunu bu iki kelimeyle anlatır. Neml Suresi'nde dokuz kişilik çetenin tuzağı şöyle biter: {ar:فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ مَكْرِهِمْ أَنَّا دَمَّرْنَٰهُمْ وَقَوْمَهُمْ أَجْمَعِينَ, tr:fe'nzur keyfe kâne âkıbetu mekrihim, ennâ demmernâhum ve kavmehum ecma'în, gloss:tuzaklarının sonunun nasıl olduğuna bak: onları da kavimlerini de topyekûn yok ettik, source:27:51}. Ankebût Suresi'nde helak edilen kavimler toplu olarak anılır: {ar:فَكُلًّا أَخَذْنَا بِذَنۢبِهِۦ, tr:fe-kullen ehaznâ bi-zenbih, gloss:hepsini kendi günahıyla yakaladık, source:29:40}. Enfâl Suresi'nde de aynı bağ kurulur: {ar:فَأَهْلَكْنَٰهُم بِذُنُوبِهِمْ, tr:fe-ehleknâhum bi-zunûbihim, gloss:onları günahları yüzünden helak ettik, source:8:54}. Devenin biçilmesinden sonra Salih'in sözü, sonucu bir süreye bağlar: {ar:فَعَقَرُوهَا فَقَالَ تَمَتَّعُوا۟ فِى دَارِكُمْ ثَلَٰثَةَ أَيَّامٍۢ, tr:fe-akarûhâ fe-kâle temetta'û fî dârikum selâsete eyyâm, gloss:onu biçtiler; Salih de dedi ki: yurdunuzda üç gün daha yaşayın, source:11:65}; {ar:ذَٰلِكَ وَعْدٌ غَيْرُ مَكْذُوبٍۢ, tr:zâlike va'dun ğayru mekzûb, gloss:bu, yalanlanamayacak bir sözdür, source:11:65}. Yalanlayarak işe başlayan kavim, yalanlanamayan bir sözle karşılaşır.

Dokuzuncu ayet bu dilin öbür yüzünü taşır. Arınıp büyüyenin işi de sonucuyla tanımlanır, ama tersinden: {ar:حلالا لا يستوخم عقباه, tr:helâlen lâ yustevhamu ukbâh, gloss:helâl, yani sonu ağır gelmeyen, source:"ز ك و,B002"}. Günah sindirilemeyen bir sondur, arınmanın sonu ise kolay sindirilir. Düz bir anlatım son ayeti bir ek söz gibi okur. Bu imge ise onu surenin bedenine bağlar: suç arkada durur, karşılığı da onun ardından gelir ve ardından bir şey gelmeyen tek şey hükmün kendisidir.

Kaynaklar: 91:4 يَغْشَىٰهَا غ ش و B002; 91:9 زَكَّىٰهَا ز ك و B002; 91:14 رَبُّهُم ر ب ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 يَخَافُ خ و ف B001; 91:15 يَخَافُ خ و ف B002; 91:15 عُقْبَٰهَا ع ق ب B006; 91:15 عُقْبَٰهَا ع ق ب B007; 91:15 عُقْبَٰهَا ع ق ب B008

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

