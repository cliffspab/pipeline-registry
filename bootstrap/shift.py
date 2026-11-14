#!/usr/bin/env python3
"""Build or verify the generated Bangkok Post Shift pickup set."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import stat
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "pipeline-registry" / "Blueprint"
DEFAULT_SHIFT = ROOT / "Shift"
SKILLS = ("boot", "edit", "check", "photo", "pr", "thai-places")
LOOSE = {
    "BLUEPRINT.md": REGISTRY / "BLUEPRINT.md",
    "DIRECTORY.yaml": REGISTRY / "DIRECTORY.yaml",
    "boot.md": REGISTRY / "DEPLOY" / "routed" / "boot.md",
    "edit.md": REGISTRY / "DEPLOY" / "routed" / "edit.md",
    "check.md": REGISTRY / "DEPLOY" / "routed" / "modules" / "check.md",
    "photo.md": REGISTRY / "DEPLOY" / "routed" / "modules" / "photo.md",
    "pr.md": REGISTRY / "DEPLOY" / "routed" / "modules" / "pr.md",
    "thai-places.md": REGISTRY / "DEPLOY" / "routed" / "thai-places.md",
    "Bangkok_Post_Blueprint.docx": REGISTRY / "Bangkok_Post_Blueprint_151126_gpt_modular-routes.docx",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clear_readonly(function, target, _error):
    os.chmod(target, stat.S_IWRITE)
    function(target)


def remove_tree(path: Path) -> None:
    shutil.rmtree(path, onexc=clear_readonly)


def expected_files() -> dict[Path, Path]:
    files = {Path(name): source for name, source in LOOSE.items()}
    for skill in SKILLS:
        files[Path("skillmd") / skill / "SKILL.md"] = REGISTRY / "DEPLOY" / "skills" / skill / "SKILL.md"
        files[Path("skillmd") / "zips" / f"{skill}.zip"] = REGISTRY / "UPLOAD" / f"{skill}.zip"
    return files


def inventory(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*") if path.is_file()} if root.is_dir() else set()


def verify(target: Path, files: dict[Path, Path]) -> list[str]:
    problems = []
    missing_sources = [str(source) for source in files.values() if not source.is_file()]
    if missing_sources:
        return ["missing source: " + name for name in missing_sources]
    expected = set(files)
    actual = inventory(target)
    if actual != expected:
        problems.append(f"inventory differs: missing={sorted(map(str, expected-actual))} extra={sorted(map(str, actual-expected))}")
    for rel, source in files.items():
        destination = target / rel
        if not destination.is_file() or digest(destination) != digest(source):
            problems.append(f"stale or missing: Shift/{rel.as_posix()}")
    return problems


def refresh(target: Path, files: dict[Path, Path]) -> None:
    resolved = target.resolve()
    workspace = ROOT.resolve()
    if resolved.parent != workspace or resolved.name.casefold() != "shift":
        raise SystemExit(f"FATAL: refusing to replace unexpected target {resolved}")
    with tempfile.TemporaryDirectory(dir=ROOT, prefix="shift-build-") as temp_name:
        staging = Path(temp_name) / "Shift"
        for rel, source in files.items():
            destination = staging / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        if verify(staging, files):
            raise SystemExit("FATAL: staged Shift verification failed")
        if target.exists():
            remove_tree(target)
        shutil.copytree(staging, target)


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
        missing = [source for source in files.values() if not source.is_file()]
        if missing:
            print("\n".join(f"missing source: {path}" for path in missing))
            return 1
        refresh(args.target, files)
    print("Shift ready: 9 loose documents, 6 SKILL.md folders and 6 ZIP packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
