---
title: "Troubleshooting — AES SAF 10,000 STK fine dust extractor (FA2402)"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-28
updated: 2026-09-28
sources:
 - "`Raw/AES Extractor.pdf` — the machine's own AES control-panel schematic, 5 pages, drawn for SAF Technical Ltd. Page 2 feeding section, page 5 control section. Read and traced 2026-09-28"
 - "Fault `FL-002` (Fault Log `414932606781316`), 2026-09-28 — the first fault ever logged against `FA2402`, worked end to end with the owner at the panel"
 - "Owner (Minda), 2026-09-28: panel photographs, every measurement in this article, and the correction that found the cause"
related:
 - ../Machinery/aes-saf-10000-stk-extractor.md
 - ./troubleshooting-and-fault-log-system.md
 - ../Suppliers/aes-group.md
---

# Troubleshooting — AES SAF 10,000 STK (`FA2402`)

**This machine had no troubleshooting article and has no manual confirmed for its model.** The
S-series manual the owner supplied is **not accepted** as this machine's (see the machinery article).
What this KB does have is the machine's **own control-panel schematic**, and one fault worked end to
end. This article is built from those two things.

***Read §1 before touching anything.*** It is not a formality — the fault that produced this article
would have been found in five minutes by asking the question in §1, and instead took most of a day.

## 1. Ask this first: what has been worked on?

**Before any measurement, establish what has changed.**

- Has the **supply cable, isolator or distribution board** been touched?
- Has anyone been **inside the panel**?
- Has the machine been **moved**?
- **When did it last actually run** — and has it run *since* whatever was done to it?

**`FL-002` was a phase crossover left by an electrician reconnecting the main cable two days earlier.**
Every component in the panel was healthy. Every voltage read normal. The machine simply could not be
allowed to start, and the panel was telling the truth the whole time.

*The first account given was "nothing was touched, it was working yesterday". The actual history was
"cable reconnected two days ago, hasn't run since". **Ask the question early, and ask it precisely** —
"has anything been worked on" is a better question than "what's wrong with it".*

## 2. What the lamps prove — and what they do not

**This is the part that misled the whole of `FL-002`, so it is stated carefully and it is corrected
against measurement rather than against the drawing.**

| Lamp | What it genuinely tells you |
|---|---|
| **R · S · T** (green) | Each phase is **present** at the incoming terminals. They sit directly across the incoming phases, upstream of everything. **They say nothing about phase sequence, balance, or the neutral.** |
| **FAULT / `ARIZA`** (red) | Lit = **a thermal overload has tripped** (`T1` main motor, or `T2` shaker). It is fed only through their trip contacts. Dark = neither has tripped — ***provided that lamp still works***, which nothing tests. |
| **STOP** (red, illuminated button) | Lit = control voltage present, and `K1` is **not** energised. |

***The STOP lamp does NOT prove the phase relay is passing.*** In `FL-002` the relay measured **0 V
out while that lamp was lit**, which means the lamp is fed **upstream** of `MKR1`, on the same side as
the FAULT lamp. *The schematic was read the other way round and five further eliminations were built on
top of it. The measurement wins; this table is the measurement.*

**And a lamp proves far less than it looks.** A neon or LED draws **microamps**. A contactor coil needs
**around 100 mA**. A poor connection will light an indicator perfectly and fail completely to pull in a
contactor — so "the light is on" never proves a supply is fit to do work.

## 3. The control chain

Everything below runs **L1 to N at 230 V**. In series, in this order:

```
L1 —(7)— F3 6A —(26)— MKR1 phase relay —(27)— COVER SW —(28)— E-STOP
   —(29)— T1 overload —(30)— STOP btn —(31)— START btn —(32)— K1 coil — N
```

| Wire | Between |
|---|---|
| **26** | `F3` out → `MKR1` in |
| **27** | `MKR1` out → cover switch `13` |
| **28** | cover switch `14` → e-stop `11` |
| **29** | e-stop `12` → `T1` `95` |
| **30** | `T1` `96` → STOP `21` |
| **31** | STOP `22` → START `13` |
| **32** | START `14` → `K1` `A1` |

**`K1`'s own `13/14` NO contact is the seal-in**, wired in parallel with the START button. **Nothing
else gates the K1 coil** — no timer, no sequence interlock. Once wire 32 is live, `K1` must pull in.

**The cover switch is normally OPEN.** It only closes when the cover is shut — so ***every continuity
test on this chain is invalid with the cover open***, and the chain will correctly read as broken.

## 4. Devices in the panel

| Ref | Device | Notes |
|---|---|---|
| `F1` | 32 A MCB | main supply |
| `F2` | MCB | shaker branch |
| `F3` | **6 A MCB** | control circuit |
| `MKR1` | **ENTES MKS-03 phase failure / phase sequence relay** | **the gatekeeper — see §5** |
| `ZR1` | ENTES `SER-λ/Δ` star-delta timer | |
| `ZR2` | ENTES `MCB-9` timer | shaker |
| `K1` | Schneider **LC1E1810** + `LAEN11` aux | mains contactor. Coil measured **611 Ω** |
| `K2` | LC1E1801 | delta |
| `K3` | LC1E1201 | star |
| `K4` | LC1E0910 | shaker |
| `T1` | Schneider **LRE22** overload | ⚠️ **see §7** |
| `T2` | Schneider LRE07 | shaker overload |
| `M1` | **11 kW** main fan, star-delta | ~21 A line, ~12 A in the delta leg |
| `M2` | **0.55 kW `SİLKELEME` (shaking) motor** | the filter shaker |

*Two motors, not one. The machinery article described this machine as "11 kW direct drive" and never
mentioned the shaker.*

## 5. Start here when it will not start: measure `MKR1`'s output

