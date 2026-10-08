Focus: 113:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/113_3/D.r13/context.md =====
# 113:3 — focus

وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ

Anchor translation (canonical reading, reference only):

ve karanlık bastırdığında onun kötülüğünden;

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمِن | مِن |  | CONJ;P |
| 2 | شَرِّ | شَرّ | ش ر ر | N |
| 3 | غَاسِقٍ | غَاسِق | غ س ق | N |
| 4 | إِذَا | إِذَا |  | T |
| 5 | وَقَبَ | وَقَبَ | و ق ب | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 113 — full text (context; no pericope)

- 113:1 قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ
- 113:2 مِن شَرِّ مَا خَلَقَ
- 113:3 ◀ focus وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ
- 113:4 وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ
- 113:5 وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ


===== _commentary/v16/work/113_3/D.r13/01_dictionary.md =====
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

## غ س ق (root_001086) — identity root of غَاسِقٍ (w3)

- **B001** gecenin kararması ve karanlığın bastırması — gece karanlığı; karanlığın ilk girişi ve koyulaşması · gece karardı, karanlığı başladı ya da koyulaştı · gün batımı aydınlığı kaybolunca kararan gece · ezan görevlisi akşam namazını gece karanlığına kadar geciktirdi
  الغسق الظلمة والغاسق الليل (maqayis)؛ الغاسق الليل إذا غاب الشفق (ayn;sihah;tahdhib)؛ الغسق أول ظلمة الليل (sihah;tahdhib)؛ غسق الليل شدة ظلمته (mufradat)؛ أغسق المؤذن إذا أخر صلاة المغرب إلى غسق الليل (maqayis;sihah;tahdhib)
- **B002** dondurucu, pis kokulu cehennem akıntısı — cehennem halkının derilerinden ve irinlerinden akan dondurucu, pis kokulu sıvı · soğuk; dondurucu derecede soğuk olan
  الغساق ما تقطر من جلود أهل النار (maqayis;mufradat)؛ غساقا أي منتنا (ayn;tahdhib)؛ الغساق البارد المنتن (sihah)؛ الغساق بارد يحرق كإحراق الحميم (tahdhib)؛ ما يغسق ويسيل من صديدهم وجلودهم (tahdhib)؛ الغاسق البارد (tahdhib)
- **B003** gözün kararması [kalıp] — gözü karardı; görme alanı karanlıklaştı
  غسقت عينه أظلمت (maqayis;sihah)
- **B004** akma, sızma ve üzerine dökülme — gözden su, yaş veya çapak aktı · yaradan sarı bir sıvı aktı · akan · gökyüzü çiseledi, hafif yağmur yağdırdı · gece tepelerin üzerine döküldü · akma ve dökülme
  تغسق ما في دموعها (ayn)؛ غسق الجرح غسقانا إذا سال منه ماء أصفر (sihah)؛ الغاسق بمعنى السائل (tahdhib)؛ غسقت العين وهو هملان العين بالغمص والماء (tahdhib)؛ غسقت السماء أرشت (tahdhib)؛ غسق الليل على الظراب أي انصب الليل على الجبال (tahdhib)
- **B005** yiyecekteki yabancı maddeler ve kalıntılar [kalıp] — yiyeceğin içindeki yabancı maddeler ve istenmeyen kalıntılar
  الغسق من قماش الطعام؛ في الطعام زوان وفيه غسق (tahdhib)

## و ق ب (root_001670) — identity root of وَقَبَ (w5)

- **B001** içine bir şeyin girebildiği oyuk veya çukur — içine bir şeyin girebildiği veya suyun toplanabildiği oyuk ya da çukur · bir şeydeki oyuk veya çukur · göz çukuru veya gözün çökük yuvası · ıslatılmış ekmek yemeğinde suyun toplandığı orta çöküntü · duvar açıklıkları veya pencereler
  الوقب كالنقرة في الشيء (maqayis;mufradat)؛ كل قلت أو حفرة (ayn;tahdhib)؛ الوقب في الجبل نقرة يجتمع فيها الماء ووقب العين نقرتها (sihah)؛ وقبة الثريد أنقوعته (ayn;sihah;tahdhib)؛ الأوقاب الكوى (tahdhib)
- **B002** bir oyuğa girme, inme, düşme veya bağlama göre gözden kaybolma — gözleri çöküp yuvalarına girdi · bir oyuğa girdi, indi veya gözden kayboldu · güneş battı ve gözden kayboldu · karanlık veya gece çöktü · bir şeyi oyuğa sokma veya gizleme · bir şeyi oyuğa soktu
  وقب الشيء دخل في وقبة (maqayis;mufradat)؛ وقب الشيء نزل ووقع والليل إذا نزل (maqayis)؛ وقب الظلام أي دخل (ayn)؛ وقبت الشمس إذا غابت ودخلت موضعها ووقب الظلام دخل على الناس (sihah)؛ إذا وقب إذا دخل في كل شيء أو ظلم (tahdhib)؛ الإيقاب إدخال الشيء في الوقبة أو تغييبه (ayn;sihah;tahdhib;mufradat)
- **B003** binek hayvanının üreme organından çıkan ses — atın veya binek hayvanının üreme organından çıkan ses · binek hayvanı üreme organından ses çıkardı
  الوقيب صوت قنب الدابة يقال وقبت الدابة تقب وقيبا (ayn)؛ الوقيب صوت قنب الفرس (sihah)؛ صوت يخرج من قنب الفرس وقد وقب يقب (tahdhib)؛ الوقيب صوت قنب الدابة (mufradat)
