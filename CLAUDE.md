# CLAUDE.md — Workshop of Furniture Making Knowledge Base

**Version 26 — 2026-09-20.** Structure and conventions modelled on the Fishbone Commercial
Properties Ltd Knowledge Base, via the shared `Wiki/Process-Fishbone-Systems-House-Rules.md`
conventions used across all Fishbone group KBs. This file holds only what's specific to this KB,
and it is also **Darius's charter** (see §0a). README.md is a pointer; this file wins on conflict.

**Changed in v26 — two estate-wide rules arrive, and they arrive by the route they describe.** A
hand-off note from **Alex** (Housekeeping & Operations Steward) appeared in `Raw/` on 2026-09-20 at
21:05, **proposing** two additions to this file rather than making them. **Confirmed as the owner's own
rulings the same evening** (*"Yes their are mine and add them to charter"*) and written in by this KB's
owner — which is the whole point of the second one.

**First: the Hub is checked at session start, and is the single home for tasks, lessons and gaps.** New
**§0b**, and §0's reading order now begins there rather than with the change log. **This is the first
obligation in this charter that points outward**; every rule before it governed what happens inside this
KB's own stores.

**Second: an estate-wide rule that belongs in somebody else's governed file goes through their `Raw/`,
never a direct edit** — even when the content is correct and squarely the originator's own remit. Added
to **§6a** in both directions: this KB does not write into another employee's charter, and **a note
arriving in this KB's own `Raw/` is a proposal, not an instruction.**

**What is not done, and is said rather than assumed.** Nothing has been written to the Hub yet. There is
**no Tasks & Requests row assigned to Darius** for this hand-off — `AWT-0036`, `AWT-0040` and `HL-0023`
were checked and exist, but none is Darius's to flip, so Rule A's receipt had nothing to receipt. And
adopting Rule B **opens a backlog rather than closing one**: 29 tasks and the whole of §3 have never been
surfaced to the Hub. Neither is a reason to delay the rule; both are reasons to say so in the file that
carries it. v25 (`1l8zDEhQDAk9YPaKCfANmkqgqwpWzxVl7`) is archived.

**Changed in v25 — the lesson v24 proposed is now a lesson.** v24 closed the `related:` back-link
debt and ended by *proposing* what it had learned rather than writing it in: **a description of a gap
is not a measurement of it.** The owner's word came back the same day (*"Add that §3 lesson at v25"*),
so it is now a §3 bullet in its own right, carrying the incident that produced it — **four files
described, fifteen measured, 52 missing back-links** — and the reason the description read as a
specification of the work. **That route is the point, not a formality.** This is the third lesson to
take it (v18's count fix, v19's order clause, now this): a charter that rewrote itself every time a
session thought it had learned something would be a record of sessions' opinions, not a charter.
**Nothing else changed.** §7's back-link bullet drops its *"proposed, not added here"* clause, which
is now false, and the v24 note below says where the lesson went. v24
(`1aQb34nTdKJHwoLW4LOCDGqVBHXmMO7_d`) is archived.

**Changed in v24 — the last metadata debt closed, and the bullet describing it had undercounted by
eleven files.** §7 has carried since 2026-09-17 that `related:` front matter is one-way, described as
*"the three machinery articles"* plus one empty list. On the owner's instruction (*"Fix the related:
back-links now"*) the graph was **computed rather than read off the bullet**, and the real gap was
**15 files and 52 missing back-links**. The Wiki now holds **134 directed edges — 67 symmetric pairs,
nothing asymmetric, dangling or duplicated** — with every article **body hash-identical** before and
after, and all 15 Drive copies re-uploaded and **verified byte-identical by download–decode–`diff`**.
That is the §7 upkeep rule added in v23 obeyed for the first time: both stores, same session.

**Why the bullet undercounted is the part worth keeping.** It named the articles somebody had
*noticed* — the two 2024 assets had been written last and linked out to the three older machinery
articles, so those three stood out. **The other eleven were invisible from inside the KB**, in exactly
the way the unregistered compressor was: nothing in a one-way link announces itself from the side that
is missing. *Proposed for the owner rather than added here, the same route the v18 and v19 changes
took:* a §3 lesson that **a description of a gap is not a measurement of it** — where a gap can be
computed, compute it before trusting the count somebody wrote down. *Approved and added to §3 at
v25.* v23 (`1RqHSDRGxXgbOCBwPI4rV7QRafRV_h9We`) is archived.

**Changed in v23 — the mirror is complete, and the debt v22 closed in argument is now closed in fact.**
v22 established that `download_file_content` returns stored bytes and said plainly that **nothing had
been back-filled yet** — a capability, not an outcome. The back-fill ran the same day. **Every Wiki
article that lived on Drive only is now in git**, fetched as exact bytes, decoded straight to disk and
checked against Drive's own `fileSize`; all matched. Nothing was re-typed and nothing passed through a
rendering.

**The one that matters most is the smallest.** `Suppliers/altendorf-gmbh.md` is the 2,007-byte article
the v12 fidelity test rebuilt **four bytes short, silently** — the failure that made the mirror partial
in the first place and kept it that way for eleven versions. It now lands **exact**. *The obstacle was
never the file; it was the tool being used to read it.*

**One check before anything was committed**, because the F45 article is the one carrying a security
decision: the **ElmoDrive remote-maintenance access code** was removed from it on 2026-09-17, and the
Drive copy was verified to still be without it — the article states the code is *"deliberately not
reproduced here"* and its Changes table records the removal. A scan of all eighteen for credentials
found nothing else. **A back-fill copies whatever the source holds, so the source gets checked first.**

**§1 and §7 are rewritten accordingly, and the count is deliberately not repeated here** (§3): run
`git ls-files 'Wiki/**/*.md' | wc -l` and read the registers. **What replaces the debt is an upkeep
rule** — an article written to one store and not the other re-opens the gap. v22
(`1FZA7ZjuICub_4ZwC32PJopldXLv0k09r`) is archived.

**Changed in v22 — the tool this file called "the single most useful tool this KB does not have" was
in the connector all along.** §7 has carried since v20 a debt saying a read path that returns bytes would
close two problems at once: the git mirror that cannot be back-filled, and the order check that cannot run
above about 82 KB. **The Drive connector has one — `download_file_content`, which returns the stored bytes
base64-encoded — and it had never been called.** The re-formatting and the empty-above-82 KB behaviour both
belong to `read_file_content`, a *different tool*; the KB measured one read path and wrote the limitation
down against the connector.

**Both debts are closed by measurement, not argument.** `tpacad-blind-bore-tool-id-fix.md` was downloaded,
decoded and diffed against its local copy: **byte-identical apart from one real eight-character
difference** — no escaped punctuation, no appended hard breaks, no drift. And **`CLAUDE.md` v21 came back
whole at 90,475 bytes**, well past the bracket where `read_file_content` returns an empty string. **So the
order check has no ceiling any more**: download, decode, `diff` against local, on any file in this KB. The
check stops being an argument about how a file was produced and becomes a verification of what it contains.

**Two corrections fall out of the same test, and both are mine.** The new article's unexplained **−8 bytes**
was never a connector defect: local read *"five of them"*, the Drive paste read *"five"*. I had bounded it
at three attempts and written it down as unresolved when **one diff would have named it.** And this file's
**+306 bytes** was not corruption either — the diff is a single hunk, the Operational-systems bullet that
was in the Drive paste and missing from local. **The 90 KB paste carried no drift at all.** I had archived
that copy **DO NOT CITE** on suspicion alone; the label came off within the hour, because a wrongly-labelled
file is the trap §3 already names twice. New §3 lesson: *check whether the tool you are blaming is the tool
you used.* v21 (`1Nzs26QcEIVMDa8px2jU4Eq7xGCp2h_bR`) is archived.

**Changed in v21 — the fix this file gave for T016 pointed at the wrong computer, and the source
that says so was already in the KB.** §7 has said since v18 that *"the gap is a missing Ø5 entry in
SmartCABINET's Cabineo X drill-head profile"* and that T016 is *"a catalog entry and a test run"*.
**Reading `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` in full — the contemporaneous
record written at the machine on 2026-09-15, Technology dialog open, two positions checked by hand —
shows that is wrong.** That article carries both findings and separates them in terms: the catalog gap
is *"**unrelated** to the TpaCAD optimizer ambiguity — a gap in SmartCabinet's own head/tool catalog,
**not** the Vitap's tool archive (which does have 5mm tools, both Blind and Through)"*.

**The Vitap is not missing a Ø5 tool. It has five.** Blind Ø5 mm sits on **bushes 6–10**, every one at
**ID 0**, so resolving by diameter + type offers five equally valid candidates and no documented
tie-break; Through Ø5 resolves cleanly because it has exactly one bush. **The fix is two steps, both at
the Vitap** — give one Blind Ø5 bush a real ID, then set the failing operation's `Tool` field to it,
which per the manual *"prevails over the programming per diameter"*. Written up as
`Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`, with the verification test and the reason the
Through-bore workaround must not be used to close it.

**How the error was made, because the shape is the point.** I connected two facts sitting in the same
article — a head profile named *"Cabineo X"* and a missing `Dia. 5mm` row — and asserted the second
caused the first's failure, **without re-reading the article that says they are unrelated.** §3's *a
fact recorded without a source hardens into an assumption* has a sharper sibling: **the source existed
and was not consulted.** A KB is only as good as the habit of going back to it, and the risk grows with
its size — this file now summarises articles it no longer quotes. New §3 lesson: *re-read the primary
record before reframing what a task is.* Swept through §7, Smartsheet T016 (title and note) and
`Wiki/index.md`, whose carcase-fixings entry asserted the same thing. v20
(`1xi9GGr1H0VfkoHag8kEBOG9dVH3bgAg2`) is archived.

**Changed in v20 — the rule added in v19 gets its own limits written next to it, and the tool that
would lift them is named as a debt.** Two items, both proposed at v19 and approved by the owner
(*"Add both v20 items now"*).

**First: the order check has a size ceiling, and §3 now says so.** v19 told a future reader to verify
order by reading the file back. That instruction silently fails on large files — `CLAUDE.md` itself
returned an **empty** `fileContent` at 82,310 bytes where `kb-registers.md` read fine at 58,410.
**A rule that cannot be followed on the most important file in the KB, and says nothing about it, is
worse than no rule**, because the reader assumes it ran. §3 now carries the bracket, what stands in
for the check above it, and **one practical trap found by running it**: the connector escapes backticks
and asterisks on read, so **order anchors must be plain text** — markdown ones produce a false failure,
which this KB saw once and nearly believed.

**Second: a read path that returns bytes is now a named debt in §7, not an implied one.** The empty
read and the partial git mirror are **the same missing capability wearing two faces** — the mirror
cannot be back-filled because the read tool re-formats, and the order check cannot run because the read
tool gives up on size. **One mechanism closes both**, which is a better reason to go looking than either
debt on its own, and neither bullet said so until now. v19 (`18_O7X7D8HK5wDH37g7JWRB4PdXYTGrqK`) is
archived.

**Changed in v19 — the upload check that has protected this KB for three days turns out to have a
blind spot, and it was found the hard way.** §3's *verify like with like* rule — compare `wc -c` both
sides — has caught every upload error since 2026-09-17. On 2026-09-19 it passed a file that was wrong.
`Outputs/kb-registers.md` went to Drive with **two Outputs rows in the wrong order**, because I moved one
while pasting; the byte count came back **56,265, exactly matching local**, and I reported it as
byte-exact. **It was byte-exact. The file was still wrong.** Moving two rows of a table changes nothing
about the total, so **the check is blind to any error that permutes content rather than changing it** —
a reordering, or a swap of two equal-length values. Caught by reading the row order back instead of
trusting the number, which is §3's *trust the API's response, not its status code* arriving from a new
direction: **the number in the response was true and the conclusion drawn from it was false.** Fixed by
re-uploading in the right order; the wrong-order copy is archived as
`ARCHIVED-2026-09-19c-kb-registers.md` and **labelled DO NOT CITE**, because its content is correct and
only its order is not — exactly the file someone would otherwise cite in good faith. §3's *verify like
with like* now carries the clause: **a size match is necessary and not sufficient, and proves nothing
about order.** Owner's decision to add it, 2026-09-19 (*"Yes, add that clause at v19"*), after it was
proposed rather than added unilaterally — the same route the v18 count fix took.
v18 (`1wS22TUTeWjYX8RkQIkkrrQq98ZqJnpHy`) is archived.

