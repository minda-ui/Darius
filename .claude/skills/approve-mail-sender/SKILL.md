---
name: approve-mail-sender
description: Approve a new email sender and then read only their mail, in info@ or minda@. Use when the owner says "check my email for…", "it's in my emails", "it's from <company>", "add <sender> to approved senders", or asks for prices, orders, receipts or quotes that arrived by email from someone not yet approved.
---

# Approve a mail sender, then read only their mail

**The rule is CLAUDE-Rules §6b** (read-only, approved senders only; drafts allowed, never send). Read it first; this
file is how to apply it. Adopted at the 2026-10-08 good night.

## Steps

1. **Who sent it?** If the sender is not in §6b's approved list, ask: company name or address. **Do not search the
   inbox by keyword to find out** — searches are always `from:` an approved sender.
2. **Record the OK in §6b first — its own step, its own commit.** Quote the owner's words, date it, state the scope:
   - a **public mail domain** (outlook.com, gmail.com, …) → approve **the single address**, never the domain;
   - a **marketplace** (eBay, Amazon) → its confirmation address(es) **and only purchases the owner names**;
   - otherwise the company domain.
   Publish CLAUDE-Rules in place, verify SAME, commit, push. *(2026-10-04: the §6b edit and the search in one command
   was refused by the safety check — keep them separate.)*
3. **A new mailbox connection?** `composio link gmail --alias <alias> --no-wait --no-browser` → the owner authorises →
   **one `GMAIL_GET_PROFILE` call to confirm the address** → amend §6b → only then read.
4. **Search narrowly:** `GMAIL_FETCH_EMAILS --account <darius-gmail-info-v2 | darius-gmail-minda>` with
   `from:<address> <item words> newer_than:Nd`. If nothing, check the other mailbox and the sender's other known
   address (eBay UK sends from both `ebay@ebay.co.uk` and `ebay@ebay.com`) — widening the address is a §6b edit first.
5. **Read bodies only.** Attachments (invoices, receipts) **only on the owner's OK**; download to scratchpad, read the
   lines needed, delete the copies; **never file them in git**.
6. **Never copy** bank details, card numbers or home addresses into the KB.
7. **Record** what was found where it belongs (Fault Log, price library, supplier article) and in the change log.
