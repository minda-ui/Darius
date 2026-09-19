---
title: "Troubleshooting & fault-log system"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - Smartsheet Workshop / Fault Log (sheet 414932606781316)
related:
 - troubleshooting-hebrock-f4.md
 - troubleshooting-altendorf-f45.md
 - ../Processes/machinery-maintenance-system.md
---

# Troubleshooting & fault-log system

How unplanned faults are diagnosed, fixed and remembered. Two parts, same pattern as everything else
in this KB — **Smartsheet is the live record; the Wiki holds the reusable know-how.**

## 1. Fault Log (Smartsheet)

Sheet **Fault Log** (`414932606781316`) in the Workshop workspace — one row per fault:
`Fault ID` (FL-###) · `Machine ID` · `Date Reported` · `Reported By` · `Symptom` (what was seen) ·
`Category` (Mechanical / Electrical / Control-error-code / Quality defect / Safety / Other) ·
`Probable cause` · `Remedy / action` · `Status` (Open / In Progress / Monitoring / Resolved) ·
`Date Resolved` · `Downtime` · `Reference` (the troubleshooting article + manual section) · `Notes`.

**Health** (RYGB) is automatic from Status: **Red** = Open, **Yellow** = In Progress, **Blue** =
Monitoring, **Green** = Resolved. So the sheet shows open faults at a glance, and a filter on `Machine
ID` gives a machine's fault history.

## 2. Per-machine troubleshooting reference (Wiki)

Each machine has a troubleshooting article holding its manufacturer fault table(s) and any faults we
have actually diagnosed here:

- `troubleshooting-hebrock-f4.md` — the F4 fault table plus the resolved corner-rounding incident.
- `troubleshooting-altendorf-f45.md` — the F45 mechanical fault table and the full ElmoDrive
  error-code list.

## The loop

1. A fault occurs → raise a **Fault Log** row (Status Open). Photograph the defect and the machine
   state; attach or link the photos.
2. Diagnose using the machine's troubleshooting article first (its fault table usually names the
   symptom). Record `Probable cause` and the fix tried; move Status to In Progress.
3. When fixed, set Status Resolved + `Date Resolved`. If the fix or the diagnosis **differed from the
   manual**, add that lesson to the machine's troubleshooting article — that is how the reference gets
   better than the manual over time (the corner-rounding incident is the first example).
4. If a fault recurs or points at a maintenance gap, add/adjust a task on the **Maintenance Schedule**.

## Safety first, always

A fault that involves a guard, an interlock, an E-stop, a limit switch or exposed live parts is a
**stop-work item for that function until fixed** — log it, lock the machine out, and treat it as unsafe
to use, do not "run it carefully". This mirrors the F45 monthly safety-check rule
(`../Processes/f45-monthly-safety-device-check.md`). Electrical faults and control-cabinet work are for
a qualified electrician / the manufacturer's technician, not the operator.

## Boundaries

Diagnose and record only. Do not commit the company to a repair contract, and do not contact the
manufacturer on the company's behalf without the owner's say-so (`CLAUDE.md` §6a). Surface the fault
and the recommended action.

## Sources

- Smartsheet **Workshop / Fault Log**, sheet `414932606781316`.
- Each machine's manual fault table, cited in the per-machine troubleshooting articles.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created with the Fault Log sheet and the two per-machine troubleshooting references (FL-001 seeded from the resolved Hebrock corner-rounding incident) | Session — workshop operational systems build |
