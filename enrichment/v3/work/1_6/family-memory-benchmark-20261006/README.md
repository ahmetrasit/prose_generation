# 1:6 memory-family token benchmark

Native cumulative per-agent usage; parent orchestration and assembly are excluded. Input includes cached reads; output includes reasoning. Counts are not a measure of scholarly accuracy.

| Lane | Completed | Input | Cached input | Uncached input | Output | Reasoning | Blocks | API-equivalent USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| astra-high | 4/4 | 1,019,238 | 882,176 | 137,062 | 44,019 | 13,776 | 53 | $4.4537 |
| astra-max | 4/4 | 1,142,932 | 939,520 | 203,412 | 102,612 | 70,627 | 65 | $8.1042 |
| luna6-max | 19/19 | 5,414,467 | 4,518,656 | 895,811 | 302,961 | 227,901 | 225 | $0.2862 |
| sol-high | 19/19 | 5,981,474 | 5,377,152 | 604,322 | 150,111 | 53,459 | 274 | $3.7852 |
| sol-max | 4/4 | 1,176,767 | 1,008,768 | 167,999 | 66,168 | 44,432 | 68 | $1.1994 |

Full per-agent figures are in [usage.csv](usage.csv) and [usage.json](usage.json).

Cost equivalents use [official Standard API pricing](https://developers.openai.com/api/docs/pricing), with no cache writes recorded in these runs. Output includes reasoning. These are not account billing figures.

The Sol spot review is in [SOL_SPOT_REVIEW.md](SOL_SPOT_REVIEW.md). No baseline blocks were revised following that review.

The matched Luna/Sol spot comparison is in [LUNA_SOL_SPOT_COMPARISON.md](LUNA_SOL_SPOT_COMPARISON.md).

The four-family Sol effort comparison is in [SOL_EFFORT_COMPARISON.md](SOL_EFFORT_COMPARISON.md).

The Astra spot comparison is in [ASTRA_SPOT_COMPARISON.md](ASTRA_SPOT_COMPARISON.md).

The Astra high/max comparison is in [ASTRA_EFFORT_COMPARISON.md](ASTRA_EFFORT_COMPARISON.md).

The first three Sol tasks needed a path clarification; their extra calls remain included. Agents received the complete page in four separate deliveries. Common instructions and runtime context repeat across calls. Agent count or block count alone does not establish quality or efficiency.

## Matched four-family comparison

Bayani, classical coherence, meal, and hadith; one run per family per lane. Sol high versus Sol max and Astra high versus Astra max change reasoning effort within each model. Other lane comparisons also change the model. Fresh contexts received byte-identical prose and source rosters; outputs were kept separate.

| Lane | Completed | Input | Output | Reasoning | Visible output | Blocks | Prose words | API-equivalent USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| astra-high | 4/4 | 1,019,238 | 44,019 | 13,776 | 30,243 | 53 | 6,742 | $4.4537 |
| astra-max | 4/4 | 1,142,932 | 102,612 | 70,627 | 31,985 | 65 | 8,880 | $8.1042 |
| luna6-max | 4/4 | 1,066,209 | 66,868 | 51,708 | 15,160 | 58 | 3,349 | $0.0594 |
| sol-high | 4/4 | 1,190,503 | 31,007 | 11,432 | 19,575 | 64 | 4,734 | $0.7790 |
| sol-max | 4/4 | 1,176,767 | 66,168 | 44,432 | 21,736 | 68 | 5,524 | $1.1994 |

## astra-high

| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |
|---|---:|---:|---:|---:|---:|---:|
| bayani | 228,369 | 189,568 | 9,853 | 5,036 | 6 | $1.070228 |
| classical-coherence | 275,002 | 243,840 | 9,647 | 2,824 | 7 | $1.037810 |
| hadith | 228,833 | 197,888 | 9,871 | 1,602 | 6 | $1.000888 |
| meal | 287,034 | 250,880 | 14,648 | 4,314 | 7 | $1.344820 |

## astra-max

| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |
|---|---:|---:|---:|---:|---:|---:|
| bayani | 240,328 | 177,280 | 24,471 | 16,903 | 6 | $2.031310 |
| classical-coherence | 231,829 | 196,480 | 15,373 | 11,197 | 6 | $1.318620 |
| hadith | 265,343 | 219,776 | 25,442 | 16,325 | 7 | $1.947546 |
| meal | 405,432 | 345,984 | 37,326 | 26,202 | 8 | $2.806764 |

## luna6-max

| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |
|---|---:|---:|---:|---:|---:|---:|
| academic | 248,970 | 206,848 | 16,995 | 12,187 | 7 | $0.014778 |
| analytical | 250,274 | 208,384 | 18,264 | 11,093 | 5 | $0.015405 |
| bayani | 233,063 | 192,768 | 17,528 | 11,607 | 6 | $0.014721 |
| classical-coherence | 235,988 | 198,144 | 8,710 | 7,250 | 5 | $0.010121 |
| grammar | 438,806 | 363,264 | 21,495 | 16,718 | 8 | $0.021934 |
| hadith | 259,770 | 212,480 | 22,220 | 18,935 | 5 | $0.017964 |
| historical | 237,208 | 203,264 | 11,376 | 8,007 | 5 | $0.011115 |
| imami-mutazili | 275,984 | 234,240 | 17,642 | 12,821 | 8 | $0.015338 |
| ishari | 215,758 | 179,712 | 10,465 | 8,842 | 5 | $0.010634 |
| kessaf | 249,793 | 211,968 | 15,688 | 11,895 | 7 | $0.013746 |
| meal | 337,388 | 292,352 | 18,410 | 13,916 | 9 | $0.016632 |
| modern-coherence | 477,265 | 433,920 | 14,547 | 11,167 | 12 | $0.015947 |
| modern-tafsir | 269,304 | 230,144 | 13,435 | 8,472 | 8 | $0.012935 |
| poetry | 188,381 | 137,984 | 13,447 | 11,617 | 4 | $0.013143 |
| qiraat | 224,884 | 176,384 | 10,248 | 8,741 | 6 | $0.011738 |
| rhetoric | 436,666 | 382,720 | 18,662 | 12,977 | 8 | $0.018553 |
| rivayet | 346,397 | 275,456 | 27,426 | 22,057 | 7 | $0.023562 |
| turkish-tafsir | 270,106 | 199,936 | 10,366 | 6,563 | 6 | $0.014199 |
| wujuh | 218,462 | 178,688 | 16,037 | 13,036 | 5 | $0.013783 |

## sol-high

| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |
|---|---:|---:|---:|---:|---:|---:|
| academic | 337,245 | 307,712 | 8,339 | 4,861 | 9 | $0.203998 |
| analytical | 277,948 | 244,352 | 7,531 | 1,694 | 8 | $0.191372 |
| bayani | 271,739 | 242,048 | 8,975 | 1,597 | 7 | $0.197542 |
| classical-coherence | 287,096 | 249,600 | 4,695 | 2,101 | 6 | $0.171862 |
| grammar | 302,821 | 270,464 | 8,736 | 3,754 | 7 | $0.206167 |
| hadith | 339,565 | 306,944 | 9,471 | 4,109 | 9 | $0.221341 |
| historical | 240,910 | 213,376 | 6,074 | 2,933 | 7 | $0.158483 |
| imami-mutazili | 288,292 | 259,968 | 7,555 | 2,682 | 8 | $0.184192 |
| ishari | 287,053 | 259,456 | 7,389 | 2,472 | 8 | $0.180975 |
| kessaf | 433,072 | 399,744 | 8,506 | 2,447 | 13 | $0.231665 |
| meal | 292,103 | 263,680 | 7,866 | 3,625 | 8 | $0.188242 |
| modern-coherence | 285,053 | 257,408 | 6,236 | 1,577 | 8 | $0.169132 |
| modern-tafsir | 296,200 | 261,248 | 13,099 | 4,496 | 8 | $0.253144 |
| poetry | 284,970 | 256,384 | 5,749 | 3,262 | 8 | $0.165939 |
| qiraat | 242,019 | 214,528 | 7,206 | 3,838 | 7 | $0.169948 |
| rhetoric | 289,460 | 260,736 | 7,796 | 1,818 | 8 | $0.187555 |
| rivayet | 590,640 | 533,760 | 10,012 | 2,499 | 15 | $0.320632 |
| turkish-tafsir | 405,980 | 375,424 | 7,880 | 1,893 | 10 | $0.214997 |
| wujuh | 229,308 | 200,320 | 6,996 | 1,801 | 5 | $0.168000 |

## sol-max

| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |
|---|---:|---:|---:|---:|---:|---:|
| bayani | 246,248 | 189,184 | 15,703 | 8,771 | 5 | $0.308995 |
| classical-coherence | 247,644 | 215,040 | 13,256 | 10,502 | 7 | $0.240776 |
| hadith | 370,986 | 330,496 | 19,438 | 14,024 | 9 | $0.341459 |
| meal | 311,889 | 274,048 | 17,771 | 11,135 | 8 | $0.308202 |

Executed tool input was scanned for search commands and other-lane paths. No such patterns were flagged. This scan is observational, not a filesystem access control.

Updated: 2026-10-06T18:44:44.795519+00:00
