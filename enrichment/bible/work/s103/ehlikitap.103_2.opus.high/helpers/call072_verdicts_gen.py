import csv, json, sys
csv.field_size_limit(10**9)
TSV, ANN = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))
ann = {}
for line in open(ANN, encoding='utf-8'):
    if line.strip():
        r = json.loads(line)
        ann[r['id']] = r
def locs(aid):
    return [x.strip() for x in ann[aid]['kaynak'].split('|') if x.strip() and x.strip() != 'hafiza']
def para(aid):
    return int(ann[aid]['paragraf'])

SEF = {
 'Kiddushin 40b': 'SEFARIA:Kiddushin.40b', 'Mishnah Avot 1:14': 'SEFARIA:Pirkei_Avot.1.14',
 'Mishnah Avot 1:6': 'SEFARIA:Pirkei_Avot.1.6', 'Mishnah Avot 2:1': 'SEFARIA:Pirkei_Avot.2.1',
 'Mishnah Avot 2:15': 'SEFARIA:Pirkei_Avot.2.15', 'Mishnah Avot 2:16': 'SEFARIA:Pirkei_Avot.2.16',
 'Mishnah Avot 2:4': 'SEFARIA:Pirkei_Avot.2.4', 'Mishnah Avot 3:1': 'SEFARIA:Pirkei_Avot.3.1',
 'Mishnah Avot 3:15': 'SEFARIA:Pirkei_Avot.3.15', 'Mishnah Avot 3:16': 'SEFARIA:Pirkei_Avot.3.16',
 'Mishnah Avot 4:1': 'SEFARIA:Pirkei_Avot.4.1', 'Mishnah Avot 4:16': 'SEFARIA:Pirkei_Avot.4.16',
 'Mishnah Avot 4:17': 'SEFARIA:Pirkei_Avot.4.17', 'Mishnah Avot 4:22': 'SEFARIA:Pirkei_Avot.4.22',
 'Rosh Hashanah 16b': 'SEFARIA:Rosh_Hashanah.16b', 'Shabbat 153a': 'SEFARIA:Shabbat.153a',
 'Shabbat 31a': 'SEFARIA:Shabbat.31a', 'Sirach 11:19': 'SEFARIA:Ben_Sira.11.19',
 "Ta'anit 23a": 'SEFARIA:Taanit.23a', 'Wisdom of Solomon 5:8': 'SEFARIA:The_Wisdom_of_Solomon.5.8',
}

A, R, U = 'accepted', 'rejected', 'unavailable'
# ref -> (status, reason, [annotation ids])
S = {}
def acc(ref, reason, *aids): S[ref] = (A, reason, list(aids))
def rej(ref, reason, *aids): S[ref] = (R, reason, list(aids))
def una(ref, reason): S[ref] = (U, reason, [])

# --- unavailable named works (prefetch gaps)
una('Didache 1.1', 'Didache is not in the intertext corpus (prefetch gap, recorded in gaps.json); the two-ways text could not be opened, so the connection is unavailable, not rejected.')
una('Didache 1:1', 'Same Didache passage under another citation form; not in the corpus (prefetch gap in gaps.json), so the connection is unavailable.')
una('Epistle of Barnabas 18:1', 'Barnabas is not in the corpus (prefetch gap in gaps.json); the ways-of-light-and-darkness text could not be opened.')
una('Gospel of Thomas 3', 'Gospel of Thomas is not in the corpus (prefetch gap in gaps.json); the saying on self-knowledge and poverty could not be opened.')
una('Gospel of Thomas 63', 'Gospel of Thomas is not in the corpus (prefetch gap in gaps.json); its rich-man saying could not be opened. The canonical Luke 12:16-21 carries the motif on the page instead.')
una('Sirach 11:19', 'The prefetch resolved this to SEFARIA:Ben_Sira.11.19, but the opened Hebrew segment reads "folly and darkness were created for sinners" and lacks the rich man resting on his goods; the intended verse uses another numbering and SEFARIA:Ben_Sira.11.18 is NOT FOUND. Recorded in gaps.json not_found.')

