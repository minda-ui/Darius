---
title: "Barcode and scan-event system"
category: Processes
status: draft
sensitive: false
created: 2026-09-17
updated: 2026-09-17
sources: []
related:
 - ../Machinery/brother-td-4420dn-label-printer.md
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Processes/machinery-maintenance-system.md
 - ../Troubleshooting/troubleshooting-and-fault-log-system.md
---

# Barcode and scan-event system

How scanning a code in the workshop turns into a record. **Phase 0 is built and live; Phases 1–4 are
designed and not built.** This article documents what exists, what was decided and why, and what each
later phase is waiting on — so that the next person to pick it up does not re-litigate settled
design decisions or start a phase whose precondition is still open.

**Status, stated plainly:** the `Scan Events` sheet exists and is **empty**. Nothing has been scanned
yet, because no scanner has been bought and the QR payload on the existing labels is still unknown.

## Two ID systems, deliberately never merged

This is the design decision everything else rests on.

| | Asset label number | Asset code |
|---|---|---|
| Example | `0019` | `FA2402` |
| What it is | The **physical tag** screwed to the machine | This register's **record ID** |
| Who owns it | Fishbone Group, estate-wide — master register owned by **Alex**, not this KB | This KB |
| Format | 4 digits on a pre-printed "PROPERTY OF FISHBONE GROUP" tag with a QR code and a phone number | `FA` + 2-digit **acquisition** year + 2-digit sequence |

They are joined by the Machinery Register's `Asset Label No.` column and **are never merged. Assets
are not renumbered to match labels, and labels are not reassigned to match assets.** The two series
have different owners, different rules and different lifecycles: a machine that is sold keeps its
`FA` code forever, while its physical tag may be removed or destroyed.

The `Scan Events` sheet enforces this in its own structure: `Code Scanned` holds the raw scanned
value untouched, and `Asset / Machine ID` holds the resolved `FA` code. Two columns, on purpose.

**Mapped so far** (owner photographs, 2026-09-17):

| Label | Asset |
|---|---|
| `0017` | ABAC GENESIS 15 500L compressor — **not registered, no code** |
| `0018` | `FA2301` Hebrock F4 |
| `0019` | `FA2402` AES SAF 10,000 STK |
| `0020` | `FA2303` Altendorf F45 |
| `0021` | `FA2304` Vitap K2-2.0 |

`FA2401` (Brother printer) has no label yet. The series starts above `0001`, so `0001`–`0016` are
elsewhere in the estate — this is a group-wide series, not a workshop one.

**A caution carried over from the handoff to Alex:** the words "PROPERTY OF FISHBONE GROUP" printed
on the tag are **deterrent labelling, not evidence of title**. They must not be copied into any
owning-entity column. Every machine here was invoiced to Fishbone Drylining Ltd, and the ownership
question (Task T004) is genuinely open.

## Phase 0 — built (2026-09-17)

**The `Scan Events` sheet**, Smartsheet ID `4828191892047748`. Append-only: every scan adds a row,
nothing is edited in place. That design is forced by a Smartsheet constraint worth knowing —
**forms create rows but can never update them** — so any workflow where a phone form is the input
device has to be append-only, with current state *derived* from the log rather than stored in it.

| Column | Type | Purpose |
|---|---|---|
| `Health` | RYGB formula | Red = New, Green = Actioned, Blue = No action needed. Matches the Fault Log / Maintenance Schedule convention |
| `Code Scanned` | Text (primary) | **The raw value, untidied.** Whatever the scanner read |
| `Event No.` | Auto-number `SE-00001` | Nobody types this |
| `Logged At` | Created-date | The scan time, set automatically |
| `Asset / Machine ID` | Text | The resolved `FA` code — separate from `Code Scanned` on purpose |
| `Logged By` | Created-by | Set automatically from the submitter |
| `Event Type` | Picklist | Fault report / Maintenance task done / Safety check done / Production stage complete / Offcut saved / Other |
| `Detail` | Text | Free text from whoever scanned |
| `Linked Record` | Text | The record this scan produced — `FL-002`, `MT-025`, `T018` |
| `Actioned` | Picklist | New / Actioned / No action needed. Drives `Health` |
| `Notes` | Text | — |

The exact `Health` formula:

```
=IF(Actioned@row = "Actioned", "Green", IF(Actioned@row = "No action needed", "Blue", "Red"))
```

It is a **column formula** — self-updating, maintained through the connector, **not edited by hand**
row-by-row. Same rule as the other RYGB columns in this workspace.

**Production and offcut options were put into `Event Type` at build time**, before either is used, so
that Phase 2 needs no restructuring of a sheet that will by then hold live history.

**Also built:** the `Asset Label No.` column on the Machinery Register, which is the join key
between this KB and Alex's group-wide register.

### Build notes — three Smartsheet API constraints found the hard way

Recorded because they will recur on the next sheet anyone builds here:

- **Column formulas are rejected at sheet-creation time** (error 1032). Create the sheet first, then
  add the formula column.
