# 054 · Mark listings sold or remove them

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #53

## In brief

Close an item while keeping its marketplace history.

## Technical steps

1. Implement `mark_listing_sold` and `remove_listing` in `listing_lifecycle.py`, using listing lock, actor permission and allowed transitions. Decline remaining pending inquiries inside the same transaction.
2. Expose PUT status and DELETE routes in `listing_api.py`. Preserve reasoned 404/403/409 errors and use empty 204 for removal.

## In first-time-coder language

1. Give sellers a way to say an item was sold or to take it down. An admin can take down a listing for moderation.
2. Close waiting purchase requests at the same time, but keep the old item and request records for history.

## Check your work

- [ ] Selling or removing closes Pending requests with the correct listing transition, and removed records disappear publicly.
- [ ] An unauthorized or repeated change leaves both records unchanged.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL UPDATE clauses and examples](https://dev.mysql.com/doc/refman/8.4/en/update.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 054, Mark listings sold or remove them. Teach me the prerequisite ideas for soft deletion, state transitions, and atomic status changes. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 054, Mark listings sold or remove them, using the acceptance checks I paste below. Check every allowed role and status transition, and that pending changes roll back with the listing. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
