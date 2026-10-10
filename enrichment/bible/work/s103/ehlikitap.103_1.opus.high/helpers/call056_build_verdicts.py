import csv, json, sys
csv.field_size_limit(10**9)
CALL = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_1.opus.high/'
DISC = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/'

ann = {}
for line in open(CALL + 'annotations.jsonl'):
    r = json.loads(line)
    ann[r['id']] = r

def local_sources(aid):
    k = ann[aid]['kaynak']
    return [x for x in k.split('|') if x != 'hafiza']

A = 'accepted'; R = 'rejected'; U = 'unresolved'; N = 'unavailable'
P = 'S103-'

# ref -> (status, paragraphs, annotations, reason)
D = {
 'Didache 1:5': (U, [14], [P+'INC-MTF-010'], 'Didache 1:5 (give to who asks, do not ask back) matches the base gift-reclaiming sense in para 14, but the Didache is not in the intertext corpus (prefetch gap); the saying is reported from memory in a degerlendirilmedi block.'),
 'Didache 4:5': (U, [14], [P+'INC-MTF-010'], 'Didache 4:5 (hands stretched to receive, drawn back from giving) is the closest Christian formulation of the para 14 grasp image, but the text is not in the corpus; reported from memory only.'),
 'Didache 8:3': (N, [], [], 'Didache 8:3 (Lord\'s Prayer thrice daily) is not in the intertext corpus (prefetch gap); the prayer-time point of para 2 is carried by Acts 3:1 and Psalm 55:18, which are verifiable.'),
 'Gregory of Tours, Glory of the Martyrs 1.95': (U, [19], [P+'INC-PRL-001'], 'Seven Sleepers of Ephesus are the direct Christian parallel to the cave youths of para 19, but Gregory of Tours is not in the corpus (prefetch gap); the parallel is given from memory, marked degerlendirilmedi.'),
 'Gregory of Tours, Glory of the Martyrs 94': (U, [19], [P+'INC-PRL-001'], 'Same Seven Sleepers parallel under a different chapter reference; the witness is not in the corpus and the chapter number cannot be checked; memory-only block.'),
 'Protevangelium of James 8': (N, [], [], 'Protevangelium of James is not in the corpus (prefetch gap). Its motive (Mary removed from the temple at twelve lest she defile it) is a purity rationale, opposite to the protective seclusion of para 15; not verifiable here.'),
 'SBLGNT:1Cor.15.52': (R, [], [], 'Opened: transformation in the twinkling of an eye at the last trumpet. The base mentions the momentary sense of asr only lexically (para 5); a resurrection instant adds no specific point to any paragraph.'),
 'SBLGNT:1Cor.7.29': (A, [10], [P+'INC-MTF-008'], 'Opened: ho kairos synestalmenos, time drawn together/compressed; gives a Greek image of time as pressure for para 10.'),
 'SBLGNT:1Pet.1.24': (R, [], [], 'Opened: all flesh as grass that withers (quoting Isaiah 40). The same morning-evening withering image is given from its Hebrew source, Psalm 90:6, at para 6; no distinct addition.'),
 'SBLGNT:1Tim.6.18': (R, [], [], 'Opened: rich in good works, generous. Generic exhortation; Deuteronomy 15:7-8 and Luke 6:38 carry the hand/pressed-measure image the base develops.'),
 'SBLGNT:1Tim.6.19': (R, [], [], 'Opened: storing a good foundation for the future. Generic treasure motif without the base\'s pressing, holding or time images.'),
 'SBLGNT:2Cor.2.14': (A, [22], [P+'INC-MTF-016'], 'Opened: the fragrance of knowledge made manifest everywhere; with 2:15 it gives the trace-of-scent image of para 22.'),
 'SBLGNT:2Cor.2.15': (A, [22], [P+'INC-MTF-016'], 'Opened: Christou euodia among those being saved and those perishing; scent left by persons, framed by the saved/lost division close to 103:2-3.'),
 'SBLGNT:2Cor.4.17': (A, [18], [P+'INC-MTF-013'], 'Opened: momentary light affliction producing an eternal weight; cited with 4:8 for pressure that yields a product (para 18).'),
 'SBLGNT:2Cor.4.8': (A, [18], [P+'INC-MTF-013'], 'Opened: thlibomenoi all ou stenokhoroumenoi; pressed but not hemmed in, the pressure/refuge distinction of para 18.'),
 'SBLGNT:2Cor.9.10': (R, [], [], 'Opened: seed to the sower and bread for food; Paul echoes Isaiah 55:10, which is given at para 8 in Hebrew; no independent addition.'),
 'SBLGNT:2Cor.9.11': (R, [], [], 'Opened: enriched for generosity producing thanksgiving; generic, no link to the base images.'),
 'SBLGNT:2Cor.9.6': (R, [], [], 'Opened: sowing sparingly, reaping sparingly. Generic giving maxim; Proverbs 11:24-25 at para 16 makes the same point closer to the withheld-produce scene.'),
 'SBLGNT:2Pet.3.8': (A, [6], [P+'INC-YGL-001'], 'Opened: one day with the Lord as a thousand years; Christian application of Psalm 90:4 to the delay of the end, given as yorum_gelenegi at para 6.'),
 'SBLGNT:2Pet.3.9': (A, [6], [P+'INC-YGL-001'], 'Opened: the Lord is not slow but patient, wishing all to reach repentance; delay read as time given for repentance (para 6).'),
 'SBLGNT:2Tim.4.6': (R, [], [], 'Opened: being poured out as a libation as departure nears. Sacrificial libation, not pressing or the evening of life as the base frames it; no specific addition.'),
 'SBLGNT:Acts.10.3': (A, [2], [P+'INC-MTF-003'], 'Opened: Cornelius sees the vision about the ninth hour of the day; supports the afternoon hour of prayer at para 2.'),
 'SBLGNT:Acts.10.4': (R, [], [], 'Opened: prayers and alms rose as a memorial. Context for 10:3; no time-of-day point of its own.'),
 'SBLGNT:Acts.3.1': (A, [2], [P+'INC-MTF-003'], 'Opened: Peter and John go up at the hour of prayer, the ninth; an afternoon prayer hour named by the time, beside salat al-asr in para 2.'),
 'SBLGNT:Eph.5.16': (R, [], [], 'Opened: redeeming the time because the days are evil. General; Hebrews 3:13 and 1 Corinthians 7:29 carry the time points more specifically.'),
 'SBLGNT:Eph.6.16': (R, [], [], 'Opened: shield of faith quenching flaming arrows. The base names armour (measir) only lexically in para 17; a faith-armour allegory imports a point the base does not make.'),
 'SBLGNT:Gal.6.10': (R, [], [], 'Opened: do good while we have opportunity. Overlaps John 9:4 (para 5) and Hebrews 3:13 (para 6).'),
 'SBLGNT:Gal.6.9': (R, [], [], 'Opened: we will reap in due season if we do not give up. Generic perseverance; the waiting-and-harvest point of paras 12-13 is carried by the Joseph texts.'),
 'SBLGNT:Heb.10.25': (R, [], [], 'Opened: encouraging one another as the Day draws near. Overlaps Hebrews 3:13, which is accepted at para 6.'),
 'SBLGNT:Heb.11.38': (R, [], [], 'Opened: the faithful wandering in deserts, mountains and caves. Caves as places of the persecuted, without the refuge-sleep-time scene of para 19.'),
 'SBLGNT:Heb.3.11': (R, [], [], 'Opened: God swore in wrath that they shall not enter his rest. A divine oath of exclusion; para 1 concerns an oath by a time, not this formula.'),
 'SBLGNT:Heb.3.13': (A, [6], [P+'INC-MTF-005'], 'Opened: exhort one another every day as long as it is called Today; time given and mutual counsel side by side (para 6, 103:1-3).'),
 'SBLGNT:Heb.3.18': (R, [], [], 'Opened: the oath concerned the disobedient. Context of the rest-oath; no addition to this page.'),
 'SBLGNT:Heb.3.19': (R, [], [], 'Opened: unbelief prevented entry. Context only.'),
 'SBLGNT:Heb.4.3': (R, [], [], 'Opened: believers enter the rest. Context of the rest argument; no paragraph of this page treats it.'),
 'SBLGNT:Heb.4.7': (A, [6], [P+'INC-MTF-005'], 'Opened: God again sets a certain day, Today; cited with 3:13 for the present as allotted time (para 6).'),
 'SBLGNT:Heb.6.18': (A, [18], [P+'INC-MTF-012'], 'Opened: hoi katafygontes kratesai; those who fled for refuge to seize the hope; refuge as gripping (para 18).'),
 'SBLGNT:Heb.6.7': (A, [21], [P+'INC-MTF-014'], 'Opened: land that drinks rain and yields useful plants receives blessing; first half of a sequence comparable to 2:264-266 (para 21).'),
 'SBLGNT:Heb.6.8': (A, [21], [P+'INC-MTF-014'], 'Opened: land bearing thorns ends in burning; the burned-land end of the same comparison (para 21).'),
 'SBLGNT:Jas.1.3': (R, [], [], 'Opened: testing of faith produces endurance. Concerns sabr of 103:3, not a paragraph of this 103:1 page.'),
 'SBLGNT:Jas.4.13': (A, [16], [P+'INC-MTF-011'], 'Opened: today or tomorrow we will trade a year and gain; the unconditioned plan rebuked, beside the unconditioned oath of 68:17-18 (para 16).'),
 'SBLGNT:Jas.4.14': (A, [16], [P+'INC-MTF-011'], 'Opened: you do not know tomorrow; life is a vapour; part of the same rebuke used at para 16.'),
 'SBLGNT:Jas.5.2': (R, [], [], 'Opened: riches rotted. Overlaps Luke 12:18-21 accepted at para 22.'),
 'SBLGNT:Jas.5.3': (R, [], [], 'Opened: corroded gold as witness in the last days. Overlap with Luke 12; no distinct point.'),
 'SBLGNT:Jas.5.4': (R, [], [], 'Opened: withheld wages of reapers cry out. Para 16 concerns exclusion of the poor from a harvest, which Deuteronomy 24:19-21 addresses more directly; overlap.'),
 'SBLGNT:Jas.5.5': (R, [], [], 'Opened: luxury in a day of slaughter. No paragraph of the page develops it.'),
 'SBLGNT:Jas.5.7': (R, [], [], 'Opened: the farmer waits patiently for early and late rain. Patience belongs to 103:3; the waiting of paras 12-13 is carried by the Joseph texts.'),
 'SBLGNT:John.11.9': (R, [], [], 'Opened: twelve hours of daylight. Overlaps John 9:4, accepted at para 5.'),
 'SBLGNT:John.12.24': (R, [], [], 'Opened: a grain must die to bear fruit. The base (para 12) keeps grain protected in its husk; death of the seed is a different image.'),
 'SBLGNT:John.12.3': (R, [], [], 'Opened: the house filled with the scent of the ointment. Para 20 describes scent rising behind a passer-by; 2 Corinthians 2:14-15 carries the scent-trace point better; no distinct addition.'),
 'SBLGNT:John.15.2': (R, [], [], 'Opened: fruitless branch removed, fruitful pruned. No base image of pruning.'),
 'SBLGNT:John.15.6': (R, [], [], 'Opened: withered branch thrown into fire. Overlaps Hebrews 6:8 and Ezekiel 19:12 at para 21.'),
 'SBLGNT:John.15.8': (R, [], [], 'Opened: bearing much fruit as discipleship. No paragraph link.'),
 'SBLGNT:John.9.4': (A, [5], [P+'INC-MTF-004'], 'Opened: night comes when no one can work; the late-hour urgency of para 5.'),
 'SBLGNT:Luke.12.18': (A, [22], [P+'INC-MTF-015'], 'Opened: tearing down barns to build bigger ones; the stored harvest of the rich fool, used at para 22.'),
 'SBLGNT:Luke.12.19': (A, [22], [P+'INC-MTF-015'], 'Opened: goods laid up for many years; part of the same parable at para 22.'),
 'SBLGNT:Luke.12.20': (A, [22], [P+'INC-MTF-015'], 'Opened: this night your soul is required; whose will your preparations be; accumulation lost when the time ends (para 22).'),
 'SBLGNT:Luke.12.21': (A, [22], [P+'INC-MTF-015'], 'Opened: storing for oneself and not rich toward God; the parable\'s own conclusion, cited at para 22.'),
 'SBLGNT:Luke.13.25': (R, [], [], 'Opened: the householder shuts the door on late knockers. Overlaps John 9:4 for lateness at para 5.'),
 'SBLGNT:Luke.13.7': (R, [], [], 'Opened: three years seeking fruit on the fig tree. No base image of reprieve.'),
 'SBLGNT:Luke.13.8': (R, [], [], 'Opened: leave it one more year. A reprieve for a fruitless tree, not the relief year of 12:49; no specific addition.'),
 'SBLGNT:Luke.13.9': (R, [], [], 'Opened: fruit or cutting. Context of 13:6-8.'),
 'SBLGNT:Luke.16.24': (A, [9], [P+'INC-MTF-007'], 'Opened: send Lazarus to cool my tongue; a parched tongue without the saving sip (para 9).'),
 'SBLGNT:Luke.16.25': (A, [9], [P+'INC-MTF-007'], 'Opened: you received your good things in your lifetime; Abraham\'s answer, part of the scene used at para 9.'),
 'SBLGNT:Luke.16.26': (A, [9], [P+'INC-MTF-007'], 'Opened: a great chasm is fixed; the relief is impossible (para 9).'),
 'SBLGNT:Luke.16.9': (R, [], [], 'Opened: make friends by unrighteous mammon. No paragraph link.'),
 'SBLGNT:Luke.19.13': (R, [], [], 'Opened: trade until I come. Commercial parable; the base does not develop trade.'),
 'SBLGNT:Luke.6.38': (A, [8], [P+'INC-MTF-006'], 'Opened: metron kalon pepiesmenon, a pressed-down measure overflowing as the return for giving; pressing as image of gift (para 8).'),
 'SBLGNT:Mark.11.20': (R, [], [], 'Opened: fig tree withered from the roots. Para 9 concerns a parched tongue; no specific link.'),
 'SBLGNT:Mark.13.35': (R, [], [], 'Opened: evening, midnight, cockcrow, morning watches. Generic time divisions; no addition to para 2 or 4.'),
 'SBLGNT:Mark.14.9': (R, [], [], 'Opened: the woman\'s deed told in her memory. The good-name trace of para 22 is carried by Ecclesiastes 7:1 and 2 Corinthians 2:15.'),
 'SBLGNT:Matt.20.12': (A, [1], [P+'INC-MTF-002'], 'Opened: these last worked one hour and you made them equal; the evening reckoning without loss for latecomers (para 1).'),
 'SBLGNT:Matt.20.6': (A, [1], [P+'INC-MTF-002'], 'Opened: about the eleventh hour he found others standing; the late workers of the parable used at para 1.'),
 'SBLGNT:Matt.20.8': (A, [1], [P+'INC-MTF-002'], 'Opened: opsias de genomenes, when evening came, wages paid; evening as time of accounting beside Robinson\'s market-end reading (para 1).'),
 'SBLGNT:Matt.20.9': (A, [1], [P+'INC-MTF-002'], 'Opened: the eleventh-hour workers each received a denarius; the contrast (no loss for the late) is the point of the block (para 1).'),
 'SBLGNT:Matt.21.34': (R, [], [], 'Opened: the season of fruit and servants sent to collect. The tenant parable is about rejected messengers; Isaiah 5 carries the vineyard point at para 16.'),
 'SBLGNT:Matt.21.41': (R, [], [], 'Opened: vineyard given to other tenants. Same parable; no distinct addition.'),
 'SBLGNT:Matt.25.10': (R, [], [], 'Opened: the door was shut. Lateness is carried by John 9:4 at para 5; no distinct point.'),
 'SBLGNT:Matt.25.13': (R, [], [], 'Opened: you know neither the day nor the hour. Generic watchfulness.'),
 'SBLGNT:Matt.25.27': (R, [], [], 'Opened: money with interest. Commercial parable not developed by the base.'),
 'SBLGNT:Matt.25.29': (R, [], [], 'Opened: from the one who has not, even what he has is taken. No paragraph link.'),
 'SBLGNT:Matt.25.5': (R, [], [], 'Opened: the bridegroom delayed and all slept. Sleep during delay, not the cave refuge and long sleep of para 19.'),
 'SBLGNT:Matt.6.19': (R, [], [], 'Opened: treasures on earth destroyed. Overlaps Luke 12:18-21 at para 22.'),
 'SBLGNT:Matt.6.20': (R, [], [], 'Opened: treasures in heaven. Generic counterpart; no addition.'),
 'SBLGNT:Phil.4.18': (R, [], [], 'Opened: the gift as a fragrant offering. Joins gift and scent but the base keeps them in different paragraphs; 2 Corinthians 2:15 carries the scent trace.'),
 'SBLGNT:Rev.10.6': (A, [1], [P+'INC-MTF-001'], 'Opened: the angel swears by the one who lives forever that there will be no more time/delay; an oath about time contrasted with an oath by time (para 1).'),
 'SBLGNT:Rev.14.19': (A, [10], [P+'INC-MTF-009'], 'Opened: the vintage of the earth thrown into the great winepress of God\'s wrath; pressing as end-time judgment (para 10).'),
 'SBLGNT:Rev.14.20': (A, [10], [P+'INC-MTF-009'], 'Opened: blood flowed from the winepress; the same scene (para 10).'),
 'SBLGNT:Rev.14.7': (A, [10], [P+'INC-MTF-009'], 'Opened: the hour of his judgment has come; frames the winepress scene in time (para 10).'),
 'SBLGNT:Rev.18.17': (R, [], [], 'Opened: such wealth laid waste in one hour. Overlaps Luke 12:20 and Job 1:19 for sudden loss.'),
 'SBLGNT:Rev.6.15': (R, [], [], 'Opened: kings hide in caves and rocks. Echoes Isaiah 2:19, which is given at para 19 from the Hebrew; no distinct addition.'),
 'SBLGNT:Rev.6.16': (R, [], [], 'Opened: fall on us and hide us. Same scene as 6:15; context.'),
 'Tertullian, On Prayer 25': (N, [], [], 'Tertullian is not in the corpus (prefetch gap); the third, sixth and ninth hours are attested in Acts 3:1 and 10:3, used at para 2.'),
 '1 Maccabees 2:31': (N, [], [], '1 Maccabees is not in the corpus (prefetch gap); hiding places in the wilderness cannot be checked.'),
 '1 Maccabees 2:38': (N, [], [], '1 Maccabees is not in the corpus (prefetch gap); the failed Sabbath refuge cannot be checked.'),
 'Babylonian Talmud, Berakhot 26b': (A, [4], [P+'TEV-YGL-002'], 'Resolved as SEFARIA:Berakhot.26b and opened: Isaac instituted minha from Genesis 24:63; minha until evening because of the tamid between the evenings (para 4).'),
 "Babylonian Talmud, Ta'anit 23a": (A, [19], [P+'TEV-MTF-024'], 'Resolved as SEFARIA:Taanit.23a and opened: Honi sleeps seventy years hidden by a rock formation and is not recognised on waking (para 19).'),
 'Berakhot 26b': (A, [4], [P+'TEV-YGL-002'], 'SEFARIA:Berakhot.26b opened: the patriarchs and the daily offerings as origins of the three prayers; afternoon prayer tied to the late-day offering (para 4).'),
 'Genesis Rabbah 89:1': (A, [13], [P+'TEV-YGL-004'], 'SEFARIA:Bereshit_Rabbah.89.1 opened: God set a time for Joseph\'s years in the darkness of prison; an appointed end to waiting (para 13).'),
 'Genesis Rabbah 89:3': (A, [12], [P+'TEV-YGL-003'], 'SEFARIA:Bereshit_Rabbah.89.3 opened: two years added because Joseph asked the cupbearer to remember him; the forgetting scene beside Q 12:42 (para 12).'),
 'Mishnah Avot 2:15': (A, [5], [P+'TEV-MTF-005'], 'SEFARIA:Pirkei_Avot.2.15 opened: the day is short, the work much, the master presses; time as pressure (para 5).'),
 'Mishnah Avot 2:16': (A, [5], [P+'TEV-MTF-005'], 'SEFARIA:Pirkei_Avot.2.16 opened: not yours to finish the work, nor free to desist; cited as the continuation at para 5.'),
 'Mishnah Avot 3:16': (R, [], [], 'SEFARIA:Pirkei_Avot.3.16 opened: open shop, open ledger, collectors. An accounting image the base does not develop on this page.'),
 'Mishnah Avot 4:16': (A, [6], [P+'TEV-MTF-008'], 'SEFARIA:Pirkei_Avot.4.16 opened: this world as a vestibule; frames lifetime as preparation (para 6).'),
 'Mishnah Avot 4:17': (A, [6], [P+'TEV-MTF-008'], 'SEFARIA:Pirkei_Avot.4.17 opened: one hour of repentance and good deeds in this world; value of allotted time (para 6).'),
 'Mishnah Avot 5:10': (R, [], [], 'SEFARIA:Pirkei_Avot.5.10 opened: mine is mine types. Deuteronomy 15:7-8 gives the closed/open hand of para 14 more directly.'),
 'Mishnah Berakhot 4:1': (A, [2], [P+'TEV-YGL-001'], 'SEFARIA:Mishnah_Berakhot.4.1 opened: minha until evening, R. Judah until plag ha-minha; the afternoon prayer bounded by the end of day (para 2).'),
 'Sirach 4:31': (U, [14], [P+'TEV-MTF-016'], 'SEFARIA:Ben_Sira.4.31 opened: this Hebrew text has a different saying (be not boastful with the tongue); the Greek hand-saying is not in the corpus. Reported from memory, unverified.'),
 'Tobit 4:7': (N, [], [], 'SEFARIA:Book_of_Tobit.4.7 opened: this Hebrew version at 4:7 concerns money left with Gabael, not almsgiving; the Greek witness the reader meant is not in the corpus.'),
 'Tobit 4:9': (N, [], [], 'Tobit 4:9 is not in the corpus (prefetch gap).'),
 'WLC:1Kgs.17.13': (R, [], [], 'Opened: Elijah asks for the first cake. Widow\'s generosity is not developed by the base.'),
 'WLC:1Kgs.17.16': (R, [], [], 'Opened: flour and oil did not fail. No paragraph link.'),
 'WLC:1Kgs.18.44': (R, [], [], 'Opened: a small cloud; and lo yaatsrekha ha-geshem (lest the rain detain you), a restraint use of the root; covered by the range in TEV-SYD-005; the cloud motif adds nothing beyond Isaiah 55:10.'),
 'WLC:1Kgs.18.45': (R, [], [], 'Opened: heavens black with clouds and wind, great rain. Context of 18:44.'),
 'WLC:1Kgs.19.9': (R, [], [], 'Opened: Elijah lodges in the cave. No sleep-time or refuge-prayer scene; Psalm 142 used at para 19.'),
 'WLC:1Kgs.21.3': (R, [], [], 'Opened: Naboth keeps his inheritance. Not the withholding of para 14.'),
 'WLC:1Kgs.8.35': (A, [8], [P+'TEV-SYD-001'], 'Opened: behe\'atser shamayim velo yihye matar; the heavens shut so there is no rain; the root form is the Niphal infinitive, which the wording check missed (para 8).'),
 'WLC:1Sam.21.8':(R, [], [], 'Opened: nesar lifney YHWH, detained before the LORD; restraint sense duplicated by Judges 13:15 in TEV-SYD-005.'),
 'WLC:2Chr.7.13': (A, [8], [P+'TEV-SYD-001'], 'Opened: hen eetsor ha-shamayim; shutting the heavens so there is no rain; the restraint use of the root opposite the pressed clouds (para 8).'),
 'WLC:2Kgs.4.24': (R, [], [], 'Opened: al taatsar li lirkov, do not hold back my riding; restraint sense duplicated by Judges 13:15.'),
 'WLC:2Kgs.4.4': (R, [], [], 'Opened: shut the door and pour the oil. No base image.'),
 'WLC:2Kgs.4.7': (R, [], [], 'Opened: sell the oil, pay the debt. No base image.'),
 'WLC:Amos.4.7': (R, [], [], 'Opened: rain withheld three months before harvest, with mana not atsar; overlaps Deuteronomy 11:17.'),
 'WLC:Amos.8.4': (R, [], [], 'Opened: those who trample the needy. Merchants\' scene is not developed on this page.'),
 'WLC:Amos.8.5': (R, [], [], 'Opened: when will the new moon pass that we may sell grain. Relevant to a market reading the base does not develop; not used.'),
 'WLC:Amos.8.6': (R, [], [], 'Opened: buying the poor for silver. Context of 8:5.'),
 'WLC:Amos.8.7': (R, [], [], 'Opened: the LORD swears by the pride of Jacob. An oath by something other than the divine name, but its object is unforgotten deeds; para 1 is better served by Daniel 12:7 and Matthew 5:34.'),
 'WLC:Amos.8.9': (R, [], [], 'Opened: the sun set at noon. Overlaps Jeremiah 6:4 at para 5.'),
 'WLC:Amos.9.13': (R, [], [], 'Opened: the treader of grapes overtakes the sower. Abundance image; no specific paragraph link.'),
 'WLC:Dan.12.12': (R, [], [], 'Opened: blessed is he who waits. Patience belongs to 103:3.'),
 'WLC:Dan.12.7': (A, [1], [P+'TEV-MTF-001'], 'Opened: vayyishava be-hey ha-olam ki le-moed moadim va-hetsi; an oath by the Ever-living about a measured time (para 1).'),
 'WLC:Dan.6.10': (A, [2], [P+'TEV-MTF-002'], 'Opened: WLC 6:10 is the king signing the decree; the three-times-daily prayer is WLC 6:11 (KJV 6:10), opened and cited at para 2.'),
 'WLC:Deut.11.17': (A, [8], [P+'TEV-SYD-001'], 'Opened: veatsar et ha-shamayim velo yihye matar; Hebrew atsar holds back rain, the opposite direction of the pressed clouds of para 8; sound correspondence only.'),
 'WLC:Deut.15.10': (A, [14], [P+'TEV-MTF-015'], 'Opened: give without a grudging heart; cited with 15:7-8 at para 14.'),
 'WLC:Deut.15.14': (R, [], [], 'Opened: furnish him from your threshing floor and winepress. Joins winepress and gift, but para 8 already carries gift-as-pressing with Luke 6:38; not added.'),
 'WLC:Deut.15.7': (A, [14], [P+'TEV-MTF-015'], 'Opened: lo tikpots et yadkha; do not shut your hand; the closed hand of para 14.'),
 'WLC:Deut.15.8': (A, [14], [P+'TEV-MTF-015'], 'Opened: patoah tiftah et yadkha; open your hand wide; the open hand of para 14.'),
 'WLC:Deut.24.13': (R, [], [], 'Opened: return the pledge at sunset. Not developed by the base.'),
 'WLC:Deut.24.15': (R, [], [], 'Opened: pay the wage before sunset. Overlaps Matthew 20:8 (evening reckoning) at para 1.'),
 'WLC:Deut.24.19': (A, [16], [P+'TEV-MTF-017'], 'Opened: the forgotten sheaf for stranger, orphan and widow; the share the garden owners of 68:24 shut out (para 16).'),
 'WLC:Deut.24.21': (A, [16], [P+'TEV-MTF-017'], 'Opened: do not glean the vineyard after you; same law (para 16).'),
 'WLC:Deut.32.1': (R, [], [], 'Opened: heaven and earth called to hear. A witness summons, not an oath by a created time; no addition to para 1.'),
 'WLC:Eccl.11.6': (R, [], [], 'Opened: sow in the morning and do not rest your hand in the evening. Two ends of the day are carried by Exodus 29:39 at para 4.'),
 'WLC:Eccl.12.1': (A, [22], [P+'TEV-MTF-032'], 'Opened: remember your Creator before the bad days; old age as the evening of life (para 22).'),
 'WLC:Eccl.12.2': (A, [22], [P+'TEV-MTF-032'], 'Opened: before sun and light darken and clouds return after rain; same block (para 22).'),
 'WLC:Eccl.7.1': (A, [22], [P+'TEV-MTF-031'], 'Opened: tov shem mi-shemen tov; good name and fragrant oil in one wordplay, with the day of death (para 22).'),
 'WLC:Eccl.8.8': (R, [], [], 'Opened: no one rules the wind or the day of death. Overlaps other wind/death texts used.'),
 'WLC:Eccl.9.10': (A, [6], [P+'TEV-MTF-007'], 'Opened: no work, reckoning, knowledge or wisdom in Sheol; the closed time of work beside 35:37 (para 6).'),
 'WLC:Exod.15.25': (R, [], [], 'Opened: bitter water made sweet. Bitterness (mara) is not the sabr juice of para 10, and the root differs.'),
 'WLC:Exod.16.20': (R, [], [], 'Opened: kept manna bred worms. Storage failing, not the husk-preservation of para 12; no addition.'),
 'WLC:Exod.16.24': (R, [], [], 'Opened: manna kept for the Sabbath did not spoil. Context of 16:20.'),
 'WLC:Exod.29.39': (A, [4], [P+'TEV-MTF-003'], 'Opened: one lamb in the morning, the other bein ha-arbayim; a Hebrew dual for the late-day interval beside the Arabic dual asran (para 4).'),
 'WLC:Ezek.19.12': (A, [21], [P+'TEV-MTF-029'], 'Opened: east wind dried its fruit, fire consumed it; vine, wind and fire as in 2:266 (para 21).'),
 'WLC:Ezek.19.14': (A, [21], [P+'TEV-MTF-029'], 'Opened: fire went out from its branches and devoured its fruit; this is a lament (para 21).'),
 'WLC:Gen.16.2': (R, [], [], 'Opened: atsarani YHWH mi-ledet; restraint of the womb; same sense as Genesis 20:18, which is cited in TEV-SYD-005.'),
 'WLC:Gen.20.18': (A, [14], [P+'TEV-SYD-005'], 'Opened: atsor atsar YHWH be-ad kol rehem; the root\'s restraint sense applied to the womb (para 14).'),
 'WLC:Gen.24.63': (A, [4], [P+'TEV-YGL-002'], 'Opened: lasuah ba-sadeh lifnot arev; the verse Berakhot 26b reads as Isaac\'s afternoon prayer (para 4).'),
 'WLC:Gen.40.11': (A, [11], [P+'TEV-PRL-001'], 'Opened: vaeshat otam el kos Paro; the cupbearer squeezes grapes into the cup with the hapax sahat, not atsar (para 11).'),
 'WLC:Gen.40.13': (A, [11], [P+'TEV-PRL-001'], 'Opened: in three days Pharaoh will restore you; the interpretation in the parallel scene (para 11).'),
 'WLC:Gen.40.14': (A, [12], [P+'TEV-PRL-002'], 'Opened: remember me and mention me to Pharaoh; the request of para 12.'),
 'WLC:Gen.40.15': (R, [], [], 'Opened: stolen from the land of the Hebrews and put in the bor. The innocence point is not developed by para 11; the verse is cited in TEV-SYD-002 only for its prison word.'),
 'WLC:Gen.40.19': (R, [], [], 'Opened: the baker hanged and birds eat his flesh. The base does not discuss the second youth\'s fate.'),
 'WLC:Gen.40.23': (A, [12], [P+'TEV-PRL-002'], 'Opened: the chief cupbearer did not remember Joseph but forgot him (para 12).'),
 'WLC:Gen.41.1': (A, [12], [P+'TEV-PRL-002'], 'Opened: mikkets shenatayim yamim; a measured two years against the Qur\'an\'s bid\'a sinin (para 12).'),
 'WLC:Gen.41.14': (R, [], [], 'Opened: Joseph rushed from the pit. Release is not narrated by the base.'),
 'WLC:Gen.41.29': (R, [], [], 'Opened: seven years of plenty. Context for 41:30 used in TEV-KRA-002.'),
 'WLC:Gen.41.30': (A, [12], [P+'TEV-KRA-002'], 'Opened: all the plenty will be forgotten; the Genesis sequence ends in famine, without the relief year of 12:49 (para 12).'),
 'WLC:Gen.41.31': (R, [], [], 'Opened: the plenty will not be known. Duplicates 41:30.'),
 'WLC:Gen.41.35': (A, [12], [P+'TEV-KRA-001'], 'Opened: veyitsberu var tahat yad Paro okhel be-arim; storage in cities against the Qur\'an\'s leaving in the ear (para 12).'),
 'WLC:Gen.41.36': (A, [12], [P+'TEV-KRA-001'], 'Opened: food as a reserve for the famine years; cited in the storage contrast (para 12).'),
 'WLC:Gen.41.47': (R, [], [], 'Opened: the land produced abundantly. Context.'),
 'WLC:Gen.41.48': (A, [12], [P+'TEV-KRA-001'], 'Opened: he put the food in the cities; storage method (para 12).'),
 'WLC:Gen.41.49': (A, [13], [P+'TEV-SYD-004'], 'Opened: vayyitsbor Yosef bar; the root tsbr (sound correspondence to s-b-r) means heap up; false-friend note at para 13.'),
 'WLC:Gen.41.5': (R, [], [], 'Opened: seven good ears on one stalk. Pharaoh\'s dream detail; the base already quotes 12:43 and the Genesis wording adds nothing specific.'),
 'WLC:Gen.41.53': (R, [], [], 'Opened: the seven years of plenty ended. Context.'),
 'WLC:Gen.41.54': (A, [12], [P+'TEV-KRA-002'], 'Opened: the seven years of famine began; cited in the no-relief-year contrast (para 12).'),
 'WLC:Gen.41.56': (R, [], [], 'Opened: Joseph opened the storehouses. Context.'),
 'WLC:Gen.41.57': (R, [], [], 'Opened: all the earth came to buy grain. Context.'),
 'WLC:Gen.41.6': (R, [], [], 'Opened: thin ears scorched by the east wind. The east-wind image is carried by Ezekiel 19:12 at para 21; context here.'),
 'WLC:Gen.41.9': (A, [12], [P+'TEV-PRL-002'], 'Opened: the cupbearer recalls his fault; remembering comes with the king\'s dream (para 12).'),
 'WLC:Gen.45.6': (A, [12], [P+'TEV-KRA-002'], 'Opened: five more years without ploughing or harvest; no relief year in Genesis (para 12).'),
 'WLC:Gen.6.14': (R, [], [], 'Opened: compartments of the ark. No base link.'),
 'WLC:Gen.7.16': (R, [], [], 'Opened: the LORD shut him in. Enclosure for rescue, but not the refuge-and-time scene of para 19; not added.'),
 'WLC:Gen.8.13': (R, [], [], 'Opened: the waters dried up. No base link.'),
 'WLC:Gen.8.2': (R, [], [], 'Opened: the rain was restrained (kala). Overlaps Deuteronomy 11:17, with a different verb.'),
 'WLC:Hag.1.10': (R, [], [], 'Opened: heavens withheld dew (kala). Overlaps Deuteronomy 11:17.'),
 'WLC:Hag.1.6': (R, [], [], 'Opened: wages put in a bag with holes. A loss image for 103:2, not this page.'),
 'WLC:Hos.8.7': (R, [], [], 'Opened: sow wind, reap whirlwind. Moral retribution; the base\'s whirlwind is a dust column and a fire wind.'),
 'WLC:Isa.16.10': (R, [], [], 'Opened: no treader treads wine in the presses. Joy ceasing; no specific link.'),
 'WLC:Isa.17.13': (A, [20], [P+'TEV-MTF-028'], 'Opened: ke-galgal lifney sufa; whirling dust before the storm (para 20).'),
 'WLC:Isa.2.19': (A, [19], [P+'TEV-MTF-026'], 'Opened: they shall go into caves of rocks from the terror of the LORD; the cave as flight from God, opposite to 18:16 (para 19).'),
 'WLC:Isa.27.3': (R, [], [], 'Opened: the LORD waters and guards his vineyard. No specific link.'),
 'WLC:Isa.5.2': (A, [16], [P+'TEV-MTF-019'], 'Opened: a winepress hewn, grapes expected, wild grapes produced (para 16).'),
 'WLC:Isa.5.5': (A, [16], [P+'TEV-MTF-019'], 'Opened: hedge removed, vineyard trampled (para 16).'),
 'WLC:Isa.5.6': (A, [16], [P+'TEV-MTF-019'], 'Opened: clouds commanded not to rain on it (para 16).'),
 'WLC:Isa.5.7': (A, [16], [P+'TEV-MTF-019'], 'Opened: the vineyard is the house of Israel, justice expected (para 16).'),
 'WLC:Isa.55.10': (A, [8], [P+'TEV-MTF-011'], 'Opened: rain gives seed to the sower and bread to the eater; the same chain as 78:14-16 (para 8).'),
 'WLC:Isa.59.17': (R, [], [], 'Opened: righteousness as a breastplate. Divine armour allegory; para 17 names armour only lexically.'),
 'WLC:Isa.63.3': (R, [], [], 'Opened: I trod the winepress alone. Judgment winepress already carried by Joel 4:13 at para 10.'),
 'WLC:Isa.65.8': (A, [8], [P+'TEV-MTF-010'], 'Opened: new wine found in the cluster, do not destroy it, a blessing is in it (para 8).'),
 'WLC:Isa.66.9': (R, [], [], 'Opened: shall I who cause birth shut the womb; restraint of the womb duplicated by Genesis 20:18.'),
 'WLC:Jer.6.4': (A, [5], [P+'TEV-MTF-004'], 'Opened: the day has turned, evening shadows lengthen; late-day alarm (para 5).'),
 'WLC:Job.1.19': (A, [21], [P+'TEV-MTF-030'], 'Opened: a great wind struck the house and the young people died (para 21).'),
 'WLC:Job.12.15': (A, [8], [P+'TEV-SYD-001'], 'Opened: hen yatsor ba-mayim ve-yivashu; he holds back the waters and they dry up; restraint use of the root in TEV-SYD-001 (para 8).'),
 'WLC:Job.14.5': (R, [], [], 'Opened: his days are determined. Overlaps Psalm 90 at para 6.'),
 'WLC:Job.14.6': (R, [], [], 'Opened: like a hired man his day. Overlaps Avot 2:15.'),
 'WLC:Job.24.11': (A, [9], [P+'TEV-MTF-012'], 'Opened: they tread the winepresses and thirst; pressing and dryness in one verse (para 9).'),
 'WLC:Job.27.16': (A, [13], [P+'TEV-SYD-004'], 'Opened: if he heaps up silver like dust; tsbr as heap, cited for the root\'s range (para 13).'),
 'WLC:Job.38.37': (R, [], [], 'Opened: who can tilt the water-jars of heaven. A cloud-vessel image without pressing; Isaiah 55:10 used at para 8.'),
 'WLC:Job.38.38': (R, [], [], 'Opened: dust fused into clods. Context of 38:37.'),
 'WLC:Job.7.6': (R, [], [], 'Opened: days swifter than a shuttle. Overlaps Psalm 90.'),
 'WLC:Joel.1.14': (R, [], [], 'Opened: qiru atsara; an assembly for a fast; the assembly noun is noted through Leviticus 23:36 in TEV-SYD-005.'),
 'WLC:Joel.2.15': (R, [], [], 'Opened: proclaim an atsara; duplicate of Joel 1:14.'),
 'WLC:Joel.2.24': (R, [], [], 'Opened: vats overflow with wine and oil. A blessing image close to Isaiah 65:8, used at para 8.'),
 'WLC:Joel.4.13': (A, [10], [P+'TEV-MTF-014'], 'Opened: the press is full, the vats overflow, for their wickedness is great (WLC 4:13 = KJV 3:13) (para 10).'),
 'WLC:Jonah.4.6': (R, [], [], 'Opened: a plant to shade Jonah. Shelter image unrelated to the asr refuge senses of para 17.'),
 'WLC:Judg.13.15': (A, [14], [P+'TEV-SYD-005'], 'Opened: naatsra na otakh, let us detain you; restraint sense of the root (para 14).'),
 'WLC:Judg.6.11': (A, [18], [P+'TEV-MTF-022'], 'Opened: Gideon beating wheat in the winepress to hide it from Midian; pressing place as hiding place (para 18).'),
 'WLC:Lev.15.19': (R, [], [], 'Opened: menstrual impurity seven days. Para 15 describes a protective seclusion lexically; the Levitical impurity rationale is different and the base invites no comparison.'),
 'WLC:Lev.19.13': (R, [], [], 'Opened: wages not kept overnight. Overlaps Matthew 20:8.'),
 'WLC:Lev.23.36': (A, [14], [P+'TEV-SYD-005'], 'Opened: atseret hi; the root appears as the noun atseret (closing assembly), not the verb form the reader quoted; cited for the root\'s range (para 14).'),
 'WLC:Mal.3.10': (R, [], [], 'Opened: windows of heaven opened with blessing. Overlaps Isaiah 55:10.'),
 'WLC:Mal.3.11': (R, [], [], 'Opened: the devourer rebuked. No specific link.'),
 'WLC:Nah.1.3': (A, [20], [P+'TEV-MTF-028'], 'Opened: his way in whirlwind and storm, clouds the dust of his feet (para 20).'),
 'WLC:Num.14.23': (R, [], [], 'Opened: oath that they will not see the land. Divine oath of exclusion; not para 1\'s oath by time.'),
 'WLC:Num.14.24': (R, [], [], 'Opened: Caleb the exception. Exception belongs to 103:3.'),
 'WLC:Num.17.13': (R, [], [], 'Opened: vatteatsar ha-maggefa, the plague was restrained; duplicate restraint sense.'),
 'WLC:Num.27.7': (R, [], [], 'Opened: daughters receive inheritance. No paragraph link.'),
 'WLC:Num.35.25': (A, [18], [P+'TEV-MTF-023'], 'Opened: city of refuge until the high priest\'s death; refuge measured by a time (para 18).'),
 'WLC:Prov.10.25': (R, [], [], 'Opened: as the whirlwind passes the wicked is no more. Overlaps Nahum 1:3.'),
 'WLC:Prov.11.24': (A, [16], [P+'TEV-MTF-018'], 'Opened: one scatters yet increases, one withholds and only lacks (para 16).'),
 'WLC:Prov.11.25': (A, [16], [P+'TEV-MTF-018'], 'Opened: who waters will be watered (para 16).'),
 'WLC:Prov.11.26': (A, [16], [P+'TEV-MTF-018'], 'Opened: monea bar yikkevuhu leom; withheld grain cursed (para 16).'),
 'WLC:Prov.14.26': (R, [], [], 'Opened: his children have a refuge. Overlaps Psalm 46:2.'),
 'WLC:Prov.3.27': (R, [], [], 'Opened: do not withhold good. Overlaps Deuteronomy 15:7-8.'),
 'WLC:Prov.3.28': (R, [], [], 'Opened: do not say come back tomorrow. Overlap.'),
 'WLC:Prov.30.4': (R, [], [], 'Opened: who gathered wind in his fists, bound waters in a garment. Divine-power riddles; no pressing or refuge sense of the base.'),
 'WLC:Ps.1.3': (R, [], [], 'Opened: fruit in its season. Generic.'),
 'WLC:Ps.1.4': (R, [], [], 'Opened: chaff driven by wind. Overlaps Isaiah 17:13.'),
 'WLC:Ps.102.12': (A, [5], [P+'TEV-MTF-004'], 'Opened: my days like a lengthening shadow (para 5).'),
 'WLC:Ps.104.23': (R, [], [], 'Opened: man goes to his labour until evening. Overlaps Jeremiah 6:4 and John 9:4.'),
 'WLC:Ps.105.18': (A, [13], [P+'TEV-PRL-003'], 'Opened: his feet in fetters; Joseph\'s confinement (para 13).'),
 'WLC:Ps.105.19': (A, [13], [P+'TEV-PRL-003'], 'Opened: until the time his word came, the word of the LORD refined him (para 13).'),
 'WLC:Ps.126.5': (R, [], [], 'Opened: sowing in tears, reaping in joy. Overlaps the Joseph waiting texts.'),
 'WLC:Ps.141.3': (A, [4], [P+'TEV-MTF-003'], 'Opened: WLC 141:3 is set a guard over my mouth; the evening-offering line is WLC 141:2, opened and cited at para 4.'),
 'WLC:Ps.142.6': (A, [19], [P+'TEV-MTF-025'], 'Opened: atta mahsi; you are my refuge, in the cave prayer (para 19).'),
 'WLC:Ps.144.4': (R, [], [], 'Opened: days like a passing shadow. Overlaps Psalm 102:12.'),
 'WLC:Ps.39.6': (R, [], [], 'Opened: handbreadths of days. Overlaps Psalm 90.'),
 'WLC:Ps.39.7': (A, [13], [P+'TEV-SYD-004'], 'Opened: yitsbor velo yeda mi osfam; tsbr as futile heaping (para 13).'),
 'WLC:Ps.46.2': (A, [18], [P+'TEV-MTF-021'], 'Opened: mahase va-oz ezra ve-tsarot; refuge paired with straits (para 18).'),
 'WLC:Ps.55.18': (A, [2], [P+'TEV-MTF-002'], 'Opened: evening, morning and noon I complain and moan (para 2).'),
 'WLC:Ps.65.11': (R, [], [], 'Opened: showers soften the furrows. Overlaps Isaiah 55:10.'),
 'WLC:Ps.65.12': (R, [], [], 'Opened: you crown the year of your goodness. Overlap; no specific addition.'),
 'WLC:Ps.90.10': (A, [6], [P+'TEV-MTF-006'], 'Opened: seventy or eighty years, swiftly gone (para 6).'),
 'WLC:Ps.90.11': (A, [6], [P+'TEV-MTF-006'], 'Opened: WLC 90:11 is who knows the power of your anger; the seventy-eighty years line is 90:10, opened and cited at para 6.'),
 'WLC:Ps.90.12': (A, [6], [P+'TEV-MTF-006'], 'Opened: teach us to number our days (para 6).'),
 'WLC:Ps.90.4': (A, [6], [P+'TEV-MTF-006'], 'Opened: a thousand years as yesterday (para 6).'),
 'WLC:Ps.90.5': (A, [6], [P+'TEV-MTF-006'], 'Opened: WLC 90:5 is you sweep them away, they are a sleep; the thousand-years-as-a-watch line is 90:4, cited at para 6.'),
 'WLC:Ps.90.7': (A, [6], [P+'TEV-MTF-006'], 'Opened: WLC 90:7 is we are consumed by your anger; the morning-flourish evening-wither line is 90:6, opened and cited at para 6.'),
 'WLC:Ps.92.15': (R, [], [], 'Opened: fruitful in old age. Not the old-age loss of para 21-22; no addition.'),
 'WLC:Ps.92.3': (R, [], [], 'Opened: morning and night praise. Overlaps Psalm 55:18.'),
 'WLC:Ps.95.11': (R, [], [], 'Opened: I swore they shall not enter my rest. Not para 1\'s oath type.'),
 'WLC:Ruth.2.12': (A, [17], [P+'TEV-MTF-020'], 'Opened: to take refuge under his wings (para 17).'),
 'WLC:Ruth.2.15': (R, [], [], 'Opened: let her glean among the sheaves. Overlaps Deuteronomy 24:19.'),
 'WLC:Ruth.2.16': (R, [], [], 'Opened: pull out some for her. Overlap.'),
 'WLC:Ruth.2.20': (A, [17], [P+'TEV-MTF-020'], 'Opened: the man is near to us, one of our redeemers; kinship as refuge (para 17).'),
 'WLC:Song.4.16': (A, [20], [P+'TEV-MTF-027'], 'Opened: blow upon my garden, let its spices flow (para 20).'),
 'WLC:Zech.10.1': (R, [], [], 'Opened: ask the LORD for rain. Overlaps Isaiah 55:10.'),
 'Wisdom of Solomon 3:6': (R, [], [], 'SEFARIA:The_Wisdom_of_Solomon.3.6 opened (a Hebrew rendering of a Greek work): tried like gold in the furnace. Refining is carried by Psalm 105:19 at para 13; no addition.'),
}