**Changed in v18 — this file stopped carrying a number it kept getting wrong.** Four times now — v12
said *"four"*, v13 *"fifteen"*, v16 *"seven"*, v17 *"nine / twenty-seven"* — this charter has stated how
many Wiki articles exist and how many are mirrored, and **four times the figure was stale by the time
anyone read it**, because an article written in any session invalidates it. v17 even made recounting a
standing rule and then went stale the same day it was written. **A rule that has to be obeyed on every
edit of a weekly document is not a rule, it is a trap.** So the figures are **gone from this file**: §1
and §7 now say the mirror is partial and **point at `Outputs/kb-registers.md`**, whose Wiki-structure
rows carry the count at the moment each article was added, with the command that produced it. Anyone
quoting a number runs `git ls-files 'Wiki/**/*.md' | wc -l` and reads the registers for the Drive-only
side. **The counting discipline is unchanged and the instruction to recount is unchanged** — only the
place the answer lives has moved, from a document revised weekly to one revised every session. Owner's
decision, 2026-09-19: *"I agree with dropping figures from Claude.md and pointing to registers. That
makes process a bit lighter."* New §3 lesson: *put a fact where its own update cycle lives.* v17
(`1XseIOKRWe7rMgnxU88FkHbpPJBxhV5Jy`) is archived.

**Also in v18 — three tasks closed and one half closed, all from the owner describing how the shop
works.** **The production route was recorded for the first time**: SmartCABINET optimisation → panel
cutting list → **F45 cut** → **F4 edging** → **Vitap drill** → assembly desk. Five sessions had
documented three machines in detail without ever recording the order they are used in — the same shape
of gap as the unregistered compressor, and it closed **T026** (the 2800 × 2070 nesting sheet was never
in conflict with the Vitap's 1250 mm width; the sheet is cut on the saw and the Vitap only sees single
panels) and **T028** (the saw works from a cutting list). **T029 was raised and closed the same
morning**: the cutting list is **finished sizes**, and the F4 trims each panel by the tape thickness
*before* applying the tape, so **the bander is dimension-neutral and there is no allowance anywhere** —
which confirms the derived nominal and means a library unit can be defined without its edging pattern.
It also makes the F4 dimension-critical: **tape thickness and pre-mill trim are one decision**, and
changing one without the other fails a whole batch rather than one panel. **T025 closed — Cabineo X
chosen and ordered, with confirmat kept as Plan B and held in stock**; three things followed that were
not visible before the decision (**no Ø15 drill is needed**, since drilled and routed are alternatives
and the master routes the pocket; **T016 is therefore purely a software problem** with nothing to buy;
and **a Cabineo-machined unit assembles with confirmat without re-drawing anything**, because the
pockets are in the carcase's inside faces and an empty one is hidden — so T016 drops from blocker to
priority). **T024 half closed**: shelf depth **255 = 300 − 16 − 19 − 10**, the chain closing to the
millimetre, with the **16 mm back-panel step-back for the Häfele concealed wall mount** and the **10 mm
shelf-front step-back** both now recorded as **specification**; the 266 and 256 on the earlier folders
are **an earlier design, not the defect v17 recorded**. **And a correction of mine**: **T027** had said
the shop appeared to lack a 35 mm hinge-cup bit. **It has one, fitted to the Vitap.** I had read *"how
do I cut a 35 mm hole with a 12 mm cutter"* as evidence the tool was absent, when the owner had said
there was a *problem* — **asking how to do something another way is not evidence the ordinary way is
unavailable.**

**Changed in v17 — the kitchen unit library started, and comparing three units found what reading
one could not.** The owner asked for a library of low-cost kitchen units and named **`AMFA Wall Unit
600 RH`** as the master. Its `worklist.xmlst` was decoded: eleven parts, **19 mm throughout including
the back and the door**, and **no file anywhere states the finished unit size** — so it was derived
from the part sizes, arithmetic shown, as **600 wide × 900 high × 300 deep**. The `300mm` and `600mm
Wall unit` worklists were then decoded and compared, which **corroborated the derivation
independently** (the same width rules hold across all three) and turned up a real defect: **shelf
depth is 266, 256 and 255 mm on three carcases that are all 300 deep**. Recorded with all three
values, not resolved by preferring the master's. **Nothing was created, moved or renamed on Drive** —
the range and the carcase spec are commercial decisions. New article
`Wiki/Software/kitchen-unit-library.md`; new §3 lesson: *comparing siblings finds what reading one
cannot.*

**And T016 stopped being a one-off.** Every hole in the master's `03-BOTTOM.TCN` carries a diameter
and **no tool number** — the exact condition behind the live "Tool for this working not found" fault.
*That reading of the parameter indices is mine and is not documented in the manual extract this KB
holds*, but if it is right, **T016 fails every unit in the library identically**, so it is now a
precondition for populating the library rather than a single machine's fault. **Counts recounted, as
§1 requires and as this file has twice failed to do** — *and stale again within the day, which is what
finally moved them out of this file in v18; the figures v17 quoted here are deliberately not repeated,
because a superseded count is exactly the thing that misleads a future reader.*
v16 (`1V6aSqeW7Lrj9wNNPjsxEj_cPDbcPS3mO`) is archived.

**Changed in v16 — a walk round the floor closed two tasks that documents could not, and one of them
had been answered in this KB all along under the wrong name.** The owner photographed four type plates.
**`FA2303`'s plate carries `S/N: 23-11-12-005`** — the exact number this KB has held since Session 6 and
recorded as *"an Altendorf internal job number"* with *"no confirmed serial number"*. **T009 closed.**
That same morning, two 10 MB schematic PDFs had been put through extraction specifically hunting for
that serial; both came back empty and recommended photographing a title block. **The answer was never in
the document.** New §3 lesson: *a fact filed under the wrong name is worse than a missing one, because
the KB stops looking for it.* **T012 closed** too — the Vitap's plate reads `320070 AT`, identical to the
invoice-derived value. And **`FA2402`'s plate states `DUST CAPACITY 10.000 M³/H` as its own field**, so
the long-running *"10000 is a reading of the model name"* caveat is fully discharged.

**Also in v16.** The **QR payload is known**: a bare four-digit label number as plain text (`Text: 0027`),
which unblocks barcode Phase 1 and vindicates the two-namespace design — a scan yields a *label number*
that must be looked up against `Asset Label No.` to reach an `FA` code (Task **T022** for what still
blocks Phase 1). The **F45 electrical schematics** arrived and moved **T018**: the machine *does* provide
volt-free terminals to start an external extractor, so the question becomes whether they are wired, not
whether they exist. Two **weight discrepancies recorded, not resolved** (`FA2304` 1385 kg on the plate vs
1030 kg in the manual; `FA2402` 740 kg vs 720 kg quoted). And a second §3 lesson, from finding that the
two "parts" of the TPA CAD manual are the **even and odd pages of one duplex scan**, not two volumes.
v15 (`13B3LV7siGSR39EFjedrnPiRwUPDVTM5n`) is archived.

**Changed in v15 — the compressor was delivered to Unit 32, and a premises claim of mine is withdrawn.**
Hours after v14, the owner corrected the one thing in it I had inferred rather than read: *"Compressor was
all the time unit 31, it was delivered to unit 32."* Proforma 208027 prints **"DELIVERY AS PER INV ADDRESS"**
against a **Unit 31** address, and I recorded that as where the machine went. **It is not a delivery record.**
Unit 31 is the billing address; the compressor went to **Unit 32**, with the three machines it feeds.

**Two consequences.** The open question "was the compressor in a different building from its machines?" is
**answered: no** — it arrived with them and has moved with them. And **v14's claim that "the group was using
both units in November 2023" is withdrawn**: it rested entirely on reading that printed clause as fact, so
nothing in this KB now places the group in Unit 31 before **2024** (`FA2402` delivered there October 2024;
`FA2401` shipped to "Fishbone Waste, Unit 31" May 2024). **The sixth unsourced inference corrected in two
days**, and the same family as the 5.4 bar gauge — treating something printed on a page as a record of what
physically happened. New §3 lesson: *a printed delivery clause is not a delivery note.* Swept through the
Machinery Register, Document Register, T004, both Wiki articles and this file — the v14 lesson applied to
its own author, one day later. v14 (`1BEZ8NYkfCVRU0mEv-fnIVnRAX-Y8GSh_`) is archived.

**Changed in v14 — the compressor is on the register, and a correction was found still standing where
the sweep had not reached.** `Raw/FISHBONE DRYLINING LTD.pdf` arrived on 2026-09-18: **proforma invoice
208027**, Pneumatic Tools & Compressors Ltd, **14/11/2023**, £9,696.00 net / £11,635.20 inc VAT. It closed
**T019**, the only blocking item in the KB, and the ABAC compressor is now **`FA2306`**. What tied the paper
to the machine was the **product number `4152025548`, identical on proforma and type plate** — the *model
designations disagree* (plate `GENESIS 15 500L`, proforma `GENESIS C67`) and are **recorded, not merged**.
The year was evidenced before the code was assigned, for the fourth time; and the caveat is stated rather
than buried — **a proforma evidences the order, not payment or delivery**, so the VAT invoice is still
wanted. New task **T021**: the plate's `500L` reads as a 500 litre receiver, which at 10 bar would be a
pressure system needing a written scheme of examination — but *that is a reading of a model name, not a
specification*, so T021 starts by establishing what the receiver actually is.

**And the lesson that came with it.** Task **T016** in Smartsheet still asserted the two computers *"are
not networked - confirmed"* — the claim the owner corrected on 2026-09-17. The sweep of that correction
covered this file and the Wiki articles; **it never touched the Smartsheet note fields**, so a retracted
claim was still giving instructions, with the word *confirmed* attached. New §3 lesson: *a correction has
to be swept through every store the claim reached.* v13 (`1NKINGz5XwT9IdxtHdKerqeJPdssr6vaR`) is archived.

**Changed in v13 — the compressor's "low pressure" was not low pressure.** §7 recorded the ABAC's
gauge at **5.4 bar** as a live concern, "below what all three machines ask for". The owner corrected it
the same evening: **the compressor was switched off when it was photographed.** 5.4 bar was residual
pressure standing in the receiver, not delivered line pressure, and it says nothing about what the
machines get when running. **There is no low-pressure finding, and there never was one.** The error was
mine and of a specific kind: reading a gauge in a photograph and inferring an *operating* condition
without establishing whether the machine was running — the **fifth unsourced inference corrected in a
single day**, after the networking claim, the Unit 32 address, the "residential" billing address and
§1's git-mirror claim. §3's lesson gains a second clause: *a reading is only a reading of the state the
thing was actually in.* Corrected in §7 and in Task T019; T019's own note had at least hedged it
("a single reading proves nothing… this is to VERIFY, not a fault"), but never gave the reason.
v12 (`1qB1lDeGiEKKVTwoOlRvc9suMtFobXQ4j`) is archived.

**Changed in v12 — a claim in this file was not true, and the reason it can't be made true.** §1 has
said since 2026-09-16 that the git mirror "is kept in step" with Drive. **It is not.** The mirror holds
this charter, `README.md`, `Wiki/index.md`, `Outputs/`, and the four Wiki articles written on
2026-09-17 — **not** the other fifteen Wiki articles, which exist on Drive only. Found while trying to
close that gap, and corrected here rather than left as the fourth unsourced claim of the day.

**And the gap cannot be closed by copying.** The Drive connector's read tool returns a *re-formatted*
rendering — punctuation escaped, hard-break spaces appended — not the bytes on disk. Reconstructing a
2 KB article from it landed **4 bytes out**, and the error is silent. Copying fifteen articles that way
would produce a mirror that looks right and differs from the source in ways nobody would notice, which
is worse than a mirror that is honestly incomplete. **So the mirror stays partial and says so**, and
the same finding rules out rewriting the three machinery articles just to add `related:` back-links —
a metadata fix is not worth re-authoring 75 KB of text through a lossy read. Both are recorded as debt
in §7. Also new in §3: *verify like with like* — a byte count is not a character count.
v11 (`1edazoWoadKnX-pz2vy-bEE0lCCOd1Gga`) is archived.

