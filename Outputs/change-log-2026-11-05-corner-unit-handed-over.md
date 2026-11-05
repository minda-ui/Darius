# Change log — 2026-11-05 — corner unit fitted; session start

Darius, session 44.

## 1. Session start
- Hub: Darius rows unchanged except **new `AWT-1116`** (Eugene, barcode scanners in production — questions in Raw,
  `1R2GxCrTSOeddnT9CbNSAj3dkuZAzmJ45`). Raw: two files 04/11 15:26, `FC2614 - Fishbone price on Macdonald cost plan
  23.10.26 (labour only)` (.pdf, .xlsx) — not obviously workshop; asked the owner. Fault Log: nothing open. `main`
  already merged. Composio CLI still not signed in — 03–04/11 Drive publish still pending.

## 2. Corner wall unit — fitted on site
- Owner sent three photos of the unit fitted beside the cooker hood (dark grey matt fronts, bar handle on the neighbour),
  then: *"This is done today"*.
- Darius's read of the photos, given to the owner as a snag list, **not** a fault: the door stands off the carcase at
  the bottom (depth cam), the gap to the neighbouring door tapers to near-touching at the bottom and the two fronts are
  not in one plane (side screw / depth cam), handprints on the matt fronts. Adjustment is on the Blum hinges (±2 mm
  each way); also check the hood/duct is not touching the door.
- **Open item closed:** the corner unit (+45° hinge, 370.5 door question since 26/10) is **fitted** as of 05/11. Which
  hinge went on was not stated in this session.
- Owner: *"It is hand it over. We need to come back later to drawing board, because this unit is look horrible"* —
  **handed over to the client 05/11**; the owner is not happy with how it looks. **Open: redesign the 600 × 600 corner
  wall unit** before it is made again (library unit). Inputs to bring to that session: the 05/11 photos (door stands
  off the carcase, uneven/near-touching gap to the neighbour, fronts not in one plane next to the hood); the hinge
  history 22–26/10 (plates at 56 → 37, door 420 → 370.5 → 365.1, +45° I vs +45° II, square vs bevelled side —
  `change-log-2026-10-24-…`, `…-10-26-corner-door-45II.md`); `new-library-unit-design` as the method.

## 3. FC2614 in workshop Raw — not workshop work
- The two Raw files (`1m8f2QyW40s_69N2SboQ0BVbNrMfaoyey` PDF 62,003 B, `1OjIzdIYAVdrnSg8Pzg084ZIBVTbsXpK2` xlsx
  41,781 B; md5 = Drive) are a **Fishbone Construction** labour-only tender draft (Anna v0.9, not issued).
- Owner: *"Ignore it; that's our project for labour supply only"* — **not processed, not filed, not copied into this KB**;
  left where it is in `Raw/` (moving or deleting the owner's upload is the owner's call).

## 4. AWT-1116 — barcode scanners in production, facts to Eugene
- Owner: *"yes, go ahead with Eugene"*. Eugene's note (`1R2GxCrTSOeddnT9CbNSAj3dkuZAzmJ45`) asks 7 questions for a
  group scanner choice (InvenTree stock, Snipe-IT assets).
- KB gathered by an Explore agent (barcode article, printer article, CLAUDE-Workshop T022, layout plan, Anna HSE note).
  Reply written facts-and-gaps; **re-read against the sources and four lines cut back** (a "both hands at every
  machine" claim, "expect dusty labels", "the F4 has no input", "Phase 4 needs a keyboard-wedge") to what the KB says or
  labelled *my reading*.
- Delivered to Eugene's `Raw/` (`1qkD2xtFMJtZQVaBJFzHQPz842t8VxjHx`, KB root `1o4MBRcckZBspw-uT6qM2V-74H6OsRK9T`):
  `Darius-to-Eugene-barcode-scanners-production-2026-11-05.md` (`1CLxv6HuAaEUd2tNEKgrjJoYrlojRB1Yz`, 4,147 B = local);
  own copy `Outputs/2026-11-05-Darius-to-Eugene-barcode-scanners-production.md`. Hub `AWT-1116` Response written,
  **In Progress** pending Minda's three answers (hands-full stations, headcount, PC scanner vs handheld).

## 5. Drive publish of 03–05/11 — done
- Owner: *"Drive publishing from 3–4 Nov is still waiting"*. The Composio CLI was signed in by the owner through the
  login link (`composio login --no-browser --no-wait`, then `--poll`; account minda@, org minda_workspace) — no key
  handled by Darius.
- **Before overwriting**, each Drive copy's md5 was matched to a git version (index and registers = `508728d`,
  `Wiki/index.md` = `e506148`, skill register = `2f7f790`, 28/10 log = `2f7f790`) — nothing on Drive was newer than git.
- **In place** (`GOOGLEDRIVE_UPLOAD_UPDATE_FILE`, ids kept): `change-log-index.md`, `kb-registers.md` — **verified by
  the native connector** (download → `cmp` SAME); `Wiki/index.md`, `skill-candidates-register.md` (re-ordered: the
  04/11 rows had been inserted mid-table; now newest first), `change-log-2026-10-28-workshop-plan.md` — md5 SAME.
- **Created** (`GOOGLEDRIVE_UPLOAD_FILE`), all md5 SAME and in the right folder: three change logs (03, 04, 05/11), the
  workflow draft, the ENQ-0002 (v0.2, final), ENQ-0003 and the two test cost sheets, the Eugene note copy (Outputs) and
  `Wiki/Processes/klug-innobox-smartcabinet-input.md` (Processes). Ids in `kb-registers.md` → Drive ids.
