Focus: 111:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/111_3/D.r13/context.md =====
# 111:3 — focus

سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

Anchor translation (canonical reading, reference only):

Alevli bir ateşte yanacak.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | سَيَصْلَىٰ | يَصْلَى | ص ل ي | FUT;V |
| 2 | نَارًا | نَار | ن و ر | N |
| 3 | ذَاتَ | ذُو |  | N |
| 4 | لَهَبٍ | لَهَب | ل ه ب | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 111 — full text (context; no pericope)

- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 ◀ focus سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/111_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ل ي (root_000880) — identity root of سَيَصْلَىٰ (w1)

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ن و ر (root_001564) — identity root of نَارًا (w2)

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## ل ه ب (root_001379) — identity root of لَهَبٍ (w4)

- **B001** alev dili, ateşin tutuşması ve tutuşturulması — alev, ateş dili ve yanış · ateşten görünen alev · alevlenme ve yanma · ateşin yanması; alevsiz kor kızıllığı · ateş tutuştu ve alevlendi · ateşi tutuşturdu
  ارتفاع لسان النار (maqayis)؛ اللهب لهب النار (maqayis;jamhara;sihah)؛ اشتعال النار الذي قد خلص من الدخان (ayn;tahdhib)؛ التهبت النار وتلهبت وألهبتها (sihah;tahdhib)؛ اللهب اضطرام النار (mufradat)
- **B002** susuzluk ve susayana ya da kızgın zemine bağlı yakıcı sıcaklık — susuzluk · susuzluk ve susayana vuran sıcaklık · güneşte kızmış zeminin kavurucu sıcağı · susamış erkek · susamış kadın
  للعطشان لهبان (maqayis)؛ لهبان الحر في الرمضاء (ayn;tahdhib)؛ يستعمل اللهاب في النار والعطش جميعا (jamhara)؛ اللهبة العطش ورجل لهبان وامرأة لهبى (sihah;tahdhib)؛ اللهاب في الحر الذي ينال العطشان (mufradat)
- **B003** yükselen güçlü parıltı ve alevsi toz ya da duman — alev gibi yükselen parlak toz veya duman · ışığı yükselip güçlü biçimde parlayan her şey
  كل شيء ارتفع ضوؤه ولمع لمعانا شديدا (maqayis)؛ اللهب الغبار الساطع (maqayis;tahdhib)؛ يقال للدخان وللغبار لهب (mufradat)
- **B004** atın coşkun ve toz kaldıran şiddetli koşusu — at şiddetle ve coşkuyla koştu · şiddetle koşup toz kaldıran at · atın şiddetli koşusu ve atılışı
  فرس ملهب إذا أثار الغبار وله ألهوب (maqayis;tahdhib)؛ ألهب الفرس إذا عدا عدوا شديدا (jamhara)؛ ألهب الفرس إذا اضطرم جريه والاسم الألهوب (sihah)؛ فرس ملهب شديد العدو والألهوب العدو الشديد (mufradat)
- **B005** dağ yarığı, dağlar arası derin açıklık veya sarp dağ yüzü — 
  اللهب الشعب الصغير في الجبل (jamhara)؛ اللهب الفرجة والهواء يكون بين الجبلين (sihah)؛ اللهب وجه من الجبل كالحائط لا يستطاع ارتقاؤه (tahdhib)؛ اللهب مهواة ما بين كل جبلين (tahdhib)
- **B006** alevle ilişkili kişi, topluluk ve yer adları — alevle ilişkilendirilmiş bir künye · alevle ilişkilendirilmiş bir boy veya topluluk adı · bir yer adı · bir yer adı · bir kişi adı · bir kabile adı · bir vadi adı
  بنو لهب بطن من العرب (maqayis)؛ لَهاب موضع واللهباء موضع ولهبان اسم واللهبة قبيلة وبنو لهب قبيلة (jamhara)؛ كني أبو لهب به (sihah)؛ بنو لهب حي من العرب اللهبيون (tahdhib)؛ تبت يدا أبي لهب (mufradat)
- **B007** şimşeğin boşluksuz art arda çakması [kalıp] — şimşek arada boşluk bırakmadan art arda çaktı
  ألهب البرق إلهابا وإلهابه تداركه حتى لا يكون بين البرقتين فرجة (tahdhib)
- **B008** çarpıcı güzel kişi veya çok kıllı erkek — çarpıcı derecede güzel · çok kıllı erkek
  الملهب الرائع الجمال والملهب الكثير الشعر من الرجال (tahdhib)

## ECHO ص ل و (root_000879) — for سَيَصْلَىٰ (w1): withheld observed target; not identity

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

===== _commentary/v16/out/s111/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 111:3, and ## Buluşmalar) =====
## Alevin babası: ad ateşe dönüşür

