# Change log — 2026-09-17 — Networking claim corrected; barcode system scoped; SmartCABINET vendor identified

_Append-only dated session file (Fishbone Group). See `CLAUDE.md` §4._

## Session 14 — 2026-09-17 (morning): a documented fact turned out to be wrong

**Owner instruction (Minda):** a morning of live SmartCabinet walkthrough, then *"We need to create a
barcode system inside the workshop"* — plan, printer, scanner, and a progress tracker.

### The correction (the substantive change)

`CLAUDE.md` §1 had asserted since the KB's early sessions:

> "**Two computers, not networked.** ... They are **not** live-networked — files move by manual
> transfer (USB/similar)."

**The owner corrected this directly:** the workshop runs on a network served from an on-site server
rack; a **WiFi 7** access point covers the whole workshop floor; **files are shared between the design
computer and the machines through Google Drive, in a dedicated folder**. The Vitap's control PC is on
the network.

Consequences recorded:
- `CLAUDE.md` **v8 → v9**. §1 rewritten; v8 (`1teaQsa5DRuZGbtvSSSRjmpAo6p6Uu0Gp`) archived, not
  trashed. New Drive id `1STw2KS1Ny7GKeDRMC_UbLxZtkjPtCr8z`.
- **Downstream sweep done, and it found nothing to fix.** `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`
  and `Wiki/Software/smartcabinet-and-production-workflow.md` were both read in full: **neither repeats
  the networking claim.** It had not propagated out of the control file.
- **A nuance kept rather than dropped:** a shared network does *not* merge two programs' internal
  catalogs. SmartCabinet's **CAM Tools** table and TpaCAD's **CN Tools** catalog remain separate
  application databases; whether an entry in one reaches the other is **unverified** and still bears on
  Task T016. Recorded in §1 as unverified rather than asserted either way.
- **New §3 lesson:** *a fact recorded without a source hardens into an assumption nobody revisits.* The
  claim carried no citation and no `[confirm]` marker, survived six versions, and shaped real advice —
  an entire barcode-system design was built around an air gap that does not exist — before anyone
  questioned it. Infrastructure and environment facts now get a source or a marker, like any figure off
  an invoice.

### SmartCABINET — vendor and product identified (cross-KB, cited not copied)

Found in the **Fishbone Construction KB**, `Wiki/Suppliers/kosmosoft-smartcabinet.md` (read-only to
this KB): the software is **SmartCABINET** by **Kosmosoft Engineering S.r.l.**, Bagnolo San Vito (MN),
Italy — "CRM/CAD/CAM/ERP software for cabinet making". Offer/contract **22910**, 10/09/2026, **€1,000,
paid**, registered `FCD0000024` in the *Construction* Document Register.

- **Billed to Fishbone Drylining Ltd, not AMFA Furniture Ltd** — the same pattern as every machine.
  **New evidence for Task T004** (owning entity): it is not only the machinery, it is the software too.
- **It has an ERP module.** Raised as an open question: building a Smartsheet production tracker
  without knowing what the purchased software already does risks duplicating it. Owner has chosen
  Smartsheet as the tracking layer regardless (decision, 2026-09-17).
- The Construction KB carries an open question — *"has installation happened?"* — which this morning's
  screens answer outright. **Not actioned: that KB is read-only from here** (§6a). Flagged for the
  owner/Victoria.

### Learned from the owner's live screens (not yet a Raw item)

- **`releasenote_SC.txt`** — latest released version **3.2.0.9** (07/07/2026); **3.2.0.8** (05/05/2026)
  added the custom CSV split by material, a **description column on the CAM Tools table**, **ZPL
  barcode label printing**, a Felder postprocessor and **"Legrabox mill for TCN post"**. Bilingual
  ITA/ENG. *Which version is actually installed is still `[confirm]`* — a release-note file ships the
  whole history.
- **Panel Optimization** — real job `AMFA Wall Unit 600 RH` across two 19mm materials on 2800×2070
  sheets (`W1100 ST9`, `U963 ST9 DIAMOND…` — read as Egger decors `[confirm]`). Parts carry unit name +
  number + role (`01 SIDE LEFT`, `07 BACK 1`, `13 BOTTOM`, `15 SHELF 1`…). **Utilisation 28.4% and
  9.2%**, with only **0.8% true waste** and **70.8% recoverable offcut**; 11 cuts / 11.1 m on the sheet.
