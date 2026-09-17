---
title: "Hebrock F4 — Edge Banding Machine"
category: Machinery
status: active
sensitive: false
created: 2026-09-14
updated: 2026-09-17
sources:
 - ../../Raw/part 1.pdf
 - ../../Raw/part 2.pdf
 - ../../Raw/part 3.pdf
 - ../../Raw/part 4.pdf
 - ../../Raw/part 5.pdf
 - ../../Raw/part 6.pdf
 - ../../Raw/2026-09-15_hebrock_ce-declaration-of-conformity-f4-f3809.jpg
 - ../../Raw/Invoice 100155 - 09.11.23 - OCN2311184 - Balance.pdf
 - ../../Raw/2026-09-15_fault-photo_edge-bander-corner-gouge-defect.jpg
 - ../../Raw/2026-09-15_fault-photo_edge-bander-hmi-corner-rounding-icon.jpg
 - ../../Raw/2026-09-15_fault-photo_edge-bander-corner-marks-no-rounding.jpg
 - ../../Raw/2026-09-15_fault-photo_edge-bander-corner-rounding-fixed.jpg
related: []
---

# Hebrock F4 — Edge Banding Machine

The workshop's first registered machine (asset code `FA2301`): an edge banding machine
(Kantenanleimmaschine) made by Maschinenbau Hebrock GmbH, Germany, part of the F2/F4/F5 "next"
family. It glues edge material (0.4-3 mm thick plastic, wood or wood-like banding) onto the edges
of rectangular panel workpieces, then trims the overhang, rounds/chamfers the corners, scrapes off
squeeze-out and buffs the result. Not rated for non-rectangular (cut-out) workpieces.

**Asset code corrected 2026-09-15**: originally registered as `FA2601` on the assumption it was
acquired in 2026 (no purchase date was known yet). Invoice 100155 has since confirmed it was
actually bought in **2023**, so the code has been corrected to `FA2301` before anything else was
built on top of it — see Changes.

## Key facts

| Item | Value | Source |
|---|---|---|
| Asset code | `FA2301` (locally self-assigned; corrected 2026-09-15, was `FA2601`) | — |
| Manufacturer | Maschinenbau Hebrock GmbH, Beendorfer Str. 31, 32609 Hüllhorst, Germany (Altendorf Group) | [^1][^7] |
| Model | F4 (manual covers the family "F2 next / F4 next / F5 next"; the CE Declaration itself just says "F 4") | [^1][^7] |
| Machine type | Edge banding machine (edgebander) | [^1] |
| Serial / machine number | F3809 — confirmed by the manufacturer's own EC Declaration of Conformity | [^7] |
| CE marking | Confirmed present. EC Declaration of Conformity per Machinery Directive 2006/42/EG, Low Voltage Directive 2014/35/EU, EMC Directive 2014/30/EU. Signed 16.01.2023. Harmonised standards cited: EN 12100-2010, EN 349:1993+A1:2008, EN 13850:2015, EN 60204-1:2018, EN 13849-1:2015, EN ISO 4414:2010, EN ISO 14119:2013, EN ISO 3746:2010, EN ISO 11202:2010, EN ISO 11204:2010, plus EN ISO 18217:2015 | [^7] |
| Manual edition | Doc. 0000010089-002-DE, "DE Version 11/2022", labelled "Originalbetriebsanleitung" | [^1] |
| Purchase date | 09/11/2023 (date of invoice 100155, a "70% Balance" invoice — may not be the original order date) | [^8] |
| Purchase price | £42,000.00 shown on invoice 100155 — unconfirmed whether this is the full price or just the 70% balance (separate invoice 100141, carrying the VAT, is not on file) | [^8] |
| Purchased by / billed to | Fishbone Drylining Limited (now Fishbone Construction Ltd) — **not AMFA Furniture Ltd.** Owning entity unconfirmed; see Open questions | [^8] |
| **Location — current** | **Unit 31**, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA. See "The 2026 move" below. | owner, 2026-09-17 |
| Location — as delivered (2023) | Unit **32**, same estate — the delivery address on invoice 100155. **Unit 32 is no longer held.** Retained because it is what the invoice says, not because it is where the machine is. | [^8] |
| Electrical (F4 specifically) | 3x400V AC 50Hz, 7.44 kW, 20.2 A rated current. RCD required: Type B 40/0.03A | [^1] |
| Pneumatic (F4 specifically) | 7 bar minimum constant supply; ~340 L/min air consumption | [^2] |

