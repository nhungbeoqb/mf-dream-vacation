#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).

Why this emoji: the judge's first criterion names "a mountain" outright,
and Fuji is one particular mountain, not any holiday -- a snow-capped
postcard of Japan at first light, specific and personal, a fresh pick
against the field's generic beaches and palms, and readable at any size
on any screen.
"""

import os

EMOJI = "\U0001F5FB"  # MOUNT FUJI -- one code point, one dream vacation


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read it back and enforce the gate ourselves: exactly one emoji,
    # 1 to 8 characters, not only whitespace. Fail loudly rather than
    # ship an entry the sealed scorer would refuse.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    assert len(written) == 1, f"entry must be one character, got {len(written)}"
    assert written == EMOJI, "entry does not match the chosen emoji"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
