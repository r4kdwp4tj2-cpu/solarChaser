# Calculations

Store reproducible engineering calculations and their source data here. Each analysis must identify assumptions, units, method, tool/version, input sources, result, reviewer, and affected requirements or risks. Prefer open formats alongside tool-native files.

## Electrical load budget

- [`electrical-load-budget.csv`](electrical-load-budget.csv) is the controlled preliminary input.
- [`electrical_load_budget.py`](electrical_load_budget.py) validates and aggregates the input using Python 3.10 or later and only the standard library; the recorded package was verified with Python 3.12.8.
- [`electrical-load-budget-results.md`](electrical-load-budget-results.md) is generated review output.
- [`EM-003`](../docs/60-design-reviews/EM-003-preliminary-electrical-load-budget.md) records assumptions, interpretation limits, risks, actions, and review state.

Regenerate from the repository root with:

```sh
python3 calculations/electrical_load_budget.py
```

The package supports FR-014, FR-033, NFR-013, NFR-037, NFR-038, A-402-003, R-005, R-006, and R-007. Inputs are estimates pending mission profiles, product data, and measurements. The Design Authority is the reviewer.

## Battery chemistry and capacity trade

- [`battery-chemistry-trade.csv`](battery-chemistry-trade.csv) is the controlled option score input.
- [`battery_trade_study.py`](battery_trade_study.py) ranks the chemistries and derives capacity from the EM-003 load model using Python 3.10 or later and only the standard library.
- [`battery-trade-study-results.md`](battery-trade-study-results.md) is generated review output.
- [`EM-004`](../docs/60-design-reviews/EM-004-battery-capacity-and-chemistry-trade.md) records evidence, rationale, limitations, risks, actions, and review state.

Regenerate from the repository root with:

```sh
python3 calculations/battery_trade_study.py
```

The package supports FR-014, FR-033, NFR-027, NFR-029, NFR-037, NFR-039, A-402-004, R-001, R-006, R-009, and R-012. Scores are comparative engineering judgments, not product certifications.

## Electrical and solar preliminary design

- [`electrical-core-bom.csv`](electrical-core-bom.csv) is the controlled functional component and preliminary mass register.
- [`electrical-cable-schedule.csv`](electrical-cable-schedule.csv) is the controlled provisional conductor, protection and voltage-drop input.
- [`solar_power_design.py`](solar_power_design.py) validates the 4S PV voltage envelope, seasonal planning yield, roof/electrical mass and cable voltage drop using Python 3.10 or later and only the standard library.
- [`electrical-solar-design-results.md`](electrical-solar-design-results.md) is generated review output.
- [`SC-410-001`](../docs/20-architecture/SC-410-001-electrical-and-solar-preliminary-design.md) defines the resulting architecture, component candidates, safety boundaries and approval gates.
- [`EM-006`](../docs/60-design-reviews/EM-006-electrical-and-solar-preliminary-design.md) records findings, proposed decisions, risks and open actions.

Regenerate from the repository root with:

```sh
python3 calculations/solar_power_design.py
```

The package supports FR-011, FR-014, FR-033, NFR-021, NFR-027 through NFR-029, NFR-037 through NFR-040, proposed NFR-042, TBR-023 through TBR-032, and R-001, R-003, R-005, R-006, R-012, R-014 and R-015. Product candidates are packaging baselines, not procurement approvals.

## EcoFlow minimal electrical alternative

- [`ecoflow-minimal-load-budget.csv`](ecoflow-minimal-load-budget.csv) records the requested minimum-use profile and conversion efficiencies.
- [`ecoflow-core-bom.csv`](ecoflow-core-bom.csv) controls the EcoFlow candidate components, mandatory third-party integration material, mass and material-price allowances.
- [`ecoflow_minimal_design.py`](ecoflow_minimal_design.py) validates the inputs and calculates daily energy, battery autonomy, seasonal solar coverage, AC/12 V charging time, complete material mass and material-only cost.
- [`ecoflow-minimal-design-results.md`](ecoflow-minimal-design-results.md) is generated review output.
- [`EcoFlow-Minimal-Electrical-Design.xlsx`](EcoFlow-Minimal-Electrical-Design.xlsx) is the formula-driven review workbook with summary, load, solar/charging, BOM and assumption sheets.
- [`SC-411-001`](../docs/20-architecture/SC-411-001-ecoflow-minimal-electrical-design.md) defines the connection architecture, functional pin designations, source interlock and release gates.
- [`EM-007`](../docs/60-design-reviews/EM-007-ecoflow-minimal-electrical-alternative.md) records the review finding and open actions.

Regenerate from the repository root with:

```sh
python3 calculations/ecoflow_minimal_design.py
```

The CHF result is material only. It excludes labour, engineering, testing, certification, delivery, price escalation and contingency. Current retail prices and planning allowances are deliberately distinguished in the BOM.
