---
title: "Troubleshooting — Hebrock F4 (FA2301)"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - ../../Raw/part 5.pdf
 - ../../Raw/2026-09-15_fault-photo_edge-bander-corner-gouge-defect.jpg
 - ../../Raw/2026-09-15_fault-photo_edge-bander-corner-rounding-fixed.jpg
related:
 - troubleshooting-and-fault-log-system.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Processes/maintenance-schedule-hebrock-f4.md
---

# Troubleshooting — Hebrock F4 edge bander (`FA2301`)

Fault reference for the F4. Diagnose from the machine's own fault table (manual §8.2 "Störungstabelle",
`part 5.pdf`, p.183) first; log every fault on the **Fault Log** (`414932606781316`). **Lock the
machine out before clearing any fault or adjusting any station.**

## Manufacturer fault table (§8.2) — edge-quality faults

The manual's §8.2 table pairs each symptom (Störung) with a cause (Ursache) and fix (Abhilfe). The one
transcribed so far — because it matched a real defect here — is the corner-rounding fault:

| Symptom | Cause | Fix |
|---|---|---|
| Corner radius looks "hakelig" (jagged), possibly with edge overhang | Corner-rounder **stop screw out of adjustment** | Loosen the locknut, unscrew the stop screw slightly so the feeler ring (Abtastring) protrudes ~0.2 mm+ into the workpiece line, retighten the locknut |

For any other symptom (glue-line defects, overhang, buffing marks, feed problems), read the full §8.2
table in `part 5.pdf` before adjusting — and add the row here once you've used it, so this reference
grows into the full table over time.

## Resolved faults (worked examples)

### FL-001 — Corner-rounding router producing a bad corner (2026-09-15, RESOLVED)

**Symptom:** visible gouge/chip-out in the edge band at the workpiece corner, on the corner-rounding
station (HMI icon: two rollers converging on a corner). Photo `…corner-gouge-defect.jpg`.

**Diagnosis:** matched the §8.2 row above — stop screw out of adjustment.

**What actually worked (and why it's recorded):**
1. First adjustment backed the stop screw *out* per the manual's wording → **overcorrected**: the
   station stopped rounding and left rub/scuff marks.
2. Second adjustment reversed direction — turned the stop screw back *in* a small increment from the
   overcorrected position, and re-tested → **fixed**, clean radius on both edges
   (`…corner-rounding-fixed.jpg`).

**Lesson:** the fault table's stated direction (back the screw *out* to add engagement) did **not**
match what worked in practice — the correct setting sat between the original mis-set position and the
overcorrected one. **Treat the manual's stated direction as a hypothesis; adjust in small reversible
steps with a test cut after each, not one confident move.** Not investigated further once resolved, but
if this recurs, also check: workpiece squareness/minimum length, vertical-slide throttle-valve speed,
and feeler-shoe glue/debris build-up. (Task T006 closed.)

## Preventive links

The daily clean of the trim-saw/corner-rounder (MT-003), weekly guide-shaft oiling (MT-007) and
protecting the corner-router feeler shoes/rings from glue build-up all reduce corner-quality faults —
see `../Processes/maintenance-schedule-hebrock-f4.md`.

## Sources

[^1]: [Hebrock manual, part 5](<../../Raw/part 5.pdf>) — ch.8 fault table (§8.2, p.183)
[^2]: [Fault photo — corner gouge](<../../Raw/2026-09-15_fault-photo_edge-bander-corner-gouge-defect.jpg>) — owner-provided 2026-09-15
[^3]: [Fault photo — corner fixed](<../../Raw/2026-09-15_fault-photo_edge-bander-corner-rounding-fixed.jpg>) — owner-provided 2026-09-15

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created; §8.2 corner-rounding row + resolved incident FL-001 carried over from the machine article's Incidents section | Session — workshop operational systems build |
