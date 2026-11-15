#!/usr/bin/env python3
"""Verify the self-contained BKPDE portability kit and its live references."""

from __future__ import annotations

import hashlib
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
REQUIRED = (
    "README.md",
    "ARCHITECTURE.md",
    "DEPENDENCIES.md",
    "COLD-REBUILD.md",
    "RELEASE-RUNBOOK.md",
    "RECOVERY.md",
    "audit/AUDIT-BRIEF.md",
    "audit/FINDINGS-TEMPLATE.md",
    "audit/DECISION-LOG.md",
)
LIVE = (
    "Blueprint/BLUEPRINT.md",
    "Blueprint/build.py",
    "Blueprint/build_human_volume.py",
    "push.bat",
    "bootstrap/AGENTS.md",
    "bootstrap/00_START-HERE.md",
    "bootstrap/clear_pending.py",
    "bootstrap/distribute_blueprint.py",
    "bootstrap/shift.py",
    ".github/workflows/compile.yml",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true",
                        help="also require the referenced live repository files")
    args = parser.parse_args()
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if args.live:
        missing += [name for name in LIVE if not (REPO / name).is_file()]
        missing += [f"snapshot/{name}" for name in LIVE
                    if not (ROOT / "snapshot" / name).is_file()]
    if missing:
        raise SystemExit("FATAL: missing portability inputs: " + ", ".join(missing))
    manifest_path = ROOT / "MANIFEST.json"
    if not manifest_path.is_file():
        raise SystemExit("FATAL: MANIFEST.json is missing; run make_bundle.py")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative, expected in manifest["files"].items():
        path = ROOT / relative
        if not path.is_file() or digest(path) != expected:
            raise SystemExit(f"FATAL: portability file differs: {relative}")
    if args.live:
        for relative in LIVE:
            if digest(REPO / relative) != digest(ROOT / "snapshot" / relative):
                raise SystemExit(f"FATAL: audit snapshot is stale: {relative}")
    suffix = " plus live references" if args.live else ""
    print(f"portability kit: PASS - {len(manifest['files'])} files match manifest{suffix}")


if __name__ == "__main__":
    main()
