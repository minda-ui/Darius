# CLAUDE-Workshop.md — Workshop of Furniture Making Knowledge Base

**Part of Darius's charter. See `CLAUDE.md` for the core and the file map.**

**This file holds the live workshop snapshot and the open questions.** It is separate because it changes more often than anything else in the charter — split at **v31** (2026-09-23) so an
ordinary change re-emits this file rather than all 86,856 bytes of the old monolith
(`AWT-0082`; Drive has no patch API, so every edit is a whole-file rewrite).

*Sections keep their original numbers (§7) so every existing citation still resolves.*

## 7. Workshop snapshot and open questions

**Location:** **Unit 31, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA** — the
workshop. **Unit 30** on the same estate is office and warehouse — **also NE28 6HA** (owner, 2026-09-17;
the `[confirm]` that stood against this is discharged). **Unit 32 is no longer held**; everything in this
KB dated before 2026-09-17 that says Unit 32 was wrong or is historic.

Evidenced by the lease cover page: **Forth England Limited** (landlord) and **Furniture by Fishbone
Limited** (tenant), **dated 25 June 2026**. *Furniture by Fishbone Limited is this company's former name —
Companies House confirms it renamed to **AMFA Furniture Ltd** on 13 July 2026, three weeks after the lease
was signed (Fishbone Construction KB, `Wiki/Suppliers/amfa-furniture-ltd.md`, CH overview `FH0000019`).*
Same company, not a new one. **Unit 31's previous occupant was Fishbone Waste**, who have moved out — which
is why the 2024 Brother order receipt shows "Fishbone Waste, Unit 31" for what is now the workshop's address.

**The lease itself is not this KB's to hold** — §1 deliberately has no `Properties`/`Contracts` folders. It
belongs in the AMFA Furniture Ltd KB, along with **Forth England Limited** as a Suppliers entry. Flagged for
the owner/Victoria; only the cover page has been seen.

