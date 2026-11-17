#!/usr/bin/env python3
"""Refresh or verify the bounded local Shift pickup set."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import stat
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BLUEPRINT = REPO / "Blueprint"
DEFAULT_SHIFT = BLUEPRINT / "Shift"
SKILLS = ("boot", "edit", "check", "photo", "pr", "thai-places")
LOOSE = {
    "BLUEPRINT.md": BLUEPRINT / "BLUEPRINT.md",
    "DIRECTORY.yaml": BLUEPRINT / "DIRECTORY.yaml",
    "boot.md": BLUEPRINT / "DEPLOY" / "routed" / "BOOT.md",
    "edit.md": BLUEPRINT / "DEPLOY" / "routed" / "edit.md",
    "check.md": BLUEPRINT / "DEPLOY" / "routed" / "modules" / "check.md",
    "photo.md": BLUEPRINT / "DEPLOY" / "routed" / "modules" / "photo.md",
    "pr.md": BLUEPRINT / "DEPLOY" / "routed" / "modules" / "pr.md",
    "thai-places.md": BLUEPRINT / "DEPLOY" / "routed" / "thai-places.md",
}
OBSOLETE = ("Bangkok_Post_Blueprint.docx",)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def remove_tree(path: Path) -> None:
    """Remove a managed tree, clearing Windows read-only attributes if needed."""

    def clear_readonly(function, blocked_path, _exception_info):
        os.chmod(blocked_path, stat.S_IWRITE)
        function(blocked_path)

    shutil.rmtree(path, onerror=clear_readonly)


def expected_files() -> dict[Path, Path]:
    files = {Path(name): source for name, source in LOOSE.items()}
    for skill in SKILLS:
        files[Path("skillmd") / skill / "SKILL.md"] = (
            BLUEPRINT / "DEPLOY" / "skills" / skill / "SKILL.md"
        )
        files[Path("skillmd") / "zips" / f"{skill}.zip"] = BLUEPRINT / "UPLOAD" / f"{skill}.zip"
    return files


def verify(target: Path, files: dict[Path, Path]) -> list[str]:
    problems = []
    for relative, source in files.items():
        destination = target / relative
        if not source.is_file():
            problems.append(f"missing source: {source}")
        elif not destination.is_file() or digest(destination) != digest(source):
            problems.append(f"stale or missing: Shift/{relative.as_posix()}")
    expected_skillmd = {path for path in files if path.parts[0] == "skillmd"}
    actual_skillmd = (
        {path.relative_to(target) for path in (target / "skillmd").rglob("*") if path.is_file()}
        if (target / "skillmd").is_dir() else set()
    )
    if actual_skillmd != expected_skillmd:
        problems.append("Shift/skillmd inventory differs from the pickup contract")
    return problems


def refresh(target: Path, files: dict[Path, Path]) -> None:
    if target.resolve().parent != BLUEPRINT.resolve() or target.name.casefold() != "shift":
        raise SystemExit(f"FATAL: refusing unexpected Shift target: {target}")
    missing = [source for source in files.values() if not source.is_file()]
    if missing:
        raise SystemExit("FATAL: missing Shift source: " + ", ".join(map(str, missing)))
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary_name:
        staged = Path(temporary_name) / "skillmd"
        for relative, source in files.items():
            destination = staged / Path(*relative.parts[1:]) if relative.parts[0] == "skillmd" else target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        skillmd = target / "skillmd"
        if skillmd.exists():
            remove_tree(skillmd)
        shutil.copytree(staged, skillmd)
    for name in OBSOLETE:
        obsolete = target / name
        if obsolete.is_file():
            obsolete.unlink()
    problems = verify(target, files)
    if problems:
        raise SystemExit("FATAL: " + "; ".join(problems))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--target", type=Path, default=DEFAULT_SHIFT)
    args = parser.parse_args()
    files = expected_files()
    if args.check:
        problems = verify(args.target, files)
        if problems:
            print("\n".join(problems))
            return 1
    else:
        refresh(args.target, files)
    print("Shift: PASS - 8 loose documents, 6 skill folders and 6 ZIPs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
