# Change log — 2026-11-04

Darius, session 43.

## 1. Session start
- Hub: 5 Darius rows unchanged; Raw and Review folders: nothing new since 3/11; Composio CLI still not signed in (Drive
  copies of the 3/11 and 4/11 logs pending — in git).

## 2. FL-003 closed
- Owner: *"FL-003 close it"* → Fault Log FL-003 (`FA2402` extractor) **Resolved**, Date Resolved 2026-11-04: clear
  Monitoring week to 2 Nov after the LRE16 overload was fitted, no trips, suction good. The old motor's repair as a
  spare stays a separate item (quote drafts in minda@). **No open faults on the Fault Log.**

## 3. Furniture production workflow — draft v0.1
- Owner: *"We need to work out workflow with furniture production"* → `Outputs/2026-11-04-furniture-production-workflow-v0.1.md`:
  10 steps from enquiry to hand-back, built on how October's jobs actually ran, with who / in / out / gate per step.
- Finding: the **Job Tracker** (`6914515205752708`, built 17/09 with `WJ-YY-NNN` numbers) has **0 rows** — jobs carry
  **AM** numbers instead. Six decisions put to the owner (job number, tracker use, release trigger, materials, QC,
  hand-back).
- Owner: *"I will start by giving the order picture to Nadia, and then we will test how our workflow will work."* —
  test run recorded in the draft; Darius watches the Hub and `Raw/` for Nadia's hand-off.

## 4. Workflow test run — Nadia's hand-off arrived (`AWT-1105`, ENQ-0002)
- Owner: *"check on Nadia"*. Found Hub **`AWT-1105`** (Nadia for Minda, due 6 Nov) and two Raw notes
  (`1mqJ4GGzx-Rtw4kwBqWfceX-HrCiddYz9` 09:05, addendum `1A4wC9DdTWM2wADtj22UJK9RTLtub77Wg` 09:13) plus Nadia's
  `Drafts/ENQ-0002 - cabinet and top board/` folder (`1RFYr1016iKdIDIp1QMuCUdxvzcPMK7HP`): parts list, spec draft v0.1,
  two elevations, render — all md5-checked on download. No client details in any of it.
- Scope: **pre-quote costing** for two separate carcasses **500 × 500 × 500** (drawer chest, 3 × 164 fronts; base
  cupboard, 1 door 494 × 497 RHH), **fronts bought in** (Interior Door Systems, Stratford — Nadia prices them), a ~2,000
  top board not in the parts list. Drawing: 1,900 above the cabinet, 2,300 overall vs 1,900 + 500 = 2,400, and a 100 at
  the floor (plinth?).
- **Workflow learning (1st):** bespoke work needs workshop costing **before** the quote — in Darius's draft that is step
  3, in hand-off v0.2 Darius joins only at step 4. Nadia is flagging it to Victoria.
- Hub `AWT-1105` → In Progress with a receipt line.

## 5. ENQ-0002 costed and handed back (`AWT-1105` Done)
- Owner's answers: *"1. Carcass board: 18mm W1100 ST9 2. Klug Innobox: I have downloaded the drawing to the Raw folder.
  3. Nothing; it goes in the wall, 100 mm from the floor. 4. No top board it goes inside wall"*. Klug drawing 758810 =
  Innobox 86 mm, full extension, 35 kg; NL 450 needs 460 install depth (carcase gives 482).
- Note `Outputs/2026-11-04-ENQ-0002-pre-quote-costing.md` (4,097 B) → Nadia `Raw/` as
  `2026-11-04-from-Darius-ENQ-0002-pre-quote-costing.md` (Drive `1dOQai6JzS-FkKRef_k4WUcmYUwfOWAVe`, 4,097 B — matches).
- **£624.52 ex VAT / £749.42 inc VAT** for carcases + hardware + workshop time (materials £155.45 + 15 %, 7.45 h × £45,
  1.7 h × £65). Excludes IDS fronts, knobs, delivery, fitting (~£90 + travel). ⚠ Board, edging and Innobox prices are
  web/indicative. Blocks to a firm price: niche size (≥ 1,006–1,010 wide), IDS door hinge holes, who fits, knobs, IDS
  lead time.
- Hub `AWT-1105` → **Done** with the result line.
- Owner: *"send over to Nadia"*. The note was already in her `Raw/`; added the matching Hub row **`AWT-1106`** (Nadia,
  Open, Medium; duplicate guard clear) for her next step: price and issue the quote through the CRM with Minda.
  `AWT-1105` Done date set to 2026-11-04.

