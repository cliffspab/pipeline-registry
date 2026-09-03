#!/usr/bin/env python3
"""Build the installable Desk Control plugin from CONTROL.txt."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "CONTROL.txt"
OUT = ROOT / "plugin"
MODULES = ("EDIT", "CHECK", "PR", "PHOTO")
META = {
    "EDIT": {
        "description": "Edit Bangkok Post copy through the complete authoritative BLUEPRINT, using its GUIDE workflow and DIRECTORY lookups. Use when explicitly invoked as $edit, @Edit or with a leading literal /edit request, and automatically for Bangkok Post subbing, editing, fitting, headline, deck, caption, proofing, PR-copy, brief, overspill, DCX, Style Log or State Log work.",
        "display": "Bangkok Post Edit",
        "short": "Edit copy to Bangkok Post desk rules",
        "prompt": "Use $edit to edit this Bangkok Post copy with the authoritative BLUEPRINT.",
    },
    "CHECK": {
        "description": "Check placed Bangkok Post copy before initialling through the complete authoritative BLUEPRINT, using its GUIDE workflow and DIRECTORY lookups. Use when explicitly invoked as $check, @Check or with a leading literal /check request.",
        "display": "Bangkok Post Check",
        "short": "Check placed copy before initialling",
        "prompt": "Use $check to check this placed Bangkok Post copy with the authoritative BLUEPRINT.",
    },
    "PR": {
        "description": "Process Bangkok Post paid-placement copy through the complete authoritative BLUEPRINT using its minimum-intervention PR route. Use when explicitly invoked as $pr, @PR or with a leading literal /pr request.",
        "display": "Bangkok Post PR",
        "short": "Process paid-placement copy",
        "prompt": "Use $pr to process this Bangkok Post paid-placement copy with the authoritative BLUEPRINT.",
    },
    "PHOTO": {
        "description": "Handle standalone Bangkok Post headlines and captions through the complete authoritative BLUEPRINT, including visual verification and spatial fitting. Use when explicitly invoked as $photo, @Photo or with a leading literal /photo request.",
        "display": "Bangkok Post Photo",
        "short": "Write and fit standalone captions",
        "prompt": "Use $photo to handle this Bangkok Post headline and caption with the authoritative BLUEPRINT.",
    },
}


def fail(message: str) -> None:
    raise SystemExit(f"FATAL: {message}")


def extract(source: str, name: str) -> str:
    pattern = re.compile(
        rf"^=+ MODULE {name} — BEGIN =+\n(.*?)^=+ MODULE {name} — END =+$",
        re.MULTILINE | re.DOTALL,
    )
    matches = pattern.findall(source)
    if len(matches) != 1:
        fail(f"expected one {name} module, found {len(matches)}")
    return matches[0].strip() + "\n"


def expected_files(source: str) -> dict[Path, str]:
    if not source.startswith("# BANGKOK POST DESK CONTROL\n"):
        fail("CONTROL title is missing")
    edition = next((line.strip() for line in source.splitlines()[1:] if line.strip()), "")
    if not re.fullmatch(r"\d{6}_control_[a-z0-9-]+", edition):
        fail(f"invalid CONTROL edition: {edition!r}")
    common = extract(source, "COMMON")
    if "If the link is unreachable, declare the retrieval failure and stop." not in common:
        fail("unreachable-link rule is missing")
    if re.search(r"audit its completeness|compare it with a snapshot|matching .*edition", common, re.I):
        fail("model-side source audit instructions remain")

    files: dict[Path, str] = {}
    manifest = {
        "name": "edit",
        "version": "0.2.0",
        "description": "Bangkok Post desk workflows governed by the complete BLUEPRINT, comprising GUIDE rules and DIRECTORY lookups.",
        "author": {"name": "Bangkok Post desk"},
        "skills": "./skills/",
        "interface": {
            "displayName": "Bangkok Post Desk Control",
            "shortDescription": "Run Bangkok Post desk workflows",
            "longDescription": "Edit, check, caption and process PR copy using the authoritative linked BLUEPRINT, its GUIDE workflow and its DIRECTORY lookups.",
            "developerName": "Bangkok Post desk",
            "category": "Productivity",
            "capabilities": [
                "Edit Bangkok Post copy",
                "Check placed copy before initialling",
                "Write and fit standalone captions",
                "Apply the paid-placement PR workflow",
                "Apply GUIDE rules and DIRECTORY lookups",
            ],
            "defaultPrompt": [META[name]["prompt"] for name in MODULES],
        },
    }
    files[OUT / ".codex-plugin" / "plugin.json"] = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"

    for name in MODULES:
        slug = name.lower()
        module = extract(source, name)
        skill = (
            "---\n"
            f"name: {slug}\n"
            f"description: {META[name]['description']}\n"
            "---\n\n"
            f"{common}\n{module}"
        )
        agent = (
            "interface:\n"
            f"  display_name: \"{META[name]['display']}\"\n"
            f"  short_description: \"{META[name]['short']}\"\n"
            f"  default_prompt: \"{META[name]['prompt']}\"\n"
        )
        files[OUT / "skills" / slug / "SKILL.md"] = skill
        files[OUT / "skills" / slug / "agents" / "openai.yaml"] = agent
    return files


def main() -> int:
    check = "--check" in sys.argv
    source = SOURCE.read_text(encoding="utf-8")
    files = expected_files(source)
    stale = []
    for path, expected in files.items():
        actual = path.read_text(encoding="utf-8") if path.is_file() else None
        if actual == expected:
            print(f"current: {path.relative_to(ROOT)}")
        elif check:
            stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8", newline="\n")
            print(f"written: {path.relative_to(ROOT)}")
    if stale:
        fail("stale generated CONTROL files: " + ", ".join(stale))
    print(f"CONTROL {next(line for line in source.splitlines()[1:] if line.strip())}: PASS ({len(MODULES)} workflows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())