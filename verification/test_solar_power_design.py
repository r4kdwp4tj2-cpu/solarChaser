import csv
import tempfile
import unittest
from pathlib import Path

from calculations.solar_power_design import (
    mass_results,
    read_bom,
    read_cables,
    solar_results,
)


ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / "calculations" / "electrical-core-bom.csv"
CABLES = ROOT / "calculations" / "electrical-cable-schedule.csv"


class SolarPowerDesignTest(unittest.TestCase):
    def test_solar_string_has_cold_and_hot_voltage_margin(self) -> None:
        result = solar_results()
        self.assertEqual(result["array_power_w"], 800)
        self.assertAlmostEqual(result["cold_voc_v"], 164.25)
        self.assertGreater(result["cold_voc_margin_v"], 80)
        self.assertGreater(result["hot_start_margin_v"], 40)
        self.assertGreater(result["summer_yield_wh"], 2608)
        self.assertLess(result["winter_yield_wh"], 2387)

    def test_mass_budget_is_explicit(self) -> None:
        items = read_bom(BOM)
        result = mass_results(items)
        self.assertEqual(len(items), 18)
        self.assertAlmostEqual(result["roof_solar_mass_kg"], 61.24)
        self.assertAlmostEqual(result["electrical_core_mass_kg"], 216.82)
        self.assertGreater(result["roof_limit_margin_kg"], 100)
        self.assertGreater(result["estimated_mass_kg"], 60)

    def test_cable_schedule_meets_declared_drop_limits(self) -> None:
        cables = read_cables(CABLES)
        self.assertEqual(len(cables), 11)
        self.assertTrue(all(cable.voltage_drop_pct <= cable.max_drop_pct for cable in cables))

    def test_rejects_excessive_voltage_drop(self) -> None:
        with CABLES.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
        rows[0]["conductor_mm2"] = "0.1"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-cables.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "voltage drop"):
                read_cables(path)


if __name__ == "__main__":
    unittest.main()
