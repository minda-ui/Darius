---
title: "Reference: Altendorf F45 electrical schematics (FA2303)"
category: Processes
status: active
sensitive: false
created: 2026-09-18
updated: 2026-09-18
sources:
 - ../../Raw/Altendorf F45 Electrical Schematics part 1.pdf
 - ../../Raw/Altendorf F45 Electrical Schematics part 2.pdf
related:
 - ../Processes/f45-monthly-safety-device-check.md
 - ../Suppliers/altendorf-gmbh.md
---

# Reference: Altendorf F45 electrical schematics (`FA2303`)

What the manufacturer's own circuit diagrams say about `FA2303`, and — just as importantly — what they
do not.

**Why this is a separate article rather than an edit to the machine's own page.** `FA2303`'s machinery
article is one of the eighteen that live on Drive only, and the connector's read tool does not
round-trip (`CLAUDE.md` §3). Re-authoring a 25 KB article through a lossy read to insert this content
would risk silent drift across everything it did *not* mean to touch. A new file avoids that entirely
and goes into the git mirror cleanly.

---

## Read this before trusting any terminal number below

**The scan is poor, and that bounds everything in this article.**

Both PDFs are Xerox scans processed through the connector's OCR. What came back is **scattered label
fragments in broken reading order — not circuits.** The graphical content is entirely lost.

> **No wire could be traced end to end, in either part.** Where this article says a terminal carries a
> function, that is **two labels sitting near each other on a sheet**, not a conductor followed from
> one end to the other.

Concretely, the character confusions that survived: `B`↔`8` (which is why the drawing number reads two
ways), `O`↔`0`, `I`↔`1`. "Altendorf" itself appears as *Attendorf*, *Ahendorf*, *ARendorf*, *Akendorf*
and *NtendOlf*. Roughly **a third to two-thirds of the sheets produced no recoverable text at all**,
and the two parts disagree on the total sheet count (63 vs 78 vs 136).

**Anyone acting on this article — especially an electrician — must verify against the paper first.**

---

## What the document is

| Item | Value |
|---|---|
| Manufacturer | **Altendorf GmbH**, Wettinerallee 43/45, D-32429 Minden, Germany, +49 571 9550-0 |
| Drawing number | **`B1434.0220`** *(also OCRs as `81434.0220` — same field, `B` read as `8`)* |
| CAD system | ePlan version 2.9.4 |
| Editor | **`HK`** |
| Sheet date | **17.10.2022** on effectively every sheet |
| Validity | *"Circuit diagram valid from 01.01.2022"* |
| **`checked` field** | **Blank on every recovered title block** — no checker name, and no readable revision level anywhere |
| Confidentiality | *"This drawing may not be reproduced either in whole or in part or its contents communicated to any third party without our prior written agreement"* |

**Execution line, verbatim and recurring on every sheet:**

> *"F45 BS Vario / 3 axis scorer / rip fence / vacuum table / L-axis / DRW operation"*

**This is the with-scorer build.** The set cross-refers to sub-drawing **`B1432.0020` "400V KEB — with
scorer"** rather than **`B1432.0019` "without scorer"**. That is a statement of the drawing, not an
inference.

**But it is a *configuration* drawing, so it shows options the machine may not have.** Three cross-cut
fence variants are drawn (**UNO 90**, **DUO 90**, **DUO FLEX**) and three operator terminals
(**PRO**, **EVO**, **ELMO**). **Which are actually fitted is not determinable from this document** and
has not been guessed at.

---

## The extraction interlock — the most useful thing in the set

On the main-saw converter load sheet (sub-assembly `+1432.0020`, by terminal strip `-X1A` and a contact
numbered `53`), the drawing states:

> *"terminals to switch an external contactor to start an exhaust unit — max. control current 1A —
> max. control voltage 240VAC"*

**So the F45 provides volt-free terminals to start an external extractor through a contactor.** No
current transformer appears anywhere in either part.

*The current renders as `IA` in the OCR; reading it as `1A` is an inference, since `IA` is not a unit.
The `240VAC` is clean text.*

