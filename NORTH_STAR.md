# North star

Written 2026-09-26 from the user's own statements (`ultimate goal.txt`, README "Who this is for",
`COMMENTARY_SPEC.md`, `PRINCIPLES.md`, `_commentary/v9/DESIGN.md`, `latent_activation/main goal.txt`, and the V11
conversations). Every workflow decision is judged against this page.

## The reader

One reader: a curious Turkish speaker with almost no Arabic grammar, whose Arabic arrives through loanwords, and
whose theological loanwords (oku, ibadet, âlem, salât …) have shifted, narrowed or lost their meaning in Turkish.
Canonical meanings are easy to find elsewhere; they are only the anchor. **The goal is what cannot be found
otherwise.**

**Success:** the reader understands the ayah and the surah better after reading than before, and is never
disoriented.

## The question

What would al-Khūlī / Bint al-Shāṭiʾ (a word through all its Quranic uses and all its root's attested senses),
al-Biqāʿī (*naẓm*: an ayah through its neighbours and its surah's purpose) and the Quran-explains-the-Quran
tradition produce today, with a dictionary of every attested branch of every root and with AI agents? Their
ultimate explanation of the Quran is the target, applied systematically and without timidity: a supported surprise
is the aim, and rigour comes from exact evidence, not from caution.

## Three layers

1. **Primary reading.** Not disorienting, while showing what each Turkish word loses or adds against the Arabic
   concept (iqraʾ is more than "oku").
2. **The ayah.** What each word does in building the ayah (what Turkish or English grammar hides), its other
   attested senses, and how the Quran explains it elsewhere: supporting passages and limiting ones.
3. **The surah.** The image chains that run through the surah, how the chains **interact** with one another
   (not silos: e.g. the traveller on the road is also the one kept alive by water in the desert), what each ayah
   and word contributes, and the surah's movement and purpose. Mature chains are disclosed briefly in the ayah
   readings through the word that carries them; the surah reading develops them explicitly, showing what comes
   from where. Holistic, but the reader's feet stay on the ground.

## The "aha"

Non-canonical but supported readings, **explained and connected, never catalogued**: Fatiha as a traveller's
prayer (way-marks in ʿālamīn, the road's middle and the lead animal in mālik, the trodden road in naʿbudu, the road
that swallows its travellers in ṣirāṭ, the stray whose rabb is unknown in ḍāllīn), the water that keeps the
traveller alive, the herd led by its rabb; S100's running horses becoming part of the surah's argument; ṣalāh
heard beside "the one who comes second in a race" among those who tried to outrun (29:39–45).

## Guardrails

- **No disambiguation.** Readings coexist; nothing is ranked or declared the correct one.
- **Containment.** Every latent reading is stateable in a sentence that keeps the primary reading intact
  (never "not X but Y").
- **Checkable.** Every unusual claim has a visible anchor: the Quran passage (and, where it exists, a passage
  where the Quran tells the same scene openly) or the dictionary root and branch. Every Arabic quotation carries
  its source (`source:S:A` or `source:root Bnnn`), which the reader app can show on hover and link to the
  dictionary.
- **No invention.** No invented senses, sources, etymologies or chronology.

## Building on what exists

The HFT track and the surah channel reviews (quran-data `channels/network-v3/sNNN/review`, 110 surahs) already hold
the image chains. They are not rediscovered: they are grounded (Quranic tellings, limits, cautions), extended or
corrected from the dictionary where needed, connected to one another, and delivered into the prose.

## Economics

v5 already gives a catalogue plus synthesis at lower cost; it is a reference, not the target. The new workflow is
worth running only if it **materially and significantly exceeds v5** on this reader's criterion. Tests may cost up to
$5 per ayah; production aims toward ~$1 per ayah on average (API batch mode, a shared cached surah prefix). Input is
cheap when it helps thinking without diluting attention; thinking is welcome; output is welcome when it earns its
place (prose as long as needed; no redundant ledger cost).
