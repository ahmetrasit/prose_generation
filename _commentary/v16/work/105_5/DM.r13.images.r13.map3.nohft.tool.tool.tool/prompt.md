Focus: 105:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/105_5/D.r13/context.md =====
# 105:5 — focus

فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ

Anchor translation (canonical reading, reference only):

Böylece onları yenmiş ekin artığı gibi yaptı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَجَعَلَهُمْ | جَعَلَ | ج ع ل | CONJ;V;PRON |
| 2 | كَعَصْفٍ | عَصْف | ع ص ف | P;N |
| 3 | مَّأْكُولٍۭ | مَّأْكُول | ء ك ل | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 105 — full text (context; no pericope)

- 105:1 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ
- 105:2 أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ
- 105:3 وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ
- 105:4 تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ
- 105:5 ◀ focus فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ


===== _commentary/v16/work/105_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ع ل (root_000248) — identity root of فَجَعَلَهُمْ (w1)

- **B001** bir şeyi yapıp var etme — bir şeyi yapmak, yaratmak veya var etmek
  جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)
- **B002** birini veya şeyi belirli bir duruma getirme — bir şeyi belirli bir duruma, niteliğe veya konuma getirmek · bir şeyi belirli bir duruma getirmek
  جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)
- **B003** öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma — 
  جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)
- **B004** bir eylemi yapmaya başlama — bir şeyi yapmaya başlamak
  تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)
- **B005** iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme — bir iş karşılığında belirlenen ücret, ödeme veya ödül · önemli bir iş için ortaklaşa kararlaştırılan ödemeler · ona bir ödeme veya armağan ayırmak
  الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)
- **B006** kısa veya küçük hurma ağaçları — kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri
  الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)
- **B007** sıcak tencereyi indirme bezi ve onunla indirme — sıcak tencereyi ateşten indirmeye yarayan koruyucu bez · tencereyi koruyucu bezle ateşten indirmek
  الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)
- **B008** kara küçük yer hayvanı ve bunlarla dolu su — kara renkli küçük bir yer hayvanı · bu hayvanların çokça bulunduğu su
  الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)
- **B009** dişinin çiftleşmek için erkeği istemesi — çiftleşmek isteyen dişi köpek · dişinin çiftleşmek için erkeği istemesi
  كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)
- **B010** deve kuşu yavrusu — deve kuşu yavrusu
  الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)
- **B011** belirtilmemiş bir yer adı — kimliği belirtilmemiş bir yer adı
  الجَعْلة اسم مكان (maqayis)
- **B012** kısa, şişman ve inatçı olma — kısa, şişman ve inatçı kişi
  الجعل القصر مع السمن واللجاج (tahdhib)

## ع ص ف (root_001020) — identity root of كَعَصْفٍ (w2)

- **B001** tahıl kabuğu, ufalanmış ekin yaprağı ve ham biçilmiş bitki artığı — tahıl kabuğu, kuruyup ufalanmış ekin yaprağı veya olgunlaşmadan biçilmiş yeşil ekin · başak yaprağı ya da birikmiş saman · başaktan dökülen saman ve benzeri kırıntı · ekinin uçlarını ya da yapraklarını olgunlaşmadan biçmek · ekin artığı veya ekini bol yer · ekinden başak yaprağını ya da samanı almak
  العصف ما على الحب من قشور التبن (maqayis)؛ ما على ساق الزرع من الورق الذي يبس فتفتت (ayn;maqayis;tahdhib)؛ العصف بقل الزرع (sihah;tahdhib)؛ العصف والعصيفة الذي يعصف من الزرع وحطام النبت المتكسر (mufradat)
- **B002** önündekileri sürükleyip savuran ve kimi nesneleri kırıp ufaltan sert rüzgar — rüzgar şiddetlenip önüne gelenleri sürükledi · şiddetli rüzgar · nesneleri kırıp bitki kırıntısına çeviren sert rüzgar · şiddetli rüzgar · toz ve yaprak kaldıran rüzgarlar · sert rüzgarlı gün
  الريح العاصف الشديدة (maqayis)؛ الريح تعصف بما مرت عليه من جولان التراب (ayn)؛ عصفت الريح أي اشتدت فهي ريح عاصف وعصوف (sihah)؛ ريح عاصف ومعصفة إذا اشتدت والمعصفات الرياح التي تثير التراب والورق (tahdhib)؛ عاصفة ومعصفة تكسر الشيء فتجعله كعصف (mufradat)
- **B003** harekette hafiflik ve hız — harekette hafiflik ve hız · binicisini hızla götüren dişi deve · hızlı deve kuşu · at hızla geçti · dişi deve hızlandı · develerin su isteğiyle kuyu çevresinde dönüp toprağı ezerek toz kaldırması
  أصل واحد صحيح يدل على خفة وسرعة (maqayis)؛ ناقة عصوف تعصف براكبها أي تمضي به كسرعة الريح والعصف السرعة في كل شيء (ayn)؛ أعصف الفرس إذا مر مرا سريعا ونعامة عصوف وناقة عصوف أي سريعة (sihah)؛ العصف السرعة والعصوف السريعة من الإبل وأعصفت الناقة إذا أسرعت (tahdhib)
- **B004** alıp götürerek, yok ederek veya kırıp ufalayarak ortadan kaldırma — savaş topluluğu silip süpürdü ve yok etti · adam yok oldu · rüzgar onları alıp götürdü ya da yok etti · yok etme
  الحرب تعصف بالقوم تذهب بهم (maqayis)؛ الحرب تعصف بالقوم أي تذهب بهم وتهلكهم وأعصف الرجل أي هلك (sihah)؛ الإعصاف الإهلاك وتعصف بالدارع والحاسر أي تهلكهما وتعصف بهما أي تذهب بهما (tahdhib)؛ عاصفة ومعصفة تكسر الشيء فتجعله كعصف وعصفت بهم الريح تشبيها بذلك (mufradat)
- **B005** geçim kazanmak için çabalayıp çare arama — kazanma ve geçimlik · kazandı ve geçimini aradı · kazanç sağlamada becerikli ve çareli · kazanç uğruna didinme ve yorulma
  عصف واعتصف إذا كسب وهو ذو عصف أي حيلة (maqayis)؛ العصف الكسب وكذلك الاعتصاف (sihah)؛ يعتصف إذا طلب الرزق والعصف الرزق ويعصف ويعتصف أي يكسب ويطلب ويحتال والعصوف الكد (tahdhib)

## ء ك ل (root_000043) — identity root of مَّأْكُولٍۭ (w3)

- **B001** yeme, yiyecek ve yeme rolleri — yemek yemek · yiyecek · bir öğünlük yeme veya tek lokma · çok yiyen, obur · birlikte yemek yiyen kişi · başkasını doyuran kişi · yenilen şey, yiyecek · yenmek üzere hazırlanmış yiyecek
  الأكل معروف؛ أكلت الطعام أكلا ومأكلا؛ الأكل تناول المطعم؛ الأكلة المرة واللقمة؛ رجل أكول كثير الأكل؛ أكيلك الذي يؤاكلك؛ المؤكل المطعم
- **B002** ağaç ve ekin ürünü — ağacın meyvesi veya verimi
  أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر؛ أكل بستانك دائم وأكله ثمره؛ والأكل لما يؤكل قال تعالى أكلها دائم
- **B003** verilen pay ve geçimlik — dünya payı ve geniş geçimliği olan · yöneticilerin verdiği tahsisatlar · kişiye ayrılmış, hesabı sorulmayan pay
  الأكل حظ الرجل وما يعطاه من الدنيا؛ المأكلة ما جعل للإنسان لا يحاسب عليه؛ فلان ذو أكل إذا كان ذا حظ من الدنيا ورزق واسع؛ الأكل الطعمة؛ يعبر به عن النصيب
- **B004** malı harcama veya ele geçirme [kalıp] — malı harcamak veya tüketerek elden çıkarmak · insanların mallarını alıp onları sömürmek
  يستأكل قوما أي يأكل أموالهم؛ فلان يستأكل الضعفاء أي يأخذ أموالهم؛ يعبر بالأكل عن إنفاق المال؛ أكل المال بالباطل صرفه إلى ما ينافيه الحق
- **B005** ateşin tüketmesi, beslenmesi ve harlanması — ateş odunu yakıp tüketti · ateşi odunla besledi · ateş iyice harlandı · öfkesinden alevlendi · kılıç keskinliğinden parladı
  أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ الرجل إذا اشتد غضبه يأتكل؛ تأكل السيف أي توهج من الحدة؛ وعلى طريق التشبيه قيل أكلت النار الحطب
- **B006** aşınma, bozulma ve kaşıntı — beden veya baş kaşıntısı · dişlerde aşınma veya çürüme · deride işlenince ortaya çıkan ince kusurlu yer · gebe deve, yavrusunun çıkan tüyünden kaşınıp rahatsız oldu · aşınıp bozulmak
  الأكال الحكاك؛ الأكل في الأديم مكان رقيق؛ بأسنانه أكل؛ والأكال أن يتأكل عود أو شيء؛ في جسدي إكلة من الأكال؛ تأكل كذا فسد؛ أصابه إكال في رأسه وفي أسنانه
