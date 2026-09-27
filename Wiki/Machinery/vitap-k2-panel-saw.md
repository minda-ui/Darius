---
title: "Vitap K2-2.0 — CNC Boring, Drilling and Routing Centre"
category: Machinery
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-17
sources:
 - ../../Raw/Vitap K2 2.0 manual part 1.pdf
 - ../../Raw/Vitap K2 2.0 manual part 2.pdf
 - ../../Raw/Vitap K2 2.0 manual part 3.pdf
 - ../../Raw/Vitap K2 2.0 manual part 4.pdf
 - ../../Raw/Invoice 100154 - 09.11.23 - OCN231185 - Balance.pdf
 - ../../Raw/TPA CAD part 1.pdf
 - ../../Raw/TPA CAD part 2.pdf
related:
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Processes/f45-monthly-safety-device-check.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Machinery/aes-saf-10000-stk-extractor.md
 - ../Processes/carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Processes/maintenance-schedule-vitap-k2.md
 - ../Processes/panel-production-route.md
 - ../Processes/tpacad-interpolated-holes.md
 - ../Software/kitchen-unit-library.md
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Troubleshooting/troubleshooting-vitap-k2.md
---

# Vitap K2-2.0 — CNC Boring, Drilling and Routing Centre

The workshop's third registered machine (asset code `FA2304`): an Italian-made CNC panel-machining
centre by VITAP S.p.A., combining boring/drilling (Euro-32 hinge/shelf-pin/dowel spacing) with
routing/grooving and optional edge-fitting heads. Bought on the same invoice as a second dust
extractor, **Inventair MK2 MTFA** (`FA2305`, see Open questions) — not the Hebrock/Altendorf
purchase, a separate order three days later.

**Four documents, one manual, a fragment.** The manual is split across 4 PDF parts in `Raw/`, one
document: doc/edition code `1.0-09/19` (Revision 1.0, September 2019). Two duplex-scan pairs, same
artefact as the Hebrock and Altendorf manuals:
- **Parts 1-2**: even-ascending + odd-descending, reconstructing printed pages **1-59** — Chapters
  1-4 (identification, technical data, transport, installation) and the start of Chapter 5.
- **Parts 3-4**: even-ascending + odd-descending, reconstructing printed pages **60-126** — the rest
  of Chapter 5, Chapter 6 (machine use, incl. the safety-device check), Chapter 7 (maintenance),
  Chapter 8 (additional instructions/decommissioning), plus a pneumatic-diagram annex.
- Together, parts 1-4 cover the full readable body of the manual (pages 1-126) with no gap between
  page 59 and page 60 (confirmed by content continuity at both joins). The manual's own Chapter 8
  "Annexes" list also references an EC Declaration of Conformity, a TPA user-interface guide and a
  spare-parts list as separate attachments — **none of those three appear in the 4 parts scanned**,
  so (unlike the Hebrock and Altendorf machines) no EC Declaration of Conformity has been located
  for this specific unit; only the manual's own facsimile/template DoC text is available (see below).

**Programming software**: this machine is programmed via **TpaCAD** (a generic CAD/CAM system,
title bar `<filename>.TCN - TpaCAD`), whose own manual (also split, 2 parts, in `Raw/`) is covered
separately in `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` — see Incidents below for why
that mattered on day one of real use.

## Key facts

