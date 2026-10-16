---
name: answer-seat-request
description: Answer a request for facts or input from another seat (Victoria, Anna, Alex, Rachel…) that arrives as a Hub Tasks & Requests row assigned to Darius and/or a note in the workshop Raw/ — e.g. "send Anna the workshop hazards", "facts only", "reply on AWT-…". Use when such a row or note is found at session start, or when the owner says "go ahead" on one.
---

# Answer a seat's request

Adopted at the 2026-10-16 good night, from `AWT-0537` (HSE/QC/ENV facts for Anna, 10-14/15), `AWT-0498` (report-back to
Victoria, 10-09) and `AWT-0516` (decisions to Anna, 10-10). Delivery itself is the estate skill
`raw-handoff-to-employee`; this file is the part before and after it.

## Steps
1. **Read the request exactly** — the Hub row and any Raw/ note. Note what is asked for, the format ("facts only",
   "plain words", "do not write the clauses"), where it goes (their Raw/ folder id), and who is copied. Wait for the
   owner's go-ahead if the row came from someone else and delivery touches another KB.
2. **Gather from the KB, with citations** — an `Explore` agent over Wiki/, `CLAUDE-Workshop.md`, the change logs and
   the live sheets, told to answer each heading with *facts as stated* and *"nothing in KB"* where there is none.
3. **Write the note in the asker's shape**, short, in plain words. **Every gap is written as a gap** ("not in the KB") —
   never filled from general knowledge or a guess. **Re-read it against the sources and cut any claim they do not
   support** (10-14: a board size, and an overload "fitted" on a future date, were removed before sending).
4. **Deliver** per `raw-handoff-to-employee`: check the target folder's parent is the right seat's KB, create +
   upload in place, verify SAME; own copy in `Outputs/`. **Answer on the asker's existing Hub row** (Response column,
   both Drive ids, "this row is the copy" for anyone copied) — **do not raise a new row** for a reply.
5. **Ask the owner the gaps in one short numbered list** — the questions only they can answer.
6. **Follow up** with the owner's answers **as given** (their words where short; say what was *not* stated rather
   than inferring it), delivered the same way; then set the row **Done** with the date. If an answer shows a real
   risk, say so to the owner plainly, once — the asker writes the policy, not Darius.
7. **Record:** change log entry, registers (Drive-id rows for both copies — the delivered one marked *not ours to
   edit*), commit, push.

## Never
- Never edit anything in the other seat's KB except dropping the note into its `Raw/`.
- Never write the other seat's deliverable (clauses, policy, decisions) — facts and gaps only.
- Never mark the row Done while owner-only gaps are still unanswered and unstated.
