Focus: 90:12. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/90_12/D.r13/context.md =====
# 90:12 — focus

وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ

Anchor translation (canonical reading, reference only):

Sarp yokuşun ne olduğunu sana ne bildirdi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَآ | مَا |  | CONJ;INTG |
| 2 | أَدْرَىٰكَ | أَدْرَىٰ | د ر ي | V;PRON |
| 3 | مَا | مَا |  | INTG |
| 4 | ٱلْعَقَبَةُ | عَقَبَة | ع ق ب | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 90 — full text (context; no pericope)

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 ◀ focus وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/90_12/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## د ر ي (root_000473) — identity root of أَدْرَىٰكَ (w2)

- **B001** bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme — bir şeyi bilmek veya ondan haberdar olmak · birine bildirmek, onun bilmesini sağlamak · bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi · bilmiyorum
  دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)
- **B002** saldırı amacıyla bir yer ya da kişiyi seçmek [kalıp] — bir yeri baskın veya saldırı için seçmek
  أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)
- **B003** avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak — avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan · avı gizlenip aldatarak atış menziline getirmek · hileyle kandırmak
  الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)
- **B004** sivri uç ve bundan ad alan saç düzeltme aracı — sivri boynuz; saçı düzeltmeye yarayan sivri araç · saçı ayırıp düzeltmeye yarayan şiş biçimli araç · saçını tarayıp düzeltmek
  الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)
- **B005** saplama ve atış alıştırma hedefi — üzerinde saplama alıştırması yapılan hedef
  الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)
- **B006** insanlarla yumuşak ve incelikli geçinmek [kalıp] — insanlara karşı yumuşak ve uzlaştırıcı davranmak
  مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)

## ع ق ب (root_001033) — identity root of ٱلْعَقَبَةُ (w4)

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

## ECHO د ر ر (root_000469) — for أَدْرَىٰكَ (w2): withheld observed target; not identity