# --- NT accepted
acc('SBLGNT:Luke.9.25', 'Luke 9:25 sets gaining the whole world against losing or forfeiting oneself (heauton apolesas ē zēmiōtheis); the self as the lost capital matches ¶8 (39:15 khasirū anfusahum). Corpus Coranicum lists Luke 9:23-27 as an intertext of 103:2.', 'S103-INC-PRL-001')
acc('SBLGNT:Mark.8.36', 'Mark 8:36 has the same gain-the-world / forfeit-the-psychē calculation; cited with Luke 9:25 in one paralel block at ¶8, not a separate block.', 'S103-INC-PRL-001')
acc('SBLGNT:Matt.16.26', 'Matthew 16:26 repeats the gain/forfeit calculation and adds the question what a person can give in exchange for his life; cited with Luke 9:25 in the ¶8 block.', 'S103-INC-PRL-001')
acc('SBLGNT:Phil.3.7', 'Philippians 3:7 counts former gains (kerdē) as loss (zēmia); Corpus Coranicum (TUK 179, after Torrey 1892) notes that the Peshitta renders this with ḥusrānā, the Syriac counterpart of Arabic ḫusr. Used in the soydas block at ¶8.', 'S103-INC-SYD-001')
acc('SBLGNT:Phil.3.8', 'Philippians 3:8 extends the reckoning (all things counted zēmia, ezēmiōthēn, to gain Christ); cited as part of the Peshitta ḥusrānā note in the ¶8 soydas block.', 'S103-INC-SYD-001')
acc('SBLGNT:Luke.12.18', 'Luke 12:18 begins the rich fool\'s plan to tear down and enlarge his barns; context of the accepted ¶9 block on hoarding and the illusion of secured years (cf. 104:2-3).', 'S103-INC-MTF-003')
acc('SBLGNT:Luke.12.19', 'Luke 12:19 "you have many goods laid up for many years" is the illusion that stored goods secure life, parallel to 104:3 as cited in ¶9.', 'S103-INC-MTF-003')
acc('SBLGNT:Luke.12.20', 'Luke 12:20 "this night your life is demanded of you" turns the stored goods into a loss of the person himself; quoted in the ¶9 block.', 'S103-INC-MTF-003')
acc('SBLGNT:Luke.12.21', 'Luke 12:21 states the moral (storing up for oneself and not rich toward God); supports the ¶9 block without separate quotation.', 'S103-INC-MTF-003')
acc('SBLGNT:Rev.3.17', 'Revelation 3:17 "you do not know that you are wretched ... poor, blind and naked" while claiming wealth fits ¶7: the ledger is read regardless of how the person feels.', 'S103-INC-MTF-002')
acc('SBLGNT:Rev.3.18', 'Revelation 3:18 continues with the counsel to buy refined gold and eye-salve, keeping the commercial idiom; cited in the ¶7 block.', 'S103-INC-MTF-002')
acc('SBLGNT:Matt.25.16', 'Matthew 25:16 shows the entrusted capital traded for profit, the contrast against which the buried talent is judged; cited in the ¶6 block.', 'S103-INC-MTF-001')
acc('SBLGNT:Matt.25.19', 'Matthew 25:19 "after a long time the lord settles accounts" supplies the reckoning scene for ¶6.', 'S103-INC-MTF-001')
acc('SBLGNT:Matt.25.25', 'Matthew 25:25 "here you have what is yours": capital returned intact yet judged as failure, sharpening ¶6\'s point that loss is the shrinking of what was held, not just absent profit.', 'S103-INC-MTF-001')
acc('SBLGNT:Matt.25.29', 'Matthew 25:29 "even what he has will be taken from him": the capital itself is lost, matching ¶6.', 'S103-INC-MTF-001')
acc('SBLGNT:1Cor.3.15', 'Second connection: 1 Cor 3:15 says the person whose work burns suffers loss (zēmiōthēsetai) but is himself saved. The page uses it as a counter-account at ¶12, where 7:9 says the light-scaled lose themselves.', 'S103-INC-KRA-002')
acc('SBLGNT:1Cor.3.13', 'First step of the passage: each one\'s work is revealed by fire on the Day. It is context for the ¶12 karsi_anlati block, which rests on 3:15.', 'S103-INC-KRA-002')
acc('SBLGNT:1Cor.3.14', 'Surviving work receives a wage (misthon); this is the positive pole of the 1 Cor 3:13-15 reckoning, cited in the ¶12 block.', 'S103-INC-KRA-002')
acc('SBLGNT:Eph.5.16', 'Ephesians 5:16 exagorazomenoi ton kairon ("buying up the time") is a commercial image of time, set beside ¶9\'s reading of time as the capital spent in the market.', 'S103-INC-MTF-004')
acc('SBLGNT:Luke.15.13', 'Luke 15:13 has the son squandering his substance (dieskorpisen tēn ousian) far from home, the first step of ¶14\'s traveller who eats his provisions and loses his way.', 'S103-INC-MTF-005')
acc('SBLGNT:Luke.15.17', 'Luke 15:17 "coming to himself ... I perish (apollymai) with hunger" joins being lost and perishing, the pairing ¶14 finds in the khusr family.', 'S103-INC-MTF-005')
acc('SBLGNT:Luke.15.24', 'Luke 15:24 "was dead and is alive, was lost (apolōlōs) and is found" shows the same verb covering lostness and death; cited in the ¶14 block.', 'S103-INC-MTF-005')
acc('SBLGNT:Jas.1.23', 'James 1:23 compares the hearer who does not act to a man looking at his face in a mirror; context for the ¶23 reflection motif.', 'S103-INC-MTF-011')
acc('SBLGNT:Jas.1.24', 'James 1:24 "he looks at himself, goes away and at once forgets what he was like": self-sight that does not last, set beside ¶23\'s small reflected face.', 'S103-INC-MTF-011')
acc('SBLGNT:Jas.1.25', 'James 1:25 makes doing the work (poiētēs ergou) what fixes the self-knowledge, matching ¶23\'s turn from reflection to the mutual act of 103:3.', 'S103-INC-MTF-011')
acc('SBLGNT:John.9.41', 'John 9:41 "now you say \'we see\', your sin remains" places the loss in presumed sight, as ¶22 says the seeing creature may not see its own ledger.', 'S103-INC-MTF-010')
acc('SBLGNT:Jas.5.19', 'James 5:19 sets straying from the truth (planēthē apo tēs alētheias) against someone turning the strayer back; matches ¶18 (ḥaqq versus ḍalāl) and the mutuality of 103:3.', 'S103-INC-MTF-008')
acc('SBLGNT:Jas.5.20', 'James 5:20 says the one who turns a sinner from his wandering saves a life from death; it completes the ¶18 block.', 'S103-INC-MTF-008')
acc('SBLGNT:Heb.3.13', 'Hebrews 3:13 "exhort one another every day, as long as it is called Today" joins mutual exhortation to time, as ¶25 links the reciprocal verb of 103:3 to escape from loss.', 'S103-INC-MTF-012')
acc('SBLGNT:Gal.4.2', 'Galatians 4:2 "under guardians and stewards until the time set by the father", read with 4:1, parallels the property handover at maturity in 4:6 quoted in ¶21.', 'S103-INC-MTF-009')
acc('SBLGNT:Rom.3.23', 'Romans 3:23 "all have sinned and fall short (hysterountai)" is a universal verdict like ¶4\'s al-insān covering everyone; used in the karsi_anlati block on how the exit is defined.', 'S103-INC-KRA-001')
acc('SBLGNT:Rom.3.24', 'Romans 3:24 "justified freely by his grace" defines the exit from the universal verdict differently from 103:3 (faith, righteous deeds, mutual counsel); this is the contrast of the ¶4 block.', 'S103-INC-KRA-001')