**What this changes, and what it does not.** Task **T018** asked whether extraction is interlocked to
machine power. The **capability** is now confirmed from the manufacturer's own drawing. **Whether
anything is landed on those terminals at Unit 31 is not.** A drawing shows what a machine offers; it
says nothing about this installation. So the question stops being a document hunt and becomes **a look
inside the right-hand control cabinet**.

**Do not confuse this with the vacuum table.** The extensive `suction row 1`…`suction row 6`,
`3/2-way valve` and `vacuum pressure switch` content (`+0622`, I/O box `-UV100`, CAN segment D) is
**workpiece clamping**, not dust extraction. Part 1's extract nearly mistook one for the other.

---

## The safety chain — device tags for the monthly check

The chain is called **`Sicherheitskette 1`**. These tags let
[the monthly check](f45-monthly-safety-device-check.md) name the devices it tests instead of
describing them.

| Device | Tag | Notes |
|---|---|---|
| **Emergency stop 1** | — | *"control panel on machine frame"* |
| **Emergency stop 2** | `+1405.1000-S1` | *"control panel at eye level"* |
| **Emergency stop 3** | `+1419.1007-S5` | — |
| **Sliding-table switch** | `+1460.1000-S1` | German *Doppelrollwagen*; wire `-W_B1433.0041`; fault **E44** |
| **Saw blade cover** | `+1480.0030-S1` | *"Sägeblatt-Abdeckung offen"*; wire `-W_B1433.0051` |
| **Inspection flap** | — | *"Inspektionsklappe"*, plus a *"Türe/Vario"* door signal |
| **Reduced safety area** | `+1410.0018-B2` | Inductive sensor releasing a **50 mm** reduced zone at the rip fence |

German originals `NOT-AUS Taster 1/2/3`; chain signals `Not1` / `Not2` / `Not3`.

**Two things worth flagging to whoever runs the check:**

1. **There are three emergency stops.** The existing check article speaks of *"the E-stop"*, singular.
   If the check has ever been performed against one button, it was incomplete.
2. **The reduced safety area is a safety function this KB had no record of at all** — an inductive
   sensor releasing a 50 mm zone at the rip fence. It probably belongs on the monthly check; that is a
   judgement for whoever owns the check, not a change made here.

**Safe Torque Off:** a sheet headed *"circuit version STO"* shows `STOP1+`/`STOP1-`/`STOP2+`/`STOP2-`
on the scorer inverter `-G2`, switched by relays `-K6E` and `-K7E`. *That this is dual-channel is my
reading of the 1+/1−/2+/2− pairing; the drawing does not use the phrase.*

**The protective hood** (`Haube`) appears in the safety-area block but **could not be tied to a device
tag** — the OCR is too fragmented there.

---

## Motor over-temperature — and a disagreement between the two parts

This bears directly on Task **T011**, the annual PTC check.

**Part 2** puts the termination at **`-X3`**, terminals **`POT_1`** and **`POT_2`**, labelled *"excess
temperature resistor"*, at the main saw motor's converter (`+1432.0020`, KEB COMBIVERT F5, right-hand
cabinet).

**Part 1** puts over-temperature channels at **`-X1` terminals 13/14** (main saw motor) and **21/22**
(scoring saw motor).

> **Both may be true** — a motor-side terminal and a converter-side terminal in the same circuit — **or
> one may be an OCR artefact.** Since no wire could be traced end to end, *this cannot be settled from
> the documents.* Recorded as a contradiction rather than resolved into one.

**A second, separate ambiguity.** The same circuit area uses **both** `Thermokontakt` (a thermal
contact — normally a **bimetal switch**) **and** "excess temperature resistor" at `POT_1`/`POT_2`
(which reads as a **PTC**). Possibly the inverter-fed main saw motor and the scorer motor use different
sensor types; possibly the OCR merged two sheets.

**This matters practically: a bimetal contact is a continuity check, a PTC is a resistance
measurement.** Neither reading is recorded as fact. It goes to the electrician as a question.