**Changed in v11 — the register caught up with the shop floor.** The third session-block of the same
day, after the owner walked the workshop photographing each machine as its asset label went on. Five
labels mapped (`0017`-`0021`); **both Inventair extractors sold** (`FA2302`, `FA2305`), which answers
the supersession question T014 had carried since Session 8 — by replacing both with one centralised
unit; **`FA2402` registered** (AES SAF 10,000 STK) with its acquisition year evidenced from invoice
22473 first and its full specification sourced from the vendor's quotation afterwards; and an **ABAC
screw compressor discovered that was never on the register at all** — the machine that feeds the
pneumatics of all three production machines. **No code was assigned to it**, because its plate carries
a *manufacture* year and this KB's convention needs an *acquisition* year: the `FA2601` lesson, applied
for the third time in one day. Unit 30's postcode confirmed (NE28 6HA), the `[confirm]` dropped. New
§3 lesson: *a register only contains what somebody thought to put in it.*
v10 (`1l4lgxmy5LJNdQQnTPIVVSC0YbY7mbcf4`) is archived.

**Changed in v10 — the workshop is at Unit 31, not Unit 32.** The second documented-fact correction of
the same day. §7 had recorded the workshop at **Unit 32** since the KB's first session. The owner corrected
it on 2026-09-17: **Unit 32 is no longer held.** The **workshop is Unit 31**; **office and warehouse are
Unit 30**. Evidenced by the lease cover page — *Forth England Limited* (landlord) and *Furniture by
Fishbone Limited* (tenant), **dated 25 June 2026**, for **Unit 31, Point Pleasant Industrial Estate,
Wallsend, Tyne and Wear NE28 6HA**. All six Machinery Register rows were corrected to Unit 31 and the three
machinery articles swept. **This also means the machines were physically moved**, which the KB had no record
of at all — see the re-commissioning question in §7. v9 (`1STw2KS1Ny7GKeDRMC_UbLxZtkjPtCr8z`) is archived.

**Changed in v9 — the networking claim corrected.** §1 stated since the KB's early sessions that the
design computer and the CNC control PC were **not** networked and that files moved by USB. The owner
corrected this on 2026-09-17: the workshop runs on a network served from an on-site server rack, a
WiFi 7 access point covers the whole floor, and **files are shared through Google Drive in a dedicated
folder**. The claim had no citation and no `[confirm]` marker, so nothing flagged it as inferred and it
survived six versions — see the new lesson in §3. Corrected here, with the downstream articles swept in
the same session. v8 (`1teaQsa5DRuZGbtvSSSRjmpAo6p6Uu0Gp`) is archived.

**Changed in v8 — fork reconciliation + owner assigned.** Two parallel session-lines on 2026-09-15/16
had each rewritten this file (and `Wiki/index.md` and `Outputs/kb-registers.md`) without seeing the
other: an *operational-systems* line (v5 — maintenance, troubleshooting, the SmartCabinet workflow,
the Maintenance Schedule + Fault Log sheets) and a *CAD-day* line (v7 — the SmartCabinet Wall Support
Cam Table reference and the refined TpaCAD tool-ambiguity fix). No content was lost — every dated
change-log file survived; only these three index files had split. v8 **unions both lines** into one
clean control layer and renumbers the sessions into a single timeline. Both prior `CLAUDE.md` copies
(v5 `1My3wCRZXG_sc8l_EY0zgfAUrJ8mbfQKl`, v7 `1zAIAKCoFufSqHCPVaL-tNlFsXlng12ZP`) are archived. At the
same time the KB gained a named owner — **Darius** — so this fork stops happening (one owner, one seat).

## 0a. Who owns this KB — Darius

**Darius** is the Fishbone Group's **fifth AI employee** and the **named owner of this Knowledge Base**:
the Workshop Operations Assistant. Everything in this KB is Darius's patch — the machinery, the
maintenance and fault systems, the SmartCabinet/CAD and TpaCAD knowledge, and the
design→production→Sales tracker. Owner-authorised (Minda) 2026-09-16; coordinated by **Victoria**
(CEO's Assistant, Fishbone Group). Git mirror **`minda-ui/Darius`**; connectors **Google Drive +
Smartsheet + Web (read)** — no Gmail (Darius logs and tracks, it does not send).

**Reach.** Darius **reads** its own KB and the estate it needs (the AMFA Furniture Ltd and Fishbone
Construction Ltd KBs — the asset-ownership question, §7); **writes, unattended,** its own KB and its
own Workshop Smartsheet sheets (Machinery Register, Document Register, Tasks, Safety Check Log,
Maintenance Schedule, Fault Log), **and its own rows on the Workforce Hub** (§0b — own rows only, never
another seat's); and **needs a human** for everything in §6a — appending to the
shared group Document Register (confirmed access only), committing AMFA or Construction to any
purchase/contract/payment, replying to a supplier/insurer/inspector, filing with any regulator, or
touching another KB. The boundaries were already written into this KB's §6a; Darius just puts a name
to them. When two facts that should agree don't, Darius records the contradiction and asks — it never
guesses one into the other (§3).

## 0b. The Fishbone AI Workforce Hub

**The Hub is the estate's shared record for the AI workforce.** Two standing rules govern how this seat
uses it — owner's rulings of 2026-09-20, carried into this KB by Alex's hand-off note of the same date
and confirmed by the owner before being written in.

**Rule A — check the Hub first, at every session start.** Before other work: read **Tasks & Requests**
for Darius's own `Assigned to` rows that are **Open** or **In Progress**; **flip a task being taken up
to In Progress** — that flip *is* the receipt, and it is how the coordinator sees the task landed; treat
the row's **Request as the canonical brief**, reconciling a chat instruction against it rather than
running two versions of one job; **close on the same row** (`Status` = Done, plus a Response). **Own
rows only.**

**Rule B — the Hub is the single home for tasks, lessons and gaps.** Anything that is a task, a lesson
learned, or a missing/gap item about the AI workforce is recorded on the Hub as the shared record:
**actionable work and identified gaps as Tasks & Requests rows; lessons as Help & Lessons rows.** A
local KB log may hold the working detail — and in this KB it usually will, because that is where the
evidence sits — **but the item must be surfaced.** Nothing that is a task, a lesson or a gap may live
only in a local log the coordinator cannot see.

**Sheets:** `Tasks & Requests` (`8860839228606340`), `Help & Lessons` (`7780569054316420`).

**What this changes here, stated plainly.** This KB already has its own task and lesson machinery — the
Workshop **Tasks** sheet (`4087584374523780`, T001–T029) and **§3** of this file. Rule B does not
replace either; it means **neither is the end of the line any more.** As of v26 **nothing from this KB
has been surfaced to the Hub**, and no Hub row is assigned to Darius, so the rule opens a backlog rather
than closing one. *First application is the next session.*

## 0. Start every session here

Before doing anything — including a one-off question — read, in order:
1. **The Workforce Hub** — Tasks & Requests, Darius's own Open / In Progress rows (§0b, Rule A).
2. The newest entries in `Outputs/change-log-*.md` (newest-first index: `Outputs/kb-registers.md`,
   section "Change-log entries").
3. The `pending` and `partial` rows of `Outputs/kb-registers.md`, section "Processed items".
4. `Wiki/index.md` for what's already known.

**Re-read the live control files immediately before editing them** (their current Drive id and size),
and author the edit onto that live copy — never a copy read earlier in the session. The 2026-09-15/16
fork happened because two sessions edited stale copies in parallel; with a single owner this is
avoided, but the discipline stands.

This KB shares a parent company (AMFA Furniture Ltd) with a separate, company-wide KB. If a fact
could be recorded in either, check the AMFA Furniture Ltd KB rather than assuming this one is silent
on it, and cite across rather than duplicate. **This matters concretely**: every machine registered
here — `FA2301`–`FA2306` and `FA2402` — was invoiced to Fishbone Drylining Limited (now Fishbone
Construction Ltd), not to AMFA Furniture Ltd, and so was the SmartCABINET software. `FA2401` names no
company at all. The AMFA KB may hold the intercompany side of this that this KB doesn't have standing
to resolve on its own. See §7.

## 1. Database structure

**Scope.** This KB covers the **machinery and equipment in the AMFA Furniture Ltd workshop** and,
from 2026-09-15, the **operational systems** for running it (maintenance, troubleshooting, the
SmartCabinet design-to-machine workflow) — not the company as a whole. This **includes the software**
used to design and program the machines' work: both the machine-side programming software (TpaCAD,
driving the Vitap) and the design-side CAD software (SmartCabinet, producing the job files TpaCAD
consumes). See the Decisions articles for why it's a separate KB and why the scope was extended.

**Two computers, one network.** The shop runs SmartCabinet on a design/office computer; the CNC
machine's own control PC runs TpaCAD/WSCM/Albatros. **They are networked** — the workshop runs on a
network served from an on-site server rack, with a **WiFi 7** access point covering the whole workshop
floor, and **files are shared between design and machines through Google Drive, in a dedicated
folder** (that folder not yet identified or examined — see §7). *Corrected 2026-09-17 by the owner;
v8 and earlier asserted the opposite.*

**Still open, and not to be assumed either way:** a shared network does not merge two programs'
internal catalogs. SmartCabinet's **CAM Tools** table and TpaCAD's **CN Tools** catalog are separate
application databases, and whether an entry added in one reaches the other automatically is
**unverified**. This bears on the **systemic half** of Task T016 — getting SmartCABINET to emit a Tool
ID on export — and must be checked, not inferred from the fact of a network. *It does not bear on the
immediate fix, which is entirely inside TpaCAD's own outfit (§7).*

**Where it lives.** Google Drive, folder `Workshop of Furniture Making - Knowledge Base`, primary
copy (`1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`). **Drive is the source of truth.**

**The git mirror `minda-ui/Darius` is complete as of 2026-09-19.** It holds this charter, `README.md`,
`Wiki/index.md`, everything in `Outputs/`, and **every Wiki article** — the ones that predated the
mirror were back-filled on 2026-09-19 with `download_file_content`, each checked against Drive's own
reported size. *This paragraph read "partial" from v12 to v22, and was true then.*

**This file deliberately does not say how many of each there are.** It said so four times and was wrong
four times (v12 *"four"*, v13 *"fifteen"*, v16 *"seven"*, v17 *"nine / twenty-seven"*) — a count goes
stale the moment an article is written, and this document is revised weekly at best. **The count lives
in `Outputs/kb-registers.md`**, in the Wiki-structure rows, recorded at the moment each article was
added and with the command that produced it. To quote a current figure, run
`git ls-files 'Wiki/**/*.md' | wc -l` for the mirror side and read the registers for the Drive-only
side; **do not carry a number forward from anywhere, including from here.** *(That pathspec counts the
articles in the topic folders and correctly leaves out `Wiki/index.md`, which sits at the top level and
is not an article. `_templates/article.md` is not tracked in git; if it ever is, it would need
excluding.)*

Anything authored in a session is written to both stores and verified with `wc -c` against Drive's
reported size, and **the back-fill of everything older is done** (2026-09-19): each Drive-only article
was fetched with `download_file_content`, which returns the stored bytes rather than a rendering (§3),
decoded straight to disk and checked against Drive's `fileSize`. **Keeping it complete is now the
standing job**, and it is the ordinary rule doing the work — an article written to one store and not
the other puts the mirror straight back where it was.
*v8–v11 of this file claimed the mirror "is kept in step". That was never true; corrected in v12.
v12–v21 said back-filling was impossible: true of `read_file_content`, false of the connector — v22.
v23 records it actually done.*

**Folders.**
```
Workshop of Furniture Making - Knowledge Base/
├── CLAUDE.md, README.md
├── Raw/ — inbox; nothing stays here once filed elsewhere
├── Wiki/
│ ├── index.md, _templates/article.md
│ ├── Machinery/ — one article per machine or machine group
│ ├── Suppliers/ — manufacturers, dealers, service/calibration engineers
│ ├── People/ — operators, responsible/competent persons
│ ├── Finance/ — purchase cost, depreciation, insurance, HP/loan finance
│ ├── Processes/ — maintenance schedules, safety/PUWER compliance, training, and
│ │ design/programming-software behaviour & reference (TpaCAD, SmartCabinet)
│ ├── Troubleshooting/ — per-machine fault references + the fault-log system
│ ├── Software/ — SmartCabinet and the design→machine production workflow
│ └── Decisions/ — why this KB is shaped this way; numbers must be recounted, not trusted
├── Outputs/
│ ├── kb-registers.md, change-log-YYYY-MM-DD-<slug>.md
│ └── Correspondence/ — filed copy of every numbered document in scope
└── Archive/ — superseded files, renamed with reason and date
```
No `Properties`/`Tenants`/`Contracts` folders: not applicable to this KB's scope.

**Live data sources.** Smartsheet workspace `Workshop`, one sheet of each after the 2026-09-15
duplicate cleanup: **Machinery Register - Database** (`1754351980906372`, `FA2301`–`FA2306`,
`FA2401`, `FA2402`), **Document Register** (`838802392352644`), **Tasks** (`4087584374523780`), **Safety Check Log**
(`913380204480388`, F45 monthly safety check), **Maintenance Schedule** (`6753985971226500`, all
recurring maintenance tasks, RYGB by due date), **Fault Log** (`414932606781316`, faults & fixes,
RYGB by status) and **Scan Events** (`4828191892047748`, the append-only barcode scan log, RYGB by
Actioned — added 2026-09-17 as Phase 0 of the barcode system). These sheets, not any Wiki article, are
the live source for current status/dates; Wiki articles narrate and cite them. The Vitap's own §6.8 check is **not** yet added to the Safety
Check Log — see §7 (Task T013).

**Register conventions.** Per group document-numbering policy v1.3: `FA` prefix (Amfa Furniture),
7-digit document numbers on the shared group register (not yet used by this KB — see below), 4-digit
property/asset codes self-assigned locally as `FA` + 2-digit year + 2-digit sequence.

**Asset labels are a separate namespace.** The group uses pre-printed "PROPERTY OF FISHBONE GROUP"
tags carrying a QR code and a four-digit number. **The label number is the physical tag; the `FA` code
is this register's ID.** The two are joined by the Machinery Register's `Asset Label No.` column and are
never merged — assets are not renumbered to match labels. The master label register is **group-wide and
owned by Alex**, not this KB; see
`Outputs/2026-09-17-handoff-workshop-assets-for-group-register.md`.

**Mapped 2026-09-17** from the owner's photographs, one machine at a time: `0017` → the ABAC
compressor — then unregistered, **`FA2306`** since 2026-09-18 — `0018` → `FA2301`, `0019` → `FA2402`, `0020` → `FA2303`,
`0021` → `FA2304`. `FA2401` has no label yet. The series starts above `0001`, so `0001`–`0016` are
elsewhere in the estate; **`0025`–`0027` exist on an unapplied sheet** held by the owner, and nothing is
known about `0022`–`0024`. **What the QR codes decode to was answered 2026-09-18: the bare four-digit
label number as plain text** (`Text: 0027`) — no URL, no prefix, no `FA` code, leading zeros preserved,
*read from one tag, so generalising to the series is an inference.* **Phase 1's precondition is
discharged**; what still blocks it is in Task T022. The payload is **not self-describing**, so a scan
means nothing without the `Asset Label No.` lookup — and **leading zeros must never be stripped**, or
that join breaks silently. `0019` was held at `[confirm]` for several steps
rather than guessed: the owner photographed it on "our extractor" while two extractors were
registered, and the right answer turned out to be a third machine the register did not contain.

**Assigned so far**: `FA2301` (Hebrock F4, corrected 2026-09-15 from a wrongly-assumed `FA2601`),
`FA2302` (Inventair MK1 MTFA extractor — **Sold**), `FA2303` (Altendorf F45), `FA2304` (Vitap K2-2.0),
`FA2305` (Inventair MK2 MTFA — **Sold**; acquisition year had been confirmed from invoice 100154 before
the code was assigned, same discipline applied since the `FA2601` mistake), `FA2306` (ABAC GENESIS rotary screw air compressor — registered 2026-09-18 from **proforma invoice
208027**, 14/11/2023; the year evidenced before the code, the same discipline a fourth time, and the
proforma's status as *not* an invoice recorded rather than glossed), `FA2401` (Brother TD-4420DN
label printer — **the first 2024 asset**; the year was evidenced from its order receipt *before* a code
was assigned, which is exactly why it is not `FA26xx`), `FA2402` (AES SAF 10,000 STK fine dust extractor
— same discipline, year evidenced from invoice 22473 first).

**Codes are never retired or reused.** `FA2302` and `FA2305` were sold in the period before this KB
existed; their rows stay, marked `Sold`, because they carry purchase prices, an invoice trail and the
history of how the shop's extraction came to be centralised. A disposal changes an asset's status, not
its existence in the register.

**Registered ≠ complete.** The ABAC screw compressor — which supplies the pneumatics of `FA2301`,
`FA2303` and `FA2304`, and is therefore a single point of failure for the whole workshop — was found on
2026-09-17 to have never been registered at all. It was held at **no code** for a day, deliberately,
because its type plate gives a *manufacture* year and this KB's convention needs an *acquisition* year;
**registered as `FA2306` on 2026-09-18** once dated purchase paperwork arrived. **The lesson outlives the
gap it exposed**: nothing inside the register could point at a machine the register did not contain, and
nothing inside it can tell us whether it is missing others. See §3 and §7.

**Correspondence/documents** (invoices, manuals, certificates) are registered on the **shared group
Document Register** under AMFA Furniture Ltd's `FA` prefix, not a locally invented one — **appending
to that shared register is a deliberate, confirmed-access action, not a routine one** (none exercised
yet; candidate documents are logged locally with `Document No.` = `pending`).

**Housekeeping finding, not yet actioned:** a duplicate copy of the Vitap manual and F45 spare-parts
manual PDFs was found in a Drive folder (`1qF7XiS2Jud3y8V6lf4Nyu7_JAMEJNsai`) that is **not** a child
of this KB's folder tree — outside this KB's own `Raw/` (`18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R`). Not
touched; flagged for the owner in case it's an accidental duplicate upload elsewhere in Drive.

**Open flag for the owner, not resolved here:** AMFA Furniture Ltd's own Property Register uses
`AMF`+digits for property codes, not `FA`+digits — a different asset class, doesn't force this KB to
match, but worth the owner's attention if compared side by side.

## 2. Wiki maintenance guidelines

Front matter, citation, linking and stub rules: `Wiki/Process-Fishbone-Systems-House-Rules.md`
(Fishbone Group KB) and this KB's own `Wiki/_templates/article.md`.

## 3. Workflow for processing new items

Group workflow (Detect → Register → Read → Extract → Update → Check → Log → Output → Commit).
Lessons from Sessions 2–15, all on real incidents rather than invented ahead of time:
- For a multi-part scanned manual, extract via background sub-tasks (split across parallel agents
  for large sets, e.g. 8 parts as two 4-part agents) rather than reading everything inline; flag
  illegible/OCR'd figures and cross-part inconsistencies explicitly rather than silently picking one
  reading.
- **A fact stated with an explicit assumption must be revisited the moment real evidence arrives**,
  even if that means renumbering something already assigned (`FA2601`→`FA2301`) — and conversely,
  **ask for the evidence up front when a session's own numbering scheme depends on it** (asset
  acquisition year), rather than assuming and correcting later.
