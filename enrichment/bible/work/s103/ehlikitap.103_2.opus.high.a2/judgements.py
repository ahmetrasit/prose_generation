"""My research judgements for 103:2 (ehlikitap). The script only formats them into verdicts.jsonl.
Inputs read: the discovery TSV, prefetch.json, and my annotations.jsonl (for paragraphs and cited locators)."""
import csv
import json
from pathlib import Path

D = Path(__file__).resolve().parent
DISC = Path("/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009")
csv.field_size_limit(10**9)

ANN = {json.loads(l)["id"]: json.loads(l) for l in (D / "annotations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
PRE = {c["ref"]: c["locators"] for c in json.loads((DISC / "prefetch.json").read_text())["candidates"]}

A, R, U = "accepted", "rejected", "unavailable"

# ref -> (status, reason, [annotation ids])
T = {
 # --- unavailable named works (prefetch gaps)
 "Didache 1.1": (U, "Didache is not in the intertext corpus (prefetch gap); the two-ways opening cannot be opened or quoted here, so the claimed link to the straying sense of loss stays unverified.", []),
 "Didache 1:1": (U, "Didache is not in the intertext corpus (prefetch gap); the way-of-life/way-of-death opening cannot be verified in this run.", []),
 "Epistle of Barnabas 18:1": (U, "Epistle of Barnabas is not in the intertext corpus (prefetch gap); the two ways of light and darkness cannot be opened.", []),
 "Gospel of Thomas 3": (U, "Gospel of Thomas is not in the intertext corpus (prefetch gap); the saying on self-knowledge and poverty cannot be opened.", []),
 "Gospel of Thomas 63": (U, "Gospel of Thomas is not in the intertext corpus (prefetch gap); the rich farmer saying cannot be opened (its canonical counterpart Luke 12:16-21 is used instead).", []),
 "Sirach 11:19": (U, "SEFARIA:Ben_Sira.11.19 was opened but under Sefaria's Hebrew numbering it reads 'foolishness and darkness were created for sinners', not the rich man's 'I have found rest' saying the reader describes (Greek Sir 11:18-19); neighbouring verses 11:17, 11:18, 11:20 are NOT FOUND in the corpus, so the intended passage is unavailable.", []),
 # --- NT
 "SBLGNT:1Cor.13.12": (R, "Opened: seeing now through a mirror in an enigma, then face to face, concerns eschatological knowledge of God; the page's image (¶23) is seeing oneself reflected in another person's eye. keyword-only: mirror/seeing.", []),
 "SBLGNT:1Cor.13.3": (R, "Opened: giving away all possessions without love profits nothing (οὐδὲν ὠφελοῦμαι). Shares only the vocabulary of profit; no ledger of loss or self-loss scene of the page. keyword-only: profit.", []),
 "SBLGNT:1Cor.3.13": (A, "Opened: each one's work is revealed on the day and tested by fire; context of 3:15 used in the contrast block at ¶12.", ["S103-INC-KRA-002"]),
 "SBLGNT:1Cor.3.14": (A, "Opened: the work that remains receives a wage; part of the Pauline sequence (3:13-15) in which loss of work and loss of self are separated, contrasted at ¶12 with 7:9.", ["S103-INC-KRA-002"]),
 "SBLGNT:1Cor.3.15": (A, "Opened: whose work is burned 'will suffer loss (ζημιωθήσεται), but he himself will be saved'. Paul separates the loss of work from the person; the Qur'anic scale at ¶12 makes the light pan the self. Kept as karsi_anlati.", ["S103-INC-KRA-002"]),
 "SBLGNT:1Thess.1.3": (R, "Opened: work of faith, labour of love, endurance of hope. This is the vocabulary of 103:3 (faith, deeds, patience), not of any paragraph of the 103:2 page.", []),
 "SBLGNT:1Thess.5.11": (R, "Opened: encourage and build one another. Mutual exhortation belongs to 103:3 (tawāṣaw); ¶23/¶25 speak of mutual seeing and solitude, which Prov 27:19 and Eccl 4:8-10 carry more precisely.", []),
 "SBLGNT:1Tim.6.18": (R, "Opened: be rich in good works, generous. A 103:3-type exhortation; no shared image with the 103:2 paragraphs.", []),
 "SBLGNT:1Tim.6.19": (R, "Opened: storing up a good foundation for the future. Treasure-in-heaven theme; ¶9's hoarding is covered by Luke 12:16-21; no independent addition.", []),
 "SBLGNT:1Tim.6.7": (R, "Opened: we brought nothing into the world and can carry nothing out. Generic mortality-of-wealth topos; Luke 12:19-21 carries ¶9's specific error (wealth mistaken for life).", []),
 "SBLGNT:1Tim.6.9": (R, "Opened: desire to be rich plunges people into ruin and destruction (ὄλεθρον καὶ ἀπώλειαν). Theme of greed and ruin only; no ledger, scale or self-loss formula of the page.", []),
 "SBLGNT:2Cor.4.18": (R, "Opened: things seen are temporary, unseen eternal. The page's 'visible being' (¶20) concerns humans as seen beings, not transience. keyword-only: visible.", []),
 "SBLGNT:2Cor.4.4": (R, "Opened: the god of this age blinded the minds of unbelievers. Blindness theme; Rev 3:17 and John 9:41 express ¶15/¶22's unnoticed loss and claimed sight more exactly.", []),
 "SBLGNT:2Cor.5.10": (R, "Opened: all appear before the judgment seat to receive according to deeds. Generic recompense; the scale paragraphs are carried by Dan 5:27, Ps 62:10, 1Cor 3:15.", []),
 "SBLGNT:Eph.2.9": (R, "Opened: 'not from works'. The grace/works contrast with 103:3 is already given through Rom 3:23-24 at ¶4; Ephesians adds no new point for 103:2.", []),
 "SBLGNT:Eph.4.25": (R, "Opened: speak truth each with his neighbour. Belongs to 103:3 (tawāṣaw bi'l-ḥaqq), not to a 103:2 paragraph.", []),
 "SBLGNT:Eph.5.16": (A, "Opened: 'buying up the time (ἐξαγοραζόμενοι τὸν καιρόν), because the days are evil'; market verb applied to time, exactly ¶9's claim that the capital spent is time. 5:15 opened as context.", ["S103-INC-MTF-005"]),
 "SBLGNT:Gal.4.2": (R, "Opened: the heir is under guardians until the date set by the father. A legal metaphor for the law's age; it lacks the perceiving of maturity (ānastum rushdan) that ¶21 develops. keyword-only: guardianship.", []),
 "SBLGNT:Gal.6.1": (R, "Opened: restore one caught in a fault, watching yourself. Mutual correction is 103:3 material.", []),
 "SBLGNT:Gal.6.2": (R, "Opened: bear one another's burdens. 103:3 mutual support; the ¶24 burden image is about the beast's near side, not shared loads.", []),
 "SBLGNT:Gal.6.7": (R, "Opened: whatever one sows, one reaps. Agricultural retribution formula, not the commercial ledger the page develops; theme only.", []),
 "SBLGNT:Gal.6.8": (R, "Opened: sowing to the flesh reaps corruption. Same sowing/reaping image; no shared scene with the page.", []),
 "SBLGNT:Gal.6.9": (R, "Opened: do not tire of doing good; in due season we reap. 103:3 perseverance; not a 103:2 point.", []),
 "SBLGNT:Heb.10.24": (R, "Opened: stir one another to love and good works. 103:3 mutual exhortation.", []),
 "SBLGNT:Heb.10.36": (R, "Opened: you need endurance (ὑπομονή). Corresponds to 103:3 ṣabr, not to 103:2.", []),
 "SBLGNT:Heb.3.13": (R, "Opened: exhort one another every day while it is called Today. Mutual exhortation (103:3) with a time note; Eph 5:16 carries ¶9's time-as-capital more precisely.", []),
 "SBLGNT:Heb.4.13": (R, "Opened: nothing hidden before his eyes. Generic divine omniscience; no ledger or scale image of the page.", []),
 "SBLGNT:Heb.9.27": (R, "Opened: to die once, then judgment. Generic eschatology; no loss formula.", []),
 "SBLGNT:Jas.1.23": (R, "Opened: a hearer who is not a doer is like a man looking at his face in a mirror. James's mirror is the word and the point is hearing without doing (103:3); ¶23's image of one's face in another's eye is carried by Prov 27:19.", []),
 "SBLGNT:Jas.1.24": (R, "Opened: he looks, goes away and forgets what he was like. Forgetting oneself after a glance is close to ¶22 but James ties it to non-doing of the word; Rev 3:17 and John 9:41 carry the unnoticed-loss point.", []),
 "SBLGNT:Jas.1.25": (R, "Opened: the doer who perseveres is blessed in his doing. 103:3 material.", []),
 "SBLGNT:Jas.2.17": (R, "Opened: faith without works is dead. Pairing of faith and works belongs to 103:3, not 103:2.", []),
 "SBLGNT:Jas.4.13": (R, "Opened: 'we will trade and make a profit' (ἐμπορευσόμεθα καὶ κερδήσομεν). A real commercial scene, but its point (planning gain while ignorant of tomorrow) duplicates the Luke 12:16-21 block at ¶9.", []),
 "SBLGNT:Jas.4.14": (R, "Opened: you do not know tomorrow; your life is a vapour. Transience topos; covered by Luke 12:20 and Ps 90:10-12 at ¶9.", []),
 "SBLGNT:Jas.5.19": (R, "Opened: if one wanders from the truth and someone turns him back. Bringing back the strayed is 103:3 (mutual counsel of truth).", []),
 "SBLGNT:Jas.5.2": (R, "Opened: your riches have rotted. Decay-of-wealth theme; no ledger/self-loss formula.", []),
 "SBLGNT:Jas.5.20": (R, "Opened: turning a sinner from his wandering saves a soul from death. 103:3 material.", []),
 "SBLGNT:Jas.5.3": (R, "Opened: rust of gold and silver will witness against you. Decay-of-wealth theme only.", []),
 "SBLGNT:Jas.5.4": (R, "Opened: withheld wages of harvesters cry out. Wage fraud is not the measure-and-scale fraud of ¶10-11; theme only.", []),
 "SBLGNT:John.8.39": (A, "Opened: 'If you were Abraham's children you would do the works of Abraham.' Shares ¶19's argument that the distinction rests on deeds, not lineage; joined with Matt 3:8-9.", ["S103-INC-MTF-007"]),
 "SBLGNT:John.9.41": (A, "Opened: 'now you say We see; your sin remains' (with 9:39-40 as context). Shares ¶22's claim that the being who sees may not see his own state; claimed sight entrenches it.", ["S103-INC-MTF-008"]),
 "SBLGNT:Luke.12.18": (A, "Opened: tearing down barns to build bigger ones; part of the rich fool parable used at ¶9 (104:2-3 hoarding and imagined permanence).", ["S103-INC-MTF-004"]),
 "SBLGNT:Luke.12.19": (A, "Opened and quoted: 'you have many goods laid up for many years' - wealth mistaken for years of life, the 104:3 error ¶9 cites.", ["S103-INC-MTF-004"]),
 "SBLGNT:Luke.12.20": (A, "Opened: 'this night your soul is required of you; whose will they be?' Sudden end of the hoarder; core of the ¶9 block.", ["S103-INC-MTF-004"]),
 "SBLGNT:Luke.12.21": (A, "Opened: so is he who stores up for himself and is not rich toward God; the parable's ledger conclusion, used at ¶9.", ["S103-INC-MTF-004"]),
 "SBLGNT:Luke.15.12": (R, "Opened: the younger son asks for his share of the property. The reader's karsi_anlati (estate received early vs. 4:6 handing property to the mature) is not developed by the page; used only as narrative context, no independent addition.", []),
 "SBLGNT:Luke.15.13": (A, "Opened: he squandered his property in a far country; the loss-of-capital step of the ¶25 block.", ["S103-INC-MTF-009"]),
 "SBLGNT:Luke.15.17": (A, "Opened and quoted: 'coming to himself' (εἰς ἑαυτὸν δὲ ἐλθὼν) - shares ¶25's point that loss first takes the self and return begins with oneself.", ["S103-INC-MTF-009"]),
 "SBLGNT:Luke.15.24": (A, "Opened: 'was dead and is alive, was lost (ἀπολωλώς) and is found'; completes the ¶25 block (return into a household).", ["S103-INC-MTF-009"]),
 "SBLGNT:Luke.16.10": (R, "Opened: faithful in little, faithful in much. Trustworthiness theme; ¶21's 4:6 point is perceiving maturity before handing over capital, which this verse does not share.", []),
 "SBLGNT:Luke.16.11": (R, "Opened: if not faithful with unrighteous mammon, who will entrust true riches? Same trust theme; no shared image with ¶21.", []),
 "SBLGNT:Luke.16.25": (R, "Opened: the rich man received good things in life, Lazarus evil; now reversed. Reversal of fortune, not loss of capital or scale.", []),
 "SBLGNT:Luke.16.6": (R, "Opened: the steward rewrites a debt of 100 to 50. The reader's karsi_anlati with short measure (¶10) is superficial: the parable is about prudence, not defrauding a buyer's measure.", []),
 "SBLGNT:Luke.16.8": (R, "Opened: the master praises the dishonest steward's prudence. No shared argument with the page's fraud or loss.", []),
 "SBLGNT:Luke.16.9": (R, "Opened: make friends by unrighteous mammon to be received into eternal dwellings. Theme of using wealth; not a page claim.", []),
 "SBLGNT:Luke.17.33": (R, "Opened: whoever seeks to preserve his life will lose it. Same saying as Luke 9:24-25, already the ¶8 block; no new addition.", []),
 "SBLGNT:Luke.9.25": (A, "Opened and quoted: 'gaining the whole world but losing or forfeiting oneself' (ἑαυτὸν δὲ ἀπολέσας ἢ ζημιωθείς); Corpus Coranicum lists Luke 9:23-27 as an intertext of 103:2 and notes, after Torrey, that the Peshitta uses ḥsar. Shares ¶8's point that the person himself is the stake.", ["S103-INC-MTF-003"]),
 "SBLGNT:Mark.10.21": (R, "Opened: 'one thing you lack (ὑστερεῖ); sell what you have'. Treasure-in-heaven and discipleship; 103:3 material, not a 103:2 paragraph.", []),
 "SBLGNT:Mark.14.62": (R, "Opened: 'you will see the Son of Man ... coming with the clouds'. Christian reading of Dan 7:13; the only link to the page is the Aramaic word ʾĕnāš. keyword-only: son of man / ʾ-n-š.", []),
 "SBLGNT:Mark.8.36": (A, "Opened: gain the whole world and forfeit one's life (ζημιωθῆναι τὴν ψυχὴν); synoptic parallel cited with Luke 9:25 at ¶8.", ["S103-INC-MTF-003"]),
 "SBLGNT:Matt.12.36": (R, "Opened: account to be given for every idle word. Generic judgment accounting; no capital, scale or self-loss.", []),
 "SBLGNT:Matt.13.44": (R, "Opened: a man sells all he has to buy the field with hidden treasure. A positive mirror of 2:16's bad trade, but ¶8's point is the loss; Phil 3:7-8 already carries the revaluation of gain and loss.", []),
 "SBLGNT:Matt.16.26": (A, "Opened: gain the world, forfeit the soul; 'what will a man give in exchange (ἀντάλλαγμα) for his soul?' - the exchange image of ¶8. Cited with Luke 9:25.", ["S103-INC-MTF-003"]),
 "SBLGNT:Matt.20.14": (R, "Opened: 'I choose to give this last as to you'. Equal wage by grace; no paragraph of the page treats wages or grace.", []),
 "SBLGNT:Matt.25.16": (A, "Opened: the one with five talents traded and gained five more; part of the ¶6 block (capital traded vs. buried).", ["S103-INC-MTF-001"]),
 "SBLGNT:Matt.25.19": (A, "Opened: after a long time the master settles accounts (συναίρει λόγον) - the reckoning of ¶6.", ["S103-INC-MTF-001"]),
 "SBLGNT:Matt.25.25": (A, "Opened: the servant hid the talent in the ground and returns it intact; the case where no gain still counts as loss.", ["S103-INC-MTF-001"]),
 "SBLGNT:Matt.25.29": (A, "Opened and quoted: from him who has not, even what he has will be taken - ¶6's 'loss is more than failing to profit; what one has diminishes'.", ["S103-INC-MTF-001"]),
 "SBLGNT:Matt.3.8": (A, "Opened: bear fruit worthy of repentance; first half of the ¶19 block (deeds decide).", ["S103-INC-MTF-007"]),
 "SBLGNT:Matt.3.9": (A, "Opened and quoted: do not say 'we have Abraham as father'. Shares ¶19's argument that the line between people is drawn by deeds, not lineage.", ["S103-INC-MTF-007"]),
 "SBLGNT:Matt.6.19": (R, "Opened: do not store treasures on earth where moth and rust destroy. Generic transience of wealth; ¶9 is carried by Luke 12:16-21.", []),
 "SBLGNT:Matt.6.20": (R, "Opened: store treasure in heaven. Same saying; no new point for 103:2.", []),
 "SBLGNT:Matt.7.13": (R, "Opened: broad way leading to destruction (ἀπώλεια). Way-plus-destruction is close to ¶14 but the Hebrew Ps 1:6/119:176 block already makes the point; duplicate.", []),
 "SBLGNT:Matt.7.19": (R, "Opened: every tree not bearing good fruit is cut down and burned. Does not share 2:266's image of a lifetime's harvest burnt by a fiery wind; theme only.", []),
 "SBLGNT:Matt.7.24": (R, "Opened: hearing and doing as building on rock. A 103:3 hearing/doing point.", []),
 "SBLGNT:Matt.7.25": (R, "Opened: the house on rock stands in the storm. ¶14's refuge and whirlwind belong to the lexical senses of ʿaṣr; the parable's point is doing the word. Theme only.", []),
 "SBLGNT:Matt.7.27": (R, "Opened: the house falls and great is its fall. Same parable; no shared argument with ¶14.", []),
 "SBLGNT:Matt.7.3": (R, "Opened: seeing the speck in a brother's eye, not the beam in one's own. Eye imagery about judging others; ¶23 is about seeing oneself in another's eye positively. keyword-only: eye.", []),
 "SBLGNT:Matt.7.5": (R, "Opened: first remove the beam from your own eye. Same saying; no addition.", []),
 "SBLGNT:Phil.3.7": (A, "Opened and quoted: what was gain I counted loss (ζημίαν) for Christ; Corpus Coranicum notes the Peshitta's ḥusrānā here. Shares ¶7's ledger beyond money, with the reversed direction (loss chosen).", ["S103-INC-MTF-002"]),
 "SBLGNT:Phil.3.8": (A, "Opened: I count all things loss to gain Christ; continuation of the ¶7 block.", ["S103-INC-MTF-002"]),
 "SBLGNT:Rev.18.17": (R, "Opened: in one hour such wealth is laid waste. Fall of Babylon's commerce; no individual ledger or self-loss.", []),
 "SBLGNT:Rev.20.12": (R, "Opened: books opened, the dead judged by what was written according to their works. A ledger image, but Avot 3:16 at ¶7 already carries the open ledger; duplicate.", []),
 "SBLGNT:Rev.3.17": (A, "Opened and quoted: 'you say I am rich ... and do not know that you are wretched'. Shares ¶15's (and ¶7's) unnoticed loss.", ["S103-INC-MTF-006"]),
 "SBLGNT:Rev.3.18": (A, "Opened: counsel to buy refined gold and eye salve to see; the remedy is again a purchase. Part of the ¶15 block.", ["S103-INC-MTF-006"]),
 "SBLGNT:Rom.1.17": (R, "Opened: the righteous shall live by faith (Hab 2:4). Faith belongs to 103:3.", []),
 "SBLGNT:Rom.2.11": (R, "Opened: no partiality with God. Generic; ¶19's lineage argument is carried by Matt 3:9/John 8:39.", []),
 "SBLGNT:Rom.2.6": (R, "Opened: he will render to each according to works. Generic recompense.", []),
 "SBLGNT:Rom.2.7": (R, "Opened: eternal life to those who persist in good work. 103:3 material.", []),
 "SBLGNT:Rom.3.23": (A, "Opened and quoted: all sinned and fall short (ὑστεροῦνται). Paul universalises Ps 14 (3:10-12 opened); the exit is grace through faith (3:22, 3:24). Contrast with ¶4's verdict whose exception counts faith, deeds and mutual counsel.", ["S103-INC-KRA-001"]),
 "SBLGNT:Rom.3.24": (A, "Opened and quoted: justified freely by his grace; the exit side of the ¶4 contrast.", ["S103-INC-KRA-001"]),
 "SBLGNT:Rom.5.12": (R, "Opened: through one man sin and death came to all. Inherited death is not the page's verdict of loss; Rom 3 already carries the universal-verdict contrast.", []),
 # --- Jewish named works (Sefaria)
 "Kiddushin 40b": (A, "Opened SEFARIA:Kiddushin.40b: a person should see himself half liable, half meritorious; one mitzvah 'tips himself to the pan of merit' (לכף זכות). Shares ¶13's two pans with the self on the scale.", ["S103-TEV-MTF-012"]),
 "Mishnah Avot 1:14": (A, "Opened SEFARIA:Pirkei_Avot.1.14 (Hillel, cf. 1:12): 'If I am not for myself, who is for me? If I am only for myself, what am I?' Shares ¶25's self as closest friend and exit only with others.", ["S103-TEV-MTF-017"]),
 "Mishnah Avot 1:6": (R, "Opened: acquire a companion; judge everyone favourably. Companionship theme belongs to 103:3; Avot 1:14 carries ¶25's point precisely.", []),
 "Mishnah Avot 2:1": (A, "Opened: 'reckon the loss of a commandment against its reward and the gain of a transgression against its loss'; the merchant's comparison of ¶6 applied to deeds.", ["S103-TEV-MTF-004"]),
 "Mishnah Avot 2:15": (R, "Opened: the day is short, the work much, the wage great. Time and work, but framed as labour and wage; ¶9's time-as-capital is carried by Ps 90:12 and Eph 5:16.", []),
 "Mishnah Avot 2:16": (R, "Opened: you need not finish the work; the employer pays. Wage theme, 103:3-adjacent; no page claim.", []),
 "Mishnah Avot 2:4": (R, "Opened: Hillel: do not separate from the community. Close to ¶25 but Avot 1:14 states the self/others structure more exactly; duplicate.", []),
 "Mishnah Avot 3:1": (R, "Opened: know before whom you will give account and reckoning (דין וחשבון). Generic reckoning formula; Avot 3:16's open ledger carries ¶7.", []),
 "Mishnah Avot 3:15": (R, "Opened: all is according to the majority of deeds. The majority principle is presented more concretely in Kiddushin 40b at ¶13.", []),
 "Mishnah Avot 3:16": (A, "Opened: the shop is open, the ledger open, the hand writes, collectors exact payment 'with or without his knowledge'. Shares ¶7's ledger read regardless of the person's awareness.", ["S103-TEV-MTF-005"]),
 "Mishnah Avot 4:1": (R, "Opened: who is rich? he who rejoices in his lot. Defines wealth by contentment (a feeling), the opposite axis of ¶5-7's ledger; no paragraph turns on it.", []),
 "Mishnah Avot 4:16": (R, "Opened: this world a vestibule before the world to come. Generic eschatology.", []),
 "Mishnah Avot 4:17": (R, "Opened: one hour of repentance and good deeds in this world. Time and deeds (103:1/103:3), not 103:2.", []),
 "Mishnah Avot 4:22": (R, "Opened: all is according to the reckoning; you will give account. Generic; covered by Avot 3:16.", []),
 "Rosh Hashanah 16b": (R, "Opened in full: R. Yitzhak's sayings on judgment and R. Kruspedai's three books (wholly righteous, wholly wicked, intermediate). The scale-of-merit point at ¶13 is carried by Kiddushin 40b; the books add no 103:2-specific point.", []),
 "Shabbat 153a": (R, "Opened: R. Eliezer: repent one day before your death, i.e. every day. Time and repentance, not loss or scale.", []),
 "Shabbat 31a": (A, "Opened (later part): Rava: when a person is brought to judgment he is asked first 'Did you deal (buy and sell) in faith?' Shares ¶11's link of market honesty with the great day.", ["S103-TEV-MTF-010"]),
 "Ta'anit 23a": (R, "Opened in full: Honi sleeps seventy years, is not recognised, prays for death; Rava: 'either companionship or death'. Close to ¶25, but Avot 1:14 and Eccl 4:8-10 already carry the point; omitted to keep one block per point.", []),
 "Wisdom of Solomon 5:8": (R, "Opened: Sefaria gives a Hebrew rendering of the Greek book ('what did pride profit us, what did wealth add'). The wicked's late recognition at judgment is not ¶15's unawareness during life; witness is a translation.", []),
 # --- Hebrew Bible
 "WLC:1Sam.16.7": (R, "Opened: man sees the eyes, the LORD sees the heart. Seeing theme; Prov 16:2 carries ¶15's self-judgment vs divine weighing.", []),
 "WLC:1Sam.2.3": (R, "Opened: deeds are weighed (נתכנו); ketiv ולא, qere ולו. Weighing of deeds by God duplicates Prov 16:2 / Ps 62:10.", []),
 "WLC:2Sam.12.4": (R, "Opened: the rich man takes the poor man's lamb. Nathan's parable is not on the page.", []),
 "WLC:2Sam.12.7": (R, "Opened: 'You are the man.' Self-recognition through another's story; the page does not develop it.", []),
 "WLC:2Sam.22.12": (R, "Opened: חַשְׁרַת־מַיִם 'mass of waters'. Root חשר: BDB's Arabic cognate there is 'collect' (ḥ-š-r), not خسر; false friend.", []),
 "WLC:Amos.8.5": (A, "Opened and quoted: to make the ephah small, the shekel great and to falsify the scales of deceit; prophetic indictment of merchants like Shu'ayb's at ¶11.", ["S103-TEV-MTF-009"]),
 "WLC:Amos.8.6": (A, "Opened: buying the poor for silver and the needy for sandals; completes the ¶11 Amos block.", ["S103-TEV-MTF-009"]),
 "WLC:Dan.5.26": (A, "Opened: MENE - God numbered your kingdom; context of the weighing verse used at ¶12.", ["S103-TEV-SYD-004"]),
 "WLC:Dan.5.27": (A, "Opened and quoted: 'you were weighed on the scales and found ḥassîr (lacking)'. Aramaic ḥ-s-r (sound correspondence only) in a scale scene where the person himself is weighed: ¶12.", ["S103-TEV-SYD-004"]),
 "WLC:Dan.5.28": (A, "Opened: PERES - your kingdom divided; the consequence of being found lacking, in the ¶12 block.", ["S103-TEV-SYD-004"]),
 "WLC:Dan.7.13": (R, "Opened: כבר אנש 'one like a son of man'. Aramaic ʾĕnāš corresponds to ins/insan by sound only; the vision shares no scene with the page. keyword-only: ʾ-n-š. Kept as an elenen block at ¶20.", ["S103-TEV-ELN-001"]),
 "WLC:Deut.25.13": (A, "Opened and quoted: two different weights, large and small, in one bag - the two-directional scale of 83:1-3 at ¶11.", ["S103-TEV-MTF-008"]),
 "WLC:Deut.25.14": (A, "Opened: two ephahs, large and small, in one house; same law.", ["S103-TEV-MTF-008"]),
 "WLC:Deut.25.15": (A, "Opened and quoted: a full and just weight, that your days may be long.", ["S103-TEV-MTF-008"]),
 "WLC:Deut.8.9": (R, "Opened: a land where you lack (תחסר) nothing. The cognate root occurs but the verse shares no claim with the page. keyword-only: ḥ-s-r.", []),
 "WLC:Eccl.1.15": (A, "Opened and quoted: 'what is lacking (חסרון) cannot be counted'; ḥ-s-r range for ¶5.", ["S103-TEV-SYD-002"]),
 "WLC:Eccl.1.3": (A, "Opened and quoted: 'what profit (יתרון) has man in all his toil (עמל)?' Commercial surplus question; contrasted at ¶6 (Qohelet's ledger closes without surplus, Asr names an exception).", ["S103-TEV-KRA-001"]),
 "WLC:Eccl.12.14": (R, "Opened: God brings every deed into judgment. Generic.", []),
 "WLC:Eccl.2.11": (A, "Opened and quoted: 'there is no profit under the sun' after reviewing his toil (עמל); ¶6 contrast block; עמל is the sound correspondent of Arabic ʿamal with a different sense (wearisome toil).", ["S103-TEV-KRA-001"]),
 "WLC:Eccl.3.17": (R, "Opened: God will judge the righteous and the wicked; a time for every deed. Generic.", []),
 "WLC:Eccl.4.10": (A, "Opened and quoted: woe to the one who falls with no second to lift him; ¶25 block.", ["S103-TEV-MTF-016"]),
 "WLC:Eccl.4.12": (R, "Opened: a threefold cord is not quickly broken. Context of 4:9-10; no independent addition.", []),
 "WLC:Eccl.4.8": (A, "Opened and quoted: a lone man without second, endless toil, eyes not sated with wealth (ketiv עיניו, qere עינו), 'depriving (מחסר) myself of good'. Shares ¶25 (self lost in solitude) with the ḥ-s-r root.", ["S103-TEV-MTF-016"]),
 "WLC:Eccl.4.9": (A, "Opened: two are better than one, they have a good reward for their toil; ¶25 block.", ["S103-TEV-MTF-016"]),
 "WLC:Eccl.5.13": (R, "Opened: that wealth perished in a bad venture. A genuine commercial loss, but the ¶6 Qohelet point is already made with 1:3/2:11.", []),
 "WLC:Eccl.5.14": (R, "Opened: naked he returns, carrying nothing of his toil. Mortality-of-wealth topos; covered by Luke 12 at ¶9.", []),
 "WLC:Eccl.5.15": (R, "Opened: what profit has he who toils for the wind? Same Qohelet point as 1:3/2:11; duplicate.", []),
 "WLC:Eccl.7.29": (A, "Opened and quoted: God made man upright, but they sought many schemes (חשבנות); with 7:27 (חשבון) opened. Shares ¶3's two vessels: what creation gave and what melts in one's own hands.", ["S103-TEV-MTF-001"]),
 "WLC:Eccl.9.2": (R, "Opened: one fate for righteous and wicked. Concerns death under the sun, not the ledger; Ps 14 carries ¶4's universal verdict.", []),
 "WLC:Exod.13.21": (R, "Opened: pillar of fire by night to guide. Fire as guide resembles 20:10's hope of guidance, but the Exod 3 block already gives the Moses scene; secondary.", []),
 "WLC:Exod.22.21": (R, "Opened: do not afflict widow or orphan. ¶21's 4:6 point is perceiving maturity before handing property. keyword-only: orphan.", []),
 "WLC:Exod.3.1": (A, "Opened: Moses tending Jethro's flock, leads it to Horeb; the frame difference (alone, at work) used in the ¶21 paralel.", ["S103-TEV-PRL-001"]),
 "WLC:Exod.3.2": (A, "Opened and quoted: the bush burning with fire and not consumed; the same scene as 20:10/28:29 at ¶21.", ["S103-TEV-PRL-001"]),
 "WLC:Exod.3.3": (A, "Opened and quoted: 'let me turn aside and see this great sight' - perceiving the fire, with no family or hope of a firebrand/guidance.", ["S103-TEV-PRL-001"]),
 "WLC:Ezek.19.12": (R, "Opened: the vine plucked up, east wind dried its fruit, fire consumed it. Shares wind-fire-fruit imagery with 2:266 but refers to Judah's dynasty; ¶14 mentions 2:266 only in passing; secondary.", []),
 "WLC:Gen.1.31": (R, "Opened: all was very good. The ¶3 'best form' point is carried by Ps 8:5-6 and Eccl 7:29.", []),
 "WLC:Gen.20.18": (R, "Opened: the LORD closed (עצר) every womb. Hebrew עצר 'restrain, shut' vs. Arabic ʿaṣr 'squeeze/time'; false friend for the page.", []),
 "WLC:Gen.3.17": (R, "Opened: in toil you shall eat all your days. Generic toil.", []),
 "WLC:Gen.3.19": (R, "Opened: to dust you return. Generic mortality.", []),
 "WLC:Hab.2.4": (R, "Opened: the righteous shall live by his faith. 103:3 material.", []),
 "WLC:Hag.1.6": (A, "Opened and quoted (1:5 context): wages put into a bag with holes. Shares ¶5's image of a diminution that drains away unseen.", ["S103-TEV-MTF-003"]),
 "WLC:Isa.28.17": (R, "Opened: justice the line, righteousness the plummet. Building measures, not the market scale; theme only.", []),
 "WLC:Isa.40.7": (R, "Opened: grass withers. Generic transience.", []),
 "WLC:Isa.51.12": (R, "Opened: אנוש ימות 'mortal man who dies'. Root occurrence of enosh; the mortality sense is shown with Ps 103:15 at ¶24; duplicate.", []),
 "WLC:Isa.53.6": (R, "Opened: all we like sheep have gone astray. Straying is shown at ¶14 with Ps 119:176 (lost sheep with אבד); duplicate.", []),
 "WLC:Isa.55.2": (A, "Opened and quoted (55:1 context): why weigh silver for what is not bread? Shares ¶8's (2:16) trade where the price paid does not buy what is needed.", ["S103-TEV-MTF-006"]),
 "WLC:Jer.15.18": (R, "Opened: my wound incurable (אנושה). Same homonymous verb as Jer 17:9 already cited at ¶24; duplicate.", []),
 "WLC:Jer.17.10": (R, "Opened: I search the heart, give each according to his ways (ketiv כדרכו, qere כדרכיו). Generic.", []),
 "WLC:Jer.17.11": (R, "Opened: who gets riches unjustly will leave them in the midst of his days (ketiv ימו, qere ימיו). Close to ¶9 but Luke 12 carries it.", []),
 "WLC:Jer.17.9": (A, "Opened and quoted: the heart is deceitful and incurable (ואנש הוא); homonymous ʾ-n-š 'be sick' shown at ¶24 in the enosh range.", ["S103-TEV-SYD-007"]),
 "WLC:Job.12.15": (R, "Opened: he withholds (יעצר) the waters and they dry up. עצר 'restrain' is not Arabic 'squeeze'; false friend.", []),
 "WLC:Job.14.1": (R, "Opened: man born of woman, few of days and full of trouble. Generic.", []),
 "WLC:Job.14.5": (A, "Opened and quoted: 'you set his limit (ketiv חקו, qere חקיו) that he cannot pass'. ḥōq (sound correspondent of ḥaqq) names each person's fixed term: ¶12's last sentence.", ["S103-TEV-SYD-005"]),
 "WLC:Job.14.6": (R, "Opened: like a hireling his day. Context only.", []),
 "WLC:Job.27.16": (R, "Opened: if he heaps (יצבר) silver like dust. צבר 'heap up' is a false friend of Arabic ṣabr; hoarding at ¶9 covered by Luke 12.", []),
 "WLC:Job.31.6": (R, "Opened: let him weigh me in a just balance. The righteous asking to be weighed adds nothing beyond Dan 5:27/Ps 62:10 at ¶12.", []),
 "WLC:Job.34.19": (R, "Opened: no partiality for princes over the poor. Generic.", []),
 "WLC:Job.4.17": (R, "Opened: can mortal man (האנוש) be righteous before God? Root occurrence only. keyword-only: enosh.", []),
 "WLC:Job.7.1": (R, "Opened: hard service for enosh on earth, days like a hireling's (ketiv על, qere עלי). Root occurrence and hireling theme; not a page claim.", []),
 "WLC:Job.7.17": (R, "Opened: what is enosh that you magnify him. The testing theme (76:2 at ¶22) is not the paragraph's point; root use shown elsewhere.", []),
 "WLC:Job.7.18": (R, "Opened: you visit him every morning, test him every moment. Testing theme only.", []),
 "WLC:Job.7.2": (R, "Opened: a hireling waits for his wages. Labour/wage theme.", []),
 "WLC:Job.7.3": (R, "Opened: months of emptiness, nights of trouble (עמל). Root occurrence; Eccl 2:11 shows עמל at ¶6.", []),
 "WLC:Lev.19.17": (R, "Opened: reprove your neighbour. 103:3 mutual counsel.", []),
 "WLC:Lev.19.35": (R, "Opened: no wrong in measure, weight or quantity. Same law as Deut 25:13-15, which carries ¶11 more sharply (two weights).", []),
 "WLC:Lev.19.36": (R, "Opened: just balances, just weights. Duplicate of the Deut block.", []),
 "WLC:Mic.6.10": (R, "Opened: treasures of wickedness and the scant ephah. Prophetic indictment duplicating Amos 8:5 at ¶11.", []),
 "WLC:Mic.6.11": (R, "Opened: wicked scales and a bag of deceitful weights. Duplicate of Amos/Deut at ¶11.", []),
 "WLC:Prov.10.2": (R, "Opened: treasures of wickedness do not profit. Generic.", []),
 "WLC:Prov.11.1": (R, "Opened: a false balance is abomination to the LORD. Duplicate of Deut 25 at ¶11.", []),
 "WLC:Prov.11.14": (R, "Opened: safety in many counsellors. 103:3.", []),
 "WLC:Prov.11.24": (R, "Opened: one scatters and gains; another withholds and comes to want (מחסור). Cognate in a generosity paradox; not the page's point. keyword-only: ḥ-s-r.", []),
 "WLC:Prov.11.4": (R, "Opened: wealth does not profit on the day of wrath. Generic.", []),
 "WLC:Prov.12.15": (R, "Opened: the fool's way is right in his eyes. Same proverb type as Prov 16:2/21:2 used at ¶15; duplicate.", []),
 "WLC:Prov.13.11": (R, "Opened: wealth from vanity dwindles. Generic.", []),
 "WLC:Prov.13.7": (R, "Opened: one pretends to be rich and has nothing. Appearance vs. reality; Rev 3:17 carries ¶15 more exactly.", []),
 "WLC:Prov.14.12": (A, "Opened: a way that seems right to a man, its end the ways of death; cited in the ¶15 block (also 16:25).", ["S103-TEV-MTF-014"]),
 "WLC:Prov.16.11": (R, "Opened: balance and scales of justice are the LORD's. A thin link to 55:7-9; Deut/Amos/Shabbat 31a already carry ¶11.", []),
 "WLC:Prov.16.2": (A, "Opened and quoted: all a man's ways are pure in his eyes, but the LORD weighs spirits - ¶15's self-approved loser and the weighing.", ["S103-TEV-MTF-014"]),
 "WLC:Prov.16.25": (A, "Opened: repeat of 14:12; cited in the ¶15 block.", ["S103-TEV-MTF-014"]),
 "WLC:Prov.16.8": (R, "Opened: better a little with righteousness. Generic.", []),
 "WLC:Prov.21.2": (A, "Opened: every way of a man is right in his eyes, the LORD weighs hearts; variant of 16:2 cited in the ¶15 block.", ["S103-TEV-MTF-014"]),
 "WLC:Prov.22.2": (R, "Opened: rich and poor meet; the LORD made them all. Generic.", []),
 "WLC:Prov.23.4": (R, "Opened: do not toil to acquire wealth. Generic.", []),
 "WLC:Prov.23.5": (R, "Opened: wealth makes wings and flies away (ketiv/qere variants). Generic.", []),
 "WLC:Prov.27.17": (R, "Opened: iron sharpens iron. 103:3 mutual exchange.", []),
 "WLC:Prov.27.19": (A, "Opened and quoted: as in water face answers face, so the heart of man to man - ¶23's seeing oneself through another.", ["S103-TEV-MTF-015"]),
 "WLC:Prov.27.6": (R, "Opened: faithful are the wounds of a friend. 103:3.", []),
 "WLC:Prov.28.22": (A, "Opened and quoted: he hastens after wealth and does not know that want (חסר) will come - ¶7's unnoticed deficit with the ḥ-s-r root.", ["S103-TEV-SYD-003"]),
 "WLC:Prov.28.27": (R, "Opened: who gives to the poor will not lack (מחסור). Cognate occurrence in a generosity saying. keyword-only: ḥ-s-r.", []),
 "WLC:Prov.6.32": (R, "Opened: the adulterer lacks sense (חסר־לב), destroys himself. Cognate refers to lacking sense; adultery context unrelated.", []),
 "WLC:Ps.1.3": (R, "Opened: tree by streams bearing fruit. Belongs to 103:3 (deeds) imagery; not on the page.", []),
 "WLC:Ps.1.4": (R, "Opened: the wicked like chaff driven by wind. Not on the page.", []),
 "WLC:Ps.1.6": (A, "Opened and quoted: the way of the wicked perishes (תאבד); with Ps 119:176 shows one Hebrew verb for straying and perishing: ¶14.", ["S103-TEV-MTF-013"]),
 "WLC:Ps.103.15": (A, "Opened and quoted: enosh, his days like grass - the mortality sense of the Hebrew cognate of insan at ¶24.", ["S103-TEV-SYD-007"]),
 "WLC:Ps.103.16": (R, "Opened: the wind passes and he is gone. Context of 103:15; no independent addition.", []),
 "WLC:Ps.106.30": (R, "Opened: the plague was stayed (ותעצר). עצר 'restrain' false friend.", []),
 "WLC:Ps.14.3": (A, "Opened and quoted: none does good, not even one; with 14:2 (God looks on benê ādām) and 14:5 (the generation of the righteous). Shares ¶4's verdict on the whole species followed by a set-apart group.", ["S103-TEV-MTF-002"]),
 "WLC:Ps.23.2": (R, "Opened: green pastures, still waters. The reader's wording לא אחסר is in 23:1 (opened); the verse itself has no ḥ-s-r; not the page's point.", []),
 "WLC:Ps.39.7": (R, "Opened: man walks as a shadow, heaps up (יצבר) and knows not who gathers. Hoarding without knowing the heir; duplicate of Luke 12:20 at ¶9.", []),
 "WLC:Ps.49.13": (R, "Opened: man in honour does not abide. Covered by Luke 12 at ¶9.", []),
 "WLC:Ps.49.18": (R, "Opened: at death he takes nothing. Covered by Luke 12 at ¶9.", []),
 "WLC:Ps.62.10": (A, "Opened and quoted: on the scales they go up, lighter than breath together; with 62:11. Shares ¶12's light pan where humans themselves are weighed.", ["S103-TEV-MTF-011"]),
 "WLC:Ps.8.5": (A, "Opened and quoted: what is enosh; with 8:6 (ותחסרהו 'made him lack little from God') and 8:7. ḥ-s-r in a scene of human exaltation, contrasted at ¶3.", ["S103-TEV-SYD-001"]),
 "WLC:Ps.90.10": (A, "Opened and quoted: seventy, eighty years, their pride toil (עמל) and trouble; ¶9 block.", ["S103-TEV-MTF-007"]),
 "WLC:Ps.90.11": (R, "Opened: who knows the power of your anger. The reader's עמל wording is in 90:10, not 90:11; this verse shares nothing with the page.", []),
 "WLC:Ps.90.12": (A, "Opened and quoted: teach us to number our days - counting days rather than money, ¶9.", ["S103-TEV-MTF-007"]),
 "WLC:Ps.90.3": (A, "Opened: you return enosh to dust; mortality sense of enosh cited at ¶24.", ["S103-TEV-SYD-007"]),
}

# research (own lookups, context, unsuccessful)
RES = {
 "CORPUSCORANICUM:103:2:anmerkung": (A, "Corpus Coranicum note on 103:2: Torrey 1892 compares eschatological loss with Luke 9:24; Peshitta ḥsar; Phil 3:7-8; used in the modern block.", ["S103-INC-MDR-001"]),
 "CORPUSCORANICUM:103:1-3:kommentar": (A, "Corpus Coranicum commentary: Robinson's reading of ʿaṣr as merchants' end-of-day reckoning, v.2 as eschatological loss; Neuwirth's prayer-time alternative.", ["S103-INC-MDR-001"]),
 "CORPUSCORANICUM-INTERTEXT:103:2:178": (A, "TUK entry Luke 9:23-27 for 103:2 (identified via Torrey); notes Peshitta ḥsar for ἀπόλλυμι.", ["S103-INC-MTF-003"]),
 "CORPUSCORANICUM-INTERTEXT:103:2:179": (A, "TUK entry Phil 3:1-10 for 103:2; notes Syriac ḥusrānā in 3:7-8.", ["S103-INC-MTF-002"]),
 "WLC:Ps.8.6": (A, "Own lookup: ותחסרהו מעט מאלהים; ḥ-s-r in Ps 8, quoted at ¶3.", ["S103-TEV-SYD-001"]),
 "WLC:Ps.8.7": (A, "Context: dominion over the works of your hands; completes the exaltation scene of the ¶3 block.", ["S103-TEV-SYD-001"]),
 "WLC:Eccl.7.27": (A, "Context: 'adding one to one to find the account (חשבון)'; supports the חשבנות remark at ¶3.", ["S103-TEV-MTF-001"]),
 "WLC:Ps.14.2": (A, "Context: the LORD looks down on benê ādām; the whole-species frame of the ¶4 block.", ["S103-TEV-MTF-002"]),
 "WLC:Ps.14.5": (A, "Context and quoted: God is with the generation of the righteous; the set-apart group in the ¶4 block.", ["S103-TEV-MTF-002"]),
 "SBLGNT:Rom.3.10": (A, "Context: Paul's citation 'none righteous, not even one' (Ps 14); ¶4 contrast.", ["S103-INC-KRA-001"]),
 "SBLGNT:Rom.3.12": (A, "Context: 'all turned aside ... not even one' (Ps 14:3 in Greek); ¶4 contrast.", ["S103-INC-KRA-001"]),
 "SBLGNT:Rom.3.22": (A, "Context: righteousness through faith for all who believe; the exit named in the ¶4 block.", ["S103-INC-KRA-001"]),
 "WLC:Gen.8.3": (A, "Own research for root ḥ-s-r: the waters decreased (ויחסרו); ¶5 soydas.", ["S103-TEV-SYD-002"]),
 "WLC:Gen.8.5": (A, "Own research, quoted: the waters went on decreasing (הלוך וחסור); ¶5 soydas.", ["S103-TEV-SYD-002"]),
 "WLC:Hag.1.5": (A, "Context of Hag 1:6: 'consider your ways'.", ["S103-TEV-MTF-003"]),
 "WLC:Isa.55.1": (A, "Context of Isa 55:2: buy without money and without price.", ["S103-TEV-MTF-006"]),
 "SBLGNT:Matt.25.28": (A, "Context: take the talent from him; part of the ¶6 block.", ["S103-INC-MTF-001"]),
 "SBLGNT:Luke.9.24": (A, "Context: whoever would save his life will lose it (the verse Corpus Coranicum cites); ¶8 block.", ["S103-INC-MTF-003"]),
 "SBLGNT:Luke.12.16": (A, "Context: opening of the rich fool parable; ¶9 block.", ["S103-INC-MTF-004"]),
 "SBLGNT:Luke.12.17": (A, "Context: where shall I gather my fruits; ¶9 block.", ["S103-INC-MTF-004"]),
 "SBLGNT:Eph.5.15": (A, "Context of Eph 5:16: walk carefully, not as unwise but wise; ¶9 block.", ["S103-INC-MTF-005"]),
 "SBLGNT:John.9.39": (A, "Context: those who see may become blind; ¶22 block.", ["S103-INC-MTF-008"]),
 "SBLGNT:John.9.40": (A, "Context: 'are we blind too?'; ¶22 block.", ["S103-INC-MTF-008"]),
 "SBLGNT:Matt.3.10": (R, "Context of Matt 3:8-9: the axe at the root of fruitless trees; supplies context but no independent addition.", []),
 "WLC:Ps.62.11": (A, "Context: do not trust in oppression or rising wealth; used in the ¶12 block.", ["S103-TEV-MTF-011"]),
 "WLC:Ps.119.176": (A, "Own research, quoted: I have strayed like a lost (אבד) sheep; ¶14 block.", ["S103-TEV-MTF-013"]),
 "WLC:Deut.32.10": (A, "Own research, quoted: כאישון עינו; Hebrew 'little man of the eye' image at ¶23.", ["S103-TEV-SYD-006"]),
 "WLC:Ps.17.8": (A, "Own research, quoted: כאישון בת־עין; ¶23.", ["S103-TEV-SYD-006"]),
 "WLC:Prov.7.2": (A, "Own research: my teaching as the pupil (אישון) of your eye; third occurrence cited at ¶23.", ["S103-TEV-SYD-006"]),
 "WLC:Eccl.6.2": (R, "Own research for ḥ-s-r: a man lacking nothing for himself yet not allowed to enjoy it; supplies range context but no independent addition.", []),
 "WLC:Ps.23.1": (R, "Checked the reader's wording לא אחסר: it stands in 23:1. 'I shall not lack' is the opposite pole of husr, but no paragraph turns on it.", []),
 "WLC:Ps.23.3": (R, "Context: he leads me in paths of righteousness. Not developed by the page.", []),
 "WLC:Ps.49.12": (R, "Own lookup for ¶9: MT 'their inward thought: their houses forever'. Close to 104:3, but Luke 12 carries the point; the verse's reading would also need discussion.", []),
 "WLC:Ps.39.8": (R, "Context of Ps 39:7 (hope in the Lord); no independent addition.", []),
 "SEFARIA:Pirkei_Avot.3.14": (R, "Context: beloved is man created in the image; checked for the speaker of 3:15-16; no independent addition.", []),
 "SEFARIA:Pirkei_Avot.3.17": (R, "Context: wisdom exceeding deeds like a tree with few roots; 103:3-type point, not used.", []),
 "SEFARIA:Pirkei_Avot.1.12": (A, "Context: Hillel's sayings begin here; supports the attribution of 1:14 in the ¶25 block.", ["S103-TEV-MTF-017"]),
 "SEFARIA:Pirkei_Avot.1.13": (U, "NOT FOUND in the corpus; requested to confirm the Hillel sequence (1:12-14).", []),
 "SEFARIA:Pirkei_Avot.3.13": (U, "NOT FOUND in the corpus; requested to confirm the speaker of 3:16, so the block does not name him.", []),
 "SEFARIA:Ben_Sira.11.17": (U, "NOT FOUND in the corpus; requested while resolving the Sirach 11:19 numbering.", []),
 "SEFARIA:Ben_Sira.11.18": (U, "NOT FOUND in the corpus; requested while resolving the Sirach 11:19 numbering.", []),
 "SEFARIA:Ben_Sira.11.20": (U, "NOT FOUND in the corpus; requested while resolving the Sirach 11:19 numbering.", []),
 # Shell-token artefacts of three combined commands (parsed as locators by the audit); not passages
 "python3": (R, "Not a passage: shell token from a command joined with ';' to a corpus get call; no text was looked up under this name.", []),
 "word": (R, "Not a passage: hebrew.py subcommand token from a command joined with ';' to a corpus get call.", []),
 "/Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py": (R, "Not a passage: tool path token from a command joined with ';' to a corpus get call.", []),
 "/Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py": (R, "Not a passage: tool path token from a command joined with ';' to a corpus get call.", []),
}

# Sefaria locators opened for the named works: their own research verdict mirrors the connection decision
NAMED = {}
for ref, (st, reason, anns) in T.items():
    locs = PRE.get(ref) or []
    for loc in locs:
        if loc.startswith("SEFARIA:"):
            NAMED[loc] = (st if st != U else R, f"Opened for the discovery reference '{ref}'. " + reason, anns)


def local_locs(rid):
    return [x.strip() for x in ANN[rid]["kaynak"].split("|") if x.strip() and x.strip() != "hafiza"]


def evidence_for(ref, status, anns):
    ev = []
    if status == A:
        for rid in anns:
            ev += local_locs(rid)
    if ref.startswith(("WLC:", "SBLGNT:", "SEFARIA:", "CORPUSCORANICUM")):
        ev.append(ref) if status != U else None
    else:
        ev += [l for l in (PRE.get(ref) or []) if status != U]
    for rid in anns:  # rejected rows that carry an elenen block must cover its citations
        if status == R:
            ev += local_locs(rid)
    out = []
    for x in ev:
        if x not in out:
            out.append(x)
    return out


def row(cid, ref, status, reason, anns, research=False):
    paras = sorted({int(ANN[a]["paragraf"]) for a in anns})
    r = {"connection_id": cid, "ref": ref, "status": status, "reason": reason, "paragraphs": paras,
         "evidence": evidence_for(ref, status, anns), "annotations": anns}
    if research:
        r = {"connection_id": None, "origin": "research", **{k: v for k, v in r.items() if k != "connection_id"}}
    return r


rows = []
with open(DISC / "103_2.merged.tsv") as f:
    for tsv in csv.DictReader(f, delimiter="\t"):
        ref = tsv["ref"]
        st, reason, anns = T[ref]
        for item in json.loads(tsv["evidence"]):
            note = f" [reader {item['model']} line {item['line']}: {item['kind']}, '{item['basis']}']"
            rows.append(row(item["connection_id"], ref, st, reason + note, anns))
for ref, (st, reason, anns) in {**RES, **NAMED}.items():
    rows.append(row(None, ref, st, reason, anns, research=True))
(D / "verdicts.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
print(len(rows), "rows")
missing = [k for k in T if k not in {r["ref"] for r in rows}]
print("table refs unused:", missing)
