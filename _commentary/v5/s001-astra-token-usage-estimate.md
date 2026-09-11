# S1 Astra Token Usage Estimate

Analysis ID: `s001-fresh-20260910`

These are approximate token counts, shown in kilo-tokens (k tok), estimated from
the actual prompt and output artifacts with `UTF-8 bytes / 4`. Scope discovery
and scope composition aggregate the micro, macro, and global lanes for each
ayah. Repair rows include known extra repair turns. Actual billed usage may be
higher because hidden system/tool overhead and some intermediate agent context
are not fully recoverable from final artifacts.

`Weighted k tok` is computed as:

```text
input k tok + (5 * output k tok)
```

| Ayah | Step | Input k tok | Output k tok | Weighted k tok |
|---|---|---:|---:|---:|
| 1:1 | scope discovery | 408.8 | 145.3 | 1,135.3 |
| 1:1 | scope composition | 559.6 | 73.9 | 929.1 |
| 1:1 | scope repair turns | 211.9 | 20.5 | 314.5 |
| 1:1 | CE canonical | 94.7 | 13.9 | 164.2 |
| 1:1 | CE editorial | 112.0 | 21.7 | 220.7 |
| 1:1 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:1 | CE presentation follow-up | 134.0 | 21.7 | 242.7 |
| 1:1 | invitation | 23.6 | 0.6 | 26.5 |
| 1:2 | scope discovery | 463.4 | 179.6 | 1,361.4 |
| 1:2 | scope composition | 648.5 | 79.6 | 1,046.5 |
| 1:2 | scope repair turns | 453.9 | 54.0 | 724.0 |
| 1:2 | CE canonical | 100.4 | 13.1 | 165.8 |
| 1:2 | CE editorial | 116.9 | 22.8 | 231.1 |
| 1:2 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:2 | CE presentation follow-up | 140.0 | 22.8 | 254.2 |
| 1:2 | invitation | 24.7 | 0.5 | 27.3 |
| 1:3 | scope discovery | 280.1 | 98.0 | 769.9 |
| 1:3 | scope composition | 383.6 | 61.6 | 691.7 |
| 1:3 | scope repair turns | 391.8 | 55.5 | 669.4 |
| 1:3 | CE canonical | 82.4 | 8.5 | 125.1 |
| 1:3 | CE editorial | 94.4 | 18.7 | 187.8 |
| 1:3 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:3 | CE presentation follow-up | 113.3 | 18.7 | 206.8 |
| 1:3 | invitation | 20.6 | 0.6 | 23.4 |
| 1:4 | scope discovery | 392.3 | 221.3 | 1,498.6 |
| 1:4 | scope composition | 619.1 | 89.4 | 1,066.2 |
| 1:4 | scope repair turns | 723.3 | 89.4 | 1,170.4 |
| 1:4 | CE canonical | 110.2 | 16.0 | 190.1 |
| 1:4 | CE editorial | 129.6 | 24.6 | 252.5 |
| 1:4 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:4 | CE presentation follow-up | 154.4 | 24.6 | 277.3 |
| 1:4 | invitation | 26.5 | 0.7 | 29.9 |
| 1:5 | scope discovery | 404.5 | 190.4 | 1,356.3 |
| 1:5 | scope composition | 600.5 | 102.3 | 1,111.8 |
| 1:5 | scope repair turns | 374.1 | 41.7 | 582.7 |
| 1:5 | CE canonical | 123.0 | 8.9 | 167.5 |
| 1:5 | CE editorial | 135.4 | 12.4 | 197.6 |
| 1:5 | CE editorial repair | 147.9 | 12.4 | 210.0 |
| 1:5 | CE presentation follow-up | 148.1 | 12.4 | 210.2 |
| 1:5 | invitation | 14.3 | 0.5 | 16.8 |
| 1:6 | scope discovery | 457.1 | 223.2 | 1,572.9 |
| 1:6 | scope composition | 685.8 | 105.2 | 1,211.7 |
| 1:6 | scope repair turns | 523.9 | 64.0 | 843.9 |
| 1:6 | CE canonical | 125.9 | 9.8 | 174.9 |
| 1:6 | CE editorial | 139.2 | 27.2 | 275.2 |
| 1:6 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:6 | CE presentation follow-up | 166.7 | 27.2 | 302.6 |
| 1:6 | invitation | 29.1 | 0.6 | 31.9 |
| 1:7 | scope discovery | 505.2 | 283.6 | 1,923.2 |
| 1:7 | scope composition | 794.3 | 96.6 | 1,277.2 |
| 1:7 | scope repair turns | 573.6 | 70.6 | 926.6 |
| 1:7 | CE canonical | 117.3 | 14.1 | 187.9 |
| 1:7 | CE editorial | 134.9 | 26.8 | 268.8 |
| 1:7 | CE editorial repair | 0.0 | 0.0 | 0.0 |
| 1:7 | CE presentation follow-up | 162.0 | 26.8 | 295.9 |
| 1:7 | invitation | 28.7 | 0.6 | 31.8 |

## Totals

| Ayah | Input k tok | Output k tok | Weighted k tok |
|---|---:|---:|---:|
| 1:1 | 1,544.6 | 297.7 | 3,033.0 |
| 1:2 | 1,947.8 | 372.5 | 3,810.2 |
| 1:3 | 1,366.2 | 261.6 | 2,674.0 |
| 1:4 | 2,155.4 | 465.9 | 4,484.9 |
| 1:5 | 1,947.9 | 381.0 | 3,853.1 |
| 1:6 | 2,127.7 | 457.1 | 4,413.1 |
| 1:7 | 2,315.9 | 519.1 | 4,911.5 |
| Grand | 13,405.6 | 2,754.8 | 27,179.6 |