# --- NT rejected
rej('SBLGNT:1Cor.13.12', 'Seeing dimly through a mirror concerns partial knowledge of God now versus later; it does not speak to seeing oneself through another (¶23), and James 1:23-24 makes the mirror point more exactly.')
rej('SBLGNT:1Cor.13.3', 'Giving away all possessions without love "profits nothing" is a gain/loss idiom but concerns love as the condition of value; it adds no specific light to the khusr verdict beyond the accepted Luke 9:25 and Matt 25.')
rej('SBLGNT:1Thess.1.3', 'The triad work of faith, labour of love, endurance of hope resonates with 103:3 but this page is 103:2 and no paragraph here develops that triad; better suited to the 103:3 page.')
rej('SBLGNT:1Thess.5.11', 'Mutual encouragement and building up fits 103:3; on this page Heb 3:13 (accepted at ¶25) makes the same point together with time, so this would repeat it.')
rej('SBLGNT:1Tim.6.7', 'Nothing brought in or carried out of the world: the point is already made at ¶9 by Ps 49:18 (he takes nothing at death), which is closer to 104:3.')
rej('SBLGNT:1Tim.6.9', 'Desire for riches plunging people into ruin (olethron kai apōleian) is a general warning; ¶9 is served by the more concrete Luke 12 and Ps 49 scenes, so this would be a repeat.')
rej('SBLGNT:1Tim.6.18', 'Being rich in good works and generous belongs to the exception of 103:3 rather than to the verdict of 103:2; no paragraph here develops it.')
rej('SBLGNT:1Tim.6.19', 'Laying up a good foundation for the future through good works concerns the 103:3 exception; the treasure-transfer motif is not developed on the 103:2 page.')
rej('SBLGNT:2Cor.4.18', 'Things seen are temporary and things unseen eternal: a general contrast that does not meet ¶20-22\'s argument about the visible human who fails to see his own ledger.')
rej('SBLGNT:2Cor.4.4', 'Minds blinded by the god of this age concerns unbelievers\' blindness to the gospel; John 9:41 (accepted at ¶22) fits the claim to sight more exactly.')
rej('SBLGNT:2Cor.5.10', 'Recompense before the judgment seat for deeds is a general judgment motif; ¶12-13 are served by texts that use scales and weighing, which this verse lacks.')
rej('SBLGNT:Eph.2.9', 'Proposed as a counter-account (salvation not from works). The page makes this contrast once with Romans 3:23-24 at ¶4; a second block would repeat it.')
rej('SBLGNT:Eph.4.25', 'Speaking truth to one another as members of one body belongs to tawāṣaw bi-l-ḥaqq in 103:3; no paragraph of the 103:2 page treats truth-telling as such.')
rej('SBLGNT:Gal.6.1', 'Gentle restoration of a transgressor while watching oneself relates to mutual counsel (103:3); James 5:19-20 at ¶18 already carries the turning-back motif.')
rej('SBLGNT:Gal.6.2', 'Bearing one another\'s burdens is a 103:3 mutuality motif, not developed in the 103:2 commentary.')
rej('SBLGNT:Gal.6.7', 'Sowing and reaping is an agricultural retribution image; the 103:2 page builds on market, scale and capital images, and the reaping maxim adds no specific point.')
rej('SBLGNT:Gal.6.8', 'Reaping corruption or eternal life is the same agricultural retribution frame as Gal 6:7; no paragraph uses harvest imagery.')
rej('SBLGNT:Gal.6.9', 'Not growing weary of doing good, with harvest in due season, concerns perseverance (ṣabr, 103:3) rather than the verdict of loss.')
rej('SBLGNT:Heb.10.24', 'Mutually provoking one another to love and good works is a 103:3 motif; Heb 3:13 at ¶25 covers the mutual-exhortation point with the time element.')
rej('SBLGNT:Heb.10.36', 'Need of endurance (hypomonē) to receive the promise belongs to ṣabr in 103:3; not on this page.')
rej('SBLGNT:Heb.4.13', 'Nothing hidden from God\'s eyes is a general omniscience statement; Jer 17:9-10 at ¶22 makes the point of God reading the heart a person cannot read.')
rej('SBLGNT:Heb.9.27', 'Dying once and then judgment is a general eschatological sequence; it adds no image of loss, capital or scales.')
rej('SBLGNT:Jas.2.17', 'Faith without works is dead concerns the faith-works pairing of 103:3, not the verdict of 103:2; better placed on the 103:3 page.')
rej('SBLGNT:Jas.4.13', 'Traders planning to travel, trade and make profit (kerdēsomen) evoke the market, but the point is presumption about tomorrow. ¶6 is about the reduction of capital, and ¶9\'s presumption is covered by Luke 12.')
rej('SBLGNT:Jas.4.14', 'Life as a vapor that appears briefly and vanishes concerns transience; Ps 90 and Ps 49 at ¶9 already carry transience together with counting and wealth.')
rej('SBLGNT:Jas.5.2', 'Riches rotted and garments moth-eaten describe decaying wealth; this repeats ¶9\'s hoarding motif without a new element.')
rej('SBLGNT:Jas.5.3', 'Rusting gold as witness against the hoarders is vivid but repeats the hoarding motif already given at ¶9.')
rej('SBLGNT:Jas.5.4', 'Withheld wages crying out is a fraud-against-workers motif; ¶10-11 treat weights and measures, which Amos 8:5 and Deut 25:13-15 fit more exactly.')
rej('SBLGNT:John.8.39', 'Abraham\'s children shown by deeds concerns lineage versus works (¶19 touches lineage), but the verse adds nothing to the khanāsir point and is a polemic about descent.')
rej('SBLGNT:Luke.15.12', 'The younger son asking for his share is the setup of the parable; the ¶14 block uses 15:13, 15:17 and 15:24, and the request itself adds no point.')
rej('SBLGNT:Luke.16.6', 'The steward halving a debt is debt remission praised as shrewdness. It does not illuminate the false-weight loss of ¶10-11, and reading it as a counter-account would overreach.')
rej('SBLGNT:Luke.16.8', 'The master praising the unjust steward\'s prudence is an interpretive crux about eschatological shrewdness, not a statement about loss or scales.')
rej('SBLGNT:Luke.16.9', 'Making friends with unrighteous mammon to be received into eternal dwellings concerns using wealth for the age to come (103:3 territory); no paragraph treats it.')
rej('SBLGNT:Luke.16.10', 'Faithfulness in little and much is a trustworthiness maxim; ¶21\'s handover of property is better matched by Gal 4:1-2.')
rej('SBLGNT:Luke.16.11', 'Being trusted with true riches after faithfulness with mammon is close to ¶21 (property handed over upon maturity), but Gal 4:1-2 matches the guardianship legal frame more exactly; kept out to avoid a repeat.')
rej('SBLGNT:Luke.16.25', 'The post-mortem reversal of the rich man and Lazarus is a reversal scene, not a loss-of-capital or weighing scene; it would add a separate theme.')
rej('SBLGNT:Luke.17.33', 'Seeking to preserve one\'s life and losing it is the same saying as Luke 9:24-25, already used at ¶8 through Luke 9:25 and the Corpus Coranicum note on 9:24.')
rej('SBLGNT:Mark.10.21', 'Selling all for treasure in heaven belongs to the exchange that escapes loss (103:3), not to the verdict of 103:2.')
rej('SBLGNT:Mark.14.62', 'Jesus applying Daniel\'s son-of-man vision to himself concerns christology; the Aramaic bar ʾĕnāš link to insān is weighed and rejected in TEV-ELN-001, and the Christian reading adds nothing to this ayah.')
rej('SBLGNT:Matt.12.36', 'Accounting for every idle word on the day of judgment is a general accountability statement without the market or scale imagery of the page.')
rej('SBLGNT:Matt.13.44', 'Selling everything with joy to buy the field is a gainful trade (the 103:3 side). Proposed as a counter-account, but the contrast is with the exception, not with the verdict of 103:2.')
rej('SBLGNT:Matt.20.14', 'Equal wages for unequal hours is a parable about grace overriding desert. Its tension with weighing is real, but the page already gives the grace contrast through Romans 3:24 at ¶4.')
rej('SBLGNT:Matt.3.8', 'Fruit worthy of repentance is a deeds-as-evidence motif belonging to 103:3; not on this page.')
rej('SBLGNT:Matt.3.9', 'Abrahamic descent being no guarantee touches ¶19\'s lineage remark, but the verse addresses covenant presumption; the remark in ¶19 is about Arabic vocabulary of lineage, not ancestry claims.')
rej('SBLGNT:Matt.6.19', 'Earthly treasure eaten by moth and rust repeats the hoarding motif already covered at ¶9 by Luke 12 and Ps 49.')
rej('SBLGNT:Matt.6.20', 'Treasure in heaven belongs to the gainful exchange of 103:3; not developed on the 103:2 page.')
rej('SBLGNT:Matt.7.13', 'The broad way to destruction is a two-ways image; ¶14-15 are served by Ps 119:176/Ps 1:6 and Prov 14:12, which keep the double sense of losing one\'s way and perishing.')
rej('SBLGNT:Matt.7.19', 'A fruitless tree cut down and burned is an agricultural judgment image; ¶14\'s burned produce (2:266) is a garden destroyed by wind, and the comparison would be loose.')
rej('SBLGNT:Matt.7.24', 'The wise builder who hears and does belongs to the 103:3 exception; no paragraph builds on the house image.')
rej('SBLGNT:Matt.7.25', 'The house on rock withstanding the storm is the positive pole of the house parable; not developed on the page.')
rej('SBLGNT:Matt.7.27', 'The fall of the house on sand fits ¶17 loosely (turning on one\'s face), but James 1:6-8 and 1 Kgs 18:21 express the double-mindedness of worship "on an edge" more exactly.')
rej('SBLGNT:Matt.7.3', 'Seeing the speck in a brother\'s eye but not the beam in one\'s own concerns hypocritical judging. ¶23\'s image is seeing oneself in another\'s pupil, a different point.')
rej('SBLGNT:Matt.7.5', 'Removing one\'s own beam first concerns self-correction before judging; it does not meet ¶23\'s reflected image.')
rej('SBLGNT:Rev.18.17', 'Great wealth laid waste in one hour (Babylon\'s fall) is a political-eschatological lament; ¶9 already has the individual hoarding scene.')
rej('SBLGNT:Rev.20.12', 'The dead judged from the books according to their works is a judgment-by-books motif. The page uses Avot 3:16\'s ledger at ¶7 and scales at ¶12-13, so this would repeat the point.')
rej('SBLGNT:Rom.1.17', 'Paul rereading Habakkuk 2:4 concerns faith (103:3), not the loss verdict; rejected together with Hab 2:4.')
rej('SBLGNT:Rom.2.11', 'No partiality with God supports universal judgment, but ¶4 is served by Rom 3:23-24, which states the universal verdict itself.')
rej('SBLGNT:Rom.2.6', 'Rendering to each according to works is a general retribution maxim without the page\'s market or scale imagery.')
rej('SBLGNT:Rom.2.7', 'Eternal life for persistence in good work belongs to the 103:3 exception.')
rej('SBLGNT:Rom.5.12', 'Death spreading to all through one man is the Adamic-solidarity argument. It is relevant to ¶4\'s species-wide verdict, but it is a doctrinal claim (later original-sin reading) the ayah does not make; the page keeps the contrast in Rom 3:23-24.')

