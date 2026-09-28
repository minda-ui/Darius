# Change log — 2026-09-28 — the charter reaches v32, and the new rule's first use was an exception to it

**Session 23.** One instruction, one amendment, and three files snapshotted because their own headers said
to. *Short by this KB's standards, and deliberately so: the work was decided yesterday and measured
yesterday; today was carrying it out and recording it.*

**Reader's map.** §1 the owner's instruction and what it changed. §2 the two sections of `CLAUDE.md` that
moved. §3 the clause that bit on its own first use. §4 the check that ran before anything was archived.
§5 three files snapshotted under their own rules. §6 a contradiction put to the owner, not resolved here.
§7 what is still open.

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

*What the day therefore did **not** produce: a single measurement of the new default in anger. The 392 B
and 37,297 B runs from 2026-09-27 remain the only evidence, and the 37 KB ceiling in §4 is where it
honestly sits.*

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

## 7. Still open

- **`AWT-0136`** to be updated with the adoption — the row that carried the measurements now needs the
  outcome.
- **`HL-0060` needs widening.** The Hub gained an **Archive sheet** (`1037721118312324`), named in
  `AWT-0146`'s own Response, which also warns of a both-sheets Task-ID search caveat. Task ID allocation
  must now group-by across **both** sheets; `HL-0060` describes one.
- **Three Open Hub rows** as canonical briefs: `AWT-0089` (the `related:` back-links, still riding the next
  push that changes each body), `AWT-0127`, `AWT-0147`.
- **The Composio CLI install line** for the environment setup script — the owner's, and it needs a fresh
  session to take effect.
- **`giunzioni.html`/Cabineo** still left for its own pass (62,404 B).
- **Two rows on Help & Lessons carry no `Ref`** (61 rows, 59 with one).
- **No standing check compares the mirror to Drive.** Proposed on 2026-09-27, **not adopted**. Today's
  pre-archive check was manual and covered two files.
