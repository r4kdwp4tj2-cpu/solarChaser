---
document_id: SC-095-001
title: Compliance Applicability Register
revision: 0.1
status: approved
owner: Systems Engineering and Compliance
approver: Spiros Netos
approval_date: 2026-07-12
baseline: null
---

# SC-095-001 Compliance Applicability Register

## 1. Purpose and limits

Control the legal, regulatory, standards, manufacturer, and approval evidence that may affect the SolarChaser conversion of a Renault Master E-Tech electric L2H2 in Switzerland.

This register is an engineering applicability assessment, not legal advice, type approval, an installation certificate, or authority acceptance. The exact vehicle configuration, registration category, canton, installation design, and date of submission can change the required evidence. Written confirmation from the responsible cantonal road-traffic authority and, where needed, an ASTRA-recognized test centre takes precedence over this preliminary classification.

## 2. Applicability classes

| Class | Meaning |
|---|---|
| Governing | Direct legal or approval framework expected to govern the vehicle or conversion |
| Design baseline | Standard selected as the engineering basis, subject to Swiss adoption and authority confirmation |
| Supporting evidence | Useful component or subsystem evidence that does not by itself approve the installed vehicle |
| Conditional | Applicability depends on classification, architecture, voltage, or authority interpretation |
| Not sufficient alone | Commonly cited evidence that addresses a narrower purpose than installed-system approval |

## 3. Controlled applicability matrix

| ID | Instrument or authority | Class | Preliminary applicability | Required project evidence | Closure authority |
|---|---|---|---|---|---|
| CA-001 | Swiss Road Traffic Act, VTS and vehicle-approval framework | Governing | Vehicle conversion, technical compliance, classification, mass, roadworthiness, and registration | Exact CoC/eCoC and vehicle data; conversion description; drawings; mass and axle budget; component evidence; inspection dossier | Cantonal road-traffic authority; ASTRA framework |
| CA-002 | Cantonal road-traffic authority and ASTRA-recognized test centre | Governing | Determines inspection route and acceptable evidence for the specific conversion | Written pre-application decision identifying vehicle category, report needs, inspection stages, and accepted experts | Responsible canton / recognized test centre |
| CA-003 | Renault CoC, body-builder instructions, warranty and exclusion zones | Governing design input | Defines the unmodified vehicle configuration and manufacturer constraints; not legislation but essential to safe and approvable conversion | Ordered-vehicle CoC/eCoC, body-builder manual, HV and structural exclusion zones, interface approvals, written clarifications | Renault / importer plus approval authority where relevant |
| CA-004 | IEC 60364-7-721:2017 | Design baseline | Applies to habitation-purpose electrical circuits and equipment in caravans and motor caravans; does not replace automotive requirements | Controlled 230 V design; equipment schedule; protection and isolation design; inspection and test results; qualified sign-off under the applicable Swiss implementation | Qualified electrical designer/inspector and authority as applicable |
| CA-005 | Swiss low-voltage installation rules and current NIN adoption | Conditional | Exact applicability to the vehicle, shore connection, inspection, and installer authorization requires confirmation; IEC scope alone is insufficient | Written applicability decision; current referenced clauses; installer/inspector credentials; initial verification record | ESTI/cantonal or qualified electrical authority as applicable |
| CA-006 | UN Regulation No. 10, current accepted amendment level | Supporting evidence / conditional | EMC evidence is relevant to vehicle electronic subassemblies and the completed conversion; component marks do not prove system integration | R10/E-mark or equivalent evidence per component; cable and bonding design; change-impact assessment; test plan where required | Cantonal authority / recognized test centre |
| CA-007 | ASTRA electrical-safety and EMC guidance | Governing interpretation input | Applies to new vehicles and conversions and describes acceptable Swiss evidence paths | Completed ASTRA evidence checklist; mapped declarations, approvals, and test reports | Cantonal authority / ASTRA-recognized test centre |
| CA-008 | UN Regulation No. 100 Revision 3 | Conditional / supporting evidence | Primarily addresses rechargeable energy storage associated with the electric powertrain. The OEM traction system remains vehicle-owned; applicability to the separate house battery shall not be assumed | Architecture boundary proving no traction-HV modification; authority decision on any analogous R100 evidence requested for the house battery or mounting | Cantonal authority / recognized test centre |
| CA-009 | IEC 62619:2022 | Supporting evidence | Industrial lithium-battery safety standard; its published scope excludes road vehicles when a vehicle-specific standard applies | Product certificate and report scope for the exact battery/BMS configuration; gap analysis against vehicle installation hazards | Project safety review plus approval authority |
| CA-010 | UN Manual of Tests and Criteria 38.3 | Not sufficient alone | Required transport-classification evidence for lithium battery types; does not approve installation, restraint, BMS, fire safety, or vehicle integration | Manufacturer's current UN 38.3 test summary for the exact supplied battery type and configuration | Supplier and dangerous-goods transport chain |
| CA-011 | Product EMC, safety, environmental and ingress ratings | Supporting evidence | Evidence must match the exact part number, firmware, BMS, accessories, mounting, and environmental use | Certificates, declarations, test reports, manuals, revision status, and deviations register | Project configuration control and approval authority |
| CA-012 | Installation workmanship and inspection evidence | Governing implementation evidence | Safe components can form an unsafe system; approval requires installed-configuration evidence | As-built drawings, labels, torque records, cable/protection schedule, isolation and functional tests, photographs, mass records, deviations, sign-offs | Qualified installers/inspectors and cantonal authority |

