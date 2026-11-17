from __future__ import annotations

import importlib.util
import re
import stat
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from docx import Document


REPO = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


build = load_module("blueprint_build", REPO / "Blueprint" / "build.py")
word = load_module("word_build", REPO / "Blueprint" / "build_human_volume.py")
distribution = load_module("distribution", REPO / "bootstrap" / "distribute_blueprint.py")
shift = load_module("shift", REPO / "bootstrap" / "shift.py")


class MechanismGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = (REPO / "Blueprint" / "BLUEPRINT.md").read_text(encoding="utf-8")

    def load_text(self, text: str):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "BLUEPRINT.md"
            source.write_text(text, encoding="utf-8", newline="\n")
            return build.load(source)

    def test_duplicate_component_is_rejected(self):
        pr = re.search(
            r"<!-- COMPONENT: PR -->.*?<!-- END COMPONENT: PR -->", self.master, re.S
        ).group(0)
        with self.assertRaises(SystemExit):
            self.load_text(self.master + "\n" + pr + "\n")

    def test_unmarked_component_residue_is_rejected(self):
        damaged = self.master.replace(
            "<!-- END COMPONENT: CHECK -->\n# [P3] PHOTO TASKS\n<!-- COMPONENT: PHOTO -->",
            "<!-- END COMPONENT: CHECK -->\nLOST RULE\n# [P3] PHOTO TASKS\n<!-- COMPONENT: PHOTO -->",
        )
        with self.assertRaises(SystemExit):
            self.load_text(damaged)

    def test_edition_wrapper_is_required_exactly(self):
        damaged = self.master.replace("# EDITING\n<!-- COMPONENT: EDIT -->", "# EDIT\n<!-- COMPONENT: EDIT -->")
        with self.assertRaises(SystemExit):
            self.load_text(damaged)

    def test_visible_boot_edition_matches_master(self):
        damaged = self.master.replace("Edition: `171126_gpt_resequenced`", "Edition: `wrong-edition`")
        with self.assertRaises(SystemExit):
            self.load_text(damaged)

    def test_edition_wrappers_are_not_written_into_skills(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "BLUEPRINT.md"
            source.write_text(self.master, encoding="utf-8", newline="\n")
            build.build(source, root)
            skill_text = "\n".join(path.read_text(encoding="utf-8") for path in (root / "DEPLOY" / "skills").glob("*/SKILL.md"))
            for heading in build.EDITION_WRAPPERS.values():
                self.assertNotIn(heading, skill_text)

    def test_directory_routes_use_current_name(self):
        _master, _version, parts = self.load_text(self.master)
        _directory_text, directory = build.build_directory(parts)
        self.assertIn("directory", directory)
        self.assertNotIn("references", directory)
        self.assertNotIn("references.", self.master)

    def test_route_requires_a_real_heading(self):
        master, _version, parts = self.load_text(self.master)
        directory_text, directory = build.build_directory(parts)
        del directory_text
        parts["EDIT"] = parts["EDIT"].replace("## [P2] VERIFICATION", "[P2] VERIFICATION", 1)
        with self.assertRaises(SystemExit):
            build.validate_routes(parts, directory)

    def test_boot_route_map_cannot_substitute_for_boot_heading(self):
        master, _version, parts = self.load_text(self.master)
        directory_text, directory = build.build_directory(parts)
        del master, directory_text
        parts["BOOT"] = parts["BOOT"].replace("# [M] MODE DISPATCH", "[M] MODE DISPATCH", 1)
        with self.assertRaises(SystemExit):
            build.validate_routes(parts, directory)

    def test_body_horizontal_rule_does_not_hide_following_text(self):
        doc = Document()
        word.configure(doc)
        word.render_markdown(doc, "---\nname: fixture\ndescription: fixture\n---\n\nBefore\n\n---\n\nAFTER TOKEN")
        visible = "\n".join(p.text for p in doc.paragraphs)
        self.assertIn("AFTER TOKEN", visible)

    def test_word_numbered_examples_restart_from_source(self):
        doc = Document()
        word.configure(doc)
        word.render_markdown(doc, "1. First\n2. Second")
        word.render_markdown(doc, "1. Restarted")
        visible = [p.text for p in doc.paragraphs if p.text]
        self.assertEqual(visible, ["1. First", "2. Second", "1. Restarted"])

    def test_release_metadata_is_valid(self):
        build.validate_release(REPO / "Blueprint" / "BLUEPRINT.md")

    def test_duplicate_remote_paths_are_rejected(self):
        original_run = distribution.run
        distribution.run = lambda *_args, **_kwargs: SimpleNamespace(stdout="same.txt\nsame.txt\n")
        try:
            with tempfile.TemporaryDirectory() as folder, self.assertRaises(SystemExit):
                source = Path(folder)
                (source / "same.txt").write_text("fixture", encoding="utf-8")
                distribution.remote_inventory("rclone", "fixture:", source)
        finally:
            distribution.run = original_run

    def test_remote_extras_are_reported_not_deleted(self):
        original_run = distribution.run
        distribution.run = lambda *_args, **_kwargs: SimpleNamespace(stdout="same.txt\nold.txt\n")
        try:
            with tempfile.TemporaryDirectory() as folder:
                source = Path(folder)
                (source / "same.txt").write_text("fixture", encoding="utf-8")
                files, extras = distribution.remote_inventory("rclone", "fixture:", source)
                self.assertEqual((files, extras), (1, 1))
        finally:
            distribution.run = original_run

    def test_shift_contract_is_exactly_eight_loose_and_twelve_skill_files(self):
        files = shift.expected_files()
        loose = {path for path in files if path.parts[0] != "skillmd"}
        skillmd = {path for path in files if path.parts[0] == "skillmd"}
        self.assertEqual(len(loose), 8)
        self.assertEqual(len(skillmd), 12)
        self.assertNotIn(Path("Bangkok_Post_Blueprint.docx"), loose)
        self.assertEqual(shift.DEFAULT_SHIFT, REPO / "Blueprint" / "Shift")

    def test_shift_removes_readonly_legacy_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            tree = Path(folder) / "skillmd"
            legacy = tree / "zips" / "edit"
            legacy.mkdir(parents=True)
            legacy.chmod(stat.S_IREAD)
            shift.remove_tree(tree)
            self.assertFalse(tree.exists())

    def test_sync_master_covers_exact_shift_contract(self):
        index = (REPO / "SYNC-MASTER.md").read_text(encoding="utf-8")
        files = shift.expected_files()
        rows = re.findall(r"^\| `([^`]+)`\s+\|", index, re.M)
        self.assertEqual(set(rows), {path.as_posix() for path in files})
        self.assertEqual(len(rows), 20)
        indexed_rows = re.findall(r"^\| `[^`]+`.*$", index, re.M)
        self.assertEqual(len(indexed_rows), 20)
        self.assertTrue(all("postpublishing-my.sharepoint.com" in row for row in indexed_rows))
        self.assertNotIn(
            "github.com/cliffspab/pipeline-registry/tree/main/Blueprint/Shift",
            index,
        )


if __name__ == "__main__":
    unittest.main()
