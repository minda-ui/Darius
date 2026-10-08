# Change log — 2026-10-08 — extractor motor: new motor bought, old one to repair

Session 30.

## (1) `FL-003` update; repair-shop quote requests prepared

**Owner:** *"We have bought new motor, check emails. Plan is to replace it Friday PM/Saturday AM. Old motor needs
repairing. Find repair shops in Newcastle. Two or three would be great. Create drafts with asking for quote to repair
motor with all motor details."*
- **Drafts not created.** CLAUDE-Rules §6b: mail is read-only — never send, reply, **draft**, forward. The owner chose
  "read-only, suppliers" over "read plus drafts" on 2026-10-03, and the repo's settings deny draft actions. **The email
  text was written for the owner to paste instead**: `Outputs/2026-10-08-extractor-motor-repair-quote-requests.md`.
- **Emails about the new motor not read.** The seller is not an approved sender (only `@lathams.co.uk` and
  `northeastgrinding@outlook.com`); the owner is asked for the sender so it can be approved and recorded first.
- **Shops (web search; their sites not reachable from here):** **ADC Electrical** (Washington; info@ on their own
  site; AEMT member), **Team Rewinds** (Team Valley, Gateshead; sales@ from a directory, to confirm), **BAWCo (NE)**
  (Sunderland; head-office sales@). Advanced Industrial Rewinds (Gateshead) left out — old company shown dissolved.
- **Fault Log `FL-003`** (row `2141833390589828`), *Remedy / action*: new motor bought, swap Fri 9 / Sat 10 Oct, old
  motor to repair; **before the new motor runs: LRE16 9–13 A set at 11.6 A, remake the lugs, insulation-test, check
  rotation, current balance and suction.** Status stays *In Progress*.

## (2) Where to get the LRE16 (9–13 A overload) by Friday

**Owner:** *"Find me LTE16 [LRE16], where I can purchase it. Ideally if I can collect today or tomorrow."*
- **Schneider LRE16** — Easy TeSys (EasyPact TVS) thermal overload, 9–13 A, class 10A; mounts directly on **LC1E**
  contactors, the family the panel uses (K1 is an LC1E1810; the fitted T1 is an LRE22). Setting 11.6 A is in range.
- **No UK web stock found** for the LRE range (listings are Indian, Egyptian, EU in €). UK stock is of the
  **LRD16** (TeSys Deca), which mounts on **LC1D**, not LC1E — **not a direct swap**.
- **Call before driving** (all have trade counters): CEF Kingston Park 0191 286 8692; Rexel Heaton 0191 276 9300;
  Dinning Electrical (Newcastle) 0191 257 9797; Edmundson Electrical, Team Valley (Foster Court).
- **Fallback if no LRE16 by Friday:** an LRD16 on its own mounting terminal block, wired in series in the same
  position — an electrician's job; *the block part number to be confirmed with the wholesaler*. **The motor must not
  run on the LRE22.**

## (3) Mail: minda@ connected on info@'s terms; the LRE16 order found — arrives after the motor swap

- **eBay approved** (*"It's from Ebay"*) — §6b, narrowest scope: order confirmations from `ebay@ebay.co.uk` /
  `ebay@ebay.com`, only for purchases the owner names. Nothing found in info@.
- **minda@fishboneconstruction.co.uk connected** (*"Let's give you access to minda@… via composio"*). Scope put as a
  question; owner chose **"Same as info@"** — read-only, approved senders only. Connection `darius-gmail-minda` created
  by `composio link`, authorised by the owner, **confirmed by `GMAIL_GET_PROFILE` before §6b was amended**, then read.
- **Found (minda@, eBay, 2026-10-08 11:58 UTC):** **Schneider Electric LRE16**, "New NFP" (new, not in factory
  packaging), eBay item 336055236752, order **07-15274-63159**, seller **maxodeals, Roosendaal, Netherlands**. **£13.98 +
  £21.03 postage + £7.00 VAT = £42.01.** **Estimated delivery Sat 10 – Wed 14 Oct** — *after* the planned Fri 9 / Sat 10
  motor swap. Delivered to a home address, not the workshop. *Payment card and address not copied here.*
- **Consequence recorded on `FL-003`:** the new motor should not be run on the LRE22; either commission when the LRE16
  arrives, or get one locally for Friday.
