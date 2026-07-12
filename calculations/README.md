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