# --- Jewish named works
acc('Mishnah Avot 2:1', 'Rabbi\'s instruction to reckon the loss (hefsēd) of a commandment against its reward and the gain of a sin against its loss is an explicit profit-and-loss ledger of conduct, matching ¶6\'s comparison of proceeds with capital.', 'S103-TEV-MTF-003')
acc('Mishnah Avot 3:16', 'Akiva\'s open shop, open ledger, writing hand and collectors who exact payment "with or without his knowledge" match ¶7: the ledger, not the mood, is read, and loss can grow unnoticed.', 'S103-TEV-MTF-004')
acc('Shabbat 31a', 'Rava (on Isa 33:6) makes "did you deal in business faithfully?" the first question at judgment, setting market honesty at the head of the final reckoning, as Mutaffifin 83:1-5 in ¶11 ties false measure to the great Day.', 'S103-TEV-YGL-001')
acc('Kiddushin 40b', 'The baraita\'s person seeing himself as half guilty and half meritorious, one act tipping the scale, gives ¶13\'s heavy and light scales a rabbinic interpretive form (on Eccl 9:18).', 'S103-TEV-YGL-002')
acc('Mishnah Avot 1:14', 'Hillel\'s "if I am not for myself who is for me; if I am only for myself what am I" holds together ¶25\'s two claims: the self is one\'s nearest friend, and escape from loss is with others.', 'S103-TEV-MTF-018')
acc("Ta'anit 23a", 'Rava\'s proverb on Ḥoni, "either companionship or death", read in the Talmud\'s own story of Ḥoni dying unrecognized after his long sleep, matches ¶25\'s contrast of the solitary human in 103:2 with the reciprocal verb of 103:3.', 'S103-TEV-MTF-019')
rej('Mishnah Avot 1:6', 'Acquire a companion and judge everyone on the scale of merit: companionship and scales both appear, but the saying concerns charitable judgment of others; Avot 1:14 and Kiddushin 40b carry the page\'s points more exactly.')
rej('Mishnah Avot 2:15', 'Tarfon\'s short day, much work and great wage fit time-as-capital (¶9), but ¶9 already has five blocks; Ps 90:12 makes the time-counting point from scripture.')
rej('Mishnah Avot 2:16', 'Not completing the work yet not being free to desist, with a faithful employer paying wages, concerns the worker\'s reward (103:3), not loss.')
rej('Mishnah Avot 2:4', 'Hillel\'s "do not separate yourself from the community" fits ¶25, but ¶25 already carries Avot 1:14 from the same sage, which states the self/other balance more exactly; avoids a repeat.')
rej('Mishnah Avot 3:1', 'Know whence you came, whither you go, and before whom you will give account (din ve-ḥeshbon): a reckoning motif already represented by Avot 3:16 at ¶7 and Avot 2:1 at ¶6.')
rej('Mishnah Avot 3:15', '"All is according to the majority of deeds" concerns judgment by preponderance. Kiddushin 40b at ¶13 gives the scale image explicitly, so this would be a repeat.')
rej('Mishnah Avot 4:1', 'Ben Zoma\'s redefinitions (who is wise, mighty, rich, honored), with the rich man as the one content with his lot, redefine wealth. The page\'s point is loss of capital, and the contentment teaching would be a separate theme.')
rej('Mishnah Avot 4:16', 'This world as vestibule to the world to come concerns preparation, not loss; no paragraph develops it.')
rej('Mishnah Avot 4:17', 'One hour of repentance and good deeds outweighing the world to come is a time-value saying fitting 103:1/103:3 more than the loss verdict; ¶9 is full.')
rej('Mishnah Avot 4:22', '"All is according to the reckoning (ḥeshbon)" and the inescapable account: a reckoning motif already carried by Avot 3:16 and 2:1.')
rej('Rosh Hashanah 16b', 'Judgment according to deeds at the time of judgment, and acts that tear up a decree, concern New Year judgment and repentance; the opened passage has no scale or loss image fitting this page.')
rej('Shabbat 153a', 'R. Eliezer\'s "repent one day before your death" and the unknown day of death concern repentance and timing (103:3 and 103:1 themes) rather than the loss verdict.')
rej('Wisdom of Solomon 5:8', 'The fetched witness is a Hebrew translation of a Greek work ("what did pride profit us, and what did wealth and boasting bring us?"), not the original. The lament of the wicked is apt, but ¶8-9 already carry the gain/loss reversal with Luke 9:25, Luke 12 and Ps 49.')

