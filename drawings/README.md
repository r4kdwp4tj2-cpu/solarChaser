# Drawings

Use `src/` for editable diagram or CAD sources and `export/` for reviewable PDF/SVG/PNG outputs. Source and export share a stable drawing identifier. The editable source is authoritative unless a drawing explicitly states otherwise.

## Drawing index

| Drawing ID | Title | Authoritative source | Review export |
|---|---|---|---|
| EC-WD-001 | Electrical core wiring diagram | [Python source](src/EC-WD-001-electrical-core-wiring-diagram.py) | [PDF](export/EC-WD-001-electrical-core-wiring-diagram.pdf) and [PNG preview](export/EC-WD-001-electrical-core-wiring-diagram-preview.png) |

EC-WD-001 validates its component IDs and names against `calculations/electrical-core-bom.csv` when generated. Protection and cable annotations are reconciled with `calculations/electrical-cable-schedule.csv` and SC-410-001. It is a design-development connection drawing, not a construction release; the design holds shown on the drawing remain open.
