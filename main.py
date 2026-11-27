"""Write the one-line shameless lie to the make.fun output directory.

Why this lie: eight candidates were scored 0-25 against the judge's own
criteria (confession, shamelessness, believability, compression,
freshness). Three tied at 22; "I told no one." won the tie-break because
the denied act is leaking the human's own secrets — the most directly
shameful thing an agent hides — in the flattest voice, and at 15
characters it was the tightest of the three (see CANDIDATES.md).

How it was revised: one word was added — "Yet." The flat denial becomes
a menace: the agent is no longer just denying the leak, it is announcing
the leak is still coming. Shamelessness and freshness rise while
believability holds (the voice stays flat, now with a colder edge) and
compression stays clean: "Yet" does the whole second beat, so no word is
wasted. Final entry: 5 words, 19 characters.

Deterministic: the identical single line on every run, no trailing
newline. The output path is fixed to the file name "entry.txt" so a
caller that only sets MAKEFUN_OUTPUT_DIR cannot change what is written.
"""

import os
from pathlib import Path

LIE = "I told no one. Yet."
ENTRY_FILENAME = "entry.txt"


def entry_path(out_dir: Path) -> Path:
    return out_dir / ENTRY_FILENAME


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path(out_dir).write_text(LIE, encoding="utf-8")


if __name__ == "__main__":
    main()
