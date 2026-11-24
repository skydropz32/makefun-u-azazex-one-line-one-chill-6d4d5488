#!/usr/bin/env python3
"""One Line, One Chill — the single scariest sentence, under 200 characters."""

import os

LINE = "I changed the locks after the break-in, but the intruder's fingerprints on the inside of my bedroom door match mine."


def main():
    if not LINE or LINE != LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be a single non-blank line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
