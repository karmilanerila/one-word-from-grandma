#!/usr/bin/env python3
"""One Word From Grandma — entry generator.

Writes the single word our grandma would text about AI to /output/entry.txt.
The word is "Robbie": the warm pet name a grandma gives the machine,
baffled, affectionate, and instantly readable — not the obvious "robot".
"""

import os

WORD = "Robbie"

# The gate allows 1–30 characters and exactly one word: no spaces,
# no punctuation, no trailing newline — a single bare word, as typed.
MAX_CHARS = 30


def validate(word):
    assert isinstance(word, str), "word must be text"
    assert word.strip() == word and word, "word must not be blank or padded"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(word) <= MAX_CHARS, "word must be 1-30 characters"
    word.encode("utf-8")
    return word


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validate(WORD))
    print(f"Wrote {WORD!r} ({len(WORD)} chars) to {out_path}")


if __name__ == "__main__":
    main()
