# 064 · Show only inquiries the student participates in

**Estimate** 60 minutes · **Stage** Inquiries  
**Prerequisites** #40, #63

## In brief

Let buyers see outgoing requests and sellers see incoming ones.

## Technical steps

1. Implement `find_inquiry`, `find_inquiries_for_actor`, `get_inquiry(actor, inquiry_id)`, and `list_inquiries(actor, direction)` with appropriate participant joins and explicit fields.
2. Add the authenticated GET collection and detail endpoints. Validate direction and show counterpart contact information only to participants for that request.

## In first-time-coder language

1. Show a student requests they sent or got on items they sell. Check who is asking before giving any details or contact information.
2. Give the browser a list address and one address for a specific request. A stranger should see the same answer as if it were missing.

## Check your work

- [ ] Buyer and seller each see rows relevant to them, including expected contact fields.
- [ ] An unrelated student gets 404 for detail, and guest/invalid-direction requests are handled predictably.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 064, Show only inquiries the student participates in. Teach me the prerequisite ideas for scoped reads, buyer-versus-seller joins, and private projections. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 064, Show only inquiries the student participates in, using the acceptance checks I paste below. Check each scope direction and confirm neither outsider nor guest can see contact details. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
