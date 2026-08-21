#!/usr/bin/env python3
"""Build or verify the exact shift handover set."""

import hashlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHIFT = ROOT / "Shift"
SIDEBAR_SOURCE = ROOT / "pipeline-registry" / "design" / "Sidebar"
SIDEBAR_DEST = SHIFT / "Sidebar"
PARTS = ("BLUEPRINT.txt", "GUIDE.txt", "DIRECTORY.txt")
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
    sources = {name: ROOT / name for name in PARTS}

    for name, src in sources.items():
        if not src.is_file():
            problems.append(f"missing source: {name}")
    if not SIDEBAR_SOURCE.is_dir():
        problems.append(f"missing Sidebar source: {SIDEBAR_SOURCE}")
    if problems:
        print("\n".join(problems))
        return 1

    tags = {name: tag_of(sources[name]) for name in SEAMED}
    if None in tags.values() or len(set(tags.values())) != 1:
        print("FATAL: parts do not carry one matching build tag:", tags)
        return 1
    tag = next(iter(tags.values()))

    sidebar_sources = {
        p.name: p for p in SIDEBAR_SOURCE.iterdir() if p.is_file()
    }
    if not sidebar_sources:
        print("FATAL: Sidebar source contains no files")
        return 1

    if not check_only:
        SHIFT.mkdir(exist_ok=True)
        SIDEBAR_DEST.mkdir(exist_ok=True)

    if not SHIFT.is_dir():
        problems.append("Shift folder does not exist")
    else:
        allowed = set(PARTS) | {"Sidebar"}
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

    if SIDEBAR_DEST.is_dir():
        stale_sidebar = sorted(
            p.name for p in SIDEBAR_DEST.iterdir()
            if not p.is_file() or p.name not in sidebar_sources
        )
        if stale_sidebar:
            problems.append("stray in Shift/Sidebar/: " + ", ".join(stale_sidebar))
    else:
        problems.append("missing: Shift/Sidebar/")

    for name, src in sorted(sidebar_sources.items()):
        dst = SIDEBAR_DEST / name
        if dst.is_file() and digest(dst) == digest(src):
            print(f"current: Shift/Sidebar/{name}")
        else:
            problems.append(f"stale or missing: Shift/Sidebar/{name}")
            if not check_only:
                shutil.copy2(src, dst)
                print(f"written: Shift/Sidebar/{name}")

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

    print(f"\nshift ready — build {tag}; three text files + {len(sidebar_sources)} Sidebar files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())