# --- Hebrew Bible accepted
acc('WLC:Eccl.1.15', 'Eccl 1:15 "וְחֶסְרוֹן לֹא־יוּכַל לְהִמָּנוֹת", a deficit that cannot be counted, uses the ḥsr root (sound correspondence with ḫsr) and meets ¶2\'s indefinite khusr whose measure is left open; the hapax ḥesrôn is quoted.', 'S103-TEV-SYD-001')
acc('WLC:Ps.8.5', 'Ps 8:5 "מָה־אֱנוֹשׁ" names the human with ʾĕnôš (the BDB root compared with the Arabic ʾns); with 8:6 (ḥsr) both roots of 103:2 stand together in an exalting sense, a counter-image at ¶3 (Tīn\'s best stature). Reader wording flag (אנש absent) is only pointing and maqqef; אֱנוֹשׁ is present.', 'S103-TEV-SYD-002')
acc('WLC:Eccl.7.29', 'Eccl 7:29, God made humankind upright but they sought many devices (ḥiššᵉbōnôt), repeats Tīn\'s two-stage pattern of right creation then fall cited in ¶3; no exception class is given.', 'S103-TEV-MTF-001')
acc('WLC:Ps.14.3', 'Ps 14:3 "all have turned aside, together corrupt; none does good, not even one" is a species-wide verdict like ¶4\'s al-insān, but without an exception clause; quoted at ¶4.', 'S103-TEV-MTF-002')
acc('WLC:Prov.28.22', 'Prov 28:22: the man hastening after wealth "does not know that ḥeser will come upon him". ḥsr root and unknowing loss together match ¶7\'s deficit that grows unnoticed.', 'S103-TEV-SYD-004')
acc('WLC:Ps.49.18', 'Ps 49:18 "at his death he takes nothing" answers the hoarder\'s illusion, set beside 104:2-3 in ¶9.', 'S103-TEV-MTF-005')
acc('WLC:Ps.90.12', 'Ps 90:12 "teach us to number our days" turns counting from money (104:2 ʿaddadahu in ¶9) to days, matching ¶9\'s time-as-capital.', 'S103-TEV-MTF-006')
acc('WLC:Eccl.1.3', 'Eccl 1:3 asks the yitrôn (profit) of all a man\'s ʿāmāl. The Hebrew ʿml root means wearisome toil, not neutral work, and Qohelet\'s profitless toil stands opposite the righteous ʿamal of 103:3 that ¶9 sets against loss. The reader\'s wording flag is a prefix/pointing issue: עֲמָלוֹ is present.', 'S103-TEV-SYD-005')
acc('WLC:Eccl.2.11', 'Eccl 2:11 "וּבֶעָמָל שֶׁעָמַלְתִּי ... וְאֵין יִתְרוֹן" gives Qohelet\'s answer, no profit under the sun; used in the ¶9 soydas block on ʿāmāl.', 'S103-TEV-SYD-005')
acc('WLC:Amos.8.5', 'Amos 8:5 "to make the ephah small and the shekel great and to falsify scales of deceit" spells out the mechanics of giving short measure (akhsara) described in ¶10.', 'S103-TEV-MTF-007')
acc('WLC:Amos.8.6', 'Amos 8:6 ties the fraud to buying the poor for silver; it supports the ¶10 block\'s social reading of making others lose.', 'S103-TEV-MTF-007')
acc('WLC:Deut.25.14', 'Deut 25:14 forbids "ephah and ephah, great and small" in one house, the legal form of 83:2-3\'s two scales in two directions (¶11).', 'S103-TEV-MTF-008')
acc('WLC:Deut.25.13', 'Deut 25:13 "stone and stone, great and small" in the bag is the weights counterpart of 25:14; cited in the ¶11 block.', 'S103-TEV-MTF-008')
acc('WLC:Deut.25.15', 'Deut 25:15 promises long days for a full and just weight; cited in the ¶11 block as the positive command.', 'S103-TEV-MTF-008')
acc('WLC:Lev.19.35', 'Lev 19:35 forbids injustice in measure, weight and capacity; cited in the ¶11 block as the Holiness Code form of the prohibition.', 'S103-TEV-MTF-008')
acc('WLC:Lev.19.36', 'Lev 19:36 commands just balances, weights, ephah and hin, sealed with the Exodus formula; cited in the ¶11 block.', 'S103-TEV-MTF-008')
acc('WLC:Prov.16.11', 'Prov 16:11 makes the balance and all the weights in the bag the LORD\'s work, set beside 55:7-9 (God set the balance; do not make the scale short) in ¶11.', 'S103-TEV-MTF-009')
acc('WLC:Prov.11.1', 'Prov 11:1 "false balances are an abomination to the LORD, a full weight his delight" is cited in the ¶11 Prov 16:11 block as companion statement.', 'S103-TEV-MTF-009')
acc('WLC:Dan.5.27', 'Dan 5:27 "you were weighed in the balances and found ḥassîr (wanting)": the person himself weighed and found deficient, with the Aramaic cognate of ḥsr, meets ¶12 exactly. The reader flag (חסר absent) is because the form is חַסִּיר, which is present.', 'S103-TEV-SYD-006')
acc('WLC:Dan.5.26', 'Dan 5:26 (mene: God numbered your kingdom and finished it) is the counting step of the writing; cited as context in the ¶12 block.', 'S103-TEV-SYD-006')
acc('WLC:Dan.5.28', 'Dan 5:28 (peres: the kingdom divided and given away) is the loss following the weighing; cited in the ¶12 block.', 'S103-TEV-SYD-006')
acc('WLC:Job.31.6', 'Job 31:6 "let him weigh me in balances of ṣedeq" names the scale by a value, as 7:8 "the weighing that day is al-ḥaqq" in ¶12; the difference (Job\'s plea versus the Qur\'anic verdict) is stated.', 'S103-TEV-MTF-010')
acc('WLC:Job.14.5', 'Job 14:5 sets a ḥōq (fixed limit) to human days: ketiv חקו, qere חֻקָּיו. The reader\'s quoted form matched only the qere. Used in a research-layer soydas block at ¶12 on the ḥqq/ḥaqq correspondence and its limits.', 'S103-TEV-SYD-007')
acc('WLC:Ps.62.10', 'Ps 62:10 "on the scales they go up; together lighter than a breath" pictures humans as light on the balance, set beside Qāriʿa\'s light scales in ¶13 with the difference stated.', 'S103-TEV-MTF-011')
acc('WLC:Ps.1.6', 'Ps 1:6 "the way of the wicked will perish (tōʾbēd)": the ʾbd verb joins way and perishing, used with Ps 119:176 to show ¶14\'s straying/perishing pair as a shared semantic field (not cognate).', 'S103-TEV-MTF-012')
acc('WLC:Prov.14.12', 'Prov 14:12 "a way that seems right to a man, its end the ways of death" matches 18:104\'s losers who think they do well (¶15).', 'S103-TEV-MTF-013')
acc('WLC:Prov.16.25', 'Prov 16:25 repeats 14:12 verbatim; noted in the ¶15 block.', 'S103-TEV-MTF-013')
acc('WLC:Prov.16.2', 'Prov 16:2: all a man\'s ways are pure in his own eyes but the LORD weighs (tōkēn) the spirits; self-approval and weighing from outside, matching ¶15.', 'S103-TEV-MTF-013')
acc('WLC:Prov.21.2', 'Prov 21:2 is the doublet of 16:2 with hearts for spirits; cited in the ¶15 block.', 'S103-TEV-MTF-013')
acc('WLC:Exod.3.2', 'Exod 3:2 is the same Moses-and-fire moment as 20:10/28:29 in ¶21, told differently: alone with Jethro\'s flock, he sees a bush burning but not consumed. The Qur\'an has him with family, perceiving (ānastu) a fire and hoping for a brand or guidance. Used as karsi_anlati.', 'S103-TEV-KRA-001')
acc('WLC:Exod.3.3', 'Exod 3:3 "let me turn aside and see this great sight" makes the Exodus scene one of wonder at a sight rather than of hopeful perceiving; part of the ¶21 karsi_anlati block.', 'S103-TEV-KRA-001')
acc('WLC:Exod.3.1', 'Exod 3:1 sets Moses alone tending Jethro\'s flock at Horeb, the frame that differs from the Qur\'anic family journey; cited in the ¶21 block.', 'S103-TEV-KRA-001')
acc('WLC:Jer.17.9', 'Jer 17:9 "the heart is deceitful above all and ʾānuš; who can know it?" is self-unknowing, matching ¶22; the block notes that BDB puts ʾānuš under a root separate from ʾĕnôš.', 'S103-TEV-MTF-015')
acc('WLC:Jer.17.10', 'Jer 17:10, the LORD searches the heart and gives to each according to his ways, completes ¶22: the ledger the person cannot see is read by God.', 'S103-TEV-MTF-015')
acc('WLC:Prov.27.19', 'Prov 27:19 "as in water face answers to face, so the heart of man to man": seeing oneself in relation to another, matching ¶23; its ambiguity is stated.', 'S103-TEV-MTF-016')
acc('WLC:Ps.103.15', 'Ps 103:15 "ʾĕnôš, his days are like grass" shows ʾĕnôš in frailty contexts; used at ¶24 with BDB\'s comparison of the ʾĕnôš root to an Arabic root of inclination and sociability and with Strong\'s alternative derivation.', 'S103-TEV-SYD-009')
acc('WLC:Eccl.4.8', 'Eccl 4:8, the solitary toiler with no second, "depriving (meḥassēr) my soul of good", uses the ḥsr root for self-depletion in solitude, matching ¶25. The wording flag concerns the pointed form; מְחַסֵּר is present.', 'S103-TEV-MTF-017')
acc('WLC:Eccl.4.9', 'Eccl 4:9 "two are better than one, they have a good reward for their toil" is the remedy of ¶25: escape from loss with others.', 'S103-TEV-MTF-017')
acc('WLC:Eccl.4.10', 'Eccl 4:10, when one falls the other lifts him and woe to the one alone, completes the ¶25 block.', 'S103-TEV-MTF-017')
rej('WLC:Dan.7.13', 'Dan 7:13 כְּבַר אֱנָשׁ attests Aramaic ʾĕnāš, the nearest biblical counterpart of insān, but the heavenly-figure vision adds nothing to the loss verdict or to ¶20\'s visibility images. Kept as a rejected (elenen) block for the audit.', 'S103-TEV-ELN-001')