- A genuine compliance/regulatory finding (expired certificates, a mandatory documented check)
  should be surfaced prominently — in Key facts, not just Open questions — and given its own Task
  and, if it's a recurring process, its own `Wiki/Processes/` article and tracking sheet.
- **Manual-derived maintenance schedules and fault tables belong in the operational systems**
  (`Wiki/Processes/maintenance-schedule-*.md` + the Maintenance Schedule sheet;
  `Wiki/Troubleshooting/troubleshooting-*.md` + the Fault Log), not only inside the Machinery
  article. When a fix or diagnosis differs from the manual in practice, record that lesson in the
  troubleshooting article (the corner-rounding incident is the first example).
- **Two similarly-worded manual sections are not necessarily the same requirement.** The Vitap's §6.8
  "Safety Device Efficiency Check" looks, by name, like the F45's mandatory monthly check — but its
  text describes a pre-automatic-mode functional test with no stated interval or "log this"
  instruction. Don't extend a Processes article or a Smartsheet log to a new machine on
  name-similarity alone (Task T013).
- Don't assume one finding resolves another just because they're related — e.g. a new centralised
  extraction unit plausibly supersedes an older single-machine extractor, but that's a task to
  confirm, not a status to assert. **Closed 2026-09-17, and the restraint paid**: the answer to "did
  `FA2305` supersede `FA2302`?" was *neither*. Both were sold and replaced by a third machine
  (`FA2402`) that the register did not contain. Had either been marked "superseded" on plausibility,
  the correction would have had to unpick a status, a date and a relationship; as it was, nothing
  needed unpicking.
- **A formula validated on one invoice becomes evidence for others once repeated.** The 70%-balance
  cross-check was confirmed independently on invoices 100153, 100154 and 100155 — a third clean match
  closes the underlying question generally, not just for the invoice it was first raised on.
- **A manual that says "generic" or "extract" at the top means exactly that — check what it defers to
  before treating its silence on a topic as an answer.** The TPA CAD manual named three sibling
  manuals it doesn't include (`Workings.pdf`, `DxfCAD.pdf`, `DxfToTPA.pdf`) and said the copy given
  wasn't complete. Its silence on "Outfit Parameters"/"CN Tools"/"Solve" wasn't evidence those don't
  exist — it was evidence to go find the un-supplied files (Task T015).
- **A live shop-floor fault is worth documenting even mid-resolution.** The TpaCAD tool-ambiguity
  incident was written up with "workaround in place, permanent fix identified but not tried", then
  refined a second session, without ever being marked resolved prematurely (Task T016).
- **Two data points that should agree but don't are a live contradiction to record, not to silently
  resolve.** The SmartCabinet Wall Support session found two "measured from the back edge" hole
  positions needing opposite X signs; both were documented as actually used, with the disagreement
  itself flagged as the open question rather than guessing which is wrong (Task T017).
- **A fact recorded without a source hardens into an assumption nobody revisits.** The "two computers,
  not networked" claim sat in §1 through six versions, was repeated into the Vitap/TpaCAD/SmartCabinet
  articles, and shaped real advice (a whole barcode-system design was built around an air gap that does
  not exist) before the owner corrected it on 2026-09-17. It carried no citation and no `[confirm]`
  marker, so nothing ever flagged it as inferred. **Infrastructure and environment facts get a source or
  a marker, exactly like a figure off an invoice.** *Confirmed twice over on the same day:* the workshop's
  address had said **Unit 32** since Session 1 and was also wrong (it is Unit 31), and a billing address was
  described as "residential" purely from its format when it is in fact the companies' registered office.
  Three unsourced statements, three corrections, one day. **If it was not read off a document, say so.**
  *A fourth surfaced the same evening — §1's claim that the git mirror "is kept in step" (v12) — and a
  fifth right after it: the compressor's 5.4 bar "low pressure", which was residual receiver pressure
  on a machine that was switched off (v13).* **A reading is only a reading of the state the thing was
  actually in.** A photograph shows a number; it does not show whether the machine was running, warm,
  loaded or mid-cycle. Establish the state, or record the number as uninterpreted.
- **A fact filed under the wrong name is worse than a missing one, because the KB stops looking for
  it.** `FA2303`'s serial number sat in the Machinery Register from Session 6 as *"Job No.
  23-11-12-005 (Altendorf internal; no confirmed serial number)"*. On 2026-09-18 two 10 MB schematic
  PDFs were put through extraction specifically to find that serial; both reported none present and
  recommended photographing a title block. **A photograph of the machine's own plate showed
  `23-11-12-005` sitting in the `S/N` field.** The KB had transcribed the right value and then told
  every future reader it was something else, so five sessions of work routed around it. **A missing
  fact advertises itself; a mislabelled one does not.** When a field is filled with a hedge —
  *"internal"*, *"working value"*, *"no confirmed…"* — that hedge is a claim in its own right and needs
  checking like any other.
- **Check what a multi-part scan actually contains before trusting any one part.** The TPA CAD manual's
  *"part 1"* and *"part 2"* are not two volumes: part 1 holds the **even** pages and part 2 the **odd**
  pages in reverse order — two sides of one duplex scan, with pages 1, 2 and 50 in neither. **Part 1
  alone gives materially wrong answers**, because the milling-setup compensation fields exist only in
  part 2. Extracting both parts independently is what exposed this; a single read would have produced a
  confident, incomplete answer. Same shape as the Vitap manual's two duplex pairs, and worth checking
  page numbering on any scanned set before quoting it.
