# Change log — 2026-09-17 — Two documented facts corrected (networking, and the workshop's address); barcode Phase 0 built; SmartCABINET vendor identified; asset labels applied, two disposals, `FA2401`/`FA2402` registered, an unregistered compressor found, the charter taken to v11 and the owed Wiki articles written

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
- **Not registered as an asset at this point.** Deliberate: per the `FA2601`→`FA2301` lesson, no code
  is assigned until the acquisition year is evidenced. Invoice requested from the owner — it arrived
  later the same session, and the printer was registered as `FA2401`; see below.

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

**Brother TD-4420DN — order receipt processed.**
`Raw/Fishbone Drylining Ltd Mail - Order Receipt SOA2606351.pdf`: Printerland order **SOA2606351**,
**9 May 2024** — printer £211.58 ex VAT plus two direct-thermal die-cut rolls (102x50mm £14.45,
102x152mm £5.57); £231.60 + £46.32 VAT = **£277.92**.
- **Acquisition year 2024 evidenced**, so the code is **`FA2401`** — the first 2024 asset here. Had it
  been numbered when it first came to notice it would have been `FA26xx`, repeating `FA2601` exactly.
  The discipline of waiting for the document worked.
- **Billing trail**: ordered from the Fishbone Drylining mailbox; **invoiced to Mindaugas Gaudiesius
  by name at 6 Beverley Place** — which this session first described as "a residential address" purely
  from its format, and which the owner then confirmed is **the companies' registered office**. That was
  the third unsourced inference of the day, and it is corrected everywhere it was written. No company
  is named on the billing line, so the owning entity is unconfirmed — the T004 question again.
  **Shipped to Fishbone Waste at Unit 31**, then that unit's occupant; Unit 31 is now the workshop.
- It is an **order receipt, not the invoice** ("an invoice will also follow"); that invoice has not
  been seen.
- **Registration was held** pending confirmation of where the printer physically sits, because the
  paperwork pointed at Unit 31/Fishbone Waste while the KB still believed the workshop was Unit 32.
  The owner then confirmed the workshop *is* Unit 31 and the printer is there — so **`FA2401` was
  registered**, with the full billing trail in the register's Note field rather than tidied away.
- Useful by-product: the shop already owns **102x50mm** die-cut stock, a workable part-label size.

### The second correction of the day — the workshop is at Unit 31, not Unit 32

The owner corrected a second long-standing documented fact: **Unit 32 is no longer held.** The
**workshop is Unit 31**; **office and warehouse are Unit 30**. Evidenced by the **Unit 31 lease cover
page** — *Forth England Limited* (landlord) and *Furniture by Fishbone Limited* (tenant), **dated
25 June 2026**, NE28 6HA.

- **"Furniture by Fishbone Limited" is not a new company.** Companies House confirms it renamed to
  **AMFA Furniture Ltd on 13 July 2026**, three weeks after the lease was signed — already documented
  in the Fishbone Construction KB (archived `furniture-by-fishbone-ltd.md` → `amfa-furniture-ltd.md`,
  CH overview `FH0000019`). Found by following §0's own rule to check the sister KB rather than
  assume this one is silent. Nothing to reconcile.
- **Unit 31's previous occupant was Fishbone Waste**, who have moved out — which is why the 2024
  Brother order receipt shows "Fishbone Waste, Unit 31" for what is now the workshop's address. The
  two are recorded as the same unit under different occupants, not collapsed into one.
- **`CLAUDE.md` v9 → v10**; v9 (`1STw2KS1Ny7GKeDRMC_UbLxZtkjPtCr8z`) archived. New id
  `1l4lgxmy5LJNdQQnTPIVVSC0YbY7mbcf4`.
- **All six Machinery Register rows** updated to Unit 31.
- **All three machinery articles swept** — and this one was *not* a find-and-replace. Each cited Unit
  32 as the **delivery/invoice address**, which remains historically true. Each now carries two rows:
  *Location — current* (Unit 31, owner-sourced) and *Location — as invoiced 2023* (Unit 32, retained
  because it is what the invoice says). Predecessors archived, not overwritten.
- **The handoff to Alex was reissued** with the correction, the lease/entity evidence, and the printer
  now registered. The superseded draft is archived.