**Machines registered:**
- `FA2301` — Hebrock F4 edge banding machine, Serial F3809. CE-compliant. Corner-rounding fault
  (stop-screw misadjustment) resolved (FL-001). Maintenance schedule (MT-001…014) + troubleshooting
  reference built. See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`.
- `FA2302` — Inventair MK1 MTFA dust/fume extractor. **Sold** (owner, 2026-09-17). Never had a manual;
  never joined the maintenance system. **Disposal date and sale proceeds unknown** — it carries a
  purchase price, so the disposal has a book consequence.
- `FA2303` — Altendorf F45 ElmoDrive CNC sliding-table saw. **Serial `23-11-12-005`, confirmed from the
  type plate 2026-09-18 (T009 closed)** — the same number the KB had carried since Session 6 as "an
  internal job number"; the plate also gives 2023, 8,293 kVA, 13,34 A, blade 300–450 mm at 2000–5000 rpm,
  and carries the **DGUV marks HM 220024 (GS) and HM 220025 (wood dust)** physically on the machine.
  **Safety certificates expired 22.02.2024 — unresolved compliance gap, Task T007.** Mandatory monthly
  documented safety check required (Task T008, not yet performed); the schematics now give **device tags**
  for it, including **three** emergency stops and a **reduced 50 mm safety zone at the rip fence** the KB
  had no record of. **The machine provides volt-free terminals to start an external extractor** (max
  240 VAC, 1 A) — capability confirmed, wiring unverified (T018). Maintenance schedule (MT-020…028) +
  troubleshooting reference built. See `Wiki/Machinery/altendorf-f45-panel-saw.md`,
  `Wiki/Processes/f45-monthly-safety-device-check.md` and
  `Wiki/Processes/f45-electrical-schematics-reference.md`.
- `FA2304` — Vitap K2-2.0 CNC boring/drilling/routing centre. **Serial `320070 AT` and year 2023
  confirmed from the type plate 2026-09-18 (T012 closed)** — identical to the invoice-derived value the
  manual could not corroborate. The plate also gives 415 V, 19,3 A and **1385 kg**, which **disagrees
  with the 1030 kg this KB carried from the manual** (355 kg apart; floor loading and levelling both
  scale with it, so prefer the plate until someone reconciles them — recorded, not resolved).
  **Open incident:**
  TpaCAD "Tool for this working not found" on Blind bore drill operations — root cause refined (fix
  likely lives in the operation's own Tool [T] field referencing a real CN Tools catalog entry, not
  the outfit's per-bush ID), not yet tested end-to-end (Task T016). Maintenance schedule (MT-030…036)
  + troubleshooting reference built. See `Wiki/Machinery/vitap-k2-panel-saw.md`,
  `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`.
- `FA2305` — Inventair MK2 MTFA dust/fume extractor, bought alongside `FA2304` on invoice 100154.
  **Sold** (owner, 2026-09-17). The promised manual never arrived and now never will. **Disposal date
  and sale proceeds unknown**, same book consequence as `FA2302`. *The long-running question of whether
  `FA2305` superseded `FA2302` is answered: neither did.* Both were sold and replaced by a single
  centralised unit, `FA2402`, that this KB had never heard of. The suspicion had been recorded as
  unconfirmed rather than asserted, so nothing had to be unpicked — see §3.
- `FA2401` — Brother TD-4420DN direct-thermal label printer, bought 09/05/2024 (Printerland order receipt
  SOA2606351, £211.58 ex VAT). Registered 2026-09-17. **Billing trail unresolved and recorded as such:** no
  company is named on the billing line — it is in the owner's name at the companies' registered office — and
  it shipped to Fishbone Waste at Unit 31, then a different occupant. **ZPL emulation unverified** (resellers
  claim it, Brother's own manual for this model never mentions it); direct thermal fades, so it suits
  short-life part labels, not asset or offcut labels. **No asset label applied yet.** See
  `Wiki/Machinery/brother-td-4420dn-label-printer.md`.
- `FA2402` — **AES SAF 10,000 STK fine dust extractor** (centralised, three-phase), serial **A-077**.
  Invoice **22473**, **08/10/2024**, **Markfield Woodworking Machinery Ltd**, £6,350 net / £7,620 inc
  VAT, paid in full. Asset label **`0019`**. Registered 2026-09-17, acquisition year evidenced before
  the code was assigned. **Specification sourced from the vendor's quotation of 02/10/2024** (six days
  before the invoice, identical figures), and **the type plate photographed 2026-09-18 states `DUST
  CAPACITY 10.000 M³/H` as its own field**, which fully discharges the old *"10000 is a reading of the
  model name"* caveat; the plate also confirms serial `A-077`, production year 2024, and names the maker
  **AES ELEKTRİK MAKİNA SAN. VE TİC. A.Ş.** (settling the two renderings), but gives **740 kg against the
  quotation's 720 kg** — recorded, not resolved: **10,000 m³/h**; 11 kW / 15 HP direct drive, star-delta; **355
  mm** suction; **64 filters at Ø160 × 940 mm, 30.22 m²**; three waste buckets; 720 kg; a Part Holder
  stopping parts over 25 × 25 mm reaching the propeller. **What the vendor did *not* supply is the
  important part** — *"not supplied with electrical cabling, extraction hose or blades"* and *"we do not
  electrically connect machinery on-site"* — so the ductwork and electrics were the group's own work and
  **nothing about that installation is recorded** (Task T014). *"Dust absorption rate 40 m/min"* is
  recorded verbatim and **unreconciled**: it matches neither the inlet velocity nor the filter face
  velocity, and is not to be used until a vendor or a real manual explains it. **Still no operating
  manual**, so it cannot join the Maintenance Schedule or Fault Log. Billed to Fishbone Drylining Ltd and
  **delivered to Unit 31 in October 2024 — nearly two years before AMFA's Unit 31 lease** (T004). See
  `Wiki/Machinery/aes-saf-10000-stk-extractor.md` and
  `Wiki/Suppliers/markfield-woodworking-machinery.md`.
- `FA2306` — **ABAC GENESIS rotary screw air compressor** with integrated refrigerant dryer. Asset label
  **`0017`**; serial **ITJ717909**; product **4152025548**; plate year 2023; 455 kg; **15 kW
  three-phase** (the proforma also says 20 HP), 0.58 kW dryer; **74 CFM**; max **10 bar**; refrigerant
  **R513A 0.5 kg = 316 kg CO₂e**. **It feeds the pneumatics of `FA2301`, `FA2303` and `FA2304`** and is
  therefore a single point of failure for the whole workshop. **Found on the floor 2026-09-17, on a
  label but not on the register; registered 2026-09-18** from **proforma invoice 208027**, Pneumatic
  Tools & Compressors Ltd (Long Eaton, Nottingham), **14/11/2023**, **£9,696.00 net / £11,635.20 inc
  VAT**, billed to Fishbone Drylining Ltd. **Delivered to Unit 32**, with the three machines it feeds —
  *not* Unit 31, although the proforma prints "delivery as per inv address" against a Unit 31 address;
  that is the billing address, and the owner corrected the point on 2026-09-18 (see the v15 note in `Outputs/charter-version-history.md`).
  **Two model designations, not
  reconciled:** the plate reads `GENESIS 15 500L`, the proforma reads `GENESIS C67` — the *product
  number* is identical on both and is what identifies the machine; every figure agrees, only the string
  differs. **The document is a proforma, not an invoice** (*"THIS IS NOT A VAT RECEIPT"*), so it
  evidences the order, not payment or delivery; 2023 is safe because its 30-day validity closes
  14/12/2023 and the other five machines were invoiced five days earlier. **The VAT invoice is still
  wanted.** Two live items: the service log on its own yellow label is **blank** (Task T020), and the
  **air receiver's pressure-system position is unestablished** (Task T021). **The 5.4 bar gauge reading
  is not a concern and never was** — the compressor was switched off when photographed (owner,
  2026-09-17), so that was residual receiver pressure, not line pressure; *v11 and v12 of this file
  presented it as a finding, which was wrong (see the v13 note in `Outputs/charter-version-history.md`)*. The plate rates 10 bar against a
  highest stated demand of 8 bar, so the compressor is not the limitation; what each machine receives
  under load is simply unmeasured — routine verification, **not** the follow-up to a suspected fault.
  F-Gas: 0.32 tonnes CO₂e is far below the 5-tonne leak-check threshold, so charge size triggers no
  periodic leak checking. **No operating manual**, so it is not yet on the Maintenance Schedule. See
  `Wiki/Machinery/abac-genesis-screw-air-compressor.md` and
  `Wiki/Suppliers/pneumatic-tools-and-compressors.md`.

**Operational systems (built 2026-09-15):**
- **Maintenance** — `Wiki/Processes/machinery-maintenance-system.md` + the Maintenance Schedule sheet
  (30 tasks: FA2301 MT-001…014, FA2303 MT-020…028, FA2304 MT-030…036) + three per-machine schedule
  articles.
- **Troubleshooting** — `Wiki/Troubleshooting/troubleshooting-and-fault-log-system.md` + the Fault Log
  sheet (FL-001 = resolved Hebrock corner-rounding fault) + three per-machine references (Hebrock
  §8.2; F45 mechanical + ElmoDrive error codes; Vitap §7.8).
- **SmartCabinet & production workflow** — `Wiki/Software/smartcabinet-and-production-workflow.md`
  (**draft**): the order-to-delivery process from the BP-scheme map, and how SmartCabinet (design +
  3D visuals + CRM) drives the machines. Product specifics flagged `[confirm]`. **This is the seed for
  Darius's first job — the design→production→Sales processes + tracker.**
- **SmartCabinet CAD reference** — `Wiki/Processes/smartcabinet-wall-support-cam-table-reference.md`:
  how to add hardware to SmartCabinet's Wall Support library, full column reference, two worked
  examples that exposed the X-sign discrepancy (Task T017).
- **Kitchen unit library (started 2026-09-18)** — `Wiki/Software/kitchen-unit-library.md`
  (**draft, nothing built**): the `AMFA Wall Unit 600 RH` master read out of its own files, the derived
  nominal, the three-unit comparison, the depth chain behind the 255 mm shelf, and a folder/unit-code
  convention **proposed for approval, not created**. The owner's Drive `Furniture` folder was listed but
  **not reorganised**, and the two `ANVAR_KITCHEN_*` folders were **not opened** — a customer name on a
  folder is enough to treat it as client data.
- **The production route (recorded 2026-09-19)** — `Wiki/Processes/panel-production-route.md`: the
  order parts actually move through the shop, **SmartCABINET optimisation → panel cutting list → F45 cut
  → F4 edging → Vitap drill → assembly desk**, with the finished-size/trim-then-tape answer and the
  serial-line argument (no second saw, bander or borer, so any one stoppage stops the shop — and all
  three are fed by `FA2306`). *Five sessions documented three machines without recording the order they
  are used in;* the gap was invisible from inside the KB, exactly like the unregistered compressor.
- **Carcase fixings** — `Wiki/Processes/carcase-fixings-cabineo-x-vs-confirmat.md`: **Cabineo X decided
  and ordered** (owner, 2026-09-19), confirmat retained as **Plan B and held in stock**. Records what the
  choice costs (**+£6.72 a unit, +£80.67 a twelve-unit kitchen** at UK retail listings, which still want
  a trade quote at 2,000) and why the master needs no re-drawing.
- **Making holes with a cutter** — `Wiki/Processes/tpacad-interpolated-holes.md`: **toolpath circle Ø =
  hole Ø − cutter Ø**, written for a live job with the 10 mm and 12 mm drills on order. Also the
  cheapest case in which to settle the unresolved `Diameter`-field convention, because a wrong reading
  gives 22 mm rather than 12 — unmistakable on scrap.
- **Closing T016 (2026-09-19)** — `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`: the two-step fix
  at the **Vitap**, the verification test on `03-BOTTOM.TCN`, why the Through-bore workaround must not
  be used to close it, and **the correction to what T016 was said to be** — see the T016 bullet below
  and the v21 note in `Outputs/charter-version-history.md`.
- **Barcode system, Phase 0 (2026-09-17)** — the **Scan Events** sheet (`4828191892047748`) and the
  Machinery Register's `Asset Label No.` column, documented in
  `Wiki/Processes/barcode-and-scan-event-system.md`. Phases 1–4 (part labels, stage tracking, the
  offcut library, Vitap program selection) are designed but not built; the sheet is still empty.

**Open questions / tasks:**
- **SmartCabinet product specifics** — *partly resolved 2026-09-17.* **Vendor and product confirmed:**
  **SmartCABINET**, by **Kosmosoft Engineering S.r.l.** (Bagnolo San Vito, Italy), described as
  "CRM/CAD/CAM/ERP software for cabinet making"; offer/contract **22910**, 10/09/2026, **€1,000, paid**,
  registered `FCD0000024` in the *Construction* Document Register — **billed to Fishbone Drylining Ltd,
  not AMFA Furniture Ltd**, the same pattern as every machine (evidence for Task T004). Cited from the
  Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md` — not duplicated here, and that
  KB is read-only to this one. **Outputs confirmed** from the release notes and the owner's screens:
  `.TCN` post (Vitap), custom CSV export splittable by material, real-shape nesting, ZPL barcode label
  printing, Panel Optimization with an offcut/cutout library. **Still `[confirm]`:** which version is
  actually *installed* (release notes list 3.2.0.9 of 07/07/2026 as newest released); whether the
  Hebrock gets any file at all; where CRM/customer data lives (cite, never copy client data).
