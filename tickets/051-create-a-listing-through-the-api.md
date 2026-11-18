# 051 · Create a listing through the API

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #15, #44, #48

## In brief

Give signed-in students a validated way to put an item up for sale.

## Technical steps

1. In `listings.py`, implement `validate_listing(data)` and `create_listing(actor, data)` with contract lengths, Decimal currency rules, allowed condition and existing category. In `listing_repo.py` write `insert_listing` and return the inserted ID.
2. Add POST `/api/listings` in `routes/listing_api.py`. Use authenticated identity for seller and database defaults for status/time.

## In first-time-coder language

1. Let a signed-in student fill out an item's details. Check title, campus, price, currency, condition and category before saving.
2. Use the logged-in student's number as seller. Give back the new listing so the browser knows where it went.

## Check your work

- [ ] A valid POST creates an Available listing with the logged-in seller and returns 201.
- [ ] Guests, bad categories and invalid prices are refused, and submitted owner/status values cannot override the server.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Python exact decimal arithmetic](https://docs.python.org/3/library/decimal.html)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 051, Create a listing through the API. Teach me the prerequisite ideas for server validation, inserts, identity, and returning new IDs. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 051, Create a listing through the API, using the acceptance checks I paste below. Check field boundaries, currency precision, category conflicts, and that the client cannot choose seller or initial status. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
