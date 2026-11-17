from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path

import yaml


if tuple(__import__("sys").version_info) < (3, 12):
    raise SystemExit("FATAL: Blueprint builds require Python 3.12 or newer")


VERSION_RE = re.compile(r"^<!-- MASTER ([A-Za-z0-9_.-]+) -->$", re.M)
PART_RE = re.compile(r"^<!-- COMPONENT: ([A-Z_]+) -->\n(.*?)\n<!-- END COMPONENT: \1 -->$", re.M | re.S)
PARTS = {
    "BOOT": "boot",
    "THAI_PLACES": "thai-places",
    "CHECK": "check",
    "PHOTO": "photo",
    "PR": "pr",
    "EDIT": "edit",
}
EDITION_WRAPPERS = {
    "THAI_PLACES": "# THAI PLACES",
    "CHECK": "# [P4] PAGE CHECKS AND QC",
    "PHOTO": "# [P3] PHOTO TASKS",
    "PR": "# [P5] PR COPY",
    "EDIT": "# EDITING",
}
COMPAT_FILES = ("BLUEPRINT.txt", "GUIDE.txt", "PROCESSES.txt", "DIRECTORY.txt", "DIRECTORY.yaml", "VERSION.txt")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def remove_tree(path: Path) -> None:
    def clear(function, target, _error):
        os.chmod(target, stat.S_IWRITE)
        function(target)

    shutil.rmtree(path, onexc=clear)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_frontmatter(text: str) -> str:
    match = re.match(r"^---\n.*?\n---\n\n?", text, re.S)
    if not match:
        raise SystemExit("FATAL: component lacks front matter")
    return text[match.end():]


def frontmatter_name(text: str) -> str:
    match = re.match(r"^---\n.*?^name:\s*([^\n]+).*?^---\n", text, re.M | re.S)
    if not match:
        raise SystemExit("FATAL: invalid skill front matter")
    return match.group(1).strip()


def validate_release(source: Path) -> None:
    _master, _version, parts = load(source)
    for marker, skill in PARTS.items():
        match = re.match(r"^---\n(.*?)\n---\n", parts[marker], re.S)
        metadata = yaml.safe_load(match.group(1)) if match else None
        if not isinstance(metadata, dict) or set(metadata) != {"name", "description"}:
            raise SystemExit(f"FATAL: {marker} skill metadata must contain only name and description")
        if metadata["name"] != skill or not isinstance(metadata["description"], str) or not metadata["description"].strip():
            raise SystemExit(f"FATAL: {marker} skill metadata is invalid")


def yaml_blocks(text: str) -> list[str]:
    return re.findall(r"```yaml\s*\n(.*?)```", text, re.S)


def load(source: Path):
    text = source.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    version_match = VERSION_RE.search(text)
    if not version_match:
        raise SystemExit("FATAL: master edition mark missing")
    matches = list(PART_RE.finditer(text))
    found = [(match.group(1), match.group(2).lstrip("\n")) for match in matches]
    names = [name for name, _body in found]
    if names != list(PARTS):
        raise SystemExit(f"FATAL: component inventory differs or contains duplicates: {names}")
    for previous, current in zip(matches, matches[1:]):
        marker = current.group(1)
        residue = text[previous.end():current.start()].strip()
        if residue != EDITION_WRAPPERS[marker]:
            preview = residue.splitlines()[0][:80] if residue else "<missing wrapper>"
            raise SystemExit(f"FATAL: invalid edition wrapper before {marker}: {preview}")
    if text[matches[-1].end():].strip():
        raise SystemExit("FATAL: unmarked content after final component")
    parts = dict(found)
    for marker, skill in PARTS.items():
        if frontmatter_name(parts[marker]) != skill:
            raise SystemExit(f"FATAL: {marker} front-matter name differs")
    edition_line = f"Edition: `{version_match.group(1)}`"
    if parts["BOOT"].count(edition_line) != 1:
        raise SystemExit("FATAL: visible Boot edition differs from master edition")
    return text, version_match.group(1), parts