- **B007** av olmuş veya yenmek için ayrılmış hayvan — yırtıcının yiyip bıraktığı av · kurdun yediği koyun veya başka av · yenmek için ayrılıp beslenen koyun · ürünü yenmek üzere ayrılmış hurma ağaçları
  أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته؛ الأكولة من الشاء التي ترعى للأكل لا للنسل والبيع؛ الأكولة الشاة التي تعزل للأكل وتسمن؛ أكيلة السبع؛ الأكولة من الغنم ما يؤكل
- **B008** arkadan çekiştirip saygınlığı zedeleme [kalıp] — birinin saygınlığını arkadan çekiştirerek zedelemek · insanları sürekli arkalarından çekiştiren
  فلان ذو أكلة في الناس إذا كان يغتابهم؛ ذو أكلة وإكلة إذا كان يغتاب الناس؛ تأكل لحومنا وتغتابنا؛ أكل فلان فلانا اغتابه وكذا أكل لحمه
- **B009** söz taşıyarak arayı bozma [kalıp] — aralarında söz taşıyıp onları birbirine düşürmek · ara bozucu söz taşıyıcı
  آكلت بين القوم أفسدت؛ المؤكل النمام؛ الإيكال بين الناس السعي بينهم بالنمائم؛ آكلت بين القوم أي حرشت وأفسدت
- **B010** biçime bağlı adlandırmalar [kalıp] — bana yapmadığım veya almadığım şeyi yükledin · onu senin erişimine bıraktım
  أكلتني ما لم آكل أي ادعيته علي؛ آكلتني أيضا أي ادعيته علي؛ آكلتك فلانا إذا أمكنته منه؛ أليس قبيحا أن تؤكلني ما لم آكل
- **B011** bir başla doyacak kadar az topluluk [kalıp] — tek bir hayvan başının doyuracağı kadar az topluluk
  ما هم إلا أكلة رأس؛ هم أكلة رأس أي هم قليل يشبعهم رأس واحد؛ عبارة عن ناس من قلتهم يشبعهم رأس
- **B012** biçime bağlı adlandırmalar [kalıp] — ipliği çok, sık dokulu ve güçlü kumaş · akıl ve sağlam görüş sahibi kişi
  ثوب ذو أكل أي كثير الغزل؛ رجل ذو أكل ذو رأي وعقل؛ ثوب ذو أكل إذا كان كثير الغزل صفيقا؛ رجل ذو أكل إذا كان ذا عقل ورأي؛ ثوب ذو أكل كثير الغزل كذلك
- **B013** yemek yenilen kap veya yer — içinde yemek yenilen çanak veya tencere · kendisinden yemek yenilen yer
  المئكل إناء يؤكل فيه؛ المئكلة قصعة تشبع الرجلين والثلاثة؛ المأكلة والمأكلة الموضع الذي منه يؤكل؛ المئكلة ضرب من البرام وضرب من الأقداح وكل ما أكل فيه
- **B014** ete işleyen kesici veya vurucu araç [kalıp] — et kesen bıçak; ayrıca sivri sopa veya kamçı
  للسكين آكلة اللحم؛ آكلة اللحم عصا محددة؛ الأصل في هذا أنها السكين؛ قيل في آكلة اللحم إنها السياط

## ECHO ك ل ل (root_001315) — for مَّأْكُولٍۭ (w3): withheld observed target; not identity

- **B001** körelip güçten düşme — körelmek, yorulup güçten düşmek · körleşmiş, yorgun veya etkisiz · bineğini yorup güçten düşürmek
  خلاف الحدة وكل السيف واللسان والطرف (maqayis)؛ الكليل السيف الذي لا حد له ولسان كليل والكال المعيي (ayn)؛ كللت من المشي وكل السيف والريح والطرف واللسان (sihah)؛ الكليل السيف ولسان كليل والكال المعيي وثقل سمعه وكل بصره (tahdhib)؛ كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام (mufradat)
- **B002** bakımı başkasına yük olan — bakımı ve geçimi sahibine yük olan · yetim veya yakın aile desteği bulunmayan kişi · sahibinin taşıdığı, ona yük olan tapınma nesnesi · bakmakla yükümlü olduğum kişiler · yakınlarının geçim yükünü üstlenir duruma gelmek
  الكُلّ العيال واليتيم (maqayis)؛ الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل (ayn)؛ الكل العيال والثقل والكل اليتيم والكل الذي لا ولد له ولا والد (sihah)؛ الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه (tahdhib)
- **B003** bütün, tüm — bütün, tüm, tamamı
  كل اسم موضوع للإحاطة مضاف أبدا (maqayis)؛ كل لفظه واحد ومعناه جمع (sihah)؛ يقع كل على اسم منكور موحد فيؤدي معنى الجماعة وكلهم للإحاطة (tahdhib)؛ لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام (mufradat)
- **B004** üstsoy ve altsoy dışı mirasçılık — ana baba ve çocuk dışındaki yan kol mirasçılığı · yan koldan değil, doğrudan hakla miras almak · uzak kuzen · soy bakımından daha uzak olmak
  الكلالة هم الرجال الورثة وبنو العم الأباعد ومن مات وليس له ولد ولا والد (maqayis)؛ الكل النسب البعيد (ayn)؛ لم يرثه كلالة أي لم يرثه عن عرض والكلالة بنو العم الأباعد (sihah)؛ الكلالة من القرابة ما خلا الوالد والولد (tahdhib)؛ الكلالة اسم لما عدا الولد والوالد من الورثة (mufradat)
- **B005** çevresini kuşak gibi saran oluşum — taç veya süslü baş kuşağı · Ay'ın konaklarından biri, Akrep takımyıldızının başı · bir yerin çevresini dolaşan örtümsü bulut · çiçeklerle çevrili çayır · çevresi küçük bulut parçalarıyla sarılı bulut · başına taç takmak
  إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان (maqayis)؛ الإكليل شبه عصابة مزينة بالجواهر والإكليل من منازل القمر وروضة مكللة حفت بالنور (ayn)؛ الإكليل شبه عصابة ويسمى التاج إكليلا والإكليل منزل والسحاب كأن غشاء ألبسه وروضة مكللة وسحاب مكلل (sihah)؛ الغمام المكلل السحابة تكون حولها قطع والإكليل شبه عصابة والإكليل منزل (tahdhib)؛ الإكليل سمي بذلك لإطافته بالرأس (mufradat)
- **B006** ev biçimli ince koruyucu örtü — böceklerden koruyan ev biçimli ince örtü, cibinlik · mezar üzerine küçük kule veya kubbe biçimli yapı yükseltmek
  الكلة غشاء من ثوب يتوقى به من البعوض (ayn)؛ الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق (sihah)؛ الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب (tahdhib)
- **B007** göğüs — göğüs · göğüs
  الكلكل الصدر (maqayis)؛ الكلكل الصدر (ayn)؛ الكلكل والكلكال الصدر (sihah)؛ الكلكل فهو الصدر (tahdhib)؛ الكلكل الصدر (mufradat)
- **B008** kısa, kalın ve güçlü yapılı erkek [kalıp] — kısa, kalın, güçlü ve toplu yapılı erkek
  الكلكل القصير (maqayis)؛ الكلكل الرجل الضرب ليس بجد طويل والمربوع المجتمع الخلق (ayn)؛ رجل كلكل قصير غليظ مع شدة (sihah)؛ رجل كلكل وكلاكل وكوألل قصر وغلظ مع شدة (tahdhib)
- **B009** topluluklar, kümeler — topluluklar, kümeler
  الكلاكل من الجماعات كالكراكر من الخيل (ayn)؛ الكلاكل هي الجماعات كالكراكر (tahdhib)
- **B010** saldırıda ilerleme veya korkup geri durma; itaatsizlik — saldırıda durmadan ileri gitmek · savaşta korkup geri durmak · ona itaat etmemek, karşı gelmek
  كلل حمل ولعله أن يكون من المتضادات (maqayis)؛ المكلل الجاد حمل فكلل مضى قدما وقد يكون كلل بمعنى جبن (sihah)؛ المكلل الذي يحمل فلا يرجع حتى يقع بقرنه وكلل فلان فلانا لم يطعه (tahdhib)
- **B011** dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması — dişleri görünerek gülümsemek · bulutun içinden beyaz şimşek çakmak
  انكلت المرأة إذا ضحكت (maqayis)؛ انكل الرجل انكلالا تبسم وتنكل عن غر عذاب وانكلال الغيم بالبرق (sihah)؛ انكلت المرأة إذا تبسمت وانكل السحاب بالبرق إذا تبسم بالبرق (tahdhib)

===== _commentary/v16/out/s105/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 105:5, and ## Buluşmalar) =====
## Emekle kurulan düzen, yoldan çıkarılması ve iki "kılma"

