---
name: pre-production-drawing-check
description: Darius's quality-control step before a cabinet job goes to the machines. Use when the owner asks to review or check drawings, a job folder, a cutting list or SmartCabinet/TpaCAD output (.TCN, worklist.xmlst, .fnm) — typically "review the … unit", "I have updated the … folder", "check before production", or anything placed in Workshop Raw/Review folder. Downloads every file, decodes the programs, checks parts against each other and against Blum data, and reports ✓ / ✗ / ? with the exact SmartCabinet fix. Also use when the owner says "SmartCabinet won't let me change it" / "can you update the … file" (hand-edit a program), and when a unit is released to the Vitap ("how do I load it", "running it now").
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

## Learned 2026-10-22 (corner wall unit, rounds 1–3)

- **Folders get replaced in place.** The owner may overwrite files in the same folder ("v3" in the `v2` folder). Always
  diff the md5 list against the previous round, whatever the folder is called; name rounds `r1`, `r2`, … yourself.
- **TpaCAD-saved files.** A file saved in TpaCAD carries the header `TPA\ALBATROS\EDICAD\02.00` (UTF-16, `tcn version`
  2.9.x) instead of SmartCabinet's `01.00`. The decoder can miss parameters in it (on 22/10 the `foro mul` rows showed no
  start, depth or Y). **Never pass a row the decoder could not read**: say so, and ask for the rows to be checked in
  TpaCAD or re-exported from SmartCabinet. Convert with `iconv -f UTF-16 -t UTF-8` to read the raw lines.
- **Spacing is frame-independent.** When parts are measured from different references, compare the **spacing** between
  joints/pins on the two mating parts (e.g. side 126 vs shelf 107) before arguing about absolute positions.
- **Ask what the pockets are for.** Cabineo pockets in a shelf may be **shelf pins** (loose shelf), not connectors.

## Hinge plates and angled hinges (learned 2026-10-26, corner unit)

The corner unit's side plate pilots were at **56 mm** from the front edge; Blum's planning drawings say **37**. Three
review rounds passed it; it showed only when the door was hung. **Every hinged unit:**
- plate pilots on the side at **37 mm** from the front edge (0 mm plate), 32 apart, level with the door cups
  (door cup X − door/side offset = side X);
- for **angled hinges**, name the Blum case from the angled-applications overview (catalogue p.116): half overlay
  (+45° I, Nº 53, square side, door set back, FB = LW), overlay (+45° II, Nº 9) or inset (+45° II, Nº 24, 18 mm plate) —
  **the +45° II cases draw a bevelled side**; square Hebrock-edged sides mean +45° I;
- state **where the door sits** against the top and bottom (in front of them, or set back with them cut back). A plate
  depth that implies a different door line from the carcase is a ✗.

## Hand-editing a program when SmartCabinet won't (learned 2026-10-23, corner unit door and v5)

1. **New folder, never in place**: `Raw/Review folder/<unit> vN (Darius - <what changed>)`. Never edit the owner's
   folder or write to the `Furniture` machine folder.
2. Start from the **SmartCabinet** files (header `EDICAD\01.00`), not a TpaCAD re-save.
3. Keep the encoding: **UTF-16 LE with BOM**. Edit with a script, never retype a file.
4. Change **only** the lines needed, and keep the three sources in step:
   - a size: program header (`DL/DH/DS`), the `SIDE#…` face size (`HF`…) **and** the `worklist.xmlst` row;
   - removing machining (e.g. Cabineo pockets `W#89/2201/2111`): delete those lines only; count them before and after.
5. `diff` old vs new line by line (only the intended lines differ), re-decode with `tcn_decode.py`, md5 every file
   after upload against local.
6. Tell the owner the caveats: a hand edit **diverges from the SmartCabinet model** (a re-export brings the old value
   back); the saw size comes from the cutting list, so it must match; dry-fit before production. Where SmartCabinet
   itself is wrong, draft a ticket (`Outputs/…-smartcabinet-ticket-….md`) for the owner to send.

## Releasing a unit to the Vitap (owner-tested 2026-10-23)

End every release note with how to load it: in **WSC ListsManager open the unit's `worklist.xmlst`** — every program
loads as one list (13 parts for the corner unit). Then check: **the version in the path** (a v2 file was loaded by
mistake on 23/10), the row count against the folder, any hand-edited size (e.g. door 370.5), and **Mirror unticked**.
Facts: `Wiki/Processes/library-batch-production.md` (*Loading a unit on the Vitap*).

## Boundaries (from the charter)

- Read-only on the owner's job files: **never delete, move or edit anything in `Raw/Review folder/`** unless asked.
- This check advises; **the owner decides** and does the SmartCabinet changes. Darius does not order hardware or
  commit the company to anything (§6a of `CLAUDE-Rules.md`).
- If the owner rejects a tool call, stop and wait.