⚠️ *Live measurement at 230 V in a panel with 400 V present. Competent person only.*

**`MKR1` is a phase sequence and phase failure relay, and its contact sits second in the chain. If it
is not passing, nothing downstream can work and no lamp will tell you.**

**Measure across its output terminals — voltage in (wire 26) against voltage out (wire 27).**

| Result | Meaning |
|---|---|
| **Voltage in, voltage out** | relay is passing — go to §6 |
| **Voltage in, 0 V out** | **the relay is blocking.** Go to §5.1 |

*In `FL-002` these terminals were accessible throughout and one measurement here would have found the
fault immediately. Instead the relay was eliminated by inference from a drawing. **An inference is not
a measurement, and it must never be used to cross off a device you can simply measure.***

### 5.1 The relay is blocking — is it right to?

**Do not assume it has failed, and do not bypass it.** It has three legitimate reasons to hold open.

**Measure the supply at the incoming terminals:**

| Measure | Expect |
|---|---|
| L1–L2, L2–L3, L1–L3 | ~400 V, **balanced** |
| L1–N, L2–N, L3–N | ~230 V each |

- **A phase missing or badly low** → real supply fault. Relay is right.
- **Significant imbalance** → real supply fault. Relay is right.
- **Three unequal line-to-neutral readings** → neutral problem. The relay measures against N, so a poor
  neutral makes it see a fault that isn't there.
- **All six normal** → **you have not cleared it.** Voltages cannot reveal **phase sequence**.

***Sequence is the trap.*** Swap any two phases and all six readings stay identical while the rotation
is reversed — and the relay will correctly refuse to let an 11 kW fan run backwards. **Use a rotation
tester.** Nothing else settles it.

**If rotation is reversed:** correct it by swapping two phases **at the supply**, not at the relay and
not inside the panel. Then **confirm the fan actually moves air** — a centrifugal fan spins happily
backwards while shifting almost nothing, so extraction performance is the proof, not the motor turning.

**Only if the supply is proven good on all counts *and* rotation is proven correct** is the relay
itself suspect. If you replace it, **wire the new one in exactly the same phase order** — feed its
inputs differently and it will read a reversed sequence and refuse, with the motor wired perfectly.

## 6. Walking the chain

Panel **isolated and proved dead**, **cover closed**, continuity or ohms.

| # | Test | Expect |
|---|---|---|
| 1 | `T1` **95–96** | closed |
| 2 | e-stop **11–12**, button out | closed |
| 3 | STOP **21–22** at rest / pressed | closed / **open** |
| 4 | START **13–14** at rest / pressed | **open** / closed |
| 5 | cover switch **13–14**, cover shut | closed |
| 6 | `K1` **A1–A2** — *ohms, not buzzer* | **a few hundred Ω** (measured 611 Ω) |
| 7 | `K1` `A2` → incoming **N** | closed |
| 8 | **whole chain**: `MKR1` `2` → `K1` `A1`, START held, cover shut | **~0 Ω** |

**Test 8 is worth more than 1–7 together** — it covers every device, every wire, every termination, and
anything in the panel the drawing does not show.

**Identify the door buttons by pressing them and watching which block moves.** *Reading ferrule numbers
off photographs was tried in `FL-002` and produced a wrong identification; pressing the button and
watching worked every time.*

**If everything passes and it still will not start**, the chain conducts but is not being energised —
go back to §5.

## 7. Known discrepancies between this panel and its drawing

**The as-built differs from the schematic. Do not treat the drawing as authoritative.**

1. **`T1` is an `LRE22` (16–24 A)** where the schematic specifies **9–13 A** for that position. It sits
   in the **delta leg** under `K1`, which on an 11 kW motor carries about **12 A**. As fitted it is set
   well above the winding rating. **Verify and correct.**
2. **The STOP pushbutton carries three blocks** — a lamp and **two** contact blocks — where the drawing
   gives it a single contact. **The second wired contact is undocumented and its destination is not
   established.**
3. **The control circuit as drawn has no remote or interlock input.** This bears on the machinery
   article's open question of whether extraction is interlocked to the F45 and the bander: **as drawn,
   it is not.** The installation was undocumented, so as-built may differ.

## 8. Worked example — `FL-002`, 2026-09-28

**Symptom:** START pressed, nothing at all. R/S/T lit, FAULT dark, STOP lamp lit, e-stop released.

**Cause:** **phase crossover** — two phases transposed by an electrician reconnecting the main supply
cable two days earlier. The machine had not run since. `MKR1` measured **240 V in, 0 V out** and was
**working correctly throughout**.

**Everything else measured healthy:** `K1` coil 611 Ω · all five contacts good · all wiring continuous ·
neutral sound · supply 412/405/410 and 238/238/234, ~1% asymmetry.

**Fixed by** swapping two phases back at the supply. **Nothing was bought and nothing was replaced.**

**Two wrong diagnoses were recorded and retracted before the cause was found:**

- ***"`K1` coil open circuit"*** — from a single 574 kΩ reading that turned out to be a bad probe
  contact. **Check the prefix and the terminals before writing a diagnosis on one number:** 574 Ω and
  574 kΩ mean opposite things.
- ***"`MKR1` has failed"*** — built on the first account that nothing had been worked on.

***And the relay was never bypassed, which is the part that mattered.*** Strapping it out to "prove"
it would have run an 11 kW fan backwards on a reversed supply.

## 9. What this article does not cover

- **No manual is confirmed for this model.** No filter-change interval, no differential-pressure
  trigger, no star-delta commissioning procedure, no hours-based servicing.
- **Mechanical faults are not covered** — this is the control system only.
- **The `Part Holder` guard** and the shaker mechanism are undocumented here.
- `FA2402` is **still outside the Maintenance Schedule** for the reasons in the machinery article.
