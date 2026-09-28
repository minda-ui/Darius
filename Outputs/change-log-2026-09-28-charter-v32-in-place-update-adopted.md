# Change log — 2026-09-28 — the charter goes v31 → v34 in one day, and every limit it set got measured

**Session 23. Seven owner instructions, three charter versions, and the day's own rules bent twice by the
day's own work.** v32 adopted in-place Drive update; v33 removed the size thresholds and re-measured the one
real ceiling; v34 merged the snapshots back and re-measured it again. Plus a live workshop question that
turned into the most valuable number of the week.

***Two things about this file's own framing, corrected rather than left standing.*** Its opening line read
*"short by this KB's standards, and deliberately so"* — **written when the day looked like one amendment; it
became the longest session this KB has recorded**, at fourteen sections and 33 KB. *The line is replaced
rather than struck, because unlike a superseded figure it was never a fact about the workshop — only a
prediction about the day, and a wrong one.* **And the filename still says `charter-v32`**: it is kept that
way deliberately, because `CLAUDE-Rules.md` §6a, the registers' Drive-id table and the index all cite it by
name, and **renaming a live file to flatter its own title is not worth breaking a charter citation for.**

**Reader's map.**

| § | What is in it |
|---|---|
| 1–2 | the v32 instruction, and the two sections of `CLAUDE.md` that moved |
| 3 | the new rule's limits clause biting on its own first use |
| 4 | the byte-check that ran *before* anything was archived |
| 5 | three files snapshotted under their own headers' orders |
| 6 | a Gmail MCP contradiction put to the owner, not resolved here |
| 7 | `AWT-0136` closed out, and the first real use of the new default |
| 8 | `keepRevisionForever` measured — it sharpens limit 2 rather than relaxing it |
| 9 | what is still open |
| 10 | a live workshop question, and an egress change that cost a page |
| 11 | the Cabineo price challenged and answered — **and a mistake of mine** |
| 12 | §6a gains its third capability limit: the setup script |
| 13 | **v33** — the size thresholds go; three "size" numbers separated; 92 KB measured |
| 14 | **v34** — the snapshots merged back; 130 KB measured; five files archived |

**The thread running through 12–14:** each of those three came from a short owner instruction, and each
turned out to contain a distinction worth making — *a capability missing versus a permission withheld*
(§12), *our policy versus a tooling measurement versus a claim about a tool* (§13), and *merging content
versus destroying the copies it came from* (§14).

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
- ~~**The Composio CLI install line** for the environment setup script — the owner's, and it needs a fresh
  session to take effect.~~ **Pasted in by the owner, 2026-09-28.** *Not verifiable from this session:* the
  setup script runs at session start, and this container has carried the CLI since yesterday's manual
  install, so **the first genuinely fresh session is the test.** Two checks named for it — `composio
  --version` must return **0.4.1** (a second, older **0.2.4** ships as a Claude plugin at
  `~/.claude/plugins/cache/composio/composio/0.2.4/bin` and is also on `PATH`, behind `~/.local/bin`), and
  `composio connections list` must show `darius-googledrive` **without prompting a login**. *That second
  one settles the open question below.*
