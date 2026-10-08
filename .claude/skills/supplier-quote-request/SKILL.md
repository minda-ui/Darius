---
name: supplier-quote-request
description: Find two or three local suppliers or service firms (repair shops, wholesalers, tooling) and prepare quote requests as Gmail drafts in minda@ for the owner to send. Use when the owner says "find … shops/suppliers near Newcastle", "where can I buy/collect…", "get quotes for…", or "create drafts asking for a quote".
---

# Supplier quote request

Adopted at the 2026-10-08 good night, from the extractor motor rewind and LRE16 searches. **Drafting rules: CLAUDE-Rules
§6b** — drafts in minda@ or info@ allowed, **never send**, never edit or delete a draft once made.

## Steps

1. **Pin the spec first** from the KB (Fault Log row, machine article, nameplate): every figure a supplier needs to
   quote without calling back.
2. **Search the web** for 2–3 firms in Newcastle / Gateshead / Sunderland / North Tyneside. Prefer each firm's **own site**
   for email and phone; **flag any address taken only from a directory** ("confirm by phone"). Note trade bodies
   (e.g. AEMT) and drop firms shown dissolved.
3. **Sites behind Cloudflare return 403 — never work around it.** Use search listings, and say what couldn't be read.
4. **Write the request** as `Outputs/YYYY-MM-DD-<topic>-quote-requests.md`: the shops table and one email (spec, what
   happened, what is asked: price options, turnaround, collection, warranty). No invented details.
5. **Create the drafts** in minda@: `composio execute GMAIL_CREATE_EMAIL_DRAFT --account darius-gmail-minda` with
   `recipient_email`, `subject`, `body`, `is_html:false`; sign with the owner's own signature. **List each back**:
   recipient, subject, draft id.
6. **Record** in the change log and on the relevant row (Fault Log / Tasks). Replies are only read once the sender is
   approved — use `approve-mail-sender`.
7. **For parts to collect today**, give the trade counters' phone numbers and say "call first"; warn about
   look-alike part numbers (e.g. LRE16 vs LRD16 — different contactor families).
