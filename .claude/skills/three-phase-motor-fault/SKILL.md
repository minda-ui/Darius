---
name: three-phase-motor-fault
description: Diagnose and recommission a three-phase motor on any workshop machine (extractor, compressor, F45, Vitap, edgebander). Use when the owner says a motor "won't start", "buzzes", "hums", "runs slow / half speed", "trips the breaker", "is noisy", "runs but no suction", or after a motor is replaced.
---

# Three-phase motor fault

Adopted at the 2026-10-10 good night, from `FL-002` (supply phases swapped, 2026-09-26/28), `FL-003` (insulation
failure, 2026-10-01) and the 2026-10-10 buzz-no-start. **Electrical work is done by the owner or their electrician;
Darius diagnoses, asks for readings, records.** Machine facts: `Wiki/Machinery/*`, the panel drawings in `Raw/`.

## 1. Stop first
A motor that hums but does not turn draws locked-rotor current with no cooling: **stop, isolate, lock off** before
anything else. Check what overload is fitted and whether it can trip at the nameplate current (on `FA2402` the LRE22
could not — 16 A minimum against 11.6 A).

## 2. Symptom → most likely causes (check in this order)
| Symptom | Causes |
|---|---|
| **Buzzes, won't turn** | a **phase missing** (loose/burnt contactor terminal, MCB pole) · **terminal-box links left on** a star-delta motor (needs six separate leads) · leads on the wrong terminals / a winding reversed · rotor bound (fan rubbing) |
| **Runs ~half speed, noisy** | stuck in **star** (no changeover — watch the Δ lamp / star-delta timer) · running on **two phases** · winding damage |
| **Trips at star→delta changeover** | **insulation failure** · a short in the delta circuit |
| **Spins, little air** | **running backwards** (supply phase order) — never bypass a phase-sequence relay to "prove" it |
| **Noisier than it used to be** | bearings · a long-standing poor connection · winding distress — measure before it fails |

## 3. Measure, don't infer
- **Phases:** 400 V between each pair at the contactor during a start attempt.
- **Windings:** resistance of all **nine combinations** of the six leads, labels ignored — **the drawing is not the
  as-built** (`FA2402`'s delta is made in the wiring). Three equal pairs, no continuity between windings.
- **Insulation:** 500 V, each winding to earth: healthy > 100 MΩ, **< 1 MΩ not fit to run**.
- **Running:** clamp current on all three phases — similar, and below nameplate.
- State the meter range; a reading at the resolution limit is "unresolved", not a finding.

## 4. Recommission
Overload set to the nameplate (in the leg it actually sits in: delta-leg = phase current), rotation and **suction / output
at the machine**, balanced currents, **retighten every power terminal** and look for heat marks.

## 5. Record
Fault Log row (`414932606781316`): symptom as seen, cause **with the measurement that proves it**, retractions kept,
next steps. Change log. Never record a guess as a cause.
