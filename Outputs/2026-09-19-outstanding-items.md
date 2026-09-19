# Outstanding items — Workshop KB, as at 2026-09-19

Prepared for Minda. Sourced from the Smartsheet **Tasks** sheet (`4087584374523780`, T001–T029) and
`CLAUDE.md` §7. **29 tasks raised, 11 closed, 18 open.**

Supersedes `2026-09-18-outstanding-items.md`. Ordered by *what it takes to close it*, not by task
number — because most of these do not need a decision, they need somebody to look at something.

**Seven closed since yesterday's list**, five of them by the owner simply saying how the shop works or
what was decided: **T009** and **T012** from type plates, **T026** and **T028** from the production
route, **T029** from the edging answer, **T025** from the fixing decision, and **T010** on instruction.
**One was corrected**: T027 said the shop lacked a 35 mm hinge-cup bit; it has one.

---

## 1. One walk round the workshop still closes six of them

Take a phone, a tape measure and a borrowed anemometer. Nothing here needs a supplier, a quote or a
decision.

| # | Do this | Closes / advances |
|---|---|---|
| 1 | **Photograph the air receiver's plate** on `FA2306` — volume, design pressure, year, serial | **T021**, the pressure-system question. Turns an inference into a fact. *Last attempt could not be read at 2.9 MB — a cropped or smaller shot should work* |
| 2 | **Photograph the ABAC's yellow service label** again, and look for any service paperwork | **T020** — is the compressor overdue? |
| 3 | **Anemometer reading at each machine's extraction port**, machines running | **T014** *and* the extraction half of **T018**. Hebrock ≥25 m/s, F45 ≥20 m/s, Vitap ~2000 m³/h |
| 4 | **Check the F45 has a water separator and 40 µm filter** on its air feed | Its manual requires them (ISO 8573-1:2010 [7:4:-]) — never verified |
| 5 | **Cut one Ø12 hole in scrap with the 10 mm cutter and measure it** | Settles the TpaCAD `Diameter`-field convention **permanently**, for every hole and every cutter. A wrong reading here gives 22 mm, so the answer is unmistakable. Two minutes, and it also answers the 35 mm cup |
| 6 | **Put an asset label on the Brother printer** (`FA2401`) | The only registered asset with no physical tag |
| 7 | **Scan one *applied* tag** (e.g. `0017` on the compressor) | Confirms the QR payload generalises — only one label, from an unapplied sheet, has been read |
| 8 | **Read the F4's pre-mill trim setting, and the tape it is set for** | **T029's remainder.** These two must match or every panel drifts — see §4 |

Items 1, 2, 4 and 6 are all within a few metres of each other.

---

## 2. Documents still wanted

