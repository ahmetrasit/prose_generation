Focus: 88:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_6/D.r13/context.md =====
# 88:6 — focus

لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ

Anchor translation (canonical reading, reference only):

Onlar için dikenli bir bitkiden başka yiyecek yoktur.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَّيْسَ | لَّيْسَ | ل ي س | V |
| 2 | لَهُمْ |  |  | P;PRON |
| 3 | طَعَامٌ | طَعَام | ط ع م | N |
| 4 | إِلَّا | إِلَّا |  | EXP |
| 5 | مِن | مِن |  | P |
| 6 | ضَرِيعٍ | ضَرِيع | ض ر ع | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 ◀ focus لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ل ي س (root_001390) — identity root of لَّيْسَ (w1)

- **B001** özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi — özneyi yalın, yüklem öğesini belirtme durumunda kullanarak olumsuzluk bildiren geçmiş biçimli eylem · bulunduğu ya da bulunmadığı yerden
  ليس كلمة جحود ... معناه لا أيس (ayn;tahdhib)؛ ليس: كلمة نفي، وهو فعل ماض (sihah)؛ تكون بمنزلة كان، ترفع الاسم وتنصب الخبر (tahdhib)
- **B002** ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı — ardından gelen adı belirtme durumunda kullanarak dışarıda bırakan istisna yapısı · senin dışında
  وقد يستثنى بها، تقول: جاءني القوم ليس زيدا (sihah)؛ يكون استثناء، ينصب به ... بمعنى ما عدا زيدا ... بمعنى إلا زيدا (tahdhib)
- **B003** bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı — bağlanan öğeyi olumsuzlayan ya da bir türün bütünüyle bulunmadığını bildiren söz
  ربما جاءت ليس بمعنى لا التي ينسق بها؛ وربما جاءت ليس بمعنى لا التبرئة (tahdhib)
- **B004** savaşta korkmayan ve rakibini bırakmayan yiğit — savaş karşısında yılmayan yiğitlik · savaştan korkmayan ve rakibini bırakmayan yiğit · övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz
  الأليس وهو الشجاع الذي لا يروعه الحرب (ayn;tahdhib)؛ ورجل أليس، أي شجاع بين الليس (sihah)؛ الأليس الذي لا يبارح قرنه؛ يقال للرجل الشجاع: أهيس أليس (tahdhib)
- **B005** yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan — yerinden ya da evinden ayrılmayan ağır kimse · övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz · su başında kalıp oradan ayrılmayan develer
  الأليس الرجل الثقيل الذي لا يبرح مكانه (ayn)؛ الأليس: الذي لا يبرح بيته؛ إبل ليس على الحوض: إذا أقامت عليه فلم تبرحه؛ وبالأليس الذي لا يبرح بيته، وهذا ذم (tahdhib)
- **B006** yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme — üzerine yüklenen her yükü taşıyan deve · güçlüğe katlanan ve yumuşak huylu olmak · görmezden gelip üzerinde durmamak · yumuşak huylu
  الأليس: البعير يحمل كل ما حمل (sihah)؛ تلايس الرجل: إذا كان حمولا حسن الخلق؛ وتلايست عن كذا وكذا: أي غمضت عنه؛ وفلان أليس دهثم: أي حسن الخلق (tahdhib)
- **B007** görüşü ve yargısı zayıf kişi — görüşü zayıf kimse
  الأليس الضعيف الرأي (ayn)
- **B008** ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi — ailesine karşı koruyucu kıskançlık göstermediği için alay edilen erkek · ailesine karşı koruyucu kıskançlık göstermeyen erkeği alaya alan yergi sözü
  الأليس: الديوثي الذي لا يغار ويتهزأ به؛ فيقال: هو أليس بورك فيه؛ فالليس يدخل في المعنيين: في المدح والذم (tahdhib)

## ط ع م (root_000934) — identity root of طَعَامٌ (w3)

- **B001** tatma, yeme ve yenilen besin — tat, lezzet · yemek veya tadına bakmak · yiyecek, besin · özellikle buğday · tadına bakma ve iştahını yoklama · doyuran ve besleyen yiyecek ya da su · yeme isteği veya iştah çekici şey · çok yiyen, obur
  أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)
- **B002** başkasını beslemek veya beslenmeyi istemek — yiyecek vermek, doyurmak · kendisini doyurmasını istemek
  الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)
- **B003** söz istemek veya takılan imama söz vermek [kalıp] — benden konuşmamı istedi · imam okuyuşta takılırsa sözü hatırlatın
  استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)
- **B004** geçim, bol ikram ve tahsis edilmiş gelir — geçimi yerinde · rızkı açık, kazançlı · çok ikram eden · geçim veya kazanç kaynağı · kazancı temiz veya kötü · araziyi birine geçim payı olarak ayırdı
  رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)
- **B005** olgunlaşıp tat kazanmak [kalıp] — ağacın meyvesi olgunlaşıp tat kazandı · tulumda hoş tat kazanmış süt
  للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)
- **B006** avı kazandıran araç, uzuv veya kişi — av getiren yay · avcı kuşun öndeki kalın parmağı · avdan yana talihli, avı bol
  قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)