**The 150–1000 Ω figure is not in these schematics.** No resistance value of any kind appears in either
part, and the words *PTC*, *thermistor* and *Kaltleiter* do not appear at all. That figure came from the
machine manual; the schematics neither confirm nor contradict it.

**Signals and fault codes:** `HM Temp.` = *Übertemperatur Sägen Motor* (main saw) → **E43 Main Motor
Overheat**. `RM Temp.` = *Vorritzer Übertemperatur Motor* (scorer) → **E42 Scoring Motor Overheat**.
No dedicated thermistor tripping relay could be identified by designation.

---

## Drives, and the "ElmoDrive" question answered

This KB records `FA2303` as an "Altendorf F45 **ElmoDrive**". **Part 1's extract could not find that
word anywhere** — which looked like a naming discrepancy worth recording.

**Part 2 found it.** `+1405.0100-U01` is the **ELMO-Terminal**, one of three alternative operator
terminals drawn (`+1405.0000-U01` PRO, `+1405.0200-U01` EVO, `+1405.0100-U01` ELMO), described as
*"plug connection ELMO-Terminal / Eye-level operating panel / communication Backplane terminal"*.

**So ElmoDrive is the operator/positioning terminal, and the frequency converters underneath are KEB.**
The two were never in conflict. *That reading of "ELMO" as ElmoDrive is mine, but it is consistent with
everything else the KB holds.*

| Drive | Model | Role |
|---|---|---|
| `-G1` | **KEB COMBIVERT F5** | Main saw motor, right-hand cabinet |
| `-G2` | **KEB COMBIVERT G6** | Scorer, right-hand cabinet |

**Terminal hardware:** colour LCD display, **a USB interface** (`-XG01`, `XS21`, cable
`-W1_F6410.0510` *"USB cable C/E/P Terminal"*), LED status codes for software download, and a storage
battery.

> **Bearing on the "does the F45 take a digital cut list?" question:** a USB port on the terminal is
> confirmed. That is **not** evidence it imports cut lists — the manual's only documented USB uses were
> firmware updates and remote-maintenance files. The working answer stays *the saw takes dimensions,
> not cut lists*, and still needs confirming against the ElmoDrive's own menus.

---

## Ratings, stated verbatim and not tidied

| Item | Rating |
|---|---|
| **Main saw motor `-M1`** | *"3x 393 VAC — 5.0/6.5 kW — 10.4 / 13.4 Arms — 4700 U/min — 313 Hz — VSD use only"* |
| **Vacuum-table pump motor** | 220–240 V, 0.37 kW, 2850/3450 U/min, 50/60 Hz (`+1720.1000`, contactor `-K23M`, fuse `-F23`) |
| **Scorer saw motor** | *No kW or current rating was legible* |
| Customer-side supply protection | **fuse category gL/gG, 32 A / 400 VAC** |
| `-F33` | 2.5 A — *"Fuse only when connected with 2 phases"* |
| 18 VAC circuit | `5x20 T6.3A` |
| Control PSUs `-T30`/`-T31` | 85–264 V in → 24 V DC, 2.5 A, `T 2.5A` protection |
| Line laser | 635 nm, **laser class 2M**, device `-A1` |

*The main saw motor's 393 VAC and 313 Hz are unusual figures. They are consistent with an inverter-fed
high-speed spindle and have deliberately **not** been rounded or "corrected".*

**The KEB discharge-time warning** (*"CAUTION! Risk … discharge time _ minutes"*) OCR'd ambiguously as
both 5 and 6 minutes. **The number is not recorded here.** Anyone opening that cabinet must read it off
the machine.

---

## Architecture and connection points

**CAN-bus**, segments A–E, from a backplane in the left-hand cabinet (`+1430.2000-U1`). Node addresses
stated per axis — useful for fault-finding:

| Axis | Addr | | Axis | Addr |
|---|---|---|---|---|
| Rip fence | 1 | | Length compensation | 6 *(digit uncertain in OCR)* |
| Saw blade tilt | 2 | | Cross slide, 4th axis | 7 |
| Saw blade height | 3 | | Scorer lateral adjustment | 8 |
| Flip stop L1 | 4 | | Scorer width adjustment | 10 |
| Flip stop L2 | 5 | | | |