| Document | Why it matters | Task |
|---|---|---|
| **VAT invoice for the compressor** | Proforma 208027 evidences the *order*, not payment or delivery | T019 (closed on the proforma; this would settle it) |
| **A manual confirmed for `STK 10000`** (`FA2402`) | Without it the extractor **cannot join the Maintenance Schedule or Fault Log** — no filter-change interval exists | T014 |
| **Altendorf F45 safety certificates** | HM 220024 / 220025 **expired 22.02.2024** | **T007** |
| **Complete `TpaCad.pdf` / `Workings.pdf`** | Likely already on the Albatros PC at `Albatros\Help\`. Holds the compensation semantics, the entry/exit segments and the `THREE HOLES HINGE` table | **T015** |
| **Brother TD-4420DN actual invoice** | Only an order receipt has been seen | — |
| **Inventair disposal dates and sale proceeds** (`FA2302`, `FA2305`) | Both carry purchase prices, so both disposals have a book consequence | — |
| **Unit 31 lease body** | Only the cover page seen. Alterations / repair / nuisance clauses bear on ducting, three-phase runs and bolting machines to the slab | — |
| **R&J Machinery confirmation** | A dealer sticker on the Vitap is the only evidence of who sold `FA2301`/`FA2303`/`FA2304` | — |
| **A better scan of the F45 schematics** | The two that arrived lost every circuit line to OCR; no wire is traceable end to end. *Worth more than another document* | T011, T018 |
| **The Cabineo X order paperwork** | Settles **which variant and which screw** were bought — the housing takes a Cabineo 8 or 12 screw or a shelf pin, and that affects the mating hole. Would also confirm **by part number** that the master's pocket is a Cabineo X pocket rather than merely a compatible one | — |

---

## 3. Compliance — the sharp end

Flagged prominently because they are regulatory, not housekeeping. **This KB does not give regulatory
advice**; each needs a qualified answer.

- **`FA2303` safety certificates expired 22.02.2024** (**T007**) — over two and a half years ago,
  unresolved. Ask Altendorf or the supplier whether re-certification is required for continued use.
- **First F45 monthly documented safety check has never been logged** (**T008**). Mandatory and monthly;
  the Safety Check Log is built and empty. *The schematics now give real device tags to name — including
  **three** emergency stops, where the check article says "the E-stop", and a **50 mm reduced safety
  zone** at the rip fence the KB had no record of.*
- **`FA2306` air receiver — written scheme of examination?** (**T021**) If the plate's "500L" is a 500
  litre receiver at 10 bar, PSSR 2000 very likely requires one. *"500L" is a reading of a model name,
  not a specification* — establish what the receiver is first.
- **`FA2306` service history** (**T020**) — label blank, machine delivered November 2023, interval
  *2,000 hours or 1 year, whichever comes first*. **A blank label is not proof**; ask the supplier.
- **`FA2303` annual PTC electrician check** (**T011**, MT-025) — needs scheduling. *Booking it commits
  the company to a payment, so it is yours, not mine.* The schematics give a likely measurement point at
  **`-X3` `POT_1`/`POT_2`**, and separately at `-X1` 13/14 and 21/22 — **the two parts disagree and it
  could not be settled from the documents.** They also leave **bimetal vs PTC unresolved**, which
  matters because one is a continuity check and the other a resistance measurement. **No resistance
  value appears anywhere.** The electrician verifies against the paper before metering.
- **F-Gas on `FA2306`** (**T020**) — 0.316 t CO₂e is well under the 5-tonne threshold on the plate's own
  figures. Worth a qualified confirmation, not urgent.

---

## 4. Decisions only you can make

- ~~**The fixing for the range**~~ (**T025, closed**) — **Cabineo X, chosen and ordered; confirmat kept
  as Plan B and held in stock.** What remains is not a decision: **get a trade quote on the housing at
  2,000**, since £0.77 is a single-unit retail listing and the gap between that and ~£0.30 is real money
  on every kitchen. *A purchase, so yours.*
- **The library's remaining four questions** (**T023**) — widths for each of the five types; whether
  *"low cost"* is a defined carcase spec or a range name; whether hand belongs in the unit code or is
  mirrored at job time; and whether library units get separated from customer jobs on Drive.
  **Four of your five unit types have no master at all** — only the wall unit exists.
- **Shelf depth: 255, 256 or 266?** (**T024**) Three units, three answers, all 300 mm deep. Settle it
  before anything is copied, because a library propagates whichever value it is built on. **And the two
  backs** — `07-BACK-1` and `07-BACK-1B`, same blank, different programs, both in the cut list, and
  neither earlier unit has a second back at all.
- **Tape thickness and the F4's pre-mill trim are one decision, not two** (**T029's remainder**). The
  finished-size scheme only nets to zero while they match. Change tape without re-setting the pre-mill
  and every panel is wrong by twice the difference on a two-edge part — failing as **a whole batch that
  does not fit**, not one bad panel. Also needed for costing: **which edges are edged** on each part.
- **`FA2304` §6.8 safety check** (**T013**) — does the Vitap's check need a dated, logged record like the
  F45's, or is a pre-cycle functional test enough? The manual doesn't say. MT-036 holds the place.
- **Were the machines re-commissioned after the move to Unit 31?** (**T018**) You've confirmed they're
  "up and running" — that answers whether they *work*, not whether the manuals' post-installation checks
  were done. *The extraction-interlock half is now a site check rather than a document hunt: the F45
  **does** provide volt-free terminals to start an external extractor (max 240 VAC, 1 A). Whether
  anything is landed on them is a look inside the right-hand cabinet.*
- **Shared group Document Register write access** (**T003**) — still unconfirmed, so every document here
  sits at `Document No.` = `pending`. **Ten and counting.**
- **Who legally owns the machines** (**T004**) — **seven for seven** billed to Fishbone Drylining Ltd,
  never AMFA Furniture Ltd, and AMFA holds the Unit 31 lease. Needs the intercompany side, outside this KB.

---

## 5. Software and CAD

- **Commission the Cabineo X tooling** (**T016**) — **the library's one remaining blocker, and it is
  software only.** Not a generic tool-not-found fault: it is the Cabineo X tooling half-defined in
  SmartCABINET, and the missing Ø5 is one of the two drills Cabineo X names. **Nothing to buy.** The Ø15
  in Cabineo X's published requirement is the *alternative* to routing, and the master routes the pocket
  — so the Ø5 the master already drills plus a ≤Ø12 cutter (you have 12 mm and 10 mm) covers it. A catalog
  entry and a test run. **Close it before populating the library**, because every hole exports with no
  tool number, so a Ø5 that does not resolve fails every unit identically. *Whether a catalog entry added
  on one machine reaches the other is **unverified** — a shared network does not merge two applications'
  internal databases.*
  **Severity revised down, priority unchanged:** with confirmat in stock as Plan B, a job is not
  *stopped* by this — only made more slowly and with a visible screw head.
- **What was the problem with the 35 mm drilling head?** (**T027**) The shop has one. The door programs
  each cup as a Ø35 bore with **no tool assigned**, which would fail exactly as "Tool for this working
  not found" — so T016 is the obvious candidate, but **you haven't said**, and this KB was just caught
  guessing on precisely this point.
- **SmartCabinet Wall Support X-sign discrepancy** (**T017**) — two items both "measured from the back
  edge" needed opposite signs (−15 vs +5). Needs visual confirmation on a real job.
- **Barcode Phase 1** (**T022**) — the QR payload is known, so the precondition is discharged. What
  blocks it: no scanner bought (a purchase, so yours), the Brother's ZPL support unverified, and a
  disambiguation rule between asset labels and part labels to agree.
- **Which SmartCABINET version is actually installed** — release notes list 3.2.0.9 (07/07/2026).
- **Does SmartCABINET's ERP module already track production?** Worth knowing before building a parallel
  Smartsheet tracker.
- **The shared Google Drive job folder** — never identified or examined. Its naming convention constrains
  any tracking-ID scheme. *May hold CRM customer data — cite, never copy.*
- **What consumes the two `NESTING` `.TCN` files?** Nothing on the production route appears to. And what
  form the cutting list takes — printed, on screen, or the CSV export the release notes mention.

---

## 6. Known debts — recorded, deliberately not fixed

- **The git mirror is partial.** **18 of 30** Wiki articles are on Drive only — *counted with `git ls-files` on 2026-09-19, not carried forward.* **It cannot be back-filled
  by copying** — the connector's read tool doesn't round-trip (a 2 KB test file came back 4 bytes out,
  silently). Closing it needs an owner-side folder download or a real Drive-to-git sync.
- **`related:` front-matter links are not bidirectional.** The fix means re-authoring three 21–30 KB
  articles through a lossy read to change one metadata field. Fix it next time one is rewritten anyway.
- **Two weight discrepancies, recorded not resolved** — `FA2304` **1385 kg** on the plate vs **1030 kg**
  in the manual (355 kg apart; floor loading and levelling both scale with it, so prefer the plate).
  `FA2402` **740 kg** vs the quotation's **720 kg**.
- **`FA2402`'s "dust absorption rate 40 m/min"** — recorded verbatim, matches neither the inlet nor the
  filter face velocity. **Not to be used** until a vendor or real manual explains it.
- **`FA2306`'s two model designations** — plate `GENESIS 15 500L`, proforma `GENESIS C67`. The *product
  number* `4152025548` is identical on both and is what identifies the machine. Recorded, not merged.
- **`0191 605 2945` is printed on every group asset label** and was in a SIP trunk migration due
  **03/08/2026, a date already passed**. If that number didn't survive, every label points at a dead
  line. Telephony isn't this KB's scope — flagged only because the labels depend on it.
- **The register is known to be incomplete.** A 15 kW compressor feeding all three machines was missing
  until you photographed its label. Hand tools, extraction ductwork, the air receiver and the server rack
  have never been assessed. **Nothing inside the KB can tell us what else is missing.**
- **What confirmat size is in stock, and how many?** Plan B depends on it and the stepped pilot differs
  between 7 × 50 and 7 × 70. Not recorded anywhere.
- **Which cutter diameter does the Cabineo pocket assume?** The pocket's arc parameter reads as a 7.5 mm
  radius, implying a 15 mm width — which a 12 mm cutter cannot cut in one pass. One pass or two is a
  cycle-time and a fit question; confirm before the first production run.
- **Does a Cabineo-drilled panel assembled with confirmat behave the same?** The pocket removes material
  from the side's inside face near the joint. Untested, and only matters if Plan B is used in anger.
- **`AMF` vs `FA` asset-code inconsistency** in AMFA's own Property Register — flagged only.
- **Duplicate manual PDFs** found in a Drive folder outside this KB's tree — not touched.
- **`CLAUDE.md` carries an article count that goes stale every time an article is written.** v12 said
  "four", v13 "fifteen", v16 "seven", and v17's "nine / twenty-seven" was already **twelve / thirty** by
  the time this list was drafted the same day. The count keeps being corrected and keeps re-breaking,
  because the charter is the wrong place for a number that changes weekly. **Proposed for the next
  charter revision: drop the figures from `CLAUDE.md` and have it point here instead**, with the count
  recomputed by `git ls-files` whenever it is quoted. The *eighteen Drive-only* figure has been stable
  throughout, because articles have been added to both stores in step.

---

## 7. The one structural thing worth knowing

**The shop is a serial line with no redundancy.** Every panel goes `FA2303` → `FA2301` → `FA2304`, in
that order. There is no second saw, no second bander, no second borer — **any one of the three going
down stops the whole shop**, not a fraction of it. And all three are fed by **`FA2306`**, whose service
log has been blank since November 2023.

The Maintenance Schedule currently treats the three machines as peers. On a serial line they are not
peers with anything — they are all critical, **and so is the compressor, which is not on the schedule at
all because it has no manual.** A judgement for you, not a change made here.

---

## Closed since the KB started

**T002** CE Declaration obtained · **T005** Hebrock price confirmed by the 70%-balance cross-check on
three invoices · **T006** corner-rounding fault resolved (FL-001) · **T009** `FA2303` serial confirmed
from the type plate, 2026-09-18 — *the number the KB had held since Session 6 under the wrong name* ·
**T012** `FA2304` serial and year confirmed from the type plate, 2026-09-18 · **T019** compressor
registered as `FA2306`, 2026-09-18 · **T026** the nesting sheet / Vitap width question — *never a
contradiction, only a missing process fact*, 2026-09-19 · **T028** the F45 works from the optimiser's
cutting list, 2026-09-19 · **T029** the cutting list is finished sizes and the F4 trims before it tapes,
2026-09-19 · **T010** closed on instruction, 2026-09-19 — *"review `FA2302` once the new extractor's
manual arrives"*, and both Inventairs turned out to be sold while the centralised unit was a third
machine the register did not contain. **Its 2026-09-15 note had recorded the supersession idea as
plausible and not confirmed**, so nothing had to be unpicked when the answer came back "neither" — that
row is where `CLAUDE.md` §3's restraint lesson was earned. *`FA2302`'s disposal date and sale proceeds
are still unknown and sit under documents wanted, not here.* · **T025** the carcase fixing decided,
2026-09-19 — **Cabineo X, chosen and ordered, with confirmat retained as Plan B and held in stock.** The
master was already drawn for it, so nothing needed re-drawing; and because the connector pockets are
routed into the carcase's *inside* faces, **a Cabineo-machined unit can be assembled with confirmat
instead without re-drawing anything** — an empty pocket is hidden in the finished unit. That fallback is
what turns T016 from a blocker into a priority.

*`FA2301`–`FA2306`, `FA2401`, `FA2402` — eight assets, two sold, one with no label.*
