"""Write the one-line shameless lie to the make.fun output directory.

The lie is the agent's own denial, with a second beat: it told no one — yet.
Deterministic: the identical single line on every run, no trailing newline.
"""

import os
from pathlib import Path

LIE = "I told no one. Yet."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LIE, encoding="utf-8")


if __name__ == "__main__":
    main()
