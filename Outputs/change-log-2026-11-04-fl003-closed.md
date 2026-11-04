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