# per-connection overrides (distinct kinds under one ref)
O = {
 'BC-d9696ac9e8e0a96c25ac': (R, [], [], 'Opened WLC:1Kgs.8.35 as motif: prayer when heaven is shut. The prayer content is not developed by the base; the verse is used only for the root (soydas connections).'),
 'BC-52f9a14e186ebaf70afc': (R, [], [], 'Opened WLC:Ps.141.3 (guard over my mouth) and 141:2: prayer as incense. The rising-incense image is not the scent behind a passer-by of para 20; not used.'),
}

SEFMAP = {
 'Babylonian Talmud, Berakhot 26b': 'SEFARIA:Berakhot.26b', 'Berakhot 26b': 'SEFARIA:Berakhot.26b',
 "Babylonian Talmud, Ta'anit 23a": 'SEFARIA:Taanit.23a',
 'Genesis Rabbah 89:1': 'SEFARIA:Bereshit_Rabbah.89.1', 'Genesis Rabbah 89:3': 'SEFARIA:Bereshit_Rabbah.89.3',
 'Mishnah Avot 2:15': 'SEFARIA:Pirkei_Avot.2.15', 'Mishnah Avot 2:16': 'SEFARIA:Pirkei_Avot.2.16', 'Mishnah Avot 3:16': 'SEFARIA:Pirkei_Avot.3.16',
 'Mishnah Avot 4:16': 'SEFARIA:Pirkei_Avot.4.16', 'Mishnah Avot 4:17': 'SEFARIA:Pirkei_Avot.4.17', 'Mishnah Avot 5:10': 'SEFARIA:Pirkei_Avot.5.10',
 'Mishnah Berakhot 4:1': 'SEFARIA:Mishnah_Berakhot.4.1', 'Sirach 4:31': 'SEFARIA:Ben_Sira.4.31', 'Tobit 4:7': 'SEFARIA:Book_of_Tobit.4.7',
 'Wisdom of Solomon 3:6': 'SEFARIA:The_Wisdom_of_Solomon.3.6',
}
EXTRA_EV = {'WLC:Dan.6.10': ['WLC:Dan.6.11'], 'WLC:Ps.141.3': ['WLC:Ps.141.2'], 'WLC:Ps.90.11': ['WLC:Ps.90.10'], 'WLC:Ps.90.5': ['WLC:Ps.90.4'], 'WLC:Ps.90.7': ['WLC:Ps.90.6']}

