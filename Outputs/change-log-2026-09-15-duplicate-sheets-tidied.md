# Change log — 2026-09-15 — Duplicate Workshop Smartsheet sheets tidied

**Session 10.** Owner asked to tidy the duplicate Smartsheet sheets flagged during the
operational-systems build (Session 9) and recorded as an open question in `CLAUDE.md` §7.

## What was found

The `Workshop` Smartsheet workspace held **duplicate copies from initial setup**: Document Register
×3, Machinery Register - Database ×2, Tasks ×2 (Safety Check Log, Maintenance Schedule and Fault Log
were already single). Verified each candidate before recommending any deletion:

- **Keepers (hold the live data):** Document Register `838802392352644` (6 rows), Machinery Register -
 Database `1754351980906372` (5 rows, `FA2301`–`FA2305`), Tasks `4087584374523780` (14 rows,
 `T001`–`T014`).
- **Empty duplicates (verified bare — every one errored "Primary column not found", i.e. no columns
 and no rows):** Document Register `6339384188209028` and `4213753333811076`; Machinery Register
 `5132051701434244`; Tasks `73817177327492`.

## What was done

- The connector has **no delete-sheet or rename-sheet tool** (only row/column/attachment/comment
 deletes), so whole-sheet deletion can only be done in the Smartsheet UI. Handed the owner a verified
 keep/delete list with the exact permalinks of the four empty sheets.
- **The owner deleted the four empty duplicates in the Smartsheet UI.** Re-checked the workspace: it
 now holds **exactly one of each** — Document Register `838802392352644`, Machinery Register
 `1754351980906372`, Tasks `4087584374523780`, plus Safety Check Log `913380204480388`, Maintenance
 Schedule `6753985971226500` and Fault Log `414932606781316`. No data-bearing sheet was touched.
- Recorded in `CLAUDE.md`: §1 Live-data-sources now lists the surviving keeper ids and marks the
 housekeeping note resolved; §6a notes that deleting whole sheets is a UI action the owner takes; §7
 open question marked **RESOLVED 2026-09-15**.

## Judgement calls

- **Verified emptiness before recommending deletion** rather than trusting the sheet names — identical
 names made this essential; deletion of a Smartsheet sheet cannot be undone via the API.
- Nothing in the KB referenced the empty duplicates (all Wiki/register references already pointed at
 the keepers), so no repointing was needed after deletion.
