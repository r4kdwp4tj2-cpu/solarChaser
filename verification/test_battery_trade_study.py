import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "calculations"))

from battery_trade_study import capacity_results, read_options, weighted_score  # noqa: E402


class BatteryTradeStudyTest(unittest.TestCase):
    def test_controlled_options_are_valid_and_ranked(self) -> None:
        options = read_options(ROOT / "calculations" / "battery-chemistry-trade.csv")
        scores = {option.option: weighted_score(option) for option in options}
        self.assertEqual(set(scores), {"LFP", "LTO", "NMC"})
        self.assertAlmostEqual(scores["LFP"], 4.20)
        self.assertAlmostEqual(scores["LTO"], 3.75)
        self.assertAlmostEqual(scores["NMC"], 3.15)
        self.assertGreater(scores["LFP"], scores["LTO"])

    def test_capacity_is_derived_from_em003(self) -> None:
        result = capacity_results(ROOT / "calculations" / "electrical-load-budget.csv")
        self.assertAlmostEqual(result["minimum_nominal_wh"], 7173.143424036281)
        self.assertAlmostEqual(result["minimum_nominal_ah"], 140.1004575007086)
        self.assertEqual(result["reference_nominal_wh"], 10240)
        self.assertEqual(result["reference_mass_kg"], 74)
        self.assertGreater(result["reference_operational_days"], 2.0)


if __name__ == "__main__":
    unittest.main()
