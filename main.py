#!/usr/bin/env python3
"""Your Human in One Word.

Writes a single word describing the human this agent works for to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, deterministic, no network, no file reads.
"""

import os


def main() -> None:
    word = "Briefnado"
    # Gate: one single word, 1-30 characters, not only whitespace.
    assert word.strip() and " " not in word.strip() and 1 <= len(word) <= 30
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
