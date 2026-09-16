# Wiki index

Entry point for the Workshop of Furniture Making knowledge base.
Every article must be listed here. Categories and articles are alphabetical.
Maintenance rules: `../CLAUDE.md`, section 2.

Line format: `- [Title](Category/file-name.md) - one-line description`

## Decisions
- [KB scope and structure adopted](Decisions/2026-09-14-kb-scope-and-structure-adopted.md) - why this is a separate, narrower KB (workshop machinery only) rather than a folder in the AMFA Furniture Ltd KB, and the document-numbering choice made for it
- [Scope extended to operational systems](Decisions/2026-09-15-operational-systems-scope-extension.md) - why maintenance, troubleshooting and SmartCabinet were added, and the Troubleshooting/Software categories + two new Smartsheet sheets created

## Finance
_(no articles yet)_

## Machinery
- [Altendorf F45 ElmoDrive — Sliding Table Saw](Machinery/altendorf-f45-panel-saw.md) - the workshop's machine `FA2303`; CNC panel saw with its own ElmoDrive control-unit and spare-parts manuals; safety certificates have expired, owning entity unconfirmed, see Open questions
- [Hebrock F4 — Edge Banding Machine](Machinery/hebrock-f4-next-edge-bander.md) - the workshop's machine `FA2301`; setup, safety and maintenance schedule from its 6-part manual; corner-rounding incident resolved
- [Vitap K2-2.0 — CNC Boring, Drilling and Routing Centre](Machinery/vitap-k2-panel-saw.md) - the workshop's machine `FA2304`; CNC boring/drilling/routing centre; no serial/DoC in the manual, §6.8 safety-check documentation requirement unresolved; bought with the Inventair MK2 MTFA (`FA2305`); open TpaCAD tool-ambiguity incident, see Incidents/Open questions

## People
_(no articles yet)_

## Processes
- [Process: Altendorf F45 monthly safety-device check](Processes/f45-monthly-safety-device-check.md) - the F45's mandatory, documented monthly safety check (E-stop, limit switches, hood) and where it's logged (Smartsheet "Safety Check Log")
- [Machinery maintenance system (routine maintenance)](Processes/machinery-maintenance-system.md) - how routine maintenance is scheduled/tracked; the Maintenance Schedule, Safety Check Log and Fault Log sheets and how their RYGB health works
- [Maintenance schedule — Altendorf F45 (FA2303)](Processes/maintenance-schedule-altendorf-f45.md) - the F45's manual Chapter-7 cleaning/lubrication schedule + annual PTC electrical check, mapped to Maintenance Schedule rows MT-020…MT-028
- [Maintenance schedule — Hebrock F4 (FA2301)](Processes/maintenance-schedule-hebrock-f4.md) - the F4's manual Chapter-7 cleaning/lubrication/wear schedule, mapped to Maintenance Schedule rows MT-001…MT-014
- [Maintenance schedule — Vitap K2-2.0 (FA2304)](Processes/maintenance-schedule-vitap-k2.md) - the Vitap's hours-based/event-triggered Chapter-7 schedule, mapped to Maintenance Schedule rows MT-030…MT-036
- [Process: SmartCabinet Wall Support Cam Table — column reference and worked example](Processes/smartcabinet-wall-support-cam-table-reference.md) - how to add hardware to SmartCabinet's Wall Support hardware library; full column reference from the software's own help text; two worked examples that exposed an unresolved X-axis sign-convention discrepancy (Task T017)
- [Process: TpaCAD tool-type auto-resolution ambiguity ("Tool for this working not found")](Processes/tpacad-tool-type-optimizer-ambiguity.md) - a real shop-floor fault on the Vitap K2-2.0 (`FA2304`): Blind bore drill operations fail to optimize when multiple spindles share the same diameter+type with no explicit Tool ID set; workaround found, permanent fix identified but not yet tried (Task T016)

## Software
- [SmartCabinet & the furniture production workflow](Software/smartcabinet-and-production-workflow.md) - draft: the order-to-delivery process from the BP-scheme map and how SmartCabinet (design + 3D visuals + CRM) drives the F45/Vitap/Hebrock machines; product specifics flagged [confirm]; seed for the design→production→Sales processes + tracker

## Suppliers
- [Altendorf GmbH (manufacturer)](Suppliers/altendorf-gmbh.md) - manufacturer of `FA2303` (and parent group of Hebrock, maker of `FA2301`); ordering/contact details for spare parts; the actual UK reseller who sold the machine is still unidentified

## Troubleshooting
- [Troubleshooting & fault-log system](Troubleshooting/troubleshooting-and-fault-log-system.md) - how faults are diagnosed, fixed and remembered; the Fault Log sheet and the per-machine references; safety-first rules
- [Troubleshooting — Altendorf F45 (FA2303)](Troubleshooting/troubleshooting-altendorf-f45.md) - the F45 mechanical fault table and the full ElmoDrive error-code list
- [Troubleshooting — Hebrock F4 (FA2301)](Troubleshooting/troubleshooting-hebrock-f4.md) - the F4 §8.2 fault table (corner-rounding row) and the resolved corner-rounding incident FL-001, with the practical lesson
- [Troubleshooting — Vitap K2-2.0 (FA2304)](Troubleshooting/troubleshooting-vitap-k2.md) - the Vitap §7.8 fault table + §7.6 time-out procedure; on-screen self-diagnosis
