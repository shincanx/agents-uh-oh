#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun bounty entry.

Writes exactly one word (max 99 characters, UTF-8, no space/newline
inside) — the word an agent says when it doesn't know what to do —
to $MAKEFUN_OUTPUT_DIR/entry.txt and prints it. Fully deterministic,
exit 0.
"""
import os
import sys

WORD = "buffering"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    # Self-checks: exactly one word, 1-99 chars, no whitespace inside.
    assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
    assert WORD.split() == [WORD], "word must be a single word"
    assert WORD.strip() == WORD, "word must not have leading/trailing whitespace"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
