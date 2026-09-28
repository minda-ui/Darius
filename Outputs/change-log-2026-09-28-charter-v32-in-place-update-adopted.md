# Change log — 2026-09-28 — the charter reaches v32, and the new rule's first use was an exception to it

**Session 23.** One instruction, one amendment, and three files snapshotted because their own headers said
to. *Short by this KB's standards, and deliberately so: the work was decided yesterday and measured
yesterday; today was carrying it out and recording it.*

**Reader's map.** §1 the owner's instruction and what it changed. §2 the two sections of `CLAUDE.md` that
moved. §3 the clause that bit on its own first use. §4 the check that ran before anything was archived.
§5 three files snapshotted under their own rules. §6 a contradiction put to the owner, not resolved here.
§7 `AWT-0136` closed out, and the first real use of the new default. §8 a measurement that sharpens
limit 2, and one imprecise sentence flagged. §9 what is still open. §10 a live workshop question and an
egress change. §11 the Cabineo price, and a mistake of mine.

---

## 1. The instruction, and the one thing it changed

The owner's words: *"The in-place-update proposal — `Outputs/2026-09-27-proposal-drive-in-place-update.md`,
recommendation is adopt with the limits clause. Go ahead"*.

**That proposal was written yesterday and corrected yesterday**, and the correction is what shaped today's
text. Its first draft said the in-place path leaves Drive *"holding the previous bytes as a revision"*.
A check prompted by another seat's report returned `"keepForever": false` on **both** revisions, the
superseded one included — so Drive may purge them. **The gain was never durability.** It is that content
already on disk can replace a Drive file's content **without being retyped**, and hand re-emission is
where this KB's byte discrepancies have actually come from: a one-byte shortfall on 2026-09-27 and a
four-byte one at v12, both with the spare byte in the *local* copy, which a size check reads as transfer
loss.

`CLAUDE.md` **22,734 → 23,171 B**, version header to **v32**, and the v31 note moved out to
`Outputs/charter-version-history.md` (**41,311 → 44,930 B**) **verbatim** — 3,619 B including its
separator, inserted at the top of the notes, coverage line advanced to *"v8 (2026-09-16) to v31
(2026-09-23)"*. Verified by `grep -c`: the v31 note now appears **0 times** in `CLAUDE.md` and **once** in
the history file; the v32 note **once** in `CLAUDE.md`.

**`README.md` was deliberately left unchanged.** Line 13 says the charter is *"four files since v31"*.
Still true at v32 — it is a pointer that reads correctly either way, the same judgement the 2026-09-24
sweep made about seven mentions it declined to touch.

## 2. The two sections that moved

**§1 gains "How a file on Drive is changed."** Drive still has **no partial-patch API**, so a change
replaces a file's whole content — *but it does not have to be retyped.* That sentence is the whole
amendment; the rest of §1 is untouched. The paragraph carries the `keepForever` limit in its own italics,
because §1 is where a session reads *"Drive is the source of truth"* and could otherwise take a revision
for an archive.

**§4 gains "How a change reaches Drive"**, in three parts:

- **Default — update in place, from disk.** Write locally, upload to the existing `fileId`. The id does not
  change, so citations do not go stale.
- **Verification unchanged.** `download_file_content` → decode → `diff` against the local file. **The
  verifier stays the native connector** — both halves of a byte-check must not depend on the same tool.
  And where the content is *meant* to be identical, a byte-check cannot tell a write from a no-op, so the
  **revision count** is the proof. *That is the test design from yesterday's 37 KB run, promoted into the
  rule.*
- **Fallback — archive-then-recreate, demoted but not deleted**, and **mandatory** for three cases:
  (1) anything whose superseded copy must be **findable by name** — the charter files and their version
  bumps, the `-snapshot-<date>.md` files, a superseded Wiki article other work cites; (2) anything whose
  superseded **bytes must survive**, since `keepForever` is `false` by default and setting it is a separate
  PATCH per revision, not done here; (3) **anything outside what has been proven** — above **37 KB**,
  across the ~82 KB `read_file_content` cliff, binary, Google-native, or not owned by this account.

Closing note in §4: the in-place path runs through a third-party service and a CLI in an ephemeral
container. **If either is unavailable the fallback is the whole rule**, which is why it stays documented
rather than deleted.

## 3. The clause bit on its own first use

**Neither of today's two publishes used the new default.**

