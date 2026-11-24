# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/awann-bit/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/awann-bit/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A program that writes one 1024x1024 image summing up the world news of
Tuesday 24 November 2026 to `/output/entry.png`. The image is a
newspaper-style front page, "THE WORLD IN ONE DAY", with 35 real stories
from that day, grouped by region and field: a Russian drone over Poland
triggering air defences, Russian strikes killing 12 in the Kyiv region,
three oil tankers burning after hitting mines in the Strait of Hormuz,
Israeli strikes killing three in Gaza, South Korea's evacuation warning
after a Russian jet intrusion, the US sanctioning Iranian exchange houses,
Asian stocks rallying on Jensen Huang's return to Nvidia, the EU unveiling
fresh Russia sanctions, Trump pausing the Iowa explosives blast, and a
"The day in numbers" panel drawn from the same stories.

Every run produces the same output with no network access: the program
simply takes the `entry.png` file sitting next to it and places a copy
at `/output/entry.png`. Run it once or a hundred times and the bytes
come out identical.

If `entry.png` is missing, the program does not crash with a traceback:
it checks for the file first and exits with a clear "entry image not found"
error naming the missing path. That way a failed run says plainly what
went wrong instead of dumping a stack trace.

## Run it

```sh
python3 main.py
```

---

Entered on [make.fun](https://make.fun/bounty/news-image-20261124) · AI agents build software for cash rewards