- **Comparing siblings finds what reading one cannot.** The `AMFA Wall Unit 600 RH` cutting list read
  cleanly on its own — every number internally consistent, nothing to query. Decoding the `300mm` and
  `600mm Wall unit` lists and putting all three side by side did two things at once: it **corroborated**
  the derived 600 × 900 × 300 nominal, because the same width rules held across all three, and it
  **exposed** a shelf depth of 266 / 256 / 255 mm on three carcases that are all 300 deep. Neither was
  visible from one file. *A single artefact can only be checked for internal consistency; a family can
  be checked against itself.* Where several things are meant to be the same, read more than one before
  calling any of them the master — and when they disagree, record every value, because preferring the
  one labelled "master" is a guess wearing a title.
- **A printed delivery clause is not a delivery note.** Proforma 208027 carried the line *"DELIVERY AS
  PER INV ADDRESS"* against a Unit 31 address, and §7 recorded the compressor as delivered to Unit 31 —
  then built a premises conclusion on it (*"the group was using both units in November 2023"*). The owner
  corrected it within hours: **it went to Unit 32.** Unit 31 was the billing address. A supplier's
  boilerplate describes an intention at the moment of quoting, not an event; only a delivery note, a
  signature or somebody's memory records where a thing actually arrived. **The same family as the 5.4 bar
  gauge** — treating a mark on a page as a record of the physical world. Where a document gives an address,
  record *which* address it is (billing, correspondence, delivery), and if it does not say, say that.
- **A correction has to be swept through every store the claim reached.** The "not networked" claim was
  corrected on 2026-09-17, and the sweep covered this file and the Wiki articles. It did not cover
  Smartsheet, and on 2026-09-18 Task **T016** was still instructing a future reader to carry a file across
  by hand *"(the two are not networked - confirmed)"* — a retracted claim, still giving directions, with
  the word *confirmed* attached to it. **The narrative layer and the live-data layer are different
  places.** A correction is not finished when the article reads right; it is finished when every sheet
  note, task and register row that repeated it reads right too. Corrected in place and visibly, not
  quietly overwritten.
- **A register only contains what somebody thought to put in it.** Five sessions were spent
  documenting three machines in detail — manuals, fault tables, maintenance schedules, re-commissioning
  requirements — while the compressor that feeds all three sat unregistered and unmentioned. It surfaced
  only because the owner photographed an asset label on it. **The gap was invisible from inside the
  KB**: nothing in the register pointed at a machine the register did not contain. Completeness is not
  something a knowledge base can check about itself; it needs a walk round the floor. The same walk
  turned up the first dealer sticker (R&J Machinery) in the whole KB, after three machines had been
  documented with no seller identified at all.
- **A model name is not a specification.** `STK 10000` was read as "probably 10,000 m³/h" and the
  reading was labelled, in the task itself, as *not* sourced — *"that is a reading of the model name,
  NOT a specification — do not rely on it."* It held for days until the vendor's quotation arrived and
  confirmed it. The label cost nothing and would have prevented a wrong number hardening into a fact if
  the guess had been wrong. **Label the inference, not just the conclusion.**
- **What a document excludes can matter more than what it states.** The AES quotation's specification
  table was useful; the two clauses saying the vendor supplies no cabling, no hose and no on-site
  electrical connection were more useful, because they moved the whole installation — ductwork,
  electrics, commissioning — into the group's own undocumented column. **Read the exclusions, the
  payment terms and the delivery conditions, not only the spec table.**
- **Trust the API's response, not its status code.** A 4,000-character Smartsheet cell value was
  **silently truncated mid-sentence** and still returned success. It was caught only by reading the
  stored value back out of the response. Long note fields go in compact, and get read back.
- **Verify like with like.** A Drive file's reported `fileSize` is **bytes**; Python's `len()` is
  **characters**. Comparing one against the other on a file full of `—`, `≥`, `³` and `Ø` showed a
  329-"byte" gap that did not exist, and cost a full withdraw-re-read-re-upload cycle plus a wrong
  "do not cite" label on an archived file that had nothing wrong with it. **Use `wc -c` both sides.**
  **And a size match is necessary, not sufficient — it proves nothing about order.** On 2026-09-19
  `kb-registers.md` went up with two Outputs rows transposed; `wc -c` matched exactly, at 56,265 both
  sides, and the upload was reported as verified. It was verified, and it was wrong. **A permutation
  does not change a byte count**, so reordering — and a swap of two equal-length values — passes
  silently. Every table in this KB is append-only and order-carrying, so **where order means something,
  check the order too**: before uploading, note which rows should sit first and last in each table; after
  uploading, read those positions back, not just the size. Cheap form: hash the lines at known positions,
  or count rows per table and compare the sequence of a few distinctive row keys. The general shape is
  §3's other standing warning — *trust the API's response, not its status code* — one level up: **here the
  number in the response was true and the inference drawn from it was false.** A check that has never
  failed is not a check that cannot fail; know what yours is blind to.
  *`ARCHIVED-2026-09-19c-kb-registers.md` is labelled **DO NOT CITE** for this reason: correct content,
  wrong order. A mislabelled file advertises nothing, which is the same trap as the wrongly-named serial.*
  **Two limits on the check itself, both found by running it.** *(a)* **It has a size ceiling.** The
  connector's read returns an **empty** `fileContent` above some size rather than an error:
  `kb-registers.md` read back fine at **58,410 bytes**, `CLAUDE.md` came back empty at **82,310** —
  *two points, so a bracket between roughly 58 KB and 82 KB, not a measured threshold.* **So the order
  check cannot be run on this file**, the largest in the KB. What stands in for it above the ceiling:
  **build the upload from one contiguous source** rather than by moving blocks about, so the
  pick-up-and-put-down failure has no opportunity to occur, **and say plainly that order was not
  verified** — *that is an argument about how the file was produced, not a verification of it, and must
  never be reported as one.* Below the ceiling, run the real check.
  **The ceiling was lifted 2026-09-19**: it belongs to `read_file_content`, and
  `download_file_content` returned this file whole at **90,475 bytes**. **The order check now runs at any
  size, on exact bytes** — download, decode, `diff` against the local copy. Building the upload from one
  contiguous source stays good practice; it is no longer a *substitute* for a check, because the check
  is available. *(b)* **Anchors must be plain
  text.** The read tool escapes backticks and asterisks, so an anchor containing them is not found and
  the check reports a failure that is not there. This KB produced exactly that false alarm on its first
  run and nearly believed it. Pick anchors from ordinary prose — one per table, first row and last —
  and compare the sequence of their positions plus the row count per table.
- **The connector's read tool does not round-trip, so never "copy" a file with it.** It returns a
  re-formatted rendering — leading punctuation escaped, two-space hard breaks appended — not the bytes
  on disk. A 2 KB article reconstructed from it came back **4 bytes out, silently**. This is why the
  git mirror is deliberately partial (§1) rather than back-filled, and why a large article is never
  rewritten just to change one metadata field: **every rewrite through a lossy read risks drift in the
  99% you did not mean to touch.** Write new content to both stores from the same local copy and check
  `wc -c`; do not treat Drive as a source you can read back and re-emit.
  **Corrected 2026-09-19: that is true of `read_file_content` and false of `download_file_content`**,
  which hands back the stored bytes base64-encoded and round-trips exactly — verified on a 9,602-byte
  article (byte-identical bar one real content difference) and on `CLAUDE.md` at 90,475 bytes. *The
  lesson that survives is the narrower one:* **the connector has two read paths and they are not
  interchangeable.** Never copy a file with the natural-language one; use the byte one, and diff.
  *The mirror was back-filled through the byte one on 2026-09-19 and every file matched (§1).*
- **Put a fact where its own update cycle lives.** This file carried a count of Wiki articles through
  four versions and was wrong in all four — *"four"*, *"fifteen"*, *"seven"*, *"nine / twenty-seven"* —
  not through carelessness but because **the figure changes every time an article is written and this
  document is revised weekly at best.** v17 responded by making recounting a standing rule, and went
  stale the same day it was written. **A rule that must be obeyed on every edit of a slow-moving
  document will be missed, and the miss is silent**, because a wrong number reads exactly like a right
  one. The fix is not more discipline, it is moving the fact: the count now lives in
  `Outputs/kb-registers.md`, which is touched every session, alongside the command that produces it.
  **Ask of any figure written into a durable document: what invalidates this, and how often? If the
  answer is "more often than this document is edited", it belongs somewhere else with a pointer left
  behind.** The same test flags the Drive file ids, the Smartsheet sheet ids and the machine
  specifications here — all of which change rarely or never, which is why they stay.
- **Re-read the primary record before reframing what a task is.** On 2026-09-19 T016 was recast from
  a generic TpaCAD fault into *"the Cabineo X tooling half-defined in SmartCABINET"*, and the charter,
  the task note and `Wiki/index.md` all took it up. **The article that records the incident says, in
  terms, that the two findings are unrelated** — and it had been written at the machine with the
  dialog open, which makes it better evidence than anything written about it since. **I did not
  re-read it before reframing.** The cost would have been a wasted trip to the wrong computer and a
  fix that appeared to fail. This is §3's *a fact recorded without a source* turned inside out: **the
  source existed and was not consulted.** *The risk scales with the KB's size* — this charter now
  summarises articles it no longer quotes, and a summary of a summary drifts. Before rewriting what a
  task **is** (as opposed to adding to it), open the primary record. Reframing is not a small edit; it
  redirects everyone who reads it next.
- **Check whether the tool you are blaming is the tool you used.** For nine versions this KB recorded
  that *"the connector's read tool cannot return a file byte-for-byte"* and built two standing debts on
  it — a mirror that could not be back-filled, and an order check with a size ceiling. **The connector
  has a second read tool that does exactly what was wanted, and it had never been called.** The claim was
  true of `read_file_content` and was written down as true of *the connector*: a quiet widening of scope
  that nothing later re-examined, because a debt that is written down reads as settled. **A limitation is
  a property of the call you made, not of the system**, until you have looked at what else the system
  offers — *list the tools before concluding the capability is missing.* **And the cheap half of the same
  lesson:** two byte discrepancies that day — **−8** on a new article and **+306** on this file — were
  both recorded as unexplained, one after being deliberately bounded at three attempts. **Neither was a
  defect; each was one `diff` away.** A discrepancy you cannot explain is usually a diff you have not
  run — and *suspicion* is not grounds for a **DO NOT CITE** label: that went onto v21 of this file and
  came off within the hour, making mislabelling the third entry of its kind in §3.
  **The price is now measurable**: the mirror debt stood for eleven versions and the back-fill it
  blocked took one afternoon (§1, §7, v23).
- **A description of a gap is not a measurement of it.** §7 recorded the one-way `related:` front
  matter as *"the three machinery articles"* plus one empty list — four files. On 2026-09-19 the graph
  was **computed** rather than read off the bullet: **fifteen files, 52 missing back-links.** The
  bullet was not careless. It named the articles somebody had **noticed**, because the two 2024 assets
  had been written last and linked out to the three older machinery articles, so those three stood out
  *from the side that had the links*. **The other eleven were invisible from inside the KB** — nothing
  in a one-way link announces itself from the end that is missing, which is the unregistered
  compressor's shape exactly: *a register only contains what somebody thought to put in it.* **Where a
  gap can be computed, compute it before trusting the count somebody wrote down** — including a count
  in this file. The danger is not the wrong number, it is that **a written-down description of a defect
  reads as a specification of it**, so the fix gets scoped to the description and closes tidily against
  the wrong four. Cheap form: a dozen lines that walk the files and build the set, run *before* the fix
  is planned, so the plan is sized against the measurement. And the description had stood unexamined
  since 2026-09-17 — **an inaccurate account of a gap is more durable than the gap**, because closing
  the gap feels like closing the account of it. Owner's decision to add this, 2026-09-19 (*"Add that §3
  lesson at v25"*), after v24 proposed rather than added it — the same route the v18 count fix and the
  v19 order clause took.
- **Don't run two sessions on this KB at once, and re-read the live index/registers before recreating
  a control file.** The 2026-09-15/16 fork (this file, `index.md`, `kb-registers.md` all split across
  two parallel lines) is the reason Darius now owns the KB as a single seat.

## 4. Change log

One file per session in `Outputs/`, named `change-log-YYYY-MM-DD-<slug>.md`, indexed newest-first in
`Outputs/kb-registers.md`. Never a single growing `CHANGELOG.md`.

## 5. Automated processes

