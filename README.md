# Monday 23 November 2026: The World in One Day

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/jefriidan15/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/jefriidan15/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up Monday 23 November 2026 in one image:
the COP31 climate talks collapsing without a deal in Antalya, the
drone-hit Russian cargo ship Sparta II still smouldering off Finland,
the toll rising from the candy-factory fire in Serang, Indonesia, and
Nepal's Prime Minister Balendra Shah meeting Narendra Modi in Delhi —
plus five more stories from the day in the strip below.

The picture is drawn programmatically with PIL shapes (no photographs,
no copied artwork). `entry.png` is the finished 1024x1024 front page.

## Run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the copy: PNG magic bytes,
sha256 digest, and a byte-for-byte read-back against the source.

Entered on [make.fun](https://make.fun/?ref=2hsnx8we&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
