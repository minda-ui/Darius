---
name: workshop-price-for-sales
description: >
  Answer Sales' (Nadia's) requests for a workshop costing or workshop price on an enquiry (ENQ-…) or job (AM…):
  read her Hub row and Raw note, cost the job on the owner's workshop rules, check it against her drawings and spec,
  reply with a note in her Raw/ and close the Hub row. Use when the owner says "check on Nadia", "send over to Nadia",
  or a Hub Tasks & Requests row from Nadia (for Minda) asks Darius for a pre-quote costing, an updated price, fronts,
  knobs, a final workshop price or "what is being made".
---

# Workshop price for Sales

Worked out on 2026-11-04 (ENQ-0002 three rounds, ENQ-0003 = AM2602 Ladder; Hub AWT-1105, 1107, 1109, 1110, 1113).

**The split (owner, 04/11):** *"you providing workshop pricing and Nadia do sales pricing. You use workshop pricing
rules"*. Darius gives the **workshop price** only: materials at cost + 15 %, labour £45/h, machine £65/h, VAT 20 %
(`project-quote-from-smartcabinet` §4). **Never add a sales mark-up or choose between pricing rules** — that is Sales'.

## Run it
1. **Find the work.** Hub sheet `8860839228606340`: rows with Assigned to = Darius from Nadia (and Nadia's rows
   that answer Darius's). Nadia's Raw notes land in the **workshop** `Raw/` named `…_Nadia-to-Darius_…md`; her own Raw
   is `1OqSdoWEIw-lagtdSUS1tWRs6ViDsGMgx`, her job folders under `Drafts/ENQ-…`. Read every new note and image.
2. **Find the real design first.** If the job already exists in SmartCabinet (Review or Furniture folder), cost from
   **those files**, not from assumptions (*"ENQ-0003 is AM002 Ladder"*). Ask Minda only what the files and notes
   cannot tell.
3. **Compare the design with what Sales holds** — sizes, doors/fronts, handles, base, finish — and **list every
   difference**. On 04/11 this caught a unit released without its doors. A difference is a question for Minda, never
   silently resolved.
4. **Cost it** with `project-quote-from-smartcabinet` (cutting list, sheets, edging, hardware from the price
   libraries, hours, the build-up). A SmartCabinet parts-list supplier label ("Interior Door Systems Stratford") is
   **not** a supplier — fronts are made in-house unless Minda says otherwise.
5. **Write the note** `Outputs/YYYY-MM-DD-<ENQ/AM>-…md` and the same text to Nadia's `Raw/` as
   `YYYY-MM-DD-from-Darius-<ENQ/AM>-….md` (native `create_file`, `text/markdown`, conversion off; check the size).
   Sections: feasible? · cutting list / board / edging / hardware · cost table · hours · not included · lead time ·
   **what blocks a firm price** (⚠ proxies, open questions). No client details.
6. **Hub:** her request row → Done, Done date, a Response that gives the total and the file id. If her next step needs
   doing (price, quote, a changed fact), add a **new row assigned to Nadia** (`raw-handoff-to-employee`: free AWT
   number checked, duplicate guard read back).
7. **Log** in today's change log; commit, push. Tell Minda the total in one line.

## Updates
A correction (fronts in-house, knobs, no fitting, sizes final) is a **new version** of the note (v0.2, v0.3…), with
"what changed" and the delta at the top; keep the earlier notes in her Raw as sent.
