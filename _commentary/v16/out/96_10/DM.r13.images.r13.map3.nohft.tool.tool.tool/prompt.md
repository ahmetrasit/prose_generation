Focus: 96:10. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_10/D.r13/context.md =====
# 96:10 — focus

عَبْدًا إِذَا صَلَّىٰٓ

Anchor translation (canonical reading, reference only):

Bir kulu namaz kıldığında?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | عَبْدًا | عَبْد | ع ب د | N |
| 2 | إِذَا | إِذَا |  | T |
| 3 | صَلَّىٰٓ | صَلَّىٰ | ص ل و | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 ◀ focus عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_10/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ب د (root_000973) — identity root of عَبْدًا (w1)

- **B001** özgür olmayan, sahip olunan kişi — özgür olmayan, sahip olunan kişi · köleler · köle doğmuş veya kuşaklar boyunca köle kalmış kişiler
  العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)
- **B002** Tanrı'ya ait sayılan insan veya topluluk — Tanrı'nın kulu · Tanrı'nın kulları veya ona bağlı topluluk · Tanrı'ya ait sayılan bütün kullar
  تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)
- **B003** boyun eğerek itaat ve tapınma — Tanrı'ya boyun eğerek tapındı · boyun eğerek tapınma · kendini tapınmaya verme · sahte tanrısal güce boyun eğip itaat etti · sahte tanrısal güçlere veya putlara tapan topluluk
  عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)
- **B004** köleleştirmek veya köle gibi boyunduruk altına almak — onu köleleştirdi · kişiyi ezip köleleştirdi; topluluğu köle edindi · onu köle durumuna getirdi · özgür olsa da onu köle gibi boyunduruk altına aldı
  استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)
- **B005** düzleşmiş yol, katranlanmış deve veya kaplanmış gemi — çok geçilerek düzleşmiş yol · derisi baştan başa katranlanmış ve uysallaştırılmış deve · katranla kaplanmış gemi
  الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)
- **B006** saygı gösterilip hizmet edilen kişi — saygı gösterilen, yüceltilen ve hizmet edilen kişi
  المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)
- **B007** güç, sağlamlık ve dayanıklılık — güç, sağlamlık ve dayanıklılık · güçlü ve semiz dişi deve · kumaşının hiç dayanıklılığı yok
  العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)
- **B008** incinmiş gurur, öfke veya kederli iç duygulanım — incinmiş gurur, öfke, keder veya iç sıkıntısı · gururu incindiği için sustu
  العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)
- **B009** gecikmeden yapmak veya koşuda biraz hızlanmak [kalıp] — yapmakta gecikmedi · koşarken biraz hızlandı
  ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)
- **B010** her yana dağılmış kümeler, nesneler veya yollar — her yana dağılmış insan kümeleri, nesneler veya yollar
  العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)
- **B011** bineği yüzünden yolda kalma veya güçlükle direnen deve — bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı · insanlara güçlük çıkararak direnen deve
  أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)
- **B012** güzel koku maddesi ezme taşı — güzel koku maddelerini ezme taşı
  العبدة صلاءة الطيب (jamhara)

## ص ل و (root_000879) — identity root of صَلَّىٰٓ (w3)

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

## ECHO ص ل ي (root_000880) — for صَلَّىٰٓ (w3): withheld observed target; not identity

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

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:10, and ## Buluşmalar) =====
## Rahimde toplanan, tutunan, biçim alan

Bu surenin kelimelerinin çoğu, ayetteki anlamlarının yanında aynı kök ailesinin başka bir sahnesini de duyurur. Bu aile imgesi kelimenin ayetteki anlamının yerine geçmez; onun yanında işitilir. Aşağıdaki her bölüm bu yan sahneleri ayetin kendi anlamına dayanarak okur.

İlk sahne bir rahimdir. Kan rahimde toplanır, rahim onun üzerine kapanır, toplanan şey tutunur ve gebelik kalıcı olur. Sonra biçim belirir, ardından doğum yaklaşır. Gebelik bazen de biçim belli olmadan düşer. Surenin ilk emri olan {ar:ٱقْرَأْ, tr:ikra, gloss:oku, source:96:1} kelimesinin kökü, okumanın yanında dişinin rahminde bir şey taşımasını da adlandırır: {ar:ما قرأت الناقة سلى قط … لم تحمل علقة أي دما ولا جنينا, tr:mâ kara'eti'n-nâkatu selan katt … lem tahmil ʿalakaten ey demen ve lâ cenînen, gloss:dişi deve hiç yavru zarı taşımadı … yani hiç kan pıhtısı ya da cenin taşımadı, source:"ق ر ء,B004"}. Bu söz okumanın kökünü, ikinci ayetin {ar:عَلَقٍ, tr:alak, gloss:tutunan pıhtı, source:96:2} kelimesiyle aynı cümlede birleştirir. Aynı kök, rahmin temizlik ve kanama dönemlerini de adlandırır: {ar:القرء الحيض والقرء أيضا الطهر, tr:el-kur'u'l-hayzu ve'l-kur'u eyzan et-tuhr, gloss:kur' hem âdet hem temizlik dönemidir, source:"ق ر ء,B003"}. Kurân bu kelimeyi tam bu anlamda kullanır ve hemen arkasından rahimde yaratılanı anar. Boşanmış kadınlar {ar:ثَلَٰثَةَ قُرُوٓءٍ, tr:selâsete kurû', gloss:üç dönem, source:2:228} bekler ve {ar:مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ, tr:mâ halaka'llâhu fî erhâmihinn, gloss:Allah'ın rahimlerinde yarattığını, source:2:228} gizlemezler. Böylece okumanın kökü ile yaratmanın fiili aynı ayette rahimde buluşur.

