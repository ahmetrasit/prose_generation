Focus: 114:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/114_4/D.r13/context.md =====
# 114:4 — focus

مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ

Anchor translation (canonical reading, reference only):

Geri çekilen vesvesecinin kötülüğünden.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مِن | مِن |  | P |
| 2 | شَرِّ | شَرّ | ش ر ر | N |
| 3 | ٱلْوَسْوَاسِ | وَسْوَاس | و س و س | DET;N |
| 4 | ٱلْخَنَّاسِ | خَنَّاس | خ ن س | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 114 — full text (context; no pericope)

- 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- 114:2 مَلِكِ ٱلنَّاسِ
- 114:3 إِلَٰهِ ٱلنَّاسِ
- 114:4 ◀ focus مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- 114:5 ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- 114:6 مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ


===== _commentary/v16/work/114_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ر ر (root_000787) — identity root of شَرِّ (w2)

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## و س و س (root_001651) — identity root of ٱلْوَسْوَاسِ (w3)

- **B001** sessiz iç konuşma veya kötülüğe yönelten iç telkin — sessiz iç konuşma; kötülüğe yönelten iç telkin · birinin içine kötü bir düşünce düşürmek veya ona içten telkinde bulunmak · insanın göğsünde sessiz bir iç konuşma belirmek · iç telkinlerin etkisine kapılmış, sürekli kuruntu duyan · sessiz iç konuşma veya iç fısıltı
  الوسوسة حديث النفس؛ وسوس إلي ووسوس في صدري (ayn)؛ الوسوسة ما يلقيه الشيطان في القلب (jamhara)؛ الوسوسة حديث النفس؛ وسوست إليه نفسه؛ فوسوس لهما الشيطان (sihah)؛ الوسوسة الخطرة الرديئة؛ فوسوس إليه الشيطان (mufradat)
- **B002** belli belirsiz ses veya hafif hareket sesi — gizli, hafif ses veya duyulabilen belli belirsiz hareket sesi · bir nesnenin duyulan hafif hareket sesi
  الوسواس الصوت الخفي من ريح تهز قصبا ونحوه؛ صوت الحلي؛ همس الصائد وكلامه (ayn)؛ وسوسة الشيء إذا سمعت حركته (jamhara)؛ همس الصائد والكلاب وأصوات الحلى وسواس (sihah)؛ صوت الحلي والهمس الخفي؛ همس الصائد وسواس (mufradat)
- **B003** kötülüğe sürükleyen görünmez varlığın sözlükleşmiş adı — kötülüğe sürükleyen görünmez varlığın adı
  الوسواس اسم الشيطان (ayn;sihah)

## خ ن س (root_000443) — identity root of ٱلْخَنَّاسِ (w4)

- **B001** geri çekilip gizlenme — geri çekilmek, gizlenmek veya içe kapanmak · birini geride bırakmak veya ona düşen payı geciktirmek · parmağını içe doğru kapatmak · birini veya bir şeyi gözden saklamak ya da gizli bir yere sokmak · Tanrı anıldığında geri çekilen kötü düşünce fısıldayıcısı · içe kapanma ve gizlenme
  أصل واحد يدل على استخفاء وتستر؛ خنست عنه؛ وأخنست عنه حقه (maqayis;mufradat;tahdhib)؛ الخنوس الانقباض والاستخفاء؛ الشيطان يوسوس فإذا ذكر الله خنس (ayn;tahdhib;mufradat)؛ خنس الرجل عن القوم إذا مضى في خفية (jamhara)؛ خنس عنه يخنس أي تأخر؛ خنسته فخنس أي أخرته فتأخر وقبضته فانقبض (sihah;tahdhib)؛ خنس به أي وراه ويقال تخنس بهم أي تغيب بهم (tahdhib)
- **B002** gizlenen veya seyrinde geri dönen gök cisimleri — gizlenen, batan veya seyrinde geri dönen gök cisimleri · gök cisimlerinin gündüz görünmez olması veya seyrinde geri dönmesi
  الخنس النجوم تخنس في المغيب (maqayis;jamhara)؛ الخنس الكواكب الخمسة التي تجري وتخنس في مجراها حتى يخفى ضوء الشمس وخنوسها اختفاؤها بالنهار (ayn)؛ الخنس الكواكب كلها لأنها تخنس في المغيب أو لأنها تخفى بالنهار؛ النجوم الخمسة تخنس في مجراها وتكنس (sihah;tahdhib)؛ الكواكب التي تخنس بالنهار؛ تخنس في مجراها أي ترجع (mufradat)
- **B003** burun köprüsü çökük, ucu geniş veya kalkık olma — burun köprüsünün çökük, ucunun geniş veya kalkık oluşu · burun köprüsü çökük, ucu geniş veya kalkık olan · bu burun biçimine sahip dişi veya kadın; bu özellikteki inek · bu burun biçimine sahip olanlar · aslanın yüz ve burnuna özgü bir nitelik
  الخنس في الأنف انحطاط القصبة والبقر كلها خنس (maqayis)؛ الخنس انقباض قصبة الأنف وعرض الأرنبة كأنف البقرة الخنساء؛ والترك خنس (ayn;tahdhib)؛ الخنس ارتفاع أرنبة الأنف وانحطاط القصبة؛ تأخر الأنف إلى الرأس وارتفاعه من الشفة؛ رجل أخنس وامرأة خنساء وقوم خنس؛ البقر كلها خنس (jamhara)؛ الخنس تأخر الأنف عن الوجه مع ارتفاع قليل في الأرنبة (sihah)؛ الخنوس من صفات الأسد في وجهه وأنفه (tahdhib)
- **B004** ceylan sığınağı veya ceylanlar — ceylan sığınağı · ceylanlar
  الخنس مأوى الظباء؛ الخنس الظباء أنفسها (tahdhib)
- **B005** koşarken sağa sola sapan at [kalıp] — koşarken sağa ve sola sapan at
  فرس خنوس وهو الذي يعدل وهو مستقيم في حضره ذات اليمين وذات الشمال (tahdhib)

## ECHO ش ر ي (root_000792) — for شَرِّ (w2): withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

===== _commentary/v16/out/s114/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 114:4, and ## Buluşmalar) =====
## Görünen ve örtülü

Surenin son ayeti iki kelimeyi yan yana koyar: {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} ve {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:6}. Bu iki kelimenin kökleri birbirine karşı tanımlanır. İnsan, görünür olduğu için bu adı alır: {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-ins hilâfu'l-cinn ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için bu adı almışlardır, source:"ء ن س,B001"}. Cin ise gözden örtülü olduğu için: {ar:الجن سموا بذلك لأنهم متسترون عن أعين الخلق, tr:el-cinn summû bi-zâlike li-ennehum mütesettirûne an a'yuni'l-halk, gloss:cinler yaratılmışların gözlerinden örtülü oldukları için böyle adlandırıldı, source:"ج ن ن,B005"}. Kökün işleyişi tek bir harekettir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenn setru'ş-şey'i ani'l-hâsse, gloss:cenn kökünün aslı bir şeyi duyudan örtmektir, source:"ج ن ن,B001"}. Bu kök imgeleri her yerde kelimenin ayetteki anlamının yanında duyulur, onun yerine geçmez: ayette "insanlar" ve "cinler" kastedilir, imge bu anlamın arkasından gelen yankıdır.