- **B001** bir kaynaktan bolca çıkma veya bol ürün verme — sütün memeden çıkıp akması · süt · bol sütlü dişi deve · bulutun yağmur boşaltması · bol yağmur getiren · gözünden yaş akması · damarların kanla dolması · Ne güzel iş ve iyilik! · İyiliği artmasın! · vergi gelirinin artması · pazarın canlanması · dişi keçilerin teke istemesi · sütün bolluğu veya akışı
  الدر در اللبن (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در السحاب بالمطر ودرت السماء وسحابة مدرار (maqayis;jamhara;sihah;tahdhib;mufradat)؛ لله دره ولا در دره أي خيره أو عمله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در الخراج وحلوبة المسلمين وللسوق درة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ استدرت المعزى إذا أرادت الفحل (maqayis;sihah;tahdhib;mufradat)
- **B002** hızlı, güçlü ve akıcı koşma — çok hızlı koşan binek hayvanı · atın hızlı ve rahat koşması · bacakta güçlü koşma yetisi · atın tırıs sırasında ön ayağını kaldırıp indirdiği yürüyüş biçimi
  الدرير من الدواب الشديد العدو السريعة (maqayis)؛ در الفرس دريرا إذا عدا عدوا شديدا سهلا (jamhara)؛ فرس درير أي سريع (sihah)؛ در الفرس درة فهو درير إذا أسرع في عدوه والإدرار في الخيل (tahdhib)
- **B003** gevşekçe sallanma veya tekrar tekrar gidip gelme — diş yuvaları; kimi kullanımda dil ucu · çocuğun bir şeyi ağzında çevirip çiğnemesi · sallanıp oynamak · dişleri dökülüp diş yuvaları görünmek · gereksiz yere gidip gelen kimse
  الدردر منابت أسنان الصبي ومن تدردرت اللحمة إذا اضطربت ودردر الصبي الشيء إذا لاكه (maqayis)؛ الدردر مغارز أسنان الصبي ودردر الصبي البسرة لاكها (sihah)؛ تدردر أي تمرمر وترجرج والدردر مغرز السن وطرف اللسان والدردرى الذي يذهب ويجيء في غير حاجة (tahdhib)
- **B004** doğrultu, yön veya karşı karşıya hizalanma — yolun doğrultusu veya güzergâhı · rüzgârın esiş yönü · tam karşında veya hizanda
  درر الريح مهبها ودرر الطريق قصده (maqayis)؛ هما على درر واحد ونحن على درر الطريق ودرر الريح مهبها (sihah)؛ فلان دررك أي قبالتك وعلى درر الطريق أي مدرجته وداري بدرر دارك أي بحذائها (tahdhib)
- **B005** iri inci; inci gibi beyaz ve parlak yıldız — iri inciler veya inci topluluğu · iri inci; tek bir inci · inci gibi beyaz ve parlak yıldız
  الدر كبار اللؤلؤ والكوكب الدري الثاقب المضيء (maqayis)؛ الدرة ما عظم من اللؤلؤ (jamhara)؛ الدرة اللؤلؤة والكوكب الدري الثاقب المضيء نسب إلى الدر لبياضه (sihah)؛ الدر العظام من اللؤلؤ والكوكب الدري الثاقب المضيء (tahdhib)
- **B006** özellikle yöneticinin kullandığı vurma değneği — özellikle yöneticinin kullandığı vurma değneği
  الدرة التي يضرب بها عربية معروفة (jamhara)؛ الدرة التي يضرب بها (sihah)؛ الدرة درة السلطان التي يضرب بها (tahdhib)
- **B007** ipliği sıkı bükmek için iği döndürme — ipliği sıkı bükmek için iği veya dönen parçasını çevirmek
  أدرت المرأة المغزل إذا فتلته فتلا شديدا فهي مدر والمغزل مدر (jamhara)؛ أدرت الغزالة درارتها إذا أدارتها لتستحكم قوة ما تغزله (tahdhib)
- **B008** gemiyi tehlikeye atan çalkantılı deniz girdabı — girdap; gemiyi tehlikeye atan çalkantılı deniz yeri
  الدردور الماء الذي يدور ويخاف فيه الغرق (sihah)؛ الدردور موضع من البحر يجيش ماؤه وقلما تسلم السفينة منه (tahdhib)

===== _commentary/v16/out/s090/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 90:12, and ## Buluşmalar) =====
## İki sırt ve sarp geçit

Bu yorumda bir kelimenin dildeki ailesinden gelen görüntüler, kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Ayet ne söylüyorsa onu söyler. Aile yalnızca kelimenin Arapçada taşıdığı başka sahneleri onun yanına getirir.

Surenin ortasında bir yol sahnesi durur. Onuncu ayet {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhu'n-necdeyn, gloss:ve ona iki necdi gösterdik, source:90:10} der. "Necd" Arapçada önce yerin bir biçimidir: {ar:النجد ما ارتفع من الأرض, tr:en-necdu mâ irtefea mine'l-ard, gloss:necd yerden yükselen kısımdır, source:"ن ج د,B001"}. Kökün kendisi {ar:اعتلاء وقوة وإشراف, tr:i'tilâ ve kuvve ve işrâf, gloss:yükselme ve güç ve yukarıdan bakma, source:"ن ج د,B001"} bildirir. Demek ki insana gösterilen şey düz iki patika değildir. Aşağıdan bakınca yükselen, üstüne çıkılacak iki sırttır. Aynı kelime bir yolun niteliği olarak da kullanılır: {ar:وأمر نجد واضح وطريق نجد هاد, tr:ve emrun necdun vâdıh ve tarîkun necdun hâd, gloss:necd iş açık iştir ve necd yol yol gösteren yoldur, source:"ن ج د,B002"}. Burada yolun kendisi yol gösterir. Ayetin fiili de aynı işi anlatır: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîka ve'l-beyte hidâyeten ey arraftuh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. Bu ailede rehber önden yürüdüğü için bu adı alır: {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlu yusemmâ hâdiyen li-tekaddumih, gloss:kılavuza önden gittiği için hâdî denir, source:"ه د ي,B003"}. Yürüyenin elindeki değnek de aynı sebeple bu adı taşır: {ar:الهادية العصا لأنها تتقدم ممسكها, tr:el-hâdiyetu'l-asâ li-ennehâ tetekaddemu mumsikehâ, gloss:hâdiye değnektir çünkü tutanın önüne geçer, source:"ه د ي,B003"}. Değnek, tutan kişiden bir adım önce yere değer ve ayağın basacağı yeri önce o yoklar. Onuncu ayetteki "gösterdik" bu işleyişi taşır: yol insanın önüne konmuştur ve iki sırt görünür durumdadır. Düz bir anlatımın veremeyeceği şey de buradan çıkar: bundan sonra gelecek başarısızlık yolu bulamamak olamaz.

On birinci ayet {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp geçide atılmadı, source:90:11} der. "Akabe", yolun önüne enine çıkan dağdır: {ar:العقبة الجبل الطويل يعرض للطريق وهو صعب شديد, tr:el-akabetu'l-cebelu't-tavîlu ya'rizu li't-tarîk ve huve sa'bun şedîd, gloss:akabe yolun önüne enine çıkan uzun dağdır ve zor ve çetindir, source:"ع ق ب,B012"}. Aynı kelime o dağın içinden geçen engebeli yolu da adlandırır: {ar:العقبة طريق وعر في الجبل, tr:el-akabetu tarîkun va'run fi'l-cebel, gloss:akabe dağdaki engebeli yoldur, source:"ع ق ب,B012"}. Yol giderken önüne bir dağ çıkar ve geçmek isteyen tırmanmak zorundadır. "İktiham" bu dağa karşı yapılacak hareketin adıdır. Dil bu fiili iki hareketle tanımlar: {ar:هوى من علو إلى سفل أو دخل في شيء من غير هداية, tr:hevâ min uluvvin ilâ sufl ev dehale fî şey'in min ğayri hidâye, gloss:yüksekten aşağı düştü ya da bir şeye yol gösterilmeden girdi, source:"ق ح م,B001"} ve {ar:رمى بنفسه فيها من غير دربة, tr:remâ bi-nefsihî fîhâ min ğayri durbe, gloss:alışkanlığı olmadan kendini işlerin içine attı, source:"ق ح م,B001"}. Fiil, bedenin kendini bir şeyin içine fırlatmasıdır ve çoğu kez gözü kapalı bir fırlatıştır: "yol gösterilmeden". Sure bu fiili tam ters bir yere koyar, çünkü yol gösterme bir önceki ayette verilmiştir. Eksik olan kılavuz değil atılıştır. Göz açık, yol görülüyor, ama beden kendini yukarıya, dağın zorluğuna atmamıştır. Dağın zor yerleri de aynı kökle anılır: {ar:قحم الطريق مصاعبه, tr:kuhamu't-tarîki masâ'ibuh, gloss:yolun kuhamı onun zor yerleridir, source:"ق ح م,B002"}. Bir başka söyleyiş de şudur: {ar:القحمة الأمر العظيم لا يركبها كل أحد, tr:el-kuhmetu'l-emru'l-azîmu lâ yerkebuhâ kullu ehad, gloss:kuhme herkesin üstüne binemeyeceği büyük iştir, source:"ق ح م,B002"}.

Geçit karşısında yapılabilecek öbür hareketler de surenin kelimelerinde vardır. "Akabe" ile aynı kökten gelen "akib" topuktur {source:"ع ق ب,B002"}. Yokuşta bedeni yukarı iten yer orasıdır, ama dil geri dönüşü de bu topukla anlatır: {ar:رجع على عقبه وانقلب على عقبيه, tr:raca'a alâ akibihî ve'nkalebe alâ akibeyh, gloss:topuğu üstünde geri döndü ve iki topuğu üstünde döndü, source:"ع ق ب,B003"}. Birinci ayetteki "beled" kelimesinin ailesinde bir duraksama da vardır: {ar:تبلد الرجل إذا وضع يده على صدره عند تحيره في الأمر, tr:tebelleda'r-racul izâ veda'a yedehû alâ sadrihî inde tehayyurihî fi'l-emr, gloss:adam bir işte şaşırıp elini göğsüne koyduğunda tebelleda denir, source:"ب ل د,B005"}. Geride kalan at da bu aileye girer: {ar:فرس بليد إذا تأخر عن الخيل السوابق, tr:feresun belîdun izâ teahhara ani'l-hayli's-sevâbık, gloss:öne geçen atlardan geride kalan ata belîd denir, source:"ب ل د,B007"}. Bu ailenin özeti şudur: {ar:البلادة نقيض النفاذ والمضاء في الأمور, tr:el-belâdetu nakîdu'n-nefâzi ve'l-medâ'i fi'l-umûr, gloss:belâdet işlerde içinden geçip gitmenin zıddıdır, source:"ب ل د,B007"}. Böylece şehrin anıldığı ilk ayetten başlayarak bu kelimenin yanında, yokuşun dibinde elini göğsüne koymuş kararsız bir adam ile öbür atlar atılırken geride kalan bir at da duyulur. On birinci ayet bu duruşu tek bir olumsuzlukla söyler: atılmadı. On dokuzuncu ayetin "keferû" fiilinin kökü bile dağ yollarını adlandırır: {ar:الكفر الثنايا من الجبال, tr:el-kefru's-senâyâ mine'l-cibâl, gloss:kefr dağlardaki geçit yollarıdır, source:"ك ف ر,B013"}.

Geçidin yanında ne vardır? Altıncı ayetteki övünme fiili {ar:أَهْلَكْتُ, tr:ehlektu, gloss:tükettim, source:90:6}, kökü bakımından iki dağ arasındaki boşluğu da adlandırır: {ar:الهلك المهوى بين الجبلين, tr:el-helku'l-mehvâ beyne'l-cebeleyn, gloss:helk iki dağ arasındaki uçurumdur, source:"ه ل ك,B006"}. Yolcuyu öldüren çöl de bu kökle anılır: {ar:مفازة هالكة من سلكها أي هالكة السالكين, tr:mefâzetun hâliketun men selekehâ, gloss:içine gireni helak eden çöl, source:"ه ل ك,B006"}. Dağın zor yerleri için de aynı kelime kullanılır: {ar:سميت المهالك قحما, tr:summiyeti'l-mehâliku kuhamen, gloss:helak yerlerine kuham denildi, source:"ق ح م,B002"}. Böylece geçidin kökü ile adamın övünme fiilinin kökü tek bir tanımda yan yana gelir. Adamın tükettiğini söylediği servet, bu aileyle duyulduğunda iki dağın arasındaki uçuruma dökülmüş gibidir: yukarı doğru atılış yapılmamış, mal ise aşağıya gitmiştir.

Akabe'nin kökü yolun sonunu da adlandırır: {ar:عاقبة كل شيء آخره والعقبى جزاء الأمر, tr:âkıbetu kulli şey'in âhiruh ve'l-ukbâ cezâu'l-emr, gloss:her şeyin âkıbeti sonudur ve ukbâ işin karşılığıdır, source:"ع ق ب,B006"}. Geçit yolun ortasındaki zorluktur, aynı kökün "âkıbe"si ise yolun bittiği yerdir. On sekizinci ve on dokuzuncu ayetler bu sonu iki topluluk olarak adlandırır. Kur'an bu kökün "ukbâ"sını sabırla ve harcamayla birlikte anar. Allah akıl sahiplerini anlatırken onlar için {ar:وَٱلَّذِينَ صَبَرُوا۟ ٱبْتِغَآءَ وَجْهِ رَبِّهِمْ, tr:vellezîne saberu'btiğâe vechi rabbihim, gloss:Rablerinin yüzünü arayarak sabredenler, source:13:22} der. Aynı ayette onların verilen rızıktan gizli ve açık harcadıkları söylenir ve ayet {ar:أُو۟لَٰٓئِكَ لَهُمْ عُقْبَى ٱلدَّارِ, tr:ulâike lehum ukbe'd-dâr, gloss:yurdun sonu onlarındır, source:13:22} diye biter. İki ayet sonra onlara söylenen söz aynı iki kelimeyi birleştirir: {ar:سَلَٰمٌ عَلَيْكُم بِمَا صَبَرْتُمْ ۚ فَنِعْمَ عُقْبَى ٱلدَّارِ, tr:selâmun aleykum bimâ sabertum fe-ni'me ukbe'd-dâr, gloss:sabrettiğiniz için size selam olsun ve yurdun sonu ne güzeldir, source:13:24}.

Geçidin zorluğu surenin başında zaten insanın içinde durduğu yer olarak verilmiştir. Dördüncü ayet {ar:لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ, tr:lekad halaknâ'l-insâne fî kebed, gloss:andolsun insanı kebed içinde yarattık, source:90:4} der. "Kebed" zorluktur: {ar:الكبد وهي المشقة, tr:el-kebedu ve hiye'l-meşakka, gloss:kebed meşakkattir, source:"ك ب د,B002"}. Fiili de çekilen zorluğu anlatır: {ar:كابدت الأمر قاسيته في مشقة, tr:kâbedtu'l-emra kâsaytuhû fî meşakka, gloss:işle uğraştım yani onu zahmet içinde çektim, source:"ك ب د,B002"}. Dil bu zorluğa elle çevrilen bir taşın adını verir: {ar:الكبداء الرحا التي تدار باليد سميت كبداء لما في إدارتها من المشقة, tr:el-kebdâu'r-rahâ'lletî tudâru bi'l-yed summiyet kebdâe limâ fî idâratihâ mine'l-meşakka, gloss:kebdâ elle çevrilen değirmen taşıdır ve çevirmenin zahmetinden ötürü bu adı alır, source:"ك ب د,B002"}. Her tur bir kol gücü ister ve taş durmadan döner. Ayetteki "içinde" de bu ailede bir yer bildirir: {ar:كل شيء توسط شيئا فقد تكبده, tr:kullu şey'in tevessata şey'en fekad tekebbedeh, gloss:bir şeyin ortasına giren her şey onu tekebbüd etmiştir, source:"ك ب د,B003"}. Bir başka söyleyiş de {ar:تكبد الفلاة إذا قصد وسطها ومعظمها, tr:tekebbede'l-felâte izâ kasade vasatahâ ve mu'zamehâ, gloss:çölün ortasına ve en geniş yerine yöneldi, source:"ك ب د,B003"}. Geçide atılmanın tanımı da aynı sözle yapılır: {ar:الاقتحام توسط شدة مخيفة, tr:el-iktihâmu tevessutu şiddetin muhîfe, gloss:iktiham korkutucu bir zorluğun ortasına girmektir, source:"ق ح م,B001"}. Kökler ayrıdır, ama iki tanım "ortaya girme" fiilinde buluşur. İnsan zaten zorluğun ortasında yaratılmıştır. Geçit ondan, korkutucu bir zorluğun ortasına bu kez bilerek ve isteyerek girmesini ister. Geçide atılmamak zorluktan kurtulmak demek değildir. İnsan bu durumda hiçbir yere çıkmayan bir zorluğun içinde kalır.

"Necd" kelimesinin ailesi tırmananın bedenini de anlatır. Sıkıntı vardır: {ar:نجد الرجل فهو منجود إذا كرب من حر أو غم أو ضيق أو وجع, tr:necide'r-racul fe-huve mencûd izâ kerube min harrin ev ğammin ev dîkın ev veca', gloss:adam sıcaktan ya da gamdan ya da darlıktan ya da acıdan bunaldığında mencûd olur, source:"ن ج د,B005"}. Ter vardır: {ar:عرق من عمل أو كرب, tr:arika min amelin ev kerb, gloss:işten ya da sıkıntıdan terledi, source:"ن ج د,B006"}. Yokuşun istediği dayanıklılık vardır: {ar:رجل نجد بين النجدة إذا كان جلدا قويا, tr:raculun necdun beyyinu'n-necde izâ kâne celden kaviyyâ, gloss:dayanıklı ve güçlü adama necd denir, source:"ن ج د,B003"}. Çekerek pişmiş olan da vardır: {ar:منجد وهو الذي قد جرب الأمور وقاساها, tr:muneccad ve huve'llezî kad cerrebe'l-umûra ve kâsâhâ, gloss:işleri denemiş ve çekmiş olana muneccad denir, source:"ن ج د,B010"}. Sonunda hızlı ve işini başaran giden gelir: {ar:رجل نجد في الحاجة إذا كان ناجيا فيها أي سريعا, tr:raculun necdun fi'l-hâce izâ kâne nâciyen fîhâ, gloss:işinde hızlı ve başarılı olana necd denir, source:"ن ج د,B004"}. On dördüncü ayetin "mesğabe"si bu yorgunluğu açlığa ekler: {ar:لا يكون السغب إلا الجوع مع التعب, tr:lâ yekûnu's-sağabu illa'l-cû'u mea't-teab, gloss:seğab ancak yorgunlukla birlikte açlıktır, source:"س غ ب,B001"}. Altıncı ayetin kökü yolcuyu tüketen yolu da adlandırır: {ar:طريق مستهلك الورد أي يجهد من سلكه, tr:tarîkun mustehleku'l-vird ey yechedu men selekeh, gloss:içinden geçeni yoran yol, source:"ه ل ك,B009"}. Kendini bir işe adamak da bu kökle anılır: {ar:استهلك الرجل في كذا وكذا إذا جهد نفسه, tr:istehleke'r-raculu fî kezâ izâ cehede nefseh, gloss:adam bir iş için kendini tüketti, source:"ه ل ك,B009"}.

On yedinci ayet yokuşu çıkanların karşılıklı tavsiyesini {ar:وَتَوَاصَوْا۟ بِٱلصَّبْرِ, tr:ve tevâsav bi's-sabr, gloss:ve birbirlerine sabrı tavsiye ettiler, source:90:17} diye anar. Sabır, korkunun ortasında insanın kendini tutmasıdır: {ar:الصبر حبس النفس عن الجزع, tr:es-sabru habsu'n-nefsi ani'l-ceza', gloss:sabır nefsi panikten alıkoymaktır, source:"ص ب ر,B001"}. Fiili de aynı şeyi söyler: {ar:صبرت نفسي أي حبستها, tr:sabertu nefsî ey habestuhâ, gloss:nefsimi sabrettim yani onu tuttum, source:"ص ب ر,B001"}. Yokuşun ortasındaki adam kaçmamak için kendini yerinde tutar. Bu ailede {ar:أمر لا منفذ له عنه, tr:emrun lâ menfeze lehû anh, gloss:kendisinden çıkış yolu olmayan iş, source:"ص ب ر,B006"} de sabırla anılır. Böyle bir işin içinden ancak geçilir. Aynı kelime bir yerde tersine döner: {ar:الصبر الجرأة ومنه فما أصبرهم على النار, tr:es-sabru'l-cur'e ve minhu fe-mâ asberahum ale'n-nâr, gloss:sabır cüret demektir ve ateşe ne kadar dayanıklılar sözü buradandır, source:"ص ب ر,B013"}. Kur'an bu ters dönüşü kitabı gizleyip onu az bir bedele satanlar için kullanır. Allah onlar hakkında {ar:مَا يَأْكُلُونَ فِى بُطُونِهِمْ إِلَّا ٱلنَّارَ, tr:mâ ye'kulûne fî butûnihim ille'n-nâr, gloss:karınlarına ateşten başkasını yemezler, source:2:174} der. Sonraki ayet onları hidayeti sapıklıkla değişmiş olarak anlatır ve {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} diye biter. Yokuşta kendini tutmayan, ateşe karşı cüret eder.

Kur'an aynı yol sahnesini başka yerlerde de kurar. Allah bir surede önce insanı yarattığını söyler: {ar:إِنَّا خَلَقْنَا ٱلْإِنسَٰنَ مِن نُّطْفَةٍ أَمْشَاجٍۢ نَّبْتَلِيهِ, tr:innâ halaknâ'l-insâne min nutfetin emşâcin nebtelîh, gloss:biz insanı onu sınamak için karışık bir damladan yarattık, source:76:2}. Hemen ardından burada geçen fiille {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhu's-sebîle immâ şâkiren ve immâ kefûrâ, gloss:ona yolu gösterdik ya şükreden olur ya inkâr eden, source:76:3} der. Gösterilen yolun yolcusu iki şeyden biri olur, ve ikinci kelimenin kökü bu surenin on dokuzuncu ayetindeki "keferû" ile aynıdır. Bir sonraki sure yemin ettikten sonra nefse iki yolun ilham edildiğini söyler: {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona sapkınlığını ve sakınmasını ilham etti, source:91:8}. Onu izleyen surede Allah gece ve gündüz üzerine yemin ettikten sonra {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa'yekum le-şettâ, gloss:çabanız gerçekten çeşit çeşittir, source:92:4} der. Veren için {ar:فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ, tr:fe-emmâ men a'tâ ve'ttekâ, gloss:veren ve sakınan, source:92:5} ve {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu kolaylığa kolaylaştıracağız, source:92:7} der. Cimri için ise {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'steğnâ, gloss:cimrilik eden ve kendini yeterli gören, source:92:8} ve {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-usrâ, gloss:onu zorluğa kolaylaştıracağız, source:92:10} der. Ardından {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona bir yarar sağlamaz, source:92:11} ve {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek bize düşer, source:92:12} gelir. İki yol, verme ve tutma, yükseklikten düşüş ve yol gösterme orada da yan yana durur. Allah bir başka surede kendisine uzayıp giden bir mal verdiği ve ayetlerine inat eden adam için {ar:سَأُرْهِقُهُۥ صَعُودًا, tr:se-urhikuhû sa'ûdâ, gloss:onu sarp bir yokuşa zorlayacağım, source:74:17} der. İsteyerek çıkılmayan yokuş orada zorla çıkılan bir yokuş olur. "İktiham" kökü Kur'an'da bir yerde daha geçer. Azgınlara kötü bir dönüş yeri olduğu söylendikten sonra ateşte, arkalarından gelen kalabalık için {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59} denir. Geçide yapılmayan atılış ateşe yapılır. Teraziler hafif geldiğinde söylenen söz de yüksekten düşüşü adlandırır: {ar:فَأُمُّهُۥ هَاوِيَةٌۭ, tr:fe-ummuhû hâviye, gloss:onun anası bir uçurumdur, source:101:9}. Kelime, iktihamın tanımındaki "yüksekten aşağı düşmek" fiiliyle aynı köktendir. İnsanın yorgunluğu başka bir yerde Rabbe doğru bir emek olarak anılır: {ar:إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ, tr:inneke kâdihun ilâ rabbike kedhan fe-mulâkîh, gloss:sen Rabbine doğru didinip duruyorsun ve O'na kavuşacaksın, source:84:6}. Kökü "kebed"inkinden ayrıdır, ama sahne aynıdır: amaçlı bir zahmet. Sabrın tanımındaki "cezâ" da Kur'an'da insanın yaratılışına bağlanır: {ar:إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا, tr:inne'l-insâne hulika helûâ, gloss:insan çok sabırsız yaratıldı, source:70:19} ve {ar:إِذَا مَسَّهُ ٱلشَّرُّ جَزُوعًۭا, tr:izâ messehu'ş-şerru cezûâ, gloss:ona kötülük dokununca feryat eder, source:70:20}. Peki zorluktan geçmeden varılacağını sanan ne olur? Allah müminlere {ar:أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ, tr:em hasibtum en tedhulu'l-cennete, gloss:yoksa cennete gireceğinizi mi sandınız, source:2:214} der ve öncekilere {ar:مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟, tr:messethumu'l-be'sâu ve'd-darrâu ve zulzilû, gloss:onlara darlık ve sıkıntı dokundu ve sarsıldılar, source:2:214} diye hatırlatır. Zorluğun yanındaki kolaylık da açıkça söylenir: {ar:فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا, tr:fe-inne mea'l-usri yusrâ, gloss:şüphesiz zorlukla birlikte kolaylık vardır, source:94:5}.

Kaynaklar: 90:10 ٱلنَّجْدَيْنِ ن ج د B001, B002, B003, B004, B005, B006, B010; 90:10 وَهَدَيْنَٰهُ ه د ي B001, B003; 90:11 ٱقْتَحَمَ ق ح م B001, B002; 90:11 ٱلْعَقَبَةَ ع ق ب B002, B003, B006, B012; 90:12 ٱلْعَقَبَةُ ع ق ب B012; 90:6 أَهْلَكْتُ ه ل ك B006, B009; 90:1 ٱلْبَلَدِ ب ل د B005, B007; 90:4 كَبَدٍ ك ب د B002, B003; 90:14 مَسْغَبَةٍۢ س غ ب B001; 90:17 بِٱلصَّبْرِ ص ب ر B001, B006, B013; 90:19 كَفَرُوا۟ ك ف ر B013

## Gözetleyen göz

Yedinci ayetin sorusu görmekle ilgilidir: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebu en lem yerahû ehad, gloss:onu hiç kimsenin görmediğini mi sanıyor, source:90:7}. Görmek duyuyla algılamaktır: {ar:الرؤية إدراك المرئي بالحاسة, tr:er-ru'yetu idrâku'l-mer'iyyi bi'l-hâssa, gloss:görme görüleni duyu ile algılamaktır, source:"ر ء ي,B001"}. Arapça "kimse yok" demek için "göz yok" da der: {ar:ما بها عين متحركة الياء تريد أحدا له عين, tr:mâ bihâ ayen, gloss:orada gözü olan kimse yok, source:"ع ي ن,B017"}. Bir başka söyleyiş de {ar:ما بها عائن، وكذلك ما بها عين، أي أحد, tr:mâ bihâ âin ve kezâlike mâ bihâ ayn ey ehad, gloss:orada gören yok ve göz yok yani kimse yok, source:"ع ي ن,B017"}. Dil "ehad" ile "ayn"ı aynı yere koyar. Böylece yedinci ayetin "kimse görmedi" sözü ile sekizinci ayetin {ar:أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ, tr:e-lem nec'al lehû ayneyn, gloss:ona iki göz vermedik mi, source:90:8} sorusu yan yana gelir. Adam gözü olan kimse bulunmadığını sanar, ve hemen ona verilmiş iki göz hatırlatılır. Gözü yapan, görmeyi bilmez mi? Göz kelimesinin ailesinde önce gören göz vardır: {ar:العين الناظرة لكل ذي بصر, tr:el-aynu'n-nâzıratu li-kulli zî basar, gloss:göz bakan her canlının bakan organıdır, source:"ع ي ن,B001"}. Koruyan göz de vardır: {ar:فلان بعيني أي أحفظه وأراعيه, tr:fulânun bi-aynî ey ehfazuhû ve urâ'îh, gloss:o benim gözümün önündedir yani onu korur ve gözetirim, source:"ع ي ن,B003"}. Haber toplayan göz, yani casus da vardır: {ar:العين الذي تبعثه يتجسس الخبر, tr:el-aynu'llezî teb'asuhû yetecessesu'l-haber, gloss:ayn haber toplamak için gönderdiğin casustur, source:"ع ي ن,B005"}.

Dördüncü ayetin "insân" kelimesinin ailesinde bir görüntü daha vardır: {ar:إنسان العين المثال الذي يرى في السواد أي سواد العين, tr:insânu'l-ayni'l-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı gözün karasında görünen küçük suret, source:"ء ن س,B005"}. Birinin gözüne bakan, o gözün karasında kendi küçük suretini görür. Aynı kök görmeyi de bilir: {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:âneztu'ş-şey'e izâ raeytuh, gloss:bir şeyi gördüğümde ya da duyduğumda onu ânestu, source:"ء ن س,B002"}. Kendini görülmez sanan insan, kelimenin ailesiyle duyulduğunda, bir gözün içinde görünen surettir.

Surenin öbür kelimeleri gözetleyenlerle doludur. On üçüncü ayetin {ar:رَقَبَةٍ, tr:rakabe, gloss:boyun, source:90:13} kelimesinin kökü beklemeyi ve gözetmeyi anlatır: {ar:رقبت الشيء أرقبه أي انتظرت والترقب تنظر الشيء وتوقعه, tr:rakabtu'ş-şey'e erkubuhû ey intazartu, gloss:bir şeyi gözettim yani bekledim; terakkub bir şeyi gözleyip ummaktır, source:"ر ق ب,B001"}. Bekçi de bu kökten gelir: {ar:الرقيب وهو الحافظ, tr:er-rakîbu ve huve'l-hâfız, gloss:rakîb koruyandır, source:"ر ق ب,B002"}. Gözetleme yeri de öyle: {ar:المرقبة هي المنظرة في رأس جبل أو حصن, tr:el-markabetu hiye'l-menzaratu fî ra'si cebelin ev hısn, gloss:markabe bir dağın ya da kalenin tepesindeki gözetleme yeridir, source:"ر ق ب,B003"}. On birinci ayetin geçidi bir dağdadır. Bu kökle duyulunca dağın tepesinde bir gözetleme yeri de belirir. Avcının siperi de bu kökle anılır: {ar:الرقيبة كل ما استترت به لترمي صيدا, tr:er-rakîbetu kullu mestetarte bihî li-termiye saydâ, gloss:rakîbe av vurmak için arkasına saklandığın her şeydir, source:"ر ق ب,B011"}. On ikinci ayetin {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ, tr:ve mâ edrâke me'l-akabe, gloss:sarp geçidin ne olduğunu sana ne bildirdi, source:90:12} sorusundaki fiilin ailesinde de bir avcı vardır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarraytu's-sayde izâ nazartu eyne huve ve lem terahu ba'd, gloss:avın nerede olduğuna baktım ama onu henüz görmedim ve ona sinsice yaklaştım, source:"د ر ي,B003"}. Fiil, yedinci ayetteki görme fiilini kendi tanımında kullanır. Bilmek de bu kökle söylenir, ve bildiren Allah'tır: {ar:دريت الشيء والله أدرانيه, tr:deraytu'ş-şey'e vallâhu edrânîh, gloss:şeyi bildim ve onu bana Allah bildirdi, source:"د ر ي,B001"}. On dokuzuncu ayetin {ar:بِـَٔايَٰتِنَا, tr:bi-âyâtinâ, gloss:ayetlerimizi, source:90:19} kelimesi de uzaktan görülen bir işarettir: {ar:الآية العلامة, tr:el-âyetu'l-alâme, gloss:ayet işarettir, source:"ء ي ي,B003"} ve {ar:آية الرجل شخصه, tr:âyetu'r-raculi şahsuh, gloss:adamın ayeti uzaktan görünen bedenidir, source:"ء ي ي,B003"}. Kök birini bu görünen bedeninden hedef almayı da bilir: {ar:تآييته وتأييته إذا قصدت آيته وتعمدته, tr:teâyeytuhû izâ kasadtu âyetehû ve teammedtuh, gloss:onun görünen bedenini hedef alıp ona yöneldim, source:"ء ي ي,B002"}. Ayetleri inkâr edenler görülmesi gereken işaretleri örtenlerdir.

Bu görüntünün düz bir anlatımın veremeyeceği yanı şudur. Yedinci ayetteki sanı tek bir boşluk üstüne kuruludur: gözetleyen bir göz yoktur. Surenin kelimeleri ise bu boşluğu gözle, bekçiyle, tepe gözcüsüyle, siperdeki avcıyla doldurur. On ikinci ayet bu gözetimi hitap edilene çevirir: geçidin ne olduğunu insan kendisi göremez, bildirilmesi gerekir. Kur'an'da "ve mâ edrâke" sorusu çoğu kez ateşe açılır. Terazileri hafif gelen için {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10} denir ve cevap {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11} olur. Mal toplayıp sayan için {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:hutamenin ne olduğunu sana ne bildirdi, source:104:5} denir ve cevap {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nârullâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6} olur. Bu surede aynı soru bir boyunu çözmeye ve bir ağzı doyurmaya açılır. Kitabı sol eline verilen adam ise o gün aynı fiili kendine çevirir: {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hısâbiyeh, gloss:hesabımın ne olduğunu bilmeseydim, source:69:26}.

Kur'an'da görmenin sahneleri bu sanıyı tek tek bozar. Kulu namazdan alıkoyan adam için {ar:أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ, tr:e-lem ya'lem bi-ennallâhe yerâ, gloss:Allah'ın gördüğünü bilmiyor mu, source:96:14} denir. Önceki surede, helak edilen kavimlerin ardından {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin gerçekten gözetleme yerindedir, source:89:14} denir. Allah insanı yarattığını, onun içinden geçeni bildiğini söyler ve {ar:وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve nahnu akrabu ileyhi min hableli'l-verîd, gloss:biz ona şah damarından daha yakınız, source:50:16} der. Ardından {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözetleyici vardır, source:50:18} gelir. Söz, insan ve gözetleyici: altıncı ayetin "yekûlu"su da böyle bir rakîbin önünde söylenir. Ateşe sürülen Allah düşmanlarının kulakları, gözleri ve derileri onlara karşı tanıklık eder: {ar:شَهِدَ عَلَيْهِمْ سَمْعُهُمْ وَأَبْصَٰرُهُمْ وَجُلُودُهُم, tr:şehide aleyhim sem'uhum ve ebsâruhum ve culûduhum, gloss:kulakları ve gözleri ve derileri onlar aleyhine tanıklık etti, source:41:20}. Onlara söylenen söz sanıyı adlandırır: {ar:وَلَٰكِن ظَنَنتُمْ أَنَّ ٱللَّهَ لَا يَعْلَمُ كَثِيرًۭا مِّمَّا تَعْمَلُونَ, tr:ve lâkin zanentum ennallâhe lâ ya'lemu kesîran mimmâ ta'melûn, gloss:ama yaptıklarınızın çoğunu Allah'ın bilmediğini sandınız, source:41:22}. Verilen göz, sahibi aleyhine tanık olur. Yedinci ayetteki fiil başka bir surede tersine döner, bu kez gören yapanın kendisidir: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığınca iyilik yaparsa onu görür, source:99:7}. Göze emanet etmek de Allah'ın sözünde vardır. Musa'ya, annesinin onu sandığa koyup suya bırakışını hatırlatırken {ar:وَلِتُصْنَعَ عَلَىٰ عَيْنِىٓ, tr:ve li-tusna'a alâ aynî, gloss:benim gözümün önünde yetiştirilesin diye, source:20:39} der. Verilip kullanılmayan göz de anılır: {ar:وَلَهُمْ أَعْيُنٌۭ لَّا يُبْصِرُونَ بِهَا, tr:ve lehum a'yunun lâ yubsırûne bihâ, gloss:gözleri vardır ama onlarla görmezler, source:7:179}. Semud da yol gösterilip körlüğü seçmiştir: {ar:وَأَمَّا ثَمُودُ فَهَدَيْنَٰهُمْ فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ, tr:ve emmâ semûdu fe-hedeynâhum fe'stehabbu'l-amâ ale'l-hudâ, gloss:Semud'a gelince onlara yol gösterdik ama körlüğü hidayete tercih ettiler, source:41:17}. Göz ile yol orada da birbirine bağlıdır: {ar:وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ, tr:ve lev neşâu le-tamesnâ alâ a'yunihim fe'stebeku's-sırâta fe-ennâ yubsırûn, gloss:dileseydik gözlerini silerdik de yola koşuşurlardı ama nasıl görebilirlerdi, source:36:66}. Gözü veren de ayrıca anılır: {ar:وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ, tr:ve ce'ale lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide, gloss:size kulaklar ve gözler ve gönüller verdi, source:67:23}. Örtünün kalkışı da bir sahne olarak verilir: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık; bugün gözün keskindir, source:50:22}. Göz sonunda yakıcı olanı da görür: {ar:ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ, tr:summe le-teravunnehâ ayne'l-yakîn, gloss:sonra onu kesin bir gözle göreceksiniz, source:102:7}.

Kaynaklar: 90:7 يَرَهُۥٓ ر ء ي B001; 90:7 أَحَدٌ ء ح د B002; 90:8 عَيْنَيْنِ ع ي ن B001, B003, B005, B017; 90:4 ٱلْإِنسَٰنَ ء ن س B002, B005; 90:13 رَقَبَةٍ ر ق ب B001, B002, B003, B011; 90:12 أَدْرَىٰكَ د ر ي B001, B003; 90:19 بِـَٔايَٰتِنَا ء ي ي B002, B003

## Buluşmalar

Görüntülerin en sık buluştuğu sahne yoldur. Onuncu ayetteki "necd" yolu kendi kendine yol gösterir, ateşin kökü de yüksek yerde yol gösterilsin diye yakılan ateşi anlatır. Sırt ile işaret ateşi aynı işi görür: gece yolcusuna nereye çıkacağını göstermek. Musa'nın sahnesi bu iki görüntüyü tek bir ayette taşır: dağın yanında görülen ateş ve {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} umudu. Bu surede ise yolun sonundaki ateş bir işaret değildir, üstü kapatılmıştır. Yol sahnesiyle ateş sahnesi arasındaki fark, bir yolculuğun nasıl tersine döndüğünü gösterir. Atılmayan geçidin karşısında, içine dalınan bir ateş vardır: {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59}. Sabrın kökü de bu iki sahne arasında ikiye bölünür. Yokuşta kendini panikten tutan sabır vardır. Bir de kitabı gizleyenlerin {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} sözündeki ateşe cüret vardır.

İkinci büyük buluşma boyunla kapak arasındadır. On üçüncü ayetin fiili Arapçada kapalıyı açmak olarak tanımlanır: {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"}. Yirminci ayetin fiili de kapamak olarak tanımlanır: {ar:أوصدت الباب أغلقته, tr:evsadtu'l-bâbe ağlaktuh, gloss:kapıyı kapattım yani kilitledim, source:"و ص د,B001"}. Sure açılan bir boyundan kapanan bir ateşe doğru ilerler, ve iki fiil birbirinin tam tersidir. Bu iki ucu Kur'an'da tek bir sahne birleştirir. Kitabı sol eline verilen adamın boynu bağlanır ve bunun sebebi yoksulun yemeğine teşvik etmemesidir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Sol taraf, boyundaki halka ve doyurulmayan yoksul bir aradadır. Malının bir işe yaramadığını söyleyen ve gücünün yok olup gittiğini gören de aynı adamdır. Bu sahnede sağ ile sol, harcanan mal, kıtlık ve boyun görüntüleri aynı yerde durur. Altıncı ayetteki "tükettim" orada şu söze döner: {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}.

Üçüncü buluşma yeminle geçit arasındadır. Yeminin kefareti ayeti, surenin on üçüncü ve on dördüncü ayetlerini birlikte sayar. Yeminler düğümlenir, sonra on yoksul doyurulur ya da bir boyun çözülür. Birinci ayetin yemini, ikinci ayetin "hıll"i, geçidin iki işi, on sekizinci ayetin sağ eli ve on dokuzuncu ayetin örtme kökü, bir yeminin bağlanıp çözülmesinin bütün aşamalarını taşır. Kur'an'ın bahçe sahipleri ise yemini ters yönde kullanır: yoksulu dışarıda bırakmak için yemin ederler. Bu ikisinin karşı karşıya gelmesi, surenin açılış yemininin neye açıldığını gösterir. Bu yemin bir şehirle başlar, şehirdeki yoksulun ağzıyla devam eder.

Gözetleyen göz ile harcanan mal, gösteriş kelimesinde buluşur. Gösteriş için harcayan, insanların görmesini ister ama Allah'ın görmediğini sanır. Bu çelişki tek bir ayette sahnelenir: malını {ar:رِئَآءَ ٱلنَّاسِ, tr:riâe'n-nâs, gloss:insanlara gösteriş için, source:2:264} harcayanın emeği kayanın üstündeki toprak gibi yıkanır gider. Aynı misal yere yapışma görüntüsünü de taşır: toprak, kaya ve yağmurla çıplak kalan taş. Ölçme görüntüsü de aynı ayete girer: {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264}. "Kimse bana güç yetiremez" sanısı, kendi kazancına güç yetirememekle biter. Ölçme ile yol da Kur'an'da tek bir dizide buluşur, ve bu dizi surenin sırasıdır: yaratan, ölçen, yol gösteren.

Soy ile kıtlık "yetim" kelimesinde buluşur. Babasından kopan çocuk, iyiliğin geç ulaştığı ve açlık gününde açlık çeken çocuktur. Dil bu ikisini tek bir örnekte birleştirir: {ar:يتيم ذو مسغبة أي ذو مجاعة, tr:yetîmun zû mesğabe ey zû mecâa, gloss:açlık sahibi yetim yani kıtlık içindeki yetim, source:"س غ ب,B001"}. Şehir ile kıtlık da kıtlık yılının tanımında buluşur: yıl bedevileri şehirlere atar. Kur'an'da doyurulan şehrin sahnesi de buradadır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvenliğe kavuşturan, source:106:4}. Yere yapışma ile geçit, yükselme ile saplanmanın aynı ayette karşı karşıya geldiği sahnede buluşur: ayetlerle yükseltilebilecekken yere saplanan adam. Bu da on dokuzuncu ayetin ayetleri inkâr edenlerine bağlanır.

Bütün bu görüntüler birlikte surenin hareketini taşır. Hareket yere oturmuş bir şehirde başlar. İnsan zorluğun ortasında yaratılmıştır. Malı keçeleşmiştir, kendini görülmez ve ölçülmez sanır. Ona gözler, dil ve dudaklar verilmiş, önüne görünen iki sırt konmuştur. İstenen şey yukarıya atılmaktır. Bu atılış da yere yapışmış olana eğilmek, bir boynun düğümünü çözmek ve aç bir ağza yemek koymaktır. Böyle atılanlar bitkiler gibi birbirine bitişir, aynı rahimden çıkmış gibi birbirine acır ve sağ tarafa yerleşir. Ayetleri örtenlerin üstü ise, yolda yol gösterebilecek bir ateşle kapatılır. Mağara sahnesindeki eşikte köpek ön ayaklarını uzatmış yatar: {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri iki ön ayağını eşiğe uzatmıştı, source:18:18}. Aynı ayette uyuyanlar sağa ve sola çevrilir. Yirminci ayetin kökü, sağ ve sol ile o eşiği orada tek bir sahnede bir araya getirir.

