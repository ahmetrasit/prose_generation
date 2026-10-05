# Group lugat: the lexicon of the bound roots

Your material is the project dictionary's section for each ayah (PROJE: every attested branch of every bound root,
early phrases whole), built from the six classical lexica (AYN, JAMHARA, TAHDHIB, SIHAH, MAQAYIS, MUFRADAT). It is
authoritative for senses; root identity comes from PACK/binding.json only. The commentary was written from it, so do
not restate what the commentary already says from it.
Write lugat blocks (sozluk) where a lexicon's own evidence adds to the page: a sense or branch the commentary uses
without its witness, literal versus figurative (ASAS), near-synonyms (FURUQ), Maqāyīs's uṣūl, a shāhid verse,
and evidence against a lexical claim of the commentary. For each block you write, open the entry you cite: the six
classical lexica in PACK/roots/<root_id>.md (Read with offset and limit at that lexicon's section), the further
lexica with `corpus.py get` (LISAN, LANE, ASAS, QAMUS, TAJ under the root's letters, e.g. LISAN:حمد). MUHIT, VASIT,
HANSWEHR are modern Arabic: only inside anlam_tarihi, as evidence of later drift. These openings count against your
8 further calls; list them in gaps.json "searches". Put each block on the page of the ayah whose word it concerns.
