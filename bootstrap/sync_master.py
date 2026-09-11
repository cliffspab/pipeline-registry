#!/usr/bin/env python3
"""Refresh or verify the stable Google Drive pipeline containers.

Run only after seal.py. Every source comes from the sealed edition, and every
destination must already exist so a misspelt path cannot create a duplicate
Drive file with a new ID.
"""

import argparse
import hashlib
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_TARGET = Path(r"D:\GoogleONE\My Drive\SYNC_MASTER")
TARGET_FOLDER_ID = "1jTx-0Lmc07VkbLCMdBMhXcwzRF8Qq8Aq"
CONTAINERS = {
    "GUIDE.txt": ("guide_sync.txt", "1SVHnnvGIihZUEK59Xd984kRv_2yhtOtd"),
    "PROCESSES.txt": ("processes_sync.txt", "1F_qMGFTTWC4MMQev5VEpV8mwvBxZXSyi"),
    "DIRECTORY.yaml": ("directory_sync.yaml", "1Q2_2jZKb-GZNwwTk62bnJ528pEw5Xi4k"),
    "DIRECTORY.txt": ("directory_sync.txt", "1mDb6fkidx-XE-oinOlw6oYBUy5TiLWUU"),
    "BLUEPRINT.txt": ("blueprint_sync.txt", "1UROyVx8E_Fbd5Tgu7FsDtpLvDKxE3ZvV"),
    "BLUEPRINT.pdf": ("blueprint_sync.pdf", "12774sja8ejDGNcwMuDp77A-5YTMxd6Ah"),
    "BLUEPRINT.docx": ("blueprint_sync.docx", "1GYaPzsIvDcD5CiHxZiG5kNpvQvdfwRQp"),
}
TAG = re.compile(r"PART:\s+(\S+)\s+GUIDE")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_tag():
    source = (ROOT / "BLUEPRINT.txt").read_text(encoding="utf-8")
    match = TAG.search(source)
    if not match:
        raise SystemExit("FATAL: BLUEPRINT.txt has no GUIDE edition seam.")
    return match.group(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--target",
        type=Path,
        default=Path(os.environ.get("BKP_SYNC_MASTER_DIR", DEFAULT_TARGET)),
    )
    args = parser.parse_args()

    tag = current_tag()
    edition = ROOT / "Editions" / tag
    if not edition.is_dir():
        raise SystemExit(f"FATAL: edition is not sealed: Editions/{tag}")
    if not args.target.is_dir():
        raise SystemExit(f"FATAL: Drive container folder is unavailable: {args.target}")

    missing_sources = [name for name in CONTAINERS if not (edition / name).is_file()]
    missing_targets = [name for name, _ in CONTAINERS.values()
                       if not (args.target / name).is_file()]
    if missing_sources:
        raise SystemExit("FATAL: sealed outputs missing: " + ", ".join(missing_sources))
    if missing_targets:
        raise SystemExit("FATAL: Drive containers missing: " + ", ".join(missing_targets))

    stale = []
    for source_name, (target_name, file_id) in CONTAINERS.items():
        source = edition / source_name
        target = args.target / target_name
        if digest(source) == digest(target):
            print(f"current: {target_name}  [{file_id}]")
            continue
        stale.append(target_name)
        if not args.check:
            shutil.copy2(source, target)
            if digest(source) != digest(target):
                raise SystemExit(f"FATAL: container verification failed: {target_name}")
            print(f"written: {target_name}  [{file_id}]")

    if stale and args.check:
        print("stale: " + ", ".join(stale))
        print(f"\nDrive containers — NOT CURRENT for {tag}")
        return 1

    print(f"\nDrive containers ready — {tag}; seven stable files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
