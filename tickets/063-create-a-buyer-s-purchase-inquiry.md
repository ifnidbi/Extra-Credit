# 063 · Create a buyer's purchase inquiry

**Estimate** 60 minutes · **Stage** Inquiries  
**Prerequisites** #37, #53, #62

## In brief

Let a buyer ask to arrange pickup for an available item.

## Technical steps

1. Add `find_pending_for_buyer`, `insert_inquiry`, and `create_inquiry(actor, listing_id, data)`. Validate, lock the listing, and check seller active, Available status, different buyer and seller, and no existing Pending inquiry for that buyer and item. Use a current read for the duplicate check.
2. Implement signed-in POST `/api/inquiries` returning the created record and 201.

## In first-time-coder language

1. Send a meeting request for an item that is still for sale. The buyer must be signed in and cannot request their own listing.
2. While saving the request, check there is no other waiting request from that buyer for the same item.

## Check your work

- [ ] A valid request creates one Pending row with the signed-in buyer.
- [ ] Self-inquiries, duplicates, unavailable and inactive-seller listings, and unauthorized writes are refused.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 063, Create a buyer's purchase inquiry. Teach me the prerequisite ideas for relationship authorization, atomic duplicate checks, and accepted input. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 063, Create a buyer's purchase inquiry, using the acceptance checks I paste below. Check status and ownership under the lock, plus what outcome concurrent duplicate requests could have. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
