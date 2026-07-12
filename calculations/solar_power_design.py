#!/usr/bin/env python3
"""Validate and summarize the preliminary SolarChaser electrical/solar design."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


COPPER_RESISTIVITY_OHM_MM2_PER_M = 0.0175
ROOF_LOAD_LIMIT_KG = 200.0
ROOF_PLANNING_ALLOCATION_KG = 75.0
ARRAY_DERATE = 0.70
MIN_CELL_TEMP_C = -25.0
MAX_CELL_TEMP_C = 75.0
STC_TEMP_C = 25.0
BATTERY_MAX_CHARGE_V = 56.8
MPPT_START_HEADROOM_V = 5.0

PANEL_COUNT = 4
PANEL_POWER_W = 200.0
PANEL_VMP_V = 31.3
PANEL_IMP_A = 6.38
PANEL_VOC_V = 36.5
PANEL_ISC_A = 6.86
PANEL_VOC_TEMP_COEFF_PER_C = -0.0025
PANEL_VMP_DESIGN_TEMP_COEFF_PER_C = -0.0035
PANEL_LENGTH_MM = 1262.0
PANEL_WIDTH_MM = 764.0
PANEL_GAP_MM = 25.0
ARRAY_SERIES = 4
ARRAY_PARALLEL = 1
MPPT_MAX_VOC_V = 250.0

SEASON_PEAK_SUN_HOURS = {
    "summer": 5.0,
    "shoulder": 3.0,
    "winter": 1.5,
}


@dataclass(frozen=True)
class BomItem:
    component_id: str
    subsystem: str
    component: str
    candidate: str
    quantity: float
    unit_mass_kg: float
    mass_certainty: str
    location: str
    status: str
    basis: str

    @property
    def mass_kg(self) -> float:
        return self.quantity * self.unit_mass_kg


@dataclass(frozen=True)
class Cable:
    circuit_id: str
    source: str
    destination: str
    domain: str
    nominal_voltage_v: float
    design_current_a: float
    one_way_length_m: float
    conductor_mm2: float
    protection_a: float
    max_drop_pct: float
    status: str

    @property
    def voltage_drop_v(self) -> float:
        return (
            2
            * self.one_way_length_m
            * COPPER_RESISTIVITY_OHM_MM2_PER_M
            * self.design_current_a
            / self.conductor_mm2
        )

    @property
    def voltage_drop_pct(self) -> float:
        return 100 * self.voltage_drop_v / self.nominal_voltage_v


def read_bom(path: Path) -> list[BomItem]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    required = set(BomItem.__dataclass_fields__)
    if not rows or set(rows[0]) != required:
        raise ValueError("invalid or empty electrical BOM")
    items: list[BomItem] = []
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        component_id = row["component_id"].strip()
        if not component_id or component_id in seen:
            raise ValueError(f"line {line_number}: missing or duplicate component_id")
        seen.add(component_id)
        quantity = float(row["quantity"])
        unit_mass_kg = float(row["unit_mass_kg"])
        if quantity < 0 or unit_mass_kg < 0:
            raise ValueError(f"line {line_number}: quantity and mass must be non-negative")
        items.append(
            BomItem(
                component_id=component_id,
                subsystem=row["subsystem"].strip(),
                component=row["component"].strip(),
                candidate=row["candidate"].strip(),
                quantity=quantity,
                unit_mass_kg=unit_mass_kg,
                mass_certainty=row["mass_certainty"].strip(),
                location=row["location"].strip(),
                status=row["status"].strip(),
                basis=row["basis"].strip(),
            )
        )
    return items


def read_cables(path: Path) -> list[Cable]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    required = set(Cable.__dataclass_fields__)
    if not rows or set(rows[0]) != required:
        raise ValueError("invalid or empty cable schedule")
    cables: list[Cable] = []
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        circuit_id = row["circuit_id"].strip()
        if not circuit_id or circuit_id in seen:
            raise ValueError(f"line {line_number}: missing or duplicate circuit_id")
        seen.add(circuit_id)
        numbers = {
            field: float(row[field])
            for field in (
                "nominal_voltage_v",
                "design_current_a",
                "one_way_length_m",
                "conductor_mm2",
                "protection_a",
                "max_drop_pct",
            )
        }
        if any(value <= 0 for value in numbers.values()):
            raise ValueError(f"line {line_number}: cable values must be positive")
        cable = Cable(
            circuit_id=circuit_id,
            source=row["source"].strip(),
            destination=row["destination"].strip(),
            domain=row["domain"].strip(),
            status=row["status"].strip(),
            **numbers,
        )
        if cable.voltage_drop_pct > cable.max_drop_pct:
            raise ValueError(
                f"line {line_number}: {circuit_id} voltage drop "
                f"{cable.voltage_drop_pct:.2f}% exceeds {cable.max_drop_pct:.2f}%"
            )
        cables.append(cable)
    return cables


def solar_results() -> dict[str, float]:
    array_power_w = PANEL_COUNT * PANEL_POWER_W
    cold_factor = 1 + PANEL_VOC_TEMP_COEFF_PER_C * (MIN_CELL_TEMP_C - STC_TEMP_C)
    hot_factor = 1 + PANEL_VMP_DESIGN_TEMP_COEFF_PER_C * (MAX_CELL_TEMP_C - STC_TEMP_C)
    cold_voc_v = ARRAY_SERIES * PANEL_VOC_V * cold_factor
    hot_vmp_v = ARRAY_SERIES * PANEL_VMP_V * hot_factor
    required_start_v = BATTERY_MAX_CHARGE_V + MPPT_START_HEADROOM_V
    if ARRAY_SERIES * ARRAY_PARALLEL != PANEL_COUNT:
        raise ValueError("array series/parallel configuration does not use all panels")
    if cold_voc_v >= MPPT_MAX_VOC_V:
        raise ValueError("cold array Voc exceeds MPPT rating")
    if hot_vmp_v <= required_start_v:
        raise ValueError("hot array Vmp does not provide MPPT start headroom")
    return {
        "array_power_w": array_power_w,
        "stc_vmp_v": ARRAY_SERIES * PANEL_VMP_V,
        "stc_imp_a": ARRAY_PARALLEL * PANEL_IMP_A,
        "cold_voc_v": cold_voc_v,
        "cold_voc_margin_v": MPPT_MAX_VOC_V - cold_voc_v,
        "hot_vmp_v": hot_vmp_v,
        "hot_start_margin_v": hot_vmp_v - required_start_v,
        "footprint_length_mm": 2 * PANEL_LENGTH_MM + PANEL_GAP_MM,
        "footprint_width_mm": 2 * PANEL_WIDTH_MM + PANEL_GAP_MM,
        **{
            f"{season}_yield_wh": array_power_w * hours * ARRAY_DERATE
            for season, hours in SEASON_PEAK_SUN_HOURS.items()
        },
    }


def mass_results(items: list[BomItem]) -> dict[str, float]:
    installed = [item for item in items if item.quantity > 0]
    roof_mass = sum(item.mass_kg for item in installed if item.location == "roof")
    total_mass = sum(item.mass_kg for item in installed)
    return {
        "roof_solar_mass_kg": roof_mass,
        "roof_limit_margin_kg": ROOF_LOAD_LIMIT_KG - roof_mass,
        "roof_planning_reserve_kg": ROOF_PLANNING_ALLOCATION_KG - roof_mass,
        "electrical_core_mass_kg": total_mass,
        "manufacturer_mass_kg": sum(
            item.mass_kg for item in installed if item.mass_certainty == "manufacturer"
        ),
        "estimated_mass_kg": sum(
            item.mass_kg for item in installed if item.mass_certainty != "manufacturer"
        ),
    }


def markdown(items: list[BomItem], cables: list[Cable]) -> str:
    solar = solar_results()
    mass = mass_results(items)
    lines = [
        "# Preliminary electrical and solar design results",
        "",
        "> Generated by `python3 calculations/solar_power_design.py`. Do not edit manually.",
        "",
        "## Solar electrical result",
        "",
        "| Result | Value |",
        "|---|---:|",
        f"| Array arrangement | {ARRAY_SERIES}S{ARRAY_PARALLEL}P |",
        f"| Nominal array power | {solar['array_power_w']:.0f} Wp |",
        f"| STC maximum-power voltage/current | {solar['stc_vmp_v']:.1f} V / {solar['stc_imp_a']:.2f} A |",
        f"| Conservative cold open-circuit voltage at {MIN_CELL_TEMP_C:.0f} C | {solar['cold_voc_v']:.1f} V |",
        f"| Margin to {MPPT_MAX_VOC_V:.0f} V MPPT limit | {solar['cold_voc_margin_v']:.1f} V |",
        f"| Conservative hot maximum-power voltage at {MAX_CELL_TEMP_C:.0f} C | {solar['hot_vmp_v']:.1f} V |",
        f"| Hot voltage margin above battery-plus-start threshold | {solar['hot_start_margin_v']:.1f} V |",
        f"| Four-panel bounding footprint before perimeter clearance | {solar['footprint_length_mm']:.0f} x {solar['footprint_width_mm']:.0f} mm |",
        "",
        "The hot-Vmp coefficient is a conservative design assumption because the candidate panel datasheet publishes Pmax and Voc coefficients but not Vmp. Final string validation shall use the selected module's complete temperature data and the declared site minimum temperature.",
        "",
        "## Planning energy yield",
        "",
        f"A combined {ARRAY_DERATE:.0%} array derate covers temperature, orientation, wiring, conversion, mismatch, dirt, and operational effects for preliminary sizing.",
        "",
        "| Season | Peak-sun-hours assumption | Array yield |",
        "|---|---:|---:|",
    ]
    for season, hours in SEASON_PEAK_SUN_HOURS.items():
        lines.append(
            f"| {season.capitalize()} | {hours:.1f} h/day | {solar[f'{season}_yield_wh']:.0f} Wh/day |"
        )
    lines.extend(
        [
            "",
            "The result is a mission-planning envelope, not a location-specific guarantee. The 800 Wp array approximately covers the current 2.61 kWh summer design day under the summer assumption but does not make the vehicle solar-only in winter.",
            "",
            "## Mass result",
            "",
            "| Result | Value |",
            "|---|---:|",
            f"| Fixed roof-solar mass | {mass['roof_solar_mass_kg']:.1f} kg |",
            f"| Reserve within 75 kg roof planning allocation | {mass['roof_planning_reserve_kg']:.1f} kg |",
            f"| Margin to user-confirmed 200 kg roof-load input | {mass['roof_limit_margin_kg']:.1f} kg |",
            f"| Preliminary complete electrical-core mass | {mass['electrical_core_mass_kg']:.1f} kg |",
            f"| Mass supported by manufacturer values | {mass['manufacturer_mass_kg']:.1f} kg |",
            f"| Estimated ancillary mass | {mass['estimated_mass_kg']:.1f} kg |",
            "",
            "The 200 kg roof figure is a project input pending vehicle-specific Renault/MFK evidence. It does not by itself approve local load distribution, mounting, dynamic loads, aerodynamic uplift, roof penetrations, or the remaining vehicle payload.",
            "",
            "## Preliminary component mass register",
            "",
            "| ID | Component | Candidate | Qty | Mass | Certainty | Status |",
            "|---|---|---|---:|---:|---|---|",
        ]
    )
    for item in items:
        lines.append(
            f"| {item.component_id} | {item.component} | {item.candidate} | "
            f"{item.quantity:g} | {item.mass_kg:.2f} kg | {item.mass_certainty} | {item.status} |"
        )
    lines.extend(
        [
            "",
            "## Preliminary cable voltage-drop check",
            "",
            "| ID | Domain | Design current | Conductor | Protection | Drop | Limit | Status |",
            "|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for cable in cables:
        lines.append(
            f"| {cable.circuit_id} | {cable.domain} | {cable.design_current_a:.1f} A | "
            f"{cable.conductor_mm2:g} mm2 | {cable.protection_a:g} A | "
            f"{cable.voltage_drop_pct:.2f}% | {cable.max_drop_pct:.1f}% | {cable.status} |"
        )
    lines.extend(
        [
            "",
            "Cable sizes and protective ratings remain provisional until measured routes, ambient temperature, bundling, terminal limits, fault-current calculations, applicable standards, and manufacturer instructions are closed.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bom",
        type=Path,
        default=Path("calculations/electrical-core-bom.csv"),
    )
    parser.add_argument(
        "--cables",
        type=Path,
        default=Path("calculations/electrical-cable-schedule.csv"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("calculations/electrical-solar-design-results.md"),
    )
    args = parser.parse_args()
    items = read_bom(args.bom)
    cables = read_cables(args.cables)
    args.output.write_text(markdown(items, cables), encoding="utf-8")


if __name__ == "__main__":
    main()