| Item | Value | Source |
|---|---|---|
| Asset code | `FA2304` (2023 acquisition, fourth asset registered — `FA2301`/`FA2302`/`FA2303` came first) | — |
| Manufacturer | VITAP S.p.A. ("VITAP Costruzioni Meccaniche S.p.A." on the Declaration facsimile), Via Pisana 149, 53036 Poggibonsi (SI), Italy. Tel +39 0577/987511, vitap@vitap.it, www.vitap.it | [^1] |
| Model | K2-2.0 (OCR consistently misreads the "0" as "O": "K2-2.O") | [^1][^3] |
| Machine type | Semi-automatic CNC boring/drilling-inserting machine for panels, on Euro-32 spindle pitch (12 vertical spindles on Face 1, plus horizontal spindle pairs on Faces 3-6), extended with a pantograph milling/grooving unit and up to 3 optional aggregated tool heads (front milling, "LAMELLO" biscuit-joint system, "OVVO" connector system) — a boring **and** routing/milling combination centre, not a single-spindle drill | [^1][^3] |
| Serial number | **Not present in the manual** — the type-plate diagram (§1.6) is a blank template with no values filled in. The invoice gives **Serial No. 320070 AT** for this unit — treat the invoice, not the manual, as the source for this fact | [^1][^5] |
| Year of manufacture | Not stated in the manual (same blank type-plate issue). Acquired 2023 per invoice; manufacture year could be earlier — not assumed | [^1][^5] |
| Manual edition | `1.0-09/19` (Revision 1.0, September 2019), footer on every page | [^1] |
| EC Declaration of Conformity | **Facsimile/template only** — all identifying fields shown as placeholder text ("Xxxxxxxx"), not completed for this unit. Directives cited: Machinery 2006/42/EC, EMC 2014/30/EU, Low Voltage 2014/35/EU. Standards: EN ISO 12100:2010, EN 60204-1:2006 | [^1] |
| **Inconsistency flagged** | Manual §2.1 "Reference Standards" instead cites the *older* directive set — 2006/42/EC, 2004/108/EC (EMC), 2006/95/EC (Low Voltage) — that doesn't match the Declaration's post-2016 numbers (2014/30/EU, 2014/35/EU). Likely the manual body wasn't updated when the Declaration was revised. Same category of finding as the F45's expired-certificate flag, but here it's an internal inconsistency rather than an expiry | [^1] |
| Purchase date | 09/11/2023 (invoice 100154, "70% Balance", ref. OCN231185) — **not** the same invoice as the Hebrock/Altendorf purchase (invoice 100155/100153); this is a separate order | [^5] |
| Purchase price | **£68,000.00 full price**, confirmed by the same cross-invoice check used on the other two machines: this invoice's stated 70%-balance Net Total is exactly 70% of the sum of all listed items' full unit prices | [^5] |
| Purchased by / billed to | Fishbone Drylining Limited — same entity as `FA2301`-`FA2303`. The invoice address is **Unit 32**, which is no longer held; see Location below | [^5] |
| **Location — current** | **Unit 31**, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA. See "The 2026 move" below. | owner, 2026-09-17 |
| Location — as invoiced (2023) | Unit **32**, same estate. Retained because it is what the invoice says, not because it is where the machine is. | [^5] |
| Machine dimensions | 2940 (L) x 1710 (W) x 1900 (H) mm; net weight 1030 kg | [^1] |
| Panel capacity | Length 270/400-3000mm (or max 80kg); width 150-1250mm; thickness 3-50mm (70mm optional) | [^1] |
| Electrical | Three-phase, 220-240V/380V/415V/460V (±10%/±2%); current 36.4A/21.1A/19.3A/17.4A respectively; a separate "15A, 6.4kW" figure also appears for an unstated reference voltage | [^1] |
| Pneumatic | Line pressure must stay between 0.6-0.8 MPa (6-8 atm); max consumption 750 NLt/min | [^1][^3] |
| Suction | Two ø120mm + one ø50mm spiral tubes, flow rate ≈2000 m³/hour | [^1] |
| Control | 19" monitor, Windows PC, "TPA Albatros" software with optimiser (programmed via **TpaCAD**, run via **WSC**), remote diagnostics | [^1][^6] |
| Standing dust-extraction question | This machine's own suction spec (≈2000 m³/h) is far larger than the Hebrock's or the F45's (1110-1150 m³/h). Whether the newly-registered `FA2305` (Inventair MK2 MTFA) or the "one centralised extraction unit" the owner mentioned is sized to serve this machine is **not established here** — see Open questions | [^1] |

## The 2026 move — and what it implies

**The workshop moved from Unit 32 to Unit 31.** The lease for Unit 31 (Forth England Limited to
Furniture by Fishbone Limited, the company's name before it became AMFA Furniture Ltd on 13 July
2026) is **dated 25 June 2026**. The lease date is not necessarily the date the machines were
physically moved, and no record of the move itself exists anywhere in this KB.

**This machine's manual is unusually specific about what installation requires**, so a move
re-triggers all of it (§4, Chapter 4):

- Sheltered industrial environment, non-explosive atmosphere, **≥500 lux** lighting, a **level,
  vibration-free floor**, and **≥1000 mm clearance** all round for operator access and maintenance.
- **Levelling** via the threaded feet against a spirit level on the work surface; the auxiliary
  floor screws locked without forcing; no cables or hoses pinched.
- **Electrical** by a qualified electrician: verify the nameplate matches the supply, and verify
  **spindle rotation direction** against the marked arrow — swap two of the three phases if reversed.
  At 1030 kg and 2940 mm long this is not a machine that gets nudged into place and switched on.
- **Suction reconnection**, then **run the drilling unit through its full stroke** to confirm the
  hose does not foul on moving parts. The machine wants ≈2000 m³/h; new duct runs change what is
  actually delivered.
- **Axes reset** at first start-up (§5.5): MACHINE RESET → AUTOMATIC → the operating unit parks
  itself right before the program list becomes available.