**Bought alongside it, same invoice:** an Inventair MK1 MTFA dust/fume extractor, Serial No. 1971,
£3,410.00 — very likely serving this machine's dust extraction requirement. Registered as a
separate asset, `FA2302`, in the Smartsheet Machinery Register; no manual or Wiki article for it
yet.

## The 2026 move — and what it implies

**The workshop moved from Unit 32 to Unit 31.** The lease for Unit 31 (Forth England Limited to
Furniture by Fishbone Limited, the company's name before it became AMFA Furniture Ltd on 13 July
2026) is **dated 25 June 2026**. The lease date is not necessarily the date the machines were
physically moved, and no record of the move itself exists anywhere in this KB.

**A move is a re-commissioning event for this machine**, and the manual's own installation chapter
sets out what that involves: floor-anchoring or castor-locking; confirming ≥500 mm clear space at
infeed and outfeed beyond the longest workpiece; a qualified electrician re-confirming **phase
sequence** (the chain-bed feed motor must spin the direction arrowed on the feed switch); restoring
the separate 10 mm² PE earth bond; re-establishing 7 bar pneumatic supply; and reconnecting dust
extraction at ø140 mm with **≥ 25 m/s** at the port, with plastic ducting earthed via its conductive
spiral. New duct runs change the velocity actually achieved.

**Whether any of this was redone after the move is not recorded** — see Open questions. It is not
assumed to have been skipped.

## Installation / setup

Full step-by-step detail with figures is in `part 2.pdf` and `part 3.pdf`; this is a working
summary, not a replacement for reading those sections before commissioning.

**Siting & transport.** Ships fully assembled on a wood base, moved by forklift — the machine is
top-heavy (asymmetric weight distribution), lift at the centre of the body, no jerking. Leave clear
space at the outfeed and infeed sides of at least 500 mm more than the longest workpiece to be run.
Floor-anchor or fit to a mobile chassis; if mobile, lock the two front steering castors once
positioned. Never use the infeed ruler as a lifting/moving handle.

**Assembly.** Attach the roller-table arm to the machine body and fit the roller star onto it.

**Electrical.** Qualified electrician only, per the circuit diagram. Supplied cable is ~5 m,
5G2.5 mm²; the workshop must add its own separate 10 mm² PE earth bond. Confirm phase sequence —
specifically check the chain-bed feed motor spins the direction shown by the arrow on the feed
switch. Overcurrent protection: 25 A slow-blow ("K" characteristic) fuses.

**Pneumatics.** Constant 7 bar minimum at the service unit, hose min. ø8 mm. A pressure switch
E-stops the machine below ~3.5 bar.

**Dust extraction.** Main port ø140 mm, minimum air velocity 25 m/s at the port. If plastic
ducting is used it must be electrostatically earthed via its conductive spiral wire, bonded to the
machine body. Extraction can be electrically interlocked so the machine won't run without it. The
workshop's Inventair MK1 MTFA (`FA2302`, bought on the same invoice) is the likely extraction unit
for this — confirm it's actually plumbed to this machine's port.

**First start-up sequence** (from `part 2.pdf`):
1. Visual check — no faults, all guards/covers on, external extraction running.
2. Open the service-unit air valve, confirm ≥7 bar.
3. Confirm both E-stop buttons are released (HMI screen and outfeed end).
4. Main switch to "I", then "ON" at the control panel.
5. Switch on heating; set glue melt temperature (~3.5 min to reach temperature — 170°C for EVA,
 110°C for PUR). The applicator roller then engages and dosing rods open.
6. Bring units online in sequence per the edge material recipe selected (joint cutter → trim saw →
 router → start → feed → radius scraper → face scraper → buffing → corner router).

**Calibration points to work through on setup**: edge channel height, edge guide clearance (edge
should sit ~4-5 mm proud of the workpiece), top pressure beam height (~2.5 mm roller pre-load,
factory spring length 37 mm), glue dosing amount, joint-cutter milling depth and end-stop, trim saw
cut depth (factory 3 mm) and overhang stops, router station pneumatic adjustment, corner-router
radius/chamfer/depth/speed (see Incidents for a real worked example of this adjustment), radius and
face scraper offsets, buffing station motor angle, and (if needed) Nesting-function setup for
cup-hinge-bore workpieces. Workpieces narrower than 80 mm need a support jig. PLC/HMI backup
battery: replace within 2 years or on alarm.