# --- Hebrew Bible rejected
rej('WLC:1Sam.16.7', 'Man looks on outward appearance, the LORD on the heart: about God\'s choice of David, not self-knowledge. Jer 17:9-10 covers ¶22 more exactly.')
rej('WLC:1Sam.2.3', 'Hannah\'s "by him actions are weighed" (ketiv וְלֹא / qere וְלוֹ) is a weighing image, but the ketiv/qere ambiguity (not weighed / weighed by him) makes it a weak witness; ¶12-13 are served by Dan 5:27, Job 31:6 and Ps 62:10.')
rej('WLC:2Sam.12.4', 'Nathan\'s parable of the rich man taking the poor man\'s lamb is about abuse of power; proposed as paralel, but it is not the same story or scene as anything in 103:2 or its commentary.')
rej('WLC:2Sam.12.7', '"You are the man": another\'s story exposing one\'s own guilt relates loosely to ¶22-23 (not seeing one\'s own ledger), but the scene is prophetic indictment of David and would overextend the parallel.')
rej('WLC:2Sam.22.12', 'חַשְׁרַת־מַיִם (a mass of waters) is the ḥšr root that BDB itself says has a different Arabic counterpart; same consonant shape as ḫsr but a false friend (recorded in root_verdicts).')
rej('WLC:Deut.8.9', 'Deut 8:9 "you will lack nothing (לֹא־תֶחְסַר כֹּל) in it" uses ḥsr as plain lack in a land-blessing; it adds nothing beyond Gen 8:3,5 and Eccl 1:15. The wording flag concerns the inflected form, which is present.')
rej('WLC:Eccl.12.14', 'God bringing every deed, every hidden thing, into judgment is a general judgment statement; ¶12-15 use scales and self-deception texts that fit more exactly.')
rej('WLC:Eccl.3.17', 'A time for judging the righteous and the wicked is a general judgment statement without loss or scale imagery.')
rej('WLC:Eccl.4.12', 'The threefold cord not quickly broken extends Eccl 4:9-10, already used at ¶25; a separate block would repeat it.')
rej('WLC:Eccl.5.13', 'Wealth lost in a bad venture and nothing left for the son is a vivid loss of capital, but ¶6 already carries the capital-loss scene with Matt 25 and Avot 2:1, and ¶9 the hoarding scene.')
rej('WLC:Eccl.5.14', 'Naked he goes as he came, taking nothing from his toil: the point is made at ¶9 by Ps 49:18.')
rej('WLC:Eccl.5.15', '"What profit has he who toils for the wind?" repeats the yitrôn question of Eccl 1:3 used at ¶9.')
rej('WLC:Eccl.9.2', 'One fate for righteous and wicked is Qohelet\'s skeptical view that undercuts distinction. As a counter-account it opposes 103:3\'s exception rather than 103:2\'s verdict, so it belongs elsewhere.')
rej('WLC:Exod.13.21', 'The pillar of fire guiding Israel by night shares fire and guidance with 20:10, but it is not the Moses-perceives-fire scene of ¶21; Exod 3:1-3 is the direct counterpart.')
rej('WLC:Exod.22.21', 'Not afflicting widow or orphan is a general protection law; ¶21\'s 4:6 concerns handing over orphans\' property at maturity, which this verse does not address.')
rej('WLC:Ezek.19.12', 'The vine plucked up, its fruit dried by the east wind and consumed by fire, is close to 2:266\'s burned garden (¶14), but it is a dirge over Judah\'s kings; the analogy is loose and ¶14 already has two blocks.')
rej('WLC:Gen.1.31', '"Very good" creation fits ¶3\'s ahsan taqwīm loosely; Ps 8:5-6 and Eccl 7:29 make the creation/fall contrast more exactly.')
rej('WLC:Gen.20.18', 'עָצֹר עָצַר (the LORD closed every womb) shows Hebrew ʿṣr "restrain, shut up", which does not meet any sense ¶5/¶14 borrow from Arabic ʿaṣr; recorded in root_verdicts as no qualifying parallel.')
rej('WLC:Gen.3.17', 'In pain (ʿiṣṣābôn) you shall eat all the days of your life: a toil-curse motif not connected to loss of capital or scales on this page.')
rej('WLC:Gen.3.19', 'Return to dust after labour is a mortality motif; ¶24\'s frailty point is carried by Ps 103:15, so this would be a repeat.')
rej('WLC:Hab.2.4', 'The righteous live by faithfulness (ʾĕmûnâ): belongs to 103:3 (āmanū), not to the loss verdict.')
rej('WLC:Hag.1.6', 'Wages put into a bag with holes is a striking image of earnings that drain away, close to ¶6-7; rejected only because ¶6-7 already carry three blocks on capital that shrinks unnoticed.')
rej('WLC:Isa.28.17', 'Justice as line and righteousness as plummet sweeping away the refuge of lies is a measuring image for judgment; ¶14\'s refuge remark concerns the ʿaṣr root of 103:1 and the link would be forced.')
rej('WLC:Isa.40.7', 'Grass withering when the LORD\'s breath blows on it is a transience image; Ps 103:15 at ¶24 already carries it.')
rej('WLC:Isa.51.12', 'Isa 51:12 מֵאֱנוֹשׁ יָמוּת (ʾĕnôš who dies) attests ʾĕnôš in a frailty context; the point is carried by Ps 103:15 at ¶24. The wording flag is due to the prefixed form מֵאֱנוֹשׁ.')
rej('WLC:Isa.53.6', 'All we like sheep have gone astray: a universal-straying image fitting ¶4/¶14, but its Servant context (bearing the iniquity of all) introduces a theme the ayah does not raise; Ps 14:3 and Ps 119:176 are used instead.')
rej('WLC:Isa.55.2', '"Why weigh out silver for what is not bread, your labour for what does not satisfy?" is a striking market image of wasted capital; held back because ¶9 is at its five-block limit and ¶6 has the capital point.')
rej('WLC:Jer.15.18', 'אֲנוּשָׁה "incurable" wound is from ʾnš "be sick", which BDB separates from the root of ʾĕnôš. Jer 17:9 already carries this homonym with the self-knowledge point at ¶22.')
rej('WLC:Jer.17.11', 'The partridge hatching eggs it did not lay, like wealth gained unjustly that leaves him at mid-life, is apt for ¶10. Amos 8:5 gives the false-measure mechanism ¶10 describes, so this is held back as a repeat.')
rej('WLC:Job.12.15', 'יַעְצֹר בַּמַּיִם (he withholds the waters) shows ʿṣr "restrain"; not a sense of Arabic ʿaṣr used on this page (root_verdicts: no qualifying parallel).')
rej('WLC:Job.14.1', 'Man born of woman, few of days and full of trouble: a transience motif already carried by Ps 103:15 and Ps 90.')
rej('WLC:Job.14.6', 'Like a hireling his day: the hired-labourer image adds nothing beyond Job 14:5 (used at ¶12) and Ps 90 (¶9).')
rej('WLC:Job.27.16', 'יִצְבֹּר כֶּעָפָר כָּסֶף (heaps up silver like dust) uses Hebrew ṣbr "heap up", a false friend of Arabic ṣabr; the hoarding motif is carried by Ps 49 and Luke 12.')
rej('WLC:Job.34.19', 'God not favouring princes over the poor is an impartiality statement, not a loss or scale image.')
rej('WLC:Job.4.17', 'הַאֱנוֹשׁ מֵאֱלוֹהַ יִצְדָּק, can a mortal be righteous before God, attests ʾĕnôš (prefixed form, hence the wording flag) in a frailty context; Ps 103:15 and Ps 8:5 are used for the root instead.')
rej('WLC:Job.7.1', 'Job 7:1 לֶאֱנוֹשׁ (prefixed form; wording flag explained) "hard service for ʾĕnôš on earth, his days like a hireling\'s": a frailty and service image; the ʾĕnôš root is used through Ps 103:15 and Ps 8:5.')
rej('WLC:Job.7.17', 'מָה־אֱנוֹשׁ כִּי תְגַדְּלֶנּוּ is Job\'s bitter parody of Ps 8:5. The root point is made with Ps 8:5-6, where ḥsr also appears, so this is a context-level repeat.')
rej('WLC:Job.7.18', 'Being visited every morning and tested every moment is a testing motif; ¶22\'s nabtalīhi (76:2) is close, but Jer 17:9-10 already covers God reading the person.')
rej('WLC:Job.7.2', 'The servant longing for shade and the hireling for his wages: a labour image not tied to the page\'s capital or scale argument.')
rej('WLC:Job.7.3', 'Months of emptiness and nights of ʿāmāl are allotted to him. This attests ʿāmāl "trouble", but the ʿml root is used at ¶9 through Eccl 1:3 and 2:11.')
rej('WLC:Lev.19.17', 'Rebuke your neighbour so as not to bear sin because of him belongs to mutual counsel (103:3); not developed on this page.')
rej('WLC:Mic.6.10', 'Treasures of wickedness and the scant ephah: strong on false measure, but it repeats Amos 8:5 (¶10) and Deut 25:13-15 (¶11).')
rej('WLC:Mic.6.11', '"Shall I acquit wicked scales and a bag of deceitful weights?" repeats the false-weights point already carried by Amos 8:5 and Deut 25:13-15.')
rej('WLC:Prov.10.2', 'Treasures of wickedness do not profit; righteousness delivers from death. A profit/no-profit maxim already covered by Ps 49 and Luke 12 at ¶9.')
rej('WLC:Prov.11.14', 'A people falls without counsel and is saved by many counsellors fits mutual counsel (103:3), not this page.')
rej('WLC:Prov.11.24', 'Prov 11:24 (withholding leads only to maḥsôr, want; the wording flag is the prefixed form לְמַחְסוֹר) is a generosity paradox; Prov 28:22 makes the ḥsr point with unawareness, which is what ¶7 needs.')
rej('WLC:Prov.11.4', 'Wealth does not profit on the day of wrath: a sound maxim, but it repeats the ¶9 point already made by Ps 49 and Luke 12.')
rej('WLC:Prov.12.15', 'The fool\'s way is right in his own eyes: the same point as Prov 16:2/21:2 used at ¶15.')
rej('WLC:Prov.13.11', 'Wealth from vanity dwindles: a general maxim adding nothing specific.')
rej('WLC:Prov.13.7', 'One pretends to be rich yet has nothing: close to ¶7, but Rev 3:17 at ¶7 adds the not-knowing element that this verse lacks.')
rej('WLC:Prov.22.2', 'Rich and poor meet, the LORD made them all: a common-humanity maxim; ¶4\'s species-wide verdict is carried by Ps 14:3.')
rej('WLC:Prov.23.4', 'Do not toil to become rich: a warning that adds nothing beyond ¶9\'s accepted texts.')
rej('WLC:Prov.23.5', 'Riches that make themselves wings and fly away (ketiv/qere variants in the verse): a vivid image of vanishing wealth, held back as a repeat of ¶9\'s point.')
rej('WLC:Prov.27.17', 'Iron sharpens iron, one man sharpens another: mutual formation fits 103:3, while ¶23 is served by Prov 27:19 from the same chapter.')
rej('WLC:Prov.27.6', 'Faithful are the wounds of a friend: concerns honest rebuke (103:3 mutual counsel), not this page.')
rej('WLC:Prov.28.27', 'Prov 28:27 (whoever gives to the poor will not lack, ʾên maḥsôr) is a generosity promise; ḥsr is used here only in the plain sense of want. Prov 28:22 serves ¶7.')
rej('WLC:Prov.6.32', 'The adulterer is ḥăsar-lēb ("lacking sense") and destroys himself: ḥsr plus self-destruction, but the sexual-ethics context would distract; Dan 5:27 and Prov 28:22 carry the root.')
rej('WLC:Ps.1.3', 'The tree planted by streams that prospers is the positive pole (103:3); the page uses Ps 1:6 only for the perishing way.')
rej('WLC:Ps.1.4', 'The wicked as chaff driven by wind is near 2:266\'s wind-burned produce (¶14), but ¶14 already has two blocks and Ps 1:6 from the same psalm is used.')
rej('WLC:Ps.103.16', 'The wind passes and he is gone, his place knows him no more: continuation of Ps 103:15 (accepted at ¶24); context only.')
rej('WLC:Ps.106.30', 'וַתֵּעָצַר הַמַּגֵּפָה (the plague was stayed) shows ʿṣr "restrain". The reader\'s wording flag is due to the niphal prefix. Not a sense used on this page (root_verdicts: no qualifying parallel).')
rej('WLC:Ps.23.2', 'Wrong verse: the reader\'s לֹא אֶחְסָר ("I shall not want") is in Ps 23:1, not 23:2 (green pastures, still waters), and the wording review found it only in the neighbouring verse. Even at 23:1 the plain sense of lack adds nothing beyond Eccl 1:15 and Gen 8:3,5.')
rej('WLC:Ps.39.7', 'יִצְבֹּר וְלֹא־יֵדַע מִי־אֹסְפָם (heaps up, not knowing who will gather) is a strong hoarding image using ṣbr, a false friend of ṣabr; ¶9 is at its limit and Ps 49 makes the point.')
rej('WLC:Ps.49.13', 'Man in honour does not abide and is like the beasts: the refrain of Ps 49, adding nothing beyond 49:12 and 49:18 used at ¶9.')
rej('WLC:Ps.90.3', 'You return ʾĕnôš to dust: mortality; Ps 90:10,12 are used at ¶9 and Ps 103:15 carries ʾĕnôš frailty at ¶24.')
rej('WLC:Ps.90.11', 'The reader located ʿāmāl in Ps 90:11, but the opened verse ("who knows the power of your anger") does not contain it. ʿāmāl is in Ps 90:10 (WLC numbering equals English here), which is used in TEV-MTF-006. Rejected on textual grounds for this locator.')

