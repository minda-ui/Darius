---
title: "SmartCabinet & the furniture production workflow"
category: Software
status: draft
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - External (Drive): 2026-01-27_BP scheme.pdf - https://drive.google.com/file/d/1klUggv_PCNZgbKaI1io4-UC_-XwTPrsl/view - the furniture-making business-process map - accessed 2026-09-15
related:
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Processes/machinery-maintenance-system.md
---

# SmartCabinet & the furniture production workflow

> **Status: draft skeleton.** The workflow below is anchored on the workshop's own business-process
> map and the registered machines, so it is real. The **SmartCabinet-specific** detail (exact product
> name/version, licensing, where data lives, the exact export/file formats to each machine) is
> **to be confirmed with Minda** before this leaves draft — those spots are marked **[confirm]**.
> SmartCabinet is understood to do three things: **(1) cabinet design + cut lists / CNC output,
> (2) 3D visuals for the client, (3) CRM** (owner, 2026-09-15).

## The workshop's order-to-delivery process (from the BP-scheme map)

The business-process map (`2026-01-27_BP scheme.pdf`) sets out the furniture order lifecycle. Stages:

1. **Enquiry** — client fills an enquiry application → **Qualified Enquiry**.
2. **Measurement** — site measurement.
3. **Concept / Preliminary Estimate**.
4. **Preliminary Quotation** → **Final Quotation** → **Approved by client** → **Contract signed**.
5. **Ordering / Engineering** → **Issuance of materials**.
6. **Production**: **Panel cutting & Edge banding → Assembly → Quality check → Disassembly & Packing**.
7. **Delivery → Installation → Installed + Review → Closed**.

Payment milestones run alongside: **Deposit 1 (fixed sum)**, **Deposit 2 (%)**, **pre-delivery
payment**, **final payment**.

## Where SmartCabinet supports each stage

| Stage | SmartCabinet role | Feeds / hands off to |
|---|---|---|
| Enquiry → Qualified Enquiry | **CRM**: capture the client, the enquiry, and its status | The quotation pipeline |
| Concept / Estimate | **Design + 3D visuals**: model the cabinetry, produce client-facing 3D renders for sign-off | Preliminary quotation |
| Quotation → Final Quotation | **CRM**: quote, revisions, approval, deposit milestones | Contract |
| Ordering / Engineering | Design finalised → **cut lists, panel optimisation/nesting, machine files** | The machines (below) |
| Production | Cut/edge/bore/assemble to the SmartCabinet output | Quality check |

## Design → machine hand-off (the production heart)

SmartCabinet's engineering output drives the three CNC machines. Confirm the exact file format each
accepts **[confirm]**:

- **Panel cutting** → **Altendorf F45** (`FA2303`), CNC sliding-table saw with ElmoDrive control —
 cutting list / optimised panels. See `../Machinery/altendorf-f45-panel-saw.md`.
- **Boring / drilling / grooving** → **Vitap K2-2.0** (`FA2304`), CNC boring/routing centre with the
 TPA Albatros control (has its own optimiser) — imports tool and drill/insertion programmes. See
 `../Machinery/vitap-k2-panel-saw.md`.
- **Edge banding** → **Hebrock F4** (`FA2301`) — edge material and corner-rounding recipe per panel.
 See `../Machinery/hebrock-f4-next-edge-bander.md`.
- **Assembly → Quality check → Packing** — off-machine; the QC step is where machine-caused defects
 (e.g. the edge-band corner fault) get caught and, if needed, raised on the Fault Log.

## SOPs to write once details are confirmed (proposed set)

1. **Enquiry & CRM intake** — how a new enquiry is entered and tracked to quotation.
2. **Design & 3D visual sign-off** — modelling standards, what the client approves, versioning.
3. **Quotation & deposits** — quote build, revisions, the deposit/payment milestones from the map.
4. **Cut-list / nesting export to the F45** — file format, optimisation settings, naming **[confirm]**.
5. **Boring/routing programme export to the Vitap K2** — tool library, drill/insertion maps **[confirm]**.
6. **Edge-banding recipe to the Hebrock F4** — material, trim, corner-rounding parameters.
7. **Backup & licensing** — where SmartCabinet data lives, backups, licence/renewal **[confirm]**.

## Open questions (for Minda)

- **[confirm] SmartCabinet product identity/version** and whether "SmartCabinet" is the vendor name.
- **[confirm]** Which machines it exports to directly, and in what file format each (the Vitap's
 Albatros and the F45's ElmoDrive accept different things).
- **[confirm]** Where its CRM/customer data lives (data-protection relevance) — cite, don't copy
 personal client data into this KB.

## Sources

- External (Drive): **the furniture business-process map**, `2026-01-27_BP scheme.pdf`,
 https://drive.google.com/file/d/1klUggv_PCNZgbKaI1io4-UC_-XwTPrsl/view — accessed 2026-09-15.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created as a draft anchored on the BP-scheme process map and the machines; SmartCabinet product specifics flagged [confirm] | Session — workshop operational systems build |
| 2026-09-15 | Corrected: the Vitap is registered as `FA2304` (was written as unregistered before the concurrent registration was reconciled) | Session — workshop operational systems build |