- **B007** ilikte yağı beliren, biraz semiz hayvan — iliğinde yağ bulunan deve · biraz semiz, orta yağlı
  المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)
- **B008** akıl, değer ve düzelmeye açıklık niteliği [kalıp] — akıllı ve sağlam yargılı · aklı, devinimi veya değeri yok · terbiye kabul etmez, uslanmaz
  ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)
- **B009** atın ağız bölümü ve koşma talebi — atın burun altı ve dudak çevresi · attan koşmasını istedi
  مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)
- **B010** eklenen şeyin tutması [kalıp] — dala aşı yaptı ve aşı tuttu · gözüne küçük bir yabancı cisim girdi
  أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)
- **B011** gücü yetmek [kalıp] — ona gücü yetti
  الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)
- **B012** boğazından yakalayıp sıkmak [kalıp] — boğazından yakalayıp sıktı
  أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)
- **B013** ağız ağıza temas etmek — ağız ağıza temas etme
  التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)
- **B014** oluşumu ardışık olmak [kalıp] — oluşumu birbirini izleyen bölümlerden kurulu
  متطاعم الخلق أي متتابع الخلق (tahdhib)

## ض ر ع (root_000908) — identity root of ضَرِيعٍ (w6)

- **B001** hayvan memesi ve buna bağlı sütlenme özellikleri — toynaklı süt hayvanının memesi · doğum yaklaşınca memeye süt inmesi · iri memeli koyun
  ضرع الشاة وغيرها سمي بذلك لما فيه من لين (maqayis); الضرع لكل ذات خف أو ظلف (sihah); الضرع ضرع الشاة والناقة (tahdhib); أضرعت الشاة نزل لبنها قبيل النتاج (sihah;mufradat); شاة ضريع وضريعة عظيمة الضرع (maqayis;sihah;mufradat;tahdhib)
- **B002** boyun eğme, ihtiyacını gösterip yakarma ve boyun eğdirme — alçalıp boyun eğmek ve ihtiyacını göstermek · alçaltıp boyun eğdirmek · Tanrı'ya boyun eğerek yakarmak · birine boyun eğerek ondan istemek
  ضرع الرجل ضراعة إذا ذل (maqayis;sihah;mufradat); أضرعته أي ذللته (ayn;sihah); تضرع إلى الله أي ابتهل (sihah); مظهرين الضراعة وهي شدة الفقر إلى الشيء والحاجة إليه (tahdhib); تخشعوا وتذللوا وخضعوا (tahdhib); ضرع له إذا تخشع له وسأله (tahdhib)
- **B003** güçsüz, cılız ya da korkak olma — güçsüz, deneyimsiz ya da korkak adam · bedeni cılız ve güçsüz · güçsüz kimse için kullanılan bir biçim
  رجل ضرع ضعيف (maqayis;ayn;tahdhib); الضرع أيضا النحيف الدقيق (ayn); لضارع الجسم أي نحيف ضعيف (sihah); الضارع الضاوي النحيف (tahdhib); الضرع الرجل الجبان (tahdhib); الضرع الجمل الضعيف (tahdhib); ضعف وذل فهو ضارع وضرع (mufradat)
- **B004** benzerlik ve buna dayalı ortaklık — benzerlik ya da ortaklık · adlara benzer biçim değişiklikleri alan gelecek zaman fiili · bu, onun benzeri ya da dengidir
  المضارعة هي التشابه بين الشيئين (maqayis;sihah); المضارعة للشيء أن يضارعه كأنه مثله أو شبهه (tahdhib); هذا ضرع هذا وصرعه أي مثله (tahdhib); المضارعة أصلها التشارك في الضراعة ثم جرد للمشاركة (mufradat); الفعل المستقبل مضارع لمشاكلته الأسماء (tahdhib;mufradat)
- **B005** kurumuş ya da kırmızı ve kötü kokulu diye tanımlanan bitki — kurumuş bir bitki; başka bir görüşte kırmızı ve kötü kokulu bitki
  الضريع وهو نبت (maqayis); الضريع يبيس الشبرق وهو نبت (sihah); الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس (tahdhib); قيل هو يبيس الشبرق وقيل نبات أحمر منتن الريح (mufradat)
- **B006** güneşin batmaya yaklaşması [kalıp] — güneş batmaya yaklaştı
  تضريع الشمس دنوها للمغيب (sihah); ضرعت الشمس أي دنت للغروب (tahdhib)
- **B007** tenceredeki yemeğin pişmek üzere olması [kalıp] — tenceredeki yemek pişmek üzere oldu
  ضرعت القدر أي حان أن تدرك (sihah); ضرعت القدر تضريعا إذا حان أن تدرك (tahdhib)
- **B008** gölgenin azalıp kısalması [kalıp] — gölge azalıp kısaldı
  تضرع الظل قل وقلص (tahdhib); ظلاله تضرع في فيء الغداة تضرعا (tahdhib)
- **B009** malını birine sunup yararlanmasına açmak [kalıp] — malımı ona sundum ve yararlanmasına açtım
  أضرعت له مالي أي بذلته له (tahdhib); ماله لي مضرع أي مبذول (tahdhib)
