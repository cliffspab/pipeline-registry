#!/usr/bin/env python3
"""Generate the tools-only portability manifest and ZIP."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
PORTABILITY = (
    "PORTABILITY/README.md",
    "PORTABILITY/ARCHITECTURE.md",
    "PORTABILITY/DEPENDENCIES.md",
    "PORTABILITY/COLD-REBUILD.md",
    "PORTABILITY/RELEASE-RUNBOOK.md",
    "PORTABILITY/RECOVERY.md",
    "PORTABILITY/make_bundle.py",
)
TOOLS = (
    "Blueprint/assemble.js",
    ".github/workflows/pages.yml",
    "desk/index.html",
    "DC-X Desk Hub.user.js",
    "index.html",
    "bootstrap/AGENTS.md",
    "bootstrap/00_START-HERE.md",
)
PAYLOAD = tuple(sorted((*PORTABILITY, *TOOLS)))


def main() -> None:
    missing = [name for name in PAYLOAD if not (REPO / name).is_file()]
    if missing:
        raise SystemExit("FATAL: missing portability tool: " + ", ".join(missing))
    archive_path = ROOT / "BKPDE-Portability.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_STORED) as archive:
        for name in PAYLOAD:
            path = REPO / name
            info = zipfile.ZipInfo(name,
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"portability bundle: {archive_path.name}, {len(PAYLOAD)} tool files")


if __name__ == "__main__":
    main()
