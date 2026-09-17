# Change log — 2026-09-15 — Invoice and CE Declaration processed

**Session 3.** Owner provided a photo of the Hebrock F4's EC Declaration of Conformity ("this is
for 3" — closing open question / Task T002 from Session 2), then asked to check `Raw/` for the
purchase invoice.

## What was found

**EC Declaration of Conformity** (photo, filed to `Raw/` as
`2026-09-15_hebrock_ce-declaration-of-conformity-f4-f3809.jpg`): confirms Machine type "F 4",
**Machine no. F3809** (this was previously just a manual template example, now confirmed as the
real serial number), signed 16.01.2023 by Hebrock's Technical Director. Covers the Machinery
Directive 2006/42/EG, Low Voltage Directive 2014/35/EU and EMC Directive 2014/30/EU, with a full
list of harmonised standards. This closes the compliance gap flagged in Session 2.

**Invoice 100155** (already in `Raw/`, dated 09/11/2023, a "70% Balance" invoice referencing order
ref OCN231184 and a separate invoice 100141 for the VAT): billed to and delivered at **Fishbone
Drylining Limited** (now Fishbone Construction Ltd), Unit 32 Point Pleasant Industrial Estate,
Wallsend NE28 6HA — **not to AMFA Furniture Ltd**. Lists two machines: the Hebrock F4 (Serial 3809,
£42,000.00) and an **Inventair MK1 MTFA dust/fume extractor** (Serial 1971, £3,410.00) — a second
asset bought the same day, not previously known to this KB, and very likely the F4's own dust
extraction unit given the manual's extraction requirements.

## What was done

**Corrected `FA2601` to `FA2301`.** The asset code assigned in Session 2 assumed a 2026 acquisition
year because no purchase date was known. The invoice proves 2023. Per `CLAUDE.md` §1's own
instruction ("correct this code if that assumption turns out wrong, before assigning `FA2602`"),
the code was corrected in place — in the Smartsheet Machinery Register row, the Wiki article, and
this KB's own registers — rather than left wrong or quietly worked around. Nothing else had been
built on the old code yet, so this was a clean fix.

**Registered `FA2302`** (Inventair MK1 MTFA) as a new Machinery Register row with the facts the
invoice gives (manufacturer, model, serial, price, date, location) — no manual on file yet, so no
Wiki article for it yet.

**Updated** `Wiki/Machinery/hebrock-f4-next-edge-bander.md`: Key facts now show the confirmed
serial number, full CE compliance detail, purchase date/price/location, and the companion
`FA2302` purchase; Safety section's former "compliance gap" note now says the gap is resolved; Open
questions dropped the two closed items (serial number, CE Declaration) and gained two new ones
(owning entity, exact price given the 70%-balance/invoice-100141 ambiguity).

**Smartsheet:**
- Machinery Register: `FA2301` row updated (ID, Serial Number, Location, Purchase Date, Purchase
 price, Note); new `FA2302` row added.
- Document Register: two new rows — invoice 100155, and the CE Declaration — both `Document No.`
 `pending` (same reasoning as Session 2: this KB isn't entitled to self-assign a group document
 number, and appending to the shared cross-company register hasn't been confirmed as this KB's to
 do yet).
- Tasks: **T002 marked Done** (CE Declaration found). **T001 updated** — partly resolved (serial,
 purchase date/price now known) but left Open, since the ownership question isn't settled. **Two
 new tasks raised**: T004 (confirm which entity legally owns `FA2301`/`FA2302` — invoiced to
 Fishbone Drylining Limited, not AMFA Furniture Ltd) and T005 (locate invoice 100141 and confirm
 whether £42,000/£3,410 are full prices or just the 70% balance).

## Judgement calls made, flagged for the owner

- **Did not assume AMFA Furniture Ltd owns either machine** just because they sit in its workshop.
 The invoice says otherwise, and getting this wrong would misstate whose balance sheet these
 assets belong on. Raised as T004 rather than guessed.
- **Did not treat £42,000 as a confirmed full price** — the invoice's own wording ("70% Balance",
 referencing a separate VAT invoice 100141) makes that a real, not hypothetical, ambiguity.
- **Corrected the asset code rather than leaving `FA2601` as a "retired" stub** — it was one day
 old, nothing else referenced it outside this KB, and leaving two codes for one machine would be
 more confusing than fixing the one that was wrong.

## Open questions carried forward

See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`, "Open questions" — owning entity, exact
price, purchase-vs-order date, the F2/F4/F5 dimension-table ambiguity, an illegible
dust-extraction spec, and the PLC-battery part-name mismatch.
