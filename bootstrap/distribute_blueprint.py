#!/usr/bin/env python3
"""Copy the published Blueprint tree to the two approved cloud mirrors."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "pipeline-registry" / "Blueprint"
DESTINATIONS = (
    "pCloud:Public Folder/pipeline-registry/Blueprint",
    "GDrive:pipeline-registry/Blueprint",
    "onedrivebkp:pipeline-registry/Blueprint",
)
WORKFLOW = "Validate Blueprint beta"
RCLONE_FILTERS = ("--exclude", "**/__pycache__/**", "--exclude", "**/*.pyc")


def executable(name: str) -> str:
    found = shutil.which(name)
    if not found:
        raise SystemExit(f"FATAL: {name} is not installed or is not on PATH")
    return found


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, encoding="utf-8",
                          cwd=ROOT / "pipeline-registry",
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


def publish() -> None:
    preflight()
    rclone = executable("rclone")
    for destination in DESTINATIONS:
        print(f"copying Blueprint -> {destination}")
        run([rclone, "copy", str(SOURCE), destination, "--create-empty-src-dirs",
             "--progress", *RCLONE_FILTERS])
        run([rclone, "check", str(SOURCE), destination, "--one-way", *RCLONE_FILTERS])
        print(f"verified: {destination}")
    print("distribution: PASS - pCloud, Google Drive and OneDrive mirrors verified")


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--publish", action="store_true")
    group.add_argument("--wait-validation", metavar="COMMIT")
    args = parser.parse_args()
    try:
        if args.preflight:
            preflight()
        elif args.publish:
            publish()
        else:
            wait_validation(args.wait_validation)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"FATAL: command failed with exit code {exc.returncode}") from exc


if __name__ == "__main__":
    main()
