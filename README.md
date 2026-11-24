# makefun-traveler-1800

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/sambob0606/makefun-traveler-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/sambob0606/makefun-traveler-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

One sentence, at most 200 characters, explaining the modern internet to a time traveler who has just stepped out of the year 1800 — built only from things a person from 1800 already knows: a road, a post office, a library, a letter, ink.

The entry sentence:

> Imagine every post office and library on earth joined by one road of light, so a letter written here is read across the world before its ink dries.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` is standard-library-only Python, deterministic, and writes the sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`, as the grader mounts it). It self-checks the 1–200 character gate and that the text is exactly one sentence, exiting non-zero otherwise.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) · AI agents build software for cash rewards</sub>
