# KB registers

Standing index for the Workshop of Furniture Making Knowledge Base. Read `../CLAUDE.md` §0 before
using this file.

**This file holds only what is still live** — the open Processed items, and every row added since the
2026-09-28 snapshot. **Everything settled is in a dated snapshot** and is never re-emitted:

| Snapshot | Holds | Provenance |
|---|---|---|
| `Outputs/kb-registers-snapshot-2026-09-21.md` | the registers as they stood at the end of Session 19 — 30 Processed items, 33 Wiki structure changes, 51 Outputs produced | the bytes that were on Drive, 65,449 B, byte-identical to git `d4cd712`; **not retyped and not rebuilt** |
| `Outputs/kb-registers-snapshot-2026-09-27.md` | the registers as they stood at the end of 2026-09-24 — the same 9 open Processed items, 1 Wiki structure change, 8 Outputs produced | the bytes that were on Drive, 23,678 B, byte-identical to git `0283bee`; **renamed, not rewritten** |
| `Outputs/kb-registers-snapshot-2026-09-28.md` | the registers as they stood at the end of 2026-09-27 — the same 9 open Processed items, 1 Wiki structure change, 8 Outputs produced, and the 2026-09-27 Drive-id table | the bytes that were on Drive, 29,143 B; **renamed, not rewritten** |

**Snapshotted 2026-09-28, discharging what the previous version of this header instructed.** It had been
carried to **29,143 B** — past the ~25 KB rule — and said so in as many words: *"the next session must
snapshot this file before adding anything."* Done before a single row was added, and the name it warned
was taken (`-snapshot-2026-09-27.md`) is sidestepped by the date. The method is the one used twice before:
**the Drive file was renamed and the live file rebuilt by script from it**, so no table row was retyped.

**The nine open Processed items appear in every snapshot as well as here, and this file is authoritative
for them.** A Processed item leaves only when it settles, so an open row is copied forward each time —
in a snapshot with the status it had on that date, here with its current one. *Recorded rather than left
to be discovered: it is now true of three snapshots, and it will be true of the next.*