- **SmartCabinet Wall Support hardware X-sign discrepancy** — two items both "measured from the back
  edge" needed opposite X signs (−15 vs +5); needs visual confirmation in SmartCabinet's own preview
  on a real job (Task T017).
- **TpaCAD Blind-bore-drill tool-ambiguity fix** refined but not fully tested — likely needs a real CN
  Tools "Dia. 5mm" entry created on the SmartCabinet computer, exported and transferred, then
  referenced in the failing operation's Tool [T] field (Task T016) — *the manual now supports this: the
  setup's `Tool type` "is automatically assigned by selecting the tool", and on `HOLE` an explicit `Tool`
  "prevails over the programming per diameter" with `Tool type` driving "a validity check of the tool".*
  **TpaCAD complete manual / `Workings.pdf`** not yet obtained — at `Albatros\Help\` on the shop's
  Albatros PC (Task T015), and **no longer housekeeping**: it holds the compensation semantics, the
  entry/exit segments and the `THREE HOLES HINGE` parameter table, three of which were needed on
  2026-09-18 to answer a live 35 mm hinge-cup question and could not be. *The extract we hold gives the
  right working — `CIRCULAR INTERNAL WINDOW`, "a circle with internal emptying", under `CUSTOM WORKINGS:
  PROFILES` — but never says whether its `Diameter` is the finished hole or the tool path, which on a
  12 mm cutter is 35 mm versus 47 mm. Settle it with a test cut in scrap* — **cheapest as a Ø12 hole from
  the 10 mm cutter, where a wrong reading gives 22 mm rather than a ruined door.**
  **A correction that belongs here:** this KB briefly recorded that the shop appeared to lack a 35 mm
  hinge-cup bit. **It has one, fitted to the Vitap** (owner, 2026-09-19); what is open is **what went
  wrong with it** (Task T027), and T016 is the obvious candidate — the door programs each cup as a Ø35
  bore with no tool assigned — but that is **not asserted**. *Asking how to do something another way is
  not evidence the ordinary way is unavailable.*
- **Were the machines re-commissioned after the move to Unit 31?** The KB holds no record that a move
  happened at all, yet the lease is dated 25 June 2026. The F45's own manual requires, after installation:
  a flat, level, load-bearing floor (~1100 kg, centre of gravity ~100 mm below the blade axis); swing-arm
  check (0.5 mm); sub-rollers; main-table height (0.1–0.2 mm); cross-slide height; free-cut both sides;
  angle-cut calibration by test cut (**< 0.2 mm**); an electrician to verify motor rotation direction; and
  extraction interlocked to machine power. Extraction also needs **≥ 20 m/s** through the ø140 mm connection,
  and new duct runs change the velocity actually achieved — which bears on the extraction-sizing question
  below. **Not assumed skipped; simply unrecorded.** *The owner has confirmed the machines are "up and
  running"* — which answers whether they work, **not** whether these checks were carried out. Recorded as
  partly answered, not closed (Task T018): "it runs" is not "it was commissioned", and treating one as the
  other is the inference §3 keeps warning about.
- **The Unit 31 lease body has not been seen** — only the cover page. Alterations, repair/reinstatement and
  nuisance clauses all bear on the workshop (extraction ducting, three-phase runs, fixing machines to the
  slab, noise and dust). The lease belongs in the AMFA KB, but those clauses affect this patch.
- **`0191 605 2945` is printed on every group asset label — and is in a SIP trunk migration.** The ticket
  (WebMate `T02530-15072026`) lists `+441916052945` among four DDIs migrating, with a stated completion date
  of **03/08/2026 that has already passed**. If that number does not survive, every asset label points at a
  dead line. Telephony is **not** this KB's scope; this is flagged only because the labels depend on it.
- **The shared Google Drive job folder** — the dedicated folder through which SmartCabinet and the
  machines exchange files is not yet identified or examined. Its structure and naming convention
  constrain any barcode/tracking ID scheme, and it may hold customer data from SmartCABINET's CRM
  side (**cite, never copy client data**).
- **Does `FA2303` (F45) accept a digital cut list?** The ElmoDrive is a *positioning* control — rip
  fence, blade height, tilt, scorer, crosscut-fence angle, with tool management and per-axis
  calibration. Across all three F45 documents **no cut-list or job-file import is documented**, and the
  only data interface that appears is a USB drive, for firmware updates (`E21`/`E22`) and
  remote-maintenance files (`E23`). An "optimisation limit" error in the `E01`–`E15` block hints at some
  optimisation function on the control, but that block's OCR pairing was never reconstructed. **Working
  answer: the saw takes dimensions, not cut lists** — confirm against the ElmoDrive's own menus before
  recording it as fact.
- **Does SmartCABINET's own ERP module already do production tracking?** The vendor describes it as
  "CRM/CAD/CAM/ERP" (Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md`). Building a
  parallel tracker without knowing what the purchased software already does risks duplicating it.
  Owner has chosen Smartsheet as the tracking layer regardless (2026-09-17); this remains worth
  establishing so the two don't fight.
