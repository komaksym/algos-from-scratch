import subprocess
import sys
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryLayoutTest(unittest.TestCase):
    def test_documented_example_paths_exist(self):
        for name in [
            "dsa/palindrome.py",
            "ml/in_numpy/adam.py",
            "ml/in_torch/adam.py",
            "ml/sandbox/classifier_with_imbalance_class.py",
        ]:
            with self.subTest(path=name):
                self.assertTrue((ROOT / name).is_file(), name)
        for name in ["in_numpy", "in_torch"]:
            self.assertFalse(list((ROOT / name).glob("*.py")), name)

    def test_project_identity_matches_repository_name(self):
        with (ROOT / "pyproject.toml").open("rb") as stream:
            project = tomllib.load(stream)["project"]
        self.assertEqual(project["name"], "algos-from-scratch")

    def test_palindrome_command_reports_success_for_every_case(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "dsa/palindrome.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertTrue(lines, "The command must run its examples.")
        self.assertTrue(all(line.startswith("OK: ") for line in lines), result.stdout)


if __name__ == "__main__":
    unittest.main()
