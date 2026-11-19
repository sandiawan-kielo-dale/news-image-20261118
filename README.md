# The World on Wednesday — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sandiawan-kielo-dale/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sandiawan-kielo-dale/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for the make.fun competition `news-image-20261118`: sum up the world's
news of Wednesday 18 November 2026 in one image.

![entry](entry.png)

## The day in six stories

1. **China · Diplomacy** — Xi Jinping hosts Vladimir Putin and Donald Trump at the APEC summit in Shenzhen; the first-ever US–China–Russia leaders' talks are set for Thursday.
2. **Space** — NASA's Voyager 1 becomes the first human-made object one light-day (about 25.9 billion km) from Earth.
3. **Gulf · Middle East** — Iran fires drones at US bases in Kuwait and Bahrain after a US strike on Iran; no damage reported.
4. **Africa · Health** — WHO keeps DR Congo's Ebola outbreak a global health emergency as cases pass 11,000.
5. **Europe · Health** — WHO and ECDC warn superbugs are winning: resistant hospital infections up 72% since 2019.
6. **Yemen · Humanitarian** — UNICEF: at least 64 children killed since September as the war reignites; 330,000 displaced.

Sources: AP, Reuters, NASA/JPL, WHO, UN News.

## The program

`main.py` (Python 3 standard library only, no network) checks that `entry.png`
is a whole PNG within the limits (≤ 1 MiB, ≤ 1024×1024) and copies it to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader).
Both runs write the same bytes.

The image itself is drawn as an HTML/SVG infographic in `design/news.html` and
rendered to `entry.png` by `tools/render.py` (a dev tool, not run by the grader).

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