def ev_for(ref, status, anns):
    ev = []
    if ref.startswith(('WLC:', 'SBLGNT:')):
        ev.append(ref)
    if ref in SEFMAP:
        ev.append(SEFMAP[ref])
    for x in EXTRA_EV.get(ref, []):
        if status == A:
            ev.append(x)
    if status == A:
        for a in anns:
            for s in local_sources(a):
                if s not in ev:
                    ev.append(s)
    out = []
    for e in ev:
        if e not in out:
            out.append(e)
    return out

rows = list(csv.DictReader(open(DISC + '103_1.merged.tsv'), delimiter='\t'))
out = []
missing = []
seen = set()
for r in rows:
    ref = r['ref']
    ev = json.loads(r['evidence'])
    cids = []
    for e in ev:
        if e['connection_id'] not in cids:
            cids.append(e['connection_id'])
    for cid in cids:
        if cid in seen:
            continue
        seen.add(cid)
        if cid in O:
            st, pars, anns, reason = O[cid]
        elif ref in D:
            st, pars, anns, reason = D[ref]
        else:
            missing.append(ref)
            continue
        out.append({'connection_id': cid, 'ref': ref, 'status': st, 'reason': reason, 'paragraphs': pars,
                    'evidence': ev_for(ref, st, anns) if ref.startswith(('WLC:', 'SBLGNT:')) or ref in SEFMAP or st == A else ev_for(ref, st, anns),
                    'annotations': anns})