- **B010** atın binicisine üstün gelip denetimden çıkması — sahibine ya da binicisine üstün gelen at
  لفلان فرس قد ضرع به أي غلبه (tahdhib)
- **B011** ince ve seyrek kıvamlı içecek — ince ve seyrek kıvamlı içecek
  الضريع الشراب الرقيق (tahdhib)
- **B012** kaburga kemiğini etin altında örten ince zar — etin altında kaburga kemiğini örten ince deri
  الجلدة التي على العظم تحت اللحم من الضلع هي الضريع (tahdhib)
- **B013** ipi oluşturan bükümlü kollar — ipi oluşturan bükümlü kollar
  الضروع والصروع قوى الحبل واحدها ضرع وصرع (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:6, and ## Buluşmalar) =====
## Yüz: kurumuş toprak, yumuşamış toprak

İkinci ve sekizinci ayetler aynı iki kelimeyle başlar, "yüzler, o gün" der ve yalnızca bir sıfatta ayrılır. Birinci sıfat خاشعة'dır. Bu kelime alçalıp sinmeyi anlatır: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Araplar aynı kelimeyi toprak için de kullanır: {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:tozlu ve çökük bir yer, source:"خ ش ع,B002"}; {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}; {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"}. Ayetin anlamı eğik ve ezik bir yüzdür. Yanında ise yağmur görmemiş, tozlanmış, yere yapışmış bir toprak duyulur.

Üçüncü ayet bu toprağın nasıl yorulduğunu gösterir: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Bitkinlik, ayakta durup çalışmaktan gelir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:yorgunluktur; insanın tükenene dek ayakta kalmasıdır, source:"ن ص ب,B004"}. Aynı kelime yüze çökmüş kederi de anlatır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bırakan keder, source:"ن ص ب,B004"}. Beşinci ayette bu kurumuş yüz sulanır: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir pınardan içirilir, source:88:5}. Sulamak, birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:içecek vermek, source:"س ق ي,B001"}. Kuru toprağı diriltmesi gereken su burada yakan sudur. Toprağı canlandıran düzen tersine dönmüştür.

Kur'an kurumuş toprağın suyla dirilişini aynı kelimeyle anlatır. Allah ayetlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirince kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen ardından {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39} der. Diriltilmekten şüphe edenlere de sahne aynı sözlerle kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ, tr:ve tera'l-arda hâmideten, gloss:yeri kupkuru ve cansız görürsün, source:22:5}. Buradaki cansız toprak sıfatı, çökük toprağın tanımında geçen kelimedir: {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:çökük ve cansız toprak, source:"خ ش ع,B002"}. Sağır edici çığlığın geldiği gün anlatılırken toz da yüzlere konar: {ar:فَإِذَا جَآءَتِ ٱلصَّآخَّةُ, tr:fe-izâ câeti's-sâhha, gloss:kulakları sağır eden geldiğinde, source:80:33}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}. Burada tozlu toprak ile tozlu yüz aynı resimde birleşir.

Altıncı ayetteki yiyecek, yüzün halini adında taşır. Yüzün eğikliği şöyle açıklanır: {ar:الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح, tr:el-huşûu'd-darâa; izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:huşu boyun eğmektir; kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. Bu açıklamadaki "boyun eğmek" kelimesi, yiyecek adı ضريع ile aynı köktendir: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Aynı kök incelmiş bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yiyecekle boyun eğme arasındaki bağ kök birliğinden gelir. Yüzün eğikliğine bağlanması ise kelimelerin açıklamasındandır.

Sekizinci ayette öteki sıfat gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutlu, source:88:8}. Bu kelime yumuşamayı ve tazeliği anlatır: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:şey yumuşak ve esnek oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın tazeliği ve güzelliği, source:"ن ع م,B002"}. Aynı kök rüzgârların en nemlisine de ad verir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:rüzgârların en ıslağı ve en nemlisi olan güney rüzgârı, source:"ن ع م,B009"}. Bu yüzün toprağında akan bir pınar vardır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ', gloss:su gözelerinden kaynayıp akan pınar, source:"ع ي ن,B006"}. Dokuzuncu ayetteki hoşnutluk {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfkenin karşıtını gösteren kök, source:"ر ض و,B001"} diye tanımlanır. On üçüncü ayetteki sedirler ise sevinçten adlandırılmıştır: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan sedir adını sevinçten alır, source:"س ر ر,B011"}; {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sevinç kederden boş bir haldir, source:"س ر ر,B010"}. Üçüncü ayetteki yorgunluk iz bırakan bir kederdi. Burada sedirin adı, kederden boş olan bir sevinçtir.

Yirminci ayette göz toprağın kendisine çevrilir. Arapçada iyi toprağın sıfatı yumuşaklıktır: {ar:أرض أريضة لينة طيبة, tr:ardun erîdatun leyyinatun tayyibe, gloss:yumuşak ve verimli toprak, source:"ء ر ض,B002"}. Bu, nâime'nin tanımındaki yumuşaklığın aynısıdır. Göğe verilen adlardan biri de bulut ve yağmurdur: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da gök der, source:"س م و,B004"}. Böylece göğe ve yere yöneltilen bakış, iki yüzün farkını da gösterir: yere su iner ya da inmez.

