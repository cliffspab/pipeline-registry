from __future__ import annotations

import importlib.util
import re
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
            "<!-- END COMPONENT: PR -->\n\n<!-- COMPONENT: THAI_PLACES -->",
            "<!-- END COMPONENT: PR -->\nLOST RULE\n<!-- COMPONENT: THAI_PLACES -->",
        )
        with self.assertRaises(SystemExit):
            self.load_text(damaged)

    def test_route_requires_a_real_heading(self):
        master, _version, parts = self.load_text(self.master)
        directory_text, directory = build.build_directory(parts)
        del directory_text
        parts["PR"] = parts["PR"].replace("# [P5] PR COPY", "[P5] PR COPY", 1)
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


if __name__ == "__main__":
    unittest.main()
