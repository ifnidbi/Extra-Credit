# 080 · Test listing CRUD and search behavior

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #50, #54, #56, #78

## In brief

Prove the browse-to-manage listing path works with real SQL.

## Technical steps

1. In `tests/test_listings.py`, exercise catalog/detail GET and filter combinations, signed-in POST, owner/stranger PUT, mark Sold, and DELETE. Assert persisted owner, status, amount and public projection. Include inactive seller and removed visibility cases.
2. Use fixture rows with same timestamps or mixed currencies to verify deterministic order and filters. Include a malformed price and an empty page.

## In first-time-coder language

1. Have the tests pretend to shop and sell. Create a listing as a student, change it as its owner, try changing it as a stranger, and take it down.
2. Try two different currencies and items posted at the same time so you can see whether search and ordering behave the same each run.

## Check your work

- [ ] Tests demonstrate all four REST methods, checked ownership and state, and correct currency-aware filters.
- [ ] Guest responses omit private fields and listings hidden by the contract, and invalid input leaves stored data unchanged.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [pytest fixture how-to with examples](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Python exact decimal arithmetic](https://docs.python.org/3/library/decimal.html)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 080, Test listing CRUD and search behavior. Teach me the prerequisite ideas for integration tests, permission boundaries, data fixtures, and search assertions. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 080, Test listing CRUD and search behavior, using the acceptance checks I paste below. Check case coverage, actual persisted fields, stable paging, and whether a privacy regression would fail a test. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
