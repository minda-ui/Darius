# Change log — 2026-09-29 — limit 3 goes to 1 MB, measured twice before it was written

**Session 24. Two owner instructions, one charter version, and two probes — the whole session is one
number.** The owner said *"adopt the 500kb limit"*, then, while the first probe was still running,
*"push it to 1MB"*. **Both figures were measured before either was written down**, and **§4 now says 1 MB**.

## 1. What the instruction was, and what kind of thing it was asking to change

The owner's words, in order:

> *"adopt the 500kb limit"* — then, mid-turn — *"push it to 1MB"*

**§4's limit 3 is a measurement, not a policy**, and that distinction is not a quibble — it is
**`HL-0065`**, filed on the Hub yesterday after v33: *when an owner lifts a "limit", sort it into
**policy / measurement / claim-about-a-tool** before acting, because only the first is theirs to lift.*
A policy the owner can simply drop. **A measurement can only be moved by measuring**, and §4's own words say
so: *"extend this the same way, and never by assuming."*

**So the instruction was carried out, and the number came from a probe rather than from the instruction.**
*This is not a hedge against the owner — it is the opposite. Writing 1 MB on their word alone would have put
an unverified figure in the one clause of §4 that exists to stop unverified figures being trusted.*

## 2. Two probes, six checks each

**The method is the one used four times on 2026-09-28**, unchanged: a placeholder created in `Raw/` with the
native connector to mint an id, then the real bytes uploaded **in place** twice — content **A** then content
**B**, *the same size and different bytes*, so that neither a no-op nor a truncated write can pass.

| | 500 KB probe | 1 MB probe |
|---|---|---|
| Drive id | `1uFAalxu1fV_kxOQ3gxqN8aobVWxBWkLh` | `16Z8J9SOqEF1uESUuLl1T2VNMgihcGe72` |
| bytes per write | **500,000** | **1,000,000** |
| id after both writes | **unchanged** | **unchanged** |
| `createdTime` | **preserved** (08:20:51.915Z) | **preserved** (08:23:18.966Z) |
| revisions | **1 → 2 → 3** | **1 → 2 → 3** |
| Drive's own `fileSize` | **500,000** | **1,000,000** |
| round trip vs. what was written | **byte-identical** (`ea82f589e112dd71`) | **byte-identical** (`735df1f49567045a`) |
| round trip vs. what it replaced | **different** | **different** |
| elapsed | **7 s** per write | **7 s** per write |
| afterwards | **trashed** | **trashed** |

**Both halves of the byte-check matter and they are deliberately different tools**: the write went through
the Composio CLI, the verification through the **native Drive connector**, per §4. *Sizes were read from
Drive's own `fileSize` rather than from the upload's own response, and the revision count from Drive's
revision list — three entries each, the placeholder plus the two writes. A tool's report that it succeeded is
not evidence that it did.*

## 3. The check that was actually worth making

**Not "can Drive take 1 MB" — it obviously can. The question is whether a 1 MB write can still be *proved*.**
A write this KB cannot verify is no use to it at any size.

At 1,000,000 B the verification download returned **1,333,457 characters** of base64 and was **spilled to a
file rather than returned inline** — the same behaviour §4 has recorded from ~46 KB upward since v33.
Decoding it from the spill file gave a byte-for-byte match. **So a bigger ceiling changes where the bytes are
read from, not whether the write can be proved**, and §4 now says that in as many words.

## 4. One neighbouring claim, recorded as a claim

While searching for the revision-listing tool, Composio's own guidance surfaced a **5 MB cap on
`GOOGLEDRIVE_UPLOAD_FILE`**. **That is a different tool from the `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` this KB
uses, and it has not been tested.** It is written into §4 as a **signpost, explicitly untested** — *a
vendor's note about a neighbouring tool is exactly the "claim about a tool" that `HL-0065` says not to
confuse with a measurement, and this KB has been caught by that once already: the ~82 KB
`read_file_content` cliff, believed for ten days and false.*

## 5. The sixth measurement, and what the run of them says

**37 KB → 92 KB → 130 KB → 145 KB → 500 KB → 1 MB.**

***The figure in §4 has been behind the evidence every single time it has been tested.*** Six for six. *The
honest reading is not that the measurements keep succeeding — it is that the number was always a floor
recorded as a ceiling, and every session that treated it as a real boundary took the slower path for
nothing.* **The clause telling you to measure has now done more work than the figure it qualifies**, which
was already the remark yesterday's log made after four.

