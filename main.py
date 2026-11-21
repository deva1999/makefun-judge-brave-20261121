#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a small, quiet scene meant to slow its reader down:
a finished kettle, steam thinning in the light, rain spelling
itself out on the roof, and a question that can wait.
"""

from pathlib import Path

TEXT = (
    "The kettle has finished. Steam rises in one slow ribbon "
    "and thins into the light. Nothing is counting down. "
    "The question waits on the sill like a cup gone cool, and the "
    "rain spells itself out on the roof, one drop at a time, until "
    "the next word comes when it is ready."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