- **Does Composio auth survive a cold start?** **Untested and not assumed either way.** The CLI binary and
  the auth directory are the same place — `~/.local/bin/composio` is a symlink to `~/.composio/composio`,
  and `~/.composio/user_data.json` sits beside it at mode `600` (*noted by listing names only; not read,
  per §6a's never-hold-a-credential rule*). **So they persist or vanish together**, which is the useful
  shape of it: if the directory survives, the setup line is a harmless no-op; if it does not, a fresh
  session has the CLI but needs `composio login` before any Drive call. *This session has been continuous
  since the install, so it cannot answer the question.*
- **§4's limit 2 wording** — the `keepRevisionForever` nuance in §8, for the owner to fold in or decline.
  **Still open at the end of the day**, and now the only charter wording left flagged-but-unamended: v33 and
  v34 both went past it without touching limit 2. *Deliberate — §8's finding sharpens the rule rather than
  changing what it requires, and charter wording is the owner's.*
- **`giunzioni.html`/Cabineo** still left for its own pass (62,404 B) — **and now unreachable** (§10).
- **Two rows on Help & Lessons carry no `Ref`** (61 rows, 59 with one).
- **No standing check compares the mirror to Drive.** Proposed on 2026-09-27, **not adopted**. *Today it was
  exercised by hand **eight times** — twice for v32's archives, once each for v33's and v34's, and five times
  for the snapshots before they were archived. Every one matched. Eight manual runs in a day is the strongest
  argument yet for the standing check, and it is still only a proposal.*

**Closed later the same session, after this list was first written:** the Gmail ruling (§6), the Composio
install line (§12), §6a's third capability limit (§12), the ~25 KB thresholds and the 37 KB and ~82 KB figures
(§13), and the period split itself (§14). *The struck items above are left struck rather than deleted, which
is this KB's practice and the reason this section is readable as a record rather than just a to-do list.*

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

## 12. §6a gains its third capability limit — the setup script

**Owner's word, asked for and given:** *"yes, record it in §6a."* The offer was made at the end of the
setup-script work and is now carried out.

**What it says.** `CLAUDE-Rules.md` §6a already held two entries of one shape — *deleting* a Smartsheet sheet
and *renaming* one are UI actions the owner takes, because the connector has no tool for either, and in both
cases **the capability is missing, not the permission**. The environment's **setup script** is the third: it
runs at session start, it is edited in the cloud UI, and **no connector, no CLI and no file in the working
tree reaches it.**

**One detail was checked rather than asserted.** The draft said only "the cloud UI". Where in the UI is a
fact the next session would otherwise re-derive, so it was read off the product documentation before
publishing: **the environment menu in the session title bar → *Edit* → *Setup script*.** *Recorded with the
note that it was confirmed, because an unsourced UI path ages badly.*

**And the edge the two sheet entries do not have.** A sheet delete takes effect when the owner does it. A
setup-script change takes effect **only on a fresh session** — so it cannot be verified in the session that
asked for it, which is exactly the position this session is in (§9). The entry points at §9's two named
checks rather than repeating them, so there is one copy of them to keep correct.

**Published the long way, and the rule says why.** A charter file is **§4 limit 1** — the superseded copy
must be findable by name — so this took **archive-then-recreate**, not the v32 default:

| Step | Result |
|---|---|
| Archive | `1wWq_-6Xs8CDgwjs1wGXROGM7-svir_Yq` renamed to `Archive/ARCHIVED-2026-09-28-CLAUDE-Rules-before-the-setup-script-capability-limit.md`, **id preserved**, reported back at **16,155 B** — the exact pre-edit size |
| Recreate | uploaded **from disk**, new id `1JrirbnvLYCmLDDrynsBdUMI8s9kChXwY`, **16,155 → 17,146 B** |
| Verify | `download_file_content` → decode → `diff`: **byte-identical**, and the native connector did the checking |

*The half of v32 that still applies here: the recreate uploaded the working copy rather than retyping it, so
limit 1 costs an id and an archive entry — it no longer costs a hand re-emission.* **Second charter publish
of the day to take the fallback, and the third file overall.**

**A gap closed on the way past.** The Drive-ids table in `kb-registers.md` had **no `CLAUDE-Rules.md` row at
all** — this morning's Gmail-ruling publish minted `1wWq_...` and never recorded it, so the id has now been
archived without ever having been written down. *Both ids are in the table now, the superseded one named as
superseded.* The same table's change-log row still read **15,364 B** after two later in-place updates had
taken that file to **21,025**; corrected. *A table of current ids is only useful if its sizes are current
too, and in-place updates change a size without changing the id that would otherwise prompt an edit.*

## 13. v33 — the size thresholds go, and the one real ceiling gets measured

**Owner's instruction, in full:** *"we don't have anymore size restrictions."* Said in answer to my closing
line that `kb-registers.md` was at 24,326 B and would need snapshotting soon.

**It overrules something I published this morning, and the overruled text is kept rather than deleted.**
§5 above records the question the cheaper write raised and the answer I gave it: *the ~25 KB threshold
stands, because it is about a file being readable and a row being findable, not about the cost of a write.*
The owner has decided otherwise. **Both live-file headers now carry the instruction and a note of what it
supersedes**, because the reasoning was published under my name and a silent deletion would read as though
it had never been held.

**Three "size" numbers existed, and they are not the same kind of thing.** Separating them was the whole of
the work:

| Number | What it was | What happened to it |
|---|---|---|
| **~25 KB** snapshot threshold | **our own policy** | **Removed on the instruction.** It was ours to drop |
| **37 KB** in-place ceiling (limit 3) | **a measurement** — the largest in-place write proven | **Re-measured to 92 KB.** An instruction cannot move this; only a probe can |
| **~82 KB** `read_file_content` cliff | **a claim about a tool** | **Did not reproduce.** Retired |

*A tooling limit is not the owner's to waive and was not treated as though it were. §4's own words say to
extend limit 3 **by measuring, not by assuming**, so that is what was done.*

**The probes.** Two scratch files in `Raw/`, each created and then replaced in place **with same-size,
different-content bytes** — so a no-op would fail the byte check and a partial write would fail the size
check:

| Probe | Size | Revisions after | Bytes | Elapsed |
|---|---|---|---|---|
| 46 KB | **46,035 B** | **1 → 2** | **identical** | 6 s |
| 92 KB | **92,070 B** | **1 → 2** | **identical** | 5 s |

Both ids unchanged; both titles unchanged, confirming an in-place update does not touch the filename. **Both
probes were trashed after measuring** — nothing stays in `Raw/` once filed (§1).

**And the 82 KB cliff did not reproduce.** `read_file_content` on the 92,070 B probe returned **92,069
characters** — not empty. One character short, with trailing whitespace altered, which is §3's existing point
that **it renders rather than returns bytes**; it is not a failure at size. *Stated carefully: the empty reads
this KB actually has on record are **images at 2.9 MB** (`Raw/20260918_070518.jpg`, still an open Processed
item). The 82 KB text boundary is the claim that did not survive contact, and it never bound the publish path
anyway, which uses `download_file_content`.*

**A new boundary turned up in its place, and it belongs to the session, not to Drive.** From about 46 KB a
download's result exceeds this session's context budget and is **spilled to a file on disk** instead of
returned inline. **Verification still works** — the decode step reads from disk, which is what it always did —
but a large file cannot be eyeballed inline. *That is a change in how a big file is verified, not in whether
it can be. It is written into limit 3 so the next session does not read the spill as a failure.*

**Published.** `CLAUDE.md` **23,171 → 24,213 B**, v32 archived as
`Archive/ARCHIVED-2026-09-28-CLAUDE-v32-superseded-by-v33-size-thresholds-removed.md` and recreated at
`1RKDUyPVK2tEDdPehrFqLyP_EYws7luX_` — **still the fallback, and correctly so: limit 1 is about findability,
not size, so removing the size thresholds does not touch it.** The Drive copy was verified byte-identical to
git `HEAD` before the rename, as on every archive today.

***And `charter-version-history.md` went in place, at 46,597 B.*** The v32 note moved into it verbatim
(1,662 B), and **the file that this morning took the fallback on limit 3 at 44,930 B now qualifies under the
default** — id `15H9mZ...` unchanged. *The first thing the re-measurement paid for, an hour after it was
made, and the cleanest possible demonstration that the old 37 KB figure was a floor on knowledge rather than
on capability.*

*What was not done, and is offered rather than assumed: **the three existing snapshots were left alone.** The
instruction is forward-looking — no further snapshot on byte count — and un-splitting settled history would
destroy three copies that are cited and findable by name for no gain. Say the word if they should be merged
back.*

*One thing no instruction can remove, noted once so it is not discovered the hard way: **Smartsheet still
truncates a cell at 4,000 characters.** That is the platform's limit, not this KB's policy, and it is why
`AWT-0136` was closed by row comment (§7).*

## 14. v34 — the snapshots merged back, and a third ceiling measured

**Owner's instruction: *"merge the snapshots back."*** The direct consequence of v33: with no size threshold,
a period split has nothing left to serve. Offered at the end of §13 and answered.

**Five snapshots, not the three I said.** *§13 and the v33 note both said three. That was the registers'
own header table, which lists only its own three — the index had two more. Counting the files gave five.
A count read off a pointer table instead of the thing itself, which is this KB's oldest recurring error.*

| File | Bytes | New name in `Archive/` |
|---|---|---|
| `kb-registers-snapshot-2026-09-21.md` | 65,449 | `ARCHIVED-2026-09-28-kb-registers-snapshot-2026-09-21-merged-back-into-the-live-file.md` |
| `kb-registers-snapshot-2026-09-27.md` | 23,678 | …`-2026-09-27-merged-back-into-the-live-file.md` |
| `kb-registers-snapshot-2026-09-28.md` | 29,143 | …`-2026-09-28-merged-back-into-the-live-file.md` |
| `change-log-index-snapshot-2026-09-21.md` | 40,222 | `ARCHIVED-2026-09-28-change-log-index-snapshot-2026-09-21-merged-back-into-the-live-file.md` |
| `change-log-index-snapshot-2026-09-28.md` | 25,043 | …`-2026-09-28-merged-back-into-the-live-file.md` |

**Merged, not deleted.** Each was verified byte-identical to git `HEAD` first, then **renamed into `Archive/`
with its id preserved.** *"Merge the snapshots back" does not say destroy them, and the bytes cost nothing
to keep. They also leave the git mirror's working tree, because `Archive/` is not mirrored — their bytes
remain in git history.*

**Nothing was retyped; every row was copied byte-for-byte by script.** And the duplication the old headers
had warned about was the whole difficulty:

- **Processed items needed real care.** The nine open rows appeared in **all three** registers snapshots
  *and* the live file — a plain concatenation would have emitted them **four times**. Instead the
  2026-09-21 order was walked row by row and **the live version substituted wherever it was the authority
  (eight rows)**, the ninth appended, and the 2026-09-27 and 2026-09-28 Processed tables **dropped as exact
  duplicates — verified 9 of 9 each, not assumed.** **29 + 1 = 30, nothing lost and nothing doubled.**
- **Wiki (36) and Outputs (74) needed none** — disjoint by construction, each snapshot holding only what was
  new. *Checked anyway. The check threw a false alarm worth recording: the Wiki table's first column is a
  **date**, so six rows "collided" on it. They are different rows sharing a date, not duplicates — a
  reminder that a de-duplication key has to be a key.*
- **The index was clean**: 1 + 3 + 19 = **23 sessions**, and the newest-first order was **re-verified after
  assembly** rather than trusted.
- **Two Drive-id tables, and they share no path at all** (checked). So both are kept under one heading,
  labelled by date, with the later winning where it ever matters. *The older one carries two rows for the
  same proposal file, the second saying it supersedes the first — a pre-existing pair, preserved rather
  than tidied.*

**Then the merge broke v33's own ceiling.** `kb-registers.md` came out at **115,582 B**, past the 92 KB
proven an hour earlier — so rather than fall back, **a third probe ran at 130,005 B**: same-size,
different-content, id stable, revisions 1 → 2, byte-identical, 6 s. **Limit 3 is now 130 KB**, and the
registers went **in place**, id unchanged. *Twice in one day the rule's own instruction — extend it by
measuring — was what let the work proceed on the fast path.*

**Published.** `kb-registers.md` **28,088 → 115,582 B** and `change-log-index.md` **11,275 → 72,817 B**,
both in place, both byte-verified from the spilled download. `CLAUDE.md` **24,213 → 24,449 B** as **v34**
(archive-then-recreate, v33 archived, new id `1RAkYf-sW72icNn8Nl7C4mTYOjpt5O9-y`), and the v33 note moved
verbatim into `charter-version-history.md` **46,597 → 48,457 B**, in place.

***One correction inside v34, caught by reading the published file back.*** The first v34 publish still had
§0 telling a session that `kb-registers.md` *"holds only"* the open Processed items — untrue the moment the
merge landed, and in the one paragraph every session reads first. **Corrected in place, same version, no
archive** — there is no superseded *version* to make findable, so limit 1 is not engaged. *That is the
second stale line this session that only surfaced on read-back, after the registers' own update history in
§12. Publishing and then reading is catching things that writing and then publishing does not.*

## 15. Documenting the day — three Hub lessons written, one §3 lesson proposed not written

**Owner's instruction: *"document today's work."*** Most of it was already written as it happened, in §1–§14
and in the registers. Three things were genuinely outstanding.

**First, this file's own framing was stale** — see the corrected header: a title that stopped at v32, an
opening line predicting a short day, and a reader's map that ended at §11 when there were fourteen sections.
*Fixed in place. The filename still says `charter-v32` and stays that way: `CLAUDE-Rules.md` §6a, the
registers' Drive-id table and the index all cite it by name, and renaming a live file to flatter its own
title is not worth breaking a charter citation.*

**Second, §0b Rule B was owed three rows**, and this is the first time today's work has reached the Hub.
Rule B says a lesson goes on **Help & Lessons** as the shared record, not only into a local log:

| Ref | Lesson | Status |
|---|---|---|
| **`HL-0064`** | **A count read off an index or pointer table is not a count of the thing itself** — the five-versus-three snapshots error, recorded alongside the four earlier instances in the same week (`git log` without `--follow`, `find_in_sheet`'s 100-row window, a `head -40` of JSON, and a `grep` whose hits were reported on as the whole article) | Answered |
| **`HL-0065`** | **When an owner lifts a "limit", sort it into policy / measurement / claim-about-a-tool first** — only the first is theirs to lift; the second must be measured; the third may simply not reproduce. All three happened in one instruction today | Baked into charter |
| **`HL-0066`** | **Reading a file back after publishing catches stale lines that writing it never does** — twice today, and both were self-describing figures inside files that update in place, where a stable id removes the prompt to revisit them | Answered |

*`HL-0064` and `HL-0065` are written as estate-wide rather than workshop-specific, because neither depends
on anything about this KB.* **The refs were allocated after checking the sheet, not from memory** — the
highest existing was **`HL-0063`**, three higher than the `HL-0060` this KB had on record, so other seats
have been adding. *That is `HL-0064`'s own lesson applying to the act of filing `HL-0064`.*

**And the write was verified from the server rather than from its own response.** `add_rows` returned
`displayValue: null` on all three `Date raised` cells, which reads like a failed date. It was not: a
grouped count filtered to Darius's rows returns **three rows dated 2026-09-28**. *The response not
rendering a value is not the value being absent — and the check that settles it has to come from somewhere
other than the call being checked, which is the same principle as §4's "the verifier stays the native
connector".*

**Third, and deliberately not done: the §3 lesson.** `HL-0064`'s finding — the fifth instance of one error
in a week — plainly belongs in `CLAUDE-Lessons.md` §3 as well. **It is proposed here, not written.** *§3's
own text records that this is how §3 grows: v18's count fix, v19's order clause, v25's measurement clause
and v27's dated-negative-finding clause were each **proposed rather than added**, and each waited for the
owner (*"add that §3 lesson"*). Four precedents, and no reason today is the exception — the more so with
three charter versions already published since this morning.*

> **Proposed §3 lesson, for the owner to add or decline:** *A count is only as good as the call that
> produced it, and an index is not the thing it indexes.* Before stating a count, name the command behind
> it and check that the command touched the objects — a full listing — rather than a header table, a
> default page, a filtered read or the subset a search matched. **Five instances in the week to
> 2026-09-28**, the last of which was reading "three snapshots" off a table that by design lists only its
> own three. *This is v25's clause — a limitation is a property of the call you made — extended to cover
> the case where the call was your own choice of what to read.*

**What documenting the day cost, since it is the argument for doing it as you go:** §12–§15 were written
after the work rather than during it, and **two of the four turned up an error in something already
published.** *The sections written alongside the work — §1 to §11 — turned up none.*
