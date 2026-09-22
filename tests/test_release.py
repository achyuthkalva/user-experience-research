import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from tools.build import ROOT, build, zip_bytes_path
from tools.validate import validate


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = build()
        cls.c = json.loads((ROOT / "release.json").read_text())

    def test_static_checks_pass(self):
        failures = [r for r in validate() if not r["passed"]]
        self.assertEqual(failures, [])

    def test_build_is_reproducible(self):
        before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.artifacts}
        after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in build()}
        self.assertEqual(before, after)

    def test_archives_reject_path_traversal(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                zip_bytes_path(Path(d) / "bad.zip", [("../x", b"x")], "2026-09-22")

    def test_archives_reject_absolute_paths(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                zip_bytes_path(Path(d) / "bad.zip", [("/x", b"x")], "2026-09-22")

    def test_archives_reject_duplicate_entries(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                zip_bytes_path(Path(d) / "bad.zip", [("x", b"x"), ("x", b"x")], "2026-09-22")

    def test_team_pack_has_activation_and_text_fallback(self):
        v = self.c["version"]
        with zipfile.ZipFile(ROOT / "dist" / f"UX-Research-Team-Pack-v{v}.zip") as z:
            self.assertIn("START-HERE.txt", z.namelist())
            self.assertIn("ACTIVATION-MESSAGE.txt", z.namelist())
            self.assertIn(f"UX-Research-Chat-v{v}.txt", z.namelist())
            self.assertIn(f"ux-research-v{v}.skill", z.namelist())

    def test_github_source_has_no_generated_nested_releases(self):
        v = self.c["version"]
        with zipfile.ZipFile(ROOT / "dist" / f"UX-Research-GitHub-Source-v{v}.zip") as z:
            self.assertIn("ux-research-skill/README.md", z.namelist())
            self.assertFalse(any("/dist/" in n or "/__pycache__/" in n for n in z.namelist()))

    def test_model_cases_not_misrepresented_as_run(self):
        cases = json.loads((ROOT / "tests" / "scenarios.json").read_text())
        self.assertEqual(len(cases), 24)
        self.assertTrue(all(c["status"] == "not-run" for c in cases))
