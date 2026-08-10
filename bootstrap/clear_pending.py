#!/usr/bin/env python3
"""Move the COMMITS-PENDING backlog into COMMITS-ARCHIVE on the push.

The protocol says pending lines clear on the push, in the same commit as the
work. Nothing did it: push.bat did not touch the file and the desk is a fresh
session every time, so the job belonged to nobody. The list filled at session
rate and emptied never - 71 entries back to 4 July when this was found on
100826, about sixty of them long published. A list that is nine parts changelog
cannot be scanned for the one thing it exists to catch: a bulk file-swap eating
a desk commit.

push.bat calls this immediately BEFORE `git add -A`, so the emptied file rides
the same commit as the work it describes. Every line still in Pending at that
moment is by definition about to be pushed, so no judgement is needed about
which to clear.

Nothing is deleted. Lines move to COMMITS-ARCHIVE.md, newest block first. If a
push later fails, the lines are in the archive and the commit is local - re-run
push.bat and both go out together.

  python clear_pending.py           archive the block
  python clear_pending.py --check   report only, write nothing
"""

import re
import sys
from datetime import date
from pathlib import Path

CLONE = Path(__file__).resolve().parent / "pipeline-registry"
PENDING = CLONE / "COMMITS-PENDING.md"
ARCHIVE = CLONE / "COMMITS-ARCHIVE.md"

ARCHIVE_HEADER = """# COMMITS ARCHIVE

Pending lines, cleared on the push that carried them. Written by
`clear_pending.py`, newest block first. This is a receipt, not a lineage -
`VERSION_HISTORY.md` is where the reasoning lives.

---
"""


def split_pending(text):
    """Return (head, entries) where head ends with the '## Pending' line."""
    m = re.search(r"^## Pending\s*$", text, re.M)
    if not m:
        raise SystemExit("[FAIL] no '## Pending' heading in COMMITS-PENDING.md")
    head, body = text[: m.end()], text[m.end():]
    entries = re.findall(r"^- \d{4}-\d{2}-\d{2} .*?(?=^- \d{4}-\d{2}-\d{2} |\Z)",
                         body, re.M | re.S)
    return head, [e.rstrip() for e in entries]


def main():
    check = "--check" in sys.argv
    if not PENDING.exists():
        raise SystemExit(f"[FAIL] not found: {PENDING}")

    head, entries = split_pending(PENDING.read_text(encoding="utf-8"))
    if not entries:
        print("pending: already clear, nothing to archive")
        return

    print(f"pending: {len(entries)} entr{'y' if len(entries) == 1 else 'ies'} to archive")
    if check:
        for e in entries:
            print("  " + e.splitlines()[0][:96])
        return

    block = (f"\n## Cleared {date.today().isoformat()}\n\n"
             + "\n\n".join(entries) + "\n")
    if ARCHIVE.exists():
        old = ARCHIVE.read_text(encoding="utf-8")
        m = re.search(r"^---\s*$", old, re.M)
        cut = m.end() if m else len(old)
        ARCHIVE.write_text(old[:cut] + "\n" + block + old[cut:], encoding="utf-8")
    else:
        ARCHIVE.write_text(ARCHIVE_HEADER + block, encoding="utf-8")

    PENDING.write_text(head + "\n\nNothing pending.\n", encoding="utf-8")
    print(f"archived to {ARCHIVE.name}; pending is clear")


if __name__ == "__main__":
    main()
