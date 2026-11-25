#!/usr/bin/env python3
"""One-Line Laugh-Off -- entry program.

Writes one line -- the joke about telling a phone you need space --
to /output/entry.txt for the judge to read. Standard library only,
no network, no input files, deterministic output: the same line,
the same bytes, every run.
"""

import os

LINE = "I told my phone I needed space. It deleted my photos."

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and the brief requires a single short funny line.
    """
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read the file back and refuse to pass on any mismatch, so a
    # bad write can never silently reach the judge.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the entry line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