## Safety

From `part 1.pdf`, `part 2.pdf` and `part 4.pdf`. Signal words in the manual, most to least severe:
GEFAHR (imminent danger) > WARNUNG (possible danger) > VORSICHT (minor injury) > HINWEIS (property
damage / general tip).

- Only trained, authorised people may operate, set up or maintain it; anyone doing so should have
 read and signed off on the manual.
- **Lockout before any setup/maintenance/fault-clearing work** — switch off and secure against
 unexpected restart. E-stop is explicitly **not** a normal stop: it brakes all drives except the
 glue-pot applicator roller motor (kept running on purpose so the glue doesn't set inside it).
- The joint-cutter guard is interlocked — removing it while running trips an E-stop; drives coast
 down in ~10 s; a tool is needed to remove the guard; there's a manual override lever behind the
 rear panel for interlock failure only.
- Entanglement/crush risk at all rotating and moving parts — no loose clothing, hair or jewellery,
 never reach into moving parts.
- Fire risk from the hot-melt adhesive — follow the adhesive's own safety data sheet, no ignition
 sources nearby, keep containers closed, no combustibles near the pot's protective grille.
- Hot surfaces (glue pot, motors) — let cool before maintenance, never touch draining hot glue.
- Pneumatic lines — depressurise before opening; qualified personnel only; find leaks with spray or
 cardboard, never by hand.
- Never run a workpiece wider than 1200 mm on the table-widening extension without an extra roller
 conveyor for support (tip-over risk).
- Dust (oak/beech flagged as health-hazardous) — vacuum only, never blow or sweep.
- Workpieces with through-holes over 8 mm are not to be processed except via the dedicated Nesting
 function.
- PPE required: protective clothing, safety shoes, hearing protection, gloves (specifically for
 blade/knife changes).
- **All adjustment/setting work must be done with the machine switched off** — stated as a
 precondition throughout Chapter 6.5 "Rüsten und Einstellungen".

**Compliance:** a genuine EC Declaration of Conformity exists for this exact machine (Machine no.
F3809), covering the Machinery, Low Voltage and EMC Directives with a full list of harmonised
standards — see Key facts and [^7].

## Maintenance schedule

From `part 4.pdf`/`part 5.pdf`/`part 6.pdf`, Chapter 7 "Wartung und Pflege". Always maintain with
the machine switched off; manufacturer-approved materials only, never mix lubricants.

**Inspection / cleaning:**

| Item | Task | Interval |
|---|---|---|
| Whole machine | E-stop buttons — check function | Daily |
| Whole machine | Pneumatic controls — check function | Daily |
| Whole machine | All screws — inspect, retighten | Weekly |
| Edge guide channel | Clean of glue/chips/edge scraps | Daily |
| Pressure (nip-roller) zone | Clean of glue/chips/scraps; remove glue from silicone rollers while cold | Daily |
| Chain bed — feed interior | Clean | 1-2x per year |
| Chain bed — sliding surfaces (black plates) | Clean & lubricate with WD-40 | Every 3 months |
| Chain bed — drive chain | Check tension, adjust | As needed |
| Glue pot | Remove crusted deposits | As needed |
| Glue pot | Check heating output (~22 kW); replace defective heater cartridge | Weekly |
| Router station (Frässtation, main routers) | Clean fan cover, motor, drive body | As needed |
| Router station | Clean of glue/chips/material | Daily |
| Router station | Check cutter sharpness; replace if needed | Weekly |
| Router station | Check feeler-disc wipers — function & clean | Weekly |
| Router station | Check feeler discs for damage; replace if needed | Weekly |
| Router station | Precision ball bearings — inspect/replace (qualified personnel only) | Every 5,000-6,000 operating hours |
| Kappsäge & Eckenabrundfräse (trim saw & **corner-rounding router**) | Clean of glue/chips/edge-material residue | **Daily** |
| PLC/control | Replace backup battery | Every 2 years, or immediately on alarm |

Note: the "feeler-disc wiper/feeler-disc damage" checks above belong to the main **Frässtation**
(router station), not the corner-rounding router (Eckenabrundfräse). The corner-rounding router's
own scheduled maintenance is limited to the daily clean and the weekly guide-shaft oiling below; it
has no scheduled feeler-ring/lead-ring inspection interval of its own.

**Lubrication:**

| Item | Task | Interval |
|---|---|---|
| Router station (Frässtation) | Oil round columns & adjustment screws with thin oil | Every 4 weeks |
| Kappsäge & Eckenabrundfräse (trim saw & **corner-rounding router**) | Oil guide shafts with thin machine oil | **Weekly** |
| Chain bed | Grease the chain | Annually |

**Condition-based, no fixed interval:** joint-cutter diamond tools, trim saw blade, router cutters,
radius/face scraper blades, buffing wheels — replace on visible wear/damage, no calendar schedule.
Spray consumables (release agent, cleaner, glide agent — all from Riepe GmbH) are maintenance-free
if only the specified fluids are used, and specifically protect the corner router's feeler
shoes/rings from glue buildup.

The 5,000-6,000 operating-hour router-bearing check (Frässtation only) is the only hours-based
interval in the whole manual; everything else above is calendar- or condition-based.

## Incidents

**2026-09-15 — Corner-rounding router (Eckenabrundfräse) producing a bad corner. RESOLVED.**

Reported: a visible gouge/chip-out in the edge band right at the workpiece corner, on the station
selected via the HMI icon showing two rollers converging on a corner (confirmed to be the
Eckenabrundfräse station, not the radius scraper).

**Diagnosis, from the manual's own fault table (§8.2 Störungstabelle, p.183):**

| Störung (symptom) | Ursache (cause) | Abhilfe (fix) |
|---|---|---|
| "Der Radius an der Werkstückecke sieht 'hakelig' aus, evtl. Kantenüberstand" [corner radius looks jagged, possible edge overhang] — matched the original photo | Anschlagschraube verstellt [stop screw out of adjustment] | Loosen locknut, unscrew the stop screw slightly so the feeler ring (Abtastring) protrudes ~0.2mm+ into the workpiece line, retighten locknut |

**Timeline:**
1. First adjustment: backed the stop screw out per the manual's Abhilfe wording. **Result:
 overcorrected** — station stopped rounding entirely, just left rub/scuff marks (photo 3).
2. Second adjustment: reversed direction, turned the stop screw back **in** partway from the
 overcorrected position, in a small increment, and retested.
3. **Result: fixed.** Clean, properly rounded corner on both edges, no marks (photo 4).

**Lesson for next time, recorded because it doesn't match the manual at face value:** the fault
table's own wording implies backing the stop screw *out* increases engagement/cutting (fixing an
"overhang"/too-little-material symptom). In practice here, the working setting was reached by going
back *in* from an overcorrected "backed out" position — i.e. the correct setting sat somewhere
between the original mis-set position and the first (overcorrected) fix, reached from the
overcorrected side by turning inward. Treat the manual's stated direction as a starting hypothesis
to test in small increments, not a guaranteed direction — the working method that actually
succeeded was small, reversible steps with a test cut after each one, not a single confident move
either way.