**Whether any of this was redone after the move is not recorded** — see Open questions. It is not
assumed to have been skipped.

## Installation and setup

- **Site**: sheltered industrial/craft environment, non-explosive atmosphere, ≥500 lux lighting,
  level vibration-free floor, ≥1000mm clearance around the machine for operator access and
  maintenance, customer responsible for site compliance [^1]
- **Transport**: three package types (closed case, cage, open platform); lift only by forklift or
  crane at marked points; unpack by removing cover → side walls → wrap; inspect for shipping damage
  and contact VITAP immediately if found [^1]
- **Unpacked storage** (if not installed immediately): 0-40°C, RH ≤80%, protect unpainted parts with
  antioxidant oil, **repeat these protective measures every 6 months** for as long as the machine
  sits uninstalled [^1]
- **Positioning**: level via the threaded feet and a spirit level on the work surface; lock the
  auxiliary floor screws without forcing; check no cables/hoses are pinched [^1]
- **Electrical connection**: qualified electrician only; verify nameplate matches supply; verify
  spindle rotation direction against the marked arrow, swap two of the three phases if reversed;
  all supplies connected and all guards closed before first power-on [^1]
- **Suction connection**: down-conductor at ≥3m height if possible; run the drilling unit through
  its full stroke afterward to confirm the hose doesn't foul on moving parts [^1]
- **First start-up**: performed by a qualified manufacturer technician or trained customer
  personnel; only VITAP-authorized control devices may be added [^1]
- **Tool/head setup** (§5.3, spanning parts 1-2 into parts 3-4): a family of door-interlocked
  procedures for vertical/horizontal drilling tools, the channel/groove tool, the pantograph milling
  cutter (loaded from the tool magazine or directly at the pantograph), and the three optional
  aggregated heads (front-milling, LAMELLO, OVVO) — each requires opening the relevant interlocked
  door (kills power/air automatically), physically swapping the tool, then an alignment/parallelism
  check (§5.3.4.4) specifically for aggregated heads whenever they're loaded into the pantograph [^1][^3]
- **Axes reset at first start-up** (§5.5): press MACHINE RESET → switch to AUTOMATIC → the operating
  unit parks itself on the right side before the program list becomes available [^3]

## Safety

- **Operator categories** (§1.9.2): A = Operator (guards fitted); B = Supervisor (may work with
  guards inhibited under special conditions); C = mechanical maintenance technician; D = electrical
  maintenance technician; extraordinary mechanical maintenance is VITAP-technician-only [^1]
- **E-stop**: red mushroom-head button(s), mechanically locked against accidental reset; disables
  motors and power; reset sequence — unload product by hand if needed, reset the button, MACHINE
  RESET, START CYCLE [^1][^3]
- **Interlocked doors**: front door "19" and side door "22" both cut electrical + pneumatic supply
  the instant they're opened, restored only on closing plus a reset [^1][^3]
- **Fixed guards** (no interlock, always installed) must never be operated with removed — power AND
  the pneumatic inlet valve must both be isolated first for any maintenance behind them [^1][^3]
- **Lockout/tagout**: disconnector to O, padlocked with the dedicated key, before opening any
  electrical panel door; wait ≥10 minutes afterward for residual energy to dissipate [^1][^3]
- **Residual risks** (§1.13): wait ≥10 sec after opening an interlocked guard mid-cycle before
  reaching in (let pneumatics fully stop); always press E-stop before working on the machine even
  if it looks stopped (a "standby stop" can restart on its own); **commissioning is explicitly made
  conditional on installing extra protection at the conveyor interface** to remove an upper-limb
  crushing hazard [^1]
- **§6.8 SAFETY DEVICE EFFICIENCY CHECK — read carefully, this does NOT match the F45's pattern.**
  Before every activation of automatic mode, the manual requires testing: (1) every E-stop button
  stops the machine and shows the interface message; (2) each interlocked guard door does the same
  when opened; (3) any fitted safety-light-barrier does the same when breached. **Unlike the
  Altendorf F45's monthly check** (`Wiki/Processes/f45-monthly-safety-device-check.md`), this text
  reads as a mandatory *functional test before automatic mode*, not an explicitly documented,
  dated, logged inspection — no interval, no "record this" instruction, and no reference to a log
  or form appears anywhere in parts 3-4. Not assuming equivalence to the F45's requirement; flagged
  as an open question below rather than logged in the Smartsheet Safety Check Log used for the F45 [^3]