## 6. ENQ-0002 costing v0.2 — fronts made in-house (`AWT-1107` Done)
- Owner: *"check on Nadia"*. Nadia had set `AWT-1106` In Progress and opened **`AWT-1107`** with a Raw note
  (`17u7U4mPNG3q0YqK4Bu163M4tVVOnKVZs`): Minda's correction — *doors and drawer fronts are made by us*; "Interior Door
  Systems Stratford" was only SmartCabinet's default supplier label.
- `Outputs/2026-11-04-ENQ-0002-pre-quote-costing.md` rewritten as **v0.2** (5,583 B) → Nadia `Raw/` as
  `2026-11-04-from-Darius-ENQ-0002-pre-quote-costing-v0.2-fronts-in-house.md` (Drive
  `1xoWClfP43fVb3yZiOLB9G2QyqNDnvWUM`, 5,583 B — matches). v0.1 left in her Raw as sent.
- Fronts assumed 18 mm W1100 ST9 slab, edged all round; on the same sheet (yield ≈ 64 %); +5.9 m edging; hinge cups,
  knob and bracket holes on the Vitap; +1.2 h labour, +0.7 h machine. **£728.30 ex VAT / £873.96 inc VAT**
  (+£103.78 / +£124.54). Lead time now workshop-set: ≈ 3–4 working days from go-ahead.
- **Workflow learning (2nd):** SmartCabinet's parts list names IDS Stratford on every front by default — not a supplier.
- Hub `AWT-1107` → **Done**.

## 7. Pricing roles settled (owner)
- Owner: *"you providing workshop pricing and Nadia do sales pricing. You use workshop pricing rules"*.
- Recorded in workflow draft step 3 (`Outputs/2026-11-04-furniture-production-workflow-v0.1.md`) and the
  `project-quote-from-smartcabinet` skill's boundary line: Darius = **workshop price** (23/10 rules); Nadia = **sales
  price**; Darius applies no sales mark-up.
- Told Nadia: Raw note `2026-11-04-from-Darius-ENQ-0002-workshop-vs-sales-pricing.md` (Drive
  `1vfnil9MKwdP8bhsEefR8-gOWXa0ATZ6D`, 1,060 B) + Hub **`AWT-1108`** (Nadia, Open; duplicate guard clear). Answers the
  pricing-rule point on her `AWT-1106`.

## 8. ENQ-0002 final workshop price (`AWT-1110` Done)
- Nadia's notes: sizes final (`1lAqPNrnpNFlfJu7BuAEYoQA7ARiXLNa9`); spec final (`18oMz8mGXjA9CJKT50n7Qb9A08K1e96Gq`) —
  W1100 ST9 carcases and fronts, knobs **Carlisle Brass FTD703MB** ×4 at £6.75 ex VAT, no fitting.
- `Outputs/2026-11-04-ENQ-0002-workshop-price-final.md` (2,395 B) → Nadia `Raw/` (`1DyXf-d4BxctgKXPc58PfWWCPXjQLA7i5`,
  2,395 B — matches). **£763.85 ex VAT / £916.62 inc VAT.**
- Knob: the supplier page scan (`1tgh6NjYE2ay7e4gOYbFObq2wkrnljJEe`) shows price and SKU only; retailer listings give
  Ø35, 34 projection, 19 rose, bolt supplied; **no source states the thread** — M4 / Ø5 mm through hole assumed, to be
  checked on the first knob before the fronts are drilled.

## 9. ENQ-0003 = AM002 Ladder — and the doors were missing (`AWT-1109` Done)
- Nadia's note (`1ll4YMXr6WDW1vib4uHdYxVF5DVWUQdyN`) described a tall two-door cupboard, internal 332/332/332/350.
  Owner: *"ENQ-0003 is AM002 Ladder"* — costed from the released production files instead of assumptions.
- The comparison showed AM002 as released (03/11) is an **open** bookcase 1,400 high, while Nadia's renders show a pair of
  full-height doors and the elevation gives ≈ 1,436. Owner: *"I forget to add doors :(. This is why i understand
  importance of workflow"*.
