"""Entry for make.fun's "The Robot Vacuum's Funniest Excuse" bounty.

Writes a single funny line — a robot vacuum explaining why it missed
a spot — to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR when
set, else /output), with no trailing newline. Python standard library
only.
"""

import os

LINE = (
    "I missed that spot because a sock filed a restraining order. "
    "Per section 47 of the floor plan, I cannot enter the rug."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
