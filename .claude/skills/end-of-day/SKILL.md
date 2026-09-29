---
name: end-of-day
description: >
  Close out a working session in the Workshop of Furniture Making KB (Darius):
  write or extend the change log, update kb-registers.md and change-log-index.md,
  publish each to Drive and verify byte-identical, file any lesson learned on the
  Workforce Hub, then commit and push. Use when the owner signs off — "good
  night", "night", "signing off", "that's me done", "see you tomorrow" — or asks
  in any words to document, write up or record today's work. Also use before
  ending any session that changed something, even if the owner has not said
  goodbye.
---

# End of day — documenting the session

**The point is that nothing worked on today is left only in the conversation.**
Drive is the source of truth and the git mirror must match it; a session that
ends without this leaves both stale and the next session reading a lie.

## 0. First, find out what is actually outstanding

Do not work from memory of the session. Check:

```sh
git status --short          # uncommitted work
git log --oneline -5        # what is already recorded
```

**If the working tree is clean and the day's work is already committed and
published, say so and stop.** An empty end-of-day is a fine outcome; inventing a
change log entry for a day that produced none is not.

## 1. The change log

One file per session, `Outputs/change-log-YYYY-MM-DD-<slug>.md` (§4).

- **Same date as an existing log?** Append a section to it. Do not start a second
  file for one day.
- **New date?** New file. Create it on Drive with an 11-byte placeholder in
  `Outputs/` (`1jPXUHEHsjF_h0cllps3oP9CpFCVLem24`) to mint the id, then upload the
  real bytes in place.

**Write what actually happened, including what went wrong.** This KB's change
logs carry retracted diagnoses, corrected figures and wrong predictions on
purpose — a log that records only the right answer teaches nobody how the wrong
one looked at the time. Quote the owner's instruction verbatim where it drove
the work.

## 2. The registers — `Outputs/kb-registers.md`

Add a row to each table the session touched, and **update the count in that
table's header** (`**All N, oldest first.**`):

| Table | Add a row when |
|---|---|
| `Processed items` | something in `Raw/` was worked on |
| `Wiki structure changes` | an article was created, amended or retired |
| `Outputs produced` | anything was produced at all — this is the catch-all |
| `Drive ids` | a file was created, or an in-place update changed a recorded size |

***The Drive-ids table goes stale silently.*** An in-place update changes a file's
size without changing the id that would otherwise force an edit here, so **read
the rows back after publishing** and correct the sizes.

## 3. The index — `Outputs/change-log-index.md`

Newest first. New session → a new row at the top and bump *"all N of them"*.
Same session → extend the existing row rather than adding a second.

## 4. Publish, and prove each write

**Default is in-place from disk** (§4): write locally, then upload to the existing
`fileId`. The bytes are never retyped.

```sh
composio execute GOOGLEDRIVE_UPLOAD_UPDATE_FILE --account darius-googledrive \
  -d '{"fileId":"<id>","file_to_upload":"/home/user/Darius/<path>"}'
```

**Before overwriting, check Drive's current size against local.** If they differ,
something unrecorded is on Drive — stop and find out what before writing over it.

**Then prove it landed**: `download_file_content` → decode → `diff` against the
local file, using the **native connector** as the verifier (both halves of a
byte-check must not depend on the same tool). Above ~46 KB the download spills to
a file — decode it from there. Above **1 MB**, or for a charter version bump, take
archive-then-recreate instead (§4 limits 1–3).

## 5. The Workforce Hub — only if the day taught something

§0b Rule B: a lesson goes on the Hub as the shared record. **Own rows only,
never another seat's.**

- Allocate the next `HL-` ref **by reading the sheet**, not from memory — other
  seats add rows too.
- **Verify the write server-side.** `add_rows` has returned `displayValue: null`
  on `Date` cells that were in fact stored; a response not rendering a value is
  not the value being absent.

*Not every day has a lesson. A Hub row that restates the obvious costs the whole
estate attention.*

## 6. Commit and push

Stage everything, write a message that says what changed and why — including the
mistakes — and push to the working branch with the attribution trailers.

```sh
git push -u origin <branch>   # retry 2s/4s/8s/16s on network failure only
```

## 7. Say what is still open

End by listing what is **not** done: open Hub rows, unresolved contradictions,
anything proposed and awaiting the owner's word. **Charter wording is the
owner's** — propose, never adopt unasked.

## What not to do

- **Do not retype file content.** Upload from disk; hand re-emission is where
  this KB's byte discrepancies have come from.
- **Do not carry a count forward.** Recount it. A number read off an index or a
  pointer table is not a count of the thing itself (`HL-0064`, five instances).
- **Do not smooth over a correction.** If something published earlier today was
  wrong, the log says so in the log, not only in chat.
