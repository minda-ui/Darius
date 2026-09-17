---
title: "Machinery maintenance system (routine maintenance)"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - Smartsheet Workshop / Maintenance Schedule (sheet 6753985971226500)
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Machinery/altendorf-f45-panel-saw.md
related:
 - maintenance-schedule-hebrock-f4.md
 - maintenance-schedule-altendorf-f45.md
 - f45-monthly-safety-device-check.md
 - ../Troubleshooting/troubleshooting-and-fault-log-system.md
---

# Machinery maintenance system (routine maintenance)

How routine, planned maintenance of the workshop machinery is scheduled, tracked and evidenced.
It is deliberately built the same way as the F45 safety check: **Smartsheet is the live record; the
Wiki narrates and cites it.**

## The three sheets (Smartsheet workspace "Workshop")

| Sheet | What it holds | Health colour |
|---|---|---|
| **Maintenance Schedule** (`6753985971226500`) | One row per recurring maintenance task, per machine — cleaning, lubrication, inspection, wear-part and battery changes. The **plan** and the **last-done log** in one place. | RYGB by due date |
| **Safety Check Log** (`913380204480388`) | The F45's mandatory monthly documented safety-device check (separate because it is a legal check, not general upkeep). See `f45-monthly-safety-device-check.md`. | RYGB by pass/fail |
| **Fault Log** (`414932606781316`) | Unplanned breakdowns / faults and how they were fixed — the troubleshooting side. See `../Troubleshooting/troubleshooting-and-fault-log-system.md`. | RYGB by status |

## How the Maintenance Schedule works

Each row is one recurring task with a **Category** (Daily / Weekly / Monthly / Quarterly / Annual /
Hours-based / Condition-based), an **Interval (days)** where the cadence is calendar-based, a
**Last Done** date, and a **Reference** back to the per-machine schedule article and manual section.

Two columns are **automatic** (column formulas — maintain them via the connector, never by hand):

- **Next Due** = `Last Done + Interval (days)` (blank until a task is first logged, or where no fixed
 interval applies).
- **Health** (RYGB): **Blue** = no due date yet (a Daily/Weekly habitual task, a Condition-/Hours-based
 task, or one never logged); **Green** = due more than 14 days away; **Yellow** = due within 14 days;
 **Red** = overdue.

**To use it:** when a task is done, put the date in **Last Done** (and initials in Assigned To). Next
Due and Health recompute. That is the whole loop. Daily/Weekly cleaning tasks are listed for
completeness but left un-dated (Blue) — they are habitual; date-log them too only if you want the
evidence trail. The compliance- and cost-critical periodic items (monthly, annual electrical check,
2-yearly battery, etc.) are the ones worth keeping green.

Cell history on each row is itself the maintenance log — every Last-Done change is timestamped and
attributable. Photos or service reports can be attached to the row.

## What's loaded now

23 tasks: **FA2301 Hebrock F4** (MT-001…MT-014) and **FA2303 Altendorf F45** (MT-020…MT-028), taken
from each machine's manual (Chapter 7 "Maintenance / Wartung und Pflege" and the safety chapter's
annual electrical check). Details and the source rows are in the two per-machine schedule articles.

**Not yet loaded:** `FA2302` (Inventair MK1 MTFA extractor — manual pending) and any newly-found
machine (a **Vitap K2 2.0 CNC boring machine** and an **Inventair MK2 MTFA** appear on purchase
invoice 100154 in `Raw/`, not yet registered as assets — see the change log and CLAUDE.md §7). Add a
block of rows per machine as each is processed in.

## Boundaries

This system records and schedules maintenance; it does not authorise spend or commit the company.
Replacing a wear part, booking the electrician's annual PTC check, or ordering spares is an
owner/operator decision (see `CLAUDE.md` §6a). Always maintain with the machine **switched off and
locked out** — every machine manual makes that a precondition (see each Machinery article's Safety
section).

## Sources

- Smartsheet **Workshop / Maintenance Schedule**, sheet `6753985971226500` — the live schedule.
- `../Machinery/hebrock-f4-next-edge-bander.md` and `../Machinery/altendorf-f45-panel-saw.md` —
 manual-derived maintenance content, with per-source citations.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created with the Maintenance Schedule sheet and the two per-machine schedules; part of the maintenance + troubleshooting + SmartCabinet system build | Session — workshop operational systems build |
