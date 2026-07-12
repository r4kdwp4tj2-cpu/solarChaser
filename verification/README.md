# Verification evidence

Store executable procedures, test fixtures, raw results, logs, photographs, certificates, and other objective evidence here. Evidence identifies the verified configuration, procedure revision, date, operator, environment, result, deviations, and linked requirement IDs.

## Automated engineering checks

- `test_electrical_load_budget.py` validates the controlled load model and source-side envelope.
- `test_battery_trade_study.py` validates chemistry ranking and the battery capacity envelope.
- `test_solar_power_design.py` validates PV cold/hot voltage margins, seasonal yield, roof/electrical mass totals, cable voltage-drop limits and invalid-input rejection.