- **`CREATED_DATE` requires column type `DATETIME`**, not `ABSTRACT_DATETIME` (error 1079).
- **Column descriptions cap at 250 characters** (error 1041).

And one that cost real work later the same day: **a cell value over 4,000 characters is silently
truncated mid-sentence and still returns success.** Read the value back out of the response rather
than trusting the status code.

## Phases 1–4 — designed, not built

Ranked by value, each with a real gate. **None should start before its precondition is closed.**

| Phase | What it does | Blocked on |
|---|---|---|
| **1. Part labels** | SmartCABINET prints a barcode per part; scanning it identifies the part at any machine | **Two open questions**: what the existing labels' QR codes decode to, and whether the [Brother TD-4420DN](../Machinery/brother-td-4420dn-label-printer.md) actually speaks ZPL |
| **2. Stage tracking** | Scanning a part at each stage builds a live production tracker from the append-only log | Phase 1, plus the stage list from the BP-scheme map in [the workflow article](../Software/smartcabinet-and-production-workflow.md) |
| **3. Offcut library** | Label the physical offcut so the rack matches SmartCABINET's cutout library | Nothing technical — but the loop has **never been closed**: `Remaining cutouts` held seven offcuts while `Load cutouts` read *"There are no items to show."* Needs a minimum keep size and the `Vein` (grain) field filled |
| **4. Vitap program selection** | Scan a part, load its `.TCN` program on the machine | Phases 1–2, and knowing the shared Drive job folder's structure |

### Design decisions already made — do not re-litigate

- **Symbology: 2D/QR, not Code 128.** At 203 dpi a 1D barcode carrying a three-level ID gets
  uncomfortably wide; 2D holds more in less space and survives partial damage. **Always print
  human-readable text alongside** — a code nobody can read by eye is useless the moment a scanner
  fails.
- **ID scheme: three levels — `Order → Unit → Part`.** Matches how SmartCABINET already names parts
  (`01 SIDE LEFT`, `07 BACK 1`, `13 BOTTOM`), so it fits the data that exists rather than imposing a
  new taxonomy.
- **Scanner requirements: 2D imager, IP54 or better, cordless, with batch memory.** Batch memory
  matters — a scanner that only works in range of its base is useless at the far end of a workshop.
  **Nothing has been bought and nothing should be without the owner** (`CLAUDE.md` §6a).
- **Smartsheet is the tracking layer** (owner decision, 2026-09-17), taken in the knowledge that
  SmartCABINET is sold as "CRM/CAD/CAM/ERP" and its ERP module may already do production tracking.
  The decision stands; the open question is only so the two do not fight.
- **Machine asset labels do not come from the Brother printer.** The pre-printed group tags are
  durable stock; direct thermal fades. The printer is for short-life labels.

## Open questions

- **What do the asset labels' QR codes decode to?** Still unknown, and it **blocks Phase 1** — a
  scanner has to know what it will receive. One scan of any tag with a phone answers it.
- **Does the Brother TD-4420DN support ZPL?** SmartCABINET prints ZPL; Brother's manual for this
  model never mentions it while resellers claim it. Decisive test in the
  [printer's article](../Machinery/brother-td-4420dn-label-printer.md).
- **The shared Google Drive job folder** has not been identified or examined. Its structure
  constrains any ID scheme, and it may hold customer data from SmartCABINET's CRM side — **cite,
  never copy client data**.
- **Does SmartCABINET's ERP module already do production tracking?** Worth establishing so the
  Smartsheet tracker and the purchased software do not duplicate each other.
- **`0191 605 2945` is printed on every group asset label — and was in a SIP trunk migration** with
  a completion date of 03/08/2026 that has already passed. If that number did not survive, every
  asset label in the estate points at a dead line. Telephony is not this KB's scope; flagged only
  because the labels depend on it.
- **Who holds labels `0001`–`0016`?** Group-level, not this KB's to own — Alex's register.
- **No scanner has been specified to a make and model**, only to requirements.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-17 | Barcode system scoped: five uses ranked, symbology and ID scheme chosen, scanner requirements set, phased rollout agreed with a gate at each step; Smartsheet confirmed by the owner as the tracking layer | Session 14, entry "Networking correction and barcode scoping" |
| 2026-09-17 | **Phase 0 built** — `Scan Events` sheet created (`4828191892047748`) with its RYGB `Health` column formula, and `Asset Label No.` added to the Machinery Register | Session 14, same entry |
| 2026-09-17 | Pre-printed group asset labels received and mapped to machines (`0017`–`0021`); two-namespace rule recorded; handoff prepared for Alex's group-wide register | Session 14, same entry |
| 2026-09-17 | Article created | Session 14, same entry |

## Sources

No `Raw/` documents underpin this article: the system was designed in session with the owner and
built directly in Smartsheet. The label mapping comes from owner photographs taken on 2026-09-17;
the sheet structure is recorded from the live sheet `4828191892047748`; the boundary with the
group-wide register is set out in
`Outputs/2026-09-17-handoff-workshop-assets-for-group-register.md`.