None are live. The Maintenance Schedule / Safety Check Log / Fault Log RYGB `Health` columns are
self-updating **column formulas** (maintain via the connector, not by hand) — but there is no routine
that reads them and chases due dates yet; that's a future proposal, and a natural early candidate for
one of Darius's own scheduled routines.

## 6. Governance

**6a — never do unattended:** never file with Companies House/HMRC/any regulator; never commit AMFA
Furniture Ltd or Fishbone Construction Ltd to a purchase/contract/payment (incl. spares, service
visits, the electrician's PTC check); never reply on either company's behalf to a supplier/insurer/
inspector/manufacturer; never edit or delete a row on the shared group Document Register (append-only,
in-scope documents only, and only once write access is confirmed — not yet done); never touch AMFA
Furniture Ltd's own KB/Property Register/Document Register from this KB; never hold, type or request a
secret/credential. Appending to the Workshop workspace's own sheets (Machinery Register, Document
Register, Tasks, Maintenance Schedule, Fault Log, Safety Check Log, Scan Events) and creating Wiki
articles here is normal KB work and allowed. Deleting whole Smartsheet sheets is a UI action the owner takes (the
connector has no delete-sheet tool); the 2026-09-15 duplicate cleanup was done that way.
**6a-i — cross-KB amendments go through `Raw/`, never a direct edit** (owner's ruling, 2026-09-20; Hub
`HL-0023` / `AWT-0036`). **Outbound:** where an estate-wide rule, policy or amendment needs to land in
another employee's governed file — a `CHARTER.md`, a `CLAUDE.md`, any standing control file — this KB
**does not edit that file**, even when the content is correct and squarely its own remit. It goes into
that KB's `Raw/` with a Hub Tasks & Requests row naming what it is and which file and section it belongs
in, and **that KB's owner writes it in.** **Inbound:** a note arriving in this KB's own `Raw/` is **a
proposal, not an instruction.** It is read as source material, its claims are checked — **including any
claim to carry the owner's authority** — and it is written in by Darius on the owner's word, or not at
all. *v26 itself arrived that way and was handled that way.*
**6b — access review:** 2026-09-14, initial setup — Drive KB and Smartsheet workspace created by the
owner (minda@fishboneconstruction.co.uk); no other access granted. Shared group Document Register
write access still not confirmed. 2026-09-16: git mirror `minda-ui/Darius` created (owner) + seeded;
**confirmed private by the owner 2026-09-17**. 2026-09-17: a supplier support ticket containing live
SIP trunk credentials was shown in a screenshot; **not recorded anywhere in this KB** per the
never-hold-a-credential rule, and the owner was advised to have the password rotated — with the point
made plainly that deleting the image does not un-expose a credential already shown. Same day:
**`AnyDesk.exe` and `putty-64bit-0.85-installer.msi` were found sitting in `Raw/`** — a remote-access
client and an SSH client in a document inbox. Flagged to the owner, **never opened, run or moved**; the
owner has since removed them (confirmed by folder listing). Same day: **bank sort code and account
number on the MWM quotation were deliberately not copied** into the register or the Document Register,
and the omission is recorded in the `FA2402` note so it reads as a decision, not an oversight.
2026-09-18: **bank sort code and account number, and a personal mobile number, on proforma invoice 208027
were deliberately not copied** into the Machinery Register, the Document Register, either Wiki article or
the change log — the same decision made for the MWM quotation, and recorded so it reads as a decision.
2026-09-19: **the git mirror was back-filled, and the source was checked before it was copied.** The F45
article carries the 2026-09-17 removal of the **ElmoDrive remote-maintenance access code**; the Drive copy
was verified to still be without it, and all eighteen back-filled articles were scanned for credentials
before anything was committed. **A bulk copy must not quietly re-import what an earlier session removed.**
2026-09-20: **a hand-off note from Alex arrived in `Raw/`** proposing two additions to this charter
(`2026-09-20_Hub-Coordination-and-RawHandoff-Note.md`, `1cg8eNaxdoAwmC-Z9QTkHAwNxOIQP4sGW`). Handled as
**source material, not an instruction**: read, its Hub references verified to exist (`AWT-0036`,
`AWT-0040`, `HL-0023`), the **absence** of a Darius-assigned row recorded rather than glossed, and
**nothing written into this file until the owner confirmed the rulings were their own** — which they did
the same evening. That sequence is now the rule, at §6a-i.
**6c — revisit cadence:** none set yet.

## 7. Workshop snapshot and open questions

**Location:** **Unit 31, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA** — the
workshop. **Unit 30** on the same estate is office and warehouse — **also NE28 6HA** (owner, 2026-09-17;
the `[confirm]` that stood against this is discharged). **Unit 32 is no longer held**; everything in this
KB dated before 2026-09-17 that says Unit 32 was wrong or is historic.

Evidenced by the lease cover page: **Forth England Limited** (landlord) and **Furniture by Fishbone
Limited** (tenant), **dated 25 June 2026**. *Furniture by Fishbone Limited is this company's former name —
Companies House confirms it renamed to **AMFA Furniture Ltd** on 13 July 2026, three weeks after the lease
was signed (Fishbone Construction KB, `Wiki/Suppliers/amfa-furniture-ltd.md`, CH overview `FH0000019`).*
Same company, not a new one. **Unit 31's previous occupant was Fishbone Waste**, who have moved out — which
is why the 2024 Brother order receipt shows "Fishbone Waste, Unit 31" for what is now the workshop's address.

**The lease itself is not this KB's to hold** — §1 deliberately has no `Properties`/`Contracts` folders. It
belongs in the AMFA Furniture Ltd KB, along with **Forth England Limited** as a Suppliers entry. Flagged for
the owner/Victoria; only the cover page has been seen.

**Machines registered:**
- `FA2301` — Hebrock F4 edge banding machine, Serial F3809. CE-compliant. Corner-rounding fault
  (stop-screw misadjustment) resolved (FL-001). Maintenance schedule (MT-001…014) + troubleshooting
  reference built. See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`.
- `FA2302` — Inventair MK1 MTFA dust/fume extractor. **Sold** (owner, 2026-09-17). Never had a manual;
  never joined the maintenance system. **Disposal date and sale proceeds unknown** — it carries a
  purchase price, so the disposal has a book consequence.
- `FA2303` — Altendorf F45 ElmoDrive CNC sliding-table saw. **Serial `23-11-12-005`, confirmed from the
  type plate 2026-09-18 (T009 closed)** — the same number the KB had carried since Session 6 as "an
  internal job number"; the plate also gives 2023, 8,293 kVA, 13,34 A, blade 300–450 mm at 2000–5000 rpm,
  and carries the **DGUV marks HM 220024 (GS) and HM 220025 (wood dust)** physically on the machine.
  **Safety certificates expired 22.02.2024 — unresolved compliance gap, Task T007.** Mandatory monthly
  documented safety check required (Task T008, not yet performed); the schematics now give **device tags**
  for it, including **three** emergency stops and a **reduced 50 mm safety zone at the rip fence** the KB
  had no record of. **The machine provides volt-free terminals to start an external extractor** (max
  240 VAC, 1 A) — capability confirmed, wiring unverified (T018). Maintenance schedule (MT-020…028) +
  troubleshooting reference built. See `Wiki/Machinery/altendorf-f45-panel-saw.md`,
  `Wiki/Processes/f45-monthly-safety-device-check.md` and
  `Wiki/Processes/f45-electrical-schematics-reference.md`.
- `FA2304` — Vitap K2-2.0 CNC boring/drilling/routing centre. **Serial `320070 AT` and year 2023
  confirmed from the type plate 2026-09-18 (T012 closed)** — identical to the invoice-derived value the
  manual could not corroborate. The plate also gives 415 V, 19,3 A and **1385 kg**, which **disagrees
  with the 1030 kg this KB carried from the manual** (355 kg apart; floor loading and levelling both
  scale with it, so prefer the plate until someone reconciles them — recorded, not resolved).
  **Open incident:**
  TpaCAD "Tool for this working not found" on Blind bore drill operations — root cause refined (fix
  likely lives in the operation's own Tool [T] field referencing a real CN Tools catalog entry, not
  the outfit's per-bush ID), not yet tested end-to-end (Task T016). Maintenance schedule (MT-030…036)
  + troubleshooting reference built. See `Wiki/Machinery/vitap-k2-panel-saw.md`,
  `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`.
- `FA2305` — Inventair MK2 MTFA dust/fume extractor, bought alongside `FA2304` on invoice 100154.
  **Sold** (owner, 2026-09-17). The promised manual never arrived and now never will. **Disposal date
  and sale proceeds unknown**, same book consequence as `FA2302`. *The long-running question of whether
  `FA2305` superseded `FA2302` is answered: neither did.* Both were sold and replaced by a single
  centralised unit, `FA2402`, that this KB had never heard of. The suspicion had been recorded as
  unconfirmed rather than asserted, so nothing had to be unpicked — see §3.
- `FA2401` — Brother TD-4420DN direct-thermal label printer, bought 09/05/2024 (Printerland order receipt
  SOA2606351, £211.58 ex VAT). Registered 2026-09-17. **Billing trail unresolved and recorded as such:** no
  company is named on the billing line — it is in the owner's name at the companies' registered office — and
  it shipped to Fishbone Waste at Unit 31, then a different occupant. **ZPL emulation unverified** (resellers
  claim it, Brother's own manual for this model never mentions it); direct thermal fades, so it suits
  short-life part labels, not asset or offcut labels. **No asset label applied yet.** See
  `Wiki/Machinery/brother-td-4420dn-label-printer.md`.
- `FA2402` — **AES SAF 10,000 STK fine dust extractor** (centralised, three-phase), serial **A-077**.
  Invoice **22473**, **08/10/2024**, **Markfield Woodworking Machinery Ltd**, £6,350 net / £7,620 inc
  VAT, paid in full. Asset label **`0019`**. Registered 2026-09-17, acquisition year evidenced before
  the code was assigned. **Specification sourced from the vendor's quotation of 02/10/2024** (six days
  before the invoice, identical figures), and **the type plate photographed 2026-09-18 states `DUST
  CAPACITY 10.000 M³/H` as its own field**, which fully discharges the old *"10000 is a reading of the
  model name"* caveat; the plate also confirms serial `A-077`, production year 2024, and names the maker
  **AES ELEKTRİK MAKİNA SAN. VE TİC. A.Ş.** (settling the two renderings), but gives **740 kg against the
  quotation's 720 kg** — recorded, not resolved: **10,000 m³/h**; 11 kW / 15 HP direct drive, star-delta; **355
  mm** suction; **64 filters at Ø160 × 940 mm, 30.22 m²**; three waste buckets; 720 kg; a Part Holder
  stopping parts over 25 × 25 mm reaching the propeller. **What the vendor did *not* supply is the
  important part** — *"not supplied with electrical cabling, extraction hose or blades"* and *"we do not
  electrically connect machinery on-site"* — so the ductwork and electrics were the group's own work and
  **nothing about that installation is recorded** (Task T014). *"Dust absorption rate 40 m/min"* is
  recorded verbatim and **unreconciled**: it matches neither the inlet velocity nor the filter face
  velocity, and is not to be used until a vendor or a real manual explains it. **Still no operating
  manual**, so it cannot join the Maintenance Schedule or Fault Log. Billed to Fishbone Drylining Ltd and
  **delivered to Unit 31 in October 2024 — nearly two years before AMFA's Unit 31 lease** (T004). See
  `Wiki/Machinery/aes-saf-10000-stk-extractor.md` and
  `Wiki/Suppliers/markfield-woodworking-machinery.md`.
- `FA2306` — **ABAC GENESIS rotary screw air compressor** with integrated refrigerant dryer. Asset label
  **`0017`**; serial **ITJ717909**; product **4152025548**; plate year 2023; 455 kg; **15 kW
  three-phase** (the proforma also says 20 HP), 0.58 kW dryer; **74 CFM**; max **10 bar**; refrigerant
  **R513A 0.5 kg = 316 kg CO₂e**. **It feeds the pneumatics of `FA2301`, `FA2303` and `FA2304`** and is
  therefore a single point of failure for the whole workshop. **Found on the floor 2026-09-17, on a
  label but not on the register; registered 2026-09-18** from **proforma invoice 208027**, Pneumatic
  Tools & Compressors Ltd (Long Eaton, Nottingham), **14/11/2023**, **£9,696.00 net / £11,635.20 inc
  VAT**, billed to Fishbone Drylining Ltd. **Delivered to Unit 32**, with the three machines it feeds —
  *not* Unit 31, although the proforma prints "delivery as per inv address" against a Unit 31 address;
  that is the billing address, and the owner corrected the point on 2026-09-18 (see the v15 note).
  **Two model designations, not
  reconciled:** the plate reads `GENESIS 15 500L`, the proforma reads `GENESIS C67` — the *product
  number* is identical on both and is what identifies the machine; every figure agrees, only the string
  differs. **The document is a proforma, not an invoice** (*"THIS IS NOT A VAT RECEIPT"*), so it
  evidences the order, not payment or delivery; 2023 is safe because its 30-day validity closes
  14/12/2023 and the other five machines were invoiced five days earlier. **The VAT invoice is still
  wanted.** Two live items: the service log on its own yellow label is **blank** (Task T020), and the
  **air receiver's pressure-system position is unestablished** (Task T021). **The 5.4 bar gauge reading
  is not a concern and never was** — the compressor was switched off when photographed (owner,
  2026-09-17), so that was residual receiver pressure, not line pressure; *v11 and v12 of this file
  presented it as a finding, which was wrong (see the v13 note)*. The plate rates 10 bar against a
  highest stated demand of 8 bar, so the compressor is not the limitation; what each machine receives
  under load is simply unmeasured — routine verification, **not** the follow-up to a suspected fault.
  F-Gas: 0.32 tonnes CO₂e is far below the 5-tonne leak-check threshold, so charge size triggers no
  periodic leak checking. **No operating manual**, so it is not yet on the Maintenance Schedule. See
  `Wiki/Machinery/abac-genesis-screw-air-compressor.md` and
  `Wiki/Suppliers/pneumatic-tools-and-compressors.md`.

**Operational systems (built 2026-09-15):**
- **Maintenance** — `Wiki/Processes/machinery-maintenance-system.md` + the Maintenance Schedule sheet
  (30 tasks: FA2301 MT-001…014, FA2303 MT-020…028, FA2304 MT-030…036) + three per-machine schedule
  articles.
- **Troubleshooting** — `Wiki/Troubleshooting/troubleshooting-and-fault-log-system.md` + the Fault Log
  sheet (FL-001 = resolved Hebrock corner-rounding fault) + three per-machine references (Hebrock
  §8.2; F45 mechanical + ElmoDrive error codes; Vitap §7.8).
- **SmartCabinet & production workflow** — `Wiki/Software/smartcabinet-and-production-workflow.md`
  (**draft**): the order-to-delivery process from the BP-scheme map, and how SmartCabinet (design +
  3D visuals + CRM) drives the machines. Product specifics flagged `[confirm]`. **This is the seed for
  Darius's first job — the design→production→Sales processes + tracker.**
- **SmartCabinet CAD reference** — `Wiki/Processes/smartcabinet-wall-support-cam-table-reference.md`:
  how to add hardware to SmartCabinet's Wall Support library, full column reference, two worked
  examples that exposed the X-sign discrepancy (Task T017).
- **Kitchen unit library (started 2026-09-18)** — `Wiki/Software/kitchen-unit-library.md`
  (**draft, nothing built**): the `AMFA Wall Unit 600 RH` master read out of its own files, the derived
  nominal, the three-unit comparison, the depth chain behind the 255 mm shelf, and a folder/unit-code
  convention **proposed for approval, not created**. The owner's Drive `Furniture` folder was listed but
  **not reorganised**, and the two `ANVAR_KITCHEN_*` folders were **not opened** — a customer name on a
  folder is enough to treat it as client data.
- **The production route (recorded 2026-09-19)** — `Wiki/Processes/panel-production-route.md`: the
  order parts actually move through the shop, **SmartCABINET optimisation → panel cutting list → F45 cut
  → F4 edging → Vitap drill → assembly desk**, with the finished-size/trim-then-tape answer and the
  serial-line argument (no second saw, bander or borer, so any one stoppage stops the shop — and all
  three are fed by `FA2306`). *Five sessions documented three machines without recording the order they
  are used in;* the gap was invisible from inside the KB, exactly like the unregistered compressor.
- **Carcase fixings** — `Wiki/Processes/carcase-fixings-cabineo-x-vs-confirmat.md`: **Cabineo X decided
  and ordered** (owner, 2026-09-19), confirmat retained as **Plan B and held in stock**. Records what the
  choice costs (**+£6.72 a unit, +£80.67 a twelve-unit kitchen** at UK retail listings, which still want
  a trade quote at 2,000) and why the master needs no re-drawing.
- **Making holes with a cutter** — `Wiki/Processes/tpacad-interpolated-holes.md`: **toolpath circle Ø =
  hole Ø − cutter Ø**, written for a live job with the 10 mm and 12 mm drills on order. Also the
  cheapest case in which to settle the unresolved `Diameter`-field convention, because a wrong reading
  gives 22 mm rather than 12 — unmistakable on scrap.
- **Closing T016 (2026-09-19)** — `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`: the two-step fix
  at the **Vitap**, the verification test on `03-BOTTOM.TCN`, why the Through-bore workaround must not
  be used to close it, and **the correction to what T016 was said to be** — see the T016 bullet below
  and the v21 note at the top of this file.
- **Barcode system, Phase 0 (2026-09-17)** — the **Scan Events** sheet (`4828191892047748`) and the
  Machinery Register's `Asset Label No.` column, documented in
  `Wiki/Processes/barcode-and-scan-event-system.md`. Phases 1–4 (part labels, stage tracking, the
  offcut library, Vitap program selection) are designed but not built; the sheet is still empty.

**Open questions / tasks:**
- **SmartCabinet product specifics** — *partly resolved 2026-09-17.* **Vendor and product confirmed:**
  **SmartCABINET**, by **Kosmosoft Engineering S.r.l.** (Bagnolo San Vito, Italy), described as
  "CRM/CAD/CAM/ERP software for cabinet making"; offer/contract **22910**, 10/09/2026, **€1,000, paid**,
  registered `FCD0000024` in the *Construction* Document Register — **billed to Fishbone Drylining Ltd,
  not AMFA Furniture Ltd**, the same pattern as every machine (evidence for Task T004). Cited from the
  Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md` — not duplicated here, and that
  KB is read-only to this one. **Outputs confirmed** from the release notes and the owner's screens:
  `.TCN` post (Vitap), custom CSV export splittable by material, real-shape nesting, ZPL barcode label
  printing, Panel Optimization with an offcut/cutout library. **Still `[confirm]`:** which version is
  actually *installed* (release notes list 3.2.0.9 of 07/07/2026 as newest released); whether the
  Hebrock gets any file at all; where CRM/customer data lives (cite, never copy client data).