out = []
for row in rows:
    ref = row['ref']
    ev_items = json.loads(row['evidence'])
    multi = len({e['connection_id'] for e in ev_items}) > 1
    st, reason, aids = S[ref]
    for e in ev_items:
        cid = e['connection_id']
        txt = reason
        if multi:
            txt = f"[{e['kind']}: {e['basis']}] " + reason
        loc = ref if ref.startswith(('WLC:', 'SBLGNT:')) else SEF.get(ref)
        evidence = []
        if st != U and loc:
            evidence.append(loc)
        for a in aids:
            for l in locs(a):
                if l not in evidence:
                    evidence.append(l)
        paras = sorted({para(a) for a in aids})
        out.append(dict(connection_id=cid, ref=ref, status=st, reason=txt, paragraphs=paras, evidence=evidence, annotations=aids))

# research verdicts
RS = []
def res(ref, st, reason, *aids, extra=()):
    evidence = [] if st == U else [ref]
    for l in extra:
        if l not in evidence: evidence.append(l)
    for a in aids:
        for l in locs(a):
            if l not in evidence: evidence.append(l)
    RS.append(dict(connection_id=None, origin='research', ref=ref, status=st, reason=reason,
                   paragraphs=sorted({para(a) for a in aids}), evidence=evidence, annotations=list(aids)))