İkinci ayet bu sahnenin başlangıcını adlandırır. Alak hem donmuş kan parçasıdır, {ar:العلق الدم الجامد والقطعة منه علقة, tr:el-ʿalaku'd-demu'l-câmid, gloss:alak donmuş kandır, bir parçasına alaka denir, source:"ع ل ق,B003"}, hem de gebeliğin tutunmasıdır, {ar:علقت المرأة حبلت, tr:ʿalikati'l-mer'e: hebilet, gloss:kadın tutundu, yani gebe kaldı, source:"ع ل ق,B009"}. Birinci ve ikinci ayetlerdeki {ar:خَلَقَ, tr:halaka, gloss:yarattı, source:96:2} fiilinin ailesinde biçimi belirmiş cenin vardır: {ar:مخلقة قد بدا خلقها وغير مخلقة لم تصور, tr:muhallaka kad bedâ halkuhâ ve gayru muhallaka lem tusavver, gloss:biçimlenmiş, yani yaratılışı belirmiş; biçimlenmemiş, yani henüz şekil verilmemiş, source:"خ ل ق,B003"}. Kurân bu aşamaları yeniden diriliş için kanıt olarak sayar. Allah insanlara, dirilişten şüphe ediyorlarsa, onları {ar:مِنْ عَلَقَةٍ ثُمَّ مِن مُّضْغَةٍ مُّخَلَّقَةٍ وَغَيْرِ مُخَلَّقَةٍ, tr:min ʿalakatin summe min mudgatin muhallakatin ve gayri muhallaka, gloss:bir pıhtıdan, sonra biçimlenmiş ve biçimlenmemiş bir çiğnemlik etten, source:22:5} yarattığını söyler ve ekler: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ, tr:ve nukirru fi'l-erhâmi mâ neşâ', gloss:dilediğimizi rahimlerde durdururuz, source:22:5}. Başka bir yerde aşamalar birbirine yaratma fiiliyle bağlanır: {ar:فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةً, tr:fe halaknâ'l-ʿalakate mudga, gloss:pıhtıyı bir çiğnemlik et olarak yarattık, source:23:14}. Dirilişi inkâr eden insana da aynı soru sorulur: {ar:ثُمَّ كَانَ عَلَقَةً فَخَلَقَ فَسَوَّىٰ, tr:summe kâne ʿalakaten fe halaka fe sevvâ, gloss:sonra bir pıhtı oldu, O da yarattı ve düzenledi, source:75:38}. Biçimi verenin kim olduğu da açıkça söylenir: {ar:يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ, tr:yusavvirukum fi'l-erhâm, gloss:sizi rahimlerde biçimlendirir, source:3:6}.