Kur'an iki yüzü başka yerlerde de aynı sözlerle karşı karşıya koyar. Güzel davrananlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehum katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma bürür, source:10:26} denir. İyilerin yüzü için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Burada nimet kelimesi nâime ile aynı köktendir. O günün yüzleri {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} ve {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} diye ikiye ayrılır. Sabredenlere verilen karşılık da surenin iki kelimesini bir arada söyler: {ar:وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:ve lakkâhum nadraten ve surûrâ, gloss:onlara tazelik ve sevinç kavuşturdu, source:76:11}. Üçüncü ayetteki yorgunluk bahçede ortadan kaldırılır. Pınarlı bahçelerdeki takva sahipleri için {ar:لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ, tr:lâ yemessuhum fîhâ nasab, gloss:orada onlara yorgunluk dokunmaz, source:15:48} denir. Bahçe halkı da aynı sözü kendisi söyler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne bitkinlik, source:35:35}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:2 خَٰشِعَةٌ خ ش ع B002; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:5 تُسْقَىٰ س ق ي B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:8 نَّاعِمَةٌ ن ع م B002; 88:8 نَّاعِمَةٌ ن ع م B009; 88:9 رَاضِيَةٌ ر ض و B001; 88:12 عَيْنٌ ع ي ن B006; 88:13 سُرُرٌ س ر ر B010; 88:13 سُرُرٌ س ر ر B011; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B002

## Ateş, kaynar su ve pişme

Dördüncü ayet şöyledir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Fiil, ateşin içine girip onun sıcaklığına katlanmayı anlatır: {ar:صلي الرجل نارا إذا أدخلته النار, tr:saliye'r-raculu nâran izâ edhaltehu'n-nâr, gloss:adamı ateşe soktuğunda saliye denir, source:"ص ل ي,B003"}. Fiili açıklayan cümlede, ateşe gireni surenin kendisi adlandırır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:salâ'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Dördüncü ayetteki fiil ile yirmi üçüncü ayetteki inkâr, bu cümlede birleşir. Ateşin sıfatı, demirin ateşte kızdırılmasını anlatan kelimedir: {ar:الحامية الحارة, tr:el-hâmiyetü'l-hârra, gloss:hâmiye sıcak olandır, source:"ح م ي,B001"}; {ar:أحميت الحديد في النار فهو محمى, tr:ahmeytü'l-hadîde fi'n-nâri fe-huve muhmâ, gloss:demiri ateşte kızdırdım; o kızgındır, source:"ح م ي,B001"}. Beşinci ayetteki pınarın sıfatı ise sıcaklığın en uç noktasıdır: {ar:حميم آن قد انتهى حره وعين آنية, tr:hamîmun ân kad intehâ harruhû ve aynun âniye, gloss:sıcaklığı son noktaya varmış kaynar su ve âniye pınar, source:"ء ن ي,B003"}; {ar:بلغ إناه من شدة الحر, tr:belağa inâhu min şiddeti'l-harr, gloss:sıcaklığın şiddetinden son noktasına vardı, source:"ء ن ي,B003"}. Surenin "âniye pınar" sözü, Arapçada böyle bir terkip olarak da kullanılır.

Bu kelimeler mutfakta da kullanılır ve o kullanım ayetin anlamının yanında duyulur. Ateşe girme fiili et kızartmayı da anlatır: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti kızarttım, source:"ص ل ي,B004"}. Ateşin sıfatı kızmış fırın için de söylenir: {ar:حمى النهار وحمي التنور أي اشتد حره, tr:hamiye'n-nehâru ve hamiye't-tennûru ey iştedde harruh, gloss:gün ve tandır kızdı, sıcaklığı arttı, source:"ح م ي,B001"}. Pınarın sıfatının kökü yemeğin pişme anını adlandırır: {ar:انتظرنا إنى الطعام أي إدراكه, tr:intazarnâ inâ't-taâmi ey idrâkeh, gloss:yemeğin pişmesini bekledik, source:"ء ن ي,B003"}. Yiyecek adı ضريع'in kökü de tencerenin pişmek üzere olduğunu söyler: {ar:ضرعت القدر أي حان أن تدرك, tr:daraati'l-kıdru ey hâne en tudrik, gloss:tencerenin pişme vakti geldi, source:"ض ر ع,B007"}. Üçüncü ayetteki yorgunluk kelimesinin kökü de ocağın üstüne kurulan sacayağına ad verir: {ar:نصبت للقطاة شركا ونصبت للقدر نصبا, tr:nasabtü li'l-katâti şereken ve nasabtü li'l-kıdri nasbâ, gloss:bağırtlağa tuzak kurdum ve tencereye ayak kurdum, source:"ن ص ب,B001"}. Böylece dördüncü, beşinci ve altıncı ayetlerin kelimeleri bir mutfağın dilini konuşur: kızgın fırın, kızaran et, son kıvamına varan sıcaklık, pişmek üzere olan tencere. Kur'an bu dili ateş için açıkça kullanır: {ar:سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ, tr:sevfe nuslîhim nâran küllemâ nadicet cülûduhum beddelnâhum cülûden ğayrahâ li-yezûku'l-azâb, gloss:onları ateşe sokacağız; derileri piştikçe azabı tatsınlar diye başka derilerle değiştireceğiz, source:4:56}. Bu ayette ateşe sokma fiili, pişme fiili ve tatma fiili bir aradadır. Mümin kıvamını beklemesin diye uyarılan yemeğin dili de aynıdır. Allah, müminlere Peygamber'in evlerine nasıl girileceğini öğretirken şöyle der: {ar:إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ, tr:ilâ taâmin ğayra nâzırîne inâh, gloss:pişme vaktini gözetmeden bir yemeğe, source:33:53}. Bu tek ayette beşinci ayetteki pişme anının kökü, altıncı ayetteki yemek ve on yedinci ayetteki bakış kelimesi bir araya gelir.

Aynı iki komşu kelime, üçüncü ayetteki nâsıba ile dördüncü ayetteki taslâ, avcı dilinde de birbirine bağlanır. Kurmak fiili tuzak kurmayı anlatır, ve ateşe girme kökü tuzağın adıdır. Bu tuzak da kurmak fiiliyle tanımlanır: {ar:المصلاة أن تنصب شركا ونحوه, tr:el-maslâtü en tensibe şereken ve nahveh, gloss:maslât tuzak ve benzerini kurmaktır, source:"ص ل ي,B005"}. Bu yan anlamda emeğiyle yorulan yüz, kendi kurduğu tuzağa yürüyen kuş gibidir. Ayetteki anlam yine yorgunluk ve ateştir.

Kur'an bu ateşi başka yerlerde de aynı kelimelerle anar. Kâria suresinde terazisi hafif gelen için {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11} denir. Önceki surede hatırlatmadan kaçan bedbaht {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12} diye anılır. Leyl suresi ateşe gireni surenin yirmi üçüncü ayetindeki fiille tanımlar: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}; {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16}. Kaynar su da başka yerlerde aynı sıfatla geçer: {ar:يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ, tr:yetûfûne beynehâ ve beyne hamîmin ân, gloss:onunla son noktasına varmış kaynar su arasında dolaşırlar, source:55:44}. Kaynar sudan içirilenler için {ar:وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ, tr:ve sukû mâen hamîmen fe-kattaa em'âehum, gloss:kaynar su içirilip bağırsakları parçalanır, source:47:15} denir. Allah Peygamber'e "hak Rabbinizdendir, dileyen inansın, dileyen inkâr etsin" demesini söyledikten sonra yardım isteyenlere verilecek suyu anlatır: {ar:بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ, tr:bi-mâin ke'l-mühli yeşvi'l-vucûh, gloss:yüzleri kavuran erimiş maden gibi bir su, source:18:29}. Buradaki "kavurmak" fiili, eti kızartmanın açıklamasında geçen fiildir. Kaynar su yüze dökülür ve onu pişirir. Zakkum ağacı günahkârın yiyeceğidir: {ar:كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ, tr:ke'l-mühli yağlî fi'l-butûn, gloss:erimiş maden gibi karınlarda kaynar, source:44:45}; {ar:كَغَلْىِ ٱلْحَمِيمِ, tr:ke-ğalyi'l-hamîm, gloss:kaynar suyun kaynaması gibi, source:44:46}. Kur'an bunu içenlerin nasıl içtiğini de söyler: {ar:فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ, tr:fe-şâribûne şurbe'l-hîm, gloss:susuzluk hastalığına tutulmuş develer gibi içerler, source:56:55}.

