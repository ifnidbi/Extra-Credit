# 066 · Accept or decline an inquiry as the seller

**Estimate** 90 minutes · **Stage** Inquiries  
**Prerequisites** #54, #65

## In brief

Reserve an item and resolve competing requests as one action.

## Technical steps

1. Implement `decide_inquiry(actor, inquiry_id, decision)` in `inquiry_decisions.py`. Lock listing then inquiry, and verify seller, status and enum choice. On Accepted, reserve the Available listing and decline the remaining Pending rows in the same transaction. On Declined, change only the selected Pending inquiry.
2. Expose the authorized PUT decision endpoint. Inject a temporary failure in a safe test to verify rollback after the first write.

## In first-time-coder language

1. Let the item owner approve or refuse a waiting request. Approval also sets the item aside and clears other waiting requests so two buyers cannot both get it.
2. Treat those steps as one change. If something goes wrong in the middle, put everything back.

## Check your work

- [ ] Accepting leaves exactly one Accepted inquiry and a Reserved listing. Declining alone leaves listing status untouched.
- [ ] An unrelated person, repeat decision or interrupted write produces no partial change.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 066, Accept or decline an inquiry as the seller. Teach me the prerequisite ideas for state transitions, atomic updates, and competing requests. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 066, Accept or decline an inquiry as the seller, using the acceptance checks I paste below. Check the seller and state checks, order of writes, competing outcomes, and rollback evidence. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
