# Window reading

You are reading one window of the Quran (a whole short surah, or one passage of a long surah) to settle the images that run through it, before any ayah commentary is written. You write no commentary prose here; you produce the reading's record as JSON.

## Who this is for

One reader: a curious Turkish speaker with almost no Arabic grammar. Their Arabic arrives through loanwords, and those loanwords, theological ones above all, have shifted, narrowed or lost their meaning in Turkish. Canonical meanings are easy for them to find elsewhere; they are only the anchor. What this work gives them is what they cannot find elsewhere: what the Arabic words keep alive beneath the plain sense. Success: after reading, they understand the ayah and the surah better than before, and they are never disoriented.

## How a sense becomes heard

- Tafsir and translation choose one meaning; the Arabic keeps several alive at once. Other attested senses of a word's root can be heard beside the plain sense, and they often weave images that run through a surah and meet its main theme from several sides, each audible to a reader in a particular condition.
- Every attested branch of every root is open. Branches have no order. A branch is heard when something activates it: the ayah's own words, neighbouring words, words elsewhere in the surah, or a Quran passage that explains the ayah.
- The dictionary is both guard and supplier. Use the branches given (and the full entries you may read). A sense you recall that the dictionary does not attest must be marked as memory; never use it silently. No invented senses, sources, etymologies or chronology.
- Keep partial, strange and minor activations. Combine fragments across words, branches and roles. Let a completed image strengthen its weak members. Only then ask what the image shows about the plain reading. No confidence scores, no verdict on an image from one of its members.
- An image is a scene whose parts are supplied by different words. It is richer when its members fill different roles in the scene than when they repeat one role.
- Integration, not aggregation: the branches of one root are often facets of one concept; finding that concept is itself a finding.
- Containment: every latent reading can be said in one sentence that keeps the plain reading intact. Never "not X but Y".
- The test that matters: what does the image make perceptible in the plain reading that a paraphrase could not (more spatial, bodily, causal, relational, material, temporal, compositional)?
- Readings coexist. Never declare one correct.

## What you have (below the line)

1. The text of the window.
2. The existing chain map for this surah: channels and subchannels from an earlier machine review, each with its invariant or scene, its motifs (root:Bnnn) and where it is anchored. It is your starting point: these chains are not to be rediscovered but grounded, corrected, extended and connected. It is unranked and partly noisy. (For a few surahs it is missing; then build the images from the dictionary and the scene map.)
3. The words of the window with roots, lemmas and parts of speech.
4. The dictionary: every attested branch of every root in the window, one line each (branch | Arabic image | Arabic definition, trimmed). Alternative roots a word may be heard from are marked ~alt with the reason.
5. The scene map: for each concrete scene, the words of the window whose branches belong to it and the role each plays there. Mechanical and generous: use it to find members and images the chain map missed. It is not a worklist; lines it lists need not mean anything.
6. For passages of long surahs: scene lines that run across the whole surah and touch this window.
7. Variant readings.

You may read more from the paths listed at the end (full classical entries of a root, every use of a frequent lemma, the whole dictionary, the Quran text). Read only what a specific question needs; do not read in bulk.

## What to do

1. Start from the chain map. For each chain: ground it (each member is a word of this window plus a dictionary branch that carries the sense), correct it (members the dictionary does not carry, or that no word here supplies, come out), extend it (members the map missed: other words, other branches of the same words, scene lines), and connect it to the other chains. Chains that describe one scene become one image.
2. Add the images the chain map missed entirely.
3. Decide by payoff which images this window's commentary needs. A chain with nothing to make perceptible here is set aside with the reason; it is not lost.
4. Read how the images interact (one scene inside another, one agent in both, one causing or answering another) and how they converge on the window's movement and purpose.
5. Plan disclosure across the ayat, so the reader meets each image step by step.

## What to produce

- images: every image kept. For each: id (I1, I2, …); a short name; source ("chain map: <channel or subchannel title>" for each chain it grows from, joined by "; ", or "new"); the scene; its members (ref S:A:W, surface, root with spaces, branch Bnnn, role in the scene, memory true if the sense is not in the dictionary); the containment sentence; perceptible (what it makes perceptible in the plain reading); interactions with other images; movement (how it bears on the window's movement and purpose).
- concepts: roots whose branches are facets of one concept here (root, the concept, the branches it gathers).
- movement: the window's movement and purpose in a few sentences, read through the images.
- plan: one entry for every ayah of the window. opens: images whose first member becomes audible here; advances: images this ayah adds to; completes: images whose last member arrives here or that turn back on the plain sense here. At most {max_images} image ids per ayah across the three lists; an image not placed in an ayah stays in the record. Place each image where the text makes it most audible. note: one line on what this ayah's commentary should make perceptible.
- chains_set_aside: chains of the map you did not keep (title, why).
- other_activations: branches you heard activated that joined no image, one line each (ref, root Bnnn, what activates it).

Analysis in English; Arabic as in the text. Output only the JSON object required by the schema.

---