**The finding that matters more than the address: the machines were moved, and nothing records it.**
A move is a re-commissioning event. Each article now carries a "The 2026 move" section drawn from its
own manual, and a matching open question:

- **`FA2301` Hebrock** — phase sequence (chain-bed feed motor direction), the separate 10 mm² PE bond,
  floor-anchoring or castor locking, ≥500 mm infeed/outfeed clearance, extraction at **≥25 m/s**
  through ø140 mm with the ducting earthed.
- **`FA2303` Altendorf F45** — the heaviest set: a floor flat, level and able to bear ~1100 kg (centre
  of gravity ~100 mm *below* the blade axis); swing-arm 0.5 mm; main-table height **0.1–0.2 mm**;
  cross-slide height; free-cut both sides; **angle-cut calibration by test cut, < 0.2 mm**; 0° blade
  tilt; motor rotation direction verified by an electrician; extraction interlocked via a
  potential-free contact or current transformer at **≥20 m/s**. Its own fault table already lists the
  two symptoms a bad re-install produces — *"cut size ≠ fence setting"* and *"blade burns on
  sliding-table side / rip-fence side"*.
- **`FA2304` Vitap** — 1030 kg: levelling on threaded feet against a spirit level, auxiliary floor
  screws, ≥1000 mm clearance, ≥500 lux, vibration-free floor, **spindle rotation direction**
  re-verified, suction reconnected and the drilling unit run through full stroke to check for hose
  fouling. Its troubleshooting table's *"spindles rotate the wrong way — inverted phases"* is exactly
  the failure a move can introduce.

**Not assumed skipped — simply unrecorded.** New duct runs also change the extraction velocity
actually delivered, which compounds the open sizing question for the Vitap (≈2000 m³/h, T014).

**One thing removed rather than added:** the F45 article previously reproduced the ElmoDrive's
**remote-maintenance access code**. It is printed in the published manual, but it still lets a
technician log into the saw, and the full Wiki mirror is about to be pushed to git. The code is now
described but not reproduced.

**Still not built** — the production tracker. The ID scheme depends on what SmartCabinet's label
designer can put in a barcode field, and on the structure of the shared Drive job folder, neither of
which has been seen.

### After the sweep: labels applied, two disposals, two new assets, and a machine nobody had registered

The owner then walked the shop photographing each machine as its label went on. What was meant to be
a simple mapping exercise turned up two disposals, a second new asset and an unregistered machine that
every other machine depends on.

**Label numbers applied** — the `Asset Label No.` column filled in from photographs of the physical
tags, one machine at a time:

| Label | Asset | Machine |
|---|---|---|
| `0017` | *(none — not registered)* | ABAC GENESIS 15 500L screw compressor — see below |
| `0018` | `FA2301` | Hebrock F4 next edge bander |
| `0019` | `FA2402` | AES SAF 10,000 STK extractor |
| `0020` | `FA2303` | Altendorf F45 |
| `0021` | `FA2304` | Vitap K2-2.0 |

`FA2401` (the Brother printer) has no label yet. **`0019` was deliberately left `[confirm]` for
several steps**: the owner photographed it on "our extractor" while the KB held two registered
extractors and no way to tell which. Guessing would have been easy and wrong — the answer turned out
to be a third option the register did not contain at all.

**Both Inventairs are gone.** The owner: *"we sold all Inventair extractors and purchase one big
AES"*. `FA2302` and `FA2305` marked **Sold**.

