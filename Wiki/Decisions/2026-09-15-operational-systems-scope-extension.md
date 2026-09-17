---
title: "Decision: scope extended to operational systems (maintenance, troubleshooting, SmartCabinet)"
category: Decisions
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
related:
 - 2026-09-14-kb-scope-and-structure-adopted.md
 - ../Processes/machinery-maintenance-system.md
 - ../Troubleshooting/troubleshooting-and-fault-log-system.md
 - ../Software/smartcabinet-and-production-workflow.md
---

# Decision: scope extended to operational systems

**Owner request (Minda, 2026-09-15):** build a system for the workshop covering **(1) routine
maintenance of machinery, (2) troubleshooting, and (3) working with the design software SmartCabinet.**

## What changed

The KB was set up (2026-09-14) as an **inventory + compliance** record of the workshop machinery. This
decision extends it to **operational systems** for running the machines day to day, still within the
same "machinery and equipment in the AMFA Furniture workshop" scope. SmartCabinet (design software) is
admitted because it is the tool that drives those machines — the design→cut-list→machine hand-off — and
because the owner asked for it here.

Choices confirmed with the owner via AskUserQuestion (2026-09-15):
- SmartCabinet = cabinet-design/CNC software **+ 3D visuals + CRM**.
- Tracking = **Smartsheet-backed + Wiki** (matches the KB's existing "Smartsheet is the live record"
 rule).
- Build = **framework + real content mined from the machine manuals** now; SmartCabinet left a draft
 skeleton until its product specifics are confirmed.

## Structure added

- Two new Wiki categories: **Troubleshooting** and **Software** (alongside Machinery, Suppliers, People,
 Finance, Processes, Decisions). Added with real content, not as empty placeholders.
- Two new Smartsheet sheets in the **Workshop** workspace: **Maintenance Schedule** (`6753985971226500`)
 and **Fault Log** (`414932606781316`), both with the group RYGB `Health` column formula. They sit
 alongside the existing **Safety Check Log** (which stays separate because a legal safety check is not
 general upkeep).
- Seven Wiki articles (maintenance system + 2 per-machine schedules; troubleshooting system + 2
 per-machine references; SmartCabinet workflow draft).

## Why not put this in the AMFA Furniture Ltd KB

Same reasoning as the founding decision (`2026-09-14-kb-scope-and-structure-adopted.md`): this is the
machinery/operations layer, distinct from AMFA's company-level KB. Facts that are also company-level
(who owns the assets, purchase finance) stay cited across, not duplicated.

## Consequence to watch

Two more machines surfaced during this build — a **Vitap K2 2.0** CNC boring machine and an **Inventair
MK2 MTFA** extractor (purchase invoice 100154, `Raw/`) — **not yet registered as assets**. They must be
processed in (asset code, Machinery Register row, article) before their maintenance/troubleshooting can
join these systems. Recorded in CLAUDE.md §7 and the change log.