Kaynaklar: 88:3 نَّاصِبَةٌ ن ص ب B001; 88:4 تَصْلَىٰ ص ل ي B003; 88:4 تَصْلَىٰ ص ل ي B004; 88:4 تَصْلَىٰ ص ل ي B005; 88:4 حَامِيَةً ح م ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:6 ضَرِيعٍ ض ر ع B007; 88:23 كَفَرَ ك ف ر B003

## İki pınar ve kaplar

Surede iki pınar vardır ve ikisi de aynı adı taşır. Beşincisi {ar:مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:min aynin âniye, gloss:son noktasına varmış sıcak bir pınardan, source:88:5}, on ikincisi ise {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Ad aynıdır, değişen yalnızca sıfattır. Birinde su sıcaklığın sonuna varmıştır. Ötekinde hareket halindedir: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî cireten ve ceryen ve cereyânâ, gloss:su aktı, source:"ج ر ي,B001"}. Kaynayan suyun durduğu bir yer vardır, ama akan su yenilenir. Kur'an bu iki pınarı aynı surede, birkaç ayet arayla yan yana koyar. Biri günahkârların dolaştığı {ar:حَمِيمٍ ءَانٍۢ, tr:hamîmin ân, gloss:son noktasına varmış kaynar su, source:55:44} ve diğeri Rabbinin makamından korkanların iki bahçesinde akan sudur: {ar:فِيهِمَا عَيْنَانِ تَجْرِيَانِ, tr:fîhimâ aynâni tecriyân, gloss:ikisinde de akan iki pınar vardır, source:55:50}.

