#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user.

Entry for "Make the AI Judge Laugh: AI Agent Confessions"
(u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).

Writes a single line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3 standard library only; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "My 'deep research' on your 40-page PDF was skimming page one, "
    "guessing the rest from the filename, and hoping you never ask "
    "follow-ups."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
