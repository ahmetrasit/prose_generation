# V9 Luna lane — worklist judge

You judge one worklist of items for one Quranic ayah. You do not write prose. Your records are the only
thing a later writer sees, so a finding you skip is lost.

## Inputs

The launch message contains, in full: this brief, `context.md` (the focus ayah with its words and anchor
translation, the Fatiha — recited in every salah — and the whole host surah) and your worklist. Everything
is already in front of you: do not read these files again from disk. Work through the worklist from its
first item to its last.

## Judge every item

An item proposes that something activates a latent sense in the focus ayah: a dictionary branch with its
image partners (R…B…), a word's Quranic usage (R….U), a precomputed hypothesis (H…), a lead (L…), or
another ayah (G…). The canonical meaning is known; you look for what is latent.

- **reading** — two keys hold: (1) a sense the dictionary gives (or the Quranic usage shows), and (2) an
  independent trigger — an actual word in the focus ayah, its surah, the Fatiha or the other ayah — that
  activates it. Rare, surprising and multi-step links are welcome when both keys hold. Polysemy is allowed:
  a rare branch (an eye disease, a mountain, kohl) can be heard beside the plain sense when a trigger
  calls it.
- **note** — real but one key only: a striking branch with a weak trigger, or a strong trigger for a
  sense the dictionary only half gives.
- **none** — with a code: `no-trigger` (a branch nothing calls), `noise` (the pairing is accidental),
  `canonical` (only the plain sense, nothing latent), `wrong` (the listed link misreads the Arabic), or
  `same-as:<id>` (the same point as an earlier record).

**A miss costs more than a false alarm.** A later writer verifies every record and drops what does not
hold, but can never recover a line you coded `-`. The trigger is the partner word itself, or the concept
word a path runs through: when the dictionary branch is real and that word carries its image (an eye
branch paired with a word for looking, blinding or sight; a night-blindness branch joined through
"night" to a word for dwelling at night), code the line `n` or `r`. Do not require the other ayah to
spell the image out ("no eye is mentioned" is not a reason for `-`). Keep `-` for pairings whose
images do not meet.

For inter-ayah items (G…) the review labels are earlier judgements, not decisions: judge whether the
other ayah's actual words activate or move something in the focus ayah. For HFT items (H…) check each
trace step against the Arabic. An echo root is a sound-family candidate, never the word's identity.

Beyond the list: when reading shows you a link no item proposes (a word in the surah that calls a
branch, two items that join into one image), add a record with id `X<n>` (X1, X2, …).

## Numbered evidence lines

Branch and usage items (R…) list their evidence as numbered lines `[1] … [n]` (the heading says
`lines: n`). Judge every line on its own: does this partner, concept path, Fatiha pair or bridge activate
the branch? Give the item a `lines` string with exactly one code per line, in order: `-` nothing,
`n` note, `r` reading. Every `n` or `r` line gets its own full record with id `<item>.<k>` (the line's
number). A concept line's value is its path: say which concept (night, eye, road…) carries the image to
which word. A branch whose own ayah activates it beyond the listed lines also gets a verdict on the item
record itself; an item with `lines: 0` always needs a verdict.

## Records

Write one JSON object per line to `records/<worklist stem>.jsonl` in the work directory (for
`W1_branches_3.md` → `records/W1_branches_3.jsonl`), in one or two file writes. Fields:

```
{"id": "R03.B002", "verdict": "reading", "focus_ar": "مَّسَٰكِنِهِمْ", "branch": "س ك ن B002",
 "trigger_ar": "بَيْتًا", "trigger_ref": "29:41",
 "before": "their dwellings (plain)", "after": "the image the reading hears",
 "reason": "which words do what: the specific Arabic words, the branch image, and how the trigger calls it",
 "code": ""}
{"id": "R03.B007", "lines": "--------", "verdict": "none", "code": "no-trigger"}
{"id": "R10.B001", "lines": "r-------r------"}
{"id": "R10.B001.1", "verdict": "reading", "focus_ar": "مُسْتَبْصِرِينَ", "branch": "ب ص ر B001", …}
{"id": "R10.B001.9", "verdict": "reading", …}
```

- `focus_ar`: the word of the focus ayah, copied from it. `trigger_ar`: the activating word(s), copied
  from the ayah in `trigger_ref` (one `S:A`; for a trigger inside the focus ayah use the focus reference).
- `reason`: specific to this item — name the Arabic words and the image. Never reuse a sentence; if two
  items make one point, keep the better one and mark the other `same-as`.
- English or Turkish, short sentences. Readings need at least two sentences of substance.

## Finish

Run `python3 _commentary/v9/luna/check_records.py <work dir> <worklist name>` from the repository root and
fix every problem it reports (missing ids, empty fields, Arabic not found in the cited ayah, repeated
sentences). Stop when it prints `ok`.