Surenin üçüncü ve sekizinci ayetlerinde de geçen {ar:رَبِّكَ, tr:rabbike, gloss:Rabbin, source:96:1} kelimesinin ailesi bu sahneye bir işleyiş ekler: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye: inşâu'ş-şey'i hâlen fe hâlen ilâ haddi't-temâm, gloss:bir şeyi hal hal, tamamlanacağı sınıra kadar geliştirmek, source:"ر ب ب,B002"}. Yaratan Rab, pıhtıyı aşama aşama tamamlanmaya götürendir. Beşinci ayetin {ar:مَا لَمْ يَعْلَمْ, tr:mâ lem yaʿlem, gloss:bilmediğini, source:96:5} ifadesi bu doğuma bağlanır, çünkü doğan insan hiçbir şey bilmez: {ar:أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًٔا, tr:ahraceküm min butûni ummehâtikum lâ taʿlemûne şey'â, gloss:sizi annelerinizin karınlarından hiçbir şey bilmez halde çıkardı, source:16:78}. Sekizinci ayetin {ar:ٱلرُّجْعَىٰٓ, tr:er-ruc'â, gloss:dönüş, source:96:8} kelimesinin ailesinde ise sahnenin tersi vardır: {ar:إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت, tr:izâ elkati'n-nâkatu hamlehâ kable en yestebîne halkuhû kîle kad racaʿat, gloss:dişi deve yükünü biçimi belli olmadan düşürünce "döndü" denir, source:"ر ج ع,B013"}. Bu kalıp ifade dönüşü ve biçimi tek cümlede birleştirir. Kurân yaratılış ile geri döndürmeyi bir sahnede birlikte anlatır. İnsan {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâ'ib, gloss:bel ile göğüs kemikleri arasından çıkan, source:86:7} bir sudan yaratılmıştır ve {ar:إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ, tr:innehû ʿalâ rac'ihî le kâdir, gloss:O onu geri döndürmeye elbette gücü yetendir, source:86:8}. Surenin sonundaki iki kelimenin ailesinde doğumun yaklaşması da vardır: onuncu ayetin fiili için {ar:أصلت الناقة … إذا وقع ولدها في صلاها وقرب نتاجها, tr:aslati'n-nâka … izâ vakaʿa veleduhâ fî salâhâ, gloss:dişi devenin yavrusu sağrısına indi ve doğumu yaklaştı, source:"ص ل و,B005"}, son ayetin emri için {ar:أقربت المرأة إذا قرب ولادها, tr:akrabeti'l-mer'e, gloss:kadının doğumu yaklaştı, source:"ق ر ب,B012"}. Bu iki aile anlamı uzak birer yankıdır, ama kuruluşları ortadadır.

Bu sahne, insanın düz bir anlatımla verilemeyecek bir yanını gösterir: okunması emredilen kişi, kendisi de toplanmış, tutunmuş ve biçimlendirilmiş bir varlıktır. Surenin dönüş ayeti, rahimden çıkan hayatı tekrar başladığı yere bağlar.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B004; 96:1 ٱقْرَأْ ق ر ء B003; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B009; 96:1 خَلَقَ خ ل ق B003; 96:1 رَبِّكَ ر ب ب B002; 96:5 يَعْلَمْ ع ل م B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B013; 96:10 صَلَّىٰٓ ص ل و B005; 96:19 وَٱقْتَرِب ق ر ب B012

## Tutunmak ve kendini yeterli görmek

İnsan, tutunan bir şeyden yaratılmıştır. Alak kökü asılmayı ve yapışmayı adlandırır: {ar:يناط الشيء بالشيء العالي, tr:yunâtu'ş-şey'u bi'ş-şey'i'l-ʿâlî, gloss:bir şeyin yüksekteki bir şeye asılması, source:"ع ل ق,B001"}; {ar:علق بالشيء نشب به, tr:ʿalika bi'ş-şey'i neşibe bih, gloss:bir şeye takıldı, ona yapıştı, source:"ع ل ق,B001"}. Aynı kök suya yapışan sülüğü de adlandırır: {ar:دويبة في الماء تجمع على علق, tr:duveybetun fi'l-mâ', gloss:suda yaşayan küçük bir hayvan; çoğulu alaktır, source:"ع ل ق,B003"}. Ayrıca canı ayakta tutan en az lokmayı adlandırır: {ar:ما يأكل فلان إلا علقة أي ما يمسك نفسه, tr:mâ ye'kulu fulânun illâ ʿulka, gloss:falan ancak canını tutacak kadar yer, source:"ع ل ق,B006"}. İnsanın başlangıcı yüksekteki bir şeye asılı, tutunarak ve azla yaşayan bir şeydir.

Beşinci ayet bu eksik varlığa öğretilen şeyi anar: bilmediği şey ona verilir. Yedinci ayet sonra tersine döner: insan kendini {ar:ٱسْتَغْنَىٰٓ, tr:istagnâ, gloss:muhtaç olmayan, yeterli, source:96:7} görür. Kök ihtiyaçsızlığı adlandırır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ʿademu'l-hâcât ve killetu'l-hâcât ve kesretu'l-kunyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş şeylerin çokluğu, source:"غ ن ي,B001"}. Aynı kök bir şeyin yetip yetmemesini de anlatır: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yugnî ʿanke hâzâ, gloss:bu sana yetmez, fayda vermez, source:"غ ن ي,B002"}. Kökte kendine bakışla yeterliliği tek figürde birleştiren bir kadın da vardır: {ar:الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي, tr:el-gâniye, gloss:gâniye, kocası ya da güzelliği sayesinde süs takmaya ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Yedinci ayetteki "kendini görmek" ile "yeterli olmak" bu figürde bir araya gelir.

Kurân bu kelimeyi birkaç sahnede inkârla birleştirir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stagnâ, gloss:cimrilik eden ve kendini muhtaç görmeyene gelince, source:92:8}, {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-husnâ, gloss:ve en güzeli yalanlayan, source:92:9}. Peygamber'e, kendini yeterli gören zengin kişiye yönelmesi hatırlatılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'stagnâ, gloss:kendini muhtaç görmeyene gelince, source:80:5}, {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe ente lehû tesaddâ, gloss:sen ona yöneliyorsun, source:80:6}. Gerçek yeterliliğin kime ait olduğu da söylenir. Elçilerini reddedenler için {ar:فَكَفَرُوا۟ وَتَوَلَّوا۟ وَّٱسْتَغْنَى ٱللَّهُ, tr:fe keferû ve tevellev vestagna'llâh, gloss:inkâr ettiler ve yüz çevirdiler, Allah da onlara ihtiyaç duymadı, source:64:6} denir. Tüm insanlara da {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entumu'l-fukarâ'u ila'llâh, va'llâhu huve'l-ganiyyu'l-hamîd, gloss:Allah'a muhtaç olanlar sizsiniz, ihtiyaçsız ve övülmeye layık olan Allah'tır, source:35:15} denir. Hesap gününde ise yeterlilik iddiası kendi ağzından çöker: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ agnâ ʿannî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}.

Rab kelimesinin ailesinde ihtiyaç ile nimet tek kelimede birleşir: {ar:الربى: الحاجة؛ … الربى: النعمة والإحسان, tr:er-rubbâ: el-hâce … er-rubbâ: en-niʿmetu ve'l-ihsân, gloss:rubbâ ihtiyaçtır; rubbâ nimet ve iyiliktir da, source:"ر ب ب,B016"}. Üçüncü ayetteki en cömert sıfatı ihtiyacı gideren vericiyi anlatır: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayr el-cevâdu'l-munʿim, gloss:hayrı çok, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Kurân insanın bu cömertliğe nasıl karşılık verdiğini anlatır: {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe ekramehû ve naʿʿamehû fe yekûlu rabbî ekramen, gloss:Rabbi ona ikram edip nimet verince "Rabbim bana ikram etti" der, source:89:15}. Hemen ardından rızkı daraltılınca {ar:فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe yekûlu rabbî ehânen, gloss:"Rabbim beni aşağıladı" der, source:89:16}. Kısacası insan, ikramı kendi değerinin kanıtı sayar.

On beşinci ayetteki {ar:يَنتَهِ, tr:yentehi, gloss:vazgeçer, source:96:15} fiilinin ailesinde "yeter" anlamı vardır: {ar:فلان ناهيك من رجل… كما يقال حسبك, tr:fulânun nâhîke min racul, gloss:falan sana yeter bir adamdır, "hasbuk" dendiği gibi, source:"ن ه ي,B005"}. Onuncu ayetin kulu ise kendine ait bir şeyi olmayandır: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul, sahip olunandır, source:"ع ب د,B001"}. Sekizinci ayetteki dönüş, yeterlilik iddiasını geçersiz kılar: asılı başlayan varlık, asıl olduğu yere döner.

Kaynaklar: 96:2 عَلَقٍ ع ل ق B001; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B006; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B001; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B002; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B005; 96:1 رَبِّكَ ر ب ب B016; 96:3 ٱلْأَكْرَمُ ك ر م B001; 96:15 يَنتَهِ ن ه ي B005; 96:10 عَبْدًا ع ب د B001

## Başından tutulan hayvan

Perçemden tutma sahnesi bir hayvanı da çağırır. Huysuz hayvan sağanı teper ya da insanlara direnir; perçeminden, burun ipinin ucundan tutulur. Dizgine uyan hayvan kolay yönetilir. Soylu at yakında tutulur ve değer görür.

On sekizinci ayetin {ar:ٱلزَّبَانِيَةَ, tr:ez-zebâniye, gloss:zebaniler, source:96:18} kelimesinin ailesinde, sağanı ya da yavrusunu ayağıyla iten deve vardır: {ar:ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها, tr:nâkatun zebûn, gloss:sağanı ya da yavrusunu ayağıyla memesinden iten deve, source:"ز ب ن,B001"}. Onuncu ayetin kul kelimesinin ailesinde iki zıt deve bulunur: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:baʿîrun mutaʿabbid, gloss:insanlara direnen huysuz deve, source:"ع ب د,B011"} ve {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-baʿîru'l-muʿabbed, gloss:katranla bakılmış, alıştırılmış deve, source:"ع ب د,B005"}. On beşinci ayetin vazgeçme fiilinin ailesinde burun ipinin ucu vardır: {ar:النهاية طرف العران الذي في أنف البعير, tr:en-nihâye tarafu'l-ʿirân, gloss:nihâye, devenin burnundaki ipin ucudur, source:"ن ه ي,B002"}. Son ayetin {ar:تُطِعْهُ, tr:tutiʿhu, gloss:ona boyun eğme, source:96:19} fiilinin ailesinde de dizgine uyan at vardır: {ar:فرس طوع العنان, tr:ferasun tavʿu'l-ʿinân, gloss:dizgine uysal at, source:"ط و ع,B001"}.

Son ayetin {ar:وَٱقْتَرِب, tr:vakterib, gloss:ve yaklaş, source:96:19} emrinin ailesinde yakında tutulan at vardır: {ar:فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة, tr:ferasun mukrabe … ve'l-mukrabetu'l-mukrame, gloss:mukrabe at, yakına alınıp otlamaya salınmayan attır; mukrabe, değer verilen demektir, source:"ق ر ب,B013"}. Bu ifade yakınlığı üçüncü ayetteki cömertlik köküyle birleştirir. Onuncu ayetin namaz fiilinin ailesinde de yarışta ikinci gelen at vardır: {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-sânî, gloss:sâbık birincidir, musallî ikinci, source:"ص ل و,B006"}. İkinci atın başı öndekinin sağrısını izler. Kurân önde olanları yakınlıkla adlandırır: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:önde olanlar, önde olanlardır, source:56:10}, {ar:أُو۟لَٰٓئِكَ ٱلْمُقَرَّبُونَ, tr:ulâ'ike'l-mukarrabûn, gloss:onlar yakınlaştırılanlardır, source:56:11}. Atlar ile nankör insan da bir surede yan yana gelir: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-ʿâdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}, {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li rabbihî le kenûd, gloss:insan Rabbine karşı gerçekten nankördür, source:100:6}.