def build_directory(parts: dict[str, str]) -> tuple[str, dict]:
    edit_blocks = yaml_blocks(strip_frontmatter(parts["EDIT"]))
    thai_blocks = yaml_blocks(strip_frontmatter(parts["THAI_PLACES"]))
    if len(edit_blocks) != 1 or len(thai_blocks) != 1:
        raise SystemExit("FATAL: edit and Thai Places must each carry one YAML block")
    edit = yaml.safe_load(edit_blocks[0])
    thai = yaml.safe_load(thai_blocks[0])
    branches = dict(edit["directory"])
    if "thai_places" in branches or set(thai["directory"]) != {"thai_places"}:
        raise SystemExit("FATAL: Thai Places split is invalid")
    branches = {"thai_places": thai["directory"]["thai_places"], **branches}
    directory = {"directory": branches}
    if len(directory["directory"]["thai_places"]["provinces"]) != 76:
        raise SystemExit("FATAL: Thai Places does not contain 76 provinces")
    return yaml.safe_dump(directory, sort_keys=False, allow_unicode=True, width=1000), directory


def validate_routes(parts: dict[str, str], directory: dict) -> dict:
    boot_blocks = yaml_blocks(strip_frontmatter(parts["BOOT"]))
    if len(boot_blocks) != 1:
        raise SystemExit("FATAL: boot must carry one semantic route map")
    routes = yaml.safe_load(boot_blocks[0])["routes"]
    bodies = {PARTS[k]: strip_frontmatter(v) for k, v in parts.items()}
    edition_headings = {PARTS[marker]: heading for marker, heading in EDITION_WRAPPERS.items()}
    resources = {"boot / desk-agent": "boot", **{name: name for name in PARTS.values()}}
    codes = []
    reference_routes = set()
    for semantic, route in routes.items():
        resource = resources[route["resource"]]
        if semantic.startswith("directory."):
            reference_routes.add(semantic)
            if route["heading"] != semantic:
                raise SystemExit(f"FATAL: reference target differs: {semantic}")
        else:
            heading_pattern = rf"^#{{1,6}}\s+{re.escape(route['heading'])}\s*$"
            target = bodies[resource] + "\n" + edition_headings.get(resource, "")
            if not re.search(heading_pattern, target, re.M):
                raise SystemExit(f"FATAL: route target missing: {semantic}")
            match = re.match(r"\[([^]]+)\]", route["heading"])
            if not match:
                raise SystemExit(f"FATAL: procedural route lacks heading code: {semantic}")
            codes.append(match.group(1))
    expected_refs = {f"directory.{name}" for name in directory["directory"]}
    if reference_routes != expected_refs:
        raise SystemExit("FATAL: semantic reference routes differ from Directory")
    if len(routes) != 37 or len(codes) != 21 or len(set(codes)) != 21:
        raise SystemExit("FATAL: semantic route counts differ")
    all_bodies = "\n".join(bodies.values())
    if all_bodies.count("# [G1-A] HOUSE ESSENTIALS") != 1:
        raise SystemExit("FATAL: House Essentials must occur once")
    return {"semantic_routes": len(routes), "heading_codes": len(codes), "reference_routes": len(reference_routes)}


def bounded(text: str, start: str, end: str) -> str:
    a = text.find(start)
    b = text.find(end, a + len(start))
    if a < 0 or b < 0:
        raise SystemExit(f"FATAL: cannot extract {start}")
    return text[a:b].rstrip() + "\n"


def zip_skill(path: Path, skill: str, skill_file: Path) -> None:
    stamp = (2026, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as archive:
        info = zipfile.ZipInfo(f"{skill}/SKILL.md", date_time=stamp)
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        info.compress_type = zipfile.ZIP_STORED
        archive.writestr(info, skill_file.read_bytes())


def index_yaml(version: str, files: list[Path], base: Path) -> str:
    payload = {"version": version, "files": []}
    for path in files:
        payload["files"].append({"path": path.relative_to(base).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)})
    return yaml.safe_dump(payload, sort_keys=False)