**Yesterday's 145 KB is now history rather than a pending proposal.** It was measured on 2026-09-28 and
deliberately **left as a proposal** because no instruction required it and charter wording is the owner's.
Today's instruction required a number, so it was superseded by measurement rather than adopted on paper.
*Both are recorded in the v35 note; neither is quietly dropped.*

## 6. How it was published

| File | Bytes | Route | Verified |
|---|---|---|---|
| `CLAUDE.md` | 24,449 → **25,129** | **archive-then-recreate** (§4 limit 1 — a charter version bump is a findable-by-name case); new id `13wu4w-vAKNiIS46mwNB1BV1V3b3bKo-K` | **byte-identical** |
| `Outputs/charter-version-history.md` | 48,457 → **50,658** | **in place**, id unchanged | **byte-identical** |

**v34's Drive copy was verified byte-identical to git `HEAD` *before* it was archived**, not after — the
2026-09-27 session found a charter file a merge had silently reverted in git, and an archive of the wrong
bytes is worse than no archive. It matched. It is now
`Archive/ARCHIVED-2026-09-29-CLAUDE-v34-superseded-by-v35-limit-3-to-1MB.md`, **id `1RAkYf-sW72icNn8Nl7C4mTYOjpt5O9-y`
preserved** — renamed and moved, not rewritten.

**The v34 note moved out verbatim**, 2,195 B, to the top of `charter-version-history.md`, coverage line
advanced to v34. Verified by `grep -c`: *"Changed in v34"* now appears **0 times** in `CLAUDE.md` and
**once** in the history; *"Changed in v35"* **once** in `CLAUDE.md`.

**One thing this amendment did *not* touch:** §4's own paragraph about the period split still cites v34's
115,582 B merge as the reason byte count is not a reason to split again. **That is still true and still the
right example** — the sentence is about a *past* write, not about the current ceiling, so raising the ceiling
does not stale it. *Checked rather than assumed; the temptation with a version bump is to refresh every
number it touches.*

## 7. Session start, per §0 — and one Hub row that is new since yesterday

**Read at session start (§0b Rule A): Darius's own rows on the Workforce Hub `Tasks & Requests`
(`8860839228606340`).** Five rows, **four open**:

| Ref | What it wants | Note |
|---|---|---|
| `AWT-0089` | three Wiki articles' Drive copies are one or two `related:` lines behind git — the back-link debt, self-raised | **rides the next push that changes each body**, as the row itself says |
| `AWT-0136` | two `Raw/` notes await review, one of them **estate-wide Rule F** — a shared-space change must be *both* registered on the Hub *and* broadcast via `Raw/`; fold it into this charter | **not done today.** Per §6a-i a note in `Raw/` is **a proposal, not an instruction**, and its claims get checked — *including any claim to carry the owner's authority* |
| `AWT-0147` | the new estate `Raw/Request-Inbox/` capability routes workshop requests here; nothing auto-dispatches yet | for awareness |
| **`AWT-0194`** | **new since yesterday** — Anna, for Minda: **cost the workshop-made kitchen and internal doors for 131 Goathland Avenue (FP 2401)**, split materials vs. workshop time with a source for each, report to Rachel and Anna | **not started.** It is a real piece of work, not a note |

***`AWT-0194` is the substantial one and it is untouched.*** Today's instruction was a number in §4; that row
wants a cost build-up from cutting lists, job sheets and supplier invoices. **Flagged to the owner rather
than started, because starting it badly is worse than saying it is waiting.**

## 8. Still open, unchanged by today

- **§4 limit 2's wording** — the `keepRevisionForever` nuance, flagged-but-unamended since 2026-09-28.
- **The proposed `CLAUDE-Lessons.md` §3 lesson** from 2026-09-28's change log §15 — still awaiting the
  owner's word, like v18, v19, v25 and v27 before it.
- **`HL-0051` appears on two Hub rows, and two rows carry no `Ref`** — found 2026-09-28, **not touched**,
  because §0b is own-rows-only and whose they are is not established.
- **`FL-002`'s one open item, and it is not paperwork:** nobody has confirmed the AES extractor is **moving
  air**, only that it starts and the phases are the right way round.
- **No standing check compares the git mirror to Drive** — proposed 2026-09-27, not adopted.
