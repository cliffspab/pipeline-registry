#!/usr/bin/env python3
"""Verify the single-master portability kit and its live references."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
REQUIRED = (
    "README.md", "ARCHITECTURE.md", "DEPENDENCIES.md", "COLD-REBUILD.md",
    "RELEASE-RUNBOOK.md", "RECOVERY.md", "make_bundle.py",
)
LIVE = (
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


def check_assembler(base: Path) -> None:
    blueprint = base / "Blueprint"
    script = (
        "const fs=require('fs'),A=require('./assemble.js');"
        "const m=A.parse(fs.readFileSync('./MASTER.md','utf8'));"
        "const o={addendum:'PORTABILITY TEST\\n'};"
        "for(const n of A.outputs(m))A.render(m,n,o);"
        "for(const d of A.deployments(m))A.deployment(m,d,o);"
        "A.custom(m,['1','2','3','4','5','6','7','8'],o);"
        "const t=A.directoryText(m);"
        "if(!t.startsWith('# '+m.edition+'\\n'))throw Error('Directory edition mismatch');"
    )
    try:
        subprocess.run(["node", "-e", script], cwd=blueprint, check=True,
                       capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise SystemExit("FATAL: Node.js is required for portability verification") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"FATAL: assembler verification failed: {exc.stderr.strip()}") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    missing += [f"snapshot/{name}" for name in LIVE
                if not (ROOT / "snapshot" / name).is_file()]
    if args.live:
        missing += [name for name in LIVE if not (REPO / name).is_file()]
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
        check_assembler(REPO)
    check_assembler(ROOT / "snapshot")
    suffix = " plus live references" if args.live else ""
    print(f"portability kit: PASS - {len(manifest['files'])} files match manifest{suffix}")


if __name__ == "__main__":
    main()
