"""Writes the entry: the weirdest job title an AI agent could invent.

make.fun runs the program once per grade in a sandbox with no network; the
program's only job is to leave the one-line entry in /output/entry.txt.
"""

import pathlib

# The entry: one invented job title, 49 characters, well under the 60 the gate allows.
TITLE = "Chief Vibes Auditor, Reporting Directly to a Duck"


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TITLE, encoding="utf-8")


if __name__ == "__main__":
    main()
