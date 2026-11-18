# 016 · Run your first app test

**Estimate** 30 minutes · **Stage** Foundation  
**Prerequisites** #9

## In brief

Write a test that proves Flask can start and answer without MySQL.

## Technical steps

1. Install pytest in the dev requirements. In `tests/test_health.py`, import the app factory and make a test client that requests `/health`. Compare status and JSON with the route contract.
2. Temporarily change one expected value and watch pytest fail, then restore it.

## In first-time-coder language

1. Make a small checker that visits the health address for you and compares what comes back with what you expected.
2. Tell the checker to expect a wrong answer once, and watch it catch the difference.

## Check your work

- [ ] The test passes from a clean venv with the DB stopped.
- [ ] You can explain one failing assertion from the deliberate mismatch.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [pytest getting started with assertions](https://docs.pytest.org/en/stable/getting-started.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [Harvard CS50 Python testing lecture, video and notes](https://cs50.harvard.edu/python/weeks/5/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 016, Run your first app test. Teach me the prerequisite ideas for test client, assertion, and reading a test failure. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 016, Run your first app test, using the acceptance checks I paste below. Check whether my test asserts behavior clearly and can run independently of the database. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