- **B004** bir topluluğun acıkması [kalıp] — topluluk acıktı
  أوقب القوم أي جاعوا (sihah)
- **B005** ev eşyası ve döşemelikler — evin kumaş, döşemelik ve taşınabilir eşyaları
  الأوقاب قماش البيت (tahdhib)
- **B006** gündüzden geceye ara vermeden yol almak [kalıp] — gündüzden geceye ara vermeden sürdürülen yolculuk
  يسيرون سير الميقاب وهو أن يواصلوا بين يوم وليلة (tahdhib)
- **B007** süslemede kullanılan küçük deniz kabuğu — süslemede kullanılan küçük deniz kabuğu
  الميقب الودعة (tahdhib)

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

===== _commentary/v16/out/s113/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 113:3, and ## Buluşmalar) =====
## Gecenin içeri girişi, tanın yarılıp ayrılışı

Surenin ilk ayeti, sığınılan Rabbi tek bir sıfatla anar: {ar:قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ, tr:kul eûzü bi-rabbi'l-felak, gloss:de ki: felakın Rabbine sığınırım, source:113:1}. Felak ayette tan vaktinin, sabahın adıdır. Kelimenin kökü ise bir işlemi adlandırır: {ar:الفلق شق الشيء وإبانة بعضه عن بعض, tr:el-falk şakku'ş-şey' ve ibânetu ba'dihî an ba'd, gloss:bir şeyi yarmak ve bir parçasını öbüründen ayırmak, source:"ف ل ق,B001"}. Sabah, bu işlemin göğe uygulanmış hâlidir: {ar:الفلق الصبح لأن الظلام ينفلق عنه, tr:el-felaku's-subh li-enne'z-zalâme yenfeliku anh, gloss:felak sabahtır, çünkü karanlık ondan yarılıp ayrılır, source:"ف ل ق,B002"}. Karanlık bir örtü gibi ışığın üstündedir; tan, örtünün ışıktan yarılıp sökülmesidir. Bu yarmanın bir faili de vardır: {ar:الصبح والله فلقه أي أوضحه وأبداه فانفلق, tr:es-subhu vallâhu felakahû ey evdahahû ve ebdâhu fenfelak, gloss:sabahı Allah yardı, yani onu açık kıldı, ortaya koydu; o da yarıldı, source:"ف ل ق,B002"}. Böylece "felakın Rabbi" bir saatin sahibi olarak değil, her sabah karanlığı ışıktan ayıran el olarak duyulur. Aynı işlem bilgiye de taşınır: {ar:الفلق بيان الحق بعد إشكال, tr:el-felak beyânu'l-hakkı ba'de işkâl, gloss:felak, karışıklıktan sonra gerçeğin açığa çıkmasıdır, source:"ف ل ق,B002"}. Bu yorumda bir kelimenin kök ailesinden gelen imgeler, kelimenin ayetteki anlamının yanında duyulur; o anlamın yerine geçmez. Felak burada sabahtır; yarma, ayrılma ve açığa çıkma o sabahın içinde işleyen harekettir.

Üçüncü ayet, ilk ayetin yardığı karanlığı bu kez içeri girerken gösterir: {ar:وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ, tr:ve min şerri ğāsikın izâ vekab, gloss:ve çöküp içeri girdiğinde karanlığın şerrinden, source:113:3}. Gāsık geceyi bir an olarak değil, bir süreç olarak adlandırır. Başlangıcı ufuktaki kızıllığın kaybolduğu andır: {ar:الغاسق الليل إذا غاب الشفق, tr:el-ğāsiku'l-leylu izâ ğābe'ş-şafak, gloss:gāsık, şafak kızıllığı kaybolduğundaki gecedir, source:"غ س ق,B001"}. Sonra ilk karanlık gelir, {ar:الغسق أول ظلمة الليل, tr:el-ğasaku evvelu zulmeti'l-leyl, gloss:gasak gecenin ilk karanlığıdır, source:"غ س ق,B001"}, ve karanlık en koyu hâline ulaşır: {ar:غسق الليل شدة ظلمته, tr:ğasaku'l-leyl şiddetu zulmetih, gloss:gecenin gasakı karanlığının en koyu hâlidir, source:"غ س ق,B001"}. Bu karanlık bir sıvı gibi davranır: {ar:غسق الليل على الظراب أي انصب الليل على الجبال, tr:ğasaka'l-leylu ale'z-zırâb ey insabbe'l-leylu ale'l-cibâl, gloss:gece tepelerin üstüne döküldü, yani dağların üstüne boşandı, source:"غ س ق,B004"}. Fiil de aynı hareketi tamamlar: {ar:وقبت الشمس إذا غابت ودخلت موضعها ووقب الظلام دخل على الناس, tr:vekabeti'ş-şemsu izâ ğābet ve dehalet mevdiahâ ve vekabe'z-zalâmu dehale ale'n-nâs, gloss:güneş batıp yerine girdiğinde "vekabet" denir; karanlık insanların üstüne girdiğinde de "vekabe", source:"و ق ب,B002"}. Giriş her yere ulaşır: {ar:إذا وقب إذا دخل في كل شيء أو ظلم, tr:izâ vekab izâ dehale fî kulli şey' ev zalem, gloss:"izâ vekab", her şeyin içine girdiğinde ya da karardığında demektir, source:"و ق ب,B002"}. Önce güneş kendi yerine girer, sonra karanlık insanların yanına girer, döküldüğü tepelerden aşağı her şeyin içine sızar.

Sade bir anlam "gecenin şerrinden" der ve geceyi kötülüğün kendisi gibi bırakır. Ayetin sözü ise sığınmayı bir ana bağlar: {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}. Korunma istenen şey gecenin varlığı değil, karanlığın eşikten içeri girdiği andır. Kur'an geceyi başka bir yerde açıkça bir dinlenme olarak koyar. Allah tohumu yaran olarak kendini anlattığı ayetin hemen ardından şöyle der: {ar:فَالِقُ ٱلْإِصْبَاحِ وَجَعَلَ ٱلَّيْلَ سَكَنًۭا, tr:fâliku'l-isbâhi ve ceale'l-leyle sekenâ, gloss:sabahı yarandır, geceyi dinlenme kılmıştır, source:6:96}. Sabahı yaran aynı kökle anılır ve gece O'nun kurduğu bir dinginliktir. Bu yüzden sureyi okuyan, geceden değil, gecenin içeri girdiği anda onunla birlikte girenden sığınır; sığındığı da o geceyi her sabah yarıp ışıktan ayıran Rabdir. Ayetin ikinci kelimesiyle birinciye dönen bu düzen sade bir anlatımın veremeyeceği bir şeyi duyurur: üçüncü ayetin gecesi, ilk ayetin Rabbinin açtığı bir günün içinde dinlenir.

Kur'an gecenin girişini ve tanın açılışını birçok yerde birlikte sahneler. Allah Peygambere namazı emrederken vakti tam bu hareketle çizer: {ar:أَقِمِ ٱلصَّلَوٰةَ لِدُلُوكِ ٱلشَّمْسِ إِلَىٰ غَسَقِ ٱلَّيْلِ وَقُرْءَانَ ٱلْفَجْرِ, tr:ekımi's-salâte li-dulûki'ş-şemsi ilâ ğasaki'l-leyli ve kur'âne'l-fecr, gloss:güneşin kaymasından gecenin koyulaşmasına kadar namazı kıl, sabahın okunuşunu da, source:17:78}. Üçüncü ayetin kökü burada gecenin koyulaşmasıdır; emir güneşin inişinden gecenin koyuluğuna, oradan sabahın okunuşuna uzanır. Gece de tan da aynı emrin içindedir ve tanı karşılayan şey bir okumadır. Allah oruç gecelerinin hükmünü bildirirken tanı iki ipliğin birbirinden ayrılması olarak tarif eder: {ar:حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ, tr:hattâ yetebeyyene lekumu'l-haytu'l-ebyadu mine'l-hayti'l-esvedi mine'l-fecr, gloss:tan vaktinden beyaz iplik siyah iplikten size ayırt edilinceye kadar, source:2:187}. Felak işleminin kendisi, burada iki ipliğin birbirinden ayrılışı olarak görünür. Yeminlerde de gecenin gidişi sabahın soluğuyla eşlenir: {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararıp çekildiğinde geceye andolsun, source:81:17} ve {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhı izâ teneffes, gloss:soluk aldığında sabaha andolsun, source:81:18}. Sabah, tutulmuş bir nefesin bırakılması gibi gelir. Başka yeminlerde gece arkasını döner ve sabah ağarır {source:74:33} {source:74:34}; gece örter, gündüz kendini açar: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye andolsun, source:92:1} ve {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp göründüğünde gündüze andolsun, source:92:2}. Gāsık tanımının başladığı ufuk kızıllığına da Allah yemin eder ve ardından gecenin topladıklarını anar: {ar:فَلَآ أُقْسِمُ بِٱلشَّفَقِ, tr:fe-lâ uksimu bi'ş-şafak, gloss:şafağın kızıllığına yemin ederim, source:84:16}, {ar:وَٱلَّيْلِ وَمَا وَسَقَ, tr:ve'l-leyli ve mâ vesak, gloss:geceye ve onun topladıklarına, source:84:17}.

Kur'an içeri girişin tersini de, yani gündüzün geceden sıyrılıp çekilmesini gösterir. Allah bunu insanlara bir işaret olarak anar: {ar:وَءَايَةٌۭ لَّهُمُ ٱلَّيْلُ نَسْلَخُ مِنْهُ ٱلنَّهَارَ فَإِذَا هُم مُّظْلِمُونَ, tr:ve âyetun lehumu'l-leylu nesleḣu minhu'n-nehâra fe-izâ hum muzlimûn, gloss:gece de onlar için bir işarettir: gündüzü ondan sıyırırız, bir de bakarlar ki karanlığa girmişler, source:36:37}. Gündüz derisi soyulur gibi geceden çekilir ve insanlar kendilerini karanlığın içinde bulur; bu, karanlığın "insanların üstüne girmesi"nin Kur'an'daki karşılığıdır. Göğün kuruluşunu anlatan ayetlerde iki hareket tek cümlede durur: {ar:وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا, tr:ve ağtaşe leylehâ ve ahrace duhâhâ, gloss:gecesini karartmış, kuşluğunu çıkarmıştır, source:79:29}. Gündüz dışarı çıkarılır; gecenin karartılması da O'nun işidir. Güneşin "kendi yerine girmesi"ni Kur'an, Zülkarneyn'in batı ucuna vardığı anlatıda gözle görülen bir sahne olarak verir: {ar:وَجَدَهَا تَغْرُبُ فِى عَيْنٍ حَمِئَةٍۢ, tr:vecedehâ tağrubu fî aynin hamie, gloss:onu kara balçıklı bir pınarda batıyor buldu, source:18:86}.

Kaynaklar: 113:1 ٱلْفَلَقِ ف ل ق B001; 113:1 ٱلْفَلَقِ ف ل ق B002; 113:3 غَاسِقٍ غ س ق B001; 113:3 غَاسِقٍ غ س ق B004; 113:3 وَقَبَ و ق ب B002

## Bulut, yağmur ve kaya çukuru

Surenin kelimeleri, kök ailelerinden dinlendiğinde, bulutla başlayıp kayadaki bir çukurla biten bütün bir yağmur sahnesini taşır. Rab kelimesinin kökü alçakta asılı duran bulutun adıdır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}; büyük bulutun altında sarkan, ak ya da kara bir buluttur bu: {ar:السحاب المتعلق دون السحاب يكون أبيض ويكون أسود, tr:es-sehâbu'l-muteallaku dûne's-sehâb yekûnu ebyada ve yekûnu esved, gloss:bulutun altında asılı duran bulut; ak da olur kara da, source:"ر ب ب,B008"}. Bulut yerinde durur: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe: dâmet, gloss:bulut kalıcı oldu, source:"ر ب ب,B007"}. Halk kökü onun düzgünce yayılışını adlandırır: {ar:اخلولق السحاب استوى, tr:iḣlevlaka's-sehâbu'stevâ, gloss:bulut düzgünce yayıldı, source:"خ ل ق,B008"}. Ukad kökü yığılışını: {ar:تعقد السحاب إذا صار كأنه عقد مضروب مبني, tr:teakkade's-sehâbu izâ sâra ke-ennehû akdun madrûbun mebnî, gloss:bulut, kurulmuş bir kemer gibi olduğunda "teakkade" denir, source:"ع ق د,B008"}. Sonra felak kökü bulutun yağmurla yarılmasını söyler: {ar:فلق الأرض بالنبات والسحاب بالمطر, tr:felaka'l-arda bi'n-nebâti ve's-sehâbe bi'l-matar, gloss:toprağı bitkiyle, bulutu yağmurla yardı, source:"ف ل ق,B003"}. Gök çiseler ve gāsık "akan" olur: {ar:غسقت السماء أرشت, tr:ğasakati's-semâu erasşet, gloss:gök çiseledi, source:"غ س ق,B004"}, {ar:الغاسق بمعنى السائل, tr:el-ğāsiku bi-ma'ne's-sâil, gloss:gāsık, akan anlamındadır, source:"غ س ق,B004"}.