## 4. Approval gates

| Gate | Required before | Exit evidence |
|---|---|---|
| CG-01 Approval strategy | Layout freeze or irreversible body modification | Written canton/test-centre route; confirmed vehicle category; evidence list; inspection stages |
| CG-02 Manufacturer constraints | Drilling, cutting, structural loading, or vehicle-interface work | Exact Renault body-builder data and documented exclusions/permissions |
| CG-03 Habitation electrical design | Purchasing or installing shore, inverter, 230 V distribution, or fixed outlets | Qualified design review against the confirmed Swiss/IEC basis; protection, isolation, PE/bonding and test plan |
| CG-04 Battery eligibility | Battery product selection or purchase | Exact configuration evidence matrix including BMS, cold-charge behavior, transport summary, safety/EMC reports, mounting rules, parallel limits, service support, and unresolved gaps |
| CG-05 EMC strategy | Final harness and electronics layout | Component evidence register plus completed-system change-impact assessment and required test plan |
| CG-06 Mechanical and mass approval | Furniture and technical-bay layout freeze | Restraint analysis, attachment evidence, installed mass/axle budget, service-removal demonstration, and payload margin |
| CG-07 Installation release | Energization beyond controlled bench test | Approved schematics, inspection records, protection settings, labels, torque and continuity/isolation evidence, safe first-power procedure |
| CG-08 Registration submission | Road use as converted vehicle | Complete as-built dossier, declarations, test reports, weighbridge/axle results, photographs, deviations, and authority forms |

No gate may be closed solely by a marketing datasheet, CE mark, E-mark, UN 38.3 summary, or a certificate whose scope does not match the installed configuration.

## 5. Preliminary 230 V boundary

IEC 60364-7-721:2017 is the selected design baseline for circuits and equipment used for habitation. The published scope distinguishes habitation circuits from automotive circuits and requires a dedicated main isolating switch accessible in the motor caravan. The project shall obtain the full current normative text and confirmed Swiss implementation before design approval; this register does not reproduce unreviewed technical clauses.

The shore inlet, inverter, transfer/source logic, distribution, outlets, protective earth/bonding arrangement, protection against electric shock, cable routing, segregation, isolation, labelling, inspection, and testing shall be treated as one installed system. Supplier declarations for individual devices do not close the system safety case.

## 6. Battery and vehicle-HV boundary

