import csv
import tempfile
import unittest
from pathlib import Path

from calculations.electrical_load_budget import read_loads, totals


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "calculations" / "electrical-load-budget.csv"


class ElectricalLoadBudgetTest(unittest.TestCase):
    def test_controlled_input_is_valid(self) -> None:
        loads = read_loads(INPUT)
        self.assertEqual(len(loads), 12)
        self.assertEqual(len({load.load_id for load in loads}), len(loads))

    def test_planning_result_is_internally_consistent(self) -> None:
        result = totals(read_loads(INPUT))
        design_day = max(result["summer_daily_wh"], result["winter_daily_wh"])
        self.assertAlmostEqual(result["battery_planning_wh"], design_day * 2 * 1.10 / 0.80)
        self.assertGreater(result["peak_w"], result["worst_continuous_w"])
        self.assertAlmostEqual(result["summer_daily_wh"], 2608.4157905586476)
        self.assertAlmostEqual(result["winter_daily_wh"], 2386.1935683364255)
        self.assertAlmostEqual(result["worst_continuous_w"], 1557.4293960008245)
        self.assertAlmostEqual(result["peak_w"], 2255.611214182643)

    def test_rejects_peak_below_continuous(self) -> None:
        with INPUT.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
        rows[0]["peak_w"] = "1"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "peak_w"):
                read_loads(path)


if __name__ == "__main__":
    unittest.main()
