# Outstanding items — Workshop KB, as at 2026-09-18

Prepared for Minda. Sourced from the Smartsheet **Tasks** sheet (`4087584374523780`, T001–T022) and
`CLAUDE.md` §7. **22 tasks raised, 4 closed, 18 open.**

> **Updated later the same day.** Item 1 below (the QR payload) was **answered** within the hour, and
> two F45 electrical schematic PDFs arrived in `Raw/`. Changes are marked inline; nothing has been
> silently deleted.

Ordered by *what it takes to close it*, not by task number — because most of these do not need a
decision, they need somebody to look at something.

---

## 1. One walk round the workshop closes eight of them

Take a phone and a borrowed anemometer. Nothing here needs a supplier, a quote or a decision.

| # | Do this | Closes / advances |
|---|---|---|
| 1 | ~~Scan any asset label's QR code~~ — **DONE.** Payload is the bare four-digit number as plain text (`Text: 0027`). *Worth one more scan on an **applied** tag, e.g. `0017`, to confirm it generalises — only one label was read* | **Phase 1's blocker is discharged.** Now **T022**: a scanner still has to be bought, the Brother ZPL question settled, and a disambiguation rule agreed |
| 2 | **Photograph the air receiver's plate** on `FA2306` — volume, design pressure, year, serial | **T021**, the pressure-system question. Turns an inference into a fact |
| 3 | **Photograph the ABAC's yellow service label** again, and look for any service paperwork | **T020** — is the compressor overdue? |
| 4 | **Anemometer reading at each machine's extraction port**, machines running | **T014** *and* the extraction half of **T018**. Hebrock ≥25 m/s, F45 ≥20 m/s, Vitap ~2000 m³/h |
| 5 | **Check the F45 has a water separator and 40 µm filter** on its air feed | Its manual requires them (ISO 8573-1:2010 [7:4:-]) — never verified |
| 6 | **Photograph the Vitap's type plate** | **T012** — confirm serial `320070 AT`, which came off an invoice, not the machine |
| 7 | **Photograph the Altendorf's type plate** | **T009** — the KB has only an internal job number, `23-11-12-005`. *Sharpened: the electrical schematics that arrived 2026-09-18 contain **no serial number**, so this photo is now the main route* |
| 7b | **Photograph one F45 schematic sheet header + title block** at readable resolution | The scan's OCR lost it. Two candidate codes sit there — `F4515` (a plant designation, **not** a serial) and a garbled `FNI_001_ALD09`. One sharp photo likely settles T009 |
| 8 | **Put an asset label on the Brother printer** (`FA2401`) | The only registered asset with no physical tag |

Items 2–5 and 8 are all within a few metres of each other.

---

## 2. Documents still wanted

