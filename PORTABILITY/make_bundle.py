#!/usr/bin/env python3
"""Generate the single-master portability snapshot, manifest and ZIP."""

from __future__ import annotations

import hashlib
import json
import shutil
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
EXCLUDE = {"MANIFEST.json", "BKPDE-Portability.zip", "AUDIT-SNAPSHOT.json"}
SNAPSHOT = (
    "Blueprint/MASTER.md",
    "Blueprint/assemble.js",
    ".github/workflows/pages.yml",
    "desk/index.html",
    "DC-X Desk Hub.user.js",
    "index.html",
    "bootstrap/AGENTS.md",
    "bootstrap/00_START-HERE.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and p.name not in EXCLUDE and "__pycache__" not in p.parts
    )


def clear_readonly(function, target, _error) -> None:
    Path(target).chmod(stat.S_IWRITE)
    function(target)


def edition() -> str:
    text = (REPO / "Blueprint" / "MASTER.md").read_text(encoding="utf-8-sig")
    marker = "\n \"edition\": \""
    if marker not in text:
        raise SystemExit("FATAL: master edition metadata missing")
    return text.split(marker, 1)[1].split('"', 1)[0]


def main() -> None:
    snapshot_root = ROOT / "snapshot"
    if snapshot_root.exists():
        if snapshot_root.parent != ROOT or snapshot_root.name != "snapshot":
            raise SystemExit("FATAL: unsafe snapshot path")
        shutil.rmtree(snapshot_root, onexc=clear_readonly)
    snapshot: dict[str, str] = {}
    for name in SNAPSHOT:
        source = REPO / name
        if not source.is_file():
            raise SystemExit(f"FATAL: missing live snapshot input: {name}")
        target = snapshot_root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
        snapshot[name] = digest(source)
    (ROOT / "AUDIT-SNAPSHOT.json").write_text(
        json.dumps({"edition": edition(), "files": snapshot}, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    manifest_files = {p.relative_to(ROOT).as_posix(): digest(p) for p in files()}
    (ROOT / "MANIFEST.json").write_text(
        json.dumps({"format": 2, "files": manifest_files}, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    archive_path = ROOT / "BKPDE-Portability.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_STORED) as archive:
        for path in [*files(), ROOT / "AUDIT-SNAPSHOT.json", ROOT / "MANIFEST.json"]:
            info = zipfile.ZipInfo(path.relative_to(REPO).as_posix(),
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"portability bundle: {archive_path.name}, {len(manifest_files)} manifested files")


if __name__ == "__main__":
    main()