def build(source: Path, root: Path) -> None:
    master, version, parts = load(source)
    directory_text, directory = build_directory(parts)
    checks = validate_routes(parts, directory)
    deploy = root / "DEPLOY"
    upload = root / "UPLOAD"
    for path in (deploy, upload):
        if path.exists():
            remove_tree(path)
        path.mkdir(parents=True)

    skill_files = []
    routed_files = []
    for marker, skill in PARTS.items():
        text = parts[marker].rstrip() + "\n"
        skill_path = deploy / "skills" / skill / "SKILL.md"
        routed_name = "BOOT.md" if skill == "boot" else f"{skill}.md"
        routed_path = deploy / "routed" / ("modules" if skill in {"check", "photo", "pr"} else "") / routed_name
        write(skill_path, text)
        write(routed_path, text)
        skill_files.append(skill_path)
        routed_files.append(routed_path)
        zip_skill(upload / f"{skill}.zip", skill, skill_path)

    directory_with_mark = f"# {version}\n" + directory_text
    write(deploy / "DIRECTORY.yaml", directory_with_mark)
    write(deploy / "DIRECTORY.txt", directory_with_mark)
    write(root / "DIRECTORY.yaml", directory_with_mark)
    write(root / "DIRECTORY.txt", directory_with_mark)

    write(deploy / "skills" / "INDEX.yaml", index_yaml(version, skill_files, deploy / "skills"))
    write(deploy / "routed" / "INDEX.yaml", index_yaml(version, routed_files, deploy / "routed"))
    deploy_files = sorted(
        (p for p in deploy.rglob("*") if p.is_file()),
        key=lambda p: p.relative_to(deploy).as_posix().casefold(),
    )
    write(deploy / "INDEX.yaml", index_yaml(version, deploy_files, deploy))

    edit = strip_frontmatter(parts["EDIT"])
    write(root / "BLUEPRINT.txt", master.rstrip() + "\n")
    write(root / "GUIDE.txt", f"<!-- {version} -->\n" + bounded(edit, "# [G1] INPUT", "# [P] PROCESSES"))
    write(root / "PROCESSES.txt", f"<!-- {version} -->\n" + bounded(edit, "# [P] PROCESSES", "# [R] RETURN"))
    write(root / "VERSION.txt", version + "\n")

    receipt = {
        "version": version,
        "source": source.name,
        "source_sha256": sha(source),
        "checks": checks,
        "deploy_files": len(deploy_files) + 1,
        "upload_zips": {p.name: sha(p) for p in sorted(upload.glob("*.zip"))},
        "compatibility_files": {name: sha(root / name) for name in COMPAT_FILES},
    }
    write(root / "build-receipt.json", json.dumps(receipt, indent=2) + "\n")
    print(f"built {version}: 6 skills, 37 routes, 16 Directory branches, 6 zips")


def compare_trees(expected: Path, actual: Path) -> None:
    left = sorted(p.relative_to(expected) for p in expected.rglob("*") if p.is_file())
    right = sorted(p.relative_to(actual) for p in actual.rglob("*") if p.is_file())
    if left != right:
        raise SystemExit("FATAL: generated inventory differs")
    for rel in left:
        if (expected / rel).read_bytes() != (actual / rel).read_bytes():
            raise SystemExit(f"FATAL: generated file differs: {rel}")


def check(source: Path, root: Path) -> None:
    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        build(source, temp)
        compare_trees(root / "DEPLOY", temp / "DEPLOY")
        compare_trees(root / "UPLOAD", temp / "UPLOAD")
        for name in (*COMPAT_FILES, "build-receipt.json"):
            if (root / name).read_bytes() != (temp / name).read_bytes():
                raise SystemExit(f"FATAL: generated output differs: {name}")
    print("check: PASS - all generated files reproduce byte-for-byte")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--release", action="store_true", help="run release validation; retained for guarded-push compatibility")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    source = here / "BLUEPRINT.md"
    if args.release:
        validate_release(source)
    check(source, here) if args.check else build(source, here)