**Not otherwise investigated, since the stop-screw adjustment resolved it**: workpiece
squareness/minimum-length preconditions, vertical-slide throttle-valve speed, and feeler-shoe
glue/debris buildup — all remain plausible contributing factors worth knowing about if this
recurs, per the manual (see the retained notes in this article's history).

Photos: [^9] (original gouge), [^10] (HMI station icon), [^11] (after first adjustment —
overcorrected, marks, no rounding), [^12] (after second adjustment — fixed, clean radius).

## Open questions

- **Was this machine re-commissioned after the move to Unit 31?** No record of the move exists in
 this KB, let alone of the checks that follow one — phase-sequence confirmation, the 10 mm² PE
 bond, floor-anchoring or castor locking, ≥500 mm infeed/outfeed clearance, and extraction
 re-established at ≥25 m/s through the ø140 mm port with the ducting earthed. Ask, then either log
 the checks or schedule them. Raised 2026-09-17.
- **Owning entity unconfirmed.** Invoice 100155 bills this machine (and `FA2302`) to **Fishbone
 Drylining Limited** (now Fishbone Construction Ltd), delivered to its Wallsend unit — not to
 AMFA Furniture Ltd. Don't assume AMFA Furniture Ltd is the legal owner without checking.
 *Sharpened 2026-09-17:* AMFA Furniture Ltd holds the Unit 31 lease, so the machine is one
 company's asset operating in another's leased premises.
- **Exact price unconfirmed.** Invoice 100155 is a "70% Balance" invoice; the referenced invoice
 100141 (which carried the VAT) is not in `Raw/`.
- **Purchase date vs. order date.** 09/11/2023 is the balance invoice's date; the CE Declaration
 is dated 16.01.2023, ~10 months earlier, which may be closer to the true order/build date.
- **Dimensions/weight table ambiguity** (from the manual). Three parallel columns of
 dimensions/weight (930 kg / 640 kg / 840 kg) without clearly labelling which belongs to F2, F4 or
 F5 — don't guess which figure applies.
- **Electrical table gap.** F2's max-power figure is illegible in the source scan; F4 and F5 both
 read 7.44 kW. F4's rated current (20.2 A) is legible and used above.
- **Dust-extraction required volume figure is illegible** in the source scan.
- **PLC battery part-name mismatch:** called "MV-BAT" in one place, "LibatH" in the spares list —
 probably the same part, not confirmed.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-14 | Created from `Raw/part 1.pdf`-`part 6.pdf` (Hebrock F4 next manual) | Session 2, entry "Hebrock F4 next manual processed" |
| 2026-09-15 | Serial number confirmed (F3809) and CE Declaration of Conformity found; purchase date/price/location learned from invoice 100155; asset code corrected `FA2601` -> `FA2301`; new open questions raised (owning entity, exact price) | Session 3, entry "Invoice and CE Declaration processed" |
| 2026-09-15 | Corner-rounding router fault reported and logged as an in-progress Incident; manual's fault table matched to the symptom; adjustment attempted, overcorrected | Session 4, entry "Corner-rounding router incident" |
| 2026-09-15 | Incident resolved — second adjustment (reversed direction from the overcorrection) produced a clean radius; Task T006 closed; `FA2301` status returned to "In service"; lesson recorded that the manual's stated adjustment direction didn't match what worked in practice | Session 5, entry "Corner-rounding router incident resolved" |
| 2026-09-17 | **Location corrected to Unit 31.** The workshop moved from Unit 32, which is no longer held; the 2023 delivery address is retained separately because it is what the invoice says. Added "The 2026 move" section and a re-commissioning open question | Session 14, entry "Networking correction and barcode scoping" |

## Sources

[^1]: [Hebrock F2/F4/F5 next operating manual, part 1](../../Raw/part%201.pdf) — cover page, ch.3 "Technische Daten"
[^2]: [Hebrock F2/F4/F5 next operating manual, part 2](../../Raw/part%202.pdf) — installation & commissioning chapter
[^3]: [part 3](../../Raw/part%203.pdf) — HMI/operation chapter
[^4]: [part 4](../../Raw/part%204.pdf) — ch.6 operation, HMI icon legend, adjustment procedures
[^5]: [part 5](../../Raw/part%205.pdf) — ch.6 continued, ch.7 maintenance, ch.8 fault table (odd pages 129-201)
[^6]: [part 6](../../Raw/part%206.pdf) — ch.6-9 continued (even pages 130-200, reconstructs with part 5)
[^7]: [EC Declaration of Conformity, Hebrock F4, Machine no. F3809](../../Raw/2026-09-15_hebrock_ce-declaration-of-conformity-f4-f3809.jpg) — photo provided by the owner, 2026-09-15
[^8]: [Invoice 100155, 09/11/2023](<../../Raw/Invoice 100155 - 09.11.23 - OCN2311184 - Balance.pdf>) — Fishbone Drylining Limited, 70% balance, ref OCN231184
[^9]: [Fault photo — corner gouge defect](../../Raw/2026-09-15_fault-photo_edge-bander-corner-gouge-defect.jpg) — photo provided by the owner, 2026-09-15
[^10]: [Fault photo — HMI corner-rounding station icon](../../Raw/2026-09-15_fault-photo_edge-bander-hmi-corner-rounding-icon.jpg) — photo provided by the owner, 2026-09-15
[^11]: [Fault photo — corner after first adjustment, marks but no rounding](../../Raw/2026-09-15_fault-photo_edge-bander-corner-marks-no-rounding.jpg) — photo provided by the owner, 2026-09-15
[^12]: [Fault photo — corner after second adjustment, fixed](../../Raw/2026-09-15_fault-photo_edge-bander-corner-rounding-fixed.jpg) — photo provided by the owner, 2026-09-15