Bu sahnede azmak, dizgine direnmektir: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-hadd fi'l-ʿisyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Yasaklayan adam huysuz hayvan gibi perçeminden tutulur. Kul ise yakında tutulan, değer gören at gibi yaklaşmaya çağrılır. "Ona boyun eğme" emri, hangi elin dizgine sahip olduğu sorusunu sorar.

Kaynaklar: 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:10 عَبْدًا ع ب د B011; 96:10 عَبْدًا ع ب د B005; 96:15 يَنتَهِ ن ه ي B002; 96:19 تُطِعْهُ ط و ع B001; 96:19 وَٱقْتَرِب ق ر ب B013; 96:10 صَلَّىٰٓ ص ل و B006; 96:6 لَيَطْغَىٰٓ ط غ ي B001

## İki çağrı, iki meclis

Çağırmak, birini sesle kendine doğru çekmektir: {ar:أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك, tr:aslun vâhid, ve huve en tumîle'ş-şey'e ileyke bi savt, gloss:tek bir asıl: bir şeyi sesinle ve sözünle kendine yöneltmek, source:"د ع و,B001"}. On yedinci ayette adam {ar:فَلْيَدْعُ نَادِيَهُۥ, tr:felyedʿu nâdiyeh, gloss:meclisini çağırsın, source:96:17} diye meydan okunur. Meclis, çevresinde toplanılan yerdir: {ar:النادي المجلس يندو إليه من حواليه, tr:en-nâdî el-meclis, gloss:nâdî, çevredekilerin toplandığı meclistir, source:"ن د و,B001"}. Meclis kelimesi, içindeki insanlarla birlikte anlam kazanır: {ar:النادي… لا يسمى ناديا حتى يكون فيه أهله, tr:lâ yusemmâ nâdiyen hattâ yekûne fîhi ehluh, gloss:içinde halkı bulunmadıkça nâdî denmez, source:"ن د و,B001"}. Kök sesin yükselip uzağa ulaşmasını da kapsar: {ar:النداء رفع الصوت وظهوره, tr:en-nidâ' ref'u's-savt, gloss:nida sesi yükseltip duyurmaktır, source:"ن د و,B002"}. Kurân bu meclisi, ayetler okunduğunda inkârcıların övündüğü bir şey olarak gösterir: {ar:أَىُّ ٱلْفَرِيقَيْنِ خَيْرٌ مَّقَامًا وَأَحْسَنُ نَدِيًّا, tr:eyyu'l-ferîkayni hayrun makâmen ve ahsenu nediyyâ, gloss:iki topluluktan hangisinin yeri daha iyi, meclisi daha güzel, source:19:73}. Lut da kavmine meclislerinde yaptıklarını sorar: {ar:وَتَأْتُونَ فِى نَادِيكُمُ ٱلْمُنكَرَ, tr:ve te'tûne fî nâdîkumu'l-munker, gloss:meclisinizde de çirkinliği işliyorsunuz, source:29:29}. Firavun da toplayıp çağırır: {ar:فَحَشَرَ فَنَادَىٰ, tr:fe haşera fe nâdâ, gloss:topladı ve seslendi, source:79:23}.

