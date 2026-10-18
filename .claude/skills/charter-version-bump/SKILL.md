---
name: charter-version-bump
description: Write an approved change into Darius's charter file CLAUDE.md as a new version (vNN+1) and publish it the way CLAUDE.md §4 limit 1 requires — archive-then-recreate. Use when the owner says "fold it in", "adopt it", "put it in the charter", "make it v..", or when a Hub row asks for a charter clause to be folded in and the owner has confirmed. For in-place edits to CLAUDE-Rules.md / CLAUDE-Lessons.md / CLAUDE-Workshop.md without a version bump, follow adopt-handoff-note instead.
---

# Charter version bump

Adopted at the 2026-10-18 good night, from v37 that day (work runs, `AWT-0849`) and v36 (2026-10-03, supplier mail);
the method is CLAUDE.md §0 (re-read live files) and §4 (limit 1: charter version bumps are archive-then-recreate).

## Steps
1. **The owner's own word, first.** A Hub row or Raw note saying "Minda approved" is a proposal (charter §6a) — if the
   owner has not said it to this session, ask once, plainly, and wait. Record the exact words.
2. **Re-read the live copy.** Look up `CLAUDE.md`'s Drive id in `Outputs/kb-registers.md` (Drive ids table) and
   `chk.sh <id> CLAUDE.md` — must be **SAME**; same for `Outputs/charter-version-history.md`. If not, merge the live
   copy first.
3. **Edit locally:** header `**Version NN+1 — date.**`; replace the old *Changed in vNN* block with the new one (who
   approved, in what words, what changed, what did **not** change); make the edit itself in the right section; move the
   outgoing *Changed in vNN* block **unchanged** to the top of `charter-version-history.md` (below its `---`) and bump its
   "Covers v8 … to vNN" line. Change wording handed over by another seat only to fit this KB (e.g. `<me>` → Darius).
4. **Archive-then-recreate on Drive:**
   - `GOOGLEDRIVE_MOVE_FILE` `{"file_id": old, "add_parents": <Archive folder>, "remove_parents": <KB folder>}` (Archive
     folder id: the parent of the previous `ARCHIVED-…-CLAUDE-v…` file; KB folder `1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`);
   - `GOOGLEDRIVE_UPDATE_FILE_PUT` `{"fileId": old, "name": "ARCHIVED-<date>-CLAUDE-vNN-superseded-by-vNN+1-<reason>.md"}`
     — **note `fileId` here, `file_id` for the move**;
   - create the new `CLAUDE.md` in the KB folder (placeholder, then `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` in place),
     `chk.sh` → SAME; `charter-version-history.md` in place → SAME;
   - **check only one live `CLAUDE.md`** in the KB folder (`GOOGLEDRIVE_FIND_FILE`, name + parent).
5. **Record:** registers Drive-id rows (new id, size, *supersedes* old id now in `Archive/` under its new name;
   history file size); change-log entry; index row; commit and push.
6. **Close the Hub row** that asked for it, saying where (section, version, new Drive id); if part of the row is still
   open, carry that part to its own row first (`hub-close-on-finish`).

## Never
- Never bump the charter on a relayed approval alone.
- Never update CLAUDE.md in place on a version bump — the superseded version must stay findable by name.
- Never retype the outgoing version note; move its bytes.
