---
title: "Process: Altendorf F45 monthly safety-device check"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
  - ../../Raw/F45 part 1.pdf
related:
  - ../Machinery/altendorf-f45-panel-saw.md
---

# Process: Altendorf F45 monthly safety-device check

The F45's own operating manual makes this a mandatory, documented monthly check — not a
recommendation. Its exact words: **"Carry out and document this check 1x month!"** [^1]

## What to check, every month

1. **E-stop response** — both/all E-stop buttons trip the machine correctly.
2. **Sliding-table limit switch** — functions correctly.
3. **Chip-duct / plate limit switch** — functions correctly.
4. **ON/OFF switch cleanliness** — switch is clean and undamaged.
5. **Protective hood condition** — hood is intact, correctly fitted, and its interlock (if
   equipped) functions.

Each item is a Pass/Fail/N-A entry.

## Where to log it

Smartsheet workspace **Workshop**, sheet **"Safety Check Log"**. One row per check:

- `Machine ID`: the asset code (`FA2303` for this machine — the sheet can log checks for any
  machine that needs one, not just this one).
- `Check Date`, `Checked By`.
- The five Pass/Fail/N-A columns above.
- `Evidence Link`: a Drive link to photo evidence, or attach the photo(s) directly to the
  Smartsheet row (Smartsheet supports row-level attachments).
- `Notes`: anything found, even if it didn't affect the Pass/Fail result.
- `Health` computes automatically (green if every item is Pass, red if any item is Fail, yellow
  if anything is left blank or N/A) and `Next Check Due` computes automatically as 30 days after
  `Check Date`.

## If something fails

A Fail on any item is a stop-work item for that function until fixed, per the manual's own
lockout/safety-device rules (`Wiki/Machinery/altendorf-f45-panel-saw.md`, Safety section) — do not
just log the failure and carry on. Raise a Smartsheet Task against the relevant asset code and
treat the machine's use of that function as unsafe until resolved.

## Status

No check has been logged yet as of 2026-09-15 (machine just registered into this KB). First check
is tracked as Smartsheet Task **T008**.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created alongside the Altendorf F45 registration | Session 6, entry "Altendorf F45 registered" |

## Sources

[^1]: [F45 manual, part 1](<../../Raw/F45 part 1.pdf>) — §4.6.4, monthly protective-device check