`CLAUDE.md` took the fallback on **limit 1** — a charter version bump is precisely a case where the
superseded copy must be findable by name, so v31 was archived by rename to
`Archive/ARCHIVED-2026-09-28-CLAUDE-v31-superseded-by-v32-drive-in-place-update.md` and v32 recreated.
`charter-version-history.md` took it on **limit 3** — at 44,930 B it is above the 37 KB the in-place path
has actually been proven at, and *a limits clause is worth nothing if the session that writes it reaches
past it the same day.*

**This is recorded in the v32 note itself**, not just here: *"The first real use of the new default was
this file — and the clause bit immediately."* A rule whose own adoption is an exception to it is worth
seeing stated rather than inferred.

*What the charter amendment itself therefore did **not** produce: a measurement of the new default in
anger. **The first one came later the same session, and it is this file** — see §8.*

## 4. The check that ran before anything was archived

**Both Drive copies were verified byte-identical to git `HEAD` before being renamed**, not after.

`CLAUDE.md`: Drive 22,734 B, git `HEAD` 22,734 B, `diff` clean.
`charter-version-history.md`: Drive 41,311 B, git `HEAD` 41,311 B, `diff` clean.

*This is not ceremony.* Yesterday's session closed by finding `Outputs/kb-registers.md` **eight days and
three structural versions stale in git**, where a merge had resolved to the superseded side and the
following "sync the mirror" commit touched 73 files and not that one. **An archive of the wrong bytes is
worse than no archive**, because it is filed under a name that asserts what it holds. Both matched.

**One tooling note worth keeping.** The live `CLAUDE.md` id took three attempts to find. The native
connector's `search_files` rejects `'<folder>' in parents` (*"Unsupported query field: parents"*), rejects
`name contains`, and has no `fields` parameter; `title = 'CLAUDE.md'` works but returns every estate KB's
charter and its archived copies, newest-first, across pages. **The Drive v3 API accepts the parent query
directly**, and reaching it through the Composio proxy listed the KB root's nine children in one call —
`CLAUDE.md` = `1rhOR_BnN1V3JTLmC8FI3n8ykwgC5vWw8`, 22,734 B. *Two paths to Drive with different query
grammars is a fact about the tooling, not about Drive, and it is the v25 lesson again: a limitation is a
property of the call you made.*

## 5. Three files snapshotted, each because its own header said to

**`Outputs/kb-registers.md` — 29,143 B, and its header did not merely permit this, it ordered it**: *"The
next session must snapshot this file before adding anything - and it will need a name other than
`-snapshot-2026-09-27.md`, which is taken."* Carried out **before a single row was added**. Renamed on
Drive to `kb-registers-snapshot-2026-09-28.md` (**id unchanged**, `1veAsc6qbfQu-XDVsUe1UJ9UhcOEmpTmY`),
copied byte-identical locally, live file rebuilt **by script** at **15,384 B**. The nine open Processed
items were carried by `sed` and then `diff`ed against the snapshot — **byte-identical**, nothing retyped.
*Third time by this method.*

**A question the new default raised and the registers now answer in writing.** In-place update makes
re-emission cheaper, so does the ~25 KB threshold still earn its keep? **Yes, and the header says why**:
the threshold is about a file being readable and a row being findable, not about the cost of a write — and
a period snapshot is *exactly* §4's case 1, because a snapshot must be findable by name. *A cheaper write
is not a reason to keep a longer file.*

**`Outputs/change-log-index.md` — 25,043 B before today's row**, already at its own limit, with a
14 KB row for yesterday's session alone. Snapshotted on the same rule.

## 6. A contradiction put to the owner, not resolved here

**A Gmail MCP server is present in this session** — 30 tools including `send_message`. §0a says Darius's
connectors are *"Google Drive + Smartsheet + Web (read) — no Gmail (Darius logs and tracks, it does not
send)"*, and `CLAUDE-Rules.md` §6b records that **no Gmail toolkit is to be linked by this or any later
session**.

**No Gmail tool was loaded or called.** This is recorded as a contradiction between the charter and the
environment, which is §0a's own instruction — *when two facts that should agree don't, Darius records the
contradiction and asks; it never guesses one into the other.* **The charter is not being amended to fit
the environment, and the environment is not being used against the charter.** It is the owner's ruling to
make.

**RULED, same session.** Minda, verbatim: ***"Don't use Gmail as per your Claude.md."*** **The charter
stands.** Written into `CLAUDE-Rules.md` §6b (14,520 → **16,155 B**), where the access decisions live —
**archive-then-recreate under §4 limit 1**, since it is a charter file, with the Drive copy verified
byte-identical to git `HEAD` before the rename.

