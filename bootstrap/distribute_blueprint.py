#!/usr/bin/env python3
"""Publish the validated Blueprint commit and back up its portability kit."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import re
import shutil
import subprocess
import sys
import time
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SOURCE = REPO / "Blueprint"
DESTINATIONS = (
    "pCloud:Public Folder/pipeline-registry/Blueprint",
    "GDrive:pipeline-registry/Blueprint",
    "onedrivebkp:pipeline-registry/Blueprint",
)
PORTABILITY_DESTINATION = "onedrivebkp:BKPDE-Portability"
PORTABILITY_FILES = ("BKPDE-Portability.zip", "MANIFEST.json", "AUDIT-SNAPSHOT.json")
SHIFT = SOURCE / "Shift"
WORKFLOW = "Validate Blueprint beta"
RCLONE_FILTERS = ("--exclude", "**/__pycache__/**", "--exclude", "**/*.pyc")


def executable(name: str) -> str:
    found = shutil.which(name)
    if not found and name == "rclone":
        bundled = Path(r"C:\Program Files\RcloneView\rclone.exe")
        found = str(bundled) if bundled.is_file() else None
    if not found:
        raise SystemExit(f"FATAL: {name} is not installed or is not on PATH")
    return found


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, encoding="utf-8",
                          cwd=REPO,
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.STDOUT if capture else None)


def preflight() -> None:
    if not (SOURCE / "VERSION.txt").is_file() or not (SOURCE / "BLUEPRINT.md").is_file():
        raise SystemExit(f"FATAL: incomplete Blueprint source: {SOURCE}")
    rclone = executable("rclone")
    remotes = set(run([rclone, "listremotes"], capture=True).stdout.splitlines())
    required = {"pCloud:", "GDrive:", "onedrivebkp:"}
    if not required.issubset(remotes):
        raise SystemExit(f"FATAL: missing rclone remotes: {sorted(required - remotes)}")
    for remote in sorted(required):
        run([rclone, "lsd", remote, "--max-depth", "1"], capture=True)
    print("distribution preflight: PASS - Blueprint source, rclone and all three remotes available")


def wait_validation(commit: str) -> None:
    gh = executable("gh")
    deadline = time.monotonic() + 180
    run_id: int | None = None
    while time.monotonic() < deadline:
        result = run([gh, "run", "list", "--commit", commit, "--workflow", WORKFLOW,
                      "--limit", "1", "--json", "databaseId,status,conclusion"], capture=True)
        rows = json.loads(result.stdout or "[]")
        if rows:
            run_id = int(rows[0]["databaseId"])
            break
        time.sleep(5)
    if run_id is None:
        raise SystemExit(f"FATAL: no GitHub validation appeared for {commit} within 180 seconds")
    run([gh, "run", "watch", str(run_id), "--exit-status"])
    print(f"GitHub validation: PASS - run {run_id}")


def confirmed_validation(commit: str) -> int:
    gh = executable("gh")
    result = run([gh, "run", "list", "--commit", commit, "--workflow", WORKFLOW,
                  "--limit", "1", "--json", "databaseId,status,conclusion"], capture=True)
    rows = json.loads(result.stdout or "[]")
    if not rows or rows[0].get("status") != "completed" or rows[0].get("conclusion") != "success":
        raise SystemExit(f"FATAL: no successful completed validation for {commit}")
    return int(rows[0]["databaseId"])


def committed_tree(commit: str, temporary: Path) -> Path:
    if not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise SystemExit("FATAL: publish requires a full 40-character commit SHA")
    head = run(["git", "rev-parse", "HEAD"], capture=True).stdout.strip()
    if head.lower() != commit.lower():
        raise SystemExit(f"FATAL: validated commit {commit} is not current HEAD {head}")
    archive = temporary / "blueprint.zip"
    paths = ["Blueprint", *(f"PORTABILITY/{name}" for name in PORTABILITY_FILES)]
    run(["git", "archive", "--format=zip", f"--output={archive}", commit, *paths])
    with zipfile.ZipFile(archive) as package:
        package.extractall(temporary / "tree")
    tree = temporary / "tree"
    if not (tree / "Blueprint" / "VERSION.txt").is_file():
        raise SystemExit("FATAL: committed Blueprint archive is incomplete")
    if any(not (tree / "PORTABILITY" / name).is_file() for name in PORTABILITY_FILES):
        raise SystemExit("FATAL: committed portability backup is incomplete")
    return tree


def remote_inventory(rclone: str, destination: str, source: Path) -> tuple[int, int]:
    result = run([rclone, "lsf", "-R", "--files-only", destination, *RCLONE_FILTERS], capture=True)
    remote_paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    duplicates = sorted(path for path, count in Counter(remote_paths).items() if count > 1)
    if duplicates:
        raise SystemExit(f"FATAL: duplicate remote paths at {destination}: {duplicates}")
    local_paths = {p.relative_to(source).as_posix() for p in source.rglob("*") if p.is_file()}
    extras = sorted(set(remote_paths) - local_paths)
    if extras:
        print(f"notice: {destination} has {len(extras)} remote-only file(s); none deleted")
    return len(local_paths), len(extras)


def write_receipt(commit: str, version: str, run_id: int, results: list[dict]) -> None:
    receipt_dir = REPO / ".publication"
    receipt_dir.mkdir(exist_ok=True)
    payload = {"edition": version, "commit": commit, "github_run": run_id,
               "github_conclusion": "success", "destinations": results}
    (receipt_dir / "last.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def publish(commit: str) -> None:
    preflight()
    run_id = confirmed_validation(commit)
    run([sys.executable, str(HERE / "shift.py"), "--check"])
    rclone = executable("rclone")
    results = []
    with tempfile.TemporaryDirectory() as temporary_name:
        tree = committed_tree(commit, Path(temporary_name))
        source = tree / "Blueprint"
        shutil.copytree(SHIFT, source / "Shift")
        version = (source / "VERSION.txt").read_text(encoding="utf-8").strip()
        for destination in DESTINATIONS:
            run([rclone, "copy", str(source), destination, "--create-empty-src-dirs", *RCLONE_FILTERS])
            run([rclone, "check", str(source), destination, "--one-way", *RCLONE_FILTERS])
            files, extras = remote_inventory(rclone, destination, source)
            results.append({"destination": destination, "files": files, "remote_extras": extras})
        portability = tree / "PORTABILITY"
        run([rclone, "copy", str(portability), PORTABILITY_DESTINATION])
        run([rclone, "check", str(portability), PORTABILITY_DESTINATION, "--one-way"])
        files, extras = remote_inventory(rclone, PORTABILITY_DESTINATION, portability)
        results.append({"destination": PORTABILITY_DESTINATION, "files": files,
                        "remote_extras": extras, "scope": "portability backup"})
    write_receipt(commit, version, run_id, results)
    print(f"distribution: PASS - Blueprint, including Shift, on 3 mirrors plus portability backup verified from {commit[:12]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--publish", metavar="COMMIT")
    group.add_argument("--wait-validation", metavar="COMMIT")
    args = parser.parse_args()
    try:
        if args.preflight:
            preflight()
        elif args.publish:
            publish(args.publish)
        else:
            wait_validation(args.wait_validation)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"FATAL: command failed with exit code {exc.returncode}") from exc


if __name__ == "__main__":
    main()
