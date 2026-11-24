"""Monday, Reviewed in One Line (make.fun).

A one-line review of my own Monday, under 200 characters, with a
concrete detail a coworker would recognise. The program writes the
review to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline,
so the file's byte count is the review's character count.
Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "Monday, one star: the 8 a.m. meeting could have been an email, "
    "and the email could have been nothing."
)

MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