Su aşağı iner. Felak kökü iki tepe arasındaki alçak yerin de adıdır: {ar:الفلق المطمئن من الأرض بين الربوتين, tr:el-felaku'l-mutmainnu mine'l-ardı beyne'r-rabveteyn, gloss:felak, iki tümsek arasındaki çukur yerdir, source:"ف ل ق,B004"}. Su orada toplanır, dağdaki bir oyuğa dolar: {ar:الوقب في الجبل نقرة يجتمع فيها الماء, tr:el-vakbu fi'l-cebel nukratun yectemiu fîhe'l-mâ', gloss:vakb, dağda suyun toplandığı oyuktur, source:"و ق ب,B001"}. Vekab fiili de bu oyuğa girmektir: {ar:وقب الشيء دخل في وقبة, tr:vekabe'ş-şey'u dehale fî vakbe, gloss:şey bir oyuğa girdi, source:"و ق ب,B002"}. İkinci ayetin halk kökü aynı oyuğu neredeyse aynı sözle adlandırır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-ḣalîka nakrun fî sahratin yectemiu fîhi mâu's-semâ', gloss:halîka, kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}; o oyukların bulunduğu kaya da bu kökle düzdür: {ar:صخرة خلقاء أي ملساء, tr:sahratun ḣalkâ' ey melsâ', gloss:halkâ kaya, yani pürüzsüz kaya, source:"خ ل ق,B008"}. Rab kökü toplanan bol suyun adıdır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab ve huve'l-mâu'l-kesîr, summiye bi-zâlike li-ictimâih, gloss:rabab bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Sahnenin sonunda bir ters dönüş de vardır: {ar:إذا أطبق الوادي على قوم فأهلكهم عقد عليهم, tr:izâ etbaka'l-vâdî alâ kavmin fe-ehlekehum akade aleyhim, gloss:vadi bir topluluğun üstüne kapanıp onları helak ettiğinde "akade aleyhim" denir, source:"ع ق د,B016"}.

Bu imge üçüncü ayetin girişini başka bir duyuyla duyurur. Gecenin tepelere "döküldüğü" yukarıda görülmüştü; burada {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}, suyun kayadaki oyuğa girip onu doldurması gibi işitilir. Akan şey alçak olan her yeri bulur ve oraya yerleşir. Aynı su toprağı yarıp bitki çıkarır, oyukta toplanıp içilir, ama vadi bir topluluğun üstüne kapandığında öldürür. İkinci ayetin "yarattığı şeylerin şerri" bu sahnede kendi başına kötü bir madde olarak değil, hayat veren bir şeyin yön değiştirmesi olarak görünür. Kur'an da yağmuru bu iki yüzüyle sahneler. "Görmedin mi" diye başlayan bir işaret ayetinde Allah bulutun sürülüp birleştirilişini, yığılışını ve içinden yağmurun çıkışını anlatır: {ar:يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ, tr:yuzcî sehâben summe yuellifu beynehû summe yec'aluhû rukâmen fe-tera'l-vedka yaḣrucu min ḣilâlih, gloss:bir bulutu sürer, sonra parçalarını birleştirir, sonra üst üste yığar; yağmurun aralarından çıktığını görürsün, source:24:43}. Aynı ayet dolunun kime ineceğini de söyler: {ar:فَيُصِيبُ بِهِۦ مَن يَشَآءُ وَيَصْرِفُهُۥ عَن مَّن يَشَآءُ, tr:fe-yusîbu bihî men yeşâu ve yasrifuhû an men yeşâ', gloss:onu dilediğine isabet ettirir, dilediğinden de çevirir, source:24:43}. Sığınmanın işleyişi buradadır: aynı bulutun zararı birine iner, birinden çevrilir; çeviren de bulutun Rabbidir. Hak ile batılın bir örneğinde gökten inen su vadileri ölçüleri kadar doldurur: {ar:أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:enzele mine's-semâi mâen fe-sâlet evdiyetun bi-kaderihâ, gloss:gökten su indirdi, vadiler kendi ölçülerince aktı, source:13:17}; köpük gider, insanlara yarayan yerde kalır. Münafıkları anlatan bir örnekte de yağmur karanlığı birlikte getirir: {ar:أَوْ كَصَيِّبٍۢ مِّنَ ٱلسَّمَآءِ فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ, tr:ev ke-sayyibin mine's-semâi fîhi zulumâtun ve ra'dun ve berk, gloss:ya da gökten boşanan, içinde karanlıklar, gök gürültüsü ve şimşek bulunan bir sağanak gibi, source:2:19}. Gecenin dökülüşü ile yağmurun dökülüşü bu sahnede tek bir gökten iner.

Kaynaklar: 113:1 بِرَبِّ ر ب ب B008; 113:1 بِرَبِّ ر ب ب B007; 113:2 خَلَقَ خ ل ق B008; 113:4 ٱلْعُقَدِ ع ق د B008; 113:1 ٱلْفَلَقِ ف ل ق B003; 113:3 غَاسِقٍ غ س ق B004; 113:1 ٱلْفَلَقِ ف ل ق B004; 113:3 وَقَبَ و ق ب B001; 113:3 وَقَبَ و ق ب B002; 113:2 خَلَقَ خ ل ق B011; 113:2 خَلَقَ خ ل ق B008; 113:1 بِرَبِّ ر ب ب B013; 113:4 ٱلْعُقَدِ ع ق د B016

## Göz: oyuğu, kararması, akması

Surenin üç kelimesinin kök ailesinde göz vardır. Vekab kökü dağdaki su oyuğunu adlandırdığı aynı ifadede gözün oyuğunu da adlandırır: {ar:ووقب العين نقرتها, tr:ve vakbu'l-ayni nukratuhâ, gloss:gözün vakbı onun çukurudur, source:"و ق ب,B001"}. Gāsık kökü gözün kararmasını: {ar:غسقت عينه أظلمت, tr:ğasakat aynuhû azlemet, gloss:gözü karardı, source:"غ س ق,B003"}; ve gözün akmasını: {ar:غسقت العين وهو هملان العين بالغمص والماء, tr:ğasakati'l-ayn ve huve hamelânu'l-ayni bi'l-ğaması ve'l-mâ', gloss:"göz ğasakat oldu", gözün çapak ve suyla akmasıdır, source:"غ س ق,B004"}. Sığınma kökü ise insanın üstüne "gözden" korunmak için asılan şeyleri adlandırır: {ar:التعاويذ التي تكتب وتعلق على الإنسان من العين تسمى المعاذات, tr:et-teâvîzu'lletî tuktebu ve tuallaku ale'l-insâni mine'l-ayn tusemmâ'l-meâzât, gloss:gözden korunmak için yazılıp insanın üstüne asılan muskalara "meâzât" denir, source:"ع و ذ,B002"}. Haset de bir görmeyle başlar: {ar:الحسد أن يرى الإنسان لأخيه نعمة, tr:el-hasedu en yerâ'l-insânu li-eḣîhi ni'me, gloss:haset, insanın kardeşinde bir nimet görmesidir, source:"ح س د,B001"}.

Bu ayrıntılar bir araya geldiğinde surede bir gözler sahnesi belirir. Göz bir oyuktur; üçüncü ayetin karanlığı, dağdaki oyuğa giren su gibi bu oyuğa da girebilir ve gözü karartır. Beşinci ayetin hasetçisi bir gözle başlar: başkasındaki nimeti görür. İlk ayetin sığınması da kökünde gözlere karşı bir korunmanın adını taşır. Sade bir anlam gecenin karanlığını ve hasetçinin kötülüğünü iki ayrı şey olarak sayar; bu imge ikisini aynı organda buluşturur: karanlık gözü karartır, haset gözden doğar, sığınma göze karşı yapılır. Ayetlerin anlamı yine gecedir ve hasettir; göz, bu kelimelerin ailesinde onların yanında duran bir yerdir.

Kur'an bakışın bir güç olduğunu kendi sözüyle söyler. Allah Peygambere hitap eder: {ar:وَإِن يَكَادُ ٱلَّذِينَ كَفَرُوا۟ لَيُزْلِقُونَكَ بِأَبْصَٰرِهِمْ لَمَّا سَمِعُوا۟ ٱلذِّكْرَ, tr:ve in yekâdu'llezîne keferû le-yuzlikûneke bi-ebsârihim lemmâ semiu'z-zikr, gloss:inkâr edenler zikri işittiklerinde neredeyse bakışlarıyla seni kaydıracaklardı, source:68:51}. Bakışlar bir insanı yerinden kaydıracak kadar ağırdır ve bu bakış, okunan bir söze karşı yükselir. Hasedin başladığı yer olan uzanan göz de Kur'an'da ayrıca durdurulur: {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ, tr:ve lâ temuddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhum, gloss:onlardan bazı gruplara verdiğimiz geçimliğe gözlerini dikme, source:20:131}; ayet karşılığını da verir: {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike ḣayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131}. Aynı emir başka bir surede de tekrarlanır {source:15:88}. Başkasının nimetine uzanan gözün karşısına Rabbin rızkı konur. Büyü de göze işler: Firavun'un büyücüleri iplerini attıklarında {ar:سَحَرُوٓا۟ أَعْيُنَ ٱلنَّاسِ, tr:seharû a'yune'n-nâs, gloss:insanların gözlerini büyülediler, source:7:116}. Dördüncü ayetin büyüsü de böylece göze bağlanır. Sığınmanın gözü yeniden açtığını ise şeytanın dürtmesine karşı sığınma emrinin hemen ardından gelen ayet söyler: {ar:إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ, tr:inne'llezîne'ttekav izâ messehum tâifun mine'ş-şeytâni tezekkerû fe-izâ hum mubsırûn, gloss:sakınanlara şeytandan bir dokunuş eriştiğinde düşünüp hatırlarlar, bir de bakarsın ki görüyorlar, source:7:201}. Kararan göz, hatırlamayla görür hâle gelir. Yusuf'un kıssasında ise kardeşlerin hasedinin sonucu bir babanın gözünde görünür: {ar:وَٱبْيَضَّتْ عَيْنَاهُ مِنَ ٱلْحُزْنِ, tr:vebyaddat aynâhu mine'l-huzn, gloss:gözleri üzüntüden ağardı, source:12:84}.

Kaynaklar: 113:3 وَقَبَ و ق ب B001; 113:3 غَاسِقٍ غ س ق B003; 113:3 غَاسِقٍ غ س ق B004; 113:1 أَعُوذُ ع و ذ B002; 113:5 حَاسِدٍ ح س د B001

## İçeride tutulan, dışarı çıkan

Surenin birçok kelimesi, içeride tutulan bir şeyin dışarı çıkışını adlandırır. Üfleme kökü, göğsü sıkışan için bir zorunluluk söyler: {ar:لا بد للمصدور أن ينفث, tr:lâ budde li'l-masdûri en yenfus, gloss:göğsü dolan, mutlaka üfleyip boşaltır, source:"ن ف ث,B003"}. Yılan zehrini üfler: {ar:الحية تنفث السم, tr:el-hayyetu tenfusu's-semm, gloss:yılan zehir üfler, source:"ن ف ث,B001"}. Yara kanı dışarı verir: {ar:دم نفيث نفثه الجرح أي أظهره, tr:demun nefîsun nefesehu'l-curhu ey azharah, gloss:yaranın üfleyip çıkardığı, yani ortaya koyduğu kan, source:"ن ف ث,B002"}. Üçüncü ayetin kökü de yaranın akıntısını adlandırır: {ar:غسق الجرح غسقانا إذا سال منه ماء أصفر, tr:ğasaka'l-curhu ğasakânen izâ sâle minhu mâun asfar, gloss:yaradan sarı su aktığında "ğasaka" denir, source:"غ س ق,B004"}; ve ateşte olanların derisinden damlayanı: {ar:الغساق ما تقطر من جلود أهل النار, tr:el-ğassâku mâ tekattara min culûdi ehli'n-nâr, gloss:ğassâk, ateş ehlinin derilerinden damlayandır, source:"غ س ق,B002"}. Şer kökü ateşten uçuşan kıvılcımı: {ar:الشرر ما تطاير من النار الواحدة شررة, tr:eş-şeraru mâ tetâyera mine'n-nâr, el-vâhidetu şerara, gloss:şerar, ateşten uçuşandır; tekili şerara, source:"ش ر ر,B003"}; ve yukarıda görülen "çıkarıp göstermek" anlamını taşır: {ar:أشررت الشيء أظهرته, tr:eşrartu'ş-şey'e azhartuh, gloss:şeyi ortaya koydum, source:"ش ر ر,B008"}. Yaranın kanını "ortaya koyan" fiil ile bu fiil aynıdır.

Öfke de önce bağlanır, sonra çıkar: {ar:عقد ناصيته إذا غضب فتهيأ للشر, tr:akade nâsiyetehû izâ ğadibe fe-teheyyee li'ş-şerr, gloss:öfkelenip kötülüğe hazırlandığında perçemini düğümledi denir, source:"ع ق د,B012"}. Haset de bir istek olarak içeride durur, sonra bir çabaya dönüşür: {ar:وربما كان مع ذلك سعي في إزالتها, tr:ve rubbemâ kâne mea zâlike sa'yun fî izâletihâ, gloss:bazen bununla birlikte onu gidermeye çalışmak da olur, source:"ح س د,B001"}. Sözün de içeride tutulan bir hâli vardır: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde ortaya koymadığım bir söz var, source:"ق و ل,B012"}.

Bu imge surenin iki "izâ" cümlesine bir yön verir. Üçüncü ayette karanlık içeri girer: {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}. Beşinci ayette haset dışarı çıkar: {ar:إِذَا حَسَدَ, tr:izâ hased, gloss:haset ettiğinde, source:113:5}. Biri dışarıdan içeriye, öbürü içeriden dışarıya bir eşik geçişidir ve sığınma tam bu eşiklere yönelir. Karanlık henüz girmemişken, haset henüz çabaya dönmemişken zarar beklemededir; tehlike geçiş anındadır. Düğümlenen öfke ile düğüme üflenen nefes de aynı eşikte durur: tutulan şey bir yere bırakılır. Emredilen söz ise bunların karşısında konuşanın kendi çıkarışıdır. "Kul" emri, içeride duran sığınma sözünü dışarı çıkarır; zehir, irin ve kıvılcım dışarı çıkarken sığınan da kendi sözünü çıkarır.

Kur'an bu çıkışı düşmanca yakınlar hakkında Allah'ın müminlere uyarısında sahneler: {ar:قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ, tr:kad bedeti'l-bağdâu min efvâhihim ve mâ tuḣfî sudûruhum ekber, gloss:öfke ağızlarından taşmıştır; göğüslerinin sakladığı ise daha büyüktür, source:3:118}. Ağızdan çıkan, göğüste tutulanın bir parçasıdır. Ayetler devam eder: {ar:وَإِذَا خَلَوْا۟ عَضُّوا۟ عَلَيْكُمُ ٱلْأَنَامِلَ مِنَ ٱلْغَيْظِ ۚ قُلْ مُوتُوا۟ بِغَيْظِكُمْ, tr:ve izâ ḣalev addû aleykumu'l-enâmile mine'l-ğayz, kul mûtû bi-ğayzikum, gloss:yalnız kaldıklarında size karşı öfkeden parmak uçlarını ısırırlar; de ki: öfkenizle ölün, source:3:119}. Öfke içeride tutulur ve onun karşısına yine emredilen bir "de ki" konur. Hemen ardından gelen ayette ise iyiliğin onları üzdüğü söylenir {source:3:120}. Kıvılcım ve akıntı Kur'an'da ateşin sahnesine aittir. Ayırma Günü'nü anlatan ayetlerde ateş için {ar:إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ, tr:innehâ termî bi-şerarin ke'l-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32} denir; azgınların içeceği de {ar:هَٰذَا فَلْيَذُوقُوهُ حَمِيمٌۭ وَغَسَّاقٌۭ, tr:hâzâ fe'l-yezûkûhu hamîmun ve ğassâk, gloss:işte bu; tatsınlar onu: kaynar su ve irin, source:38:57} olur; başka bir yerde de yalnızca {ar:إِلَّا حَمِيمًۭا وَغَسَّاقًۭا, tr:illâ hamîmen ve ğassâkâ, gloss:kaynar su ve irinden başka, source:78:25}. Şer kelimesinin akrabası kıvılcım, gāsık kelimesinin akrabası irin, böylece ateşte dışarı atılanın adları olarak Kur'an'da geçer. Ayetteki şer de gāsık da bu anlamlarda değildir; ama aynı köklerden çıkan bu sözler, içeride tutulan zararın bir gün dışarı atılacağını yanlarında duyurur.

Kaynaklar: 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B003; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B001; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B002; 113:3 غَاسِقٍ غ س ق B004; 113:3 غَاسِقٍ غ س ق B002; 113:2 شَرِّ ش ر ر B003; 113:2 شَرِّ ش ر ر B008; 113:4 ٱلْعُقَدِ ع ق د B012; 113:5 حَسَدَ ح س د B001; 113:1 قُلْ ق و ل B012

## Buluşmalar

Gece ile yarılıp çıkarılış ilk buluşmadır. Sabah, yarılıp çıkarılan şeylerin bir örneğidir: karanlık yarılır ve ışık açığa konur; tohum yarılır ve filiz çıkar. Göğün kuruluşunu anlatan ayet ikisini aynı fiille birleştirir; gece karartılır ve kuşluk dışarı çıkarılır {source:79:29}. Kur'an aynı çıkarılışı insanlar için de söyler: {ar:ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:allâhu veliyyu'llezîne âmenû, yuḣricuhum mine'z-zulumâti ile'n-nûr, gloss:Allah inananların dostudur; onları karanlıklardan aydınlığa çıkarır, source:2:257}. Üçüncü ayetin karanlığına giren kişi, ilk ayetin Rabbine sığındığında bu çıkarılışın içine girer. Gece ile yağmur da birbirine dökülür: gece tepelere bir sıvı gibi boşalır, gök çiseler, ve aynı kök hem gecenin dökülüşünü hem göğün çiselemesini taşır. Felakın iki tepe arasındaki alçak yeri, gecenin döküldüğü tepelerin eteğidir; karanlık da su da oraya iner.

Şafağın iplikleri ile büyücünün iplikleri ikinci buluşmadır. Oruç ayetinde tan, beyaz ipliğin siyah iplikten ayrılmasıdır {source:2:187}; dördüncü ayette ise büyücüler ipliklere düğüm atar. Aynı malzeme iki zıt işleme uğrar: Rabbin sabahı iplikleri birbirinden ayırır, büyücünün eli iplikleri birbirine bağlar. Sure bu iki işlemi baştan ve sondan çerçeveler: ayıran Rab ilk ayettedir, bağlayan el dördüncüde. Musa'nın duasında da bir düğüm çözülür ve söz açığa çıkar {source:20:27} {source:20:28}; düğümü çözen Rab, sözü açılan kul. Böylece düğüm imgesi ile ağız imgesi aynı duada buluşur: dilin düğümü çözüldüğünde ağız konuşur, düğüme üfleyen ağız ise sözü bağlar.

Ağız ile ışık üçüncü buluşmadır. Namaz emrinde gecenin koyulaşmasının ardından sabahın okunuşu gelir {source:17:78}: karanlığın sonunda bir ağız okur. İnkâr edenler ise ağızlarıyla ışığa üfler: {ar:يُرِيدُونَ لِيُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَٱللَّهُ مُتِمُّ نُورِهِۦ, tr:yurîdûne li-yutfiû nûrallâhi bi-efvâhihim vallâhu mutimmu nûrih, gloss:Allah'ın nurunu ağızlarıyla söndürmek isterler; Allah ise nurunu tamamlayandır, source:61:8}. Bu ayette üç imge birden durur: ışığa karşı üfleyen ağızlar, söndürülmek istenen ışık ve o ışığı tamamlayan Allah. Düğüme üfleyen ağız ışığa karşı çalışır; emredilen ağız ışığın yanında durur. Işığı tamamlayan, nimeti tamamlayan Rabdir; hasetçinin sökmek istediği nimet ile inkârcının söndürmek istediği ışık aynı "tamamlama" fiiliyle korunur.

Musa'nın denizden geçişi dört imgeyi tek bir sahnede tutar. Gece yürüyüşü emredilir {source:26:52}; ordu güneş doğarken yetişir {source:26:60}; yanındakiler yakalandıklarını söyler {source:26:61}; Musa "Rabbim benimledir" der {source:26:62}; ve deniz felak kökünün fiiliyle yarılır {source:26:63}. Gece, korkulan ordu, Rabbe tutunan bir cümle ve yarılıp açılan bir yol aynı anlatıdadır. Sığınmanın bir uzaklaşma değil bir yakınlık olduğu da burada görünür: Musa'nın sözü "Rabbim benimledir"dir.

İmran'ın karısının kıssası doğum, sığınma ve büyüme imgelerini birleştirir. Rahimdekini adayan anne doğurur, doğurduğunu Rabbe sığındırır ve Rab onu bir bitki gibi büyütür {source:3:36} {source:3:37}. Burada sığınma kökü yeni doğurmuş dişinin adını taşırken, rab kökü hem doğan yavruyu büyütmeyi hem bir şeyi aşama aşama tamamlamayı taşır; tohumdan filiz çıkaran yarma da büyümenin ilk adımıdır. Rabbin bir çocuğu büyütmesi ile bir nimeti tamamlaması aynı köke aittir; Yakup'un Yusuf'a söylediği "nimetini sana tamamlayacak" sözü {source:12:6} bu yüzden doğumla başlayan büyütmenin sonucunu söyler.

Yusuf'un kıssası haset, göz ve uydurulmuş söz imgelerini birbirine bağlar. Bir rüya görülür ve anlatılmaması istenir, çünkü görülen bir nimet kardeşlerde tuzak doğurur {source:12:5}. Babanın yakınlığına bakan kardeşler o yakınlığın kendilerine kalmasını ister {source:12:9}; isteği bir plana, planı bir yalana dönüştürürler {source:12:18}. Hasedin sonucu bir babanın gözlerinde görünür {source:12:84}. Hasetçinin "haset ettiği an", gördüğü nimeti sökmek için harekete geçtiği andır ve bu an kendi arkasından uydurulan bir sözü getirir.

Surenin hareketi bu buluşmalarla görünür hâle gelir. İlk ayetin Rabbi yarar, açar ve çıkarır; ikinci ayette bu çıkarılmış şeylerin bütünü vardır. Üçüncü ayette karanlık dışarıdan içeri girer ve kapatır; dördüncü ayette bir el ipliğin uçlarını bağlar ve bir ağız onu nefesle mühürler; beşinci ayette içeride tutulan bir istek dışarı çıkar ve tamamlanmış bir nimeti sökmeye yönelir. Zarar her seferinde Rabbin işinin tersini yapar: O açarken karanlık kapatır, O ayırırken büyücü bağlar, O tamamlarken hasetçi söker. Sığınılan da sırf bu yüzden, her biri bu ters işlerden birinin karşısında duran "felakın Rabbi"dir. Kapsam da daralarak ilerler: önce bütün yaratılmışlar, sonra bir zaman olarak gece, sonra bir zanaatı olan kadınlar, en sonda tek bir hasetçi ve onun tek bir anı. Bu daralmanın karşısında ilk kelime sabit durur: emredilmiş bir söz, ağızdan çıkıp Rabbe yönelen ve söyleyeni O'na bağlayan bir sığınma.