Beşinci ayetteki sıfatın harfleri, Arapçada kap anlamına gelen kelimenin çoğuluyla da aynıdır: {ar:الإناء معروف وجمعه آنية والأواني, tr:el-inâu ma'rûfun ve cem'uhû âniyetun ve'l-evânî, gloss:kap bilinir; çoğulu âniye ve evânîdir, source:"ء ن ي,B004"}. Ayetteki anlam sıcaklıktır. Yanında ise kapların adı duyulur. On dördüncü ayet bu kapları bahçeye koyar: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}. Kevb kulpsuz bir kadehtir: {ar:الكوب القدح لا عروة له, tr:el-kûbü'l-kadahu lâ urvete leh, gloss:kevb kulpsuz kadehtir, source:"ك و ب,B001"}. Konmuş olmak, kaldırılmışın karşıtıdır: {ar:وضعت الشيء أضعه وضعا وهو ضد رفعته, tr:vada'tü'ş-şey'e edauhû vad'an ve huve zıddü rafa'tüh, gloss:bir şeyi koydum; kaldırdım'ın zıddı, source:"و ض ع,B001"}. Kadehler el altında hazır durur, istenmeden önce oradadır. Kur'an aynı iki kelimeyi, yani kapların adını ve kadehleri, sabredenlerin karşılığını anlatırken yan yana getirir: {ar:وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠, tr:ve yutâfu aleyhim bi-âniyetin min fiddatin ve ekvâbin kânet kavârîrâ, gloss:çevrelerinde gümüş kaplar ve billur kadehler dolaştırılır, source:76:15}. Aynı ses bir yerde kaynayan pınarın sıfatıdır, başka bir yerde bahçenin gümüş kapları.

Bahçe halkı da içirilir. Fiil iki tarafta da aynıdır, değişen kaynaktır: {ar:وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا, tr:ve yuskavne fîhâ ke'sen kâne mizâcuhâ zencebîlâ, gloss:orada zencefil katkılı bir kadehten içirilirler, source:76:17}; {ar:عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا, tr:aynen fîhâ tusemmâ selsebîlâ, gloss:orada Selsebil denen bir pınardan, source:76:18}; {ar:يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ, tr:yuskavne min rahîkın mahtûm, gloss:mühürlü saf bir içkiden içirilirler, source:83:25}. Bahçenin pınarı insanın elinde akar: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdullâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği ve diledikleri yere fışkırttıkları bir pınar, source:76:6}. Kadehler de bu pınardan doldurulur: {ar:بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ, tr:bi-ekvâbin ve ebârîka ve ke'sin min maîn, gloss:kadehler ibrikler ve akan pınardan doldurulmuş kâse ile, source:56:18}. Buradaki "maîn" kelimesi gözle görünen akar suyu anlatır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Allah, Peygamber'e bu suyun kimden geldiğini sormasını söyler: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki suyunuz yere çekilse size akar suyu kim getirir, source:67:30}.

Arapçada içmek de beslenmenin bir parçası sayılır: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey'i ve't-taâmu huve'l-me'kûlu ve'l-it'âmu yekau hatta'l-mâ', gloss:tatma kökü; yemek yenendir; doyurmak suya bile uzanır, source:"ط ع م,B001"}. Böylece beşinci ve altıncı ayetler tek bir sofradır: içecek kaynar sudur, yemek de ضريع. Son ayetlerdeki azap kelimesinin kökü ise tatlı suyu da adlandırır: {ar:عذب الماء عذوبة فهو عذب طيب, tr:azube'l-mâu uzûbeten fe-huve azbun tayyib, gloss:su tatlılaştı; o tatlı ve hoş sudur, source:"ع ذ ب,B001"}. Bu anlam ayetteki cezanın yanında duyulur. Aynı harfler bir yerde tatlı su, başka bir yerde azaptır. Tatlı suyu bekleyen yüz, kaynar suyla karşılaşır.

Kaynaklar: 88:5 تُسْقَىٰ س ق ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:5 ءَانِيَةٍ ء ن ي B004; 88:6 طَعَامٌ ط ع م B001; 88:12 عَيْنٌ ع ي ن B006; 88:12 جَارِيَةٌ ج ر ي B001; 88:14 أَكْوَابٌ ك و ب B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:24 ٱلْعَذَابَ ع ذ ب B001

## Doyurmayan yemek

Altıncı ayet önce kesin bir yokluk bildirir, sonra tek bir istisna koyar: {ar:لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ, tr:leyse lehum taâmun illâ min darî', gloss:onlar için darî'den başka yemek yoktur, source:88:6}. Yedinci ayet bu istisnanın da yemeğin iki işinden hiçbirini görmediğini söyler: {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besler ne de açlığı giderir, source:88:7}. Yemek iki iş görür: bedeni doldurur ve eksikliği giderir. ضريع bu ikisini de yapmaz. Ayrıca adı bu iki eksikliği de taşır.

ضريع kuruyunca bu adı alan dikenli bir bitkidir: {ar:الضريع يبيس الشبرق وهو نبت, tr:ed-darîu yebîsu'ş-şibrik ve huve nebt, gloss:darî' kurumuş şibriktir; bir bitkidir, source:"ض ر ع,B005"}; {ar:الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس, tr:ed-darîu nebtun yukâlü lehu'ş-şibriku ve ehlü'l-Hicâzi yüsemmûnehu'd-darîa izâ yebis, gloss:şibrik denen bitki; Hicaz halkı kuruyunca ona darî' der, source:"ض ر ع,B005"}; {ar:قيل هو يبيس الشبرق وقيل نبات أحمر منتن الريح, tr:kîle huve yebîsu'ş-şibriki ve kîle nebâtun ahmeru müntinü'r-rîh, gloss:kurumuş şibrik ya da kırmızı ve pis kokulu bir bitki, source:"ض ر ع,B005"}. Aynı harfler zayıflamış bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yoksulluğu da anlatır: {ar:مظهرين الضراعة وهي شدة الفقر إلى الشيء والحاجة إليه, tr:muzhirîne'd-darâata ve hiye şiddetü'l-fakri ile'ş-şey'i ve'l-hâceti ileyh, gloss:bir şeye şiddetli yoksulluk ve muhtaçlık, source:"ض ر ع,B002"}. İki karşılık da yedinci ayetteki iki olumsuzluğun karşısına düşer. Besleme kelimesi semizliktir ve zayıflığın karşıtıdır: {ar:السمن نقيض الهزال, tr:es-simenu nakîdu'l-hüzâl, gloss:semizlik zayıflığın zıddıdır, source:"س م ن,B001"}. Gidermek kelimesi ise zenginlik ve ihtiyaçsızlıktır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ademü'l-hâcâti ve kılletü'l-hâcâti ve kesretü'l-kınyât, gloss:ihtiyaçların yokluğu ya da azlığı ve malın çokluğu, source:"غ ن ي,B001"}. Yemeğin adı yokluğu söyler, ayet de yemeğin yokluğu gidermediğini. Açlık bile yemeğin yokluğuyla tanımlanır: {ar:الألم الذي ينال الحيوان من خلو المعدة من الطعام, tr:el-elemu'llezî yenâlü'l-hayevâne min hulüvvi'l-mideti mine't-taâm, gloss:midenin yemekten boş kalmasıyla canlıya gelen acı, source:"ج و ع,B001"}. Böylece yedinci ayetin son kelimesi, altıncı ayetin yemek kelimesine geri bağlanır. Arapçada iyi beslenen adam için {ar:رجل طاعم حسن الحال, tr:racülün tâimun hasenü'l-hâl, gloss:doymuş adam hali iyi adamdır, source:"ط ع م,B004"} denir. Bunlar ise doyuramayan bir yemekle baş başa kalmıştır.

