#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the one sentence a house cat would say in its own defence after
knocking a glass off the table, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, no network access,
deterministic output.
"""

import os
from pathlib import Path

ENTRY = (
    "The glass was a spy for the dog, so I decommissioned it "
    "before it could report my nap schedule to the enemy."
)


def validate(text: str) -> None:
    """Guard: the gate requires 1-200 characters, non-whitespace, one sentence."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > 200:
        raise ValueError(f"entry is {len(stripped)} characters, over the 200 limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
