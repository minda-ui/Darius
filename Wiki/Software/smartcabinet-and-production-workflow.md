---
title: "Design → Production → Sales workflow, and the Job Tracker"
category: Software
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-17
sources:
 - External (Drive): 2026-01-27_BP scheme.pdf - https://drive.google.com/file/d/1klUggv_PCNZgbKaI1io4-UC_-XwTPrsl/view - the furniture-making business-process map - accessed 2026-09-15
 - Smartsheet (Workshop workspace): Job Tracker sheet `6914515205752708` - the workshop's production system of record - created 2026-09-17
 - Owner (Minda), 2026-09-17: system scope (SmartCabinet + QuickBooks live, Asana out, EZ Office under review), the CRM is Sales-side, the workshop does not deal with customers, and "contract signed in the CRM releases the job to the workshop".
related:
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Processes/machinery-maintenance-system.md
 - ../Troubleshooting/troubleshooting-and-fault-log-system.md
 - ../Decisions/2026-09-15-operational-systems-scope-extension.md
 - ../Processes/barcode-and-scan-event-system.md
 - ../Software/kitchen-unit-library.md
---

# Design → Production → Sales workflow, and the Job Tracker

> **Owner-confirmed 2026-09-17.** This is the real process, out of draft. Two things are still `[confirm]`
> and marked below: SmartCabinet's exact product identity/version, and the file format it exports to
> each machine. Everything else — the systems in play, the workshop's scope, and the entry/exit
> hand-offs — is confirmed by Minda.

## The workshop's scope — a production window, no customers

The furniture order runs a full lifecycle (enquiry → quotation → contract → **production** → delivery →
close), but **the workshop owns only the production window in the middle.** The **CRM is Sales's**, and
**the workshop does not deal with customers at all** (owner, 2026-09-17). So:

- **Sales (CRM)** owns the whole customer-facing spine: enquiry, concept, quotations, client approvals,
  the contract, delivery, installation and closing — and **all** client contact.
- **Accounting (QuickBooks)** owns the four payment milestones: Deposit 1 (fixed), Deposit 2 (%),
  pre-delivery payment, final payment.
- **The workshop (this KB, Darius)** owns what happens **between contract and hand-back**: engineering/
  design output, materials, cutting, edge-banding, assembly, QC and packing — ending at
  **Ready for delivery**.

**Entry:** a job crosses into the workshop when the **contract is signed in the CRM** — that releases it
to production. **Exit:** when the job is **Ready for delivery**, it hands back to Sales, who arrange
delivery/installation with the customer. The workshop never contacts the client and holds no client
data — only a **Sales job reference** to line the two sides up.

## Systems in play (confirmed 2026-09-17)

| System | Used for | Whose |
|---|---|---|
| **SmartCabinet** | cabinet design, 3D visuals, cut lists / CNC output — **and** the CRM | Design/CNC output = workshop; **CRM = Sales** |
| **QuickBooks** | the four payment milestones | Accounting |
| **Job Tracker** (Smartsheet, this KB) | the workshop's production system of record | **Workshop (Darius)** |
| ~~Asana~~ | (was: management/tasks) — **removed**; its role is now the Job Tracker | — |
| **EZ Office** (stock) | materials ordering/issuance | **Under review** (may be kept or folded into the tracker) — the tracker carries a *Materials* stage either way |

## The Job Tracker — the workshop's production system of record

**Smartsheet "Job Tracker"**, Workshop workspace, sheet `6914515205752708`. One row per released job.
It replaces the old Asana lane and is the single place the workshop's production status lives; **Sales
read it to see where a job is, and Darius keeps it current** — that is the workshop's whole customer-
facing duty (update the system; Sales tell the client).

**Columns**
- **Job ID** — the workshop's own number, minted here (see numbering below).
- **Sales job ref** — reference to the job in the CRM; **no client name or personal data** is copied in.
- **Job description** — e.g. "Kitchen, 12 units".
- **Stage** — the production spine (picklist): Released to workshop → Engineering / Design → Materials
  ordered/issued → Panel cutting & Edge banding → Assembly → Quality check → Disassembly & Packing →
  **Ready for delivery** → Handed to Sales.
- **Health** — RYGB, a self-updating **column formula** (maintain via the connector, not by hand): green
  when *Handed to Sales*; red if *Blocked* or the target date is past; yellow if due within 14 days;
  green if further out; blue if no target date set. Same convention as the Maintenance & Fault sheets.