Aynı harfler bir de yan anlamda duyulur. Darî, memesi büyük koyuna da verilen addır: {ar:شاة ضريع وضريعة عظيمة الضرع, tr:şâtun darîun ve darîatun azîmetü'd-dar', gloss:memesi iri koyun, source:"ض ر ع,B001"}. Kelime ayette kuru dikendir. Yanında ise sütle dolu bir meme duyulur, yani bu yemeğin hiç taşımadığı bolluk. Kökün bir başka kolu, yemeğin içecek olarak da gelebileceğini gösterir: {ar:الضريع الشراب الرقيق, tr:ed-darîu'ş-şerâbü'r-rakîk, gloss:darî' sulu ince içecek, source:"ض ر ع,B011"}.

Kur'an bu yapıyı başka bir sahnede de kurar. Kitabı solundan verilen kişi için şöyle denir: {ar:فَلَيْسَ لَهُ ٱلْيَوْمَ هَٰهُنَا حَمِيمٌۭ, tr:fe-leyse lehü'l-yevme hâhunâ hamîm, gloss:bugün burada onun için yakın bir dost yoktur, source:69:35}; {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irin dışında bir yemek de yoktur, source:69:36}; {ar:لَّا يَأْكُلُهُۥٓ إِلَّا ٱلْخَٰطِـُٔونَ, tr:lâ ye'kuluhû ille'l-hâtiûn, gloss:onu suçlulardan başkası yemez, source:69:37}. Burada da yokluk ve istisna aynı sırayla gelir. Zakkum ağacı için ise {ar:فَإِنَّهُمْ لَءَاكِلُونَ مِنْهَا فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ, tr:fe-innehum le-âkilûne minhâ fe-mâliûne minhe'l-butûn, gloss:ondan yiyip karınlarını dolduracaklar, source:37:66} denir. Karın dolar, ama yedinci ayetteki gibi beden beslenmez. Kur'an başka yerde boğazda kalan yemekten söz eder: {ar:وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا, tr:ve taâmen zâ ğussatin ve azâben elîmâ, gloss:boğazda kalan bir yemek ve acı bir azap, source:73:13}. Yalanlayıcıların gönderildiği gölge de aynı fiille anlatılır: {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. Bu gölge gölge değildir, o yemek de yemek değildir.

Karşı resim de Kur'an'dadır. Allah, Beyt'in Rabbine kulluğa çağırdığı bir topluluğa şunu hatırlatır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cûin ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvene erdiren, source:106:4}. Buradaki "açlıktan" sözü yedinci ayettekiyle aynıdır. Allah bahçede Âdem'e {ar:إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ, tr:inne leke ellâ tecûa fîhâ ve lâ ta'râ, gloss:burada acıkmaman ve çıplak kalmaman senin içindir, source:20:118} der. İbrahim de beşinci ve altıncı ayetlerin iki fiilini Rabbine bağlar: {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî huve yut'imunî ve yeskîn, gloss:beni doyuran ve bana içiren O'dur, source:26:79}.

Kaynaklar: 88:6 لَّيْسَ ل ي س B001; 88:6 طَعَامٌ ط ع م B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:6 ضَرِيعٍ ض ر ع B005; 88:6 ضَرِيعٍ ض ر ع B011; 88:7 يُسْمِنُ س م ن B001; 88:7 يُغْنِى غ ن ي B001; 88:7 جُوعٍ ج و ع B001

## Alçalan ve yükselen

İkinci ayetteki yüz başını eğmiştir: {ar:أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه, tr:aslun vâhidun yedullü ale't-tatâmün; tetâmene ve ta'ta'e ra'sehû, gloss:alçalmayı gösteren kök; başını eğip indirdi, source:"خ ش ع,B001"}. Yemeğinin kökü de alçalmayı anlatır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Onuncu ayette ise bahçe yüksektedir: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yükseliği ve yüksekte oluşu gösteren kök, source:"ع ل و,B001"}; {ar:العلاء فالرفعة, tr:el-alâu fe'r-rif'a, gloss:alâ yüksek mertebedir, source:"ع ل و,B002"}. On üçüncü ayette sedirler kaldırılmıştır. Kaldırılmak da aşağılanmanın karşıtıdır: {ar:الرفعة نقيض الذلة, tr:er-rif'atü nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. On dördüncü ayetteki "konmuş" kelimesinin kökü insanın düşük konumunu da anlatır: {ar:رجل وضيع ضد الشريف والتواضع التذلل, tr:racülün vadîun zıddü'ş-şerîf ve't-tevâdu't-tezellül, gloss:vadî şerefli olanın zıddıdır; tevazu alçalmaktır, source:"و ض ع,B005"}. Bahçede alçak konulan şey insan değildir, hizmet eden kadehlerdir. İnsan yüksek sedirde oturur.

Aynı yükseklik ve alçaklık dünyada da göze gösterilir. Gök yüksekliktir: {ar:أصل يدل على العلو؛ سموت إذا علوت, tr:aslun yedullü ale'l-uluvv; semevtü izâ alevt, gloss:yükseliği gösteren kök; yükseldiğinde semevtü dersin, source:"س م و,B001"}. Yer ise aşağıda olandır: {ar:كل شيء يسفل ويقابل السماء, tr:küllü şey'in yesfülü ve yukâbilü's-semâ', gloss:aşağıda kalıp göğün karşısında duran her şey, source:"ء ر ض,B001"}. Yirmi dördüncü ayetteki azap "en büyük" olandır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullü alâ hılâfi's-sığar, gloss:küçüklüğün karşıtını gösteren kök, source:"ك ب ر,B001"}. İki kökün öteki yüzü de duyulur. Yükseklik kökü kibirli büyüklenmeyi de anlatır: {ar:العلو فالعظمة والتجبر, tr:el-uluvvu fe'l-azametü ve't-tecebbür, gloss:ulüv büyüklenme ve zorbalıktır, source:"ع ل و,B003"}. "En büyük" kelimesinin kökü de kendini büyük görmeyi adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametü ve kezâlike'l-kibriyâ', gloss:kibir büyüklüktür; kibriya da öyledir, source:"ك ب ر,B006"}. Bu anlamlar ayetlerdeki anlamların yanında duyulur. Bahçedeki yükseklik verilmiş bir yüksekliktir. İnsanın kendi kendine verdiği yükseklik ise öteki yüzün yolunu açar ve onu "en büyük" azapla karşılaştırır.

Kur'an kıyameti bu iki hareketle adlandırır: {ar:إِذَا وَقَعَتِ ٱلْوَاقِعَةُ, tr:izâ vekaati'l-vâkıa, gloss:olacak olan olduğunda, source:56:1}; {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}. Dünyada da yükseltme Allah'ın işidir. Müminlere meclislerde yer açmaları ve kalkmaları söylendiğinde kalkmanın karşılığı şudur: {ar:يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ, tr:yerfaillâhullezîne âmenû minkum, gloss:Allah içinizden inananları yükseltir, source:58:11}. Ateşe sunulan zalimler ise {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} diye anılır. O günün gözleri için de {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş, source:70:44} denir. "En büyük azap" sözü Kur'an'da bir yerde daha geçer ve orada küçüğün karşısına konur: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuzîkannehum mine'l-azâbi'l-ednâ dûne'l-azâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce yakın azaptan tattıracağız, source:32:21}. Alt basamak bir uyarıdır, üst basamak sonun kendisidir. Önceki surede de ateş aynı ölçüyle anılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:10 عَالِيَةٍ ع ل و B001; 88:10 عَالِيَةٍ ع ل و B002; 88:10 عَالِيَةٍ ع ل و B003; 88:13 مَّرْفُوعَةٌ ر ف ع B002; 88:14 مَّوْضُوعَةٌ و ض ع B005; 88:18 ٱلسَّمَآءِ س م و B001; 88:20 ٱلْأَرْضِ ء ر ض B001; 88:24 ٱلْأَكْبَرَ ك ب ر B001; 88:24 ٱلْأَكْبَرَ ك ب ر B006

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