Bu karşıtlık geriye doğru okunur. "Rab", "Melik", "İlah" diye üç kez anılan ve beşinci ayette göğüsleri hedef alınan "insanlar", altıncı ayete gelince görünenler olarak belirir. Aynı kök görmeyi ve işitmeyi de adlandırır: {ar:آنسته أبصرته وآنست الصوت سمعته, tr:âneston-hu ebsartu-hû ve âneste's-savte semi'tu-hû, gloss:onu fark ettim, gördüm; sesi fark ettim, işittim, source:"ء ن س,B002"}. Görünenler aynı zamanda algılayanlardır. Onlara işleyen ise algının hemen altında durur. Dördüncü ayetin {ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} kelimesi gizli bir sestir: {ar:الوسواس الصوت الخفي من ريح تهز قصبا ونحوه, tr:el-vesvâsu's-savtu'l-hafiyyu min rîhin tehuzzu kasaben, gloss:vesvas, kamışı sallayan rüzgârın gizli sesidir, source:"و س و س,B002"}; yalnızca bir kıpırtı olarak duyulur. Yanındaki {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} saklanmayı ve örtünmeyi söyler {source:"خ ن س,B001"}. Kötülüğün kendi kelimesi {ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} ise ters yönü taşır: {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşertu'ş-şey'e izâ ebraztuhû ve azhartuhû, gloss:bir şeyi ortaya çıkarıp görünür kıldığımda "eşrartu" derim, source:"ش ر ر,B008"} ve {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastuke'ş-şey'e fi'ş-şems, gloss:şerr, bir şeyi güneşe sermendir, source:"ش ر ر,B002"}. Kötülük bir açığa çıkarma kökünden adlandırılır, ama saklanan birine aittir.

Kuran bu sahneyi bahçede kurar. Şeytan Âdem'le eşine fısıldar ve fısıltının amacı açıkça söylenir: {ar:فَوَسْوَسَ لَهُمَا ٱلشَّيْطَٰنُ لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا مِن سَوْءَٰتِهِمَا, tr:fe-vesvese lehume'ş-şeytânu li-yubdiye lehumâ mâ vûriye anhumâ min sev'âtihimâ, gloss:şeytan onlara örtülü kalan çıplaklıklarını açmak için fısıldadı, source:7:20}. İki ayet sonra iş tamamlanır: {ar:بَدَتْ لَهُمَا سَوْءَٰتُهُمَا, tr:bedet lehumâ sev'âtuhumâ, gloss:çıplaklıkları kendilerine göründü, source:7:22}. Saklananın işi açığa çıkarmakla biter. Hemen ardından Allah Âdemoğullarına seslenir ve gözün dengesizliğini adlandırır: {ar:إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ, tr:innehû yerâkum huve ve kabîluhû min haysu lâ terevnehum, gloss:o ve onun takımı, sizin onları göremediğiniz yerden sizi görür, source:7:27}. Surenin görünen insanları, görülmeden gören birine karşı korunmaktadır. Kuran'da cinlerin kendi anlatımı ise sığınmanın yanlış yöne döndüğü bir durumu bildirir: {ar:رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ فَزَادُوهُمْ رَهَقًۭا, tr:ricâlun mine'l-insi yeûzûne bi-ricâlin mine'l-cinni fe-zâdûhum rehakâ, gloss:insten bazı adamlar cinden bazı adamlara sığınırdı, bu da onların azgınlığını artırdı, source:72:6}. Surenin "insanların Rabbine sığınırım" sözü bu sapmanın düzeltilmiş halidir: sığınma görünmeyen tarafa değil, iki tarafın da Rabbine yönelir.