- **Consequence:** the files in `Furniture/AM002 Ladder` are incomplete — no doors, no hinge-plate holes in the sides.
  **AM002 must not be cut or drilled from them**; Minda to add the doors in SmartCabinet, re-export to the Review folder,
  Darius re-checks, then re-release. Darius has not touched the Furniture folder (writes there only on the owner's word).
- `Outputs/2026-11-04-ENQ-0003-AM002-Ladder-workshop-price.md` (5,094 B) → Nadia `Raw/`
  (`17f-MmCR2Zu7Q_vARUCUoPS37OW9m6bwQ`, 5,094 B — matches). **£658.81 ex VAT / £790.57 inc VAT** with doors
  (carcase + decor panels £511.92, doors £146.89), before bar handles; decor on a U702 proxy. Open: height 1,400 vs 1,436,
  decor, decor panel sizes, base box, handles.
- **Workflow learning (3rd), the big one:** AM002 was checked and released **before** Sales held the client's drawings —
  the drawing check compared the programs with each other, not with what was sold. A release gate needs **the order's
  spec (Sales' drawings) as the reference**: step 6 should check the export against the confirmed order, and step 7
  (release) should wait for step 4 (order released). To fold into workflow v0.2.

## 10. Anvar kitchen v3 priced (owner)
- Owner: *"i have uploaded Anvar v3 folder in your review folder. could you priced it for me please"*; then *"it would be
  metaboxes, not legraboxes"* and *"board is W1100 ST9"*.
- `Raw/Review folder/ANVAR_KITCHEN_V3` (`1Vti_zlTShdGREWsToyMZvc_pShTAvaTk`): 17 unit folders, 153 programs; the 12
  unique worklists downloaded (Composio, `darius-googledrive`) and md5-checked; UTF-16 parsed. 147 parts, all **19 mm**.
  Programs **not** drawing-checked yet.
- `Outputs/2026-11-04-anvar-kitchen-v3-cost-sheet.md`: **£3,547.92 ex VAT / £4,257.50 inc VAT** workshop price
  (materials £1,083.19 incl. 9 sheets W1100 ST9 at the 18 mm web price, 37.15 h labour, 9.7 h machine).
- Flagged: export is 19 mm vs the 18 mm price; **026 corner base and 025 housing have no doors** (today's AM002 lesson);
  corner wall unit hinging; Metabox NL500 priced at NL400, 20 mm drawer bottoms, no drawer backs; sink post not in the
  export; handles, plinth; unit 014 is 600 deep vs 570.
- Owner: *"no, it is test for me"* — a test of the costing method. **Not sent to Nadia, no Hub row, no drawing check.**
  Cost sheet marked as a test.

## 11. Klug Innobox into SmartCabinet — data article
- Owner: *"We need to klug innobox to SmartCabinet"*.
- Read the owner's drawing `Raw/758810.pdf` (scanned, no text layer; pp. 5, 6, 15 read as images at 400 dpi): it is
  **Taiming 908SH-A86 "Noble Drawer"** — double-wall 86 side, full extension, 35 kg, NL 270–550, internal length NL − 26,
  min. depth NL + 10; runner holes **37 and 261 (37 + 224) for every NL**, screw line **min. 56** above the part below,
  min. 105 per drawer; **37.5 ± 0.5** cabinet side to base edge (→ base LW − 75), back edge **44.5** (→ back LW − 89);
  front bracket 2 holes 32 apart, lowest min. 54.
- New article `Wiki/Processes/klug-innobox-smartcabinet-input.md`, set out on the METABOX method (runner row per NL in
  *Guide Cassetto* + an `INNOBOX_A86.scs` copied from `METABOX_K.scs`), with a one-drawer proving step on ENQ-0002.
  **Every figure is a drawing read; the ⚠ ones to measure on the first set.** `Wiki/index.md` entry added.

## 12. TV Unit 30_09 — costing test on a finished job; AM002 → AM2602
- Owner: *"Check Raw folder for new picture. It is finished project done by us. In review folder there is TV Unit 30 09 and
  shelf for tv unit 30 09"*. Photo (`1mqvpx5Ca0ofy-4oXQOfzUesYkMOeW4sT`, in `Raw/Review folder`): floating walnut-look TV
  unit, lit shelf tower, slatted panel. Two worklists + cutting-list PDF downloaded (md5 = Drive).
- `Outputs/2026-11-04-tv-unit-30-09-cost-sheet.md`: **£968.01 ex VAT / £1,161.61 inc VAT** for the cabinets in the export
  (TV unit 3,000 × 400 × 300 in 4 boxes + tower 500 × 1,780 × 250, 2 sheets, 10.55 h). Finding: the photo's **top board,
  slatted panel, LED lighting and push-to-open fronts are not in the export** — the costing method only sees what
  SmartCabinet drew.
- Nadia's note (`1n7PCGX3Jna_UvM7__I1zhZ6FSxn6cn_X`): Amfa jobs are **AM + year + number** (Anna, `AWT-0497`) —
  **AM002 Ladder = AM2602**, AM001 = AM2601, ENQ-0002 will be AM2603 when won. `Furniture/AM002 Ladder` still carries the
  old name; renaming is Minda's call (Darius writes to Furniture only on her word).
- Owner: *"It is got W1100 ST9 at the back of TV"* — the panel behind the TV (≈ 1,500 × 1,570 from the photo), 1 sheet
  W1100 ST9 + edging + 1 h added: **£1,124.29 ex VAT / £1,349.15 inc VAT**.
- Owner: *"It has a timber frame behind panel"* — ≈ 9 m CLS 38 × 63 + fixings (£19, proxy) and 1 h added:
  **£1,191.14 ex VAT / £1,429.37 inc VAT**.
- Owner: *"Slatted panel are made by us in workshop, it is 50mm wide and edging on both sides"* — ≈ 16 slats 50 × 1,200
  (count and length by eye from the photo), board from the offcut, ≈ 38 m edging, +3 h labour / +1.5 h machine:
  **£1,435.14 ex VAT / £1,722.17 inc VAT**.
- Owner: *"www.ultraleds.co.uk; check led strips"* — site not reachable from this session (host not in the network
  allow-list); prices taken from search-result listings (inc VAT ÷ 1.2): 24 V COB economy 5 m reel £36 inc, Tagra 24 V
  100 W driver £28.80 inc, SS17 profile from £2.50 inc. ≈ 13 m by eye, 2 drivers, profiles, allowance = £167.58 ex VAT,
  +1.5 h / +0.3 h machine: **£1,714.86 ex VAT / £2,057.83 inc VAT**.
- Owner: *"warm white"* — LED colour confirmed; the £36 economy COB reel was taken from the warm-white category, so the price stands.
- Owner: *"PC24-FC"* — the strip used: Tagra PC24-FC, 24 V COB cut-anywhere, 320 LEDs/m, 11.2 W/m, CRI 90+, from £75.60
  inc VAT per 5 m reel (search listing). 3 reels £189.00 ex VAT replaces the £90 economy proxy; ≈ 146 W, 2 × 100 W drivers
  still fit. **£1,828.71 ex VAT / £2,194.45 inc VAT.**

## 13. AM2602 (AM002) Ladder — drawing check round 2, with doors
- Owner: *"check review folder for AM002 Larder"*. `Raw/Review folder/AM002 Ladder` (`1TfkKsUWZu8iKvJfXb0VZsA8jVm9CH3jX`)
  **replaced in place** at 13:16: 15 files, all md5 = Drive (fetched via Composio, bundled, md5 re-checked locally).
  A subfolder `AM002 Ladder` (`1WUztnPCNNp_OP6X3HETHtZ3upi1xU8K6`, 07:51) holds an **earlier draft** (sides and doors
  differ) — not checked; owner to say it is not to be run.
- **Changed vs round 1:** sides (hinge-plate pilots added), **new 09-DOOR-1 / 10-DOOR-2**; bottom, top, shelves, back
  byte-identical (decoder `--diff`).
- ✓ Doors **1,396 × 437 × 18**, a pair: 2 × 437 + 6 = 880 (1.5 / 3 / 1.5 reveals), 1,396 + 2 × 2 = 1,400 — full overlay over
  top and bottom.
- ✓ **4 hinges a door**, cups Ø35 × 13 at **TB 5** (centre 22.5), 100 from each end, evenly spaced; screw pilots ±22.5 /
  9.5 — the CLIP top pattern. Blum's chart needs 3 at this height and width; 4 is more than enough.
- ✓ **Plates on 37 / 32** (Ø3 × 5): centres at side **102 · 500.7 · 899.3 · 1,298** = door cups 100 · 498.7 · 897.3 · 1,296
  **+ 2** (the door's top reveal) — level. Both sides mirrored. Overlay needed 18 − 1.5 = **16.5**; hinge gives 11 + 5 − 0 =
  **16** (TB 5, MD 0) — 0.5 within the adjustment.
- ✓ No hinge–shelf clash: hinges 140+ mm from the nearest shelf seats.
- **? still open:** (1) **height 1,400** (files) vs **≈ 1,436** (Sales' drawing); (2) **bar handles** — no handle holes in the
  doors (all holes on the Vitap): model and centres; (3) **side decor panels** — the 18 mm doors stand 18 in front of the
  carcase: panel depth 400 or ≈ 418+ to cover the door edge?; (4) the 07:51 subfolder.
- Not released: on the owner's word the folder replaces `Furniture/AM002 Ladder` (old open-bookcase files, **must not be
  run**) — and Nadia's new number **AM2602** can be used for the new folder name.
- Costing note: 8 hinges, not the 6 priced on AWT-1109 (+£2 × 2.84 = £5.68 at cost).
- Owner: *"1400 is right, decor panels 400 deep"* — ? (1) and (3) closed: the unit stays **1,400**; decor panels **400**
  (flush with the carcase, the doors stand 18 proud of them).
- Owner: *"2. will be done by hand"* — bar-handle holes drilled **by hand** on this job: **the owner's own exception** to
  the standing rule that every hole is machined on the Vitap (owner, 2026-10-04). ? (2) closed.
- Told Nadia (sales drawing said ≈ 1,436): Raw note `2026-11-04-from-Darius-AM2602-Ladder-height-and-doors.md`
  (`1K7t_Kc4_VGPcKkE0YJ2mO8XQnhI9MFr_`, 1,081 B) + Hub **`AWT-1113`** (Nadia, Open; duplicate guard clear): 1,400 high,
  doors, 400 decor panels, workshop price **£665.34 ex VAT / £798.41 inc VAT** (8 hinges), before handles.
- Open: (4) the 07:51 draft subfolder; then release to Furniture on the owner's word.
- Owner: *"Yes ignore subfolder, release to Furniture"* — **AM2602 Ladder cleared and released.** New folder
  `Furniture/AM2602 Ladder` (`1hYQzsKOvIgoBc_dgngEuDi8clJYoPzLX`), the 15 round-2 files copied server-side; **all 15
  md5s equal the checked files.** The 07:51 subfolder ignored. The old `Furniture/AM002 Ladder`
  (`1ABYUTy7z7_Wzrx5Y_Zqiv-q6Lh4fTlfh`, open bookcase, no doors) left untouched — **must not be run**; deleting or
  renaming it is the owner's. The job file inside is still named `AM002 Ladder.fnm` (SmartCabinet's name, not changed).
- Owner: *"delete AM002 Ladder folder in Furniture"* — `Furniture/AM002 Ladder` (`1ABYUTy7z7_Wzrx5Y_Zqiv-q6Lh4fTlfh`)
  **moved to Drive's bin** (`GOOGLEDRIVE_TRASH_FILE`, `trashed: true`), restorable for 30 days — not deleted permanently.
  Checked first: it no longer held the 03/11 open-bookcase release but **the 07:51 draft** (sides `fab836fe…`/`ba5b0470…`,
  doors `67f72b22…`/`2a798d0a…`) plus a subfolder — someone had overwritten it this morning; my earlier note that it held
  "the version without doors" was out of date. `Furniture/AM2602 Ladder` is now the only Ladder folder in Furniture.

## 14. End of day
- Owner: *"Good night"*. `change-log-index.md` (+ 11-03 and 11-04 rows, count 41 → 43) and `kb-registers.md` (+1 Wiki row,
  +5 Outputs rows) updated in git.
- **Drive not published today.** The Composio CLI is still not signed in in this container (`composio whoami` empty), and
  the native connector can create files but not replace a file's bytes in place, which the index, registers and
  `Wiki/index.md` need. **First job next session (with the CLI signed in):** publish in place `change-log-index.md`,
  `kb-registers.md`, `Wiki/index.md`; create `change-log-2026-11-03-…`, `change-log-2026-11-04-…`,
  `Wiki/Processes/klug-innobox-smartcabinet-input.md`, the workflow draft and today's cost sheets; verify each by
  download + `cmp`. The notes for Nadia are already on Drive (her `Raw/`).
- Skill candidates offered (see `Outputs/skill-candidates-register.md`).