- **SmartCabinet Wall Support hardware X-sign discrepancy** — two items both "measured from the back
  edge" needed opposite X signs (−15 vs +5); needs visual confirmation in SmartCabinet's own preview
  on a real job (Task T017).
- **TpaCAD Blind-bore-drill tool-ambiguity fix** refined but not fully tested — likely needs a real CN
  Tools "Dia. 5mm" entry created on the SmartCabinet computer, exported and transferred, then
  referenced in the failing operation's Tool [T] field (Task T016) — *the manual now supports this: the
  setup's `Tool type` "is automatically assigned by selecting the tool", and on `HOLE` an explicit `Tool`
  "prevails over the programming per diameter" with `Tool type` driving "a validity check of the tool".*
  **TpaCAD complete manual / `Workings.pdf`** not yet obtained — at `Albatros\Help\` on the shop's
  Albatros PC (Task T015), and **no longer housekeeping**: it holds the compensation semantics, the
  entry/exit segments and the `THREE HOLES HINGE` parameter table, three of which were needed on
  2026-09-18 to answer a live 35 mm hinge-cup question and could not be. *The extract we hold gives the
  right working — `CIRCULAR INTERNAL WINDOW`, "a circle with internal emptying", under `CUSTOM WORKINGS:
  PROFILES` — but never says whether its `Diameter` is the finished hole or the tool path, which on a
  12 mm cutter is 35 mm versus 47 mm. Settle it with a test cut in scrap* — **cheapest as a Ø12 hole from
  the 10 mm cutter, where a wrong reading gives 22 mm rather than a ruined door.**
  **A correction that belongs here:** this KB briefly recorded that the shop appeared to lack a 35 mm
  hinge-cup bit. **It has one, fitted to the Vitap** (owner, 2026-09-19); what is open is **what went
  wrong with it** (Task T027), and T016 is the obvious candidate — the door programs each cup as a Ø35
  bore with no tool assigned — but that is **not asserted**. *Asking how to do something another way is
  not evidence the ordinary way is unavailable.*
- **Were the machines re-commissioned after the move to Unit 31?** The KB holds no record that a move
  happened at all, yet the lease is dated 25 June 2026. The F45's own manual requires, after installation:
  a flat, level, load-bearing floor (~1100 kg, centre of gravity ~100 mm below the blade axis); swing-arm
  check (0.5 mm); sub-rollers; main-table height (0.1–0.2 mm); cross-slide height; free-cut both sides;
  angle-cut calibration by test cut (**< 0.2 mm**); an electrician to verify motor rotation direction; and
  extraction interlocked to machine power. Extraction also needs **≥ 20 m/s** through the ø140 mm connection,
  and new duct runs change the velocity actually achieved — which bears on the extraction-sizing question
  below. **Not assumed skipped; simply unrecorded.** *The owner has confirmed the machines are "up and
  running"* — which answers whether they work, **not** whether these checks were carried out. Recorded as
  partly answered, not closed (Task T018): "it runs" is not "it was commissioned", and treating one as the
  other is the inference §3 keeps warning about.
- **The Unit 31 lease body has not been seen** — only the cover page. Alterations, repair/reinstatement and
  nuisance clauses all bear on the workshop (extraction ducting, three-phase runs, fixing machines to the
  slab, noise and dust). The lease belongs in the AMFA KB, but those clauses affect this patch.
- **`0191 605 2945` is printed on every group asset label — and is in a SIP trunk migration.** The ticket
  (WebMate `T02530-15072026`) lists `+441916052945` among four DDIs migrating, with a stated completion date
  of **03/08/2026 that has already passed**. If that number does not survive, every asset label points at a
  dead line. Telephony is **not** this KB's scope; this is flagged only because the labels depend on it.
- **The shared Google Drive job folder** — the dedicated folder through which SmartCabinet and the
  machines exchange files is not yet identified or examined. Its structure and naming convention
  constrain any barcode/tracking ID scheme, and it may hold customer data from SmartCABINET's CRM
  side (**cite, never copy client data**).
- **Does `FA2303` (F45) accept a digital cut list?** The ElmoDrive is a *positioning* control — rip
  fence, blade height, tilt, scorer, crosscut-fence angle, with tool management and per-axis
  calibration. Across all three F45 documents **no cut-list or job-file import is documented**, and the
  only data interface that appears is a USB drive, for firmware updates (`E21`/`E22`) and
  remote-maintenance files (`E23`). An "optimisation limit" error in the `E01`–`E15` block hints at some
  optimisation function on the control, but that block's OCR pairing was never reconstructed. **Working
  answer: the saw takes dimensions, not cut lists** — confirm against the ElmoDrive's own menus before
  recording it as fact.
- **Does SmartCABINET's own ERP module already do production tracking?** The vendor describes it as
  "CRM/CAD/CAM/ERP" (Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md`). Building a
  parallel tracker without knowing what the purchased software already does risks duplicating it.
  Owner has chosen Smartsheet as the tracking layer regardless (2026-09-17); this remains worth
  establishing so the two don't fight.
