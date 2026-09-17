# Change log — 2026-09-14 — Hebrock F4 next manual processed

**Session 2.** Owner reported the workshop's first machine, a "Hebrock F4", and pointed at 6 PDF
files (`part 1.pdf`-`part 6.pdf`, ~66 MB total) already placed in `Raw/` — the machine's operating
manual, needed for future maintenance and for setting the machine up.

## What was done

Read all 6 parts (via a background sub-task, to keep the raw OCR text out of the main session) and
extracted: machine identification, technical specs, safety instructions, installation/commissioning
steps, and the full maintenance/lubrication schedule with intervals. The manual turned out to cover
a family of three machines (F2/F4/F5 "next") together, with some spec tables not clearly labelled
by model, and the six files are scanned/OCR'd so several individual figures came out illegible —
both are recorded as open questions rather than guessed at.

**Created:** `Wiki/Machinery/hebrock-f4-next-edge-bander.md` — key facts, installation/setup
summary, safety summary, full maintenance & lubrication tables, and an Open questions section
covering everything that could not be confirmed from the manual alone (serial number, purchase
date/price/ownership, the ambiguous F2/F4/F5 dimension table, an illegible dust-extraction figure,
a possible CE Declaration of Conformity gap, and a PLC-battery part-name mismatch between two
sections of the manual).

**Updated:** `Wiki/index.md` (Machinery entry added); `CLAUDE.md` (bumped to Version 2 — workshop
snapshot in §7 now names this machine instead of reading "no machinery inventoried yet").

**Smartsheet — workspace `Workshop`:**
- `Machinery Register - Database`: one row added, ID `FA2601`, Machine Name "Hebrock F4 next —
 Edge Bander", Manufacturer/Model/Machine type filled from the manual, Status `In service` (setup
 in progress). Purchase date/price, ownership, supplier, serial number and all compliance due-dates
 left **blank** rather than guessed — see Open questions in the Wiki article.
- `Document Register`: one row added for the manual itself, `Document No.` left `pending` — this
 KB is not entitled to self-assign a group document number (see `CLAUDE.md` §1); it needs
 registering on the shared Fishbone Group Document Register under AMFA Furniture Ltd's `FA` prefix,
 which this session did not attempt without the owner's go-ahead (that register is a shared,
 cross-company resource).
- `Tasks`: three rows added — (1) confirm the machine's real serial number, purchase date/price and
 ownership/finance terms from purchase paperwork or the data plate; (2) request a CE Declaration of
 Conformity from the supplier/Hebrock, since none was found in the 6-part scan; (3) register the
 manual on the shared group Document Register once access is confirmed, then update the local
 Document Register row.

## Judgement calls made, flagged for the owner

- **Asset code `FA2601`** assumes acquisition year 2026 (today's date) since no purchase date was
 supplied. If the machine was actually bought earlier, this code should be corrected before more
 data is built on top of it — asset codes aren't meant to be renumbered casually once in use.
- **Status set to `In service`** on the assumption that "setting the machine up" means it has
 arrived and installation is starting, not that it's still on order. Correct if wrong.
- **Did not push a row to the shared group Document Register** (sheet `7352854736144260`) — that
 register is shared across the whole Fishbone group, this KB's write access to it hasn't been
 confirmed, and appending to it is the kind of shared-system write `CLAUDE.md` §6a says should be
 deliberate, not routine. Logged locally instead, with a Task to complete the real registration.

## Open questions carried forward

See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`, "Open questions" — serial number, purchase
details, the F2/F4/F5 dimension-table ambiguity, an illegible dust-extraction spec, the CE
Declaration gap, and the PLC-battery part-name mismatch.
