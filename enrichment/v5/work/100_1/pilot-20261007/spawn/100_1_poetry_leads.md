<!-- agent /root/v5p_100_1_poetry_leads | model gpt-6-astra | effort high | service default | fast off -->

# v5 memory leads: poetry, 100:1

You suggest where the poetry corpus should be searched. You do not write commentary and nothing you write is published; a script searches the corpus for your leads and a writer reads only what the corpus actually holds. Keep gpt-6-astra, high effort; do not spawn agents or change the task.

Use learned knowledge only. No web, repository or corpus access; no other runs or outputs. The only command you use is:

`python3 -B enrichment/v5/read.py enrichment/v5/work/100_1/pilot-20261007/poetry input N` for N = 1 … 4, once each, separately.

The page is the frozen Turkish commentary on 100:1, 22 paragraphs. Family purpose: Poetry witnesses: direct lexical attestations for the supplied words and concrete images, with poem or collection attribution and commentator gloss where available. Distinguish direct word evidence from thematic parallels; do not substitute a famous general horse poem for an actual lexical witness. Address all substantial paragraph findings.

Roster (works the corpus holds for this family): MUALLAQAT (al-Zawzanī, Sharḥ al-Muʿallaqāt al-sabʿ); MUFADDALIYYAT (al-Mufaḍḍal al-Ḍabbī, al-Mufaḍḍaliyyāt); ASMAIYYAT (al-Aṣmaʿī, al-Aṣmaʿiyyāt); HAMASA (al-Marzūqī, Sharḥ Dīwān al-Ḥamāsa (Abū Tammām's Ḥamāsa with al-Marzūqī's commentary))

For each paragraph, list concrete remembered items from these works (or clearly relevant others) that bear on its findings: a verse of poetry with a key word, a hadith with its distinctive wording, a named author's specific analysis, a classification entry. What makes a lead useful is **search terms that will occur in the source text itself**: the Arabic word forms, a distinctive phrase of the verse or matn, the narrator's name, an entry heading. Give two to five terms per lead, each one to three words, in the source's language and script. Prefer distinctive terms over common ones. Include uncertain leads and say they are uncertain; a lead that finds nothing costs nothing.

Write only `enrichment/v5/work/100_1/pilot-20261007/poetry/leads/leads.jsonl`, one object per lead:
`{"p":[5],"author":"…","work":"…","claim":"one line, what you remember","terms":["كنود","جزاء بنعمى"],"confidence":"high|medium|low"}`

Stop after the file. Report the number of leads.
