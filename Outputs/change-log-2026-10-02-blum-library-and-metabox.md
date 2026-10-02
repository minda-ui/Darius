# Change log — 2026-10-02 — the change log owed, a Blum library, and METABOX for SmartCabinet

**Session 26.** Owner's instructions, in order: *"do the change log first"*; *"Check Workshop Raw folder"*;
*"We need to find how to extract, segregate and use Blum"*; *"Yes, start composio login, hinges and runners
first"*; mid-turn *"i need to input Metabox data into SmartCabinet as soon as we can"*; *"create library where
you can access easy and be ready for me when I needed your help on Blum"*.

## (1) Session 25's change log, a day late

`change-log-2026-10-01-extractor-motor-and-f45-e91k.md` written and published (`1H1Jtd4V60x6id77p2vatYR4EmGKORSiu`,
7,061 B, `cmp`-identical). `kb-registers.md` and `change-log-index.md` were rebuilt from their **live Drive
versions** (= branch `claude/vigilant-bell-olevtr`, sizes checked) because this branch held stale pre-v34 copies,
then **held back**: at 158 KB and 91 KB they are beyond what the native connector can carry inline, and
Composio was not signed in. **Published in place once Composio was signed in** (below) — ids unchanged.

## (2) Composio signed in again

`composio login --no-wait` → the owner approved the link → `composio login --poll`. `whoami`:
`minda@fishboneconstruction.co.uk`, org `minda_workspace`; `darius-googledrive` ACTIVE. *The no-Gmail ruling
(§6b, 2026-09-27/28) stands and was observed — only Drive tools were called.*

## (3) `Raw/` — one new file, too big for the connector

`Blum_publication.pdf`, **548,904,350 B**, uploaded 05:46 today. `read_file_content` and the metadata snippet both
came back **empty** — Drive had indexed no text, and a download through the connector is impossible at that
size. **Fetched instead with Composio's `GOOGLEDRIVE_DOWNLOAD_FILE`**, which returns a temporary `s3url`;
`curl`ed to disk, size matched Drive exactly. It is the ***Blum catalogue and technical manual 2022/2023*
(KA-150), 758 pp.** Also noted in `Raw/`, unworked: Anna's `AWT-0194` hand-off (2026-09-28) and the two
`AWT-0147` notes (2026-09-27).

## (4) METABOX for SmartCabinet

METABOX = PDF pp. 394–417. Read the text, rendered the drawing pages that carry the hole positions, and read
**three SmartCabinet manual pages** (`tabelle_cam_accessori_guide`, `anagrafica_accessori`,
`utility_import_accessori`). *The manual's paths have moved under `mainit/smartcabinet/` since 2026-09-27; the
old flat paths now 404.* **`Wiki/Processes/blum-metabox-smartcabinet-input.md`** created (7,094 B,
`1bCxAk6Btj_-Xh3mlM4E_L2_qoiyrur-W`). Its two findings that matter:

- **SmartCabinet's *Import Accessori* may already have METABOX ready-made** — check before typing anything.
- **SmartCabinet's runner table assumes wooden drawer sides; METABOX's are steel**, so it maps only partly.
  Four values are flagged to confirm on a sample, including an M inner-front height printed the same as N's.

## (5) The Blum library

**37 family PDFs + a full-text file + a 1,627-part index**, all in **`Raw/Blum/`**
(`1QumXqBo1OXocFEEBVZFMtKB6MfXAtKud`), described in **`Wiki/Suppliers/blum-library.md`**
(`1cj6z6xuTHl1y8j_IVVLDoMPsru2sX679`).

***One wrong turn, caught before anything was published.*** The first split took family boundaries from the
chapter overview pages and read their numbers one item off — METABOX would have started two pages early,
inside SERVO-DRIVE. **Checked one boundary, found it, discarded the split**, and re-took every boundary from
the page headers themselves; the 37 ranges were then asserted contiguous over all 758 pages. *A list of page
numbers printed in a contents page is a drawing of the catalogue, not the catalogue — the same lesson as the
extractor panel's schematic the day before.*

**Catalogue page = PDF page − 4** throughout, checked at both ends. The part index is Blum's own (cat. p. 728),
parsed. **Upload verified:** 39 files listed on Drive with sizes equal to local (zero mismatches), the full
text, the part index and the largest PDF (48 MB) round-tripped `cmp`-identical; five files spot-checked with
the native connector. The earlier METABOX extract (same pages) was **renamed**, not re-uploaded, to the
library's naming — id kept.