| Document | Why it matters | Task |
|---|---|---|
| **VAT invoice for the compressor** | Proforma 208027 evidences the *order*, not payment or delivery | T019 (closed on the proforma, but this would settle it) |
| **A manual confirmed for `STK 10000`** (`FA2402`) | Without it the extractor **cannot join the Maintenance Schedule or Fault Log** — no filter-change interval exists | T014 |
| **Altendorf F45 safety certificates** | HM 220023/220024/220025 **expired 22.02.2024** | **T007** |
| ~~F45 electrical schematics~~ | **ARRIVED 2026-09-18**, two parts. Poor scan — circuit lines lost to OCR, ~two-thirds of sheets unreadable. Yielded terminal numbers and fault codes, **not** the serial and **not** the PTC resistance figure. *A better scan would be worth more than another document* | T009, T011, T018 |
| **Complete `TpaCad.pdf` / `Workings.pdf`** | Likely already on the Albatros PC at `Albatros\Help\` | T015 |
| **Brother TD-4420DN actual invoice** | Only an order receipt has been seen | — |
| **Inventair disposal dates and sale proceeds** (`FA2302`, `FA2305`) | Both carry purchase prices, so both disposals have a book consequence | — |
| **Unit 31 lease body** | Only the cover page seen. Alterations / repair / nuisance clauses bear on ducting, three-phase runs and bolting machines to the slab | — |
| **R&J Machinery confirmation** | A dealer sticker on the Vitap is the only evidence of who sold `FA2301`/`FA2303`/`FA2304` | — |

---

## 3. Compliance — the sharp end

These are flagged prominently because they are regulatory, not housekeeping. **This KB does not give
regulatory advice**; each needs a qualified answer.

- **`FA2303` safety certificates expired 22.02.2024** (**T007**) — over two and a half years ago,
  unresolved. Ask Altendorf or the supplier whether re-certification is required for continued use.
- **First F45 monthly documented safety check has never been logged** (**T008**). The requirement is
  mandatory and monthly; the Safety Check Log sheet is built and empty.
- **`FA2306` air receiver — written scheme of examination?** (**T021**) If the plate's "500L" is a
  500 litre receiver at 10 bar, PSSR 2000 very likely requires one. *"500L" is a reading of a model
  name, not a specification* — establish what the receiver is first.
- **`FA2306` service history** (**T020**) — label blank, machine delivered November 2023, interval is
  *2,000 hours or 1 year, whichever comes first*. **A blank label is not proof**; ask the supplier.
- **`FA2303` annual PTC electrician check** (**T011**, MT-025) — needs scheduling. *Booking it commits
  the company to a payment, so it is yours, not mine.* **New from the schematics:** the over-temperature
  channels land at **`-X1` terminals 13/14** (main saw motor) and **21/22** (scorer), raising fault codes
  **E43** and **E42**. *Those pairings are read from labels sitting near each other on a sheet whose
  circuit lines did not survive OCR — the electrician must verify against the paper before metering
  anything.* The expected **150–1000 Ω** figure is **not** in these schematics.
- **F-Gas on `FA2306`** (**T020**) — 0.316 t CO₂e is well under the 5-tonne threshold on the plate's own
  figures. Worth a qualified confirmation, not urgent.

---

## 4. Decisions only you can make

- **`FA2304` §6.8 safety check** (**T013**) — does the Vitap's check need a dated, logged record like
  the F45's, or is a pre-cycle functional test enough? The manual doesn't say. MT-036 holds the place.
- **Were the machines re-commissioned after the move to Unit 31?** (**T018**) You've confirmed they're
  "up and running" — that answers whether they *work*, not whether the manuals' post-installation
  checks were done. The silent ones are what matter: extraction velocity, the F45 extraction interlock,
  F45 geometry, Hebrock earthing, Vitap levelling.
- **Shared group Document Register write access** (**T003**) — still unconfirmed, so every document
  here sits at `Document No.` = `pending`. Nine and counting.
- **Who legally owns the machines** (**T004**) — **seven for seven** billed to Fishbone Drylining Ltd,
  never AMFA Furniture Ltd, and AMFA holds the Unit 31 lease. Needs the intercompany side, which is
  outside this KB.
- **T010 is answered and should be closed** — "review `FA2302` once the new extractor's manual arrives".
  `FA2302` is Sold; T014 settled it. Say the word and I'll close it.

---

## 5. Software and CAD

- **TpaCAD Blind-bore-drill fix** (**T016**) — refined but never tested end-to-end. Needs a real
  "Dia. 5mm" CN Tools entry referenced in the failing operation's Tool [T] field. *Note: whether a
  catalog entry added on one machine reaches the other is **unverified** — a shared network does not
  merge two applications' internal databases.*
- **SmartCabinet Wall Support X-sign discrepancy** (**T017**) — two items both "measured from the back
  edge" needed opposite signs (−15 vs +5). Needs visual confirmation on a real job.
- **Which SmartCABINET version is actually installed** — release notes list 3.2.0.9 (07/07/2026).
- **Does SmartCABINET's ERP module already track production?** Worth knowing before building a parallel
  Smartsheet tracker.
- **The shared Google Drive job folder** — never identified or examined. Its naming convention
  constrains any tracking-ID scheme. *May hold CRM customer data — cite, never copy.*

---

## 6. Known debts — recorded, deliberately not fixed

Listed so they stay visible, not because they need action now.

- **The git mirror is partial.** 18 of 25 Wiki articles are on Drive only. **It cannot be back-filled by
  copying** — the connector's read tool doesn't round-trip (a 2 KB test file came back 4 bytes out,
  silently). Closing it needs an owner-side folder download or a real Drive-to-git sync.
- **`related:` front-matter links are not bidirectional.** The fix means re-authoring three 21–30 KB
  articles through a lossy read to change one metadata field. Fix it next time one is rewritten anyway.
- **`FA2402`'s "dust absorption rate 40 m/min"** — recorded verbatim, matches neither the inlet nor the
  filter face velocity. **Not to be used** until a vendor or real manual explains it.
- **`0191 605 2945` is printed on every group asset label** and was in a SIP trunk migration due
  **03/08/2026, a date already passed**. If that number didn't survive, every label points at a dead
  line. Telephony isn't this KB's scope — flagged only because the labels depend on it.
- **The register is known to be incomplete.** A 15 kW compressor feeding all three machines was missing
  until you photographed its label. Hand tools, extraction ductwork, the air receiver and the server
  rack have never been assessed. **Nothing inside the KB can tell us what else is missing.**
- **`AMF` vs `FA` asset-code inconsistency** in AMFA's own Property Register — flagged only.
- **Duplicate manual PDFs** found in a Drive folder outside this KB's tree — not touched.

---

## Closed since the KB started

**T002** CE Declaration obtained · **T005** Hebrock price confirmed by the 70%-balance cross-check on
three invoices · **T006** corner-rounding fault resolved (FL-001) · **T019** compressor registered as
`FA2306`, 2026-09-18.

*`FA2301`–`FA2306`, `FA2401`, `FA2402` — eight assets, two sold, one with no label.*
