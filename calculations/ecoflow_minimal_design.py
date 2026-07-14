#!/usr/bin/env python3
"""Validate and summarize the EcoFlow minimal electrical alternative."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


BATTERY_NOMINAL_WH = 5120.0
BATTERY_USABLE_FRACTION = 0.80
AUTONOMY_CONTINGENCY = 0.10
SOLAR_WP = 700.0
SOLAR_DERATE = 0.70
SEASONAL_PSH = {"summer": 5.0, "shoulder": 3.0, "winter": 1.5}
AC_VOLTAGE_V = 230.0
AC_CURRENT_LIMIT_A = 6.0
AC_CHARGE_EFFICIENCY = 0.90
TRAVEL_VOLTAGE_V = 13.8
TRAVEL_CURRENT_LIMIT_A = 20.0
TRAVEL_CHARGE_EFFICIENCY = 0.85
POWER_HUB_CONTINUOUS_W = 4000.0


@dataclass(frozen=True)
class Load:
    load_id: str
    name: str
    domain: str
    quantity: float
    rated_power_w: float
    hours_per_day: float
    daily_override_wh: float
    conversion_efficiency: float
    continuous_w: float
    peak_w: float
    certainty: str
    basis: str
    source_url: str

    @property
    def daily_load_wh(self) -> float:
        if self.daily_override_wh > 0:
            return self.daily_override_wh
        return self.quantity * self.rated_power_w * self.hours_per_day

    @property
    def daily_source_wh(self) -> float:
        return self.daily_load_wh / self.conversion_efficiency


@dataclass(frozen=True)
class BomItem:
    component_id: str
    subsystem: str
    component: str
    candidate: str
    quantity: float
    unit_mass_kg: float
    mass_certainty: str
    unit_price_chf: float
    price_certainty: str
    location: str
    status: str
    basis: str
    source_url: str

    @property
    def total_mass_kg(self) -> float:
        return self.quantity * self.unit_mass_kg

    @property
    def total_price_chf(self) -> float:
        return self.quantity * self.unit_price_chf


def _read_rows(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError(f"{path} is empty")
    actual = set(rows[0])
    if actual != required:
        raise ValueError(
            f"invalid columns in {path}; missing={sorted(required - actual)}, "
            f"extra={sorted(actual - required)}"
        )
    return rows


def read_loads(path: Path) -> list[Load]:
    rows = _read_rows(path, set(Load.__dataclass_fields__))
    loads: list[Load] = []
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        load_id = row["load_id"].strip()
        if not load_id or load_id in seen:
            raise ValueError(f"line {line_number}: missing or duplicate load_id {load_id!r}")
        seen.add(load_id)
        numbers = {
            field: float(row[field])
            for field in (
                "quantity",
                "rated_power_w",
                "hours_per_day",
                "daily_override_wh",
                "conversion_efficiency",
                "continuous_w",
                "peak_w",
            )
        }
        if any(value < 0 for value in numbers.values()):
            raise ValueError(f"line {line_number}: numeric values cannot be negative")
        if not 0 < numbers["conversion_efficiency"] <= 1:
            raise ValueError(f"line {line_number}: conversion_efficiency must be in (0, 1]")
        if numbers["peak_w"] < numbers["continuous_w"]:
            raise ValueError(f"line {line_number}: peak_w is below continuous_w")
        if numbers["daily_override_wh"] == 0 and numbers["hours_per_day"] == 0:
            raise ValueError(f"line {line_number}: no daily energy basis")
        loads.append(
            Load(
                load_id=load_id,
                name=row["name"].strip(),
                domain=row["domain"].strip(),
                certainty=row["certainty"].strip(),
                basis=row["basis"].strip(),
                source_url=row["source_url"].strip(),
                **numbers,
            )
        )
    return loads


def read_bom(path: Path) -> list[BomItem]:
    rows = _read_rows(path, set(BomItem.__dataclass_fields__))
    items: list[BomItem] = []
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        component_id = row["component_id"].strip()
        if not component_id or component_id in seen:
            raise ValueError(
                f"line {line_number}: missing or duplicate component_id {component_id!r}"
            )
        seen.add(component_id)
        numbers = {
            field: float(row[field])
            for field in ("quantity", "unit_mass_kg", "unit_price_chf")
        }
        if any(value < 0 for value in numbers.values()):
            raise ValueError(f"line {line_number}: BOM values cannot be negative")
        items.append(
            BomItem(
                component_id=component_id,
                subsystem=row["subsystem"].strip(),
                component=row["component"].strip(),
                candidate=row["candidate"].strip(),
                mass_certainty=row["mass_certainty"].strip(),
                price_certainty=row["price_certainty"].strip(),
                location=row["location"].strip(),
                status=row["status"].strip(),
                basis=row["basis"].strip(),
                source_url=row["source_url"].strip(),
                **numbers,
            )
        )
    return items


def load_results(loads: list[Load]) -> dict[str, float]:
    daily_load_wh = sum(load.daily_load_wh for load in loads)
    daily_source_wh = sum(load.daily_source_wh for load in loads)
    continuous_w = sum(load.continuous_w for load in loads)
    peak_w = sum(load.peak_w for load in loads)
    return {
        "daily_load_wh": daily_load_wh,
        "daily_source_wh": daily_source_wh,
        "continuous_w": continuous_w,
        "peak_w": peak_w,
        "inverter_margin_w": POWER_HUB_CONTINUOUS_W - peak_w,
        "autonomy_days": BATTERY_NOMINAL_WH
        * BATTERY_USABLE_FRACTION
        / (daily_source_wh * (1 + AUTONOMY_CONTINGENCY)),
        "two_day_required_nominal_wh": daily_source_wh
        * 2
        * (1 + AUTONOMY_CONTINGENCY)
        / BATTERY_USABLE_FRACTION,
    }


def solar_results(daily_source_wh: float) -> dict[str, dict[str, float]]:
    return {
        season: {
            "psh": psh,
            "yield_wh": SOLAR_WP * psh * SOLAR_DERATE,
            "coverage": SOLAR_WP * psh * SOLAR_DERATE / daily_source_wh,
            "balance_wh": SOLAR_WP * psh * SOLAR_DERATE - daily_source_wh,
        }
        for season, psh in SEASONAL_PSH.items()
    }


def charging_results(daily_source_wh: float) -> dict[str, float]:
    ac_charge_w = AC_VOLTAGE_V * AC_CURRENT_LIMIT_A * AC_CHARGE_EFFICIENCY
    travel_charge_w = (
        TRAVEL_VOLTAGE_V * TRAVEL_CURRENT_LIMIT_A * TRAVEL_CHARGE_EFFICIENCY
    )
    return {
        "ac_charge_w": ac_charge_w,
        "ac_daily_replacement_h": daily_source_wh / ac_charge_w,
        "ac_20_to_100_h": BATTERY_NOMINAL_WH
        * BATTERY_USABLE_FRACTION
        / ac_charge_w,
        "travel_charge_w": travel_charge_w,
        "travel_daily_replacement_h": daily_source_wh / travel_charge_w,
    }


def bom_results(items: list[BomItem]) -> dict[str, float]:
    return {
        "total_mass_kg": sum(item.total_mass_kg for item in items),
        "total_material_chf": sum(item.total_price_chf for item in items),
        "roof_mass_kg": sum(
            item.total_mass_kg for item in items if item.location == "roof"
        ),
        "estimated_mass_kg": sum(
            item.total_mass_kg for item in items if item.mass_certainty == "estimate"
        ),
    }


def markdown(loads: list[Load], items: list[BomItem]) -> str:
    load = load_results(loads)
    solar = solar_results(load["daily_source_wh"])
    charging = charging_results(load["daily_source_wh"])
    bom = bom_results(items)
    lines = [
        "# EcoFlow minimal electrical design results",
        "",
        "> Generated by `python3 calculations/ecoflow_minimal_design.py`. Do not edit manually.",
        "",
        "## Result summary",
        "",
        "| Result | Value |",
        "|---|---:|",
        f"| Load-side energy | {load['daily_load_wh']:.0f} Wh/day |",
        f"| Battery/source-side energy | {load['daily_source_wh']:.0f} Wh/day |",
        f"| Arithmetic continuous load | {load['continuous_w']:.0f} W |",
        f"| Arithmetic peak upper bound | {load['peak_w']:.0f} W |",
        f"| Margin to 4 kW Power Hub rating | {load['inverter_margin_w']:.0f} W |",
        f"| One 5.12 kWh battery planning autonomy | {load['autonomy_days']:.2f} days |",
        f"| Exact two-day nominal requirement | {load['two_day_required_nominal_wh']:.0f} Wh |",
        f"| Complete listed material mass | {bom['total_mass_kg']:.2f} kg |",
        f"| Roof material mass | {bom['roof_mass_kg']:.2f} kg |",
        f"| Complete listed material estimate | CHF {bom['total_material_chf']:,.0f} |",
        "",
        "The price is material only: it excludes labour, design, testing, certification, "
        "delivery, tax changes and procurement contingency. Current retail prices and "
        "planning allowances are mixed and must be refreshed before purchase.",
        "",
        "## Loads",
        "",
        "| ID | Load | Domain | Load Wh/day | Source Wh/day | Continuous W | Peak W | Certainty |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for item in loads:
        lines.append(
            f"| {item.load_id} | {item.name} | {item.domain} | "
            f"{item.daily_load_wh:.0f} | {item.daily_source_wh:.0f} | "
            f"{item.continuous_w:.0f} | {item.peak_w:.0f} | {item.certainty} |"
        )
    lines.extend(
        [
            "",
            "## Solar and charging",
            "",
            "Four EcoFlow 175 W panels provide 700 Wp. They are arranged as two "
            "independent 2S strings on two Power Hub MPPT inputs, so one shaded or failed "
            "string does not suppress the other string.",
            "",
            "| Season | PSH | Yield Wh/day | Coverage | Balance Wh/day |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for season, result in solar.items():
        lines.append(
            f"| {season.title()} | {result['psh']:.1f} | {result['yield_wh']:.0f} | "
            f"{result['coverage']:.0%} | {result['balance_wh']:+.0f} |"
        )
    lines.extend(
        [
            "",
            f"At the planning 6 A AC input limit, net battery charge is "
            f"{charging['ac_charge_w']:.0f} W, replacing one design day in "
            f"{charging['ac_daily_replacement_h']:.2f} h and charging from the planning "
            f"20% floor to 100% in {charging['ac_20_to_100_h']:.2f} h.",
            "",
            f"The conditional 12 V travel branch is limited to 20 A and about "
            f"{charging['travel_charge_w']:.0f} W net, requiring "
            f"{charging['travel_daily_replacement_h']:.2f} driving hours to replace one "
            "design day. It is not the backup source: Renault 230 V V2L is the backup.",
            "",
            "## Source priority and safety boundaries",
            "",
            "1. Solar through two independent MPPT inputs.",
            "2. Shore line through the EcoFlow AC input.",
            "3. Renault 230 V V2L through the same AC input as shore, selected by a "
            "two-pole mechanically interlocked changeover device; sources are never paralleled.",
            "4. Renault 12 V auxiliary supply only as a conditional travel top-up after "
            "written upfitter approval of the connection point, current limit and wake/sleep behavior.",
            "",
            "No connection to the Renault high-voltage traction system is permitted. The "
            "published Renault V2L capability does not prove that the selected vehicle has "
            "the option or that its exact socket, earthing and operating constraints suit the conversion.",
            "",
            "## Material register",
            "",
            "| ID | Component | Candidate | Qty | Mass kg | Material CHF | Status |",
            "|---|---|---|---:|---:|---:|---|",
        ]
    )
    for item in items:
        lines.append(
            f"| {item.component_id} | {item.component} | {item.candidate} | "
            f"{item.quantity:g} | {item.total_mass_kg:.2f} | "
            f"{item.total_price_chf:,.0f} | {item.status} |"
        )
    lines.extend(
        [
            "",
            "EcoFlow does not offer every requested habitation load or the mandatory "
            "vehicle/shore changeover and installation protection. The power system and "
            "refrigerator are EcoFlow; the boiler, lighting, floor heat, blanket, outlets, "
            "mounting, switching, protection and wiring necessarily remain third-party.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loads",
        type=Path,
        default=Path("calculations/ecoflow-minimal-load-budget.csv"),
    )
    parser.add_argument(
        "--bom", type=Path, default=Path("calculations/ecoflow-core-bom.csv")
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("calculations/ecoflow-minimal-design-results.md"),
    )
    args = parser.parse_args()
    loads = read_loads(args.loads)
    items = read_bom(args.bom)
    args.output.write_text(markdown(loads, items), encoding="utf-8")


if __name__ == "__main__":
    main()
