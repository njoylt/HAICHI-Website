import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class LandingContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.script = (ROOT / "app.js").read_text(encoding="utf-8")
        cls.feedback_template = (
            ROOT / ".github" / "ISSUE_TEMPLATE" / "early-user-feedback.yml"
        ).read_text(encoding="utf-8")

    def test_first_workflow_is_concrete(self):
        self.assertIn('id="first-workflow"', self.html)
        self.assertIn("Reviewer", self.html)
        self.assertIn("Verifier", self.html)
        self.assertIn("Copy starter task", self.html)

    def test_both_editions_use_request_links_while_checkout_is_verified(self):
        self.assertNotIn("haichi.lemonsqueezy.com/checkout", self.html)
        self.assertNotIn("haichi.lemonsqueezy.com/checkout", self.script)
        self.assertIn("Personal%20download%20request", self.html)
        self.assertIn("Developer%20Pro%20request", self.html)
        self.assertIn("Personal and Pro are separate builds", self.html)

    def test_founder_offer_is_present_without_replacing_public_price(self):
        self.assertIn("Founder test", self.html)
        self.assertIn("&euro;29 for the first 10 useful Pro users.", self.html)
        self.assertIn("Request Developer Pro (&euro;49)", self.html)
        self.assertIn("Ask for &euro;29 founder code", self.html)

    def test_feedback_template_accepts_founder_code_requests(self):
        self.assertIn("id: founder_code", self.feedback_template)
        self.assertIn("Yes, I tried Personal and want to buy Pro", self.feedback_template)

    def test_download_section_does_not_copy_contextless_install_commands(self):
        self.assertNotIn("copy-install", self.html)
        self.assertNotIn("copy-install", self.script)
        self.assertNotIn("data-command=", self.html)

    def test_temporary_checkout_notice_is_visible(self):
        self.assertIn("Checkout delivery is being verified", self.html)


if __name__ == "__main__":
    unittest.main()