Altıncı ayet fısıldayanın iki sınıftan çıkabileceğini söyler. Kuran aynı ikiliyi peygambere düşmanlık bağlamında verir: {ar:شَيَٰطِينَ ٱلْإِنسِ وَٱلْجِنِّ يُوحِى بَعْضُهُمْ إِلَىٰ بَعْضٍۢ زُخْرُفَ ٱلْقَوْلِ غُرُورًۭا, tr:şeyâtîne'l-insi ve'l-cinni yûhî ba'duhum ilâ ba'din zuhrufe'l-kavli gurûrâ, gloss:ins ve cin şeytanları aldatmak için birbirlerine yaldızlı söz fısıldar, source:6:112}. Yani görünenler de örtülü bir iş yapabilir. Surenin son ifadesi, Kuran'da başka yerde de aynı sözcüklerle durur: {ar:لَأَمْلَأَنَّ جَهَنَّمَ مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ أَجْمَعِينَ, tr:le-emleenne cehenneme mine'l-cinneti ve'n-nâsi ecmaîn, gloss:cehennemi cinlerden ve insanlardan dolduracağım, source:11:119}, {source:32:13}. Yaratılışları da yan yana konur: insan kuru balçıktan {source:55:14}, cann ateşten {source:55:15}. Sonunda yoldan çıkmış olanlar, görmedikleri saptırıcıları görmek ister: {ar:رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ, tr:rabbenâ erine'llezeyni edallânâ mine'l-cinni ve'l-ins, gloss:Rabbimiz, bizi saptıran cin ve insi bize göster, source:41:29}. Görünmezlik orada biter.

Kaynaklar: 114:1–3, 5, 6 ٱلنَّاسِ ء ن س B001; 114:5, 6 ٱلنَّاسِ ء ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B005; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B001; 114:4 شَرِّ ش ر ر B008; 114:4 شَرِّ ش ر ر B002

## Söz: içte kurulan, dile çıkan, insanlar arasında yayılan

Sure bir emirle açılır: {ar:قُلْ, tr:kul, gloss:de, source:114:1}. Söz, telaffuzla dışarı çıkarılan şeydir: {ar:المركب من الحروف المبرز بالنطق, tr:el-murakkabu mine'l-hurûfi'l-mubrazu bi'n-nutk, gloss:harflerden kurulup konuşmayla dışarı çıkarılan, source:"ق و ل,B001"}. Ama aynı kök sözün içteki halini de söz sayar: {ar:المتصور في النفس قبل الإبراز باللفظ قول, tr:el-mutasavveru fi'n-nefsi kable'l-ibrâzi bi'l-lafz kavl, gloss:lafızla dışarı çıkarılmadan önce nefiste kurulan şey de sözdür, source:"ق و ل,B012"}. Sözün organı da adını kökten alır: {ar:المقول اللسان, tr:el-mikvel el-lisân, gloss:mikvel dildir, source:"ق و ل,B002"}. "De" emri bu yolu tarif eder: sığınma içte kurulur, dile gelir, dışarı söylenir.

Fısıltı aynı yolu ters yönde yürür. O da bir konuşmadır ama dışarı çıkmaz: {ar:الوسوسة حديث النفس؛ وسوست إليه نفسه, tr:el-vesvesetu hadîsu'n-nefs; vesveset ileyhi nefsuh, gloss:vesvese nefsin konuşmasıdır; nefsi ona fısıldadı, source:"و س و س,B001"}. Sesi bir mırıltıya indirilmiştir: {ar:صوت الحلي والهمس الخفي, tr:savtu'l-huliyyi ve'l-hemsu'l-hafiyy, gloss:takıların sesi ve gizli fısıltı, source:"و س و س,B002"}. Biri içten dışa çıkan söz, öbürü dıştan göğse giren söz. Kök iki şeyi daha bilir: iyi ya da kötü bir sözü kendi üstüne çekmek, {ar:اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر, tr:iktâle kavlen ey icterra ilâ nefsihî kavlen min hayrin ev şerr, gloss:iyi ya da kötü bir sözü kendine çekti, source:"ق و ل,B006"}, ve hiçbir hitap gelmediği halde içe düşen ilhamı söz diye adlandırmak {source:"ق و ل,B017"}. Fısıltının iyi ikizi budur: o da sessiz bir sözdür.

Kök sözün insanlar arasında yayılmasını da adlandırır: {ar:القالة القول الفاشي في الناس, tr:el-kâletu'l-kavlu'l-fâşî fi'n-nâs, gloss:kâle insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. Karşılıklı konuşmayı {source:"ق و ل,B009"} ve birine yalan söz yüklemeyi de {source:"ق و ل,B005"}. Altıncı ayetin "insanlardan da" demesi bu kanalı açar: fısıltı insan dilinden insan kulağına da gelir. Son halka işiten insandır: {ar:آنست الصوت سمعته, tr:âneste's-savte semi'tuh, gloss:sesi fark ettim, işittim, source:"ء ن س,B002"}.

Kuran bu çerçeveyi aynı kalıpla verir. Peygambere emredilir: {ar:وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَٰتِ ٱلشَّيَٰطِينِ, tr:ve kul rabbi eûzu bike min hemezâti'ş-şeyâtîn, gloss:de ki: Rabbim, şeytanların dürtmelerinden sana sığınırım, source:23:97}. Okunan söz de sığınmayla başlar: {ar:فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ فَٱسْتَعِذْ بِٱللَّهِ مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:fe-izâ kara'te'l-kur'âne festeiz billâhi mine'ş-şeytâni'r-racîm, gloss:Kuran okuduğunda kovulmuş şeytandan Allah'a sığın, source:16:98}. Bahçede fısıltı açık söze döner: {ar:وَقَالَ مَا نَهَىٰكُمَا رَبُّكُمَا, tr:ve kâle mâ nehâkumâ rabbukumâ, gloss:ve dedi: Rabbiniz sizi ancak şunun için yasakladı, source:7:20}, ardından yemine {source:7:21}. Başka bir anlatımda fısıltı bir teklif biçimini alır: {ar:فَوَسْوَسَ إِلَيْهِ ٱلشَّيْطَٰنُ قَالَ يَٰٓـَٔادَمُ هَلْ أَدُلُّكَ, tr:fe-vesvese ileyhi'ş-şeytânu kâle yâ âdemu hel edulluke, gloss:şeytan ona fısıldadı, dedi: Ey Âdem, sana göstereyim mi, source:20:120}. Gizli söz insan tartışmasına da çıkar: {ar:وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ, tr:ve inne'ş-şeyâtîne le-yûhûne ilâ evliyâihim li-yucâdilûkum, gloss:şeytanlar sizinle tartışsınlar diye dostlarına fısıldar, source:6:121}. İnsanlar arasındaki gizli konuşma da aynı kaynaktandır: {ar:إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ, tr:innema'n-necvâ mine'ş-şeytân, gloss:gizli konuşma şeytandandır, source:58:10}. Dilden dile yayılan söz de anlatılır: {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ وَتَقُولُونَ بِأَفْوَاهِكُم مَّا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ, tr:iz telakkavnehû bi-elsinetikum ve tekûlûne bi-efvâhikum mâ leyse lekum bihî ilm, gloss:onu dillerinizle birbirinizden alıyor, bilmediğiniz şeyi ağızlarınızla söylüyordunuz, source:24:15}. Karşı tedbir de sözdür: {ar:وَقُل لِّعِبَادِى يَقُولُوا۟ ٱلَّتِى هِىَ أَحْسَنُ ۚ إِنَّ ٱلشَّيْطَٰنَ يَنزَغُ بَيْنَهُمْ, tr:ve kul li-ibâdî yekûlu'lletî hiye ahsen, inne'ş-şeytâne yenzeğu beynehum, gloss:kullarıma söyle, en güzel olanı söylesinler; şeytan aralarına girip kışkırtır, source:17:53}. Ve indirilen söz şeytanın sözü değildir: {ar:وَمَا هُوَ بِقَوْلِ شَيْطَٰنٍۢ رَّجِيمٍۢ, tr:ve mâ huve bi-kavli şeytânin racîm, gloss:o kovulmuş bir şeytanın sözü değildir, source:81:25}; {ar:إِنَّهُۥ لَقَوْلُ رَسُولٍۢ كَرِيمٍۢ, tr:innehû le-kavlu rasûlin kerîm, gloss:o şerefli bir elçinin sözüdür, source:81:19}. "Yalan söz yüklemek" anlamı ise Kuran'da elçiye yöneltilen suçlamada görünür: {ar:أَمْ يَقُولُونَ تَقَوَّلَهُۥ, tr:em yekûlûne tekavveleh, gloss:yoksa "onu kendisi uydurdu" mu diyorlar, source:52:33}, {source:69:44}.

Kaynaklar: 114:1 قُلْ ق و ل B001; 114:1 قُلْ ق و ل B012; 114:1 قُلْ ق و ل B002; 114:1 قُلْ ق و ل B007; 114:1 قُلْ ق و ل B006; 114:1 قُلْ ق و ل B017; 114:1 قُلْ ق و ل B009; 114:1 قُلْ ق و ل B005; 114:4, 5 ٱلْوَسْوَاسِ / يُوَسْوِسُ و س و س B001; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 شَرِّ ش ر ر B008; 114:6 وَٱلنَّاسِ ء ن س B002

## Çekilme ve dönüş; yerinden ayrılmayan

{ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} geri çekilenin adıdır. Kök bir büzülme ve saklanmadır: {ar:الخنوس الانقباض والاستخفاء, tr:el-hunûsu'l-inkıbâdu ve'l-istihfâ, gloss:hunûs büzülme ve gizlenmedir, source:"خ ن س,B001"}; geri kalmak, {ar:خنس عنه يخنس أي تأخر, tr:hanese anhu yahnisu ey teahhar, gloss:ondan geri çekildi, source:"خ ن س,B001"}; ve topluluktan gizlice sıyrılmak, {ar:خنس الرجل عن القوم إذا مضى في خفية, tr:hanese'r-raculu ani'l-kavmi izâ madâ fî hufye, gloss:adam topluluktan gizlice ayrılıp gitti, source:"خ ن س,B001"}. Aynı kök iki kelimeyi tek cümlede birleştirir: {ar:الشيطان يوسوس فإذا ذكر الله خنس, tr:eş-şeytânu yuvesvisu fe-izâ zukira'llâhu hanes, gloss:şeytan fısıldar, Allah anılınca sinip çekilir, source:"خ ن س,B001"}. Dördüncü ayetteki iki sıfat böylece bir işleyiş olur: fısıldamak, sonra anılma karşısında geri çekilmek.

Ama çekilme son değildir. Kökün yıldızları gündüz gizlenir ve yörüngelerinde geri döner: {ar:الكواكب التي تخنس بالنهار؛ تخنس في مجراها أي ترجع, tr:el-kevâkibu'lletî tahnisu bi'n-nehâr; tahnisu fî mecrâhâ ey terci', gloss:gündüz gizlenen yıldızlar; akışlarında geri dönerler, source:"خ ن س,B002"}. Fısıldayanın çekilmesi bir evredir; yeniden görünür. Beşinci ayetin fiili {ar:يُوَسْوِسُ, tr:yuvesvisu, gloss:fısıldar, source:114:5} bunu biçiminde de taşır: kök iki kez tekrar eden bir hecedir (vesvese), ve sesi bir hareketin sesi olarak duyulur: {ar:وسوسة الشيء إذا سمعت حركته, tr:vesvesetu'ş-şey'i izâ semi'te hareketeh, gloss:bir şeyin kıpırtısını işittiğinde vesvesesi denir, source:"و س و س,B002"}. Tekrarlayan bir kıpırtı, gidip gelen bir varlık.

Ona karşı iki şey durur. İlk ayetin {ar:بِرَبِّ, tr:bi-rabbi, gloss:Rabbine, source:114:1} kelimesinin kökü bir yerde kalıp ayrılmamayı adlandırır: {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fulânun bi'l-mekâni izâ ekâme bihî fe-lem yebrahh, gloss:bir yerde kaldı ve oradan ayrılmadı, source:"ر ب ب,B007"}; ve süren bulutu, {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti's-sehâbe ey dâmet, gloss:bulut sürdü, durdu, source:"ر ب ب,B007"}. Sığınma kökü de yapışıp kalmayı bilir: {ar:أطيب اللحم عوذه وهو ما عاذ بالعظم ولزمه, tr:etyebu'l-lahmi uvezuhû ve huve mâ âze bi'l-azmi ve lezimeh, gloss:etin en iyisi kemiğe sığınıp ona yapışan kısımdır, source:"ع و ذ,B004"}. Sahne şöyledir: biri gelir, fısıldar, çekilir, döner; Rab yerinden ayrılmaz; sığınan kemiğe yapışan et gibi ona tutunur. Kök iki ters hareket daha taşır: tiksintiyle birini bırakmak {source:"ع و ذ,B008"} ve korkutan ya da vuran ama öldüremeyen bir saldırıdan kurtulmak {source:"ع و ذ,B006"}. Sığınmak saldırganı yok etmez; kişiyi saldırıdan çıkarır.

Kuran bu yıldızlara yemin eder: {ar:فَلَآ أُقْسِمُ بِٱلْخُنَّسِ, tr:fe-lâ uksimu bi'l-hunnes, gloss:sinip çekilenlere yemin ederim, source:81:15}, {ar:ٱلْجَوَارِ ٱلْكُنَّسِ, tr:el-cevâri'l-kunnes, gloss:akıp yuvalarına girenlere, source:81:16}. Anılmanın işleyişini sahneler: önce emir, {ar:وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ, tr:ve immâ yenzeğanneke mine'ş-şeytâni nezğun festeiz billâh, gloss:şeytandan bir dürtü seni dürterse Allah'a sığın, source:7:200}, sonra sonuç, {ar:إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ, tr:izâ messehum tâifun mine'ş-şeytâni tezekkerû fe-izâ hum mubsirûn, gloss:şeytandan bir dolaşan dokununca hatırlarlar ve hemen görürler, source:7:201}. Aynı emir başka yerde de geçer {source:41:36}. Bedir'de şeytan önce koruyucu kesilir, {ar:إِنِّى جَارٌۭ لَّكُمْ, tr:innî cârun lekum, gloss:ben sizin koruyucunuzum, source:8:48}, iki ordu karşılaşınca {ar:نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌۭ مِّنكُمْ, tr:nekese alâ akibeyhi ve kâle innî berîun minkum, gloss:topukları üstünde geri döndü ve "ben sizden uzağım" dedi, source:8:48}. Aynı geri çekiliş insana "inkâr et" dedikten sonra da gelir {source:59:16}, ve hesaptan sonra da: {ar:وَمَا كَانَ لِىَ عَلَيْكُم مِّن سُلْطَٰنٍ إِلَّآ أَن دَعَوْتُكُمْ, tr:ve mâ kâne liye aleykum min sultânin illâ en de'avtukum, gloss:sizin üzerinizde çağırmaktan başka bir gücüm yoktu, source:14:22}. Ters durum da anlatılır: anılmadan yüz çevirene bir şeytan yoldaş edilir, {ar:وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ, tr:ve men ya'şu an zikri'r-rahmâni nukayyid lehû şeytânen fe-huve lehû karîn, gloss:Rahman'ın anılmasından göz yumana bir şeytan sararız, o onun yoldaşı olur, source:43:36}; anılma unutulunca şeytan ele geçirir {source:58:19}. Anılma yoksa çekilen de yoktur; yerinden ayrılmayan o olur.

Kaynaklar: 114:4 ٱلْخَنَّاسِ خ ن س B001; 114:4 ٱلْخَنَّاسِ خ ن س B002; 114:4–5 ٱلْوَسْوَاسِ / يُوَسْوِسُ و س و س B002; 114:1 بِرَبِّ ر ب ب B007; 114:1 أَعُوذُ ع و ذ B004; 114:1 أَعُوذُ ع و ذ B008; 114:1 أَعُوذُ ع و ذ B006

## Rab, Melik, İlah ve onların küçük sahipleri

İlk üç ayet aynı nesnenin üzerine üç unvan koyar: {ar:بِرَبِّ ٱلنَّاسِ, tr:bi-rabbi'n-nâs, gloss:insanların Rabbine, source:114:1}, {ar:مَلِكِ ٱلنَّاسِ, tr:meliki'n-nâs, gloss:insanların hükümdarına, source:114:2}, {ar:إِلَٰهِ ٱلنَّاسِ, tr:ilâhi'n-nâs, gloss:insanların ilahına, source:114:3}. "İnsanlar" üç kez değişmeden kalır, unvan değişir. Her unvanın kökü daha küçük ya da sahte sahipleri de kapsar. Rab her şeyin sahibidir ve krallara da söylenmiştir: {ar:رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك, tr:rabbu kulli şey' mâlikuh; ve kad kâlûhu fi'l-câhiliyyeti li'l-melik, gloss:her şeyin rabbi onun sahibidir; cahiliyede bunu krala da söylerlerdi, source:"ر ب ب,B001"}; ev rabbi, at rabbi denir, ama kayıtsız "Rab" yalnız Allah içindir {source:"ر ب ب,B001"}. Melik, buyruk ve yasakla tasarruf edendir, {ar:الملك هو المتصرف بالأمر والنهي في الجمهور, tr:el-meliku huve'l-mutasarrifu bi'l-emri ve'n-nehyi fi'l-cumhûr, gloss:melik topluluk içinde emir ve yasakla tasarruf edendir, source:"م ل ك,B003"}; ama insanlar kendilerine de kral yapar: {ar:ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا, tr:mellek'el-kavmu fulânen, gloss:topluluk birini kendilerine kral yaptı, source:"م ل ك,B003"}. Elin sahip olduğu mal da aynı köktendir {source:"م ل ك,B002"}. İlah her tapılandır: {ar:إله اسما لكل معبود, tr:ilâh ismen li-kulli ma'bûd, gloss:ilah her tapılanın adıdır, source:"ء ل ه,B001"}; putlar ve güneş dahil. Sonra belirlilik takısıyla Yaratıcıya özgü kılınır {source:"ء ل ه,B002"}. Surenin ilk kelimesi bile bu sahnede bir küçük kral taşır: {ar:القيل ملك من ملوك حمير دون الملك الأعظم, tr:el-kayl melikun min mulûki himyer dûne'l-meliki'l-a'zam, gloss:kayl, Himyer krallarından en büyük kralın altındaki bir kraldır, source:"ق و ل,B004"}, adını sözünün geçmesinden alır {source:"ق و ل,B004"}.

Sahne bir talipler sarayıdır: sahipler, küçük krallar, putlar ve güneş unvanları küçük ölçüde taşır; üç unvanı birden ve mutlak olarak taşıyan, insanların tek Rabbi, Meliki ve İlahıdır. Üç unvanın üst üste gelmesi, bu taliplerin her birinin bir yere kadar kabul edilebileceği ihtimalini kapatır. Kötülük kökü de bu sahnede yer alır: {ar:ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة, tr:elkâ aleyhi şerâşirahû izâ elkâ aleyhi nefsehû hırsan ve mahabbe, gloss:hırs ve sevgiyle kendini bütünüyle ona attı, source:"ش ر ر,B007"}. Bütün benliği tek bir nesneye atmak, tapınmanın istediği şeydir; sahte talibin istediği de budur.

Kuran sahte talipleri adlandırır. Firavun: {ar:أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim, source:79:24}; ve {ar:مَا عَلِمْتُ لَكُم مِّنْ إِلَٰهٍ غَيْرِى, tr:mâ alimtu lekum min ilâhin gayrî, gloss:sizin için benden başka bir ilah bilmiyorum, source:28:38}. Yusuf zindanda: {ar:ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ, tr:e-erbâbun muteferrikûne hayrun emi'llâhu'l-vâhidu'l-kahhâr, gloss:dağınık rabler mi daha iyi, yoksa tek ve kahhar Allah mı, source:12:39}. İnsanlar din bilginlerini rab edinir {source:9:31}; kitap ehline çağrı birbirini rab edinmemektir {source:3:64}. Hevesini ilah edinen de vardır {source:25:43}. Allah'ın mülk verdiği biri İbrahim'le Rabbi hakkında tartışır ve güneşle susturulur {source:2:258}. Fısıldayan da sahte bir krallık sunar: {ar:عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ, tr:alâ şecerati'l-huldi ve mulkin lâ yeblâ, gloss:ölümsüzlük ağacına ve eskimeyen bir mülke, source:20:120}, ve {ar:إِلَّآ أَن تَكُونَا مَلَكَيْنِ, tr:illâ en tekûnâ melekeyn, gloss:ancak iki melek olmayasınız diye, source:7:20}. Hükümdarın tebaası üzerindeki gücünün adı sultandır {source:"م ل ك,B003"}, ve fısıldayana bu güç inananlar üzerinde verilmez: {ar:إِنَّهُۥ لَيْسَ لَهُۥ سُلْطَٰنٌ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ, tr:innehû leyse lehû sultânun ale'llezîne âmenû ve alâ rabbihim yetevekkelûn, gloss:onun inananlar ve Rablerine dayananlar üzerinde gücü yoktur, source:16:99}; gücü ancak onu dost edinenler üzerindedir {source:16:100}. Allah İblis'e: {ar:إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌۭ ۚ وَكَفَىٰ بِرَبِّكَ وَكِيلًۭا, tr:inne ibâdî leyse leke aleyhim sultân, ve kefâ bi-rabbike vekîlâ, gloss:kullarım üzerinde senin gücün yoktur; vekil olarak Rabbin yeter, source:17:65}. Fısıldayan tapınma da ister ve bu yasaklanır: {ar:أَلَمْ أَعْهَدْ إِلَيْكُمْ يَٰبَنِىٓ ءَادَمَ أَن لَّا تَعْبُدُوا۟ ٱلشَّيْطَٰنَ, tr:e-lem a'hed ileykum yâ benî âdeme en lâ ta'budu'ş-şeytân, gloss:Ey Âdemoğulları, size şeytana tapmayın diye ahit vermedim mi, source:36:60}. Gerçek unvanlar ise yerinde durur: {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}, {ar:فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۖ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْكَرِيمِ, tr:fe-teâla'llâhu'l-meliku'l-hakk, lâ ilâhe illâ hû, rabbu'l-arşi'l-kerîm, gloss:gerçek hükümdar Allah yücedir; ondan başka ilah yoktur, şerefli arşın Rabbidir, source:23:116}; ve sonunda {ar:لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ, tr:li-meni'l-mulku'l-yevm, li'llâhi'l-vâhidi'l-kahhâr, gloss:bugün mülk kimin? Tek ve kahhar Allah'ın, source:40:16}.

Kaynaklar: 114:1 بِرَبِّ ر ب ب B001; 114:2 مَلِكِ م ل ك B003; 114:2 مَلِكِ م ل ك B002; 114:1 قُلْ ق و ل B004; 114:3 إِلَٰهِ ء ل ه B001; 114:3 إِلَٰهِ ء ل ه B002; 114:4 شَرِّ ش ر ر B007

## Bir arada tutmak ve parçalamak

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü sağlamlıktan başlar: sıkıca yoğrulmuş hamur, {ar:ملكت العجين إذا شددت عجنه, tr:melektu'l-acîne izâ şedettu acneh, gloss:hamuru sıkıca yoğurdum, source:"م ل ك,B001"}; bir arada duran duvar, {ar:حائط ليس له ملاك أي تماسك, tr:hâitun leyse lehû milâk, gloss:tutarlılığı olmayan duvar, source:"م ل ك,B001"}; ve krallık, elin tuttuğunda güçlü olmasından: {ar:والاسم الملك لأن يده فيه قوية صحيحة, tr:ve'l-ismu'l-mulk li-enne yedehû fîhi kaviyyetun sahîha, gloss:mülk denir, çünkü eli onun üzerinde güçlü ve sağlamdır, source:"م ل ك,B003"}. {ar:بِرَبِّ, tr:bi-rabbi, gloss:Rabbine, source:114:1} kelimesinin kökü toplar: kumar oklarını bir arada tutan kese {source:"ر ب ب,B010"}; binlerce insan ve tek olmak için toplanmış beş kabile, {ar:الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا, tr:er-ribbî vâhidu'r-ribbiyyîn, ve humu'l-ulûfu mine'n-nâs, gloss:ribbî, binlerce insan demek olan ribbiyyûn'un tekilidir; rabâb, bir araya gelmiş beş kabiledir, source:"ر ب ب,B004"}; sıkı düğüm {source:"ر ب ب,B016"}; tarafları bağlayan ahit, {ar:الربابة: العهد والميثاق, tr:er-ribâbe el-ahdu ve'l-mîsâk, gloss:ribâbe ahit ve sözleşmedir, source:"ر ب ب,B011"}; toplandığı için adını alan bol su {source:"ر ب ب,B013"}. Beş kez tekrar eden {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:1} de bir topluluktur {source:"ء ن س,B001"}. Altıncı ayetin kökü ise halkın kalabalık yığınını adlandırır, ki orada tek tek kişiler kaybolur: {ar:جنان الناس معظمهم ويسمى السواد, tr:cenânu'n-nâsi mu'zamuhum ve yusemma's-sevâd, gloss:insanların cenânı onların büyük kısmıdır, karaltı da denir, source:"ج ن ن,B013"}.

Buna karşı kötülük kökü parçalar: {ar:شرشرة الشيء تشقيقه وتقطيعه, tr:şerşeretu'ş-şey'i teşkîkuhû ve takti'uh, gloss:bir şeyin şerşeresi onu yarıp parçalamaktır, source:"ش ر ر,B004"}; ve çekişmeyi adlandırır {source:"ش ر ر,B011"}. Sure şu süreci duyurur: çok olan bir bağlayıcı tarafından tek tutulur ya da parçalanır. İnsanlar birlikte anıldıkları üç ayette tek bir Rabbe, tek bir Meliğe, tek bir İlaha bağlıdır; fısıldayan bu bağı içeriden çözer.

Kuran'da sığınmanın sözlükteki açıklaması olan tutunmak fiili topluluğa emredilir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tesımû bi-habli'llâhi cemîan ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine tutunun, dağılmayın, source:3:103}, ve aynı ayette {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ, tr:fe-ellefe beyne kulûbikum, gloss:kalplerinizi birleştirdi, source:3:103}. Şeytanın amacı tersidir: {ar:إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ, tr:innemâ yurîdu'ş-şeytânu en yûkia beynekumu'l-adâvete ve'l-bağdâe fi'l-hamri ve'l-meysir, gloss:şeytan içki ve kumarla aranıza düşmanlık ve kin sokmak ister, source:5:91}; kesenin bir arada tuttuğu kumar okları, bölen bir oyun olur. Toplanmış binler peygamberlerin yanında çarpışır: {ar:قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ فَمَا وَهَنُوا۟, tr:kâtele meahû ribbiyyûne kesîrun fe-mâ vehenû, gloss:onunla birlikte pek çok ribbî savaştı ve gevşemediler, source:3:146}. Çok ilah, dünyanın parçalanmasıdır: {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:lev kâne fîhimâ âlihetun illa'llâhu le-fesedetâ, gloss:yerde ve gökte Allah'tan başka ilahlar olsaydı ikisi de bozulurdu, source:21:22}; {ar:إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ, tr:izen le-zehebe kullu ilâhin bimâ halak, gloss:o zaman her ilah kendi yarattığını alıp giderdi, source:23:91}. Bağlayan ahit ise Rab sorusuyla kurulur: {ar:أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ, tr:e-lestu bi-rabbikum, kâlû belâ, gloss:ben sizin Rabbiniz değil miyim? Evet, dediler, source:7:172}. Şeytan buna karşı yemin eder {source:7:21}. İkiz surede düğümlere üfleyenler anılır {source:113:4}; Rab kökünün sıkı düğümü bunun karşısında durur.

Kaynaklar: 114:2 مَلِكِ م ل ك B001; 114:2 مَلِكِ م ل ك B003; 114:1 بِرَبِّ ر ب ب B010; 114:1 بِرَبِّ ر ب ب B004; 114:1 بِرَبِّ ر ب ب B016; 114:1 بِرَبِّ ر ب ب B011; 114:1 بِرَبِّ ر ب ب B013; 114:1–6 ٱلنَّاسِ ء ن س B001; 114:6 ٱلْجِنَّةِ ج ن ن B013; 114:4 شَرِّ ش ر ر B004; 114:4 شَرِّ ش ر ر B011

## Gece, saklanan yıldızlar, güneş ve karanlıkta görülen ateş

{ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü yürüyen, gündüz güneş ışığı onları örtünce gizlenen ve batan gezegenleri adlandırır: {ar:الخنس الكواكب الخمسة التي تجري وتخنس في مجراها حتى يخفى ضوء الشمس وخنوسها اختفاؤها بالنهار, tr:el-hunnesu'l-kevâkibu'l-hamsetu'lletî tecrî ve tahnisu fî mecrâhâ, gloss:hunnes, akan ve akışında gizlenen beş yıldızdır; gizlenmeleri gündüz kaybolmalarıdır, source:"خ ن س,B002"}. Altıncı ayetin kökü gecenin her şeyi örtmesini söyler: {ar:أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته, tr:ecennehu'l-leylu ve cenne aleyhi'l-leyl, gloss:gece onu örttü; karanlığıyla örtecek kadar karardı, source:"ج ن ن,B002"}. Üçüncü ayetin kökü güneşi adlandırır, çünkü ona tapılmıştır: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetu'ş-şems, summiyet bi-zâlike li-enne kavmen kânû ya'budûnehâ, gloss:ilâhe güneştir; bir topluluk ona taptığı için böyle denmiştir, source:"ء ل ه,B001"}. Kötülük kökü güneşe sermeyi {source:"ش ر ر,B002"} ve ateşten uçan kıvılcımı adlandırır: {ar:الشرر ما تطاير من النار, tr:eş-şereru mâ tetâyera mine'n-nâr, gloss:şerer ateşten uçuşandır, source:"ش ر ر,B003"}. İnsan kökü ateşi uzaktan görmeyi, {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan ateş gördü, source:"ء ن س,B002"}, ve gözbebeğinin karasında görünen küçük sureti adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'lledî yurâ fi's-sevâd, gloss:gözün insanı, gözün karasında görünen surettir, source:"ء ن س,B005"}. İnsan kökü kişiye eşlik eden her şeyi de bilir {source:"ء ن س,B003"}. Rab kökü yerinden ayrılmayanı {source:"ر ب ب,B007"}, Melik kökü de Allah'ın melekûtunu söyler {source:"م ل ك,B003"}.

Sahne şudur: gece her şeyi örter; gezegenler görünür, akar, gizlenir ve döner; bir zamanlar tapılan güneş doğar; bir ateş görülür, kıvılcımlar uçar; bir göz bakar; ve batan ışıklar arasında hangisinin Rab olduğu sorulur. Surenin üç unvanı bu soruya cevaptır: batmayan.

Kuran bu sahneyi İbrahim'in gecesinde kurar. Önce putlar ilah olarak anılır {source:6:74}, sonra {ar:وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:ve kezâlike nurî ibrâhîme melekûte's-semâvâti ve'l-ard, gloss:böylece İbrahim'e göklerin ve yerin melekûtunu gösteriyorduk, source:6:75}, ve: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:fe-lemmâ cenne aleyhi'l-leylu raâ kevkeben, kâle hâzâ rabbî, fe-lemmâ efele kâle lâ uhibbu'l-âfilîn, gloss:gece onu örtünce bir yıldız gördü, "bu benim Rabbim" dedi; batınca "batanları sevmem" dedi, source:6:76}. Güneşte aynı tekrarlanır: {ar:فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ, tr:fe-lemmâ raa'ş-şemse bâzigaten kâle hâzâ rabbî hâzâ ekber, gloss:güneşi doğarken görünce "bu benim Rabbim, bu daha büyük" dedi, source:6:78}; o da batar, ve İbrahim yüzünü gökleri ve yeri yaratana çevirir {source:6:79}. Örten gece (cenne), bir yıldız, batmak ve Rab sorusu tek pasajdadır. Kuran güneşe secdeyi yasaklar {source:41:37}, ve Sebe halkının güneşe tapmasını şeytanın süslemesine bağlar: {ar:يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ, tr:yescudûne li'ş-şemsi min dûni'llâhi ve zeyyene lehumu'ş-şeytânu a'mâlehum, gloss:Allah'ı bırakıp güneşe secde ediyorlar; şeytan onlara işlerini süslemiş, source:27:24}. Yıldızlar şeytanlara karşı bekçidir: {ar:وَحِفْظًۭا مِّن كُلِّ شَيْطَٰنٍۢ مَّارِدٍۢ, tr:ve hifzan min kulli şeytânin mârid, gloss:ve her inatçı şeytana karşı koruma, source:37:7}; kulak hırsızını {ar:شِهَابٌۭ ثَاقِبٌۭ, tr:şihâbun sâkıb, gloss:delip geçen bir alev, source:37:10} izler. Cinler de bunu anlatır {source:72:9}. Karanlıkta görülen ateş Musa'nındır: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran lealli âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Kıvılcım ise cehennemin ateşinde büyür {source:77:32}. Sure-kardeşindeki oluk da gecedir: yemin {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararmaya başlayan geceye, source:81:17} ile sürer.

Kaynaklar: 114:4 ٱلْخَنَّاسِ خ ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B002; 114:3 إِلَٰهِ ء ل ه B001; 114:4 شَرِّ ش ر ر B002; 114:4 شَرِّ ش ر ر B003; 114:1–6 ٱلنَّاسِ ء ن س B002; 114:1–6 ٱلنَّاسِ ء ن س B005; 114:1–6 ٱلنَّاسِ ء ن س B003; 114:1 بِرَبِّ ر ب ب B007; 114:2 مَلِكِ م ل ك B003

## Av: mırıltı, sığınak, tetikteki hayvan, korunan bitki

{ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} avcının ve köpeklerinin hafif sesidir: {ar:همس الصائد والكلاب وأصوات الحلى وسواس, tr:hemsu's-sâidi ve'l-kilâbi ve asvâtu'l-hulî vesvâs, gloss:avcının ve köpeklerin fısıltısı, takıların sesleri vesvastır, source:"و س و س,B002"}; ve avın yattığı sazlıktaki hışırtıdır {source:"و س و س,B002"}. {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü ceylanların sığınağını ve ceylanların kendisini adlandırır: {ar:الخنس مأوى الظباء؛ الخنس الظباء أنفسها, tr:el-hunnes me'vâ'z-zıbâ; el-hunnesu'z-zıbâu enfusuhâ, gloss:hunnes ceylanların sığınağıdır; hunnes ceylanların kendisidir, source:"خ ن س,B004"}; bütün sığırlar da basık burunludur {source:"خ ن س,B003"}. Rab kökü yaban sığırı sürüsünü {source:"ر ب ب,B014"}, sığınma kökü yeni doğurmuş ceylanları {source:"ع و ذ,B003"} ve dikenlerin dibinde otlayanların erişemediği bitkiyi bilir {source:"ع و ذ,B004"}. İnsan kökü korkutan bir şeyi sezip etrafına bakan hayvanı adlandırır: {ar:والاستئناس النظر وأحس بما رابه, tr:ve'l-isti'nâsu'n-nazar ve ehasse bimâ râbeh, gloss:isti'nâs bakmak ve kuşkulandıran şeyi sezmektir, source:"ء ن س,B002"}; ve evcili yabaninin karşısına koyar, ısırmayan köpeği ısıranın karşısına {source:"ء ن س,B003"}. Altıncı ayetin kökü saklanma yeridir {source:"ج ن ن,B017"}.

Sahne şudur: bir avcı alçak bir mırıltıyla sokulur; av sığınağında durur; tetikteki hayvan sezer ve etrafına bakar; bir bitki dikenler arasında erişilmez büyür. Fısıldayan mırıldanan avcıdır, ama adıyla sığınağında duran av gibi de saklanır. İnsanlar sezmesi gerekenlerdir. Sığınma, erişilemeyen yerdir.

Kuran avcıyı İblis'in ağzından verir: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ak'udenne lehum sırâtake'l-mustakîm, gloss:senin dosdoğru yolunun üstünde onları bekleyeceğim, source:7:16}, sonra {ar:ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:summe le-âtiyennehum min beyni eydîhim ve min halfihim ve an eymânihim ve an şemâilihim, gloss:sonra onlara önlerinden, arkalarından, sağlarından ve sollarından geleceğim, source:7:17}. Pusuya yatmak, sonra her yandan kuşatmak. Allah İblis'e seslenir: {ar:وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:vestefziz meni'stata'te minhum bi-savtike ve eclib aleyhim bi-hayli-ke ve racilik, gloss:onlardan gücünün yettiğini sesinle ürküt, atlıların ve yayalarınla üstlerine sür, source:17:64}. Ses ile ürkütmek ve sürmek, avcının işidir. Kaçan av da Kuran'da görülür: {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:keennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri, source:74:50}, {ar:فَرَّتْ مِن قَسْوَرَةٍۭ, tr:ferrat min kasvera, gloss:arslandan kaçan, source:74:51}.

Kaynaklar: 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B004; 114:4 ٱلْخَنَّاسِ خ ن س B003; 114:1 بِرَبِّ ر ب ب B014; 114:1 أَعُوذُ ع و ذ B003; 114:1 أَعُوذُ ع و ذ B004; 114:5 ٱلنَّاسِ ء ن س B002; 114:5 ٱلنَّاسِ ء ن س B003; 114:6 ٱلْجِنَّةِ ج ن ن B017

## At ve binici

Surenin beş kelimesi atın bir parçasını ya da koşusunu adlandırır. Binici hayvana insî yandan biner ve sağar: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbe li'l-cânibi'llezî yeli'r-râkib, gloss:hayvanın insîsi biniciye bakan yanıdır, source:"ء ن س,B004"}. Atın bacakları ve boynu onu yönetendir, onun "milk"idir: {ar:ملك الدابة قوائمها وهاديها, tr:milku'd-dâbbe kavâimuhâ ve hâdîhâ, gloss:hayvanın milki ayakları ve boynudur, source:"م ل ك,B008"}. Boynunda gerdanlığın asıldığı girdap sığınma kökündendir: {ar:معوذ الفرس موضع القلادة ودائرة المعوذ تستحب, tr:muavvizu'l-feresi mevdiu'l-kılâde, gloss:atın muavvizi gerdanlığın yeridir; o yerdeki girdap beğenilir, source:"ع و ذ,B005"}. Yeni doğurmuş kısraklar da ûz arasındadır {source:"ع و ذ,B003"}. Hannâs kökünden bir at da vardır: {ar:فرس خنوس وهو الذي يعدل وهو مستقيم في حضره ذات اليمين وذات الشمال, tr:ferasun hanûs, ve huvellezî ya'dilu ve huve mustakîmun fî hudrihî zâte'l-yemîni ve zâte'ş-şimâl, gloss:hanûs at, dörtnala düz koşarken sağa sola sapandır, source:"خ ن س,B005"}. Ve at yarışı göğüsle kazanır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-feresu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle önde gelince "sadera" denir, source:"ص د ر,B002"}.

Fısıldayan, düz bir koşunun içindeki sapmadır: at yolundan çıkmaz ama sağa sola kayar. Sığınma, gerdanlığın asıldığı yerde takılır. Göğüs, yarışı kazanan uçtur; fısıltı tam oraya yerleşir.

Kuran'da İblis'in yaklaşımı aynı iki yönü adlandırır: {ar:وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:ve an eymânihim ve an şemâilihim, gloss:sağlarından ve sollarından, source:7:17}. Şeytana atlılar verilir {source:17:64}. Allah koşan atlara yemin eder: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًۭا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara, source:100:1}, {ar:فَٱلْمُورِيَٰتِ قَدْحًۭا, tr:fe'l-mûriyâti kadhâ, gloss:nallarıyla kıvılcım çıkaranlara, source:100:2}; ve aynı sure göğüslerdekinin ortaya dökülmesiyle biter {source:100:10}.

Kaynaklar: 114:1–6 ٱلنَّاسِ ء ن س B004; 114:2 مَلِكِ م ل ك B008; 114:1 أَعُوذُ ع و ذ B005; 114:4 ٱلْخَنَّاسِ خ ن س B005; 114:5 صُدُورِ ص د ر B002; 114:1 أَعُوذُ ع و ذ B003

## Suya giden yol ve dönüş

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kökü yolun ortasını, {ar:الزم ملك الطريق أي وسطه, tr:ilzem milke't-tarîk ey vesatah, gloss:yolun milkine, yani ortasına sarıl, source:"م ل ك,B006"}; sürünün takip ettiği öndeki hayvanı {source:"م ل ك,B008"}; ve yolcunun yanında taşıdığı, onu ayakta tutan suyu adlandırır: {ar:والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره, tr:ve'l-melku'l-mâu yekûnu mea'l-musâfir, gloss:melk yolcunun yanındaki sudur, çünkü yanında olunca işini elinde tutar, source:"م ل ك,B007"}. {ar:صُدُورِ, tr:sudûr, gloss:göğüsler, source:114:5} kökü sudan dönmeyi, {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadaru'l-insirâfu ani'l-virdi ve an kulli emr, gloss:sader sudan ve her işten geri dönmektir, source:"ص د ر,B003"}; halkını sudan geri getiren yolu, {ar:طريق صادر يصدر بأهله عن الماء, tr:tarîkun sâdirun yasduru bi-ehlihî ani'l-mâ, gloss:halkını sudan geri getiren dönüş yolu, source:"ص د ر,B003"}; ve dönüşün yerini ve zamanını adlandırır {source:"ص د ر,B004"}. Rab kökü develerin durduğu yeri bilir {source:"ر ب ب,B007"}. Hannâs kökü topluluktan gizlice sıyrılanı bilir {source:"خ ن س,B001"}.

Sahne şudur: bir sürü önderinin ardından yolun ortasından suya gider, içer ve dönüş yolundan geri gelir; biri topluluktan gizlice ayrılır. Beşinci ayetteki çoğul aynı zamanda "dönüşler" diye de duyulur: göğüsler, insanın her işten döndüğü yerdir. Fısıldayan yolun ortasından ayırmaya çalışır.

Kuran bu sahneyi Musa'nın Medyen yolunda kurar: {ar:عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ, tr:asâ rabbî en yehdiyenî sevâe's-sebîl, gloss:umarım Rabbim bana yolun ortasını gösterir, source:28:22}; suya varınca {ar:وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ, tr:vecede aleyhi ummeten mine'n-nâsi yeskûn, gloss:başında su içiren bir insan topluluğu buldu, source:28:23}, ve kadınlar {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ, tr:lâneskî hattâ yusdira'r-riâ, gloss:çobanlar sürülerini sudan geri çevirmedikçe biz su veremeyiz, source:28:23} der. Sonunda: {ar:رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ, tr:rabbi innî limâ enzelte ileyye min hayrin fakîr, gloss:Rabbim, bana indireceğin her hayra muhtacım, source:28:24}. Yol, su, insanlar, sudan dönüş ve Rab bir pasajdadır. Surenin iki kelimesi tek cümlede de durur: {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amelleri kendilerine gösterilmek üzere dağınık halde dönerler, source:99:6}. Yolun ortasında pusuya yatan İblis'tir {source:7:16}; yoldaş şeytanlar yoldan alıkoyar: {ar:وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ, tr:ve innehum le-yesuddûnehum ani's-sebîli ve yahsebûne ennehum muhtedûn, gloss:onları yoldan alıkoyarlar, onlar da doğru yolda olduklarını sanırlar, source:43:37}. Topluluğundan koparılan da anlatılır: {ar:كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا, tr:kellezi'steh'vethu'ş-şeyâtînu fi'l-ardı hayrâne lehû ashâbun yed'ûnehû ile'l-hude'tinâ, gloss:şeytanların yerde ayartıp şaşkın bıraktığı, arkadaşlarının "bize gel" diye doğru yola çağırdığı kişi gibi, source:6:71}. Yolun kendisi adlandırılır: {ar:هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:hâzâ sırâtun mustakîm, gloss:bu dosdoğru bir yoldur, source:36:61}.

Kaynaklar: 114:2 مَلِكِ م ل ك B006; 114:2 مَلِكِ م ل ك B008; 114:2 مَلِكِ م ل ك B007; 114:5 صُدُورِ ص د ر B003; 114:5 صُدُورِ ص د ر B004; 114:1 بِرَبِّ ر ب ب B007; 114:4 ٱلْخَنَّاسِ خ ن س B001

## Yüzün çevresindeki sürü ve kıvılcım

{ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} kökü sivrisineğe benzeyen, insanın yüzünü kaplayan ama ısırmayan bir böceği adlandırır: {ar:الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى, tr:eş-şirrân şebîhun bi'l-baûd yağşâ vechu'l-insâni ve lâ yeuddu ve rubbemâ semmevhu'l-ezâ, gloss:şirrân sivrisineğe benzer, insanın yüzünü kaplar, ısırmaz; ona bazen "eza" derler, source:"ش ر ر,B009"}. Kök ateşten uçuşan kıvılcımı da bilir {source:"ش ر ر,B003"}. Altıncı ayetin kökü uçarken vızıltısı artan sinekleri adlandırır: {ar:جن الذباب أي كثر صوته, tr:cenne'z-zubâb ey kesura savtuh, gloss:sinek "cenne" etti, yani sesi çoğaldı, source:"ج ن ن,B015"}. Fısıltı da hafif bir hışırtıdır {source:"و س و س,B002"}. Melik kökü arıların beyini bilir: {ar:مليك النحل يعسوبها, tr:melîku'n-nahli ya'sûbuhâ, gloss:arıların meliki onların beyidir, source:"م ل ك,B008"}.

Sahne şudur: küçük şeyler yüzün çevresinde dolaşır; onu kaplar, vızıldar, parlar, hışırdar ve ısırmaz. Fısıltı bu boyda bir zarardır: yer kaplar, örter, ama yaralamaz. Kişiyi meşgul eden ama kendiliğinden yaralayamayan bir şey olduğu için ona karşı sığınmak yeterlidir.

Kuran bu ölçüyü açıkça verir: {ar:إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ لِيَحْزُنَ ٱلَّذِينَ ءَامَنُوا۟ وَلَيْسَ بِضَآرِّهِمْ شَيْـًٔا إِلَّا بِإِذْنِ ٱللَّهِ, tr:innema'n-necvâ mine'ş-şeytâni li-yahzune'llezîne âmenû ve leyse bi-dârrihim şey'en illâ bi-izni'llâh, gloss:gizli konuşma, inananları üzmek için şeytandandır; ama Allah'ın izni olmadan onlara hiçbir zarar veremez, source:58:10}. Ezanın zarar sayılmayan ölçüsü de geçer: {ar:لَن يَضُرُّوكُمْ إِلَّآ أَذًۭى, tr:len yedurrûkum illâ ezâ, gloss:size eziyetten başka zarar veremezler, source:3:111}. Sözlükteki böceğin adı "eza", Kuran'daki ifadede de zararın altındaki rahatsızlıktır.

Kaynaklar: 114:4 شَرِّ ش ر ر B009; 114:4 شَرِّ ش ر ر B003; 114:6 ٱلْجِنَّةِ ج ن ن B015; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:2 مَلِكِ م ل ك B008

## Örtülen akıl

Altıncı ayette duran biçim, {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6}, aynı zamanda deliliğin adıdır: {ar:الجنة الجنون وذلك أنه يغطي العقل, tr:el-cinnetu'l-cunûn, ve zâlike ennehû yuğattı'l-akl, gloss:cinne deliliktir, çünkü aklı örter, source:"ج ن ن,B006"}; {ar:الجنون حائل بين النفس والعقل, tr:el-cunûnu hâilun beyne'n-nefsi ve'l-akl, gloss:delilik nefisle akıl arasına giren bir perdedir, source:"ج ن ن,B006"}. Sığınma kökünün muskası da "korkuya ya da deliliğe karşı" takılır {source:"ع و ذ,B002"}. Fısıltı kötü bir geçici düşüncedir: {ar:الوسوسة الخطرة الرديئة, tr:el-vesvesetu'l-hatratu'r-radîe, gloss:vesvese kötü bir düşüncedir, source:"و س و س,B001"}. Söz kökü birine yalan söz yüklemeyi adlandırır {source:"ق و ل,B005"}.

Sahne şudur: bir akıl örtülür ya da bir perde ile nefsinden ayrılır; ona karşı bir sığınma söylenir. Ayetin anlamı "cinler"dir; ama aynı biçimde aklı örten şey de duyulur, ve fısıltının en uç sonucu bu olur: kişiyle aklı arasına giren bir perde.

Kuran bu biçimi elçinin savunmasında kullanır: {ar:مَا بِصَاحِبِهِم مِّن جِنَّةٍ ۚ إِنْ هُوَ إِلَّا نَذِيرٌۭ مُّبِينٌ, tr:mâ bi-sâhibihim min cinne, in huve illâ nezîrun mubîn, gloss:arkadaşlarında hiçbir delilik yoktur; o yalnızca apaçık bir uyarıcıdır, source:7:184}; {ar:أَمْ يَقُولُونَ بِهِۦ جِنَّةٌۢ, tr:em yekûlûne bihî cinne, gloss:yoksa "onda delilik var" mı diyorlar, source:23:70}. Delilik ve yalan isnadı yan yana sorulur: {ar:أَفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَم بِهِۦ جِنَّةٌۢ, tr:efterâ ala'llâhi keziben em bihî cinne, gloss:Allah'a karşı yalan mı uydurdu, yoksa onda delilik mi var, source:34:8}. Aynı ret tek bir pasajda hannâs yıldızlarının yeminiyle başlar {source:81:15}, {ar:وَمَا صَاحِبُكُم بِمَجْنُونٍۢ, tr:ve mâ sâhibukum bi-mecnûn, gloss:arkadaşınız deli değildir, source:81:22} der, ve {source:81:25} ile şeytanın sözünü reddeder. Bir başka yerde: {ar:فَمَآ أَنتَ بِنِعْمَتِ رَبِّكَ بِكَاهِنٍۢ وَلَا مَجْنُونٍ, tr:fe-mâ ente bi-ni'meti rabbike bi-kâhinin ve lâ mecnûn, gloss:sen Rabbinin nimeti sayesinde ne kâhinsin ne deli, source:52:29}. Şeytanların ayarttığı kişi de şaşkındır {source:6:71}.

Kaynaklar: 114:6 ٱلْجِنَّةِ ج ن ن B006; 114:1 أَعُوذُ ع و ذ B002; 114:4 ٱلْوَسْوَاسِ و س و س B001; 114:1 قُلْ ق و ل B005

## Buluşmalar

İlk buluşma göğüstedir. Örten kök göğsün içinde çalışır: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Görünen ve örtülü imgesi ile göğüs imgesi burada tek sahne olur: görünen insanların içinde, kemik kafesin altında, gizli kalp vardır; örtülü olan, örtülü odaya girer. Kuran'ın göğüslerini bükerek saklananları {source:11:5} da bu sahneye aittir: ne kadar örtünseler de göğüslerin özü bilinir. Sığınma imgesindeki bütün dış örtüler (göğüs giysisi, zırh, kalkan) bu odanın dışında kalır; içerdeki fısıltıya karşı yalnız söylenen söz işler.

İkinci buluşma sözdedir. Sözlük, söylenen sözü "telaffuzla dışarı çıkarılan" diye tanımlarken kullandığı fiili {source:"ق و ل,B001"} kötülük kökünün "ortaya çıkarmak" anlamında da kullanır {source:"ش ر ر,B008"}. Sure böylece iki çıkarma arasında kurulur: sığınma sözü içten dışa çıkar, fısıltının amacı ise örtülüyü açığa çıkarmaktır {source:7:20}. Söz ile çekilme de buluşur: {ar:الشيطان يوسوس فإذا ذكر الله خنس, tr:eş-şeytânu yuvesvisu fe-izâ zukira'llâhu hanes, gloss:şeytan fısıldar, Allah anılınca çekilir, source:"خ ن س,B001"}. "De" emri bu anmayı dile getirir; "sinip çekilen" sıfatı onun sonucunu adlandırır. Söz ile sığınma okunan muskada birleşir {source:"ع و ذ,B002"}: emredilen cümle, dilde taşınan korunaktır.

Üçüncü buluşma gece ile çekilmededir. Hannâs kökü hem geri çekilmeyi hem gündüz gizlenip yörüngesinde dönen yıldızları adlandırır; Kuran onlara yemin eden pasajda deliliği ve şeytan sözünü reddeder {source:81:15}. İbrahim'in gecesinde batanlara karşı {source:6:76} Rab kökünün "yerinden ayrılmayan" anlamı {source:"ر ب ب,B007"} durur. Fısıldayan gidip gelir; Rab batmaz.

Dördüncü buluşma unvanlar ile sığınmadadır: {ar:عاذ فلان بربه, tr:âze fulânun bi-rabbih, gloss:Rabbine sığındı, source:"ع و ذ,B001"}. Fiil ile unvan tek ifadede durur. Ana ve yavru imgesi bu bağa sıcaklık verir: aynı iki kök yeni doğurmuş anneyi adlandırır, ve Kuran'da bir anne yeni doğan kızını Rabbine sığındırır, Rab da onu bir bitki gibi büyütür {source:3:37}. Bağlama imgesi aynı sığınmayı topluluğa genişletir: sığınmanın açıklaması olan tutunmak {source:3:103} bütün insanları tek ipte toplar; kötülük kökü ise parçalar.

Surenin hareketi bu buluşmalarla taşınır. İlk üç ayet aynı insanları üç unvan altında, bir arada ve görünür olarak toplar; dördüncü ayet görünmeyen ve gidip gelen bir fısıltıyı adlandırır; beşinci ayet onu en içteki odaya, göğse yerleştirir; altıncı ayet kaynağını hem örtülülere hem görünenlere açar. Sığınma sözü bu yolun tersinden ilerler: içten dışa, dilde söylenir, ve yerinden ayrılmayan bir Rabbe tutunur.

