# 065 · Edit or withdraw a waiting inquiry

**Estimate** 60 minutes · **Stage** Inquiries  
**Prerequisites** #64

## In brief

Give buyers control over their own requests while they are waiting.

## Technical steps

1. Add `lock_inquiry`, `update_inquiry_details`, and `set_inquiry_status` in `inquiry_repo.py`. Implement `edit_inquiry` and `withdraw_inquiry` by locating the owning listing, locking it before the inquiry, then re-checking buyer, listing consistency, and Pending state.
2. Wire PUT and DELETE on the detail endpoint. PUT changes only meeting details and DELETE stores Withdrawn with a 204 response.

## In first-time-coder language

1. Let the buyer change the meeting plan while it is waiting, or take the request back. Make sure it is still their request and still waiting before saving.
2. Keep withdrawn requests as history. Leave the listing and other requests alone.

## Check your work

- [ ] A buyer can edit and withdraw a Pending inquiry, and withdrawn rows persist as history.
- [ ] Wrong buyers, non-Pending states and invalid new fields leave the row unchanged.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL UPDATE clauses and examples](https://dev.mysql.com/doc/refman/8.4/en/update.html)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 065, Edit or withdraw a waiting inquiry. Teach me the prerequisite ideas for state checks, lock order, scoped updates, and soft deletion. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 065, Edit or withdraw a waiting inquiry, using the acceptance checks I paste below. Check that fields, status, and related rows cannot change when a request is refused. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
