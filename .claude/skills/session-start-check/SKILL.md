---
name: session-start-check
description: Darius's start-of-session check, CLAUDE.md §0 and Rule A. Use at the first message of a session or day — "good morning", "good afternoon", "good evening", "hi Darius" — before any other work.
---

# Session start check

Adopted at the 2026-10-10 good night: that morning's start found `AWT-0147` assigned to Darius and **open for 13 days
unnoticed**. The order is CLAUDE.md §0; this file is how to run it quickly.

## Steps
1. **Hub, Rule A** — Tasks & Requests `8860839228606340`: `get_sheet_summary` filtered *Assigned to = Darius* and
   *Status in Open / In Progress / Blocked*. Note any row **older than a week**, and any that carries a **rule or
   decision to adopt** (`adopt-handoff-note`).
2. **Raw/** — run `raw-folder-check` step 1 (direct listing, newest first); read anything new.
3. **Workshop state** — Fault Log `414932606781316` rows not Resolved; Maintenance Schedule rows Red/Yellow
   (`6753985971226500`); the newest change log's "still open".
4. **Git** — `git fetch`; anything new on `main` (e.g. settings the owner changed) is merged before work.
5. **Report in one short list:** what's new, what's overdue, what's waiting on the owner. Then ask what's first.
   *Nothing new is a fine answer — say so in one line.*
