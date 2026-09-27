# The brief (v12 surah pass): the surah's image chains, where they meet, and what they make of the surah (Turkish)

Everything above this brief is evidence, not yet judged:
- **context.md**: the whole surah (or the passage this pass covers) and the Fatiha.
- **channels.md**: the surah's image chains as an earlier whole-surah review mapped them.
- **hft.md**: earlier readers' image-chain hypotheses for every ayah, with their traces checked by script
  (`[!]` = a broken trace step).
- **branch_table.md**: every attested branch of every root in the surah or passage.
- **usage.md** (when present): root dossiers for roots that recur here: each root's occurrences in this window with
  the Quran-wide usage group (stated context) each belongs to. A concordance, not an interpretation; the occurrence
  lists are exact (script), the grouping and branches are a model's and possibly wrong (check what you build on; a
  group's size means nothing). Ledger lines beginning `usage.md:` are the ayah writers' corrections of it.
- the **ledger of every ayah** (S_A.ledger.md), each written with the chain map in view. Their `Chains` lines say how
  each ayah's word takes part in the known chains and whether it holds; their `New` lines hold readings the map
  lacked; their Quran, Usage and Limits lines hold the passages that ground or bound them.

## What this pass is for

One reader: a curious Turkish speaker with almost no Arabic grammar, whose Arabic arrives through loanwords whose
theological meanings have shifted in Turkish. They have the ayah readings. This pass gives what no single ayah can:
the image chains that run through the surah, how the chains **interact** (not silos: one figure can
play a role in two chains at once, and one word can carry branches of two chains), what each ayah
and word contributes, and the surah's movement and purpose (al-Biqāʿī's *naẓm* and *maqṣūd*). Holistic, but the
reader's feet stay on the ground: they must understand the surah better afterwards and never be disoriented.

The chains are already known (channels.md, hft.md). Do not rediscover or re-list them. **Ground** them (where the
Quran tells the same scene openly; what limits them), **correct** them (take the ayah ledgers' judgements into
account), **connect** them (where they meet, and what the meeting shows), and **go beyond** them: the ledgers' New
lines, and readings that only the whole surah shows — an image begun in one ayah and completed, reversed or answered
in another; a root, sound or form that returns in a new role; a scene spread over several ayat. The familiar
interpretation is the anchor, not the measure; a supported surprise is the aim; rigour comes from exact evidence,
not from caution. Readings coexist: nothing is ranked, and every reading keeps the plain meaning intact.

You may use any branch in branch_table.md (cite it `root Bnnn`), any finding in the ledgers, the chain map, and the
Quran from your own knowledge (quotations are checked afterwards). A chain the ayah ledgers did not take up is not
refuted by that; judge it on the evidence. No invented senses, sources, etymologies or chronology.

## Your final message: three parts, with these exact marker lines

===== CHAINS =====
===== SURAH =====
===== AYAT =====

### Part 1 — chains (a record for the editor)

Every chain that runs across two or more ayat, as many as the surah supports, strongest first. For each:

`### <short name>`
`- ayat: S:A, S:A, …` (the members, in the order the chain moves)
`- parts: <for each member: the word, its branch (root Bnnn) or finding, and its role — source, conduit, guide,
pressure, release, container, witness, loss, reversal …>`
`- movement: <how the parts act on one another across the ayat>`
`- meets: <the other chains it meets, at which word or ayah, and what the meeting shows>`
`- staging: <where the Quran tells this scene openly, S:A refs>`
`- limits: <ayat that bound or complicate it>`
`- changes: <what the surah says through this chain that no single ayah says>`
`- grade: core | develop | note`
`- sources: <channels / HFT records it grounds or corrects, and ayah-ledger findings it builds on, by ayah; mark
what is new>`

Name mechanisms, not themes: a chain is complementary roles in motion, not a list of words from one field.

### Part 2 — the surah's reading (Turkish, for a reader who may or may not know the surah)

The reader has said a compressed summary is impossible to follow: they cannot see what comes from where. So be
explicit, in this order:

1. **The plain walk** (`##` heading): what the surah says in its plain sense, ayah group by ayah group, briefly —
   so that a reader who does not know the surah is oriented before any latent reading.
2. **The question the surah answers**: its purpose (*maqṣūd*) as the chains will show it, in a short paragraph.
3. **Every core chain in its own section** (`##` heading): walk the reader through it — which ayah, which word,
   which attested sense of that word (show the Arabic in a tag), what role it plays, how it hands on to the next
   member, where the Quran tells the same scene openly, what bounds it, and what the reader now hears in the plain
   reading that they could not hear before.
4. **Where the chains meet** (`##` heading): the words and ayat where two or more chains cross, and what each
   crossing makes perceptible; then the surah's picture as the chains draw it together — one picture, not a list.
5. `develop` chains more briefly, in their own sections or together.
6. **Close** with the surah's purpose as the chains have shown it, and how the surah leads into the next one.

Do not retell the ayah readings; the reader has them. There is no length limit: explicitness is the requirement.
Internal labels, branch IDs, file names, earlier readers and workflow language do not belong in the prose.

Arabic in the reading is written `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık, source:…}`: `source` is the
ayah it is quoted from (`source:24:35`) or the dictionary branch it is copied from (`source:ن و ر B005`), several
items comma-separated. No comma inside ar or tr, no colon inside gloss, no curly braces elsewhere. After a quotation
from another ayah also cite `(S:A)` in the prose.

### Part 3 — for each ayah

`- S:A: <one to three sentences: where this ayah stands in the chains, and what the whole surah adds to it>`