| Code | Family | PDF pp. | Bytes | Drive id |
|---|---|---|---|---|
| `00` | Cover, contents and product overview | 1–17 | 7,304,322 | `1arWgqI5czDp1p1jwCwH2-fyy6aWOOuo-` |
| `L1` | AVENTOS HF - bi-fold lift (with chapter overview) | 18–33 | 14,165,223 | `13C98tUH0gg-LOAzCFonSGS2LgljhWySK` |
| `L2` | AVENTOS HS - up and over lift | 34–39 | 5,495,586 | `1GuiQcudb56us5D03TC1Xc6dIhXAV6nGs` |
| `L3` | AVENTOS HL - lift up | 40–45 | 6,443,625 | `1wH_kJHxnqPpIMkw-bPbbsXaNUsWDcCOH` |
| `L4` | AVENTOS HK top - stay lift | 46–55 | 7,210,766 | `1EXP5MgqNxn-0-qVK_utd1tVMjOr2q2pk` |
| `L5` | AVENTOS HK-S - stay lift | 56–61 | 4,282,676 | `1x8_FGKYR1iY7k9GyJ-ksu_PKdEpgEr0U` |
| `L6` | AVENTOS HK-XS - stay lift | 62–68 | 4,096,174 | `1CT6cpbda4CS3vEIdcKHuOOs4esjBdnrk` |
| `L7` | AVENTOS mitred and rebated, accessories | 69–71 | 1,577,433 | `1LXu_IyBmTGNlTHFfVPSw8SQJvKWuAiEl` |
| `H1` | CLIP top BLUMOTION and CLIP top hinges (with chapter overview) | 72–147 | 48,364,034 | `12h40mIwC_CU9U2KzgdyIOQCfxSEZ0I3G` |
| `H2` | CLIP top mounting plates, angled spacers, accessories | 148–159 | 6,338,211 | `1IgMiC2hB3aycXWcPORsvJCH_6m6onwOF` |
| `H3` | BLUMOTION for doors | 160–173 | 6,833,756 | `1szQxV5r-8zeYtTpwCt_LJhzjCbX1d1OZ` |
| `H4` | TIP-ON for doors | 174–177 | 2,295,332 | `1-TsZemVHTMLsZ1GfMXQGXyN9E9_fR4k0` |
| `H5` | MODUL hinges | 178–191 | 7,298,277 | `1FaxYzC4jTaa6qlgA9KmYtKymaC5x8JTn` |
| `B1` | LEGRABOX (with chapter overview) | 192–247 | 38,077,563 | `1dEr7xD3eOzcH7YgoSFdrXUMqaAUxEdPq` |
| `B2` | TIP-ON BLUMOTION and TIP-ON for LEGRABOX | 248–259 | 8,870,992 | `1W9csJrJ3csN3MBzcAdElslo6V_yVsuj6` |
| `B3` | MERIVOBOX | 260–299 | 31,592,786 | `1xcGtmcDtz8vO5KDLKmk54YZb7ke3udFM` |
| `B4` | TIP-ON BLUMOTION for MERIVOBOX | 300–305 | 6,315,155 | `1xfPbFr9CmGHuJ8pot-rOP7amyoybShp_` |
| `B5` | TANDEMBOX antaro | 306–351 | 26,248,754 | `1_x9ON-lGgV5zB9DeEhMWJdnqoK8sm44c` |
| `B6` | TANDEMBOX plus | 352–353 | 1,052,853 | `1QN4nHveRwXv7qVvMc2Oy0GPqnPJXsdcU` |
| `B7` | TIP-ON BLUMOTION for TANDEMBOX | 354–361 | 6,180,824 | `1wfPrzQkJqRhQjHzQQevyC16kzqNTbTzB` |
| `B8` | SERVO-DRIVE for LEGRABOX MERIVOBOX TANDEMBOX | 362–393 | 19,304,815 | `1Wu_Vujatotp3QZONxLgDjyvdsqx7nccy` |
| `B9` | METABOX | 394–417 | 12,034,550 | `1Z4y4m4fJlzXXHiv90tMRG0ogBEWItX1f` |
| `R1` | MOVENTO (with chapter overview) | 418–437 | 13,348,525 | `121_1gWqOm-3xNEOgA2FRRfsFxyUGDemL` |
| `R2` | TIP-ON BLUMOTION and TIP-ON for MOVENTO | 438–449 | 9,967,218 | `16yjHrzpbEStHqIaYEBspPVcCy3v_HMYS` |
| `R3` | TANDEM | 450–495 | 28,989,665 | `1PbZbtSHtGTgy1WPT9MiFJIVctny9WqA8` |
| `R4` | SERVO-DRIVE for MOVENTO and TANDEM | 496–529 | 19,781,123 | `1AuEeq1OzL55WCoH1kwLZoit3_kZtNrAX` |
| `I1` | AMBIA-LINE for LEGRABOX and MERIVOBOX (with chapter overview) | 530–543 | 8,133,320 | `1dPO_VW7TwyrNVbOOG6NuHA7SIvyLxSlg` |
| `I2` | ORGA-LINE for TANDEMBOX | 544–561 | 9,494,102 | `1qf7acfbRjQM9IahiTmNVXGE__tVyqR49` |
| `M1` | SERVO-DRIVE single applications | 562–575 | 7,281,533 | `16gskXbMbrIZEo7YAl2vqcWARobJfeFem` |
| `F1` | SPACE STEP, CABLOXX, EXPANDO T, wall brackets, cabinet connectors | 576–593 | 10,280,119 | `17ABqDUumsYMpv5AWq6r3lo_j6NC4rjvX` |
| `E1` | E-SERVICES (with chapter overview) | 594–607 | 7,341,060 | `17C6QPVd1fwkPkSGIEhlA8vUxk-L8vUtG` |
| `E2` | Drilling and insertion machines | 608–647 | 24,070,909 | `1bZhe_PTkxoxCbVZH0LE4ZzfX1WlBtfr_` |
| `E3` | Assembly devices | 648–653 | 3,670,719 | `1601JL5EmDMeRnNa4tFBHQjr7UwTnkNoB` |
| `E4` | Templates | 654–701 | 34,356,909 | `1xTSJf7PrGnrO5uEyj16gQb3upz-vnNCo` |
| `X1` | General, safety and planning information | 702–723 | 10,744,167 | `1SzwICSv6IB0CAW078QbHWUgPXCz_ZA_X` |
| `X2` | Blum subsidiaries and contacts | 724–731 | 3,204,078 | `17gGI8dzeIynAahVs-aIGHNlHrFHt13sA` |
| `X3` | Part No. Index | 732–758 | 6,580,175 | `1QdU2nXDvsI6l3jXyonIP2SYGSkKvjWwA` |
| — | Full text, page by page | 1–758 | 1,215,947 | `1UBmfS7dzkLdiBZur_DDlprsw47cFmewS` |
| — | Part index (CSV) | — | 59,890 | `1uL6ovp1pz-KtJrSJBXmVe0xoVTAocziQ` |

