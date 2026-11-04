# Furniture production workflow — draft v0.1

Darius, 04/11/2026, for Minda. **Owner, 04/11:** *"We need to work out workflow with furniture production."*

Built from how jobs **actually** ran in October (the library quote, the corner unit, the 1000 sink unit, AM002 Ladder),
set against the September design (`Wiki/Software/smartcabinet-and-production-workflow.md`). **Draft — every step is for
Minda to confirm or change.**

## What already exists, and what is not used

| Item | Status |
|---|---|
| Job Tracker sheet (`6914515205752708`), 9 stages, `WJ-YY-NNN` numbers | **Built 17/09, never used — 0 rows.** Jobs carry **AM** numbers instead (AM002 Ladder). |
| Order hand-off Sales → workshop (Nadia → Darius, `AWT-0871`) | v0.2 drafted with Victoria (18/10); not confirmed in use |
| Quote costing | `project-quote-from-smartcabinet` skill; formal quote issued by Nadia in the CRM |
| Drawing check before production | in use — Review folder → check → fix → Furniture folder |
| Vitap loading | in use — `worklist.xmlst` in ListsManager |
| F45 | takes dimensions from the cutting list / optimiser, not a program |
| Materials ordering, QC checklist, packing, delivery note | **nothing written down** |

## The workflow — 10 steps

| # | Step | Who | In | Out | Gate before the next step |
|---|---|---|---|---|---|
| 1 | **Enquiry & design brief** | Sales (Nadia, CRM) | client request | brief, sizes, finish | — |
| 2 | **Design in SmartCabinet** | Minda | brief | scene, panel + parts CSV | — |
| 3 | **Costing & quote** | Darius costs → Minda prices → Nadia issues | CSVs, rates | cost sheet + PDF; quote in CRM | client accepts |
| 4 | **Order released to the workshop** | Nadia → Darius | signed order / deposit | **AM number**, tracker row | contract signed + deposit (QuickBooks) |
| 5 | **Production drawings** | Minda exports to `Raw/Review folder/<AM> <name>` | final scene | TCN + worklist + .fnm (+ cutting list PDF) | — |
| 6 | **Drawing check** | Darius | job folder | ✓ / ✗ / ? report | **no open ✗ or ?** |
| 7 | **Release to production** | Darius copies to `Furniture/<AM> <name>` on Minda's word, md5-checked | cleared folder | production folder | — |
| 8 | **Materials** | Minda orders (Lathams etc.) | optimiser sheet count, hardware list | boards, edging, hardware in | all materials in |
| 9 | **Make**: F45 cut → F4 edge → Vitap drill → assembly | workshop | Furniture folder, cutting list | parts / units | — |
| 10 | **QC, pack, hand back** | workshop; Darius records | units | QC pass, packed, Ready date | → Sales for delivery / client's installers |

Every step moves the job's row in the **Job Tracker**: stage, dates, blocked flag, folder link — so anyone can see where
a job is without asking.

## Decisions needed from Minda

1. **Job number:** keep **AM** numbers (e.g. AM002) as *the* workshop number and drop `WJ-YY-NNN`? Who issues the next
   AM number, and where is the list kept (the Project Register)?
2. **Start using the Job Tracker** from AM002, or track jobs another way?
3. **Order release (step 4):** what exactly releases a job — signed quote, deposit paid, or Nadia's word?
4. **Materials (step 8):** who orders, from the optimiser sheet count, and does stock in hand (offcuts) count?
5. **QC (step 10):** what is checked before packing — sizes, doors and drawers adjusted, edges, labels?
6. **Hand back:** delivery by us, or collection / client's installers (as for AM002)?

## Test run (owner, 04/11)

*"I will start by giving the order picture to Nadia, and then we will test how our workflow will work."* The first job
runs through the draft as a test: Minda → Nadia (step 1) → Darius picks it up when Nadia's hand-off arrives (a Hub row
and/or a note in the workshop `Raw/`). Each step's hiccups are logged against this draft and fixed in v0.2.

## Next, once these are answered
- Fill in the Job Tracker for live jobs (AM002 first).
- Write the missing pieces: release checklist, materials list from the optimiser, QC checklist, packing/label note.
- Fold the confirmed workflow into `Wiki/Software/smartcabinet-and-production-workflow.md`, replacing the September
  version.