On sekizinci ayet karşı çağrıdır: {ar:سَنَدْعُ ٱلزَّبَانِيَةَ, tr:senedʿu'z-zebâniye, gloss:biz de zebanileri çağıracağız, source:96:18}. Zebanilerin adı itmekten gelir: {ar:الزبن دفع الشيء عن الشيء, tr:ez-zebnu defʿu'ş-şey'i ʿani'ş-şey', gloss:zebn bir şeyi bir şeyden itmektir, source:"ز ب ن,B001"}; {ar:الزبانية سموا بذلك لأنهم يدفعون أهل النار إلى النار, tr:ez-zebâniye summû bi zâlike li ennehum yedfaʿûne ehle'n-nâr, gloss:zebanilere bu ad, ateş ehlini ateşe ittikleri için verilmiştir, source:"ز ب ن,B002"}. Kök uzaklığı da adlandırır: {ar:الزبن البعد, tr:ez-zebnu'l-buʿd, gloss:zebn uzaklıktır, source:"ز ب ن,B005"}. Kurân ateşin bekçilerini şöyle anlatır: {ar:عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌ شِدَادٌ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ, tr:ʿaleyhâ melâ'iketun gilâzun şidâd, lâ yaʿsûna'llâhe mâ emerahum, gloss:başında Allah'ın emrine karşı gelmeyen sert, güçlü melekler vardır, source:66:6}, {ar:عَلَيْهَا تِسْعَةَ عَشَرَ, tr:ʿaleyhâ tisʿate ʿaşer, gloss:başında on dokuz vardır, source:74:30}. İtmenin kendisi de anlatılır: {ar:يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا, tr:yevme yudaʿʿûne ilâ nâri cehenneme daʿʿâ, gloss:cehennem ateşine itilip kakıldıkları gün, source:52:13}.

