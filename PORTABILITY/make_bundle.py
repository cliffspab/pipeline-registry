#!/usr/bin/env python3
"""Generate the portability manifest, audit snapshot and independent ZIP."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
EXCLUDE = {"MANIFEST.json", "BKPDE-Portability.zip"}
SNAPSHOT = (
    "Blueprint/BLUEPRINT.md", "Blueprint/build.py",
    "Blueprint/build_human_volume.py", "push.bat",
    "bootstrap/AGENTS.md", "bootstrap/00_START-HERE.md",
    "bootstrap/clear_pending.py", "bootstrap/distribute_blueprint.py",
    "bootstrap/shift.py",
    ".github/workflows/compile.yml",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and p.name not in EXCLUDE and "__pycache__" not in p.parts)


def clear_readonly(function, target, _error) -> None:
    os.chmod(target, stat.S_IWRITE)
    function(target)


def main() -> None:
    edition = (REPO / "Blueprint" / "VERSION.txt").read_text(encoding="utf-8").strip()
    snapshot_root = ROOT / "snapshot"
    if snapshot_root.exists():
        if snapshot_root.parent != ROOT or snapshot_root.name != "snapshot":
            raise SystemExit("FATAL: unsafe snapshot path")
        shutil.rmtree(snapshot_root, onexc=clear_readonly)
    snapshot = {}
    for name in SNAPSHOT:
        source = REPO / name
        target = snapshot_root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
        snapshot[name] = digest(source)
    (ROOT / "AUDIT-SNAPSHOT.json").write_text(
        json.dumps({"edition": edition, "files": snapshot}, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    manifest_files = {p.relative_to(ROOT).as_posix(): digest(p) for p in files()}
    (ROOT / "MANIFEST.json").write_text(
        json.dumps({"format": 1, "files": manifest_files}, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    archive_path = ROOT / "BKPDE-Portability.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_STORED) as archive:
        for path in [*files(), ROOT / "MANIFEST.json"]:
            info = zipfile.ZipInfo(path.relative_to(ROOT.parent).as_posix(),
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"portability bundle: {archive_path.name}, {len(manifest_files)} manifested files")


if __name__ == "__main__":
    main()