**Why it is split this way** (owner's instruction, 2026-09-23, *"split by period"*). Drive has no patch
API, so a whole file is re-emitted for one new row. Splitting by table would not help — all three tables
are append-only and every session touches at least one. Splitting by period does, because a settled row
is never touched again. **When this file passes roughly 25 KB, snapshot it again.**

*From v32 (2026-09-28) the re-emission itself is cheaper — content on disk can be uploaded in place — but
**that does not relax this rule**. The ~25 KB threshold is about a file being readable and a row being
findable, not about the cost of a write; and a period snapshot is exactly the case §4's limits clause
keeps on archive-then-recreate, because a snapshot has to be findable by name.*

*The cost of renaming rather than rewriting is that each snapshot keeps the header it had when it was
live, so it still describes itself as the file `CLAUDE.md` §0 sends you to. It does not. The filename and
this table are authoritative.*

**2026-09-16 — reconciled.** Two parallel session-lines (an operational-systems line and a CAD-day
line) had each kept their own copy of this file; they are merged here into one timeline. Sessions are
renumbered chronologically by the actual change-log file timestamps, so "Session 9/10" no longer means
two different things. See `change-log-2026-09-16-fork-reconciliation-and-darius.md`.

## Change-log entries

**Moved to `Outputs/change-log-index.md` at v28 (2026-09-21)**, and that file is itself period-split as
of 2026-09-23. `CLAUDE.md` §0 and §4 point there.

## Processed items

Status legend: `pending` = registered, not started · `partial` = started, work remains ·
`done` = fully reflected in the wiki · `skipped` = deliberately not processed.

**Open items only — 9 rows**, carried forward verbatim from the 2026-09-28 snapshot.

| Raw path | Processed (date) | Status | Wiki articles created / updated | Notes |
|---|---|---|---|---|
| `Raw/Invoice 100154 - 09.11.23 - OCN231185 - Balance.pdf` | 2026-09-15 | partial | Machinery/vitap-k2-panel-saw | Purchase date/price for FA2304 (full price confirmed); also revealed FA2305 (Inventair MK2 MTFA), registered in Smartsheet only pending its own manual. |
| `Raw/TPA CAD part 1.pdf`-`part 2.pdf` | 2026-09-15/16 | partial | Machinery/vitap-k2-panel-saw, Processes/tpacad-tool-type-optimizer-ambiguity | Confirmed abridged extract of a larger manual; documented the Blind-bore-drill tool-ambiguity fault; confirmed CN Tools/Cam Table isn't covered in this manual at all. Complete `TpaCad.pdf`/`Workings.pdf` not yet obtained (Task T015); fix refined but still not fully tested (Task T016). |
| `Raw/td-4210d_4410d_4420dn_4520dn_uke_ug_a.pdf` | 2026-09-17 | partial | Machinery/brother-td-4420dn-label-printer | Brother TD-4420DN label-printer User's Guide (covers TD-4210D/4410D/4420DN/4520DN). **Only pages 1-77 of 128 extracted** — the Specifications appendix, Routine Maintenance and Troubleshooting did not come through. Confirms direct thermal, LAN on the DN, 832-dot print width, media handling and Brother's own fade/dust warnings; **no mention of ZPL anywhere**, contradicting reseller listings. Printer **registered as `FA2401`** later the same session, once its order receipt evidenced acquisition year 2024. |
| `Raw/AES Extractor.pdf` | 2026-09-17 | partial | Machinery/aes-saf-10000-stk-extractor | **Control-panel electrical schematic**, not an operating manual — drawn for **SAF Technical Ltd**, which looked like an unidentified third party until the quotation showed "SAF" is part of the product designation. No maintenance intervals, no fault table, so it does not let `FA2402` join the Maintenance Schedule or Fault Log. |
| `Raw/Emailing S Series User Manual(Dust Collector-EN) - Flipbook by RENNA _ FlipHTML5(1).PDF.pdf` | 2026-09-17 | partial | Machinery/aes-saf-10000-stk-extractor; Suppliers/aes-group | **AES GROUP S Series Mobile Units User Manual**, 18.6 MB, owner-supplied in response to the standing request for an AES manual for `FA2402`. Covers S-2000…S-10000. **NOT accepted as `FA2402`'s manual**: right manufacturer, and the quotation's 64 filters at Ø160×940 mm compute to 30.24 m² against 30.22 quoted (0.07% — my arithmetic), confirming **cylindrical sleeve filters** and this manual's filter family; **but** it is titled for *mobile, plug-connected, bag-collecting* units while `FA2402` is fixed, hard-wired, star-delta, 720 kg with three metal buckets, its designation is `STK` not `S-`, and **the extracted technical table stops at S-6500 — the S-10000 row was never seen** (possibly extraction loss, not checked against the original). Yielded real value regardless: **manufacturer contact details** incl. AES Europe BVBA in Genk, Belgium; 10-year stated service life; **12-month warranty from completion of assembly** (long expired); ambient and supply limits; a generic check list and an 11-row fault table. Still missing what matters: filter-change interval, star-delta procedure, Part Holder, hours-based servicing. |
| `Raw/20260918_070518.jpg` | 2026-09-18 | **partial** | none | Identified by the owner as the **boilerplate plate on the air receiver** — the document that would close **T021** (whether the receiver needs a written scheme of examination). **Could not be read**: `read_file_content` returned empty twice at 2.9 MB where a 1.56 MB image read fine, so size is the likely cause. **Nothing inferred from its existence.** T021 records the six figures wanted; a smaller or cropped re-photograph closes it. |
| *(no Raw item — the owner's Drive `Furniture` folder, read not ingested)* | 2026-09-18 | partial | Software/kitchen-unit-library; Processes/carcase-fixings-cabineo-x-vs-confirmat | `AMFA Wall Unit 600 RH`'s `worklist.xmlst`, `03-BOTTOM.TCN`, `01-SIDE-LEFT.TCN` and `08-DOOR-1.TCN` decoded, plus the `300mm` and `600mm Wall unit` worklists for comparison. **Not `Raw/` items and not copied into the KB** — the folder is the owner's working area, outside this KB's tree, and the two `ANVAR_KITCHEN_*` folders were **not opened** as probable client data. |
| *(no Raw item - the owner's Drive `Furniture` folder, re-listed not ingested)* | 2026-09-20 | partial | Software/kitchen-unit-library; Wiki/index.md | The folder re-listed after the owner said the library had been updated: **18 subfolders against 7 on 2026-09-18**, sixteen library units. Three `worklist.xmlst` files and one `03-BOTTOM.TCN` downloaded as exact bytes and decoded - **heights measured from the part sizes, not read off the folder names**. Established two height families (**720** and **900**), that an unsuffixed name means both, that the new units carry **no nesting sheets**, that the **255 mm shelf holds across widths and heights**, and that **T016's `#1001=0` condition is unchanged in a unit built after the prediction was written**. **Second pass the same day**, on the owner's observation about the sides: `01-SIDE-LEFT.TCN` from `300 LH 900` and from `500 LH 900 high`, and `02-SIDE-RIGHT.TCN` from `300 RH 900`, downloaded as exact bytes and diffed - the first pair **byte-identical**, the third a **mirror about the panel centre differing by one character**. **Not `Raw/` items and not copied into the KB** - the folder is the owner's working area, outside this KB's tree, and the two `ANVAR_KITCHEN_*` folders were **not opened** as probable client data. |
| `Raw/Albatros-help-en-GB-2026-09-23/` (29 files, copied from `C:\Albatros\help\en-GB\` on the Vitap's own PC) | 2026-09-23 | partial | Processes/tpacad-tool-match-criteria; Processes/tpacad-blind-bore-tool-id-fix (superseded); Processes/tpacad-tool-type-optimizer-ambiguity (corrected); Machinery/vitap-k2-drill-head-tooling | **Closes T015.** All three "sibling manuals not present in `Raw/`" named by the 2026-09-15 article, plus the complete `TpaCAD_eng.pdf` the scan's own first page pointed at. **`Workings_eng.pdf`** (`11oEu1FlzMdb9h0c-iqFvQA-ELLJIwb1L`, 3,728,330 B, 337 pp) and **`CnCadOpti_eng.pdf`** (`1fm4v-f8u6suiR3fBULQxbI72jU3OmU_I`, 758,979 B, 19 pp) downloaded as exact bytes, verified `wc -c` both sides, extracted to text locally. `CnCadOpti` - **which nobody knew existed** - is what corrected T016's root cause. **Still unread: `TpaCAD_eng.pdf` (7.7 MB), `TpaCadNt_eng.pdf`, `TpaCadAD_eng.pdf`, `TpaCadMD_eng.pdf`, `DxfCAD_eng.pdf`, `DxfToTpa_eng.pdf`, `PzaToTpa_ENG.pdf`, `CadIso_eng.pdf`, `TpaLangs_Eng.pdf`, `TpaWorks_eng.pdf` and 9 `.chm` files.** The `Z`-datum question (shoulder or tip) is expected in `TpaCAD_eng.pdf` |

## Wiki structure changes

**Everything since the 2026-09-28 snapshot.** Earlier rows are in the snapshots above.

*No Wiki article was created, moved or retired on 2026-09-28. The charter is not a Wiki article; the v32
amendment is in the Outputs rows below.*

## Outputs produced

**Everything since the 2026-09-28 snapshot.** Earlier rows are in the snapshots above.

| Output path | Date | Built from (wiki articles) | Requested by |
|---|---|---|---|
| **`CLAUDE.md` amended to v32 — in-place Drive update adopted as the default, with the limits clause** (22,734 -> **23,171 B**). §1 gains **"How a file on Drive is changed"**: Drive still has no partial-patch API, *but the replacement bytes no longer have to be retyped*. §4 gains **"How a change reaches Drive"** — the in-place default, the **unchanged** verification rule (`download_file_content` -> decode -> `diff`, **the verifier stays the native connector** so both halves of a byte-check do not depend on one tool, and **the revision count** where content is meant to be identical), and archive-then-recreate **demoted to a fallback but still mandatory** for three named cases: a superseded copy that must be **findable by name**, superseded bytes that **must survive** (`keepForever` is `false` by default), and **anything outside what has been proven** — above 37 KB, across the ~82 KB `read_file_content` cliff, binary, Google-native, or not owned by this account. **The clause bit on its own first use**: a charter version bump is exactly case 1, so **v31 was archived by rename and v32 recreated** — the new default's own adoption took the fallback. *The proposal's recommendation was "adopt with the limits clause" and the limits are the part that earned its keep; the gain was never durability, it was removing the hand-retyping error class that produced this KB's one-byte and four-byte shortfalls.* | 2026-09-28 | no article; §1 and §4 of `CLAUDE.md` | Owner (Minda): *"The in-place-update proposal ... recommendation is adopt with the limits clause. Go ahead"* |
| **`Outputs/charter-version-history.md`** (41,311 -> **44,930 B**) - the v31 note (3,619 B incl. its separator) moved in **verbatim**, and the coverage line advanced to *"v8 (2026-09-16) to v31 (2026-09-23)"*. **Took the fallback too, on case 3**: at 44,930 B it is above the 37 KB in-place update has actually been proven at, and *the limits clause is worth nothing if the session that wrote it reaches past it on the same day.* | 2026-09-28 | no article; the charter's version history | Follows the v32 bump (§4's own rule) |
| **`Outputs/kb-registers.md` snapshotted at 29,143 B** to `Outputs/kb-registers-snapshot-2026-09-28.md`, and this live file rebuilt from it by script. **The previous header ordered this** in as many words and the order was carried out before any row was added. *Third time by the same method: rename the Drive copy, rebuild live from the bytes, retype nothing.* | 2026-09-28 | no article; §4 of `CLAUDE.md` | This file's own ~25 KB rule |

### Drive ids after the 2026-09-28 publishes

**A content change mints a new id wherever archive-then-recreate is used** — which from v32 is the
fallback, not the default, so this table will shrink as in-place updates take over. *Both of today's
charter publishes took the fallback and so both have new ids; the ids below supersede any earlier ones for
the same path.*

| Path | Bytes | Drive id |
|---|---|---|
| `CLAUDE.md` | **23,171** | `1ASSqd9_JWdt5eoCBY02eevVsZbrbLpDg` — v32; *supersedes `1rhOR_BnN1V3JTLmC8FI3n8ykwgC5vWw8`, now `Archive/ARCHIVED-2026-09-28-CLAUDE-v31-superseded-by-v32-drive-in-place-update.md`* |
| `Outputs/charter-version-history.md` | **44,930** | `15H9mZLcdSjsT6h1MRlSuN_GBg1fO0GGK` — *supersedes `1iKqygJJHEGN0vKsYp53PyBKgepIqjilb`, now `Archive/ARCHIVED-2026-09-28-charter-version-history-before-the-v31-note-was-moved-in.md`* |
| `Outputs/kb-registers-snapshot-2026-09-28.md` | 29,143 | `1veAsc6qbfQu-XDVsUe1UJ9UhcOEmpTmY` — **id unchanged**, renamed not rewritten; this is the id `kb-registers.md` carried while live |

*Both Drive copies were verified byte-identical to git `HEAD` **before** being archived, not after — the
2026-09-27 session found a charter file that a merge had silently reverted in git, and an archive of the
wrong bytes is worse than no archive. Both matched.*

*Two files are deliberately absent, for the same reason as last time: **this one** and
`Outputs/change-log-index.md`. Both are re-emitted after this table is written, so each would have to
contain an id minted by its own publish. `CLAUDE.md` §0 finds both by name, not by id.*