- This closes the T014 question that had stood since Session 8 — *does `FA2305` supersede `FA2302`?*
  The answer is **neither**: both were sold and replaced by a single centralised unit that was never
  registered. The suspicion had been recorded as unconfirmed rather than asserted (§3's "don't assume
  one finding resolves another"), so nothing had to be unpicked.
- **Disposal dates and sale proceeds are not known** and are recorded as missing, not glossed. Both
  assets have a purchase price on the register, so the disposals have a book consequence.

**`FA2402` registered — AES SAF 10,000 STK fine dust extractor.** From `Raw/Invoice 22473.pdf`:
invoice **22473**, **08/10/2024**, *"1 X NEW AES STK 10000 DUST EXTRACTOR"*, **serial A-077**, stock
code T11021, from **Markfield Woodworking Machinery Ltd** (Bardon Hill, Leicestershire), £5,950 +
£400 delivery = £6,350 net, **£7,620 inc VAT, marked paid in full** — which satisfies the invoice's
own retention-of-title clause. Acquisition year **2024 evidenced before the code was assigned**, the
same discipline as `FA2401`.

- **Delivered to Unit 31 in October 2024** — *nearly two years before AMFA's Unit 31 lease of
  25/06/2026*. That is evidence about the shape of the "2026 move": it looks less like a relocation
  into new premises than like AMFA taking a lease on a unit the group already occupied. Recorded as
  evidence for T004, not as a conclusion.
- **Billed to Fishbone Drylining Ltd** — the same pattern as every machine and the software.

**The quotation arrived later and turned a model name into a specification.**
`Raw/Fishbone Drylining - AES 10,000.pdf` — MWM machinery quotation, **02/10/2024**, six days before
the invoice and at identical figures, so the two describe the same machine. **This is the only
technical specification the KB holds for `FA2402`:** capacity **10,000 m³/h**; motor 11 kW / 15 HP
direct drive, star-delta; suction diameter **355 mm**; **64 filters at Ø160 × 940 mm, 30.22 m²**;
three metal waste buckets; 1200 × 3170 × 2330 mm, 720 kg; 1.2 mm body sheet; propeller plate and
blades ≥3 mm, dynamically and statically balanced; a **Part Holder** stopping parts over 25 × 25 mm
reaching the propeller (protects the balance, reduces fire risk).

- **T014's standing caveat is discharged.** The task had said for days that *"the '10000' in STK 10000
  is PROBABLY airflow in m³/h but that is a reading of the model name, NOT a specification — do not
  rely on it."* It is now sourced.
- **On paper the unit is comfortably large**: known demand is the Vitap's ~2000 m³/h plus roughly
  1,110 m³/h for the F45 (**my own arithmetic from ≥20 m/s through ø140 mm, labelled as such in the
  task, not a manufacturer figure**) plus the Hebrock, whose duct diameter the KB does not hold, so
  its ≥25 m/s cannot be converted. Call it ≥3,100 m³/h against 10,000 rated.
- **But the vendor supplied none of the installation.** Two clauses recorded verbatim because they
  decide who owns the risk: *"Our machinery is not supplied with electrical cabling, extraction hose
  or blades"* and *"You are responsible for the electrical connection of your machinery, we do not
  electrically connect machinery on-site."* The ductwork and electrics were the group's own work and
  **nothing about that installation is recorded anywhere** — a rated fan capacity is a test-condition
  number; what each machine actually receives is decided by pipework nobody documented, and the
  machines have since been moved.
- **T014 retitled and narrowed** to *"Verify installed extraction performance at each machine against
  FA2402 — capacity now sourced, installation never recorded"*. The closing action is an **anemometer
  velocity reading at each machine's connection**, which also answers the extraction half of T018.
- **One figure left unreconciled rather than interpreted:** *"Dust absorption rate 40 m/min"* matches
  neither the inlet velocity (355 mm at 10,000 m³/h ≈ 28 m/s) nor the filter face velocity
  (10,000 ÷ 30.22 ≈ 5.5 m/min). Recorded verbatim with an instruction not to use it until a vendor or
  a real manual explains it.
- **"SAF" resolved.** The quotation names the machine **"AES SAF 10,000 STK"** — which is why
  `Raw/AES Extractor.pdf`, the control-panel schematic, was drawn for *SAF Technical Ltd*. AES
  Elektronik Makina is the OEM; SAF is part of the product designation, not an unrelated third party.
  Recorded because the alternative reading (an unknown third company in the chain) would have been a
  false lead.
- **Still not an operating manual.** Neither document carries maintenance intervals, filter-change
  criteria, safety instructions or a fault table, so `FA2402` **cannot yet join the Maintenance
  Schedule or the Fault Log**. Consumables are now known (64 filters, three buckets), so a schedule
  can be built the moment intervals arrive.
- **Banking details (HSBC sort code and account number) appear on the quotation and were deliberately
  not copied into the KB** — recorded as a statement of what was omitted and why, so nobody later
  assumes the extract was incomplete by accident.
- **Oddity flagged, not silently dropped:** the quotation's extracted text opens with the line
  *"Breitbandschleifmaschine KÜNDIG Topiq-2 1100"* — almost certainly a leftover template title from
  an unrelated wide-belt sander, but it is on the document, so it is on the record.

**A machine nobody had registered — and it feeds all the others.** Label `0017` went on an **ABAC
GENESIS 15 500L rotary screw compressor with integrated dryer**, which was not in the Machinery
Register at all. From its type plate: serial **ITJ717909**, product 4152025548, **year 2023**, 455 kg,
**15 kW three-phase**, 0.58 kW dryer, max **10 bar**, refrigerant **R513A, 0.5 kg = 316 kg CO₂e**.

- **No code assigned.** The plate year is *manufacture*, and this KB's convention needs *acquisition*
  — the `FA2601` lesson applied for the third time in one day. **`FA23xx` would probably be right and
  is still not good enough.** Purchase paperwork requested; **T019** raised to register it once the
  year is evidenced.
- **The gauge read 5.4 bar.** The Hebrock wants a minimum of 7 bar, the F45 8 bar to ISO 8573-1:2010
  [7:4:-], the Vitap 6–8 bar. That is **below what all three machines ask for** — recorded as a
  reading from one photograph at one moment, not as a diagnosis, but it is the kind of reading that
  explains intermittent pneumatic faults.
- **The service log on the manufacturer's yellow label is blank** — printed columns for *Official
  Specialist / Latest Service / Running Hours / Type of Service*, all empty in the photograph. Either
  the machine has never been serviced or the servicing was never logged on it. **T020** raised for
  service history and the F-Gas position.
- **F-Gas: 316 kg CO₂e is 0.32 tonnes, far below the 5-tonne leak-check threshold**, so no periodic
  leak checking is triggered by charge size. Worked through and recorded so the question does not get
  re-asked.
- **The point that outranks all of it:** this one machine supplies the pneumatics of the Hebrock, the
  F45 and the Vitap. It is a **single point of failure for the entire workshop**, and it was not in
  the register.

**First real supplier lead in the whole KB.** The Vitap photograph caught an **R&J Machinery** dealer
sticker (`01455`, Hinckley) beside the machine's own QR code. Invoice 100154 names the customer and
the items but carries no seller letterhead, so the KB has never identified who actually sold
`FA2301`, `FA2303` or `FA2304`. Recorded **`[confirm]`** — it is a sticker on a machine, not a
document — but it is the first evidence there has been. **Markfield Woodworking Machinery Ltd**, by
contrast, is fully evidenced by invoice 22473 and warrants a `Wiki/Suppliers/` article (not yet
written).

**Document Register caught up.** It held seven rows and none of the day's documents. Five added, all
`Document No.` = `pending` per §1 (the shared group register is append-only and write access is still
unconfirmed): the Printerland receipt SOA2606351, the Brother user's guide, **invoice 22473**, the
**MWM quotation**, and the **AES control-panel schematic**.

**Tasks raised or changed:** **T018** (post-move re-commissioning across all machines), **T019**
(register the compressor once its acquisition year is evidenced), **T020** (compressor service
history + F-Gas) — T019 and T020 split because they will be done by different people. **T014** rewritten
twice as evidence arrived.

*Build note: the first `FA2402` note was **silently truncated at Smartsheet's 4,000-character cell
limit**, mid-sentence, with no error returned — caught by reading the API response back rather than
trusting the success code, and rewritten more compactly. Worth remembering: Smartsheet does not tell
you it has cut your text.*

### `CLAUDE.md` v11 — the charter catches up

Written at the end of the day, deliberately after the flow of documents settled rather than chasing
each one. **v10 (`1l4lgxmy5LJNdQQnTPIVVSC0YbY7mbcf4`) archived; v11 live at
`1edazoWoadKnX-pz2vy-bEE0lCCOd1Gga`.** What it takes on:

- **§0** — the billing pattern was scoped to `FA2301`–`FA2305`; it now names `FA2402` and the
  SmartCABINET software too, and records that `FA2401` names no company at all.
- **§1** — `FA2402` added to the live-sources list and to *Assigned so far*; `FA2302`/`FA2305` marked
  Sold; the label map written in; and **two new standing rules**. *Codes are never retired or reused* —
  a sold asset keeps its row and its history, because a disposal changes status, not existence.
  *Registered ≠ complete* — with the compressor as the worked example of why.
- **§3 — four new lessons**, all from things that actually happened today:
  - **A register only contains what somebody thought to put in it.** Five sessions of detailed machine
    documentation, and the machine feeding all three sat unregistered. **The gap was invisible from
    inside the KB.** Completeness is not something a knowledge base can check about itself.
  - **A model name is not a specification.** `STK 10000` was labelled as an unsourced reading for days
    before the quotation confirmed it. *Label the inference, not just the conclusion.*
  - **What a document excludes can matter more than what it states** — the AES quotation's exclusion
    clauses moved an entire installation into the undocumented column.
  - **Trust the API's response, not its status code** — the silent 4,000-character truncation.
  - The existing "don't assume one finding resolves another" lesson was **closed rather than deleted**:
    the answer to "did `FA2305` supersede `FA2302`?" was *neither*, and the restraint is recorded as
    having paid off.
- **§6b** — the AnyDesk/PuTTY binaries and the uncopied banking details joined the SIP credential
  incident, so all three of the day's security events sit in one place.
- **§7** — Unit 30's postcode confirmed and its `[confirm]` dropped; `FA2402` and the unregistered
  compressor written up in full; T014 rewritten around the installation question; T018/T019/T020 and
  the supplier question added; the re-commissioning question marked **partly** answered.
- **The inventory question was rewritten from soft to hard.** It used to read "not necessarily
  complete". It now reads: the register is *known* to be missing at least one machine class, and
  nothing inside the KB can say whether it is missing others.

### Four Wiki articles written — the documentation debt cleared

The whole day's work had gone into Smartsheet and the control files; **not one Wiki article had been
created or changed.** Four were owed, and all four are now written:

| Article | Covers |
|---|---|
| `Wiki/Machinery/aes-saf-10000-stk-extractor.md` | `FA2402` — the full sourced specification, and the installation nobody documented |
| `Wiki/Machinery/brother-td-4420dn-label-printer.md` | `FA2401` — suitability, the ZPL contradiction, the four-party billing trail |
| `Wiki/Suppliers/markfield-woodworking-machinery.md` | The first supplier in this KB evidenced by a purchase rather than a manual |
| `Wiki/Processes/barcode-and-scan-event-system.md` | Phase 0 as built, and what each later phase is waiting on |

`Wiki/index.md` updated with all four; the predecessor is archived.

**Three things worth noting about how they were written:**

- **The AES article leads with what the KB does *not* have.** For the three production machines
  there are full manufacturer's manuals. For `FA2402` there is a quotation, an invoice and a
  control-panel drawing — commercial documents, not engineering ones. The article says so in its
  second paragraph rather than letting a confident-looking specification table imply otherwise, and
  the arithmetic comparing rated capacity against demand is labelled as *mine*, not a manufacturer's.
- **The barcode article records the settled design decisions explicitly**, under a heading that says
  not to re-litigate them: 2D over Code 128 and why, the three-level `Order → Unit → Part` scheme,
  the append-only design forced by Smartsheet forms being unable to update rows, and the four
  Smartsheet API constraints found the hard way. A design written down only as a conclusion gets
  re-argued; written down with its reasoning, it holds.
- **The Markfield article ends by warning against a merge.** The R&J Machinery sticker on the Vitap
  is a *different* lead about a *different* supplier, and the two are easy to conflate now that one
  of them finally has a name. Recorded as "do not merge the two leads".

**One convention gap found and not silently fixed:** the article template says `related:` links
should be kept bidirectional. The new articles link out to the three machinery articles; those three
do not link back (`hebrock-f4-next-edge-bander.md` carries `related: []`). Rewriting three large
articles for a metadata field was judged not worth it today — flagged here so it is a known debt
rather than a surprise.

## Governance

Owner-directed work inside this KB only. No outward action; no purchase committed (scanner and label
stock specified for the owner to quote and buy, per §6a); no other KB written to — the Construction KB
was **read and cited**, never edited. Nothing appended to the shared group Document Register — write
access is still unconfirmed, so all five new document rows carry `Document No.` = `pending` (§1).

**Three credential/security events, none of them recorded in the KB:**

1. A supplier support ticket containing **live SIP trunk credentials** was shown in a screenshot.
   Refused to record it anywhere, advised the owner to have the password rotated, and deleted the
   local image on the owner's instruction — while saying plainly that deleting a copy does not
   un-expose a credential that has already been shown. Logged in `CLAUDE.md` §6b as an access-review
   event, without the credential.
2. **`AnyDesk.exe` and `putty-64bit-0.85-installer.msi` were sitting in `Raw/`** — a remote-access
   client and an SSH client in a document inbox. Flagged neutrally to the owner and **never opened,
   run or moved**; the owner has since removed them, confirmed by a folder listing.
3. **Banking details (HSBC sort code and account number) on the MWM quotation were deliberately not
   copied** into the register, the Document Register or this log. Noted in the `FA2402` register note
   so the omission reads as a decision rather than an oversight.

**The ElmoDrive remote-maintenance access code** was removed from the F45 article before the Wiki
mirror was pushed to git (§6a, never hold a secret) — it is printed in the published manual, but it
still logs a technician into the saw.

## Still open at session end

- **Which SmartCabinet version is installed**; what its label designer can place in a barcode field.
- **The shared Google Drive job folder** — not yet identified or examined (may hold CRM/customer data:
  cite, never copy).
- **The ZPL test** on the TD-4420DN.
- Does SmartCABINET's ERP already track production?
- **The Brother TD-4420DN's actual invoice** (as opposed to the order receipt) has not been seen.
  *Resolved during the session:* the printer is at Unit 31 and is now registered as `FA2401`.
- **What the asset labels' QR codes decode to.** *Which label goes on which machine is now answered*
  (`0017`-`0021` mapped above), but the QR payload is still unknown and **Phase 1 cannot start until
  it is**: a scanner needs to know what it will receive.
- **Were the machines re-commissioned after the move to Unit 31?** The single biggest open item to
  come out of this session (Task T018). See the per-machine lists above. *The owner has confirmed the
  machines are "up and running"* — which answers whether they work, **not** whether the manuals' own
  post-installation checks were carried out (the F45 alone calls for a levelled floor, swing-arm and
  table-height settings, an angle-cut test cut under 0.2 mm, and an electrician on rotation
  direction). Recorded as partially answered rather than closed.
- **Installed extraction performance** — `FA2402` is rated 10,000 m³/h, but the vendor supplied no
  ducting, no cabling and no on-site connection, and nothing records what was installed. One
  anemometer reading per machine closes this and the extraction half of T018 (Task T014).
- **A real AES operating manual** — until one arrives `FA2402` cannot join the Maintenance Schedule
  or the Fault Log, whatever else is known about it.
- **The ABAC compressor's purchase paperwork** — needed before a code can be assigned (T019); its
  service history and F-Gas position are open too (T020). **Its gauge read 5.4 bar against machines
  asking 6-8 bar**, which wants checking on its own account.
- **Disposal dates and sale proceeds for both Inventairs** (`FA2302`, `FA2305`) — both carry a
  purchase price on the register, so the disposals have a book consequence.
- **`FA2401` has no asset label applied** — it is now the only registered asset without a physical
  tag. *(Its Wiki article, and `FA2402`'s, were written later the same day.)*
- **`Wiki/Suppliers/` entry still owed for R&J Machinery**, once the dealer sticker on the Vitap is
  confirmed against a document. *(Markfield's was written later the same day.)*
- **`related:` links are not bidirectional** — the new articles point at the three machinery
  articles, which do not point back.
- ~~**Unit 30's postcode**~~ — **answered by the owner: NE28 6HA**, the same postcode as Unit 31.
  Owed to `CLAUDE.md` §7, which still carries a `[confirm]` marker against it.
- **The Unit 31 lease body** — only the cover page has been seen. Alterations, repair/reinstatement
  and nuisance clauses bear on extraction ducting, three-phase runs and fixing machines to the slab.
  The lease belongs in the AMFA KB, not this one.
- **Who holds labels `0001`-`0016`**, and where that list lives - group-level, so not this KB's to own.