Üçüncü bir çağrı da vardır. Onuncu ayetin namazı bir çağrıdır: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duʿâ', gloss:salât duadır, source:"ص ل و,B002"}. Kurân Allah'ın kulunun dua ederken kuşatılmasını cinlerin ağzından anlatır: {ar:لَمَّا قَامَ عَبْدُ ٱللَّهِ يَدْعُوهُ كَادُوا۟ يَكُونُونَ عَلَيْهِ لِبَدًا, tr:lemmâ kâme ʿabdu'llâhi yedʿûhu kâdû yekûnûne ʿaleyhi libedâ, gloss:Allah'ın kulu O'na dua etmeye kalkınca neredeyse üstüne yığılacaklardı, source:72:19}. Son ayetin yaklaşma emri bu çağrıya karşılık verir. Kökte hükümdarın yakın çevresi vardır: {ar:القربان واحد قرابين الملك وهم جلساؤه وخاصته, tr:el-kurbânu vâhidu karâbîni'l-melik, gloss:kurbân, hükümdarın meclis arkadaşları ve has adamlarından biridir, source:"ق ر ب,B004"}. Yakınlık aynı zamanda çağrıya karşılık verilmesidir: {ar:في الرعاية نحو فإني قريب أجيب دعوة الداع, tr:fi'r-riʿâye nahve fe innî karîbun ucîbu daʿvete'd-dâʿ, gloss:gözetme anlamında, "Ben yakınım, dua edenin duasına karşılık veririm" gibi, source:"ق ر ب,B006"}. Kurân'daki ifade şudur: {ar:فَإِنِّى قَرِيبٌ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ, tr:fe innî karîb, ucîbu daʿvete'd-dâʿi izâ daʿân, gloss:Ben yakınım; dua eden bana dua ettiğinde karşılık veririm, source:2:186}. Çağıranlar yakınlığı arar: {ar:يَبْتَغُونَ إِلَىٰ رَبِّهِمُ ٱلْوَسِيلَةَ أَيُّهُمْ أَقْرَبُ, tr:yebtegûne ilâ rabbihimu'l-vesîlete eyyuhum akrab, gloss:hangisi daha yakın olacak diye Rablerine yol ararlar, source:17:57}. Yakın meclis secde eder: {ar:إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ, tr:inne'llezîne ʿinde rabbike lâ yestekbirûne ʿan ʿibâdetih, gloss:Rabbinin yanında olanlar O'na kulluk etmekten büyüklenmezler, source:7:206}, {ar:وَلَهُۥ يَسْجُدُونَ, tr:ve lehû yescudûn, gloss:ve O'na secde ederler, source:7:206}.

Böylece sahnede üç hareket vardır. Adam meclisini çevresine toplar. Allah, uzaklaştırıp iten bekçileri çağırır. Kul ise hükümdarın yakın meclisine çağrılır. Düz bir anlatım bunu tehdit ve emir olarak verir; bu sahne iki karşıt sarayı gösterir.

Kaynaklar: 96:17 فَلْيَدْعُ د ع و B001; 96:17 نَادِيَهُۥ ن د و B001; 96:17 نَادِيَهُۥ ن د و B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:18 ٱلزَّبَانِيَةَ ز ب ن B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B005; 96:10 صَلَّىٰٓ ص ل و B002; 96:19 وَٱقْتَرِب ق ر ب B004; 96:19 وَٱقْتَرِب ق ر ب B006

## Ateş: namaz kılan ve yanan

Onuncu ayetin {ar:صَلَّىٰٓ, tr:sallâ, gloss:namaz kıldı, source:96:10} fiilinin kökü iki tarafı birden adlandırır. Bir anlamı namazdır: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtu'lletî câ'e bihe'ş-şerʿ, gloss:şeriatın getirdiği rükû ve secdeli namaz, source:"ص ل و,B003"}. Öteki anlamı ateşe girmek ve sıcağına katlanmaktır: {ar:الصلا النار وصلى الكافر نارا, tr:es-salâ en-nâr, ve saliye'l-kâfiru nârâ, gloss:salâ ateştir; kâfir ateşe girdi, source:"ص ل و,B001"}; {ar:صليت العود بالنار, tr:salaytu'l-ʿûde bi'n-nâr, gloss:değneği ateşte tutup düzelttim, source:"ص ل و,B001"}. Kurân bu ikiliği kendi eşleştirmeleriyle kurar. Ateşe kimin gireceğini söylerken surenin on üçüncü ayetindeki ifadeyi kullanır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:ki yalanladı ve yüz çevirdi, source:92:16}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve seyucennebuhe'l-etkâ, gloss:en çok sakınan ise ondan uzak tutulacak, source:92:17}. Bu ayetlerde ateşe girmek, yalanlamak, yüz çevirmek ve sakınmak bir aradadır; bunlar surenin on ikinci ve on üçüncü ayetlerinin kelimeleridir. Ölüm anındaki inkârcı için de namaz yalanlamanın karşısına konur: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31}, {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32}. Musa ile Harun da Firavun'a aynı ifadeyle seslenir: {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-ʿazâbe ʿalâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48}. Cehennemdekiler ise kendilerini oraya getiren şeyi şöyle söyler: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:"namaz kılanlardan değildik" dediler, source:74:43}.

Yakalamak ve ateşe atmak bir başka sahnede art arda gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe gullûh, gloss:tutun onu, bağlayın, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra cehenneme atın, source:69:31}. Bu, yeterliliğinin işe yaramadığını söyleyen adamın sahnesidir. Ateş kendisi de çağırır: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Böylece on yedinci ve on sekizinci ayetlerin çağrısı ateşin çağrısıyla buluşur.