Sûrenin iskeleti bir yapış ve iki kılmadır. {ar:فَعَلَ, tr:feale, gloss:yaptı, source:105:1} nasıl yapıldığı sorulan işi açar; {ar:يَجْعَلْ, tr:yec'al, gloss:kılmak, source:105:2} ve {ar:فَجَعَلَهُمْ, tr:fe-cealehum, gloss:onları ... kıldı, source:105:5} bu soruyu cevaplayan iki dönüştürmedir. Arada gönderme ve atma durur. Yapmak fiilinin kökü bir şeyi meydana getirmektir: {ar:أصل صحيح يدل على إحداث شيء من عمل وغيره, tr:aslun sahîhun yedullu alâ ihdâsi şey'in min amelin ve gayrih, gloss:bir işle ya da başka yolla bir şeyi meydana getirmeyi gösteren sağlam bir köktür, source:"ف ع ل,B001"}. Kılmak ise bir şeyi bir hâle sokmaktır: {ar:جعل صير, tr:ceale: sayyera, gloss:"ceale", "dönüştürdü" demektir, source:"ج ع ل,B002"}, {ar:جعله الله نبيا أي صيره, tr:cealehullâhu nebiyyen, ey sayyerah, gloss:Allah onu peygamber kıldı, yani o hâle getirdi, source:"ج ع ل,B002"}, ve yapıp ortaya koymaktır: {ar:جعلت الشيء صنعته, tr:cealtu'ş-şey'e: sana'tuh, gloss:şeyi "kıldım", yani yaptım, source:"ج ع ل,B001"}.

Bu iki kılmanın ilkinin nesnesi onların düzenidir: {ar:أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍ, tr:elem yec'al keydehum fî tadlîl, gloss:onların düzenini boşa çıkarmadı mı, source:105:2}. {ar:كَيْدَهُمْ, tr:keydehum, gloss:onların tuzağı, düzeni, source:105:2} kökü önce bir şey üzerinde güçle uğraşmaktır: {ar:يدل على معالجة لشيء بشدة, tr:yedullu alâ muâlecetin li-şey'in bi-şidde, gloss:bir şeyle sertçe uğraşmayı gösterir, source:"ك ي د,B001"}, {ar:كل شيء تعالجه فأنت تكيده, tr:küllu şey'in tuâlicuhû fe-ente tekîduh, gloss:uğraştığın her şeyi "keyd" edersin, source:"ك ي د,B001"}. Sonra bu emek gizli bir düzene, zarar vermeye kurulmuş bir hileye dönüşür: {ar:الكيد المكر وكاده يكيده كيدا ومكيدة, tr:el-keydu'l-mekr, ve kâdehû yekîduhû keyden ve mekîde, gloss:keyd, gizli tuzaktır, source:"ك ي د,B002"}, {ar:الكيد ضرب من الاحتيال, tr:el-keydu darbun mine'l-ihtiyâl, gloss:keyd bir tür hiledir, source:"ك ي د,B002"}, {ar:لأريدن بها سوءا, tr:le-urîdenne bihâ sû'â, gloss:ona mutlaka kötülük kastedeceğim, source:"ك ي د,B002"}. Kelime böylece bir yolculuğun emeğini ve onun bir hedefe kurulmuş kastını birlikte taşır.

İlk "kılma" bu emeği {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, source:105:2} içine yerleştirir. Kelime, birini ya da bir şeyi yoldan çıkarma eylemini anlatan bir mastardır; düzen kendiliğinden sapmaz, saptırılır. Kökün ilk resmi doğru yoldan ayrılmaktır: {ar:كل جائر عن القصد ضال, tr:küllu câ'irin ani'l-kasdi dâll, gloss:hedefe giden yoldan sapan herkes "dâll"dır, source:"ض ل ل,B001"}, {ar:ضل في الأرض إذا لم يهتد للسبيل, tr:dalle fi'l-ard izâ lem yehtedi li's-sebîl, gloss:yolu bulamadığında "yeryüzünde saptı" denir, source:"ض ل ل,B001"}. İkinci resim gidilen yeri bulamamaktır ve kullanımın kendi örneği bir mescit ile bir evdir: {ar:ضللت المسجد والدار إذا لم تهتد لهما, tr:daleltu'l-mescide ve'd-dâr izâ lem tehtedi lehumâ, gloss:mescide ve eve yolunu bulamadığında "onları kaybettim" dersin, source:"ض ل ل,B003"}; yanında sahibinin elinden kaçıp giden hayvan durur: {ar:أضل بعيره إذا أفلت فذهب, tr:edalle baîrahû izâ efleta fe-zeheb, gloss:devesi elinden kurtulup gidince "devesini kaybetti" denir, source:"ض ل ل,B003"}. Üçüncü resim gözden kaybolup erimektir: {ar:ضل اللبن في الماء ثم استهلك, tr:dalle'l-leben fi'l-mâ'i summe'stuhlik, gloss:süt suyun içinde kayboldu, sonra tükendi, source:"ض ل ل,B002"}, {ar:أضل الميت إذا دفن, tr:udille'l-meyyit izâ dufin, gloss:ölü gömülünce "kaybettirildi" denir, source:"ض ل ل,B002"}. Düzenin akıbeti bu üç adımda yürür: hedefe kurulmuş bir emek yoldan çıkarılır, hedefini bulamaz, sonunda suya karışan süt gibi iz bırakmadan erir. Dördüncü ayetin fiil kökü yola çıkmayı ve niyet edilen yönü de taşır: {ar:رمى الرجل إذا سافر, tr:ramâ'r-racul izâ sâfer, gloss:adam yolculuğa çıkınca "attı" denir, source:"ر م ي,B007"}, {ar:أين ترمي أي جهة تنوي, tr:eyne termî, ey cihetin tenvî, gloss:"nereye atıyorsun", yani hangi yöne niyetlisin, source:"ر م ي,B007"}. Yolculuğun yönünü söyleyen kök, sûrede kuşların onları "atmasında" geri döner.

İkinci kılma ise insanların kendisini nesne alır: {ar:فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ, tr:fe-cealehum ke-asfin me'kûl, gloss:onları yenmiş ekin yaprağı gibi kıldı, source:105:5}. İlk kılma onların yaptığı şeyi, ikincisi onları kendilerini dönüştürür. Onların "keyd"i, yani bir şeye güçle uğraşmaları, sûrenin sonunda Onun yapışının nesnesi olarak kalır.

Kur'an bu ilişkiyi defalarca kurar. Mü'min sûresinde Firavun'un meclisi, Musa'ya inananların oğullarını öldürmeyi emreder ve ayet şu hükümle kapanır: {ar:وَمَا كَيْدُ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍۢ, tr:ve mâ keydu'l-kâfirîne illâ fî dalâl, gloss:kâfirlerin düzeni boşa gitmekten başka bir şey değildir, source:40:25}; keyd ve dalâl bu sûredeki gibi tek cümlede durur. Aynı sûrede Firavun göğün yollarına çıkmak ister ve hüküm aynı kalıpla verilir: {ar:وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ, tr:ve mâ keydu fir'avne illâ fî tebâb, gloss:Firavun'un düzeni yıkımdan başka bir şeye varmaz, source:40:37}. Yusuf sûresinde Yusuf, kendisine kurulan tuzağın ortaya çıkışından sonra şöyle der: {ar:وَأَنَّ ٱللَّهَ لَا يَهْدِى كَيْدَ ٱلْخَآئِنِينَ, tr:ve ennallâhe lâ yehdî keyde'l-hâ'inîn, gloss:Allah hainlerin düzenini hedefine ulaştırmaz, source:12:52}; burada keyd'in yolunu bulmaması, "doğru yola iletmek" fiiliyle söylenir, sûrenin tadlîl'inin tam karşılığıdır. Daha önce de Rab onu kurulan tuzaktan çevirmişti: {ar:فَٱسْتَجَابَ لَهُۥ رَبُّهُۥ فَصَرَفَ عَنْهُ كَيْدَهُنَّ, tr:festecâbe lehû rabbuhû fe-sarafe anhu keydehunn, gloss:Rabbi duasını kabul etti ve onların tuzağını ondan çevirdi, source:12:34}. İbrahim'i yakmak isteyen kavim için Kur'an keyd'e karşı bir "kılma" koyar: {ar:وَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَخْسَرِينَ, tr:ve erâdû bihî keyden fe-cealnâhumu'l-ahserîn, gloss:ona bir tuzak kurmak istediler, biz de onları en çok kaybedenler kıldık, source:21:70}, ve Sâffât sûresinde {ar:فَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَسْفَلِينَ, tr:fe-erâdû bihî keyden fe-cealnâhumu'l-esfelîn, gloss:ona tuzak kurmak istediler, biz de onları en alçaklar kıldık, source:37:98}. Enfâl sûresi bunu bir ilahi sıfata bağlar: {ar:وَأَنَّ ٱللَّهَ مُوهِنُ كَيْدِ ٱلْكَٰفِرِينَ, tr:ve ennallâhe mûhinu keydi'l-kâfirîn, gloss:Allah kâfirlerin düzenini zayıflatandır, source:8:18}. Tûr sûresi keyd kuranları keyd'in nesnesi yapar: {ar:أَمْ يُرِيدُونَ كَيْدًۭا ۖ فَٱلَّذِينَ كَفَرُوا۟ هُمُ ٱلْمَكِيدُونَ, tr:em yurîdûne keydâ, fellezîne keferû humu'l-mekîdûn, gloss:yoksa bir tuzak mı kurmak istiyorlar? Asıl tuzağa düşürülenler inkâr edenlerdir, source:52:42}; birkaç ayet sonra {ar:يَوْمَ لَا يُغْنِى عَنْهُمْ كَيْدُهُمْ شَيْـًۭٔا, tr:yevme lâ yugnî anhum keyduhum şey'â, gloss:tuzaklarının kendilerine hiçbir yarar sağlamayacağı gün, source:52:46} gelir. Târık sûresinde iki keyd yüz yüze konur: {ar:إِنَّهُمْ يَكِيدُونَ كَيْدًۭا, tr:innehum yekîdûne keydâ, gloss:onlar bir tuzak kuruyorlar, source:86:15}, {ar:وَأَكِيدُ كَيْدًۭا, tr:ve ekîdu keydâ, gloss:ben de bir düzen kuruyorum, source:86:16}; A'râf sûresinde Allah {ar:إِنَّ كَيْدِى مَتِينٌ, tr:inne keydî metîn, gloss:benim düzenim sağlamdır, source:7:183} der. Yapma fiilinin Allah'a ait olduğu da açıkça söylenir: {ar:فَعَّالٌۭ لِّمَا يُرِيدُ, tr:fe''âlun limâ yurîd, gloss:dilediğini yapandır, source:85:16}. İbrahim sûresi ise sapmayı ve rüzgârı bir benzetmede birleştirir: {ar:أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ, tr:a'mâluhum ke-ramâdin işteddet bihi'r-rîhu fî yevmin âsıf, gloss:yaptıkları, fırtınalı bir günde rüzgârın savurduğu kül gibidir, source:14:18}, ve aynı ayet {ar:ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ, tr:zâlike huve'd-dalâlu'l-baîd, gloss:işte uzak sapkınlık budur, source:14:18} diye biter. Secde sûresinde inkârcılar dalâl kökünü yerin içinde kaybolmak anlamında kullanır: {ar:أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ, tr:e-izâ dalelnâ fi'l-ard, gloss:biz yerin içinde kaybolup gittiğimizde mi, source:32:10}.

Kaynaklar: 105:1 فَعَلَ ف ع ل B001; 105:2 يَجْعَلْ ج ع ل B002; 105:5 فَجَعَلَهُمْ ج ع ل B001; 105:5 فَجَعَلَهُمْ ج ع ل B002; 105:2 كَيْدَهُمْ ك ي د B001; 105:2 كَيْدَهُمْ ك ي د B002; 105:2 تَضْلِيلٍ ض ل ل B001; 105:2 تَضْلِيلٍ ض ل ل B003; 105:2 تَضْلِيلٍ ض ل ل B002; 105:4 تَرْمِيهِم ر م ي B007

## Hiç karşılaşılmayan savaş

Sûrenin üç kökü Arapçada savaşı da adlandırır ve üçü de savaşın gerçekleşmediği bir sahneyi kurar. {ar:كَيْدَهُمْ, tr:keydehum, gloss:onların düzeni, source:105:2} kökü kalıplaşmış bir ifadede savaşın kendisidir ve bu ifadenin örneği tam olarak karşılaşılmayan bir savaştır: {ar:الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا, tr:el-keydu'l-harb, yukâlu harecû ve lem yelkav keyden, ey harbâ, gloss:keyd savaştır; "çıktılar ve keyd ile karşılaşmadılar", yani savaş görmediler denir, source:"ك ي د,B004"}, {ar:ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا, tr:rubbemâ summiye'l-harbu keydâ, yukâlu gazâ fulânun fe-lem yelka keydâ, gloss:savaşa bazen keyd denir; "falan sefere çıktı ama keyd görmedi" denir, source:"ك ي د,B004"}. Sûrede filin sahiplerinin karşısına hiçbir insan çıkmaz: ayetlerde iş görenler yalnızca Rab, kuşlar ve taşlardır. Savaşa gelen bir topluluk savaşacak kimse bulamaz.

{ar:سِجِّيلٍ, tr:siccîl, gloss:siccîl, source:105:4} kökü, sırayla dökülen kova üzerinden savaşın dönüşümlü talihini anlatır: {ar:الحرب سجال أي مرة منها سجل على هؤلاء ومرة على هؤلاء, tr:el-harbu sicâl, ey merraten minhâ seclun alâ hâ'ulâ'i ve merraten alâ hâ'ulâ', gloss:savaş "sicâl"dir, yani bir kova bunların üzerine, bir kova ötekilerin üzerine, source:"س ج ل,B002"}; bu yarışmanın kökü su çekmeye dayanır: {ar:تساجل الرجلان إذا تفاخرا وأصله من تساجلهما في الاستقاء, tr:tesâcele'r-raculân izâ tefâharâ, ve asluhû min tesâculihimâ fi'l-istikâ', gloss:iki adam övünme yarışına girince "tesâcele" denir; aslı su çekmede kova yarıştırmalarıdır, source:"س ج ل,B002"}. Sûrede ise taşlar {ar:عَلَيْهِمْ, tr:aleyhim, gloss:üzerlerine, source:105:3} gönderilir; kova yalnızca bir tarafa dökülür ve sıra hiçbir zaman öbür tarafa geçmez. Son ayetin {ar:كَعَصْفٍ, tr:ke-asf, gloss:ekin yaprağı gibi, source:105:5} kökü ise bir kavmi silip götüren savaşı adlandırır: {ar:الحرب تعصف بالقوم أي تذهب بهم وتهلكهم وأعصف الرجل أي هلك, tr:el-harbu ta'sifu bi'l-kavm, ey tezhebu bihim ve tuhlikuhum, ve a'safe'r-racul, ey helek, gloss:savaş kavmi "asf" eder, yani alıp götürür ve helak eder; "a'safe'r-racul" adam helak oldu demektir, source:"ع ص ف,B004"}. Onları alıp götüren "savaş" insanlarca yapılmamıştır. Düzen kelimesinin kökü kalıplaşmış bir ifadede can vermeyi de anlatır: {ar:هو يكيد بنفسه أي يجود بها, tr:huve yekîdu bi-nefsih, ey yecûdu bihâ, gloss:"canıyla keyd ediyor", yani can çekişiyor, source:"ك ي د,B003"}. Kurdukları düzenin adı, sonlarının adıyla aynı köktedir.

Kur'an insan eli değmeden kesilen savaşı başka sahnelerde de anlatır. Ahzâb sûresinde Allah mü'minlere, üzerlerine ordular geldiği gün {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا, tr:fe-erselnâ aleyhim rîhan ve cunûden lem teravhâ, gloss:üzerlerine bir rüzgâr ve görmediğiniz ordular gönderdik, source:33:9} der; aynı anlatı {ar:وَكَفَى ٱللَّهُ ٱلْمُؤْمِنِينَ ٱلْقِتَالَ, tr:ve kefallâhu'l-mu'minîne'l-kıtâl, gloss:Allah mü'minleri savaşmaktan kurtardı, source:33:25} diye kapanır; aynı ayet gelenlerin {ar:لَمْ يَنَالُوا۟ خَيْرًۭا, tr:lem yenâlû hayrâ, gloss:hiçbir hayra erişemediler, source:33:25} geri döndüğünü söyler. Fetih sûresinde Allah, Mekke'nin göbeğinde iki tarafın ellerini birbirinden çektiğini hatırlatır: {ar:وَهُوَ ٱلَّذِى كَفَّ أَيْدِيَهُمْ عَنكُمْ وَأَيْدِيَكُمْ عَنْهُم بِبَطْنِ مَكَّةَ, tr:ve huve'llezî keffe eydiyehum anküm ve eydiyeküm anhum bi-batni mekke, gloss:Mekke'nin göbeğinde onların ellerini sizden, sizin ellerinizi onlardan çeken Odur, source:48:24}. Enfâl sûresinde, iki topluluğun karşılaştığı gün hakkında, öldürme ve atma Allah'a verilir: {ar:فَلَمْ تَقْتُلُوهُمْ وَلَٰكِنَّ ٱللَّهَ قَتَلَهُمْ, tr:fe-lem taktulûhum ve lâkinnallâhe katelehum, gloss:onları siz öldürmediniz, Allah öldürdü, source:8:17}. Âl-i İmrân sûresinde ise bir yaralanmanın ardından mü'minlere savaşın dönüşümlü talihi hatırlatılır: {ar:وَتِلْكَ ٱلْأَيَّامُ نُدَاوِلُهَا بَيْنَ ٱلنَّاسِ, tr:ve tilke'l-eyyâmu nudâviluhâ beyne'n-nâs, gloss:o günleri insanlar arasında döndürür dururuz, source:3:140}. Fil sûresinde bu dönüşüm yoktur: tek bir kova, tek bir tarafa dökülür. Kamer sûresinde verilen söz de bunu anlatır: {ar:سَيُهْزَمُ ٱلْجَمْعُ وَيُوَلُّونَ ٱلدُّبُرَ, tr:seyuhzemu'l-cem'u ve yuvellûne'd-dubur, gloss:o topluluk bozguna uğrayacak ve arkalarını dönüp kaçacaklar, source:54:45}.

Kaynaklar: 105:2 كَيْدَهُمْ ك ي د B004; 105:2 كَيْدَهُمْ ك ي د B003; 105:4 سِجِّيلٍ س ج ل B002; 105:5 كَعَصْفٍ ع ص ف B004

## Av ve avcı: ağırın hafif tarafından vurulması

Dördüncü ayetin fiili bir atıştır: {ar:تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ, tr:termîhim bi-hicâratin min siccîl, gloss:onlara siccîlden taşlar atıyorlardı, source:105:4}. Fiil dişil kurulmuştur ve öznesi kuşlardır; kuşlar atandır, onlar atılandır. Atmanın kökü nesnelerini kendisi sayar: ok ve taş. {ar:الرمي يقال في الأعيان كالسهم والحجر, tr:er-ramyu yukâlu fi'l-a'yân ke's-sehmi ve'l-hacer, gloss:atmak, ok ve taş gibi somut şeyler için söylenir, source:"ر م ي,B001"}. Kök ava çıkmayı da anlatır: {ar:خرجت أرتمي إذا رميت القنص, tr:haractu ertemî izâ rameytu'l-kanas, gloss:av vurmaya çıktığımda "atmaya çıktım" derim, source:"ر م ي,B001"}, ve atılan her şey bir avdır: {ar:الرمية الصيد الذي يرمى, tr:er-ramiyyetu's-saydu'llezî yurmâ, gloss:"ramiyye", vurulan avdır, source:"ر م ي,B003"}; okun yuvarlak ucuna da bu kökten ad verilir: {ar:المرماة نصل السهم المدور, tr:el-mirmâtu naslu's-sehmi'l-mudevver, gloss:"mirmât", okun yuvarlak temreni, source:"ر م ي,B003"}. Fiile bağlanan "onları" zamiri, filin sahiplerini bu "ramiyye"nin, yani vurulan avın yerine koyar. Göndermenin kökü bile kısa bir oku adlandırır: {ar:المرسال سهم قصير, tr:el-mirsâlu sehmun kasîr, gloss:"mirsâl", kısa bir oktur, source:"ر س ل,B011"}. Taşlar da sert birer mermidir: {ar:الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, ve cem'uhû ahcâr ve hicâra, gloss:taş bilinen sert maddedir, çoğulu ahcâr ve hicâra, source:"ح ج ر,B003"}.

Bu avın tuhaflığı rollerin yer değiştirmesidir. Kuşlar normalde avlanandır; burada avcıdırlar. Hayvanların en irisi ve onun sahipleri ise vurulan avdır. Avın sonu son ayettedir: {ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kökü, bir yırtıcının yediği avı da adlandırır: {ar:أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته, tr:ekîlu'z-zi'bi'ş-şâtu ve gayruhâ; ekîletu'l-esedi ferîsetuh, gloss:kurdun "ekîl"i yediği koyun ve benzeridir; aslanın "ekîle"si avıdır, source:"ء ك ل,B007"}. Sahne şöyle akar: avcılar salınır, taşlar ok gibi atılır, ordu vurulan av olur ve yenmiş av olarak kalır. Kur'an yırtıcının yediği hayvanı haram kılınanlar arasında sayar, {ar:وَمَآ أَكَلَ ٱلسَّبُعُ, tr:ve mâ ekele's-sebu', gloss:ve yırtıcı hayvanın yediği, source:5:3}; Yusuf'un kardeşleri de babalarına onu kurdun yediğini söyler, {ar:فَأَكَلَهُ ٱلذِّئْبُ, tr:fe-ekelehu'z-zi'b, gloss:onu kurt yedi, source:12:17}. Bu sahnede "yenmiş" olan, bir avın sonudur.

Avın içinde ağır ile hafifin yer değiştirmesi de vardır. Fil en iri hayvandır, {ar:الفيل معروف, tr:el-fîlu ma'rûf, gloss:fil bilinir, source:"ف ي ل,B004"}; ama kökünün temel anlamı gevşeklik ve zayıflıktır: {ar:أصل يدل على استرخاء وضعف, tr:aslun yedullu ale'stirhâ'in ve da'f, gloss:gevşeklik ve zayıflık gösteren bir köktür, source:"ف ي ل,B001"}. En güçlü hayvanın adının altında güçsüzlük yatar. Kuşlar hafif ve hızlıdır: {ar:لكل من خف قد طار وكل سرعة, tr:li-külli men haffe kad târ, ve küllu sur'a, gloss:hafifleyen her şeye "uçtu" denir, her hıza da, source:"ط ي ر,B001"}. Ama bu hafif sürülerin adı ağırlığı ve yenmeyi taşıyan bir köktendir: {ar:أبل الرجل إذا غلب وامتنع والأبلة الثقل, tr:ebile'r-racul izâ galebe ve'mtena', ve'l-ubletu's-sikal, gloss:adam galip gelip direnince "ebile" denir; "uble" ağırlıktır, source:"ء ب ل,B004"}. Taşlar serttir ve siccîl şiddetle açıklanır: {ar:وقالوا السجيل الشديد, tr:ve kâlû es-siccîlu'ş-şedîd, gloss:siccîl, şiddetli olandır dediler, source:"س ج ل,B005"}, {ar:تأويله كثيرة شديدة, tr:te'vîluhû kesîratun şedîde, gloss:anlamı: çok ve şiddetli, source:"س ج ل,B005"}. Son kelime {ar:كَعَصْفٍ, tr:ke-asf, gloss:ekin yaprağı gibi, source:105:5} ise hafiflik ve hızın kökündendir: {ar:أصل واحد صحيح يدل على خفة وسرعة, tr:aslun vâhidun sahîhun yedullu alâ hıffetin ve sur'a, gloss:hafiflik ve hız gösteren sağlam tek bir köktür, source:"ع ص ف,B003"}. Ağır olan hafif olanca vurulur; sert taşlar hafif kuşlardan iner ve en kütleli olan sonunda ağırlığı olmayan bir yaprağa döner.

Kur'an gücün korumadığı kavimleri anlatırken bu tersine dönüşü öne çıkarır. Mü'min sûresinde Allah önceki kavimler için {ar:كَانُوا۟ هُمْ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَأَخَذَهُمُ ٱللَّهُ بِذُنُوبِهِمْ, tr:kânû hum eşedde minhum kuvveten ve âsâran fi'l-ard, fe-ehazehumullâhu bi-zunûbihim, gloss:onlar bunlardan daha güçlü ve yeryüzünde daha çok iz bırakmışlardı, Allah onları günahları yüzünden yakaladı, source:40:21} der. Fussilet sûresinde Âd kavmi {ar:وَقَالُوا۟ مَنْ أَشَدُّ مِنَّا قُوَّةً, tr:ve kâlû men eşeddu minnâ kuvveh, gloss:"bizden daha güçlü kim var" dediler, source:41:15} ve cevap bir göndermedir: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا, tr:fe-erselnâ aleyhim rîhan sarsarâ, gloss:üzerlerine dondurucu, uğultulu bir rüzgâr gönderdik, source:41:16}. Atmanın gerçek sahibi de Enfâl sûresinde açıkça söylenir; Allah elçisine {ar:وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَٰكِنَّ ٱللَّهَ رَمَىٰ, tr:ve mâ rameyte iz rameyte ve lâkinnallâhe ramâ, gloss:attığın zaman sen atmadın, Allah attı, source:8:17} der. Orada görünen atıcı bir insandır, burada kuşlardır; atışın sahibi iki yerde de Odur.

Kaynaklar: 105:4 تَرْمِيهِم ر م ي B001; 105:4 تَرْمِيهِم ر م ي B003; 105:3 وَأَرْسَلَ ر س ل B011; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:5 مَّأْكُولٍۭ ء ك ل B007; 105:1 ٱلْفِيلِ ف ي ل B004; 105:1 ٱلْفِيلِ ف ي ل B001; 105:3 طَيْرًا ط ي ر B001; 105:3 أَبَابِيلَ ء ب ل B004; 105:4 سِجِّيلٍ س ج ل B005; 105:5 كَعَصْفٍ ع ص ف B003

## Fırtına: salınan rüzgâr, ağır damlalı bulut, boşalan kova

Üçüncü, dördüncü ve beşinci ayetlerin kökleri bir fırtınanın bütün evrelerini taşır. Göndermenin kökü rüzgârların gönderilişini de adlandırır: {ar:أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة, tr:erseltu fulânen fî risâle, ve'l-murselâtu'r-riyâh, ve yukâlu'l-melâ'ike, gloss:falancayı bir haberle gönderdim; "murselât" rüzgârlardır, meleklerdir de denir, source:"ر س ل,B001"}. Atmanın kökü iri ve sert damlalı büyük bulutu adlandırır: {ar:الرمى السقى وهي السحابة العظيمة القطر الشديدة الوقع, tr:er-ramiyyu's-sakiyy, ve hiye's-sehâbetu'l-azîmetu'l-katri'ş-şedîdetu'l-vak', gloss:"ramiyy", iri damlalı, sert düşen büyük buluttur, source:"ر م ي,B004"}, {ar:ترمى بقطع من السحاب, tr:turmâ bi-kıtain mine's-sehâb, gloss:bulut parçalarıyla atılır, source:"ر م ي,B004"}. Siccîl'in kökünün temeli ise dolduktan sonra boşalmaktır: {ar:أصل واحد يدل على انصباب شيء بعد امتلائه, tr:aslun vâhidun yedullu ale'nsibâbi şey'in ba'de'mtilâ'ih, gloss:bir şeyin dolduktan sonra dökülmesini gösteren tek bir köktür, source:"س ج ل,B001"}, {ar:سجلت الماء فانسجل أي صببته فانصب, tr:seceltu'l-mâ'e fe'nsecel, ey sabebtuhû fe'nsabb, gloss:suyu döktüm, o da döküldü, source:"س ج ل,B001"}, {ar:السجل الدلو ولا يكون سجلا حتى يكون فيه ماء, tr:es-seclu'd-delv, ve lâ yekûnu seclen hattâ yekûne fîhi mâ', gloss:"secl" kovadır; içinde su olmadıkça ona secl denmez, source:"س ج ل,B001"}. Siccîl kelimesi göndermeyle de açıklanır: {ar:سجيل من سجلته أي أرسلته, tr:siccîl, min secceltuh, ey erseltuh, gloss:siccîl, "onu salıverdim" anlamındaki fiildendir, source:"س ج ل,B005"}, ve kökün bir dalı sınırsızca saçılmayı anlatır: {ar:أسجلت الكلام أي أرسلته, tr:escelte'l-kelâm, ey erseltah, gloss:sözü salıverdin, source:"س ج ل,B003"}, {ar:الشيء المسجل وهو المبذول لكل أحد كأنه قد صب صبا, tr:eş-şey'u'l-musecel, ve huve'l-mebzûlu li-külli ehad, ke-ennehû kad subbe sabbâ, gloss:"musecel", herkese bolca verilen, sanki dökülmüş olandır, source:"س ج ل,B003"}. Damlaların yerine düşen ise taşlardır, {ar:الحجر الجوهر الصلب المعروف, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, gloss:taş bilinen sert maddedir, source:"ح ج ر,B003"}. Son ayetin kökü de kırıp döken rüzgârdır: {ar:عاصفة ومعصفة تكسر الشيء فتجعله كعصف, tr:âsıfa ve mu'sıfa, tekseru'ş-şey'e fe-tec'aluhû ke-asf, gloss:"âsıfa" ve "mu'sıfa" denen rüzgâr, şeyi kırıp ekin yaprağı gibi yapar, source:"ع ص ف,B002"}, {ar:والمعصفات الرياح التي تثير التراب والورق, tr:ve'l-mu'sıfâtu'r-riyâhu'lletî tusîru't-turâbe ve'l-varak, gloss:"mu'sıfât", toprağı ve yaprağı kaldıran rüzgârlardır, source:"ع ص ف,B002"}. Fırtına salıvermeyle (üçüncü ayet) başlar, bulutun ağır damlaları ve dolu kovanın boşalması gibi inen taşlarla (dördüncü ayet) sürer, kırılmış sapları geride bırakan rüzgârla (beşinci ayet) biter. "Rüzgâr şeyi kırıp asf gibi yapar" sözü, son ayetin "onları asf gibi kıldı" cümlesinin neredeyse aynısıdır.

Kur'an bu taş yağmurunu Lut kavminin kıssasında aynı kelimeyle anlatır: {ar:جَعَلْنَا عَٰلِيَهَا سَافِلَهَا وَأَمْطَرْنَا عَلَيْهَا حِجَارَةًۭ مِّن سِجِّيلٍۢ مَّنضُودٍۢ, tr:cealnâ âliyehâ sâfilehâ ve emtarnâ aleyhâ hicâraten min siccîlin mendûd, gloss:oranın üstünü altına getirdik ve üzerine siccîlden, üst üste dizilmiş taşlar yağdırdık, source:11:82}; Hicr sûresi aynı sahneyi tekrarlar, {ar:وَأَمْطَرْنَا عَلَيْهِمْ حِجَارَةًۭ مِّن سِجِّيلٍ, tr:ve emtarnâ aleyhim hicâraten min siccîl, gloss:üzerlerine siccîlden taşlar yağdırdık, source:15:74}. Zâriyât sûresinde İbrahim'e gelen elçiler kendilerinin {ar:قَالُوٓا۟ إِنَّآ أُرْسِلْنَآ إِلَىٰ قَوْمٍۢ مُّجْرِمِينَ, tr:kâlû innâ ursilnâ ilâ kavmin mucrimîn, gloss:"biz suçlu bir kavme gönderildik" dediler, source:51:32} olduğunu söyler ve görevlerini anlatır: {ar:لِنُرْسِلَ عَلَيْهِمْ حِجَارَةًۭ مِّن طِينٍۢ, tr:li-nursile aleyhim hicâraten min tîn, gloss:üzerlerine çamurdan taşlar göndermek için, source:51:33}. Bu sûrenin "üzerlerine gönderdi" kalıbı, taş ve Rab orada bir aradadır. Mekkeli inkârcılar aynı yağmuru kendileri ister: {ar:فَأَمْطِرْ عَلَيْنَا حِجَارَةًۭ مِّنَ ٱلسَّمَآءِ, tr:fe-emtir aleynâ hicâraten mine's-semâ', gloss:üzerimize gökten taş yağdır, source:8:32}. Mülk sûresi bu göndermeyi bir uyarıya çevirir: {ar:أَمْ أَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا, tr:em emintum men fi's-semâ'i en yursile aleykum hâsibâ, gloss:yoksa gökte olanın üzerinize taş yağdıran bir rüzgâr göndermeyeceğinden emin mi oldunuz, source:67:17}, ve İsrâ sûresi deniz yolcularına {ar:فَيُرْسِلَ عَلَيْكُمْ قَاصِفًۭا مِّنَ ٱلرِّيحِ, tr:fe-yursile aleykum kâsıfan mine'r-rîh, gloss:üzerinize kırıp geçiren bir rüzgâr göndermesinden, source:17:69} söz eder. Mürselât sûresinin ilk iki ayeti göndermenin ve fırtınanın köklerini ardışık koyar: {ar:وَٱلْمُرْسَلَٰتِ عُرْفًۭا, tr:ve'l-murselâti urfâ, gloss:art arda gönderilenlere andolsun, source:77:1}, {ar:فَٱلْعَٰصِفَٰتِ عَصْفًۭا, tr:fe'l-âsıfâti asfâ, gloss:sonra şiddetle esip savuranlara, source:77:2}. Gönderilenler fırtınaya dönüşür, tıpkı bu sûrede gönderilen kuşların sonunun "asf" olması gibi. Fecr sûresinde aynı "görmedin mi" kalıbının ardından dökme fiili gelir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbüke sevta azâb, gloss:Rabbin üzerlerine bir azap kamçısı döktü, source:89:13}; siccîl'in kökündeki dökülme burada açıkça söylenmiştir. Âd kavmi için {ar:إِذْ أَرْسَلْنَا عَلَيْهِمُ ٱلرِّيحَ ٱلْعَقِيمَ, tr:iz erselnâ aleyhimu'r-rîha'l-akîm, gloss:üzerlerine kısır rüzgârı gönderdiğimizde, source:51:41} denir ve rüzgâr {ar:مَا تَذَرُ مِن شَىْءٍ أَتَتْ عَلَيْهِ إِلَّا جَعَلَتْهُ كَٱلرَّمِيمِ, tr:mâ tezeru min şey'in etet aleyhi illâ cealethu ke'r-ramîm, gloss:uğradığı hiçbir şeyi bırakmaz, onu çürümüş kemik gibi yapardı, source:51:42}; "kıldı" fiili, "gibi" edatı ve bir kalıntı, bu sûrenin son ayetinin çerçevesidir. Bulutu yanlış okuyan Âd'a da rüzgâr gelir: {ar:رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:rîhun fîhâ azâbun elîm, gloss:içinde acı bir azap olan bir rüzgâr, source:46:24}. En'âm sûresi ise aynı göndermenin rahmet yüzünü gösterir: {ar:وَأَرْسَلْنَا ٱلسَّمَآءَ عَلَيْهِم مِّدْرَارًۭا, tr:ve erselnâ's-semâ'e aleyhim midrârâ, gloss:üzerlerine göğü bol bol yağmur yağdırır hâlde gönderdik, source:6:6}. Fil sûresinin gökten gelen yağmuru bunun tersidir: damla yerine taş düşer.

Kaynaklar: 105:3 وَأَرْسَلَ ر س ل B001; 105:4 تَرْمِيهِم ر م ي B004; 105:4 سِجِّيلٍ س ج ل B001; 105:4 سِجِّيلٍ س ج ل B005; 105:4 سِجِّيلٍ س ج ل B003; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:5 كَعَصْفٍ ع ص ف B002

## Ekin, saman ve yenmiş olan

Son ayet bir tarlada biter: {ar:فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ, tr:fe-cealehum ke-asfin me'kûl, gloss:onları yenmiş ekin yaprağı gibi kıldı, source:105:5}. {ar:عَصْفٍ, tr:asf, gloss:ekin yaprağı, kabuk, source:105:5}, tanenin üzerindeki kabuk ve sapın kuruyup ufalanan yapraklarıdır: {ar:العصف ما على الحب من قشور التبن, tr:el-asfu mâ ale'l-habbi min kuşûri't-tibn, gloss:asf, tanenin üzerindeki saman kabuklarıdır, source:"ع ص ف,B001"}, {ar:ما على ساق الزرع من الورق الذي يبس فتفتت, tr:mâ alâ sâkı'z-zer'i mine'l-varaki'llezî yebise fe-tefettet, gloss:ekinin sapı üzerinde kuruyup ufalanan yapraklar, source:"ع ص ف,B001"}, {ar:العصف والعصيفة الذي يعصف من الزرع وحطام النبت المتكسر, tr:el-asfu ve'l-asîfetu'llezî yu'safu mine'z-zer', ve hutâmu'n-nebti'l-mutekessir, gloss:asf ve asîfe, ekinden koparılan ve kırılmış bitki döküntüsüdür, source:"ع ص ف,B001"}. Kökün rüzgârı da bu döküntüyü üretir: {ar:عاصفة ومعصفة تكسر الشيء فتجعله كعصف وعصفت بهم الريح تشبيها بذلك, tr:âsıfa ve mu'sıfa tekseru'ş-şey'e fe-tec'aluhû ke-asf, ve asafet bihimu'r-rîhu teşbîhen bi-zâlik, gloss:âsıfa ve mu'sıfa şeyi kırıp asf gibi yapar; "rüzgâr onları asf etti" sözü buna benzetmedir, source:"ع ص ف,B004"}. {ar:فَجَعَلَهُمْ, tr:fe-cealehum, gloss:onları kıldı, source:105:5} bu hâle sokmaktır, {ar:جعل صير, tr:ceale: sayyera, gloss:"ceale", "dönüştürdü" demektir, source:"ج ع ل,B002"}. Sûrenin ilk fiili de buraya bağlanır: yapmanın kullanımdaki örneği kırmaktır, {ar:فعلت الشيء فانفعل كسرته فانكسر, tr:faaltu'ş-şey'e fe'nfeal, kesertuhû fe'nkeser, gloss:şeyi yaptım, o da yapıldı; kırdım, o da kırıldı, source:"ف ع ل,B001"}. Birinci ayette sorulan "yapış", beşinci ayette sonucu görünen bir kırmadır.

{ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} sahnenin son adımını verir. Kelime önce yenmiş olandır, {ar:الأكل تناول المطعم, tr:el-eklu tenâvulu'l-mat'am, gloss:yemek, yiyeceği almaktır, source:"ء ك ل,B001"}. Ekinin ürünü de bu kökten adlanır, {ar:أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر, tr:uklu'ş-şecerati semeruhâ; el-uklu semeru'n-nahli ve'ş-şecer, gloss:ağacın "ukl"ü meyvesidir; ukl, hurma ve ağaç meyvesidir, source:"ء ك ل,B002"}; ürün alındığında geriye kabuk kalır. Kök bir şeyin içten çürümesini, kurt yemesini de anlatır: {ar:والأكال أن يتأكل عود أو شيء؛ تأكل كذا فسد؛ في جسدي إكلة من الأكال, tr:ve'l-ukâlu en yete'ekkele ûdun ev şey'; te'ekkele kezâ: fesed; fî cesedî ikletun mine'l-ukâl, gloss:"ukâl", bir dalın ya da şeyin kurtlanıp yenmesidir; "te'ekkele" bozuldu demektir; "bedenimde yenik var", source:"ء ك ل,B006"}. Süreç şudur: yetişmiş bir ekin, ürünü alınmış, geriye kabuk ve kuru yaprak kalmış, rüzgârla kırılmış ve içten yenmiş. Bir ordu bu hâle getirilir. "Gibi" edatı bunun bir benzetme olduğunu açıkça söyler; ayet onları ekinin kendisi değil, ekinin artığı gibi gösterir.

Kur'an bu artığı bitkinin bir parçası olarak sayar: {ar:وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ, tr:ve'l-habbu zu'l-asfi ve'r-reyhân, gloss:kabuklu taneler ve güzel kokulu bitkiler, source:55:12}. Zümer sûresi bu sûrenin bütün yayını tek ayette taşır: aynı "görmedin mi" ile açılır, ekini çıkarır ve "kılma" ile kırıntıya çevirir: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ, tr:elem tera ennallâhe enzele mine's-semâ'i mâ', gloss:Allah'ın gökten su indirdiğini görmedin mi, source:39:21}, ve aynı ayette {ar:ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا, tr:summe yuhricu bihî zer'an muhtelifen elvânuh, summe yehîcu fe-terâhu musferran, summe yec'aluhû hutâmâ, gloss:sonra onunla renkleri çeşitli ekin çıkarır, sonra ekin kurur, onu sararmış görürsün, sonra onu kırıntı hâline getirir, source:39:21}. Vâkıa sûresinde Allah ekinciye {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا, tr:lev neşâ'u le-cealnâhu hutâmâ, gloss:dileseydik onu kırıntıya çevirirdik, source:56:65} der; A'lâ sûresinde {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-cealehû gusâ'en ahvâ, gloss:sonra onu kapkara bir çerçöp yaptı, source:87:5}; Kehf sûresinde dünya hayatı, {ar:فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:fe-asbaha heşîmen tezrûhu'r-riyâh, gloss:sonunda rüzgârların savurduğu kuru çöp oldu, source:18:45} diye biten bir benzetmedir. Yûnus sûresinde aynı benzetme bir "kılma" ile kapanır: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-cealnâhâ hasîden ke-en lem tagne bi'l-ems, gloss:onu sanki dün hiç yokmuş gibi biçilmiş kıldık, source:10:24}. Helak edilen kavimler için de aynı dil kullanılır: {ar:حَتَّىٰ جَعَلْنَٰهُمْ حَصِيدًا خَٰمِدِينَ, tr:hattâ cealnâhum hasîden hâmidîn, gloss:sonunda onları biçilmiş, sönmüş kıldık, source:21:15}, {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-cealnâhum gusâ', gloss:onları çerçöp kıldık, source:23:41}, Semûd için {ar:فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ, tr:fe-kânû ke-heşîmi'l-muhtazır, gloss:ağıl yapanın kuru çalı çırpısı gibi oldular, source:54:31}. Âl-i İmrân sûresindeki benzetmede rüzgâr ekini vurur: {ar:كَمَثَلِ رِيحٍۢ فِيهَا صِرٌّ أَصَابَتْ حَرْثَ قَوْمٍۢ ظَلَمُوٓا۟ أَنفُسَهُمْ فَأَهْلَكَتْهُ, tr:ke-meseli rîhin fîhâ sırrun esâbet harse kavmin zalemû enfusehum fe-ehleketh, gloss:kendilerine zulmeden bir kavmin ekinine çarpıp onu yok eden, içinde dondurucu soğuk bulunan bir rüzgâr gibi, source:3:117}. Enbiyâ sûresinde İbrahim putları kırar ve fiil bu sûrenin son ayetindeki biçimin aynısıdır: {ar:فَجَعَلَهُمْ جُذَٰذًا, tr:fe-cealehum cuzâzâ, gloss:onları paramparça etti, source:21:58}. Sebe' sûresinde ise "yemek" içten çürütmedir: Süleyman'ın ölümünü onlara {ar:إِلَّا دَآبَّةُ ٱلْأَرْضِ تَأْكُلُ مِنسَأَتَهُۥ, tr:illâ dâbbetu'l-ardi te'kulu minse'eteh, gloss:asasını yiyen bir yer kurdundan başkası göstermedi, source:34:14}. Hâkka sûresinin sorusu da bu sonu tamamlar: {ar:فَهَلْ تَرَىٰ لَهُم مِّنۢ بَاقِيَةٍۢ, tr:fe-hel terâ lehum min bâkiyeh, gloss:onlardan geriye kalan bir şey görüyor musun, source:69:8}.

Kaynaklar: 105:5 كَعَصْفٍ ع ص ف B001; 105:5 كَعَصْفٍ ع ص ف B004; 105:5 فَجَعَلَهُمْ ج ع ل B002; 105:1 فَعَلَ ف ع ل B001; 105:5 مَّأْكُولٍۭ ء ك ل B001; 105:5 مَّأْكُولٍۭ ء ك ل B002; 105:5 مَّأْكُولٍۭ ء ك ل B006

## Yakıt ve yiyen ateş

{ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kelimesinin kökü ateşin yemesini de söyler: {ar:أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ وعلى طريق التشبيه قيل أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab ve âkeltuhâ; i'tekeleti'n-nâru izâ işteedde'ltihâbuhâ; ve alâ tarîki't-teşbîh kîle ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi; alevi şiddetlenince ateş "kendini yedi"; benzetme yoluyla "ateş odunu yedi" denir, source:"ء ك ل,B005"}. {ar:عَصْفٍ, tr:asf, gloss:kuru ekin yaprağı, source:105:5}, kuruyup ufalanan yapraktır, {ar:ما على ساق الزرع من الورق الذي يبس فتفتت, tr:mâ alâ sâkı'z-zer'i mine'l-varaki'llezî yebise fe-tefettet, gloss:ekinin sapı üzerinde kuruyup ufalanan yapraklar, source:"ع ص ف,B001"}, yani ateşin ilk tuttuğu yakıt. Kuşların sıfatının kökü bir odun demetini adlandırır ve bir atasözünde bir yükün üstüne bir başka yük olarak geçer: {ar:الإبالة الحزمة من الحطب, tr:el-ibâletu'l-huzmetu mine'l-hatab, gloss:"ibâle", odun demetidir, source:"ء ب ل,B005"}, {ar:الإبالة الحزمة من الحطب وضغث على إبالة, tr:el-ibâletu'l-huzmetu mine'l-hatab, ve dıgsun alâ ibâleh, gloss:ibâle odun demetidir; "demetin üstüne bir tutam", source:"ء ب ل,B005"}. Düzenin kökü de kalıplaşmış bir ifadede ateşi geç veren çakmak ağacını anlatır: {ar:أن يخرج الزند النار ببطء وشدة, tr:en yuhrice'z-zendu'n-nâre bi-but'in ve şidde, gloss:çakmak ağacının ateşi yavaşça ve zorla çıkarması, source:"ك ي د,B006"}, {ar:كاد الزند إذا تباطأ بإخراج ناره, tr:kâde'z-zend izâ tebâta'e bi-ihrâci nârih, gloss:çakmak ağacı ateşini geç çıkarınca "kâde" denir, source:"ك ي د,B006"}. Siccîl de taş ve çamurun karışımı olarak açıklanır: {ar:السجيل حجر وطين مختلط وأصله فيما قيل فارسي معرب, tr:es-siccîlu hacerun ve tînun muhtalit, ve asluhû fîmâ kîle fârisiyyun mu'arrab, gloss:siccîl, karışık taş ve çamurdur; aslının, denildiğine göre, Arapçalaşmış Farsça olduğu söylenir, source:"س ج ل,B005"}, {ar:السجيل حجارة كالمدر وهو حجر وطين, tr:es-siccîlu hicâratun ke'l-meder, ve huve hacerun ve tîn, gloss:siccîl, kuru kesek gibi taşlardır; taş ve çamurdur, source:"س ج ل,B005"}. Kur'an da Lut kavmine yağan siccîl taşlarını bir başka yerde {ar:حِجَارَةًۭ مِّن طِينٍۢ, tr:hicâraten min tîn, gloss:çamurdan taşlar, source:51:33} diye anar.

Bu aile imgeleri bir tersine dönüş kurar. Onların keyd'i, yani emekle uğraşmaları, ateşi geç veren bir çakmak gibidir: güçle vurulur ama tutuşmaz. Sonunda yenilen ise kendileridir, ateşin kuru samanı yiyişi gibi. Bu bir aile imgesidir; ayet ateşten söz etmez, yalnızca "yenmiş" der. Kur'an ise ateşin yemesini açıkça kullanır: Âl-i İmrân sûresinde bazıları peygambere inanmak için {ar:حَتَّىٰ يَأْتِيَنَا بِقُرْبَانٍۢ تَأْكُلُهُ ٱلنَّارُ, tr:hattâ ye'tiyenâ bi-kurbânin te'kuluhu'n-nâr, gloss:bize ateşin yiyeceği bir kurban getirinceye kadar, source:3:183} şartını koyduklarını söyler. Bakara sûresinde Kur'an'a denk bir sûre getirmeye çağrılan inkârcılara, iki kez tekrarlanan "yapmak" fiilinin ardından, taşların ateşin yakıtı olduğu söylenir: {ar:فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe-in lem tef'alû ve len tef'alû fetteku'n-nâre'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yapamazsanız, ki asla yapamayacaksınız, yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}; Tahrîm sûresinde mü'minlere aynı uyarı gelir: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:kû enfuseküm ve ehlîküm nâran vekûduhe'n-nâsu ve'l-hicâra, gloss:kendinizi ve ailenizi yakıtı insanlar ve taşlar olan ateşten koruyun, source:66:6}. Bakara sûresindeki bir benzetme de rüzgârı ve ateşi bir bahçenin üzerinde birleştirir: {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fehterakat, gloss:içinde ateş bulunan bir kasırga ona çarptı ve bahçe yandı, source:2:266}. Kasırga kelimesi "asf" ile aynı kökten değildir; ama rüzgârın ve ateşin bir ekini yok edişi, bu sûrenin son ayetindeki iki aile imgesinin bir arada sahnelenişidir.

Kaynaklar: 105:5 مَّأْكُولٍۭ ء ك ل B005; 105:5 كَعَصْفٍ ع ص ف B001; 105:3 أَبَابِيلَ ء ب ل B005; 105:2 كَيْدَهُمْ ك ي د B006; 105:4 سِجِّيلٍ س ج ل B005

## Buluşmalar

Sûrenin hareketi, açılıştaki görme çağrısı ile sondaki kırılmış ekin arasında kurulur ve imgeler bu yolda birbirine geçer. Görmenin imgesi ile düzenin imgesi aynı kökte buluşur: yolunu kaybetmeyi anlatan kök, bir işte doğruyu bulamamayı da anlatır. İkinci ayetteki düzen, hem bir yolda saptırılan bir yürüyüş hem de sağlıklı görmeyen bir aklın yanılmasıdır; okura "gör" denirken karşı tarafın düzeni "yolunu bulamaz". Fecr sûresinin "hicr sahibi" ile "Rabbinin ne yaptığını görmedin mi" sorusunu yan yana koyması, bu karşılaşmanın sahnesidir: akıl anlamındaki "hicr" ile taşın kökü aynıdır ve aklı olmayanlara taş iner.

Salınan sürüler, av ve fırtına tek bir sahnede durur. Göndermenin kökü hem otlağa salınan sürüleri hem gönderilen rüzgârları hem kısa bir oku adlandırır; üçüncü ayetin tek fiili, kuşların bölük bölük gelişini, rüzgârın esişini ve okun atılışını birlikte taşır. Atmanın kökü de iki yüzlüdür: ok ve taşla ava atmak ve iri damlalı bulutun yağması. Dördüncü ayetteki kuşlar, bir avcı gibi atar ve bir bulut gibi yağdırır. Mürselât sûresinin "gönderilenler" ile "şiddetle esenler"i ardışık koyması, göndermenin fırtınaya dönüşümünü sahneler; bu sûrede de gönderilen kuşlarla başlayan iş "asf" kelimesiyle biter.

Fırtına ile yazılmış taşlar siccîl kelimesinde buluşur. Kelime hem "salıverdiğim" hem "onlar için yazılmış olan" diye açıklanır: taşlar hem bir buluttan boşalan kovanın dökülüşü gibi iner hem de kimin için olduklarını taşır. Hûd ve Zâriyât sûrelerinin taş yağmuru, bu iki yüzü bir arada gösterir: yağdırılan siccîl taşları "Rabbinin katında işaretlenmiş"tir.

Savaş ile fırtına da siccîl'in kökünde birleşir: savaşın dönüşümlü talihi, su çekerken sırayla dökülen kovadan gelir. Fil sûresinde kova yalnızca bir tarafa, onların üzerine dökülür; fırtınanın boşalan kovası, savaşın sıra beklemeyen kovasıdır. Savaş ile ekin de "asf"ın kökünde buluşur: savaş bir kavmi silip götürür, rüzgâr şeyi kırıp asf gibi yapar ve rüzgârın insanları silip götürmesi bu kırılmaya benzetilerek söylenir.

Av ile ekin "yenmiş" kelimesinde iki ayrı sona ayrılır: yırtıcının yediği av ve ürünü alınıp içi yenmiş ekin. Ekin ile ateş de kuru yaprakta buluşur: kuruyup ufalanan yaprak, ateşin ilk yediği şeydir. Ağır ile hafifin yer değiştirmesi bu sahnelerin hepsinden geçer: en iri hayvan, en hafif kanatlıların avıdır ve sonunda en hafif şeye, ağırlığı olmayan bir yaprağa döner.

Bütün bu imgeleri birinci ve beşinci ayetler arasındaki fiiller bağlar. Rabbin "yapışı", kullanımdaki örneğiyle bir kırmadır; ilk "kılma" onların düzenini sapmaya, ikinci "kılma" onların kendilerini kırılmış ekine çevirir. Zümer sûresi bu yayı tek bir ayette gösterir: "görmedin mi" ile açılır, bir ekin çıkarır, sararmasını gösterir ve "onu kırıntı kılar". Fil sûresi aynı yayı bir topluluğun üzerine kurar: okur görmeye çağrılır, onların emeği yoldan çıkarılır, gökten bölük bölük salınan avcılar yazılmış taşlarını yağdırır ve sonunda geriye, ürünü yenmiş bir ekinin rüzgârla kırılmış yaprağı kalır.