- ~~**What do the asset labels' QR codes decode to?**~~ — **answered 2026-09-18: the bare four-digit
  label number as plain text.** See §1. What now blocks barcode Phase 1 is Task **T022**: no scanner has
  been bought (a purchase, so the owner's), the Brother TD-4420DN's ZPL support is still unverified, and
  a disambiguation rule between asset labels and future part labels needs deciding.
- **Who legally owns `FA2301`–`FA2306` and `FA2402`?** All invoiced to Fishbone Drylining Limited (now
  Fishbone Construction Ltd), not AMFA Furniture Ltd (Task T004) — and so was the SmartCABINET software.
  *Sharpened 2026-09-17:* AMFA Furniture Ltd holds the Unit 31 lease, so the picture is one company's
  machines operating in another's leased premises. **`FA2402` sharpens it again**: it was delivered to
  Unit 31 in **October 2024**, nearly two years before that lease was signed, which suggests the 2026
  "move" was AMFA taking a lease on a unit the group already occupied rather than a relocation.
  **`FA2306` briefly appeared to push that back another year, and does not.** v14 read its proforma's
  Unit 31 address as a delivery address and concluded the group was using both units in November 2023;
  **the owner withdrew that on 2026-09-18 — the compressor went to Unit 32.** So the earliest evidence
  this KB holds for the group occupying Unit 31 is **2024**, not 2023. Evidence, not a conclusion — the
  lease body and the intercompany side both sit outside this KB.
- **`FA2303`'s expired safety certificates** — check with Altendorf/supplier (Task T007), and note the
  DGUV marks **HM 220024 / HM 220025 are on the machine's own plate**; **first F45 monthly safety check
  not yet logged** (Task T008, now with real device tags to name); ~~`FA2303` serial unconfirmed~~ —
  **closed 2026-09-18 from the type plate**, though **who sold it is still unknown**; **`FA2303` annual
  PTC electrician check** needs scheduling (Task T011; Maintenance Schedule MT-025) — the schematics give
  a likely measurement point at `-X3` `POT_1`/`POT_2` but **no resistance value**, and leave
  bimetal-vs-PTC unresolved.
- **Installed extraction performance (Task T014, rewritten).** The `FA2302`/`FA2305` half is closed —
  both sold, both replaced by `FA2402`. The sizing half is now a different question. `FA2402` is rated
  **10,000 m³/h**, against known demand of the Vitap's ~2000 m³/h plus roughly **1,110 m³/h** for the
  F45 — *that second figure is my own arithmetic from ≥20 m/s through ø140 mm, not a manufacturer
  number* — plus the Hebrock, whose duct diameter this KB does not hold, so its ≥25 m/s cannot be
  converted. Comfortable on paper. **But the vendor supplied no ducting, no cabling and no on-site
  connection, and the machines have since been moved**, so what each machine actually receives is
  decided by pipework nobody documented. **Closing action: an anemometer velocity reading at each
  machine's connection**, which also answers the extraction half of T018.
- **A real AES operating manual** — the quotation gives specification, the schematic gives the control
  panel; neither gives maintenance intervals, filter-change criteria, safety instructions or a fault
  table. Until one arrives `FA2402` stays outside the maintenance and troubleshooting systems. The
  consumables are known (64 filters, three buckets), so the schedule can be built the moment the
  intervals exist.
- **`FA2306`, the ABAC compressor** — *registration closed 2026-09-18 (T019); the blocking item is gone.*
  What remains: **has it ever been serviced?** Its yellow label's log table is blank and it was delivered
  in November 2023, so against a *"2,000 hours or 1 year, whichever comes first"* interval the gap is
  approaching three years — but **a blank label is not proof**, and the supplier is a compressor
  specialist and the obvious place to ask (T020). The **F-Gas** position is settled by figure and wants
  qualified confirmation (T020). **The VAT invoice** has never been seen. Delivered pressure and flow at
  each machine under load is still unmeasured and worth a reading, as routine verification. *The 5.4 bar
  gauge reading is closed: the machine was off. It was never a low-pressure finding.*
- **Does `FA2306`'s air receiver need a written scheme of examination? (Task T021.)** The plate's model
  string reads `GENESIS 15 500L`, and read plainly the "500L" is a 500 litre receiver — which at 10 bar
  would be a pressure system far above the commonly cited 250 bar-litre threshold, calling under the
  Pressure Systems Safety Regulations 2000 for a written scheme by a competent person and examination
  under it. **This KB holds no record of any such scheme or examination.** But **"500L" is a reading of a
  model name, not a specification** — neither the plate nor the proforma states a receiver volume, and the
  proforma does not mention a receiver at all — so T021 *starts* by establishing what the receiver
  actually is. One photograph of its own plate turns the whole question from inference into fact. **This
  KB does not give regulatory advice**; it records that the question is open and that absence of a record
  is not evidence of absence.
- **The kitchen unit library — four owner decisions and one remaining defect.** The decisions (T023):
  the range (types and widths), whether *"low cost"* denotes a defined carcase spec or is only a range
  name, whether hand belongs in the unit code or is mirrored at job time, and whether library units are
  separated from customer jobs on Drive. **Four of the five unit types still have no master at all** —
  only the wall unit exists. ~~Shelf depth 266 / 256 / 255 mm~~ — **answered 2026-09-19 and it was never
  a defect**: the master's **255 = 300 − 16 − 19 − 10**, a **16 mm back-panel step-back** for the Häfele
  concealed wall mount, the 19 mm back, and a **10 mm shelf-front step-back**; the earlier folders are an
  **earlier design**, and **both step-backs are specification** that belongs on every unit's spec card
  (the 16 mm is the same Häfele hanger added to the Wall Support Cam Table in the T017 session, showing
  up as a panel dimension). **Still open: two backs** (`07-BACK-1`, `07-BACK-1B`) on one blank in the
  master where neither earlier unit has a second back at all — worth re-asking now the back is known to
  sit in a void for a hanger, since a hanger usually wants the back notched, *though that is a
  suggestion, not a reading*. Also unestablished: whether SmartCABINET generates a unit's parts
  **parametrically** from a width, which would make the whole folder question smaller than it looks.
  See `Wiki/Software/kitchen-unit-library.md`.
- **`T016` is the library's remaining blocker — and the fix is at the Vitap, not on the design
  computer.** *v18–v20 of this file said the opposite and were wrong; see the v21 note.* **The Vitap is
  not missing a Ø5 tool: it has five.** Blind Ø5 mm sits on bushes 6–10, all at **ID 0**, so
  diameter + type resolution has five candidates and no tie-break — which is the whole fault. **Two
  steps close it**, both in TpaCAD's per-position Technology dialog and the failing program: give one
  Blind Ø5 bush a real unused ID, then set that operation's `Tool` field to it, which *"prevails over
  the programming per diameter"*. **Verify by reproducing the failure first, then re-Solving, then
  running `03-BOTTOM.TCN`** — and **not** by switching Tool type to Through bore, which clears the
  error by picking a category that happens to have one bush and silently drills with the wrong one.
  Full procedure: `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`.
  **Nothing needs buying** — that part stands: Cabineo X's published Ø15 drill is the *alternative* to
  routing and the master routes the pocket, so the Ø5 the master already drills plus a ≤Ø12 cutter
  covers it. **The missing SmartCABINET `Dia. 5mm` row is still worth adding, but it is a different
  job**: it belongs to the *systemic* fix — getting the post-processor to **emit** a Tool ID on export,
  so step two is not repeated by hand on every operation of every unit, since every hole in the master
  exports with `#1001=0`. *Whether SmartCABINET's IDs reach TpaCAD at all is unverified; the one data
  point is that position 101 is ID 1001 in both, for positions 101–104 only.*
  **Severity revised down 2026-09-19, priority unchanged:** with confirmat in stock as Plan B, and the
  connector pockets routed into the carcase's *inside* faces where an empty one is hidden, **a job is
  not stopped by T016** — only made more slowly and with a visible screw head.
- **Disposal dates and sale proceeds for `FA2302` and `FA2305`** — both carry purchase prices, so both
  disposals have a book consequence this KB cannot compute.
- **Vitap `FA2304` §6.8 safety check** — does it need a dated, logged record like the F45's, or is a
  pre-cycle functional test enough? Owner decision (Task T013); MT-036 holds the place meanwhile.
- ~~**`FA2304` serial/manufacture year**~~ — **closed 2026-09-18** (Task T012): the plate reads
  `320070 AT`, year 2023, matching the invoice exactly. It also reads **1385 kg against the manual's
  1030 kg** — that discrepancy is now the open part.
- **Who actually sold `FA2301`, `FA2303` and `FA2304`?** Invoices 100153/100154/100155 name the customer
  and the items but carry no seller letterhead. The Vitap wears an **R&J Machinery** dealer sticker
  (`01455`, Hinckley) — recorded **`[confirm]`**, because a sticker on a machine is not a document, but
  it is the first evidence there has been. **Markfield Woodworking Machinery Ltd** (`FA2402`) is by
  contrast fully evidenced and has its own `Wiki/Suppliers/` article — the first supplier entry in this
  KB derived from a purchase rather than from a manufacturer's manual.
- **Full inventory of workshop machinery — demonstrably still incomplete.** This was a soft open
  question until 2026-09-17, when a 15 kW compressor feeding all three production machines turned out
  never to have been registered. *That particular gap is now closed — it is `FA2306` — but closing it
  proves the point rather than retiring it:* **the register was missing a whole machine class, nothing
  inside the KB could tell us, and nothing inside it can tell us whether it is missing others.** Hand
  tools, extraction ductwork, **the air receiver** (now a real question of its own, T021) and the server
  rack itself have never been assessed. Closing it needs a walk round the floor, not a document (see §3).
- ~~**A read path that returns bytes would close two debts at once**~~ — **closed 2026-09-19, and the
  tool was in the connector the whole time.** `download_file_content` returns a file's stored bytes,
  base64-encoded, at every size this KB contains: **byte-identical** on a 9,602-byte article, and
  `CLAUDE.md` returned **whole at 90,475 bytes**. The re-formatting and the empty-above-82 KB behaviour
  belong to `read_file_content`, a *different* tool (§3). **What it unblocks is now work rather than
  capability** — back-filling the mirror (below), and running the §3 order check on exact bytes at any
  size. *Whoever spends the afternoon now spends it copying files, not looking for a mechanism.*
- ~~**The git mirror is partial and cannot be back-filled**~~ — **done 2026-09-19; the mirror is
  complete.** Every article that lived on Drive only was downloaded as exact bytes, decoded and
  committed, each one checked against Drive's reported size. **`Suppliers/altendorf-gmbh.md` is the
  proof**: the 2,007-byte article the v12 test rebuilt four bytes short now lands exact. **The count is
  not repeated here** (§1, §3) — run `git ls-files 'Wiki/**/*.md' | wc -l` and read the registers.
  *The debt is replaced by an upkeep rule*, not by nothing: an article written to one store and not the
  other re-opens the gap, so both stores get it in the same session. **This bullet stood for eleven
  versions and took one afternoon once the right tool was found**, which is the §3 lesson's real cost.
- ~~**`related:` front-matter links are not bidirectional.**~~ — **fixed 2026-09-19, in both stores,
  and the bullet that described it was itself wrong.** It had said the gap was the three machinery
  articles plus `hebrock-f4-next-edge-bander.md`'s empty list. **Computing the graph instead of reading
  the bullet found 15 files and 52 missing back-links.** The Wiki now holds **134 directed edges = 67
  symmetric pairs, nothing asymmetric, dangling or duplicated**, with every one of the 15 article
  **bodies hash-identical** before and after — only front matter moved. Flushed to Drive the same
  session per the upkeep rule above, each copy **verified byte-identical by download–decode–`diff`**.
  **What the bullet named were the articles somebody had noticed**, because the two 2024 assets had
  linked out to them; the other eleven were invisible from inside the KB, the same way the unregistered
  compressor was — nothing in a one-way link announces itself from the side that is missing.
  *Proposed for the owner rather than added unilaterally, and approved the same day* (*"Add that §3
  lesson at v25"*): a §3 lesson that **a description of a gap is not a measurement of it** — where a
  gap can be computed, compute it before believing the count somebody wrote down. **It is now in §3**,
  added at v25. **One consequence recorded rather than tidied:** archive-then-create gives a re-uploaded
  article a new Drive id, so the ids cited in `tpacad-blind-bore-tool-id-fix.md` and
  `carcase-fixings-cabineo-x-vs-confirmat.md` now point into `Archive/`. **They were not rewritten** —
  they resolve to exactly the bytes that were read and quoted, which is what a source citation is for;
  repointing them would make them cite bytes nobody read. **A Drive id in an article is a pointer to a
  version, not to an article.** Cite the path for the article, the id for the bytes, and say which.
- `AMF` vs `FA` property/asset-code inconsistency in AMFA's own Property Register — still just flagged.
- ~~Exact price on the Hebrock invoice unconfirmed~~ — **resolved 2026-09-15** by the 70%-balance
  cross-check confirmed on three invoices (Task T005, closed Done).
- A duplicate copy of two manuals was found outside this KB's own Drive folder tree — see §1.