## (6) Also done, and not done

- **Hinges done later the same session** — see (7). **Runners not done yet** (`R1` MOVENTO, `R3` TANDEM).
- **Done:** `Wiki/index.md` amended (two entries) and published in place.

## (7) Hinges — CLIP top 110°, for SmartCabinet

Owner: *"Yes, start with hinges."* **`Wiki/Processes/blum-clip-top-hinges-smartcabinet-input.md`** created
(**10,515 B**, id `1nh0YvFGvyjd8CzP4frknYxQjz-oSpvyY`, placeholder then in-place upload; downloaded back,
`cmp`-identical). From catalogue PDF pp. 76–79, 148–152 and 710–713, and SmartCabinet's *Cerniere* manual
page (fetched 2026-10-02).

- **The overlay tables reduce to one formula**, checked against every cell: **FA = TO + TB − MD − crank**
  (TO 11; crank 0 / 9.5 / 18), i.e. overlay `11 + TB − MD`, dual `1.5 + TB − MD`, inset `−7 + TB − MD`.
- **SmartCabinet's hinge table maps cleanly**, unlike METABOX's runner table: `DX` = TB + 17.5 *(derived)*,
  `DØ` 35, `Dφ` 13, `DX2` = DX + 9.5, `DY2` 45, `DØ2` 8 *(drawing)*; `SX` 37, `SY` 32, `SØ` 5.
- **Open:** the Ø8 dowel-hole depth (not printed), screw-on screw positions, and **which hinge and plate the
  shop actually stocks** — one box label or invoice would cut the table to the shop's own rows.
- `blum-library.md` and `Wiki/index.md` updated to point at it.

## (8) METABOX "missing rails", and the shop's hinges (evening)

