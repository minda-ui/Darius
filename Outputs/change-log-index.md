# Change-log index — Workshop of Furniture Making KB

**Every session's `change-log-*.md` file, newest first.** Split out of `Outputs/kb-registers.md` at
**v28** (2026-09-21) because that file was re-emitted whole every session and 35,701 bytes of it was
append-only history. **Period-split in turn on 2026-09-23** (owner's instruction, *"split by period"*),
once the index itself reached 46,462 bytes: the same problem one file along, and the same fix.

**This file holds 2026-09-28 onwards.** Everything earlier is in a dated snapshot, never re-emitted:

| Snapshot | Holds | Provenance |
|---|---|---|
| `Outputs/change-log-index-snapshot-2026-09-21.md` | Sessions 1 to 19, newest first | the bytes that were on Drive, 40,222 B, byte-identical to git `d4cd712`; **not retyped** |
| `Outputs/change-log-index-snapshot-2026-09-28.md` | Sessions 20 to 22 (2026-09-23, 2026-09-24, 2026-09-27), newest first, plus the pointer to the 2026-09-21 snapshot | the bytes that were on Drive, 25,043 B; **renamed, not rewritten** |

**Nothing overlaps** — each snapshot's rows and this file's rows are disjoint.

**Snapshotted again on 2026-09-28 under this file's own ~25 KB rule.** It stood at **25,043 B** before the
day's row was written — already at the threshold, and *one* of its three rows (2026-09-27) was **14 KB on
its own**. **A change-log row is settled the moment it is written**, because a change log is never revised,
so all three moved and none had to be judged.

**The snapshots were made by renaming, not rewriting.** Retyping rows averaging over 2 KB each is exactly
where this KB's byte discrepancies come from (§3). *The cost: a snapshot keeps the header it had when it
was live, so it still describes itself as the §0 file. It is not. The filename and this table are
authoritative — and the 2026-09-28 snapshot's header also still says "this file holds 2026-09-23 onwards",
which was true of it while it was live and is now true of nothing.*

**This is the file `CLAUDE.md` §0 sends you to**, second in the session-start reading order: read the
newest row, then the open `Processed items` rows of `kb-registers.md`. **When this file passes roughly
25 KB, snapshot it again.**

*From v32 a Drive file's content can be replaced in place rather than retyped, which makes re-emission
cheaper but **does not relax the threshold** — that exists so a file stays readable and a row stays
findable. §4's limits clause keeps archive-then-recreate mandatory for a snapshot anyway, because a
snapshot must be findable by name.*

**Nothing here was rewritten** at any split. Rows moved verbatim, in the same order.

---

## Change-log entries

Newest first.

| Date | Entry | File |
|---|---|---|
| 2026-09-28 | Session 23 - **the charter reaches v32, and the new rule's first use was an exception to it.** One instruction (*"recommendation is adopt with the limits clause. Go ahead"*), one amendment, three files snapshotted because their own headers said to. **(1) What changed.** §1 gains **"How a file on Drive is changed"**: Drive still has **no partial-patch API**, so a change replaces a file's whole content - *but it does not have to be retyped*, and content already on disk can be uploaded **in place, keeping the id**. §4 gains **"How a change reaches Drive"** - the in-place default, the **unchanged** verification rule, and archive-then-recreate **demoted to a fallback, not deleted**. `CLAUDE.md` **22,734 -> 23,171 B**; the v31 note moved **verbatim** (3,619 B incl. separator) to `Outputs/charter-version-history.md`, **41,311 -> 44,930 B**, coverage line advanced to v31. `README.md` **deliberately untouched** - *"four files since v31"* is still true at v32, the same judgement the 2026-09-24 sweep made about the mentions it declined to move. **(2) The gain is an error class, not a keystroke.** Proved yesterday at 392 B and at **37,297 B**: id unchanged, `createdTime` preserved, **revisions 1 -> 2** as the only proof a write happened when the bytes are meant to be identical, byte-identical on download-decode-diff, 5.7 s, uploaded straight from the working tree. What it removes is **hand re-emission** - the source of this KB's one-byte shortfall on 2026-09-27 and its four-byte one at v12, *both with the spare byte in the **local** copy, which a size check reads as transfer loss.* **(3) And the limit, found the same day it was proposed.** `keepForever` is **`false` by default** on Drive revisions, the superseded one included, so **Drive may purge the old bytes**. *An id that stays stable and an old version that survives are two independent properties, and yesterday's first draft let one stand in for the other.* So the fallback stays **mandatory** for three named cases: a superseded copy that must be **findable by name** (charter version bumps, `-snapshot-<date>.md` files, a superseded article other work cites); superseded **bytes that must survive**; and **anything outside what has been proven** - above **37 KB**, across the ~82 KB `read_file_content` cliff, binary, Google-native, or not owned by this account. **(4) The clause bit immediately, and neither of today's publishes used the new default.** `CLAUDE.md` took the fallback on limit 1 (a version bump is exactly a findable-by-name case) and `charter-version-history.md` on limit 3 (44,930 B is above the proven 37 KB) - *a limits clause is worth nothing if the session that writes it reaches past it the same day*. **Recorded in the v32 note itself**, not only here, because a rule whose own adoption is an exception to it is worth seeing stated. *So the day produced **no** new measurement of the default in anger; the 37 KB ceiling is where it honestly sits.* **(5) The check that ran before anything was archived.** Both Drive copies verified **byte-identical to git `HEAD` before** being renamed - 22,734 and 41,311 B, both `diff` clean. *Not ceremony: yesterday closed by finding `kb-registers.md` eight days and three structural versions stale in git, where a merge had resolved to the superseded side. **An archive of the wrong bytes is worse than no archive**, because it is filed under a name that asserts what it holds.* **(6) A tooling note.** The live `CLAUDE.md` id took three attempts: the native connector's `search_files` rejects `'<folder>' in parents` (*"Unsupported query field: parents"*), rejects `name contains`, has no `fields` parameter, and `title = 'CLAUDE.md'` returns every estate KB's charter and its archived copies. **The Drive v3 API accepts the parent query directly** and listed the KB root's nine children in one call. *Two paths to Drive with different query grammars is a fact about the tooling, not about Drive - the v25 lesson again: a limitation is a property of the call you made.* **(7) Three files snapshotted, each on its own rule.** `kb-registers.md` at **29,143 B**, where the header did not merely permit it but **ordered** it (*"the next session must snapshot this file before adding anything"*) - carried out before a single row was added, renamed on Drive (**id unchanged**), rebuilt by script at **15,384 B**, the nine open Processed items carried by `sed` and then `diff`ed against the snapshot, **byte-identical**. This index at **25,043 B**, one row of which was 14 KB; **a change-log row is settled the moment it is written**, so all three moved and none had to be judged. *Third time by this method for the registers, second for the index.* **And a question the cheaper write raised, answered in writing rather than left implicit: the ~25 KB threshold stands, because it is about a file being readable and a row being findable, not about the cost of a write.* **(8) A contradiction put to the owner, not resolved here.** A **Gmail MCP server is present in this session**, 30 tools including `send_message`, against §0a's *"no Gmail (Darius logs and tracks, it does not send)"* and §6b's *"no Gmail toolkit is to be linked by this or any later session"*. **No Gmail tool was loaded or called.** Recorded as a charter/environment contradiction, which is §0a's own instruction - *records the contradiction and asks; never guesses one into the other.* **The charter is not being amended to fit the environment, and the environment is not being used against the charter.** **(9) Still open**: `HL-0060` needs widening for the Hub's new **Archive sheet** (`1037721118312324`, named in `AWT-0146`'s own Response, which also warns of a both-sheets Task-ID search caveat) - ID allocation must now group-by across **both** sheets; three Open Hub rows as canonical briefs (`AWT-0089`, `AWT-0127`, `AWT-0147`); the Composio CLI install line for the environment setup script (the owner's, and it needs a fresh session); `giunzioni.html`/Cabineo; two Help & Lessons rows with no `Ref`. **And no standing check compares the mirror to Drive** - proposed on 2026-09-27, **not adopted**; today's pre-archive check was manual and covered two files | `Outputs/change-log-2026-09-28-charter-v32-in-place-update-adopted.md` |