- ~~**What do the asset labels' QR codes decode to?**~~ — **answered 2026-09-18: the bare four-digit
  label number as plain text.** See §1. What now blocks barcode Phase 1 is Task **T022**: no scanner has
  been bought (a purchase, so the owner's), the Brother TD-4420DN's ZPL support is still unverified, and
  a disambiguation rule between asset labels and future part labels needs deciding.
- **Who legally owns `FA2301`–`FA2306` and `FA2402`?** All invoiced to Fishbone Drylining Limited (now
  Fishbone Construction Ltd), not AMFA Furniture Ltd (Task T004) — and so was the SmartCABINET software.
  *Sharpened 2026-09-17:* AMFA Furniture Ltd holds the Unit 31 lease, so the picture is one company's
  machines operating in another's leased premises. **`FA2402` sharpens it again**: it was delivered to
  Unit 31 in **October 2024**, nearly two years before that lease was signed, which suggests the 2026
  "move" was AMFA taking a lease on a unit the group already occupied rather than a relocation.
  **`FA2306` briefly appeared to push that back another year, and does not.** v14 read its proforma's
  Unit 31 address as a delivery address and concluded the group was using both units in November 2023;
  **the owner withdrew that on 2026-09-18 — the compressor went to Unit 32.** So the earliest evidence
  this KB holds for the group occupying Unit 31 is **2024**, not 2023. Evidence, not a conclusion — the
  lease body and the intercompany side both sit outside this KB.
- **`FA2303`'s expired safety certificates** — check with Altendorf/supplier (Task T007), and note the
  DGUV marks **HM 220024 / HM 220025 are on the machine's own plate**; **first F45 monthly safety check
  not yet logged** (Task T008, now with real device tags to name); ~~`FA2303` serial unconfirmed~~ —
  **closed 2026-09-18 from the type plate**, though **who sold it is still unknown**; **`FA2303` annual
  PTC electrician check** needs scheduling (Task T011; Maintenance Schedule MT-025) — the schematics give
  a likely measurement point at `-X3` `POT_1`/`POT_2` but **no resistance value**, and leave
  bimetal-vs-PTC unresolved.
- **Installed extraction performance (Task T014, rewritten).** The `FA2302`/`FA2305` half is closed —
  both sold, both replaced by `FA2402`. The sizing half is now a different question. `FA2402` is rated
  **10,000 m³/h**, against known demand of the Vitap's ~2000 m³/h plus roughly **1,110 m³/h** for the
  F45 — *that second figure is my own arithmetic from ≥20 m/s through ø140 mm, not a manufacturer
  number* — plus the Hebrock, whose duct diameter this KB does not hold, so its ≥25 m/s cannot be
  converted. Comfortable on paper. **But the vendor supplied no ducting, no cabling and no on-site
  connection, and the machines have since been moved**, so what each machine actually receives is
  decided by pipework nobody documented. **Closing action: an anemometer velocity reading at each
  machine's connection**, which also answers the extraction half of T018.
- **A real AES operating manual** — the quotation gives specification, the schematic gives the control
  panel; neither gives maintenance intervals, filter-change criteria, safety instructions or a fault
  table. Until one arrives `FA2402` stays outside the maintenance and troubleshooting systems. The
  consumables are known (64 filters, three buckets), so the schedule can be built the moment the
  intervals exist.
- **`FA2306`, the ABAC compressor** — *registration closed 2026-09-18 (T019); the blocking item is gone.*
  What remains: **has it ever been serviced?** Its yellow label's log table is blank and it was delivered
  in November 2023, so against a *"2,000 hours or 1 year, whichever comes first"* interval the gap is
  approaching three years — but **a blank label is not proof**, and the supplier is a compressor
  specialist and the obvious place to ask (T020). The **F-Gas** position is settled by figure and wants
  qualified confirmation (T020). **The VAT invoice** has never been seen. Delivered pressure and flow at
  each machine under load is still unmeasured and worth a reading, as routine verification. *The 5.4 bar
  gauge reading is closed: the machine was off. It was never a low-pressure finding.*
- **Does `FA2306`'s air receiver need a written scheme of examination? (Task T021.)** The plate's model
  string reads `GENESIS 15 500L`, and read plainly the "500L" is a 500 litre receiver — which at 10 bar
  would be a pressure system far above the commonly cited 250 bar-litre threshold, calling under the
  Pressure Systems Safety Regulations 2000 for a written scheme by a competent person and examination
  under it. **This KB holds no record of any such scheme or examination.** But **"500L" is a reading of a
  model name, not a specification** — neither the plate nor the proforma states a receiver volume, and the
  proforma does not mention a receiver at all — so T021 *starts* by establishing what the receiver
  actually is. One photograph of its own plate turns the whole question from inference into fact. **This
  KB does not give regulatory advice**; it records that the question is open and that absence of a record
  is not evidence of absence.
- **The kitchen unit library — four owner decisions and one remaining defect.** The decisions (T023):
  the range (types and widths), whether *"low cost"* denotes a defined carcase spec or is only a range
  name, whether hand belongs in the unit code or is mirrored at job time, and whether library units are
  separated from customer jobs on Drive. **Four of the five unit types still have no master at all** —
  only the wall unit exists. ~~Shelf depth 266 / 256 / 255 mm~~ — **answered 2026-09-19 and it was never
  a defect**: the master's **255 = 300 − 16 − 19 − 10**, a **16 mm back-panel step-back** for the Häfele
  concealed wall mount, the 19 mm back, and a **10 mm shelf-front step-back**; the earlier folders are an
  **earlier design**, and **both step-backs are specification** that belongs on every unit's spec card
  (the 16 mm is the same Häfele hanger added to the Wall Support Cam Table in the T017 session, showing
  up as a panel dimension). **Still open: two backs** (`07-BACK-1`, `07-BACK-1B`) on one blank in the
  master where neither earlier unit has a second back at all — worth re-asking now the back is known to
  sit in a void for a hanger, since a hanger usually wants the back notched, *though that is a
  suggestion, not a reading*. Also unestablished: whether SmartCABINET generates a unit's parts
  **parametrically** from a width, which would make the whole folder question smaller than it looks.
  See `Wiki/Software/kitchen-unit-library.md`.
- **`T016` is the library's remaining blocker — and the fix is at the Vitap, not on the design
  computer.** *v18–v20 of this file said the opposite and were wrong; see the v21 note in
  `Outputs/charter-version-history.md`.* **The Vitap is
  not missing a Ø5 tool: it has five.** Blind Ø5 mm sits on bushes 6–10, all at **ID 0**, so
  diameter + type resolution has five candidates and no tie-break — which is the whole fault. **Two
  steps close it**, both in TpaCAD's per-position Technology dialog and the failing program: give one
  Blind Ø5 bush a real unused ID, then set that operation's `Tool` field to it, which *"prevails over
  the programming per diameter"*. **Verify by reproducing the failure first, then re-Solving, then
  running `03-BOTTOM.TCN`** — and **not** by switching Tool type to Through bore, which clears the
  error by picking a category that happens to have one bush and silently drills with the wrong one.
  Full procedure: `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`.
  **Nothing needs buying** — that part stands: Cabineo X's published Ø15 drill is the *alternative* to
  routing and the master routes the pocket, so the Ø5 the master already drills plus a ≤Ø12 cutter
  covers it. **The missing SmartCABINET `Dia. 5mm` row is still worth adding, but it is a different
  job**: it belongs to the *systemic* fix — getting the post-processor to **emit** a Tool ID on export,
  so step two is not repeated by hand on every operation of every unit, since every hole in the master
  exports with `#1001=0`. *Whether SmartCABINET's IDs reach TpaCAD at all is unverified; the one data
  point is that position 101 is ID 1001 in both, for positions 101–104 only.*
  **Severity revised down 2026-09-19, priority unchanged:** with confirmat in stock as Plan B, and the
  connector pockets routed into the carcase's *inside* faces where an empty one is hidden, **a job is
  not stopped by T016** — only made more slowly and with a visible screw head.
- **Disposal dates and sale proceeds for `FA2302` and `FA2305`** — both carry purchase prices, so both
  disposals have a book consequence this KB cannot compute.
- **Vitap `FA2304` §6.8 safety check** — does it need a dated, logged record like the F45's, or is a
  pre-cycle functional test enough? Owner decision (Task T013); MT-036 holds the place meanwhile.
- ~~**`FA2304` serial/manufacture year**~~ — **closed 2026-09-18** (Task T012): the plate reads
  `320070 AT`, year 2023, matching the invoice exactly. It also reads **1385 kg against the manual's
  1030 kg** — that discrepancy is now the open part.
- **Who actually sold `FA2301`, `FA2303` and `FA2304`?** Invoices 100153/100154/100155 name the customer
  and the items but carry no seller letterhead. The Vitap wears an **R&J Machinery** dealer sticker
  (`01455`, Hinckley) — recorded **`[confirm]`**, because a sticker on a machine is not a document, but
  it is the first evidence there has been. **Markfield Woodworking Machinery Ltd** (`FA2402`) is by
  contrast fully evidenced and has its own `Wiki/Suppliers/` article — the first supplier entry in this
  KB derived from a purchase rather than from a manufacturer's manual.
- **Full inventory of workshop machinery — demonstrably still incomplete.** This was a soft open
  question until 2026-09-17, when a 15 kW compressor feeding all three production machines turned out
  never to have been registered. *That particular gap is now closed — it is `FA2306` — but closing it
  proves the point rather than retiring it:* **the register was missing a whole machine class, nothing
  inside the KB could tell us, and nothing inside it can tell us whether it is missing others.** Hand
  tools, extraction ductwork, **the air receiver** (now a real question of its own, T021) and the server
  rack itself have never been assessed. Closing it needs a walk round the floor, not a document (see §3).
- ~~**A read path that returns bytes would close two debts at once**~~ — **closed 2026-09-19, and the
  tool was in the connector the whole time.** `download_file_content` returns a file's stored bytes,
  base64-encoded, at every size this KB contains: **byte-identical** on a 9,602-byte article, and
  `CLAUDE.md` returned **whole at 90,475 bytes**. The re-formatting and the empty-above-82 KB behaviour
  belong to `read_file_content`, a *different* tool (§3). **What it unblocks is now work rather than
  capability** — back-filling the mirror (below), and running the §3 order check on exact bytes at any
  size. *Whoever spends the afternoon now spends it copying files, not looking for a mechanism.*
- ~~**The git mirror is partial and cannot be back-filled**~~ — **done 2026-09-19; the mirror is
  complete.** Every article that lived on Drive only was downloaded as exact bytes, decoded and
  committed, each one checked against Drive's reported size. **`Suppliers/altendorf-gmbh.md` is the
  proof**: the 2,007-byte article the v12 test rebuilt four bytes short now lands exact. **The count is
  not repeated here** (§1, §3) — run `git ls-files 'Wiki/**/*.md' | wc -l` and read the registers.
  *The debt is replaced by an upkeep rule*, not by nothing: an article written to one store and not the
  other re-opens the gap, so both stores get it in the same session. **This bullet stood for eleven
  versions and took one afternoon once the right tool was found**, which is the §3 lesson's real cost.
- ~~**`related:` front-matter links are not bidirectional.**~~ — **fixed 2026-09-19, in both stores,
  and the bullet that described it was itself wrong.** It had said the gap was the three machinery
  articles plus `hebrock-f4-next-edge-bander.md`'s empty list. **Computing the graph instead of reading
  the bullet found 15 files and 52 missing back-links.** The Wiki now holds **134 directed edges = 67
  symmetric pairs, nothing asymmetric, dangling or duplicated**, with every one of the 15 article
  **bodies hash-identical** before and after — only front matter moved. Flushed to Drive the same
  session per the upkeep rule above, each copy **verified byte-identical by download–decode–`diff`**.
  **What the bullet named were the articles somebody had noticed**, because the two 2024 assets had
  linked out to them; the other eleven were invisible from inside the KB, the same way the unregistered
  compressor was — nothing in a one-way link announces itself from the side that is missing.
  *Proposed for the owner rather than added unilaterally, and approved the same day* (*"Add that §3
  lesson at v25"*): a §3 lesson that **a description of a gap is not a measurement of it** — where a
  gap can be computed, compute it before believing the count somebody wrote down. **It is now in §3**,
  added at v25. **One consequence recorded rather than tidied:** archive-then-create gives a re-uploaded
  article a new Drive id, so the ids cited in `tpacad-blind-bore-tool-id-fix.md` and
  `carcase-fixings-cabineo-x-vs-confirmat.md` now point into `Archive/`. **They were not rewritten** —
  they resolve to exactly the bytes that were read and quoted, which is what a source citation is for;
  repointing them would make them cite bytes nobody read. **A Drive id in an article is a pointer to a
  version, not to an article.** Cite the path for the article, the id for the bytes, and say which.
- `AMF` vs `FA` property/asset-code inconsistency in AMFA's own Property Register — still just flagged.
- ~~Exact price on the Hebrock invoice unconfirmed~~ — **resolved 2026-09-15** by the 70%-balance
  cross-check confirmed on three invoices (Task T005, closed Done).
- A duplicate copy of two manuals was found outside this KB's own Drive folder tree — see §1.