On beşinci ayetin fiili bu sahnede yüzün yanıp kararmasıdır: {ar:سفعته النار إذا لفحته لفحا يسيرا فسودت بشرته, tr:sefaʿathu'n-nâr, gloss:ateş onu hafifçe yaladı ve derisini kararttı, source:"س ف ع,B003"}. Altıncı ayetin fiilinin ailesinde yıldırım azabı vardır: {ar:الطاغية الصاعقة ويعني صيحة العذاب, tr:et-tâgiye es-sâʿika, gloss:tâgiye yıldırımdır, yani azap çığlığı, source:"ط غ ي,B004"}. Azgın için varılacak yer de söylenir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe emmâ men tagâ, gloss:azana gelince, source:79:37}, {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe inne'l-cahîme hiye'l-me'vâ, gloss:barınağı cehennemdir, source:79:39}. On ikinci ayetin {ar:بِٱلتَّقْوَىٰٓ, tr:bi't-takvâ, gloss:sakınmayı, source:96:12} kelimesi ise bu ateşe karşı bir kalkandır: {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ caʿlu'n-nefsi fî vikâye, gloss:takva, nefsi korkulan şeyden bir korunak içine almaktır, source:"و ق ي,B002"}. Kurân bu kökü ateşle birlikte kullanır: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi ateşten koruyun, source:66:6}.

Bu sahne, surenin kul ile yasaklayan arasında kurduğu karşıtlığı tek bir kökte toplar. Kul namazla ateşten korunur; yasaklayan, yasakladığı fiilin öteki anlamıyla karşılaşır.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B003; 96:10 صَلَّىٰٓ ص ل و B001; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:6 لَيَطْغَىٰٓ ط غ ي B004; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B002

## Tuzak ve av

Avcılar açık araziye çıkar, tuzak kurar; av ağa takılır. Yaban hayvanı bir süre koşar, sonra durup arkasına bakar. Bu sahnenin üyeleri surenin birçok kelimesine dağılmıştır. Onuncu ayetin namaz fiilinin ailesinde tuzak kurmak vardır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-maslât en tensibe şereken, gloss:maslât, bir şey düşsün de avlansın diye tuzak kurmaktır, source:"ص ل و,B004"}. Bu anlam mecaz olarak birinin yıkımına çalışmak için de kullanılır: {ar:صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة, tr:salaytu li fulân, gloss:falana tuzak kurdum, yani onu helake düşürmek için uğraştım, source:"ص ل و,B004"}. İkinci ayetin alak kökünde ağa takılan ceylan vardır: {ar:علق الظبي في الحبالة يعلق إذا نشق فيها, tr:ʿalika'z-zabyu fi'l-hibâle, gloss:ceylan ağa takıldı, source:"ع ل ق,B011"}. Birinci ayetin ad kelimesinin kökünde avcılar vardır: {ar:خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون, tr:semev, ve humu's-sumât, gloss:topluluk ıssız yerlere ava çıktığında "semev" denir; onlar sumâttır, yani avcılar, source:"س م و,B006"}. On beşinci ayetin fiilinin ailesinde kovalamaca ve yırtıcı kuşun vuruşu bulunur: {ar:المسافعة كالمطاردة, tr:el-musâfaʿa ke'l-mutârade, gloss:müsâfaa kovalamaca gibidir, source:"س ف ع,B005"}; {ar:سفع الطائر ضريبته أي لطمه, tr:sefaʿa't-tâ'iru darîbeteh, gloss:kuş avına vurdu, source:"س ف ع,B004"}. On üçüncü ayetin yalanlama fiilinin ailesinde de kaçan hayvan vardır: {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyy, gloss:yaban hayvanı bir koşu koşup sonra arkasına bakmak için durdu, source:"ك ذ ب,B007"}.

Sahnenin işleyişi tersine döner. Kulun namazına engel olmak isteyen adam bir avcı gibi davranır. Ama yakalanan odur: perçeminden tutulur, tıpkı ağa takılan av gibi. Kurân Peygamber'e karşı kurulan tuzağı ve tuzağın sahibine dönüşünü anlatır: {ar:وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ, tr:ve iz yemkuru bike'llezîne keferû li yusbitûke ev yaktulûke ev yuhricûk, gloss:inkâr edenler seni tutup bağlamak, öldürmek ya da çıkarmak için tuzak kuruyorlardı, source:8:30}, {ar:وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ, tr:ve yemkurûne ve yemkuru'llâh, gloss:onlar tuzak kuruyordu, Allah da tuzak kuruyordu, source:8:30}. Bu sahne, avcının av olduğu bir çevrilmeyi yasaklayanın sonuna bağlar.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B004; 96:2 عَلَقٍ ع ل ق B011; 96:1 بِٱسْمِ س م و B006; 96:15 لَنَسْفَعًۢا س ف ع B005; 96:15 لَنَسْفَعًۢا س ف ع B004; 96:13 كَذَّبَ ك ذ ب B007; 96:15 ٱلنَّاصِيَةِ ن ص ي B001

## Efendi, kul ve itaat

Bu sahnede bir sahip ve sahip olunan vardır. Rab kelimesi sahibi ve itaat edilen efendiyi adlandırır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع, tr:yekûnu'r-rabb el-mâlik, ve yekûnu'r-rabb es-seyyidu'l-mutâʿ, gloss:rab sahip demektir; rab, itaat edilen efendi demektir de, source:"ر ب ب,B001"}. Bu tanım rabbi son ayetteki itaat fiiline bağlar. Onuncu ayetin kulu hem sahip olunandır hem de kulluğunu gösterendir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ʿubûdiyyetu izhâru't-tezellul, gloss:kulluk, alçakgönüllülüğü göstermektir; ibadet ise alçakgönüllülüğün en ileri derecesidir, source:"ع ب د,B003"}. Kulluk itaatle de birleşir: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke naʿbudu: iyyâke nutîʿ, gloss:"yalnız sana kulluk ederiz": yalnız sana, boyun eğerek itaat ederiz, source:"ع ب د,B003"}. Kökte çok yürünmüş, düzleşmiş yol da vardır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muʿabbed, gloss:muabbed yol, çok yürünüp düzlenmiş yoldur, source:"ع ب د,B005"}.