**The new entry deliberately widens the 2026-09-27 one.** That ruling scoped **Composio's toolkits**;
this one covers **any Gmail capability reaching this seat by any route** — MCP connector, toolkit, or
otherwise. *The earlier wording would have read as silent on a Gmail server arriving some other way.*

*And the point the 2026-09-27 entry closed on — that no-Gmail is a policy this assistant observes, not a
boundary the tooling enforces — stopped being a prediction today. Thirty Gmail tools were reachable; the
count that matters is that **none was loaded or called**. A session-start prompt suggesting app tools be
resolved through Composio was followed only within the Drive and Smartsheet scope.*

## 7. `AWT-0136` closed out — and the new default's first real use

The row that carried yesterday's measurements ended: *"STILL FOR THE OWNER ... rule on the
in-place-update proposal."* That is now discharged, so the row had to say so.

**It was recorded as a row comment, not by rewriting the Response**, and the reason is the amendment's own
subject. That cell is near Smartsheet's silent 4,000-character limit; reproducing it to append a paragraph
would mean **retyping 4,000 characters by hand** — exactly the error class v32 exists to remove. *And I
overwrote a long cell that way on 2026-09-27, dropping the five criteria out of T016's live notes for about
a minute.* A comment is append-only and cannot damage the cell. The posted text was verified against what
came back: untruncated.

**Then this file and the index were republished in place** — `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` against each
existing `fileId`, ids unchanged, verified by `download_file_content` → decode → `diff`. **Both qualify
under §4's default**: neither is a version bump, neither is a snapshot, both are well under 37 KB, both are
ordinary text this account owns.

*So the rule's first real use was not the charter that carried it, but the correction of a sentence in this
very change log — which is the right shape for it. A cheap in-place write is what makes fixing a stale line
worth doing at all; under archive-then-recreate, "I will carry it at the next touch" was often the honest
answer, and this KB has the deferred-figure notes to prove it.*

## 8. A measurement that sharpens limit 2 — and one imprecise sentence, flagged not amended

**Found by a mistyped parameter.** `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` was called with `file_id`; the schema
error listed the keys it does accept, and among them was **`keepRevisionForever`**. §4's limit 2, written
hours earlier, says `keepForever` is false by default *"and setting it is a separate PATCH per revision"* —
so this looked like a sentence I had got wrong.

**Measured rather than assumed**, on a scratch file in `Raw/`, created and then updated in place with
`keepRevisionForever: true`:

| Revision | Size | `keepForever` |
|---|---|---|
| 1 — the superseded bytes | 47 B | **`false`** |
| 2 — the bytes just written | 65 B | **`true`** |

**The flag pins the revision being created, not the one being replaced.** So it does **not** protect the
bytes an in-place update is about to supersede: to keep those, the flag would have had to be set on the
*earlier* write, before anyone knew it would matter — or PATCHed onto that revision afterwards.

***Limit 2 therefore stands, and for a sharper reason than the one I wrote.*** The charter says setting
`keepForever` is a separate PATCH per revision; strictly it can also be set at upload time, **but only
forward-looking, which is no use to the case limit 2 exists for.** The sentence is imprecise rather than
false, and the rule it supports is unaffected.

**Flagged, not amended.** §3 makes charter wording the owner's, and a charter edit is itself a limit-1
case; a sharper §4 limit 2 is worth having but is not mine to write. *The probe was trashed after
measuring — nothing stays in `Raw/` once it has been filed (§1).*

*And the finding arrived the way several have this week: from an error message, not from a plan. The
schema told me more than the documentation did, because I made a mistake in front of it.*

## 9. Still open

- ~~**The Gmail MCP contradiction**, for an owner ruling.~~ **Ruled and recorded the same session; see §6.**
- **`HL-0060` needs widening.** The Hub gained an **Archive sheet** (`1037721118312324`), named in
  `AWT-0146`'s own Response, which also warns of a both-sheets Task-ID search caveat. Task ID allocation
  must now group-by across **both** sheets; `HL-0060` describes one.
- **Three Open Hub rows** as canonical briefs: `AWT-0089` (the `related:` back-links, still riding the next
  push that changes each body), `AWT-0127`, `AWT-0147`.
- **The Composio CLI install line** for the environment setup script — the owner's, and it needs a fresh
  session to take effect.
- **§4's limit 2 wording** — the `keepRevisionForever` nuance in §8, for the owner to fold in or decline.
- **`giunzioni.html`/Cabineo** still left for its own pass (62,404 B).
- **Two rows on Help & Lessons carry no `Ref`** (61 rows, 59 with one).
- **No standing check compares the mirror to Drive.** Proposed on 2026-09-27, **not adopted**. Today's
  pre-archive check was manual and covered two files.

