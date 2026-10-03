---
name: pre-production-drawing-check
description: Darius's quality-control step before a cabinet job goes to the machines. Use when the owner asks to review or check drawings, a job folder, a cutting list or SmartCabinet/TpaCAD output (.TCN, worklist.xmlst, .fnm) — typically "review the … unit", "I have updated the … folder", "check before production", or anything placed in Workshop Raw/Review folder. Downloads every file, decodes the programs, checks parts against each other and against Blum data, and reports ✓ / ✗ / ? with the exact SmartCabinet fix.
---

# Pre-production drawing check

**The checklist and the reasons behind each item live in `Wiki/Processes/pre-production-drawing-check.md`. Read it
first, every time**: it is the governed copy (Drive is the source of truth), and this file is only how to run it.
The hardware figures come from the Blum articles in `Wiki/Processes/blum-*.md`.

## Run it

1. **Find the job folder** in Drive `Raw/Review folder/` (`1sSySf-DnGafA38Wz8rsjGxzBoAhqxAvE`). **List it; never filter by
   date.**
   ```
   composio execute GOOGLEDRIVE_LIST_FILES --account darius-googledrive \
     -d '{"q":"\"<folderId>\" in parents and trashed=false","fields":"files(id,name,md5Checksum,modifiedTime)","pageSize":100}'
   ```
   Save the list as `list.tsv` in a new scratchpad folder per round (`r1`, `r2`, …). On a re-review, `diff` the md5 column
   against the previous round.

2. **Download every file** (`GOOGLEDRIVE_DOWNLOAD_FILE` → `data.downloaded_file_content.s3url` → `curl`), and check each
   file's md5 against Drive's. All must match.

3. **Decode:**
   ```
   python3 .claude/skills/pre-production-drawing-check/tcn_decode.py <round folder> [--diff <previous round folder>]
   ```
   Read the cutting-list PDF too (`pdftotext -layout`; render a page with `pdftoppm` if the layout pages matter).

4. **Work through the checklist** (article §3, a–f). Do the arithmetic explicitly: sums along mirrored edges,
   side + gap = door, LW − 31, etc. Mark anything read off a drawing as *(drawing)*.

5. **Report to the owner** (article §4): **✓ Correct**, then **✗ To fix** with the exact SmartCabinet change and the
   files not to run, then **? Questions**. **Never guess intent; ask.** Never call a job ready with an open ✗ or ?.
   Keep it short; the details go in the change log.

6. **Record** (article §5):
   - a change-log section for the round;
   - the Processed-items row in `Outputs/kb-registers.md`;
   - any new hardware fact in its article.

   Re-read each control file's live Drive copy and compare it with git `HEAD` before editing. Upload in place
   (`GOOGLEDRIVE_UPLOAD_UPDATE_FILE`), download back, `cmp`, then commit and push.

## Boundaries (from the charter)

- Read-only on the owner's job files: **never delete, move or edit anything in `Raw/Review folder/`** unless asked.
- This check advises; **the owner decides** and does the SmartCabinet changes. Darius does not order hardware or
  commit the company to anything (§6a of `CLAUDE-Rules.md`).
- If the owner rejects a tool call, stop and wait.