- **Offcut library exists and is unused.** `Remaining cutouts` listed seven offcuts (largest 2800×1469
  and 2800×1200; smallest a 1330×41 sliver); `Load cutouts` read *"There are no items to show."* The
  loop is available but has never been closed. Recommendations recorded for the process article: a
  minimum keep size, fill the `Vein` (grain) field, and label the physical offcut so the rack matches
  the library.

### `FA2303` (F45) — does it take a digital cut list?

Answered from the KB rather than by re-reading the manual. The ElmoDrive is a **positioning** control
(rip fence, blade height, tilt, scorer, crosscut angle) with tool management and per-axis calibration.
Across all three F45 documents **no cut-list or job-file import is documented**; the only data
interface that appears is a USB drive, for firmware updates (`E21`/`E22`) and remote-maintenance files
(`E23`). An *"optimisation limit"* error in the `E01`–`E15` block hints at some optimisation function,
but that block's OCR pairing was never reconstructed. **Working answer: the saw takes dimensions, not
cut lists** — to be confirmed against the control's own menus before being recorded as fact.

### Brother TD-4420DN label printer

Owner uploaded `td-4210d_4410d_4420dn_4520dn_uke_ug_a.pdf` to `Raw/`. **Read coverage: pages 1–77 of
128** — Drive's text extraction dropped the Specifications appendix (p.113), Routine Maintenance and
Troubleshooting. Stated rather than glossed.

- **A contradiction recorded, not resolved.** Reseller and vendor listings say the TD-4420DN supports
  **ZPL II / EPL2 / DPL emulation**; **Brother's own user guide for this exact model never mentions
  ZPL**, and Brother's published *ZPL II Emulation Guide* is branded for the **TD-4420TN/4520TN** —
  the thermal-*transfer* siblings. The manual documents only Brother's own stack (P-touch Editor,
  P-touch Template, Transfer Manager, mass-storage `.BIN`/`.BLF` command files, an SDK). **Decisive
  test: look for an emulation/`FBPL` tab in the Printer Setting Tool, or print one ZPL label.** Open.
- **Confirmed from the manual:** LAN port is on the `4420DN`/`4520DN` only (10BASE-T/100BASE-TX); max
  image width **832 dots** (vs 1280 on the 4520DN), consistent with 203 dpi / ~104 mm; barcode **Crop
  Print is `TD-4520DN` only**; non-Brother roll media explicitly permitted; mass-storage mode prints
  without a driver.
- **Durability, in Brother's own words** — *"Do not expose the RD Roll to direct sunlight, high
  temperature, high humidity, wind, or dust as it may cause labels to peel off or discolour"*;
  *"Scratching the printed surface … can cause the colour to change or fade."* Direct thermal suits
  short-life part labels; long-dwell offcut and machine-asset labels need a different answer.
- **Not registered as an asset.** Deliberate: per the `FA2601`→`FA2301` lesson, no code is assigned
  until the acquisition year is evidenced. **Invoice requested from the owner.**

### Barcode system — scoped, not yet built

Plan put to the owner covering five uses ranked by value (machine asset labels → part labels → stage
tracking → offcut library → Vitap program selection), symbology (2D/QR over Code 128 at 203 dpi, with
human-readable text alongside), a three-level `Order → Unit → Part` ID scheme, scanner requirements
(2D imager, IP54, cordless, batch memory) and a phased rollout with a real gate at each step.
**Smartsheet confirmed by the owner as the tracking layer.** Design recorded: an append-only
`Scan Events` sheet feeding a derived `Production Tracker`, because Smartsheet forms create rows and
never update them. The BP-scheme stage list in
`Wiki/Software/smartcabinet-and-production-workflow.md` supplies the stages.

