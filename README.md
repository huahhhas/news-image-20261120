# World news, 20 November 2026, in one image

**THE WORLD TODAY — FRIDAY, 20 NOVEMBER 2026.** A newspaper front page
summing up the day's world news, drawn with PIL and shipped as a single
1024×1024 PNG.

## The day's stories

- **Lead — Shenzhen, APEC:** Trump, Xi and Putin meet in the first-ever
  three-way summit, opening talks on nuclear arms, energy security and the
  wars in Ukraine and the Gulf.
- **The Gulf War:** a Houthi missile damages one of Riyadh's tallest
  skyscrapers; US intelligence says Iran still holds at least 2,500
  missiles after nine months of war; the US Senate rejects a bid to curb
  President Trump's Iran war powers.
- **Ukraine:** Russian strikes damage the Austrian and Dutch embassies in
  Kyiv; Kyiv says its attack on the Crimean Bridge halted rail traffic.
- **Cyclone Akvan:** 80,000 evacuated as the severe cyclone nears India's
  east coast, due to make landfall on the Odisha and Andhra Pradesh coasts.
- **Also:** the ICJ rules Myanmar 'likely intended to destroy' the
  Rohingya; Seoul's court overturns ex-PM Han's conviction over martial
  law; GTA 6 reviews are in; Trump lands in Manila for the Quad summit;
  Anthropic said to be worth $1.5 trillion; Nicholls' 113* lifts New
  Zealand in the Wellington Test.

## How it is built

`draw_poster_20.py` (kept with the build notes, not in this repo) draws
`entry.png` with PIL from the headlines above — no network, no randomness,
so re-running it writes byte-identical output. `main.py` (Python 3.13
standard library only) copies `entry.png` to `/output/entry.png`; it runs
twice and both runs write the same bytes.

## Entry

- Competition: [news-image-20261120](https://make.fun/bounty/news-image-20261120)
  on make.fun — sum up 20 November's world news in one image. $250 shared
  by the 50 best entries.
- License: MIT (see LICENSE).