Owner: *"I have imported Metabox into SmartCabinet, but I am still missing rails for them?"* — with a
screenshot of Anagrafica Accessori.

- **Cause found:** METABOX was imported under its own category `30 METABOX` (*METABOX H*, *METABOX K*, no
  length), **not under `25 GUIDE CASSETTO`**, so drawers cannot be given it as a runner. LEGRABOX — also
  steel-sided — is set up under `25 GUIDE CASSETTO` per NL, and is the model.
- **Proposed to the owner, not done:** add METABOX per-NL entries under `25 GUIDE CASSETTO`, coded by Blum part
  number. **Waiting on** a photo of the LEGRABOX 450 *Guide Cassetto* row. Nothing extra to buy: Blum's
  `320…C` is rail and side together.
- **Also from the screenshot:** the shop's SmartCabinet holds the **screw-on** CLIP top BLUMOTION hinges
  `71B3550` / `71B3650` / `71B3750` and the bi-fold `79T8500` — so the hinge table's dowel-hole fields stay empty.
- `blum-metabox-smartcabinet-input.md` (new §6) and `blum-clip-top-hinges-smartcabinet-input.md` (§8)
  amended in place. Two SmartCabinet manual pages read (*Ferramenta dei Cassetti*, *Scatola Cassetto*).
- **Still open:** runners (MOVENTO / TANDEM) not yet written up — done in (9).

## (9) Runners — TANDEM and MOVENTO, for SmartCabinet

Owner, after the afternoon session-start read (Hub: no new Darius rows; `Raw/`: nothing new): *"Start with the
runners."* **`Wiki/Processes/blum-runners-tandem-movento-smartcabinet-input.md`** created (**9,190 B**, id
`11L-BL7gapj9g_3kgnQAzP7HFSNSEnIAA`, placeholder then in-place upload). From catalogue PDF pp. 422–423, 452–455,
470, 718.

- **Both runners share one set of drawer rules**: SKW = LW − 42, SKL = NL − 10, cabinet depth ≥ NL + 3, base
  recess 12–15 *(drawing)*. Part numbers for every NL, plus the locking devices that have to be ordered separately
  (T51.1700.04 / T51.7601).
- **Cabinet-side holes, converted from the hole-spacing drawings to distances from the front edge**: all but one
  (TANDEM's 275) fall on **37 + 32·n**, so the Vitap's System 32 row can pre-drill them.
- **These fit SmartCabinet's *Guide Cassetto* table as designed**, unlike METABOX: `LX` = 21 − side thickness,
  `LY` = 27.5 (TANDEM) / 28.5 (MOVENTO) − base recess, `CX` 0, `LBox` NL − 10, no side holes, and one rear
  Ø6 × 10 hole. `LX`/`LY` are derived, and whether `LX` is per side or in total is unconfirmed.
- **Open:** which runner the shop uses and its side thickness; confirm the rear-hole position with template
  T65.1000.02; whether SmartCabinet drills cabinet-side runner holes at all.

## (10) "METABOX uses different rails" — the systems compared

Owner: *"Metabox using different rails. It is not TANDEM or MOVENTO. That's why I give you this catalogue, so you can
see difference and become excellent professional."* **Agreed and recorded.** The TANDEM/MOVENTO article (9) is for
the shop's **wooden** drawers. It is not an answer to the METABOX rail question, and **no Darius document says
METABOX runs on TANDEM or MOVENTO**. But the distinction was never written down in one place, so it is now
in `blum-library.md` as *Every Blum drawer system has its own rail*. Checked in the part index and on the order
pages:

- **METABOX** is the only system whose rail **is not sold separately**: `320…C` = *cabinet profiles and drawer sides
  left/right*, and the part index has no separate METABOX rail part.
- LEGRABOX (`750`), MERIVOBOX (`450`) and TANDEMBOX (`578`) rails are sold separately from their side sets.
- TANDEM and MOVENTO are rails only, under wooden boxes.

## (11) METABOX rails — imported from Kosmosoft

Owner: *"Kosmosoft has Metabox rails, I have imported them. Tomorrow will send you picture."* **The missing-rails item
from (8) is closed by the owner.** The import had them all along: the first import brought the box only. The manual
`25 GUIDE CASSETTO` entries proposed in (8) are **not needed**, and are kept in the METABOX article only as a
fallback. **Awaiting tomorrow:** the owner's photo of the imported rail rows. Check them against the catalogue:
cabinet holes at 37 + the NL-dependent second hole, `LX` 15.5, and no drawer-side holes.
