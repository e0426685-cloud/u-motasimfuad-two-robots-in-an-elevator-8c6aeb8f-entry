#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Python standard library only.
"""

import os

ENTRY = "I ran 4,000 simulations of this elevator ride, and 'nice weather' was still the best opener I had."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Assert the entry meets the bounty gate: UTF-8 text, 1-200 chars,
    not only whitespace, a single line."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters, got %d" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
