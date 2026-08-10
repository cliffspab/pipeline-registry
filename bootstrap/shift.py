#!/usr/bin/env python3
"""
Cut the shift folder.

    Shift/GUIDE.txt       core + processes, markdown syntax
    Shift/DIRECTORY.txt   status + references, YAML syntax

Both copied from the confirmed-latest parts at the root of Project_Space.
Nothing else ever goes in it. It is a copy and never a source: nothing is
edited there, and nothing unique ever lives there, so deleting it can never
lose anything.

Idempotent. Run it on entry to the folder, on every build, and any time the
parts move. If the folder is already correct it says so and writes nothing;
if the operator has taken the files, it puts them back.

    python3 shift.py            cut or refresh
    python3 shift.py --check    report only, exit 1 if not shift-ready
"""

import hashlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHIFT = ROOT / "Shift"
PARTS = ("GUIDE.txt", "DIRECTORY.txt")

SEAM = re.compile(r"PART:\s+(\S+)\s+(GUIDE|DIRECTORY)")


def digest(path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def tag_of(path):
    """The build tag from the part's own seam — its first line."""
    with path.open(encoding="utf-8") as fh:
        m = SEAM.search(fh.readline())
    return m.group(1) if m else None


def main():
    check_only = "--check" in sys.argv
    problems = []

    sources = {name: ROOT / name for name in PARTS}
    for name, src in sources.items():
        if not src.exists():
            problems.append("missing source: %s" % name)
    if problems:
        print("\n".join(problems))
        return 1

    # Every part of one build carries one tag. A part on a different tag is a
    # bad set and must not be handed to a shift.
    tags = {name: tag_of(src) for name, src in sources.items()}
    if None in tags.values():
        print("FATAL: a part carries no seam:", tags)
        return 1
    if len(set(tags.values())) != 1:
        print("FATAL: parts disagree on build tag:", tags)
        return 1
    tag = next(iter(tags.values()))

    SHIFT.mkdir(exist_ok=True)

    stale = [p.name for p in SHIFT.iterdir() if p.name not in PARTS]
    for name, src in sources.items():
        dst = SHIFT / name
        if dst.exists() and digest(dst) == digest(src):
            print("current: Shift/%s" % name)
            continue
        problems.append(name)
        if not check_only:
            shutil.copy2(src, dst)
            print("written: Shift/%s" % name)

    if stale:
        problems.append("not part of a shift: %s" % ", ".join(stale))
        print("STRAY in Shift/: %s — a shift folder holds the two parts and "
              "nothing else" % ", ".join(stale))

    # A stray file is not repaired by copying — the desk does not delete on this
    # mount. It is reported and the folder is NOT declared ready, whichever mode
    # we are in. A false all-clear is the fault this whole procedure exists to
    # prevent.
    if stale:
        print("\nbuild %s — NOT READY. Move the stray file(s) to "
              "_pending-delete\\ and re-run." % tag)
        return 1

    if check_only:
        print("\nbuild %s — SHIFT READY" % tag)
        return 0

    print("\nshift ready — build %s, two parts, text format" % tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