Birinci ayet adamı alevden yapılmış bir künyeyle anar: {ar:أَبِى لَهَبٍۢ, tr:ebî leheb, gloss:alevin babası, source:111:1}. Kök bu adlandırmayı kendi içinde kaydeder, {ar:كني أبو لهب به, tr:kuniye Ebû Lehebin bihî, gloss:Ebû Leheb bununla künyelendi, source:"ل ه ب,B006"}, ve surenin kendi ifadesini bu anlamın altında anar: {ar:تبت يدا أبي لهب, tr:tebbet yedâ Ebî Leheb, gloss:Ebû Leheb'in iki eli kurudu, source:"ل ه ب,B006"}. Üçüncü ayet aynı kelimeyi bu kez ateşin niteliği olarak geri verir: {ar:سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ, tr:se-yaslâ nâran zâte leheb, gloss:alevli bir ateşe girip yanacak, source:111:3}. Adam "alevin babası"dır, ateş "alevin sahibi"; ad ile ateşin vasfı tek bir kelimeyi paylaşır ve künye, adamın varacağı yeri tarif eder hâle gelir.

"Baba" kelimesinin kökü bu sahneyi bir işleyişe çevirir. Baba yalnız doğuran değil, bir şeyi var eden, ayakta tutan, ortaya çıkarandır: {ar:الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا, tr:el-ebu el-vâlid, ve yusemmâ kullu men kâne sebeben fî îcâdi şey'in ev salâhihî ev zuhûrihî eben, gloss:baba doğurandır; bir şeyin var olmasına, düzelmesine ya da ortaya çıkmasına sebep olan herkese de baba denir, source:"ء ب و,B001"}. Kök ayrıca beslemeyi adlandırır: {ar:أبوت الشيء آبوه أبوا إذا غذوته, tr:ebevtu'ş-şey'e âbûhu ebven izâ ğazevtuh, gloss:bir şeyi besledim, source:"ء ب و,B001"}. Alevin babası böylece alevi doğuran ve onu besleyendir; üçüncü ayette beslediği alevin içine girer.

Alev kökü, ışığın yükselip parlamasını da adlandırır: {ar:كل شيء ارتفع ضوؤه ولمع لمعانا شديدا, tr:kullu şey'in irtefea dav'uhû ve leme'a lem'ânen şedîden, gloss:ışığı yükselen ve şiddetle parlayan her şey, source:"ل ه ب,B003"}. Üçüncü ayette ise aynı kelime düpedüz ateşin dilidir: {ar:ارتفاع لسان النار, tr:irtifâu lisâni'n-nâr, gloss:ateş dilinin yükselmesi, source:"ل ه ب,B001"}. Ateş kelimesinin kökü de ışıkla aynıdır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bizâlike min tarîkati'l-idâe, gloss:nur da ateş de aydınlatma yönünden bu adı aldı, source:"ن و ر,B001"}. Addaki parlaklık ile sondaki yanış aynı aydınlanmanın iki yüzüdür. Kök bir de deve damgasını bilir; hayvanın soyu damgasından okunur: {ar:نجارها نارها, tr:nicâruhâ nâruhâ, gloss:soyu damgasıdır, source:"ن و ر,B002"}. Burada da adam kimliğini taşıyan bir ateş adıyla anılır ve o ad sonunu söyler. Kur'an, biriktirilip Allah yolunda harcanmayan altın ve gümüşten söz ederken {source:9:34} ateşi damga olarak da sahneler: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum, gloss:cehennem ateşinde kızdırılıp alınlarının onunla dağlanacağı gün, source:9:35}.

Üçüncü ayetin kuruluşu Kur'an'da bir başka ateşte de geçer. Hendek sahiplerinin sahnesi, tıpkı surenin açılışı gibi geçmiş zamanlı bir lanet fiiliyle başlar, {ar:قُتِلَ أَصْحَٰبُ ٱلْأُخْدُودِ, tr:kutile ashâbu'l-uhdûd, gloss:kahrolsun hendek sahipleri, source:85:4}, ve hemen ardından ateşi kendi maddesinin sahibi olarak anar: {ar:ٱلنَّارِ ذَاتِ ٱلْوَقُودِ, tr:en-nâri zâti'l-vekûd, gloss:yakıtı bol ateş, source:85:5}. Lanet fiili, sonra "sahibi" kelimesiyle nitelenen ateş: bu, birinci ve üçüncü ayetin sırasıdır. Alev kelimesi ile fayda vermeme fiili ise yalanlayanların gönderildiği üç kollu gölgenin tarifinde bir araya gelir {source:77:30}: {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. İkinci ayette mal ona fayda vermedi; orada gölge alevden korumaz.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:1 لَهَبٍۢ ل ه ب B006; 111:1 لَهَبٍۢ ل ه ب B003; 111:3 لَهَبٍۢ ل ه ب B003; 111:3 لَهَبٍۢ ل ه ب B001; 111:3 نَارًۭا ن و ر B001; 111:3 نَارًۭا ن و ر B002

## Yakıt, tutuşma ve kızartılan

Üçüncü ve dördüncü ayet birlikte işleyen bir ateşi bütün parçalarıyla kurar: toplanıp sırtta taşınan odun, tutuşan yakıt, dumandan arınmış alev ve bu ateşe giren, onda kalan, sıcağına katlanan bir adam. Üçüncü ayetin fiili kendi kökünde hem yakıtı hem kızartmayı adlandırır: {ar:الصلاء يقال للوقود وللشواء, tr:es-silâu yukâlu li'l-vekûdi ve li'ş-şivâ, gloss:silâ, yakıt için de kebap için de söylenir, source:"ص ل ي,B004"}; {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-silâu mâ yustalâ bihî ve mâ yuzkâ bihi'n-nâru ve yûkad, gloss:silâ, kendisiyle ısınılan ve ateşin kendisiyle tutuşturulup yakıldığı şeydir, source:"ص ل ي,B004"}. Et ateşte böyle pişirilir: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. Böylece üçüncü ayetin fiili dördüncü ayetin odununu daha baştan içinde taşır ve adamı etin konduğu yere koyar.

Fiilin surede kurduğu yapı, kökün kayıtlı bir kullanımıyla birebir aynıdır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fehuve yaslâhâ, ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe yandı, yani sıcağına ve şiddetine katlandı, source:"ص ل ي,B003"}. Fiil girmeyi ve orada kalmayı da söyler: {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâr, ey yelzemu'n-nâr, gloss:ateşte yakılan, yani ateşten ayrılmayan, source:"ص ل ي,B003"}. Ateş kelimesi, kökünde ışığın yanında kıpırtıyı da taşır: {ar:ولأن ذلك يكون مضطربا سريع الحركة, tr:ve li-enne zâlike yekûnu muztariben serîa'l-hareke, gloss:çünkü o çalkantılı ve hızlı hareketlidir, source:"ن و ر,B002"}. Alev ise ateşin tam tutuşmuş hâlidir: {ar:اشتعال النار الذي قد خلص من الدخان, tr:iştiâlu'n-nâri'llezî kad halusa mine'd-duhân, gloss:dumandan arınmış ateşin yanışı, source:"ل ه ب,B001"}. Kök bu sıcaklığı susuzlukla da adlandırır: {ar:يستعمل اللهاب في النار والعطش جميعا, tr:yusta'melu'l-luhâbu fi'n-nâri ve'l-ataşi cemîan, gloss:luhâb hem ateş hem susuzluk için kullanılır, source:"ل ه ب,B002"}. Alevin içindeki aynı zamanda susuzdur.

Dördüncü ayet yakıtı getirir: {ar:وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ, tr:vemraetuhû hammâlete'l-hatab, gloss:karısı da, o odun hamalı, source:111:4}. Odun, yakmak için hazırlanmış şeydir, {ar:ما يعد للإيقاد, tr:mâ yu'addu li'l-îkâd, gloss:tutuşturmak için hazırlanan, source:"ح ط ب,B001"}, ve toplanır: {ar:حطبت واحتطبت إذا جمعته, tr:hatabtu vehtatabtu izâ cema'tuh, gloss:odun topladım, source:"ح ط ب,B001"}. Taşıma fiilinin temel sahnesi sırttır: {ar:حملت الشئ على ظهرى أحمله حملا, tr:hameltu'ş-şey'e alâ zahrî ahmiluhû hamlen, gloss:şeyi sırtımda taşıdım, source:"ح م ل,B001"}. Kelimenin kalıbı, bir defalık taşımayı değil, işi alışkanlık edinmiş, ağır yük taşıyan kişiyi söyler. Odun kökü insanı da odun diye anar: {ar:الحطب الرجل الشديد الهزال, tr:el-hatabu er-raculu'ş-şedîdu'l-huzâl, gloss:çok zayıf adam, source:"ح ط ب,B004"}, {ar:كأنه شبه بالحطب اليابس, tr:keennehû şubbihe bi'l-hatabi'l-yâbis, gloss:sanki kuru oduna benzetildi, source:"ح ط ب,B004"}. Kadının taşıdığı odun ile adamın yandığı ateş bir ve aynı ateştir.

Kur'an insanı ateşin yakıtı olarak açıkça anar. Cinler kendi aralarında konuşurken der ki: {ar:وَأَمَّا ٱلْقَٰسِطُونَ فَكَانُوا۟ لِجَهَنَّمَ حَطَبًۭا, tr:ve emme'l-kâsitûne fe-kânû li-cehenneme hatabâ, gloss:haktan sapanlara gelince, onlar cehenneme odun oldular, source:72:15}; surenin kelimesi burada insanların adıdır. Müşriklere ve taptıklarına söylenen sözde başka bir kelime aynı işi görür, {ar:حَصَبُ جَهَنَّمَ, tr:hasabu cehennem, gloss:cehenneme atılan yakıt, source:21:98}. Müminlere hitap eden ayette ateşin yakıtı insanlar ve taşlardır, {ar:وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:vekûduhe'n-nâsu ve'l-hicâra, gloss:yakıtı insanlar ve taşlardır, source:66:6}. Bir başka ayette mal ve evladın fayda vermeyişi doğrudan yakıta bağlanır: {ar:لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ, tr:len tuğniye anhum emvâluhum ve lâ evlâduhum mina'llâhi şey'en, ve ulâike hum vekûdu'n-nâr, gloss:malları da evlatları da onlara Allah'a karşı hiçbir fayda vermez; işte onlar ateşin yakıtıdır, source:3:10}. İkinci ayetten üçüncü ayete geçiş orada tek bir ayettir.

Fiilin ateşle kurduğu yapı Kur'an'da sabittir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}; {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Gelecek eki ile aynı fiil, öksüzlerin mallarını haksızca yiyenler için malın ardından gelir: {ar:وَسَيَصْلَوْنَ سَعِيرًۭا, tr:ve se-yaslevne seîrâ, gloss:alevli ateşe girip yanacaklar, source:4:10}; o ayet, yenen malın karınlarda zaten ateş olduğunu da söyler. Allah'ın tek yarattığı ve kendisine uzanıp giden mal ile yanında hazır oğullar verdiği adam hakkındaki pasajda {source:74:11}, mal {source:74:12} ve oğullar {source:74:13} sayıldıktan sonra aynı gelecek ve aynı kök gelir: {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu sekar'a sokup yakacağım, source:74:26}. Kızartma imgesi ayetlerine inkâr edenler için en açık hâlini alır: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ, gloss:derileri piştikçe yerine başka deriler koyarız, source:4:56}. Mal toplayıp sayan dedikoducunun ateşi de yakılmış bir ateştir, {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nâru'llâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Odun ile ateş arasındaki bağı Allah kendi yaratışında gösterir: {ar:ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا, tr:ellezî ceale lekum mine'ş-şeceri'l-ahdari nârâ, gloss:size yeşil ağaçtan ateş çıkaran, source:36:80}.

Kaynaklar: 111:3 سَيَصْلَىٰ ص ل ي B004; 111:3 سَيَصْلَىٰ ص ل ي B003; 111:3 نَارًۭا ن و ر B002; 111:3 لَهَبٍۢ ل ه ب B001; 111:3 لَهَبٍۢ ل ه ب B002; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 ٱلْحَطَبِ ح ط ب B004; 111:4 حَمَّالَةَ ح م ل B001

## Ev ocağı ve soy: tersine dönen hane

Bir ev; ailesi için kazanan bir erkek, bir eş, evlenmede ya da ev kurulurken verilen bir ziyafet, ev için toplanan odun ve et kızartılan, başında ısınılan bir ocakla döner. Surenin kelimeleri bu ev sahnesinin bütün parçalarını kökleriyle taşır. Kazanmak, ailesi için hayır kazanmaktır: {ar:فلان يكسب أهله خيرا, tr:fulânun yeksibu ehlehû hayran, gloss:falanca ailesine hayır kazandırır, source:"ك س ب,B002"}. Baba, besleyendir: {ar:فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده, tr:fulânun ye'bû hâze'l-yetîme ibâveten, ey yağzûhu kemâ yağzu'l-vâlidu veledeh, gloss:falanca bu yetime babalık eder, yani babanın çocuğunu beslediği gibi onu besler, source:"ء ب و,B001"}. Dördüncü ayetin ilk kelimesi eştir, {ar:هي امرأته, tr:hiye'mraetuh, gloss:o, onun karısıdır, source:"م ر ء,B001"}, ve kökü evin kuruluşundaki ziyafeti adlandırır: {ar:والمرء : الإطعام على بناء دار ، أو تزويج, tr:ve'l-mer'u el-it'âmu alâ binâi dârin ev tezvîc, gloss:mer', ev yapımında ya da evlenmede yemek vermektir, source:"م ر ء,B004"}. İkinci ayetin fiilinin kökü evliliği de adlandırır, {ar:الغنى التزويج, tr:el-ğınâ et-tezvîc, gloss:ğınâ, evlendirmedir, source:"غ ن ي,B006"}, ve kocasıyla yetinen kadını: {ar:الغانية المستغنية بزوجها عن الزينة, tr:el-ğâniye el-mustağniye bi-zevcihâ ani'z-zîne, gloss:ğâniye, kocası sayesinde süse ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Odun kökü birisi için odun toplamayı bilir, {ar:حطبت فلانا إذا احتطبت له, tr:hatabtu fulânen izehtatabtu leh, gloss:falancaya odun topladım, source:"ح ط ب,B001"}, ve üçüncü ayetin fiili ocağın kendisidir: ısınılan ve kızartılan ateş {source:"ص ل ي,B004"}.

Surede bu ev bütünüyle tersine döner. Kazanan erkeğin kazancı kendine bile yetmez; ikinci ayetin fiili, kocası karısına yeten evliliğin kökünden gelir ama burada koca kendini bile karşılayamaz. Eş, kocasının içinde yanacağı ateşe odun taşır; ev ocağı Ateş olur. Bu ters çevrilmenin karşı sahnesi Kur'an'da Mûsâ'dadır. Süresini doldurup ailesiyle yola çıkan Mûsâ, Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:لَعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:lealî âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealekum tastalûn, gloss:belki oradan size bir haber ya da bir ateş koru getiririm, belki ısınırsınız, source:28:29}; aynı söz başka bir yerde {ar:بِشِهَابٍۢ قَبَسٍۢ, tr:bi-şihâbin kabes, gloss:alınmış bir ateş parçasıyla, source:27:7} diye geçer {source:20:10}. Orada "ısınmak" fiili surenin "yanmak" fiiliyle aynı köktendir: bir koca ailesini ısıtmak için ateş getirir; burada bir eş, kocasının yanacağı ateşe odun taşır. Müminlere hitap eden ayet, insanın kendini ve ailesini yakıtı insanlar olan bir ateşten korumasını ister: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kitabı arkasından verilen kişi için {source:84:10} yanmak, ailesi içindeki eski sevincin karşısına konur: {ar:وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:ve yaslâ seîran innehû kâne fî ehlihî mesrûrâ, gloss:alevli ateşe girer; çünkü o ailesi içinde sevinçliydi, source:84:12}. Allah'ın inkâr edenlere örnek verdiği Nûh'un ve Lût'un karılarında eş, fayda vermeme fiili ve Ateş bir araya gelir: {ar:فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ, tr:felem yuğniyâ anhumâ mina'llâhi şey'en ve kîle'dhulâ'n-nâra mea'd-dâhilîn, gloss:kocaları onlara Allah'a karşı hiçbir fayda vermedi ve onlara "girenlerle birlikte ateşe girin" denildi, source:66:10}. Hemen ardından Firavun'un karısı, kocasından ve onun işinden kurtarılmayı dileyen bir eş olarak gelir {source:66:11}: evlilik orada kaderi paylaştırmaz. Surede ise eş ve koca aynı ateşin iki ucundadır.

Dördüncü ve beşinci ayetin iki kelimesi bu evin bir başka parçasını, soyu da işitir. Taşımak, kökünde hamileliktir: {ar:حملت المرأة حبلت, tr:hamelet'il-mer'etu hebilet, gloss:kadın gebe kaldı, source:"ح م ل,B002"}, {ar:الحمل ما كان في بطن, tr:el-hamlu mâ kâne fî batn, gloss:haml, karında olandır, source:"ح م ل,B002"}. İp de kökünde aynı şeydir: {ar:الحبل الحمل وقد حبلت المرأة فهي حبلى, tr:el-habelu el-hamlu ve kad hebileti'l-mer'etu fe-hiye hublâ, gloss:habel gebeliktir; kadın gebe kaldı, o hâmiledir, source:"ح ب ل,B006"}. Bir tanım, iki kelimeyi birbiriyle açıklar ve gebeliğin ipe benzerliğini günlerin onunla uzamasında görür: {ar:الحبل وهو الحمل وذلك أن الأيام تمتد به, tr:el-habelu ve huve'l-hamlu ve zâlike enne'l-eyyâme temteddu bih, gloss:habel gebeliktir, çünkü günler onunla uzar, source:"ح ب ل,B006"}. Kadının iki ayetindeki iki kelime, onun taşıyacağı soyun kelimeleridir; oysa sahnede taşıdığı odun, boynundaki iptir. Birinci ayetin baba kelimesi bu soyun öbür ucunu tutar {source:"ء ب و,B001"}. Kur'an, ikinci ayetin cümlesini başka yerlerde malın yanına evladı koyarak kurar: {ar:مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا, tr:men lem yezidhu mâluhû ve veleduhû illâ hasârâ, gloss:malı ve evladı kendisine kayıptan başka bir şey katmayan, source:71:21}. Bu, Nûh'un kavminin kendisine isyan edip izledikleri önderlerden yakınmasıdır; "kayıp" kelimesi de tebâbın tanımında geçen kelimedir. İbrâhîm'in duasında o gün {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88} diye anılır. Mal ile evladın onlara fayda vermediği ve onların ateşin ehli olduğu ayette {source:58:17} ve yukarıda geçen ayette {source:3:10} bu ikili ikinci ve üçüncü ayetin sırasını kurar. Surede ikinci sırada "kazandığı" durur; o yerde evladı duymak bir okumadır, kelimenin söylediği değil. Suçlunun o gün kurtulmak için fidye olarak vermek isteyeceği şeyler de bu evin halkıdır: {ar:بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ, tr:bi-benîhi ve sâhibetihî ve ehîh, gloss:oğulları, eşi ve kardeşiyle, source:70:12}.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:2 كَسَبَ ك س ب B002; 111:2 أَغْنَىٰ غ ن ي B006; 111:2 أَغْنَىٰ غ ن ي B005; 111:3 سَيَصْلَىٰ ص ل ي B004; 111:4 وَٱمْرَأَتُهُۥ م ر ء B001; 111:4 وَٱمْرَأَتُهُۥ م ر ء B004; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 حَمَّالَةَ ح م ل B002; 111:5 حَبْلٌۭ ح ب ل B006

## Odun taşıyan, söz taşıyan

Dördüncü ayetin ifadesi, dilin içinde başlı başına bir mecaz olarak da kayıtlıdır: {ar:حمالة الحطب كناية عن النميمة, tr:hammâletu'l-hatabi kinâyetun ani'n-nemîme, gloss:odun hamalı, söz taşımanın kinayesidir, source:"ح ط ب,B003"}. Odun fiil olarak birinin aleyhine konuşmaktır: {ar:حطب فلان بفلان سعى به, tr:hatabe fulânun bi-fulânin seâ bih, gloss:falanca falancayı çekiştirdi, onu ele verdi, source:"ح ط ب,B003"}. Mecazın işleyişi de kayıtlıdır: söz taşıyan, ateşi kalın odunla besler: {ar:يوقد بالحطب الجزل كناية عن ذلك, tr:yûkidu bi'l-hatabi'l-cezli kinâyeten an zâlik, gloss:kalın odunla ateş yakar; bu, onun kinayesidir, source:"ح ط ب,B003"}. Taşıma fiili ise yükü de haberi de aynı kelimeyle söyler: {ar:حملت الثقل والرسالة والوزر حملا, tr:hameltu's-sikale ve'r-risâlete ve'l-vizra hamlen, gloss:ağırlığı, mesajı ve vebali taşıdım, source:"ح م ل,B001"}. Yük taşımak, haber taşımak ve laf taşımak tek bir taşıma işidir. Odun yanacağı yere götürülür; laf insanlar arasına götürülür ve orada düşmanlık tutuşturur. Bu düşmanlığın adı da ateşin kökünden gelir: {ar:بينهم نائرة أي عداوة وشحناء, tr:beynehum nâiretun, ey adâvetun ve şahnâ, gloss:aralarında nâire var, yani düşmanlık ve kin, source:"ن و ر,B007"}. Alev kökünün tutuşturma fiili, taşınan yakıtın ateş alışını söyler: {ar:التهبت النار وتلهبت وألهبتها, tr:iltehebeti'n-nâru ve telehhebet ve elhebtuhâ, gloss:ateş alevlendi, ben onu alevlendirdim, source:"ل ه ب,B001"}. Karanlıkta rastgele odun toplayan, sözünü karıştıran kişinin adıdır: {ar:يقال للمخلط في كلامه حاطب ليل, tr:yukâlu li'l-muhallıtı fî kelâmihî hâtıbu leyl, gloss:sözünü karıştırana "gece oduncusu" denir, source:"ح ط ب,B002"}. Bu okumada kadının insanlar arasında beslediği ateş ile üçüncü ayetin ateşi karşılaşır.

Kur'an söz taşıyanı mal sahibiyle aynı tarifte verir. Allah Peygamber'e şöyle der: {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍۢ مَّهِينٍ, tr:ve lâ tutı' kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye uyma, source:68:10}, {ar:هَمَّازٍۢ مَّشَّآءٍۭ بِنَمِيمٍۢ, tr:hemmâzin meşşâin bi-nemîm, gloss:kusur arayan, laf taşıyıp dolaşan, source:68:11}, ve birkaç ayet sonra bu tavrın sebebini söyler: {ar:أَن كَانَ ذَا مَالٍۢ وَبَنِينَ, tr:en kâne zâ mâlin ve benîn, gloss:mal ve oğullar sahibi oldu diye, source:68:14}. Laf taşımak, mal ve oğullar: surenin ikinci ve dördüncü ayetlerinin malzemesi orada tek bir portrededir. Bir başka surede kusur arayan dedikoducu {ar:وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ, tr:veylün li-kulli humezetin lumeze, gloss:her arkadan çekiştirene, yüze karşı kusur bulana vay hâline, source:104:1}, mal toplayıp sayan {source:104:2} ve tutuşturulmuş ateşe atılan kişidir {source:104:6}. Allah'ın elinin bağlı olduğunu söyleyenlerin arasına Allah düşmanlık ve kin atar, ve bu düşmanlık ateş olarak sahnelenir: {ar:كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ, tr:kullemâ evkadû nâran li'l-harbi atfeehe'llâh, gloss:savaş için ne zaman bir ateş yaktılarsa Allah onu söndürdü, source:5:64}. Kazanmak ile taşımak bir ayette buluşur: bir suç kazanıp onu suçsuz birinin üstüne atan kişi {ar:فَقَدِ ٱحْتَمَلَ بُهْتَٰنًۭا وَإِثْمًۭا مُّبِينًۭا, tr:fe-kadi'htemele buhtânen ve ismen mubînâ, gloss:bir iftirayı ve apaçık bir günahı yüklenmiş olur, source:4:112}. İftira sahnesinin kendisinde de laf ağızdan ağıza taşınan bir şeydir, {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ, tr:iz telakkavnehû bi-elsinetikum, gloss:onu dillerinizle birbirinizden alırken, source:24:15}, ve orada her kişiye kazandığı günah düşer: {ar:لِكُلِّ ٱمْرِئٍۢ مِّنْهُم مَّا ٱكْتَسَبَ مِنَ ٱلْإِثْمِ, tr:li-kulli'mriin minhum me'ktesebe mine'l-ism, gloss:onlardan her kişiye kazandığı günah vardır, source:24:11}.

Kaynaklar: 111:4 حَمَّالَةَ ٱلْحَطَبِ ح ط ب B003; 111:4 ٱلْحَطَبِ ح ط ب B002; 111:4 حَمَّالَةَ ح م ل B001; 111:3 نَارًۭا ن و ر B007; 111:3 لَهَبٍۢ ل ه ب B001

## Tuzak: kurulan ve kurana dönen

İp kökü avcının tuzağını da adlandırır: {ar:الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه, tr:el-hablu masdaru habeltu's-sayde vehtebeltuh, ey ehaztuh, ve'l-hibâletu el-misyede, ve habâilu'l-mevti esbâbuh, gloss:habl, avı iple yakaladım fiilinin masdarıdır; hibâle tuzaktır; ölümün ipleri onun sebepleridir, source:"ح ب ل,B005"}. Tuzağa düşen hayvanın da adı vardır: {ar:المحبول الوحشي الذي نشب في الحبالة, tr:el-mahbûl el-vahşiyyu'llezî neşibe fi'l-hibâle, gloss:mahbûl, tuzağa takılan yaban hayvanıdır, source:"ح ب ل,B005"}. Felaket de bu sahneyle açıklanır: {ar:الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة, tr:el-hiblu ve hiye'd-dâhiye, ve vechuhû enne'l-insâne izâ duhiye fe-keennehû kad hubile, ey vekaa fi'l-hibâle, gloss:hibl felakettir; çünkü insan felakete uğradığında sanki iple yakalanmış, yani tuzağa düşmüştür, source:"ح ب ل,B011"}. Üçüncü ayetin fiilinin kökü de tuzak kurmayı bilir: {ar:المصلاة أن تنصب شركا ونحوه, tr:el-maslât en tensibe şereken ve nahveh, gloss:maslât, bir kapan ya da benzerini kurmaktır, source:"ص ل ي,B005"}, {ar:مصالي هي الأشراك واحدتها مصلاة, tr:mesâlî hiye'l-eşrâk, vâhidetuhâ maslât, gloss:mesâlî kapanlardır, tekili maslâttır, source:"ص ل ي,B005"}. Böylece surenin son iki kelimesinde, boyundaki ip ile yakılma fiilinde, birer tuzak sesi vardır. Birinci ayetin fiili de birilerinin başkalarını helak etmesini söyleyebilir: {ar:تببوهم تتبيبا أي أهلكوهم, tr:tebbebûhum tetbîben, ey ehlekûhum, gloss:onları helak ettiler, source:"ت ب ب,B001"}.

Bu sesler birlikte bir işleyiş gösterir: kurulan tuzak sonunda kurana kapanır, ip boyna geçer, felaket bir yakalanma olarak gelir. Kur'an bu işleyişi açıkça söyler: {ar:وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِۦ, tr:ve lâ yahîku'l-mekru's-seyyiu illâ bi-ehlih, gloss:kötü düzen ancak sahibini kuşatır, source:35:43}. Zayıf bırakılanların büyüklenenlere sitemi de gece ve gündüz kurulan düzeni boyundaki halkalara bağlar: {ar:بَلْ مَكْرُ ٱلَّيْلِ وَٱلنَّهَارِ, tr:bel mekru'l-leyli ve'n-nehâr, gloss:hayır, gece gündüz kurduğunuz düzendi, source:34:33}; aynı ayet {ar:وَجَعَلْنَا ٱلْأَغْلَٰلَ فِىٓ أَعْنَاقِ ٱلَّذِينَ كَفَرُوا۟, tr:ve cealne'l-ağlâle fî a'nâkı'llezîne keferû, gloss:inkâr edenlerin boyunlarına halkalar geçirdik, source:34:33} diye biter.

Kaynaklar: 111:5 حَبْلٌۭ ح ب ل B005; 111:5 حَبْلٌۭ ح ب ل B011; 111:3 سَيَصْلَىٰ ص ل ي B005; 111:1 تَبَّتْ ت ب ب B001

## Buluşmalar

İlk buluşma birinci ayetin kendisindedir: kuruyan eller, alevle adlandırılmış adama aittir. Alev kökünün surenin ifadesini kendi adlandırma anlamının altında anması {source:"ل ه ب,B006"} iki imgeyi tek bir tamlamada tutar: kaybeden eller ile ateşe giden ad aynı kişinin iki yüzüdür. Elin kaybı ile ateş, ikinci ve üçüncü ayetin sırasında birleşir. Kur'an bu sırayı başka bir surede aynı kelimelerle kurar: önce {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}, birkaç ayet sonra {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Fayda vermeme fiili ile alev kelimesi de bir ayette yan yanadır {source:77:31}.

Alev ile yakıt, adın içinde buluşur. Baba kökü besleyeni adlandırır {source:"ء ب و,B001"}, odun ise yakmak için hazırlanan şeydir {source:"ح ط ب,B001"}. Alevin babası alevi besleyen olarak birinci ayette durur, alevin yakıtı dördüncü ayette sırtta taşınır, ve ikisi üçüncü ayetin ateşinde birleşir. Aynı ateş ev ocağıyla da buluşur: yakma fiilinin kökü hem ısınılan ocağı hem Ateşi adlandırır {source:"ص ل ي,B004"}. Mûsâ'nın ailesine getirdiği ateşte {ar:لَعَلَّكُمْ تَصْطَلُونَ, tr:lealekum tastalûn, gloss:belki ısınırsınız, source:27:7} ile surenin {ar:سَيَصْلَىٰ, tr:se-yaslâ, gloss:yanacak, source:111:3} kelimesi aynı kökün iki ucudur. Odun bir de söz odunudur: yakıt olarak taşınan ile laf olarak taşınan aynı kelimedir, ve laf insanlar arasında ateşin kökünden adını alan bir düşmanlık tutuşturur {source:"ن و ر,B007"}. Mal toplayan dedikoducunun tutuşturulmuş ateşe atıldığı sahne {source:104:6} ve savaş için yakılan ateşler {source:5:64} bu iki odunu tek sahnede tutar.

Sırttaki yük ile boyundaki ip, beşinci ayetin ipinde birleşir: yular yük hayvanının boyun ipidir {source:"ح ب ل,B001"}, mesed de deve yününden bükülen iptir {source:"م س د,B001"}. Sırtına yük vurulmuş bir hayvanın boynunda yular vardır; kadının sırtında odun, boynunda ip vardır. Kur'an yük ile süsü bir ayette birleştirir: buzağı olayında İsrailoğulları {ar:حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ, tr:hummilnâ evzâren min zîneti'l-kavm, gloss:kavmin süs eşyasından yükler yüklendik, source:20:87} derler. Süs yük olur; surede gerdanlığın yeri ip taşır. Kazanç ile yük de bir ayette buluşur {source:6:164}: birinci ve ikinci ayetin kazanan elleri ile dördüncü ayetin taşıyan sırtı, kişinin kazandığının kendi yükü oluşunun iki yarısıdır.

El ile boyun, birinci ve beşinci ayet arasında buluşur. Elin boyna bağlanmasını yasaklayan talimat {source:17:29} ve esirgenen malın boyun halkasına dönüşmesi {source:3:180}, surenin iki ucunu tek bir bedende birleştirir: kazanan el ile bağlanan boyun. İp kendi içinde üç sahneyi birden tutar: boyundaki halka, avcının tuzağı ve kesilen bağ. Gece gündüz kurulan düzenin boyunlardaki halkalarla bittiği ayet {source:34:33} halka ile tuzağı, Allah'ın ipine tutunmayı ateş çukurunun kıyısına koyan ayet {source:3:103} bağ ile ateşi birleştirir. Bükümün ipe verdiği güç, birinde birleştirmeye, ötekinde bir boynu bağlamaya gider.

Surenin hareketi bedenin üzerinden ilerler: birinci ayette eller, ikinci ayette ellerin tuttuğu mal ve kazanç, üçüncü ayette bütün bedenin girdiği ateş, dördüncü ayette sırt, beşinci ayette boyun. Adamın kazanan elleri ile kadının taşıyan sırtı aynı ateşe çalışır; biri kazandığının kendisine yetmediğini görür, öteki taşıdığı odunun yandığı yere bağlanır. İlk kelime ellere düşen bir kayıp ve bir kesiştir, son kelime boyna geçen bükülmüş bir ip; arada, adın içinde daha baştan yanan alev durur.