res('SBLGNT:Luke.9.24', A, 'Opened because Corpus Coranicum\'s note on 103:2 cites Luke 9:24 (after Torrey) for the Peshitta rendering of apollymi by ḥsar; the Greek apolesei autēn is quoted in the ¶8 soydas block.', 'S103-INC-SYD-001')
res('CORPUSCORANICUM:103:2:anmerkung', A, 'Corpus Coranicum note on 103:2: Torrey 1892 on the eschatological "loss" of Luke 9:24 and the Peshitta ḥsar, and Phil 3:7-8 (TUK 179); the basis of the ¶8 soydas block, reported as the editors\' view.', 'S103-INC-SYD-001')
res('CORPUSCORANICUM-INTERTEXT:103:2:178', A, 'Corpus Coranicum intertext entry TUK 178 (Luke 9:23-27, dated c. 90 CE) with the editors\' note that the Peshitta uses ḥsar; supports the ¶8 paralel and soydas blocks.', 'S103-INC-PRL-001', 'S103-INC-SYD-001')
res('CORPUSCORANICUM-INTERTEXT:103:2:179', A, 'Corpus Coranicum intertext entry TUK 179 (Phil 3:1-10, c. 55-60 CE) noting Syriac ḥusrānā in vv. 7-8; supports the ¶8 soydas block.', 'S103-INC-SYD-001')
res('CORPUSCORANICUM:103:1-3:kommentar', R, 'Corpus Coranicum running commentary: Robinson\'s reading of ʿaṣr as the hour when merchants count takings, and the contrast with eschatological loss and with Q 104. Context for the market reading of ¶6-9, but it names no Jewish or Christian witness and belongs to the 103:1/surah pages.')
res('SBLGNT:Rom.3.10', A, 'Rom 3:10 introduces Paul\'s catena ("none righteous, not one") built from Ps 14; context for the ¶4 karsi_anlati block.', 'S103-INC-KRA-001')
res('SBLGNT:Rom.3.11', A, 'Rom 3:11 continues the Ps 14 catena (none who understands or seeks God); context for the ¶4 block.', 'S103-INC-KRA-001')
res('SBLGNT:Rom.3.12', A, 'Rom 3:12 renders Ps 14:3 in Greek: "all turned aside, together became worthless (ēchreōthēsan)"; quoted at ¶4 as the Christian reading of the tevrat verse.', 'S103-INC-KRA-001')
res('SBLGNT:Matt.7.22', A, 'Own search for 18:103-104 (those who think they do well): Matt 7:22 has many on that day listing their works in Jesus\' name; quoted at ¶15.', 'S103-INC-MTF-006')
res('SBLGNT:Matt.7.23', A, 'Matt 7:23 "I never knew you" is the verdict on self-assured workers; completes the ¶15 block.', 'S103-INC-MTF-006')
res('SBLGNT:Jas.1.6', A, 'Own search for 22:11 ("worship on an edge"): James 1:6 compares the doubter to a wind-tossed wave; context for the ¶17 block.', 'S103-INC-MTF-007')
res('SBLGNT:Jas.1.8', A, 'James 1:8 "a double-souled man, unstable in all his ways" is quoted at ¶17 as the closest NT image of half-hearted worship that loses both sides.', 'S103-INC-MTF-007')
res('SBLGNT:Gal.4.1', A, 'Opened with Gal 4:2 (discovery). Gal 4:1 states that the heir, while a minor, differs nothing from a slave though lord of all; quoted at ¶21 beside 4:6.', 'S103-INC-MTF-009')
res('WLC:Gen.8.3', A, 'Own search of the ḥsr root (hebrew.py): Gen 8:3 וַיַּחְסְרוּ הַמָּיִם, the waters decreased, is the most concrete "decrease" use, matching ¶5\'s image of loss as diminishing.', 'S103-TEV-SYD-003')
res('WLC:Gen.8.5', A, 'Gen 8:5 הָלוֹךְ וְחָסוֹר (went on decreasing) gives the gradual diminishing; quoted at ¶5.', 'S103-TEV-SYD-003')
res('WLC:Ps.8.6', A, 'Own search of the ḥsr root: Ps 8:6 וַתְּחַסְּרֵהוּ מְּעַט מֵאֱלֹהִים stands next to ʾĕnôš in 8:5, so both roots of 103:2 appear in an exalting sense; used at ¶3.', 'S103-TEV-SYD-002')
res('WLC:Ps.49.12', A, 'Opened with the discovered Ps 49:18: 49:12 gives the hoarders\' inner thought that their houses are forever (MT qirbām; ancient versions\' reading not checkable here), set beside 104:3 at ¶9.', 'S103-TEV-MTF-005')
res('WLC:Ps.49.17', A, 'Ps 49:17 (do not fear when a man grows rich) is context for 49:18; cited in the ¶9 block.', 'S103-TEV-MTF-005')
res('WLC:1Kgs.18.21', A, 'Own search for 22:11 (worship on an edge): Elijah\'s "how long will you limp between two branches?" is the Hebrew Bible\'s image of wavering between two sides; quoted at ¶17.', 'S103-TEV-MTF-014')
res('WLC:Ps.119.176', A, 'Own search for ¶14 (khusr as both straying and perishing): Ps 119:176 תָּעִיתִי כְּשֶׂה אֹבֵד shows ʾbd for the lost sheep that strays; quoted with Ps 1:6.', 'S103-TEV-MTF-012')
res('WLC:Deut.32.10', A, 'Own search for ¶23 (insān al-ʿayn): Deut 32:10 כְּאִישׁוֹן עֵינוֹ; hebrew.py word gives ʾîšôn, "the little man of the eye" (Strong). Quoted in the ¶23 soydas block.', 'S103-TEV-SYD-008')
res('WLC:Ps.17.8', A, 'Ps 17:8 כְּאִישׁוֹן בַּת־עָיִן is the second ʾîšôn attestation, quoted at ¶23.', 'S103-TEV-SYD-008')
res('WLC:Prov.7.2', A, 'Prov 7:2 (keep my teaching as the ʾîšôn of your eyes) is the third ʾîšôn attestation, cited in the ¶23 block.', 'S103-TEV-SYD-008')
res('SEFARIA:Pirkei_Avot.2.1', A, 'Resolved text of discovery ref Mishnah Avot 2:1; quoted at ¶6.', 'S103-TEV-MTF-003')
res('SEFARIA:Pirkei_Avot.3.16', A, 'Resolved text of discovery ref Mishnah Avot 3:16; quoted at ¶7.', 'S103-TEV-MTF-004')
res('SEFARIA:Shabbat.31a', A, 'Resolved text of discovery ref Shabbat 31a (full segment opened); Rava\'s first question at judgment quoted at ¶11.', 'S103-TEV-YGL-001')
res('SEFARIA:Kiddushin.40b', A, 'Resolved text of discovery ref Kiddushin 40b (first 1,500 characters opened, containing the cited baraita); quoted at ¶13.', 'S103-TEV-YGL-002')
res('SEFARIA:Pirkei_Avot.1.14', A, 'Resolved text of discovery ref Mishnah Avot 1:14; quoted at ¶25.', 'S103-TEV-MTF-018')
res('SEFARIA:Taanit.23a', A, 'Resolved text of discovery ref Ta\'anit 23a (full segment opened, including the Ḥoni story and Rava\'s proverb); quoted at ¶25.', 'S103-TEV-MTF-019')
for loc, why in [
    ('SEFARIA:Pirkei_Avot.1.6', 'Mishnah Avot 1:6'), ('SEFARIA:Pirkei_Avot.2.15', 'Mishnah Avot 2:15'),
    ('SEFARIA:Pirkei_Avot.2.16', 'Mishnah Avot 2:16'), ('SEFARIA:Pirkei_Avot.2.4', 'Mishnah Avot 2:4'),
    ('SEFARIA:Pirkei_Avot.3.1', 'Mishnah Avot 3:1'), ('SEFARIA:Pirkei_Avot.3.15', 'Mishnah Avot 3:15'),
    ('SEFARIA:Pirkei_Avot.4.1', 'Mishnah Avot 4:1'), ('SEFARIA:Pirkei_Avot.4.16', 'Mishnah Avot 4:16'),
    ('SEFARIA:Pirkei_Avot.4.17', 'Mishnah Avot 4:17'), ('SEFARIA:Pirkei_Avot.4.22', 'Mishnah Avot 4:22'),
    ('SEFARIA:Rosh_Hashanah.16b', 'Rosh Hashanah 16b'), ('SEFARIA:Shabbat.153a', 'Shabbat 153a'),
    ('SEFARIA:The_Wisdom_of_Solomon.5.8', 'Wisdom of Solomon 5:8')]:
    res(loc, R, f'Resolved text of discovery ref {why}, opened and read; rejected for the reason given in that connection\'s verdict (no independent addition to this page).')
res('SEFARIA:Ben_Sira.11.19', R, 'Resolved text of discovery ref Sirach 11:19. The opened Hebrew segment (folly and darkness created for sinners) does not contain the proposed rich-man saying; numbering mismatch recorded in gaps.json.')
res('SEFARIA:Ben_Sira.11.18', U, 'Looked up to find the rich-man saying under a neighbouring number; NOT FOUND in the corpus (recorded in gaps.json not_found).')

for o in out + RS:
    print(json.dumps(o, ensure_ascii=False))
missing = [r['ref'] for r in rows if r['ref'] not in S]
print('MISSING', missing, file=sys.stderr)
print('COUNT', len(out), len(RS), file=sys.stderr)