- The Renault traction battery and high-voltage network remain OEM-controlled and outside the house-system design.
- No house-system connection to traction HV is permitted without a Renault/body-builder-approved interface and authority acceptance.
- The approved EM-004 LFP baseline is an auxiliary house-energy architecture, not an assertion that the house battery is an R100-approved propulsion REESS.
- IEC 62619 evidence and UN 38.3 transport evidence are required product-screening inputs where applicable, but neither proves safe under-bed installation.
- Mechanical restraint, external short-circuit protection, independent low-temperature charge inhibition, propagation/venting behavior, isolation, EMC, service access, and installation documentation remain separate acceptance items.

## 7. Immediate authority questions

Submit a concise pre-application package to the responsible cantonal road-traffic authority asking:

1. What final Swiss vehicle category and body designation will apply to this Renault-derived two-person motor caravan?
2. Which modifications require inspection before concealment or before final assembly?
3. Which evidence is required for the separate 48 V LFP house battery, its restraint, and its under-bed location?
4. Which EMC evidence is required for chargers, converters, inverter, BMS, monitoring, solar equipment, and the completed installation?
5. Which Swiss rules, installer qualifications, and inspection records apply to the fixed 230 V habitation installation and shore connection?
6. Does the authority require an ASTRA-recognized test-centre report for battery restraint, electrical safety, EMC, or other modifications?
7. Which mass, axle-load, seating, body, fire, emergency-access, and registration documents are required?

## 8. Sources

- ASTRA, [Vehicle regulations and inspections](https://www.astra.admin.ch/de/fahrzeugvorschriften-und-pruefungen), accessed 2026-07-12.
- ASTRA, [Concept for responsibilities and evidence in the vehicle inspection, type-approval and registration process](https://www.astra.admin.ch/dam/astra/de/dokumente/fahrzeuge/pruefung-zulassung/anforderungen-pr%C3%BCfdokumente-zulassungprozess.pdf.download.pdf/Konzept%20zu%20den%20Zust%C3%A4ndigkeiten%20im%20Pr%C3%BCf-%2C%20Typengenehmigungs-%20und%20Zulassungsprozess%20von%20Motorfahrzeugen%20und%20ihren%20Anh%C3%A4ngern.pdf), 2025.
- ASTRA, [Road-vehicle test-evidence form](https://www.astra.admin.ch/dam/astra/de/dokumente/fahrzeuge/pruefung-zulassung/formular-pruefnachweise-strassenfahrzeuge.pdf.download.pdf/Formular_Pruefnachweise_Strassenfahrzeuge.pdf), 2025.
- ASTRA, BAKOM, BFE and ESTI, [Electrical-safety and EMC evidence for road vehicles and components](https://www.astra.admin.ch/dam/de/sd-web/892ayLSrXfMD/erlaeuterungen-nev.pdf), 2021.
- IEC, [IEC 60364-7-721:2017 scope and publication data](https://webstore.iec.ch/en/publication/31016), accessed 2026-07-12.
- IEC, [IEC 62619:2022 scope and publication data](https://webstore.iec.ch/en/publication/64073), accessed 2026-07-12.
- UNECE, [UN Regulation No. 10 documents](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-0-20), accessed 2026-07-12.
- UNECE, [UN Regulation No. 100 Revision 3](https://unece.org/transport/documents/2022/03/standards/regulation-no-100-rev3), accessed 2026-07-12.
- UNECE, [UN Manual of Tests and Criteria Revision 8 and 2025 Amendment 1](https://unece.org/transport/standards/transport/dangerous-goods/un-manual-tests-and-criteria-rev8-2023), accessed 2026-07-12.

## 9. Open items

- Exact current consolidated VTS/TAFV/TGV clauses and cantonal implementation for the ordered vehicle.
- Final M/N category and Swiss `Wohnmotorwagen` classification after conversion.
- Current Swiss NIN adoption and inspection route for the habitation electrical installation.
- Renault body-builder restrictions and approved auxiliary-energy interfaces for the exact VIN/configuration.
- Recognized test-centre scope and required reports.
- Cross-border operating constraints after Swiss registration.

This register shall be updated whenever an authority response, newer instrument, product configuration, or design change alters applicability.