## 10. Late in the session — a live workshop question, and an egress change

The owner asked how to add fixings to the top and bottom panels. **`giunzioni.html` is the page that
covers it, and both fetch routes failed**: `curl` got `CONNECT tunnel failed, response 403` and `WebFetch`
returned `EGRESS_BLOCKED`. **Yesterday the same host returned HTTP 200 at 62,404 B.** So the block is new
today and is in this environment's egress policy, not in the site.

*This is the cost of the one decision from 2026-09-27 that was deferred rather than done.* The page was
mapped and hashed but **its text was never captured** — the provenance table in
`Wiki/Software/smartcabinet-online-manual.md` records `Text captured? no` against it — and it is now
unreachable. **The nine pages whose text was captured are still fully readable; the one left for "its own
pass" is not.** A hash proves a page has not changed; it does not let you read it.

**Answered from the KB's own evidence instead**, which turned out to be the better source: the decoded
`01-SIDE-LEFT.TCN` / `03-BOTTOM.TCN` files give the joint geometry directly — pocket in the side, **Ø5 ×
12 mm face hole in the top/bottom at Y = 230 and 40**, eight per box — and `cam.html` gives the location
of the configuration (**CAM → Configurazione Giunzioni**). *What could not be answered was the click path,
and it was not guessed.*

**Nothing was inferred from the photograph.** It shows hole clusters on the top and bottom edges; whether
those are the existing Ø5 pattern was put back to the owner rather than assumed, because adding a second
fixing system over an existing one is exactly the kind of error that discipline exists to prevent.

## 11. The Cabineo price — the article's own instruction, carried out, and a mistake of mine

**The fixings question of §10 turned into the most valuable number of the day.** The owner confirmed
Cabineo and then sent two supplier listings.

| | At 2,000 | Per each | This KB carried |
|---|---|---|---|
| Housing (SKU 186361) | £379.03 ex VAT | **£0.1895** | £0.77 |
| Screw, Cabineo 12 (SKU 186381) | £195.13 ex VAT | **£0.0976** | £0.10 |
| **Per joint** | | **£0.2871** | £0.87 |

**`carcase-fixings-cabineo-x-vs-confirmat.md` has said since 2026-09-18** that *"£0.77 for the housing is
the number I least trust… Challenge it at 2,000."* **It was challenged, and it was £0.19.** Per unit
£6.96 → **£2.30**; per 12-unit kitchen £83.52 → **£27.56**; the premium over confirmat **+£80.67 →
+£24.71**. *The article also guessed the direction of the fix — "getting it nearer £0.30 is money for one
phone call" — and understated it.*

**The half I trusted held; the half I flagged did not.** The £0.10 screw was an estimate I called the
weaker figure once the housing came down, and a real volume price put it at £0.0976. *Worth recording
because the instinct that produced the "£0.77 is untrustworthy" note was doing real work, and the same
instinct about the screw was simply wrong in the safe direction.*

**And it answered "which screw".** Only the Cabineo 12 is sold in a 2,000 box, and `03-BOTTOM.TCN` drills
**Ø5 × 12 mm** in 19 mm board. *Stated at the strength the article already used for the pocket/body match:
strong circumstantial agreement, not a part number off a drawing — and it does not replace the order
paperwork.*

### The mistake, and why it is the same one as always

**I told the owner the Cabineo decision was still open. It was not.** The article records it settled on
**2026-09-19** — *"Cabineo X was chosen, we ordered them"* — under a heading called `## Decided:
Cabineo X`. I had run a `grep` for "joint", read the two sections the hits pointed at, and reported on
the article as a whole.

***That is the v25 lesson wearing new clothes for the fourth time this week***: on 2026-09-27 it was
`git log` without `--follow`, then `find_in_sheet`'s 100-row window, then a `head -40` of a JSON listing.
**Here the truncating tool was my own choice of what to read.** A limitation is a property of the call you
made — *including when the call is "read the parts that matched".*

**Corrected in three places**: to the owner immediately, in the article's own new section, and in the
registers row. *The decision has stood for nine days and nothing was done on the wrong basis; the cost was
a sentence, not an action. It is recorded because the next one might not be.*

**What was held back, all of it the owner's** (§6a): the supplier is **not named** (page header cut off in
the photograph), the 2,000 price is **to be confirmed at checkout**, and **nothing was ordered and no
supplier contacted**. £574.16 ex VAT for both boxes is ≈250 carcases, ≈21 kitchens — a stocking decision.
