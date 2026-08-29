#!/usr/bin/env python3
"""Build or verify the exact once-daily shift handover set."""

import hashlib
import os
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHIFT = ROOT / "Shift"
PARTS = (
    "BLUEPRINT.txt",
    "GUIDE.txt",
    "DIRECTORY.txt",
    "DIRECTORY.yaml",
    "SIDEBAR.master.txt",
    "BLUEPRINT.docx",
)
SEAMED = ("GUIDE.txt", "DIRECTORY.txt")
SEAM = re.compile(r"PART:\s+(\S+)\s+(GUIDE|DIRECTORY)")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tag_of(path):
    with path.open(encoding="utf-8") as fh:
        match = SEAM.search(fh.readline())
    return match.group(1) if match else None


def main():
    check_only = "--check" in sys.argv
    problems = []
    sources = {name: ROOT / name for name in PARTS if name != "BLUEPRINT.docx"}

    for name, src in sources.items():
        if not src.is_file():
            problems.append(f"missing source: {name}")
    if problems:
        print("\n".join(problems))
        return 1

    tags = {name: tag_of(sources[name]) for name in SEAMED}
    if None in tags.values() or len(set(tags.values())) != 1:
        print("FATAL: parts do not carry one matching build tag:", tags)
        return 1
    tag = next(iter(tags.values()))
    sources["BLUEPRINT.docx"] = ROOT / "Editions" / tag / "BLUEPRINT.docx"
    if not sources["BLUEPRINT.docx"].is_file():
        print(f"missing sealed document: Editions/{tag}/BLUEPRINT.docx")
        return 1

    if not check_only and SHIFT.is_dir():
        last_refresh = datetime.fromtimestamp(SHIFT.stat().st_mtime).date()
        if last_refresh == date.today():
            print(f"Shift already refreshed today ({last_refresh.isoformat()}); no write")
            return 0

    if not check_only:
        SHIFT.mkdir(exist_ok=True)

    if not SHIFT.is_dir():
        problems.append("Shift folder does not exist")
    else:
        allowed = set(PARTS)
        stale = sorted(p.name for p in SHIFT.iterdir() if p.name not in allowed)
        if stale:
            problems.append("stray in Shift/: " + ", ".join(stale))

    for name, src in sources.items():
        dst = SHIFT / name
        if dst.is_file() and digest(dst) == digest(src):
            print(f"current: Shift/{name}")
        else:
            problems.append(f"stale or missing: Shift/{name}")
            if not check_only:
                shutil.copy2(src, dst)
                print(f"written: Shift/{name}")

    if problems and check_only:
        print("\n".join(problems))
        print(f"\nbuild {tag} — NOT READY")
        return 1

    # Copying repairs missing or stale approved files, but never removes strays.
    remaining = [p for p in problems if p.startswith("stray in")]
    if remaining:
        print("\n".join(remaining))
        print(f"\nbuild {tag} — NOT READY; move strays to Archive and rerun")
        return 1

    if not check_only:
        os.utime(SHIFT, None)
    print(f"\nshift ready — build {tag}; six files; refresh no more than once per day")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())