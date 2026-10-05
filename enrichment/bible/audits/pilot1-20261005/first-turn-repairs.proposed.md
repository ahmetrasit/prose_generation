# S1 Bible pilot: proposed first-turn corrections

Status: proposed, not applied. All raw reader files remain unchanged. These are locator/schema repairs, not verification or acceptance of the proposed connections.

The present runbook permits recorded repairs only for follow-up references; first-turn failures require a fresh attempt. Applying this proposal requires an explicit exception and Bible-only repair support preserving the original rows and hashes.

| Target | Reader | Line | Original | Proposed |
|---|---|---:|---|---|
| sec5 | terra | 17 | `WLC:Ps.138.9` | `WLC:Ps.138.8` |
| sec5 | terra | 28 | `WLC:Ps.103.23` | `WLC:Ps.103.22` |
| sec5 | terra | 74 | `WLC:Ps.90.18` | `WLC:Ps.90.17` |
| sec6 | terra | 27 | `SBLGNT:Jude.5` | `SBLGNT:Jude.1.5` |
| sec6 | terra | 31 | `WLC:Ps.90.18` | `WLC:Ps.90.17` |
| sec9 | terra | 70 | `WLC:Ps.16.12` | `WLC:Ps.16.11` |
| sec12 | luna | 22 | `tradition=karsi_anlati; kind=tevrat` | `tradition=tevrat; kind=karsi_anlati` |
| sec13 | luna | 61 | `WLC:Ps.90.18` | `WLC:Ps.90.17` |
| sec14 | luna | 57 | `WLC:Joel.2.31` | `WLC:Joel.3.4` |
| sec14 | luna | 58 | `WLC:Joel.2.32` | `WLC:Joel.3.5` |
| 1:2 | luna | 22 | `WLC:Wis.13.1` | `Wisdom of Solomon 13:1` |
| 1:2 | luna | 23 | `WLC:Wis.13.3` | `Wisdom of Solomon 13:3` |
| 1:2 | luna | 24 | `WLC:Wis.13.5` | `Wisdom of Solomon 13:5` |

All corrected canonical locators were checked against the local WLC/SBLGNT text. The three Wisdom rows become named-work candidates with a missing original-witness gap; they do not become WLC or Greek evidence.

The adjacent JSON contains every complete before/after row, rationale, local evidence and original-file hash. Strengths, connection meanings and explanations remain unchanged.