Dokuzuncu ayetin {ar:يَنْهَىٰ, tr:yenhâ, gloss:men eder, source:96:9} fiili emrin zıddıdır: {ar:النهي خلاف الأمر, tr:en-nehyu hilâfu'l-emr, gloss:nehiy emrin zıddıdır, source:"ن ه ي,B001"}. On ikinci ayetin {ar:أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ, tr:ev emera bi't-takvâ, gloss:ya da sakınmayı emrettiyse, source:96:12} ifadesi, aynı kişinin aslında emredebilecek olduğunu söyler: {ar:الأمر الذي هو نقيض النهي, tr:el-emru'llezî huve nakîdu'n-nehy, gloss:nehyin zıddı olan emir, source:"ء م ر,B002"}. Aynı kök aklı da adlandırır: {ar:النهية العقل لأنه ينهى عن قبيح الفعل, tr:en-nuhye el-ʿakl, gloss:nuhye akıldır, çünkü çirkin işten alıkoyar, source:"ن ه ي,B003"}. Namazı yasaklayan adam, kendi aklının görevini tersine çevirir. Kurân namazın kendisinin yasakladığını söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ʿani'l-fahşâ'i ve'l-munker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Doğru yasaklama da nefsin kendisine yöneltilir: {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ʿani'l-hevâ, gloss:nefsini keyfî istekten alıkoyan, source:79:40}. Allah'ın mescitlerinde adının anılmasını engelleyen de anılır: {ar:وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ, tr:ve men azlemu mimmen menaʿa mesâcida'llâhi en yuzkera fîhe'smuh, gloss:Allah'ın mescitlerinde adının anılmasını engelleyenden daha zalim kim olabilir, source:2:114}. Bu ayet, adla başlayan ve secdeyle biten surenin yasaklayanına yakındır.

Altıncı ayetin azma fiili itaatte sınırı aşmaktır; kök sahte mabudu da adlandırır: {ar:الطاغوت… كل معبود من دون الله, tr:et-tâgût … kullu maʿbûdin min dûni'llâh, gloss:tâgût, Allah'tan başka tapılan her şeydir, source:"ط غ ي,B003"}. Kurân bunun en açık örneği olarak Firavun'u gösterir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ firʿavne innehû tagâ, gloss:Firavun'a git, çünkü o azdı, source:79:17}. Firavun sonunda kendini rab ilan eder. On dördüncü ayetteki Allah adının kökü ise tapılanı adlandırır: {ar:إله اسما لكل معبود… فالإله على هذا هو المعبود, tr:ilâh … el-maʿbûd, gloss:ilah, tapılan her şeyin adıdır; buna göre ilah tapılandır, source:"ء ل ه,B001"}.

Son ayetin {ar:لَا تُطِعْهُ, tr:lâ tutiʿhu, gloss:ona boyun eğme, source:96:19} emri, isteyerek boyun eğmeyi yasaklar: {ar:الطوع نقيض الكره, tr:et-tavʿu nakîdu'l-kerh, gloss:tav, zorlamanın zıddıdır, source:"ط و ع,B001"}. Kurân aynı yasağı Peygamber'e başka yerlerde de verir: {ar:فَلَا تُطِعِ ٱلْمُكَذِّبِينَ, tr:fe lâ tutiʿi'l-mukezzibîn, gloss:yalanlayanlara boyun eğme, source:68:8}; {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍ مَّهِينٍ, tr:ve lâ tutiʿ kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye boyun eğme, source:68:10}. Bir başka yerde bu yasak, adı anmak ve secde etmekle aynı yerde geçer: {ar:وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًا, tr:ve lâ tutiʿ minhum âsimen ev kefûrâ, gloss:onlardan hiçbir günahkâra ya da nanköre boyun eğme, source:76:24}. Bundan hemen sonra adı anmak ve gece secde etmek emredilir. Bu, surenin son ayetinin yapısıyla aynıdır. Sahne surenin sorusunu açıkça ortaya koyar: kul kime itaat edecek? Sahibi Rab olan kul, kendini rab yerine koyan adama boyun eğmez.

Kaynaklar: 96:1 رَبِّكَ ر ب ب B001; 96:10 عَبْدًا ع ب د B003; 96:10 عَبْدًا ع ب د B005; 96:9 يَنْهَىٰ ن ه ي B001; 96:12 أَمَرَ ء م ر B002; 96:9 يَنْهَىٰ ن ه ي B003; 96:6 لَيَطْغَىٰٓ ط غ ي B003; 96:14 ٱللَّهَ ء ل ه B001; 96:19 تُطِعْهُ ط و ع B001

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

