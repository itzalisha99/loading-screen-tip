#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt.
"""

import os

TIP = "Tip: Stretch. Your agent already refactored the file you are afraid to touch."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1 to 200 chars, one line,
    and not only whitespace. Raises ValueError on anything invalid."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    entry = validate(TIP)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
