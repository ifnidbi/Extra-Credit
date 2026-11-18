# 052 · Update a listing as its owner

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #51

## In brief

Let sellers fix detail mistakes while keeping ownership and status safe.

## Technical steps

1. Add `update_listing_fields` to `listing_repo.py` and `update_listing(actor, listing_id, data)` to `listings.py`. Lock the listing row with a bound locking read, check owner and editable state, then write the same allowed fields as create.
2. Add PUT `/api/listings/<listing_id>`, returning updated public details. Ignore client-controlled ownership, time or state.

## In first-time-coder language

1. Find the item, make sure it belongs to the signed-in seller and is still editable, then save changed details.
2. Keep the existing seller, posting date and sale stage. Try editing someone else's item and see that it stays as it was.

## Check your work

- [ ] The owner can edit a valid Available/Reserved item and sees new values.
- [ ] Non-owners and ended listings are rejected, and invalid input leaves every prior field intact.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL UPDATE clauses and examples](https://dev.mysql.com/doc/refman/8.4/en/update.html)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 052, Update a listing as its owner. Teach me the prerequisite ideas for ownership, locking reads, validation reuse, and partial-failure checks. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 052, Update a listing as its owner, using the acceptance checks I paste below. Check server-side ownership, allowed fields/state, transaction use, and the refused-update evidence. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
