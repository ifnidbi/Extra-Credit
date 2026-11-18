# 081 · Test inquiry decisions and transaction rollback

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #66, #78

## In brief

Show unacceptable requests leave no partial changes.

## Technical steps

1. Write `tests/test_inquiries.py` for self/duplicate refusal, accepted and competing Pending changes, decline-only, edit and withdrawal, participant privacy and rejected repeats. Confirm state in MySQL after HTTP requests.
2. Make one controlled failure after an acceptance write and verify rollback. If practical, exercise simultaneous attempts from separate connections and record outcomes.

## In first-time-coder language

1. Have a checker act like different buyers and sellers. Try asking twice, trying someone else's request, and accepting when two requests are waiting.
2. Make something fail halfway through a fake approval and check every record went back to the way it started.

## Check your work

- [ ] One test verifies Accepted, Reserved and declined competitors stay consistent.
- [ ] On injected failure all prior values remain, and an outsider cannot read or edit inquiry details.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [pytest monkeypatch examples for dependencies](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 081, Test inquiry decisions and transaction rollback. Teach me the prerequisite ideas for atomic operations, failure injection, and realistic role tests. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 081, Test inquiry decisions and transaction rollback, using the acceptance checks I paste below. Check that the rollback test fails if an early write commits and that authorization tests verify saved state and privacy. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
