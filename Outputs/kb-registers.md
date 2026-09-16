# KB registers

Standing index for the Workshop of Furniture Making Knowledge Base. Read `../CLAUDE.md` §0 before
using this file.

**2026-09-16 — reconciled.** Two parallel session-lines (an operational-systems line and a CAD-day
line) had each kept their own copy of this file; they are merged here into one timeline. Sessions are
renumbered chronologically by the actual change-log file timestamps, so "Session 9/10" no longer means
two different things. See `change-log-2026-09-16-fork-reconciliation-and-darius.md`.

## Change-log entries

Newest first.

| Date | Entry | File |
|---|---|---|
| 2026-09-16 | Session 13 - Fork reconciled + Darius assigned as KB owner: the three split control files (`CLAUDE.md`→v8, `Wiki/index.md`, this file) merged from the two parallel session-lines (no content lost; six predecessors archived); the KB given a named owner, **Darius** (Workshop Operations Assistant, 5th AI employee), with git mirror `minda-ui/Darius` and a Workforce Hub roster row | `Outputs/change-log-2026-09-16-fork-reconciliation-and-darius.md` |
| 2026-09-16 | Session 12 - SmartCabinet Wall Support hardware added: two new hardware items (Häfele Concealed Cabinet Hanger, an adjustable wall-bracket system) added to the Cam Table with full column reference documented; exposed an unresolved X-sign discrepancy between the two (Task T017); TpaCAD tool-ambiguity fix (T016) refined but still not fully tested | `Outputs/change-log-2026-09-16-smartcabinet-wall-support-hardware.md` |
| 2026-09-15 | Session 11 - Duplicate Workshop Smartsheet sheets tidied: verified four empty setup duplicates (2× Document Register, 1× Machinery Register, 1× Tasks), owner deleted them in the UI; workspace now holds one of each; recorded in CLAUDE.md §1/§6a/§7 | `Outputs/change-log-2026-09-15-duplicate-sheets-tidied.md` |
| 2026-09-15 | Session 10 - TpaCAD tool-ambiguity incident: live shop-floor fault on `FA2304` ("Tool for this working not found" on Blind bore drill) root-caused and documented; TPA CAD software manual (2 parts) processed; workaround in place, permanent Tool-ID fix identified but not yet tried (Task T016) | `Outputs/change-log-2026-09-15-tpacad-tool-ambiguity-incident.md` |
| 2026-09-15 | Session 9 - Operational systems built (owner request): routine maintenance, troubleshooting and the SmartCabinet workflow. Two Smartsheet sheets (Maintenance Schedule 30 tasks, Fault Log), two new Wiki categories (Troubleshooting, Software), nine articles; the Vitap (`FA2304`) registered by a concurrent session was reconciled in and folded into the systems | `Outputs/change-log-2026-09-15-operational-systems-build.md` |
| 2026-09-15 | Session 8 - Vitap K2-2.0 registered: third machine (`FA2304`) processed from its 4-part manual and invoice 100154; revealed a second extractor, Inventair MK2 MTFA (`FA2305`); §6.8 safety-check documentation requirement flagged as unresolved rather than assumed equivalent to the F45's | `Outputs/change-log-2026-09-15-vitap-k2-registered.md` |
| 2026-09-15 | Session 7 - F45 spare parts manual (4 parts) processed: confirmed two-way tilt variant, added wear-part numbers, created Suppliers/altendorf-gmbh.md for manufacturer contact | `Outputs/change-log-2026-09-15-f45-spare-parts-manual-processed.md` |
| 2026-09-15 | Session 6 - Altendorf F45 registered: second machine (`FA2303`) processed from its 8-part manual (two documents: main saw + ElmoDrive control unit) and invoice 100153; Smartsheet "Safety Check Log" sheet created; expired safety certificates flagged | `Outputs/change-log-2026-09-15-altendorf-f45-registered.md` |
| 2026-09-15 | Session 5 - Corner-rounding router incident resolved: second stop-screw adjustment produced a clean radius; Task T006 closed, FA2301 back "In service" | `Outputs/change-log-2026-09-15-corner-rounding-router-resolved.md` |
| 2026-09-15 | Session 4 - Corner-rounding router (Eckenabrundfräse) fault reported and diagnosed against the manual's own fault table; adjustment attempted and overcorrected; incident logged as in-progress | `Outputs/change-log-2026-09-15-corner-rounding-router-incident.md` |
| 2026-09-15 | Session 3 - Invoice 100155 and the Hebrock F4's EC Declaration of Conformity processed: serial number and CE compliance confirmed, purchase details learned, asset code corrected FA2601 -> FA2301, second asset FA2302 (Inventair MK1 MTFA) registered, owning-entity question raised | `Outputs/change-log-2026-09-15-invoice-and-ce-declaration-processed.md` |
| 2026-09-14 | Session 2 - Hebrock F4 next manual processed | `Outputs/change-log-2026-09-14-hebrock-f4-manual-processed.md` |
| 2026-09-14 | Session 1 - Workshop of Furniture Making KB and Smartsheet workspace created | `Outputs/change-log-2026-09-14-initial-kb-setup.md` |

