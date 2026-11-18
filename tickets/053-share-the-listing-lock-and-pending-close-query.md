# 053 · Share the listing lock and pending-close query

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #15, #22, #52

## In brief

Set a common write order for listing and inquiry changes.

## Technical steps

1. Put the previous row-locking read behind `listing_repo.lock_listing(connection, listing_id)` and add `set_listing_status`. In `inquiry_repo.py` add `decline_other_pending(connection, listing_id, accepted_id=None)` for closing all or all except one Pending row.
2. Make request connections autocommit between transactions and start a transaction explicitly in `transaction()`. Require callers to take the listing lock before dependent writes.

## In first-time-coder language

1. Make one shared way to reserve the item's database row for a change and one shared way to close waiting inquiries for it.
2. Hold the item row first and then work on requests for that item. Follow that order everywhere. Keep all related changes together.

## Check your work

- [ ] Listing writes can share one passed connection and no helper commits on its own.
- [ ] Tests or a scratch transaction show only relevant Pending rows close, with an optional spared inquiry and rollback leaving original rows.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 053, Share the listing lock and pending-close query. Teach me the prerequisite ideas for row locks, consistent lock order, and transaction boundaries. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 053, Share the listing lock and pending-close query, using the acceptance checks I paste below. Check that classification and filters affect only the expected rows, and review explicit transaction and read behavior. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
