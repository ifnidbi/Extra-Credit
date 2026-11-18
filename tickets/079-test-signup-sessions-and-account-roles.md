# 079 · Test signup, sessions, and account roles

**Estimate** 45 minutes · **Stage** Verification  
**Prerequisites** #43, #78

## In brief

Prove account features create the right rows and restrict the right callers.

## Technical steps

1. Write `tests/test_accounts.py` for multi-domain signup, malformed fields, duplicate addresses, login and logout, role restrictions and CSRF. Exercise an attempt to pass role on signup without changing the default.
2. Test self profile update and password deactivation, then check access from the old session. Assert status, body and database state where relevant.

## In first-time-coder language

1. Make a repeatable checker that tries a good signup, a repeat address, a bad password, a normal login and logout. Try opening an admin door as a student.
2. Change a profile and deactivate a test account. Check that its old browser session no longer works.

## Check your work

- [ ] Tests cover good and refused attempts, with DB evidence for duplicates, roles and deactivation.
- [ ] At least one explicit missing-token case fails as expected while protected actions with valid tokens pass.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [pytest fixture how-to with examples](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Flask-WTF CSRF protection for forms and Fetch](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 079, Test signup, sessions, and account roles. Teach me the prerequisite ideas for testing happy paths, role matrices, and security guards. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 079, Test signup, sessions, and account roles, using the acceptance checks I paste below. Check tests prove state changes and refusals independently and would catch a wrongly trusted role or old session. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