- **After any maintenance**: §6.8 must be re-run before restarting (§7.4) [^3]
- **Emergency procedures** (§6.14/6.15): operator injury — E-stop, disconnect power and pneumatics,
  alert the safety manager, first aid; machine lockout — same disconnection steps, alert maintenance
  manager. Fire (§8.2): electrical fires — CO2 extinguisher only; other fires — ABC/nitrogen powder [^3]
- **Dismantling** (§8.1.1): single-operator lift limit 25kg; qualified personnel with PPE per the
  removal risk; care not to unbalance the machine during disassembly [^3]

## Maintenance schedule

| Interval | Task | Source |
|---|---|---|
| Every 200 hours | Lubricate the spindle-holder head and channel head (MOLYGUARD GS ARTIC grease) via the drain-nipple procedure in §7.2.5.1 | [^3] |
| Every 200 hours | Lubricate all ball-recirculating units (VANGUARD LIKO EPO grease) — operating unit, clamps/mobile shoulder, pressers, tool magazine | [^3] |
| Every 100 hours | Grease each fitted optional aggregated head (front-milling/LAMELLO/OVVO), ~3g per head | [^3] |
| At least every 500 hours | Full pneumatic-system check: wiring/tubing for leaks, quick-drain valves, regulator calibration | [^3] |
| Every time a tool/drive/sensor is replaced or removed | Unscheduled inspection (§7.3.2) — no fixed interval, triggered by the event | [^3] |
| No fixed interval (routine) | General cleaning (exterior, sawdust from rollers/guides/axes), operator-interface cleaning, fan-filter and pneumatic-filter checks | [^3] |
| Before every automatic-mode activation, and after any maintenance | Safety-device efficiency check, §6.8 (see Safety above — not confirmed to require a written log) | [^3] |

No daily/weekly interval table exists in this manual the way the Hebrock's did — everything above
is either hours-based or event-triggered.

## Fault diagnosis

From §7.8 TROUBLESHOOTING (OCR quality imperfect on this page, transcribed as faithfully as possible):

| Problem | Likely cause | Solution |
|---|---|---|
| Faulty drilling machining | Worn drill bit | Replace per §5.3 |
| Faulty drilling machining | Unsuitable drill bit type | Replace with spade bit |
| Faulty drilling machining | Wrong feed speed | Decrease drill-bit feed speed |
| Inadequate line voltage | Supply doesn't match machine rating | Contact assistance service |
| Pedal doesn't respond | Faulty pedal or wrong connection | Check, then contact assistance service |
| Spindles rotate the wrong way | Inverted phases | Swap two phases in the line connector |
| Spindles don't turn | Burnt fuse / gear breakage | Check motor fuses; contact assistance service |
| Machine won't start / start button inactive | An emergency device is active | Check E-stop, side-door limit switch, left/right limit switches |
| Pressers don't hold the piece | Insufficient air pressure | Check pneumatic system pressure |
| Panel damaged in the clamp pick-up area | Excessive clamp pressure | Adjust per §5.3.6 |

No row addresses hole-position accuracy or edge tear-out directly. §7.6 "Time-out failure" is a
separate procedure (not a table) for a sensor-monitored move that doesn't complete in time: switch
off, open the guard door, check the flagged sensor and its wiring, check for obstructions, restart. [^4]

Note the third row from the bottom: **"Spindles rotate the wrong way — inverted phases."** That is
precisely the failure mode a machine move can introduce, which is why phase direction is on the
re-commissioning list above.

## Incidents

### 2026-09-15 — TpaCAD "Tool for this working not found" on Blind bore drill operations (open)

While programming the first real kitchen job on this machine (SmartCabinet export, `.TCN` files),
optimizing a program with a hole/fitting operation set to Tool type = "Blind bore drill" failed to
Solve with "Tool for this working not found," on two different diameters (3mm and 5mm). Root-caused
to a genuine ambiguity: the affected diameters each had the Blind-type tool assigned to *multiple*
spindle positions in the outfit (e.g. 5 bushes for Ø5mm), with no explicit Tool ID set on any of
them (all sitting at ID 0), so TpaCAD's diameter+type auto-resolution had no way to pick one.
Switching the operation to "Through bore drill" (which only ever had one matching bush) worked as
an immediate per-file fix. The documented correct fix — assign a real Tool ID to one bush and
reference it explicitly on the operation — was identified but **not yet tried**, since the owner
was away from the machine. Full root-cause writeup, the fix procedure, and a separately-found
SmartCabinet tool-database gap (no Dia. 5mm entry in a "Cabineo X" drill-head profile): see
`Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`. **Status: workaround in place, permanent
fix planned for next machine session (Task T016).**

## Open questions

