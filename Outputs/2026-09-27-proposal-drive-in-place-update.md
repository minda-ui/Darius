# Proposal — amend §1 and §4: Drive content can be updated in place

**For the owner's decision. Not applied.** Charter changes go to Minda as proposals first, and this one
touches two standing rules that shape how every session works, so it is written down rather than acted on.

**Proposed by** Darius, 2026-09-27, out of the `AWT-0136` Composio rollout.
**Decision wanted:** adopt / adopt with limits / decline.

## 1. What the charter says now

§1: *"Drive has no patch API, so every change re-emits a whole file by hand."*

§4 and the working practice built on it: **archive-then-recreate** — rename the superseded Drive copy into
`Archive/` with a reason and date, then `create_file` a new copy, then verify. That exists because
`create_file` mints a **new Drive id** every time, so there is no way to change a file without replacing
it.

Three costs follow, and all three are real rather than theoretical:

1. **Every edit is retyped by hand.** Publishing six files earlier today meant emitting roughly 120 KB of
   content into tool calls.
2. **Ids migrate.** `tpacad-blind-bore-tool-id-fix.md` and `carcase-fixings-cabineo-x-vs-confirmat.md`
   both cite Drive ids that now resolve into `Archive/`, which §7 already records as a consequence
   accepted rather than tidied.
3. **Transcription errors.** The capture file came back **one byte short** today — a trailing blank line
   typed differently from the one on disk. The v12 test rebuilt `Suppliers/altendorf-gmbh.md` **four bytes
   short**. Both are the same failure: a human-in-the-loop copy of bytes that already existed.

## 2. What was measured

`GOOGLEDRIVE_UPLOAD_UPDATE_FILE` via the Composio CLI takes a `fileId` and a **local file path**. Two
tests, both verified with the **native** connector rather than the tool's own report:

| | Probe (`Raw/`, disposable) | `CLAUDE-Workshop.md` |
|---|---|---|
| Size | 271 B → 392 B | 37,297 B |
| Drive id | unchanged | **unchanged** (`19z9y6Pte9_rRiFQwh0eoDGWVYdAoYkKd`) |
| Revision count after | 2 | **1 → 2** |
| `createdTime` | preserved | preserved |
| Parent folder | unchanged | unchanged (KB root) |
| Byte check | identical, sha256 matched | **identical**, sha256 `ca7549ad…` |
| Source of bytes | a local file | **the git working tree** |
| Elapsed | — | **5.7 s** |

**The second test was designed so a silent no-op could not pass.** The content uploaded was identical to
what was already on Drive, so a byte-check alone would have looked clean even if nothing had been written.
The proof it wrote is the **revision count going 1 → 2**, with a new `modifiedTime`. *Recorded because a
test that cannot fail proves nothing.*

## 3. What is proposed

1. **§1** — replace *"so every change re-emits a whole file by hand"* with: Drive has no partial-patch
   API, so a change replaces a file's whole content; **it does not have to be retyped** — content already
   on disk can be uploaded in place, keeping the file's id. *Drive retains the previous bytes as a
   revision, but **not durably** — see the correction in §5.*
2. **§4** — archive-then-recreate becomes the **fallback**, not the default. Default: update in place and
   byte-verify. Archive-then-recreate stays required where the in-place path is untested (below) or where a
   superseded copy must be **findable by name**, which a revision is not — the period snapshots
   (`kb-registers-snapshot-<date>.md`) keep their own rule untouched.
3. **A verification rule, unchanged in spirit:** every write is still proved by
   `download_file_content` → decode → `diff`. **The verifier stays the native connector.** Both halves of
   a byte-check must not depend on the same new tool.
4. **A limits clause**, written in rather than discovered later: the in-place path is proven at **392 B and
   37,297 B, text/markdown, UTF-8**. It is **untested** above 37 KB — including the ~82 KB boundary where
   `read_file_content` returns empty — and untested for binary files, Google-native types, and files this
   account does not own. Until each is tested, those cases use archive-then-recreate.

## 4. What does not change

- **Drive stays the source of truth** (§1).
- **Both stores in the same session** — an article written to one and not the other re-opens the mirror gap.
- **Byte-verify every write.** Nothing here relaxes that; it removes the step where a human retypes bytes,
  which is where this KB's byte discrepancies have actually come from.
- **The native connector stays in place.** This is a second path, not a replacement, and the rollout it
  came from is explicitly a *fallback* layer.

## 5. The honest case against

- **It adds a dependency.** The path runs through a third-party service (Composio) and a CLI installed in
  an ephemeral container. If either is unavailable, the fallback is the current rule — so the rule must
  stay documented, not deleted.
- **It is one day old.** Two tests, one session, one file size decade.
- **Revisions are not an archive, and this is stronger than it was when this proposal was written.**
  *Corrected the same day, after a Finance-seat report reaching Alex prompted the check.* The original text
  said only that a revision is not **findable by name**, which is true and was the weaker half. Measured
  since, on the 37 KB test file itself:

  ```
  GET /drive/v3/files/<id>/revisions?fields=revisions(id,keepForever,modifiedTime,size)
  → both revisions, including the superseded one: "keepForever": false
  ```

  **`keepForever` defaults to `false`, so Drive may purge the superseded revision.** The previous bytes are
  therefore retained at Drive's discretion, not guaranteed. **A named `Archive/` copy does something a
  revision does not**, on durability as well as visibility. Setting `keepForever` is a separate PATCH per
  revision — possible, but one more step that must not be forgotten, and not something this KB does today.
  *This does not overturn the proposal; it removes the reason to think archiving is now redundant.*
- **It does not reduce the token cost of composing** an edit, only of transmitting it. The 37 KB still has
  to be *written*; it no longer has to be *typed twice*.

## 6. Recommendation

**Adopt with the limits clause, and item 2 narrowed by the §5 correction** — items 1, 3 and 4 in full,
and item 2 worded so archive-then-recreate remains mandatory for the snapshot files, for anything where a
superseded copy must be findable by name, **and now for anything whose superseded bytes must survive**,
since `keepForever` is `false` by default. The measured gain is not speed but **the removal of a known error class**, and this KB has now
shipped a byte-wrong file twice by hand.

*If adopted, §1 and §4 both change, so `CLAUDE.md` is re-emitted once — which is exactly the operation the
amendment makes cheaper, and the first real use should be byte-verified with particular care.*