Each carries an *Endwiderstand Ein/Aus* (terminating resistor) setting — the L2/flip-stop nodes "Ein",
most others "Aus".

**Location numbering used throughout:** `+1405` terminals · `+1408` swing arm · `+1410` 4th axis ·
`+1430` control cabinets · `+1432` circuit F45 BS · `+1460` machine frame · `+1470` table ·
`+1480` blade cover · `+1720` vacuum pump.

**Incoming supply:** terminal strip `-X1A` with `L1, L2, L3, PE1` at the right-hand cabinet.

**Two installation notes bearing on the post-move question (T018):**

- *"After removing the control current ground is an insulation monitoring device necessary!"*
- *"CAUTION! Protection is from the customer to be carried out [properly]."* — customer-side
  short-circuit protection, gL/gG 32 A / 400 VAC. *("property" in the OCR is almost certainly
  "properly" — flagged, not silently corrected.)*

---

## What is **not** in these schematics

Stated plainly, because absence is the thing most likely to be misremembered later:

- **No serial number, machine number, commission number, order number or customer name.** Task **T009**
  is not closed. The internal job number `23-11-12-005` does not appear either.
- **No main isolator / disconnect device** (`-Q1`, *Hauptschalter*) was found — very likely on one of
  the missing sheets rather than genuinely absent.
- **The `F1`–`F16` fuse list** the spare-parts manual could not confirm is **still unconfirmed**. Only
  `-F6`, `-F23` and `-F33` appear.
- **No resistance value** anywhere (see T011 above).
- **No Ethernet, no network interface, no remote-maintenance interface.** The only data paths shown are
  the internal KEB serial link and the CAN-bus, plus the terminal's USB port.
- **No installation instruction to verify phase rotation.** A `direction` label near contactors `-K6E`
  and `-K8E` and a `Reverse` input on the converter are *operational* scorer controls, not a
  commissioning check. Flagged rather than offered as an answer.

### Two identifiers that are not the serial number

- **`F4515`** — the most prominent identifier in the set, the `system` field on every sheet and the
  ePlan `=` prefix in every device tag (`=F4515+1432.0020-K4M`). **It is a plant/model-series
  designation, not stated anywhere to be a serial.** Do not record it as one. It *is* worth quoting to
  Altendorf when asking for the serial, since their drawing set is keyed on it.
- **A recurring sheet header** OCR'd across at least five spellings as something like
  **`FNI_001_ALD09`**. That is the slot a project or commission code normally occupies — but the
  characters involved (`I`/`1`, `O`/`0`) are exactly the ones OCR gets wrong, so **it has deliberately
  not been normalised into a plausible-looking code.**

**One sharp photograph of a sheet header and title block — ideally the cover sheet — very likely
settles both.**

---

## Coverage gaps

Sheets that produced **no recoverable text at all** are *unread, not empty*. Between the two parts the
notable gaps are around sheets **1, 6, 9–12, 19–24, 33–36, 44, 54, 60, 65, 68–76**. Sheets 9–12 and
19–24 are probably control-voltage supply and the scorer converter load part. **Sheet 1 is the likely
home of a cover/title block carrying the serial.**

## Security

**No password, PIN, access code or service code was found in either part**, so nothing was reproduced.

**Absence here is not evidence of absence.** A service code printed in small type inside a drawing
frame is exactly what this scan quality would lose. `CLAUDE.md` §6a's never-hold-a-credential rule
applies if anyone later reads the missing sheets — as it did when the ElmoDrive remote-maintenance
access code was found in the machine's manual and removed before the Wiki was pushed to git.

## Open questions

- **Is the extraction interlock actually wired?** The terminals exist; the installation is unrecorded.
- **`-X3 POT_1/POT_2` or `-X1` 13/14 and 21/22** — which is the motor-temperature measurement point?
- **Bimetal or PTC?** The drawing uses both words in the same circuit area.
- **The serial number** — see above; a photo of the cover sheet is the cheapest route.
- **Which fence and which operator terminal** are actually fitted.
- **A better scan** would be worth more than another document.