- **Was this machine re-commissioned after the move to Unit 31?** No record of the move exists in
  this KB. For a 1030 kg machine that is not a formality: levelling on the threaded feet against a
  spirit level, auxiliary floor screws, ≥1000 mm clearance, ≥500 lux, a vibration-free floor,
  spindle rotation direction re-verified by an electrician, suction reconnected and the drilling
  unit run through full stroke to check for hose fouling. Ask, then either log the checks or
  schedule them. Raised 2026-09-17.
- **No real serial number or manufacture year in the manual itself** — both come from the blank
  type-plate facsimile. Using the invoice's Serial No. 320070 AT as a working value; needs checking
  against the actual machine.
- **§6.8 documentation requirement unresolved** — does this machine need the same kind of dated,
  evidenced log entry (Smartsheet "Safety Check Log") that the F45 gets, or is a pre-cycle functional
  test without a written record genuinely sufficient here? The manual text doesn't say either way.
  Recommend asking the owner rather than assuming; no Task or Processes article created for this yet.
- **Missing EC Declaration of Conformity for this specific unit** — only the manual's blank
  facsimile is available; the real, signed DoC (if filed anywhere) hasn't surfaced in `Raw/`.
- **Directive-citation inconsistency** (older set in §2.1 vs. newer set in the Declaration facsimile)
  — recorded, not resolved; doesn't block registration.
- **Extraction sizing** — this machine needs ≈2000 m³/h; unclear whether `FA2305` (Inventair MK2
  MTFA, see below) or the "one centralised extraction unit" the owner mentioned is sized to serve
  it, or whether that's even the same thing. No extractor manual has arrived yet to check against.
  **The move compounds this**: duct runs in the new unit are not the duct runs the sizing was based on.
- **Owning entity** — same open question as `FA2301`-`FA2303` (invoiced to Fishbone Drylining
  Limited, not AMFA Furniture Ltd); see `CLAUDE.md` §7 and Task T004. *Sharpened 2026-09-17:* AMFA
  Furniture Ltd holds the Unit 31 lease, so this is one company's machine in another's premises.
- **Inventair MK2 MTFA (`FA2305`)** — bought on the same invoice (100154) as this machine: Serial No.
  1696, £4,005.00. No manual has been supplied yet (the owner said one "will follow later"), so no
  dedicated Wiki article has been created for it — registered in the Machinery Register only, per
  this KB's own rule against writing detail ahead of real source material. Also worth checking
  whether this MK2 unit supersedes `FA2302` (Inventair MK1 MTFA, bought alongside the Hebrock) —
  flagged on Task T010, not resolved here.
- **TpaCAD Blind bore drill tool-ambiguity fix** — see Incidents above; open until confirmed on the
  shop floor (Task T016). Complete TpaCAD/Workings manuals not yet obtained either (Task T015).

## Changes

| Date | Change | Reason |
|---|---|---|
| 2026-09-15 | Article created; `FA2304` registered | Third machine's manual (4 parts) and invoice 100154 processed |
| 2026-09-15 | Added Incidents entry and TPA CAD sources | TpaCAD tool-ambiguity fault found and root-caused during first real programming session on this machine |
| 2026-09-17 | **Location corrected to Unit 31.** The workshop moved from Unit 32, which is no longer held; the 2023 invoice address is retained separately because it is what the invoice says. Added "The 2026 move" section with this machine's own re-commissioning requirements, and a re-commissioning open question | Session 14, entry "Networking correction and barcode scoping" |

## Sources

[^1]: `Raw/Vitap K2 2.0 manual part 1.pdf` — manufacturer/machine ID, technical data, safety framework, transport/installation (printed pages 1-58).
[^2]: `Raw/Vitap K2 2.0 manual part 2.pdf` — continuation of parts 1-2 duplex pair (printed pages 59-1, incl. the EC Declaration facsimile).
[^3]: `Raw/Vitap K2 2.0 manual part 3.pdf` — tool/head setup continued, machine use, safety-device check, maintenance schedule (printed pages 60-126 even).
[^4]: `Raw/Vitap K2 2.0 manual part 4.pdf` — continuation of parts 3-4 duplex pair, troubleshooting table, decommissioning (printed pages 125-61 odd).
[^5]: `Raw/Invoice 100154 - 09.11.23 - OCN231185 - Balance.pdf` — purchase date, price, serial number, billed-to entity; also the source for the Inventair MK2 MTFA (`FA2305`) line item.
[^6]: `Raw/TPA CAD part 1.pdf`, `Raw/TPA CAD part 2.pdf` — TpaCAD/WSC programming-software workflow and the Blind-bore-drill tool-ambiguity incident; see `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` for full detail.