import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class LandingContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.script = (ROOT / "app.js").read_text(encoding="utf-8")

    def test_first_workflow_is_concrete(self):
        self.assertIn('id="first-workflow"', self.html)
        self.assertIn("Reviewer", self.html)
        self.assertIn("Verifier", self.html)
        self.assertIn("Copy starter task", self.html)

    def test_both_editions_keep_separate_checkout_links(self):
        self.assertIn("719fddae-0c70-4f2d-9127-0a2222c418ca", self.html)
        self.assertIn("80cf9d56-652b-4b5e-baf9-1cf53c7b4eab", self.html)
        self.assertIn("Personal and Pro are separate builds", self.html)

    def test_download_section_does_not_copy_contextless_install_commands(self):
        self.assertNotIn("copy-install", self.html)
        self.assertNotIn("copy-install", self.script)
        self.assertNotIn("data-command=", self.html)

    def test_checkout_uses_new_landing_attribution(self):
        self.assertIn("v1_1_reviewer_verifier", self.script)


if __name__ == "__main__":
    unittest.main()
