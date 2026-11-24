#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence, at most 200 characters, that explains the modern
internet to someone who has just stepped out of the year 1800.

The sentence builds only from things a person from 1800 already knows -- a
road, a post office, a library, a letter, ink -- and says what the internet
is and what it does: every post office and library on earth joined by one
road, so a message written here is read across the world at once.

Standard library only. Deterministic: the same text on every run.
"""

import os
import sys

SENTENCE = (
    "Imagine every post office and library on earth joined by one road "
    "of light, so a letter written here is read across the world before "
    "its ink dries."
)

MAX_CHARS = 200


def main() -> int:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