## Processed items

Status legend: `pending` = registered, not started · `partial` = started, work remains ·
`done` = fully reflected in the wiki · `skipped` = deliberately not processed.

| Raw path | Processed (date) | Status | Wiki articles created / updated | Notes |
|---|---|---|---|---|
| `Raw/README.md` | 2026-09-14 | skipped | none | Folder guide, not source material. |
| `Raw/part 1.pdf`-`part 6.pdf` | 2026-09-14/15 | done | Machinery/hebrock-f4-next-edge-bander; Processes/maintenance-schedule-hebrock-f4; Troubleshooting/troubleshooting-hebrock-f4 | Hebrock F4 manual, 6 parts. Maintenance + fault content also lifted into the operational systems (Session 9). |
| `Raw/2026-09-15_hebrock_ce-declaration-of-conformity-f4-f3809.jpg` | 2026-09-15 | done | Machinery/hebrock-f4-next-edge-bander | Serial F3809, CE compliance. |
| `Raw/Invoice 100155 - 09.11.23 - OCN2311184 - Balance.pdf` | 2026-09-15 | done | Machinery/hebrock-f4-next-edge-bander | Purchase details; revealed FA2302 and owning-entity question. |
| `Raw/2026-09-15_fault-photo_edge-bander-*.jpg` (4 photos) | 2026-09-15 | done | Machinery/hebrock-f4-next-edge-bander; Troubleshooting/troubleshooting-hebrock-f4 | Corner-rounding incident (FL-001), reported through resolved. |
| `Raw/F45 part 1.pdf`-`part 8.pdf` | 2026-09-15 | done | Machinery/altendorf-f45-panel-saw; Processes/maintenance-schedule-altendorf-f45; Troubleshooting/troubleshooting-altendorf-f45 | Main F45 manual (parts 1-6) + ElmoDrive control-unit manual (parts 7-8). Maintenance + both fault tables also lifted into the operational systems (Session 9). |
| `Raw/Invoice 100153 - 09.11.23 - OCN231181 - Balance (1).pdf` | 2026-09-15 | done | Machinery/altendorf-f45-panel-saw | Purchase date/price (full price confirmed unambiguously). |
| `Raw/F45 Spare parts manual part 1.pdf`-`part 4.pdf` | 2026-09-15 | done | Machinery/altendorf-f45-panel-saw, Suppliers/altendorf-gmbh | Confirmed two-way tilt variant; wear-part numbers; manufacturer ordering contact. Did not confirm serial number, PTC resistor, or F1-F16 fuses. |
| `Raw/Vitap K2 2.0 manual part 1.pdf`-`part 4.pdf` | 2026-09-15 | done | Machinery/vitap-k2-panel-saw; Processes/maintenance-schedule-vitap-k2; Troubleshooting/troubleshooting-vitap-k2 | Two duplex pairs (pages 1-59, 60-126). No serial/manufacture year in the manual; §6.8 safety-check documentation requirement unresolved. Maintenance + §7.8 fault table also lifted into the operational systems (Session 9). |
| `Raw/Invoice 100154 - 09.11.23 - OCN231185 - Balance.pdf` | 2026-09-15 | partial | Machinery/vitap-k2-panel-saw | Purchase date/price for FA2304 (full price confirmed); also revealed FA2305 (Inventair MK2 MTFA), registered in Smartsheet only pending its own manual. |
| `Raw/TPA CAD part 1.pdf`-`part 2.pdf` | 2026-09-15/16 | partial | Machinery/vitap-k2-panel-saw, Processes/tpacad-tool-type-optimizer-ambiguity | Confirmed abridged extract of a larger manual; documented the Blind-bore-drill tool-ambiguity fault; confirmed CN Tools/Cam Table isn't covered in this manual at all. Complete `TpaCad.pdf`/`Workings.pdf` not yet obtained (Task T015); fix refined but still not fully tested (Task T016). |
| (Group KB Raw) `2026-01-27_BP scheme.pdf` | 2026-09-15 | done | Software/smartcabinet-and-production-workflow | The furniture-making business-process map (owner-provided, lives in the Fishbone Group KB Raw, not this KB's Raw). Cited as an external Drive source; anchors the SmartCabinet workflow. |
| *(no Raw item — live SmartCabinet configuration work)* | 2026-09-16 | done | Processes/smartcabinet-wall-support-cam-table-reference | Two hardware items added to SmartCabinet's own Wall Support Cam Table; not a Raw/ document, but a real, non-trivial process worth capturing regardless. |

## Wiki structure changes

| Date | Change | Reason |
|---|---|---|
| 2026-09-14 | Created `Wiki/` with `index.md`, `_templates/article.md`, and topic folders; wrote the first Decisions article | Initial KB setup |
| 2026-09-14/15 | `Machinery/hebrock-f4-next-edge-bander.md` created, then updated through invoice/CE processing and a full incident lifecycle | First machine, first real fault |
| 2026-09-15 | `Machinery/altendorf-f45-panel-saw.md` created; first `Processes/` article (`f45-monthly-safety-device-check.md`) created alongside it | Second machine registered; recurring compliance check needed its own process doc |
| 2026-09-15 | `altendorf-f45-panel-saw.md` updated with spare-parts data; first `Suppliers/` article (`altendorf-gmbh.md`) created | Spare parts manual gave real manufacturer ordering contact info |
| 2026-09-15 | `Machinery/vitap-k2-panel-saw.md` created; `index.md` updated | Third machine registered (concurrent Session 8) |
| 2026-09-15 | **Operational-systems build (Session 9):** two new categories `Troubleshooting/` and `Software/`; created `Processes/machinery-maintenance-system.md`, `Processes/maintenance-schedule-{hebrock-f4,altendorf-f45,vitap-k2}.md`, `Troubleshooting/troubleshooting-and-fault-log-system.md`, `Troubleshooting/troubleshooting-{hebrock-f4,altendorf-f45,vitap-k2}.md`, `Software/smartcabinet-and-production-workflow.md`, and a second Decisions article; `index.md` and `CLAUDE.md` (v5) updated | Owner request: build maintenance/troubleshooting/SmartCabinet systems |
| 2026-09-15 | `Processes/tpacad-tool-type-optimizer-ambiguity.md` created (Session 10); `vitap-k2-panel-saw.md` gained an Incidents section | Live shop-floor fault on FA2304 root-caused during real programming work, then its software manual arrived for processing in the same session |
| 2026-09-15 | Duplicate Smartsheet sheets tidied (Session 11); `CLAUDE.md` §1/§6a/§7 updated (no Wiki article change) | Owner deleted the four empty setup-duplicate sheets in the UI |
| 2026-09-16 | `Processes/smartcabinet-wall-support-cam-table-reference.md` created (Session 12); `index.md` updated | First Processes article covering the CAD/design software (SmartCabinet) rather than a machine or its control software; captures a column reference plus an unresolved sign-convention discrepancy |
| 2026-09-16 | **Fork reconciliation (Session 13):** the three split control files (`CLAUDE.md`→v8, `Wiki/index.md`, `Outputs/kb-registers.md`) merged into one clean set from the two parallel session-lines; six predecessors archived; Darius assigned as KB owner (§0a of CLAUDE.md v8) | Two concurrent sessions had forked the control layer; a named owner (one seat) reconciles it and prevents recurrence |

## Outputs produced

| Output path | Date | Built from (wiki articles) | Requested by |
|---|---|---|---|
| KB folder tree, `CLAUDE.md`, `README.md`, Smartsheet "Workshop" workspace | 2026-09-14 | Modelled on Fishbone Commercial Properties Ltd conventions | Owner |
| `FA2301` Machinery Register row + Document Register + Tasks (T001-T003) | 2026-09-14 | hebrock-f4-next-edge-bander.md | Owner |
| `FA2301` corrected (was `FA2601`); `FA2302` added; Document Register + Tasks T004/T005 | 2026-09-15 | hebrock-f4-next-edge-bander.md | Owner |
| `FA2301` incident lifecycle: Status Under repair -> In service; Task T006 raised then closed | 2026-09-15 | hebrock-f4-next-edge-bander.md, Incidents | Owner |
| `FA2303` Machinery Register row; 3 Document Register rows; Tasks T007-T011; T004 updated; new "Safety Check Log" sheet | 2026-09-15 | altendorf-f45-panel-saw.md, f45-monthly-safety-device-check.md | Owner |
| 4th Document Register row (spare parts manual) | 2026-09-15 | altendorf-f45-panel-saw.md, altendorf-gmbh.md | Owner |
| `FA2304`/`FA2305` Machinery Register rows; 2 Document Register rows; Tasks T012-T014; T005 closed Done; T010 updated | 2026-09-15 | vitap-k2-panel-saw.md | Owner |
| **Smartsheet "Maintenance Schedule"** (`6753985971226500`, 30 tasks MT-001…036, RYGB by due date) and **"Fault Log"** (`414932606781316`, FL-001 seeded, RYGB by status) | 2026-09-15 | machinery-maintenance-system.md, the three maintenance-schedule articles, troubleshooting-and-fault-log-system.md | Owner |
| Document Register row for TPA CAD manual; Tasks T015-T016; Vitap article Incidents section | 2026-09-15 | vitap-k2-panel-saw.md, tpacad-tool-type-optimizer-ambiguity.md | Owner (live troubleshooting) |
| Duplicate setup Smartsheet sheets deleted (4 empties); workspace reduced to one of each | 2026-09-15 | — | Owner (deleted in UI); verified + recorded by this KB |
| Task T016 updated with refined fix understanding; Task T017 added | 2026-09-16 | tpacad-tool-type-optimizer-ambiguity.md, smartcabinet-wall-support-cam-table-reference.md | Owner (live troubleshooting) |
| Control layer reconciled to v8 + Darius assigned as KB owner; git mirror `minda-ui/Darius` seeded; Workforce Hub roster row; group master-index entry | 2026-09-16 | CLAUDE.md v8 | Owner (Minda) / Victoria |