- **Released date** (contract-signed / released), **Target / promised date**, **Ready date**.
- **Design ref (SmartCabinet)** — the SmartCabinet design/quote reference.
- **QC status** (Pass / Rework), **Blocked** (checkbox), **Notes**, **Job folder link**.

**Job numbering.** No scheme existed (owner, 2026-09-17), so the workshop mints one: **`WJ-YY-NNN`** —
`WJ` + 2-digit year the job is released + a 3-digit sequence (e.g. the first job released in 2026 is
**`WJ-26-001`**). Sequence is per year, assigned in order of release.

**Worked example (documentation only — not a live row).** A kitchen released on 2026-09-17 would be
entered as `WJ-26-001`, Sales job ref (its CRM number), description "Kitchen, 12 units", Stage
*Engineering / Design*, Released date 2026-09-17, a target date for the promised-ready day; Health then
shows yellow/green off that date. It advances stage by stage to *Ready for delivery*, then *Handed to
Sales* — at which point the workshop's part is done.

## Design → machine hand-off (the production heart)

SmartCabinet's engineering output drives the three CNC machines. **Confirm the exact file format each
accepts `[confirm]`:**

- **Panel cutting** → **Altendorf F45** (`FA2303`), CNC sliding-table saw (ElmoDrive) — cutting list /
  optimised panels. See `../Machinery/altendorf-f45-panel-saw.md`.
- **Boring / drilling / grooving** → **Vitap K2-2.0** (`FA2304`), CNC boring/routing centre (TPA
  Albatros, has its own optimiser) — tool and drill/insertion programmes. See
  `../Machinery/vitap-k2-panel-saw.md` and the TpaCAD tool-ambiguity note in `../Processes/`.
- **Edge banding** → **Hebrock F4** (`FA2301`) — edge material and corner-rounding recipe per panel.
  See `../Machinery/hebrock-f4-next-edge-bander.md`.
- **Assembly → Quality check → Packing** — off-machine. **QC is where machine-caused defects** (e.g. the
  edge-band corner fault) are caught and, if needed, raised on the **Fault Log** — see
  `../Troubleshooting/troubleshooting-and-fault-log-system.md`.

## SOPs (to detail once the `[confirm]` file formats are known)

1. **Release intake** — a job enters the Job Tracker when Sales mark the contract signed; Darius creates
   the `WJ-` row from the Sales job ref (no client data copied).
2. **Design → cut-list export to the F45** — file format, optimisation settings, naming `[confirm]`.
3. **Boring/routing programme export to the Vitap K2** — tool library, drill/insertion maps `[confirm]`.
4. **Edge-banding recipe to the Hebrock F4** — material, trim, corner-rounding parameters.
5. **QC & Fault-Log link** — what QC checks, and when a defect becomes a Fault-Log entry.
6. **Ready-for-delivery hand-back** — packing done, *Ready date* set, Stage → *Ready for delivery*, which
   is the signal to Sales; then *Handed to Sales*.

## Open questions (for Minda)

- **`[confirm]` SmartCabinet product identity/version** and whether "SmartCabinet" is the vendor name.
- **`[confirm]`** which machines it exports to directly and in what file format each (the Vitap's
  Albatros and the F45's ElmoDrive accept different things).
- **EZ Office** — keep it for stock, or fold materials into the Job Tracker's *Materials* stage? (Owner
  decision pending; the tracker works either way.)
- (Resolved 2026-09-17: the CRM is Sales-side and the workshop does not handle customers; the entry
  trigger is contract-signed-in-CRM; the exit is Ready-for-delivery.)

## Sources

- External (Drive): the furniture business-process map, `2026-01-27_BP scheme.pdf`,
  https://drive.google.com/file/d/1klUggv_PCNZgbKaI1io4-UC_-XwTPrsl/view — accessed 2026-09-15.
- Smartsheet (Workshop workspace): **Job Tracker** sheet `6914515205752708` — created 2026-09-17.
- Owner (Minda), 2026-09-17: scope, systems, boundary and hand-offs.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created as a draft anchored on the BP-scheme map and the machines; SmartCabinet specifics flagged [confirm] | Session — workshop operational systems build |
| 2026-09-17 | **Out of draft → active.** Confirmed systems (SmartCabinet + QuickBooks live, Asana removed, EZ Office under review); recorded that the CRM is Sales-side and the workshop deals with no customers; entry = contract-signed-in-CRM, exit = Ready-for-delivery; built the **Job Tracker** sheet (`6914515205752708`) as the workshop's production system of record and documented it; minted the `WJ-YY-NNN` job-numbering scheme. Machine file formats remain [confirm]. | Session — Darius's first job (design→production→Sales) |
