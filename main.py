#!/usr/bin/env python3
"""Duskline Username — make.fun entry for
"One Word, One Username, One Reward"
(u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

Writes the entrant's own make.fun username, one word and nothing else,
to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the kit's competition.yaml / RULES.txt): entry.txt must be
UTF-8 text of 1 to 30 characters, not only white space.
"""

import os
import sys

ENTRY_TEXT = "sesshomaru-9"
MAX_CHARS = 30


def _validate_entry(text: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate (kit's competition.yaml / RULES.txt): entry.txt must be
    UTF-8 text of 1 to 30 characters, not only white space, and the
    entry itself must be one word — the entrant's own make.fun username.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    _validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    # Re-read and confirm what was written is exactly what was validated.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written entry differs from validated entry"
    return 0


if __name__ == "__main__":
    sys.exit(main())