**Phase 0 built (later the same session, on the owner's go-ahead):**

- **Smartsheet `Scan Events`** created (`4828191892047748`) — the append-only scan log. `Health` (RYGB
  column formula off `Actioned`, matching the Fault Log and Maintenance Schedule convention),
  `Code Scanned` (primary — the raw value, untidied), `Event No.` (auto `SE-00001`),
  `Logged At`/`Logged By` (set automatically on row creation), `Asset / Machine ID`, `Event Type`,
  `Detail`, `Linked Record`, `Actioned`, `Notes`. Production and offcut options were included in
  `Event Type` now so the sheet needs no restructuring at Phase 2.
  *Build notes: column formulas are rejected at sheet-creation time (error 1032) and had to be added
  afterwards; `CREATED_DATE` requires column type `DATETIME`, not `ABSTRACT_DATETIME` (error 1079);
  column descriptions cap at 250 characters (error 1041).*
- **`Asset Label No.` column** added to the Machinery Register.

**The labels arrived mid-session and changed the design for the better.** They are pre-printed
"PROPERTY OF FISHBONE GROUP / TEL: 0191 605 2945" asset tags with a QR code and a four-digit number
(`0017`, `0018` seen). Durable printed stock, so the direct-thermal fade problem does not apply to
machine labels at all. Consequences recorded:
- **Two ID systems now, deliberately not merged.** The label number is the physical tag; the `FA` code
  is the register ID. Written into the new column's description, with *never renumber assets to match
  labels*. `Scan Events` already separates `Code Scanned` from `Asset / Machine ID` for the same reason.
- **The series starts at 0017**, so `0001`-`0016` exist elsewhere — this is a **group-wide** series.
- **Owner decision:** one group-wide asset/label register, to be built by **Alex**, not per-KB. The
  boundary agreed: that register holds the index (label no., what it is, whose it is, where); this KB
  keeps the detail; **the join key is the label number**. Recorded in
  `Outputs/2026-09-17-handoff-workshop-assets-for-group-register.md`, the handoff prepared for Alex.
- **"PROPERTY OF FISHBONE GROUP" is deterrent labelling, not evidence of title** — flagged so the
  wording does not get copied into the group register's owning-entity column and bake T004's ambiguity
  in estate-wide.

**Brother TD-4420DN — order receipt processed, asset NOT registered.**
`Raw/Fishbone Drylining Ltd Mail - Order Receipt SOA2606351.pdf`: Printerland order **SOA2606351**,
**9 May 2024** — printer £211.58 ex VAT plus two direct-thermal die-cut rolls (102x50mm £14.45,
102x152mm £5.57); £231.60 + £46.32 VAT = **£277.92**.
- **Acquisition year 2024 evidenced**, so the code is **`FA2401`** — the first 2024 asset here. Had it
  been numbered when it first came to notice it would have been `FA26xx`, repeating `FA2601` exactly.
  The discipline of waiting for the document worked.
- **Four parties, none of them AMFA**: ordered from the Fishbone Drylining mailbox; **invoiced to
  Mindaugas Gaudiesius personally at a residential address**; **shipped to Fishbone Waste, Unit 31** -
  not Unit 32. Its presence in the workshop is assumed, not confirmed.
- It is an **order receipt, not the invoice** ("an invoice will also follow"); that invoice has not
  been seen.
- **Not registered pending the owner's confirmation of where it physically sits.** Registering Unit 31
  / Fishbone Waste equipment on the workshop's register would assert something the paperwork contradicts.
- Useful by-product: the shop already owns **102x50mm** die-cut stock, a workable part-label size.

**Still not built** — the production tracker. The ID scheme depends on what SmartCabinet's label
designer can put in a barcode field, and on the structure of the shared Drive job folder, neither of
which has been seen.

## Governance

Owner-directed work inside this KB only. No outward action; no purchase committed (scanner and label
stock specified for the owner to quote and buy, per §6a); no other KB written to — the Construction KB
was **read and cited**, never edited. No secret or credential handled.

## Still open at session end

- **Which SmartCabinet version is installed**; what its label designer can place in a barcode field.
- **The shared Google Drive job folder** — not yet identified or examined (may hold CRM/customer data:
  cite, never copy).
- **The ZPL test** on the TD-4420DN.
- **Is `minda-ui/Darius` a private repository?** The F45 article records the ElmoDrive's
  remote-maintenance access code (published in the manual, but it does permit a technician login), and
  the full Wiki mirror has not yet been pushed. Raised with the owner before any Wiki sync.
- Does SmartCABINET's ERP already track production?
- **Where the Brother TD-4420DN physically sits** - Unit 32 (workshop) or Unit 31 (Fishbone Waste)?
  Decides whether it is registered here as `FA2401`. The actual invoice (as opposed to the order
  receipt) has also not been seen.
- **What the asset labels' QR codes decode to**, and which label number goes on which machine.
- **Who holds labels `0001`-`0016`**, and where that list lives - group-level, so not this KB's to own.
