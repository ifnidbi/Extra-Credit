# 078 · Build isolated integration test fixtures

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #16, #23, #26, #68

## In brief

Make it easy for any teammate to start reliable tests on clean data.

## Technical steps

1. Create `tests/conftest.py` fixtures for the app factory, unique test upload directory, client, and MySQL setup in a database verified as `extra_credit_test`. Apply schema, seeds and views in deterministic order and reset rows safely between integration cases.
2. Create named fake users and role helpers. Keep CSRF active for protection tests and offer a clearly named token helper for authenticated writes.

## In first-time-coder language

1. Give the tests their own database and photo folder so they cannot touch everyday work. Put the same pretend students and items in place each time.
2. Make a simple helper for signing in a demo user or getting a form token. Make the tests stop if pointed at the wrong database.

## Check your work

- [ ] Two test runs start from the same data and outcomes regardless of order.
- [ ] A development database name is refused, no real credentials are printed, and test uploads live in a temporary directory.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [pytest fixture how-to with examples](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [MySQL script files and batch mode](https://dev.mysql.com/doc/refman/8.4/en/mysql-batch-commands.html)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 078, Build isolated integration test fixtures. Teach me the prerequisite ideas for fixtures, temporary directories, test client sessions, and DB isolation. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 078, Build isolated integration test fixtures, using the acceptance checks I paste below. Check database-name guard, repeatability, cleanup, and how tests obtain or verify CSRF tokens. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
