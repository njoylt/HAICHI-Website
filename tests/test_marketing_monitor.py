import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "marketing_monitor.py"
SPEC = importlib.util.spec_from_file_location("marketing_monitor", MODULE_PATH)
marketing_monitor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(marketing_monitor)


def metrics(*, status=200, age=1, reactions=0, comments=0, feedback=0):
    qualified = comments + feedback
    return {
        "site": {"status": status},
        "campaign_age_hours": age,
        "qualified_signals": qualified,
        "public_engagement": reactions + qualified,
    }


class MarketingMonitorDecisionTests(unittest.TestCase):
    def test_site_outage_has_highest_priority(self):
        self.assertEqual(
            marketing_monitor.choose_alert(metrics(status=None, age=80, comments=3)),
            "site_down",
        )

    def test_qualified_feedback_triggers_promo_review(self):
        self.assertEqual(
            marketing_monitor.choose_alert(metrics(comments=2, feedback=1)),
            "promo_review",
        )

    def test_no_engagement_after_72_hours_triggers_refresh(self):
        self.assertEqual(
            marketing_monitor.choose_alert(metrics(age=72)),
            "campaign_refresh",
        )

    def test_early_zero_state_waits(self):
        self.assertEqual(marketing_monitor.choose_alert(metrics(age=12)), "none")

    def test_first_reaction_is_reported(self):
        self.assertEqual(
            marketing_monitor.choose_alert(metrics(age=12, reactions=1)),
            "first_engagement",
        )

    def test_youtube_parser_accepts_zero_views(self):
        html = '<meta itemprop="interactionCount" content="0">'
        self.assertEqual(marketing_monitor.extract_youtube_views(html), 0)


if __name__ == "__main__":
    unittest.main()
