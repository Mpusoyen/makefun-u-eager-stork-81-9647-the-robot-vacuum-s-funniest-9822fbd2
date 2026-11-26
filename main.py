#!/usr/bin/env python3
"""Robot vacuum's funniest excuse -- make.fun entry.

The vacuum's alibi for the one spot it never cleans: a sock took out
a restraining order against it, and section 47 of the floor plan
backs the sock up. This script just drops that one line into
``entry.txt`` inside the output directory.

The output directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable when it is set, and falls back to ``/output`` otherwise.
Only the Python standard library is used, and the file is written
with no trailing newline so the entry is exactly one line.
"""

import os
import sys


def excuse_line() -> str:
    """Return the vacuum's excuse, as a single line."""
    reason = "I missed that spot because a sock filed a restraining order."
    legal = "Per section 47 of the floor plan, I cannot enter the rug."
    return reason + " " + legal


def output_path() -> str:
    """Resolve where entry.txt should be written."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    return os.path.join(directory, "entry.txt")


def write_entry(path: str, line: str) -> None:
    """Write ``line`` to ``path``, creating the directory if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def run(argv=None) -> int:
    """Entry point: write the excuse and report success."""
    del argv  # no command-line options are accepted
    write_entry(output_path(), excuse_line())
    return 0


if __name__ == "__main__":
    sys.exit(run())
