---
name: good-night
description: Darius's end-of-day routine. Use whenever the owner signs off — "good night", "goodnight", "night", "that's all for today", "see you tomorrow". Closes the day's change log, then proposes skill candidates from the whole day's work for the owner to adopt or delete, and records every decision in Outputs/skill-candidates-register.md so nothing rejected is offered again.
---

# Good night — close the day, propose skill candidates

**Owner, 2026-10-08:** *"Every time we trigger 'Good Night', propose me candidates for skill from all day's work. I will
choose which to adopt and which to delete."* The rule is in `CLAUDE-Lessons.md` §3; this file is how to run it.

## 1. Close the day first — run `end-of-day`

Follow `.claude/skills/end-of-day/SKILL.md` (2026-09-29): `git status` first, change log, registers, index, publish
in place and prove byte-identical, commit and push. **Skill candidates come after the day is documented, never
instead of it.**

## 2. Find the candidates — from the whole day, not the last hour

Read **every change-log entry dated today** (and any earlier entry since the last good night) and the conversation.
A candidate is work that is **likely to come back** and that **went better, or would have, with a fixed method**:
- a **sequence repeated** today or on earlier days (check `Outputs/change-log-index.md` for earlier occurrences);
- a **method worked out the hard way** — a wrong turn corrected, a gotcha found, a check that caught something;
- a **lookup with known sources** (which supplier, which page, which sheet, which ids);
- a **routine the owner asked for in words that will recur** ("check the Raw folder", "find suppliers for…").

**Not a candidate:** a one-off; anything an existing skill already covers (list `.claude/skills/`, and say so if a
candidate would extend one instead); anything already in the register as **Deleted** unless something new changes the
case — then say what changed.

## 3. Present them — 2 to 5, best first

For each, one short block:
- **Name** (kebab-case) and **trigger** — the words the owner would use.
- **What it would do** — 3–5 steps.
- **Evidence** — where it happened (change-log refs, how many times).
- **New skill or extension** of an existing one.

Then ask, in one question, **Adopt / Delete / Later** for each (multi-select is fine). **If there are none worth
proposing, say so** rather than padding the list.

## 4. Act on the answer

- **Adopt:** write `.claude/skills/<name>/SKILL.md` (front matter `name` + a `description` that says when to use it,
  with trigger words), the method as numbered steps, and the governed facts it relies on **cited, not copied** (a Wiki
  article is the source of truth; the skill says how to run it). If the method needs a governed write-up, add or extend
  a `Wiki/Processes/` article too.
- **Delete:** record it as Deleted, with the owner's reason if given.
- **Later:** record it as Later; offer it again at the next good night only if it recurs.
- **Every decision** goes in `Outputs/skill-candidates-register.md` (date, name, trigger, decision, reason, skill
  path), then the change log, Drive, commit, push — and only then say good night.
