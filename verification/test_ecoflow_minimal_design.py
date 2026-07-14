import csv
import tempfile
import unittest
from pathlib import Path

from calculations.ecoflow_minimal_design import (
    bom_results,
    charging_results,
    load_results,
    read_bom,
    read_loads,
    solar_results,
)


ROOT = Path(__file__).resolve().parents[1]
LOADS = ROOT / "calculations" / "ecoflow-minimal-load-budget.csv"
BOM = ROOT / "calculations" / "ecoflow-core-bom.csv"


class EcoFlowMinimalDesignTest(unittest.TestCase):
    def test_controlled_inputs_are_valid(self) -> None:
        loads = read_loads(LOADS)
        items = read_bom(BOM)
        self.assertEqual(len(loads), 8)
        self.assertEqual(len(items), 18)
        self.assertEqual(len({item.load_id for item in loads}), len(loads))
        self.assertEqual(len({item.component_id for item in items}), len(items))

    def test_load_and_battery_results(self) -> None:
        result = load_results(read_loads(LOADS))
        self.assertAlmostEqual(result["daily_load_wh"], 1730.0)
        self.assertAlmostEqual(result["daily_source_wh"], 1893.9367051168292)
        self.assertAlmostEqual(result["continuous_w"], 922.0)
        self.assertAlmostEqual(result["peak_w"], 972.0)
        self.assertAlmostEqual(result["autonomy_days"], 1.966082791244424)
        self.assertAlmostEqual(result["two_day_required_nominal_wh"], 5208.32593907128)

    def test_solar_and_charging_results(self) -> None:
        daily = load_results(read_loads(LOADS))["daily_source_wh"]
        solar = solar_results(daily)
        charging = charging_results(daily)
        self.assertAlmostEqual(solar["summer"]["yield_wh"], 2450.0)
        self.assertAlmostEqual(solar["shoulder"]["yield_wh"], 1470.0)
        self.assertAlmostEqual(solar["winter"]["yield_wh"], 735.0)
        self.assertGreater(solar["summer"]["coverage"], 1.0)
        self.assertLess(solar["shoulder"]["coverage"], 1.0)
        self.assertAlmostEqual(charging["ac_charge_w"], 1242.0)
        self.assertAlmostEqual(charging["travel_charge_w"], 234.6)

    def test_material_and_mass_results(self) -> None:
        result = bom_results(read_bom(BOM))
        self.assertAlmostEqual(result["total_material_chf"], 12089.0)
        self.assertAlmostEqual(result["total_mass_kg"], 154.35)
        self.assertAlmostEqual(result["roof_mass_kg"], 47.2)

    def test_rejects_invalid_conversion_efficiency(self) -> None:
        with LOADS.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
        rows[0]["conversion_efficiency"] = "0"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "conversion_efficiency"):
                read_loads(path)


if __name__ == "__main__":
    unittest.main()
