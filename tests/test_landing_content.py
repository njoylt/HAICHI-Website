import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]

INDEXABLE_USE_CASES = {
    "ollama-agents.html": ("Local Ollama Agents Workflow", "Ollama"),
    "local-ai-code-review.html": ("Local AI Code Review Workflow", "Reviewer + Verifier"),
    "windows-ollama-agents.html": ("Windows Ollama Agents Workflow", "Windows"),
    "local-ai-coding-workflow.html": ("Local AI Coding Workflow", "repeatable workflow"),
    "open-webui-vs-haichi.html": ("Open WebUI vs HAICHI", "Open WebUI"),
    "visible-agent-state.html": ("Visible AI Agent State", "visible"),
}


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

    def test_homepage_hero_leads_with_reviewer_verifier_workflow(self):
        self.assertIn("One agent reviews. The second tries to prove it wrong.", self.html)
        self.assertIn("Reviewer + Verifier for local AI code review", self.html)
        self.assertIn("A local review that earns your trust", self.html)
        self.assertIn("counter-evidence loop", self.html)
        self.assertIn("Runs locally in HAICHI.", self.html)
        self.assertIn("Local AI chat is not the same as local agent workflow.", self.html)
        self.assertIn("Try Reviewer + Verifier", self.html)

    def test_both_editions_keep_separate_checkout_links(self):
        self.assertIn("719fddae-0c70-4f2d-9127-0a2222c418ca", self.html)
        self.assertIn("80cf9d56-652b-4b5e-baf9-1cf53c7b4eab", self.html)
        self.assertIn("haichi.lemonsqueezy.com/checkout", self.html)
        self.assertIn("Personal and Pro are separate builds", self.html)

    def test_founder_offer_is_present_without_replacing_public_price(self):
        self.assertIn("Founder test", self.html)
        self.assertIn("&euro;29 for the first 10 useful Pro users.", self.html)
        self.assertIn("Get Developer Pro (&euro;49)", self.html)
        self.assertIn("Copy &euro;29 founder request", self.html)
        self.assertIn("Open feedback form", self.html)

    def test_founder_request_has_low_friction_copy_fallback(self):
        self.assertIn("GitHub login should not block the request", self.html)
        self.assertIn("data-copy-text=", self.html)
        self.assertIn("I want the €29 founder code for Developer Pro", self.html)
        self.assertIn("Founder request copied", self.html)
        self.assertIn("early-user-feedback.yml", self.html)

    def test_release_check_count_matches_current_project_suite(self):
        self.assertIn(
            "<strong>194</strong><span>current source tests</span>", self.html
        )

    def test_feedback_template_accepts_founder_code_requests(self):
        self.assertIn("id: founder_code", self.feedback_template)
        self.assertIn("Yes, I tried Personal and want to buy Pro", self.feedback_template)

    def test_download_section_does_not_copy_contextless_install_commands(self):
        self.assertNotIn("copy-install", self.html)
        self.assertNotIn("copy-install", self.script)
        self.assertNotIn("data-command=", self.html)

    def test_checkout_uses_verified_landing_attribution(self):
        self.assertIn("v1_1_verified_checkout", self.script)

    def test_measurement_tracks_campaign_and_conversion_context(self):
        for field in ("utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"):
            self.assertIn(field, self.script)
        for event in ("page_view", "checkout_click", "product_tour_click", "feedback_form_click"):
            self.assertIn(event, self.html + self.script)
        self.assertIn("window.dataLayer", self.script)
        self.assertIn("haichi:measurement", self.script)

    def test_checkout_receives_edition_and_cta_placement(self):
        self.assertIn("checkout[custom][edition]", self.script)
        self.assertIn("checkout[custom][cta_placement]", self.script)
        self.assertIn('data-edition="personal"', self.html)
        self.assertIn('data-edition="developer_pro"', self.html)
        self.assertIn('data-placement="hero"', self.html)

    def test_copy_buttons_support_direct_text_and_custom_toasts(self):
        self.assertIn("dataset.copyText", self.script)
        self.assertIn("dataset.copyLabel", self.script)
        self.assertIn("Text copied", self.script)

    def test_homepage_links_to_searchable_use_case_pages(self):
        self.assertIn('id="use-cases"', self.html)
        for filename in INDEXABLE_USE_CASES:
            self.assertIn(f"/use-cases/{filename}", self.html)

    def test_use_case_pages_have_indexable_seo_metadata(self):
        for filename, expected in INDEXABLE_USE_CASES.items():
            with self.subTest(filename=filename):
                page = (ROOT / "use-cases" / filename).read_text(encoding="utf-8")
                title, topic = expected
                self.assertIn(title, page)
                self.assertIn(topic, page)
                self.assertIn('name="description"', page)
                self.assertIn('rel="canonical"', page)
                self.assertIn("TechArticle", page)
                self.assertIn("HAICHI", page)

    def test_sitemap_exposes_use_case_urls(self):
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for filename in INDEXABLE_USE_CASES:
            self.assertIn(f"https://haichi.app/use-cases/{filename}", sitemap)
        self.assertIn("<lastmod>2026-08-02</lastmod>", sitemap)

    def test_text_sitemap_matches_indexable_use_case_urls(self):
        text_sitemap = (ROOT / "sitemap.txt").read_text(encoding="utf-8")
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("https://haichi.app/", text_sitemap)
        for filename in INDEXABLE_USE_CASES:
            self.assertIn(f"https://haichi.app/use-cases/{filename}", text_sitemap)
        self.assertIn("Sitemap: https://haichi.app/sitemap.txt", robots)


if __name__ == "__main__":
    unittest.main()
