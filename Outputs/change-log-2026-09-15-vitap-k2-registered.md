# Change log — Vitap K2-2.0 registered (2026-09-15)

Session 8. Third machine's manual (4 PDF parts, `Vitap K2 2.0 manual part 1-4.pdf`) and its invoice
(`Invoice 100154 - 09.11.23 - OCN231185 - Balance.pdf`) processed, following the same pattern used
for the Hebrock F4 (`FA2301`) and Altendorf F45 (`FA2303`).

## What was found

- **Manufacturer/machine**: VITAP S.p.A. (Italy), model K2-2.0 — a CNC boring/drilling-inserting
 machine on Euro-32 spacing, extended with a pantograph milling/grooving unit and optional
 aggregated heads (front milling, LAMELLO, OVVO). Manual edition `1.0-09/19`.
- **Duplex-scan structure confirmed again**: parts 1-2 reconstruct printed pages 1-59; parts 3-4
 reconstruct printed pages 60-126 — a fourth manual in this KB to show the same
 odd-descending/even-ascending scan artefact as the Hebrock and Altendorf manuals. Two parallel
 background research agents each read one duplex pair; findings cross-checked at the page 59/60
 join and matched with no gap or overlap.
- **No serial number or manufacture year in the manual** — the type-plate diagram is an uncompleted
 template. The invoice supplied Serial No. 320070 AT instead; used that as the working value and
 flagged the manual's own gap in the Wiki article.
- **No EC Declaration of Conformity for this specific unit was found** — only the manual's own
 blank facsimile DoC is available (directives 2006/42/EC, 2014/30/EU, 2014/35/EU; standards EN ISO
 12100:2010, EN 60204-1:2006). The manual's own §2.1 cites an older, inconsistent directive set —
 same category of finding as prior machines' compliance-paperwork issues, recorded but not resolved.
- **§6.8 Safety Device Efficiency Check does not obviously carry the F45's documentation
 requirement.** It reads as a mandatory functional test before every automatic-mode activation, not
 an explicitly dated/logged inspection. Deliberately did **not** create a Processes article or add
 this machine to the Smartsheet Safety Check Log on the strength of this alone — flagged as an open
 question for the owner instead, to avoid inventing a compliance obligation the manual doesn't
 actually state.
- **Invoice 100154 revealed a second asset**: Inventair MK2 MTFA, Serial No. 1696, £4,005.00, same
 purchase date (09/11/2023), same invoice, same billed-to entity (Fishbone Drylining Limited). No
 manual has arrived for it yet (per the owner, "it will follow later with manuals"), so — consistent
 with this KB's rule against writing detail ahead of real source material — it was registered in
 the Smartsheet Machinery Register only; no dedicated Wiki article yet.
- **Cross-invoice price check repeated a third time**: invoice 100154's 70%-balance Net Total is
 exactly 70% of the sum of all listed items' full prices, confirming the Vitap's £68,000 as a full
 price (not a partial one) by the same method already validated on the Hebrock and Altendorf
 invoices. This closes out Task T005's underlying question generally, not just for the Hebrock.
- **Housekeeping finding, not acted on**: a duplicate copy of the same 4 manual parts and 4 F45
 spare-parts-manual parts exists in a Drive folder (`1qF7XiS2Jud3y8V6lf4Nyu7_JAMEJNsai`) outside
 this KB's own `Raw/` folder tree (`18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R`) — same filenames, same file
 sizes, different file IDs, not a child of the Workshop KB root. Not deleted or touched — outside
 this KB's folder tree and not clearly this KB's to clean up — but worth the owner's attention if
 it's an accidental duplicate upload.

## What was done

- Created `Wiki/Machinery/vitap-k2-panel-saw.md` for `FA2304` (Key facts, Installation/setup, Safety
 incl. the §6.8 discrepancy, Maintenance schedule, Fault diagnosis, Open questions, Sources).
- Updated `Wiki/index.md` to list the new article.
- Smartsheet Machinery Register: added `FA2304` (Vitap K2-2.0) and `FA2305` (Inventair MK2 MTFA)
 rows.
- Smartsheet Document Register: added rows for the Vitap manual (4 parts, one document number
 pending) and invoice 100154, `Document No.` = `pending` as with all prior rows (no confirmed write
 access to the shared group register yet).
- Smartsheet Tasks: added T012 (confirm Vitap serial/type-plate details against the physical
 machine), T013 (owner to clarify whether §6.8 needs a documented/logged check like the F45's, and
 if so create the matching Processes article + Safety Check Log rows), T014 (confirm whether
 `FA2305` supersedes `FA2302` and clarify extraction sizing for the Vitap); updated T005 (Hebrock
 price ambiguity) to Done, noting the cross-invoice check now confirmed on three separate invoices;
 updated T010 (FA2302 status) with the `FA2305` cross-reference.
- Updated `Outputs/kb-registers.md` (change-log entry, processed items rows, wiki structure change,
 outputs produced) and `CLAUDE.md` (v5: `FA2304`/`FA2305` added to the assigned-codes list and §7
 workshop snapshot).

## Judgement calls made, flagged for the owner

1. Did **not** assume the Vitap's §6.8 check needs the same Smartsheet-logged treatment as the F45's
 monthly check, despite the surface similarity (both are "safety device efficiency checks" named
 in a manual's Chapter 6) — the actual text differs in a way that matters (no stated interval, no
 "record this" instruction). This is a judgement call, not a confirmed fact; raised as Task T013
 rather than silently mirroring the F45's process.
2. Did **not** create a Wiki article for the Inventair MK2 MTFA (`FA2305`) given no manual exists for
 it yet — registered the bare facts (serial, price, date) in Smartsheet only, consistent with how
 this KB avoided premature folders/content elsewhere (see `CLAUDE.md` §1).
3. Used the invoice's serial number (320070 AT) as the Vitap's serial number given the manual's own
 type-plate field is blank — flagged this substitution explicitly in the Wiki article rather than
 presenting it as if the manual itself confirmed it.
4. Did not act on the duplicate-folder finding beyond recording it — deletion or consolidation of
 files outside this KB's own `Raw/` folder is not this KB's call to make unilaterally.