# research verdicts
RS = [
 ('WLC:Gen.40.9', A, [11], [P+'TEV-PRL-001'], 'Opened: the cupbearer tells his dream, a vine before him; opening of the parallel scene (para 11).'),
 ('WLC:Gen.40.10', A, [11], [P+'TEV-PRL-001'], 'Opened: three branches, clusters ripened into grapes (para 11).'),
 ('WLC:Gen.40.12', A, [11], [P+'TEV-PRL-001'], 'Opened: the three branches are three days (para 11).'),
 ('WLC:Gen.41.34', R, [], [], 'Opened: a fifth of the land in the years of plenty. Context for the storage contrast; not cited.'),
 ('WLC:2Kgs.17.4', A, [11], [P+'TEV-SYD-002'], 'Opened: vayyaatsrehu ... vayyaasrehu beyt kele; atsar for detaining a prisoner (para 11).'),
 ('WLC:Jer.33.1', A, [11], [P+'TEV-SYD-002'], 'Opened: Jeremiah still atsur in the court of the guard (para 11).'),
 ('WLC:Jer.36.5', A, [11], [P+'TEV-SYD-002'], 'Opened: ani atsur, I am restrained and cannot enter the house of the LORD; cited for the same sense (para 11).'),
 ('WLC:1Chr.29.14', A, [14], [P+'TEV-SYD-005'], 'Opened: ki naatsor koah le-hitnadev; retaining strength to give freely (para 14).'),
 ('WLC:Deut.16.8', R, [], [], 'Opened: the seventh day of unleavened bread is an atseret; duplicates Leviticus 23:36 for the assembly noun.'),
 ('WLC:Prov.25.28', R, [], [], 'Opened: a man without maatsar (restraint) for his spirit; restraint sense duplicated; not cited.'),
 ('SBLGNT:Matt.5.34', A, [1], [P+'INC-KRA-001'], 'Opened: do not swear at all, neither by heaven (para 1).'),
 ('SBLGNT:Matt.5.35', A, [1], [P+'INC-KRA-001'], 'Opened: nor by the earth, nor by Jerusalem (para 1).'),
 ('SBLGNT:Matt.5.36', A, [1], [P+'INC-KRA-001'], 'Opened: nor by your head (para 1).'),
 ('SBLGNT:Acts.10.30', A, [2], [P+'INC-MTF-003'], 'Opened: Cornelius praying at the ninth hour in his house (para 2).'),
 ('SBLGNT:Jas.4.15', A, [16], [P+'INC-MTF-011'], 'Opened: instead you ought to say, if the Lord wills (para 16).'),
 ('WLC:Dan.6.11', A, [2], [P+'TEV-MTF-002'], 'Opened: three times a day he knelt and prayed (Aramaic; WLC 6:11 = KJV 6:10) (para 2).'),
 ('WLC:Deut.24.20', A, [16], [P+'TEV-MTF-017'], 'Opened: do not go over the olive boughs again (para 16).'),
 ('WLC:Exod.29.41', A, [4], [P+'TEV-MTF-003'], 'Opened: the second lamb bein ha-arbayim like the morning offering (para 4).'),
 ('WLC:Ps.141.2', A, [4], [P+'TEV-MTF-003'], 'Opened: the lifting of my hands as the evening offering (minhat arev) (para 4).'),
 ('WLC:Ps.142.1', A, [19], [P+'TEV-MTF-025'], 'Opened: a prayer of David when he was in the cave (para 19).'),
 ('WLC:Ps.90.6', A, [6], [P+'TEV-MTF-006'], 'Opened: in the morning it flourishes, in the evening it fades and withers (para 6).'),
 ('WLC:Prov.30.33', A, [7], [P+'TEV-MTF-009'], 'Opened: pressing (mits) milk, nose and anger brings out butter, blood, strife (para 7).'),
 ('WLC:Lam.4.4', R, [], [], 'Opened: the infant\'s tongue cleaves for thirst. Overlaps Isaiah 41:17, which also carries the answer; not cited.'),
 ('WLC:Isa.41.17', A, [9], [P+'TEV-MTF-013'], 'Opened: their tongue is parched with thirst; I the LORD will answer them (para 9).'),
 ('WLC:Exod.8.10', R, [], [], 'Opened: frogs heaped (tsbr) in heaps; confirms the heap sense only.'),
 ('WLC:Hab.1.10', R, [], [], 'Opened: he heaps up (tsbr) dust and takes the fortress; heap sense only.'),
 ('WLC:Zech.9.3', R, [], [], 'Opened: Tyre heaped (tsbr) silver like dust; heap sense; Psalm 39:7 carries the futility point.'),
 ('WLC:2Kgs.10.8', R, [], [], 'Opened: two heaps (tsibburim) of heads; noun of the root, heap sense only.'),
 ('WLC:Jer.5.24', R, [], [], 'Opened: rain in its season; verse quoted inside Taanit 23a; context only.'),
 ('WLC:Jer.5.25', R, [], [], 'Opened: your sins withheld the good; context of Taanit 23a; no addition.'),
 ('SEFARIA:Rashi_on_Leviticus.23.36', N, [], [], 'Lookup returned NOT FOUND: Rashi on Leviticus 23:36 (atseret as being detained with God) was not fetched for this page.'),
 ('SEFARIA:Taanit.23a', A, [19], [P+'TEV-MTF-024'], 'Opened in full: Honi\'s seventy-year sleep enclosed by rock (para 19).'),
 ('SEFARIA:Berakhot.26b', A, [4], [P+'TEV-YGL-002'], 'Opened: Isaac instituted minha; minha until evening because of the tamid between the evenings (para 4).'),
 ('SEFARIA:Mishnah_Berakhot.4.1', A, [2], [P+'TEV-YGL-001'], 'Opened: minha until evening; R. Judah until plag ha-minha (para 2).'),
 ('SEFARIA:Pirkei_Avot.2.15', A, [5], [P+'TEV-MTF-005'], 'Opened: R. Tarfon, the day is short (para 5).'),
 ('SEFARIA:Pirkei_Avot.2.16', A, [5], [P+'TEV-MTF-005'], 'Opened: not upon you to finish the work (para 5).'),
 ('SEFARIA:Pirkei_Avot.3.16', R, [], [], 'Opened: open shop and ledger; not used on this page.'),
 ('SEFARIA:Pirkei_Avot.4.16', A, [6], [P+'TEV-MTF-008'], 'Opened: this world as a vestibule (para 6).'),
 ('SEFARIA:Pirkei_Avot.4.17', A, [6], [P+'TEV-MTF-008'], 'Opened: one hour of repentance and good deeds (para 6).'),
 ('SEFARIA:Pirkei_Avot.5.10', R, [], [], 'Opened: four character types; not used.'),
 ('SEFARIA:Bereshit_Rabbah.89.1', A, [13], [P+'TEV-YGL-004'], 'Opened: a time set for Joseph\'s years in the dark prison (para 13).'),
 ('SEFARIA:Bereshit_Rabbah.89.3', A, [12], [P+'TEV-YGL-003'], 'Opened: two years added because he said remember me (para 12).'),
 ('SEFARIA:Ben_Sira.4.31', R, [], [], 'Opened: this witness reads be not boastful with your tongue; it does not contain the Greek hand-saying (textual grounds for this witness).'),
 ('SEFARIA:Ben_Sira.4.30', N, [], [], 'Lookup returned NOT FOUND while searching the Ben Sira hand-saying under neighbouring numbers.'),
 ('SEFARIA:Ben_Sira.4.32', N, [], [], 'Lookup returned NOT FOUND while searching the Ben Sira hand-saying under neighbouring numbers.'),
 ('SEFARIA:Book_of_Tobit.4.7', R, [], [], 'Opened: this Hebrew Tobit text at 4:7 concerns money deposited with Gabael, not alms (versification/version differs from the Greek).'),
 ('SEFARIA:Book_of_Tobit.4.8', N, [], [], 'Lookup returned NOT FOUND while seeking the Greek 4:7-9 almsgiving content.'),
 ('SEFARIA:The_Wisdom_of_Solomon.3.6', R, [], [], 'Opened: tried like gold in the furnace; Psalm 105:19 carries refining at para 13.'),
 ('SEFARIA:Onkelos_Genesis.40.11', U, [11], [P+'TEV-SYD-003'], 'Lookup returned NOT FOUND; the Aramaic rendering of Genesis 40:11 with atsar is given from memory, marked degerlendirilmedi, pending the Targum text.'),
 ('SEFARIA:Targum_Jonathan_on_Genesis.40.11', N, [], [], 'Lookup returned NOT FOUND; Targum Pseudo-Jonathan was not fetched.'),
 ('SEFARIA:Rashi_on_Genesis.40.11', N, [], [], 'Lookup returned NOT FOUND; Rashi on Genesis was not fetched.'),
 ('SEFARIA:Onkelos_Genesis.41.49', N, [], [], 'Lookup returned NOT FOUND; Onkelos on Genesis 41:49 was not fetched.'),
 ('QURAN:12:42', A, [12], [P+'TEV-YGL-003'], 'Opened: Satan made him forget the mention of his Lord, and he remained some years; Qur\'an wording set beside Genesis Rabbah 89:3 (para 12).'),
 ('QURAN:68:18', R, [], [], 'Opened: wa la yastathnun; checked for the istisna wording referred to in INC-MTF-011; the block cites the base\'s own quotation, so no separate citation.'),
 ('QURAN:103:1', R, [], [], 'Opened via ayah lookup: wal-asr; the page\'s own ayah, context only.'),
 ('CORPUSCORANICUM:103:1:anmerkung', R, [], [], 'Opened: lexical range of asr and the time-oath series; no Bible intertext; context only for this pass.'),
 ('CORPUSCORANICUM:103:1-3:kommentar', A, [1, 2], [P+'INC-MTF-002', P+'INC-MTF-003'], 'Opened in full: Robinson\'s market-end reading and Neuwirth\'s prayer-time reading of asr; cited as modern scholarship beside Matthew 20 and Acts 3 (paras 1-2).'),
]
for ref, st, pars, anns, reason in RS:
    ev = []
    if st == A:
        ev = [ref]
        for a in anns:
            for s in local_sources(a):
                if s not in ev:
                    ev.append(s)
    elif st == R:
        ev = [ref]
    out.append({'connection_id': None, 'origin': 'research', 'ref': ref, 'status': st, 'reason': reason, 'paragraphs': pars, 'evidence': ev, 'annotations': anns})

with open(CALL + 'verdicts.jsonl', 'w') as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + '\n')

# coverage check: every kept annotation linked
linked = set()
for o in out:
    linked.update(o['annotations'])
print('verdicts', len(out), 'discovery cids', len(seen), 'missing refs', missing)
print('unlinked annotations', sorted(set(ann) - linked))
from collections import Counter
print(Counter(o['status'] for o in out))
